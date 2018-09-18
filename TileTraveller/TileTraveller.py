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
        position[0] = 1+1  