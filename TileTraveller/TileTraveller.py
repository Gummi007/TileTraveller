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
        print ("You can travel: " + north + "or" + east + "or" + south + ".")
        direction = input("Direction: ")
        direction = direction.lower()
        while direction != "n" or direction != "e" or direction != "s":
            print("Not a valid direction!")
            direction = input("Direction: ")
            direction = direction.lower()
        if direction == "n":
            position[1] = position[1] + 1
        elif direction == "e":
            position[0] = position[0] + 1 
        else:
            position[1] = position[1] - 1