import particle as prt
import matplotlib.pyplot as plt


dt=0
t=[]
relativna_greska=[]
for i in range(100):
    dt+=0.001
    t.append(dt)
    p1=prt.Particle(10,60,0,0,dt)
    relativna_greska.append(abs(p1.analiticki()-p1.range())/p1.analiticki()*100)

plt.plot(t, relativna_greska)
plt.title('Ovisnost relativne pogreške')
plt.xlabel('∆t [s]')
plt.ylabel('Apsolutna relativna pogreska')
plt.show()