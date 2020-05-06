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
    
    print("nconc_le_crit_gw =", params.crit_gw)    
    
    # load needed variables for calculations
    q               = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "q.asc")               ,numtype=float,mask=params.mask)
    nle_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir, "nle_ag.asc")          ,numtype=float,mask=params.mask)
    nfix_ara        = ascraster.Asciigrid(ascii_file=params.filename_nfixation_cropland                   ,numtype=float,mask=params.mask)
    nfix_igl        = ascraster.Asciigrid(ascii_file=params.filename_nfixation_intgl                      ,numtype=float,mask=params.mask)
    fsro_ag         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")         ,numtype=float,mask=params.mask)
    fara            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fara.asc")            ,numtype=float,mask=params.mask)
    figl            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"figl.asc")            ,numtype=float,mask=params.mask)
    fegl            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fegl.asc")            ,numtype=float,mask=params.mask)
    fnat            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fnat.asc")            ,numtype=float,mask=params.mask)
    fle_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fle_ag.asc")          ,numtype=float,mask=params.mask)
    frnup_ara       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_ara.asc")       ,numtype=float,mask=params.mask)
    frnup_igl       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_igl.asc")       ,numtype=float,mask=params.mask)    
    nup_max_ara     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nup_max_ara.asc")     ,numtype=float,mask=params.mask)
    nup_max_igl     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nup_max_igl.asc")     ,numtype=float,mask=params.mask)
    nox_em          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")          ,numtype=float,mask=params.mask)
    nh3_tot_egl     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")     ,numtype=float,mask=params.mask)
    nh3_tot_igl     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_igl.asc")     ,numtype=float,mask=params.mask)
    nh3_tot_ara     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_ara.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_man_ara  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_ara.asc")  ,numtype=float,mask=params.mask)
    nh3_ef_man_igl  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_igl.asc")  ,numtype=float,mask=params.mask)
    nh3_ef_fer_ara  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fer_ara.asc")  ,numtype=float,mask=params.mask)
    nh3_ef_fer_igl  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fer_igl.asc")  ,numtype=float,mask=params.mask)
    frnfe_ara       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_ara.asc")       ,numtype=float,mask=params.mask)   
    frnfe_igl       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_igl.asc")       ,numtype=float,mask=params.mask)   
    nin_max_ara     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nin_max_ara.asc")     ,numtype=float,mask=params.mask)   
    nin_max_igl     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nin_max_igl.asc")     ,numtype=float,mask=params.mask)   
    nle_ara         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nle_ara.asc")         ,numtype=float,mask=params.mask)   
    nle_igl         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nle_igl.asc")         ,numtype=float,mask=params.mask)   
      
    ## * Critical N leaching *
    one_grid = ascraster.duplicategrid(q)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
    one_min_fsro = ascraster.duplicategrid(one_grid)
    one_min_fsro.substract(fsro_ag)
    # 'ara'
    nle_crit_gw_ara = ascraster.duplicategrid(one_min_fsro)
    nle_crit_gw_ara.multiply(q)
    nle_crit_gw_ara.multiply(fara)
    nle_crit_gw_ara.multiply(params.crit_gw)
    fileout = os.path.join(params.outputdir, "nle_crit_gw_ara.asc")
    nle_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_crit_gw_ara,"nle_crit_gw_ara =")
    
    # 'igl'
    nle_crit_gw_igl = ascraster.duplicategrid(one_min_fsro)
    nle_crit_gw_igl.multiply(q)
    nle_crit_gw_igl.multiply(figl)
    nle_crit_gw_igl.multiply(params.crit_gw)
    fileout = os.path.join(params.outputdir, "nle_crit_gw_igl.asc")
    nle_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_crit_gw_igl,"nle_crit_gw_igl =")
    
    ## * Parameter v *
    # 'ara'
    v_ara_part1 = ascraster.duplicategrid(one_grid)
    v_ara_part1.substract(frnup_ara)
    v_ara_part2 = ascraster.duplicategrid(fsro_ag)
    v_ara_part2.multiply(frnup_ara)
    v_ara = ascraster.duplicategrid(v_ara_part1)
    v_ara.add(v_ara_part2)
    v_ara.substract(fsro_ag)
    v_ara.multiply(fle_ag)
    # 'igl'
    v_igl_part1 = ascraster.duplicategrid(one_grid)
    v_igl_part1.substract(frnup_igl)
    v_igl_part2 = ascraster.duplicategrid(fsro_ag)
    v_igl_part2.multiply(frnup_igl)
    v_igl = ascraster.duplicategrid(v_igl_part1)
    v_igl.add(v_igl_part2)
    v_igl.substract(fsro_ag)
    v_igl.multiply(fle_ag)

    ## * Critical N input from manure *
    ## OPTION 1 - for grid cells with EITHER 'ara' OR 'igl'
    # 'ara'    
    num1_ara = ascraster.duplicategrid(nle_crit_gw_ara)
    num1_ara.divide(v_ara, default_nodata_value = -9999)
    num1_ara.substract(nfix_ara)   
    num2_V1_ara = ascraster.duplicategrid(nox_em)
    num2_V1_ara.add(nh3_tot_egl)
    num2_V1_ara.multiply(fara) 
    num_V1_ara = ascraster.duplicategrid(num1_ara)
    num_V1_ara.substract(num2_V1_ara)
    den1_ara = ascraster.duplicategrid(fara)
    den1_ara.multiply(nh3_ef_man_ara)
    den1_ara.add(one_grid)
    den2_ara = ascraster.duplicategrid(fara)
    den2_ara.multiply(nh3_ef_fer_ara)    
    den2_ara.add(one_grid)
    one_min_frnfe_ara = ascraster.duplicategrid(one_grid)
    one_min_frnfe_ara.substract(frnfe_ara)
    frnfe_division_ara = ascraster.duplicategrid(frnfe_ara)
    frnfe_division_ara.divide(one_min_frnfe_ara, default_nodata_value = -9999)
    den2_ara.multiply(frnfe_division_ara)
    den_ara = ascraster.duplicategrid(den1_ara)
    den_ara.add(den2_ara)
    
    nman_crit_gw_V1_ara = ascraster.duplicategrid(num_V1_ara)
    nman_crit_gw_V1_ara.divide(den_ara, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir, "nman_crit_gw_V1_ara.asc")
    nman_crit_gw_V1_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    # 'igl'    
    num1_igl = ascraster.duplicategrid(nle_crit_gw_igl)
    num1_igl.divide(v_igl, default_nodata_value = -9999)
    num1_igl.substract(nfix_igl)   
    num2_V1_igl = ascraster.duplicategrid(nox_em)
    num2_V1_igl.add(nh3_tot_egl)
    num2_V1_igl.multiply(figl) 
    num_V1_igl = ascraster.duplicategrid(num1_igl)
    num_V1_igl.substract(num2_V1_igl)
    den1_igl = ascraster.duplicategrid(figl)
    den1_igl.multiply(nh3_ef_man_igl)
    den1_igl.add(one_grid)
    den2_igl = ascraster.duplicategrid(figl)
    den2_igl.multiply(nh3_ef_fer_igl)    
    den2_igl.add(one_grid)
    one_min_frnfe_igl = ascraster.duplicategrid(one_grid)
    one_min_frnfe_igl.substract(frnfe_igl)
    frnfe_division_igl = ascraster.duplicategrid(frnfe_igl)
    frnfe_division_igl.divide(one_min_frnfe_igl, default_nodata_value = -9999)
    den2_igl.multiply(frnfe_division_igl)
    den_igl = ascraster.duplicategrid(den1_igl)
    den_igl.add(den2_igl)
    
    nman_crit_gw_V1_igl = ascraster.duplicategrid(num_V1_igl)
    nman_crit_gw_V1_igl.divide(den_igl, default_nodata_value = -9999)    

    fileout = os.path.join(params.outputdir, "nman_crit_gw_V1_igl.asc")
    nman_crit_gw_V1_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    ## OPTION2 - for grid cells with BOTH 'ara' AND 'igl'
    # 'ara'    
    num2_V2_ara = ascraster.duplicategrid(nle_crit_gw_igl)
    num2_V2_ara.divide(nle_igl, default_nodata_value = -9999)
    num2_V2_ara.multiply(nh3_tot_igl)
    num2_V2_ara.add(nox_em)
    num2_V2_ara.add(nh3_tot_egl)
    num2_V2_ara.multiply(fara) 
    num_V2_ara = ascraster.duplicategrid(num1_ara)
    num_V2_ara.substract(num2_V2_ara)    
    
    nman_crit_gw_V2_ara = ascraster.duplicategrid(num_V2_ara)
    nman_crit_gw_V2_ara.divide(den_ara, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir, "nman_crit_gw_V2_ara.asc")
    nman_crit_gw_V2_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    # 'igl'     
    num2_V2_igl = ascraster.duplicategrid(nle_crit_gw_ara)
    num2_V2_igl.divide(nle_ara, default_nodata_value = -9999)
    num2_V2_igl.multiply(nh3_tot_ara)
    num2_V2_igl.add(nox_em)
    num2_V2_igl.add(nh3_tot_egl)
    num2_V2_igl.multiply(figl) 
    num_V2_igl = ascraster.duplicategrid(num1_igl)
    num_V2_igl.substract(num2_V2_igl)    
    
    nman_crit_gw_V2_igl = ascraster.duplicategrid(num_V2_igl)
    nman_crit_gw_V2_igl.divide(den_igl, default_nodata_value = -9999)

    fileout = os.path.join(params.outputdir, "nman_crit_gw_V2_igl.asc")
    nman_crit_gw_V2_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    # MAKE GRID WITH CRITICAL INPUTS FROM MANURE DEPENDING ON OPTION
    # ara
    nman_crit_gw_ara = ascraster.duplicategrid(nman_crit_gw_V1_ara)          
    for icell in range(fara.length):       
        f_ara = fara.get_data(icell) 
        f_igl = figl.get_data(icell)
        nman_ara2 = nman_crit_gw_V2_ara.get_data(icell)
        nle = nle_ag.get_data(icell)
        if (f_ara is None or f_igl is None):
            continue
        elif (f_ara > 0 and f_igl > 0 and nle > 0) :
            nman_ara = nman_ara2
        elif (f_ara ==0 and f_igl > 0):
            nman_ara = 0
        else:
            continue
            
        nman_crit_gw_ara.set_data(icell,nman_ara)

    for icell in range (nman_crit_gw_ara.length):
        nman_ara3 = nman_crit_gw_ara.get_data(icell)
        if (nman_ara3 is None):
            continue
        if (nman_ara3 < 0):
            nman_ara = 0
        else:
            continue
        nman_crit_gw_ara.set_data(icell,nman_ara)
    
    fileout = os.path.join(params.outputdir, "nman_crit_gw_ara.asc")
    nman_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_gw_ara,"nman_crit_gw_ara =")
     
    # igl
    nman_crit_gw_igl = ascraster.duplicategrid(nman_crit_gw_V1_igl)          
    for icell in range(figl.length):       
        f_igl = figl.get_data(icell) 
        f_ara = fara.get_data(icell)
        nman_igl2 = nman_crit_gw_V2_igl.get_data(icell)
        nle = nle_ag.get_data(icell)
        if (f_ara is None or f_igl is None):
            continue
        elif (f_ara > 0 and f_igl > 0 and nle > 0) :
            nman_igl = nman_igl2
        elif (f_ara > 0 and f_igl ==0):
            nman_igl = 0
        else:
            continue
            
        nman_crit_gw_igl.set_data(icell,nman_igl)
    
    for icell in range (nman_crit_gw_igl.length):
        nman_igl3 = nman_crit_gw_igl.get_data(icell)
        if (nman_igl3 is None):
            continue
        if (nman_igl3 < 0):
            nman_igl = 0
        else:
            continue
        nman_crit_gw_igl.set_data(icell,nman_igl)
    
    fileout = os.path.join(params.outputdir, "nman_crit_gw_igl.asc")
    nman_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_gw_igl,"nman_crit_gw_igl =")   
    
    ## * Critical N input from fertilizer * 
    # 'ara'
    nfer_crit_gw_ara = ascraster.duplicategrid(nman_crit_gw_ara)
    nfer_crit_gw_ara.multiply(frnfe_division_ara)

    # set to zero for all cells with no ara but igl (to avoid error in calculating nh3 emissions / deposition for these cells)
    for icell in range(nfer_crit_gw_ara.length):
        f_ara = fara.get_data(icell)
        f_igl = figl.get_data(icell)
        if (f_ara == 0 and f_igl >0) : 
            nfer_ara = 0
        else:
            continue
            
        nfer_crit_gw_ara.set_data(icell,nfer_ara) 
    fileout = os.path.join(params.outputdir,"nfer_crit_gw_ara.asc")
    nfer_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_crit_gw_ara,"nfer_crit_gw_ara =")

    # 'igl'
    nfer_crit_gw_igl = ascraster.duplicategrid(nman_crit_gw_igl)
    nfer_crit_gw_igl.multiply(frnfe_division_igl)

    # set to zero for all cells with no igl but ara (to avoid error in calculating nh3 emissions / deposition for these cells)
    for icell in range(nfer_crit_gw_igl.length):
        f_ara = fara.get_data(icell)
        f_igl = figl.get_data(icell)
        if (f_igl == 0 and f_ara >0) : 
            nfer_igl = 0
        else:
            continue
            
        nfer_crit_gw_igl.set_data(icell,nfer_igl) 
    fileout = os.path.join(params.outputdir,"nfer_crit_gw_igl.asc")
    nfer_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_crit_gw_igl,"nfer_crit_gw_igl =")    

    ## * Critical N inputs from fertilizer plus manure * ##
    # 'ara'
    nman_fer_crit_gw_ara = ascraster.duplicategrid(nman_crit_gw_ara)
    nman_fer_crit_gw_ara.add(nfer_crit_gw_ara)
    fileout = os.path.join(params.outputdir,"nman_fer_crit_gw_ara.asc")
    nman_fer_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)    
    # 'igl'
    nman_fer_crit_gw_igl = ascraster.duplicategrid(nman_crit_gw_igl)
    nman_fer_crit_gw_igl.add(nfer_crit_gw_igl)
    fileout = os.path.join(params.outputdir,"nman_fer_crit_gw_igl.asc")
    nman_fer_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)  

    
    ## * NH3 emissions at critical N input *
    # 'ara'
    nh3em_man_crit_gw_ara = ascraster.duplicategrid(nman_crit_gw_ara)
    nh3em_man_crit_gw_ara.multiply(nh3_ef_man_ara)  
    nh3em_fer_crit_gw_ara = ascraster.duplicategrid(nfer_crit_gw_ara)
    nh3em_fer_crit_gw_ara.multiply(nh3_ef_fer_ara) 
    nh3em_crit_gw_ara = ascraster.duplicategrid(nh3em_man_crit_gw_ara)
    nh3em_crit_gw_ara.add(nh3em_fer_crit_gw_ara)
    print_debug(nh3em_crit_gw_ara, "nh3em_crit_gw_ara =")
    # 'igl'
    nh3em_man_crit_gw_igl = ascraster.duplicategrid(nman_crit_gw_igl)
    nh3em_man_crit_gw_igl.multiply(nh3_ef_man_igl)  
    nh3em_fer_crit_gw_igl = ascraster.duplicategrid(nfer_crit_gw_igl)
    nh3em_fer_crit_gw_igl.multiply(nh3_ef_fer_igl) 
    nh3em_crit_gw_igl = ascraster.duplicategrid(nh3em_man_crit_gw_igl)
    nh3em_crit_gw_igl.add(nh3em_fer_crit_gw_igl)
    print_debug(nh3em_crit_gw_igl, "nh3em_crit_gw_igl =")
    
    ## * N deposition at critical N input *
    ndep_crit_gw_tot = ascraster.duplicategrid(nh3em_crit_gw_ara)
    ndep_crit_gw_tot.add(nh3em_crit_gw_igl)
    ndep_crit_gw_tot.add(nox_em)
    ndep_crit_gw_tot.add(nh3_tot_egl)
    
    fileout = os.path.join(params.outputdir,"ndep_crit_gw_tot.asc")
    ndep_crit_gw_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_gw_tot,"ndep_crit_gw_tot =")     
    
    # OPTION 1 - for grid cells with EITHER ara OR igl
    # 'ara'
    ndep_crit_gw_V1_ara = ascraster.duplicategrid(ndep_crit_gw_tot)
    ndep_crit_gw_V1_ara.multiply(fara)
    # 'igl'
    ndep_crit_gw_V1_igl = ascraster.duplicategrid(ndep_crit_gw_tot)
    ndep_crit_gw_V1_igl.multiply(figl)
 
    # OPTION 2 - for grid cells with BOTH ara + igl
    # 'ara'
    ndep_crit_gw_V2_ara = ascraster.duplicategrid(nle_crit_gw_igl)
    ndep_crit_gw_V2_ara.divide(nle_igl, default_nodata_value = -9999)
    ndep_crit_gw_V2_ara.multiply(nh3_tot_igl)
    ndep_crit_gw_V2_ara.add(nh3em_crit_gw_ara)
    ndep_crit_gw_V2_ara.add(nox_em)
    ndep_crit_gw_V2_ara.add(nh3_tot_egl)
    ndep_crit_gw_V2_ara.multiply(fara)
    # 'igl'
    ndep_crit_gw_V2_igl = ascraster.duplicategrid(nle_crit_gw_ara)
    ndep_crit_gw_V2_igl.divide(nle_ara, default_nodata_value = -9999)
    ndep_crit_gw_V2_igl.multiply(nh3_tot_ara)
    ndep_crit_gw_V2_igl.add(nh3em_crit_gw_igl)
    ndep_crit_gw_V2_igl.add(nox_em)
    ndep_crit_gw_V2_igl.add(nh3_tot_egl)
    ndep_crit_gw_V2_igl.multiply(figl)
    
    # MAKE ONE GRID FOR N DEPOSITION
    # 'ara'
    ndep_crit_gw_ara = ascraster.duplicategrid(ndep_crit_gw_V1_ara)
    for icell in range(ndep_crit_gw_ara.length):
        f_ara = fara.get_data(icell)
        f_igl = figl.get_data(icell)
        ndep_ara2 = ndep_crit_gw_V2_ara.get_data(icell)
        nle = nle_ag.get_data(icell)
        if (f_ara is None or f_igl is None):
            continue
        elif (f_ara > 0 and f_igl > 0 and nle > 0) :
            ndep_ara = ndep_ara2
        else:
            continue
            
        ndep_crit_gw_ara.set_data(icell,ndep_ara) 
    fileout = os.path.join(params.outputdir,"ndep_crit_gw_ara.asc")
    ndep_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_gw_ara,"ndep_crit_gw_ara =")

    # 'igl'
    ndep_crit_gw_igl = ascraster.duplicategrid(ndep_crit_gw_V1_igl)
    for icell in range(ndep_crit_gw_igl.length):
        f_ara = fara.get_data(icell)
        f_igl = figl.get_data(icell)
        ndep_igl2 = ndep_crit_gw_V2_igl.get_data(icell)
        nle = nle_ag.get_data(icell)
        if (f_ara is None or f_igl is None):
            continue
        elif (f_ara > 0 and f_igl > 0 and nle > 0) :
            ndep_igl = ndep_igl2
        else:
            continue
            
        ndep_crit_gw_igl.set_data(icell,ndep_igl) 
    fileout = os.path.join(params.outputdir,"ndep_crit_gw_igl.asc")
    ndep_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_gw_igl,"ndep_crit_gw_igl =")
    
    ##TEST: Total N deposition as sum of depositions#
    ndep_crit_gw_egl = ascraster.duplicategrid(ndep_crit_gw_tot)
    ndep_crit_gw_egl.multiply(fegl)
    ndep_crit_gw_nat = ascraster.duplicategrid(ndep_crit_gw_tot)
    ndep_crit_gw_nat.multiply(fnat)
    
    ndep_crit_gw_tot_TEST = ascraster.duplicategrid(ndep_crit_gw_ara)
    ndep_crit_gw_tot_TEST.add(ndep_crit_gw_igl)
    ndep_crit_gw_tot_TEST.add(ndep_crit_gw_egl)
    ndep_crit_gw_tot_TEST.add(ndep_crit_gw_nat)

    fileout = os.path.join(params.outputdir,"ndep_crit_gw_tot_TEST.asc")
    ndep_crit_gw_tot_TEST.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_gw_tot_TEST,"ndep_crit_gw_tot_TEST =")    
    
    ## * Total critical N inputs *
    # 'ara'
    nin_crit_gw_ara = ascraster.duplicategrid(nman_crit_gw_ara)
    nin_crit_gw_ara.add(nfer_crit_gw_ara)
    nin_crit_gw_ara.add(ndep_crit_gw_ara)
    nin_crit_gw_ara.add(nfix_ara)
    fileout = os.path.join(params.outputdir,"nin_crit_gw_ara.asc")
    nin_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_gw_ara,"nin_crit_gw_ara =")
    # 'igl'
    nin_crit_gw_igl = ascraster.duplicategrid(nman_crit_gw_igl)
    nin_crit_gw_igl.add(nfer_crit_gw_igl)
    nin_crit_gw_igl.add(ndep_crit_gw_igl)
    nin_crit_gw_igl.add(nfix_igl)
    fileout = os.path.join(params.outputdir,"nin_crit_gw_igl.asc")
    nin_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_gw_igl,"nin_crit_gw_igl =")
    # 'ara+igl'
    nin_crit_gw_araigl = ascraster.duplicategrid(nin_crit_gw_ara)
    nin_crit_gw_araigl.add(nin_crit_gw_igl)
    fileout = os.path.join(params.outputdir,"nin_crit_gw_araigl.asc")
    nin_crit_gw_araigl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    ## * N surface runoff at critical N inputs *
    # 'ara'
    nsro_crit_gw_ara = ascraster.duplicategrid(nin_crit_gw_ara)
    nsro_crit_gw_ara.multiply(fsro_ag)
    print_debug(nsro_crit_gw_ara,"nsro_crit_gw_ara =")
    # 'igl'
    nsro_crit_gw_igl = ascraster.duplicategrid(nin_crit_gw_igl)
    nsro_crit_gw_igl.multiply(fsro_ag)
    print_debug(nsro_crit_gw_igl,"nsro_crit_gw_igl =")
    
    ## * N uptake at critical N inputs *
    # 'ara'
    nup_crit_gw_ara = ascraster.duplicategrid(nin_crit_gw_ara)
    nup_crit_gw_ara.substract(nsro_crit_gw_ara)
    nup_crit_gw_ara.multiply(frnup_ara)
    fileout = os.path.join(params.outputdir,"nup_crit_gw_ara.asc")
    nup_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_gw_ara,"nup_crit_gw_ara =")
    # 'igl'
    nup_crit_gw_igl = ascraster.duplicategrid(nin_crit_gw_igl)
    nup_crit_gw_igl.substract(nsro_crit_gw_igl)
    nup_crit_gw_igl.multiply(frnup_igl)
    fileout = os.path.join(params.outputdir,"nup_crit_gw_igl.asc")
    nup_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_gw_igl,"nup_crit_gw_igl =") 
 
    ## * NUE at critical N inputs *
    # 'ara'
    nue_crit_gw_ara = ascraster.duplicategrid(nup_crit_gw_ara)
    nue_crit_gw_ara.divide(nin_crit_gw_ara, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_gw_ara.asc")
    nue_crit_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_gw_ara,"nue_crit_gw_ara =")
    # 'igl'
    nue_crit_gw_igl = ascraster.duplicategrid(nup_crit_gw_igl)
    nue_crit_gw_igl.divide(nin_crit_gw_igl, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_gw_igl.asc")
    nue_crit_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_gw_igl,"nue_crit_gw_igl =")
    
    ## * Maximum uptake fraction  *
    # 'ara'
    fnup_max_gw_ara = ascraster.duplicategrid(nup_max_ara)
    fnup_max_gw_ara.divide(nup_crit_gw_ara)
    fileout = os.path.join(params.outputdir,"fnup_max_gw_ara.asc")
    fnup_max_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_gw_ara,"fnup_max_gw_ara =")
    # 'igl'
    fnup_max_gw_igl = ascraster.duplicategrid(nup_max_igl)
    fnup_max_gw_igl.divide(nup_crit_gw_igl)
    fileout = os.path.join(params.outputdir,"fnup_max_gw_igl.asc")
    fnup_max_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_gw_igl,"fnup_max_gw_igl =")
    
    ## * Correction factor for grid cells where Nup,crit > Nup,max *
    # 'ara'
    fnup_corr_gw_ara = ascraster.duplicategrid(nin_max_ara)
    fnup_corr_gw_ara.substract(nfix_ara)
    temp2_ara = ascraster.duplicategrid(nh3_tot_egl)
    temp2_ara.add(nox_em)
    temp2_ara.multiply(fara)
    fnup_corr_gw_ara.substract(temp2_ara) 
    temp3_ara = ascraster.duplicategrid(nh3em_crit_gw_ara)
    temp3_ara.multiply(fara)
    temp3_ara.add(nman_crit_gw_ara)
    temp3_ara.add(nfer_crit_gw_ara)
    fnup_corr_gw_ara.divide(temp3_ara, default_nodata_value = -9999) 
    fileout = os.path.join(params.outputdir,"fnup_corr_gw_ara.asc")
    fnup_corr_gw_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_gw_ara,"fnup_corr_gw_ara =")
    # 'igl'
    fnup_corr_gw_igl = ascraster.duplicategrid(nin_max_igl)
    fnup_corr_gw_igl.substract(nfix_igl)
    temp2_igl = ascraster.duplicategrid(nh3_tot_egl)
    temp2_igl.add(nox_em)
    temp2_igl.multiply(figl)
    fnup_corr_gw_igl.substract(temp2_igl)  
    temp3_igl = ascraster.duplicategrid(nh3em_crit_gw_igl)
    temp3_igl.multiply(figl)
    temp3_igl.add(nman_crit_gw_igl)
    temp3_igl.add(nfer_crit_gw_igl)
    fnup_corr_gw_igl.divide(temp3_igl, default_nodata_value = -9999)   
    fileout = os.path.join(params.outputdir,"fnup_corr_gw_igl.asc")
    fnup_corr_gw_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_gw_igl,"fnup_corr_gw_igl =")    
        
    '''
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
    '''
    
    ########### FORWARD CALCULATIONS TO CHECK ###########
    ## * Critical N budget *
    # 'ara'
    nbud_crit_gw_ara = ascraster.duplicategrid(nin_crit_gw_ara)
    nbud_crit_gw_ara.substract(nup_crit_gw_ara)
    print_debug(nbud_crit_gw_ara,"nbud_crit_gw_ara =")
    # 'igl'
    nbud_crit_gw_igl = ascraster.duplicategrid(nin_crit_gw_igl)
    nbud_crit_gw_igl.substract(nup_crit_gw_igl)
    print_debug(nbud_crit_gw_igl,"nbud_crit_gw_igl =")
    
    ## * Critical leaching *
    # 'ara'
    nle_crit_gw_test_ara = ascraster.duplicategrid(nbud_crit_gw_ara)
    nle_crit_gw_test_ara.substract(nsro_crit_gw_ara)
    nle_crit_gw_test_ara.multiply(fle_ag)
    fileout = os.path.join(params.outputdir,"nle_crit_gw_test_ara.asc")
    nle_crit_gw_test_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_crit_gw_test_ara,"nle_crit_gw_test_ara =")
    # 'igl'
    nle_crit_gw_test_igl = ascraster.duplicategrid(nbud_crit_gw_igl)
    nle_crit_gw_test_igl.substract(nsro_crit_gw_igl)
    nle_crit_gw_test_igl.multiply(fle_ag)
    fileout = os.path.join(params.outputdir,"nle_crit_gw_test_igl.asc")
    nle_crit_gw_test_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nle_crit_gw_test_igl,"nle_crit_gw_test_igl =")
    
    ## *TEST IF FORWARD CALCULATIONS EQUAL BACKWARD CALLCULATION*
    # 'ara'
    if icell_debug<0:
        pass
    else:
        fw_ara = nle_crit_gw_test_ara.get_data(icell_debug)
        bw_ara = nle_crit_gw_ara.get_data(icell_debug)
        if fw_ara is None:
            print("FW/BW_TEST:_Forward_calculation_not_possible:_Nin,crit = None")
        
        else:
            fw_ara = round(fw_ara,4) 
            bw_ara = round(bw_ara,4)
            if fw_ara == bw_ara:
                print("FW/BW_TEST_ARABLE_LAND = SUCCESFUL")
            else:
                print("FW/BW_TEST_ARABLE_LAND = NOT_SUCCESFUL")
    # 'igl'
    if icell_debug<0:
        pass
    else:
        fw_igl = nle_crit_gw_test_igl.get_data(icell_debug)
        bw_igl = nle_crit_gw_igl.get_data(icell_debug)
        if fw_igl is None:
            print("FW/BW_TEST:_Forward_calculation_not_possible:_Nin,crit = None")
        
        else:
            fw_igl = round(fw_igl,4) 
            bw_igl = round(bw_igl,4)
            if fw_igl == bw_igl:
                print("FW/BW_TEST_INTENSIVE_GRASSLAND = SUCCESFUL")
            else:
                print("FW/BW_TEST_INTENSIVE_GRASSLAND = NOT_SUCCESFUL")
    ############################################################################################