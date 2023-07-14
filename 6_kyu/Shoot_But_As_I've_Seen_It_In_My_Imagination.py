# https://www.codewars.com/kata/5b8ea6bbcc7c0335f80001a9
# Execution Timed Out -> must to improved
from collections import Counter
from math import factorial, gcd
def find_prob(balls_set, event):
    trans = {'Aluminum': 'AL', 'Amber': 'AM', 'Beige': 'BG', 'Black': 'BK', 
             'Blue': 'BL', 'Brown': 'BN', 'Bronze': 'BZ', 'Charcoal': 'CH', 
             'Clear': 'CL', 'Gold': 'GD', 'Green': 'GN', 'Gray': 'GY', 'GraniteIV': 'GT',
             'Granite': 'GT', 'Light': 'LT', 'Olive': 'OL', 'Opaque': 'OP', 'Orange': 'OR', 
             'Pink': 'PK', 'Red': 'RD', 'Smoke': 'SM', 'Translucent': 'TL', 'Tan': 
             'TN', 'Transparent': 'TP', 'Violet': 'VT', 'Ivory': 'IV', 
             'White': 'WT', 'Yellow': 'YL'}
    balls_set = [trans[i] for i in balls_set]

    c_b = dict(Counter(balls_set))
    c_e = dict(Counter(event))
    
    for e in c_e:
        if e not in c_b:
            return ['Impossible']
        
        if c_e[e] > c_b[e]:
            return ['Impossible'] 

    up, down = 1, 1
    for e in c_e:
        up *= factorial(c_b[e])
        down *= factorial(c_b[e] - c_e[e])
    up = up * factorial(sum(c_b.values()) - sum(c_e.values()))
    down = down * factorial(sum(c_b.values()))

    g = gcd(up, down)
    return [up // g, down // g]


    


balls1 = ["Red","Red","Blue","Yellow","Yellow","Yellow","Red", "Yellow","Yellow","Blue","Yellow","Red","Blue","Yellow","Blue","Yellow","Blue","Yellow"]
e1 =["RD", "YL", "YL", "BL"]
print(find_prob(balls1, e1))