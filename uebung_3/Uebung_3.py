import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"

class Figur:
    def __init__(self):
        self.name = "Figur"
    
    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name

class Dreieck(Figur):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.name = "Dreieck"
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def Umfang(self):
        a = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        b = math.sqrt((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)
        c = math.sqrt((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)
        return a + b + c
    
    def __str__(self):
        return f"{self.name} {self.p1}-{self.p2}-{self.p3}"

class Rechteck(Figur):
    def __init__(self, p1, p2):
        super().__init__()
        self.name = "Rechteck"
        self.p1 = p1  
        self.p2 = p2  
    
    def Umfang(self):
        breite = abs(self.p2.x - self.p1.x)
        hoehe = abs(self.p2.y - self.p1.y)
        return 2 * (breite + hoehe)
    
    def __str__(self):
        return f"{self.name} {self.p1}-{self.p2}"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__()
        self.name = "Kreis"
        self.mittelpunkt = mittelpunkt
        self.radius = radius
    
    def Umfang(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"{self.name} M={self.mittelpunkt} r={self.radius}"

class Polygon(Figur):
    def __init__(self, *punkte):
        super().__init__()
        self.name = "Polygon"
        self.punkte = list(punkte)  
    
    def Umfang(self):
        if len(self.punkte) < 2:
            return 0
        umfang = 0
        for i in range(len(self.punkte) - 1):
            p1 = self.punkte[i]
            p2 = self.punkte[i + 1]
            umfang += math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        p1 = self.punkte[-1]
        p2 = self.punkte[0]
        umfang += math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        return umfang
    
    def __str__(self):
        punkte_str = "-".join(str(p) for p in self.punkte)
        return f"{self.name} {punkte_str}"

if __name__ == "__main__":
    p1 = Punkt(0, 0)
    p2 = Punkt(3, 0)
    p3 = Punkt(0, 4)
    p4 = Punkt(10, 15)
    m = Punkt(2.3, 4.2)
    
    dreieck = Dreieck(p1, p2, p3)
    rechteck = Rechteck(p1, p4)
    kreis = Kreis(m, 3.4)
    polygon = Polygon(p1, p2, p3, p1)
    
    print(dreieck)
    print(f"Umfang: {dreieck.Umfang()}")
    print(rechteck)
    print(f"Umfang: {rechteck.Umfang()}")
    print(kreis)
    print(f"Umfang: {kreis.Umfang()}")
    print(polygon)
    print(f"Umfang: {polygon.Umfang()}")