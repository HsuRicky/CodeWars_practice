# https://www.codewars.com/kata/55c6126177c9441a570000cc
def order_weight(strng):
    lst = strng.split(" ")
    return " ".join(sorted(sorted(lst), key=lambda x: (sum(int(i) for i in x))))