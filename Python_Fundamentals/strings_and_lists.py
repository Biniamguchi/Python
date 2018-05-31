#find and replace
words = "It's thanksgiving day. It's my birthday,too!"
print words
print words.find('day')
words = words.replace("day", "month")
print words

# #min and max
x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)

# #first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
