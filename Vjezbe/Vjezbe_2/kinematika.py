import matplotlib.pyplot as plt
import numpy as np

def jednoliko(f,m):
    t=[0]
    x=[0]
    v=[0]
    a=[f/m]

    for i in range(100):
        dt=0.1
        t.append(t[i]+dt)
        x.append(x[i]+v[i]*dt)
        v.append(v[i]+(f/m)*dt)
        a.append(f/m)

    plt.subplot(2,2,1)
    plt.plot(t,x)
    plt.xlabel("t")
    plt.ylabel("x")
    plt.title("Ovisnost polozaja u vremenu")
    plt.subplot(2,2,2)
    plt.plot(t,v)
    plt.xlabel("t")
    plt.ylabel("v")
    plt.title("Ovisnost brzine u vremenu")
    plt.subplot(2,2,3)
    plt.plot(t,a)
    plt.xlabel("t")
    plt.ylabel("a")
    plt.title("Ovisnost akceleracije u vremenu")

    plt.tight_layout()
    plt.show()

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

    jednoliko(10,5)