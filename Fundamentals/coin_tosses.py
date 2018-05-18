def coin_tosses():
    import random
    print "Starting the program..."
    heads = 0
    tails = 0
    for turn in range (1,5001):
        flip = round(random.random())
        if flip == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a heads! ... Got {} head(s) so far and {} tail(s) so far".format(turn, heads, tails)
        if flip == 1:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tails! ... Got {} head(s) so far and {} tail(s) so far".format(turn, heads, tails)
    print "Ending the program, thank you!"
coin_tosses()

# import random

# def coin_toss():
#     heads = 0
#     tails = 0
#     res   = "heads"
#     print "Starting coin toss 5000:"

#     for i in range(0,5001):
#         if random.randint(0,1) == 0:
#             res = "heads"
#             heads+=1
#         else:
#             res = "tails"
#             tails+=1

#         print "Attempt #{}: Throwing a coin... Its {}!...Total heads:{} | Total tails:{}".format(i,res,heads,tails)

#     print "Ending the program, thank you!"
# coin_toss()
