# https://www.codewars.com/kata/5b0737c724c0686bf8000172
def create_report(names):
    result = {}
    
    for name in names:
        if name.startswith("Labrador Duck"):
            return ["Disqualified data"]
        
        name = name.upper().replace("-", " ").split()
        count = int(name.pop())
        
        if   len(name) == 1:  code = name[0][:6]
        elif len(name) == 2:  code = name[0][:3] + name[1][:3]
        elif len(name) == 3:  code = name[0][:2] + name[1][:2] + name[2][:2]
        elif len(name) == 4:  code = name[0][0] + name[1][0] + name[2][:2] + name[3][:2]
        
        if code in result:    result[code] += count
        else:                 result[code] = count
    
    return sum([[name, result[name]] for name in sorted(result)] , [])




'''
# some error, must to improved
from collections import Counter
def create_report(names):
    names = [i.upper().split() for i in names]
    for name in names:
        temp = name[:-1]
        if len(temp) == 1:
            try:
                name[0] = name[0][:6]
            except:
                pass
        elif len(temp) == 2:
            name[0] = name[0][:3]
            name[1] = name[1][:3]
        elif len(temp) == 3:
            name[0] = name[0][:2]
            name[1] = name[1][:2]
            name[2] = name[2][:2]
        elif len(temp) == 4:
            name[0] = name[0][0]
            name[1] = name[1][0]
            name[2] = name[2][0]
            name[3] = name[3][:2]

    trans = [{"".join(i[:-1]): int(i[-1])} for i in names]
    
    c = Counter()
    for i in trans: 
        c.update(i)

    res = []
    for n, c in sorted(c.items()):
        res.append(n)
        res.append(c)

    return res
'''
# names = ["Redhead 3", "Gadwall 1", "Smew 4", "Greater Scaup 10", "Redhead 3", "Gadwall 9", "Greater Scaup 15", "Common Eider 6"]
# print(create_report(names))