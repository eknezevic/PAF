from harmonic_oscillator import HarmonicOscillator
import matplotlib.pyplot as plt
import numpy as np

HO=HarmonicOscillator(1,1,0,1)
HO.osciliranje(0.01)

plt.subplot(2,2,1)
plt.plot(HO.t,HO.x)
plt.title("ovisnost polozaja o vremenu")
plt.xlabel("t [s]")
plt.ylabel("x [m]")

plt.subplot(2,2,2)
plt.plot(HO.t,HO.v)
plt.title("ovisnost brzine o vremenu")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")

plt.subplot(2,2,3)
plt.plot(HO.t,HO.a)
plt.title("ovisnost akceleracije o vremenu")
plt.xlabel("t [s]")
plt.ylabel("a [m/s^2]")

plt.subplot(2,2,4)
dt = [0.01,0.1,1]
for i in dt:
    HO.osciliranje(i)
    plt.scatter(HO.t, HO.x, s=3, label=i)
t, x_analiticko = HO.analiticko_rjesenje()
plt.plot(t, x_analiticko, 'r-', label='analiticko')
plt.title('numericko rjesenje za razlicite ∆t')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.legend(fontsize='5',loc='lower left')

plt.tight_layout()
plt.show()