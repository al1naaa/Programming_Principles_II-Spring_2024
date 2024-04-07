import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
dis_width = 600
dis_height = 400

# Setup display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake properties
snake_block = 10
initial_snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score and level
def Your_score(score, level):
    value = score_font.render("Score: " + str(score) + " Level: " + str(level), True, yellow)
    dis.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to ensure food does not spawn on the snake
def food_on_snake(foodx, foody, snake_list):
    if [foodx, foody] in snake_list:
        return True
    return False

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake initial position
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Movement changes
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Initial speed and level
    snake_speed = initial_snake_speed
    level = 1

    # Generate initial position for food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # Food weight (size) varies between 1 to 3 blocks
    food_weight = random.randint(1, 3)
    # Food timer
    food_timer = time.time() + 5  # 5 seconds until the food disappears

    # Ensure food is not spawned on the snake
    while food_on_snake(foodx, foody, snake_List):
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for border collision
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Check if food timer has expired, generate new food if so
        if time.time() > food_timer:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # Ensure new food is not on the snake
            while food_on_snake(foodx, foody, snake_List):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            food_weight = random.randint(1, 3)  # Randomize new food weight
            food_timer = time.time() + 5  # Reset food timer

        # Draw food with varying size based on its weight
        for i in range(food_weight):
            pygame.draw.rect(dis, green, [foodx + (snake_block * i), foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for self collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)

        pygame.display.update()

        # Check for food collision
        if x1 == foodx and y1 == foody:
            Length_of_snake += food_weight  # Increase snake length by food weight
            food_timer = 0  # Immediately trigger new food generation

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
