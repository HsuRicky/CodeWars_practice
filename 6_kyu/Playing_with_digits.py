# https://www.codewars.com/kata/5552101f47fc5178b1000050
def dig_pow(n, p):
    # your code
    total = 0
    for i in str(n):
        total += int(i)**p
        p += 1
    return total / n if total % n == 0 else -1