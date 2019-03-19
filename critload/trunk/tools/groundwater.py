# ******************************************************
## Revision "$LastChangedDate: 2019-01-31 12:05:37 +0100 (Thu, 31 Jan 2019) $"
## Date "$LastChangedRevision: 620 $"
## Author "$LastChangedBy: arthurbeusen $"
# ******************************************************

import os

import ascraster

from print_debug import *

def calculate(params):
    
    print("The critical N conc in gw is", params.crit_gw)    
    
    # calculate nle,ag,crit(gw) Nle,ag(crit)=(1-fsro)*Q*fag*Nconc,le,ag(crit)
    fsro_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc"),numtype=float,mask=params.mask)
    q = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"q.asc"),numtype=float,mask=params.mask)
    fag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fag.asc"),numtype=float,mask=params.mask)
    
    one_grid = ascraster.duplicategrid(fsro_ag)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
    one_min_fsro = ascraster.duplicategrid(one_grid)
    one_min_fsro.substract(fsro_ag)
    nle_ag_crit_gw = ascraster.duplicategrid(one_min_fsro)
    nle_ag_crit_gw.multiply(q)
    nle_ag_crit_gw.multiply(fag)
    nle_ag_crit_gw.multiply(params.crit_gw)
    print_debug(nle_ag_crit_gw,"The critical leaching is")
    
    # calculate critical N input from manure
    fle_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc"),numtype=float,mask=params.mask)
    nup_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"n_up_ag.asc"),numtype=float,mask=params.mask)
    nfix_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"nfix_ag.asc"),numtype=float,mask=params.mask)
    nox_em = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc"),numtype=float,mask=params.mask)
    nh3_ef_man = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man.asc"),numtype=float,mask=params.mask)
    nh3_ef_fert = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert.asc"),numtype=float,mask=params.mask)
    frnfe = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe.asc"),numtype=float,mask=params.mask)
    
    nman_crit_gw = ascraster.duplicategrid(nle_ag_crit_gw)
    nman_crit_gw.divide(fle_ag, default_nodata_value = -99)
    nman_crit_gw.add(nup_ag)
    nman_crit_gw.divide(one_min_fsro, default_nodata_value = -99)
    nman_crit_gw.substract(nfix_ag)
    nox_times_fag = ascraster.duplicategrid(nox_em)
    nox_times_fag.multiply(fag)
    nman_crit_gw.substract(nox_times_fag)
    
    pt1 = ascraster.duplicategrid(fag)
    pt1.multiply(nh3_ef_man)
    pt1.add(one_grid)
    
    pt2 = ascraster.duplicategrid(fag)
    pt2.multiply(nh3_ef_fert)
    pt2.add(one_grid)
    
    one_min_frnfe = ascraster.duplicategrid(one_grid)
    one_min_frnfe.substract(frnfe)
    frnfe_division = ascraster.duplicategrid(frnfe)
    frnfe_division.divide(one_min_frnfe, default_nodata_value = -99)
    
    pt3 = ascraster.duplicategrid(frnfe_division)
    pt3.multiply(pt2)
    
    pt4 = ascraster.duplicategrid(pt1)
    pt4.add(pt3)
   
    nman_crit_gw.divide(pt4, default_nodata_value = -99)
    
    fileout = os.path.join(params.outputdir,"nman_crit_gw.asc")
    nman_crit_gw.write_ascii_file(fileout,output_nodata_value=-999,compress=params.lcompress)
    print_debug(nman_crit_gw,"The critical N input from manure for the groundwater criterion is")
    
    # calculate critical N input from fertilizer
    nfert_crit_gw = ascraster.duplicategrid(nman_crit_gw)
    nfert_crit_gw.multiply(frnfe_division)
    fileout = os.path.join(params.outputdir,"nfert_crit_gw.asc")
    nfert_crit_gw.write_ascii_file(fileout,output_nodata_value=-999,compress=params.lcompress)
    print_debug(nfert_crit_gw,"The critical N input from fertilizer for the groundwater criterion is")
    
    # calculate related N deposition
    nh3em_man_crit_gw = ascraster.duplicategrid(nman_crit_gw)
    nh3em_man_crit_gw.multiply(nh3_ef_man)
    nh3em_fert_crit_gw = ascraster.duplicategrid(nfert_crit_gw)
    nh3em_fert_crit_gw.multiply(nh3_ef_fert)
    nh3em_tot_crit_gw = ascraster.duplicategrid(nh3em_fert_crit_gw)
    nh3em_tot_crit_gw.add(nh3em_man_crit_gw)
    nem_tot_crit_gw = ascraster.duplicategrid(nh3em_tot_crit_gw)
    nem_tot_crit_gw.add(nox_em)
    ndep_ag_crit_gw = ascraster.duplicategrid(nem_tot_crit_gw)
    ndep_ag_crit_gw.multiply(fag)
    print_debug(ndep_ag_crit_gw,"The critical N deposition on ag. land for the groundwater criterion is")
    
    # calculate total critical N inputs groundwater
    nin_tot_crit_gw = ascraster.duplicategrid(nman_crit_gw)
    nin_tot_crit_gw.add(nfert_crit_gw)
    nin_tot_crit_gw.add(ndep_ag_crit_gw)
    nin_tot_crit_gw.add(nfix_ag)
    print_debug(nin_tot_crit_gw,"The total critical input for the groundwater criterion is")
    
    # calculate implied NUE
    nue_crit_gw = ascraster.duplicategrid(nup_ag)
    nue_crit_gw.divide(nin_tot_crit_gw, default_nodata_value = -99)
    fileout = os.path.join(params.outputdir,"nue_crit_gw.asc")
    nue_crit_gw.write_ascii_file(fileout,output_nodata_value=-999,compress=params.lcompress)
    print_debug(nue_crit_gw,"The implied NUE for the groundwater criterion is")
    
    # FORWARD CALCULATIONS TO CHECK
    # Critical N budget
    nbud_ag_crit_gw = ascraster.duplicategrid(nin_tot_crit_gw)
    nbud_ag_crit_gw.substract(nup_ag)
    print_debug(nbud_ag_crit_gw,"The critical N budget for the groundwater criterion is")
    
    # Critical surface runoff
    nsro_ag_crit_gw = ascraster.duplicategrid(nin_tot_crit_gw)
    nsro_ag_crit_gw.multiply(fsro_ag)
    print_debug(nsro_ag_crit_gw,"The critical N surface runoff for the groundwater criterion is")
    
    # Critical leaching
    nle_ag_crit_gw_test = ascraster.duplicategrid(nbud_ag_crit_gw)
    nle_ag_crit_gw_test.substract(nsro_ag_crit_gw)
    nle_ag_crit_gw_test.multiply(fle_ag)
    print_debug(nle_ag_crit_gw_test,"The critical N leaching for the groundwater criterion is")
    
    # TEST IF FORWARD CALCULATIONS EQUAL BACKWARD CALLCULATION
    bw = round(nle_ag_crit_gw.get_data(3),4)
    fw = round(nle_ag_crit_gw_test.get_data(3),4)
    
    if bw == fw:
        print("Comparison of backward and forward calculation was SUCCESFUL")
    else:
        print("ATTENTION!!! Comparison of backward and forward calculation NOT successful")