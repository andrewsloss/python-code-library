#⬜⬜⬜⬜⬜
#⬜⬜⬜⬜⬜
#⬜⬜⬜⬜⬜
#⬜⬜⬜⬜⬜
#😐⬜⬜⬜⬜

x = 0
y = 0

player = "😐"
background = "⬜"

def render(x, y):
    global player, background

    grid_x, grid_y =  5, 5

    grid = []

    playerCheck = 0

    for a in range(grid_y):
        array = []
        for b in range(grid_x):
            if a == y and b == x:
                array.append(player)
                playerCheck += 1
            else:
                array.append(background)
        grid.append(array)


    if playerCheck == 0:
        print("OUT OF BOUNDS")
        quit()

    for a in range (len(grid)):
        for b in range (len(grid[0])):
            print(grid[a][b], end = "")
        print("")

while(True):

    render(x, y)

    print("")
    
    playerInput = input("> ").lower()

    if playerInput == "w":
        y -= 1
    elif playerInput == "a":
        x -= 1
    elif playerInput == "s":
        y += 1
    elif playerInput == "d":
        x += 1

    print("")