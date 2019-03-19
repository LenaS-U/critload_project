# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/main_critload.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************
## ---------------------------------------------------------------------------
## -
## -    Name:    main_critload.py
## -    Author:  Lena Schulte-Uebbinge and Arthur Beusen
## -    Date:    January 29 2019
## -    Purpose: Calculates the critical load for deposition, groundwater and surface water.
## -
## ---------------------------------------------------------------------------

'''
Calculates the critical load for deposition, groundwater and surface water.
'''
# Python modules
import sys
import os
import traceback
import optparse
import time

# Import Global ("generalcode") modules
import general_path

# Generalcode modules
import ascraster
from error import *

# Local modules
import general_startup
import temp_values
import groundwater
import surfacewater
import deposition
from print_debug import *


def run_critload_model(args):
    '''
    Main function to start the calculation of the critical load.
    '''

    # Parse command-line arguments and set parameters for script
    # Startup logging and runtime start
    params,log,s = general_startup.general_startup(args,prefix="critload")

    # End reading arguments list of the commandline. Start the computation.


    # Print year to screen
    print("YEAR: " + str(params.year))
    
    # Calculate all parameters which are intermediate results.
    temp_values.temp_values(params)    
    
    # Calculate the critical load for groundwater.
    print("RESULTS GROUNDWATER")
    groundwater.calculate(params)

    # Calculate the critical load for surface water.
    print("RESULTS SURFACE WATER")
    surfacewater.calculate(params)

    # Calculate the critical load for deposition.
    print("RESULTS DEPOSITION")
    deposition.calculate(params)
    
    # End of the run.
    log.write_and_print(s.total("Total run"))    
    del log

if (__name__ == "__main__"):
  
    try:
        # Start timer.
        starttime_main = time.time()

        # Calculate the allocation.
        run_critload_model(sys.argv)

        # End timer.
        endtime_main = time.time()
        print('Total simulation time (in s):  ' + str(endtime_main-starttime_main))
    except MyError as val:
        val.write()

    except (optparse.OptionValueError,
            ascraster.ASCIIGridError,
            Exception) as val:
        print(str(val))
        print(str(sys.exc_info()[0]))
        print(traceback.print_exc())
    except:
        print("***** ERROR ******")
        print("main_critload.py failed.")
        print(str(sys.exc_info()[0]))
        print(traceback.print_exc())    
