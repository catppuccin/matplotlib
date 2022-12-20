import mplcatppuccin
from mplcatppuccin.plots import plot_palette
from mplcatppuccin.palette import palettes, load_color
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import math
import random

print(load_color("mocha", "overlay0"))


mpl.style.use("catppuccin")

# Plot palettes
for palette_name in palettes:
    fig = plot_palette(palette_name)
    plt.savefig(f"examples/{palette_name}_palette.png")

# plt.plot
lines = 5
steps = 100
x = [x / steps for x in range(steps + 1)]
phases = [-x * 0.2 for x in range(lines)]
y_list = [
    [math.sin(x * 2 * math.pi / steps + phase) for x in range(steps + 1)]
    for phase in phases
]

plt.figure()
for idx, y in enumerate(y_list):
    plt.plot(x, y, label=f"Color {idx+1}")
plt.grid()
plt.legend()
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
plt.boxplot([x, y], patch_artist=True)
plt.savefig("examples/boxplot.png")

# plt.bar
bars = 10
x = [0.5 + x for x in range(bars)]
y = [random.random() for _ in range(bars)]

plt.figure()
plt.bar(x, y)
plt.savefig("examples/bar.png")

# plt.patches
fig, ax = plt.subplots()
arrow_1 = mpatches.FancyArrowPatch((0.1, 0.5), (0.9, 0.8), mutation_scale=100)
arrow_2 = mpatches.FancyArrowPatch((0.5, 0.3), (1, 1.5), mutation_scale=100)
ax.add_patch(arrow_1)
ax.add_patch(arrow_2)
plt.savefig("examples/patch.png")

# plt.imshow
# TODO https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
# Follow this to register multiple nice colormaps
