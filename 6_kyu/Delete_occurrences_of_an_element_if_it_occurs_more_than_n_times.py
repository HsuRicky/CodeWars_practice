# https://www.codewars.com/kata/554ca54ffa7d91b236000023
def delete_nth(order,max_e):
    # code here
    from collections import Counter
    
    count = Counter(order)
    order.reverse()
    for e,c in count.items():
        while c > max_e:
            order.remove(e)
            c -= 1
    order.reverse()    
    return  order