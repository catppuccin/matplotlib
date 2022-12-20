import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from .palette import palettes
import math
import random

# TODO fix random seeds inside all functions


def plot_palette(palette_name):
    palette = palettes[palette_name]

    # Create figure and adjust figure height to number of colormaps
    nrows = len(palette)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    axs[0].set_title(palette_name, fontsize=14)

    for ax, color_name in zip(axs, palette):
        ax.hlines(0, 0, 1, colors=palette[color_name]["hex"], linewidth=15)
        ax.text(
            -0.01,
            0.5,
            f"{color_name} {palette[color_name]['hex']}",
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    fig.tight_layout()

    return fig


def example_plot():
    lines = 5
    steps = 100
    x = [x / steps for x in range(steps + 1)]
    phases = [-x * 0.2 for x in range(lines)]
    y_list = [
        [math.sin(x * 2 * math.pi / steps + phase) for x in range(steps + 1)]
        for phase in phases
    ]

    fig = plt.figure()
    for idx, y in enumerate(y_list):
        plt.plot(x, y, label=f"Color {idx+1}")
    plt.grid()
    plt.legend()

    return fig


def example_scatter():
    random.seed(0)
    points = 50
    x = [random.random() for _ in range(points)]
    y_1 = [random.random() for _ in range(points)]
    y_2 = [random.random() for _ in range(points)]

    fig = plt.figure()
    plt.scatter(x, y_1)
    plt.scatter(x, y_2)

    return fig


def example_boxplot():
    random.seed(0)
    points = 50
    x = [random.random() for _ in range(points)]
    y = [0.5 * random.random() for _ in range(points)]

    fig = plt.figure()
    plt.boxplot([x, y], patch_artist=True)
    return fig


def example_bar():
    random.seed(0)
    bars = 10
    x = [0.5 + x for x in range(bars)]
    y = [random.random() for _ in range(bars)]

    fig = plt.figure()
    plt.bar(x, y)
    return fig


def example_patches():
    fig, ax = plt.subplots()
    arrow_1 = mpatches.FancyArrowPatch((0.1, 0.5), (0.9, 0.8), mutation_scale=100)
    arrow_2 = mpatches.FancyArrowPatch((0.5, 0.3), (1, 1.5), mutation_scale=100)
    ax.add_patch(arrow_1)
    ax.add_patch(arrow_2)

    return fig


example_plots = {
    "plot": example_plot,
    "scatter": example_scatter,
    "boxplot": example_boxplot,
    "bar": example_bar,
    "patches": example_patches,
}
