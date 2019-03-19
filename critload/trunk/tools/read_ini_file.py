# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/read_ini_file.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************
# Import general python modules
import os
import sys
import optparse
import time
import copy
import random

# Import own general modules
import ascraster
from error import *
import general_class
import cmd_options_general

def start_init(list_args):

    # Create params object
    obj = cmd_options_general.Input()

    # Extract scriptname to set working directory
    scriptname = list_args.pop(0)

    # If an inifile is provided, integrate values into list_args
    if ("--inifile" in list_args):
        # Insert inifile arguments before other commandline arguments.
        # This way commandline options prevail over inifile options
        print("Inifile option found in the command line.")
        list_args = obj._parse_inifile(list_args) + list_args    

    usage = "usage: python %prog [options]"
    print("Argument list: %s" % list_args)
        
    # Debug print of current working directory
    print("Current workdir: %s" % os.getcwd())
        
    # Initialisation of the OptionParser
    parser = optparse.OptionParser(prog=scriptname,usage=usage)      
               
    # Set defaults for test mode
    parser.set_defaults(root = os.getcwd(),
                        parameter_ini = os.path.join(os.getcwd(), "parameters.ini"),
                        year = 2000,
                        outputdir = os.path.join(os.getcwd(), "..","output"),
                        inputdir = os.path.join(os.getcwd(), "..","input"),
                        ldebug = 0
                        )
    parser.add_option("--root",
                          type = "string",
                          dest = "root",
                          action="store",
                         help="Not used anymore.")
    parser.add_option("--parameter_ini",
                          type = "string",
                          dest = "parameter_ini",
                          action="store",
                          help="Full path to file with all 'constant' parameter values like filenames etc..")                            
    parser.add_option("--year",
                          type = "int",
                          dest = "year",
                          action="store",
                          help="Year of the simulation.")
    parser.add_option("--inputdir",
                          type = "string",
                          dest = "inputdir",
                          action="store",
                          help="Input directory with the IMAGE gridinformation.")
    parser.add_option("--outputdir",
                          type = "string",
                          dest = "outputdir",
                          action="store",
                          help="Output directory.")
    parser.add_option("--ldebug",
                          dest = "ldebug",
                          action="store",
                          help="Print debug messages 1: yes, 0: no.")
    parser.add_option("--inifile",
                          type = "string",
                          dest = "inifile",
                          action="store",
                          help="""Path to ini-file.
                          In inifile use commandline options, followed by '=', followed by argument, e.g. --outputdir = OECD.
                          Comments must be preceded by '#'. Everything after '#' on a line will be ignored by the parser."""
                          )

    (obj.options, obj.args) = parser.parse_args(args=list_args)
    # Make the same object as self.options, but with only the variable input options.
    # This is needed for writing in the log file.
    (obj.options_var, obj.args1) = parser.parse_args(args=list_args)
             
    # Set ldebug and lss_grw as int parameters:
    obj.options.ldebug = int(obj.options.ldebug)

    # Read all the default parameter settings out of the parameter.ini
    # Here all the other semi constant parameters for the model are set!
    obj._parse_parameter_inifile(obj.options,obj.options.parameter_ini)

    return obj
