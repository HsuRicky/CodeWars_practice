# https://www.codewars.com/kata/54d512e62a5e54c96200019e
def prime_factors(n):
    from itertools import accumulate
    from collections import Counter

    res = []
    temp = n
    i = 2
    while temp / i != 1:
        if temp % i == 0:
            res.append(i)
            temp = temp / i
        else: i += 1
    
    if n == i: res.append(n)
    else: res.append(int(n / list(accumulate(res, func= lambda x,y: x*y))[-1]))

    return "".join(["(" + str(e[0]) + "**" + str(e[1]) + ")" if e[1] != 1 else "("+ str(e[0]) + ")" for e in list(Counter(res).items())])