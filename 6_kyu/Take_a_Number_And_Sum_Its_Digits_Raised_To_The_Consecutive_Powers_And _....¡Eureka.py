# https://www.codewars.com/kata/5626b561280a42ecc50000d1
def sum_dig_pow(a, b): 
    res = []
    for i in range(a, b + 1):
        total = 0
        for n, e in enumerate(str(i)):
            total += int(e)**(n + 1)
            if total == i:
                res.append(i)
    return res