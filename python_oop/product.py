class Product(object):
    def __init__(self, price,item_Name,weight,brand,status):        
        self.price = price
        self.item_Name = item_Name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self.status

    def addTax(self,tax):
        self.price *= tax
        return self.price

    def return_item(self,reason):
         if reason.find('defect' or 'broke' or 'malfunction') > -1:
            self.status = "defective"
            self.price = 0
        if reason.find('new' or 'unopen') > -1:
            self.status = "for sale"
        if reason.find('opened') > -1:
            self.status = "used"
            self.price *= 0.20
        return self.status, self.price

    def display_info(self):
        print "Price: ${}".format(self.price)
        print "Item Name:", self.item
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self

#Another solution

#class Product(object):
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

# soap = Product(5,"Soap",2,"Dove",5)
# print soap.addTax(12)
# soap.sell()
# print vars(soap).items()
# soap.status = "ASKDJH" # Checking privacy
# print vars(soap).items()
# soap.Return("in box")
# print vars(soap).items()
# print "\n"

# soap.sell().Return("opened").sell().displayInfo()
# for k,v in vars(soap).items():
#     print k,v