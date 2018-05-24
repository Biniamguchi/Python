class Product(object):
    
    def __init__(self, item, price, weight, brand, cost):
        self.item = item
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def Sell(self):
        self.status = "sold"
        return self.status
    
    def addTax(self, tax):
        self.price *= tax
        return self.price

    def returnItem(self, reason):
        if reason.find('defect' or 'broke' or 'malfunction' or 'not work') > -1:
            self.status = "defective"
            self.price = 0
        if reason.find('new' or 'unopen' or 'with box' or 'not open') > -1:
            self.status = "for sale"
        if reason.find('opened' or 'used') > -1:
            self.status = "used"
            self.price *= 0.20
        return self.status, self.price

    def displayInfo(self):
        print "Item Name:", self.item
        print "Price: ${}".format(self.price)
        print "Weight:", self.weight, "lbs."
        print "Brand:", self.brand
        print "Cost: ${}".format(self.cost)
        print "Status:", self.status
        return self


class Store(object):

    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        product_info = [
            product.item,
            product.price,
            product.weight,
            product.brand,
            product.cost,
            product.status
            ]
        self.products.append(product_info)
        print product.item, "added to inventory."
        print "---"

    def remove_product(self, product):
        self.products.remove([
            product.item,
            product.price,
            product.weight,
            product.brand,
            product.cost,
            product.status
        ])
        print product.item, "removed from inventory."
        print "---"

    def inventory(self):
        for product in self.products:
            print "Item Name:", product[0]
            print "Price: ${}".format(product[1])
            print "Weight:", product[2], "lbs."
            print "Brand:", product[3]
            print "Cost: ${}".format(product[4])
            print "Status:", product[5]
            print "---"

# Initializing objects
product1 = Product("Baseball", 5, 3, "Wilson", 1)
product2 = Product("Bat", 25, 6, "MLB", 10)
store1 = Store("Fairfax","Bill")

# Adding products
store1.add_product(product1)
store1.add_product(product2)

# Check inventory
store1.inventory()

# Removing product
store1.remove_product(product1)

# Check inventory
store1.inventory()



#Another solution(Morrantho)

# class Product(object):
#     def __init__(self,price,name,weight,brand,cost):
#         self.price  = price
#         self.name   = name
#         self.weight = weight
#         self.brand  = brand
#         self.cost   = cost
#         self.status = "For Sale"
#     def sell(self):
#         self.status = "Sold"
#         return self
#     def addTax(self,tax):
#         return self.cost+tax
#     def Return(self,reason):
#         if type(reason) != str:return
#         reason = reason.lower()

#         if reason == "defective":
#             self.status = reason
#             self.price  = 0
#         elif reason == "in box":
#             self.status = "For Sale"
#         elif reason == "opened":
#             self.status = "Used"
#             self.cost *= .20
#         return self
#     def displayInfo(self):
#         print " Price:{}\n Name:{}\n Weight:{}\n Brand:{}\n Cost:{}".format(self.price,self.name,self.weight,self.brand,self.cost)
#         return self

# soap        = Product(5,"Soap",2,"Dove",5)
# paperTowels = Product(10,"Paper Towels",2.5,"Bounty",10)
# Gum         = Product(2,"Gum",.25,"5ive",.25)

# class Store(object):
#     def __init__(self,products,location,owner):
#         self.products = products
#         self.location = location
#         self.owner    = owner
#     def addProduct(self,p):
#         if type(p) != Product:return
#         self.products.append(p)
#         print "Added "+p.name
#         return self
#     def removeProduct(self,name):
#         if type(name) != str:return
#         cnt=0
#         for prod in self.products:
#             if prod.name == name:
#                 self.products.pop(cnt)
#                 print "Removed "+name
#             cnt+=1

#         # for ind in range(0,len(self.products)-1):
#         #     if self.products[ind].name == name:
#         #         self.products.pop(ind)

        
#         #if vars(prod).items()[1][1] == name:
#             #self.products.pop(ind)

#         return self
#     def inventory(self):
#         print "\nInventory:"

#         for prod in self.products:
#             print "    "+prod.name

#         return self

# s = Store(
#     [soap,paperTowels],
#     "Virginia",
#     "John Doe"
# )
# s.removeProduct("Soap")
# s.addProduct(Gum)
# s.inventory()