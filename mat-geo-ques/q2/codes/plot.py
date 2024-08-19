#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/aditya/Desktop/python/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

#Given points
P = np.array(([3,6])).reshape(-1,1)
Q = np.array(([-12,-3])).reshape(-1,1)


#Ratio


#Point
#print(R)

#Generating all lines

x_PQ = line_gen(P,Q)



#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')

#Labeling the coordinates
tri_coords = np.block([[P,Q]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.1f}, {tri_coords[1,i]:.1f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# use set_position
ax = plt.gca()
plt.annotate(f'{-7.0,0.0}',(-7,0),textcoords="offset points", xytext=(20,-10),ha='right') # horizontal alignment can be left, right or center
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# set the y-spine
ax.spines['bottom'].set_position('zero')

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()
plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/fig.png')
#subprocess.run(shlex.split("termux-open chapters/10/7/2/1/figs/fig.pdf"))
#else
plt.show()
