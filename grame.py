import sys
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Screen with Text in a Rectangle")

COLOR_BACKGROUND = (30, 30, 40)
COLOR_RECT = (52, 152, 219)
COLOR_TEXT = (255, 255, 255)

game_rect = pygame.Rect(250, 225, 300, 150)

game_font = pygame.font.SysFont(None, 36)
text_surface = game_font.render("Play Game", True, COLOR_TEXT)

text_rect = text_surface.get_rect()
text_rect.center = game_rect.center

clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill(COLOR_BACKGROUND)
    pygame.draw.rect(screen, COLOR_RECT, game_rect)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
