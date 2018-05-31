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

# Hacker Challenge
# def layered_multiples(list_mult):
#     list_1s = []                            # create empty list output of 1s
#     for idx in range(0,len(list_mult)):     # FOR to iterate thru idxs of list_mult
#         list_1s.append([])                  # Append empty sub-list into list_1s
#         while list_mult[idx] > 0:           # FOR to divide up nums in each idx of list_mult
#             list_1s[idx].append(1)          # Append 1 into sub-list until num < 1
#             list_mult[idx] -= 1
#     return list_1s



# def layered_multiples(arr):
#     print arr
#     new_array = []
#     for x in arr:
#         val_arr = []
#         for i in range(0,x):
#             val_arr.append(1)
#         new_array.append(val_arr)
#     return new_array
