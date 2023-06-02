# Napišite program koji crta putanju dvije čestice koje međudjeluju gravitacijskom silom. Provjerite valjanost
# programa na primjeru Sunca i Zemlje. Promatrajte problem u dvije dimenzije i koristite Euler-ovu metodu
# za rješavanje vezanih diferencijalnih jednadžbi.
# U početnom trenutku Sunce se nalazi u ishodištu i nema početnu brzinu, a Zemlja je udaljena jednu as-
# tronomsku jedinicu (1 a.u. = 1.486 · 1011 m) i ima početnu okomitu komponentu brzine v⊥ = 29783 m/s
# Masa Sunca je MS = 1.989 · 1030 kg, masa Zemlje je MZ = 5.9742 · 1024 kg, gravitacijska konstanta je
# G = 6.67408 · 10−11 Nm2/ kg2 , a jedna godina ima 365.242 dana.

import numpy as np

class Fgrav:
    def __init__(self,m1,x01,y01,vx1,vy1,m2,x02,y02,vx2,vy2):
        self.G=6.67408e-11
        self.m1=m1
        self.r1=[np.array((x01,y01))]
        self.v1=[np.array((vx1,vy1))]
        self.x1=[x01]
        self.y1=[y01]

        self.m2=m2
        self.r2=[np.array((x02,y02))]
        self.v2=[np.array((vx2,vy2))]
        self.x2=[x02]
        self.y2=[y02]

    def __move(self):
        a1=-self.G*self.m2*(self.r1[-1]-self.r2[-1])/((self.r1[-1][0]-self.r2[-1][0])**2 +(self.r1[-1][1]-self.r2[-1][1])**2)**(3/2)
        self.a1.append(a1)
        self.v1.append(self.v1[-1]+self.a1[-1]*self.dt)
        self.r1.append(self.r1[-1]+self.v1[-1]*self.dt)
        self.x1.append(self.r1[-1][0])
        self.y1.append(self.r1[-1][1])

    
        a2=-self.G*self.m1*(self.r2[-1]-self.r1[-1])/((self.r1[-1][0]-self.r2[-1][0])**2 +(self.r1[-1][1]-self.r2[-1][1])**2)**(3/2)
        self.a2.append(a2)
        self.v2.append(self.v2[-1]+self.a2[-1]*self.dt)
        self.r2.append(self.r2[-1]+self.v2[-1]*self.dt)
        self.x2.append(self.r2[-1][0])
        self.y2.append(self.r2[-1][1])

        self.t.append(self.t[-1]+self.dt)

    def polozaj(self,T, dt):
        self.T=T
        self.dt=dt
        self.t=[0]
        self.a1=[]
        self.a2=[]
        while self.t[-1]<self.T:
            self.__move()
        return self.x1, self.y1, self.x2, self.y2
