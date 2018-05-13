print 'hello'
# Get even 1000
for i in range (1, 1001):
    if i % 2 == 0:
        print i;

 # Sum odd 5000 
sum = 0
for i in range (1,5001):
    if i % 2 ==1 :
        sum= sum +i
        print sum
# multiples of 5 from 5 to 1,000,000
for i in range (5, 1000000):
    if i % 5 == 0:
        print i;
#sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
sum = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    sum = sum +i
    print sum;
# average of the values in the list: a = [1, 2, 5, 10, 255, 3]
ave = 0
sum = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    sum = sum + i
    ave = sum/len(a)
    print ave;
#find and replace
string = "If monkeys like bananas, then I must be a monkey!"
print string
print string.find("monkey")
string = string.replace("monkey", "alligator")
print string

#min and max
x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)

#first and last
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

l = [2,3,1,7,4,12]
sum = 0
test_l = type(i)
if test_l is int:
    for i in l:
        sum+=i
    print sum
else:
    print "not integer"