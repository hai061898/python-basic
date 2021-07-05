import re
s = input()
print (re.findall("\d+",s))

# findall () được sử dụng khi bạn muốn lặp quá trình tìm kiếm cho toàn bộ các dòng trong tệp,
#  nó sẽ trả về một danh sách tất cả các kết quả khớp chỉ với một bước
# trả về số