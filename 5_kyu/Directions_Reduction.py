# https://www.codewars.com/kata/550f22f4d758534c1100025a
def dirReduc(arr:list):
    dic = {"NORTH": "SOUTH",
           "SOUTH": "NORTH",
           "EAST": "WEST",
           "WEST": "EAST"}
    
    res = []
    for i in range(len(arr)):
        if res and dic[arr[i]] == res[-1]: res.pop()
        else: res.append(arr[i])
    return res

# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# u = ["NORTH", "WEST", "SOUTH", "EAST"]
# print(dirReduc(a))


