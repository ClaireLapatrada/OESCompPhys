import pygame
from pygamef import button
import time

pygame.init()
display_width = 800
display_height = 600
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Balls')
black = (0,0,0)
white = (255,255,255)
yellow = (233,196,106)
orange = (244,162,97)
red = (231,111,81)
turq = (175,238,238)
navy = (38,70,83)
sky = (135,206,250)
fc = (42,157,143)
pred = (231,111,81)
mass_kg = 1
x, y = display_width/2, display_height/3
ball = pygame.draw.circle(gameDisplay, orange, (x,y), 40)
def gravit():
    global gravity
    gravity = True

def loop():
    global y
    global gravity
    x, y = display_width/2, display_height/3
    dragging = False
    gravity = False
    run = True
    mouse_x, mouse_y = pygame.mouse.get_pos()
    previous_time = pygame.time.get_ticks()
    while run:
        gameDisplay.fill(navy)
        pygame.draw.circle(gameDisplay, orange, (x,y), 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = x - mouse_x
                    offset_y = y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    x = mouse_x + offset_x
                    y = mouse_y + offset_y
            if gravity:
                    drag = 0
                    v = 0
                    # time_chunk always at 0.01, step is used as a value to show the current value at a certain time (added by 0.01 each iteration).
                    time_chunk, step, c = 0.001, 0.001, 0.001
                    # define gravity and mass values
                    mass_kg = 0.5
                    gravityms2 = 9.81
                    # create lists for graph
                    positions, velocities, accelerations = [], [], []
                    # calculate net force
                    netforce =  (gravityms2*mass_kg) - drag
                    # calculate acceleration
                    a = netforce / mass_kg
                    # print out acceleration
                    # iterate through the eahc time chunk (0.01 sec)
                    while y <= display_height-40:
                        # print out values
                        print("At time chunk: " + str(step))
                        print("Current Velocity: " + str(v))
                        print("Current Position: " + str(y))
                        print('\n')
                        # append values to the lists for graph
                        positions.append(y)
                        velocities.append(v)
                        accelerations.append(a)
                        # update the velocity and position using linearization formula
                        v = v + (a * time_chunk)
                        y = y + (v * time_chunk)
                        # update time chunk
                        step += c
                        pygame.draw.circle(gameDisplay, orange, (x,y), 40)
                    gravity = False
        pygame.draw.rect(gameDisplay, white, (45,45,110,60))
        button("gravity", 50, 50, 100, 50, fc, pred, white, gravit)
        pygame.display.update()
        clock.tick(60)

loop()