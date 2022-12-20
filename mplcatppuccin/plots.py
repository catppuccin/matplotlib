import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from .palette import palettes
from .colormaps import get_colormap_from_list
import math
import random
import numpy as np

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
    bars = 4
    points = 50
    x = [
        [scale * random.random() for _ in range(points)]
        for scale in [random.random() for _ in range(bars)]
    ]

    fig = plt.figure()
    plt.boxplot(x, patch_artist=True)
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
    arrow_1 = mpatches.FancyArrowPatch((0, 1), (1, 0), mutation_scale=100)
    arrow_2 = mpatches.FancyArrowPatch((0, 0), (1, 1), mutation_scale=100)
    ax.set_xlim([-0.1, 1.1])
    ax.set_ylim([-0.1, 1.1])
    ax.add_patch(arrow_1)
    ax.add_patch(arrow_2)

    return fig


def example_imshow(palette_name):
    data = np.random.randint(10, size=(30, 30))
    fig, ax = plt.subplots()
    im = ax.imshow(data)
    ax.tick_params(
        left=False, right=False, labelleft=False, labelbottom=False, bottom=False
    )

    fig.colorbar(im, ax=ax, ticks=[])

    return fig


def plot_examples(colormaps):
    """
    Helper function to plot data with associated colormap.
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    n = len(colormaps)
    fig, axs = plt.subplots(
        1, n, figsize=(n * 2 + 2, 3), constrained_layout=True, squeeze=False
    )
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()


example_plots = {
    "plot": example_plot,
    "scatter": example_scatter,
    "boxplot": example_boxplot,
    "bar": example_bar,
    "patches": example_patches,
    "imshow": example_imshow,
}
