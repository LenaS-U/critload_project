# ******************************************************
## Revision "$LastChangedDate: 2019-03-14 08:53:42 +0100 (Thu, 14 Mar 2019) $"
## Date "$LastChangedRevision: 625 $"
## Author "$LastChangedBy: arthurbeusen $"
## URL "$HeadURL: http://pbl.sliksvn.com/globalnutrients/critload/trunk/tools/temp_values.py $"
## Copyright 2019, PBL Netherlands Environmental Assessment Agency and Wageningen University.
## Reuse permitted under Gnu Public License, GPL v3.
# ******************************************************

# Python modules
import os

# Generalcode modules
import ascraster

# Local modules
from print_debug import *

def griddivide(grid1,grid2,default_nodata_value = 0):
    '''
    Calculate result of grid1/grid2 
    '''
    # Make a copy of the first grid.
    grid3 = ascraster.duplicategrid(grid1)

    for icell in range(grid3.length):
        # Get values from both grids.
        val1 = grid1.get_data(icell)
        val2 = grid2.get_data(icell)

        # If both grids have nodata, keep nodata.
        if (val1 == None or val2 == None):
            continue
        # Do the calculation
        try:
            val3 = val1/val2
        except (ZeroDivisionError,TypeError):
            val3 = default_nodata_value
        
        # Put result in grid.
        grid3.set_data(icell,val3)

    return grid3
    
def temp_values(params):
    
    # calculate fag   
    a_tot = ascraster.Asciigrid(ascii_file=params.filename_gridcell_area,numtype=float,mask=params.mask)
    a_ag = ascraster.Asciigrid(ascii_file=params.filename_agri_area,numtype=float,mask=params.mask)
    fag = ascraster.duplicategrid(a_ag)
    fag.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fag.asc")
    fag.write_ascii_file(fileout, output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fag,"fag =")

    # calculate fland
    a_nat = ascraster.Asciigrid(ascii_file=params.filename_natural_area,numtype=float,mask=params.mask)
    fland = ascraster.duplicategrid(a_ag)
    fland.add(a_nat)
    fland.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fland.asc")
    fland.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(a_ag,"fland =")
    
    # calculate fnat
    fnat = ascraster.duplicategrid(a_nat)
    fnat.divide(a_tot, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"fnat.asc")
    fnat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fnat,"fnat =")

    # calculate frNfe
    n_fert = ascraster.Asciigrid(ascii_file=params.filename_fert_inp,numtype=float,mask=params.mask)
    n_man = ascraster.Asciigrid(ascii_file=params.filename_manure_inp,numtype=float,mask=params.mask)
    fert_man = ascraster.duplicategrid(n_man)
    fert_man.add(n_fert)
    #frnfe = ascraster.duplicategrid(n_fert)
    #frnfe.divide(fert_man, default_nodata_value = -9999, minimum=0.00001, maximum=0.9999)
    frnfe = griddivide(n_fert,fert_man,default_nodata_value = 0)
    
    # replace '0' by 0.0001 in frNfe
    for icell in range(frnfe.length):
        val = frnfe.get_data(icell)
        if (val == None or val > 0):
            continue
        if val == 0.0:
            res = 0.0001
        frnfe.set_data(icell,res) 
    
    # replace '1' by 0.9999 in frNfe
    for icell in range(frnfe.length):
        val = frnfe.get_data(icell)
        if (val == None or val < 1):
            continue
        if val == 1.0:
            res = 0.9999
        frnfe.set_data(icell,res) 
    
    print_debug(frnfe,"frNfe =")
    fileout = os.path.join(params.outputdir,"frnfe.asc")
    frnfe.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)

    # calculate total NH3 emission
    nh3_spread_man = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_manure,numtype=float,mask=params.mask)
    nh3_stor = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_storage,numtype=float,mask=params.mask)
    nh3_graz = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_grazing,numtype=float,mask=params.mask)
    nh3_spread_fert = ascraster.Asciigrid(ascii_file=params.filename_nh3_em_spread_fert,numtype=float,mask=params.mask)
    nh3_tot = ascraster.duplicategrid(nh3_spread_man)
    nh3_tot.add(nh3_stor)
    nh3_tot.add(nh3_graz)
    nh3_tot.add(nh3_spread_fert)
    print_debug(nh3_tot,"nh3_tot =")
    
    # calculate corrected N deposition grid - for all cells where Ndep < NH3em, replace Ndep by NH3em
    ndep_tot = ascraster.Asciigrid(ascii_file=params.filename_n_deposition,numtype=float,mask=params.mask)
    ndep_tot_corr = ascraster.duplicategrid(ndep_tot)
    for icell in range(nh3_tot.length):
        # Get values from both grids.
        nh3 =  nh3_tot.get_data(icell)
        dep = ndep_tot.get_data(icell)
    
        # If both grids have nodata, keep nodata.
        if (nh3 == None or dep == None or dep >= nh3):
            continue
        if dep < nh3:
            depcorr = nh3
        ndep_tot_corr.set_data(icell,depcorr)
    fileout = os.path.join(params.outputdir,"ndep_tot_corr.asc")
    ndep_tot_corr.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)    
    print_debug(ndep_tot,"ndep_tot =")
    print_debug(ndep_tot_corr,"ndep_tot_corr =")

    # calculate ndep_ag
    ndep_ag = ascraster.duplicategrid(ndep_tot_corr)
    ndep_ag.multiply(fag)
    fileout = os.path.join(params.outputdir,"ndep_ag.asc")
    ndep_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_ag,"ndep_ag =")
    
    # calculate n_in_ag
    nfix_ag = ascraster.Asciigrid(ascii_file=params.filename_nfixation_agri,numtype=float,mask=params.mask)
    n_in_ag = ascraster.duplicategrid(fert_man)
    n_in_ag.add(nfix_ag)
    n_in_ag.add(ndep_ag)
    fileout = os.path.join(params.outputdir,"n_in_ag.asc")
    n_in_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(n_in_ag,"n_in_ag =")
    
    # calculate frnup
    nsro_ag = ascraster.Asciigrid(ascii_file=params.filename_nsro_ag,numtype=float,mask=params.mask)
    n_up = ascraster.Asciigrid(ascii_file=params.filename_crop_uptake,numtype=float,mask=params.mask)
    nin_min_nsro = ascraster.duplicategrid(n_in_ag)
    nin_min_nsro.substract(nsro_ag)
    frnup = ascraster.duplicategrid(n_up)
    frnup.divide(nin_min_nsro, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"frnup.asc")
    frnup.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(frnup,"frnup =")
    
    # calculate NUE
    nue = ascraster.duplicategrid(n_up)
    nue.divide(n_in_ag, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue.asc")
    nue.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue,"nue =")
    
    # calculate fnh3em,man
    nh3_man_tot = ascraster.duplicategrid(nh3_tot)
    nh3_man_tot.substract(nh3_spread_fert)
    #nh3_ef_man = ascraster.duplicategrid(nh3_man_tot)
    #nh3_ef_man.divide(n_man, default_nodata_value = -9999)
    nh3_ef_man = griddivide(nh3_man_tot,n_man,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_man.asc")
    nh3_ef_man.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_man,"nh3_ef_man =")
    
    # calculate fnh3em,fert
    #nh3_ef_fert = ascraster.duplicategrid(nh3_spread_fert)
    #nh3_ef_fert.divide(n_fert, default_nodata_value = -9999)
    nh3_ef_fert = griddivide(nh3_spread_fert,n_fert,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"nh3_ef_fert.asc")
    nh3_ef_fert.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nh3_ef_fert,"nh3_ef_fert =")
    
    # calculate NOx emissions: NOx = *corrected* Ndep - (NH3,spread,fe+NH3,spread,man+NH3stor+NH3,graz)
    nox_em = ascraster.duplicategrid(ndep_tot_corr)
    nox_em.substract(nh3_tot)
    fileout = os.path.join(params.outputdir,"nox_em.asc")
    nox_em.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nox_em,"nox_em =")    
    
    # calculate N budget agriculture: Nbud,ag = Nin,ag - Nup,ag
    nbud_ag = ascraster.duplicategrid(n_in_ag)
    nbud_ag.substract(n_up)
    fileout = os.path.join(params.outputdir,"nbud_ag.asc")
    nbud_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nbud_ag,"nbud_ag =")
    
    # calculate N load to surface water via groundwater due to *recent* N inputs: agriculture
    ngw_ag = ascraster.Asciigrid(ascii_file=params.filename_groundwaterload_ag,numtype=float,mask=params.mask)
    fgw_rec_ag = ascraster.Asciigrid(ascii_file=params.filename_fraction_recent_groundwaterload_ag,numtype=float,mask=params.mask)
    ngw_ag_rec = ascraster.duplicategrid(ngw_ag)
    ngw_ag_rec.multiply(fgw_rec_ag)
    fileout = os.path.join(params.outputdir,"ngw_ag_rec.asc")
    ngw_ag_rec.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ngw_ag_rec,"ngw_ag_rec =")
    
    # calculate Denitrification in soil: Nde,ag = Nbud,ag - Nsro,ag - Nle,ag
    nle_ag = ascraster.Asciigrid(ascii_file=params.filename_leaching_ag,numtype=float,mask=params.mask)
    nde_ag = ascraster.duplicategrid(nbud_ag)
    nde_ag.substract(nsro_ag)
    nde_ag.substract(nle_ag)
    fileout = os.path.join(params.outputdir,"nde_ag.asc")
    nde_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nde_ag,"nde_ag =")
        
    # calculate leaching fraction fle,ag
    nbud_min_nsro_ag = ascraster.duplicategrid(nbud_ag)
    nbud_min_nsro_ag.substract(nsro_ag)
    #fle_ag = ascraster.duplicategrid(nle_ag)
    #fle_ag.divide(nbud_min_nsro_ag, default_nodata_value = -9999)
    fle_ag = griddivide(nle_ag,nbud_min_nsro_ag,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fle_ag.asc")
    fle_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fle_ag,"fle_ag =")   
    
    # calculate runoff fraction fsro,ag
    #fsro_ag = ascraster.duplicategrid(nsro_ag)
    #fsro_ag.divide(n_in_ag, default_nodata_value = -9999)
    fsro_ag = griddivide(nsro_ag,n_in_ag,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fsro_ag.asc")
    fsro_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fsro_ag,"fsro_ag =")   
    
    # calculate fraction of N leaching that is delivered to surface water via groundwater in first x years
    #fgw_rec_le_ag = ascraster.duplicategrid(ngw_ag_rec)
    #fgw_rec_le_ag.divide(nle_ag, default_nodata_value = -9999)
    fgw_rec_le_ag = griddivide(ngw_ag_rec,nle_ag,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fgw_rec_le_ag.asc")
    fgw_rec_le_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fgw_rec_le_ag,"fgw_rec_le_ag =")
    
    # calculate ndep_nat
    ndep_nat = ascraster.duplicategrid(ndep_tot_corr)
    ndep_nat.multiply(fnat)
    fileout = os.path.join(params.outputdir,"ndep_nat.asc")
    ndep_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ndep_nat,"ndep_nat =")

    # calculate N budget nature: Nbud,nat = Ndep,nat + Nfix,nat
    nfix_nat = ascraster.Asciigrid(ascii_file=params.filename_nfixation_nat,numtype=float,mask=params.mask)
    nbud_nat = ascraster.duplicategrid(ndep_nat)
    nbud_nat.add(nfix_nat)
    fileout = os.path.join(params.outputdir,"nbud_nat.asc")
    nbud_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nbud_nat,"nbud_nat =")
    
    # calculate N load to surface water via groundwater due to *recent* N inputs: natural areas
    ngw_nat = ascraster.Asciigrid(ascii_file=params.filename_groundwaterload_nat,numtype=float,mask=params.mask)
    fgw_rec_nat = ascraster.Asciigrid(ascii_file=params.filename_fraction_recent_groundwaterload_nat,numtype=float,mask=params.mask)
    ngw_nat_rec = ascraster.duplicategrid(ngw_nat)
    ngw_nat_rec.multiply(fgw_rec_nat)
    fileout = os.path.join(params.outputdir,"ngw_nat_rec.asc")
    ngw_nat_rec.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(ngw_nat_rec,"ngw_nat_rec =")
    
    # calculate Denitrification in soil: Nde,nat = Nbud,nat - Nsro,nat - Nle,nat
    nsro_nat = ascraster.Asciigrid(ascii_file=params.filename_nsro_nat,numtype=float,mask=params.mask)
    nle_nat = ascraster.Asciigrid(ascii_file=params.filename_leaching_nat,numtype=float,mask=params.mask)
    nde_nat = ascraster.duplicategrid(nbud_nat)
    nde_nat.substract(nsro_nat)
    nde_nat.substract(nle_nat)
    fileout = os.path.join(params.outputdir,"nde_nat.asc")
    nde_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nde_nat,"nde_nat =")
        
    # calculate leaching fraction fle,nat
    nbud_min_nsro_nat = ascraster.duplicategrid(nbud_nat)
    nbud_min_nsro_nat.substract(nsro_nat)
    #fle_nat = ascraster.duplicategrid(nle_nat)
    #fle_nat.divide(nbud_min_nsro_nat, default_nodata_value = -9999)
    fle_nat = griddivide(nle_nat,nbud_min_nsro_nat,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fle_nat.asc")
    fle_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fle_nat,"fle_nat =")   
    
    # calculate runoff fraction fsro,nat
    #fsro_nat = ascraster.duplicategrid(nsro_nat)
    #fsro_nat.divide(nbud_nat, default_nodata_value = -9999)
    fsro_nat = griddivide(nsro_nat,nbud_nat,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fsro_nat.asc")
    fsro_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fsro_nat,"fsro_nat =")   
    
    # calculate fraction of N leaching that is delivered to surface water via groundwater in first x years - natural areas
    #fgw_rec_le_nat = ascraster.duplicategrid(ngw_nat_rec)
    #fgw_rec_le_nat.divide(nle_nat, default_nodata_value = -9999)
    fgw_rec_le_nat = griddivide(ngw_nat_rec,nle_nat,default_nodata_value = 0)
    fileout = os.path.join(params.outputdir,"fgw_rec_le_nat.asc")
    fgw_rec_le_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(fgw_rec_le_nat,"fgw_rec_le_nat =")
    
    # calculate variable load to surface water from agriculture: Nload,var,ag = Nsro,ag + Ngw,rec,ag
    nload_var_ag = ascraster.duplicategrid(ngw_ag_rec)
    nload_var_ag.add(nsro_ag)
    fileout = os.path.join(params.outputdir,"nload_var_ag.asc")
    nload_var_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_var_ag,"nload_var_ag =")
    
    # calculate variable load to surface water from nature: Nload,var,nat = Nsro,nat + Ngw,rec,nat
    nload_var_nat = ascraster.duplicategrid(ngw_nat_rec)
    nload_var_nat.add(nsro_nat)
    fileout = os.path.join(params.outputdir,"nload_var_nat.asc")
    nload_var_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_var_nat,"nload_var_nat =")   

    # calculate fixed load to surface water from agriculture: Ngw,fixed,ag = Ngw,ag * (1-fgw,rec,ag)
    grid1 = ascraster.duplicategrid(fgw_rec_ag)
    for i in range(grid1.length):
        grid1.set_data(i,1.0)
    grid1.substract(fgw_rec_ag)
    nload_fixed_ag = ascraster.duplicategrid(ngw_ag)
    nload_fixed_ag.multiply(grid1)
    fileout = os.path.join(params.outputdir,"nload_fixed_ag.asc")
    nload_fixed_ag.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_fixed_ag,"nload_fixed_ag =")   
    
    # calculate fixed load to surface water from nature: Ngw,fixed,nat = Ngw,nat * (1-fgw,rec,nat)
    grid1 = ascraster.duplicategrid(fgw_rec_nat)
    for i in range(grid1.length):
        grid1.set_data(i,1.0)
    grid1.substract(fgw_rec_nat)
    nload_fixed_nat = ascraster.duplicategrid(ngw_nat)
    nload_fixed_nat.multiply(grid1)
    fileout = os.path.join(params.outputdir,"nload_fixed_nat.asc")
    nload_fixed_nat.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_fixed_nat,"nload_fixed_nat =")    

    # calculate total load from point sources
    nallo = ascraster.Asciigrid(ascii_file=params.filename_n_point_alloch_matter,numtype=float,mask=params.mask)
    nww = ascraster.Asciigrid(ascii_file=params.filename_n_point_wastewater,numtype=float,mask=params.mask)
    naqua = ascraster.Asciigrid(ascii_file=params.filename_n_point_aquaculture,numtype=float,mask=params.mask)
    ndep_sw = ascraster.Asciigrid(ascii_file=params.filename_n_point_dep_surfacewater,numtype=float,mask=params.mask)
    npoint_tot = ascraster.duplicategrid(nallo)
    npoint_tot.add(nww)
    npoint_tot.add(naqua)
    npoint_tot.add(ndep_sw)
    fileout = os.path.join(params.outputdir,"npoint_tot.asc")
    npoint_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(npoint_tot,"npoint_tot =") 
    
    # calculate total load from erosion
    nero_ag = ascraster.Asciigrid(ascii_file=params.filename_n_in_erosion_ag,numtype=float,mask=params.mask)
    nero_nat = ascraster.Asciigrid(ascii_file=params.filename_n_in_erosion_nat,numtype=float,mask=params.mask)
    nero_tot = ascraster.duplicategrid(nero_ag)
    nero_tot.add(nero_nat)
    fileout = os.path.join(params.outputdir,"nero_tot.asc")
    nero_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nero_tot,"nero_tot =")    
    
    # calculate total n load to surface water: Nload,tot = Nload,var,ag + Nload,var,nat + Ngw,fixed,ag + Ngw,fixed,nat + Npoint + Nero
    nload_tot = ascraster.duplicategrid(nload_var_ag)
    nload_tot.add(nload_var_nat)
    nload_tot.add(nload_fixed_ag)
    nload_tot.add(nload_fixed_nat)
    nload_tot.add(npoint_tot)
    nload_tot.add(nero_tot)
    fileout = os.path.join(params.outputdir,"nload_tot.asc")
    nload_tot.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nload_tot,"nload_tot =")        
    
