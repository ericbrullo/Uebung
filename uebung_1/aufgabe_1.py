class vektor_3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)

v1 = vektor_3 (3, 4, 6)

print(v1.len())




