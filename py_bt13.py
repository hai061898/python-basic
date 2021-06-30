s = input("nhập chuỗi")
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(words))))

#Hàm sorted() trong Python sắp xếp các phần tử của một đối tượng theo thứ tự nhất định (tăng dần hoặc giảm dần) 
#Trong Python, List là một kiểu dữ liệu linh hoạt nhất. Nó là dẫy (sequence)
#  phần tử (element), nó cho phép loại bỏ, hoặc thêm các phần tử vào danh sách, đồng thời cho phép cắt lát (Slice) các phần tử
# Hàm set() được tích hợp sẵn trong Python sử dụng để tạo một đối tượng set từ iterable đã cho.

# # tập hợp rỗng
# print(set())

# # string
# print(set('Python'))

# # tuple
# # viết bởi Quantrimang.com
# print(set(('a', 'e', 'i', 'o', 'u')))

# # list
# print(set(['a', 'e', 'i', 'o', 'u']))

# # range
# print(set(range(5)))

# set()
# {'P', 'o', 't', 'n', 'y', 'h'}
# {'a', 'o', 'e', 'u', 'i'}
# {'a', 'o', 'e', 'u', 'i'}
# {0, 1, 2, 3, 4}