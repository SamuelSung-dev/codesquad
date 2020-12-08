from copy import deepcopy


class RubiksCube:
    def __init__(self):
        self.cube = {
            "front": ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
            "right": ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
            "up":    ["B", "B", "B", "B", "B", "B", "B", "B", "B"],
            "back":  ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            "left":  ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            "down":  ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
        }

    def show_row(self, face, num):
        if num == 0:
            print(self.cube[face][0], self.cube[face]
                  [1], self.cube[face][2], end="")
        elif num == 1:
            print(self.cube[face][7], self.cube[face]
                  [8], self.cube[face][3], end="")
        elif num == 2:
            print(self.cube[face][6], self.cube[face]
                  [5], self.cube[face][4], end="")

    def show(self):
        print("                ", end="")
        self.show_row("up", 0)
        print("\n                ", end="")
        self.show_row("up", 1)
        print("\n                ", end="")
        self.show_row("up", 2)
        print("\n\n ", end="")
        self.show_row("left", 0)
        print("     ", end="")
        self.show_row("front", 0)
        print("     ", end="")
        self.show_row("right", 0)
        print("     ", end="")
        self.show_row("back", 0)
        print("\n ", end="")
        self.show_row("left", 1)
        print("     ", end="")
        self.show_row("front", 1)
        print("     ", end="")
        self.show_row("right", 1)
        print("     ", end="")
        self.show_row("back", 1)
        print("\n ", end="")
        self.show_row("left", 2)
        print("     ", end="")
        self.show_row("front", 2)
        print("     ", end="")
        self.show_row("right", 2)
        print("     ", end="")
        self.show_row("back", 2)
        print("\n\n                ", end="")
        self.show_row("down", 0)
        print("\n                ", end="")
        self.show_row("down", 1)
        print("\n                ", end="")
        self.show_row("down", 2)

    def rotate(self, face, 0):
        """
        docstring
        """
        pass

    def rotate_top_left(self):
        top = deepcopy(self.cube[0])
        self.cube[0][0] = top[1]
        self.cube[0][1] = top[2]
        self.cube[0][2] = top[0]

    def rotate_top_right(self):
        top = deepcopy(self.cube[0])
        self.cube[0][0] = top[2]
        self.cube[0][1] = top[0]
        self.cube[0][2] = top[1]

    def rotate_right_up(self):
        right = [deepcopy(self.cube[0][2]), deepcopy(
            self.cube[1][2]), deepcopy(self.cube[2][2])]
        self.cube[0][2] = right[1]
        self.cube[1][2] = right[2]
        self.cube[2][2] = right[0]

    def rotate_right_down(self):
        right = [deepcopy(self.cube[0][2]), deepcopy(
            self.cube[1][2]), deepcopy(self.cube[2][2])]
        self.cube[0][2] = right[2]
        self.cube[1][2] = right[0]
        self.cube[2][2] = right[1]

    def rotate_left_down(self):
        left = [deepcopy(self.cube[0][0]), deepcopy(
            self.cube[1][0]), deepcopy(self.cube[2][0])]
        self.cube[0][0] = left[2]
        self.cube[1][0] = left[0]
        self.cube[2][0] = left[1]

    def rotate_left_up(self):
        left = [deepcopy(self.cube[0][0]), deepcopy(
            self.cube[1][0]), deepcopy(self.cube[2][0])]
        self.cube[0][0] = left[1]
        self.cube[1][0] = left[2]
        self.cube[2][0] = left[0]

    def rotate_bottom_right(self):
        bottom = deepcopy(self.cube[2])
        self.cube[2][0] = bottom[2]
        self.cube[2][1] = bottom[0]
        self.cube[2][2] = bottom[1]

    def rotate_bottom_left(self):
        bottom = deepcopy(self.cube[2])
        self.cube[2][0] = bottom[1]
        self.cube[2][1] = bottom[2]
        self.cube[2][2] = bottom[0]
