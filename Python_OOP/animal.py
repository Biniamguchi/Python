class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.health
        return self

Lion = Animal("King",100)
Lion.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self,name,heal):
        super(Dog,self).__init__(name,heal)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog = Dog("Marley",0)
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self,name,heal):
        super(Dragon,self).__init__(name,heal)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon,self).displayHealth()
        print "I am a dragon"

dragon = Dragon("don",0)
dragon.run().run().fly().fly().displayHealth()

animal2 = Animal("anim2",120)
# animal2.pet().fly() - AttributeError: 'Animal' object has no attribute 'pet'
#                     - AttributeError: 'Animal' object has no attribute 'fly'
# dog.fly() - AttributeError: 'Dog' object has no attribute 'fly'