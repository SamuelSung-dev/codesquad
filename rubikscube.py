from collections import deque


class RubiksCube:
    adjacency_table = {
        "F": {"D": 0, "L": 2, "U": 4, "R": 6},
        "U": {"F": 0, "L": 0, "B": 0, "R": 0},
        "D": {"B": 4, "L": 4, "F": 4, "R": 4},
        "L": {"D": 6, "B": 2, "U": 6, "F": 6},
        "R": {"D": 2, "F": 2, "U": 2, "B": 6},
        "B": {"D": 4, "R": 2, "U": 0, "L": 6},
    }

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

    def rotate_face(self, face, is_clockwise):
        if is_clockwise:
            self.cube[face].pieces.rotate(2)
        else:
            self.cube[face].pieces.rotate(-2)

    def rotate_front_adjacent(self, is_clockwise):
        tmp = {"D": [], "L": [], "U": [], "R": []}
        i = 0
        for key, value in tmp.items():
            self.cube[key].pieces.rotate(i)
            for ii in range(3):
                value.append(self.cube[key].pieces.popleft())
            value.reverse()
            i = i-2
        if is_clockwise:
            self.cube["U"].pieces.extendleft(tmp["L"])
            self.cube["R"].pieces.extendleft(tmp["U"])
            self.cube["D"].pieces.extendleft(tmp["R"])
            self.cube["L"].pieces.extendleft(tmp["D"])
        else:
            self.cube["U"].pieces.extendleft(tmp["R"])
            self.cube["R"].pieces.extendleft(tmp["D"])
            self.cube["D"].pieces.extendleft(tmp["L"])
            self.cube["L"].pieces.extendleft(tmp["U"])

        i = 0
        for key in tmp:
            self.cube[key].pieces.rotate(i)
            i = i+2


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
