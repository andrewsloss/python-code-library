import pygame

pygame.init()

GAME_TITLE = "THE BEST GAME EVER MADE"
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
GRAVITY = 1
JUMP_HEIGHT = 20
X_VELOCITY, Y_VELOCITY = 15, JUMP_HEIGHT
X_RECTANGLE, Y_RECTANGLE = 50, 50
bool_gravity = True
jumping = False

pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + (Y_RECTANGLE / 2)))
clock = pygame.time.Clock()
running = True

playerPos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
player = pygame.Rect(playerPos.x, playerPos.y, X_RECTANGLE, Y_RECTANGLE)

class objects:

    objectPos = None
    objectRect = None

    def __init__(self, x, y, width, height):
        self.objectPos = pygame.Vector2(x, y)
        self.objectRect = pygame.Rect(self.objectPos.x, self.objectPos.y, width, height)

    def __str__(self):
        return f"{self.objectPos.x} {self.objectPos.y}"

obj = objects(400, 600, 200, 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    player.center = playerPos
    pygame.draw.rect(screen, "lightblue", player)

    obj.objectRect.center = obj.objectPos
    pygame.draw.rect(screen, "white", obj.objectRect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jumping = True
    if keys[pygame.K_a]:
        playerPos.x -= X_VELOCITY
    if keys[pygame.K_d]:
        playerPos.x += X_VELOCITY

    if jumping:
        playerPos.y -= Y_VELOCITY
        Y_VELOCITY -= GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            Y_VELOCITY = JUMP_HEIGHT
            jumping = False

    if bool_gravity and not(jumping):
        playerPos.y += Y_VELOCITY
        Y_VELOCITY += GRAVITY
        if playerPos.y >= SCREEN_HEIGHT - (Y_RECTANGLE / 2):
            playerPos.y = SCREEN_HEIGHT
            Y_VELOCITY = JUMP_HEIGHT
            bool_gravity = False
    
    if player.colliderect(obj.objectRect):
        jumping = False
        bool_gravity = True
        

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()