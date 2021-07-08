dic = {}
chuoi=input("Nhập chuỗi cần đếm ký tự: ")

for c in chuoi:
    dic[c] = dic.get(c,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

# Sử dụng dict để lưu trữ các cặp key/value.
# Sử dụng dict.get() để tra cứu key với giá trị mặc định.