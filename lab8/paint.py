import pygame


def rect(screen):
    x_local, y_local = x, y
    width, height = x2-x, y2-y
    if x2 < x:
        x_local = x2
        width = x - x2
    if y2 < y:
        y_local = y2
        height = y - y2

    pygame.draw.rect(screen, colors[current_color], (x_local, y_local, width, height), width=3)

def circle(screen):
    pygame.draw.circle(screen, colors[current_color], (x,y), radius=((x2-x)**2+(y2-y)**2)**0.5, width=3)

def eraser(screen):
    pygame.draw.circle(screen_work, (0, 0, 0), (x2, y2), radius=10)
    #global x, y, x2, y2
    #pygame.draw.line(screen_work, (0, 0, 0), (x, y), (x2, y2), width=20)
    #x, y = x2, y2


pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen_work = pygame.Surface(screen.get_size())
instruments = pygame.Surface((295, 50))
pygame.draw.rect(instruments, (255, 255, 255), (5, 5, 40, 40), width=3)
pygame.draw.circle(instruments, (255, 255, 255), (75, 25), radius=20, width=3)
pygame.draw.rect(instruments, (255, 255, 255), (105, 5, 30, 40), width=0)
pygame.draw.rect(instruments, (200, 0, 0), (105, 5, 30, 15))
pygame.draw.rect(instruments, (255, 0, 0), (145, 5, 40, 40))
pygame.draw.rect(instruments, (0, 255, 0), (195, 5, 40, 40))
pygame.draw.rect(instruments, (0, 0, 255), (245, 5, 40, 40))

colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
current_color = 'red'
modes = {'rect':rect, 'circle':circle, 'eraser':eraser}
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
            if 145 <= x <= 285 and 755 <= y <= 800:
                if x<190:
                    current_color = 'red'
                elif x<240:
                    current_color = 'green'
                else:
                    current_color = 'blue'
            elif 0 <= x <= 145 and 755 <= y <= 800:
                if x<50:
                    current_mode = 'rect'
                elif x<100:
                    current_mode = 'circle'
                else:
                    current_mode = 'eraser'

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
