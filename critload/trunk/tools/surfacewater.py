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
    nman_egl         = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "n_man_eff_grass_ext.asc"),numtype=float,mask=params.mask)
    nup_egl          = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "n_up_grass_ext.asc")      ,numtype=float,mask=params.mask)    
    q                = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "q.asc")                  ,numtype=float,mask=params.mask)
    npoint_tot       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"npoint_tot.asc")         ,numtype=float,mask=params.mask)
    nero_tot         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nero_tot.asc")           ,numtype=float,mask=params.mask)
    nload_fixed_ag   = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_ag.asc")     ,numtype=float,mask=params.mask)
    nload_fixed_nat  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_nat.asc")    ,numtype=float,mask=params.mask)
    fle_ag           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc")             ,numtype=float,mask=params.mask)
    fle_nat          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_nat.asc")            ,numtype=float,mask=params.mask)
    fsro_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")            ,numtype=float,mask=params.mask)
    fsro_nat         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_nat.asc")           ,numtype=float,mask=params.mask)
    frnup_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_agri.asc")              ,numtype=float,mask=params.mask)
    fgw_rec_le_ag    = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_ag.asc")      ,numtype=float,mask=params.mask)
    fgw_rec_le_nat   = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_nat.asc")     ,numtype=float,mask=params.mask)
    n_fix_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_fix_agri.asc")          ,numtype=float,mask=params.mask)
    nox_em           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")             ,numtype=float,mask=params.mask)
    nh3_tot_egl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")        ,numtype=float,mask=params.mask)
    nh3_ef_man_agri  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_agri.asc")    ,numtype=float,mask=params.mask)
    nh3_ef_fert_agri = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert_agri.asc")   ,numtype=float,mask=params.mask)
    frnfe_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_agri.asc")         ,numtype=float,mask=params.mask)
    fagri            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fagri.asc")              ,numtype=float,mask=params.mask)
    fegl             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fegl.asc")               ,numtype=float,mask=params.mask)
    fnat             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fnat.asc")               ,numtype=float,mask=params.mask)
    
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
    nh3em_fert_crit_sw = ascraster.duplicategrid(nfert_crit_sw)
    nh3em_fert_crit_sw.multiply(nh3_ef_fert_agri)
    nh3em_tot_crit_sw = ascraster.duplicategrid(nh3em_fert_crit_sw)
    nh3em_tot_crit_sw.add(nh3em_man_crit_sw)
    nem_tot_crit_sw = ascraster.duplicategrid(nh3em_tot_crit_sw)
    nem_tot_crit_sw.add(nox_em)
    nem_tot_crit_sw.add(nh3_tot_egl)
    ndep_ag_crit_sw = ascraster.duplicategrid(nem_tot_crit_sw)
    ndep_ag_crit_sw.multiply(fagri)
    print_debug(ndep_ag_crit_sw,"The critical N deposition for the surface water criterion is")
    
    # calculate total critical N inputs surface water
    nin_tot_crit_sw = ascraster.duplicategrid(nman_crit_sw)
    nin_tot_crit_sw.add(nfert_crit_sw)
    nin_tot_crit_sw.add(ndep_ag_crit_sw)
    nin_tot_crit_sw.add(n_fix_agri)
    print_debug(nin_tot_crit_sw,"The total critical input for the surface water criterion is")
    
    # calculate N surface runoff at critical N inputs surface water
    nsro_ag_crit_sw = ascraster.duplicategrid(nin_tot_crit_sw)
    nsro_ag_crit_sw.multiply(fsro_ag)
    print_debug(nsro_ag_crit_sw,"The critical N surface runoff for the surface water criterion is")
         
    # calculate N uptake at critical N inputs
    nup_ag_crit_sw = ascraster.duplicategrid(nin_tot_crit_sw)
    nup_ag_crit_sw.substract(nsro_ag_crit_sw)
    nup_ag_crit_sw.multiply(frnup_agri)
    print_debug(nup_ag_crit_sw,"The N uptake for the surface criterion is")

    # calculate NUE
    nue_crit_sw = ascraster.duplicategrid(nup_ag_crit_sw)
    nue_crit_sw.divide(nin_tot_crit_sw, default_nodata_value = -9999)
    #fileout = os.path.join(params.outputdir,"nue_crit_sw.asc")
    #nue_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_sw,"The NUE for the surface water criterion is")
    
    # FORWARD CALCULATIONS TO CHECK
    # 1: N load from agricultural land
    # Critical N budget
    nbud_ag_crit_sw = ascraster.duplicategrid(nin_tot_crit_sw)
    nbud_ag_crit_sw.substract(nup_ag_crit_sw)
    print_debug(nbud_ag_crit_sw,"The critical N budget for the surface water criterion is")
    # nle ag crit sw
    nle_ag_crit_sw = ascraster.duplicategrid(nbud_ag_crit_sw)
    nle_ag_crit_sw.substract(nsro_ag_crit_sw)
    nle_ag_crit_sw.multiply(fle_ag) # ,minimum = 0.0
    print_debug(nle_ag_crit_sw,"The critical N leaching for the surface water criterion is")
    # ngw_rec_ag crit sw
    ngw_rec_ag_crit_sw = ascraster.duplicategrid(nle_ag_crit_sw)
    ngw_rec_ag_crit_sw.multiply(fgw_rec_le_ag)
    print_debug(ngw_rec_ag_crit_sw,"The critical groundwater N load to surface water from agriculture due to RECENT N inputs for the surface water criterion is")
    # nload var ag crit sw
    nload_var_ag_crit_sw = ascraster.duplicategrid(nsro_ag_crit_sw)
    nload_var_ag_crit_sw.add(ngw_rec_ag_crit_sw)
    print_debug(nload_var_ag_crit_sw,"The variable critial N load to surface water from ag. areas for the surface water criterion is")
   
    # 2: N load from natural land
    # ndep nat crit sw
    ndep_nat_crit_sw = ascraster.duplicategrid(nem_tot_crit_sw)
    ndep_nat_crit_sw.multiply(fnat)
    print_debug(ndep_nat_crit_sw,"The critical N deposition on natural areas for the surface water criterion is")
    # nbud nat crit sw
    nbud_nat_crit_sw = ascraster.duplicategrid(ndep_nat_crit_sw)
    nbud_nat_crit_sw.add(n_fix_nat)
    print_debug(nbud_nat_crit_sw,"The critical N budget for natural areas for the surface water criterion is")
    # nsro nat crit sw
    nsro_nat_crit_sw = ascraster.duplicategrid(nbud_nat_crit_sw)
    nsro_nat_crit_sw.multiply(fsro_nat)
    print_debug(nsro_nat_crit_sw,"The critical N surface runoff for natural areas for the surface water criterion is")
    # nle nat crit sw
    nle_nat_crit_sw = ascraster.duplicategrid(nbud_nat_crit_sw)
    nle_nat_crit_sw.substract(nsro_nat_crit_sw)
    nle_nat_crit_sw.multiply(fle_nat)
    print_debug(nle_nat_crit_sw,"The critical N leaching for natural areas for the surface water criterion is")
    # ngw_rec_nat crit sw
    ngw_rec_nat_crit_sw = ascraster.duplicategrid(nle_nat_crit_sw)
    ngw_rec_nat_crit_sw.multiply(fgw_rec_le_nat)
    print_debug(ngw_rec_nat_crit_sw,"The critical groundwater N load to surface water from natural areas due to RECENT N inputs for the surface water criterion is")
    # nload var nat crit sw
    nload_var_nat_crit_sw = ascraster.duplicategrid(nsro_nat_crit_sw)
    nload_var_nat_crit_sw.add(ngw_rec_nat_crit_sw)
    print_debug(nload_var_nat_crit_sw,"The variable critial N load to surface water from natural areas for the surface water criterion is")
    
    # 3: N load from extensive grassland
    # ndep egl crit sw
    ndep_egl_crit_sw = ascraster.duplicategrid(nem_tot_crit_sw)
    ndep_egl_crit_sw.multiply(fegl)
    print_debug(ndep_egl_crit_sw,"The critical N deposition on extensive grasslands for the surface water criterion is")
    # nin egl crit sw
    nin_egl_crit_sw = ascraster.duplicategrid(ndep_egl_crit_sw)
    nin_egl_crit_sw.add(n_fix_egl)
    nin_egl_crit_sw.add(nman_egl)
    print_debug(nin_egl_crit_sw,"The critical N input to extensive grasslands for the surface water criterion is")   
    # nsro egl crit sw
    nsro_egl_crit_sw = ascraster.duplicategrid(nin_egl_crit_sw)
    nsro_egl_crit_sw.multiply(fsro_ag)
    print_debug(nsro_egl_crit_sw,"The critical N surface runoff for extensive grasslands for the surface water criterion is")
    # nbud egl crit sw
    nbud_egl_crit_sw = ascraster.duplicategrid(nin_egl_crit_sw)
    nbud_egl_crit_sw.substract(nup_egl)
    print_debug(nbud_egl_crit_sw,"The critical N budget runoff for extensive grasslands for the surface water criterion is")   
    #  nle egl crit sw
    nle_egl_crit_sw = ascraster.duplicategrid(nbud_egl_crit_sw)
    nle_egl_crit_sw.substract(nsro_egl_crit_sw)
    nle_egl_crit_sw.multiply(fle_ag)
    print_debug(nle_egl_crit_sw,"The critical N budget runoff for extensive grasslands for the surface water criterion is")    
    # ngw_rec_egl crit sw
    ngw_rec_egl_crit_sw = ascraster.duplicategrid(nle_egl_crit_sw)
    ngw_rec_egl_crit_sw.multiply(fgw_rec_le_ag)
    print_debug(ngw_rec_egl_crit_sw,"The critical groundwater N load to surface water from extensive grassland due to RECENT N inputs for the surface water criterion is")
    # nload var egl crit sw
    nload_var_egl_crit_sw = ascraster.duplicategrid(nsro_egl_crit_sw)
    nload_var_egl_crit_sw.add(ngw_rec_egl_crit_sw)
    print_debug(nload_var_egl_crit_sw,"The variable critial N load to surface water from extensive grassland for the surface water criterion is") 
 
    # calculate n load tot crit sw TEST
    nload_crit_sw_test = ascraster.duplicategrid(nload_var_ag_crit_sw)
    nload_crit_sw_test.add(nload_var_nat_crit_sw)
    nload_crit_sw_test.add(nload_var_egl_crit_sw)
    nload_crit_sw_test.add(nload_fixed_tot)
        
    ########### FORWARD CALCULATIONS TO CHECK ###########
    if icell_debug<0:
        pass
    else:
        fw = nload_crit_sw_test.get_data(icell_debug)
        bw = nload_crit_sw.get_data(icell_debug)
        print(fw)
        print(bw)
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
   