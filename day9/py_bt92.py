def xoaTrung( li ):
    list_moi=[]
    xem = set()
    for i in li:
        if i not in xem:
            xem.add( i )
            list_moi.append(i)
    return list_moi

li=[12,12,15,24,35,35,24,88,120,155,88,120,155]
print ("List sau khi xóa giá trị trùng là:",xoaTrung(li))
#Set trong python là một tập các giá trị không có thứ tự. Mỗi giá trị trong set là duy nhất, 
# không thể lặp lại và bất biến( tức bạn không thể thay đổi giá trị các phần tử trong set).