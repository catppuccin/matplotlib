"""Soothing pastel theme for matplotlib"""

import warnings

import matplotlib.style
import matplotlib as mpl
import pkg_resources
from .colormaps import get_colormap_from_list

__version__ = pkg_resources.require("catppuccin-matplotlib")[0].version
__author__ = "Bram de Wilde <contact@bramdewilde.com>"
__all__ = []

warning_message = """This package is deprecated, please upgrade to https://github.com/catppuccin/python (pip install catppuccin)
Follow the README in the new repo to upgrade your code (minor edits)

"""

warnings.warn(warning_message, DeprecationWarning, stacklevel=2)

# Register the included stylesheet in the mpl style library
data_path = pkg_resources.resource_filename("mplcatppuccin", "data/")
catppuccin_stylesheets = mpl.style.core.read_style_directory(data_path)
mpl.style.core.update_nested_dict(mpl.style.library, catppuccin_stylesheets)

# Register default colormaps
for palette_name in ["latte", "frappe", "macchiato", "mocha"]:
    cmap = get_colormap_from_list(palette_name, ["base", "blue"])
    mpl.colormaps.register(cmap=cmap, name=palette_name)
