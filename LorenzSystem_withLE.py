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
from scipy import stats

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
Stepsize=150000
delta=1e-9
t=np.linspace(0,30,Stepsize)
State0 = [2,3,14]
State1 = [2.0+delta,3,14]
State=odeint(model,State0,t)
State1=odeint(model,State1,t)

# Calulate Lyapunov Exponential
# Linear fit until a range. Slope gives Lyapunov Exponent.
del_z=[]
for i in range(0,len(State)):
    setx= np.sqrt((State1[i][2]-State[i][2])**2 +(State1[i][1]-State[i][1])**2+(State1[i][0]-State[i][0])**2)
    del_z.append(setx)

# To do linear fit we need to ignore flat parts, ie parts after 25 secs. So,
del_z=np.array(del_z)
print (type(t),len(t),type(del_z),len(del_z))
t_new=t[:-25000]
#print (t_new[0],t_new[1])
del_z_new=np.log(del_z[:-25000])
print (min(del_z),max(del_z))
slope, intercept, r_value, p_value, std_err = stats.linregress(t_new,del_z_new)
print (slope,intercept)
line = slope*t_new+intercept
print(min(line),max(line))

plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot(State[:,0],State[:,1],State[:,2], c='r')
ax.plot(State1[:,0],State1[:,1],State1[:,2], c ='b')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("S=10, R=28, B=8/3")


fig,ax1=plt.subplots()

ax1.set_xlabel('Time(s)')
ax1.set_ylabel('Distance between two trajectories')
ax1.semilogy(t,del_z)
ax2=ax1.twinx()
ax2.set_ylabel('Linear Fit')
ax2.plot(t_new,line,color='red')
plt.text(0,1,"Lyapunov Exponent=0.929")

plt.show()










