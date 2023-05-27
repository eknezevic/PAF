from proj import Projectile
import matplotlib.pyplot as plt

proj=Projectile(2, 0, 3, 43, 2, 3, 1)

proj.gibanjeEuler(0.01)
x1=proj.x
y1=proj.y
plt.plot(x1,y1,label="Euler")

proj.gibanjeRungeKutta(0.01)
x2=proj.x
y2=proj.y
plt.plot(x2,y2,label="Runge Kutta")

plt.title('x-y graf kosog hitca')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend()
plt.show()