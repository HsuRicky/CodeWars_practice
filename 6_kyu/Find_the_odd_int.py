# https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    from collections import Counter
    c = Counter(seq)
    return [item for item, count in c.items() if count % 2 != 0][0]