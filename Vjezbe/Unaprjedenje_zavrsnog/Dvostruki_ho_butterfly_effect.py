import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos
from scipy import*
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib.animation import PillowWriter


g= 9.81
m1, m2= 2, 0.3
L1, L2= 7, 4
pi=3.14159265
L = (L1 + L2)*1.2
t=np.linspace(0,40,1000)
# 25 numerickih tocaka u jednoj sekunddi

def fja(pocetni,t):
    th1=pocetni[0]
    dth1=pocetni[1]
    th2=pocetni[2]
    dth2=pocetni[3]
    ddth1=(0.5*L1*m2*sin(2.0*th1-2.0*th2)*dth1**2+L2*m2*sin(th1-th2)*dth2**2 
           +g*m1*sin(th1)+0.5*g*m2*sin(th1-2.0*th2)+0.5*g*m2*sin(th1))/(L1*(-m1+m2*cos(th1-th2)**2-m2))
    ddth2=((-m1-m2)*(L1*sin(th1-th2)*dth1**2-g*sin(th2))
           -(L2*m2*sin(th1-th2)*dth2**2+g*m1*sin(th1)+g*m2*sin(th1))*cos(th1-th2))/(L2*(-m1+m2*cos(th1-th2)**2-m2))
    return[dth1,ddth1,dth2,ddth2]

# zeljeni pocetni polozaji i brzine
th1_0=0.999*pi
th2_0=pi
dth1_0,dth2_0=0,0
pocetni=[th1_0,dth1_0,th2_0,dth2_0]

# zeljeni broj dvostrukih oscilatora
N=10
# zeljena razlika kutova izmedu svakog oscilatora
deltath=0.001

kord=[]
trag_x1, trag_y1 =[],[]
trag_x2, trag_y2 =[],[]
lines, traces1, traces2 =[],[],[]

for j in range(N):
    pocetni=[i-j*deltath for i in pocetni]
    y=odeint(fja, pocetni, t)
    th1= y[:,0] 
    dth1= y[:,1]
    th2= y[:,2]
    dth2= y[:,3]
    x1=L1*sin(th1)
    y1=-L1*cos(th1)
    x2=L1*sin(th1)+L2*sin(th2)
    y2=-L1*cos(th1)-L2*cos(th2)
    kord.append([x1,x2,y1,y2])
    # liste potrebne za animaciju i spremanje podataka
    trag_x1.append([])
    trag_y1.append([])
    trag_x2.append([])
    trag_y2.append([])
    lines.append(j)
    traces1.append(j)
    traces2.append(j)

fig, ax=plt.subplots(1,1,figsize=(5,5))
    
def animate(i):
    for h in range (N):
        lines[h].set_data( [0,kord[h][0][i],kord[h][1][i]], [0,kord[h][2][i],kord[h][3][i]] )
        if i == 0:
            trag_x1[h].clear()
            trag_y1[h].clear()
            trag_x2[h].clear()
            trag_y2[h].clear()
        trag_x1[h].append(kord[h][0][i])
        trag_y1[h].append(kord[h][2][i])
        trag_x2[h].append(kord[h][1][i])
        trag_y2[h].append(kord[h][3][i])
        traces1[h].set_data(trag_x2[h],trag_y2[h])
        traces2[h].set_data(trag_x1[h],trag_y1[h])

for h in range (N):
    lines[h], =plt.plot([], [], 'o-', lw=2, markersize='8') 
    traces1[h], = ax.plot([], [], '-', lw=1)
    traces2[h], = ax.plot([], [], '-', lw=1)

ani= animation.FuncAnimation(fig, animate, frames=1000, interval=40)
ax.set_xlim(-L,L)
ax.set_ylim(-L,L)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()
ani.save('ho.gif',writer='pillow',fps=25)
