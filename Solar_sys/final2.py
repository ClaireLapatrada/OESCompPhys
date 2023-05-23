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

# time
daysec = 24*60*60
t = 1*daysec/10
dupt = 1*daysec/10

paths = []
# values
smass = 1.989 * 10**30 # kg sun https://www.space.com/17001-how-big-is-the-sun-size-of-the-sun.html
mmass = 3.285 * 10**23 # kg mercury https://solarsystem.nasa.gov/planets/mercury/by-the-numbers/
vmass = 4.8685 * 10**24 # kg venus https://www.smartconversion.com/otherInfo/Mass_of_planets_and_the_Sun.aspx
emass = 5.972 * 10**24 # kg earth https://www.space.com/17638-how-big-is-earth.html
mamass = 6.4185 * 10**23 # kg mars https://www.smartconversion.com/otherInfo/Mass_of_planets_and_the_Sun.aspx
jmass = 1.8986 * 10**27 # kg https://www.smartconversion.com/otherInfo/Mass_of_planets_and_the_Sun.aspx
samass = 5.6846 * 10**26 # kg  https://www.smartconversion.com/otherInfo/Mass_of_planets_and_the_Sun.aspx
umass = 8.6810 *10**25 # kg  https://www.smartconversion.com/otherInfo/Mass_of_planets_and_the_Sun.aspx
nmass = 10.243 * 10**25 # kg  https://www.smartconversion.com/otherInfo/Mass_of_planets_and_the_Sun.aspx

srad = 695508000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
mrad = 2440000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
vrad = 6052000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
erad = 6371000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
marad = 3390000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
jrad = 69911000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
sarad = 58232000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
urad = 25362000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
nrad = 24622000 # https://solarsystem.nasa.gov/resources/686/solar-system-sizes/

msd = 58588000000 # m https://solarsystem.nasa.gov/planets/mercury/in-depth/
vsd = 108209475000 # m https://solarsystem.nasa.gov/planets/venus/by-the-numbers/
esd = 150000000000 # m https://solarsystem.nasa.gov/planets/earth/overview/
masd = 227943824000# m https://solarsystem.nasa.gov/planets/mars/by-the-numbers/
jsd = 778340821000 # m https://solarsystem.nasa.gov/planets/jupiter/by-the-numbers/
sasd = 1426666422000 # m https://solarsystem.nasa.gov/planets/saturn/by-the-numbers/
usd = 2870658186000# m https://solarsystem.nasa.gov/planets/uranus/by-the-numbers/
nsd = 4498396441000# m https://solarsystem.nasa.gov/planets/neptune/by-the-numbers/

svx = 0 # m/s
svy = 0 # m/s
mvx = 47870 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
mvy = 0 # m/s
vvx = 35020 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
vvy = 0
evx = 30000 # m/s https://www.techtarget.com/whatis/definition/Earths-mean-orbital-speed
evy = 0 # m/s
mavx = 24077 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
mavy = 0
jvx = 13070 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
jvy = 0
savx = 9690 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
savy = 0
uvx = 6810 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
uvy = 0
nvx = 5430 # m/s # https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
nvy = 0

# constant
gc = 6.67 * 10**-11
# timestep
it = 0

# initial position of each
sx, sy = 0,0 # sun
mx, my = 0, msd # mercury
vx, vy = 0, vsd # venus
ex, ey = 0, esd # earth
max, may = 0, masd # mars
jx, jy = 0, jsd # jupiter
sax, say = 0, sasd # saturn
ux, uy = 0, usd # uranus
nx, ny = 0, nsd # neptune

# lists for keeping track of values for graph
sxs = []
sys = []
mxs = []
mys = []
vxs = []
vys = []
exs = []
eys = []
maxs = []
mays = []
jxs = []
jys = []
saxs = []
says = []
uxs = []
uys = []
nxs = []
nys = []

mrxs = []
mrys = []
vrxs = []
vrys = []
erxs = []
erys = []
marxs = []
marys = []
jrxs = []
jrys = []
sarxs = []
sarys = []
urxs = []
urys = []
nrxs = []
nrys = []

skes = []
spes = []
mkes = []
mpes = []
vkes = []
vpes = []
ekes = []
epes = []
makes = []
mapes = []
jkes = []
jpes = []
sakes = []
sapes = []
ukes = []
upes = []
nkes = []
npes = []

totalme = []
totalve = []
totalee = []
totalmae = []
totalje = []
totalsae = []
totalue = []
totalne = []

mxgravs = []
mygravs = []
vxgravs = []
vygravs = []
exgravs = []
eygravs = []
maxgravs = []
maygravs = []
jxgravs = []
jygravs = []
saxgravs = []
saygravs = []
uxgravs = []
uygravs = []
nxgravs = []
nygravs = []

mzvs = []
vzvs = []
ezvs = []
mazvs = []
jzvs = []
sazvs = []
uzvs = []
nzvs = []

# init value
dist = 1
small = True
direction = 'out'

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

# linearization loop, updating gravity, acceleration, velocity, and then position
pretime = pygame.time.get_ticks()
ch = display_height//2
cw = display_width//2

mag = 9.2

change = False
z = False
paths = []

while True:
    current_time = pygame.time.get_ticks()
    mrx, mry = mx-sx, my-sy
    vrx, vry = vx-sx, vy-sy
    erx, ery = ex-sx, ey-sy
    marx, mary = max-sx, may-sy
    jrx, jry = jx-sx, jy-sy
    sarx, sary = sax-sx, say-sy
    urx, ury = ux-sx, uy-sy
    nrx, nry = nx-sx, ny-sy

    mrhat = ((mrx**2)+(mry**2))**0.5
    vrhat = ((vrx**2)+(vry**2))**0.5
    erhat = ((erx**2)+(ery**2))**0.5
    marhat = ((marx**2)+(mary**2))**0.5
    jrhat = ((jrx**2)+(jry**2))**0.5
    sarhat = ((sarx**2)+(sary**2))**0.5
    urhat = ((urx**2)+(ury**2))**0.5
    nrhat = ((nrx**2)+(nry**2))**0.5

    # x and y components of gravity for the moon and the earth
    mr = math.dist((mx, my), (sx,sy))**2
    vr = math.dist((vx, vy), (sx,sy))**2
    er = math.dist((ex, ey), (sx,sy))**2
    mar = math.dist((max, may), (sx,sy))**2
    jr = math.dist((jx, jy), (sx,sy))**2
    sar = math.dist((sax, say), (sx,sy))**2
    ur = math.dist((ux, uy), (sx,sy))**2
    nr = math.dist((nx, ny), (sx,sy))**2
    
    s_fgx = ((-gc*mmass*smass)/mr)*(mrx/mrhat) + ((-gc*vmass*smass)/vr)*(vrx/vrhat)
    + ((-gc*emass*smass)/er)*(erx/erhat) + ((-gc*mamass*smass)/mar)*(marx/marhat) 
    + ((-gc*jmass*smass)/jr)*(jrx/jrhat) + ((-gc*samass*smass)/sar)*(sarx/sarhat) 
    + ((-gc*umass*smass)/ur)*(urx/urhat) + ((-gc*nmass*smass)/nr)*(nrx/nrhat)
    s_fgy = ((-gc*mmass*smass)/mr)*(mry/mrhat) + ((-gc*vmass*smass)/vr)*(vry/vrhat)
    + ((-gc*emass*smass)/er)*(ery/erhat) + ((-gc*mamass*smass)/mar)*(mary/marhat) 
    + ((-gc*jmass*smass)/jr)*(jry/jrhat) + ((-gc*samass*smass)/sar)*(sary/sarhat) 
    + ((-gc*umass*smass)/ur)*(ury/urhat) + ((-gc*nmass*smass)/nr)*(nry/nrhat)
    m_fgx = ((-gc*mmass*smass)/mr)*(mrx/mrhat)
    m_fgy = ((-gc*mmass*smass)/mr)*(mry/mrhat)
    v_fgx = ((-gc*vmass*smass)/vr)*(vrx/vrhat)
    v_fgy = ((-gc*vmass*smass)/vr)*(vry/vrhat)
    e_fgx = ((-gc*emass*smass)/er)*(erx/erhat)
    e_fgy = ((-gc*emass*smass)/er)*(ery/erhat)
    ma_fgx = ((-gc*mamass*smass)/mar)*(marx/marhat) 
    ma_fgy = ((-gc*mamass*smass)/mar)*(mary/marhat) 
    j_fgx = ((-gc*jmass*smass)/jr)*(jrx/jrhat) 
    j_fgy = ((-gc*jmass*smass)/jr)*(jry/jrhat) 
    sa_fgx = ((-gc*samass*smass)/sar)*(sarx/sarhat) 
    sa_fgy = ((-gc*samass*smass)/sar)*(sary/sarhat)
    u_fgx = ((-gc*umass*smass)/ur)*(urx/urhat) 
    u_fgy = ((-gc*umass*smass)/ur)*(ury/urhat)
    n_fgx = ((-gc*nmass*smass)/nr)*(nrx/nrhat) 
    n_fgy = ((-gc*nmass*smass)/nr)*(nry/nrhat) 
    
    # f = ma but reversed to find acceleration
    sxa = s_fgx/smass
    sya = s_fgy/smass
    mxa = m_fgx/mmass
    mya = m_fgy/mmass
    vxa = v_fgx/vmass
    vya = v_fgy/vmass
    exa = e_fgx/emass
    eya = e_fgy/emass
    maxa = ma_fgx/mamass
    maya = ma_fgy/mamass
    jxa = j_fgx/jmass
    jya = j_fgy/jmass
    saxa = sa_fgx/samass
    saya = sa_fgy/samass
    uxa = u_fgx/umass
    uya = u_fgy/umass
    nxa = n_fgx/nmass
    nya = n_fgy/nmass

    # linearization for updating velocities
    svx = svx + (sxa*t)
    svy = svy + (sya*t)
    mvx = mvx + (mxa*t)
    mvy = mvy + (mya*t)
    vvx = vvx + (vxa*t)
    vvy = vvy + (vya*t)
    evx = evx + (exa*t)
    evy = evy + (eya*t)
    mavx = mavx + (maxa*t)
    mavy = mavy + (maya*t)
    jvx = jvx + (jxa*t)
    jvy = jvy + (jya*t)
    savx = savx + (saxa*t)
    savy = savy + (saya*t)
    uvx = uvx + (uxa*t)
    uvy = uvy + (uya*t)
    nvx = nvx + (nxa*t)
    nvy = nvy + (nya*t)
    # linearization for updating positions
    sx = sx + (svx*t)
    sy = sy + (svy*t)
    mx = mx + (mvx*t)
    my = my + (mvy*t)
    vx = vx + (vvx*t)
    vy = vy + (vvy*t)
    ex = ex + (evx*t)
    ey = ey + (evy*t)
    max = max + (mavx*t)
    may = may + (mavy*t)
    jx = jx + (jvx*t)
    jy = jy + (jvy*t)
    sax = sax + (savx*t)
    say = say + (savy*t)
    ux = ux + (uvx*t)
    uy = uy + (uvy*t)
    nx = nx + (nvx*t)
    ny = ny + (nvy*t)
    # combined velocity applying pythagorean theorem
    szv = math.hypot(svx, svy)
    mzv = math.hypot(mvx, mvy)
    vzv = math.hypot(vvx, vvy)
    ezv = math.hypot(evx, evy)
    mazv = math.hypot(mavx, mavy)
    jzv = math.hypot(jvx, jvy)
    sazv = math.hypot(savx, savy)
    uzv = math.hypot(uvx, uvy)
    nzv = math.hypot(nvx, nvy)

    # kinetic energy
    ske = 0.5 * smass * (szv**2)
    mke = 0.5 * mmass * (mzv**2)
    vke = 0.5 * vmass * (vzv**2)
    eke = 0.5 * emass * (ezv**2)
    make = 0.5 * mamass * (mazv**2)
    jke = 0.5 * jmass * (jzv**2)
    sake = 0.5 * samass * (sazv**2)
    uke = 0.5 * umass * (uzv**2)
    nke = 0.5 * nmass * (nzv**2)

    # potential energy
    spe = (-gc*emass*smass)/(math.dist((sx, sy), (ex,ey)))
    mpe = (-gc*mmass*smass)/(math.dist((mx, my), (sx,sy)))
    vpe = (-gc*vmass*smass)/(math.dist((vx, vy), (sx,sy)))
    epe = (-gc*emass*smass)/(math.dist((ex, ey), (sx,sy)))
    mape = (-gc*mamass*smass)/(math.dist((max, may), (sx,sy)))
    jpe = (-gc*jmass*smass)/(math.dist((jx, jy), (sx,sy)))
    sape = (-gc*samass*smass)/(math.dist((sax, say), (sx,sy)))
    upe = (-gc*umass*smass)/(math.dist((ux, uy), (sx,sy)))
    npe = (-gc*nmass*smass)/(math.dist((nx, ny), (sx,sy)))

    # # work
    # swork = math.hypot(s_fgx, s_fgy)*
    # mwork = math.hypot(m_fgx, m_fgy)
    # vwork = math.hypot(v_fgx, v_fgy)

    # appending to lists to keep track of values and for graphing purpose
    if it % 10000 == 0:
        sxs.append(sx)
        sys.append(sy)
        mxs.append(mx)
        mys.append(my)
        vxs.append(vx)
        vys.append(vy)
        exs.append(ex)
        eys.append(ey)
        maxs.append(max)
        mays.append(may)
        jxs.append(jx)
        jys.append(jy)
        saxs.append(sax)
        says.append(say)
        uxs.append(ux)
        uys.append(uy)
        nxs.append(nx)
        nys.append(ny)

        mrxs.append(mx)
        mrys.append(my)
        vrxs.append(vx)
        vrys.append(vy)
        erxs.append(ex)
        erys.append(ey)
        marxs.append(max)
        marys.append(may)
        jrxs.append(jx)
        jrys.append(jy)
        sarxs.append(sax)
        sarys.append(say)
        urxs.append(ux)
        urys.append(uy)
        nrxs.append(nx)
        nrys.append(ny)

        skes.append(ske)
        spes.append(spe)
        mkes.append(mke)
        mpes.append(mpe)
        vkes.append(vke)
        vpes.append(vpe)
        ekes.append(eke)
        epes.append(epe)
        makes.append(make)
        mapes.append(mape)
        jkes.append(jke)
        jpes.append(jpe)
        sakes.append(sake)
        sapes.append(sape)
        ukes.append(uke)
        upes.append(upe)
        nkes.append(nke)
        npes.append(npe)

        totalme.append(mke+mpe)
        totalve.append(vke+vpe)
        totalee.append(eke+epe)
        totalmae.append(make+mape)
        totalje.append(jke+jpe)
        totalsae.append(sake+sape)
        totalue.append(uke+upe)
        totalne.append(nke+npe)
        
        mxgravs.append(m_fgx)
        mygravs.append(m_fgy)
        vxgravs.append(v_fgx)
        vygravs.append(v_fgy)
        exgravs.append(e_fgx)
        eygravs.append(e_fgy)
        maxgravs.append(ma_fgx)
        maygravs.append(ma_fgy)
        jxgravs.append(j_fgx)
        jygravs.append(j_fgy)
        saxgravs.append(sa_fgx)
        saygravs.append(sa_fgy)
        uxgravs.append(u_fgx)
        uygravs.append(u_fgy)
        nxgravs.append(n_fgx)
        nygravs.append(n_fgy)

        mzvs.append(mzv)
        vzvs.append(vzv)
        ezvs.append(ezv)
        mazvs.append(mazv)
        jzvs.append(jzv)
        sazvs.append(sazv)
        uzvs.append(uzv)
        nzvs.append(nzv)
    # updating time step (big time step because values are really big)
    it += t
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
    # change orbit distance scale
    s = 10**mag
    [pygame.draw.circle(gameDisplay, white, i, 1) for i in paths]
    pygame.draw.circle(gameDisplay, pred, (sx/s + cw, sy/s + ch), (msd-srad)/s) # sun
    pygame.draw.circle(gameDisplay, fc, ((mx/s) + cw, (my/s) + ch), 2) # mercury
    pygame.draw.circle(gameDisplay, orange, ((vx/s) + cw, (vy/s) + ch), 3) # venus
    pygame.draw.circle(gameDisplay, navy, ((ex/s) + cw, (ey/s) + ch), 3) # earth
    pygame.draw.circle(gameDisplay, (255, 0, 0), ((max/s) + cw, (may/s) + ch), 3) # mars
    pygame.draw.circle(gameDisplay, (207,185,151), ((jx/s) + cw, (jy/s) + ch), 7) # jupiter
    pygame.draw.circle(gameDisplay, yellow, ((sax/s) + cw, (say/s) + ch), 5) # saturn
    pygame.draw.circle(gameDisplay, sky, ((ux/s) + cw, (uy/s) + ch), 4) # uranus
    pygame.draw.circle(gameDisplay, (2,7,93), ((nx/s) + cw, (ny/s) + ch), 4) # neptune
    if small:
        text_set("Sun", 7, white, sx/s + cw, sy/s + ch)
        text_set("Mercury", 7, white, (mx/s) + cw * 1.02, (my/s) + ch * 1.02)
        text_set("Venus", 7, white, (vx/s) + cw * 1.02, (vy/s) + ch * 1.02)
        text_set("Earth", 7, white, (ex/s) + cw * 1.02, (ey/s) + ch * 1.02)
        text_set("Mars", 7, white, (max/s) + cw * 1.02, (may/s) + ch * 1.02)
    text_set("Jupiter", 7, white, (jx/s) + cw * 1.02, (jy/s) + ch * 1.02)
    text_set("Saturn", 7, white, (sax/s) + cw * 1.02, (say/s) + ch * 1.02)
    text_set("Uranus", 7, white, (ux/s) + cw * 1.02, (uy/s) + ch * 1.02)
    text_set("Neptune", 7, white, (nx/s) + cw * 1.02, (ny/s) + ch * 1.02)
    paths.append(((mx/s) + cw, (my/s) + ch))
    paths.append(((vx/s) + cw, (vy/s) + ch))
    paths.append(((ex/s) + cw, (ey/s) + ch))
    paths.append(((max/s) + cw, (may/s) + ch))
    paths.append(((jx/s) + cw, (jy/s) + ch))
    paths.append(((sax/s) + cw, (say/s) + ch))
    paths.append(((ux/s) + cw, (uy/s) + ch))
    paths.append(((nx/s) + cw, (ny/s) + ch))
    text_set(f"{it/daysec} day", 14, orange, display_width//2, 80)
    text_set(f"Distance apart scale =  1px : {int(s)} km", 14, orange, display_width//2, 120)
    pygame.display.update()
    clock.tick(300)

# set window size
plt.xlim([-masd*2,masd*2])
plt.ylim([-masd*2,masd*2])
for i in range(len(exs)-1):
    # Sun
    plt.quiver(sxs[i], sys[i], sxs[i+1]-sxs[i], sys[i+1]-sys[i], color='red', scale_units='xy', angles = 'xy', scale=1)
    # Mercury
    plt.quiver(mxs[i], mys[i], mxs[i+1]-mxs[i], mys[i+1]-mys[i], color='green', scale_units='xy', angles = 'xy', scale=1)
    # Venus
    plt.quiver(vxs[i], vys[i], vxs[i+1]-vxs[i], vys[i+1]-vys[i], color='orange', scale_units='xy', angles = 'xy', scale=1)
    # Earth
    plt.quiver(exs[i], eys[i], exs[i+1]-exs[i], eys[i+1]-eys[i], color='blue', scale_units='xy', angles = 'xy', scale=1)
    # Mars
    plt.quiver(maxs[i], mays[i], maxs[i+1]-maxs[i], mays[i+1]-mays[i], color='brown', scale_units='xy', angles = 'xy', scale=1)
    # Jupiter
    plt.quiver(jxs[i], jys[i], jxs[i+1]-jxs[i], jys[i+1]-jys[i], color='gray', scale_units='xy', angles = 'xy', scale=1)
    # Saturn
    plt.quiver(saxs[i], says[i], saxs[i+1]-saxs[i], says[i+1]-says[i], color='yellow', scale_units='xy', angles = 'xy', scale=1)
    # Uranus
    plt.quiver(uxs[i], uys[i], uxs[i+1]-uxs[i], uys[i+1]-uys[i], color='cyan', scale_units='xy', angles = 'xy', scale=1)
    # Neptune
    plt.quiver(nxs[i], nys[i], nxs[i+1]-nxs[i], nys[i+1]-nys[i], color='purple', scale_units='xy', angles = 'xy', scale=1)

# graphs
plt.legend(['Sun', 'Mercury', 'Venus',  'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])
plt.xlabel('x-position in meter')
plt.xlabel('y-position in meter')
plt.title("Planets' orbit around the Sun")
plt.show()

plt.plot(mzvs)
plt.xlabel('time (Iteration) ')
plt.ylabel('Total Velocity')
plt.title("Mercury's velocity over time")
plt.show()

# merc kinetic energy graph
plt.plot(mkes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Kinetic energy')
plt.title("Merc's kinetic energy over time")
plt.show()

# merc potential energy graph(negative)
plt.plot(mpes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Potential energy')
plt.title("Merc's potential energy over time")
plt.show()

# sun kinetic energy graph
plt.plot(skes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Kinetic energy')
plt.title("Sun's kinetic energy over time")
plt.show()

# sun potential energy graph(negative)
plt.plot(spes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Potential energy')
plt.title("Sun's potential energy over time")
plt.show()

plt.plot(mkes)
plt.plot(mpes)
plt.plot(totalme)
plt.xlabel('time (Iteration) ')
plt.ylabel('Merc\'s energy over time')
plt.legend(['Kinetic', 'Potential', 'total'])
plt.title('Merc\'s Kinetic and Potential energy over time')
plt.show()