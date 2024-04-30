import pygame


def rect(screen):
    x_local, y_local = x, y
    width, height = x2 - x, y2 - y
    if x2 < x:
        x_local = x2
        width = x - x2
    if y2 < y:
        y_local = y2
        height = y - y2

    pygame.draw.rect(screen, colors[current_color], (x_local, y_local, width, height), width=3)


def circle(screen):
    pygame.draw.circle(screen, colors[current_color], (x, y), radius=((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5, width=3)


def eraser(screen):
    pygame.draw.circle(screen_work, (0, 0, 0), (x2, y2), radius=10)
    # global x, y, x2, y2
    # pygame.draw.aaline(screen_work, (0, 0, 0), (x, y), (x2, y2), width=20)
    # x, y = x2, y2


def square(screen):
    x_local, y_local = x, y
    width = x2 - x
    if x2 < x:
        x_local = x2
        width = x - x2
    if y2 < y:
        y_local = y2

    pygame.draw.rect(screen, colors[current_color], (x_local, y_local, width, width), width=3)


def equilateral_triangle(screen):
    pygame.draw.polygon(screen, colors[current_color], [(x2 - 50, y2 + 50), (x2, y2), (x2 + 50, y2 + 50)])


def right_triangle(screen):
    pygame.draw.polygon(screen, colors[current_color], [(x2, y2), (x2 + 50, y2), (x2, y2 - 50)])


def rhombus(screen):
    pygame.draw.polygon(screen, colors[current_color],
                        [(x2 - 30, y2 + 20), (x2, y2), (x2 + 30, y2 + 20), (x2, y2 + 40)])


pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen_work = pygame.Surface(screen.get_size())
instruments = pygame.Surface((500, 50))
pygame.draw.rect(instruments, (180, 180, 180), (0, 0, 500, 50))
pygame.draw.rect(instruments, (255, 255, 255), (10, 5, 30, 40), width=3)
pygame.draw.circle(instruments, (255, 255, 255), (75, 25), radius=20, width=3)
pygame.draw.rect(instruments, (255, 255, 255), (105, 5, 30, 40), width=0)
pygame.draw.rect(instruments, (200, 0, 0), (105, 5, 30, 15))
pygame.draw.polygon(instruments, (255, 255, 255), [(195, 45), (190 + 45, 45), (195, 5)])
pygame.draw.rect(instruments, (255, 0, 0), (345, 5, 40, 40))
pygame.draw.rect(instruments, (0, 255, 0), (395, 5, 40, 40))
pygame.draw.rect(instruments, (0, 0, 255), (445, 5, 40, 40))
pygame.draw.rect(instruments, (255, 255, 255), (145, 5, 40, 40), width=3)
pygame.draw.polygon(instruments, (255, 255, 255), [(250, 45), (265, 5), (285, 45)])
pygame.draw.polygon(instruments, (255, 255, 255), [(290, 25), (315, 5), (340, 25), (315, 45)])

colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
current_color = 'red'
modes = {'rect': rect, 'circle': circle, 'eraser': eraser, "square": square, "triangle": right_triangle,
         'triangle2': equilateral_triangle, 'rhombus': rhombus}
current_mode = 'rect'
clock = pygame.time.Clock()
x, y, x2, y2 = -1, -1, -1, -1

program = True
while program:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if 0 <= x <= 450 and 755 <= y <= 800:
                if x < 50:
                    current_mode = 'rect'
                elif x < 100:
                    current_mode = 'circle'
                elif x < 150:
                    current_mode = 'eraser'
                elif x < 195:
                    current_mode = 'square'
                elif x < 245:
                    current_mode = 'triangle'
                elif x < 290:
                    current_mode = "triangle2"
                elif x < 340:
                    current_mode = "rhombus"
                elif x < 390:
                    current_color = 'red'
                elif x < 440:
                    current_color = 'green'
                elif x < 500:
                    current_color = 'blue'

            x2, y2 = x, y
        if pygame.mouse.get_pressed()[0]:
            x2, y2 = pygame.mouse.get_pos()
            screen.blit(screen_work, (0, 0))
            modes[current_mode](screen)
            screen.blit(instruments, (0, 750))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            modes[current_mode](screen_work)
    screen.blit(instruments, (0, 750))
    pygame.display.flip()
