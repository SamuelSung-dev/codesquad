from collections import deque


class RubiksCube:
    def __init__(self):
        self.cube = {
            "F": Face("O"),  # Front Face
            "R": Face("G"),  # Right Face
            "U": Face("B"),  # Up Face
            "B": Face("Y"),  # Back Face
            "L": Face("W"),  # Left Face
            "D": Face("R"),  # Down Face
        }

    def show_updown(self, face):
        '''
        please use face only "U" and "D"
        '''
        print("                ", end="")
        self.cube[face].show_row(0)
        print("\n                ", end="")
        self.cube[face].show_row(1)
        print("\n                ", end="")
        self.cube[face].show_row(2)

    def show_midrow(self, row):
        print(" ", end="")
        self.cube["L"].show_row(row)
        print("     ", end="")
        self.cube["F"].show_row(row)
        print("     ", end="")
        self.cube["R"].show_row(row)
        print("     ", end="")
        self.cube["B"].show_row(row)

    def show(self):
        self.show_updown("U")
        print("\n")
        self.show_midrow(0)
        print()
        self.show_midrow(1)
        print()
        self.show_midrow(2)
        print("\n")
        self.show_updown("D")
        print()

    def rotate_face(self, face, rotation):
        tmp = []
        if rotation == "clockwise":
            tmp.append(self.cube[face]["pieces"].pop())
            tmp.append(self.cube[face]["pieces"].pop())
            self.cube[face]["pieces"].insert(0, tmp.pop(0))
            self.cube[face]["pieces"].insert(0, tmp.pop(0))
        elif rotation == "counterclockwise":
            tmp = self.cube[face]["pieces"].pop(0)
            tmp = self.cube[face]["pieces"].pop(0)
            self.cube[face]["pieces"].append(tmp.pop(0))
            self.cube[face]["pieces"].append(tmp.pop(0))

    def rotate_front_adjacent(self, rotation):
        D = []
        L = []
        U = []
        R = []
        D.append(self.cube["down"]["pieces"].pop(0))
        D.append(self.cube["down"]["pieces"].pop(0))
        D.append(self.cube["down"]["pieces"].pop(0))
        L.append(self.cube["left"]["pieces"].pop(2))
        L.append(self.cube["left"]["pieces"].pop(2))
        L.append(self.cube["left"]["pieces"].pop(2))
        U.append(self.cube["up"]["pieces"].pop(4))
        U.append(self.cube["up"]["pieces"].pop(4))
        U.append(self.cube["up"]["pieces"].pop(4))
        R.append(self.cube["right"]["pieces"].pop(6))
        R.append(self.cube["right"]["pieces"].pop(6))
        R.append(self.cube["right"]["pieces"].pop(0))
        if rotation == "clockwise":
            self.cube["down"]["pieces"].insert(0, R.pop())
            self.cube["down"]["pieces"].insert(0, R.pop())
            self.cube["down"]["pieces"].insert(0, R.pop())
            self.cube["left"]["pieces"].insert(2, D.pop())
            self.cube["left"]["pieces"].insert(2, D.pop())
            self.cube["left"]["pieces"].insert(2, D.pop())
            self.cube["up"]["pieces"].insert(4, L.pop())
            self.cube["up"]["pieces"].insert(4, L.pop())
            self.cube["up"]["pieces"].insert(4, L.pop())
            self.cube["right"]["pieces"].insert(0, U.pop())
            self.cube["right"]["pieces"].append(U.pop(0))
            self.cube["right"]["pieces"].append(U.pop(0))
        elif rotation == "counterclockwise":
            self.cube["down"]["pieces"].insert(0, L.pop())
            self.cube["down"]["pieces"].insert(0, L.pop())
            self.cube["down"]["pieces"].insert(0, L.pop())
            self.cube["left"]["pieces"].insert(2, U.pop())
            self.cube["left"]["pieces"].insert(2, U.pop())
            self.cube["left"]["pieces"].insert(2, U.pop())
            self.cube["up"]["pieces"].insert(4, R.pop())
            self.cube["up"]["pieces"].insert(4, R.pop())
            self.cube["up"]["pieces"].insert(4, R.pop())
            self.cube["right"]["pieces"].insert(0, D.pop())
            self.cube["right"]["pieces"].append(D.pop(0))
            self.cube["right"]["pieces"].append(D.pop(0))


class Face:
    def __init__(self, color):
        self.color = color
        self.pieces = deque(color*8)

    def show_row(self, row):
        if row == 0:
            print(self.pieces[0], self.pieces[1], self.pieces[2], end="")
        elif row == 1:
            print(self.pieces[7], self.color, self.pieces[3], end="")
        elif row == 2:
            print(self.pieces[6], self.pieces[5], self.pieces[4], end="")
