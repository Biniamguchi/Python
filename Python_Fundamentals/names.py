Part I
# Given the following list, create a program that outputs full names (e.g. "Michael Jordan")
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def names():
    for data in range(len(students)):
        print students[data]["first_name"],students[data]["last_name"]
names()
#or
# def printDictVals(students):
#     for dict in students:
#         values = dict.values()
#         string = " ".join(values)
#         print string
# printDictVals(students)
Part II
# Given the folllowing dictionary, create a program that prints the following format:
# Students
# 1 - MICHAEL JORDAN - 13
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def combinedNames():
    for key, data in users.items():
        count = 0
        for value in data:
            if key == "Students":
                count +=1
                first_name = value["first_name"]
                last_name = value["last_name"]
                length = len(first_name) + len(last_name)
                print "{} - {} {} - {}" .format(count,first_name, last_name, length)
            else:
                count +=1
                first_name = value["first_name"]
                last_name = value["last_name"]
                length = len(first_name) + len(last_name)
                print "{} - {} {} - {}" .format(count,first_name, last_name, length)
                
combinedNames()

def combinedNames(users):
    for key, value in users.iteritems():
        print key
        count = 0
        for dict in value:
            string = (" ".join(dict.values()))
            count += 1
            print count, "-", string.upper(), "-", len(string) - 1
