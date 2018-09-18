#https://github.com/Gummi007/TileTraveller

# 1. Seinna implementation-ið var mun auðveldara þar sem það var nánast búið að búa til allan kóðan í fyrra skiptið. 
#    Eina sem þurfti að gera var að skoða fyrri verkefnið og sjá hvað var hægt að taka saman í hvaða föll, og svo 
#    eiginlega bara copy, paste úr kóðanum í fyrra verkefninu inn í föllinn. Ef samt það ætti að gera implementation-in
#    óháð hvor öðru, semsagt byrja á seinni verkefninu fyrst, hefði seinni verið erfiðara því það væri ekki jafn
#    auðvelt að sjá hvað væri hægt að taka saman í föll. 
# 2. Seinna implementation-ið er mun auðveldara að lesa því það er notað föll. Föllin heita lýsandi nöfnum og er mun
#    auðveldara að skilja hvernig forritið virkar þrátt fyrir að skoða/skilja ekki föllin.
# 3. Skipulag er eitt vandamál í fyrra verkefninu sem hægt var að laga í seinna. Til dæmis í fyrra verkefninu var ég
#    með while lykkju fyrir hverja staðsetningu sem athugaði hvort rétt input væri slegið inn, en í seinna verkefninu
#    bjó ég til eitt fall sem gat sagt mér hvort rétt input væri slegið inn fyrir hvaða staðsetningu sem er. Semsagt
#    seinna verkefnið leysti aðalega skipulagsleysi, endurtekningar og læsileika.

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

def move_position(direction, position):
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
    position = move_position(direction, position)    
print("Victory!")