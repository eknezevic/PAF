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

jednoliko(10,5)

