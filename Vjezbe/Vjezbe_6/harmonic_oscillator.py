import numpy as np

class HarmonicOscillator:

    def __init__(self,k,m,x0,v0):
        self.k=k
        self.m=m
        self.x=[x0]
        self.v=[v0]
        self.a=[-self.k/self.m*x0]
        self.t=[0]

    # gibanje u zadanom vremenskom koraku 
    def __move(self,dt):
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.x.append(self.x[-1]+self.v[-1]*dt)
        self.a.append(-self.k/self.m*self.x[-1])
        self.t.append(self.t[-1]+dt)

    # pusta se u gibanje u vremenu
    def osciliranje(self,dt):
        self.x=[self.x[0]]
        self.v=[self.v[0]]
        self.a=[-self.k/self.m*self.x[0]]
        self.t=[0]
        while max(self.t)<15:
            self.__move(dt)

    def reset(self):
        self.x=[self.x[0]]
        self.v=[self.v[0]]
        self.a=[self.a[0]]
        self.t=[self.t[0]]

    def analiticko_rjesenje(self):
        # x(t) = C cosωt + D sinωt = Acos(ωt +φ)       A= (C^2 + D^2 )^1/2         φ = arctan(− D / C)
        w=np.sqrt(self.k/self.m)
        A=np.sqrt(self.x[0]**2+(self.v[0]/w)**2) 
        if self.x[0]==0:
            fi=np.pi/2
        else:
            fi=np.arctan(-self.v[0]/w/self.x[0])
        x_analiticko=[]
        t=np.linspace(0, 15)
        for dt in t:
            x_analiticko.append(A*np.cos(w*dt-fi))
        return t, x_analiticko

    def period(self, dt):
        vremena_nultocki=[]
        while len(vremena_nultocki)<3:
            while max(self.t)<15:
                self.__move(dt)
                if (self.x[-2]>0 and self.x[-1]<0) or (self.x[-2]<0 and self.x[-1]>0):
                    vremena_nultocki.append(self.t[-1])
                    break
        period = vremena_nultocki[-1]-vremena_nultocki[0]
        return period