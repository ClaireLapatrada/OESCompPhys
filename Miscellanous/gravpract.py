import math
import matplotlib.pyplot as plt
x1, y1 = 1, 1
x2, y2 = 3, 2
z = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

rx, ry = x2-x1, y2-y1
rhatx, rhaty = (x2-x1)/z, (y2-y1)/z

plt.quiver(x1, y1, rx, ry, color='purple', scale_units='xy', angles = 'xy', scale=1)
plt.quiver(x1, x1, rhatx, rhaty, color='black', scale_units='xy', angles = 'xy', scale=1)
plt.quiver(x1, x1, rx, 0, color='red', scale_units='xy', angles = 'xy', scale=1)
plt.quiver(x2, y1, 0, ry, color='blue', scale_units='xy', angles = 'xy', scale=1)
plt.xlim([0,5])
plt.ylim([0,5])
plt.show()
