# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/groundwater.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# Python modules
import os

# Generalcode modules
import ascraster

# Local modules
from print_debug import *

def calculate(params):
    
    print("The critical N conc in gw is", params.crit_gw)    
    
    # load needed variables for calculations
    q                = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "q.asc")               ,numtype=float,mask=params.mask)
    fsro_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")         ,numtype=float,mask=params.mask)
    fagri            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fagri.asc")           ,numtype=float,mask=params.mask)
    fle_ag           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc")          ,numtype=float,mask=params.mask)
    frnup_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_agri.asc")           ,numtype=float,mask=params.mask)
    n_fix_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_fix_agri.asc")       ,numtype=float,mask=params.mask)
    nox_em           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")          ,numtype=float,mask=params.mask)
    nh3_tot_egl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_man_agri  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_agri.asc") ,numtype=float,mask=params.mask)
    nh3_ef_fert_agri = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert_agri.asc"),numtype=float,mask=params.mask)
    frnfe_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_agri.asc")      ,numtype=float,mask=params.mask)   
    
    # calculate nle,ag,crit(gw) Nle,ag(crit)=(1-fsro)*Q*fag_crit*Nconc,le,ag(crit)
    one_grid = ascraster.duplicategrid(q)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
    one_min_fsro = ascraster.duplicategrid(one_grid)
    one_min_fsro.substract(fsro_ag)
    nle_ag_crit_gw = ascraster.duplicategrid(one_min_fsro)
    nle_ag_crit_gw.multiply(q)
    nle_ag_crit_gw.multiply(fagri)
    nle_ag_crit_gw.multiply(params.crit_gw)
    #fileout = os.path.join(params.outputdir,"nle_ag_crit_gw.asc")
    #nle_ag_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_ag_crit_gw,"The critical leaching is")
    
   # calculate critical N input from manure
    v_part1 = ascraster.duplicategrid(one_grid)
    v_part1.substract(frnup_agri)
    v_part2 = ascraster.duplicategrid(fsro_ag)
    v_part2.multiply(frnup_agri)
    v = ascraster.duplicategrid(v_part1)
    v.add(v_part2)
    v.substract(fsro_ag)
    v.multiply(fle_ag)
    
    num1 = ascraster.duplicategrid(nle_ag_crit_gw)
    num1.divide(v, default_nodata_value = -9999)
    
    num2 = ascraster.duplicategrid(nox_em)
    num2.multiply(fagri)
    
    num3 = ascraster.duplicategrid(nh3_tot_egl)
    num3.multiply(fagri) 
    
    num = ascraster.duplicategrid(num1)
    num.substract(n_fix_agri)
    num.substract(num2)
    num.substract(num3)
    
    dem1 = ascraster.duplicategrid(fagri)
    dem1.multiply(nh3_ef_man_agri)
    
    dem2 = ascraster.duplicategrid(fagri)
    dem2.multiply(nh3_ef_fert_agri)    
    dem2.add(one_grid)
    
    one_min_frnfe = ascraster.duplicategrid(one_grid)
    one_min_frnfe.substract(frnfe_agri)
    frnfe_division = ascraster.duplicategrid(frnfe_agri)
    frnfe_division.divide(one_min_frnfe, default_nodata_value = -9999)
    
    dem2.multiply(frnfe_division)
    
    dem = ascraster.duplicategrid(one_grid)
    dem.add(dem1)
    dem.add(dem2)
    
    nman_crit_gw = ascraster.duplicategrid(num)
    nman_crit_gw.divide(dem, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir,"nman_crit_gw.asc")
    nman_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_gw,"The critical N input from manure for the groundwater criterion is")
    
    # calculate critical N input from fertilizer
    nfert_crit_gw = ascraster.duplicategrid(nman_crit_gw)
    nfert_crit_gw.multiply(frnfe_division)
    fileout = os.path.join(params.outputdir,"nfert_crit_gw.asc")
    nfert_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfert_crit_gw,"The critical N input from fertilizer for the groundwater criterion is")
    
    # calculate related N deposition
    nh3em_man_crit_gw = ascraster.duplicategrid(nman_crit_gw)
    nh3em_man_crit_gw.multiply(nh3_ef_man_agri)
    nh3em_fert_crit_gw = ascraster.duplicategrid(nfert_crit_gw)
    nh3em_fert_crit_gw.multiply(nh3_ef_fert_agri)
    nh3em_tot_crit_gw = ascraster.duplicategrid(nh3em_fert_crit_gw)
    nh3em_tot_crit_gw.add(nh3em_man_crit_gw)
    nem_tot_crit_gw = ascraster.duplicategrid(nh3em_tot_crit_gw)
    nem_tot_crit_gw.add(nox_em)
    nem_tot_crit_gw.add(nh3_tot_egl)
    ndep_ag_crit_gw = ascraster.duplicategrid(nem_tot_crit_gw)
    ndep_ag_crit_gw.multiply(fagri)
    print_debug(ndep_ag_crit_gw,"The critical N deposition on ag. land for the groundwater criterion is")
    
    # calculate total critical N inputs groundwater
    nin_tot_crit_gw = ascraster.duplicategrid(nman_crit_gw)
    nin_tot_crit_gw.add(nfert_crit_gw)
    nin_tot_crit_gw.add(ndep_ag_crit_gw)
    nin_tot_crit_gw.add(n_fix_agri)
    print_debug(nin_tot_crit_gw,"The total critical input for the groundwater criterion is")
    
    # calculate N surface runoff at critical N inputs groundwater
    nsro_ag_crit_gw = ascraster.duplicategrid(nin_tot_crit_gw)
    nsro_ag_crit_gw.multiply(fsro_ag)
    print_debug(nsro_ag_crit_gw,"The critical N surface runoff for the groundwater criterion is")
    
    # calculate N uptake at critical N inputs
    nup_ag_crit_gw = ascraster.duplicategrid(nin_tot_crit_gw)
    nup_ag_crit_gw.substract(nsro_ag_crit_gw)
    nup_ag_crit_gw.multiply(frnup_agri)
    print_debug(nup_ag_crit_gw,"The N uptake for the groundwater criterion is")
    
    # calculate NUE
    nue_crit_gw = ascraster.duplicategrid(nup_ag_crit_gw)
    nue_crit_gw.divide(nin_tot_crit_gw, default_nodata_value = -9999)
    #fileout = os.path.join(params.outputdir,"nue_crit_gw.asc")
    #nue_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_gw,"The NUE for the groundwater criterion is")
    
    ########### Checking degree of exceedance of critical N leaching by FIXED N inputs ############
    # Calculate N leaching caused by N fixation alone
    nle_nfix_gw = ascraster.duplicategrid(n_fix_agri)
    nle_nfix_gw.multiply(v)
    #fileout = os.path.join(params.outputdir,"nle_nfix_gw.asc")
    #nle_nfix_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_nfix_gw,"The N leaching caused by N fixation alone is")
    # Calculate N leaching caused by NOx emissions alone
    nle_nox_gw = ascraster.duplicategrid(nox_em)
    nle_nox_gw.multiply(fagri)
    nle_nox_gw.multiply(v)
    #fileout = os.path.join(params.outputdir,"nle_nox_gw.asc")
    #nle_nox_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_nox_gw,"The N leaching caused by NOx emissions alone is")
    # Calculate N leaching caused by NH3,egl emissions alone
    nle_nh3egl_gw = ascraster.duplicategrid(nh3_tot_egl)
    nle_nh3egl_gw.multiply(fagri)
    nle_nh3egl_gw.multiply(v)
    #fileout = os.path.join(params.outputdir,"nle_nh3egl_gw.asc")
    #nle_nh3egl_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_nh3egl_gw,"The N leaching caused by NH3 emissions from ext grassland alone is")
    #############################################################################################
    
    ########### FORWARD CALCULATIONS TO CHECK ###########
    # Critical N budget
    nbud_ag_crit_gw = ascraster.duplicategrid(nin_tot_crit_gw)
    nbud_ag_crit_gw.substract(nup_ag_crit_gw)
    print_debug(nbud_ag_crit_gw,"The critical N budget for the groundwater criterion is")
  
    # Critical leaching
    nle_ag_crit_gw_test = ascraster.duplicategrid(nbud_ag_crit_gw)
    nle_ag_crit_gw_test.substract(nsro_ag_crit_gw)
    nle_ag_crit_gw_test.multiply(fle_ag)
    print_debug(nle_ag_crit_gw_test,"The critical N leaching for the groundwater criterion is")
    
    # TEST IF FORWARD CALCULATIONS EQUAL BACKWARD CALLCULATION
    if icell_debug<0:
        pass
    else:
        fw = nle_ag_crit_gw_test.get_data(icell_debug)
        bw = nle_ag_crit_gw.get_data(icell_debug)
        if fw is None:
            print("FW / BW TEST: Forward calculation not possible (Nin,crit=None)")
        
        else:
            fw = round(fw,4) 
            bw = round(bw,4)
            if fw == bw:
                print("FW / BW TEST: SUCCESFUL")
            else:
                print("FW / BW TEST: NOT SUCCESFUL")
    ############################################################################################