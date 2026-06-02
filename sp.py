import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, up_key, down_key):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.up_key = up_key
        self.down_key = down_key

    def update(self, keys):
        if keys[self.up_key]:
            self.rect.y -= 5
        if keys[self.down_key]:
            self.rect.y += 5

sprite1 = Player((255, 0, 0), 200, 250, pygame.K_w, pygame.K_s)
sprite2 = Player((0, 0, 255), 500, 250, pygame.K_UP, pygame.K_DOWN)
all_sprites = pygame.sprite.Group(sprite1, sprite2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    screen.fill((240, 240, 240))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
