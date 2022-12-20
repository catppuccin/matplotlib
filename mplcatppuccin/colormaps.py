from .palette import load_color
from matplotlib.colors import LinearSegmentedColormap


def get_colormap_from_list(palette_name, color_names):
    color_list = [load_color(palette_name, color_name) for color_name in color_names]
    cmap = LinearSegmentedColormap.from_list(palette_name, color_list)
    return cmap
