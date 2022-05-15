from concurrent.futures import process
from os.path import exists
import subprocess
import sys
import os
from tokenize import Ignore
from pygments import lex
from plySimple_Yacc import readFile
separator = "/"
directory = ""
if os.name == "nt":
    separator = "\\"


def makefolder(filename, diclex, dicyacc):
    if not os.path.exists(directory):
        os.mkdir(directory)
    makeYacc(filename, dicyacc, diclex)
    makeLex(filename, diclex)


def makeLex(filename, diclexar):
    if not diclexar["empty"]:
        if directory:
            f = open(directory + separator + filename + "_lex.py", "w")
        else:
            f = open(filename + "_lex.py", "w")
        lexar = "import ply.lex as lex\nimport sys" + "\n\n"

        if "Literals" in diclexar.keys():
            lexar += "literals = " + diclexar["Literals"] + "\n"

        if "Tokens" in diclexar.keys():
            lexar += "tokens = " + \
                diclexar["Tokens"].replace("’", "'") + "\n\n"

        if "States" in diclexar.keys():
            lexar += "states = ["
            for keyState in diclexar["States"]:
                lexar += "(" + keyState + "," + \
                    diclexar["States"][keyState].replace("’", "'") + "),"
            lexar = lexar[:-1] + "]\n\n"

        if "Ignore" in diclexar.keys():
            lexar += "t_ignore = " + diclexar["Ignore"] + "\n"
        else:
            lexar += "t_ignore = \"\""

        if "States" in diclexar.keys() and "IgnoreStates" in diclexar.keys():
            for key in diclexar["States"].keys():
                writekey = key.replace("\"", "")
                if key in diclexar["IgnoreStates"].keys():
                    lexar += "t_ignore_" + writekey + " = " + \
                        diclexar["IgnoreStates"][key] + "\n"
                else:
                    lexar += "t_ignore_" + writekey + " = \"\"\n"

        if "Precedence" in diclexar.keys():
            lexar += "precedence = " + \
                diclexar["Precedence"].replace("’", "'") + "\n\n"

        if "Code" in diclexar.keys():
            lexar += diclexar["Code"] + "\n"

        f.write(lexar)


def makeYacc(filename, dicyacc, diclexar):
    if not dicyacc["empty"]:
        if directory:
            f = open(directory + separator + filename + "_yacc.py", "w")
        else:
            f = open(filename + "_yacc.py", "w")
        yacc = "import ply.yacc as yacc\nimport sys\n"
        if not diclexar["empty"]:
            if "Tokens" in diclexar.keys() and "Literals" in diclexar.keys():
                yacc += "from " + filename + "_lex import " + "tokens, literals\n"
            elif "Tokens" in diclexar.keys():
                yacc += "from " + filename + "_lex import " + "tokens\n"
            elif "Literals" in diclexar.keys():
                yacc += "from " + filename + "_lex import " + "literals\n"
        if "Precedence" in dicyacc.keys():
            yacc += "precedence = " + dicyacc["Precedence"].replace("’", "'")
        if "Code" in dicyacc.keys():
            yacc += dicyacc["Code"]

        f.write(yacc)


def interpretador():
    global directory
    print("Please insert the filepath: ", end="")
    file = input()

    while not exists(file):
        print("This file does not exists")
        print("Please insert the filepath: ", end="")
        file = input()

    if not directory:
        print("Would you like to save the files in a folder? [y/n]")
        answer = input()
        if answer.lower() == ("y" or "yes" or "sim" or "s"):
            print("Please insert folder's name:", end="")
            directory = input()

    filename, diclex, dicyacc = readFile(file)
    if directory:
        makefolder(filename, diclex, dicyacc)
    else:
        makeLex(filename, diclex)
        makeYacc(filename, dicyacc, diclex)


def runprocess(filename, testfile):
    catArgs = ["cat", testfile]

    if directory != "":
        file = directory + separator + filename
    else:
        file = filename

    pythonArgs = ["python3", file + "_yacc.py"]
    process1 = subprocess.Popen(catArgs, stdout=subprocess.PIPE)
    subprocess.Popen(pythonArgs, stdin=process1.stdout)


def main():
    global directory

    if len(sys.argv) == 2:
        if exists(sys.argv[1]):

            filename, diclex, dicyacc = readFile(sys.argv[1])
            makeLex(filename, diclex)
            makeYacc(filename, dicyacc, diclex)
        else:
            print("File does not exist!")
            interpretador()

    elif len(sys.argv) == 4:
        if sys.argv[2] == "-f":
            directory = sys.argv[3]
            if exists(sys.argv[1]):
                filename, diclex, dicyacc = readFile(
                    sys.argv[1])
                makefolder(filename, diclex, dicyacc)
            else:
                print(f'File {sys.argv[1]} does not exist!')
                interpretador()

        elif sys.argv[2] == "-t":
            if exists(sys.argv[1]):
                filename, diclex, dicyacc = readFile(
                    sys.argv[1])
                makeLex(filename, diclex)
                makeYacc(filename, dicyacc, diclex)
                runprocess(filename, sys.argv[3])
            else:
                print(f'File {sys.argv[1]} does not exist!')
                interpretador()

        else:
            print("Invalid arguments!")
            interpretador()

    elif len(sys.argv) == 6:
        if sys.argv[2] == "-f":
            directory = sys.argv[3]
            if exists(sys.argv[1]):
                filename, diclex, dicyacc = readFile(
                    sys.argv[1])
                makefolder(filename, diclex, dicyacc)
                if sys.argv[4] == "-t":
                    runprocess(filename, sys.argv[5])
            else:
                print(f'File {sys.argv[1]} does not exist!')
                interpretador()

        elif sys.argv[4] == "-f":
            directory = sys.argv[5]
            if exists(sys.argv[1]):
                filename, diclex, dicyacc = readFile(
                    sys.argv[1])
                makefolder(filename, diclex, dicyacc)
                if sys.argv[2] == "-t":
                    runprocess(filename, sys.argv[3])
            else:
                print(f'File {sys.argv[1]} does not exist!')
                interpretador()

        else:
            print("File does not exist or invalid arguments!")
            interpretador()
    else:
        interpretador()


main()
