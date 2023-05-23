# arg = [Y, drag, MASS]
def return_position(arg):
    global y
    # defining values (can be change to solve different problems)
    # initial velocity and position
    y, drag = arg[0], arg[1]
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
        print("Note: The Drag force is more than the mass of the object, the object will have negative acceleration, aka move backward/up")
    print(f"Initial kinetic energy: {0} Jouls")
    print(f"Initial gravitational potential energy: {mass_kg*gravityms2*5} Joules")
    print(f"Final Kinetic Energy: {0.5*mass_kg*(v**2)} Joules")
    print(f"Final gravitational potential energy: {0} Joules")
    print(f"Total (K + Ug) initial energy: {0+(mass_kg*gravityms2*5)} Joules")
    print(f"Total final energy: {(0.5*mass_kg*(v**2))+0} Joules")
    print(f"Change in total energy: {((0.5*mass_kg*(v**2))+0)-(0+(mass_kg*gravityms2*5))} Joules")
    # return new position
#     return y
# Running the function
# return_position(1)