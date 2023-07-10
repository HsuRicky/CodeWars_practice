# https://www.codewars.com/kata/562c04fc8546d8147b000039
def sum_of_sums(n):
    def S(m):
        return int(m * (m + 1) / 2)

    def Z(n):
        res = 0
        for _ in range(1, n+1):
            res += S(n)
            print(n)
        return res

    return Z(n)

print(sum_of_sums(3))