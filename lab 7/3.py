import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Moving Ball')

# Ball settings
ball_color = (255, 0, 0)  # Red
ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2  # Starting position in the middle
move_distance = 20  # Distance to move each time

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_radius, ball_y - move_distance)
            elif event.key == pygame.K_DOWN:
                ball_y = min(screen_height - ball_radius, ball_y + move_distance)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_radius, ball_x - move_distance)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(screen_width - ball_radius, ball_x + move_distance)
    
    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
