input_text = input()
# print(text)
input_list = input_text.split()

text = input_list[0]
move_count = 0

try:
    move_count = int(input_list[1])
except:
    print("Second input is not integer.")
    exit()

if move_count < -100 or move_count >= 100:
    print("Second input is out of range.")
    exit()

direction = input_list[2].lower()
if direction != "l" and direction != "r":
    print("Third input is not l(L) or r(R).")
    exit()

print(text, move_count, direction)
