import pygame
from pygamef import button, text_set
import time
import math
import matplotlib.pyplot as plt

# setting up variables, screen dimension
pygame.init()
display_width = 1000
display_height = 750
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Asteroid Impact')
# colors
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
pxscale = 75590.5607043
inity = 10000 #km
y = 10000 #km
x = display_width/5
# 500 pixel : 10000 km so 1 pixel : 20 km
pxkmscale = y/500
# boolean for display queue
gook = False
disok = False
# set up explosion image and dimensions
exploimg = pygame.image.load('explo.png')
exploimg.convert()
rect = exploimg.get_rect()
imgcenter = (rect.w//2,rect.h//2)

# real background simulation
def real_drop():
    # I am sorry for using so many global variables, I didn't planned this out well.
    # It's basically just sending variables around to use in functions.
    global steps
    global drags
    global velocities
    global accelerations
    global finalk
    global y
    global x
    global mass
    global initmass
    global d
    global step
    global gook
    global positions
    global inity
    global finalv
    gravity = -9.81 #m/s^2
    # Initial velocity and updatable velocity
    initv = -1700 #m/s^2
    v = -1700
    # constants for drag
    aird = 1.27
    cd = 0.7
    # time_chunk always at 0.01, step is used as a value to show the current value at a certain time (added by 0.01 each iteration).
    # can't be smaller or program makes overflow error
    time_chunk, step, c = 0.01,0.01,0.01
    drag = 0.5*aird*(v**2)*cd*(((d/2)**2)*math.pi)
    # create lists for graph
    positions, velocities, accelerations, drags, steps = [], [], [], [], []
    # loop until asteroid reach ground
    while y >= 0:
        # try, except to prevent overflow error for big drag
        try:
            # calculate drag
            drag = 0.5*aird*(v**2)*cd*(((d/2)**2)*math.pi)
            # another overflow prevention
            if y > 100000:
                text_set("Result too large, please enter new parameters", 15, orange, display_width/2, 650)
                return "OVERFLOW"
            # calculate net force
            netforce =  (gravity*mass) + drag
            # calculate acceleration
            a = netforce / mass
            # print out values
            print("Drag: " + str(drag))
            print("Weight: " + str(gravity*mass))
            print("At time: " + str(step) + " s")
            print("Current Velocity: " + str(v) + " m/s")
            print("Current Position: " + str((y)) + " m from ground")
            print("Current Acceleration: " + str(a) + " m/s^2")
            print("Current Mass: " + str((mass)) + " kg")
            print('\n')
            # append values to the lists for graph
            positions.append(y)
            velocities.append(v)
            accelerations.append(a)
            drags.append(drag)
            # update the velocity and position using linearization formula
            v = v + (a * time_chunk)
            y = y + (v * time_chunk)
            # update time chunk
            step += c
        # prevent overflow error
        except OverflowError:
            text_set("Result too large, please enter new parameters", 15, orange, display_width/2, 650)
            return "OVERFLOW"
    gook = True
    # collect final velocity
    finalv = v
    print('done')
    print(f"Time it takes in reality: {step} seconds OR {(step)/60} minutes OR {(step)/3600} hours")
    print(f"Initial kinetic energy: {0.5*initmass*(initv**2)} Jouls")
    print(f"Initial gravitational potential energy: {mass*gravity*5} Joules")
    print(f"Final Kinetic Energy: {0.5*(mass*0.1)*(v**2)} Joules")
    print(f"Total (K + Ug) initial energy: {0+(mass*gravity*5)} Joules")
    print(f"Total final energy: {(0.5*(mass*0.1)*(v**2))+0} Joules")
    print(f"Change in total energy: {((0.5*initmass*(initv**2))+mass*gravity*5)-(0.5*mass*(v**2)+0)} Joules")
# activate gravity
def gravit():
    global gravity
    gravity = True
# calculation screen
def calculation():
    global disok
    global positions
    global gook
    global mass
    global d
    global initmass
    cal = True
    disok = False
    gook = False
    graphok = False
    # gets active when input box is clicked by user
    color_active = fc
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = red
    color = color_passive
    # color activity boolean
    active = False
    active2 = False
    # slider dimension
    input_rect = pygame.Rect(475, 200, 50, 30)
    input_rect2 = pygame.Rect(475, 300, 50, 30)
    # initialize dragging status
    rectangle_dragging = False
    rectangle_dragging2 = False
    while cal:
        # get mouse position to track movement
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # screen color
        gameDisplay.fill(navy)
        # extras: change colors
        if active:
            color = color_active
        else:
            color = color_passive
        if active2:
            color2 = color_active
        else:
            color2 = color_passive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cal = False
                pygame.quit()
                quit()
            # if mouse is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if it's left click and if it's within the slider knob dimension then color changes, activate movement, calculate offset
                if event.button == 1:            
                    if input_rect.collidepoint(event.pos):
                        active = True
                        if input_rect.x >= 300 and input_rect.x <= 650:
                            rectangle_dragging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = input_rect.x - mouse_x
                    if input_rect2.collidepoint(event.pos):
                        active2 = True
                        if input_rect2.x >= 300 and input_rect2.x <= 650:
                            rectangle_dragging2 = True
                            mouse_x, mouse_y = event.pos
                            offset_x = input_rect2.x - mouse_x
            # if mouse not clicked then deactivate
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active = False     
                    rectangle_dragging = False
                    active2 = False     
                    rectangle_dragging2 = False
            # if mouse moves then move knob by offset
            elif event.type == pygame.MOUSEMOTION:
                if rectangle_dragging:
                    if input_rect.x >= 300 and input_rect.x <= 650:
                        mouse_x, mouse_y = event.pos
                        input_rect.x = mouse_x + offset_x
                        # input_rect.y = mouse_y + offset_y
                    if input_rect.x < 300:
                        input_rect.x = 300
                    if input_rect.x > 650:
                        input_rect.x = 650
                # the same for the second slider
                if rectangle_dragging2:
                    if input_rect2.x >= 300 and input_rect2.x <= 650:
                        mouse_x, mouse_y = event.pos
                        input_rect2.x = mouse_x + offset_x
                        # input_rect.y = mouse_y + offset_y
                    if input_rect2.x < 300:
                        input_rect2.x = 300
                    if input_rect2.x > 650:
                        input_rect2.x = 650
        # ratio for the knob = (distance of the slider/ the actual mass or diameter it represents)
        initmass = int((input_rect.x-300)*28571.4286)
        mass = int((input_rect.x-300)*28571.4286)
        d = int((input_rect2.x-300)*2.85714286)
        # mass and diameter cant be 0, so i just defalt them to 1
        if mass == 0:
            mass = 1
        if d == 0:
            d = 1
        # show on screen what the mass and diameter user input
        text_set(f"Mass input: {mass} kg", 15, orange, display_width/2, 165)
        pygame.draw.rect(gameDisplay, white, (300, 215, 400, 5))
        pygame.draw.rect(gameDisplay, color, input_rect)
        text_set(f"Diameter input: {d} m", 15, orange, display_width/2, 265)
        pygame.draw.rect(gameDisplay, white, (300, 315, 400, 5))
        pygame.draw.rect(gameDisplay, color, input_rect2)
        pygame.draw.rect(gameDisplay, white, (415,(display_height/2)-5,160,60))
        # Calculate and go button
        button("Calculate", 420, display_height/2, 150, 50, fc, pred, white, real_drop)
        pygame.draw.rect(gameDisplay, white, (415,(display_height/2)+100-5,160,60))
        button("Go", 420, (display_height/2)+100, 150, 50, sky, sky, white)
        if gook:
            # only activate go button when calculation is done
            pygame.draw.rect(gameDisplay, white, (415,(display_height/2)+100-5,160,60))
            button("Go", 420, (display_height/2)+100, 150, 50, fc, pred, white, loop)
        text_set("Calculation will cause screen to freeze for a while, Please wait...", 20, orange, 500, 50)
        pygame.display.update()
        clock.tick(60)
def graph():
    # just displaying graphs when the "graph" button is clicked
    plt.plot(positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.legend(["Positions"])
    plt.show()

    plt.plot(velocities)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend(["Velocities"])
    plt.show()

    plt.plot(accelerations)
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.legend(["Acceleration"])
    plt.show()

    plt.plot(drags)
    plt.show()
def change_speed():
    # speed switch
    global tscale
    global change
    global current_time
    global pretime
    global s
    # prevent glitch by only running after some time past
    if current_time - pretime > 500:
        if change == False:
            change = True
        else:
            change = False
        if change == True:
            tscale = 60
        if change == False:
            tscale = 1
        pretime = current_time
def loop():
    # main loop, dropping screen
    global s
    global pretime
    global current_time
    global change
    global tscale
    global graphok
    global steps
    global xpositions
    global inity
    global disok
    global y
    global x
    global gravity
    global positions
    global craterdepth
    global finalv
    # Initial dropping height (x in pixel, y in km)
    x, y = display_width/5, 10000
    xpositions = []
    # initialize variables boolean
    # time initiate
    pretime = pygame.time.get_ticks()
    ptime = pygame.time.get_ticks()
    gravity = False
    run = True
    disok = False
    graphok = False
    # x position update bit
    if len(positions) < 1: # prevent division by 0
        s = 0
    else:
        s = 500/len(positions) # 45 degree angle
    # the same thing as position update
    chunk = 500/step*1000
    # initiate count variable
    count = 0
    # speed scale, will change when button clicked
    tscale = 1
    change = False
    # initial x position
    x = display_width/5
    # display radius in pixel, calculated with diameter and the scale.
    init_radius = d/(pxkmscale*2)
    radius = d/(pxkmscale*2)
    # to display, radius has to be at least one pixel. It's not accurate but for the sake of display
    if radius < 1:
        radius = 1
    start = None
    current_time = None
    # asteroids lose 90% of its mass through ablation and compression - source: https://sites.wustl.edu/meteoritesite/items/some-meteorite-realities/
    endmass = mass*0.1
    enddia = d*0.1
    # equation explained in video. Obtained from scraping online simulation with different mass.
    craterd = (2.174*enddia) + 1030.3333333334324
    craterdepth = (0.026*enddia) + 503.3333333333334
    while run: # work on time stuff
        current_time = pygame.time.get_ticks()
        gameDisplay.fill(navy)
        if disok:
            # display crater when the drop is done
            pygame.draw.ellipse(gameDisplay, orange, (pygame.Rect(x-(craterd/20)/2, 650-(craterdepth/40), craterd/20, craterdepth/20)))
        pygame.draw.rect(gameDisplay, black, (display_width/5,display_height/5,600,500))
        # show time
        text_set(f"{current_time}", 20, orange, 500, 30)
        # get event, quit when needed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        # If gravuty button is clicked, then start drop
        if gravity:
            if start == None:
                start = pygame.time.get_ticks()
            if count >= len(positions)-2:
                # stop drop when positions are 2 away from being all displayed
                end = pygame.time.get_ticks()
                disok = True
                graphok = True
                gravity = False
            elif count < len(positions):
                # if positions are not yet all display then display them.
                # prevent glitch from time
                if current_time - ptime > chunk/(tscale):
                    # add x positions. (only to create 45º angle)
                    xpositions.append(x)
                    # 120.48 comes from width and height ratio ( to make a y=x slop to create 45º angle)
                    x += s*(500/(step))*120.48
                    # display radius decrease until 10% is left
                    radius -= (init_radius*0.9)/step
                    # update count
                    count += int((500/(step))*120.48)
                    ptime = current_time
        if disok:
            # when simulation done, display impact information
            text_set(f"Sim. time taken: {round(end-start)/1000} secs", 15, orange, display_width/2, 680)
            text_set(f"Actual time taken: {round(step)} secs", 15, orange, display_width/2, 710)
            text_set(f"Actual time taken: {round(step/60)} mins", 15, orange, display_width/2, 740)
            # pygame.draw.circle(gameDisplay, orange, (x-radius, 650), craterdepth)
            # pygame.draw.rect(gameDisplay, orange, (x-radius, 650, radius*2, int(abs(craterdepth)/20)))
            text_set(f"Meteorite Mass - before: {initmass} kg after: {endmass} kg", 12, orange, display_width/2, 50)
            text_set(f"Meteorite Diameter - before: {d} m after: {enddia} m", 12, orange, display_width/2, 70)
            text_set(f"Impact energy: {0.5*endmass*(finalv**2)} joules", 12, orange, display_width/2, 90)
            text_set(f"Crater diameter: {craterd} m", 12, orange, display_width/2, 110)
            text_set(f"Crater depth: {craterdepth} m", 12, orange, display_width/2, 130)
            # explosion image change scale
            scaleex = pygame.transform.scale(exploimg, (craterd/20,100)) # not to scale
            # image dimension manipulation
            rect = scaleex.get_rect()
            imgcenter = (rect.w//2,rect.h//2)
            # display explosion image
            gameDisplay.blit(scaleex, (x-imgcenter[0],650-(imgcenter[1]*2)+(imgcenter[1]*0.2)))
        if count < len(positions):
            # display ball position
            pygame.draw.circle(gameDisplay, pred, (x, 650-(positions[count]/pxkmscale)-radius), radius)
        # white line for scales (extra)
        pygame.draw.rect(gameDisplay, white, (display_width/5 ,display_height/5,10,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 50,5,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 100,10,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 150,5,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 200,10,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 250,5,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 300,10,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 350,5,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 400,10,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 450,5,3))
        pygame.draw.rect(gameDisplay, white, (display_width/5,(display_height/5) + 500,10,3))
        # display drop info and buttons
        text_set(f"Drop height: {inity} m", 15, orange, 310, 170)
        pygame.draw.rect(gameDisplay, white, (45,45,110,60))
        button("gravity", 50, 50, 100, 50, fc, pred, white, gravit)
        pygame.draw.rect(gameDisplay, white, (45,145,110,60))
        button("restart", 50, 150, 100, 50, fc, pred, white, loop)
        pygame.draw.rect(gameDisplay, white, (45,245,110,60))
        button("reset", 50, 250, 100, 50, fc, pred, white, calculation)
        # speed changeable while simulation is still going on
        if not disok:
            pygame.draw.rect(gameDisplay, white, (25,345,140,60))
            button(f"speed = x {tscale}", 30, 350, 130, 50, fc, pred, white, change_speed)
        # if triggered graph button will appear
        if graphok:
            pygame.draw.rect(gameDisplay, white, (45,445,110,60))
            button("graph", 50, 450, 100, 50, fc, pred, white, graph)
        # display scale
        text_set(f"1 PX : {pxkmscale} m ", 20, orange, 895, 705)
        # display update and fps
        pygame.display.update()
        clock.tick(300)
# run
calculation()