import re

def create_json(filename, list_of_dic):
    filename_json = re.sub(r'([\w \\/]+).\w+', r'\1.json', filename)
    

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
