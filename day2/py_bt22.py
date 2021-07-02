from operator import itemgetter , attrgetter
l =[]
while True:
    s= input()
    if not s :
        break
    l.append(tuple(s.split(",")))
print (sorted(l, key=itemgetter(0,1,2)))    
#itemgetter(n) xây dựng một hàm có thể gọi được,
#  giả sử một đối tượng có thể lặp lại 
# (ví dụ: list, Tuple, set) làm đầu vào và 
# lấy phần tử thứ n ra khỏi nó