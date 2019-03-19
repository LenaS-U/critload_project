# ******************************************************
## Revision "$LastChangedDate: 2019-01-31 12:05:37 +0100 (Thu, 31 Jan 2019) $"
## Date "$LastChangedRevision: 620 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/aquaculture_allocation/trunk/tools/main_allocation.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

#print("Import general_path.")
import os
import sys

# Read the environment parameter with the generalcode directory
generalcode = os.getenv("DGNM_GENERALCODE")
if (generalcode == None):
    print("***** ERROR ******")
    print("Environment parameter DGNM_GENERALCODE is not set.")
    sys.exit(1)
if (not os.path.isdir(generalcode)):
    print("***** ERROR ******")
    print("Environment parameter DGNM_GENERALCODE is not set correctly.")
    print("Environment parameter DGNM_GENERALCODE found: ",generalcode)
    sys.exit(1)
#print("GENERALCODE: ",generalcode)

# Set the generalcode directory in the python path
path = generalcode
if os.path.exists(path):
    sys.path.insert(0, path)
    print(path + " is added to the python search path for modules.")
