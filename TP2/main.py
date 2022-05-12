from os.path import exists
import sys
import os
from tokenize import Ignore

from pygments import lex
from projV2_sin import readFile
separator = "/"
directory = ""
if os.name == "nt":
    separator = "\\"


def makefolder(filename, diclex, dicyacc):
    if(not os.path.exists(directory)):
        os.mkdir(directory)
    makeYacc(filename, dicyacc)
    makeLex(filename, diclex)


def makeLex(filename, diclexar):
    if directory:
        f = open(directory + separator + filename + "_lex.py", "w")
    else:
        f = open(filename + "_lex.py", "w")
    lexar = "import ply.lex as lex" + "\n\n"
    if "Literals" in diclexar.keys():
        lexar += "literals = " + diclexar["Literals"] + "\n"
    if "Tokens" in diclexar.keys():
        lexar += "tokens = " + diclexar["Tokens"].replace("’", "'") + "\n\n"
    if "States" in diclexar.keys():
        lexar += "states = ["
        for keyState in diclexar["States"]:
            lexar += "(" + keyState + "," + \
                diclexar["States"][keyState].replace("’", "'") + "),"
        lexar = lexar[:-1] + "]\n\n"
    if "Precedence" in diclexar.keys():
        lexar += "precedence = " + \
            diclexar["Precedence"].replace("’", "'") + "\n\n"
    if "Code" in diclexar.keys():
        lexar += diclexar["Code"] + "\n"
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
        lexar += "\nlexer = lex.lex()"
        f.write(lexar)


def makeYacc(filename, dicyacc):
    if dicyacc:
        if directory:
            f = open(directory + separator + filename + "_yacc.py", "w")
        else:
            f = open(filename + "_yacc.py", "w")
        yacc = "import ply.yacc as yacc\nimport sys\n"
        yacc += "from " + filename + "_lex import " + "tokens, literals\n"
        if "Precedence" in dicyacc.keys():
            yacc += "precedence = " + dicyacc["Precedence"].replace("’", "'")
        if "Code" in dicyacc.keys():
            yacc += dicyacc["Code"]

        yacc += "\nparser = yacc.yacc()\n"
        yacc += """
for linha in sys.stdin:
    parser.success = True
    parser.total = 0
    parser.parse(linha)
    if parser.success:
        print("Frase válida!")
    else:
        print("Frase inválida... Corrija e tente novamente!")"""
        f.write(yacc)


def interpretador():
    global directory
    print("Please insert the filepath: ", end="")
    file = input()

    while(not exists(file)):
        print("This file does not exists")
        print("Please insert the filepath: ", end="")
        file = input()

    if(not directory):
        print("Would you like to save the files in a folder? [y/n]")
        answer = input()
        if answer.lower() == ("y" or "yes" or "sim" or "s"):
            print("Please insert folder's name:", end="")
            directory = input()

    filename, diclex, dicyacc = readFile(file)
    if(directory):
        makefolder(filename, diclex, dicyacc)
    else:
        makeLex(filename, diclex)
        makeYacc(filename, dicyacc)


def main():
    global directory

    if len(sys.argv) == 2:
        if(exists(sys.argv[1])):
            print(sys.argv[1])
            filename, diclex, dicyacc = readFile(sys.argv[1])
            makeLex(filename, diclex)
            makeYacc(filename, dicyacc)
        else:
            print("File does not exist!")
            interpretador()

    elif len(sys.argv) == 3:
        directory = sys.argv[2]
        if(exists(sys.argv[1])):
            filename, diclex, dicyacc = readFile(sys.argv[1])
            makefolder(filename, diclex, dicyacc)
        else:
            print("File does not exist!")
            interpretador()
    else:
        interpretador()


main()
