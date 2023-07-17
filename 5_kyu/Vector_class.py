# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
class Vector:
    def __init__(self, lst:list):
        self.lst = lst

    def __str__(self):
        return f'({",".join(map(str, self.lst))})'

    def length(self):
        return len(self.lst)
    
    def check(self, l):
        if len(self.lst) != l.length(): 
            raise ValueError('Vectors must have same length.')
    def add(self, l):
        self.check(l)
        return Vector([x+y for x,y in zip(self.lst, l.lst)])
    
    def subtract(self, l):
        self.check(l)
        return Vector([x-y for x,y in zip(self.lst, l.lst)])
    
    def dot(self, l):
        self.check(l)
        return sum([x*y for x,y in zip(self.lst, l.lst)])
    
    def norm(self):
        return sum([x**2 for x in self.lst]) ** 0.5

    def equals(self, l):
        return self.lst == l.lst


# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5, 6])

# print(a)
# print(a.__str__())
# print(a.add(b))
# print(a.dot(b))