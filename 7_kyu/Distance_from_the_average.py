# https://www.codewars.com/kata/568ff914fc7a40a18500005c
def distances_from_average(test_list:list):
    ave = round(sum(test_list) / len(test_list), 2)
    return [round(ave- e, 2) for e in test_list]


# print(distances_from_average([55, 95, 62, 36, 48]))