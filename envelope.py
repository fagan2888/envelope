from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform
from mpl_toolkits.axes_grid.axislines import SubplotZero
import numpy as np

# http://matplotlib.org/users/customizing.html
plt.rcParams['figure.figsize'] = 2.4, 2.4  # inches: default 8, 6
plt.rcParams['lines.linewidth'] = 0.5
plt.rcParams['patch.linewidth'] = 0.5
# 'patch.facecolor' defined in matplotlib/rcsetup.py with default 'b' (blue)
# The face of arrow heads drawn with 'patch.facecolor'
plt.rcParams['patch.facecolor'] = 'black'


SAVEFILE = True
FILNENAME_BASE = 'envelope'
#FILEFORMATS = ('png', 'svg', 'pdf')
FILEFORMAT = 'pdf'

# To plt.show()
FIGNUM = 0


# Function to be drawn parameterized by t
def func(x, t=1):
    return t*x - t**2


# param = -param_max, -param_max + 1/param_grids_per_unit,
#         ... , param_max
paramdicts = [
    {'param_max': 2, 'param_grids_per_unit': 3},
    {'param_max': 3, 'param_grids_per_unit': 5},
    ]
#param_max, param_grids_per_unit = 2, 3
#param_max, param_grids_per_unit = 3, 5


# x = np.linspace(-x_range, x_range, x_steps)
x_range = 5
x_steps = 200

# Lower and upper bounds of the graph
y_min = -x_range**2 / (2*4)
y_max = x_range**2 / 4 + 1


# Positions of x, y labels
x_label_Pos = [1.11, 0]
y_label_Pos = [0, 1.12]


def subplots(x_label_pos=[1, 0], y_label_pos=[0, 1], x_label='$x$', y_label='$y$'):
    "Custom subplots with axes through the origin"

    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)  # numRows, numCols, plotNum

    fig.add_subplot(ax)

    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>")  # "->" otherwise
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])

    # from http://stackoverflow.com/questions/17646247/how-to-make-fuller-axis-arrows-with-matplotlib
    ax.text(x_label_pos[0], x_label_pos[1], x_label,
            transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    ax.text(y_label_pos[0], y_label_pos[1], y_label,
            transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')

    return fig, ax


x = np.linspace(-x_range, x_range, x_steps)


def do_plot(param_max, param_grids_per_unit):
    fig, ax = subplots(x_label_Pos, y_label_Pos)  # Call the local version, not plt.subplots()

    for n in range(-param_max * param_grids_per_unit, param_max * param_grids_per_unit + 1):
        y = func(x, n / param_grids_per_unit)
        ax.plot(x, y, 'k-')

    ax.set_ylim(y_min, y_max)

    ax.set_aspect('equal')


if SAVEFILE:
    TRANS = (FILEFORMAT.lower() in ['png', 'svc'])
    for fignum, paramdict in enumerate(paramdicts):
        do_plot(paramdict['param_max'], paramdict['param_grids_per_unit'])
        plt.savefig(FILNENAME_BASE + str(fignum) + '.' + FILEFORMAT.lower(),
                    transparent=TRANS, bbox_inches='tight', pad_inches=0)
else:
    do_plot(paramdicts[FIGNUM]['param_max'], paramdicts[FIGNUM]['param_grids_per_unit'])
    plt.show()
