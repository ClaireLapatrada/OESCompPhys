c = 2.998 * 10**8
nm = 10**-9
h = 6.623 * 10**-34
eV = 1.6e-19 # J

jun = [700, 660, 640, 590]
x = 430

for x in jun:
    E = (c*h)/(nm*x)
    # print(E, 'J')
    light_eV = E/eV
    print(light_eV, 'eV')