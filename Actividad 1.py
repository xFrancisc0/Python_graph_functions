import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(-1.5,1.5,0.1)
s = 1+np.sin(2*np.pi*t)
c = 1+np.cos(2*np.pi*t)
ta= 1+np.tan(2*np.pi*t)


fig, axarr = plt.subplots(2, 2)

g11 = axarr[0, 0].plot(t, s)
g12 = axarr[0, 0].plot(t, c)
axarr[0, 0].set_title('Funcion Seno y Coseno')
axarr[0, 0].grid()
axarr[0, 1].plot(t, ta)
axarr[0, 1].set_title('Funcion Tangente')
axarr[0, 1].grid()
g31 = axarr[1, 0].plot(t,s)
g32 = axarr[1, 0].plot(t,c)
g33 = axarr[1, 0].plot(t,ta)
axarr[1, 0].set_title('Funcion Seno, Coseno y Tangente')
axarr[1, 0].grid()

fig.savefig("Figura.png")
plt.show()