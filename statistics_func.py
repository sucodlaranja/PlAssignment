import statistics


# applies given function in grades
def apply_func(func, numbers):
    func_lower = func.lower()
    result = 0

    if func_lower == 'sum':
        result = round(sum(numbers), 1)
    elif func_lower == 'dp':
        result = round(statistics.stdev(numbers))
    elif func_lower == 'mode':
        result = round(statistics.mode(numbers))
    elif func_lower == 'median':
        result = round(statistics.median(numbers))
    elif func_lower == 'max':
        result = max(numbers)
    elif func_lower == 'min':
        result = min(numbers)
    elif func_lower == 'mean':
        result = round(statistics.mean(numbers))
    elif func_lower == 'grades':
        result = numbers
    return result
