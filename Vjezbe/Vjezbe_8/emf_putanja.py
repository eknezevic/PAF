# Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. Demon-
# strirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju⃗ B = (0, 0, B)
# i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?

import numpy as np

class Putanja:
    def __init__(self, m, q, vx0, vy0, vz0):
        # cestica ima sve 3 pocetne komponente brzine razlicite od 0, a pocetni polozaj neka su 0
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
        # liste polja nx3dimenzije
        self.t.append(self.t[-1]+self.dt)

    def polozaj(self,Ex,Ey,Ez,Bx,By,Bz,dt):
        self.E=np.array((Ex,Ey,Ez))
        self.B=np.array((Bx,By,Bz))
        a0=(self.q*(self.E+np.cross(self.v,self.B)))/self.m
        self.dt = dt
        self.t=[0]
        self.a=[a0]
        #  vrijeme promatranja gibanja npr 20s
        # while len(self.t)<=20:
        while self.t[-1]<10:
            self.__move()
        return self.x, self.y, self.z

        # x=[]
        # y=[]
        # z=[]
        # for i in self.r:
        #     x.append(i[0])
        #     y.append(i[1])
        #     z.append(i[2])
        
    # def koordinate(self):

        # return x,y,z




