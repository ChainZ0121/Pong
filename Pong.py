import pygame
import random
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
size = (1200, 600)
screen = pygame.display.set_mode (size)
pygame.display.set_caption('PONG')

px = 250
p2x = 250
bx = 600
by = 300
xchange1 = 0
xchange2 = 0
def p1():
    global px
    py = 45
    pw = 25
    pl = 120
    pygame.draw.rect(screen, white, [py, px, pw, pl])

def p2():
    global p2x
    by = 1127
    bw = 25
    bl = 120
    pygame.draw.rect(screen, white, [by, p2x, bw, bl])

def ball():
    global bx, by
    pygame.draw.ellipse(screen, white, [bx, by, 100, 100])

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                pause = True
            if event.key == pygame.K_s:
                xchange1 = 5
            if event.key == pygame.K_w:
                xchange1 = -5
            if event.key == pygame.K_UP:
                xchange2 = -5
            if event.key == pygame.K_DOWN:
                xchange2 = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                xchange1 = 0
            if event.key == pygame.K_s:
                xchange1 = 0
            if event.key == pygame.K_UP:
                xchange2 = 0
            if event.key == pygame.K_DOWN:
                xchange2 = 0
    if px <= 600 - 120 or px >= 0:
        px = px + xchange1
    else:
        px = px
    if p2x <= 600 - 120 or p2x >= 0:
        p2x = p2x + xchange2
    else:
        p2x = p2x
    screen.fill(black)
    p1()
    p2()
    ball()
    pygame.display.update()
    clock.tick(60)
