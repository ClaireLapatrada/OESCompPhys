# import libraries
import matplotlib.pyplot as plt
import numpy as np
import math
import pygame
import math
import matplotlib.pyplot as plt
from pygamef import text_set, button

# setting up variables, screen dimension
pygame.init()
display_width = 1400
display_height = 800
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Solar system simulation')
run = False

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

# time
it = 0
daysec = 24*60*60
t = 1*daysec/10
dupt = 1*daysec/10

# Initial values and constants
x, y = 0, 0
vx, vy = 0, 0
gc = 6.67 * 10**-11
dist = 1
small = True
direction = 'out'
pretime = pygame.time.get_ticks()
ch = display_height//2
cw = display_width//2
mag = 9.2
change = False
z = False
skes = []
spes = []

# Sun values
smass = 1.989 * 10**30 # kg sun https://www.space.com/17001-how-big-is-the-sun-size-of-the-sun.html
srad = 695508000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
svx = 0
svy = 0
sx, sy = 0,0

def change_speed():
    global t
    global dist
    global pretime
    global current_time
    global change
    if current_time - pretime > 500:
        if change == False:
            change = True
        else:
            change = False
        if change == True:
            t = dupt*10
            dist = 10
        if change == False:
            t = dupt
            dist = 1
        pretime = current_time

def zoom():
    global small
    global pretime
    global current_time
    global z
    global mag
    global direction
    global paths
    if current_time - pretime > 500:
        if z == False:
            z = True
        else:
            z = False
        if z == True:
            mag = 10.1
            small = False
            direction = 'in'
        if z == False:
            mag = 9.5
            small = True
            direction = 'out'
        pretime = current_time
        paths = []
x = 0
y = 58588000000
paths = []
def orbit(name, mass, radius, sepd, vel_x):
    # Sun gravity does not take into account of all planets here, which is inaccurate.
    # but it wouldn't affect the simulation as the impact is too small.
    global current_time
    global it
    global x, y, sx, sy, svx, svy, vx, vy
    # change orbit distance scale
    s = 10**mag
    current_time = pygame.time.get_ticks()
    rx, ry = x-sx, y-sy
    rhat = ((rx**2)+(ry**2))**0.5
    r = math.dist((x, y), (sx,sy))**2
    # Gravity
    s_fgx = ((-gc*mass*smass)/r)*(rx/rhat)
    s_fgy = ((-gc*mass*smass)/r)*(ry/rhat)
    fgx = ((-gc*mass*smass)/r)*(rx/rhat)
    fgy = ((-gc*mass*smass)/r)*(ry/rhat)
    # Acceleration
    sxa = s_fgx/smass
    sya = s_fgy/smass
    xa = fgx/mass
    ya = fgy/mass
    # Update velocity
    svx = svx + (sxa*t)
    svy = svy + (sya*t)
    vx = vx + (xa*t)
    vy = vy + (ya*t)
    # Update position
    sx = sx + (svx*t)
    sy = sy + (svy*t)
    x = x + (vx*t)
    y = y + (vy*t)
    # Combined velocity applying pythagorean theorem
    szv = math.hypot(svx, svy)
    zv = math.hypot(vx, vy)
    # Kinect energy
    ske = 0.5 * smass * (szv**2)
    ke = 0.5 * mass * (zv**2)
    # Potential energy
    spe = (-gc*mass*smass)/(math.dist((sx, sy), (x,y)))
    pe = (-gc*mass*smass)/(math.dist((x, y), (sx,sy)))
    # updating time step (big time step because values are really big)
    it += t
    print(x/s, y/s)
    gameDisplay.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
    pygame.draw.rect(gameDisplay, white, (cw-62.5, 157.5, 126, 46))
    button(f"Speed x{dist}", cw-60, 160, 120, 40, fc, pred, white, change_speed)
    pygame.draw.rect(gameDisplay, white, (cw-62.5, 217.5, 126, 46))
    button(f"Zoom {direction}", cw-60, 220, 120, 40, fc, pred, white, zoom)
    [pygame.draw.circle(gameDisplay, white, i, 1) for i in paths]
    pygame.draw.circle(gameDisplay, pred, (sx/s + cw, sy/s + ch), (sepd-srad)/s) # sun
    pygame.draw.circle(gameDisplay, fc, ((x/s) + cw, (y/s) + ch), 2) # mercury
    text_set("Sun", 7, white, sx/s + cw, sy/s + ch)
    text_set("Mercury", 7, white, (x/s) + cw * 1.02, (y/s) + ch * 1.02)
    paths.append(((x/s) + cw, (y/s) + ch))
    text_set(f"{it/daysec} day", 14, orange, display_width//2, 80)
    text_set(f"Distance apart scale =  1px : {int(s)} km", 14, orange, display_width//2, 120)


while True:
    gameDisplay.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
    orbit('Mercury', 3.285 * 10**23, 2440000, 58588000000, 47870)
    pygame.display.update()
    clock.tick(300)
