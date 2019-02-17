"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import mpl_toolkits.mplot3d.axes3d as p3
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
    return [dxdt,dydt,dzdt]

State0 = [1,1,1]


import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

length=30

def Gen_RandLine(length, dims):
    
    lineData = np.empty((dims,length*80))
    lineData[:, 0] = State0
    print (len(lineData[1]))
    for i in range(1, len(lineData[1])):
        t=np.linspace(0,length,80*length)
        State=odeint(model,State0,t)
        lineData[:, i] = State[i]
    return lineData

def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

#Set up formatting for movie files. Higher fps=faster. 
plt.rcParams['animation.ffmpeg_path'] ='C:\\ffmpeg\\bin\\ffmpeg'
FFwriter = animation.FFMpegWriter(fps = 150)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)


# Fifty lines of random 3-D lines
data = [Gen_RandLine(length, 3) for index in range(1)]

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([-30.0, 20.0])
ax.set_xlabel('X')

ax.set_ylim3d([-20.0, 30.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-10.0, 50.0])
ax.set_zlabel('Z')

ax.set_title('Lorenz Animation')

# Creating the Animation object
# 2500 below is length*80 =2400 and little more than that
line_ani = animation.FuncAnimation(fig, update_lines, 2500, fargs=(data, lines),
                                   interval=1, blit=False)
line_ani.save('Butterfly.mp4', writer=FFwriter)
plt.show()
