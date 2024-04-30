import pygame
import time
import random
import psycopg2
pygame.init()

score = 0
level = 0

conn = psycopg2.connect("postgres://salman:C27w35dr7yZuPeSyg5HSL9C52txPjBU4@dpg-coipqan79t8c738lbhug-a.frankfurt-postgres.render.com/phonebook_and_snake", sslmode='require')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS snakegame (
    username VARCHAR(255),
    user_score INT,
    user_level INT
);
""")


def get_user_level(username):
    cur.execute("SELECT user_level FROM snakegame WHERE username = %s", (username,))
    level = cur.fetchone()
    return level[0] if level else 1

def get_all_data():
    cur.execute("SELECT * FROM snakegame ORDER BY user_score DESC")
    rows = cur.fetchall()
    for row in rows:
        print(f"Username = {row[0]} Score = {row[1]} Level = {row[2]}")

def get_user_score(username):
    cur.execute("SELECT user_score FROM snakegame WHERE username = %s", (username,))
    score = cur.fetchone()
    return score[0] if score else 1

def save_game_state(username, score, level):
    cur.execute("INSERT INTO snakegame (username, user_score, user_level) VALUES (%s, %s, %s)", (username, score, level))
    conn.commit()

def update_game_state(username, score, level):
    cur.execute("UPDATE snakegame SET user_score = %s, user_level = %s WHERE username = %s", (score, level, username))
    conn.commit()




def get_nickname():
    DISPLAYSURF = pygame.display.set_mode((400,600))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)         

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

                        # Display the title
 

        DISPLAYSURF.fill((30, 30, 30))
        txt_surface = font_small.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        DISPLAYSURF.blit(txt_surface, (input_box.x+5, input_box.y+5))

        title = font_small.render("Input your nickname: ", True, (0, 255, 0))
        DISPLAYSURF.blit(title, (10, 50))
        pygame.draw.rect(DISPLAYSURF, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

    return text


NICKNAME = get_nickname()

cur.execute("SELECT count(*) FROM snakegame WHERE username='{}'".format(NICKNAME))
if cur.fetchone()[0]==0:
    save_game_state(NICKNAME, 0, 0)
    conn.commit()
else:
    cur.execute("SELECT * FROM snakegame WHERE username='{}'".format(NICKNAME))
    data=cur.fetchone()
    print("User's max score:{}".format(data[1]))
    print("User's max level:{}".format(data[2]))

    score = data[1]
    level = data[2]

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

blue = (50, 153, 213)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 102)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (100, 40, 40)

size_of_snake_block = 10

clock = pygame.time.Clock()

font1 = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 30)

def print_level(level):
    text = font2.render("Your Level: " + str(level), True, yellow)
    screen.blit(text, (200, 0))

def print_score(score):
    text = font2.render("Your Score: " + str(score), True, yellow)
    screen.blit(text, (0, 0))

def print_message(message, color):
    text = font1.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, text_rect)

def give_random_color(list_of_colors):
    random_color = random.choice(list_of_colors)
    return random_color

def timer(start_time):
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 5:
        return True
    else:
        return False

def snake(size_of_snake_block, snake_list):
    for i in snake_list:
        x = i[0]
        y = i[1]
        pygame.draw.rect(screen, green, (x, y, size_of_snake_block, size_of_snake_block))


class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, yellow, (self.x, self.y, self.width, self.height))


def generate_walls(level):
    walls = []
    for i in range(level):
        x = random.randint(0, (screen_width - size_of_snake_block) // size_of_snake_block) * size_of_snake_block
        y = random.randint(0, (screen_height - size_of_snake_block) // size_of_snake_block) * size_of_snake_block
        width = random.randint(1, 5) * size_of_snake_block
        height = random.randint(1, 5) * size_of_snake_block
        walls.append(Wall(x, y, width, height))
    return walls

def generate_food(walls):
    while True:
        food_x = round(random.randrange(size_of_snake_block, screen_width - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(40, screen_height - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0
        
        for wall in walls:
            if not any(wall.x <= food_x < wall.x + wall.width and wall.y <= food_y < wall.y + wall.height for wall in walls):
                return food_x, food_y




def game_loop():
    game_paused = False
    game_over = False

    color_is_given = False

    timer_is_started = False

    x = screen_width // 2
    y = screen_height // 2

    x_change = 0
    y_change = 0

    global score, level
 

    snake_speed = 10 + level // 3

    colors = [red, white]

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(size_of_snake_block, screen_width - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(40, screen_height - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0

    inc_speed = pygame.USEREVENT + 1
    pygame.time.set_timer(inc_speed, 5000)

    walls = generate_walls(level)


    while not game_over:
        while game_paused == True:
            screen.fill(black)
            print_message("You Lost! Press Q-Quit or P-Play Again", red)
            text = font1.render("Click S to save the game", True, green)
            screen.blit(text, (260, 290))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_paused = False
                        
                    elif event.key == pygame.K_p:
                        game_loop()

                    elif event.key == pygame.K_s:
                        update_game_state(NICKNAME, score, level)
                        print(NICKNAME, score, level, "paused")
                    
           
           
                    

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                elif event.key == pygame.K_LEFT:
                    x_change = -size_of_snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = size_of_snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -size_of_snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = size_of_snake_block
            if event.type == inc_speed and level == 10:
                    snake_speed += 2

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_paused = True


        x += x_change
        y += y_change

        screen.fill(black)

        for wall in walls:
            wall.draw(screen)


        if color_is_given == False:
            random_color = give_random_color(colors)
            color_is_given = True
            if random_color == red:
                start_time = time.time()
                timer_is_started = True

        pygame.draw.rect(screen, random_color, (food_x, food_y, size_of_snake_block, size_of_snake_block))

        snake_list.append((x, y))

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == (x, y):
                game_paused = True

        snake(size_of_snake_block, snake_list)

        print_score(score)

        print_level(level)

        pygame.display.update()

        if timer_is_started:
            if timer(start_time):
                food_x, food_y = generate_food(walls)
                timer_is_started = False
                color_is_given = False

        if x == food_x and y == food_y:
            food_x = round(random.randrange(size_of_snake_block, screen_width - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(40, screen_height - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0
            length_of_snake += 1
            if random_color == white:
                score += 1
            elif random_color == red:
                score += 2

            if score >= 3 * level:
                level += 1
                snake_speed += 0.5
                walls = generate_walls(level)


            color_is_given = False
            timer_is_started = False

        for wall in walls:
            if wall.x <= x < wall.x + wall.width and wall.y <= y < wall.y + wall.height:
                game_paused = True



        clock.tick(snake_speed)

    pygame.quit()
    quit()

get_all_data()

game_loop()
