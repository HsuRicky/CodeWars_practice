# https://www.codewars.com/kata/5262119038c0985a5b00029f
def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True