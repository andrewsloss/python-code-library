import pygame

pygame.init()
GAME_TITLE = "THE BEST GAME EVER MADE"
pygame.display.set_caption(GAME_TITLE)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

Y_GRAVITY = 1
JUMP_HEIGHT = 20

X_VELOCITY = 10
Y_VELOCITY = 20

X_RECTANGLE = 50
Y_RECTANGLE = 50

OBJ_WIDTH = 1000
OBJ_HEIGHT = 25

gravity = True
jumping = False

playerPos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
player = pygame.Rect(playerPos.x, playerPos.y, X_RECTANGLE, Y_RECTANGLE)
objectPos = pygame.Vector2((SCREEN_WIDTH - OBJ_WIDTH) / 2, SCREEN_HEIGHT - 100)
object1 = pygame.Rect(objectPos.x, objectPos.y, OBJ_WIDTH, OBJ_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    x = playerPos.x + X_RECTANGLE / 2
    y = playerPos.x + X_RECTANGLE / 2
    xy = pygame.Vector2(x, y)
    
    player.center = xy
    object1.bottomleft = objectPos
    pygame.draw.rect(screen, "lightblue", player)
    pygame.draw.rect(screen, "white", object1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jumping = True
    if keys[pygame.K_a]:
        playerPos.x -= X_VELOCITY
    if keys[pygame.K_d]:
        playerPos.x += X_VELOCITY

    if jumping:
        playerPos.y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if gravity == False:
            Y_VELOCITY = JUMP_HEIGHT
            jumping = False

    if gravity and jumping == False:
        playerPos.y += Y_VELOCITY
        Y_VELOCITY += 1
        if gravity == False:
            Y_VELOCITY = JUMP_HEIGHT

    if player.colliderect(object1):
        gravity = False
        Y_VELOCITY = JUMP_HEIGHT
        playerPos.y = objectPos.y - Y_RECTANGLE
    else:
        gravity = True

    pygame.display.update()

    clock.tick(60)

pygame.quit()
#print(f"{playerPos.y} {objectPos.y - OBJ_HEIGHT}")