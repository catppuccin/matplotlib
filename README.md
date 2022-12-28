<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://matplotlib.org/">Matplotlib</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/brambozz/matplotlib-catppuccin/stargazers"><img src="https://img.shields.io/github/stars/brambozz/matplotlib-catppuccin?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/brambozz/matplotlib-catppuccin/issues"><img src="https://img.shields.io/github/issues/brambozz/matplotlib-catppuccin?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/brambozz/matplotlib-catppuccin/contributors"><img src="https://img.shields.io/github/contributors/brambozz/matplotlib-catppuccin?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/plot.png"/>
</p>

## Previews

<details>
<summary>Line plot</summary>
<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/plot.png"/>
</details>

<details>
<summary>Bar plot</summary>
<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/bar.png"/>
</details>

<details>
<summary>Box plot</summary>
<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/boxplot.png"/>
</details>

<details>
<summary>Scatter plot</summary>
<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/scatter.png"/>
</details>

<details>
<summary>Patchs</summary>
<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/patches.png"/>
</details>

<details>
<summary>Colormap</summary>
<img src="https://raw.githubusercontent.com/brambozz/matplotlib-catppuccin/main/examples/catwalks/imshow.png"/>
</details>

## Usage

1. `pip install mplcatppuccin`
2. Import the module to register the stylesheets and colormaps

```python
import mplcatppuccin
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use("mocha")
plt.plot([0,1,2,3], [1,2,3,4])
plt.show()
```

3. Mix it with different stylesheets!
```python
mpl.style.use(["ggplot", "mocha"])
plt.plot([0,1,2,3], [1,2,3,4])
plt.show()
```

## 💝 Thanks to

- [mplcyberpunk](https://github.com/dhaitz/mplcyberpunk)
- [matplotlib-stylesheets](https://github.com/dhaitz/matplotlib-stylesheets)
- [oldplotlib](https://github.com/ckinzthompson/oldplotlib/blob/main/oldplotlib.py)
- [vapeplot](https://github.com/dantaki/vapeplot/blob/master/vapeplot/vapeplot.py)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/brambozz/matplotlib-catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
