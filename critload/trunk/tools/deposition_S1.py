# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/deposition.py $"
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

    #print("The critical N deposition rate is " + str(params.crit_dep) + " kg N ha-1 yr-1")
    
    # load needed variables for calculations
    biome           = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"gnlct.asc")            ,numtype=float,mask=params.mask)
    a_tot           = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"a_tot.asc")            ,numtype=float,mask=params.mask)
    nfix_ara        = ascraster.Asciigrid(ascii_file=params.filename_nfixation_cropland                   ,numtype=float,mask=params.mask)
    nfix_igl        = ascraster.Asciigrid(ascii_file=params.filename_nfixation_intgl                      ,numtype=float,mask=params.mask)
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
    fara            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fara.asc")            ,numtype=float,mask=params.mask)
    figl            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"figl.asc")            ,numtype=float,mask=params.mask)
    fsro_ag         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")         ,numtype=float,mask=params.mask)
    frnup_ara       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_ara.asc")       ,numtype=float,mask=params.mask)
    frnup_igl       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_igl.asc")       ,numtype=float,mask=params.mask)
    nup_max_ara     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nup_max_ara.asc")     ,numtype=float,mask=params.mask)
    nup_max_igl     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nup_max_igl.asc")     ,numtype=float,mask=params.mask)
    nin_max_ara     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nin_max_ara.asc")     ,numtype=float,mask=params.mask)   
    nin_max_igl     = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nin_max_igl.asc")     ,numtype=float,mask=params.mask)   
    ndep_corr_tot   = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"ndep_corr_tot.asc")   ,numtype=float,mask=params.mask) 
    
    # make grid with critical N deposition per biome
    ndep_crit_ha = ascraster.duplicategrid(nfix_ara)
    # watch out: can ndep_crit_ha become both -9999 and -1 (NA value?)
    for i in range(ndep_crit_ha.length):
        ndep_crit_ha.set_data(i,-9999)
          
    for icell in range(biome.length):
        val = biome.get_data(icell)
        # Ice (7) or Hot desert (16)
        if (val == 7 or val == 16):
            cl = 5.0
        # Boreal forest (10), Cool coniferous forest (11) or scrubland (17)
        elif (val == 10 or val == 11 or val == 17):
            cl = 7.5
        # Tundra (8) or wooded tundra (9)or Warm mixed forest (14)
        elif (val == 8 or val == 9 or val == 14):
            cl = 10.0
        # Temperate mixed forest (12) Temperate deciduous forest (13) 
        elif (val == 12 or val == 13):
            cl = 12.5
        # Savanna (18)
        elif (val == 18):
            cl = 15.0
        # Grassland/steppe (15)
        elif (val == 15):
            cl = 17.5                    
        # Tropical woodland (19) or Tropical forest (20)
        elif (val == 19 or val == 20):
            cl = 20
        # Biome can also have value 0 or none (-1)
        else:
            continue        
        ndep_crit_ha.set_data(icell,cl) 
    
    print_debug(biome,"biome =") 
    
    fileout = os.path.join(params.outputdir,"ndep_crit_ha.asc")
    ndep_crit_ha.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_ha,"ndep_crit_ha =") 
    
    ## * Total critical deposition *
    ndep_crit_tot = ascraster.duplicategrid(ndep_crit_ha)
    ndep_crit_tot.multiply(a_tot)
    fileout = os.path.join(params.outputdir,"ndep_crit_tot.asc")
    ndep_crit_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_tot,"ndep_crit_tot =")    
   
    ## * Fraction critical/total deposition *
    fndep_crit = ascraster.duplicategrid(ndep_crit_tot)
    fndep_crit.divide(ndep_corr_tot, default_nodata_value = -9999)

    ## * NOx and NH3 egl at critical N inputs *
    nox_em_crit =ascraster.duplicategrid(nox_em)
    nox_em_crit.multiply(fndep_crit)
    nh3_tot_egl_crit = ascraster.duplicategrid(nh3_tot_egl)
    nh3_tot_egl_crit.multiply(fndep_crit)
    
    ## * Critical NH3 emissions *
    nh3em_crit_ara = ascraster.duplicategrid(nh3_tot_ara)
    nh3em_crit_ara.multiply(fndep_crit)
    print_debug(nh3em_crit_ara,"nh3em_crit_ara =")
    nh3em_crit_igl = ascraster.duplicategrid(nh3_tot_igl)
    nh3em_crit_igl.multiply(fndep_crit)
    print_debug(nh3em_crit_igl,"nh3em_crit_igl =")
    
    '''
    nh3em_ara_igl = ascraster.duplicategrid(nh3_tot_ara)
    nh3em_ara_igl.add(nh3_tot_igl)
    # 'ara'
    nh3_fraction_ara = ascraster.duplicategrid(nh3_tot_ara)
    nh3_fraction_ara.divide(nh3em_ara_igl, default_nodata_value = -9999)   
    nh3em_crit_ara = ascraster.duplicategrid(ndep_crit_tot)
    nh3em_crit_ara.substract(nox_em)
    nh3em_crit_ara.substract(nh3_tot_egl)
    nh3em_crit_ara.multiply(nh3_fraction_ara)
    print_debug(nh3em_crit_ara,"nh3em_crit_ara =")
    # 'igl'
    nh3_fraction_igl = ascraster.duplicategrid(nh3_tot_igl)
    nh3_fraction_igl.divide(nh3em_ara_igl, default_nodata_value = -9999)   
    nh3em_crit_igl = ascraster.duplicategrid(ndep_crit_tot)
    nh3em_crit_igl.substract(nox_em)
    nh3em_crit_igl.substract(nh3_tot_egl)
    nh3em_crit_igl.multiply(nh3_fraction_igl)
    print_debug(nh3em_crit_igl,"nh3em_crit_igl =")
    '''
    
    ## * Critical N inputs from manure *
    one_grid = ascraster.duplicategrid(frnfe_ara)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
    
    # 'ara'
    one_min_frnfe_ara = ascraster.duplicategrid(one_grid)
    one_min_frnfe_ara.substract(frnfe_ara)
    frnfe_division_ara = ascraster.duplicategrid(frnfe_ara)
    frnfe_division_ara.divide(one_min_frnfe_ara, default_nodata_value = -9999)
    
    denominator_ara = ascraster.duplicategrid(frnfe_division_ara)
    denominator_ara.multiply(nh3_ef_fer_ara)
    denominator_ara.add(nh3_ef_man_ara)
 
    nman_crit_dep_ara = ascraster.duplicategrid(nh3em_crit_ara)
    nman_crit_dep_ara.divide(denominator_ara, default_nodata_value = -9999)
    
    for icell in range(nman_crit_dep_ara.length):       
        f_ara = fara.get_data(icell) 
        f_igl = figl.get_data(icell)
        if (f_ara == 0 and f_igl > 0) : 
            nman_ara = 0
        else:
            continue
        nman_crit_dep_ara.set_data(icell,nman_ara)
        
        
    for icell in range (nman_crit_dep_ara.length):
        nman_ara3 = nman_crit_dep_ara.get_data(icell)
        if (nman_ara3 is None):
            continue
        if (nman_ara3 < 0):
            nman_ara = 0
        else:
            continue
        nman_crit_dep_ara.set_data(icell,nman_ara)
    
    fileout = os.path.join(params.outputdir,"nman_crit_dep_ara.asc")
    nman_crit_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_dep_ara,"nman_crit_dep_ara =")   
    
    # 'igl'
    one_min_frnfe_igl = ascraster.duplicategrid(one_grid)
    one_min_frnfe_igl.substract(frnfe_igl)
    frnfe_division_igl = ascraster.duplicategrid(frnfe_igl)
    frnfe_division_igl.divide(one_min_frnfe_igl, default_nodata_value = -9999)
    
    denominator_igl = ascraster.duplicategrid(frnfe_division_igl)
    denominator_igl.multiply(nh3_ef_fer_igl)
    denominator_igl.add(nh3_ef_man_igl)
 
    nman_crit_dep_igl = ascraster.duplicategrid(nh3em_crit_igl)
    nman_crit_dep_igl.divide(denominator_igl, default_nodata_value = -9999)
    
    for icell in range(nman_crit_dep_igl.length):       
        f_ara = fara.get_data(icell) 
        f_igl = figl.get_data(icell) 
        if (f_igl == 0 and f_ara > 0) : 
            nman_igl = 0
        else:
            continue
        nman_crit_dep_igl.set_data(icell,nman_igl)
        
    for icell in range (nman_crit_dep_igl.length):
        nman_igl3 = nman_crit_dep_igl.get_data(icell)
        if (nman_igl3 is None):
            continue
        if (nman_igl3 < 0):
            nman_igl = 0
        else:
            continue
        nman_crit_dep_igl.set_data(icell,nman_igl)
    
    fileout = os.path.join(params.outputdir,"nman_crit_dep_igl.asc")
    nman_crit_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_dep_igl,"nman_crit_dep_igl =")
    
    ## calculate critical N input from fertilizer
    # 'ara'
    nfer_crit_dep_ara = ascraster.duplicategrid(nman_crit_dep_ara)
    nfer_crit_dep_ara.multiply(frnfe_division_ara)
    for icell in range(nfer_crit_dep_ara.length):       
        f_ara = fara.get_data(icell) 
        f_igl = figl.get_data(icell)
        if (f_ara == 0 and f_igl > 0) : 
            nfer_ara = 0
        else:
            continue
        nfer_crit_dep_ara.set_data(icell,nfer_ara)
    
    fileout = os.path.join(params.outputdir,"nfer_crit_dep_ara.asc")
    nfer_crit_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_crit_dep_ara,"nfer_crit_dep_ara =")

    # 'igl'
    nfer_crit_dep_igl = ascraster.duplicategrid(nman_crit_dep_igl)
    nfer_crit_dep_igl.multiply(frnfe_division_igl)
    for icell in range(nfer_crit_dep_igl.length):       
        f_ara = fara.get_data(icell) 
        f_igl = figl.get_data(icell) 
        if (f_igl == 0 and f_ara > 0) : 
            nfer_igl = 0
        else:
            continue
        nfer_crit_dep_igl.set_data(icell,nfer_igl)
    
    fileout = os.path.join(params.outputdir,"nfer_crit_dep_igl.asc")
    nfer_crit_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfer_crit_dep_igl,"nfer_crit_dep_igl =")

    ## * Critical N inputs from fertilizer plus manure * ##
    # 'ara'
    nman_fer_crit_dep_ara = ascraster.duplicategrid(nman_crit_dep_ara)
    nman_fer_crit_dep_ara.add(nfer_crit_dep_ara)
    fileout = os.path.join(params.outputdir,"nman_fer_crit_dep_ara.asc")
    nman_fer_crit_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)    
    # 'igl'
    nman_fer_crit_dep_igl = ascraster.duplicategrid(nman_crit_dep_igl)
    nman_fer_crit_dep_igl.add(nfer_crit_dep_igl)
    fileout = os.path.join(params.outputdir,"nman_fer_crit_dep_igl.asc")
    nman_fer_crit_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)  
      
    ## * NH3 emissions at critical N input *
    # 'ara'
    nh3em_man_crit_dep_ara = ascraster.duplicategrid(nman_crit_dep_ara)
    nh3em_man_crit_dep_ara.multiply(nh3_ef_man_ara) 
    nh3em_fer_crit_dep_ara = ascraster.duplicategrid(nfer_crit_dep_ara)
    nh3em_fer_crit_dep_ara.multiply(nh3_ef_fer_ara)
    nh3em_crit_dep_ara = ascraster.duplicategrid(nh3em_fer_crit_dep_ara)
    nh3em_crit_dep_ara.add(nh3em_man_crit_dep_ara)
    print_debug(nh3em_crit_dep_ara, "nh3em_crit_dep_ara =")
    # 'igl'
    nh3em_man_crit_dep_igl = ascraster.duplicategrid(nman_crit_dep_igl)
    nh3em_man_crit_dep_igl.multiply(nh3_ef_man_igl) 
    nh3em_fer_crit_dep_igl = ascraster.duplicategrid(nfer_crit_dep_igl)
    nh3em_fer_crit_dep_igl.multiply(nh3_ef_fer_igl)
    nh3em_crit_dep_igl = ascraster.duplicategrid(nh3em_fer_crit_dep_igl)
    nh3em_crit_dep_igl.add(nh3em_man_crit_dep_igl)
    print_debug(nh3em_crit_dep_igl, "nh3em_crit_dep_igl =") 

    ## * N deposition at critical N inputs *    
    ndep_crit_dep_tot = ascraster.duplicategrid(nh3em_crit_dep_ara)
    ndep_crit_dep_tot.add(nh3em_crit_dep_igl)
    ndep_crit_dep_tot.add(nox_em_crit)
    ndep_crit_dep_tot.add(nh3_tot_egl_crit)
    fileout = os.path.join(params.outputdir,"ndep_crit_dep_tot.asc")
    ndep_crit_dep_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_dep_tot,"ndep_crit_dep_tot =")  
    # 'ara'
    ndep_crit_dep_ara = ascraster.duplicategrid(ndep_crit_dep_tot)
    ndep_crit_dep_ara.multiply(fara)
    print_debug(ndep_crit_dep_ara,"ndep_crit_dep_ara =")
    # 'igl'
    ndep_crit_dep_igl = ascraster.duplicategrid(ndep_crit_dep_tot)
    ndep_crit_dep_igl.multiply(figl)
    print_debug(ndep_crit_dep_igl,"ndep_crit_dep_igl =")

    ## * Total critical N inputs *
    # 'ara'
    nin_crit_dep_ara = ascraster.duplicategrid(nman_crit_dep_ara)
    nin_crit_dep_ara.add(nfer_crit_dep_ara)
    nin_crit_dep_ara.add(ndep_crit_dep_ara)
    nin_crit_dep_ara.add(nfix_ara)
    fileout = os.path.join(params.outputdir,"nin_crit_dep_ara.asc")
    nin_crit_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_dep_ara,"nin_crit_dep_ara =")
    # 'igl'
    nin_crit_dep_igl = ascraster.duplicategrid(nman_crit_dep_igl)
    nin_crit_dep_igl.add(nfer_crit_dep_igl)
    nin_crit_dep_igl.add(ndep_crit_dep_igl)
    nin_crit_dep_igl.add(nfix_igl)
    fileout = os.path.join(params.outputdir,"nin_crit_dep_igl.asc")
    nin_crit_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_dep_igl,"nin_crit_dep_igl =")
    # 'ara+igl'
    nin_crit_dep_araigl = ascraster.duplicategrid(nin_crit_dep_ara)
    nin_crit_dep_araigl.add(nin_crit_dep_igl)
    fileout = os.path.join(params.outputdir,"nin_crit_dep_araigl.asc")
    nin_crit_dep_araigl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    ## * N surface runoff at critical N inputs *
    # 'ara'
    nsro_crit_dep_ara = ascraster.duplicategrid(nin_crit_dep_ara)
    nsro_crit_dep_ara.multiply(fsro_ag)
    print_debug(nsro_crit_dep_ara,"nsro_crit_dep_ara =")
    # 'igl'
    nsro_crit_dep_igl = ascraster.duplicategrid(nin_crit_dep_igl)
    nsro_crit_dep_igl.multiply(fsro_ag)
    print_debug(nsro_crit_dep_igl,"nsro_crit_dep_igl =")    
    
    ## * N uptake at critical N inputs *
    # 'ara'
    nup_crit_dep_ara = ascraster.duplicategrid(nin_crit_dep_ara)
    nup_crit_dep_ara.substract(nsro_crit_dep_ara)
    nup_crit_dep_ara.multiply(frnup_ara)
    fileout = os.path.join(params.outputdir,"nup_crit_dep_ara.asc")
    nup_crit_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_dep_ara,"nup_crit_dep_ara =")
    # 'igl'
    nup_crit_dep_igl = ascraster.duplicategrid(nin_crit_dep_igl)
    nup_crit_dep_igl.substract(nsro_crit_dep_igl)
    nup_crit_dep_igl.multiply(frnup_igl)
    fileout = os.path.join(params.outputdir,"nup_crit_dep_igl.asc")
    nup_crit_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_dep_igl,"nup_crit_dep_igl =")
    
    ## * NUE at critical N inputs *
    # 'ara'
    nue_crit_dep_ara = ascraster.duplicategrid(nup_crit_dep_ara)
    nue_crit_dep_ara.divide(nin_crit_dep_ara, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_dep_ara.asc")
    nue_crit_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_dep_ara,"nue_crit_dep_ara =")
    # 'igl'
    nue_crit_dep_igl = ascraster.duplicategrid(nup_crit_dep_igl)
    nue_crit_dep_igl.divide(nin_crit_dep_igl, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_dep_igl.asc")
    nue_crit_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_dep_igl,"nue_crit_dep_igl =")
    
    ## * Maximum uptake fraction  *
    # 'ara'
    fnup_max_dep_ara = ascraster.duplicategrid(nup_max_ara)
    fnup_max_dep_ara.divide(nup_crit_dep_ara)
    fileout = os.path.join(params.outputdir,"fnup_max_dep_ara.asc")
    fnup_max_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_dep_ara,"fnup_max_dep_ara =")
    # 'igl'
    fnup_max_dep_igl = ascraster.duplicategrid(nup_max_igl)
    fnup_max_dep_igl.divide(nup_crit_dep_igl)
    fileout = os.path.join(params.outputdir,"fnup_max_dep_igl.asc")
    fnup_max_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_dep_igl,"fnup_max_dep_igl =")
    
    ## * Correction factor for grid cells where Nup,crit > Nup,max *
    # 'ara'
    fnup_corr_dep_ara = ascraster.duplicategrid(nin_max_ara)
    fnup_corr_dep_ara.substract(nfix_ara)
    temp2_ara = ascraster.duplicategrid(nh3_tot_egl_crit)
    temp2_ara.add(nox_em_crit)
    temp2_ara.multiply(fara)
    fnup_corr_dep_ara.substract(temp2_ara) 
    temp3_ara = ascraster.duplicategrid(nh3em_crit_dep_ara)
    temp3_ara.multiply(fara)
    temp3_ara.add(nman_crit_dep_ara)
    temp3_ara.add(nfer_crit_dep_ara)
    fnup_corr_dep_ara.divide(temp3_ara, default_nodata_value = -9999) 
    fileout = os.path.join(params.outputdir,"fnup_corr_dep_ara.asc")
    fnup_corr_dep_ara.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_dep_ara,"fnup_corr_dep_ara =")
    # 'igl'
    fnup_corr_dep_igl = ascraster.duplicategrid(nin_max_igl)
    fnup_corr_dep_igl.substract(nfix_igl)
    temp2_igl = ascraster.duplicategrid(nh3_tot_egl_crit)
    temp2_igl.add(nox_em_crit)
    temp2_igl.multiply(figl)
    fnup_corr_dep_igl.substract(temp2_igl)  
    temp3_igl = ascraster.duplicategrid(nh3em_crit_dep_igl)
    temp3_igl.multiply(figl)
    temp3_igl.add(nman_crit_dep_igl)
    temp3_igl.add(nfer_crit_dep_igl)
    fnup_corr_dep_igl.divide(temp3_igl, default_nodata_value = -9999)   
    fileout = os.path.join(params.outputdir,"fnup_corr_dep_igl.asc")
    fnup_corr_dep_igl.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_dep_igl,"fnup_corr_dep_igl =")    
    
    
    ########### FORWARD CALCULATIONS TO CHECK ###########
    if icell_debug<0:
        pass
    else:
        fw = ndep_crit_dep_tot.get_data(icell_debug)
        bw = ndep_crit_tot.get_data(icell_debug)
        if fw is None:
            print("FW/BW_TEST:_Forward_calculation_not_possible:_Nin,crit = None")
        
        else:
            fw = round(fw,4) 
            bw = round(bw,4)
            if fw == bw:
                print("FW/BW_TEST = SUCCESFUL")
            else:
                print("FW/BW_TEST = NOT_SUCCESFUL")
    ############################################################################################