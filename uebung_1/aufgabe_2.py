class wgs84coord:
    def __init__ (self):
        self.longitude = 0.0
        self.latitude = 0.0 

def get_longitude(self):
    return(self.longitude)

def get_latitude(self):
    return(self.latitude)

def set_longitude(self, lat):
    if lat in range (-180, 180):
        self.longitude = lat
    else:
        print ('non valido')

def set_latitude(self, lat):
    if lat in range (-90, 90):
        self.latitude = lat
    else:
        print ('non valido')

koord = wgs84coord()
print(koord.get_latitude())
print(koord.get_longitude())

koord.set_longitude(45)
koord.set_latitude(45)
print(koord.get_latitude())
print(koord.get_longitude())
        