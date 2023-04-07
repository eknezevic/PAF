import particle as prt

p1=prt.Particle(100,45,0,0,0.01)
print('Numericki domet je {:.2f}m, a analiticki {:.2f}m. Odstupanje iznosi {:.2f}m'.format(p1.range(),p1.analiticki(),abs(p1.range()-p1.analiticki())))
p1.plot_trajectory()
p1.reset()

p1=prt.Particle(10,60,0,0,0.01)
print('Numericki domet je {:.2f}m, a analiticki {:.2f}m. Odstupanje iznosi {:.2f}m'.format(p1.range(),p1.analiticki(),abs(p1.range()-p1.analiticki())))
p1.plot_trajectory()
p1.reset()  