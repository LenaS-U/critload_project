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
    
    # load needed variables for calculations
    n_fix_egl        = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "nfix_grass_ext.asc")     ,numtype=float,mask=params.mask)
    n_fix_nat        = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "nfix_nat.asc")           ,numtype=float,mask=params.mask)
    nup_egl          = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "n_up_grass_ext.asc")     ,numtype=float,mask=params.mask)    
    q                = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "q.asc")                  ,numtype=float,mask=params.mask)
    nman_egl         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nman_egl.asc")           ,numtype=float,mask=params.mask)  
    npoint_tot       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"npoint_tot.asc")         ,numtype=float,mask=params.mask)
    nero_tot         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nero_tot.asc")           ,numtype=float,mask=params.mask)
    nload_fixed_ag   = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_ag.asc")     ,numtype=float,mask=params.mask)
    nload_fixed_nat  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_nat.asc")    ,numtype=float,mask=params.mask)
    fle_ag           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc")             ,numtype=float,mask=params.mask)
    fle_nat          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_nat.asc")            ,numtype=float,mask=params.mask)
    fsro_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")            ,numtype=float,mask=params.mask)
    fsro_nat         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_nat.asc")           ,numtype=float,mask=params.mask)
    frnup_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_agri.asc")         ,numtype=float,mask=params.mask)
    fgw_rec_le_ag    = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_ag.asc")      ,numtype=float,mask=params.mask)
    fgw_rec_le_nat   = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_nat.asc")     ,numtype=float,mask=params.mask)
    n_fix_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_fix_agri.asc")         ,numtype=float,mask=params.mask)
    nox_em           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")             ,numtype=float,mask=params.mask)
    nh3_tot_egl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")        ,numtype=float,mask=params.mask)
    nh3_ef_man_agri  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_agri.asc")    ,numtype=float,mask=params.mask)
    nh3_ef_fert_agri = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert_agri.asc")   ,numtype=float,mask=params.mask)
    frnfe_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_agri.asc")         ,numtype=float,mask=params.mask)
    fagri            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fagri.asc")              ,numtype=float,mask=params.mask)
    fegl             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fegl.asc")               ,numtype=float,mask=params.mask)
    fnat             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fnat.asc")               ,numtype=float,mask=params.mask)
    n_up_max         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_up_max.asc")           ,numtype=float,mask=params.mask)
    n_in_max         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_in_max.asc")           ,numtype=float,mask=params.mask)   
     
    # calculate Nload,crit,sw =Q*Nconc,sw(crit)
    nload_crit_sw = ascraster.duplicategrid(q)
    nload_crit_sw.multiply(params.crit_sw)
    #fileout = os.path.join(params.outputdir,"nload_crit_sw.asc")
    #nload_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_crit_sw,"The critical N load to surface water is")
   
    # calculate fixed N load to surface water
    nload_fixed_tot = ascraster.duplicategrid(npoint_tot)
    nload_fixed_tot.add(nero_tot)
    nload_fixed_tot.add(nload_fixed_ag)
    nload_fixed_tot.add(nload_fixed_nat)
    print_debug(nload_fixed_tot,"The fixed N load to surface water is")
    
    # calculate parameter 'v' 
    v_part1 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_part1.multiply(fle_ag)
    v_part2 = ascraster.duplicategrid(v_part1)
    v_part2.multiply(frnup_agri)
    v_part3 = ascraster.duplicategrid(v_part2)
    v_part3.multiply(fsro_ag)
    v_part4 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_part4.multiply(fle_ag)
    v_part4.multiply(fsro_ag)
    v = ascraster.duplicategrid(v_part1)
    v.substract(v_part2)
    v.add(v_part3)
    v.substract(v_part4)
    v.add(fsro_ag)
    print_debug(v,"The value for parameter v is")
    
    # calculate parameter 'w' 
    w_part1 = ascraster.duplicategrid(fgw_rec_le_nat)
    w_part1.multiply(fle_nat)
    w_part2 = ascraster.duplicategrid(w_part1)
    w_part2.multiply(fsro_nat)
    w = ascraster.duplicategrid(w_part1)
    w.substract(w_part2)
    w.add(fsro_nat)
    print_debug(w,"The value for parameter w is")
    
    # calculate parameter 'x' 
    x_part1 = ascraster.duplicategrid(fle_ag)
    x_part1.multiply(fgw_rec_le_ag)
    one_grid = ascraster.duplicategrid(fsro_ag)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
        
    one_min_fsro_ag = ascraster.duplicategrid(one_grid)
    one_min_fsro_ag.substract(fsro_ag)
    x_part1.multiply(one_min_fsro_ag)
    
    x = ascraster.duplicategrid(fsro_ag)
    x.add(x_part1)
    print_debug(x,"The value for parameter x is")
    
    # calculate critical N input from manure
    #numerator
    numerator = ascraster.duplicategrid(nload_crit_sw)
 
    n1 = ascraster.duplicategrid(fle_ag)
    n1.multiply(fgw_rec_le_ag)
    n1.multiply(nup_egl)
    
    n2 = ascraster.duplicategrid(nox_em)
    n2.add(nh3_tot_egl)
    n2.multiply(fagri)
    n2.add(n_fix_agri)
    n2.multiply(v)
    
    n3 = ascraster.duplicategrid(nox_em)
    n3.add(nh3_tot_egl)
    n3.multiply(fnat)
    n3.add(n_fix_nat)
    n3.multiply(w)

    n4 = ascraster.duplicategrid(nox_em)
    n4.add(nh3_tot_egl)
    n4.multiply(fegl)
    n4.add(n_fix_egl)
    n4.add(nman_egl)
    n4.add(nh3_tot_egl) #$#V1.2#$#
    n4.multiply(x)     

    numerator.substract(nload_fixed_tot)
    numerator.add(n1)    
    numerator.substract(n2)
    numerator.substract(n3)
    numerator.substract(n4)
    
    #denominator
    d1 = ascraster.duplicategrid(v)
    d1.multiply(fagri)  
    
    d2 = ascraster.duplicategrid(w)
    d2.multiply(fnat)
    
    d3 = ascraster.duplicategrid(x)
    d3.multiply(fegl)
    
    d3.add(d2)
    d3.add(d1)
    
    d4 = ascraster.duplicategrid(d3)
    d4.multiply(nh3_ef_man_agri)
    d4.add(v)

    denominator = ascraster.duplicategrid(d3)
    denominator.multiply(nh3_ef_fert_agri) 
    denominator.add(v)
    
    one_grid = ascraster.duplicategrid(fsro_ag)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
        
    one_min_frnfe_agri = ascraster.duplicategrid(one_grid)
    one_min_frnfe_agri.substract(frnfe_agri)
    frnfe_division = ascraster.duplicategrid(frnfe_agri)
    frnfe_division.divide(one_min_frnfe_agri, default_nodata_value = -9999)        
    
    denominator.multiply(frnfe_division)
    denominator.add(d4)
    
    nman_crit_sw = ascraster.duplicategrid(numerator)
    nman_crit_sw.divide(denominator, default_nodata_value = -9999)
    
    for icell in range (nman_crit_sw.length):
        nman = nman_crit_sw.get_data(icell)
        if (nman is None):
            continue
        if (nman < 0):
            man = 0
        else:
            continue
        nman_crit_sw.set_data(icell,man)
    
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
    nh3em_man_crit_sw.multiply(nh3_ef_man_agri)
    
    fileout = os.path.join(params.outputdir,"nh3em_man_crit_sw.asc")
    nh3em_man_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
        
    nh3em_fert_crit_sw = ascraster.duplicategrid(nfert_crit_sw)
    nh3em_fert_crit_sw.multiply(nh3_ef_fert_agri)
    
    fileout = os.path.join(params.outputdir,"nh3em_fert_crit_sw.asc")
    nh3em_fert_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    nh3em_crit_sw = ascraster.duplicategrid(nh3em_fert_crit_sw)
    nh3em_crit_sw.add(nh3em_man_crit_sw)
    
    fileout = os.path.join(params.outputdir,"nh3em_crit_sw.asc")
    nh3em_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    ndep_crit_sw_tot = ascraster.duplicategrid(nh3em_crit_sw)
    ndep_crit_sw_tot.add(nox_em)
    ndep_crit_sw_tot.add(nh3_tot_egl)
    ndep_crit_sw_agri = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_agri.multiply(fagri)
    print_debug(ndep_crit_sw_agri,"The critical N deposition for the surface water criterion is")
    
    # calculate total critical N inputs surface water
    nin_crit_sw_agri = ascraster.duplicategrid(nman_crit_sw)
    nin_crit_sw_agri.add(nfert_crit_sw)
    nin_crit_sw_agri.add(ndep_crit_sw_agri)
    nin_crit_sw_agri.add(n_fix_agri)
    fileout = os.path.join(params.outputdir,"nin_crit_sw_agri.asc")
    nin_crit_sw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_sw_agri,"The total critical input for the surface water criterion is")
    
    # calculate N surface runoff at critical N inputs surface water
    nsro_crit_sw_agri = ascraster.duplicategrid(nin_crit_sw_agri)
    nsro_crit_sw_agri.multiply(fsro_ag)
    print_debug(nsro_crit_sw_agri,"The critical N surface runoff for the surface water criterion is")
         
    # calculate N uptake at critical N inputs
    nup_crit_sw_agri = ascraster.duplicategrid(nin_crit_sw_agri)
    nup_crit_sw_agri.substract(nsro_crit_sw_agri)
    nup_crit_sw_agri.multiply(frnup_agri)
    fileout = os.path.join(params.outputdir,"nup_crit_sw_agri.asc")
    nup_crit_sw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_sw_agri,"The N uptake for the surface criterion is")

    # calculate NUE
    nue_crit_sw_agri = ascraster.duplicategrid(nup_crit_sw_agri)
    nue_crit_sw_agri.divide(nin_crit_sw_agri, default_nodata_value = -9999)
    #fileout = os.path.join(params.outputdir,"nue_crit_sw_agri.asc")
    #nue_crit_sw_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_sw_agri,"The NUE for the surface water criterion is")
    
    # calculate maximum uptake fraction
    fnup_max_sw = ascraster.duplicategrid(n_up_max)
    fnup_max_sw.divide(nup_crit_sw_agri)
    fileout = os.path.join(params.outputdir,"fnup_max_sw.asc")
    fnup_max_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_sw,"The fraction maximum uptake / critical uptake for surface water is")
    
    # calculate correction factor for those cases where critical N uptake exceeds max. N uptake 
    fnup_corr_sw = ascraster.duplicategrid(n_in_max)
    fnup_corr_sw.substract(n_fix_agri)
    
    temp2 = ascraster.duplicategrid(nh3_tot_egl)
    temp2.add(nox_em)
    temp2.multiply(fagri)
    fnup_corr_sw.substract(temp2)
    
    temp3 = ascraster.duplicategrid(nh3em_crit_sw)
    temp3.multiply(fagri)
    temp3.add(nman_crit_sw)
    temp3.add(nfert_crit_sw)
    fnup_corr_sw.divide(temp3, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir,"fnup_corr_sw.asc")
    fnup_corr_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_sw,"The correction factor for cases where Nup,crit>Nup,max is")
 
 
    # FORWARD CALCULATIONS TO CHECK
    # 1: N load from agricultural land
    # Critical N budget
    nbud_crit_sw_agri = ascraster.duplicategrid(nin_crit_sw_agri)
    nbud_crit_sw_agri.substract(nup_crit_sw_agri)
    print_debug(nbud_crit_sw_agri,"The critical N budget for the surface water criterion is")
    # nle ag crit sw
    nle_crit_sw_agri = ascraster.duplicategrid(nbud_crit_sw_agri)
    nle_crit_sw_agri.substract(nsro_crit_sw_agri)
    nle_crit_sw_agri.multiply(fle_ag) # ,minimum = 0.0
    print_debug(nle_crit_sw_agri,"The critical N leaching for the surface water criterion is")
    # ngw_rec_ag crit sw
    ngw_rec_crit_sw_agri = ascraster.duplicategrid(nle_crit_sw_agri)
    ngw_rec_crit_sw_agri.multiply(fgw_rec_le_ag)
    print_debug(ngw_rec_crit_sw_agri,"The critical groundwater N load to surface water from agriculture due to RECENT N inputs for the surface water criterion is")
    # nload var ag crit sw
    nload_var_crit_sw_agri = ascraster.duplicategrid(nsro_crit_sw_agri)
    nload_var_crit_sw_agri.add(ngw_rec_crit_sw_agri)
    print_debug(nload_var_crit_sw_agri,"The variable critial N load to surface water from ag. areas for the surface water criterion is")
   
    # 2: N load from natural land
    # ndep nat crit sw
    ndep_crit_sw_nat = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_nat.multiply(fnat)
    print_debug(ndep_crit_sw_nat,"The critical N deposition on natural areas for the surface water criterion is")
    # nbud nat crit sw
    nbud_crit_sw_nat = ascraster.duplicategrid(ndep_crit_sw_nat)
    nbud_crit_sw_nat.add(n_fix_nat)
    print_debug(nbud_crit_sw_nat,"The critical N budget for natural areas for the surface water criterion is")
    # nsro nat crit sw
    nsro_crit_sw_nat = ascraster.duplicategrid(nbud_crit_sw_nat)
    nsro_crit_sw_nat.multiply(fsro_nat)
    print_debug(nsro_crit_sw_nat,"The critical N surface runoff for natural areas for the surface water criterion is")
    # nle nat crit sw
    nle_crit_sw_nat = ascraster.duplicategrid(nbud_crit_sw_nat)
    nle_crit_sw_nat.substract(nsro_crit_sw_nat)
    nle_crit_sw_nat.multiply(fle_nat)
    print_debug(nle_crit_sw_nat,"The critical N leaching for natural areas for the surface water criterion is")
    # ngw_rec_nat crit sw
    ngw_rec_crit_sw_nat = ascraster.duplicategrid(nle_crit_sw_nat)
    ngw_rec_crit_sw_nat.multiply(fgw_rec_le_nat)
    print_debug(ngw_rec_crit_sw_nat,"The critical groundwater N load to surface water from natural areas due to RECENT N inputs for the surface water criterion is")
    # nload var nat crit sw
    nload_var_crit_sw_nat = ascraster.duplicategrid(nsro_crit_sw_nat)
    nload_var_crit_sw_nat.add(ngw_rec_crit_sw_nat)
    print_debug(nload_var_crit_sw_nat,"The variable critical N load to surface water from natural areas for the surface water criterion is")
    
    # 3: N load from extensive grassland
    # ndep egl crit sw
    ndep_crit_sw_egl = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_egl.multiply(fegl)
    print_debug(ndep_crit_sw_egl,"The critical N deposition on extensive grasslands for the surface water criterion is")
    # nin egl crit sw
    nin_crit_sw_egl = ascraster.duplicategrid(ndep_crit_sw_egl)
    nin_crit_sw_egl.add(n_fix_egl)
    nin_crit_sw_egl.add(nman_egl)
    nin_crit_sw_egl.add(nh3_tot_egl) #$#V1.2#$#
    print_debug(nin_crit_sw_egl,"The critical N input to extensive grasslands for the surface water criterion is")   
    # nsro egl crit sw
    nsro_crit_sw_egl = ascraster.duplicategrid(nin_crit_sw_egl)
    nsro_crit_sw_egl.multiply(fsro_ag)
    print_debug(nsro_crit_sw_egl,"The critical N surface runoff for extensive grasslands for the surface water criterion is")
    # nbud egl crit sw
    nbud_crit_sw_egl = ascraster.duplicategrid(nin_crit_sw_egl)
    nbud_crit_sw_egl.substract(nup_egl)
    print_debug(nbud_crit_sw_egl,"The critical N budget for extensive grasslands for the surface water criterion is")   
    #  nle egl crit sw
    nle_crit_sw_egl = ascraster.duplicategrid(nbud_crit_sw_egl)
    nle_crit_sw_egl.substract(nsro_crit_sw_egl)
    nle_crit_sw_egl.multiply(fle_ag)
    print_debug(nle_crit_sw_egl,"The critical N leaching for extensive grasslands for the surface water criterion is")    
    # ngw_rec_egl crit sw
    ngw_rec_crit_sw_egl = ascraster.duplicategrid(nle_crit_sw_egl)
    ngw_rec_crit_sw_egl.multiply(fgw_rec_le_ag)
    print_debug(ngw_rec_crit_sw_egl,"The critical groundwater N load to surface water from extensive grassland due to RECENT N inputs for the surface water criterion is")
    # nload var egl crit sw
    nload_var_crit_sw_egl = ascraster.duplicategrid(nsro_crit_sw_egl)
    nload_var_crit_sw_egl.add(ngw_rec_crit_sw_egl)
    print_debug(nload_var_crit_sw_egl,"The variable critial N load to surface water from extensive grassland for the surface water criterion is") 
 
    # calculate n load tot crit sw TEST
    nload_crit_sw_test = ascraster.duplicategrid(nload_var_crit_sw_agri)
    nload_crit_sw_test.add(nload_var_crit_sw_nat)
    nload_crit_sw_test.add(nload_var_crit_sw_egl)
    nload_crit_sw_test.add(nload_fixed_tot)
        
    ########### FORWARD CALCULATIONS TO CHECK ###########
    if icell_debug<0:
        pass
    else:
        fw = nload_crit_sw_test.get_data(icell_debug)
        bw = nload_crit_sw.get_data(icell_debug)
        #print(fw)
        #print(bw)
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
   