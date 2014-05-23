from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform
from mpl_toolkits.axes_grid.axislines import SubplotZero
import numpy as np

# http://matplotlib.org/users/customizing.html
plt.rcParams['figure.figsize'] = 2.4, 2.4 # inches: default 8, 6
plt.rcParams['lines.linewidth'] = 0.5
plt.rcParams['patch.linewidth'] = 0.5

# x = np.linspace(-x_range, x_range, x_steps)
x_range = 5
x_steps = 200

# param =  -param_range, -param_range + 1/param_grid_num_per_unit, ... , param_range
#param_range, param_grid_num_per_unit = 2, 3
param_range, param_grid_num_per_unit = 3, 5

# To compute a suitable range of the function
param_bound = 16

# Function to be drawn parameterized by t
def func(x, t=1):
    return t * x - t**2

# Lower and upper bounds of the graph
y_min = -x_range ** 2 / (2 * 4)
y_max = x_range ** 2 / 4 + 1

def subplots(x_label='$x$', y_label='$y$'):
    "Custom subplots with axes through the origin"
    # 'patch.facecolor' defined in matplotlib/rcsetup.py with default 'b' (blue)
    # The face of arrow heads drawn with 'patch.edgecolor'
    plt.rcParams['patch.facecolor'] = 'black'
    
    #fig, ax = plt.subplots()
    fig = plt.figure(1)
    #fig = plt.figure(figsize=(2.4,2.4))
    #fig = plt.figure(figsize=(5,5))
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>")
        #ax.axis[direction].set_axisline_style("->", size=1.5)
        ax.axis[direction].set_visible(True)
    
    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)
 
    plt.xticks([])
    plt.yticks([])
    
    # from http://stackoverflow.com/questions/17646247/how-to-make-fuller-axis-arrows-with-matplotlib
    #ax.text(1.06, 0, x_label, transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    #ax.text(0, 1.06, y_label, transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
    ax.text(1.11, 0, x_label, transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    ax.text(0, 1.12, y_label, transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')

    return fig, ax

fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-x_range, x_range, x_steps)

for n in range(-param_range * param_grid_num_per_unit, param_range * param_grid_num_per_unit + 1):
    y = func(x, n / param_grid_num_per_unit)
    ax.plot(x, y, 'k-')

#plt.ylim(ymin=y_min)
#plt.ylim([y_min, y_max])
#ax.set_xlim(left=-x_range, right=x_range)
ax.set_ylim(y_min, y_max)

#aspect = (ax.get_xlim()[1] - ax.get_xlim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0])                     
#ax.set_aspect(aspect)
ax.set_aspect('equal')

#plt.show()
#plt.savefig('envelope1.svg', transparent=True, bbox_inches='tight', pad_inches=0)
#plt.savefig('envelope1.png', transparent=True, bbox_inches='tight', pad_inches=0)
plt.savefig('envelope1.pdf', bbox_inches='tight', pad_inches=0)
