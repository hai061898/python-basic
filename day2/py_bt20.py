import sys
tk = 0 
while True:
    s = input("Nhập nhận ký giao dịch:")
    if not s :
        break
    values = s.split(" ")
    action = values[0]
    money = int(values[1])
    if action == "S":
        tk += money
    if action == "W":
        tk -= money
    else:
        pass
print (tk)      