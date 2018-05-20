# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. 
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def makingTuples():
    print my_dict.items()
makingTuples()

# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }

# def dictToTuple(dic):
#     if type(dic) != dict:
#         print "Usage: Arg must be of type dict."
#         return

#     li = []
#     for i in dic:
#         li.append((i,dic[i]))

#     return li

# t = dictToTuple(my_dict)
# print t

#or 
# def dictToTuples(dict):
#     keys = dict.keys()
#     values = dict.values()
#     tuples_list = []
#     for i in range(0,len(keys)):
#         tuples = (keys[i], values[i])
#         tuples_list.append(tuples)
#     return tuples_list