position = [1,1]
north = "(N)orth"
east = "(E)ast"
south = "(S)outh"
west = "(W)est"

while position != [3,1]:
    if position == [1,1]:
        print ("You can travel: " + north + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "n":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        position[1] = position[1] + 1  
    elif position == [1,2]:
        print ("You can travel: " + north + " or " + east + " or " + south + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "n" and direction != "e" and direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        if direction == "n":
            position[1] = position[1] + 1
        elif direction == "e":
            position[0] = position[0] + 1 
        else:
            position[1] = position[1] - 1
    elif position == [1,3]:
        print ("You can travel: "  + east + " or " + south + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "e" and direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        if direction == "e":
            position[0] = position[0] + 1 
        else:
            position[1] = position[1] - 1
    elif position == [2,3]:
        print ("You can travel: "  + east + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "e":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        position[0] = position[0] + 1
    elif position == [2,2]:
        print ("You can travel: "  + west + " or " + south + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "w" and direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        if direction == "w":
            position[0] = position[0] - 1 
        else:
            position[1] = position[1] - 1
    elif position == [2,1]:
        print ("You can travel: "  + north + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "n":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        position[1] = position[1] + 1
    elif position == [3,3]:
        print ("You can travel: "  + west + " or " + south + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "w" and direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        if direction == "w":
            position[0] = position[0] - 1
        else:
            position[1] = position[1] - 1
    elif position == [3,2]:
        print ("You can travel: "  + north + " or " + south + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "n" and direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        if direction == "n":
            position[1] = position[1] + 1
        else:
            position = [3,1]
print("Victory!")