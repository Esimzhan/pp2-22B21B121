import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
musics = ["Enzo — !Sugar crash ;; ElYotto - (slowed + reverbed) (www.lightaudio.ru).mp3","Gorgon Breath — Safe and Sound (www.lightaudio.ru).mp3", "XXXTENTACION — whoa (mind in awe) (8D Audio) (www.lightaudio.ru).mp3" ]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (123, 233, 123), pygame.Rect(200, 150, 20, 20))
    pressed = pygame.key.get_pressed()
    a = 0
    l = 0
    if pressed[pygame.K_LEFT]:
        if a != 0:
            a -=1
        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]:
        a += 1
        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
    if pressed[pygame.K_SPACE] and l % 2 == 0:
        pygame.mixer.music.pause()
        l += 1
    if pressed[pygame.K_SPACE] and l % 2 != 0:
        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
        l += 1
    pygame.display.flip()
    clock.tick(60)