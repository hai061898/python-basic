value = []
item = [x for x in input("Nhập các số nhị phân").split(',')]
for p in item:
    tamp = int(p,2)
    if not tamp%5:
        value.append(p)
print (','.join(value))        