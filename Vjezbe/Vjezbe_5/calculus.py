import numpy as np

# prvi zadatak

def d_u_tocki(f, x, dx):
    derivacija = (f(x+dx)-f(x))/dx
    return derivacija

def d_u_intervalu(f, a, b, dx, threestep=True):
    interval = np.arange(a, b, dx)
    derivacije = []
    if threestep==True:
        for x in interval:
            derivacije.append((f(x+dx)-f(x-dx))/(2*dx))
    elif threestep==False:
        for x in interval:
            derivacije.append((f(x+dx)-f(x))/dx)
    return interval, derivacije

# drugi zadatak

def integr(f, a, b, N):
    dx=abs((b-a)/N)
    g_medja = 0
    d_medja = 0
    interval = np.arange(a, b, dx)
    for x in interval:
        g_medja+=f(x+dx)*dx
        d_medja+=f(x)*dx
    return g_medja,d_medja

def trapezna_integr(f, a, b, N):
    dx=abs((b-a)/N)
    interval = np.arange(a, b, dx)
    integral = 0
    for x in interval:
        integral += (f(x)+(f(x+dx)-f(x))/2)*dx
    return integral