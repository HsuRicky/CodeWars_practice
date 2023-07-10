# https://www.codewars.com/kata/57b06f90e298a7b53d000a86
def queue_time(customers, n):
    total = [0] * n
    for i in customers:
        total[0] += i
        total.sort()
    return max(total) 