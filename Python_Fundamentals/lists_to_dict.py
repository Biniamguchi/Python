#Create a function that takes in two lists and creates a single dictionary

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def listToDic():
    name_fav = zip(name, favorite_animal)
    print name_fav
    name_fav_dict = dict(name_fav)
    print name_fav_dict
listToDic()

