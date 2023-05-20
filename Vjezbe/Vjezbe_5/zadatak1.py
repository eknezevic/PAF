import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

def kubna(x):
    return x**3
def sinus(x):
    return np.sin(x)

# test analitickog i numerickog rjesenja za trigonometrijsku funkciju
print('Derivacija u tocki daje',cal.d_u_tocki(sinus, 0.7, 0.01),',a analiticko rjesenje',np.cos(0.7))

# test analitickog i numerickog rjesenja te ovisnosti o koracima numericke derivacije za kubnu
dx= [0.001, 0.01, 0.1]

# korisnik ne bira metodu
plt.subplot(2, 1, 1)
for e in dx:
    x, y = cal.d_u_intervalu(kubna, -1, 1, e)
    plt.scatter(x, y, s=9, label = e)

x=np.arange(-1, 1, 0.01)
y = 3*x**2
plt.plot(x, y, c='red', linewidth=0.5, label = 'analiticko')

plt.title('Metoda tri-koraka')
plt.xlabel('x')
plt.ylabel('df(x)/dx')
plt.legend()

# korisnik bira twostep
plt.subplot(2, 1, 2)
for e in dx:
    x, y = cal.d_u_intervalu(kubna, -1, 1, e, False)
    plt.scatter(x, y, s=9, label=e)

x=np.arange(-1, 1, 0.01)
y = 3*x**2
plt.plot(x, y, c='red', linewidth=0.5, label = 'analiticko')

plt.title('Metoda dva-koraka')
plt.xlabel('x')
plt.ylabel('df(x)/dx')
plt.legend()

plt.tight_layout()
plt.show()