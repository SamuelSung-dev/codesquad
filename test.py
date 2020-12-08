from collections import deque
from rubikscube import RubiksCube

cube = RubiksCube()

L = deque(["L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7"])
D = deque(["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7"])
U = deque(["U0", "U1", "U2", "U3", "U4", "U5", "U6", "U7"])
R = deque(["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7"])

dic = {"D": D, "L": L, "U": U, "R": R}
tmp = {"D": [], "L": [], "U": [], "R": []}

i = 0
for key, value in tmp.items():
    dic[key].rotate(i)
    for ii in range(3):
        value.append(dic[key].popleft())
    value.reverse()
    i = i-2
dic["U"].extendleft(tmp["R"])
dic["R"].extendleft(tmp["D"])
dic["D"].extendleft(tmp["L"])
dic["L"].extendleft(tmp["U"])

i = 0
for key in tmp:
    dic[key].rotate(i)
    i = i+2
    print(dic[key])
