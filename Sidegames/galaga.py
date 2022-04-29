#
# Galaga Game
# @MyronTruesdale
# Version @4/20/20
#

# imports
import pygame
import random
import math

# import pygame.locals for easier access to keys
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initialize pygame
pygame.init()

# naming the window
pygame.display.set_caption('Galaga.py')

# screen sizing
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(center=(30,int(SCREEN_HEIGHT/2)))
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

        # keep player onscreen
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH
        if (self.rect.top <= 0):
            self.rect.top = 0
        if (self.rect.bottom >= SCREEN_HEIGHT):
            self.rect.bottom = SCREEN_HEIGHT

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
                random.randint(0,SCREEN_HEIGHT))
            )
        self.speed = random.randint(5, 20)
        
        # movement based on speed
        # removes sprite when it passes left edge
        def update(self):
            print('enemy moved')
            self.rect.move_ip(-self.speed, 0)
            if (self.rect.right < 0):
                print('killing enemy')
                self.kill()

# screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# custom event for adding enemies
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# instantiate player
player = Player()

# creating groups to hold enemy sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# clock for framerate
clock = pygame.time.Clock()

# running variable
running = True

# running loop
while running:

    # for quitting
    breaker = False
    
    # look at all the events in game
    for event in pygame.event.get():
        # check if the event is a key
        if (event.type == KEYDOWN):
            # check for different keys
            if (event.key == K_ESCAPE):
                running = False
                pygame.quit()
                breaker = True
        elif (event.type == QUIT):
            running = False
            pygame.quit()
            breaker = True
        # new enemy being added?
        elif (event.type == ADDENEMY):
            # create the enemy
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # performs closure
    if (breaker == True):
        break
    
    # get keys pressed and check user input
    pressed_keys = pygame.key.get_pressed()
    # update player position
    player.update(pressed_keys)

    # update enemy
    enemies.update()
    
    # screen coloring
    screen.fill((255,255,255))
    

    # draw everything
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if (pygame.sprite.spritecollideany(player, enemies)):
        # kill the player
        player.kill()
        running = False

    # applies changes to the screen
    pygame.display.flip()

    clock.tick(30)
