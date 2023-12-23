import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bg.jpg')
spaceship_img = pygame.image.load('spaceship.png')
alien_img = pygame.image.load('alien.png')
bullet_img = pygame.image.load('bullet.png')

spaceshipX = 370
spaceshipY = 480
spaceship_speed = 5
changeX = 0

alienX = random.randint(0, 736)
alienY = random.randint(30, 150)
alien_speedX = -1
alien_speedY = 10

bulletX = 0
bulletY = 490
bullet_speed = 5
bullet_state = "ready"

running = True

def draw_spaceship(x, y):
    screen.blit(spaceship_img, (x, y))

def draw_alien(x, y):
    screen.blit(alien_img, (x, y))

def draw_bullet(x, y):
    screen.blit(bullet_img, (x, y))

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -spaceship_speed
            elif event.key == pygame.K_RIGHT:
                changeX = spaceship_speed
            elif event.key == pygame.K_RETURN:
                if bullet_state == "ready":
                    bulletX = spaceshipX + 16
                    bulletY = spaceshipY
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0

    spaceshipX += changeX

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736

    alienX += alien_speedX
    if alienX <= 0 or alienX >= 736:
        alien_speedX = -alien_speedX
        alienY += alien_speedY

    if bullet_state == "fire":
        draw_bullet(bulletX, bulletY)
        bulletY -= bullet_speed

        if bulletY <= 0:
            bullet_state = "ready"

    draw_spaceship(spaceshipX, spaceshipY)
    draw_alien(alienX, alienY)

    pygame.display.update()