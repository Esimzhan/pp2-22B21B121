import pygame
import sys
import os
fps = pygame.time.Clock()
def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)
def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect
pygame.init()
sc = pygame.display.set_mode((1200, 720))
bird = pygame.image.load("bird (1).png")
bird.convert()
ball = pygame.image.load("ball.png")
clock =  pygame.image.load("pngegg.png")
min = pygame.image.load("mint.png")
rect = clock.get_rect()
rect.center= (1200 / 2, 720 / 2)
sc.fill((255, 255, 255))
sc.blit(clock,rect)
a = -6
b = -6
rotated = pygame.transform.rotate(min, -(6 + b))
re = rotated.get_rect(center=min.get_rect(center=(600, 360)).center)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    press = pygame.key.get_pressed()
    sc.fill((255, 255, 255))
    sc.blit(clock, rect)
    a += 6
    rotated_image = pygame.transform.rotate(bird, -(6+a))
    rec = rotated_image.get_rect(center=bird.get_rect(center=(600, 360)).center)
    sc.blit(rotated_image, rec)
    if a % 360 == 0 :
        rotated = pygame.transform.rotate(min, -(6 + b))
        re = rotated.get_rect(center=min.get_rect(center=(600, 360)).center)
        b += 6
    sc.blit(rotated, re)
    fps.tick(1)
    pygame.display.flip()