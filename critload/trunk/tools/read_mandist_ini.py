# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/read_mandist_ini.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# General python modules
import os

# Import own general modules
import my_sys

def read_mandist_ini(inputdir):
    '''
    Read the ini file from the mandist directory and stores it in a dictionary.
    '''

    # Read manure.ini file
    lines = my_sys.my_readfile(os.path.join(inputdir,'manure.ini'))

    dict_out = {}
    for line in lines:
        fields = line.split(":")
        if (len(fields) != 2):
            # Skip this line
            continue
        else:
            dict_out[fields[0].strip()] = fields[1].strip()

    return dict_out
