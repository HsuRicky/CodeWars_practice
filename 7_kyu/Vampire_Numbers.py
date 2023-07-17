# https://www.codewars.com/kata/54d418bd099d650fa000032d
def vampire_test(x, y):
    return sorted(list(str(x)) + list(str(y))) == sorted(list(str(x*y)))


# print(vampire_test(210,600))