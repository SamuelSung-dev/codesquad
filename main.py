from cube2d import Cube2d

cube = Cube2d()

cube.show()

while True:
    print("\nCUBE>", end="")
    input_text = input()

    if input_text == "Q":
        print("Bye~")
        break
