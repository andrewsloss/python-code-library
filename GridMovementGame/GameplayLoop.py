import random

#⬜⬜⬜⬜🍎
#⬜⬜⬜⬜⬜
#⬜⬜⬜⬜⬜
#⬜⬜⬜⬜⬜
#🐍⬜⬜⬜⬜


grid_x, grid_y =  10, 5

x = random.randint(0, grid_x - 1)
y = random.randint(0, grid_y - 1)

appleX = random.randint(0, grid_x - 1)
appleY = random.randint(0, grid_y- 1)

while(appleX == x and appleY == y):
    appleX = random.randint(0, grid_x - 1)
    appleY = random.randint(0, grid_y - 1)

player = "🐍"
apple = "🍎"
background = "⬜"

score = 0

def render(x, y):
    global player, apple, background, appleX, appleY, gridX, grid_y, score

    grid = []

    playerCheck = 0
    appleCheck = 0

    for a in range(grid_y):
        array = []
        for b in range(grid_x):
            if a == y and b == x:
                array.append(player)
                playerCheck += 1
            elif a == appleY and b == appleX:
                array.append(apple)
                appleCheck += 1
            else:
                array.append(background)
        grid.append(array)

    if playerCheck == 0:
        print("OUT OF BOUNDS\nHIGH SCORE = ", score)
        quit()
    
    if x == appleX and y == appleY:
        score += 1
        appleX = random.randint(0, grid_x - 1)
        appleY = random.randint(0, grid_y - 1)
        while(appleX == x and appleY == y):
            appleX = random.randint(0, grid_x - 1)
            appleY = random.randint(0, grid_y - 1)
        grid = []
        for a in range(grid_y):
            array = []
            for b in range(grid_x):
                if a == y and b == x:
                    array.append(player)
                elif a == appleY and b == appleX:
                    array.append(apple)
                else:
                    array.append(background)
            grid.append(array)

    for a in range (len(grid)):
        for b in range (len(grid[0])):
            print(grid[a][b], end = "")
        print("")
    print("SCORE = ", score)

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