import mplcatppuccin
from mplcatppuccin.plots import plot_palette, example_plots
from mplcatppuccin.palette import palettes
import matplotlib as mpl
import matplotlib.pyplot as plt

from pathlib import Path

# Plot palettes
dpi = 200
for palette_name in palettes:
    mpl.style.use(palette_name)
    palette_path = Path("examples") / palette_name

    # Plot palette separately
    fig = plot_palette(palette_name)
    fig.savefig(palette_path / "palette.png", dpi=dpi)

    # Plot examples
    for filename, plot_function in example_plots.items():
        if filename == "imshow":
            fig = plot_function(palette_name)
        else:
            fig = plot_function()
        fig.savefig(palette_path / f"{filename}.png", dpi=dpi)
        plt.close()
