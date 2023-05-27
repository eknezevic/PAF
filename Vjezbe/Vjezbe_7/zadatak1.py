from proj import Projectile
import matplotlib.pyplot as plt

proj=Projectile(2, 0, 3, 43, 2, 3, 1)
#              m, h0, v0, kut0, ro, Cd, A
t=[0.075,0.0625,0.05,0.0375,0.025,0.01,0.001,0.0001]
for dt in t:
    proj.gibanjeEuler(dt)
    x=proj.x
    y=proj.y
    plt.plot(x,y, label=dt)

# za usporedbu
proj.gibanjeRungeKutta(0.01)  
x2=proj.x
y2=proj.y
plt.plot(x2,y2,label="Runge Kutta")

plt.title('x-y graf kosog hitca')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(fontsize='8',loc='upper left')
plt.show()