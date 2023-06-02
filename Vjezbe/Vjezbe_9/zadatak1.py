import numpy as np
from gravitacija import Fgrav
import matplotlib.pyplot as plt

medudjelovanje=Fgrav(5.9742e24,1.486e11,0,0,29783, 1.989e30,0,0,0,0)
x1,y1,x2,y2=medudjelovanje.polozaj(365.242*24*60*60,100)

plt.plot(x1,y1,label='Zemlja',c='blue' )
plt.plot(x2,y2,label='Sunce',c='r')

plt.title('Zemlja-Sunce gibanje u gravitacijskom polju')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(fontsize='8',loc='upper left')
plt.show()
