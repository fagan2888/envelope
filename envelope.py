import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform
import numpy as np

# x = np.linspace(-x_range, x_range, x_steps)
x_range = 30
x_steps = 200

# param in range(-param_range, param_range + 1, param_increment)
param_range = 10
param_increment = 2

# Function to be drawn parameterized by t
def func(x, t=1):
    return t * x - t**2

# Lower bound of the graph
y_min = func(x=0, t=param_range) - 10

def subplots():
    "Custom subplots with axes through the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        #ax.spines[spine].set_color('none')
        ax.spines[spine].set_visible(False)
    
    # What's the difference?
    #ax.set_xticks([])
    plt.xticks([])
    #ax.set_yticks([])
    plt.yticks([])
    
    # from http://stackoverflow.com/questions/17646247/how-to-make-fuller-axis-arrows-with-matplotlib
    ax.text(1.01, 0, '$x$', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    ax.text(0, 1.02, '$y$', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')

    return fig, ax

fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-x_range, x_range, x_steps)

for t in range(param_min, param_max + 1, param_increment):
    y = func(x, t)
    ax.plot(x, y, 'k-')

plt.ylim(ymin=y_min)
plt.show()
