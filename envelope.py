from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform
from mpl_toolkits.axes_grid.axislines import SubplotZero
import numpy as np


SAVEFILE = False
FILNENAME_BASE = 'envelope'
#FILEFORMATS = ('png', 'svg', 'pdf')
FILEFORMAT = 'png'

MULT_SUBPLOTS = True

# To plt.show()
FIGNUM = 0


# Function to be drawn parameterized by t
def func(x, t):
    return t*x - t**2


# pvalue_array = np.linspace(-pvalue_max, pvalue_max, num_pvalues)
pvalue_dicts = [
    {'pvalue_max': 2, 'num_pvalues': 13},
    {'pvalue_max': 3, 'num_pvalues': 31},
    ]
#pvalue_max, pvalue_grids_per_unit = 2, 3
#pvalue_max, pvalue_grids_per_unit = 3, 5


# x = np.array([x_min, x_max])
x_max = 5
x_min = -x_max

# Lower and upper bounds of the graph
y_min = -x_max**2 / (2*4)
y_max = x_max**2 / 4 + 1


# http://matplotlib.org/users/customizing.html
if MULT_SUBPLOTS:
    WSPACE = 0.5
    plt.rcParams['figure.figsize'] = \
        2.4 * len(pvalue_dicts) + WSPACE * (len(pvalue_dicts) - 1), 2.4
else:
    plt.rcParams['figure.figsize'] = 2.4, 2.4  # inches: default 8, 6
plt.rcParams['lines.linewidth'] = 0.5
plt.rcParams['patch.linewidth'] = 0.5
# 'patch.facecolor' defined in matplotlib/rcsetup.py with default 'b' (blue)
# The face of arrow heads drawn with 'patch.facecolor'
plt.rcParams['patch.facecolor'] = 'black'

# Positions of x, y labels
x_label_Pos = [1.11, 0]
y_label_Pos = [0, 1.12]


def customize_axes(ax, x_label_pos=[1, 0], y_label_pos=[0, 1],
                   x_label='$x$', y_label='$y$'):
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

    return ax


x = np.array([x_min, x_max])


def do_plot(ax, pvalue_max, num_pvalues):
    pvalue_array = np.linspace(-pvalue_max, pvalue_max, num_pvalues)
    for t in pvalue_array:
        y = func(x, t)
        ax.plot(x, y, 'k-')

    ax.set_ylim(y_min, y_max)

    ax.set_aspect('equal')


if MULT_SUBPLOTS:
    fig = plt.figure(1)
    fig.subplots_adjust(wspace=WSPACE)  # http://matplotlib.org/faq/howto_faq.html

    axes = []
    for fignum, pvalue_dict in enumerate(pvalue_dicts):
        # SubplotZero(fig, numRows, numCols, plotNum)
        axes.append(SubplotZero(fig, 1, len(pvalue_dicts), fignum+1))
        fig.add_subplot(axes[fignum])
        axes[fignum] = customize_axes(axes[fignum], x_label_Pos, y_label_Pos)
        do_plot(axes[fignum], pvalue_dict['pvalue_max'], pvalue_dict['num_pvalues'])

    if SAVEFILE:
        TRANS = (FILEFORMAT.lower() in ['png', 'svc'])
        plt.savefig(FILNENAME_BASE + '_mult' + '.' + FILEFORMAT.lower(),
                    transparent=TRANS, bbox_inches='tight', pad_inches=0)
    plt.show()

elif SAVEFILE:
    TRANS = (FILEFORMAT.lower() in ['png', 'svc'])
    for fignum, pvalue_dict in enumerate(pvalue_dicts):
        fig = plt.figure(1)
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)
        ax = customize_axes(ax, x_label_Pos, y_label_Pos)

        do_plot(ax, pvalue_dict['pvalue_max'], pvalue_dict['num_pvalues'])
        plt.savefig(FILNENAME_BASE + str(fignum) + '.' + FILEFORMAT.lower(),
                    transparent=TRANS, bbox_inches='tight', pad_inches=0)

else:
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    ax = customize_axes(ax, x_label_Pos, y_label_Pos)

    do_plot(ax, pvalue_dicts[FIGNUM]['pvalue_max'], pvalue_dicts[FIGNUM]['num_pvalues'])
    plt.show()
