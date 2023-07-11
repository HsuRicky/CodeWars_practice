# https://www.codewars.com/kata/55b3425df71c1201a800009c
def stat(strg):
    # test for empty
    if strg == '': return strg
    
    # convert to seconds
    t = sorted(h*3600 + m*60 + s for h, m, s in (map(int, r.split('|')) for r in strg.split(', ')))    
    l = len(t)
    
    # calculate
    r = t[-1] - t[0] # range
    a = sum(t) // l  # average
    m = t[l//2] if l&1 else sum(t[l//2-1: l//2+1])//2 # median
    
    # convert to string
    lst = tuple('%02d|%02d|%02d' % (i//3600, (i%3600)//60, i%60) for i in (r, a, m))
    return "Range: %s Average: %s Median: %s" % lst


# some error, must to improved
'''
def stat(strg:str):
    if strg == "":
        return ""
    
    strg_list = strg.replace(" ","").replace("|",".").split(",")
    trans = [(int(j[0])*60 + int(j[1]))*60 + int(j[2]) for j in [i.split('.') for i in strg_list]]
    tup = dict((zip(strg_list, trans)))

    def ran():
        ran = tup[max(strg_list)] - tup[min(strg_list)]
        hour = ran // 3600 
        minu = (ran % 3600) // 60
        sec = (ran % 3600) % 60
        return f"{'%02d' % hour}|{'%02d' % minu}|{'%02d' % sec}"

    def ave():
        ave = sum(trans) / len(strg_list)
        hour = ave // 3600 
        minu = (ave % 3600) // 60
        sec = (ave % 3600) % 60
        return f"{'%02d' % hour}|{'%02d' % minu}|{'%02d' % sec}" 

    def median():
        if len(strg_list) % 2 != 0: 
            medi = sorted(strg_list)[len(strg_list)//2].split(".")
            return f"{'%02d' % int(medi[0])}|{'%02d' % int(medi[1])}|{'%02d' % int(medi[2])}"
        else: 
            medi = (tup[strg_list[len(strg_list)//2]] + tup[strg_list[len(strg_list)//2 - 1]]) / 2
            hour = medi // 3600 
            minu = (medi % 3600) // 60
            sec = (medi % 3600) % 60
            return f"{'%02d' % hour}|{'%02d' % minu}|{'%02d' % sec}"

    return f"Range: {ran()} Average: {ave()} Median: {median()}"
    '''


# print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
# print(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"))