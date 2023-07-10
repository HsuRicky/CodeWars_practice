# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    # your code here
    res = []
    temp = []
    args += [-99999999]
    for i, num in enumerate(args[1:]):
        temp.append(args[i])
        if args[i + 1] - args[i] != 1:
            res.append(temp)
            temp = []
    res.append(temp)
    
    result = [] 
    for x in res:
        if len(x) >= 3:
            result.append(str(x[0]) + '-' + str(x[-1]))
        else:
            result.append(','.join([str(num) for num in x]))
    return ','.join(result).strip(',')