print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
def square(num):
 '''Trả lại giá trị bình phương của số được nhập vào.

 Số nhập vào phải là số nguyên.
 '''
 return num ** 2

print (square.__doc__)


# __doc__
# Các docstrings được khai báo bằng cách sử dụng "" dấu ngoặc kép ba "" hoặc "" "dấu ngoặc kép ba" "" ngay bên dưới khai báo lớp, phương thức hoặc hàm.
#  Tất cả các chức năng phải có một chuỗi doc.

# def square(n):
    
#     '''Takes in a number n, returns the square of n'''

#     return n**2