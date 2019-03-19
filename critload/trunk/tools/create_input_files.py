# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/create_input_files.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

'''
This main routine copies files from different directories to create one year for an input directory.
'''

# Python modules
import os
import sys
import traceback

# Import Global ("generalcode") modules
import general_path

# Generalcode modules
import ascraster
from error import *
import get_versioninfo
import my_sys
import my_logging

# Local modules
import read_ini_file
import read_mandist_ini

# Set the directory for the source locations.
gnm_inputdir = r"/data/beusena/globalnutrients/scen_input/SSPs/history_2005"
gnm_outputdir = r"/data/beusena/tmp/output_history_110"
mandistdir = r"/data/beusena/mandist/preproc_nbal/SSP2_18feb2018/mandist_files"
water_inputdir = r"/data/beusena/globalnutrients/water_input/pcrglobwb_100"


def fr_recent_grw(params,runoff):
    fraction = (params.fr_max_recent_grw/ params.max_runoff) * runoff
    return min(max(0.0,fraction),params.fr_max_recent_grw)

def write_log(inputdir,mandistdir,gnm_inputdir,gnm_outputdir,water_inputdir):

    log = my_logging.Log(inputdir,"create_input_files.log")
    print("Log will be written to %s" % log.logFile)
    
    # Write parameter settings and version information to log file
    log.write_and_print("Starting run....")
    log.write("#############################################",print_time=False,lcomment=False)
    log.write("MANDIST DIRECTORY: " + mandistdir)
    log.write("GNM INPUT DIRECTORY: " + gnm_inputdir)
    log.write("GNM OUTPUT DIRECTORY: " + gnm_outputdir)
    log.write("WATER INPUT DIRECTORY: " + water_inputdir)
    log.write("#############################################",print_time=False,lcomment=False)               

    # Write svn information of input and scripts to log file.

    log.write("******************************************************",print_time=True,lcomment=True)
    dirname = os.getcwd()   
    log.write("# Version information of main script.",print_time=True,lcomment=True)
    get_versioninfo.print_versioninfo(os.path.join(dirname,"create_input_files.py"),log)

    # Write version information of generalcode directory
    dirname = os.getenv("DGNM_GENERALCODE")
    versionnumber, filename_versionnumber = get_versioninfo.get_versioninfo_files(dirname)
    log.write("# Version information of generalcode directory.",print_time=True,lcomment=True)
    get_versioninfo.print_versioninfo(os.path.join(dirname,filename_versionnumber),log)
    
    # Close logging file
    del log


def get_all_files(args):
    '''
    Get all files to create one year of the input directory to calculate of the critical load.
    '''

    # Parse command-line arguments and set parameters for script
    # Startup logging and runtime start
    param = read_ini_file.start_init(args)
    params = param.options

    # End reading arguments list of the commandline. Start the computation.
    # Check source directories.
    if not os.path.exists(mandistdir):
        raise MyError("Directory '%s' does not exist" % mandistdir)
    if not os.path.exists(gnm_outputdir):
        raise MyError("Directory '%s' does not exist" % gnm_outputdir)
    if not os.path.exists(gnm_inputdir):
        raise MyError("Directory '%s' does not exist" % gnm_inputdir)
    if not os.path.exists(water_inputdir):
        raise MyError("Directory '%s' does not exist" % water_inputdir)
    if not os.path.exists(os.path.join(mandistdir,"in"+str(params.year))):
        raise MyError("Input for year '%s' is not found on directory '%s'" % (params.year,mandistdir))
    if not os.path.exists(os.path.join(mandistdir,"out"+str(params.year))):
        raise MyError("Output for year '%s' is not found on directory '%s'" % (params.year,mandistdir))
    if not os.path.exists(os.path.join(gnm_outputdir,str(params.year))):
        raise MyError("Output for year '%s' is not found on directory '%s'" % (params.year,gnm_outputdir))
    if not os.path.exists(os.path.join(gnm_inputdir,str(params.year))):
        raise MyError("Input for year '%s' is not found on directory '%s'" % (params.year,gnm_inputdir))
    if not os.path.exists(os.path.join(water_inputdir,str(params.year))):
        raise MyError("Input for year '%s' is not found on directory '%s'" % (params.year,water_inputdir))

    # Change the input and source directories to this year.
    inputdir = os.path.join(params.root, params.inputdir,str(params.year))
    mandistdir_in = os.path.join(mandistdir,"in"+str(params.year))
    mandistdir_out = os.path.join(mandistdir,"out"+str(params.year))
    gnmdir_in = os.path.join(gnm_inputdir,str(params.year))
    gnmdir_out = os.path.join(gnm_outputdir,str(params.year))
    waterdir = os.path.join(water_inputdir,str(params.year))

    # Create input directory for this year when it does not exist.
    if not os.path.exists(inputdir):
        os.makedirs(inputdir)

    # Make a log file
    write_log(inputdir,mandistdir,gnm_inputdir,gnm_outputdir,water_inputdir)

    # Read mandist ini file (manure.ini)
    mandist_files_dict = read_mandist_ini.read_mandist_ini(mandistdir_in)

    # Create landmask
    filename = os.path.join(mandistdir_in,mandist_files_dict["LAND AREA ASC FILE"])
    mask = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Make all values one.
    for icell in range(mask.length):
        val = mask.get_data(icell)
        if (val != None):
            mask.set_data(icell,1)

    # Areas in ha.
    # Read cellarea file in m2.
    area = ascraster.Asciigrid(ascii_file = os.path.join(params.root,"..","fix_input","cellarea30.asc"),numtype = float)
    # Convert to ha
    area.multiply(0.0001)

    # Calculate the area agricultural land
    filename = os.path.join(mandistdir_in,mandist_files_dict["LAND AREA ASC FILE"])
    landarea = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(mandistdir_in,mandist_files_dict["INPUT INTENSIVE GRASS GRID FILE"])
    grass_int = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(mandistdir_in,mandist_files_dict["INPUT EXTENSIVE GRASS GRID FILE"])
    grass_ext = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(mandistdir_in,mandist_files_dict["INPUT INTENSIVE CROP GRID FILE"])
    crop_int = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(mandistdir_in,mandist_files_dict["INPUT EXTENSIVE CROP GRID FILE"])
    crop_ext = ascraster.Asciigrid(ascii_file = filename,numtype = float)

    # Landarea is in km2, the different landuse types are in percentages, so result is in ha.
    grass_int.multiply(landarea)
    grass_ext.multiply(landarea)
    crop_int.multiply(landarea)
    crop_int.multiply(landarea)

    landarea = ascraster.duplicategrid(grass_int)
    landarea.add(grass_ext)
    landarea.add(crop_int)
    landarea.add(crop_ext)

    # Create agricultural land and non-agricultural land.
    natarea = ascraster.duplicategrid(landarea)
    for icell in range(landarea.length):
        lndarea = landarea.get_data(icell)
        if (lndarea == None):
            area.set_data(icell,area.nodata_value)
        else:
            cellarea = area.get_data(icell,0.0)
            lndarea = min(cellarea,lndarea)
            landarea.set_data(icell,lndarea)
            natarea.set_data(icell,cellarea - lndarea)

    # Make the cell area of the total area inclusive the coast.
    rownum = ascraster.duplicategrid(landarea)
    maxarea = landarea.nrows * [0.0]
    for icell in range(landarea.length):
        cellarea = area.get_data(icell)
        if (cellarea != None):
            # Get row number
            irow,icol = area.get_row_col_from_index(icell)
            rownum.set_data(icell,irow)
            if (cellarea > maxarea[irow]):
                maxarea[irow] = cellarea

    for icell in range(landarea.length):
        cellarea = area.get_data(icell)
        if (cellarea != None):
            irow = rownum.get_data(icell)
            area.set_data(icell,maxarea[irow])

    # Write areas in ha to file
    area.write_ascii_file(os.path.join(inputdir,params.filename_gridcell_area))
    landarea.write_ascii_file(os.path.join(inputdir,params.filename_agri_area))
    natarea.write_ascii_file(os.path.join(inputdir,params.filename_natural_area))

    # Calculate the fraction recent groundwater to surface water
    # Read runoff in mm   
    filename = os.path.join(waterdir,"runoff.asc")
    runoff = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Correct runoff because this could be negative
    runoff.multiply(mask,minimum=0.0)
    # Calculate the fraction recent groundwater that enters the surface water.
    fr_recent_grw_grid = ascraster.duplicategrid(runoff)
    for icell in range(landarea.length):
        val = fr_recent_grw_grid.get_data(icell)
        if (val != None):
            fr = fr_recent_grw(params,val)
            fr_recent_grw_grid.set_data(icell,fr)

    # Write fraction recent groundwater to file
    fr_recent_grw_grid.write_ascii_file(os.path.join(inputdir,params.filename_fraction_recent_groundwaterload_ag))
    fr_recent_grw_grid.write_ascii_file(os.path.join(inputdir,params.filename_fraction_recent_groundwaterload_nat))
   
    # Calculate the precipitation surplus in dm3
    runoff.multiply(area)
    # Conversion from mm* ha to dm3
    runoff.multiply(1.0e8)
    # Write the precipitation surplus in dm3 to file
    runoff.write_ascii_file(os.path.join(inputdir,params.filename_precipitation_surplus))

    # Deposition
    filename = os.path.join(gnmdir_in,"ndeposition.asc")
    # Read deposition in mg N/m2/yr
    depo = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with total cell area (ha).
    depo.multiply(depo)
    # Conversion to get kg N yr-1
    depo.multiply(1.0e-2)
    # Write N deposition in kg N yr-1 to file
    depo.write_ascii_file(os.path.join(inputdir,params.filename_n_deposition))

    # Inputs [kg N yr-1]
    filename = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT FERTILIZER GRID FILE"])
    filename = os.path.splitext(filename)[0] +"_N" + os.path.splitext(filename)[1]
    # Read fertilizer in kg N ha-1
    fert     = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Read landarea in km2
    filename = os.path.join(mandistdir_in,mandist_files_dict["LAND AREA ASC FILE"])
    landarea = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Make kg N yr-1 of this (factor 100 is conversion from km2 to ha).
    fert.multiply(landarea,default_nodata_value=-9999.)
    fert.multiply(100.)
    fert.write_ascii_file(os.path.join(inputdir,params.filename_fert_inp))

    filename = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT TOTAL MANURE APPLICATION GRID FILE"])
    # Read manure in kg N ha-1
    manure   = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Read landarea in km2
    filename = os.path.join(mandistdir_in,mandist_files_dict["LAND AREA ASC FILE"])
    landarea = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Make kg N yr-1 of this (factor 100 is conversion from km2 to ha).
    manure.multiply(landarea,default_nodata_value=-9999.)
    manure.multiply(100.)
    manure.write_ascii_file(os.path.join(inputdir,params.filename_manure_inp))

    # N fixation
    filename = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT N NATURAL FIXATION GRID FILE"])
    # Read N fixation for natural area in kg N yr-1
    Nfix_nat     = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    Nfix_nat.multiply(mask,default_nodata_value=-9999.)
    # Write N fixation for natural areas in kg N yr-1 to file
    Nfix_nat.write_ascii_file(os.path.join(inputdir,params.filename_nfixation_nat))

    filename = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT N CROP FIXATION GRID FILE"])
    # Read N fixation for agricultural area in kg N yr-1
    Nfix_agri     = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    Nfix_agri.multiply(mask,default_nodata_value=-9999.)
    # Write N fixation for agricultural areas in kg N yr-1 to file
    Nfix_agri.write_ascii_file(os.path.join(inputdir,params.filename_nfixation_agri))

    # N uptake
    filename = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT UPTAKE GRID FILE"])
    filename = os.path.splitext(filename)[0] +"_N" + os.path.splitext(filename)[1]
    # Read uptake in kg N yr-1
    uptake = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    uptake.multiply(mask,default_nodata_value=-9999.)
    # Write N uptake in kg N yr-1 to file
    uptake.write_ascii_file(os.path.join(inputdir,params.filename_crop_uptake))


    # Emission spreading fertilizer
    filename_org = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT SPREADING GRID FILE"])
    filename = os.path.splitext(filename_org)[0] +"_EXT_GRASS_FERT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading fertilizer in extensive grass systems in kg N ha-1
    fert_ext_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with extensive grass area
    fert_ext_grass.multiply(grass_ext,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_INT_GRASS_FERT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading fertilizer in intensive grass systems in kg N ha-1
    fert_int_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with intensive grass area
    fert_int_grass.multiply(grass_int,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_EXT_CROP_FERT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading fertilizer in extensive crop systems in kg N ha-1
    fert_ext_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with extensive crop area
    fert_ext_crop.multiply(crop_ext,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_INT_CROP_FERT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading fertilizer in intensive crop systems in kg N ha-1
    fert_int_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with intensive crop area
    fert_int_crop.multiply(crop_int,default_nodata_value=-9999.)
    # Add the four components.
    fert_ext_grass.add(fert_int_grass)
    fert_ext_grass.add(fert_ext_crop)
    fert_ext_grass.add(fert_int_crop)
    # Write NH3 emission spreading fertilizer in kg N yr-1 to file
    fert_ext_grass.write_ascii_file(os.path.join(inputdir,params.filename_nh3_em_spread_fert))

    # Emission spreading manure
    filename_org = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT SPREADING GRID FILE"])
    filename = os.path.splitext(filename_org)[0] +"_EXT_GRASS_MANURE_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading manure in extensive grass systems in kg N ha-1
    manure_ext_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with extensive grass area
    manure_ext_grass.multiply(grass_ext,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_INT_GRASS_MANURE_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading manure in intensive grass systems in kg N ha-1
    manure_int_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with intensive grass area
    manure_int_grass.multiply(grass_int,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_EXT_CROP_MANURE_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading manure in extensive crop systems in kg N ha-1
    manure_ext_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with extensive crop area
    manure_ext_crop.multiply(crop_ext,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_INT_CROP_MANURE_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of spreading manure in intensive crop systems in kg N ha-1
    manure_int_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with intensive crop area
    manure_int_crop.multiply(crop_int,default_nodata_value=-9999.)
    # Add the four components.
    manure_ext_grass.add(manure_int_grass)
    manure_ext_grass.add(manure_ext_crop)
    manure_ext_grass.add(manure_int_crop)
    # Write NH3 emission spreading manure in kg N yr-1 to file
    manure_ext_grass.write_ascii_file(os.path.join(inputdir,params.filename_nh3_em_spread_manure))

    # Area of extensive systems and mixed and landless systems
    area_int = ascraster.duplicategrid(crop_int)
    area_int.add(grass_int)
    area_ext = ascraster.duplicategrid(crop_ext)
    area_ext.add(grass_ext)

    # Emission from storage
    filename_org = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT STORAGE GRID FILE"])
    filename = os.path.splitext(filename_org)[0] +"_EXT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of storage in extensive systems in kg N ha-1
    storage_ext = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with extensive  area
    storage_ext.multiply(area_ext,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_INT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of storage in intensive grass systems in kg N ha-1
    storage_int = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with intensive  area
    storage_int.multiply(area_int,default_nodata_value=-9999.)
    # Add the two components.
    storage_ext.add(storage_int)
    # Write NH3 emission of storage in kg N yr-1 to file
    storage_ext.write_ascii_file(os.path.join(inputdir,params.filename_nh3_em_storage))

    # Emission from grazing
    filename_org = os.path.join(mandistdir_out,mandist_files_dict["OUTPUT GRAZING GRID FILE"])
    filename = os.path.splitext(filename_org)[0] +"_EXT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of grazing in extensive systems in kg N ha-1
    grazing_ext = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with extensive grass area
    grazing_ext.multiply(grass_ext,default_nodata_value=-9999.)
    filename = os.path.splitext(filename_org)[0] +"_INT_NH3" + os.path.splitext(filename_org)[1]
    # Read NH3 volatilisation of grazing in intensive grass systems in kg N ha-1
    grazing_int = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Multiply with intensive grass area
    grazing_int.multiply(grass_int,default_nodata_value=-9999.)
    # Add the two components.
    grazing_ext.add(grazing_int)
    # Write NH3 emission of grazing in kg N yr-1 to file
    grazing_ext.write_ascii_file(os.path.join(inputdir,params.filename_nh3_em_grazing))


    # Budget, runoff, leaching & groundwater: agriculture
    my_sys.my_copyfile(os.path.join(gnmdir_out,"Nleaching_nat.asc"),\
                       os.path.join(inputdir,params.filename_leaching_nat))

    # Leaching
    filename = os.path.join(gnmdir_out,"Nleaching_arable.asc")
    le_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(gnmdir_out,"Nleaching_grass.asc")
    le_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    le_crop.add(le_grass)
    # Write N of leaching on agricultural soils in kg N yr-1 to file
    le_crop.write_ascii_file(os.path.join(inputdir,params.filename_leaching_ag))

    # Groundwater
    filename = os.path.join(gnmdir_out,"Nsgrw.asc")
    sgrw = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(gnmdir_out,"N_deep_grw.asc")
    dgrw = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    sgrw.add(dgrw)

    # Use leaching to distribute groundwater load into agricultural and natural
    filename = os.path.join(gnmdir_out,"Nleaching_nat.asc")
    le_nat = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(gnmdir_out,"Nleaching.asc")
    le_tot = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Determine the fraction of nat in the total leaching.
    le_nat.divide(le_tot,default_nodata_value=-9999.)

    grw_nat = ascraster.duplicategrid(sgrw)
    grw_agri = ascraster.duplicategrid(sgrw)
    grw_nat.multiply(le_nat)
    grw_agri.substract(grw_nat)
    # Write N of leaching on agricultural soils in kg N yr-1 to file
    grw_nat.write_ascii_file(os.path.join(inputdir,params.filename_groundwaterload_nat))
    grw_agri.write_ascii_file(os.path.join(inputdir,params.filename_groundwaterload_ag))

    # Point sources & fixed diffuse sources (erosion)[kg N yr-1]
    my_sys.my_copyfile(os.path.join(gnmdir_in,"Npoint.asc"),\
                       os.path.join(inputdir,params.filename_n_point_wastewater))
    my_sys.my_copyfile(os.path.join(gnmdir_in,"N_aquaculture.asc"),\
                       os.path.join(inputdir,params.filename_n_point_aquaculture))
    my_sys.my_copyfile(os.path.join(gnmdir_out,"N_deposition_water.asc"),\
                       os.path.join(inputdir,params.filename_n_point_dep_surfacewater))
    my_sys.my_copyfile(os.path.join(gnmdir_out,"N_gnpp.asc"),\
                       os.path.join(inputdir,params.filename_n_point_alloch_matter))
    my_sys.my_copyfile(os.path.join(gnmdir_out,"Nsoilloss_nat.asc"),\
                       os.path.join(inputdir,params.filename_n_in_erosion_nat))

    # N erosion
    filename = os.path.join(gnmdir_out,"Nsoilloss_arable.asc")
    eros_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(gnmdir_out,"Nsoilloss_grass.asc")
    eros_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    eros_crop.add(eros_grass)
    # Write N of erosion on agricultural soils in kg N yr-1 to file
    eros_crop.write_ascii_file(os.path.join(inputdir,params.filename_n_in_erosion_ag))
    
    # Surface runoff
    filename = os.path.join(gnmdir_out,"N_sro_arable.asc")
    nsro_crop = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(gnmdir_out,"N_sro_grs.asc")
    nsro_grass = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    nsro_crop.add(nsro_grass)
    # Substract the erosion from this.
    nsro_crop.substract(eros_crop) 
    # Write N of surface runoff on agricultural soils in kg N yr-1 to file
    nsro_crop.write_ascii_file(os.path.join(inputdir,params.filename_nsro_ag))

    filename = os.path.join(gnmdir_out,"N_sro_nat.asc")
    nsro_nat = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    filename = os.path.join(gnmdir_out,"Nsoilloss_nat.asc")
    eros_nat = ascraster.Asciigrid(ascii_file = filename,numtype = float)
    # Substract the erosion from this.
    nsro_nat.substract(eros_nat) 
    # Write N of surface runoff on natural soils in kg N yr-1 to file
    nsro_nat.write_ascii_file(os.path.join(inputdir,params.filename_nsro_nat))


if (__name__ == "__main__"):
  
    try:
        # Collect all files which are needed to run the critital load model.
        get_all_files(sys.argv)
    except MyError as val:
        val.write()
    except:
        print("***** ERROR ******")
        print("create_input_files.py failed.")
        print(str(sys.exc_info()[0]))
        print(traceback.print_exc())


