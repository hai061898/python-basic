def putnum(n):
    i=0
    while i< n:
        j=i
        i=i+1
        if j%7==0:
            yield j
for i in putnum (100) :
    print (i)            



# Yield là một keyworrd trong Python được sử dụng 
# để trả về giá trị của hàm mà không hủy đi trạng
#  thái của các biến trong hàm. Nó sẽ tạm giữ trạng 
# thái của các biến ngay tại vị trí yield đầu tiên, 
# để những lần goi hàm tiếp theo sẽ tiếp tục xử lý