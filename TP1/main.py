import os
import re

from TP1.csvToDic import readFile
from TP1.dicToJSON import create_json


# Main interface of the program.
def main():
    filename = ""

    # Do not allow program to end until asked.
    while filename.lower() != "q" and filename.lower() != quit:
        print("Insert the filename of your csv (Type 'quit' or 'q' to exit):")
        filename = input()
        # Do not continue until file is correct.
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
