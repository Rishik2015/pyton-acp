import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Space Invaders") 

# Define colors
BLUE = (0, 0, 255) # 

try:
    player_img = pygame.image.load('player.png')
except pygame.error as e:
    print(f"Error loading player.png: {e}")
    print("Please make sure 'player.png' is in the same directory as your script.")
    
    player_img = pygame.Surface((64, 64)) 
    player_img.fill((0, 255, 0)) 
    print("Using a green square as a placeholder for the player.")

player_x = 370 
player_y = 480 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)

    
    screen.blit(player_img, (player_x, player_y))

    
    pygame.display.flip()

pygame.quit()