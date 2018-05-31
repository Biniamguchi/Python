# Part I
# draw_stars() that takes a list of numbers and prints out *
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars():
    for i in range(len(x)):
        print "*" * x[i]
draw_stars()

# Part II
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_star(x):
    for i in x:
        if type(i) == int:
            print "*" * i
        else:
            # for a in range(len(i)): 
            print i[0].lower() * len(i)
draw_star(x)

# numlist = [4, 6, 1, 3, 5, 7, 25]
# def draw_stars(numlist):
#     for nums in numlist:
#         print "*" * nums
# draw_stars(numlist)

