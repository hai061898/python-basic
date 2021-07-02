class Person:
    name = "Person"
    def __init__(self, name =None):
        self.name =name
jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name,jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))

#  phương thức __ init __ mô phỏng contructor của lớp. 
# Phương thức này được gọi khi lớp được khởi tạo. 
# Chúng ta có thể chuyển bất kỳ số lượng đối số nào tại
#  thời điểm tạo đối tượng lớp, tùy thuộc vào định nghĩa
#  __ init __. Nó chủ yếu được sử dụng để khởi tạo các thuộc
#  tính của lớp.