#Create a new class called Bike with the following properties/attributes:
#price, max_speed, miles
#Create 3 instances of the Bike class.

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price 
        print "Max speed", self.max_speed 
        print "Ridden", self.miles, "miles"
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self
bike1 = Bike("$400", "50mph")
bike2= Bike("$200", "30mph")
Trek = Bike("$100", "15mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
Trek.reverse().reverse().reverse().displayInfo()