info = ["name", "age", "country of birth", "favorite language"]
value = ["Anna", 101, "The United States", "Python"]

info_val = zip(info, value)
print info_val

info_val_dict = dict(info_val)
print info_val_dict

# [('name', 'Anna'), ('age', 101), ('country of birth', 'The United States'), ('favorite language', 'Python')]
# {'age': 101, 'favorite language': 'Python', 'name': 'Anna', 'country of birth': 'The United States'}
def dictBasic():
    for key, data in info_val_dict.iteritems():
        print "My", key,"is", data
dictBasic()

# brian = {
#     "name" : "Brian",
#     "age" : 33,
#     "country of birth" : "America",
#     "favorite language" : "Python"
# }


# def userDict(dict):
#     keys = dict.keys()
#     values = dict.values()
#     for i in range(0,len(keys)):
#         print "My {} is {}".format(keys[i],values[i])

# def print_dictionary_values(dic):
#     for some_key, some_value in dic.iteritems():
#         print "My" + " " + some_key + " " + "is" + " " + str(some_value)