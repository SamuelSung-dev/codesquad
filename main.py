from cube2d import Cube2d

cube = Cube2d()

cube.show()

while True:
    print("\nCUBE> ", end="")
    input_text = input()

    print()
    action = []
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
            action.append(action_tmp)
        elif letter == "Q":
            action.append(letter)

    print(action)
