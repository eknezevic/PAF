from statistics import*
from scipy.stats import sem

def rucno(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9):
    x=(x1+x2+x3+x4+x5+x6+x7+x8+x9+x0)/10
    m=(((x-x0)**2+(x-x1)**2+(x-x2)**2+(x-x3)**2+(x-x4)**2+(x-x5)**2+(x-x6)**2+(x-x7)**2+(x-x8)**2+(x-x9)**2)/90)**(0.5)
    print(x,'±',m)

def python(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9):
    x=mean([x1,x2,x3,x4,x5,x6,x7,x8,x9,x0])
    m=sem([x1,x2,x3,x4,x5,x6,x7,x8,x9,x0])
    print(x,'±',m)

rucno(1,2,3,4,5,6,7,8,9,10)
python(1,2,3,4,5,6,7,8,9,10)
