#Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

class Car(object):    
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > "$10000":
            self.tax = 15
        else:
            self.tax = 12
        self.display_all()
    def display_all(self):
        print "Price:", self.price
        print "Speed: {}mph".format(self.speed)
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print  "Tax: {}%".format(self.tax)
        return self
        
# print " Price: {}\n Speed:{}\n Fuel:{}\n Mileage:{}\n Tax:{}%\n".format(self.price,self.speed,self.fuel,self.mileage,self.tax)
Toyota = Car("$22000",35,"Full","15mpg")
Nissan = Car("$23000",5,"Not Full","105mpg")
Mercedes = Car("$40000",25," Full","25mpg")
Ferari = Car("$200000",35,"Empty","15mpg")

# Toyota.display_all()
# Nissan.display_all()
# Mercedes.display_all()
# Ferari.display_all()