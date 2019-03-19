# ******************************************************
## Revision "$LastChangedDate: 2019-01-31 12:05:37 +0100 (Thu, 31 Jan 2019) $"
## Date "$LastChangedRevision: 620 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/aquaculture_allocation/trunk/tools/main_allocation.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# Specify debug_cell which results are printed to screen. When icell_debug < -1 then there is no writing to screen.
icell_debug=-1

def print_debug (grid, txt):
    if (icell_debug > -1):
        print(txt + " " + str(grid.get_data(icell_debug)))
