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
    biome            = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"gnlct.asc")            ,numtype=float,mask=params.mask)
    a_tot            = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"a_tot.asc")            ,numtype=float,mask=params.mask)
    nox_em           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc")          ,numtype=float,mask=params.mask)
    nh3_tot_egl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc")     ,numtype=float,mask=params.mask)
    nh3_ef_man_agri  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_agri.asc") ,numtype=float,mask=params.mask)
    nh3_ef_fert_agri = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert_agri.asc"),numtype=float,mask=params.mask)
    frnfe_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_agri.asc")      ,numtype=float,mask=params.mask)
    fagri            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fagri.asc")           ,numtype=float,mask=params.mask)
    n_fix_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_fix_agri.asc")      ,numtype=float,mask=params.mask)
    fsro_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc")         ,numtype=float,mask=params.mask)
    frnup_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_agri.asc")      ,numtype=float,mask=params.mask)
    n_up_max         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_up_max.asc")        ,numtype=float,mask=params.mask)
    n_in_max         = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_in_max.asc")        ,numtype=float,mask=params.mask)   
    
    # make grid with critical N deposition per biome
    ndep_crit_ha = ascraster.duplicategrid(n_fix_agri)
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
    
    print_debug(biome,"The biome ID is") 
    
    fileout = os.path.join(params.outputdir,"ndep_crit_ha.asc")
    ndep_crit_ha.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_ha,"The critical N deposition per hectare is") 
    
    # calculate total critical deposition: Ndep,tot(crit) = Ndep,crit,ha * A
    ndep_crit_tot = ascraster.duplicategrid(ndep_crit_ha)
    ndep_crit_tot.multiply(a_tot)
    #fileout = os.path.join(params.outputdir,"ndep_crit_tot.asc")
    #ndep_crit_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_crit_tot,"The total critical N deposition is")    
   
    # calculate critical N input from manure
    nh3_em_crit_agri = ascraster.duplicategrid(ndep_crit_tot)
    nh3_em_crit_agri.substract(nox_em)
    nh3_em_crit_agri.substract(nh3_tot_egl)

    one_grid = ascraster.duplicategrid(frnfe_agri)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
        
    one_min_frnfe = ascraster.duplicategrid(one_grid)
    one_min_frnfe.substract(frnfe_agri)
    frnfe_division = ascraster.duplicategrid(frnfe_agri)
    frnfe_division.divide(one_min_frnfe, default_nodata_value = -9999)
    
    denominator = ascraster.duplicategrid(frnfe_division)
    denominator.multiply(nh3_ef_fert_agri)
    denominator.add(nh3_ef_man_agri)
 
    nman_crit_dep = ascraster.duplicategrid(nh3_em_crit_agri)
    nman_crit_dep.divide(denominator, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir,"nman_crit_dep.asc")
    nman_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nman_crit_dep,"The critical N input from manure for the N deposition criterion is")
    
    # calculate critical N input from fertilizer
    nfert_crit_dep = ascraster.duplicategrid(nman_crit_dep)
    nfert_crit_dep.multiply(frnfe_division)
    fileout = os.path.join(params.outputdir,"nfert_crit_dep.asc")
    nfert_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nfert_crit_dep,"The critical N input from fertilizer for the N deposition criterion is")
    
    # calculate related N deposition
    nh3em_man_crit_dep = ascraster.duplicategrid(nman_crit_dep)
    nh3em_man_crit_dep.multiply(nh3_ef_man_agri)

    fileout = os.path.join(params.outputdir,"nh3em_man_crit_dep.asc")
    nh3em_man_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    nh3em_fert_crit_dep = ascraster.duplicategrid(nfert_crit_dep)
    nh3em_fert_crit_dep.multiply(nh3_ef_fert_agri)
    
    fileout = os.path.join(params.outputdir,"nh3em_fert_crit_dep.asc")
    nh3em_fert_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    
    nh3em_crit_dep = ascraster.duplicategrid(nh3em_fert_crit_dep)
    nh3em_crit_dep.add(nh3em_man_crit_dep)
    #
    fileout = os.path.join(params.outputdir,"nh3em_crit_dep.asc")
    nh3em_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    #
    #nh3em_crit_dep.add(nh3_tot_egl)
    ndep_crit_dep_tot = ascraster.duplicategrid(nh3em_crit_dep)
    ndep_crit_dep_tot.add(nox_em)
    ndep_crit_dep_tot.add(nh3_tot_egl)
    print_debug(ndep_crit_dep_tot,"The total critical N deposition for the N deposition criterion is")
    ndep_crit_dep_agri = ascraster.duplicategrid(ndep_crit_dep_tot)
    ndep_crit_dep_agri.multiply(fagri)
    print_debug(ndep_crit_dep_agri,"The critical N deposition on agricultural land for the N deposition criterion is")
    
    # calculate total critical N inputs wrt N deposition
    nin_crit_dep_agri = ascraster.duplicategrid(nman_crit_dep)
    nin_crit_dep_agri.add(nfert_crit_dep)
    nin_crit_dep_agri.add(ndep_crit_dep_agri)
    nin_crit_dep_agri.add(n_fix_agri)
    fileout = os.path.join(params.outputdir,"nin_crit_dep_agri.asc")
    nin_crit_dep_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nin_crit_dep_agri,"The total critical input to agriclture for the N deposition criterion is")
    
    # calculate N surface runoff at critical N inputs deposition
    nsro_crit_dep_agri = ascraster.duplicategrid(nin_crit_dep_agri)
    nsro_crit_dep_agri.multiply(fsro_ag)
    print_debug(nsro_crit_dep_agri,"The critical N surface runoff for the N deposition criterion is")
    
    # calculate N uptake at critical N inputs deposition
    nup_crit_dep_agri = ascraster.duplicategrid(nin_crit_dep_agri)
    nup_crit_dep_agri.substract(nsro_crit_dep_agri)
    nup_crit_dep_agri.multiply(frnup_agri)
    fileout = os.path.join(params.outputdir,"nup_crit_dep_agri.asc")
    nup_crit_dep_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nup_crit_dep_agri,"The N uptake for the N deposition criterion is")
        
    # calculate implied NUE
    nue_crit_dep_agri = ascraster.duplicategrid(nup_crit_dep_agri)
    nue_crit_dep_agri.divide(nin_crit_dep_agri, default_nodata_value = -9999)
    #fileout = os.path.join(params.outputdir,"nue_crit_dep_agri.asc")
    #nue_crit_dep_agri.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_dep_agri,"The NUE for the N deposition criterion is")
    
    # calculate maximum uptake fraction
    fnup_max_dep = ascraster.duplicategrid(n_up_max)
    fnup_max_dep.divide(nup_crit_dep_agri)
    fileout = os.path.join(params.outputdir,"fnup_max_dep.asc")
    fnup_max_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_max_dep,"The fraction maximum uptake / critical uptake for deposition is")
    
    # calculate correction factor for those cases where critical N uptake exceeds max. N uptake 
    fnup_corr_dep = ascraster.duplicategrid(n_in_max)
    fnup_corr_dep.substract(n_fix_agri)
    
    temp2 = ascraster.duplicategrid(nh3_tot_egl)
    temp2.add(nox_em)
    temp2.multiply(fagri)
    fnup_corr_dep.substract(temp2)
    
    temp3 = ascraster.duplicategrid(nh3em_crit_dep)
    temp3.multiply(fagri)
    temp3.add(nman_crit_dep)
    temp3.add(nfert_crit_dep)
    fnup_corr_dep.divide(temp3, default_nodata_value = -9999)
    
    fileout = os.path.join(params.outputdir,"fnup_corr_dep.asc")
    fnup_corr_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnup_corr_dep,"The correction factor for cases where Nup,crit>Nup,max is")
    
    
    ########### FORWARD CALCULATIONS TO CHECK ###########
    if icell_debug<0:
        pass
    else:
        fw = ndep_crit_dep_tot.get_data(icell_debug)
        bw = ndep_crit_tot.get_data(icell_debug)
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