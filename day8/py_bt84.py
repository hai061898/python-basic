S=["Star","Moon"]
V=["Like","Love"]
AD=["Night","Sky"]
for i in range(len(S)):
    for j in range(len(V)):
        for k in range(len(AD)):
            cau = "%s %s %s." % (S[i], V[j], AD[k])
            print (cau)