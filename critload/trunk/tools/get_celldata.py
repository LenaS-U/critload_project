# ******************************************************
## Revision "$LastChangedDate: 2019-03-26 20:34:04 +0100 (Tue, 26 Mar 2019) $"
## Date "$LastChangedRevision: 629 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/get_celldata.py $"
# ******************************************************
'''
Test script to test the functionality of ascraster.
'''
import os
import sys
import general_path

import ascraster
import my_sys

coordinate = [-81.25,39.75]

# First argument is the input directory of the raster files.
inputdir = sys.argv[1]


if not os.path.isdir(inputdir):
    print("STOP: Input directory does not exist." )

# Get for a cell the data value for all grid files.
listdir = os.listdir(inputdir)

for file1 in sorted(listdir):
    filename = os.path.join(inputdir,file1)
    ldata = False
    if (os.path.splitext(file1)[1].upper() == ".ASC"):
        # Use this file
        ldata = True
    elif (os.path.splitext(file1)[1].upper() == ".GZ"):
        if (os.path.splitext(os.path.splitext(file)[0])[1].upper() == ".ASC"):
            ldata = True
    elif (os.path.splitext(file1)[1].upper() == ".MAP"):
        ldata = True
    # Do it.
    if (ldata):
        # Open grid
        grid = ascraster.Asciigrid(ascii_file=filename)
        ind = grid.get_index_from_coordin(coordinate[0],coordinate[1])
        print(file1 + ": " + str(grid.get_data(ind)))

