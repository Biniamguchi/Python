sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

test = mL
test_type = type(test)
if test_type is int:
    if test >= 100:
        print 'That is a big number'
    else:
        print 'That is a small number!'
elif test_type is str:
    if len(test) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"
elif isinstance(test, list):
    if len(test) >= 10:
        print "Big list!"
    else:
        print "Short list."
