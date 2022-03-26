import os
import re

from csvToDic import readFile
from dicToJSON import create_json


def main():
    filename = ""

    while filename.lower() != "q" and filename.lower() != quit:
        print("Insert the filename of your csv (Type 'quit' or 'q' to exit):")
        filename = input()
        print(os.path.exists("Input/Exemplo Sem Notas.csv"))
        while not os.path.exists(filename) or not re.match(r'^[\w \\/]+\.csv$', filename):
            if filename.lower() == "q" or filename.lower() == "quit":
                break
            print("File does not exist, please insert correct path (Type 'quit' or 'q' to exit):")
            filename = input()
        

        if filename.lower() != "q" and filename.lower() != "quit":
            print("Reading " + filename + "!")
            l = readFile(filename)
            print("File read, generating JSON!")
            create_json(filename, l)
            print("JSON generated!")



main()
