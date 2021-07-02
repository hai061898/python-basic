import math
pos =[0,0]
while True:
    s=input()
    if not s:
        break
    movement = s.split(",")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "U":
        pos[0] +=steps
    elif direction == "D":
        pos[0] -= steps
    elif direction == "L":
        pos[1]-=steps
    elif direction == "R":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))