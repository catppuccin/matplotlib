import matplotlib.pyplot as plt
from .palette import palettes


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
            color_name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    return fig
