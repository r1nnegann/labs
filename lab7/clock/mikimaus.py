import pygame
from datetime import datetime
from time import sleep


def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # rotated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # rotated image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


pygame.init()

clocks = pygame.image.load("mainclock.png")
minutes = pygame.image.load('minutes.png')
seconds = pygame.image.load('seconds.png')

screen = pygame.display.set_mode(clocks.get_size())

w, h = seconds.get_size()
minutes_pos = ((screen.get_width() / 2), (screen.get_height() / 2))
seconds_pos = ((screen.get_width() / 2), (screen.get_height() / 2))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    now = datetime.now()

    current_second = now.second+now.microsecond/1000000
    seconds_angle = current_second * 6

    minute_angle = (datetime.now().minute*6)+(seconds_angle / 60)

    screen.blit(clocks, (0, 0))
    blitRotate(screen, seconds, seconds_pos, ((w / 2) - 13, (h / 2) + 125), -seconds_angle)
    blitRotate(screen, minutes, minutes_pos, ((w / 2), (h / 2) + 75), -minute_angle)
    sleep(0.05)

    pygame.display.flip()

pygame.quit()
exit()