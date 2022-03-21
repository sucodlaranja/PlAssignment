import re
import sys

headerExpression = re.compile(r'\b(?P<num>[^,]+),'
                              r'(?P<name>[^,]+),'
                              r'(?P<course>[^,]+)'
                              r'(,(?P<grades>\w+)'
                              r'((?P<grades_quant>{\d+}|{\d+,\d+})))?'
                              r'(::((?P<func>\w+)))?')

def apply_func(grades):
    split_grades = grades.split(",")
    
    sum = 0
    for number in split_grades:
        sum += float(number)
    if(dic_header['func'] == 'sum'):
        return sum
    else:
        return sum/len(split_grades)

#Reads first line and gets the necessary information
dic_header = {}
def readHeader(linha):
    match = headerExpression.search(linha)
    if(match):
        dic_header['num'] = match.group('num')
        dic_header['name'] = match.group('name')
        dic_header['course'] = match.group('course')
        if(match.group('grades')):
            dic_header['grades'] = match.group('grades')
            dic_header['grades_quant'] = match.group('grades_quant')
            if(match.group('func')):
                dic_header['func'] = match.group('func')
        else:
            dic_header['grades_quant'] = '{0}'
        


readHeader(sys.stdin.readline())
csvExpression = re.compile(r'(?P<num>\d+),'
                           r'(?P<name>[^,]+),'
                           r'(?P<course>[^,]+)'
                           r',?((?P<grades>(\d+,?)'+ (dic_header['grades_quant']) + r'))?')

dic_info = []
for linha in sys.stdin:
    match = csvExpression.search(linha)
    if(match):
        temp = {}
        temp[dic_header['num']] = match.group('num')
        temp[dic_header['name']] = match.group('name')
        temp[dic_header['course']] = match.group('course')
        if('grades' in dic_header.keys() and ('func' not in dic_header.keys())):
            temp[dic_header['grades']] = '[' + match.group('grades') + ']'
        elif 'func' in dic_header.keys():
            func_key = dic_header['grades'] + "_" + dic_header['func']
            temp[func_key] = apply_func(match.group('grades'))
        dic_info.append(temp)



    

        