from os.path import exists
import sys
import os

separator = "/"
directory = ""
if os.name == "nt":
    separator = "\\"


def makefolder():
    os.mkdir(directory, 0o666)
    makeYacc()
    makeLex()


def makeYacc():
    print("YACCC")
    #TODO: FAZER


def makeLex():
    print("LEXXX")
    #TODO: FAZER


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

    if(directory):
        makefolder()
    else:
        makeLex()
        makeYacc()


def main():
    global directory

    if len(sys.argv) == 2:
        if(exists(sys.argv[1])):
            print(sys.argv[1])
        else:
            print("File does not exist!")
            interpretador()

    elif len(sys.argv) == 3:
        directory = sys.argv[2]
        if(exists(sys.argv[1])):
            makefolder()
        else:
            print("File does not exist!")
            interpretador()

    elif sys.stdin:
        print("hello")
        # TODO: #1 Mandar como nas aulas
    else:
        interpretador()


main()
