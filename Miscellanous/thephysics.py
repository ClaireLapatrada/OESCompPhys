import math
import matplotlib.pyplot as plt
# barringer impact
gravity = -9.81 #m/s^2
density = 8000 #kg/m^3
volume = 33150 #m^3
initmass = 7509628 #kg
mass = 7509628 #kg
y = 100000 #m
d = 40 #m
initv = -1700 # m/s
v = -1700 # m/s
aird = 1.27
cd = 0.7
ks = []
mr = []
# time_chunk always at 0.01, step is used as a value to show the current value at a certain time (added by 0.01 each iteration).
time_chunk, step, c = 0.01,0.01,0.01
# define gravity and mass values
# create lists for graph
masses = [i for i in range(1000,10000)]
dias = [d for d in range(10,100)]
for mass in masses:
    for d in dias:
        positions, velocities, accelerations, drags = [], [], [], []
        while y >= 0:
                drag = 0.5*aird*(v**2)*cd*(((d/2)**2)*math.pi)
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
                print("Current Dia: " + str((d)) + " m")
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
        finalk = 0.5*mass*(v**2)
        mratio = mass/d
        ks.append(finalk)
        mr.append(mratio)

fig, ax = plt.subplots()

ax.scatter(ks, mr, s=1, vmin=0, vmax=100)
plt.scatter(mr,ks)
plt.show()