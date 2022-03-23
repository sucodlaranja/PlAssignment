from math import sqrt,pow
import statistics


#applies given function in grades
def apply_func(func,grades):
    func_lower = func.lower()
    split_grades = grades.split(",")
    result = 0
    numbers = []
    for number in split_grades:
        numbers.append(float(number))
        
    if(func_lower == 'sum'):
        result = sum(numbers) 
    elif(func_lower == 'dp'):
        result = statistics.stdev(numbers)
    elif(func_lower == 'mode'):
        result = statistics.mode(numbers)
    elif(func_lower == 'median'):
        result = statistics.median(numbers)
    elif(func_lower == 'max'):
        result = max(numbers)
    elif(func_lower == 'min'):
        result = min(numbers)
    elif(func_lower == 'mean'):
        result = statistics.mean(numbers)
    return result
