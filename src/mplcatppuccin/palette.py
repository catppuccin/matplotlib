import json
import pkg_resources
from pathlib import Path

data_path = Path(pkg_resources.resource_filename("mplcatppuccin", "data/"))
with open(data_path / "palettes.json") as json_file:
    palettes = json.load(json_file)


def load_color(palette_name, color_name, format="hex"):
    return palettes[palette_name][color_name][format]
