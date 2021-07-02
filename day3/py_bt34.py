def printDict():
    d =dict()
    for i in range(1,9):
        d[i]=i**2
        for (k,v) in d.items():
            print (v)
printDict()            