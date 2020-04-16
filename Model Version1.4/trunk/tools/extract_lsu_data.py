import os
import sys

import general_path


import ascraster
import general_class

data_file = 'C:/Users/schul028/OneDrive - WageningenUR/critload_project/lsu data/figure15data.dat'

# Read asciigrid (world)
grid = ascraster.Asciigrid(ncols=720,nrows=360,nodata_value=-1,xllcorner=-180,yllcorner=-90,cellsize=0.5)


# Read file with coordinates
data_org = general_class.read_general_file(data_file,sep=" ",out_type="list")
#coordin = [[5.2,52.3]]

# Get index in the grid for this coordinate
for item in range(len(data_org)):
    x = float(data_org[item].get_val("Lon"))
    y = float(data_org[item].get_val("Lat"))
    val = float(data_org[item].get_val("LSUfao"))
    icell = grid.get_index_from_coordin(x,y)

    # Set new data
    if (icell > -1):
        grid.set_data(icell, val)

# Effe iets meer waarden in de kaart gooien.
#for icell in range(5000,10000):
#    grid.set_data(icell,500.)

# Write to file.
grid.write_ascii_file("LSUfao.asc")


