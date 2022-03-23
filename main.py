from math import ceil, floor, sqrt
import re

#header dictionary
dic_header = {}

#Expression to read file header
headerExpression = re.compile(r'\b(?P<num>[^,]+),'
                              r'(?P<name>[^,]+),'
                              r'(?P<course>[^,]+)'
                              r'(,(?P<grades>\w+)'
                              r'((?P<grades_quant>{\d+}|{\d+,\d+})))?'
                              r'(::(?P<func>\w+(::\w+)*))?,*(\b)?')


#Applies functions in header
def apply_func(func,grades):
    split_grades = grades.split(",")
    sum = 0
    
    for number in split_grades:
        sum += float(number)
        
    if(func == 'sum'):
        return sum
    
    elif(func == 'dp'):
        size = len(split_grades)
        median = sum/size
        dp = 0
        for number in split_grades:
            dp+= pow(float(number)-median,2)
        return sqrt(dp/size)
    elif(func == 'mode'):
        numberOrder = {}
        for number in split_grades:
            if(number in numberOrder.keys()):
                numberOrder[number] += 1;
            else:
                numberOrder[number] = 1;
            
        return max(numberOrder, key=numberOrder.get)
    elif(func == 'median'):
        numbers = []
        for number in split_grades:
            numbers.append(float(number))
        numbers = sorted(numbers)
        size = len(numbers)
        print(size)
        if(size % 2 != 0):
            return numbers[int((size/2)-1)]
        else:
            return (numbers[floor(size/2)-1] + numbers[ceil(size/ 2) - 1]) / 2          
            
    else:
        return sum/len(split_grades)


#Reads first line and gets the necessary information
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
        

#reads given files and makes the info dictionary
def readFile(filepath):
    file = open(filepath, 'r', encoding="utf-8")
    readHeader(file.readline())
    csvExpression = re.compile(r'(?P<num>\d+),'
                            r'(?P<name>[^,]+),'
                            r'(?P<course>[^,\n]+)'
                            r',?((?P<grades>(\d+(.\d+)?,?)'+ (dic_header['grades_quant']) + r'))?,*(\b)?')
    
    dic_info = []
    for linha in file.readlines():
        match = csvExpression.search(linha)
        if(match):
            temp = {}
            temp[dic_header['num']] = match.group('num')
            temp[dic_header['name']] = match.group('name')
            temp[dic_header['course']] = match.group('course')
            
            if('grades' in dic_header.keys() and ('func' not in dic_header.keys())):
                temp[dic_header['grades']] = '[' + match.group('grades') + ']'
            elif 'func' in dic_header.keys():
                func_split = dic_header['func'].split("::");
                for func in func_split:
                    func_key = dic_header['grades'] + "_" + func
                    temp[func_key] = apply_func(func,match.group('grades'))
                
            dic_info.append(temp)
            
    return(dic_info)


