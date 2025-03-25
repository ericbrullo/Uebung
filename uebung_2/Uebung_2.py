class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f"{(a._x), (a._y), (a._z)}"
    
    def __add__(self, other):
        return a._x + b._x , a._y + b._y , a._z + b._z 
    
    def __sub__(self, other):
        return a._x - b._x , a._y - b._y , a._z - b._z
    
    def __mul__(self, other):
        return a._x * b._x , a._y * b._y , a._z * b._z

    def __mulskal__(self, other):
        return a._x * other , a._y * other , a._z * other 
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __cross__(self, other):
        return [(a._y*b._z) - (a._z*b._y)] , [(a._x * b._z) - (a._z * b._x)], [(a._x * b._y) - (a._y * b._x)]

    def __dot__(self, other):
        return (a._x*b._x) + (a._y*b._y) + (a._z*b._z)

    def __norm__(self):
        return self._x**2 + self._y**2 + self._z**2

a = Vector3(3,4,2)
b = Vector3(2,1,0)

c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

f = a.__mulskal__(4) 
print(f)

g = a.__cross__(b)
print(g)

h = a.__dot__(b)
print(h)

i = a.__norm__()
print(i)
