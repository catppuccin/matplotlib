"""Soothing pastel theme for matplotlib"""

import matplotlib.style
import matplotlib as mpl
import pkg_resources

__version__ = pkg_resources.require("mplcatppuccin")[0].version
__author__ = "Bram de Wilde <contact@bramdewilde.com>"
__all__ = []

# Register the included stylesheet in the mpl style library
data_path = pkg_resources.resource_filename("mplcatppuccin", "data/")
catppuccin_stylesheets = mpl.style.core.read_style_directory(data_path)
mpl.style.core.update_nested_dict(mpl.style.library, catppuccin_stylesheets)
