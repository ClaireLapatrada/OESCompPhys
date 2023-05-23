# Importing libraries and initializing Pygame
import pygame
import time
import random

clock = pygame.time.Clock()
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = [0,0,255]
turq = (175,238,238)
navy = (38,70,83)
sky = (135,206,250)
fc = (42,157,143)
# Storing display width and height in variables to use later
display_width = 800
display_height = 600
# Set up and initialize display width and height
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

# Define text object function to help simplifying the process to render the text and its rectangle
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,txtcolor,action=None,hover_action=None):
    # get mouse position (x,y)
    mouse = pygame.mouse.get_pos()
    # click is when the mouse get pressed
    click = pygame.mouse.get_pressed()
    # if the mouse is hovered within the button rectangle
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        # draw rectangle with hovered color
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if hover_action != None:
            hover_action()
        # if the mouse is clicked ( == 1), and no action is happening, then an action is activate
        if click[0] == 1 and action != None:
            action()     
    else:
        # draw rectangle with normal color
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    # set up text font and size
    smallText = pygame.font.Font("EightBitDragon-anqx.ttf",20)
    # set up text message and rectangle
    textSurf, textRect = text_objects(msg, smallText, txtcolor)
    # set up text center position
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    # display the text
    gameDisplay.blit(textSurf, textRect)
# quit game function
def quit_game():
    pygame.quit()
    quit()
# easier text set up function
def text_set(text, size, fc, xcenter, ycenter):
    # set up font text
    largeText = pygame.font.Font('EightBitDragon-anqx.ttf',size)
    # define game name text and its rectangle
    TextSurf, TextRect = text_objects(text, largeText, fc)
    # position the text center
    TextRect.center = (xcenter,ycenter)
    # display the text and its invisible rectangle
    gameDisplay.blit(TextSurf, TextRect)