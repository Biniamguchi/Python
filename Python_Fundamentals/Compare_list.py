def compare_lists(list_one, list_two):
    if list_one == list_two:
        print "The lists are the same"
    else:
        print "The lists are not the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]


compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one, list_two)
 # or 
# def compare_list(list_one, list_two):

#     if len(list_one) != len(list_two):
#         print "The lists doesn't have equal length."
#         print "The lists are not the same."
#         return

#     else:
#         for i in range (0,len(list_one)):
#             if list_one[i] == list_two[i]:
#                 pass
#             else:
#                 print "Discrepancy:", list_one[i], "is not equal to", list_two[i]
#                 print "The lists are not the same."
#                 return

#     print "The lists are the same."

# compare_list([1,2,5,6,5,16],[1,2,5,6,5,8])
# compare_list([1,2,5,6,5],[1,2,5,6,5,3])
# compare_list([1,2,5,6,5,16],[1,2,5,6,5])
# compare_list(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])