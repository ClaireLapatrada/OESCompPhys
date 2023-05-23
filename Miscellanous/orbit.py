# import libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# values
mmass = 7.3 * 10**22 # kg
emass = 5.97 * 10**24 # kg
sd = 3.84 * 10**8 # m
mvx = 10**3 # m/s
mvy = 0 #m/s
evx = 0 # m/s
evy = 0 # m/s
gc = 6.67 * 10**-11
# timestep
t = 1000
it = 0

# initial position of each
ex, ey = 0,0 # earth
mx, my = 0, sd # moon

# plot the initial position of the moon and the earth
plt.scatter(ex,ey)
plt.scatter(mx,my)

# set window size
plt.xlim([-sd*2,sd*2])
plt.ylim([-sd*2,sd*2])

# lists for keeping track of values for graph
mxs = []
mys = []
exs = []
eys = []
mxaccs = []
myaccs = []
mrxs = []
mrys = []
mkes = []
mpes = []
ekes = []
epes = []
totalme = []
mxgravs = []
mygravs = []
mzvs = []
rx, ry = 0, sd

# linearization loop, updating gravity, acceleration, velocity, and then position
while it < 4800:
    rx, ry = mx-ex, my-ey
    rhat = ((rx**2)+(ry**2))**0.5
    # x and y components of gravity for the moon and the earth
    r = math.dist((mx, my), (ex,ey))**2
    m_fgx = ((-gc*mmass*emass)/r)*(rx/rhat)
    m_fgy = ((-gc*mmass*emass)/r)*(ry/rhat)
    e_fgx = ((-gc*mmass*emass)/r)*(rx/rhat)
    e_fgy = ((-gc*mmass*emass)/r)*(ry/rhat)
    # f = ma but reversed to find acceleration
    mxa = m_fgx/mmass
    mya = m_fgy/mmass
    exa = e_fgx/emass
    eya = e_fgy/emass
    # linearization for updating velocities
    mvx = mvx + (mxa*t)
    mvy = mvy + (mya*t)
    evx = evx + (exa*t)
    evy = evy + (eya*t)
    # linearization for updating positions
    mx = mx + (mvx*t)
    my = my + (mvy*t)
    ex = ex + (evx*t)
    ey = ey + (evy*t)
    # ex = 0
    # ey = 0
    # evx = 0
    # evy = 0
    # combined velocity applying pythagorean theorem
    mzv = math.hypot(mvx, mvy)
    ezv = math.hypot(evx, evy)
    # kinetic energy
    mke = 0.5 * mmass * (mzv**2)
    eke = 0.5 * emass * (ezv**2)
    # potential energy
    mpe = (-gc*mmass*emass)/(math.dist((mx, my), (ex,ey)))
    epe = (-gc*mmass*emass)/(math.dist((ex, ey), (mx,my)))
    # printing values
    print(f"moon kE: {mke} Joules")
    print(f"moon pE: {mpe} Joules")
    print(f"earth kE: {eke} Joules")
    print(f"earth pE: {epe} Joules")
    print(f"Total moon energy: {mke+mpe}")
    print()
    # appending to lists to keep track of values and for graphing purpose
    mxs.append(mx)
    mys.append(my)
    exs.append(ex)
    eys.append(ey)
    mxaccs.append(mvx)
    myaccs.append(mvy)
    mrxs.append(rx)
    mrys.append(ry)
    mkes.append(mke)
    mpes.append(mpe)
    ekes.append(eke)
    epes.append(epe)
    totalme.append(mke+mpe)
    mxgravs.append(m_fgx)
    mygravs.append(m_fgy)
    mzvs.append(mzv)
    # updating time step (big time step because values are really big)
    it += 1
# loop throug all the values and plot the vectors from each point to another, creating an ellipse ultimately.

for i in range(len(mxs)-1):
    plt.quiver(mxs[i], mys[i], mxs[i+1]-mxs[i], mys[i+1]-mys[i], color='purple', scale_units='xy', angles = 'xy', scale=1)
    plt.quiver(exs[i], eys[i], exs[i+1]-exs[i], eys[i+1]-eys[i], color='blue', scale_units='xy', angles = 'xy', scale=1)
    # if i%50 == 0:
    #     plt.quiver(mxs[i], mys[i], mxgravs[i], mygravs[i], color='blue', scale_units='xy', angles = 'xy', scale=1e12)
    #     # gravity
    #     # plt.quiver(mxs[i], mys[i], mxgravs[i], 0, color='orange', scale_units='xy', angles = 'xy', scale=1e12)
    #     # plt.quiver(mxs[i], mys[i], 0, mygravs[i], color='red', scale_units='xy', angles = 'xy', scale=1e12)
    #     # # velocity
    #     plt.quiver(mxs[i], mys[i], mxaccs[i], 0, color='green', scale_units='xy', angles = 'xy', scale=1e-5)
    #     plt.quiver(mxs[i], mys[i], 0, myaccs[i], color='brown', scale_units='xy', angles = 'xy', scale=1e-5)


# graphs
plt.legend(['earth', 'moon'])
plt.xlabel('x-position in meter')
plt.xlabel('y-position in meter')
plt.title("Moon's orbit around earth")
plt.show()

plt.plot(mzvs)
plt.xlabel('time (Iteration) ')
plt.ylabel('Total Velocity')
plt.title("Moon's velocity over time")
plt.show()

# moon kinetic energy graph
plt.plot(mkes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Kinetic energy')
plt.title("Moon's kinetic energy over time")
plt.show()

# moon potential energy graph(negative)
plt.plot(mpes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Potential energy')
plt.title("Moon's potential energy over time")
plt.show()

# earth kinetic energy graph
plt.plot(ekes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Kinetic energy')
plt.title("earth's kinetic energy over time")
plt.show()

# earth potential energy graph(negative)
plt.plot(epes)
plt.xlabel('time (Iteration) ')
plt.ylabel('Potential energy')
plt.title("earth's potential energy over time")
plt.show()

plt.plot(mkes)
plt.plot(mpes)
plt.plot(totalme)
plt.xlabel('time (Iteration) ')
plt.ylabel('Moon\'s energy over time')
plt.legend(['Kinetic', 'Potential', 'total'])
plt.title('Moon\'s Kinetic and Potential energy over time')
plt.show()