import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racing Game')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
carImgSize = carImg.get_rect().size

def crash():
    message_display('You Crashed')

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

accel_step = 0.5

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)

    accel = [0, 0]
    speed = [0, 0]

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            etype = event.type

            if etype == pygame.QUIT:
                gameExit = True

            if etype == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    accel[0] -= accel_step
                elif event.key == pygame.K_RIGHT:
                    accel[0] += accel_step

                if event.key == pygame.K_UP:
                    accel[1] -= accel_step
                elif event.key == pygame.K_DOWN:
                    accel[1] += accel_step

            if etype == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    speed[0] = accel[0] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    speed[1] = accel[1] = 0

        speed[0] += accel[0]
        speed[1] += accel[1]
        x += speed[0]
        y += speed[1]

        gameDisplay.fill(white)
        car(x, y)

        if x > (display_width - carImgSize[0]) or x < 0:
            crash()
        if y > (display_height - carImgSize[1]) or y < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
