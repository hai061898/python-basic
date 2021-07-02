s= input("Nhập câu của bạn")
d= {"DISGITS":0, "LETTERS":0}
for c in s :
    if  c.isdigit:
        d["DISGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])   

#Hàm isalpha() trả về true nếu chuỗi có ít nhất 1 ký tự và tất cả ký tự là chữ cái
#Hàm  isdigit() trả về số 