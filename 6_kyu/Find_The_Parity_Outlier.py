# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    sor = sorted(integers, key=lambda x:(x%2 == 0, x%2 != 0))
    if sor[0] % 2 != sor[1] % 2:
        return sor[0]
    else:
        return sor[-1]