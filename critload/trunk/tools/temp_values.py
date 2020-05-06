# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/temp_values.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# Python modules
import os

# Generalcode modules
import ascraster

# Local modules
from print_debug import *

def griddivide(grid1,grid2,default_nodata_value = 0):
    '''
    Calculate result of grid1/grid2 
    '''
    # Make a copy of the first grid.
    grid3 = ascraster.duplicategrid(grid1)

    for icell in range(grid3.length):
        # Get values from both grids.
        val1 = grid1.get_data(icell)
        val2 = grid2.get_data(icell)

        # If both grids have nodata, keep nodata.
        if (val1 == None or val2 == None):
            continue
        # Do the calculation
        try:
            val3 = val1/val2
        except (ZeroDivisionError,TypeError):
            val3 = default_nodata_value
        
        # Put result in grid.
        grid3.set_data(icell,val3)

    return grid3
    
def temp_values(params):
    
    ### --------- 1. LAND UNSE FRACTIONS --------- ###
    # read input files land areas
    a_tot = ascraster.Asciigrid(ascii_file=params.filename_gridcell_area, numtype=float,mask=params.mask)
    a_ag  = ascraster.Asciigrid(ascii_file=params.filename_agri_area,     numtype=float,mask=params.mask)
    a_ara = ascraster.Asciigrid(ascii_file=params.filename_cropland_area, numtype=float,mask=params.mask)  
    a_igl = ascraster.Asciigrid(ascii_file=params.filename_intgl_area,    numtype=float,mask=params.mask)     
    a_egl = ascraster.Asciigrid(ascii_file=params.filename_extgl_area,    numtype=float,mask=params.mask)
    a_nat = ascraster.Asciigrid(ascii_file=params.filename_natural_area,  numtype=float,mask=params.mask)
    
    # calculate fag   
    fag = ascraster.duplicategrid(a_ag)
    fag.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fag.asc")
    fag.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fag,"fag =")
    # calculate fara
    fara = ascraster.duplicategrid(a_ara)
    fara.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fara.asc")
    fara.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fara,"fara =")   
    # calculate figl
    figl = ascraster.duplicategrid(a_igl)
    figl.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"figl.asc")
    figl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(figl,"figl =")   
    # calculate fegl
    fegl = ascraster.duplicategrid(a_egl)
    fegl.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fegl.asc")
    fegl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fegl,"fegl =")   
    # calculate fnat
    fnat = ascraster.duplicategrid(a_nat)
    fnat.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fnat.asc")
    fnat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnat,"fnat =")
  
    ### --------- 2. INPUTS FERTILIZER, MANURE, FIXATION --------- ###
    # read input files N inputs 
    nfer_eff_ag    = ascraster.Asciigrid(ascii_file=params.filename_fert_inp,            numtype=float,mask=params.mask)
    nfer_eff_ara   = ascraster.Asciigrid(ascii_file=params.filename_fert_inp_cropland,   numtype=float,mask=params.mask)
    nfer_eff_igl   = ascraster.Asciigrid(ascii_file=params.filename_fert_inp_grassland,  numtype=float,mask=params.mask)  
    nman_eff_ag    = ascraster.Asciigrid(ascii_file=params.filename_manure_inp,          numtype=float,mask=params.mask)    
    nman_eff_ara   = ascraster.Asciigrid(ascii_file=params.filename_manure_inp_cropland, numtype=float,mask=params.mask)
    nman_eff_igl   = ascraster.Asciigrid(ascii_file=params.filename_manure_inp_intgl,    numtype=float,mask=params.mask)    
    nman_eff_egl   = ascraster.Asciigrid(ascii_file=params.filename_manure_inp_extgl,    numtype=float,mask=params.mask)  
    nfix_ag        = ascraster.Asciigrid(ascii_file=params.filename_nfixation_agri,      numtype=float,mask=params.mask)
    nfix_ara       = ascraster.Asciigrid(ascii_file=params.filename_nfixation_cropland,  numtype=float,mask=params.mask)
    nfix_igl       = ascraster.Asciigrid(ascii_file=params.filename_nfixation_intgl,     numtype=float,mask=params.mask)
    nfix_egl       = ascraster.Asciigrid(ascii_file=params.filename_nfixation_extgl,     numtype=float,mask=params.mask)
    nfix_nat       = ascraster.Asciigrid(ascii_file=params.filename_nfixation_nat,       numtype=float,mask=params.mask)
    # read input files NH3 emissions
    nh3_spread_man      = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_manure,          numtype=float,mask=params.mask)
    nh3_spread_man_ara  = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_manure_cropland, numtype=float,mask=params.mask)
    nh3_spread_man_igl  = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_manure_intgl,    numtype=float,mask=params.mask)
    nh3_spread_man_egl  = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_manure_extgl,    numtype=float,mask=params.mask)
    nh3_stor            = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_storage,                numtype=float,mask=params.mask)
    nh3_graz            = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_grazing,                numtype=float,mask=params.mask)
    nh3_graz_igl        = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_grazing_int,            numtype=float,mask=params.mask)
    nh3_graz_egl        = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_grazing_ext,            numtype=float,mask=params.mask)
    nh3_spread_fer      = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_fert,            numtype=float,mask=params.mask)    
    nh3_spread_fer_ara  = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_fert_cropland,   numtype=float,mask=params.mask)
    nh3_spread_fer_igl  = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_fert_intgl,      numtype=float,mask=params.mask)    
    nh3_spread_fer_egl  = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_fert_extgl,      numtype=float,mask=params.mask)
    
    # split nh3 emissions from storage over intensive grassland, extensive grassland & arable land
    # intensive grassland                              
    nh3_stor_igl = ascraster.duplicategrid(nh3_stor)
    for icell in range(nh3_stor_igl.length):
        igl = a_igl.get_data(icell)
        nh3stor = nh3_stor.get_data(icell)
        if (igl == None or igl==0) :
            nh3emigl = 0
        elif (igl > 0) :
            nh3emigl = nh3stor
        else:
            continue
            
        nh3_stor_igl.set_data(icell,nh3emigl)
    fileout = os.path.join(params.outputdir, "nh3_stor_igl.asc")
    nh3_stor_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_stor_igl,"nh3_stor_igl =") 
    
    # extensive grassland
    nh3_stor_egl = ascraster.duplicategrid(nh3_stor)
    for icell in range(nh3_stor_egl.length):
        egl = a_egl.get_data(icell)
        nh3stor = nh3_stor.get_data(icell)
        if (egl == None or egl==0) :
            nh3emegl = 0
        elif (egl > 0) :
            nh3emegl = nh3stor
        else:
            continue
            
        nh3_stor_egl.set_data(icell,nh3emegl)
    fileout = os.path.join(params.outputdir, "nh3_stor_egl.asc")
    nh3_stor_egl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_stor_egl,"nh3_stor_egl =")

    # arable land
    nh3_stor_ara = ascraster.duplicategrid(nh3_stor)          
    for icell in range(nh3_stor_ara.length):
        ara = a_ara.get_data(icell)
        igl = a_igl.get_data(icell)
        egl = a_egl.get_data(icell)
        nh3stor = nh3_stor.get_data(icell)
        if (ara == None) : 
            nh3emara = 0
        elif (egl == 0 and igl == 0) :
            nh3emara = nh3stor
        elif (egl > 0 or igl > 0):
            nh3emara = 0
            nh3emara = 0
        else:
            continue
            
        nh3_stor_ara.set_data(icell,nh3emara)
    fileout = os.path.join(params.outputdir, "nh3_stor_ara.asc")
    nh3_stor_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_stor_ara,"nh3_stor_ara =")
    
 
    # Calculate total N inputs from *FERTILIZER* (incl. NH3 emissions)
    # 'ag'
    nfer_ag = ascraster.duplicategrid(nfer_eff_ag)
    nfer_ag.add(nh3_spread_fer)
    fileout = os.path.join(params.outputdir,"nfer_ag.asc")
    nfer_ag.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_ag,"nfer_ag =")
    # 'ara'
    nfer_ara = ascraster.duplicategrid(nfer_eff_ara)
    nfer_ara.add(nh3_spread_fer_ara)
    fileout = os.path.join(params.outputdir,"nfer_ara.asc")
    nfer_ara.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_ara,"nfer_ara =")
    # 'igl'
    nfer_igl = ascraster.duplicategrid(nfer_eff_igl)
    nfer_igl.add(nh3_spread_fer_igl)
    fileout = os.path.join(params.outputdir,"nfer_igl.asc")
    nfer_igl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_igl,"nfer_igl =")
    # 'araigl'
    nfer_araigl = ascraster.duplicategrid(nfer_ara)
    nfer_araigl.add(nfer_igl)
    fileout = os.path.join(params.outputdir,"nfer_araigl.asc")
    nfer_araigl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress) 
 
    # Calculate total N inputs from *MANURE* (incl. NH3 emissions)
    # 'ag'
    nman_ag = ascraster.duplicategrid(nman_eff_ag)
    nman_ag.add(nh3_spread_man)
    nman_ag.add(nh3_stor)
    nman_ag.add(nh3_graz)
    fileout = os.path.join(params.outputdir,"nman_ag.asc")
    nman_ag.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_ag,"nman_ag =")
    # 'ara'
    nman_ara = ascraster.duplicategrid(nman_eff_ara)
    nman_ara.add(nh3_spread_man_ara)
    nman_ara.add(nh3_stor_ara)
    fileout = os.path.join(params.outputdir,"nman_ara.asc")
    nman_ara.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_ara,"nman_ara =")
    # 'igl'
    nman_igl = ascraster.duplicategrid(nman_eff_igl)
    nman_igl.add(nh3_spread_man_igl)
    nman_igl.add(nh3_stor_igl)
    nman_igl.add(nh3_graz_igl)
    fileout = os.path.join(params.outputdir,"nman_igl.asc")
    nman_igl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_igl,"nman_igl =")
    # 'egl'
    nman_egl = ascraster.duplicategrid(nman_eff_egl)
    nman_egl.add(nh3_spread_man_egl)
    nman_egl.add(nh3_stor_egl)
    nman_egl.add(nh3_graz_egl)
    fileout = os.path.join(params.outputdir,"nman_egl.asc")
    nman_egl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_egl,"nman_egl =")    
    # 'araigl'
    nman_araigl = ascraster.duplicategrid(nman_ara)
    nman_araigl.add(nman_igl)
    fileout = os.path.join(params.outputdir,"nman_araigl.asc")
    nman_araigl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)

    # Calculate total N inputs from *MANURE AND FERTILIZER* (incl. NH3 emissions)
    # 'ara'
    nman_fer_ara = ascraster.duplicategrid(nman_ara)
    nman_fer_ara.add(nfer_ara)
    fileout = os.path.join(params.outputdir,"nman_fer_ara.asc")
    nman_fer_ara.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    # 'igl'
    nman_fer_igl = ascraster.duplicategrid(nman_igl)
    nman_fer_igl.add(nfer_igl)
    fileout = os.path.join(params.outputdir,"nman_fer_igl.asc")
    nman_fer_igl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    # 'araigl'
    nman_fer_araigl = ascraster.duplicategrid(nman_fer_ara)
    nman_fer_araigl.add(nman_fer_igl)
    fileout = os.path.join(params.outputdir,"nman_fer_araigl.asc")
    nman_fer_araigl.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    
    ## calculate *frNfe*
    # 'ara'
    fer_man_ara = ascraster.duplicategrid(nman_ara)
    fer_man_ara.add(nfer_ara)
    frnfe_ara = ascraster.duplicategrid(nfer_ara)
    frnfe_ara.divide(fer_man_ara, default_nodata_value = -9999)
    
    # replace '0' by 0.0001 in frnfe_ara
    for icell in range(frnfe_ara.length):
        val = frnfe_ara.get_data(icell)
        if (val == None or val > 0):
            continue
        if val == 0.0:
            res = 0.0001
        frnfe_ara.set_data(icell,res) 
    
    # replace '1' by 0.9999 in frnfe_ara
    for icell in range(frnfe_ara.length):
        val = frnfe_ara.get_data(icell)
        if (val == None or val < 1):
            continue
        if val == 1.0:
            res = 0.9999
        frnfe_ara.set_data(icell,res) 
    
    fileout = os.path.join(params.outputdir,"frnfe_ara.asc")
    frnfe_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frnfe_ara,"frnfe_ara =")
    
    # 'igl'
    fer_man_igl = ascraster.duplicategrid(nman_igl)
    fer_man_igl.add(nfer_igl)
    frnfe_igl = ascraster.duplicategrid(nfer_igl)
    frnfe_igl.divide(fer_man_igl, default_nodata_value = -9999)
    
    # replace '0' by 0.0001 in frnfe_igl
    for icell in range(frnfe_igl.length):
        val = frnfe_igl.get_data(icell)
        if (val == None or val > 0):
            continue
        if val == 0.0:
            res = 0.0001
        frnfe_igl.set_data(icell,res) 
    
    # replace '1' by 0.9999 in frnfe_igl
    for icell in range(frnfe_igl.length):
        val = frnfe_igl.get_data(icell)
        if (val == None or val < 1):
            continue
        if val == 1.0:
            res = 0.9999
        frnfe_igl.set_data(icell,res) 
    
    fileout = os.path.join(params.outputdir,"frnfe_igl.asc")
    frnfe_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frnfe_igl,"frnfe_igl =")  
    
    ## Calculate proportion of N inputs in total (arable + intensive grassland) N inputs
    # 'ara'
    frn_ara = ascraster.duplicategrid(nman_ara)
    frn_ara.add(nfer_ara)
    denominator_frn_ara = ascraster.duplicategrid(frn_ara)
    denominator_frn_ara.add(nman_igl)
    denominator_frn_ara.add(nfer_igl)
    frn_ara.divide(denominator_frn_ara, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"frn_ara.asc")
    frn_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frn_ara,"frn_ara =")  
    
    # 'igl'
    frn_igl = ascraster.duplicategrid(nman_igl)
    frn_igl.add(nfer_igl)
    denominator_frn_igl = ascraster.duplicategrid(frn_igl)
    denominator_frn_igl.add(nman_ara)
    denominator_frn_igl.add(nfer_ara)
    frn_igl.divide(denominator_frn_igl, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"frn_igl.asc")
    frn_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frn_igl,"frn_igl =")    
 
    ### --------- 3. NH3 EMISSIONS & EMISSION FRACTIONS --------- ###
   
    # calculate *TOTAL NH3 EMISSION*
    # 'ag'
    nh3_tot_ag = ascraster.duplicategrid(nh3_spread_man)
    nh3_tot_ag.add(nh3_spread_fer)
    nh3_tot_ag.add(nh3_stor)
    nh3_tot_ag.add(nh3_graz)
    print_debug(nh3_tot_ag,"nh3_tot_ag =")
    # 'ara' 
    nh3_tot_ara = ascraster.duplicategrid(nh3_spread_man_ara)
    nh3_tot_ara.add(nh3_spread_fer_ara)
    nh3_tot_ara.add(nh3_stor_ara)
    fileout = os.path.join(params.outputdir,"nh3_tot_ara.asc")
    nh3_tot_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_tot_ara,"nh3_tot_ara =")   
    # 'igl'
    nh3_tot_igl = ascraster.duplicategrid(nh3_spread_man_igl)
    nh3_tot_igl.add(nh3_spread_fer_igl)
    nh3_tot_igl.add(nh3_stor_igl)
    nh3_tot_igl.add(nh3_graz_igl)
    fileout = os.path.join(params.outputdir,"nh3_tot_igl.asc")
    nh3_tot_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_tot_igl,"nh3_tot_igl =")           
    # 'egl'
    nh3_tot_egl = ascraster.duplicategrid(nh3_spread_man_egl)
    nh3_tot_egl.add(nh3_spread_fer_egl)
    nh3_tot_egl.add(nh3_stor_egl)  
    nh3_tot_egl.add(nh3_graz_egl)
    fileout = os.path.join(params.outputdir,"nh3_tot_egl.asc")
    nh3_tot_egl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)   
    print_debug(nh3_tot_egl,"nh3_tot_egl =")   
    
    # calculate *FNH3EM,MAN*
    # 'ara'
    nh3_man_tot_ara = ascraster.duplicategrid(nh3_spread_man_ara)
    nh3_man_tot_ara.add(nh3_stor_ara)
    nh3_ef_man_ara = griddivide(nh3_man_tot_ara,nman_ara,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_man_ara.asc")
    nh3_ef_man_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_man_ara,"nh3_ef_man_ara =")
    # 'igl'
    nh3_man_tot_igl = ascraster.duplicategrid(nh3_spread_man_igl)
    nh3_man_tot_igl.add(nh3_stor_igl)
    nh3_man_tot_igl.add(nh3_graz_igl)
    nh3_ef_man_igl = griddivide(nh3_man_tot_igl,nman_igl,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_man_igl.asc")
    nh3_ef_man_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_man_igl,"nh3_ef_man_igl =")    

    # calculate *FNH3EM,FER*
    # 'ara'
    nh3_ef_fer_ara = griddivide(nh3_spread_fer_ara,nfer_ara,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_fer_ara.asc")
    nh3_ef_fer_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_fer_ara,"nh3_ef_fer_ara =")
    # 'igl'
    nh3_ef_fer_igl = griddivide(nh3_spread_fer_igl,nfer_igl,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_fer_igl.asc")
    nh3_ef_fer_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_fer_igl,"nh3_ef_fer_igl =")

    # calculate *FNH3EM,MAN,FER*
    # 'ara'
    nh3_ef_man_fer_ara = griddivide(nh3_tot_ara,fer_man_ara,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_man_fer_ara.asc")
    nh3_ef_man_fer_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_man_fer_ara,"nh3_ef_man_fer_ara =")
    # 'igl'
    nh3_ef_man_fer_igl = griddivide(nh3_tot_igl,fer_man_igl,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_man_fer_igl.asc")
    nh3_ef_man_fer_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_man_fer_igl,"nh3_ef_man_fer_igl =")
    
    ### --------- 4. N DEPOSITION & NOx emission --------- ###
    # calculate corrected N deposition grid - for all cells where Ndep < NH3em, replace Ndep by NH3em
    ndep_tot = ascraster.Asciigrid(ascii_file=params.filename_n_deposition,numtype=float,mask=params.mask)
    ndep_corr_tot = ascraster.duplicategrid(ndep_tot)
    for icell in range(nh3_tot_ag.length):
        # Get values from both grids.
        nh3 =  nh3_tot_ag.get_data(icell)
        dep = ndep_tot.get_data(icell)
    
        # If both grids have nodata, keep nodata.
        if (nh3 == None or dep == None or dep >= nh3):
            continue
        if dep < nh3:
            depcorr = nh3
        ndep_corr_tot.set_data(icell,depcorr)
    fileout = os.path.join(params.outputdir,"ndep_corr_tot.asc")
    ndep_corr_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)    
    print_debug(ndep_tot,"ndep_tot =")
    print_debug(ndep_corr_tot,"ndep_corr_tot =")
  
    # calculate NOx emissions: NOx = *corrected* Ndep - (NH3,spread,fe+NH3,spread,man+NH3stor+NH3,graz)
    nox_em = ascraster.duplicategrid(ndep_corr_tot)
    nox_em.substract(nh3_tot_ag)
    #factor = 0
    #nox_em.multiply(factor)
    fileout = os.path.join(params.outputdir,"nox_em.asc")
    nox_em.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nox_em,"nox_em =") 
 
    ## *N DEPOSITION* 
    # 'ag'
    ndep_ag = ascraster.duplicategrid(ndep_corr_tot)
    ndep_ag.multiply(fag)
    print_debug(ndep_ag,"ndep_ag =")
    # 'ara'
    ndep_ara = ascraster.duplicategrid(ndep_corr_tot)
    ndep_ara.multiply(fara)
    print_debug(ndep_ara,"ndep_ara =")
    # 'igl'
    ndep_igl = ascraster.duplicategrid(ndep_corr_tot)
    ndep_igl.multiply(figl)
    print_debug(ndep_igl,"ndep_igl =") 
    # 'egl'
    ndep_egl = ascraster.duplicategrid(ndep_corr_tot)
    ndep_egl.multiply(fegl)
    print_debug(ndep_egl,"ndep_egl =")   
    # 'nat'
    ndep_nat = ascraster.duplicategrid(ndep_corr_tot)
    ndep_nat.multiply(fnat)
    print_debug(ndep_nat,"ndep_nat =")    
   
    ### --------- 5. TOTAL INPUTS --------- ###
    ## Calculate *Total N Inputs*
    # 'ag'
    nin_ag = ascraster.duplicategrid(nfer_ag)
    nin_ag.add(nman_ag)
    nin_ag.add(nfix_ag)
    nin_ag.add(ndep_ag)
    print_debug(nin_ag,"nin_ag =")
    # 'ara'
    nin_ara = ascraster.duplicategrid(nfer_ara)
    nin_ara.add(nman_ara)
    nin_ara.add(nfix_ara)
    nin_ara.add(ndep_ara)
    fileout = os.path.join(params.outputdir,"nin_ara.asc")
    nin_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_ara,"nin_ara =")    
    # 'igl'
    nin_igl = ascraster.duplicategrid(nfer_igl)
    nin_igl.add(nman_igl)
    nin_igl.add(nfix_igl)
    nin_igl.add(ndep_igl)
    fileout = os.path.join(params.outputdir,"nin_igl.asc")
    nin_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_igl,"nin_igl =")   
    # 'araigl'
    nin_araigl = ascraster.duplicategrid(nin_ara)
    nin_araigl.add(nin_igl)
    fileout = os.path.join(params.outputdir,"nin_araigl.asc")
    nin_araigl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    # 'egl'
    nin_egl = ascraster.duplicategrid(nman_egl)
    nin_egl.add(nfix_egl)
    nin_egl.add(ndep_egl)
    print_debug(nin_egl,"nin_egl =")
    # 'nat'
    nin_nat = ascraster.duplicategrid(ndep_nat)
    nin_nat.add(nfix_nat)
    print_debug(nin_nat,"nin_nat =")  
 
    ### --------- 6. SURFACE RUNOFF, UPTAKE, FRNUP, NUE --------- ###
    # read input files uptake, surface runoff
    nsro_ag  = ascraster.Asciigrid(ascii_file=params.filename_nsro_ag,         numtype=float,mask=params.mask)    
    nsro_nat = ascraster.Asciigrid(ascii_file=params.filename_nsro_nat,        numtype=float,mask=params.mask)
    nup_ara  = ascraster.Asciigrid(ascii_file=params.filename_uptake_cropland, numtype=float,mask=params.mask)
    nup_igl  = ascraster.Asciigrid(ascii_file=params.filename_uptake_intgl,    numtype=float,mask=params.mask)   
    nup_egl  = ascraster.Asciigrid(ascii_file=params.filename_uptake_extgl,    numtype=float,mask=params.mask)   
    regions  = ascraster.Asciigrid(ascii_file=params.filename_regions,         numtype=float,mask=params.mask)   
    
    #$# To manipulate results for 1999 so that I can also get uptake per land-use type (assuming equal NUE)
    #$#nup_ag = ascraster.Asciigrid(ascii_file=params.filename_uptake_agriculture,    numtype=float,mask=params.mask)  #$#
    
    #$#nue_ag = ascraster.duplicategrid(nup_ag)
    #$#nue_ag.divide(nin_ag, default_nodata_value = -9999)
    
    #$#nup_ara = ascraster.duplicategrid(nin_ara)
    #$#nup_ara.multiply(nue_ag)
    #$#fileout = os.path.join(params.inputdir,"n_up_crops.asc")
    #$#nup_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)   
    
    #$#nup_igl = ascraster.duplicategrid(nin_igl)
    #$#nup_igl.multiply(nue_ag)
    #$#fileout = os.path.join(params.inputdir,"n_up_grass_int.asc")
    #$#nup_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)   
    
    #$#nup_egl = ascraster.duplicategrid(nin_egl)
    #$#nup_egl.multiply(nue_ag)
    #$#fileout = os.path.join(params.inputdir,"n_up_grass_ext.asc")
    #$#nup_egl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)   
 
    
    ## *N UPTAKE*
    # 'ag'
    nup_ag = ascraster.duplicategrid(nup_ara)
    nup_ag.add(nup_igl)
    nup_ag.add(nup_egl)
    print_debug(nup_ag,"nup_ag =")  
    
    ## *SURFACE RUNOFF FRACTION*
    # 'ag'
    fsro_ag = griddivide(nsro_ag,nin_ag,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fsro_ag.asc")
    fsro_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fsro_ag,"fsro_ag =") 
    # 'nat'
    fsro_nat = griddivide(nsro_nat,nin_nat,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fsro_nat.asc")
    fsro_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fsro_nat,"fsro_nat =")  

    ## *N LOAD FROM SURFACE RUNOFF*
    # 'ara'
    nsro_ara = ascraster.duplicategrid(nin_ara)
    nsro_ara.multiply(fsro_ag)
    print_debug(nsro_ara,"nsro_ara =")  
    # 'igl'
    nsro_igl = ascraster.duplicategrid(nin_igl)
    nsro_igl.multiply(fsro_ag)
    print_debug(nsro_igl,"nsro_igl =")

    ## *N UPTAKE FRACTION*
    # 'ara'
    nin_min_nsro_ara = ascraster.duplicategrid(nin_ara)
    nin_min_nsro_ara.substract(nsro_ara)
    frnup_ara = griddivide(nup_ara,nin_min_nsro_ara,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"frnup_ara.asc")
    frnup_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frnup_ara,"frnup_ara =")   
    # 'igl'
    nin_min_nsro_igl = ascraster.duplicategrid(nin_igl)
    nin_min_nsro_igl.substract(nsro_igl)
    frnup_igl = griddivide(nup_igl,nin_min_nsro_igl,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"frnup_igl.asc")
    frnup_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frnup_igl,"frnup_igl =")   

    ## *NUE*
    # 'ara'
    nue_ara = ascraster.duplicategrid(nup_ara)
    nue_ara.divide(nin_ara, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_ara.asc")
    nue_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_ara,"nue_ara =")
    # 'igl'
    nue_igl = ascraster.duplicategrid(nup_igl)
    nue_igl.divide(nin_igl, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_igl.asc")
    nue_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_igl,"nue_igl =")
    
    ## *MAXIMUM N UPTAKE*
    # make grid with yield increase per region
    yieldgap_region = ascraster.duplicategrid(nup_ara)
    for i in range(yieldgap_region.length):
        yieldgap_region.set_data(i,-9999)
          
    for icell in range(regions.length):
        val = regions.get_data(icell)
        
        # Canada (1)
        if val == 1:
            yg = 1.274
        # USA (2)
        elif val == 2:
            yg = 1.252
        # Mexico (3)
        elif val == 3:
            yg = 1.566
        # Central America (4)
        elif val == 4:
            yg = 1.797
        # Brazil (5)
        elif val == 5:
            yg = 1.343
        # Rest of South America (6)
        elif val == 6:
            yg = 1.532
        # Northern Africa (7)
        elif val == 7:
            yg = 2.711
        # Western Africa (8)
        elif val == 8:
            yg = 2.363
        # Eastern Africa (9)
        elif val == 9:
            yg = 2.424
        # South Africa (10)
        elif val == 10:
            yg = 1.848
        # Western Europe (11)
        elif val == 11:
            yg = 1.177
        # Central Europe (12)
        elif val == 12:
            yg = 1.982
        # Turkey (13)
        elif val == 13:
            yg = 1.797
        # Ukraine region (14)
        elif val == 14:
            yg = 2.633
        # Central Asia (15)
        elif val == 15:
            yg = 2.928
        # Russia region(16)
        elif val == 16:
            yg = 2.391
        # Middle East (17)
        elif val == 17:
            yg = 2.170
        # India (18)
        elif val == 18:
            yg = 1.508
        # Korea region (19)
        elif val == 19:
            yg = 1.180
        # China region (20)
        elif val == 20:
            yg = 1.503  
        # Southeastern Asia (21)
        elif val == 21:
            yg = 1.479
        # Indonesia region (22)
        elif val == 22:
            yg = 1.267
        # Japan (23)
        elif val == 23:
            yg = 1.180
        # Oceania (24)
        elif val == 24:
            yg = 1.487
        # Rest of South Asia (25)
        elif val == 25:
            yg = 1.870
        # Rest of Southern Africa (26)
        elif val == 26:
            yg = 2.551
        # Greenland (27)
        elif val == 27:
            yg = 1.000
        # Region can also have value none (-9999)
        else:
            continue        
        yieldgap_region.set_data(icell,yg) 
    
    print_debug(regions,"region_number =") 

    fileout = os.path.join(params.outputdir,"yieldgap_region.asc")
    yieldgap_region.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(yieldgap_region,"yieldgap =") 
    
    # calculate Nup(max) = Nup  * yieldgap_region
    # 'ara'
    nup_max_ara = ascraster.duplicategrid(nup_ara)
    nup_max_ara.multiply(yieldgap_region)
    fileout = os.path.join(params.outputdir,"nup_max_ara.asc")
    nup_max_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_max_ara,"nup_max_ara =") 
    # 'igl'
    nup_max_igl = ascraster.duplicategrid(nup_igl)
    nup_max_igl.multiply(yieldgap_region)
    fileout = os.path.join(params.outputdir,"nup_max_igl.asc")
    nup_max_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_max_igl,"nup_max_igl =") 
    
    
    ## *CORRECTED NUE* (NUE used to calculate Nin at Nup,max should never be higher than 0.8)
    # 'ara'
    nue_corr_ara = ascraster.duplicategrid(nue_ara)
    for icell in range(nue_corr_ara.length):
        val = nue_corr_ara.get_data(icell)
        if (val == None or val <= 0.8):
            continue
        if val > 0.8:
            res = 0.8
        nue_corr_ara.set_data(icell,res)     
    fileout = os.path.join(params.outputdir,"nue_corr_ara.asc")
    nue_corr_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_corr_ara,"nue_corr_ara =")

    # 'igl'
    nue_corr_igl = ascraster.duplicategrid(nue_igl)
    for icell in range(nue_corr_igl.length):
        val = nue_corr_igl.get_data(icell)
        if (val == None or val <= 0.8):
            continue
        if val > 0.8:
            res = 0.8
        nue_corr_igl.set_data(icell,res)     
    fileout = os.path.join(params.outputdir,"nue_corr_igl.asc")
    nue_corr_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_corr_igl,"nue_corr_igl =")
    
    ## *MAXIMUM N INPUTS* (total N inputs from all sources that correspond to maximum uptake and a max. NUE of 0.8)
    # 'ara'
    nin_max_ara = ascraster.duplicategrid(nup_max_ara)
    nin_max_ara.divide(nue_corr_ara, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nin_max_ara.asc")
    nin_max_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_max_ara,"nin_max_ara =")        
    # 'igl'
    nin_max_igl = ascraster.duplicategrid(nup_max_igl)
    nin_max_igl.divide(nue_corr_igl, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nin_max_igl.asc")
    nin_max_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_max_igl,"nin_max_igl =")
    
    ### --------- 7. BUDGET, LEACHING, DENITRIFICATION --------- ###    
    # read input files
    ngw_ag      = ascraster.Asciigrid(ascii_file=params.filename_groundwaterload_ag,                   numtype=float,mask=params.mask)
    ngw_nat     = ascraster.Asciigrid(ascii_file=params.filename_groundwaterload_nat,                  numtype=float,mask=params.mask)
    fgw_rec_ag  = ascraster.Asciigrid(ascii_file=params.filename_fraction_recent_groundwaterload_ag,   numtype=float,mask=params.mask)
    fgw_rec_nat = ascraster.Asciigrid(ascii_file=params.filename_fraction_recent_groundwaterload_nat,  numtype=float,mask=params.mask)
    nle_ag      = ascraster.Asciigrid(ascii_file=params.filename_leaching_ag,                          numtype=float,mask=params.mask)
    nle_nat     = ascraster.Asciigrid(ascii_file=params.filename_leaching_nat,                         numtype=float,mask=params.mask)
    
    ## *N BUDGET*
    # 'ag'
    nbud_ag = ascraster.duplicategrid(nin_ag)
    nbud_ag.substract(nup_ag)
    print_debug(nbud_ag,"nbud_ag =")
    # 'ara'
    nbud_ara = ascraster.duplicategrid(nin_ara)
    nbud_ara.substract(nup_ara)
    print_debug(nbud_ara,"nbud_ara =")
    # 'igl'
    nbud_igl = ascraster.duplicategrid(nin_igl)
    nbud_igl.substract(nup_igl)
    print_debug(nbud_igl,"nbud_igl =")
    # 'nat'
    nbud_nat = ascraster.duplicategrid(nin_nat)
    print_debug(nbud_nat,"nbud_nat =")
     
    ## *N load to surface water via groundwater due to *recent* N inputs*
    # 'ag'
    ngw_rec_ag = ascraster.duplicategrid(ngw_ag)
    ngw_rec_ag.multiply(fgw_rec_ag)
    print_debug(ngw_rec_ag,"ngw_rec_ag =")
    # 'nat'
    ngw_rec_nat = ascraster.duplicategrid(ngw_nat)
    ngw_rec_nat.multiply(fgw_rec_nat)
    print_debug(ngw_rec_nat,"ngw_rec_nat =")
           
    ## *LEACHING FRACTION*
    # 'ag'
    nbud_min_nsro_ag = ascraster.duplicategrid(nbud_ag)
    nbud_min_nsro_ag.substract(nsro_ag)
    fle_ag = griddivide(nle_ag,nbud_min_nsro_ag,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fle_ag.asc")
    fle_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fle_ag,"fle_ag =")     
    # 'nat'
    nbud_min_nsro_nat = ascraster.duplicategrid(nbud_nat)
    nbud_min_nsro_nat.substract(nsro_nat)
    fle_nat = griddivide(nle_nat,nbud_min_nsro_nat,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fle_nat.asc")
    fle_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fle_nat,"fle_nat =")
    
    ## *N LEACHING*
    # 'ara'
    nle_ara = ascraster.duplicategrid(nbud_ara)
    nle_ara.substract(nsro_ara)
    nle_ara.multiply(fle_ag)
    fileout = os.path.join(params.outputdir,"nle_ara.asc")
    nle_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_ara,"nle_ara =")
    # 'igl'
    nle_igl = ascraster.duplicategrid(nbud_igl)
    nle_igl.substract(nsro_igl)
    nle_igl.multiply(fle_ag)
    fileout = os.path.join(params.outputdir,"nle_igl.asc")
    nle_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_igl,"nle_igl =")    
    
    ## *FRACTION OF RECENT DELIVERY TO LEACHING* (fraction of N leaching that is delivered to surface water via groundwater in first x years)
    # 'ag'
    fgw_rec_le_ag = griddivide(ngw_rec_ag,nle_ag,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fgw_rec_le_ag.asc")
    fgw_rec_le_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fgw_rec_le_ag,"fgw_rec_le_ag =")
    # 'nat'
    fgw_rec_le_nat = griddivide(ngw_rec_nat,nle_nat,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fgw_rec_le_nat.asc")
    fgw_rec_le_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fgw_rec_le_nat,"fgw_rec_le_nat =")
    
    ## *VARIABLE N LOAD TO SURFACE WATER*
    # 'ag'
    nload_var_ag = ascraster.duplicategrid(ngw_rec_ag)
    nload_var_ag.add(nsro_ag)
    print_debug(nload_var_ag,"nload_var_ag =")
    # 'nat'
    nload_var_nat = ascraster.duplicategrid(ngw_rec_nat)
    nload_var_nat.add(nsro_nat)
    print_debug(nload_var_nat,"nload_var_nat =")   
    
    ## *FIXED LOAD TO SURFACE WATER*
    # 'ag'
    grid1 = ascraster.duplicategrid(fgw_rec_ag)
    for i in range(grid1.length):
        grid1.set_data(i,1.0)
    grid1.substract(fgw_rec_ag)
    nload_fixed_ag = ascraster.duplicategrid(ngw_ag)
    nload_fixed_ag.multiply(grid1)
    fileout = os.path.join(params.outputdir,"nload_fixed_ag.asc")
    nload_fixed_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_fixed_ag,"nload_fixed_ag =")   
    # 'nat'
    grid2 = ascraster.duplicategrid(fgw_rec_nat)
    for i in range(grid2.length):
        grid2.set_data(i,1.0)
    grid2.substract(fgw_rec_nat)
    nload_fixed_nat = ascraster.duplicategrid(ngw_nat)
    nload_fixed_nat.multiply(grid2)
    fileout = os.path.join(params.outputdir,"nload_fixed_nat.asc")
    nload_fixed_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_fixed_nat,"nload_fixed_nat =")    

    ## *TOTAL N LOAD FROM POINT SOURCES*
    nallo = ascraster.Asciigrid(ascii_file=params.filename_n_point_alloch_matter,numtype=float,mask=params.mask)
    nww = ascraster.Asciigrid(ascii_file=params.filename_n_point_wastewater,numtype=float,mask=params.mask)
    naqua = ascraster.Asciigrid(ascii_file=params.filename_n_point_aquaculture,numtype=float,mask=params.mask)
    ndep_sw = ascraster.Asciigrid(ascii_file=params.filename_n_point_dep_surfacewater,numtype=float,mask=params.mask)
    #factor = 0
    #nww.multiply(factor)
    #naqua.multiply(factor)   
    npoint_tot = ascraster.duplicategrid(nallo)
    npoint_tot.add(nww)
    npoint_tot.add(naqua)
    npoint_tot.add(ndep_sw)
    fileout = os.path.join(params.outputdir,"npoint_tot.asc")
    npoint_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(npoint_tot,"npoint_tot =") 
    
    ## *TOTAL N LOAD FROM EROSION*
    nero_ag = ascraster.Asciigrid(ascii_file=params.filename_n_in_erosion_ag,numtype=float,mask=params.mask)
    nero_nat = ascraster.Asciigrid(ascii_file=params.filename_n_in_erosion_nat,numtype=float,mask=params.mask)
    nero_tot = ascraster.duplicategrid(nero_ag)
    nero_tot.add(nero_nat)
    fileout = os.path.join(params.outputdir,"nero_tot.asc")
    nero_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nero_tot,"nero_tot =")    
    
    ## *TOTAL N LOAD TO SURFACE WATER* (Nload,tot = Nload,var,ag + Nload,var,nat + Ngw,fixed,ag + Ngw,fixed,nat + Npoint + Nero)
    nload_tot = ascraster.duplicategrid(nload_var_ag)
    nload_tot.add(nload_var_nat)
    nload_tot.add(nload_fixed_ag)
    nload_tot.add(nload_fixed_nat)
    nload_tot.add(npoint_tot)
    nload_tot.add(nero_tot)
    print_debug(nload_tot,"nload_tot =")        
    
