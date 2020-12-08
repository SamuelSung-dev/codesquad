from rubikscube import RubiksCube
from datetime import timedelta
from time import time


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
                action_tmp = action_tmp+letter_next

            actions.append(action_tmp)
        elif letter == "Q":
            actions.append(letter)
    return actions


start_time = time()
cube = RubiksCube()
control_count = 0
cube.show()
print()

while True:
    print("CUBE> ", end="")
    input_text = input()

    actions = parse_input(input_text)

    for action in actions:
        if action == "Q":
            end_time = time()-start_time
            times = str(timedelta(seconds=end_time)).split(".")
            times = times[0]
            print("경과시간:", times)
            print("조작갯수:", control_count)
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            exit()
        control_count = control_count+1
        print()
        print(action)
        face = action[0]
        is_clockwise = True
        if action.find("'") > 0:
            is_clockwise = False

        cube.rotate_face(face, is_clockwise)
        cube.rotate_adjacent(face, is_clockwise)

        cube.show()
        print()
