def find_character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):

        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])

    print new_list

test_list = ['hello','world','my','name','is','Anna']
find_character(test_list, 'o')
 
 # or
# def findCharacters (word_list, char):
#     newlist = []
#     for i in word_list:
#         if i.find(char) > -1:
#             newlist.append(i)
#     print newlist

# findCharacters(['hello','world','my','name','is','Anna'], 'o')