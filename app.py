import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_key):
        
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, 1)
        if (pressed_key[K_LEFT]):
            self.rect.move_ip(-1, 0)
        if (pressed_key[K_RIGHT]):
            self.rect.move_ip(1, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
                800,
                random.randint(0, 800)
            )
        )
        self.speed = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        
        if self.rect.right < 0:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        done = True

    pygame.display.flip()
        
    pass