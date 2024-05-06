import numpy as np
from malplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sin={"s1":[3,5],"s2":[6,11],"s3":[7,5],"s4":[7,14],"s5":[1,2]}
k=input("enter sinusodal key to generate")
if sindict[k]:
x=sin[k][0]*np.sin(2*np.pi*sin[k][1]*t)
plt.plot[k][0]*np.sin(2*np.pi*sin[k][1]*t)
plt.plot(t,x)
plt.show()
