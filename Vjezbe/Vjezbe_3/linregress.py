from statistics import*
import matplotlib.pyplot as plt
import numpy as np

def linregress(x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6):
    x=[x1,x2,x3,x4,x5,x6]
    y=[y1,y2,y3,y4,y5,y6]
    xm=mean(x)
    ym=mean(y)
    xx=mean([x1**2,x2**2,x3**2,x4**2,x5**2,x6**2])
    yy=mean([y1**2,y2**2,y3**2,y4**2,y5**2,y6**2])
    a=xm*ym/xx
    ma=((yy/xx -a**2)/6)**(1/2)
    print('Modul torzije aluminijske sipke iznosi',a,'±',ma,'Nm/rad')
    plt.scatter(x,y,c='r', label='Vrijednosti parametara')
    x_func = np.linspace(0, 1.3, 50)
    y_func = a*x_func
    plt.plot(x_func, y_func,label='y= ax')
    plt.xlabel('φ / rad')
    plt.ylabel('M / Nm')
    plt.legend()
    plt.title('Graf linearne regresije')
    plt.show()

linregress(0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472, 0.052, 0.124, 0.168, 0.236, 0.284, 0.336)