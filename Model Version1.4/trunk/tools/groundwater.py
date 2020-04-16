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
    frnup_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_agri.asc")      ,numtype=float,mask=params.mask)
    n_fix_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_fix_agri.asc")      ,numtype=float,mask=params.mask)
    n_up_max         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_up_max.asc")        ,numtype=float,mask=params.mask)
    nox_em           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")          ,numtype=float,mask=params.mask)
    nh3_tot_egl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_man_agri  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_agri.asc") ,numtype=float,mask=params.mask)
    nh3_ef_fert_agri = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert_agri.asc"),numtype=float,mask=params.mask)
    frnfe_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_agri.asc")      ,numtype=float,mask=params.mask)   
    n_in_max         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_in_max.asc")        ,numtype=float,mask=params.mask)   
    
    # calculate nle,ag,crit(gw) Nle,ag(crit)=(1-fsro)*Q*fag_crit*Nconc,le,ag(crit)
    one_grid = ascraster.duplicategrid(q)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
    one_min_fsro = ascraster.duplicategrid(one_grid)
    one_min_fsro.substract(fsro_ag)
    nle_crit_gw_agri = ascraster.duplicategrid(one_min_fsro)
    nle_crit_gw_agri.multiply(q)
    nle_crit_gw_agri.multiply(fagri)
    nle_crit_gw_agri.multiply(params.crit_gw)
    #fileout = os.path.join(params.outputdir,"nle_crit_gw_agri.asc")
    #nle_crit_gw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_crit_gw_agri,"The critical leaching is")
    
   # calculate critical N input from manure
    v_part1 = ascraster.duplicategrid(one_grid)
    v_part1.substract(frnup_agri)
    v_part2 = ascraster.duplicategrid(fsro_ag)
    v_part2.multiply(frnup_agri)
    v = ascraster.duplicategrid(v_part1)
    v.add(v_part2)
    v.substract(fsro_ag)
    v.multiply(fle_ag)
    
    num1 = ascraster.duplicategrid(nle_crit_gw_agri)
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
    
    fileout = os.path.join(params.outputdir,"nh3em_man_crit_gw.asc")
    nh3em_man_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)  
    
    nh3em_fert_crit_gw = ascraster.duplicategrid(nfert_crit_gw)
    nh3em_fert_crit_gw.multiply(nh3_ef_fert_agri)
    
    fileout = os.path.join(params.outputdir,"nh3em_fert_crit_gw.asc")
    nh3em_fert_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)  
    
    nh3em_crit_gw = ascraster.duplicategrid(nh3em_fert_crit_gw)
    nh3em_crit_gw.add(nh3em_man_crit_gw)
    
    fileout = os.path.join(params.outputdir,"nh3em_crit_gw.asc")
    nh3em_crit_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)  
    
    ndep_crit_gw_tot = ascraster.duplicategrid(nh3em_crit_gw)
    ndep_crit_gw_tot.add(nox_em)
    ndep_crit_gw_tot.add(nh3_tot_egl)
    ndep_crit_gw_agri = ascraster.duplicategrid(ndep_crit_gw_tot)
    ndep_crit_gw_agri.multiply(fagri)
    print_debug(ndep_crit_gw_agri,"The critical N deposition on ag. land for the groundwater criterion is")
    
    # calculate total critical N inputs groundwater
    nin_crit_gw_agri = ascraster.duplicategrid(nman_crit_gw)
    nin_crit_gw_agri.add(nfert_crit_gw)
    nin_crit_gw_agri.add(ndep_crit_gw_agri)
    nin_crit_gw_agri.add(n_fix_agri)
    fileout = os.path.join(params.outputdir,"nin_crit_gw_agri.asc")
    nin_crit_gw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_gw_agri,"The total critical input for the groundwater criterion is")
    
    # calculate N surface runoff at critical N inputs groundwater
    nsro_crit_gw_agri = ascraster.duplicategrid(nin_crit_gw_agri)
    nsro_crit_gw_agri.multiply(fsro_ag)
    print_debug(nsro_crit_gw_agri,"The critical N surface runoff for the groundwater criterion is")
    
    # calculate N uptake at critical N inputs
    nup_crit_gw_agri = ascraster.duplicategrid(nin_crit_gw_agri)
    nup_crit_gw_agri.substract(nsro_crit_gw_agri)
    nup_crit_gw_agri.multiply(frnup_agri)
    fileout = os.path.join(params.outputdir,"nup_crit_gw_agri.asc")
    nup_crit_gw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_gw_agri,"The N uptake for the groundwater criterion is")
    
    # calculate NUE
    nue_crit_gw_agri = ascraster.duplicategrid(nup_crit_gw_agri)
    nue_crit_gw_agri.divide(nin_crit_gw_agri, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_gw_agri.asc")
    nue_crit_gw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_gw_agri,"The NUE for the groundwater criterion is")
    
    # calculate maximum uptake fraction
    fnup_max_gw = ascraster.duplicategrid(n_up_max)
    fnup_max_gw.divide(nup_crit_gw_agri)
    fileout = os.path.join(params.outputdir,"fnup_max_gw.asc")
    fnup_max_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_gw,"The fraction maximum uptake / critical uptake for groundwater is")
    
    # calculate correction factor for those cases where critical N uptake exceeds max. N uptake 
    fnup_corr_gw = ascraster.duplicategrid(n_in_max)
    fnup_corr_gw.substract(n_fix_agri)
    
    temp2 = ascraster.duplicategrid(nh3_tot_egl)
    temp2.add(nox_em)
    temp2.multiply(fagri)
    fnup_corr_gw.substract(temp2)
    
    temp3 = ascraster.duplicategrid(nh3em_crit_gw)
    temp3.multiply(fagri)
    temp3.add(nman_crit_gw)
    temp3.add(nfert_crit_gw)
    fnup_corr_gw.divide(temp3, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir,"fnup_corr_gw.asc")
    fnup_corr_gw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_gw,"The correction factor for cases where Nup,crit>Nup,max is")
    
        
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
    nbud_crit_gw_agri = ascraster.duplicategrid(nin_crit_gw_agri)
    nbud_crit_gw_agri.substract(nup_crit_gw_agri)
    print_debug(nbud_crit_gw_agri,"The critical N budget for the groundwater criterion is")
  
    # Critical leaching
    nle_crit_gw_agri_test = ascraster.duplicategrid(nbud_crit_gw_agri)
    nle_crit_gw_agri_test.substract(nsro_crit_gw_agri)
    nle_crit_gw_agri_test.multiply(fle_ag)
    print_debug(nle_crit_gw_agri_test,"The critical N leaching for the groundwater criterion is")
    
    # TEST IF FORWARD CALCULATIONS EQUAL BACKWARD CALLCULATION
    if icell_debug<0:
        pass
    else:
        fw = nle_crit_gw_agri_test.get_data(icell_debug)
        bw = nle_crit_gw_agri.get_data(icell_debug)
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