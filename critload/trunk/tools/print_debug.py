icell_debug=1

def print_debug (grid, txt):
	if (icell_debug > -1):
		print(txt + " " + str(grid.get_data(icell_debug)))