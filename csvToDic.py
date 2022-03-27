import re

from statistics_func import apply_func

# Expression to read file header
headerExpression = re.compile(r'\b(?P<num>[^,]+),'
                              r'(?P<name>[^,]+),'
                              r'(?P<course>[^,|\n]+)'
                              r'(,(?P<grades>\w+)'
                              r'((?P<grades_quant>{\d+}|{\d+,\d+})))?'
                              r'(::(?P<func>\w+(::\w+)*))?,*(\b)?')


# Reads the header and insters int a dictionary all necessary info
def readHeader(linha):
    # header dictionary
    dic_header = {}
    match = headerExpression.search(linha)
    if (match):
        dic_header['num'] = match.group('num')
        dic_header['name'] = match.group('name')
        dic_header['course'] = match.group('course')

        if (match.group('grades')):
            dic_header['grades'] = match.group('grades')
            dic_header['grades_quant'] = match.group('grades_quant')
            if (match.group('func')):
                dic_header['func'] = match.group('func')

        else:
            dic_header['grades_quant'] = '{0}'
    return dic_header


# reads given files and makes the info dictionary
def readFile(filepath):
    file = open(filepath, 'r', encoding="utf-8")
    dic_header = readHeader(file.readline())
    csvExpression = re.compile(r'(?P<num>\d+),'
                               r'(?P<name>[^,]+),'
                               r'(?P<course>[^,\n]+)'
                               r',?((?P<grades>(\d+(.\d+)?,?)' + (dic_header['grades_quant']) + r'))?,*(\b)?')

    dic_info = []
    for linha in file.readlines():
        match = csvExpression.search(linha)
        if (match):
            temp = {}
            temp[dic_header['num']] = match.group('num')
            temp[dic_header['name']] = match.group('name')
            temp[dic_header['course']] = match.group('course')

            if 'grades' in dic_header.keys():

                numbers = []
                for number in match.group('grades').split(','):
                    if number:
                        numbers.append(float(number))

                if 'func' not in dic_header.keys():
                    temp[dic_header['grades']] = numbers
                else:
                    func_split = dic_header['func'].split("::")
                    for func in func_split:
                        func_key = dic_header['grades'] + "_" + func
                        temp[func_key] = apply_func(func, numbers)

            dic_info.append(temp)
    return (dic_info)
