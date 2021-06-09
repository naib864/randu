import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,7.5))
ax = fig.add_axes([0,0,1,1], projection='3d') # use 3d plotting

#----------------------------layout-------------------------------------

plt.style.use('ggplot')
fig.set_facecolor('w')
plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)
plt.xticks(fontname='Ubuntu Mono', fontsize=12)
plt.yticks(fontname='Ubuntu Mono', fontsize=12)

#-----------------------------------------------------------------------

x, y, z = np.loadtxt("dat/randu.dat", delimiter='\t', unpack=True) # load data from file

ax.plot(x,y,z,'.')
ax.view_init(45,-45) # set initial view
plt.draw()
plt.pause(2) # wait 2 secs, then start rotating

for angle in range(45, 110): # rotate the view
    ax.view_init(angle,-45)
    plt.draw()
    plt.pause(.01)

plt.pause(2)

for angle in range(0, 90): # rotate the view
    ax.view_init(45,angle)
    plt.draw()
    plt.pause(.01)

plt.pause(2)

ax.view_init(45,60) # view planes
plt.show()
