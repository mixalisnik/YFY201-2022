#HOpacketMat.py:HOWavePacketwiMatplotlibAnimation

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

a=1
oneoverpi=1/(np.sqrt(np.pi))
fig,ax=plt.subplots()
ax.set_xlim(-5,5)
ax.set_ylim(0,1.5)
ax.grid()#Plot a grid
plt.title("Wave Packet Animation in Harmonic Oscillator")
plt.xlabel("x")
plt.ylabel("Probability Density Function")

line,=ax.plot([],[],linewidth=5)
def init():#baseframe
    line.set_data([],[])
    return line

def animate(t):#Called repeatedly
    y=oneoverpi*np.exp(-(x-a*np.cos(5*t))**2)#Plotea0.01t
    line.set_data(x,y)
    return line,

x=np.arange(-5,5,0.01)#range for x values
ani=FuncAnimation(fig,animate,init_func=init,frames=1000,interval=10)
plt.show()


ani.save('C:/Users/mixal/gifs.gif', writer='imagemagick', fps=10)
