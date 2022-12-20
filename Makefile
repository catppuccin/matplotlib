all:
	puccinier --source mplcatppuccin/data/catppuccin_template.txt --output latte frappe macchiato mocha
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/frappe.txt
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/latte.txt
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/macchiato.txt
	sed -i '/^#/! s/\#//g' mplcatppuccin/data/mocha.txt

	mv mplcatppuccin/data/frappe.txt mplcatppuccin/data/frappe.mplstyle
	mv mplcatppuccin/data/latte.txt mplcatppuccin/data/latte.mplstyle
	mv mplcatppuccin/data/macchiato.txt mplcatppuccin/data/macchiato.mplstyle
	mv mplcatppuccin/data/mocha.txt mplcatppuccin/data/mocha.mplstyle
