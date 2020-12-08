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
        if letter == "F" or letter == "L" or letter == "R" or letter == "U" or letter == "D" or letter == "B":
            action_tmp = letter
            if letter_next == "'":
                action_tmp = action_tmp+"'"
            actions.append(action_tmp)
        elif letter == "Q":
            actions.append(letter)
    return actions


cube = RubiksCube()

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
        face = action[0]
        is_clockwise = True
        if action.find("'") > 0:
            is_clockwise = False
        cube.rotate_face(face, is_clockwise)
        if face == "F":
            cube.rotate_front_adjacent(is_clockwise)
        cube.show()
        print()
