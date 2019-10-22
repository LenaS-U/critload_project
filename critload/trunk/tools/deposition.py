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
    biome            = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"gnlct.asc"),numtype=float,mask=params.mask)
    a_tot            = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"a_tot.asc"),numtype=float,mask=params.mask)
    nox_em           = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc"),numtype=float,mask=params.mask)
    nh3_tot_egl      = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_tot_egl.asc"),numtype=float,mask=params.mask)
    nh3_ef_man_agri  = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man_agri.asc"),numtype=float,mask=params.mask)
    nh3_ef_fert_agri = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert_agri.asc"),numtype=float,mask=params.mask)
    frnfe_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe_agri.asc"),numtype=float,mask=params.mask)
    fagri            = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fagri.asc"),numtype=float,mask=params.mask)
    n_fix_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"n_fix_agri.asc"),numtype=float,mask=params.mask)
    fsro_ag          = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fsro_ag.asc"),numtype=float,mask=params.mask)
    frnup_agri       = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnup_agri.asc"),numtype=float,mask=params.mask)
        
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
        # Tundra (8) or wooded tundra (9)
        elif (val == 8 or val == 9):
            cl = 10.0
        # Temperate mixed forest (12) Temperate deciduous forest (13) or Warm mixed forest (14)
        elif (val == 12 or val == 13 or val == 14):
            cl = 12.5
        # Savanna (18)
        elif (val == 18):
            cl = 15.0
        # Grassland/steppe (15)
        elif (val == 15):
            cl = 17.5                    
        # Tropical woodland (19)
        elif (val == 19):
            cl = 19.5       
        # Tropical forest (20)
        elif (val == 20):
            cl = 25.0
        # Biome can also have value 0 or none (-1)
        else:
            continue        
        ndep_crit_ha.set_data(icell,cl) 
    
    print_debug(biome,"The biome ID is") 
    
    #fileout = os.path.join(params.outputdir,"ndep_crit_ha.asc")
    #ndep_crit_ha.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
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
    nh3em_fert_crit_dep = ascraster.duplicategrid(nfert_crit_dep)
    nh3em_fert_crit_dep.multiply(nh3_ef_fert_agri)
    nh3em_tot_crit_dep = ascraster.duplicategrid(nh3em_fert_crit_dep)
    nh3em_tot_crit_dep.add(nh3em_man_crit_dep)
    nh3em_tot_crit_dep.add(nh3_tot_egl)
    nem_tot_crit_dep = ascraster.duplicategrid(nh3em_tot_crit_dep)
    nem_tot_crit_dep.add(nox_em)
    ndep_tot_crit_dep = ascraster.duplicategrid(nem_tot_crit_dep)
    print_debug(ndep_tot_crit_dep,"The total critical N deposition for the N deposition criterion is")
    ndep_ag_crit_dep = ascraster.duplicategrid(ndep_tot_crit_dep)
    ndep_ag_crit_dep.multiply(fagri)
    print_debug(ndep_ag_crit_dep,"The critical N deposition on agricultural land for the N deposition criterion is")
    
    # calculate total critical N inputs wrt N deposition
    nin_tot_crit_dep = ascraster.duplicategrid(nman_crit_dep)
    nin_tot_crit_dep.add(nfert_crit_dep)
    nin_tot_crit_dep.add(ndep_ag_crit_dep)
    nin_tot_crit_dep.add(n_fix_agri)
    print_debug(nin_tot_crit_dep,"The total critical input for the N deposition criterion is")
    
    # calculate N surface runoff at critical N inputs deposition
    nsro_ag_crit_dep = ascraster.duplicategrid(nin_tot_crit_dep)
    nsro_ag_crit_dep.multiply(fsro_ag)
    print_debug(nsro_ag_crit_dep,"The critical N surface runoff for the N deposition criterion is")
    
    # calculate N uptake at critical N inputs deposition
    nup_ag_crit_dep = ascraster.duplicategrid(nin_tot_crit_dep)
    nup_ag_crit_dep.substract(nsro_ag_crit_dep)
    nup_ag_crit_dep.multiply(frnup_agri)
    print_debug(nup_ag_crit_dep,"The N uptake for the N deposition criterion is")
        
    # calculate implied NUE
    nue_crit_dep = ascraster.duplicategrid(nup_ag_crit_dep)
    nue_crit_dep.divide(nin_tot_crit_dep, default_nodata_value = -9999)
    #fileout = os.path.join(params.outputdir,"nue_crit_dep.asc")
    #nue_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_dep,"The NUE for the N deposition criterion is")
    
    ########### FORWARD CALCULATIONS TO CHECK ###########
    if icell_debug<0:
        pass
    else:
        fw = ndep_tot_crit_dep.get_data(icell_debug)
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