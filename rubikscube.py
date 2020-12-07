from copy import deepcopy


class RubiksCube:
    def __init__(self):
        self.cube = [["R", "R", "W"], ["G", "C", "W"], ["G", "B", "B"]]

    def show(self):
        for i in self.cube:
            for j in i:
                print(j, end=" ")
            print()

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
