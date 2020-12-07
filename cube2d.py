class Cube2d:
    def __init__(self):
        self.cube = [["R", "R", "W"], ["G", "C", "W"], ["G", "B", "B"]]

    def show(self):
        for i in self.cube:
            for j in i:
                print(j, end=" ")
            print("")
