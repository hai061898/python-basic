s = input()
v = s.encode() # có thể dùng v=s.encode('utf-8')
print (v)

# Phương thức encode() trả về phiên bản chuỗi đã được mã hóa của chuỗi ban đầu. Nếu có lỗi xảy ra, thì chương trình sẽ tạo một ValueError trừ khi các lỗi này được cung cấp với ignore hoặc replace.