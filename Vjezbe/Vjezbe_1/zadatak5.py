import matplotlib.pyplot as plt

while True:
    x1=input("Unesite x koordinatu prve tocke:")
    y1=input("Unesite y koordinatu prve tocke:")
    x2=input("Unesite x koordinatu druge tocke:")
    y2=input("Unesite y koordinatu druge tocke:")
    try: 
        x1=float(x1)
        y1=float(y1)
        x2=float(x2)
        y2=float(y2)
        break
    except ValueError:
        print("Koordinate moraju biti brojevi, ponovite unos.")
def pravac(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b=-a*x1+y1
    print("Jednadzba pravca je y={:.2f}*x + {:.2f}".format(a,b))
def graf(x1,y1,x2,y2):
    x=[x1,x2]
    y=[y1,y2]
    plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=7)
    plt.xlabel('x')
    plt.ylabel('y')
    unos=input('Zelite li prikaz grafa na ekranu ili spremanje kao PDF? prikazi/spremi:')
    if unos=='prikazi':
        plt.show()
    elif unos=='spremi':
        ime=input('Unesite ime grafa:')
        plt.savefig(f'{ime}.pdf')

pravac(x1,y1,x2,y2)
graf(x1,y1,x2,y2)