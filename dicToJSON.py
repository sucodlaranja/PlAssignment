import os
import re

from main import readFile


def main():
    filename = ""

    while filename.lower() != "q" and filename.lower() != quit:
        print("Insert the filename of your csv (Type 'quit' or 'q' to exit):")
        filename = input()
        while os.path.exists(filename) and not re.match(r'\w+\.csv', filename)  \
                and filename.lower() != "q" and filename.lower() != "quit":
            print("File does not exist, please insert correct path (Type 'quit' or 'q' to exit):")
            filename = input()

        if filename.lower() != "q" and filename.lower() != "quit":
            print("Reading " + filename + "!")
            l = readFile(filename)
            print("File read, generating JSON!")
            create_json(filename, l)
            print("JSON generated!")


def create_json(filename, list_of_dic):
    filename_json = re.sub(r'(\w+).\w+', r'\1.json', filename)
    print(list_of_dic)

    json_text = "[\n"
    for dic in list_of_dic:
        json_text += "    {\n"
        cc = 0
        for key in dic.keys():
            json_text += "      \"" + key + "\""
            if cc >= 3:
                json_text += ": " + str(dic[key]) + ",\n"
            else:
                json_text += ": \"" + dic[key] + "\",\n"
            cc += 1
        json_text = json_text[:-2] + "\n"
        json_text += "    },\n"
    json_text = json_text[:-2] + "\n]"

    json_file = open(filename_json, "w", encoding="utf-8")
    json_file.write(json_text)
    json_file.close()


main()
