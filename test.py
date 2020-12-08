from collections import deque
from rubikscube import Face, RubiksCube


adjacency_table = {
    "F": {"D": 0, "L": 2, "U": 4, "R": 6},
    "U": {"F": 0, "L": 0, "B": 0, "R": 0},
    "D": {"B": 4, "L": 4, "F": 4, "R": 4},
    "L": {"D": 6, "B": 2, "U": 6, "F": 6},
    "R": {"D": 2, "F": 2, "U": 2, "B": 6},
    "B": {"D": 4, "R": 2, "U": 0, "L": 6},
}
cube = {
    "L": deque(["L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7"]),
    "D": deque(["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7"]),
    "U": deque(["U0", "U1", "U2", "U3", "U4", "U5", "U6", "U7"]),
    "R": deque(["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7"]),
    "F": deque(["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7"]),
    "B": deque(["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7"]),
}


def rotate_adjacent(cube, face, is_clockwise):
    dic = adjacency_table[face]
    tmp = {}
    for key in dic:
        tmp[key] = []

    for key, value in dic.items():
        cube[key].rotate(-value)
        for ii in range(3):
            tmp[key].append(cube[key].popleft())
        tmp[key].reverse()

    store_key = list(dic.keys())
    load_key = deque(dic.keys())

    if is_clockwise:
        load_key.rotate()
    else:
        load_key.rotate(-1)

    for ii in range(4):
        cube[store_key[ii]].extendleft(tmp[load_key[ii]])

    for key, value in dic.items():
        cube[key].rotate(value)


rotate_adjacent(cube, "F", False)
for key, value in cube.items():
    print(key, value)


"""
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
"""
