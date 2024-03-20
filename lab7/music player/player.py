import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 220))
pygame.display.set_caption("privet")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, size=70)

sounds = {i[:-4]: pygame.mixer.Sound(f'sounds/{i}') for i in os.listdir('sounds')}
current_sound = 0
now_plays = current_sound
sound_names = tuple(sounds.keys())
mati = pygame.font.SysFont(None, 25).render("осторожно маты", True, (255, 0, 0))
instructions = pygame.font.SysFont(None, 23).render("| space - stop | enter - play | right/left arrows - change sound |", True, (0, 255, 0))
program = True
while program:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program = False
        screen.fill((30, 30, 30))
        screen.blit(font.render(sound_names[current_sound], True, (255, 255, 255)), (20, 80))
        pygame.display.flip()
        if current_sound in (5, 8, 7):
            screen.blit(mati, (5, 5))
        screen.blit(instructions, (5, 200))
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if current_sound < len(sounds)-1:
                    current_sound += 1
                else:
                    current_sound = 0
            if event.key == pygame.K_LEFT:
                if current_sound == 0:
                    current_sound = 8
                else:
                    current_sound -= 1
            if event.key == pygame.K_RETURN:
                if current_sound != now_plays:
                    sounds[sound_names[now_plays]].stop()
                now_plays = current_sound
                if sounds[sound_names[current_sound]].play().get_busy():
                    sounds[sound_names[current_sound]].stop()
                sounds[sound_names[current_sound]].play()
            if event.key == pygame.K_SPACE:
                sounds[sound_names[now_plays]].stop()
pygame.quit()
exit()