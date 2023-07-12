# https://www.codewars.com/kata/5ba0adafd6b09fd23c000255
# some error, must to improved
def run(tricks:list):
    res = {}
    for i in range(len(tricks)):
        n, p, pt, m = tricks[i]['name'], tricks[i]['probability'], tricks[i]['points'], tricks[i]['mult_base']

        first, count = 0, 1
        while True:
            next = (p ** count) * (sum([pt * (m ** i) for i in range(count + 1)]))

            if next > first:
                first = next
                count += 1
            else:
                res[n] = count
                break
    
    return res
    


# print(run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .85 }]))    