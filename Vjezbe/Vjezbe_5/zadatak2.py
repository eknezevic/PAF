import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

def kubna(x):
    return x**3
def sinus(x):
    return np.sin(x)

# granice intergracije i broj podjele koraka
a=0
b=6.32
N=np.arange(50, 1000, 20)

d_medja=[]
g_medja=[]
trapezna=[]
analiticki=[]
for n in N:
    analiticki.append(-(np.cos(b) -np.cos(a)))
    g_medja.append(cal.integr(sinus, a, b, n)[0])
    d_medja.append(cal.integr(sinus, a, b, n)[1])
    trapezna.append(cal.trapezna_integr(sinus, a, b, n))

plt.plot(N, analiticki, label = 'analiticko')
plt.scatter(N, g_medja, s=9, label = 'gornja medja')
plt.scatter(N, d_medja, s=9, label = 'donja medja')
plt.scatter(N, trapezna, s=9, label = 'trapezna')

plt.title('Integracija')
plt.xlabel('Broj koraka N')
plt.ylabel('Iznos integrala')
plt.legend()
plt.show()