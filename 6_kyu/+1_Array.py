# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
def up_array(arr):
    if arr == []: return None

    for i in arr:
        if i not in [i for i in range(0,10)]: return None

    res = [int(i) for i in str(int("".join([str(i) for i in arr])) + 1)]
    if len(arr) > len([str(res) for i in res]): res.insert(0, 0)
    return res

# print(up_array([0,2,9]))