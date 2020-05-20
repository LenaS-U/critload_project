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

    #print("The critical N concentration in surface water is", params.crit_sw)
    
    # load needed variables for calculations
    nfix_ara            = ascraster.Asciigrid(ascii_file=params.filename_nfixation_cropland                      ,numtype=float,mask=params.mask)
    nfix_igl            = ascraster.Asciigrid(ascii_file=params.filename_nfixation_intgl                         ,numtype=float,mask=params.mask)
    nallo               = ascraster.Asciigrid(ascii_file=params.filename_n_point_alloch_matter                   ,numtype=float,mask=params.mask)
    nww                 = ascraster.Asciigrid(ascii_file=params.filename_n_point_wastewater                      ,numtype=float,mask=params.mask)
    naqua               = ascraster.Asciigrid(ascii_file=params.filename_n_point_aquaculture                     ,numtype=float,mask=params.mask)
    ndep_sw             = ascraster.Asciigrid(ascii_file=params.filename_n_point_dep_surfacewater                ,numtype=float,mask=params.mask)
    nfix_egl            = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "nfix_grass_ext.asc")     ,numtype=float,mask=params.mask)
    nfix_nat            = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "nfix_nat.asc")           ,numtype=float,mask=params.mask)
    nup_egl             = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "n_up_grass_ext.asc")     ,numtype=float,mask=params.mask)    
    q                   = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "q.asc")                  ,numtype=float,mask=params.mask)
    npoint_tot          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"npoint_tot.asc")         ,numtype=float,mask=params.mask)
    nero_tot            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nero_tot.asc")           ,numtype=float,mask=params.mask)
    nload_fixed_ag      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_ag.asc")     ,numtype=float,mask=params.mask)
    nload_fixed_nat     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_fixed_nat.asc")    ,numtype=float,mask=params.mask)
    nload_var_ag        = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_var_ag.asc")       ,numtype=float,mask=params.mask)
    nload_var_nat       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nload_var_nat.asc")      ,numtype=float,mask=params.mask)
    fle_ag              = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc")             ,numtype=float,mask=params.mask)
    fle_nat             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_nat.asc")            ,numtype=float,mask=params.mask)
    fsro_ag             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")            ,numtype=float,mask=params.mask)
    fsro_nat            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_nat.asc")           ,numtype=float,mask=params.mask)
    frnup_ara           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_ara.asc")          ,numtype=float,mask=params.mask)
    frnup_igl           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_igl.asc")          ,numtype=float,mask=params.mask)    
    fgw_rec_le_ag       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_ag.asc")      ,numtype=float,mask=params.mask)
    fgw_rec_le_nat      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fgw_rec_le_nat.asc")     ,numtype=float,mask=params.mask)    
    nox_em              = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")             ,numtype=float,mask=params.mask)
    nh3_tot_egl         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")        ,numtype=float,mask=params.mask)
    nh3_ef_man_ara      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_ara.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_man_igl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_igl.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_fer_ara      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fer_ara.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_fer_igl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fer_igl.asc")     ,numtype=float,mask=params.mask)    
    nh3_ef_man_fer_ara  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_fer_ara.asc") ,numtype=float,mask=params.mask)
    nh3_ef_man_fer_igl  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_fer_igl.asc") ,numtype=float,mask=params.mask)   
    frnfe_ara           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_ara.asc")          ,numtype=float,mask=params.mask)   
    frnfe_igl           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_igl.asc")          ,numtype=float,mask=params.mask)   
    frn_ara             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frn_ara.asc")            ,numtype=float,mask=params.mask)
    frn_igl             = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frn_igl.asc")            ,numtype=float,mask=params.mask)
    fara                = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fara.asc")               ,numtype=float,mask=params.mask)
    figl                = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"figl.asc")               ,numtype=float,mask=params.mask)
    fegl                = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fegl.asc")               ,numtype=float,mask=params.mask)
    fnat                = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fnat.asc")               ,numtype=float,mask=params.mask)
    nup_max_ara         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nup_max_ara.asc")        ,numtype=float,mask=params.mask)
    nup_max_igl         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nup_max_igl.asc")        ,numtype=float,mask=params.mask)
    nin_max_ara         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nin_max_ara.asc")        ,numtype=float,mask=params.mask)   
    nin_max_igl         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nin_max_igl.asc")        ,numtype=float,mask=params.mask)   
    nman_egl            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nman_egl.asc")           ,numtype=float,mask=params.mask)  

    
    ## One grid
    one_grid = ascraster.duplicategrid(nfix_ara)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
    
    # calculate Nload,crit,sw =Q*Nconc,sw(crit)
    nload_crit_sw = ascraster.duplicategrid(q)
    nload_crit_sw.multiply(params.crit_sw)
    fileout = os.path.join(params.outputdir,"nload_crit_sw.asc")
    nload_crit_sw.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_crit_sw,"nload_crit_sw =")
   
    # calculate fixed N load to surface water
    nload_fixed_tot = ascraster.duplicategrid(nallo)
    nload_fixed_tot.add(nero_tot)
    nload_fixed_tot.add(nload_fixed_nat)
    print_debug(nload_fixed_tot,"nload_fixed_tot =")
      
    nload_var_ag_nat = ascraster.duplicategrid(nload_var_ag) 
    nload_var_ag_nat.add(nload_var_nat)
    
    nload_var_other = ascraster.duplicategrid(nww)
    nload_var_other.add(naqua)
    nload_var_other.add(ndep_sw)
    nload_var_other.add(nload_fixed_ag) # is zero if combined with scenario 1 (all ag. N load = variable)
    
    nload_var_tot = ascraster.duplicategrid(nload_var_ag_nat) 
    nload_var_tot.add(nload_var_other)
      
    nload_var_ag_nat_percent = ascraster.duplicategrid(nload_var_ag_nat)
    nload_var_ag_nat_percent.divide(nload_var_tot, default_nodata_value = -9999)

    nload_var_other_percent = ascraster.duplicategrid(nload_var_other)
    nload_var_other_percent.divide(nload_var_tot, default_nodata_value = -9999)
    
    nload_var_crit_tot = ascraster.duplicategrid(nload_crit_sw)
    nload_var_crit_tot.substract(nload_fixed_tot)
    
    nload_var_crit_ag_nat = ascraster.duplicategrid(nload_var_crit_tot)
    nload_var_crit_ag_nat.multiply(nload_var_ag_nat_percent)
    
    nload_var_crit_other = ascraster.duplicategrid(nload_var_crit_tot)
    nload_var_crit_other.multiply(nload_var_other_percent)
    
    ## Parameter 'v' 
    # 'ara'
    v_ara_part1 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_ara_part1.multiply(fle_ag)
    v_ara_part2 = ascraster.duplicategrid(v_ara_part1)
    v_ara_part2.multiply(frnup_ara)
    v_ara_part3 = ascraster.duplicategrid(v_ara_part2)
    v_ara_part3.multiply(fsro_ag)
    v_ara_part4 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_ara_part4.multiply(fle_ag)
    v_ara_part4.multiply(fsro_ag)
    v_ara = ascraster.duplicategrid(v_ara_part1)
    v_ara.substract(v_ara_part2)
    v_ara.add(v_ara_part3)
    v_ara.substract(v_ara_part4)
    v_ara.add(fsro_ag)
    print_debug(v_ara,"v_ara =")
    # 'igl'
    v_igl_part1 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_igl_part1.multiply(fle_ag)
    v_igl_part2 = ascraster.duplicategrid(v_igl_part1)
    v_igl_part2.multiply(frnup_igl)
    v_igl_part3 = ascraster.duplicategrid(v_igl_part2)
    v_igl_part3.multiply(fsro_ag)
    v_igl_part4 = ascraster.duplicategrid(fgw_rec_le_ag)
    v_igl_part4.multiply(fle_ag)
    v_igl_part4.multiply(fsro_ag)
    v_igl = ascraster.duplicategrid(v_igl_part1)
    v_igl.substract(v_igl_part2)
    v_igl.add(v_igl_part3)
    v_igl.substract(v_igl_part4)
    v_igl.add(fsro_ag)
    print_debug(v_igl,"v_igl =")
    
    ## parameter 'w' 
    # 'egl'
    w_egl_part1 = ascraster.duplicategrid(fgw_rec_le_ag)
    w_egl_part1.multiply(fle_ag)
    w_egl_part2 = ascraster.duplicategrid(w_egl_part1)
    w_egl_part2.multiply(fsro_ag)
    w_egl = ascraster.duplicategrid(w_egl_part1)
    w_egl.substract(w_egl_part2)
    w_egl.add(fsro_ag)
    print_debug(w_egl,"w_egl =")
    # 'nat'
    w_nat_part1 = ascraster.duplicategrid(fgw_rec_le_nat)
    w_nat_part1.multiply(fle_nat)
    w_nat_part2 = ascraster.duplicategrid(w_nat_part1)
    w_nat_part2.multiply(fsro_nat)
    w_nat = ascraster.duplicategrid(w_nat_part1)
    w_nat.substract(w_nat_part2)
    w_nat.add(fsro_nat)
    print_debug(w_nat,"w_nat =")
    
    ## parameter 'y1'
    y1_part1 = ascraster.duplicategrid(nfix_ara)
    y1_part1.multiply(v_ara)
    y1_part2 = ascraster.duplicategrid(nfix_igl)
    y1_part2.multiply(v_igl)
    y1_part3 = ascraster.duplicategrid(nfix_egl)
    y1_part3.add(nman_egl)
    y1_part3.multiply(w_egl)
    y1_part4 = ascraster.duplicategrid(nfix_nat)
    y1_part4.multiply(w_nat)
    y1 = ascraster.duplicategrid(y1_part1)
    y1.add(y1_part2)
    y1.add(y1_part3)
    y1.add(y1_part4)
    print_debug(y1,"y1 =")    
     
    ## parameter 'y2'
    y2_part1 = ascraster.duplicategrid(fara)
    y2_part1.multiply(v_ara)
    y2_part2 = ascraster.duplicategrid(figl)
    y2_part2.multiply(v_igl)
    y2_part3 = ascraster.duplicategrid(fegl)
    y2_part3.multiply(w_egl)
    y2_part4 = ascraster.duplicategrid(fnat)
    y2_part4.multiply(w_nat)      
    y2 = ascraster.duplicategrid(y2_part1)
    y2.add(y2_part2)
    y2.add(y2_part3)
    y2.add(y2_part4)
    print_debug(y2,"y2 =")  

    # calculate parameter 'z'
    # 'ara' (LET OP: for z_ara, we use frn_igl!)        
    one_min_frn_igl = ascraster.duplicategrid(one_grid)
    one_min_frn_igl.substract(frn_igl)
    z_ara = ascraster.duplicategrid(frn_igl)
    z_ara.divide(one_min_frn_igl, default_nodata_value = -9999)        
    print_debug(z_ara,"z_ara =") 
    
    # 'igl' (LET OP: for z_igl, we use frn_ara!)        
    one_min_frn_ara = ascraster.duplicategrid(one_grid)
    one_min_frn_ara.substract(frn_ara)
    z_igl = ascraster.duplicategrid(frn_ara)
    z_igl.divide(one_min_frn_ara, default_nodata_value = -9999)      
    print_debug(z_igl,"z_igl =")
    
    # calculate parameter 'x' 
    # ara
    x_ara_part1 = ascraster.duplicategrid(y2)
    x_ara_part1.multiply(nh3_ef_man_fer_ara)
    x_ara = ascraster.duplicategrid(y2)
    x_ara.multiply(nh3_ef_man_fer_igl)
    x_ara.add(v_igl)
    x_ara.multiply(z_ara)
    x_ara.add(x_ara_part1)
    x_ara.add(v_ara)
    print_debug(x_ara,"x_ara =")
    
    # igl
    x_igl_part1 = ascraster.duplicategrid(y2)
    x_igl_part1.multiply(nh3_ef_man_fer_igl)
    x_igl = ascraster.duplicategrid(y2)
    x_igl.multiply(nh3_ef_man_fer_ara)
    x_igl.add(v_ara)
    x_igl.multiply(z_igl)
    x_igl.add(x_igl_part1)
    x_igl.add(v_igl)
    print_debug(x_igl,"x_igl =")
    
    ## calculate critical N input from manure
    
    ## OPTION2 - for grid cells with BOTH 'ara' AND 'igl'
    # 'ara'
    numerator_V2_ara = ascraster.duplicategrid(nload_var_crit_ag_nat)
    n1_V2_ara = ascraster.duplicategrid(nox_em)
    n1_V2_ara.add(nh3_tot_egl)
    n1_V2_ara.multiply(y2)
    numerator_V2_ara.substract(y1)
    numerator_V2_ara.substract(n1_V2_ara)
    
    one_min_frnfe_ara = ascraster.duplicategrid(one_grid)
    one_min_frnfe_ara.substract(frnfe_ara)
    frnfe_division_ara = ascraster.duplicategrid(frnfe_ara)
    frnfe_division_ara.divide(one_min_frnfe_ara, default_nodata_value =-9999)
    denominator_V2_ara = ascraster.duplicategrid(frnfe_division_ara)
    denominator_V2_ara.add(one_grid)
    denominator_V2_ara.multiply(x_ara)
    
    nman_crit_sw_V2_ara = ascraster.duplicategrid(numerator_V2_ara)
    nman_crit_sw_V2_ara.divide(denominator_V2_ara, default_nodata_value = -9999)

    fileout = os.path.join(params.outputdir, "nman_crit_sw_V2_ara.asc")
    nman_crit_sw_V2_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    # 'igl'
    numerator_V2_igl = ascraster.duplicategrid(numerator_V2_ara)
    
    one_min_frnfe_igl = ascraster.duplicategrid(one_grid)
    one_min_frnfe_igl.substract(frnfe_igl)
    frnfe_division_igl = ascraster.duplicategrid(frnfe_igl)
    frnfe_division_igl.divide(one_min_frnfe_igl, default_nodata_value =-9999)
    denominator_V2_igl = ascraster.duplicategrid(frnfe_division_igl)
    denominator_V2_igl.add(one_grid)
    denominator_V2_igl.multiply(x_igl)   
    
    nman_crit_sw_V2_igl = ascraster.duplicategrid(numerator_V2_igl)
    nman_crit_sw_V2_igl.divide(denominator_V2_igl, default_nodata_value = -9999) 

    fileout = os.path.join(params.outputdir, "nman_crit_sw_V2_igl.asc")
    nman_crit_sw_V2_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    ## OPTION 2 - for grid cells with EITHER 'ara' OR 'igl'
    # 'ara'
    numerator_V1_ara = ascraster.duplicategrid(numerator_V2_ara)
    n1_V1_ara = ascraster.duplicategrid(nup_egl)
    n1_V1_ara.multiply(fgw_rec_le_ag)
    n1_V1_ara.multiply(fle_ag)
    numerator_V1_ara.add(n1_V1_ara)
    
    d1_V1_ara = ascraster.duplicategrid(nh3_ef_man_ara)
    d1_V1_ara.multiply(y2)
    d1_V1_ara.add(v_ara)
    d2_V1_ara = ascraster.duplicategrid(nh3_ef_fer_ara)
    d2_V1_ara.multiply(y2)
    d2_V1_ara.add(v_ara)   
    d2_V1_ara.multiply(frnfe_division_ara)
    denominator_V1_ara = ascraster.duplicategrid(d1_V1_ara)
    denominator_V1_ara.add(d2_V1_ara)
    
    nman_crit_sw_V1_ara = ascraster.duplicategrid(numerator_V1_ara)
    nman_crit_sw_V1_ara.divide(denominator_V1_ara, default_nodata_value = -9999)

    fileout = os.path.join(params.outputdir, "nman_crit_sw_V1_ara.asc")
    nman_crit_sw_V1_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    # 'igl'
    numerator_V1_igl = ascraster.duplicategrid(numerator_V1_ara)
    
    d1_V1_igl = ascraster.duplicategrid(nh3_ef_man_igl)
    d1_V1_igl.multiply(y2)
    d1_V1_igl.add(v_igl)
    d2_V1_igl = ascraster.duplicategrid(nh3_ef_fer_igl)
    d2_V1_igl.multiply(y2)
    d2_V1_igl.add(v_ara)   
    d2_V1_igl.multiply(frnfe_division_igl)
    denominator_V1_igl = ascraster.duplicategrid(d1_V1_igl)
    denominator_V1_igl.add(d2_V1_igl)
    
    nman_crit_sw_V1_igl = ascraster.duplicategrid(numerator_V1_igl)
    nman_crit_sw_V1_igl.divide(denominator_V1_igl, default_nodata_value = -9999)

    fileout = os.path.join(params.outputdir, "nman_crit_sw_V1_igl.asc")
    nman_crit_sw_V1_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    # MAKE GRID WITH CRITICAL INPUTS FROM MANURE DEPENDING ON OPTION
    # ara
    nman_crit_sw_ara = ascraster.duplicategrid(nman_crit_sw_V1_ara)          
    for icell in range(fara.length):       
        f_ara = fara.get_data(icell) 
        f_igl = figl.get_data(icell)
        nman_ara2 = nman_crit_sw_V2_ara.get_data(icell)
        if (f_ara is None or f_igl is None):
            continue
        elif (f_ara > 0 and f_igl > 0):
            nman_ara = nman_ara2
        elif (f_ara == 0 and f_igl > 0):
            nman_ara = 0
        else:
            continue
            
        nman_crit_sw_ara.set_data(icell,nman_ara)

    for icell in range (nman_crit_sw_ara.length):
        nman_ara3 = nman_crit_sw_ara.get_data(icell)
        if (nman_ara3 is None):
            continue
        if (nman_ara3 < 0):
            nman_ara = 0
        else:
            continue
        nman_crit_sw_ara.set_data(icell,nman_ara)
    
    fileout = os.path.join(params.outputdir, "nman_crit_sw_ara.asc")
    nman_crit_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_sw_ara,"nman_crit_sw_ara =")
    
    # igl
    nman_crit_sw_igl = ascraster.duplicategrid(nman_crit_sw_V1_igl)          
    for icell in range(figl.length):       
        f_igl = figl.get_data(icell) 
        f_ara = fara.get_data(icell)
        nman_igl2 = nman_crit_sw_V2_igl.get_data(icell)
        if (f_ara is None or f_igl is None):
            continue
        elif (f_ara > 0 and f_igl > 0):
            nman_igl = nman_igl2
        elif (f_ara > 0 and f_igl == 0):
            nman_igl = 0
        else:
            continue
            
        nman_crit_sw_igl.set_data(icell,nman_igl)
    
    for icell in range (nman_crit_sw_igl.length):
        nman_igl3 = nman_crit_sw_igl.get_data(icell)
        if (nman_igl3 is None):
            continue
        if (nman_igl3 < 0):
            nman_igl = 0
        else:
            continue
        nman_crit_sw_igl.set_data(icell,nman_igl)
    
    fileout = os.path.join(params.outputdir, "nman_crit_sw_igl.asc")
    nman_crit_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_sw_igl,"nman_crit_sw_igl =") 
    
    ## * Critical N input from fertilizer * 
    # 'ara'
    nfer_crit_sw_ara = ascraster.duplicategrid(nman_crit_sw_ara)
    nfer_crit_sw_ara.multiply(frnfe_division_ara)

    # set to zero for all cells with no ara but igl (to avoid error in calculating nh3 emissions / deposition for these cells)
    for icell in range(nfer_crit_sw_ara.length):
        f_ara = fara.get_data(icell)
        f_igl = figl.get_data(icell)
        nfer_ara = nfer_crit_sw_ara.get_data(icell)
        if (f_ara == 0 and f_igl >0) : 
            nfer_ara = 0
        else:
            continue
            
        nfer_crit_sw_ara.set_data(icell,nfer_ara) 
    fileout = os.path.join(params.outputdir,"nfer_crit_sw_ara.asc")
    nfer_crit_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_crit_sw_ara,"nfer_crit_sw_ara =")

    # 'igl'
    nfer_crit_sw_igl = ascraster.duplicategrid(nman_crit_sw_igl)
    nfer_crit_sw_igl.multiply(frnfe_division_igl)

    # set to zero for all cells with no igl but ara (to avoid error in calculating nh3 emissions / deposition for these cells)
    for icell in range(nfer_crit_sw_igl.length):
        f_ara = fara.get_data(icell)
        f_igl = figl.get_data(icell)
        nfer_igl = nfer_crit_sw_igl.get_data(icell)
        if (f_igl == 0 and f_ara >0) : 
            nfer_igl = 0
        else:
            continue
            
        nfer_crit_sw_igl.set_data(icell,nfer_igl) 
    fileout = os.path.join(params.outputdir,"nfer_crit_sw_igl.asc")
    nfer_crit_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_crit_sw_igl,"nfer_crit_sw_igl =")      

    ## * Critical N inputs from fertilizer plus manure * ##
    # 'ara'
    nman_fer_crit_sw_ara = ascraster.duplicategrid(nman_crit_sw_ara)
    nman_fer_crit_sw_ara.add(nfer_crit_sw_ara)
    fileout = os.path.join(params.outputdir,"nman_fer_crit_sw_ara.asc")
    nman_fer_crit_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)    
    # 'igl'
    nman_fer_crit_sw_igl = ascraster.duplicategrid(nman_crit_sw_igl)
    nman_fer_crit_sw_igl.add(nfer_crit_sw_igl)
    fileout = os.path.join(params.outputdir,"nman_fer_crit_sw_igl.asc")
    nman_fer_crit_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)  

    ## * NH3 emissions at critical N input *
    # 'ara'
    nh3em_man_crit_sw_ara = ascraster.duplicategrid(nman_crit_sw_ara)
    nh3em_man_crit_sw_ara.multiply(nh3_ef_man_ara)  
    nh3em_fer_crit_sw_ara = ascraster.duplicategrid(nfer_crit_sw_ara)
    nh3em_fer_crit_sw_ara.multiply(nh3_ef_fer_ara) 
    nh3em_crit_sw_ara = ascraster.duplicategrid(nh3em_man_crit_sw_ara)
    nh3em_crit_sw_ara.add(nh3em_fer_crit_sw_ara)
    print_debug(nh3em_crit_sw_ara, "nh3em_crit_sw_ara =")
    # 'igl'
    nh3em_man_crit_sw_igl = ascraster.duplicategrid(nman_crit_sw_igl)
    nh3em_man_crit_sw_igl.multiply(nh3_ef_man_igl)  
    nh3em_fer_crit_sw_igl = ascraster.duplicategrid(nfer_crit_sw_igl)
    nh3em_fer_crit_sw_igl.multiply(nh3_ef_fer_igl) 
    nh3em_crit_sw_igl = ascraster.duplicategrid(nh3em_man_crit_sw_igl)
    nh3em_crit_sw_igl.add(nh3em_fer_crit_sw_igl)
    print_debug(nh3em_crit_sw_igl, "nh3em_crit_sw_igl =")
    
    ## * N deposition at critical N input *
    ndep_crit_sw_tot = ascraster.duplicategrid(nh3em_crit_sw_ara)
    ndep_crit_sw_tot.add(nh3em_crit_sw_igl)
    ndep_crit_sw_tot.add(nox_em)
    ndep_crit_sw_tot.add(nh3_tot_egl)
    
    fileout = os.path.join(params.outputdir,"ndep_crit_sw_tot.asc")
    ndep_crit_sw_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_sw_tot,"ndep_crit_sw_tot =")        
    
    # 'ara'
    ndep_crit_sw_ara = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_ara.multiply(fara)
    print_debug(ndep_crit_sw_ara,"ndep_crit_sw_ara =")   
    # 'igl'
    ndep_crit_sw_igl = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_igl.multiply(figl)   
    print_debug(ndep_crit_sw_igl,"ndep_crit_sw_igl =")   
    # 'nat'
    ndep_crit_sw_nat = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_nat.multiply(fnat)
    print_debug(ndep_crit_sw_nat,"ndep_crit_sw_nat =")   
    # 'egl'
    ndep_crit_sw_egl = ascraster.duplicategrid(ndep_crit_sw_tot)
    ndep_crit_sw_egl.multiply(fegl)
    print_debug(ndep_crit_sw_egl,"ndep_crit_sw_egl =")
    
    ## * Total critical N inputs *
    # 'ara'
    nin_crit_sw_ara = ascraster.duplicategrid(nman_crit_sw_ara)
    nin_crit_sw_ara.add(nfer_crit_sw_ara)
    nin_crit_sw_ara.add(ndep_crit_sw_ara)
    nin_crit_sw_ara.add(nfix_ara)
    fileout = os.path.join(params.outputdir,"nin_crit_sw_ara.asc")
    nin_crit_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_sw_ara,"nin_crit_sw_ara =")
    # 'igl'
    nin_crit_sw_igl = ascraster.duplicategrid(nman_crit_sw_igl)
    nin_crit_sw_igl.add(nfer_crit_sw_igl)
    nin_crit_sw_igl.add(ndep_crit_sw_igl)
    nin_crit_sw_igl.add(nfix_igl)
    fileout = os.path.join(params.outputdir,"nin_crit_sw_igl.asc")
    nin_crit_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_sw_igl,"nin_crit_sw_igl =")
    # 'ara+igl'
    nin_crit_sw_araigl = ascraster.duplicategrid(nin_crit_sw_ara)
    nin_crit_sw_araigl.add(nin_crit_sw_igl)
    fileout = os.path.join(params.outputdir,"nin_crit_sw_araigl.asc")
    nin_crit_sw_araigl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    # 'nat'
    nin_crit_sw_nat = ascraster.duplicategrid(ndep_crit_sw_nat)
    nin_crit_sw_nat.add(nfix_nat)
    print_debug(nin_crit_sw_nat,"nin_crit_sw_nat =")
    # 'egl'
    nin_crit_sw_egl = ascraster.duplicategrid(ndep_crit_sw_egl)
    nin_crit_sw_egl.add(nfix_egl)
    nin_crit_sw_egl.add(nman_egl)
    print_debug(nin_crit_sw_egl,"nin_crit_sw_egl =")   
    
    ## * N surface runoff at critical N inputs *
    # 'ara'
    nsro_crit_sw_ara = ascraster.duplicategrid(nin_crit_sw_ara)
    nsro_crit_sw_ara.multiply(fsro_ag)
    print_debug(nsro_crit_sw_ara,"nsro_crit_sw_ara =")
    # 'igl'
    nsro_crit_sw_igl = ascraster.duplicategrid(nin_crit_sw_igl)
    nsro_crit_sw_igl.multiply(fsro_ag)
    print_debug(nsro_crit_sw_igl,"nsro_crit_sw_igl =")
    # 'nat'
    nsro_crit_sw_nat = ascraster.duplicategrid(nin_crit_sw_nat)
    nsro_crit_sw_nat.multiply(fsro_nat)
    print_debug(nsro_crit_sw_nat,"nsro_crit_sw_nat =")
    # 'egl'
    nsro_crit_sw_egl = ascraster.duplicategrid(nin_crit_sw_egl)
    nsro_crit_sw_egl.multiply(fsro_ag)
    print_debug(nsro_crit_sw_egl,"nsro_crit_sw_egl =")
    
    ## * N uptake at critical N inputs *
    # 'ara'
    nup_crit_sw_ara = ascraster.duplicategrid(nin_crit_sw_ara)
    nup_crit_sw_ara.substract(nsro_crit_sw_ara)
    nup_crit_sw_ara.multiply(frnup_ara)
    fileout = os.path.join(params.outputdir,"nup_crit_sw_ara.asc")
    nup_crit_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_sw_ara,"nup_crit_sw_ara =")
    # 'igl'
    nup_crit_sw_igl = ascraster.duplicategrid(nin_crit_sw_igl)
    nup_crit_sw_igl.substract(nsro_crit_sw_igl)
    nup_crit_sw_igl.multiply(frnup_igl)
    fileout = os.path.join(params.outputdir,"nup_crit_sw_igl.asc")
    nup_crit_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_sw_igl,"nup_crit_sw_igl =") 

    ## * NUE at critical N inputs *
    # 'ara'
    nue_crit_sw_ara = ascraster.duplicategrid(nup_crit_sw_ara)
    nue_crit_sw_ara.divide(nin_crit_sw_ara, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_sw_ara.asc")
    nue_crit_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_sw_ara,"nue_crit_sw_ara =")
    # 'igl'
    nue_crit_sw_igl = ascraster.duplicategrid(nup_crit_sw_igl)
    nue_crit_sw_igl.divide(nin_crit_sw_igl, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_sw_igl.asc")
    nue_crit_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_sw_igl,"nue_crit_sw_igl =")
    
    ## * Maximum uptake fraction  *
    # 'ara'
    fnup_max_sw_ara = ascraster.duplicategrid(nup_max_ara)
    fnup_max_sw_ara.divide(nup_crit_sw_ara)
    fileout = os.path.join(params.outputdir,"fnup_max_sw_ara.asc")
    fnup_max_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_sw_ara,"fnup_max_sw_ara =")
    # 'igl'
    fnup_max_sw_igl = ascraster.duplicategrid(nup_max_igl)
    fnup_max_sw_igl.divide(nup_crit_sw_igl)
    fileout = os.path.join(params.outputdir,"fnup_max_sw_igl.asc")
    fnup_max_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_sw_igl,"fnup_max_sw_igl =")
    
    ## * Correction factor for grid cells where Nup,crit > Nup,max *
    # 'ara'
    fnup_corr_sw_ara = ascraster.duplicategrid(nin_max_ara)
    fnup_corr_sw_ara.substract(nfix_ara)
    temp2_ara = ascraster.duplicategrid(nh3_tot_egl)
    temp2_ara.add(nox_em)
    temp2_ara.multiply(fara)
    fnup_corr_sw_ara.substract(temp2_ara) 
    temp3_ara = ascraster.duplicategrid(nh3em_crit_sw_ara)
    temp3_ara.multiply(fara)
    temp3_ara.add(nman_crit_sw_ara)
    temp3_ara.add(nfer_crit_sw_ara)
    fnup_corr_sw_ara.divide(temp3_ara, default_nodata_value = -9999) 
    fileout = os.path.join(params.outputdir,"fnup_corr_sw_ara.asc")
    fnup_corr_sw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_sw_ara,"fnup_corr_sw_ara =")
    # 'igl'
    fnup_corr_sw_igl = ascraster.duplicategrid(nin_max_igl)
    fnup_corr_sw_igl.substract(nfix_igl)
    temp2_igl = ascraster.duplicategrid(nh3_tot_egl)
    temp2_igl.add(nox_em)
    temp2_igl.multiply(figl)
    fnup_corr_sw_igl.substract(temp2_igl)  
    temp3_igl = ascraster.duplicategrid(nh3em_crit_sw_igl)
    temp3_igl.multiply(figl)
    temp3_igl.add(nman_crit_sw_igl)
    temp3_igl.add(nfer_crit_sw_igl)
    fnup_corr_sw_igl.divide(temp3_igl, default_nodata_value = -9999)   
    fileout = os.path.join(params.outputdir,"fnup_corr_sw_igl.asc")
    fnup_corr_sw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_sw_igl,"fnup_corr_sw_igl =")        
    
   
    ########### FORWARD CALCULATIONS TO CHECK ###########
    ## * Critical N budget *
    # 'ara'
    nbud_crit_sw_ara = ascraster.duplicategrid(nin_crit_sw_ara)
    nbud_crit_sw_ara.substract(nup_crit_sw_ara)
    print_debug(nbud_crit_sw_ara,"nbud_crit_sw_ara =")
    # 'igl'
    nbud_crit_sw_igl = ascraster.duplicategrid(nin_crit_sw_igl)
    nbud_crit_sw_igl.substract(nup_crit_sw_igl)
    print_debug(nbud_crit_sw_igl,"nbud_crit_sw_igl =")
    # 'nat'
    nbud_crit_sw_nat = ascraster.duplicategrid(nin_crit_sw_nat)
    print_debug(nbud_crit_sw_nat,"nbud_crit_sw_nat =")    
    # 'egl'
    nbud_crit_sw_egl = ascraster.duplicategrid(nin_crit_sw_egl)
    nbud_crit_sw_egl.substract(nup_egl)
    print_debug(nbud_crit_sw_egl,"nbud_crit_sw_egl =")   
    
    ## * Critical leaching *
    # 'ara'
    nle_crit_sw_ara = ascraster.duplicategrid(nbud_crit_sw_ara)
    nle_crit_sw_ara.substract(nsro_crit_sw_ara)
    nle_crit_sw_ara.multiply(fle_ag)
    print_debug(nle_crit_sw_ara,"nle_crit_sw_ara =")
    # 'igl'
    nle_crit_sw_igl = ascraster.duplicategrid(nbud_crit_sw_igl)
    nle_crit_sw_igl.substract(nsro_crit_sw_igl)
    nle_crit_sw_igl.multiply(fle_ag)
    print_debug(nle_crit_sw_igl,"nle_crit_sw_igl =")
    # 'nat'
    nle_crit_sw_nat = ascraster.duplicategrid(nbud_crit_sw_nat)
    nle_crit_sw_nat.substract(nsro_crit_sw_nat)
    nle_crit_sw_nat.multiply(fle_nat)
    print_debug(nle_crit_sw_nat,"nle_crit_sw_nat =")
    # 'egl'
    nle_crit_sw_egl = ascraster.duplicategrid(nbud_crit_sw_egl)
    nle_crit_sw_egl.substract(nsro_crit_sw_egl)
    nle_crit_sw_egl.multiply(fle_ag)
    print_debug(nle_crit_sw_egl,"nle_crit_sw_egl =")   
    
    ## * groundwater N load from recent inputs *
    # 'ara'
    ngw_rec_crit_sw_ara = ascraster.duplicategrid(nle_crit_sw_ara)
    ngw_rec_crit_sw_ara.multiply(fgw_rec_le_ag)   
    print_debug(ngw_rec_crit_sw_ara, "ngw_rec_crit_sw_ara =")
    # 'igl'
    ngw_rec_crit_sw_igl = ascraster.duplicategrid(nle_crit_sw_igl)
    ngw_rec_crit_sw_igl.multiply(fgw_rec_le_ag)   
    print_debug(ngw_rec_crit_sw_igl, "ngw_rec_crit_sw_igl =")
    # 'nat'
    ngw_rec_crit_sw_nat = ascraster.duplicategrid(nle_crit_sw_nat)
    ngw_rec_crit_sw_nat.multiply(fgw_rec_le_nat)
    print_debug(ngw_rec_crit_sw_nat,"ngw_rec_crit_sw_nat =")
    # 'egl'
    ngw_rec_crit_sw_egl = ascraster.duplicategrid(nle_crit_sw_egl)
    ngw_rec_crit_sw_egl.multiply(fgw_rec_le_ag)
    print_debug(ngw_rec_crit_sw_egl,"ngw_rec_crit_sw_egl =")
    
    ## * Variable critical N load to surface water *
    
    # 'ara'
    nload_var_crit_sw_ara = ascraster.duplicategrid(nsro_crit_sw_ara)
    nload_var_crit_sw_ara.add(ngw_rec_crit_sw_ara)
    print_debug(nload_var_crit_sw_ara,"nload_var_crit_sw_ara =")
    # 'igl'
    nload_var_crit_sw_igl = ascraster.duplicategrid(nsro_crit_sw_igl)
    nload_var_crit_sw_igl.add(ngw_rec_crit_sw_igl)
    print_debug(nload_var_crit_sw_igl,"nload_var_crit_sw_igl =") 
    # 'nat'
    nload_var_crit_sw_nat = ascraster.duplicategrid(nsro_crit_sw_nat)
    nload_var_crit_sw_nat.add(ngw_rec_crit_sw_nat)
    print_debug(nload_var_crit_sw_nat,"nload_var_crit_sw_nat =") 
    # 'egl'
    nload_var_crit_sw_egl = ascraster.duplicategrid(nsro_crit_sw_egl)
    nload_var_crit_sw_egl.add(ngw_rec_crit_sw_egl)
    print_debug(nload_var_crit_sw_egl,"nload_var_crit_sw_egl =")     
    
    ## * calculate n load tot crit sw TEST *
    nload_crit_sw_test = ascraster.duplicategrid(nload_var_crit_sw_ara)
    nload_crit_sw_test.add(nload_var_crit_sw_igl)   
    nload_crit_sw_test.add(nload_var_crit_sw_nat)
    nload_crit_sw_test.add(nload_var_crit_sw_egl)
    nload_crit_sw_test.add(nload_var_crit_other)
    nload_crit_sw_test.add(nload_fixed_tot)
    fileout = os.path.join(params.outputdir,"nload_crit_sw_test.asc")
    nload_crit_sw_test.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
        
    ########### FORWARD CALCULATIONS TO CHECK ###########
    if icell_debug<0:
        pass
    else:
        fw = nload_crit_sw_test.get_data(icell_debug)
        bw = nload_crit_sw.get_data(icell_debug)
        #print(fw)
        #print(bw)
        if fw is None:
            print("FW/BW_TEST:_Forward_calculation_not_possible:_Nin,crit = None")
        
        else:
            fw = round(fw,2) 
            bw = round(bw,2)
            if fw == bw:
                print("FW/BW_TEST = SUCCESFUL")
            else:
                print("FW/BW_TEST = NOT_SUCCESFUL")
    ############################################################################################

    #print(fw)
    #print(bw)    