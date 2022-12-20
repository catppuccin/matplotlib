all:
	puccinier --source mplcatppuccin/data/catppuccin_template.mplstyle --output latte frappe macchiato mocha
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/frappe.mplstyle
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/latte.mplstyle
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/macchiato.mplstyle
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/mocha.mplstyle
