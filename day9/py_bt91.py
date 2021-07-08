#set() và "&=" để thiết lập điểm giao.
list1=set([12,3,6,78,35,55,120])
list2=set([12,24,35,24,88,120,155])

list1 &= list2
li=list(list1)
print (li)