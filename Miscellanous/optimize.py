import math
import matplotlib.pyplot as plt
masses = [i for i in range(10000000)] #kg
dias = [d for d in range(1000)] #m
drag = 0.5*1.27*(v**2)*0.7*(((d/2)**2)*math.pi)
netforce =  (gravity*mass) + drag
a = netforce / mass
finalk = 0.5*mass*(v**2)