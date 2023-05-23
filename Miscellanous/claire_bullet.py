import matplotlib.pyplot as plt
import numpy as np
def drag_bounce(d):
    v, y = 0, 0
    time_chunk, step, c = 0.001, 0.001, 0.001
    gravity, mass_kg = 4.905, 0.0097
    fluid_density = 1.27
    cd = 0.295
    csa = 0.00031415926
    drag = mass_kg * fluid_density * cd * csa * v
    positions, steps = [], []
    while time_chunk <= 3:
        # calculate netforce
        netforce = - drag
        # calculate acceleration
        a = netforce / mass_kg
        # print out values
        print("At time chunk: " + str(step))
        print("Current Velocity: " + str(-v))
        print("Current Position: " + str(y))
        print('\n')
        # update the velocity and position using linearization formula
        v = v + (a * time_chunk)
        y = y + (v * time_chunk)
        # append values to the lists for graph
        positions.append(y)
        steps.append(step)
        # update time chunk
        step += c