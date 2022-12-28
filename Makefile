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
	catwalk assets/latte/plot.png assets/frappe/plot.png assets/macchiato/plot.png assets/mocha/plot.png -o assets/catwalks/plot.png
	catwalk assets/latte/scatter.png assets/frappe/scatter.png assets/macchiato/scatter.png assets/mocha/scatter.png -o assets/catwalks/scatter.png
	catwalk assets/latte/bar.png assets/frappe/bar.png assets/macchiato/bar.png assets/mocha/bar.png -o assets/catwalks/bar.png
	catwalk assets/latte/patches.png assets/frappe/patches.png assets/macchiato/patches.png assets/mocha/patches.png -o assets/catwalks/patches.png
	catwalk assets/latte/boxplot.png assets/frappe/boxplot.png assets/macchiato/boxplot.png assets/mocha/boxplot.png -o assets/catwalks/boxplot.png
	catwalk assets/latte/palette.png assets/frappe/palette.png assets/macchiato/palette.png assets/mocha/palette.png -o assets/catwalks/palette.png
	catwalk assets/latte/imshow.png assets/frappe/imshow.png assets/macchiato/imshow.png assets/mocha/imshow.png -o assets/catwalks/imshow.png
