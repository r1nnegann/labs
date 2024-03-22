import pygame
import random

def interpolate(start_color, end_color, factor: float):
    r = start_color[0] + (end_color[0] - start_color[0]) * factor
    g = start_color[1] + (end_color[1] - start_color[1]) * factor
    b = start_color[2] + (end_color[2] - start_color[2]) * factor
    return int(r), int(g), int(b)

def generate_rainbow_gradient(colors, steps):
    gradient = []
    for i in range(len(colors) - 1):
        start_color = colors[i]
        end_color = colors[i + 1]
        for step in range(steps):
            factor = step / steps
            gradient.append(interpolate(start_color, end_color, factor))
    return gradient

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()
rainbow_colors = [
    (255, 105, 180),  # Ярко-розовый
    (255, 69, 0),     # Огненно-оранжевый
    (255, 215, 0),    # Золотой
    (124, 252, 0),    # Лужайково-зеленый
    (0, 255, 127),    # Весенне-зеленый
    (64, 224, 208),   # Бирюзовый
    (70, 130, 180),   # Стальной синий
    (0, 191, 255),    # Глубокий небесно-голубой
    (138, 43, 226),   # Сине-фиолетовый
    (75, 0, 130),     # Индиго
    (148, 0, 211),    # Фиолетовый
    (255, 20, 147),   # Глубокий розовый
    (255, 160, 122),  # Светлый лососевый
    (255, 105, 180),  # Розовый
    (255, 165, 0),    # Оранжевый
    (255, 255, 0),    # Ярко-желтый
    (0, 255, 0),      # Лайм
    (0, 255, 255),    # Аква
    (0, 0, 255),      # Синий
    (255, 0, 255),    # Малиновый
    (255, 192, 203),  # Розовый пудра
    (255, 20, 147)    # Ярко-розовый
]

gradient = generate_rainbow_gradient(rainbow_colors, 40)
gradient_len = len(gradient)
program = True
color_index = 0

x, y = 400, 400

while program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += 20
        if x > 1500:
            x = 1500
    if keys[pygame.K_LEFT]:
        x -= 20
        if x < 0:
            x = 0
    if keys[pygame.K_DOWN]:
        y += 20
        if y > 1000:
            y = 1000
    if keys[pygame.K_UP]:
        y -= 20
        if y < 0:
            y = 0

    screen.fill((0, 0, 0))
    if color_index < gradient_len:
        color = gradient[color_index]
    else:
        color_index = 0

    pygame.draw.circle(screen, color, (x, y), 25)
    pygame.display.flip()


    color_index += 1
    clock.tick(60)

pygame.quit()
