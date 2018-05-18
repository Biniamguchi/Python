# function that generates ten scores between 60 and 100.
def scoresGrades():
    import random
    print "Scores and Grades"
    for i in range(1,11):
        score = random.randint(60,100)        
        if score <= 69:
            print "Score: {}; Your grade is D".format(score)
        elif score <= 79:
            grade = chr(ord('D') - 1)
            print "Score: {}; Your grade is C".format(score)
        elif score <= 89:
            grade = chr(ord('D') - 2)
            print "Score: {}; Your grade is B".format(score)
        elif score <= 100:
            grade = chr(ord('D') - 3)
            print "Score: {}; Your grade is A".format(score)
    print "End of the program. Bye!"

scoresGrades()

# import random

# def randGrades():
#     grade = 0

#     grades = [
#         {"min":90,"max":100,"grade":"A"},
#         {"min":80,"max":89,"grade":"B"},
#         {"min":70,"max":79,"grade":"C"},
#         {"min":60,"max":69,"grade":"D"},
#         {"min":0,"max":59,"grade":"F"}
#     ]

#     print "Scores and Grades:"

#     for i in range(0,10):
#         grade = random.randint(60,100)

#         for j in range(0,len(grades)):
#             if grade >= grades[j]["min"] and grade <= grades[j]["max"]:
#                 grade = "Score: "+str(grade)+"Your grade: "+grades[j]["grade"]

#         print grade
# randGrades()