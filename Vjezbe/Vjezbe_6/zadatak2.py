
from harmonic_oscillator import HarmonicOscillator
import matplotlib.pyplot as plt
import numpy as np

HO = HarmonicOscillator(1,1,0,1)
dt=np.arange(0.01, 0.1, 0.001)
numericki=[]
T_analiticki = 2*np.pi/np.sqrt(HO.k/HO.m)
analiticki=[]

for i in dt:
    T_numericki=HO.period(i)
    numericki.append(T_numericki)
    analiticki.append(T_analiticki)
    HO.reset()

plt.plot(dt, analiticki, label='analiticki period')
plt.plot(dt, numericki, label='numericki period')
plt.xlabel('dt [s]')
plt.ylabel('period T [s]')
plt.title('graf ovinsosti numerickog T o velicini koraka dt')
plt.legend()
plt.show()