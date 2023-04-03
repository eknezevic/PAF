import particcle as prt
import matplotlib.pyplot as plt

p1=prt.Particle()
p1.init(100,45,0,0,0.01)
print("Domet je {:.2f}m.".format(p1.range()))
p1.plot_trajectory()