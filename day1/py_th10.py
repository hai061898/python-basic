# mảng 2 chiều
input_str = input("Nhập X,Y:")
array = [int(x) for x in input_str.split(',')]
rowNum=array[0]
colNum=array[1]
multilist = [[0 for col in range(colNum) for row in range(rowNum)]]
for row in range(rowNum):
    for col in range(colNum):
        multilist[[row][col]]=row*col
print (multilist)        

        