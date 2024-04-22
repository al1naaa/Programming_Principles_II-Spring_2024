import psycopg2
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()





conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Aa1234"
)

cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100)
        );
    """)

cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            user_id SERIAL PRIMARY KEY,
            score INTEGER
        );
    """)
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(20, (window_y // 10)) * 10]

# fruit2 position (initially off-screen)
fruit_position2 = (-10, -10)

# Flag to control the appearance of fruit2
fruit2_visible = False

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# Set the initial time when the last fruit2 appeared
last_fruit2_time = time.time()

# Function to handle fruit2 appearance logic
def handle_fruit2():
    global fruit2_visible, last_fruit2_time, fruit_position2

    current_time = time.time()
    # If fruit2 is not visible and 10 seconds have passed since the last appearance
    if not fruit2_visible and current_time - last_fruit2_time >= 10:
        fruit_position2 = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]
        fruit2_visible = True
        last_fruit2_time = current_time
    # If fruit2 is visible and 10 seconds have passed since its last appearance
    elif fruit2_visible and current_time - last_fruit2_time >= 10:
        fruit_position2 = (-10, -10)  # Off-screen
        fruit2_visible = False
        last_fruit2_time = current_time

# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # after 2 seconds we will quit the program
    time.sleep(2)
    # deactivating pygame library
    pygame.quit()
    # quit the program
    quit()

def save_game_result(user_name, score):
    # Проверяем, существует ли пользователь в базе данных
    cur.execute("SELECT user_id FROM users WHERE username = %s", (user_name,))
    existing_user = cur.fetchone()
    if existing_user:
        user_id = existing_user[0]
    else:
        # Если пользователя нет, добавляем его в таблицу
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (user_name,))
        user_id = cur.fetchone()[0]

    # Сохраняем результат игры с привязкой к пользователю
    cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
    conn.commit()



# Запрашиваем имя игрока перед началом игры
user_name = input("Введите ваше имя: ")

# Main Function
while True:
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
            # Сохраняем результаты игры перед выходом
                save_game_result(user_name, score)
                pygame.quit()
                quit()
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        snake_speed += 2
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    elif (snake_position[0] == fruit_position2[0] and snake_position[1] == fruit_position2[1]) or (snake_position[0] == fruit_position2[0] and snake_position[1] == fruit_position2[1]+10) or (snake_position[0] == fruit_position2[0] and snake_position[1] == fruit_position2[1]-10) or (snake_position[0] == fruit_position2[0]+10 and snake_position[1] == fruit_position2[1])  or (snake_position[0] == fruit_position2[0]-10 and snake_position[1] == fruit_position2[1])  :
        score += 15
        snake_speed += 2
        fruit_position2 = (-10, -10)  # Make fruit2 disappear
        fruit2_visible = False
    else:
        snake_body.pop()

    # Check and handle fruit2 appearance logic
    handle_fruit2()

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    if fruit2_visible:
        pygame.draw.circle(game_window, white, (fruit_position2[0], fruit_position2[1]), 10)

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 or \
            snake_position[1] < 0 or snake_position[1] > window_y - 10 or \
            any(snake_position == block for block in snake_body[1:]):
        save_game_result(user_name, score)
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)