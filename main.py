from rubikscube import RubiksCube


def parse_input(input_text):
    actions = []
    for ii in range(len(input_text)):
        letter = input_text[ii]
        letter_next = ""
        try:
            letter_next = input_text[ii+1]
        except:
            letter_next = ""
        if letter == "U" or letter == "R" or letter == "L" or letter == "B":
            action_tmp = letter
            if letter_next == "'":
                action_tmp = action_tmp+"'"
            actions.append(action_tmp)
        elif letter == "Q":
            actions.append(letter)
    return actions


cube = Cube3d()

cube.show()
print()

while True:
    print("CUBE> ", end="")
    input_text = input()

    actions = parse_input(input_text)

    for action in actions:
        if action == "Q":
            print("Bye~")
            exit()

        print()
        print(action)
        if action == "U":
            cube.rotate_top_left()
        elif action == "U'":
            cube.rotate_top_right()
        elif action == "R":
            cube.rotate_right_up()
        elif action == "R'":
            cube.rotate_right_down()
        elif action == "L":
            cube.rotate_left_down()
        elif action == "L'":
            cube.rotate_left_up()
        elif action == "B":
            cube.rotate_bottom_right()
        elif action == "B'":
            cube.rotate_bottom_left()
        cube.show()
        print()
