# https://www.codewars.com/kata/562c04fc8546d8147b000039
# Execution Timed Out!!!
def sum_of_sums(n):
    def S(n):
        return int(n * (n + 1) / 2)

    def Z(n):
        res = 0
        for i in range(1, n+1):
            res += S(i)
        return res

    return S(Z(n))

# print(sum_of_sums(3))
