import json
import pkg_resources
from pathlib import Path

data_path = Path(pkg_resources.resource_filename("mplcatppuccin", "data/"))
with open(data_path / "palettes.json") as json_file:
    palettes = json.load(json_file)
