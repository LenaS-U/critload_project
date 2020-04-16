# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/print_debug.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# Specify debug_cell which results are printed to screen. When icell_debug < -1 then there is no writing to screen.
icell_debug=41792

def print_debug (grid, txt):
    if (icell_debug > -1):
        print(txt + " " + str(grid.get_data(icell_debug)))
