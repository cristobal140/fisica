from __future__ import print_function
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time
e = 2.718281
a = 3
theta = np.linspace(-6 * np.pi, 6 * np.pi, 50)

def generate(X, Y):
    '''
    Generates Z data for the points in the X, Y meshgrid and parameter phi.
    '''
    R = a * (e**(np.sin(45) * (1/np.tan(30)*theta))) * np.cos(theta)
    return  R

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make the X, Y meshgrid.
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
print ('xs:', xs)
print ('ys:', ys)
X, Y = np.meshgrid(xs, ys)
print ('y:', Y)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-2,50)

# Begin plotting.
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    # If a line collection is already remove it before drawing.
    if wframe:
        ax.collections.remove(wframe)

    # Plot the new wireframe and pause briefly before continuing.
    Z = generate(X, Y)
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)

print('Average FPS: %f' % (100 / (time.time() - tstart)))