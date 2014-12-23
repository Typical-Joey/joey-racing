import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('pew pew')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)

    pos_change = [0, 0]

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            etype = event.type

            if etype == pygame.QUIT:
                gameExit = True

            if etype == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pos_change[0] = -5
                elif event.key == pygame.K_RIGHT:
                    pos_change[0] = 5
                elif event.key == pygame.K_UP:
                    pos_change[1] = -5
                elif event.key == pygame.K_DOWN:
                    pos_change[1] = 5

            if etype == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pos_change[0] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pos_change[1] = 0

        x += pos_change[0]
        y += pos_change[1]

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()
