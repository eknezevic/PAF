import numpy as np

class Putanja:
    def __init__(self, m, q, vx0, vy0, vz0):
        # cestica ima sve 3 pocetne komponente brzine razlicite od 0, pocinje u ishodistu
        self.q=q
        self.m=m
        self.x=[0]
        self.y=[0]
        self.z=[0]
        self.r=[np.array((0,0,0))]
        self.v=[np.array((vx0,vy0,vz0))]

    def __move(self):
        Fl=self.q*(self.E+np.cross(self.v[-1],self.B))
        a=Fl/self.m
        self.a.append(a)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.r.append(self.r[-1]+self.v[-1]*self.dt)
        self.x.append(self.r[-1][0])
        self.y.append(self.r[-1][1])
        self.z.append(self.r[-1][2])
        self.t.append(self.t[-1]+self.dt)

    def polozaj(self,Ex,Ey,Ez,Bx,By,Bz,dt):
        self.E=np.array((Ex,Ey,Ez))
        self.B=np.array((Bx,By,Bz))
        self.dt = dt
        self.t=[0]
        self.a=[]
        # vrijeme promatranja gibanja
        while self.t[-1]<10:
            self.__move()
        return self.x, self.y, self.z
