# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
co = 0
lev = 0
new_level_num = 10
level_num_before = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
pygame.mixer.music.load("xxx.mp3")
pygame.mixer.music.play()

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# logic of enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(0,2000))
        # creating enemy

    def move(self): # logic of move of enemy
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(0,2000))
class coin(pygame.sprite.Sprite): # logic of coin
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pngegg (4).png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(0,1000))

    def move(self): # logic of move of coin
        self.rect.move_ip(0, SPEED + random.randint(0, 2))
        if (self.rect.top > 600):

            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(0,1000))
    def fell(self): # creating coin after earning coin
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(0,1000))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:

                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)



# Setting up Sprites
P1 = Player()
E1 = Enemy()
E2 = Enemy()
coin = coin()


# Creating Sprites Groups
Coins = pygame.sprite.Group()
Coins.add(coin)
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(E2)
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)



# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins = font_small.render("Coins: "+str(co), True, BLACK)
    level = font_small.render("level: " +str(lev), True, BLACK )
    DISPLAYSURF.blit(level, (150,10))
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins, (250, 10))


    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.pause()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        # экран пройгрыша
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    a = co % (new_level_num + level_num_before)
    if a <= 4:
        if pygame.sprite.spritecollideany(P1, Coins):
            coin.fell()
            co += 5
            lev += 1
            SPEED += 1
            level_num_before = new_level_num
            new_level_num +=10

    else:
        if pygame.sprite.spritecollideany(P1, Coins):
            coin.fell()
            co += random.randint(1,5)

    pygame.display.update()
    FramePerSec.tick(FPS)