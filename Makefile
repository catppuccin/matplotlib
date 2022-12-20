all:
	# Convert template to all flavors
	puccinier --source mplcatppuccin/data/catppuccin_template.txt --output latte frappe macchiato mocha
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/frappe.txt
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/latte.txt
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/macchiato.txt
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/mocha.txt
	mv mplcatppuccin/data/frappe.txt mplcatppuccin/data/frappe.mplstyle
	mv mplcatppuccin/data/latte.txt mplcatppuccin/data/latte.mplstyle
	mv mplcatppuccin/data/macchiato.txt mplcatppuccin/data/macchiato.mplstyle
	mv mplcatppuccin/data/mocha.txt mplcatppuccin/data/mocha.mplstyle

	# Replace mocha by flavor name for cmaps
	sed -i 's/mocha/frappe/g' mplcatppuccin/data/frappe.mplstyle
	sed -i 's/mocha/latte/g' mplcatppuccin/data/latte.mplstyle
	sed -i 's/mocha/macchiato/g' mplcatppuccin/data/macchiato.mplstyle

        # Make catwalks
	python scripts/create_example_plots.py
	catwalk examples/latte/plot.png examples/frappe/plot.png examples/macchiato/plot.png examples/mocha/plot.png -o examples/catwalks/plot.png
	catwalk examples/latte/scatter.png examples/frappe/scatter.png examples/macchiato/scatter.png examples/mocha/scatter.png -o examples/catwalks/scatter.png
	catwalk examples/latte/bar.png examples/frappe/bar.png examples/macchiato/bar.png examples/mocha/bar.png -o examples/catwalks/bar.png
	catwalk examples/latte/patches.png examples/frappe/patches.png examples/macchiato/patches.png examples/mocha/patches.png -o examples/catwalks/patches.png
	catwalk examples/latte/boxplot.png examples/frappe/boxplot.png examples/macchiato/boxplot.png examples/mocha/boxplot.png -o examples/catwalks/boxplot.png
	catwalk examples/latte/palette.png examples/frappe/palette.png examples/macchiato/palette.png examples/mocha/palette.png -o examples/catwalks/palette.png
	catwalk examples/latte/imshow.png examples/frappe/imshow.png examples/macchiato/imshow.png examples/mocha/imshow.png -o examples/catwalks/imshow.png
