"""
Model Lorenz system. Gives two plots to show how they evolve with time.

dx/dt=S(y-x)
dy/dt=x(R-z)-y
dz/dt=xy - Bz

"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

S = 10
R = 28
B = 8.0/3.0
def model(State,t):
    x=State[0]
    y=State[1]
    z=State[2]
    dxdt=S*(y-x)
    dydt=x*(R-z)-y
    dzdt=x*y -B*z
    return [dxdt,dydt,dzdt] # Returns x,y,z positions
t=np.linspace(0,50,15000)
State0 = [1,1,1]
State1 = [1.001,1,1]
State=odeint(model,State0,t)
State1=odeint(model,State1,t)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(State[:,0],State[:,1],State[:,2], c='r')
ax.plot(State1[:,0],State1[:,1],State1[:,2], c ='b')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("S=10, R=28, B=8/3")

plt.show()
