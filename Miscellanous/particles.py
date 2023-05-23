# import libraries
import matplotlib.pyplot as plt
import numpy as np
import math
import pygame
import time
import math
from statistics import mean
import random
import matplotlib.colors as mcolors

# setting up variables, screen dimension

colors = [key for key in mcolors.CSS4_COLORS.keys()]

pygame.init()
display_width = 1000
display_height = 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Particles')

navy = (38,70,83)

m = 4.65e-26
temp = 298
boltz_k = 1.38 * 10**-23
# change sd to make it looks like the particles are actually bouncing, right now the window size makes the particle goes too fast because it's small.
# some particles look like they aren't moving because the speed is too fast, and the refresh rate is too small.
sd = math.sqrt((temp*boltz_k)/m)
n = 100
area = display_width * display_height

pressure = (n*boltz_k*temp)/area
f = pressure*display_width
all_contact_t = []
particles = []
for n in range(n):
    initx = random.randint(0, display_width)
    inity = random.randint(0, display_height)
    # normal distribution
    vxs = np.random.normal(0, sd, 1000)
    vys = np.random.normal(0, sd, 1000)
    vx = random.choice(vxs)
    vy = random.choice(vys)
    # chi distribution
    v = math.sqrt(((vx)**2) + ((vy)**2))
    vy = v*math.cos(vx/vy)
    vx = v*math.sin(vx/vy)
    particles.append([initx, inity, vx, vy])

r = 4
t = 0

def pos_update(x, y, vx, vy):
    global all_contact_t
    if y > display_height or y < 0 :
        contact_time = (m*(vy*2))/f
        all_contact_t.append(contact_time)
        vy = -vy

    if x > display_width or x < 0 :
        contact_time = (m*(vx*2))/f
        all_contact_t.append(contact_time)
        vx = -vx
    
    x += vx
    y += vy
    return x, y, vx, vy

for i in range(3000):
    gameDisplay.fill(navy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for ball in particles:
        ball[0], ball[1], ball[2], ball[3] = pos_update(ball[0], ball[1], ball[2], ball[3])
    for ind, ball in enumerate(particles):
        pygame.draw.circle(gameDisplay, colors[ind], (ball[0], ball[1]), r)
    clock.tick(300)
    pygame.display.update()

print(f"AVG contact time: {mean(all_contact_t)}")



