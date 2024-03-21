import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600, 350))
pygame.display.set_caption("privet")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, size=100)
otchislenie_bool = False
sounds_otchislenie = {i[:-4]: pygame.mixer.Sound(f'otchislenie/{i}') for i in os.listdir('otchislenie')}
sounds_normal = {i[:-4]: pygame.mixer.Sound(f'sounds/{i}') for i in os.listdir('sounds')}
sounds = (sounds_normal, sounds_otchislenie)
current_sound = 0
now_plays = current_sound
sound_names = (tuple(sounds_normal), tuple(sounds_otchislenie.keys()))
mati = pygame.font.SysFont(None, 35).render("осторожно маты", True, (255, 0, 0))
mati2 = pygame.font.SysFont(None, 35).render("осторожно мощные маты", True, (255, 0, 0))
otchislenie = pygame.font.SysFont(None, 30).render("надеюсь не отчислят - F1", True, (0, 255, 0))
otchislenie2 = pygame.font.SysFont(None, 30).render("вернуться - F1", True, (0, 255, 0))
instructions = pygame.font.SysFont(None, 29).render("| space - stop | enter - play | right/left arrows - change sound |", True, (0, 255, 0))


program = True
while program:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program = False


        screen.fill((30, 30, 30))
        if not otchislenie_bool:
            screen.blit(otchislenie, (340, 5))
            if current_sound in (7,):
                screen.blit(mati, (5, 5))
        else:
            screen.blit(mati2, (5, 5))
            screen.blit(otchislenie2, (450, 5))


        screen.blit(font.render(sound_names[otchislenie_bool][current_sound], True, (255, 255, 255)), (20, 140))
        screen.blit(instructions, (5, 330))
        pygame.display.flip()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                if otchislenie_bool:
                    otchislenie_bool = False
                else:
                    otchislenie_bool = True


            if event.key == pygame.K_RIGHT:
                if current_sound < len(sounds[otchislenie_bool])-1:
                    current_sound += 1
                else:
                    current_sound = 0


            if event.key == pygame.K_LEFT:
                if current_sound == 0:
                    current_sound = len(sounds[otchislenie_bool])-1
                else:
                    current_sound -= 1


            if event.key == pygame.K_RETURN:
                if current_sound != now_plays:
                    sounds[otchislenie_bool][sound_names[otchislenie_bool][now_plays]].stop()
                now_plays = current_sound
                if sounds[otchislenie_bool][sound_names[otchislenie_bool][current_sound]].play().get_busy():
                    sounds[otchislenie_bool][sound_names[otchislenie_bool][current_sound]].stop()
                sounds[otchislenie_bool][sound_names[otchislenie_bool][current_sound]].play()


            if event.key == pygame.K_SPACE:
                sounds[otchislenie_bool][sound_names[otchislenie_bool][now_plays]].stop()
pygame.quit()
exit()