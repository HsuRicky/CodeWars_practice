# https://www.codewars.com/kata/646254375cee7a000ffaa404
def verify_latin_square(array, m):
    n = len(array)

    if any(len(row) != n for row in array):
        return "Array not square"

    if n != m:
        return "Array is wrong size"

    for row in range(n):
        values = set()
        for col in range(n):
            value = array[row][col]
            if value < 1 or value > m:
                return f"{value} at {row+1},{col+1} is not between 1 and {m}"
            if value in values:
                return f"{value} occurs more than once in row {row+1}"
            values.add(value)

    for col in range(n):
        values = set()
        for row in range(n):
            value = array[row][col]
            if value in values:
                return f"{value} occurs more than once in column {col+1}"
            values.add(value)

    return f"Valid latin square of size {m}"

'''
# Execution Timed Out!!!
from collections import Counter
def verify_latin_square(array, m):
    for i in range(len(array)):
        if len(array[i]) != len(array):
            return "Array not square"
        if len(array[i]) != m or len(array) != m:
            return "Array is wrong size"
        
        
        for e,c in Counter(array[i]).items():
            if c > 1:
                return  f"{e} occurs more than once in row {i + 1}"
            
            if e not in list(range(1, m + 1)):
                return f"{e} at {i + 1},{array[i].index(e) + 1} is not between 1 and {m}"
            

    trans = list(map(list, zip(*array)))
    for i in range(len(trans)):        
        for e,c in Counter(trans[i]).items():
            if c > 1:
                return  f"{e} occurs more than once in column {i + 1}"
        
    return  f"Valid latin square of size {m}"
'''

# print(verify_latin_square([[1, 3, 2], [3, 2, 1], [3, 1, 2]], 3))