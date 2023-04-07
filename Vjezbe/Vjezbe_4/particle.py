import numpy as np
import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self,v0,kut,x0,y0,dt):
        self.v0=v0
        self.xi=x0
        self.yi=y0
        self.dt=dt
        self.kut=np.radians(kut)
        self.xlista=[self.xi]
        self.ylista=[self.yi]
        self.vx=np.cos(self.kut)*self.v0
        self.vy=np.sin(self.kut)*self.v0

    def __move(self):
        self.xi+=self.vx*self.dt
        self.vy-=9.81*self.dt
        self.yi+=self.vy*self.dt
        self.xlista.append(self.xi)
        self.ylista.append(self.yi)
        
    def range(self):
        while self.yi>=0:
            self.__move()
        return max(self.xlista)
    
    def plot_trajectory(self):
        plt.plot(self.xlista,self.ylista)
        plt.title('Putanja u x-y ravnini')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.show()

    def reset(self):
        self.v0=0 
        self.kut=0
        self.xi=0
        self.yi=0
        self.dt=0
        self.xlista=[]
        self.ylista=[]

    def analiticki(self):
        return(self.v0**2*np.sin(2*self.kut))/9.81

