def f(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n = int(input("nhập n:"))
v = []
for i in f(n):
    v.append(str(n))
print ("Các số chẵn trong khoảng 0 và n là: ",",".join(v))

#yield để tạo ra giá trị kết tiếp trong generator
# Yield là một keyworrd trong Python được sử dụng để trả về giá trị của hàm mà không hủy đi trạng thái của các biến trong hàm