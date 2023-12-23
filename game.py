"""import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
bulletimg=pygame.image.load('bullet.png')
spaceshipX=370
spaceshipY=480
running=True
check=False
bulletX=386
bulletY=490
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.K_RETURN:
            if check is False:
                check=True
                bulletX=spaceshipX+16
                if bulletY<=0:
                    bullt=490
                    check=False
            if check is True:
                screen.blit(bulletimg,(370,480))
"""
    
            

"""import pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Load the bullet image
bullet_img = pygame.image.load('bullet.png')

# Set up initial positions
spaceshipX = 370
spaceshipY = 480
bulletX = 0  # Initialize bulletX
bulletY = 480  # Set the initial bulletY
bullet_state = "ready"  # Add a bullet state variable

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # K_RETURN represents the Enter key
                if bullet_state == "ready":
                    bulletX = spaceshipX + 16
                    bulletY = 480  # Set the initial position of the bullet
                    bullet_state = "fire"

    # Update bullet position if it's in the "fire" state
    if bullet_state == "fire":
        bulletY -= 5  # Adjust the speed of the bullet. You can modify this value.

        # Draw the bullet on the screen
        screen.blit(bullet_img, (bulletX, bulletY))

        # Check if the bullet has gone off the screen
        if bulletY <= 0:
            bullet_state = "ready"

    # Draw the spaceship on the screen
    screen.blit(spaceship_img, (spaceshipX, spaceshipY))

    # Update the display
    pygame.display.update()
"""

"""import pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Load the bullet image
bullet_img = pygame.image.load('bullet.png')

# Load the spaceship image
spaceship_img = pygame.image.load('spaceship.png')

# Set up initial positions
spaceshipX = 370
spaceshipY = 480
spaceship_speed = 5
bullet_speed = 7
bulletX = 0
bulletY = 480
bullet_state = "ready"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # K_RETURN represents the Enter key
                if bullet_state == "ready":
                    bulletX = spaceshipX + 16
                    bulletY = spaceshipY
                    bullet_state = "fire"

        # Check for key release events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if bullet_state == "fire":
                    bullet_state = "ready"

    # Check if the bullet is in the "fire" state and update its position
    if bullet_state == "fire":
        bulletY -= bullet_speed

        # Draw the bullet on the screen
        screen.blit(bullet_img, (bulletX, bulletY))

        # Check if the bullet has gone off the screen
        if bulletY <= 0:
            bullet_state = "ready"

    # Check for continuous firing while the Enter key is held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        if bullet_state == "ready":
            bulletX = spaceshipX + 16
            bulletY = spaceshipY
            bullet_state = "fire"

    # Check for spaceship movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceshipX > 0:
        spaceshipX -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceshipX < 736:
        spaceshipX += spaceship_speed

    # Draw the spaceship on the screen
    screen.blit(spaceship_img, (spaceshipX, spaceshipY))

    # Update the display
    pygame.display.update()"""



import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
#icon=pygame.display.image.load('icon.png')
#pygame.display.set_icon(icon)
background=pygame.image.load('bg.png')
spaceshipimg=pygame.image.load('spaceship.png')
alienimg=pygame.image.load('enemy.png')
alienX=random.randint(0,736)
alienY=random.randint(30,150)
alienspeedX=-1
alienspeedY=10
bulletimg=pygame.image.load('bullet.png')
spaceshipX=370
spaceshipY=480
bulletX=386
bulletY=490
changeX=0
check=False
running=True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-5
            if event.key==pygame.K_RIGHT:
                changeX=5
            if event.key==pygame.K_RETURN:
                if check is False:
                    check=True
                    bulletX=spaceshipX+16
        if event.type==pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=736:
        spaceshipX=736
    alienX+=alienspeedX
    if alienX<=0:
        alienspeedX=1
        alienY+=alienspeedY
    if alienX>=736:
        alienspeedX=-1
        alienY+=alienspeedY
    if bulletY<=0:
        bulletY=490
        check= False
    if check is True:
        screen.blit(bulletimg,(bulletX,bulletY))
        bulletY-=5
    screen.blit(spaceshipimg,(spaceshipX,spaceshipY))
    screen.blit(alienimg,(alienX,alienY))
    pygame.display.update()





"""import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

spaceshipimg = pygame.image.load('spaceship.png')
alienimg = pygame.image.load('enemy.png')
bulletimg = pygame.image.load('bullet.png')

spaceshipX = 370
spaceshipY = 480
spaceship_speed = 5
changeX = 0

alienX = random.randint(0, 736)
alienY = random.randint(30, 150)
alien_speedX = 1
alien_speedY = 30

bulletX = 0
bulletY = 490
bullet_speed = 5
bullet_state = "ready"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -5
            if event.key == pygame.K_RIGHT:
                changeX = 5
            if event.key == pygame.K_RETURN:
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
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= bullet_speed

        if bulletY <= 0:
            bullet_state = "ready"

    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
    screen.blit(alienimg, (alienX, alienY))

    pygame.display.update()
"""

"""import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

spaceshipimg = pygame.image.load('spaceship.png')
alienimg = pygame.image.load('enemy.png')
bulletimg = pygame.image.load('bullet.png')

spaceshipX = 370
spaceshipY = 480
spaceship_speed = 5
changeX = 0

alienX = random.randint(0, 736)
alienY = random.randint(30, 150)
alienspeedX = -1
alienspeedY = 10

bulletX = 0
bulletY = 490
bullet_speed = 5
bullet_state = "ready"

running = True

while running:
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

    if spaceshipX < 0:
        spaceshipX = 0
    elif spaceshipX > 736:
        spaceshipX = 736

    alienX += alienspeedX
    if alienX < 0 or alienX > 736:
        alienspeedX = -alienspeedX
        alienY += alienspeedY

    if bullet_state == "fire":
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= bullet_speed

        if bulletY <= 0:
            bullet_state = "ready"

    screen.fill((0, 0, 0))  # Fill the screen with a black background
    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
    screen.blit(alienimg, (alienX, alienY))

    pygame.display.update()"""
