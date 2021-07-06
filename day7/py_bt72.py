# tìm kiến 
import math
def search(x,y):
    bottom =0
    top = len(x)-1
    index =-1
    while top>=bottom and index ==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if x[mid] == y:
            index =mid
        elif x[mid]>y:
            top = mid-1
        else:
            bottom = mid+1
    return index
li=[2,5,7,9,11,17,222]
print (search(li,11))