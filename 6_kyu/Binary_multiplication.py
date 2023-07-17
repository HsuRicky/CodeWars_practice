# https://www.codewars.com/kata/596a81352240711f3b00006e
def bin_mul(m,n):
    m, n = max(m,n), min(m,n)
    res = []
    if n == 0: return res
    while m > 0:
        if m % 2 == 0:
            m = m / 2
            n = n * 2
        else:
            res.append(n)
            m = m // 2
            n = n * 2 
    return sorted(res, reverse=True)

# print(bin_mul(0,1000))