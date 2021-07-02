values = input("nhập chuỗi số của bạn")
number = [x for x in values.split(",")  if int(x)%2!=0]
print(",".join(number))