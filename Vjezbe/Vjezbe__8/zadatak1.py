import numpy as np
from emf import Putanja
import matplotlib.pyplot as plt

elektron=Putanja(1,-1,1,1,1)
ex,ey,ez=elektron.polozaj(0,0,0,0,0,3,0.001)
pozitron=Putanja(1,1,1,1,1)
px,py,pz=pozitron.polozaj(0,0,0,0,0,3,0.001)

ax = plt.axes(projection='3d')
ax.plot3D(ex,ey,ez, 'gray')

ax.plot(ex,ey,ez,c='blue',label='elektron')
ax.plot(px,py,pz,c='r',label='pozitron')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
ax.legend()
plt.show()