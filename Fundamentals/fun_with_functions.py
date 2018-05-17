# Create a function called odd_even that counts from 1 to 2000.
def odd_even():
    for count in range(1, 2000):
        if count % 2 == 0:
            print "Number is {}. This is an odd number.".format(count)
        else:
            print 'Number is', count,'.',('This is an odd number.')
               
odd_even()

# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
def multiply(arr,num):
    for i in range(len(arr)):
        arr[i]*= num
    return arr
a = [2, 4, 10, 16]
b = multiply(a,5)
print b 

# def multiply(li,val):
#     newLi = []

#     for i in li:
#         newLi.append(i*val)

#     return newLi
#multiply([2,4,10,16],5)

