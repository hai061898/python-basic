import re 
email = input()
frame = "(\w+)@((\w+\.)+(com))"
re2 = re.match(frame,email)
print (re2.group(1))
# Phương thức này trả về các giá trị so khớp giữa biểu thức chính quy và chuỗi cần so. Trong đó thì num này là vị trí index của list so khớp trả về mà bạn muốn lấy ra