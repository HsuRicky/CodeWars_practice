# https://www.codewars.com/kata/529adbf7533b761c560004e5
fib_cache = {0 : 0, 1 : 1}
def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = result = fibonacci(n-1) + fibonacci(n-2)
    return result
    

# 1 1 2 3 5 8 13 21 34
# print(fibonacci(8))