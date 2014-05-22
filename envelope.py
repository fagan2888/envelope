import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform
from mpl_toolkits.axes_grid.axislines import SubplotZero
import numpy as np

# x = np.linspace(-x_range, x_range, x_steps)
x_range = 50
x_steps = 200

# param in range(-param_range, param_range + 1, param_increment)
param_range, param_increment = 18, 3
#param_range, param_increment = 24, 2

# To compute a suitable range of the function
param_bound = 16

# Function to be drawn parameterized by t
def func(x, t=1):
    return t * x - t**2

# Lower and upper bounds of the graph
y_min = func(x=0, t=param_bound)
y_max = x_range ** 2 / 4 + 100

def subplots():
    "Custom subplots with axes through the origin"
    #fig, ax = plt.subplots()
    #fig = plt.figure(1)
    fig = plt.figure(figsize=(5,5))
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    
    #ax.axhline(linewidth=1.7, color="k")
    #ax.axvline(linewidth=1.7, color="k")
    
    plt.xticks([])
    plt.yticks([])
    
    # from http://stackoverflow.com/questions/17646247/how-to-make-fuller-axis-arrows-with-matplotlib
    #ax.text(1.01, 0, '$x$', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    #ax.text(0, 1.02, '$y$', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
    ax.text(1.05, 0, '$x$', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    ax.text(0, 1.06, '$y$', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
    
    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)
    
    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)
    
    return fig, ax

fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-x_range, x_range, x_steps)

for t in range(-param_range, param_range + 1, param_increment):
    y = func(x, t)
    ax.plot(x, y, 'k-')

#plt.ylim(ymin=y_min)
#plt.ylim([y_min, y_max])
ax.set_ylim(y_min, y_max)

plt.show()
#plt.savefig('envelope1.svg', transparent=True, bbox_inches='tight', pad_inches=0)
#plt.savefig('envelope1.png', transparent=True, bbox_inches='tight', pad_inches=0)
#plt.savefig('envelope1.pdf', bbox_inches='tight', pad_inches=0)
