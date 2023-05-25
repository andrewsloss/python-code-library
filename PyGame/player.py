import pygame

pygame.init()

GAME_TITLE = "THE BEST GAME EVER MADE"
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
GRAVITY = 1
JUMP_HEIGHT = 20
X_VELOCITY, Y_VELOCITY = 15, JUMP_HEIGHT
X_RECTANGLE, Y_RECTANGLE = 50, 50
TOLERANCE = 10
bool_gravity = True
jumping = False

pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + (Y_RECTANGLE / 2)))
clock = pygame.time.Clock()
running = True

X_POSITION, Y_POSITION = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

player = pygame.Rect(X_POSITION, Y_POSITION, X_RECTANGLE, Y_RECTANGLE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    pygame.draw.rect(screen, "lightblue", player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jumping = True
    if keys[pygame.K_a]:
        player.x -= X_VELOCITY
    if keys[pygame.K_d]:
        player.x += X_VELOCITY

    if jumping:
        player.y -= Y_VELOCITY
        Y_VELOCITY -= GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            player.y = SCREEN_HEIGHT - (Y_RECTANGLE / 2)
            Y_VELOCITY = JUMP_HEIGHT
            jumping = False

    if bool_gravity and not(jumping):
        player.y += Y_VELOCITY
        Y_VELOCITY += GRAVITY
        if player.y >= SCREEN_HEIGHT - (Y_RECTANGLE / 2):
            player.y = SCREEN_HEIGHT - (Y_RECTANGLE / 2)
            Y_VELOCITY = JUMP_HEIGHT
            bool_gravity = False
        
    if player.left >= SCREEN_WIDTH:
        player.x = 0
    if player.right <= 0:
        player.x = SCREEN_WIDTH - X_RECTANGLE

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()