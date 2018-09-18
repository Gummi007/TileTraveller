# position = [1,1]
# north = "(N)orth"
# east = "(E)ast"
# south = "(S)outh"
# west = "(W)est"

# while position != [3,1]:
#     if position == [1,1]:
#         print ("You can travel: " + north + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "n":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         position[1] = position[1] + 1  
#     elif position == [1,2]:
#         print ("You can travel: " + north + " or " + east + " or " + south + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "n" and direction != "e" and direction != "s":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         if direction == "n":
#             position[1] = position[1] + 1
#         elif direction == "e":
#             position[0] = position[0] + 1 
#         else:
#             position[1] = position[1] - 1
#     elif position == [1,3]:
#         print ("You can travel: "  + east + " or " + south + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "e" and direction != "s":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         if direction == "e":
#             position[0] = position[0] + 1 
#         else:
#             position[1] = position[1] - 1
#     elif position == [2,3]:
#         print ("You can travel: "  + east + " or " + west + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "e":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         position[0] = position[0] + 1
#     elif position == [2,2]:
#         print ("You can travel: "  + south + " or " + west + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "w" and direction != "s":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         if direction == "w":
#             position[0] = position[0] - 1 
#         else:
#             position[1] = position[1] - 1
#     elif position == [2,1]:
#         print ("You can travel: "  + north + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "n":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         position[1] = position[1] + 1
#     elif position == [3,3]:
#         print ("You can travel: "  + south + " or " + west + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "w" and direction != "s":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         if direction == "w":
#             position[0] = position[0] - 1
#         else:
#             position[1] = position[1] - 1
#     elif position == [3,2]:
#         print ("You can travel: "  + north + " or " + south + ".")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         while direction != "n" and direction != "s":
#             print("Not a valid direction!")
#             direction = input("Direction: ")
#             direction = direction.lower()
#         if direction == "n":
#             position[1] = position[1] + 1
#         else:
#             position = [3,1]
# print("Victory!")

def is_winning(position):
    if position == [3,1]:
        return True
    else:
        return False

def instructions(position):
    north = "(N)orth"
    east = "(E)ast"
    south = "(S)outh"
    west = "(W)est"
    if position == [1,1]:
        print ("You can travel: " + north + ".")
    elif position == [1,2]:
        print ("You can travel: " + north + " or " + east + " or " + south + ".")
    elif position == [1,3]:
        print ("You can travel: "  + east + " or " + south + ".")
    elif position == [2,3]:
        print ("You can travel: "  + east + " or " + west + ".")
    elif position == [2,2]:
        print ("You can travel: "  + south + " or " + west + ".")
    elif position == [2,1]:
        print ("You can travel: "  + north + ".")
    elif position == [3,3]:
        print ("You can travel: "  + south + " or " + west + ".")
    elif position == [3,2]:
        print ("You can travel: "  + north + " or " + south + ".")

def get_input():
    return input("Direction: ")  
    
def is_valid_move(direction, position):
    if position == [1,1]:
        if direction == "n":
            return True
        else:
            return False
    elif position == [1,2]:
        if direction == "n" or direction == "e" or direction == "s":
            return True
        else:
            return False
    elif position == [1,3]:
        if direction == "e" or direction == "s":
            return True
        else:
            return False
    elif position == [2,3]:
        if direction == "e" or direction == "w":
            return True
        else:
            return False
    elif position == [2,2]:
        if direction == "w" or direction == "s":
            return True
        else:
            return False
    elif position == [2,1]:
        if direction == "n":
            return True
        else:
            return False
    elif position == [3,3]:
        if direction == "w" or direction == "s":
            return True
        else:
            return False
    elif position == [3,2]:
        if direction == "n" or direction == "s":
            return True
        else:
            return False
    
def move_north(position):
    position[1] += 1
    return position

def move_south(position):
    position[1] -= 1
    return position

def move_east(position):
    position[0] += 1
    return position

def move_west(position):
    position[0] -= 1
    return position

def move(direction, position):
    if direction == "n":
        return move_north(position)
    elif direction == "s":
        return move_south(position)
    elif direction == "e":
        return move_east(position)
    else:
        return move_west(position)


position = [1,1]

while not is_winning(position):
    instructions(position)
    direction = get_input().lower()
    while not is_valid_move(direction, position):
        print("Not a valid direction!")
        direction = get_input().lower()
    position = move(direction, position)
print("Victory!")