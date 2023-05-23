from pydoc import visiblename
from termios import VT1
# Importing necessary libraries
# import matplotlib.pyplot as plt
# import numpy as np

# Finding acceleration from gravity and mass function

# Defining gravity and mass values
gravity = 4.905
mass_kg = 0.5
# Defining function
def return_acceleration(drag):
        # Netforce calculation
        netforce = gravity - drag
        # Acceleration calculation from Newton's second law
        a = netforce / mass_kg
        # Separate acceleration calculation
        va, ha = gravity / mass_kg, drag / mass_kg
        # Printing out values
        print("Net acceleration: " + str(a) + " m/s^2")
        print("Vertical Acceleration: " + str(va) + " m/s^2")
        print("Horizontal Acceleration: " + str(ha) + " m/s^2")
        # Return all acceleration values in this format: [Net acceleration, Vertical Acceleration, Horizontal Acceleration]
        return [a, va, ha]
# Finding the position of an object from a given mass, force values, time function

def return_position(drag):
    # defining values (can be change to solve different problems)
    # initial velocity and position
    v, y = 0, 5
    # time_chunk always at 0.01, step is used as a value to show the current value at a certain time (added by 0.01 each iteration).
    time_chunk, step, c = 0.001, 0.001, 0.001
    # define gravity and mass values
    gravity, mass_kg = 4.905, 0.5
    gravityms2 = 9.81
    # create lists for graph
    positions, velocities, accelerations = [], [], []
    # calculate net force
    netforce =  gravity - drag
    # calculate acceleration
    a = netforce / mass_kg
    # print out acceleration
    print("Acceleration: " + str(a))
    # iterate through the eahc time chunk (0.01 sec)
    while y >= 0.01:
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
        y = y - (v * time_chunk)
        # update time chunk
        step += c
        # print out drag value note
    if drag > mass_kg:
        print("Note: The Drag force is more than the mass of the object, the object will have negative acceleration, aka move backward")
    # # plotting graphs 
    # plt.plot(positions)
    # plt.plot(velocities)
    # plt.plot(accelerations)
    # # I couldn't change the x-axis to be the time, but that would be the preferred x-axis value.
    # plt.xlabel("Iteration")
    # plt.ylabel("Height (m)")
    # plt.legend(["position", "velocities", "accelerations"])
    # plt.show()
    print(f"Initial kinetic energy: {0} Jouls")
    print(f"Initial gravitational potential energy: {mass_kg*gravityms2*5} Joules")
    print(f"Final Kinetic Energy: {0.5*mass_kg*(v**2)} Joules")
    print(f"Total (K + Ug) initial energy: {0+(mass_kg*gravityms2*5)} Joules")
    print(f"Total final energy: {(0.5*mass_kg*(v**2))+0} Joules")
    print(f"Change in total energy: {((0.5*mass_kg*(v**2))+0)-(0+(mass_kg*gravityms2*5))} Joules")
    # return new position
    return 5-y
# Running the function
return_position(1)