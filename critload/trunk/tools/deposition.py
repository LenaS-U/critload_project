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

    print("The critical N deposition rate is " + str(params.crit_dep) + " kg N ha-1 yr-1")
    
    # calculate total critical deposition: Ndep,tot(crit) = Ndep,crit,ha * A
    a_tot = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"a_tot.asc"),numtype=float,mask=params.mask)
    ndep_crit_tot = ascraster.duplicategrid(a_tot)
    ndep_crit_tot.multiply(params.crit_dep)
    print_debug(ndep_crit_tot,"The total critical N deposition is")
    
   
    # calculate critical N input from manure
    
    nox_em = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nox_em.asc"),numtype=float,mask=params.mask)
    nh3_ef_man = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_man.asc"),numtype=float,mask=params.mask)
    nh3_ef_fert = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"nh3_ef_fert.asc"),numtype=float,mask=params.mask)
    frnfe = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"frnfe.asc"),numtype=float,mask=params.mask)
    
    numerator = ascraster.duplicategrid(ndep_crit_tot)
    numerator.substract(nox_em)
    
    one_grid = ascraster.duplicategrid(frnfe)
    for i in range(one_grid.length):
        one_grid.set_data(i,1.0)
        
    one_min_frnfe = ascraster.duplicategrid(one_grid)
    one_min_frnfe.substract(frnfe)
    frnfe_division = ascraster.duplicategrid(frnfe)
    frnfe_division.divide(one_min_frnfe, default_nodata_value = -9999)
    
    denominator = ascraster.duplicategrid(frnfe_division)
    denominator.multiply(nh3_ef_fert)
    denominator.add(nh3_ef_man)
 
    nman_crit_dep = ascraster.duplicategrid(numerator)
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
    fag = ascraster.Asciigrid(ascii_file=os.path.join(params.outputdir,"fag.asc"),numtype=float,mask=params.mask)
    nh3em_man_crit_dep = ascraster.duplicategrid(nman_crit_dep)
    nh3em_man_crit_dep.multiply(nh3_ef_man)
    nh3em_fert_crit_dep = ascraster.duplicategrid(nfert_crit_dep)
    nh3em_fert_crit_dep.multiply(nh3_ef_fert)
    nh3em_tot_crit_dep = ascraster.duplicategrid(nh3em_fert_crit_dep)
    nh3em_tot_crit_dep.add(nh3em_man_crit_dep)
    nem_tot_crit_dep = ascraster.duplicategrid(nh3em_tot_crit_dep)
    nem_tot_crit_dep.add(nox_em)
    ndep_tot_crit_dep = ascraster.duplicategrid(nem_tot_crit_dep)
    print_debug(ndep_tot_crit_dep,"The total critical N deposition for the N deposition criterion is")
    ndep_ag_crit_dep = ascraster.duplicategrid(ndep_tot_crit_dep)
    ndep_ag_crit_dep.multiply(fag)
    print_debug(ndep_ag_crit_dep,"The critical N deposition on agricultural land for the N deposition criterion is")
    
    # calculate total critical N inputs wrt N deposition
    nfix_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"nfix_ag.asc"),numtype=float,mask=params.mask)
    nin_tot_crit_dep = ascraster.duplicategrid(nman_crit_dep)
    nin_tot_crit_dep.add(nfert_crit_dep)

    nin_tot_crit_dep.add(ndep_ag_crit_dep)
    nin_tot_crit_dep.add(nfix_ag)
    print_debug(nin_tot_crit_dep,"The total critical input for the N deposition criterion is")
    
    # calculate implied NUE
    nup_ag = ascraster.Asciigrid(ascii_file=os.path.join(params.inputdir,"n_up_ag.asc"),numtype=float,mask=params.mask)
    nue_crit_dep = ascraster.duplicategrid(nup_ag)
    nue_crit_dep.divide(nin_tot_crit_dep, default_nodata_value = -9999)
    fileout = os.path.join(params.outputdir,"nue_crit_dep.asc")
    nue_crit_dep.write_ascii_file(fileout,output_nodata_value=-9999,compress=params.lcompress)
    print_debug(nue_crit_dep,"The implied NUE for the N deposition criterion is")
    
    
    # TEST IF FORWARD CALCULATIONS EQUAL BACKWARD CALLCULATION
    # This does not work in the real case.....      
    #bw = round(ndep_crit_tot.get_data(3),4)
    #fw = round(ndep_tot_crit_dep.get_data(3),4)
    
    #if bw == fw:
    #    print("Comparison of backward and forward calculation was SUCCESFUL")
    #else:
    #    print("ATTENTION!!! Comparison of backward and forward calculation NOT successful") 
