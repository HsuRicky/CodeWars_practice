# https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    eng = list("abcdefghijklmnopqrstuvwxyz")
    number = list(range(1,27))
    dic = dict(zip(eng, number))
    return " ".join([str(dic[e]) for e in text.lower() if e in dic])