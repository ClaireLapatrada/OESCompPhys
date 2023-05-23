# import and initiate pygame
import pygame
pygame.init()

# store RGB values in a variable
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# set up and initiate displaym fill it with black
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

# draw a pixel at (10,20) in green
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green
# draw a blue line from (100,200) to (300,400), thickness of 5.
pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)
# draw a red rectangle, top right corner at (400,400) length 50, width 25.
pygame.draw.rect(gameDisplay, red, (400,400,50,25))
# draw a white circle center at (150,150) radius of 75.
pygame.draw.circle(gameDisplay, white, (150,150), 75)
# draw a green polygon, first corner at (25,75), second at (76, 125), and so on.
pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))

# run the game/display until the red X close button is clicked
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # update frame
    pygame.display.update()