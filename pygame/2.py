import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
musics = ["eee.mp3","hhh.mp3", "xxx.mp3" ]
a = 0
l = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()


    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (123, 233, 123), pygame.Rect(200, 150, 20, 20))
    pressed = pygame.key.get_pressed()
    print(a)
    if pressed[pygame.K_LEFT]:
        if a != 0:
            a -=1

        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]:
        if a != len(musics)-1:
            a +=1
        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
    pygame.display.flip()
    clock.tick(5)