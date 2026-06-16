import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Shooter")

player = pygame.Rect(280, 350, 40, 20)
bullets = []
enemies = []
score = 0

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - 2, player.y, 5, 10))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += 5

    for bullet in bullets[:]:
        bullet.y -= 7
        if bullet.y < 0:
            bullets.remove(bullet)

    if random.randint(1, 30) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - 30), 0, 30, 30))

    for enemy in enemies[:]:
        enemy.y += 3

        if enemy.y > HEIGHT:
            enemies.remove(enemy)

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                if enemy in enemies:
                    enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 1
                break

    screen.fill((20, 20, 30))

    pygame.draw.rect(screen, (0, 255, 0), player)

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()