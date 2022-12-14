import mplcatppuccin
from mplcatppuccin.plots import plot_palette
from mplcatppuccin.palette import palettes
import matplotlib as mpl
import matplotlib.pyplot as plt

import math
import random

# TODO https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
# Follow this to register multiple nice colormaps

mpl.style.use("catppuccin")

# Plot palettes
for palette_name in palettes:
    fig = plot_palette(palette_name)
    plt.savefig(f"examples/{palette_name}_palette.png")

# plt.plot
steps = 100
x = [x / steps for x in range(steps + 1)]
y_1 = [math.sin(x * 2 * math.pi / steps) for x in range(steps + 1)]
y_2 = [math.cos(x * 2 * math.pi / steps) for x in range(steps + 1)]

plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.grid()
plt.savefig("examples/plot.png")

# plt.scatter
points = 50
x = [random.random() for _ in range(points)]
y_1 = [random.random() for _ in range(points)]
y_2 = [random.random() for _ in range(points)]

plt.figure()
plt.scatter(x, y_1)
plt.scatter(x, y_2)
plt.savefig("examples/scatter.png")

# plt.boxplot
points = 50
x = [random.random() for _ in range(points)]
y = [0.5 * random.random() for _ in range(points)]

plt.figure()
plt.boxplot([x, y])
plt.savefig("examples/boxplot.png")

# plt.line
# plt.patches
# plt.legend
# plt.colormap
# plt.show()
