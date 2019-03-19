# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/surfacewater.py $"
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

    print("The critical N concentration in surface water is", params.crit_sw)
    
    # calculate Nload,crit,sw =Q*Nconc,sw(crit)
    q = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"q.asc"),numtype=float,mask=params.mask)
    nload_crit_sw = ascraster.duplicategrid(q)
    nload_crit_sw.multiply(params.crit_sw)
    print_debug(nload_crit_sw,"The critical N load to surface water is")
    
    # calculate fixed N load to surface water
    npoint_tot = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"npoint_tot.asc"),numtype=float,mask=params.mask)
    nero_tot = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nero_tot.asc"),numtype=float,mask=params.mask)
    nload_fixed_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_ag.asc"),numtype=float,mask=params.mask)
    nload_fixed_nat = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_nat.asc"),numtype=float,mask=params.mask)
    nload_fixed_tot = ascraster.duplicategrid(npoint_tot)
    nload_fixed_tot.add(nero_tot)
    nload_fixed_tot.add(nload_fixed_ag)
    nload_fixed_tot.add(nload_fixed_nat)
    print_debug(nload_fixed_tot,"The fixed N load to surface water is")
    
    # calculate parameter 'v' 
    fle_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc"),numtype=float,mask=params.mask)
    fsro_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc"),numtype=float,mask=params.mask)
    fgw_rec_le_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_ag.asc"),numtype=float,mask=params.mask)
    v_part1 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_part1.multiply(fle_ag)
    v_part2 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_part2.multiply(fle_ag)
    v_part2.multiply(fsro_ag)
    v = ascraster.duplicategrid(v_part1)
    v.substract(v_part2)
    v.add(fsro_ag)
    print_debug(v,"The value for parameter v is")
    
    # calculate parameter 'w' 
    fle_nat = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_nat.asc"),numtype=float,mask=params.mask)
    fsro_nat = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_nat.asc"),numtype=float,mask=params.mask)
    fgw_rec_le_nat = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_nat.asc"),numtype=float,mask=params.mask)
    w_part1 = ascraster.duplicategrid(fgw_rec_le_nat)
    w_part1.multiply(fle_nat)
    w_part2 = ascraster.duplicategrid(fgw_rec_le_nat)
    w_part2.multiply(fle_nat)
    w_part2.multiply(fsro_nat)
    w = ascraster.duplicategrid(w_part1)
    w.substract(w_part2)
    w.add(fsro_nat)
    print_debug(w,"The value for parameter w is")
    
    # calculate critical N input from manure
    nup_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"n_up_ag.asc"),numtype=float,mask=params.mask)
    nfix_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"nfix_ag.asc"),numtype=float,mask=params.mask)
    nfix_nat = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"nfix_nat.asc"),numtype=float,mask=params.mask)
    nox_em = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc"),numtype=float,mask=params.mask)
    nh3_ef_man = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man.asc"),numtype=float,mask=params.mask)
    nh3_ef_fert = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert.asc"),numtype=float,mask=params.mask)
    frnfe = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe.asc"),numtype=float,mask=params.mask)
    fag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fag.asc"),numtype=float,mask=params.mask)
    fnat = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fnat.asc"),numtype=float,mask=params.mask)
    
    numerator = ascraster.duplicategrid(nload_crit_sw)
        
    pt1 = ascraster.duplicategrid(fgw_rec_le_ag)
    pt1.multiply(fle_ag)
    pt1.multiply(nup_ag)
    
    pt2 = ascraster.duplicategrid(nox_em)
    pt2.multiply(fag)
    pt2.add(nfix_ag)
    pt2.multiply(v)
    
    pt3 = ascraster.duplicategrid(nox_em)
    pt3.multiply(fnat)
    pt3.add(nfix_nat)
    pt3.multiply(w)   
    
    numerator.substract(nload_fixed_tot)
    numerator.add(pt1)
    numerator.substract(pt2)
    numerator.substract(pt3)
    
    pt4 = ascraster.duplicategrid(nh3_ef_man)
    pt4.multiply(fag)
    pt4.multiply(v)
    
    pt5 = ascraster.duplicategrid(nh3_ef_man)
    pt5.multiply(fnat)
    pt5.multiply(w)
    
    pt6 = ascraster.duplicategrid(nh3_ef_fert)
    pt6.multiply(fag)
    pt6.multiply(v)
    
    pt7 = ascraster.duplicategrid(nh3_ef_fert)
    pt7.multiply(fnat)
    pt7.multiply(w)

    pt8 = ascraster.duplicategrid(v)
    pt8.add(pt6)
    pt8.add(pt7)
    
    one_grid = ascraster.duplicategrid(fsro_ag)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
        
    one_min_frnfe = ascraster.duplicategrid(one_grid)
    one_min_frnfe.substract(frnfe)
    frnfe_division = ascraster.duplicategrid(frnfe)
    frnfe_division.divide(one_min_frnfe, default_nodata_value = -9999)
    
    denominator = ascraster.duplicategrid(frnfe_division)
    denominator.multiply(pt8)
    denominator.add(v)
    denominator.add(pt4)
    denominator.add(pt5)
    
    nman_crit_sw = ascraster.duplicategrid(numerator)
    nman_crit_sw.divide(denominator, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir,"nman_crit_sw.asc")
    nman_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_sw,"The critical N input from manure for the surface water criterion is")
    
    # calculate critical N input from fertilizer
    nfert_crit_sw = ascraster.duplicategrid(nman_crit_sw)
    nfert_crit_sw.multiply(frnfe_division)
    fileout = os.path.join(params.outputdir,"nfert_crit_sw.asc")
    nfert_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfert_crit_sw,"The critical N input from fertilizer for the surface water criterion is")
    
    # calculate related N deposition
    nh3em_man_crit_sw = ascraster.duplicategrid(nman_crit_sw)
    nh3em_man_crit_sw.multiply(nh3_ef_man)
    nh3em_fert_crit_sw = ascraster.duplicategrid(nfert_crit_sw)
    nh3em_fert_crit_sw.multiply(nh3_ef_fert)
    nh3em_tot_crit_sw = ascraster.duplicategrid(nh3em_fert_crit_sw)
    nh3em_tot_crit_sw.add(nh3em_man_crit_sw)
    nem_tot_crit_sw = ascraster.duplicategrid(nh3em_tot_crit_sw)
    nem_tot_crit_sw.add(nox_em)
    ndep_ag_crit_sw = ascraster.duplicategrid(nem_tot_crit_sw)
    ndep_ag_crit_sw.multiply(fag)
    print_debug(ndep_ag_crit_sw,"The critical N deposition for the surface water criterion is")
    
    # calculate total critical N inputs surface water
    nin_tot_crit_sw = ascraster.duplicategrid(nman_crit_sw)
    nin_tot_crit_sw.add(nfert_crit_sw)
    nin_tot_crit_sw.add(ndep_ag_crit_sw)
    nin_tot_crit_sw.add(nfix_ag)
    print_debug(nin_tot_crit_sw,"The total critical input for the surface water criterion is")
    
    # calculate implied NUE
    nue_crit_sw = ascraster.duplicategrid(nup_ag)
    nue_crit_sw.divide(nin_tot_crit_sw, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_sw.asc")
    nue_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_sw,"The implied NUE for the surface water criterion is")
    
    # FORWARD CALCULATIONS TO CHECK
    # Critical N budget
    nbud_ag_crit_sw = ascraster.duplicategrid(nin_tot_crit_sw)
    nbud_ag_crit_sw.substract(nup_ag)
    print_debug(nbud_ag_crit_sw,"The critical N budget for the surface water criterion is")
    
    # Critical surface runoff
    nsro_ag_crit_sw = ascraster.duplicategrid(nin_tot_crit_sw)
    nsro_ag_crit_sw.multiply(fsro_ag)
    print_debug(nsro_ag_crit_sw,"The critical N surface runoff for the surface water criterion is")
    
    # Critical leaching - IF NEGATIVE, set to zero
    nle_ag_crit_sw = ascraster.duplicategrid(nbud_ag_crit_sw)
    nle_ag_crit_sw.substract(nsro_ag_crit_sw)
    nle_ag_crit_sw.multiply(fle_ag,minimum = 0.0)
    
    # This part of the code is not needed with the minimum=0.0 (in line above).
    #for icell in range(nle_ag_crit_sw.length):
    #    val=nle_ag_crit_sw.get_data(icell) 
    #    if (val < 0):
    #        nle_ag_crit_sw.set_data(icell,0)        
            
    print_debug(nle_ag_crit_sw,"The critical N leaching for the surface water criterion is")
    
    
    # calculate ndep nat crit sw
    ndep_nat_crit_sw = ascraster.duplicategrid(nem_tot_crit_sw)
    ndep_nat_crit_sw.multiply(fnat)
    print_debug(ndep_nat_crit_sw,"The critical N deposition on natural areas for the surface water criterion is")
    
    # calculate nbud nat crit sw
    nbud_nat_crit_sw = ascraster.duplicategrid(ndep_nat_crit_sw)
    nbud_nat_crit_sw.add(nfix_nat)
    print_debug(nbud_nat_crit_sw,"The critical N budget for natural areas for the surface water criterion is")
    
    # calculate nsro nat crit sw
    nsro_nat_crit_sw = ascraster.duplicategrid(nbud_nat_crit_sw)
    nsro_nat_crit_sw.multiply(fsro_nat)
    print_debug(nsro_nat_crit_sw,"The critical N surface runoff for natural areas for the surface water criterion is")
        
    # calculate n le nat crit sw
    nle_nat_crit_sw = ascraster.duplicategrid(nbud_nat_crit_sw)
    nle_nat_crit_sw.substract(nsro_nat_crit_sw)
    nle_nat_crit_sw.multiply(fle_nat)
    print_debug(nle_nat_crit_sw,"The critical N leaching for natural areas for the surface water criterion is")
    
    # calculate Ngw,rec,ag(crit,sw)
    ngw_rec_ag_crit_sw = ascraster.duplicategrid(nle_ag_crit_sw)
    ngw_rec_ag_crit_sw.multiply(fgw_rec_le_ag)
    print_debug(ngw_rec_ag_crit_sw,"The critical N load to surface water from agriculture due to RECENT N inputs for the surface water criterion is")
    
    # calculate Ngw,rec,nat(crit,sw)
    ngw_rec_nat_crit_sw = ascraster.duplicategrid(nle_nat_crit_sw)
    ngw_rec_nat_crit_sw.multiply(fgw_rec_le_nat)
    print_debug(ngw_rec_nat_crit_sw,"The critical N load to surface water from natural areas due to RECENT N inputs for the surface water criterion is")
    
    # calculate nload var ag crit sw
    nload_var_ag_crit_sw = ascraster.duplicategrid(nsro_ag_crit_sw)
    nload_var_ag_crit_sw.add(ngw_rec_ag_crit_sw)
    print_debug(nload_var_ag_crit_sw,"The variable critial N load to surface water from ag. areas for the surface water criterion is")
    
    # calculate nload var nat crit sw
    nload_var_nat_crit_sw = ascraster.duplicategrid(nsro_nat_crit_sw)
    nload_var_nat_crit_sw.add(ngw_rec_nat_crit_sw)
    print_debug(nload_var_nat_crit_sw,"The variable critial N load to surface water from natural areas for the surface water criterion is")
    
    # calculate n load tot crit sw TEST
    nload_crit_sw_test = ascraster.duplicategrid(nload_var_ag_crit_sw)
    nload_crit_sw_test.add(nload_var_nat_crit_sw)
    nload_crit_sw_test.add(nload_fixed_tot)
    
    # TEST IF FORWARD CALCULATIONS EQUAL BACKWARD CALLCULATION
    # This does not work in the real case.....    
    #bw = round(nload_crit_sw.get_data(3),4)
    #fw = round(nload_crit_sw_test.get_data(3),4)
    
    # for if nbud_crit = 0
    fw2grid = ascraster.duplicategrid(nbud_ag_crit_sw)
    fw2grid.substract(nsro_ag_crit_sw)
    fw2grid.multiply(fle_ag)
    fw2grid.multiply(fgw_rec_le_ag)
    fw2grid.add(nload_crit_sw_test)
   
    #fw2 = round(fw2grid.get_data(3),4)
    
    #if bw == fw:
    #    print("Comparison of backward and forward calculation was SUCCESFUL")
    #elif bw == fw2:
    #    print("Comparison of backward and forward calculation was SUCCESFUL - negative budget")
    #else:   
    #    print("ATTENTION!!! Comparison of backward and forward calculation NOT successful")
