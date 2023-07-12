# https://www.codewars.com/kata/55f2afa960aeea545a000049
from collections import Counter
def variance(words:str):
    lst = [len(word) for word in words]
    plst = [(key, value/sum(Counter(lst).values())) for key, value in Counter(lst).items()]
    
    round(sum([(l ** 2) * p for l,p in plst]) - sum([l * p for l,p in plst]) ** 2, 4)

# print(variance("Hello world".split()))