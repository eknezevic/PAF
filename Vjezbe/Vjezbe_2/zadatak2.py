import numpy as np
import matplotlib.pyplot as plt

def kosi_hitac(v0, kut):
    g=9.81
    dt=0.1
    t=[0]
    x=[0]
    y=[0]
    vx=np.cos(np.radians(kut))*v0
    vy=[np.sin(np.radians(kut))*v0]

    for i in range(100):
        x.append(x[i]+vx*dt)
        vy.append(vy[i]-g*dt)
        y.append(y[i]+vy[i]*dt)
        t.append(t[i]+dt)

    plt.subplot(2, 2, 1)
    plt.plot(x, y)
    plt.title('Ovisnost visine o udaljenosti')
    plt.xlabel('x [s]')
    plt.ylabel('y [m]')
    plt.subplot(2, 2, 2)
    plt.plot(t, x)
    plt.title('Ovisnost udaljenosti o vremenu')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.subplot(2, 2, 3)
    plt.plot(t, y)
    plt.title('Ovisnost visine o vremenu')
    plt.xlabel('t [s]')
    plt.ylabel('y [m]')

    plt.tight_layout()  
    plt.show()

kosi_hitac(10, 5)
