import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

# Load images
mickey_body_image = pygame.image.load(r"C:\Users\Алина\Desktop\пп2\PP2\lab 7\images\images\mainclock.png")
minutes_hand_image = pygame.image.load(r"C:\Users\Алина\Desktop\пп2\PP2\lab 7\images\images\rightarm.png")
seconds_hand_image = pygame.image.load(r"C:\Users\Алина\Desktop\пп2\PP2\lab 7\images\images\leftarm.png")

mickey_rect = mickey_body_image.get_rect(center=(screen_width // 2, screen_height // 2))

def draw_rotated_image(image, angle, position):
    """Draw the rotated image on the screen."""
    # Note: Pygame rotates clockwise, but we adjust the angle for counterclockwise rotation.
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=position)
    screen.blit(rotated_image, new_rect.topleft)

def get_hand_angle(hand_type):
    """Calculate the rotation angle for the minute or second hand."""
    current_time = datetime.now().time()
    if hand_type == 'minutes':
        # Adjusting for the fact that 0 degrees should be at the top (-90 degrees correction).
        return ((current_time.minute + current_time.second / 60) / 60) * 360
    elif hand_type == 'seconds':
        return (current_time.second / 60) * 360

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(mickey_body_image, mickey_rect)

        # Calculate angles for minute and second hands
        minutes_angle = get_hand_angle('minutes')
        seconds_angle = get_hand_angle('seconds')

        # Rotate and draw hands
        draw_rotated_image(minutes_hand_image, minutes_angle - 90, mickey_rect.center)  # -90 to adjust the starting position
        draw_rotated_image(seconds_hand_image, seconds_angle - 90, mickey_rect.center)  # -90 to adjust the starting position

        pygame.display.flip()
        clock.tick(60)  # Update the display 60 times per second

if __name__ == "__main__":
    main()
