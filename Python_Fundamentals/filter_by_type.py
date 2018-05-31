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

def filterByType(val):
    if type(val) is int:
        if val >= 100:
            print val, '- is a big number'
        else:
            print val, '- is a small number!'
    elif type(val) is str:
        if len(val) >= 50:
            print len(val), "characters is a long sentence"
        else:
            print len(val), "characters is a short sentence"
    elif isinstance(val, list):
        if len(val) >= 10:
            print len(val), "is a big list!"
        else:
            print len(val), "is a short list."

filterByType(sI)
filterByType(mI)
filterByType(bI)
filterByType(eI)
filterByType(spI)
filterByType(sS)
filterByType(mS)
filterByType(bS)
filterByType(eS)
filterByType(aL)
filterByType(mL)
filterByType(lL)
filterByType(eL)
filterByType(spL)
