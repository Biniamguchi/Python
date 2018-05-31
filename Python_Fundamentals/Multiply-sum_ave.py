# prints all the odd numbers from 1 to 1000
for x in range (1,1001):
    if x % 2 ==1:
        print x

# prints all the multiples of 5 from 5 to 1,000,000
for y in range(5,1000001):
     if y % 5 ==0:
         print y

# prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
    print sum

# print sum/len(a)
# prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
ave = 0
sum = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    sum = sum + i
    ave = sum/len(a)
    print ave; 