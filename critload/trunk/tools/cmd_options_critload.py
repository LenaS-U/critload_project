# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/cmd_options_critload.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# General python modules
import os
import sys
import optparse
import time

# Import own general modules
import cmd_options_general
from error import *

class Input_Critload(cmd_options_general.Input,object):
    '''
    Parse arguments and store them using the optparse module.
    
     Pass sys.argv into class: Input(sys.argv).
     Options will be included in 'options' object of instance of Input_dgnm().
     Call options using:
     
     <instance>.options.<option>
     
     All other commandline arguments will be stored in <instance>.args
    '''
    def start_init(self,list_args):
        # Extract scriptname to set working directory
        scriptname = list_args.pop(0)

        # If an inifile is provided, integrate values into list_args
        if ("--inifile" in list_args):
            # Insert inifile arguments before other commandline arguments.
            # This way commandline options prevail over inifile options
            print("Inifile option found in the command line.")
            list_args = self._parse_inifile(list_args) + list_args      

        usage = "usage: python %prog [options]"
        self._dbg("Argument list: %s" % list_args)
        
        # Debug print of current working directory
        self._dbg("Current workdir: %s" % os.getcwd())
        
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

        (self.options, self.args) = parser.parse_args(args=list_args)
        # Make the same object as self.options, but with only the variable input options.
        # This is needed for writing in the log file.
        (self.options_var, self.args1) = parser.parse_args(args=list_args)
        
             
        # Set ldebug and lss_grw as int parameters:
        self.options.ldebug = int(self.options.ldebug)

        # Switch debugging on/off
        self.set_debug(self.options.ldebug)

        return self,list_args
    
    def __init__(self,list_args):

        # Extract scriptname to set working directory
        scriptname = list_args.pop(0)

        # If an inifile is provided, integrate values into list_args
        if ("--inifile" in list_args):
            # Insert inifile arguments before other commandline arguments.
            # This way commandline options prevail over inifile options
            print("Inifile option found in the command line.")
            list_args = self._parse_inifile(list_args) + list_args    

        usage = "usage: python %prog [options]"
        self._dbg("Argument list: %s" % list_args)
        
        # Debug print of current working directory
        self._dbg("Current workdir: %s" % os.getcwd())
        
        # Initialisation of the OptionParser
        parser = optparse.OptionParser(prog=scriptname,usage=usage)      
               
        # Set defaults for test mode
        parser.set_defaults(root = os.getcwd(),
                            parameter_ini = os.path.join(os.getcwd(), "parameters.ini"),
                            year = 1999,
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

        (self.options, self.args) = parser.parse_args(args=list_args)
        # Make the same object as self.options, but with only the variable input options.
        # This is needed for writing in the log file.
        (self.options_var, self.args1) = parser.parse_args(args=list_args)
             
        # Set ldebug and lss_grw as int parameters:
        self.options.ldebug = int(self.options.ldebug)

        # Switch debugging on/off
        self.set_debug(self.options.ldebug)

        # Check here whether the main input directory exists
        self.validate_directory(self.options.inputdir, bool_write=False)

        # Expand all file names to an absolute reference
        #self.options.root = os.path.join(os.getcwd(), self.options.root)
        self.options.outputdir = os.path.join(self.options.root, self.options.outputdir,str(self.options.year))
        self.options.inputdir = os.path.join(self.options.root, self.options.inputdir,str(self.options.year))
         
        # Read all the default parameter settings out of the parameter.ini
        # Here all the other semi constant parameters for the model are set!
        self._parse_parameter_inifile(self.options,self.options.parameter_ini)

        # Add all the directories to the filenames
        # Area & precipitation surplus
        self.options.filename_gridcell_area = os.path.join(self.options.inputdir,self.options.filename_gridcell_area)
        self.options.filename_agri_area = os.path.join(self.options.inputdir,self.options.filename_agri_area)
        self.options.filename_natural_area = os.path.join(self.options.inputdir,self.options.filename_natural_area)
        self.options.filename_precipitation_surplus = os.path.join(self.options.inputdir,self.options.filename_precipitation_surplus)
        # Inputs & uptake
        self.options.filename_fert_inp = os.path.join(self.options.inputdir,self.options.filename_fert_inp)
        self.options.filename_nfixation_agri = os.path.join(self.options.inputdir,self.options.filename_nfixation_agri)
        self.options.filename_manure_inp = os.path.join(self.options.inputdir,self.options.filename_manure_inp)
        self.options.filename_crop_uptake = os.path.join(self.options.inputdir,self.options.filename_crop_uptake)
        # Emissions & deposition
        self.options.filename_n_deposition = os.path.join(self.options.inputdir,self.options.filename_n_deposition)
        self.options.filename_nh3_em_spread_fert = os.path.join(self.options.inputdir,self.options.filename_nh3_em_spread_fert)
        self.options.filename_nh3_em_spread_manure = os.path.join(self.options.inputdir,self.options.filename_nh3_em_spread_manure)
        self.options.filename_nh3_em_storage = os.path.join(self.options.inputdir,self.options.filename_nh3_em_storage)
        self.options.filename_nh3_em_grazing = os.path.join(self.options.inputdir,self.options.filename_nh3_em_grazing)
        # Budget, runoff, leaching & groundwater: agriculture
        self.options.filename_nsro_ag = os.path.join(self.options.inputdir,self.options.filename_nsro_ag)
        self.options.filename_leaching_ag = os.path.join(self.options.inputdir,self.options.filename_leaching_ag)
        self.options.filename_groundwaterload_ag = os.path.join(self.options.inputdir,self.options.filename_groundwaterload_ag)
        self.options.filename_fraction_recent_groundwaterload_ag = os.path.join(self.options.inputdir,self.options.filename_fraction_recent_groundwaterload_ag)
        # Budget, runoff, leaching & groundwater: natural areas
        self.options.filename_nfixation_nat = os.path.join(self.options.inputdir,self.options.filename_nfixation_nat)
        self.options.filename_nsro_nat = os.path.join(self.options.inputdir,self.options.filename_nsro_nat)
        self.options.filename_leaching_nat = os.path.join(self.options.inputdir,self.options.filename_leaching_nat)
        self.options.filename_groundwaterload_nat = os.path.join(self.options.inputdir,self.options.filename_groundwaterload_nat)
        self.options.filename_fraction_recent_groundwaterload_nat = os.path.join(self.options.inputdir,self.options.filename_fraction_recent_groundwaterload_nat)
        # Point sources & fixed diffuse sources (erosion)
        self.options.filename_n_point_alloch_matter = os.path.join(self.options.inputdir,self.options.filename_n_point_alloch_matter)
        self.options.filename_n_point_wastewater = os.path.join(self.options.inputdir,self.options.filename_n_point_wastewater)
        self.options.filename_n_point_aquaculture = os.path.join(self.options.inputdir,self.options.filename_n_point_aquaculture)
        self.options.filename_n_point_dep_surfacewater = os.path.join(self.options.inputdir,self.options.filename_n_point_dep_surfacewater)
        self.options.filename_n_in_erosion_ag = os.path.join(self.options.inputdir,self.options.filename_n_in_erosion_ag)
        self.options.filename_n_in_erosion_nat = os.path.join(self.options.inputdir,self.options.filename_n_in_erosion_nat)



      
        # If no arguments are provided, print usage
        if len(list_args) == 0:
            print(parser.print_help())
            raise parser.error("No arguments provided.")
                       
        # Display all options in case of debug.
        self._dbg("Start checking the command line arguments")
        # Write all settings to screen
        self._dbg("Command line arguments found:")
        self._dbg(self.options)

        # Check given input parameters
        self.run_checks()
       

    def run_checks(self):
        '''
        Check options
            
        '''
        self.validate_directory(self.options.root, bool_write=False)
       
        # Check here whether the year is found on input directory
        try:
            self.validate_directory(self.options.inputdir, bool_write=False)
        except MyError:
            raise MyError("Directory '%s' does not exist in the input directory." % self.options.year)

        # Create new output directory if necessary
        if not os.path.exists(self.options.outputdir):
            os.makedirs(self.options.outputdir)
            
        self.validate_directory(self.options.outputdir, bool_write=True)

        # Check the input files
        self.validate_file(self.options.filename_gridcell_area)
        self.validate_file(self.options.filename_agri_area)
        self.validate_file(self.options.filename_natural_area)
        self.validate_file(self.options.filename_precipitation_surplus)
        self.validate_file(self.options.filename_fert_inp)
        self.validate_file(self.options.filename_nfixation_agri)
        self.validate_file(self.options.filename_manure_inp)
        self.validate_file(self.options.filename_crop_uptake)
        self.validate_file(self.options.filename_n_deposition)
        self.validate_file(self.options.filename_nh3_em_spread_fert)
        self.validate_file(self.options.filename_nh3_em_spread_manure)
        self.validate_file(self.options.filename_nh3_em_storage)
        self.validate_file(self.options.filename_nh3_em_grazing)
        self.validate_file(self.options.filename_nsro_ag)
        self.validate_file(self.options.filename_leaching_ag)
        self.validate_file(self.options.filename_groundwaterload_ag)
        self.validate_file(self.options.filename_fraction_recent_groundwaterload_ag)
        self.validate_file(self.options.filename_nfixation_nat)
        self.validate_file(self.options.filename_nsro_nat)
        self.validate_file(self.options.filename_leaching_nat)
        self.validate_file(self.options.filename_groundwaterload_nat)
        self.validate_file(self.options.filename_fraction_recent_groundwaterload_nat)
        self.validate_file(self.options.filename_n_point_alloch_matter)
        self.validate_file(self.options.filename_n_point_wastewater)
        self.validate_file(self.options.filename_n_point_aquaculture)
        self.validate_file(self.options.filename_n_point_dep_surfacewater)
        self.validate_file(self.options.filename_n_in_erosion_ag)
        self.validate_file(self.options.filename_n_in_erosion_nat)
 
        
        # Stop checking
        return
        


