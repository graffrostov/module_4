from math import inf

def true_divide(first, second):
    if second == 0 and first >= 0:
        result = inf
    elif second == 0 and first < 0:
        result = -inf
    else:
        result = first / second
    return result