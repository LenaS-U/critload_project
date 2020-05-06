import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

#ToC
# 1. Read files from input / output directory and replace NA values by NaN
### 1a. Read files from *OUTPUT* directory
### 1b. Read files from *INPUT* directory
### 1c. change NA values to NaN
# 2. Calculate CURRENT inputs from manure and fertilizer per hectare for each grid cell
### 2a. all agricultural land ('manha', 'ferha', 'manfer', 'manferha')
### 2b. cropland (..._ara)
### 2c. intensive grassland (..._igl)
### 2d. cropland + intensive grassland (..._araigl)
# 3. Calculate CURRENT inputs from deposition due to NOx and NH3_egl for each grid cell (for _ara, _igl, _egl, _agri, _ag)
# 4. Calculate maximum inputs from fertilizer and manure, and sum of the two for each grid cell
# 5. Calculate CRITICAL inputs from manure and fertilizer per hectare for each grid cell
# 6. Calculate areas for different cases
# 7. Print land areas + actual N inputs
### 7a. Areas
### 7b. Actual N inputs (totals)
### 7c. Actual N inputs (per hectare)
# 8. Critical N inputs for cut-off at actual N inputs
### 8a. copy original critical N inputs

#######################################################################################################################################################################################################    
# 1. Read files from input / output directory and replace NA values by NaN ############################################################################################################################
#######################################################################################################################################################################################################

### 1a. Read files from *OUTPUT* directory
os.chdir('c:\\users')
os.chdir('schul028')
os.chdir('OneDrive - WageningenUR')
os.chdir('critload_project')
os.chdir('Model Version1.4')
os.chdir('trunk')
os.chdir('output')
os.chdir('2010')

mancritsw        = np.loadtxt("nman_crit_sw.asc"         , skiprows=6)
fercritsw        = np.loadtxt("nfert_crit_sw.asc"        , skiprows=6)
mancritgw        = np.loadtxt("nman_crit_gw.asc"         , skiprows=6)
fercritgw        = np.loadtxt("nfert_crit_gw.asc"        , skiprows=6)
mancritde        = np.loadtxt("nman_crit_dep.asc"        , skiprows=6)
fercritde        = np.loadtxt("nfert_crit_dep.asc"       , skiprows=6)
frnfe_agri       = np.loadtxt("frnfe_agri.asc"           , skiprows=6)
nup_max          = np.loadtxt("n_up_max.asc"             , skiprows=6)
nup_crit_sw      = np.loadtxt("nup_crit_sw_agri.asc"     , skiprows=6)
nup_crit_gw      = np.loadtxt("nup_crit_gw_agri.asc"     , skiprows=6)
nup_crit_dep     = np.loadtxt("nup_crit_dep_agri.asc"    , skiprows=6)
fnup_max_sw      = np.loadtxt("fnup_max_sw.asc"          , skiprows=6)
fnup_max_gw      = np.loadtxt("fnup_max_gw.asc"          , skiprows=6)
fnup_max_de      = np.loadtxt("fnup_max_dep.asc"         , skiprows=6)
fnup_corr_sw     = np.loadtxt("fnup_corr_sw.asc"         , skiprows=6)
fnup_corr_gw     = np.loadtxt("fnup_corr_gw.asc"         , skiprows=6)
fnup_corr_de     = np.loadtxt("fnup_corr_dep.asc"        , skiprows=6)
nue_agri         = np.loadtxt("nue_agri.asc"             , skiprows=6)
nox_em           = np.loadtxt("nox_em.asc"               , skiprows=6)
nh3_tot_egl      = np.loadtxt("nh3_tot_egl.asc"          , skiprows=6)
fag              = np.loadtxt("fag.asc"                  , skiprows=6)
fara             = np.loadtxt("fara.asc"                 , skiprows=6)
figl             = np.loadtxt("figl.asc"                 , skiprows=6)
fegl             = np.loadtxt("fegl.asc"                 , skiprows=6)
fagri            = np.loadtxt("fagri.asc"                , skiprows=6)
nh3_ef_man       = np.loadtxt("nh3_ef_man_agri.asc"      , skiprows=6)
nh3_ef_fer       = np.loadtxt("nh3_ef_fert_agri.asc"     , skiprows=6)
nin_max          = np.loadtxt("n_in_max.asc"             , skiprows=6)
nin_tot_crit_sw     = np.loadtxt("nin_crit_sw_agri.asc"      , skiprows=6)
nin_tot_crit_gw     = np.loadtxt("nin_crit_gw_agri.asc"      , skiprows=6)
nin_tot_crit_dep    = np.loadtxt("nin_crit_dep_agri.asc"     , skiprows=6)
nh3em_crit_dep   = np.loadtxt("nh3em_crit_dep.asc"       , skiprows=6)
nh3em_crit_sw    = np.loadtxt("nh3em_crit_sw.asc"        , skiprows=6)
nh3em_crit_gw    = np.loadtxt("nh3em_crit_gw.asc"        , skiprows=6)
nh3_stor_egl     = np.loadtxt("nh3_stor_egl.asc"          , skiprows=6)
nh3_stor_igl     = np.loadtxt("nh3_stor_igl.asc"          , skiprows=6)
nh3_stor_ara     = np.loadtxt("nh3_stor_ara.asc"          , skiprows=6)

### 1b. Read files from *INPUT* directory
os.chdir('c:\\users')
os.chdir('schul028')
os.chdir('OneDrive - WageningenUR')
os.chdir('critload_project')
os.chdir('Model Version1.4')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

agarea        = np.loadtxt("a_ag.asc"                     , skiprows=6)
area_ara      = np.loadtxt("a_crop.asc"                   , skiprows=6)
area_igl      = np.loadtxt("a_gr_int.asc"                 , skiprows=6)
area_egl      = np.loadtxt("a_gr_ext.asc"                 , skiprows=6) 
nfer          = np.loadtxt("n_fe_eff.asc"                 , skiprows=6)
nfer_ara      = np.loadtxt("n_fe_eff_crop.asc"            , skiprows=6)
nfer_igl      = np.loadtxt("n_fe_eff_grass.asc"           , skiprows=6)
nman          = np.loadtxt("n_man_eff.asc"                , skiprows=6)
nman_ara      = np.loadtxt("n_man_eff_crops.asc"          , skiprows=6)
nman_igl      = np.loadtxt("n_man_eff_grass_int.asc"      , skiprows=6)
nman_egl      = np.loadtxt("n_man_eff_grass_ext.asc"      , skiprows=6)
nfix          = np.loadtxt("nfix_ag.asc"                  , skiprows=6)
nfix_ara      = np.loadtxt("nfix_crop.asc"                , skiprows=6)
nfix_igl      = np.loadtxt("nfix_grass_int.asc"           , skiprows=6)
nfix_egl      = np.loadtxt("nfix_grass_ext.asc"           , skiprows=6)
fgwrecag      = np.loadtxt("fgw_rec_ag.asc"               , skiprows=6)
fgwrecna      = np.loadtxt("fgw_rec_nat.asc"              , skiprows=6)
ndep          = np.loadtxt("ndep.asc"                     , skiprows=6)
nh3emfert     = np.loadtxt("nh3_spread_fe.asc"            , skiprows=6)
nh3emfert_ara = np.loadtxt("nh3_spread_fe_crops.asc"      , skiprows=6)
nh3emfert_igl = np.loadtxt("nh3_spread_fe_grass_int.asc"  , skiprows=6)
nh3emappl     = np.loadtxt("nh3_spread_man.asc"           , skiprows=6)
nh3emappl_ara = np.loadtxt("nh3_spread_man_crops.asc"     , skiprows=6)
nh3emappl_igl = np.loadtxt("nh3_spread_man_grass_int.asc" , skiprows=6)
nh3emstor     = np.loadtxt("nh3_stor.asc"                 , skiprows=6)
nh3emgraz     = np.loadtxt("nh3_graz.asc"                 , skiprows=6)
nh3emgraz_igl = np.loadtxt("nh3_graz_int.asc"             , skiprows=6)
regions       = np.loadtxt("image_region28.asc"           , skiprows=6)

### 1c. change NA values to NaN

mancritsw[mancritsw==-9999]               =np.nan 
fercritsw[fercritsw==-9999]               =np.nan
mancritgw[mancritgw==-9999]               =np.nan
fercritgw[fercritgw==-9999]               =np.nan
mancritde[mancritde==-9999]               =np.nan
fercritde[fercritde==-9999]               =np.nan
frnfe_agri[frnfe_agri==-9999]             =np.nan
nup_max[nup_max==-9999]                   =np.nan
nup_crit_sw[nup_crit_sw==-9999]           =np.nan
nup_crit_gw[nup_crit_gw==-9999]           =np.nan
nup_crit_dep[nup_crit_dep==-9999]         =np.nan
fnup_max_sw[fnup_max_sw==-9999]           =np.nan
fnup_max_gw[fnup_max_gw==-9999]           =np.nan
fnup_max_de[fnup_max_de==-9999]           =np.nan
fnup_corr_sw[fnup_corr_sw==-9999]         =np.nan
fnup_corr_gw[fnup_corr_gw==-9999]         =np.nan
fnup_corr_de[fnup_corr_de==-9999]         =np.nan
nue_agri[nue_agri==-9999]                 =np.nan
nox_em[nox_em==-9999]                     =np.nan
nh3_tot_egl[nh3_tot_egl==-9999]           =np.nan
fag[fag==-1]                              =np.nan
fara[fara==-1]                            =np.nan
figl[figl==-1]                            =np.nan
fegl[fegl==-1]                            =np.nan
fagri[fagri==-1]                          =np.nan
nh3_ef_man[nh3_ef_man==-9999]             =np.nan
nh3_ef_fer[nh3_ef_fer==-9999]             =np.nan
nin_max[nin_max==-9999]                   =np.nan
nin_tot_crit_sw[nin_tot_crit_sw==-9999]   =np.nan
nin_tot_crit_gw[nin_tot_crit_gw==-9999]   =np.nan
nin_tot_crit_dep[nin_tot_crit_dep==-9999] =np.nan
nh3em_crit_dep[nh3em_crit_dep==-9999]     =np.nan
nh3em_crit_sw[nh3em_crit_sw==-9999]       =np.nan
nh3em_crit_gw[nh3em_crit_gw==-9999]       =np.nan
nh3_stor_egl[nh3_stor_egl==-9999]         =np.nan
nh3_stor_igl[nh3_stor_igl==-9999]         =np.nan
nh3_stor_ara[nh3_stor_ara==-9999]         =np.nan

agarea[agarea==-1]                    =np.nan
area_ara[area_ara==-1]                =np.nan
area_igl[area_igl==-1]                =np.nan
area_egl[area_egl==-1]                =np.nan
nfer[nfer==-9999]                     =np.nan
nfer_ara[nfer_ara==-9999]             =np.nan
nfer_igl[nfer_igl==-9999]             =np.nan
nman[nman==-9999]                     =np.nan
nman_ara[nman_ara==-9999]             =np.nan
nman_igl[nman_igl==-9999]             =np.nan
nman_egl[nman_egl==-9999]             =np.nan
nfix[nfix==-9999]                     =np.nan
nfix_ara[nfix_ara==-9999]             =np.nan
nfix_igl[nfix_igl==-9999]             =np.nan
nfix_egl[nfix_egl==-9999]             =np.nan
fgwrecag[fgwrecag==-9999]             =np.nan
fgwrecna[fgwrecna==-9999]             =np.nan
ndep[ndep==-1]                        =np.nan
nh3emfert[nh3emfert==-9999]           =np.nan
nh3emfert_ara[nh3emfert_ara==-9999]   =np.nan
nh3emfert_igl[nh3emfert_igl==-9999]   =np.nan
nh3emappl[nh3emappl==-9999]           =np.nan
nh3emappl_ara[nh3emappl_ara==-9999]   =np.nan
nh3emappl_igl[nh3emappl_igl==-9999]   =np.nan
nh3emstor[nh3emstor==-9999]           =np.nan
nh3emgraz[nh3emgraz==-9999]           =np.nan
nh3emgraz_igl[nh3emgraz_igl==-9999]   =np.nan
regions[regions==-9999]               =np.nan

#######################################################################################################################################################################################################
# 2. Calculate CURRENT inputs from manure and fertilizer per hectare for each grid cell ###############################################################################################################
#######################################################################################################################################################################################################
with np.errstate(invalid='ignore'):
### 2a. all agricultural land
    manha         = np.divide(nman, agarea)
    ferha         = np.divide(nfer, agarea)
    manfer        = np.add(nman, nfer)
    manferha      = np.divide(manfer, agarea)
### 2b. cropland
    manha_ara     = np.divide(nman_ara, area_ara)
    ferha_ara     = np.divide(nfer_ara, area_ara)
    manfer_ara    = np.add(nman_ara, nfer_ara)
    manferha_ara  = np.divide(manfer_ara, area_ara)
### 2c. intensive + extensive grassland
    ferha_igl     = np.divide(nfer_igl, area_igl)
    manha_igl     = np.divide(nman_igl, area_igl)
    manha_egl     = np.divide(nman_egl, area_egl)
    manfer_igl    = np.add(nman_igl, nfer_igl)
    manferha_igl  = np.divide(manfer_igl, area_igl)
### 2d. cropland + intensive grassland
    fer_araigl      = np.add(nfer_ara, nfer_igl)
    man_araigl      = np.add(nman_ara, nman_igl)
    manfer_araigl   = np.add(fer_araigl,man_araigl)
    
    area_araigl     = np.add(area_ara, area_igl)
    ferha_araigl    = np.divide(fer_araigl, area_araigl)
    manha_araigl    = np.divide(man_araigl, area_araigl)
    manferha_araigl = np.divide(manfer_araigl, area_araigl)

    #$# add nh3 emissions #$#V1.2#$# #$#V1.4#$#
    fer_araigl = np.add(fer_araigl, nh3emfert_ara)  #$#V1.2#$# #$#V1.4#$#
    fer_araigl = np.add(fer_araigl, nh3emfert_igl)  #$#V1.2#$# #$#V1.4#$#
    man_araigl = np.add(man_araigl, nh3emappl_ara)  #$#V1.2#$# #$#V1.4#$#
    man_araigl = np.add(man_araigl, nh3emappl_igl)  #$#V1.2#$# #$#V1.4#$#
    man_araigl = np.add(man_araigl, nh3_stor_ara)      #$#V1.2#$# #$#V1.4#$#
    man_araigl = np.add(man_araigl, nh3_stor_igl)      #$#V1.2#$# #$#V1.4#$#
    man_araigl = np.add(man_araigl, nh3emgraz_igl)  #$#V1.2#$# #$#V1.4#$#
    manfer_araigl = np.add(fer_araigl, man_araigl)  #$#V1.2#$# #$#V1.4#$#
   


#######################################################################################################################################################################################################
# 3. Calculate CURRENT inputs from deposition due to NOx and NH3_egl for each grid cell ###############################################################################################################
#######################################################################################################################################################################################################
ndep_fixed      = np.add(nox_em, nh3_tot_egl)
ndep_fixed_ara  = np.multiply(ndep_fixed, fara)
ndep_fixed_igl  = np.multiply(ndep_fixed, figl)
ndep_fixed_egl  = np.multiply(ndep_fixed, fegl)
ndep_fixed_agri = np.multiply(ndep_fixed, fagri)
ndep_fixed_ag   = np.multiply(ndep_fixed, fag)

#######################################################################################################################################################################################################
# 4. Calculate maximum inputs from fertilizer and manure, and sum of the two for each grid cell #######################################################################################################
#######################################################################################################################################################################################################
print("nin_crit_max_1:  %i kg N yr-1" %(np.nansum(nin_max)))
# surface water
mancritsw_max = np.multiply(mancritsw, fnup_corr_sw) 
fercritsw_max = np.multiply(fercritsw, fnup_corr_sw) 
manfercritsw_max = np.add(mancritsw_max, fercritsw_max)
# groundwater
mancritgw_max = np.multiply(mancritgw, fnup_corr_gw) 
fercritgw_max = np.multiply(fercritgw, fnup_corr_gw) 
manfercritgw_max = np.add(mancritgw_max, fercritgw_max)
# deposition
mancritde_max = np.multiply(mancritde, fnup_corr_de) 
fercritde_max = np.multiply(fercritde, fnup_corr_de) 
manfercritde_max = np.add(mancritde_max, fercritde_max)

'''
#$*$*$*$*$*$*$*$*
# TEST to see if total nin_crit_max is correct - WORKS!
# gw
nh3mancritgwagri_max = np.multiply(mancritgw_max, nh3_ef_man)
nh3fercritgwagri_max = np.multiply(fercritgw_max, nh3_ef_fer)
nh3manfercritgwagri_max = np.add(nh3mancritgwagri_max, nh3fercritgwagri_max)
ndep_var_agrigw_max = np.multiply(nh3manfercritgwagri_max, fagri)
nin_crit_max_gw = np.add(manfercritgw_max, nfix_ara)
nin_crit_max_gw = np.add(nin_crit_max_gw, nfix_igl)
nin_crit_max_gw = np.add(nin_crit_max_gw, ndep_fixed_agri)
nin_crit_max_gw = np.add(nin_crit_max_gw, ndep_var_agrigw_max)
# In grid cells where you DO have agri-area and N fixation, but no inputs from either fertilizer or manure, there is an N_in_max, but no critical inputs are calculated because frnfe = NA (n=11) 
# Also, for groundwater there are the cells where fle=0 and thus there is no critical input calculated
print("nin_crit_max_1_gw: %i kg N yr-1" %(np.nansum(nin_max[np.where(np.isnan(mancritgw)==False)])))
print("nin_crit_max_gw:  %i kg N yr-1" %(np.nansum(nin_crit_max_gw)))

#sw
nh3mancritswagri_max = np.multiply(mancritsw_max, nh3_ef_man)
nh3fercritswagri_max = np.multiply(fercritsw_max, nh3_ef_fer)
nh3manfercritswagri_max = np.add(nh3mancritswagri_max, nh3fercritswagri_max)
ndep_var_agrisw_max = np.multiply(nh3manfercritswagri_max, fagri)
nin_crit_max_sw = np.add(manfercritsw_max, nfix_ara)
nin_crit_max_sw = np.add(nin_crit_max_sw, nfix_igl)
nin_crit_max_sw = np.add(nin_crit_max_sw, ndep_fixed_agri)
nin_crit_max_sw = np.add(nin_crit_max_sw, ndep_var_agrisw_max)
print("nin_crit_max_1_sw: %i kg N yr-1" %(np.nansum(nin_max[np.where(np.isnan(mancritsw)==False)])))
print("nin_crit_max_sw:  %i kg N yr-1" %(np.nansum(nin_crit_max_sw)))

#dep
nh3mancritdeagri_max = np.multiply(mancritde_max, nh3_ef_man)
nh3fercritdeagri_max = np.multiply(fercritde_max, nh3_ef_fer)
nh3manfercritdeagri_max = np.add(nh3mancritdeagri_max, nh3fercritdeagri_max)
ndep_var_agride_max = np.multiply(nh3manfercritdeagri_max, fagri)
nin_crit_max_de = np.add(manfercritsw_max, nfix_ara)
nin_crit_max_de = np.add(nin_crit_max_de, nfix_igl)
nin_crit_max_de = np.add(nin_crit_max_de, ndep_fixed_agri)
nin_crit_max_de = np.add(nin_crit_max_de, ndep_var_agride_max)
print("nin_crit_max_1_de: %i kg N yr-1" %(np.nansum(nin_max[np.where(np.isnan(mancritde)==False)])))
print("nin_crit_max_de:  %i kg N yr-1" %(np.nansum(nin_crit_max_de)))

#$*$*$*$*$*$*$*$*
'''

#######################################################################################################################################################################################################
# 5. Calculate CRITICAL inputs from manure and fertilizer per hectare for each grid cell ##############################################################################################################
#######################################################################################################################################################################################################
# fertilizer
fercritswha = np.divide(fercritsw, area_araigl)
fercritgwha = np.divide(fercritgw, area_araigl)
fercritdeha = np.divide(fercritde, area_araigl)
# manure
mancritswha = np.divide(mancritsw, area_araigl)
mancritgwha = np.divide(mancritgw, area_araigl)
mancritdeha = np.divide(mancritde, area_araigl)
# fertilizer+manure
manfercritsw = np.add(mancritsw,fercritsw)
manfercritgw = np.add(mancritgw,fercritgw)
manfercritde = np.add(mancritde,fercritde)

manfercritswha = np.divide(manfercritsw, area_araigl)
manfercritgwha = np.divide(manfercritgw, area_araigl)
manfercritdeha = np.divide(manfercritde, area_araigl)
#$*$*$*$*$*$*$*$* NO LONGER NEEDED?
# -> it is possible (8684 times) that mancritsw/mancritgw <> NA but area_araigl = 0. In those cases, I want to get a na.
#mancritswha[np.isinf(mancritswha)]       = np.nan
#fercritswha[np.isinf(fercritswha)]       = np.nan
#mancritgwha[np.isinf(mancritgwha)]       = np.nan
#fercritgwha[np.isinf(fercritgwha)]       = np.nan
#manfercritswha[np.isinf(manfercritswha)] = np.nan
#manfercritgwha[np.isinf(manfercritgwha)] = np.nan
#$*$*$*$*$*$*$*$*

#######################################################################################################################################################################################################
# 6. Calculate areas for different cases ##############################################################################################################################################################
#######################################################################################################################################################################################################
print("CASES")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(area_araigl))
    print("case-1-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, manfercritsw<=0)) ]))
    print("case-3-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw>0,manfercritsw<=manfer_araigl))) ]))
    print("case-4-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw>manfer_araigl,manfercritsw<=manfercritsw_max))) ]))
    print("case-5-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw>manfer_araigl,manfercritsw>manfercritsw_max))) ]))
  
    print("case-1-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, manfercritgw<=0)) ]))
    print("case-3-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw>0,manfercritgw<=manfer_araigl))) ]))
    print("case-4-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw>manfer_araigl,manfercritgw<=manfercritgw_max))) ]))
    print("case-5-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw>manfer_araigl,manfercritgw>manfercritgw_max))) ]))
    
    print("case-1-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, manfercritde<=0)) ]))
    print("case-3-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde>0,manfercritde<=manfer_araigl))) ]))
    print("case-4-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde>manfer_araigl,manfercritde<=manfercritde_max))) ]))
    print("case-5-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde>manfer_araigl,manfercritde>manfercritde_max))) ]))

    # new version - after we set nman_crit to zero in model
    manfercritmiX = np.minimum(manfercritsw, manfercritgw)
    manfercritmi  = np.minimum(manfercritmiX, manfercritde)
    print("case-1-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmi)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmi)==False, manfercritmi<=0)) ]))
    print("case-3-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmi)==False, np.logical_and(manfercritmi>0,manfercritmi<=manfer_araigl))) ]))
    print("case-4-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmi)==False, np.logical_and(manfercritmi>manfer_araigl,manfercritmi<=manfercritde_max))) ]))
    print("case-5-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmi)==False, np.logical_and(manfercritmi>manfer_araigl,manfercritmi>manfercritde_max))) ]))


''' #old version: before we set nman_crit to zero in model    
    print("case-1-mi-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-mi-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw<manfercritgw, np.logical_and(manfercritsw<manfercritde, manfercritsw<=0)))) ]))
    print("case-3-mi-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw<manfercritgw, np.logical_and(manfercritsw<manfercritde, np.logical_and(manfercritsw>0,manfercritsw<=manfer_araigl))))) ]))
    print("case-4-mi-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw<manfercritgw, np.logical_and(manfercritsw<manfercritde, np.logical_and(manfercritsw>manfer_araigl,manfercritsw<=manfercritsw_max))))) ]))
    print("case-5-mi-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw<manfercritgw, np.logical_and(manfercritsw<manfercritde, np.logical_and(manfercritsw>manfer_araigl,manfercritsw>manfercritsw_max))))) ]))
    
    print("case-1-mi-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-mi-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw<manfercritsw, np.logical_and(manfercritgw<manfercritde, manfercritgw<=0)))) ]))
    print("case-3-mi-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw<manfercritsw, np.logical_and(manfercritgw<manfercritde, np.logical_and(manfercritgw>0,manfercritgw<=manfer_araigl))))) ]))
    print("case-4-mi-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw<manfercritsw, np.logical_and(manfercritgw<manfercritde, np.logical_and(manfercritgw>manfer_araigl,manfercritgw<=manfercritgw_max))))) ]))
    print("case-5-mi-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw<manfercritsw, np.logical_and(manfercritgw<manfercritde, np.logical_and(manfercritgw>manfer_araigl,manfercritgw>manfercritgw_max))))) ]))

    print("case-1-mi-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-mi-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde<manfercritsw, np.logical_and(manfercritde<manfercritgw, manfercritde<=0)))) ]))
    print("case-3-mi-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde<manfercritsw, np.logical_and(manfercritde<manfercritgw, np.logical_and(manfercritde>0,manfercritde<=manfer_araigl))))) ]))
    print("case-4-mi-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde<manfercritsw, np.logical_and(manfercritde<manfercritgw, np.logical_and(manfercritde>manfer_araigl,manfercritde<=manfercritde_max))))) ]))
    print("case-5-mi-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde<manfercritsw, np.logical_and(manfercritde<manfercritgw, np.logical_and(manfercritde>manfer_araigl,manfercritde>manfercritde_max))))) ]))
       
    #NOT NEEDED: critical N inputs for different criteria are never the same in a grid cell
    #print("not-cons-1: %i" % np.nansum(area_araigl[np.where(np.logical_and(manfercritsw<manfercritgw, manfercritsw==manfercritde))])) # sw AND de kleinste
    #print("not-cons-2: %i" % np.nansum(area_araigl[np.where(np.logical_and(manfercritsw<manfercritde, manfercritsw==manfercritgw))])) # sw AND gw kleinste
    #print("not-cons-3: %i" % np.nansum(area_araigl[np.where(np.logical_and(manfercritgw<manfercritsw, manfercritgw==manfercritde))])) # gw AND de kleinste
    #print("not-cons-4: %i" % np.nansum(area_araigl[np.where(np.logical_and(manfercritgw==manfercritsw, manfercritgw==manfercritde))])) # allemaal kleinste
'''

#######################################################################################################################################################################################################
# 7. Print land areas + actual N inputs from fertilizer and manure ####################################################################################################################################
#######################################################################################################################################################################################################

### 7a. Areas
print("AREAS-PER-LAND-USE")
print("ag:       %i ha" %(np.nansum(agarea)))
print("ara:      %i ha" %(np.nansum(area_ara)))
print("igl:      %i ha" %(np.nansum(area_igl)))
print("egl:      %i ha" %(np.nansum(area_egl)))
print("ara-igl:  %i ha" %(np.nansum(area_araigl)))
### 7b. Actual N inputs (totals)
print("TOTAL-ACTUAL-INPUTS")
print("Act-fer-tot-all:  %i kgNyr-1" %(np.nansum(nfer)))
print("Act-fer-tot-ara:  %i kgNyr-1" %(np.nansum(nfer_ara)))
print("Act-fer-tot-igl:  %i kgNyr-1" %(np.nansum(nfer_igl)))
print("Act-fer-tot-egl:  %i kgNyr-1" % 0.0)
print("Act-man-tot-all:  %i kgNyr-1" %(np.nansum(nman)))
print("Act-man-tot-ara:  %i kgNyr-1" %(np.nansum(nman_ara)))
print("Act-man-tot-igl:  %i kgNyr-1" %(np.nansum(nman_igl)))
print("Act-man-tot-egl:  %i kgNyr-1" %(np.nansum(nman_egl)))
### 7c. Actual N inputs (per hectare)
print("ACTUAL-INPUTS-PER-HA")
print("Act-fer-ha-all:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer), np.nansum(agarea[np.where(np.isnan(nfer)==False)])))
print("Act-fer-ha-ara:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_ara), np.nansum(area_ara[np.where(np.isnan(nfer_ara)==False)])))
print("Act-fer-ha-igl:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_igl), np.nansum(area_igl[np.where(np.isnan(nfer_igl)==False)])))
print("Act-fer-ha-egl:        %.1f kgNha-1yr-1" % 0.0)
print("Act-fer-ha-araigl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(fer_araigl), np.nansum(area_araigl[np.where(np.isnan(fer_araigl)==False)])))
print("Act-man-ha-all:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman), np.nansum(agarea[np.where(np.isnan(nman)==False)])))
print("Act-man-ha-ara:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_ara), np.nansum(area_ara[np.where(np.isnan(nman_ara)==False)])))
print("Act-man-ha-igl:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_igl), np.nansum(area_igl[np.where(np.isnan(nman_igl)==False)])))
print("Act-man-ha-egl:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_egl), np.nansum(area_egl[np.where(np.isnan(nman_egl)==False)])))
print("Act-man-ha-araigl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(man_araigl), np.nansum(area_araigl[np.where(np.isnan(man_araigl)==False)])))
print("Act-fer-man-ha-all:    %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer), np.nansum(agarea[np.where(np.isnan(manfer)==False)])))
print("Act-fer-man-ha-ara:    %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_ara), np.nansum(area_ara[np.where(np.isnan(manfer_ara)==False)])))
print("Act-fer-man-ha-igl:    %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_igl), np.nansum(area_igl[np.where(np.isnan(manfer_igl)==False)])))
print("Act-fer-man-ha-egl:    %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_egl), np.nansum(area_egl[np.where(np.isnan(nman_egl)==False)])))
print("Act-fer-man-ha-araigl: %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_araigl), np.nansum(area_araigl[np.where(np.isnan(manfer_araigl)==False)])))

#######################################################################################################################################################################################################
# 8. Critical N inputs for cut-off at actual N inputs #################################################################################################################################################
#######################################################################################################################################################################################################
### 8a. copy original critical N inputs
fercritsw2    = np.copy(fercritsw)
mancritsw2    = np.copy(mancritsw)
fercritgw2    = np.copy(fercritgw)
mancritgw2    = np.copy(mancritgw)
fercritde2    = np.copy(fercritde)
mancritde2    = np.copy(mancritde)
manfercritsw2 = np.copy(manfercritsw)
manfercritgw2 = np.copy(manfercritgw)
manfercritde2 = np.copy(manfercritde)

### 8b. replace negative values by zero
with np.errstate(invalid='ignore'):
    fercritsw2[fercritsw2<0]=0
    mancritsw2[mancritsw2<0]=0
    fercritgw2[fercritgw2<0]=0
    mancritgw2[mancritgw2<0]=0
    fercritde2[fercritde2<0]=0
    mancritde2[mancritde2<0]=0
    manfercritsw2[manfercritsw2<0]=0
    manfercritgw2[manfercritgw2<0]=0
    manfercritde2[manfercritde2<0]=0

# 1c. replace Nin,crit larger than actual by actual
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fer_araigl)[0]):
        for j in range(np.shape(fer_araigl)[1]):
            if fercritsw2[i,j] > fer_araigl[i,j]:
                fercritsw2[i,j] = fer_araigl[i,j]
            if mancritsw2[i,j] > man_araigl[i,j]:
                mancritsw2[i,j] = man_araigl[i,j]
            if fercritgw2[i,j] > fer_araigl[i,j]:
                fercritgw2[i,j] = fer_araigl[i,j]
            if mancritgw2[i,j] > man_araigl[i,j]:
                mancritgw2[i,j] = man_araigl[i,j]
            if fercritde2[i,j] > fer_araigl[i,j]:
                fercritde2[i,j] = fer_araigl[i,j]
            if mancritde2[i,j] > man_araigl[i,j]:
                mancritde2[i,j] = man_araigl[i,j]            
            if fercritsw2[i,j] > fer_araigl[i,j]:
                fercritsw2[i,j] = fer_araigl[i,j]
            if manfercritsw2[i,j] > manfer_araigl[i,j]:
                manfercritsw2[i,j] = manfer_araigl[i,j]
            if manfercritgw2[i,j] > manfer_araigl[i,j]:
                manfercritgw2[i,j] = manfer_araigl[i,j]
            if manfercritde2[i,j] > manfer_araigl[i,j]:
                manfercritde2[i,j] = manfer_araigl[i,j]

# 1d. select minimum of critical N inputs for all criteria
fercritmin2X    = np.minimum(fercritsw2, fercritgw2)
fercritmin2     = np.minimum(fercritmin2X, fercritde2)
mancritmin2X    = np.minimum(mancritsw2, mancritgw2)
mancritmin2     = np.minimum(mancritmin2X, mancritde2)
manfercritmin2X = np.minimum(manfercritsw2, manfercritgw2)
manfercritmin2  = np.minimum(manfercritmin2X, manfercritde2)

#fercritmin2 = np.copy(fercritsw2)
#    for i in range(np.shape(fercritsw2)[0]):
#        for j in range(np.shape(fercritsw2)[1]):
#            if (fercritsw2[i,j] <= fercritgw2[i,j] and fercritsw2[i,j] <= fercritde2[i,j]):
#                fercritsw2[i,j] = fercritsw2[i,j]]
#            if (fercritgw2[i,j] <= fercritsw2[i,j] and fercritgw2[i,j] <= fercritde2[i,j]):
#                fercritsw2[i,j] = fercritgw2[i,j]]                
#            if (fercritde2[i,j] <= fercritsw2[i,j] and fercritde2[i,j] <= fercritgw2[i,j]):
#                fercritsw2[i,j] = fercritde2[i,j]]    
  
print("Crit-fer-sw-ha-2a: %.1f" % np.divide(np.nansum(fercritsw2),     np.nansum(area_araigl[np.where(np.isnan(fercritsw2)    ==False)])))
print("Crit-man-sw-ha-2a: %.1f" % np.divide(np.nansum(mancritsw2),     np.nansum(area_araigl[np.where(np.isnan(mancritsw2)    ==False)])))
print("Crit-fer-gw-ha-2a: %.1f" % np.divide(np.nansum(fercritgw2),     np.nansum(area_araigl[np.where(np.isnan(fercritgw2)    ==False)])))
print("Crit-man-gw-ha-2a: %.1f" % np.divide(np.nansum(mancritgw2),     np.nansum(area_araigl[np.where(np.isnan(mancritgw2)    ==False)])))
print("Crit-fer-de-ha-2a: %.1f" % np.divide(np.nansum(fercritde2),     np.nansum(area_araigl[np.where(np.isnan(fercritde2)    ==False)])))
print("Crit-man-de-ha-2a: %.1f" % np.divide(np.nansum(mancritde2),     np.nansum(area_araigl[np.where(np.isnan(mancritde2)    ==False)])))
print("Crit-nin-sw-ha-2a: %.1f" % np.divide(np.nansum(manfercritsw2),  np.nansum(area_araigl[np.where(np.isnan(manfercritsw2) ==False)])))
print("Crit-nin-gw-ha-2a: %.1f" % np.divide(np.nansum(manfercritgw2),  np.nansum(area_araigl[np.where(np.isnan(manfercritgw2) ==False)]))) 
print("Crit-nin-de-ha-2a: %.1f" % np.divide(np.nansum(manfercritde2),  np.nansum(area_araigl[np.where(np.isnan(manfercritde2) ==False)])))
print("Crit-fer-mi-ha-2a: %.1f" % np.divide(np.nansum(fercritmin2),    np.nansum(area_araigl[np.where(np.isnan(fercritmin2)   ==False)])))
print("Crit-man-mi-ha-2a: %.1f" % np.divide(np.nansum(mancritmin2),    np.nansum(area_araigl[np.where(np.isnan(mancritmin2)   ==False)])))
print("Crit-nin-mi-ha-2a: %.1f" % np.divide(np.nansum(manfercritmin2), np.nansum(area_araigl[np.where(np.isnan(manfercritmin2)==False)])))

with np.errstate(invalid='ignore'):
    print("Crit-fer-sw-ha-2b: %.1f" % np.divide(np.nansum(fercritsw2),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritsw2)    ==False, fercritsw2>0))])))
    print("Crit-man-sw-ha-2b: %.1f" % np.divide(np.nansum(mancritsw2),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritsw2)    ==False, mancritsw2>0))])))
    print("Crit-fer-gw-ha-2b: %.1f" % np.divide(np.nansum(fercritgw2),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritgw2)    ==False, fercritgw2>0))])))
    print("Crit-man-gw-ha-2b: %.1f" % np.divide(np.nansum(mancritgw2),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritgw2)    ==False, mancritgw2>0))])))
    print("Crit-fer-de-ha-2b: %.1f" % np.divide(np.nansum(fercritde2),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritde2)    ==False, fercritde2>0))])))
    print("Crit-man-de-ha-2b: %.1f" % np.divide(np.nansum(mancritde2),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritde2)    ==False, mancritde2>0))])))
    print("Crit-nin-sw-ha-2b: %.1f" % np.divide(np.nansum(manfercritsw2),  np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw2) ==False, manfercritsw2>0))])))
    print("Crit-nin-gw-ha-2b: %.1f" % np.divide(np.nansum(manfercritgw2),  np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw2) ==False, manfercritgw2>0))]))) 
    print("Crit-nin-de-ha-2b: %.1f" % np.divide(np.nansum(manfercritde2),  np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde2) ==False, manfercritde2>0))])))
    print("Crit-fer-mi-ha-2b: %.1f" % np.divide(np.nansum(fercritmin2),    np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritmin2)==False, fercritmin2>0))])))
    print("Crit-man-mi-ha-2b: %.1f" % np.divide(np.nansum(mancritmin2),    np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritmin2)==False, mancritmin2>0))])))
    print("Crit-nin-mi-ha-2b: %.1f" % np.divide(np.nansum(manfercritmin2), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin2)==False, manfercritmin2>0))])))

# Add N inputs to extensive grasslands to totals
manfercritsw2egl  = np.add(manfercritsw2, nman_egl)
manfercritgw2egl  = np.add(manfercritgw2, nman_egl)
manfercritde2egl  = np.add(manfercritde2, nman_egl)
manfercritmin2egl = np.add(manfercritmin2, nman_egl)

print("Crit-nin-sw-ha-2a-egl: %.1f" % np.divide(np.nansum(manfercritsw2egl), np.nansum(agarea[np.where(np.isnan(manfercritsw2egl)==False)])))
print("Crit-nin-gw-ha-2a-egl: %.1f" % np.divide(np.nansum(manfercritgw2egl), np.nansum(agarea[np.where(np.isnan(manfercritgw2egl)==False)]))) 
print("Crit-nin-de-ha-2a-egl: %.1f" % np.divide(np.nansum(manfercritde2egl), np.nansum(agarea[np.where(np.isnan(manfercritde2egl)==False)])))
print("Crit-nin-mi-ha-2a-egl: %.1f" % np.divide(np.nansum(manfercritmin2egl), np.nansum(agarea[np.where(np.isnan(manfercritmin2egl)==False)])))

with np.errstate(invalid='ignore'):
    print("Crit-nin-sw-ha-2b-egl: %.1f" % np.divide(np.nansum(manfercritsw2egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritsw2egl)==False, manfercritsw2egl>0))])))
    print("Crit-nin-gw-ha-2b-egl: %.1f" % np.divide(np.nansum(manfercritgw2egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritgw2egl)==False, manfercritgw2egl>0))]))) 
    print("Crit-nin-de-ha-2b-egl: %.1f" % np.divide(np.nansum(manfercritde2egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritde2egl)==False, manfercritde2egl>0))])))
    print("Crit-nin-mi-ha-2b-egl: %.1f" % np.divide(np.nansum(manfercritmin2egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin2egl)==False, manfercritmin2egl>0))])))


# 2. for cut-off at maximum N input
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-NIN,MAX")
fercritsw3 = np.copy(fercritsw)
mancritsw3 = np.copy(mancritsw)
fercritgw3 = np.copy(fercritgw)
mancritgw3 = np.copy(mancritgw)
fercritde3 = np.copy(fercritde)
mancritde3 = np.copy(mancritde)
manfercritsw3 = np.copy(manfercritsw)
manfercritgw3 = np.copy(manfercritgw)
manfercritde3 = np.copy(manfercritde)

# replace negative values by zero
with np.errstate(invalid='ignore'):
    fercritsw3[fercritsw3<0]=0
    mancritsw3[mancritsw3<0]=0
    fercritgw3[fercritgw3<0]=0
    mancritgw3[mancritgw3<0]=0
    fercritde3[fercritde3<0]=0
    mancritde3[mancritde3<0]=0
    manfercritsw3[manfercritsw3<0]=0
    manfercritgw3[manfercritgw3<0]=0
    manfercritde3[manfercritde3<0]=0

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw)[0]):
        for j in range(np.shape(fnup_max_sw)[1]):
            if (fnup_max_sw[i,j] < 1 and np.isnan(fnup_max_sw[i,j])==False):
                fercritsw3[i,j] = fercritsw3[i,j]*fnup_corr_sw[i,j]
                mancritsw3[i,j] = mancritsw3[i,j]*fnup_corr_sw[i,j]
                manfercritsw3[i,j] = fercritsw3[i,j]+mancritsw3[i,j]       
    for i in range(np.shape(fnup_max_gw)[0]):
        for j in range(np.shape(fnup_max_gw)[1]):
            if (fnup_max_gw[i,j] < 1 and np.isnan(fnup_max_gw[i,j])==False):
                fercritgw3[i,j] = fercritgw3[i,j]*fnup_corr_gw[i,j]
                mancritgw3[i,j] = mancritgw3[i,j]*fnup_corr_gw[i,j]
                manfercritgw3[i,j] = fercritgw3[i,j]+mancritgw3[i,j] 
    for i in range(np.shape(fnup_max_de)[0]):
        for j in range(np.shape(fnup_max_de)[1]):
            if (fnup_max_de[i,j] < 1 and np.isnan(fnup_max_de[i,j])==False):
                fercritde3[i,j] = fercritde3[i,j]*fnup_corr_de[i,j]
                mancritde3[i,j] = mancritde3[i,j]*fnup_corr_de[i,j]
                manfercritde3[i,j] = fercritde3[i,j]+mancritde3[i,j] 

# select minimum
fercritmin3X    = np.minimum(fercritsw3, fercritgw3)
fercritmin3     = np.minimum(fercritmin3X, fercritde3)
mancritmin3X    = np.minimum(mancritsw3, mancritgw3)
mancritmin3     = np.minimum(mancritmin3X, mancritde3)
manfercritmin3X = np.minimum(manfercritsw3, manfercritgw3)
manfercritmin3  = np.minimum(manfercritmin3X, manfercritde3)

print("Crit-fer-sw-ha-3a: %.1f" % np.divide(np.nansum(fercritsw3),     np.nansum(area_araigl[np.where(np.isnan(fercritsw3)    ==False)])))
print("Crit-man-sw-ha-3a: %.1f" % np.divide(np.nansum(mancritsw3),     np.nansum(area_araigl[np.where(np.isnan(mancritsw3)    ==False)])))
print("Crit-fer-gw-ha-3a: %.1f" % np.divide(np.nansum(fercritgw3),     np.nansum(area_araigl[np.where(np.isnan(fercritgw3)    ==False)])))
print("Crit-man-gw-ha-3a: %.1f" % np.divide(np.nansum(mancritgw3),     np.nansum(area_araigl[np.where(np.isnan(mancritgw3)    ==False)])))
print("Crit-fer-de-ha-3a: %.1f" % np.divide(np.nansum(fercritde3),     np.nansum(area_araigl[np.where(np.isnan(fercritde3)    ==False)])))
print("Crit-man-de-ha-3a: %.1f" % np.divide(np.nansum(mancritde3),     np.nansum(area_araigl[np.where(np.isnan(mancritde3)    ==False)])))
print("Crit-nin-sw-ha-3a: %.1f" % np.divide(np.nansum(manfercritsw3),  np.nansum(area_araigl[np.where(np.isnan(manfercritsw3) ==False)])))
print("Crit-nin-gw-ha-3a: %.1f" % np.divide(np.nansum(manfercritgw3),  np.nansum(area_araigl[np.where(np.isnan(manfercritgw3) ==False)]))) 
print("Crit-nin-de-ha-3a: %.1f" % np.divide(np.nansum(manfercritde3),  np.nansum(area_araigl[np.where(np.isnan(manfercritde3) ==False)])))
print("Crit-fer-mi-ha-3a: %.1f" % np.divide(np.nansum(fercritmin3),    np.nansum(area_araigl[np.where(np.isnan(fercritmin3)   ==False)])))
print("Crit-man-mi-ha-3a: %.1f" % np.divide(np.nansum(mancritmin3),    np.nansum(area_araigl[np.where(np.isnan(mancritmin3)   ==False)])))
print("Crit-nin-mi-ha-3a: %.1f" % np.divide(np.nansum(manfercritmin3), np.nansum(area_araigl[np.where(np.isnan(manfercritmin3)==False)])))

with np.errstate(invalid='ignore'):
    print("Crit-fer-sw-ha-3b: %.1f" % np.divide(np.nansum(fercritsw3),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritsw3)    ==False, fercritsw3>0))])))
    print("Crit-man-sw-ha-3b: %.1f" % np.divide(np.nansum(mancritsw3),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritsw3)    ==False, mancritsw3>0))])))
    print("Crit-fer-gw-ha-3b: %.1f" % np.divide(np.nansum(fercritgw3),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritgw3)    ==False, fercritgw3>0))])))
    print("Crit-man-gw-ha-3b: %.1f" % np.divide(np.nansum(mancritgw3),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritgw3)    ==False, mancritgw3>0))])))
    print("Crit-fer-de-ha-3b: %.1f" % np.divide(np.nansum(fercritde3),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritde3)    ==False, fercritde3>0))])))
    print("Crit-man-de-ha-3b: %.1f" % np.divide(np.nansum(mancritde3),     np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritde3)    ==False, mancritde3>0))])))
    print("Crit-nin-sw-ha-3b: %.1f" % np.divide(np.nansum(manfercritsw3),  np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw3) ==False, manfercritsw3>0))])))
    print("Crit-nin-gw-ha-3b: %.1f" % np.divide(np.nansum(manfercritgw3),  np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw3) ==False, manfercritgw3>0))]))) 
    print("Crit-nin-de-ha-3b: %.1f" % np.divide(np.nansum(manfercritde3),  np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde3) ==False, manfercritde3>0))])))                
    print("Crit-fer-mi-ha-3b: %.1f" % np.divide(np.nansum(fercritmin3),    np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritmin3)   ==False, fercritmin3>0))])))
    print("Crit-man-mi-ha-3b: %.1f" % np.divide(np.nansum(mancritmin3),    np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritmin3)   ==False, mancritmin3>0))])))
    print("Crit-nin-mi-ha-3b: %.1f" % np.divide(np.nansum(manfercritmin3), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin3)==False, manfercritmin3>0))])))

# Add N inputs to extensive grasslands to totals
manfercritsw3egl  = np.add(manfercritsw3, nman_egl)
manfercritgw3egl  = np.add(manfercritgw3, nman_egl)
manfercritde3egl  = np.add(manfercritde3, nman_egl)
manfercritmin3egl = np.add(manfercritmin3, nman_egl)

print("Crit-nin-sw-ha-3a-egl: %.1f" % np.divide(np.nansum(manfercritsw3egl),  np.nansum(agarea[np.where(np.isnan(manfercritsw3egl) ==False)])))
print("Crit-nin-gw-ha-3a-egl: %.1f" % np.divide(np.nansum(manfercritgw3egl),  np.nansum(agarea[np.where(np.isnan(manfercritgw3egl) ==False)]))) 
print("Crit-nin-de-ha-3a-egl: %.1f" % np.divide(np.nansum(manfercritde3egl),  np.nansum(agarea[np.where(np.isnan(manfercritde3egl) ==False)])))
print("Crit-nin-mi-ha-3a-egl: %.1f" % np.divide(np.nansum(manfercritmin3egl), np.nansum(agarea[np.where(np.isnan(manfercritmin3egl)==False)])))

with np.errstate(invalid='ignore'):
    print("Crit-nin-sw-ha-3b-egl: %.1f" % np.divide(np.nansum(manfercritsw3egl),  np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritsw3egl) ==False, manfercritsw3egl>0))])))
    print("Crit-nin-gw-ha-3b-egl: %.1f" % np.divide(np.nansum(manfercritgw3egl),  np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritgw3egl) ==False, manfercritgw3egl>0))]))) 
    print("Crit-nin-de-ha-3b-egl: %.1f" % np.divide(np.nansum(manfercritde3egl),  np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritde3egl )==False, manfercritde3egl>0))])))
    print("Crit-nin-mi-ha-3b-egl: %.1f" % np.divide(np.nansum(manfercritmin3egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin3egl)==False, manfercritmin3egl>0))])))

# 3. for cut-off at maximum of 150 kg N ha-1 and current N input
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-MAX(150,ACT)")

manfercritsw4 = np.copy(manfercritsw)
manfercritgw4 = np.copy(manfercritgw)
manfercritde4 = np.copy(manfercritde)

# replace negative values by zero
with np.errstate(invalid='ignore'):
    manfercritsw4[manfercritsw4<0]=0
    manfercritgw4[manfercritgw4<0]=0
    manfercritde4[manfercritde4<0]=0

# calculate inputs per hectare
manfercritswha4 = np.divide(manfercritsw4, area_araigl)
manfercritgwha4 = np.divide(manfercritgw4, area_araigl)
manfercritdeha4 = np.divide(manfercritde4, area_araigl)

with np.errstate(invalid='ignore'):
    for i in range(np.shape(manferha_araigl)[0]):
        for j in range(np.shape(manferha_araigl)[1]):
            if (manfercritswha4[i,j] > manferha_araigl[i,j] and manfercritswha4[i,j] > 150):
                manfercritswha4[i,j] = max(manferha_araigl[i,j],150)
            if (manfercritgwha4[i,j] > manferha_araigl[i,j] and manfercritgwha4[i,j] > 150):
                manfercritgwha4[i,j] = max(manferha_araigl[i,j],150)
            if (manfercritdeha4[i,j] > manferha_araigl[i,j] and manfercritdeha4[i,j] > 150):
                manfercritdeha4[i,j] = max(manferha_araigl[i,j],150)
    
#Calculate totals
manfercritsw4 = np.multiply(manfercritswha4, area_araigl)
manfercritgw4 = np.multiply(manfercritgwha4, area_araigl)
manfercritde4 = np.multiply(manfercritdeha4, area_araigl)

# re-distribute over fertilizer and manure
with np.errstate(invalid='ignore'):
    fercritsw4 = np.multiply(manfercritsw4,     frnfe_agri)
    mancritsw4 = np.multiply(manfercritsw4, (1.-frnfe_agri))
    fercritgw4 = np.multiply(manfercritgw4,     frnfe_agri)
    mancritgw4 = np.multiply(manfercritgw4, (1.-frnfe_agri))
    fercritde4 = np.multiply(manfercritde4,     frnfe_agri)
    mancritde4 = np.multiply(manfercritde4, (1.-frnfe_agri))

# select minimum
fercritmin4X    = np.minimum(fercritsw4, fercritgw4)
fercritmin4     = np.minimum(fercritmin4X, fercritde4)
mancritmin4X    = np.minimum(mancritsw4, mancritgw4)
mancritmin4     = np.minimum(mancritmin4X, mancritde4)
manfercritmin4X = np.minimum(manfercritsw4, manfercritgw4)
manfercritmin4  = np.minimum(manfercritmin4X, manfercritde4)

print("Crit-fer-sw-ha-4a: %.1f" % np.divide(np.nansum(fercritsw4), np.nansum(area_araigl[np.where(np.isnan(fercritsw4)==False)])))
print("Crit-man-sw-ha-4a: %.1f" % np.divide(np.nansum(mancritsw4), np.nansum(area_araigl[np.where(np.isnan(mancritsw4)==False)])))
print("Crit-fer-gw-ha-4a: %.1f" % np.divide(np.nansum(fercritgw4), np.nansum(area_araigl[np.where(np.isnan(fercritgw4)==False)])))
print("Crit-man-gw-ha-4a: %.1f" % np.divide(np.nansum(mancritgw4), np.nansum(area_araigl[np.where(np.isnan(mancritgw4)==False)])))
print("Crit-fer-de-ha-4a: %.1f" % np.divide(np.nansum(fercritde4), np.nansum(area_araigl[np.where(np.isnan(fercritde4)==False)])))
print("Crit-man-de-ha-4a: %.1f" % np.divide(np.nansum(mancritde4), np.nansum(area_araigl[np.where(np.isnan(mancritde4)==False)])))
print("Crit-nin-sw-ha-4a: %.1f" % np.divide(np.nansum(manfercritsw4), np.nansum(area_araigl[np.where(np.isnan(manfercritsw4)==False)])))
print("Crit-nin-gw-ha-4a: %.1f" % np.divide(np.nansum(manfercritgw4), np.nansum(area_araigl[np.where(np.isnan(manfercritgw4)==False)]))) 
print("Crit-nin-de-ha-4a: %.1f" % np.divide(np.nansum(manfercritde4), np.nansum(area_araigl[np.where(np.isnan(manfercritde4)==False)])))
print("Crit-fer-mi-ha-4a: %.1f" % np.divide(np.nansum(fercritmin4), np.nansum(area_araigl[np.where(np.isnan(fercritmin4)==False)])))
print("Crit-man-mi-ha-4a: %.1f" % np.divide(np.nansum(mancritmin4), np.nansum(area_araigl[np.where(np.isnan(mancritmin4)==False)])))
print("Crit-nin-mi-ha-4a: %.1f" % np.divide(np.nansum(manfercritmin4), np.nansum(area_araigl[np.where(np.isnan(manfercritmin4)==False)])))

with np.errstate(invalid='ignore'):
    print("Crit-fer-sw-ha-4b: %.1f" % np.divide(np.nansum(fercritsw4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritsw4)==False, fercritsw4>0))])))
    print("Crit-man-sw-ha-4b: %.1f" % np.divide(np.nansum(mancritsw4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritsw4)==False, mancritsw4>0))])))
    print("Crit-fer-gw-ha-4b: %.1f" % np.divide(np.nansum(fercritgw4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritgw4)==False, fercritgw4>0))])))
    print("Crit-man-gw-ha-4b: %.1f" % np.divide(np.nansum(mancritgw4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritgw4)==False, mancritgw4>0))])))
    print("Crit-fer-de-ha-4b: %.1f" % np.divide(np.nansum(fercritde4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritde4)==False, fercritde4>0))])))
    print("Crit-man-de-ha-4b: %.1f" % np.divide(np.nansum(mancritde4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritde4)==False, mancritde4>0))])))
    print("Crit-nin-sw-ha-4b: %.1f" % np.divide(np.nansum(manfercritsw4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw4)==False, manfercritsw4>0))])))
    print("Crit-nin-gw-ha-4b: %.1f" % np.divide(np.nansum(manfercritgw4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw4)==False, manfercritgw4>0))]))) 
    print("Crit-nin-de-ha-4b: %.1f" % np.divide(np.nansum(manfercritde4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde4)==False, manfercritde4>0))])))                
    print("Crit-fer-mi-ha-4b: %.1f" % np.divide(np.nansum(fercritmin4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(fercritmin4)==False, fercritmin4>0))])))
    print("Crit-man-mi-ha-4b: %.1f" % np.divide(np.nansum(mancritmin4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(mancritmin4)==False, mancritmin4>0))])))
    print("Crit-nin-mi-ha-4b: %.1f" % np.divide(np.nansum(manfercritmin4), np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin4)==False, manfercritmin4>0))])))

# Add N inputs to extensive grasslands to totals
manfercritsw4egl  = np.add(manfercritsw4, nman_egl)
manfercritgw4egl  = np.add(manfercritgw4, nman_egl)
manfercritde4egl  = np.add(manfercritde4, nman_egl)
manfercritmin4egl = np.add(manfercritmin4, nman_egl)

print("Crit-nin-sw-ha-4a-egl: %.1f" % np.divide(np.nansum(manfercritsw4egl), np.nansum(agarea[np.where(np.isnan(manfercritsw4egl)==False)])))
print("Crit-nin-gw-ha-4a-egl: %.1f" % np.divide(np.nansum(manfercritgw4egl), np.nansum(agarea[np.where(np.isnan(manfercritgw4egl)==False)]))) 
print("Crit-nin-de-ha-4a-egl: %.1f" % np.divide(np.nansum(manfercritde4egl), np.nansum(agarea[np.where(np.isnan(manfercritde4egl)==False)])))
print("Crit-nin-mi-ha-4a-egl: %.1f" % np.divide(np.nansum(manfercritmin4egl), np.nansum(agarea[np.where(np.isnan(manfercritmin4egl)==False)])))

with np.errstate(invalid='ignore'):
    print("Crit-nin-sw-ha-4b-egl: %.1f" % np.divide(np.nansum(manfercritsw4egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritsw4egl)==False, manfercritsw4egl>0))])))
    print("Crit-nin-gw-ha-4b-egl: %.1f" % np.divide(np.nansum(manfercritgw4egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritgw4egl)==False, manfercritgw4egl>0))]))) 
    print("Crit-nin-de-ha-4b-egl: %.1f" % np.divide(np.nansum(manfercritde4egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritde4egl)==False, manfercritde4egl>0))])))
    print("Crit-nin-mi-ha-4b-egl: %.1f" % np.divide(np.nansum(manfercritmin4egl), np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin4egl)==False, manfercritmin4egl>0))])))


# add N fixation and N deposition to output
## actual N fixation
#totals
nfix_araigl = np.add(nfix_ara,nfix_igl)
print("Act-fix-tot-all:  %i kgNyr-1" %(np.nansum(nfix)))
print("Act-fix-tot-ara:  %i kgNyr-1" %(np.nansum(nfix_ara)))
print("Act-fix-tot-igl:  %i kgNyr-1" %(np.nansum(nfix_igl)))
print("Act-fix-tot-egl:  %i kgNyr-1" %(np.nansum(nfix_egl)))
print("Act-fix-tot-araigl:  %i kgNyr-1" %(np.nansum(nfix_araigl)))
# per ha
print("Act-fix-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix),     np.nansum(agarea[np.where(np.isnan(nfix)==False)])))
print("Act-fix-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_ara), np.nansum(area_ara[np.where(np.isnan(nfix_ara)==False)])))
print("Act-fix-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_igl), np.nansum(area_igl[np.where(np.isnan(nfix_igl)==False)])))
print("Act-fix-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_egl), np.nansum(area_egl[np.where(np.isnan(nfix_egl)==False)])))
print("Act-fix-ha-araigl:  %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_araigl), np.nansum(area_araigl[np.where(np.isnan(nfix_araigl)==False)])))
## actual N deposition from NOx emissions and NH3 from extensive grazing
#totals
ndep_fixed_araigl = np.add(ndep_fixed_ara,ndep_fixed_igl)
print("Act-dep-fixed-tot-all:  %i kgNyr-1" %(np.nansum(ndep_fixed_ag)))
print("Act-dep-fixed-tot-ara:  %i kgNyr-1" %(np.nansum(ndep_fixed_ara)))
print("Act-dep-fixed-tot-igl:  %i kgNyr-1" %(np.nansum(ndep_fixed_igl)))
print("Act-dep-fixed-tot-egl:  %i kgNyr-1" %(np.nansum(ndep_fixed_egl)))
print("Act-dep-fixed-tot-araigl:  %i kgNyr-1" %(np.nansum(ndep_fixed_araigl)))
# per ha
print("Act-dep-fixed-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_ag),  np.nansum(agarea[np.where(np.isnan(ndep_fixed_ag)==False)])))
print("Act-dep-fixed-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_ara), np.nansum(area_ara[np.where(np.isnan(ndep_fixed_ara)==False)])))
print("Act-dep-fixed-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_igl), np.nansum(area_igl[np.where(np.isnan(ndep_fixed_igl)==False)])))
print("Act-dep-fixed-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_egl), np.nansum(area_egl[np.where(np.isnan(ndep_fixed_egl)==False)])))
print("Act-dep-fixed-ha-araigl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_araigl), np.nansum(area_araigl[np.where(np.isnan(ndep_fixed_araigl)==False)])))

## Variable N deposition at actual and critical N inputs (for cutoff @ Nup,max)
# totals
ndep_var_act_fer = np.add(nh3emfert_ara, nh3emfert_igl)
ndep_var_act_man = np.add(nh3emappl_ara, nh3emappl_igl)

ndep_var_act = np.add(ndep_var_act_fer, ndep_var_act_man)
ndep_var_act = np.add(ndep_var_act, nh3emgraz_igl)
#ndep_var_act = np.add(ndep_var_act, nh3emstor)      #$#V1.3#$# OUT #$#V1.1#$# ON
ndep_var_act = np.add(ndep_var_act, nh3_stor_ara)    #$#V1.3#$# #$#V1.4#$#
ndep_var_act = np.add(ndep_var_act, nh3_stor_igl)    #$#V1.3#$# #$#V1.4#$#


ndep_var_act_ag = np.multiply(ndep_var_act, fag)
ndep_var_act_ara = np.multiply(ndep_var_act, fara)
ndep_var_act_igl = np.multiply(ndep_var_act, figl)
ndep_var_act_egl = np.multiply(ndep_var_act, fegl)
ndep_var_act_araigl = np.multiply(ndep_var_act, fagri)

print("Act-dep-var-tot-all:  %i kgNyr-1" %(np.nansum(ndep_var_act_ag)))
print("Act-dep-var-tot-ara:  %i kgNyr-1" %(np.nansum(ndep_var_act_ara)))
print("Act-dep-var-tot-igl:  %i kgNyr-1" %(np.nansum(ndep_var_act_igl)))
print("Act-dep-var-tot-egl:  %i kgNyr-1" %(np.nansum(ndep_var_act_egl)))
print("Act-dep-var-tot-araigl:  %i kgNyr-1" %(np.nansum(ndep_var_act_araigl)))
# per ha
print("Act-dep-var-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_ag),  np.nansum(agarea[np.where(np.isnan(ndep_var_act_ag)==False)])))
print("Act-dep-var-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_ara), np.nansum(area_ara[np.where(np.isnan(ndep_var_act_ara)==False)])))
print("Act-dep-var-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_igl), np.nansum(area_igl[np.where(np.isnan(ndep_var_act_igl)==False)])))
print("Act-dep-var-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_egl), np.nansum(area_egl[np.where(np.isnan(ndep_var_act_egl)==False)])))
print("Act-dep-var-ha-araigl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_araigl), np.nansum(area_araigl[np.where(np.isnan(ndep_var_act_araigl)==False)])))


ndep_var_crit_fer_sw3 = np.multiply(fercritsw3, nh3_ef_fer)
ndep_var_crit_man_sw3 = np.multiply(mancritsw3, nh3_ef_man)
ndep_var_crit_tot_sw3 = np.add(ndep_var_crit_fer_sw3, ndep_var_crit_man_sw3)
ndep_var_crit_fer_gw3 = np.multiply(fercritgw3, nh3_ef_fer)
ndep_var_crit_man_gw3 = np.multiply(mancritgw3, nh3_ef_man)
ndep_var_crit_tot_gw3 = np.add(ndep_var_crit_fer_gw3, ndep_var_crit_man_gw3)
ndep_var_crit_fer_de3 = np.multiply(fercritde3, nh3_ef_fer)
ndep_var_crit_man_de3 = np.multiply(mancritde3, nh3_ef_man)
ndep_var_crit_tot_de3 = np.add(ndep_var_crit_fer_de3, ndep_var_crit_man_de3)
ndep_var_crit_fer_min3 = np.multiply(fercritmin3, nh3_ef_fer)
ndep_var_crit_man_min3 = np.multiply(mancritmin3, nh3_ef_man)
ndep_var_crit_tot_min3 = np.add(ndep_var_crit_fer_min3, ndep_var_crit_man_min3)

# only to cropland+int GL
ndep_var_crit_tot_sw3_araigl = np.multiply(ndep_var_crit_tot_sw3, fagri)
ndep_var_crit_tot_gw3_araigl = np.multiply(ndep_var_crit_tot_gw3, fagri)
ndep_var_crit_tot_de3_araigl = np.multiply(ndep_var_crit_tot_de3, fagri)
ndep_var_crit_tot_min3_araigl = np.multiply(ndep_var_crit_tot_min3, fagri)

print("Crit-dep-var-sw-ha-3a: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_sw3_araigl), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_tot_sw3_araigl)==False)])))
print("Crit-dep-var-gw-ha-3a: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_gw3_araigl), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_tot_gw3_araigl)==False)])))
print("Crit-dep-var-de-ha-3a: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_de3_araigl), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_tot_de3_araigl)==False)])))
print("Crit-dep-var-mi-ha-3a: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_min3_araigl), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_tot_min3_araigl)==False)])))

# Total actual N inputs to araigl
nin_tot_araigl = np.add(manfer_araigl, nfix_araigl)
nin_tot_araigl = np.add(nin_tot_araigl, ndep_fixed_araigl)
nin_tot_araigl = np.add(nin_tot_araigl, ndep_var_act_araigl)

# Total critical N inputs after cutoff
nin_tot_crit_sw_cutoff = np.add(fercritsw3, mancritsw3)
nin_tot_crit_sw_cutoff = np.add(nin_tot_crit_sw_cutoff, nfix_araigl)
nin_tot_crit_sw_cutoff = np.add(nin_tot_crit_sw_cutoff, ndep_fixed_araigl)
nin_tot_crit_sw_cutoff = np.add(nin_tot_crit_sw_cutoff, ndep_var_crit_tot_sw3_araigl)

nin_tot_crit_gw_cutoff = np.add(fercritgw3, mancritgw3)
nin_tot_crit_gw_cutoff = np.add(nin_tot_crit_gw_cutoff, nfix_araigl)
nin_tot_crit_gw_cutoff = np.add(nin_tot_crit_gw_cutoff, ndep_fixed_araigl)
nin_tot_crit_gw_cutoff = np.add(nin_tot_crit_gw_cutoff, ndep_var_crit_tot_gw3_araigl)

nin_tot_crit_de_cutoff = np.add(fercritde3, mancritde3)
nin_tot_crit_de_cutoff = np.add(nin_tot_crit_de_cutoff, nfix_araigl)
nin_tot_crit_de_cutoff = np.add(nin_tot_crit_de_cutoff, ndep_fixed_araigl)
nin_tot_crit_de_cutoff = np.add(nin_tot_crit_de_cutoff, ndep_var_crit_tot_de3_araigl)

nin_tot_crit_min_cutoff = np.add(fercritmin3, mancritmin3)
nin_tot_crit_min_cutoff = np.add(nin_tot_crit_min_cutoff, nfix_araigl)
nin_tot_crit_min_cutoff = np.add(nin_tot_crit_min_cutoff, ndep_fixed_araigl)
nin_tot_crit_min_cutoff = np.add(nin_tot_crit_min_cutoff, ndep_var_crit_tot_min3_araigl)

# select minimum
nin_tot_crit_miX    = np.minimum(nin_tot_crit_sw,     nin_tot_crit_gw)
nin_tot_crit_mi     = np.minimum(nin_tot_crit_miX,    nin_tot_crit_dep)

print("CASES-FOR-*ALL*-INPUTS")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(area_araigl))
    print("case-1-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw)==False, nin_tot_crit_sw<=0)) ]))
    print("case-3-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw)==False, np.logical_and(nin_tot_crit_sw>0,nin_tot_crit_sw<=nin_tot_araigl))) ]))
    print("case-4-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw)==False, np.logical_and(nin_tot_crit_sw>nin_tot_araigl,nin_tot_crit_sw<=nin_max))) ]))
    print("case-5-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw)==False, np.logical_and(nin_tot_crit_sw>nin_tot_araigl,nin_tot_crit_sw>nin_max))) ]))
  
    print("case-1-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw)==False, nin_tot_crit_gw<=0)) ]))
    print("case-3-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw)==False, np.logical_and(nin_tot_crit_gw>0,nin_tot_crit_gw<=nin_tot_araigl))) ]))
    print("case-4-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw)==False, np.logical_and(nin_tot_crit_gw>nin_tot_araigl,nin_tot_crit_gw<=nin_max))) ]))
    print("case-5-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw)==False, np.logical_and(nin_tot_crit_gw>nin_tot_araigl,nin_tot_crit_gw>nin_max))) ]))
      
    print("case-1-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep)==False, nin_tot_crit_dep<=0)) ]))
    print("case-3-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep)==False, np.logical_and(nin_tot_crit_dep>0,nin_tot_crit_dep<=nin_tot_araigl))) ]))
    print("case-4-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep)==False, np.logical_and(nin_tot_crit_dep>nin_tot_araigl,nin_tot_crit_dep<=nin_max))) ]))
    print("case-5-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep)==False, np.logical_and(nin_tot_crit_dep>nin_tot_araigl,nin_tot_crit_dep>nin_max))) ]))

    print("case-1-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_mi)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_mi)==False, nin_tot_crit_mi<=0)) ]))
    print("case-3-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_mi)==False, np.logical_and(nin_tot_crit_mi>0,nin_tot_crit_mi<=nin_tot_araigl))) ]))
    print("case-4-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_mi)==False, np.logical_and(nin_tot_crit_mi>nin_tot_araigl,nin_tot_crit_mi<=nin_max))) ]))
    print("case-5-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(nin_tot_crit_mi)==False, np.logical_and(nin_tot_crit_mi>nin_tot_araigl,nin_tot_crit_mi>nin_max))) ]))
    

'''
#PRINT NH3 EMISSIONS AT CRITICAL N INPUTS (AFTER CUTOFF)#
print("NH3_emissions")

# calculate sums for arable + intensive grassland
nh3emfert_araigl = np.add(nh3emfert_ara, nh3emfert_igl)
nh3emappl_araigl = np.add(nh3emappl_ara, nh3emappl_igl)
area_iglegl = np.add(area_egl, area_igl)
nh3emappl_graz_araigl = np.add(nh3emappl_araigl, nh3emgraz_igl)
#nh3emman_araigl = np.add(nh3emappl_graz_araigl, nh3emstor)   #$#V1.3#$# #$#V1.4#$# OUT // #$#V1.1#$# ON
nh3emman_araigl = np.add(nh3emappl_graz_araigl, nh3_stor_ara) #$#V1.3#$# #$#V1.4#$#
nh3emman_araigl = np.add(nh3emman_araigl, nh3_stor_igl)       #$#V1.3#$# #$#V1.4#$#

nin_tot_araigl_nh3 = np.add(nin_tot_araigl, nh3emfert_araigl)
nin_tot_araigl_nh3 = np.add(nin_tot_araigl_nh3, nh3emman_araigl)

### 1. Actual NH3 emissions - totals

# 1a. NH3 emissions from fertilizer application
print("Act-NH3-fer-all-tot:    %i kgNyr-1" %(np.nansum(nh3emfert)))
print("Act-NH3-fer-ara-tot:    %i kgNyr-1" %(np.nansum(nh3emfert_ara)))
print("Act-NH3-fer-igl-tot:    %i kgNyr-1" %(np.nansum(nh3emfert_igl)))
print("Act-NH3-fer-araigl-tot: %i kgNyr-1" %(np.nansum(nh3emfert_araigl)))

# 1b. NH3 emissions from manure application
print("Act-NH3-man-appl-all-tot:    %i kgNyr-1" %(np.nansum(nh3emappl)))
print("Act-NH3-man-appl-ara-tot:    %i kgNyr-1" %(np.nansum(nh3emappl_ara)))
print("Act-NH3-man-appl-igl-tot:    %i kgNyr-1" %(np.nansum(nh3emappl_igl)))
print("Act-NH3-man-appl-araigl-tot: %i kgNyr-1" %(np.nansum(nh3emappl_araigl)))

# 1c. NH3 emissions from grazing
print("Act-NH3-man-graz-all-tot:  %i kgNyr-1" %(np.nansum(nh3emgraz)))
print("Act-NH3-man-graz-igl-tot:  %i kgNyr-1" %(np.nansum(nh3emgraz_igl)))

# 1d. NH3 emissions from storage
print("Act-NH3-man-stor-tot:  %i kgNyr-1" %(np.nansum(nh3emstor)))

# 1e. Total NH3 emissions from manure on ara +igl
print("Act-NH3-man-araigl-tot: %i kgNyr-1" %(np.nansum(nh3emman_araigl)))

### 2. Actual NH3 emissions - per hectare

# 2a. NH3 emissions from fertilizer application
print("Act-NH3-fer-all-ha:    %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emfert),        np.nansum(agarea[np.where(np.isnan(nh3emfert)==False)]))))
print("Act-NH3-fer-ara-ha:    %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emfert_ara),    np.nansum(area_ara[np.where(np.isnan(nh3emfert_ara)==False)]))))
print("Act-NH3-fer-igl-ha:    %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emfert_igl),    np.nansum(area_igl[np.where(np.isnan(nh3emfert_igl)==False)]))))
print("Act-NH3-fer-araigl-ha: %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emfert_araigl), np.nansum(area_araigl[np.where(np.isnan(nh3emfert_araigl)==False)]))))

# 2b. NH3 emissions from manure application
print("Act-NH3-man-appl-all-ha:    %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emappl),        np.nansum(agarea[np.where(np.isnan(nh3emappl)==False)]))))
print("Act-NH3-man-appl-ara-ha:    %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emappl_ara),    np.nansum(area_ara[np.where(np.isnan(nh3emappl_ara)==False)]))))
print("Act-NH3-man-appl-igl-ha:    %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emappl_igl),    np.nansum(area_igl[np.where(np.isnan(nh3emappl_igl)==False)]))))
print("Act-NH3-man-appl-araigl-ha: %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emappl_araigl), np.nansum(area_araigl[np.where(np.isnan(nh3emappl_araigl)==False)]))))

# 2c. NH3 emissions from grazing
print("Act-NH3-man-graz-all-ha:  %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emgraz),        np.nansum(area_iglegl[np.where(np.isnan(nh3emgraz)==False)]))))
print("Act-NH3-man-graz-igl-ha:  %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emgraz_igl),    np.nansum(area_igl[np.where(np.isnan(nh3emgraz_igl)==False)]))))

# 2d. NH3 emissions from storage
print("Act-NH3-man-stor-ha:  %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emstor),    np.nansum(area_igl[np.where(np.isnan(nh3emstor)==False)]))))

# 2e. NH3 emissions from manure arable + igl
print("Act-NH3-man-araigl-ha:  %.1f kgNha-1yr-1" %(np.divide(np.nansum(nh3emman_araigl),    np.nansum(area_araigl[np.where(np.isnan(nh3emman_araigl)==False)]))))

### 3. Critical NH3 emissions - totals

print("Crit-NH3-fer-tot-sw:  %i kgNyr-1" %(np.nansum(ndep_var_crit_fer_sw3)))
print("Crit-NH3-man-tot-sw:  %i kgNyr-1" %(np.nansum(ndep_var_crit_man_sw3)))
print("Crit-NH3-fer-tot-gw:  %i kgNyr-1" %(np.nansum(ndep_var_crit_fer_gw3)))
print("Crit-NH3-man-tot-gw:  %i kgNyr-1" %(np.nansum(ndep_var_crit_man_gw3)))
print("Crit-NH3-fer-tot-de:  %i kgNyr-1" %(np.nansum(ndep_var_crit_fer_de3)))
print("Crit-NH3-man-tot-de:  %i kgNyr-1" %(np.nansum(ndep_var_crit_man_de3)))
print("Crit-NH3-fer-tot-mi:  %i kgNyr-1" %(np.nansum(ndep_var_crit_fer_min3)))
print("Crit-NH3-man-tot-mi:  %i kgNyr-1" %(np.nansum(ndep_var_crit_man_min3)))

### 3. Critical NH3 emissions - per hectare

print("Crit-NH3-fer-ha-sw: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_fer_sw3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_fer_sw3)==False)])))
print("Crit-NH3-man-ha-sw: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_man_sw3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_man_sw3)==False)])))
print("Crit-NH3-fer-ha-gw: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_fer_gw3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_fer_gw3)==False)])))
print("Crit-NH3-man-ha-gw: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_man_gw3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_man_gw3)==False)])))
print("Crit-NH3-fer-ha-de: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_fer_de3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_fer_de3)==False)])))
print("Crit-NH3-man-ha-de: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_man_de3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_man_de3)==False)])))    
print("Crit-NH3-fer-ha-mi: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_fer_min3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_fer_min3)==False)])))
print("Crit-NH3-man-ha-mi: %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_crit_man_min3), np.nansum(area_araigl[np.where(np.isnan(ndep_var_crit_man_min3)==False)])))      
    
    
##REGIONAL RESULTS
print("regional results")
x = np.copy(mancritmin3)
print("region-01:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==1 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-02:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==2 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-03:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==3 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-04:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==4 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-05:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==5 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-06:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==6 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-07:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==7 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-08:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==8 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-09:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==9 , np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-10:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==10, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-11:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==11, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-12:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==12, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-13:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==13, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-14:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==14, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-15:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==15, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-16:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==16, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-17:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==17, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-18:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==18, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-19:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==19, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-20:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==20, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-21:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==21, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-22:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==22, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-23:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==23, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-24:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==24, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-25:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==25, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-26:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==26, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-27:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==27, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("region-28:     %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(regions==28, np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False)))]))
print("global:        %.1f kgNyr-1" % np.nansum(x[np.where(np.logical_and(np.isnan(fercritgw3)==False, np.isnan(fercritde3)==False))]))

#PLOTS

# Exceedance of critical N inputs by actual N inputs
exceedance_sw  = np.subtract(nin_tot_araigl,nin_tot_crit_sw_cutoff)
exceedance_gw  = np.subtract(nin_tot_araigl,nin_tot_crit_gw_cutoff)
exceedance_de  = np.subtract(nin_tot_araigl,nin_tot_crit_de_cutoff)
exceedance_min = np.subtract(nin_tot_araigl, nin_tot_crit_min_cutoff)

exceedance_sw_ha = np.divide(exceedance_sw,area_araigl)
exceedance_gw_ha = np.divide(exceedance_gw,area_araigl)
exceedance_de_ha = np.divide(exceedance_de,area_araigl)
exceedance_min_ha = np.divide(exceedance_min,area_araigl)

# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_min_ha[np.isnan(agarea)]= -99999
# plot map with exceedances
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_min_ha, cmap=cmap, vmin=-1000) # exceedance critical N inputs minimum
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs [minimum]")
plt.show()

print("END")
print("END")

# Critical N inputs per hectare, no cut-off value
print("CRITICAL-INPUTS-PER-HA")
#WRONG
#print("Crit-fer-sw-ha-1: %.1f" % np.nanmean(fercritswha))
#print("Crit-man-sw-ha-1: %.1f" % np.nanmean(mancritswha))
#print("Crit-fer-gw-ha-1: %.1f" % np.nanmean(fercritgwha))
#print("Crit-man-gw-ha-1: %.1f" % np.nanmean(mancritgwha))
#print("Crit-fer-de-ha-1: %.1f" % np.nanmean(fercritdeha))
#print("Crit-man-de-ha-1: %.1f" % np.nanmean(mancritdeha))
#print("Crit-nin-sw-ha-1: %.1f" % np.nanmean(manfercritswha))
#print("Crit-nin-gw-ha-1: %.1f" % np.nanmean(manfercritgwha))
#print("Crit-nin-de-ha-1: %.1f" % np.nanmean(manfercritdeha))
#RIGHT
print("Crit-fer-sw-ha-1: %.1f" % np.divide(np.nansum(fercritsw), np.nansum(area_araigl[np.where(np.isnan(fercritsw)==False)])))
print("Crit-man-sw-ha-1: %.1f" % np.divide(np.nansum(mancritsw), np.nansum(area_araigl[np.where(np.isnan(mancritsw)==False)])))
print("Crit-fer-gw-ha-1: %.1f" % np.divide(np.nansum(fercritgw), np.nansum(area_araigl[np.where(np.isnan(fercritgw)==False)])))
print("Crit-man-gw-ha-1: %.1f" % np.divide(np.nansum(mancritgw), np.nansum(area_araigl[np.where(np.isnan(mancritgw)==False)])))
print("Crit-fer-de-ha-1: %.1f" % np.divide(np.nansum(fercritde), np.nansum(area_araigl[np.where(np.isnan(fercritde)==False)])))
print("Crit-man-de-ha-1: %.1f" % np.divide(np.nansum(mancritde), np.nansum(area_araigl[np.where(np.isnan(mancritde)==False)])))
print("Crit-nin-sw-ha-1: %.1f" % np.divide(np.nansum(manfercritsw), np.nansum(area_araigl[np.where(np.isnan(manfercritsw)==False)])))
print("Crit-nin-gw-ha-1: %.1f" % np.divide(np.nansum(manfercritgw), np.nansum(area_araigl[np.where(np.isnan(manfercritgw)==False)]))) 
print("Crit-nin-de-ha-1: %.1f" % np.divide(np.nansum(manfercritde), np.nansum(area_araigl[np.where(np.isnan(manfercritde)==False)])))

# Critical N inputs with no cutoff value but negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO")
fercritsw2 = np.copy(fercritsw)
mancritsw2 = np.copy(mancritsw)
fercritgw2 = np.copy(fercritgw)
mancritgw2 = np.copy(mancritgw)
fercritde2 = np.copy(fercritde)
mancritde2 = np.copy(mancritde)
manfercritsw2 = np.copy(manfercritsw)
manfercritgw2 = np.copy(manfercritgw)
manfercritde2 = np.copy(manfercritde)

with np.errstate(invalid='ignore'):
    fercritsw2[fercritsw2<0]=0
    mancritsw2[mancritsw2<0]=0
    fercritgw2[fercritgw2<0]=0
    mancritgw2[mancritgw2<0]=0
    fercritde2[fercritde2<0]=0
    mancritde2[mancritde2<0]=0
    manfercritsw2[manfercritsw2<0]=0
    manfercritgw2[manfercritgw2<0]=0
    manfercritde2[manfercritde2<0]=0

print("Crit-fer-sw-ha-2: %.1f" % np.divide(np.nansum(fercritsw2), np.nansum(area_araigl[np.where(np.isnan(fercritsw2)==False)])))
print("Crit-man-sw-ha-2: %.1f" % np.divide(np.nansum(mancritsw2), np.nansum(area_araigl[np.where(np.isnan(mancritsw2)==False)])))
print("Crit-fer-gw-ha-2: %.1f" % np.divide(np.nansum(fercritgw2), np.nansum(area_araigl[np.where(np.isnan(fercritgw2)==False)])))
print("Crit-man-gw-ha-2: %.1f" % np.divide(np.nansum(mancritgw2), np.nansum(area_araigl[np.where(np.isnan(mancritgw2)==False)])))
print("Crit-fer-de-ha-2: %.1f" % np.divide(np.nansum(fercritde2), np.nansum(area_araigl[np.where(np.isnan(fercritde2)==False)])))
print("Crit-man-de-ha-2: %.1f" % np.divide(np.nansum(mancritde2), np.nansum(area_araigl[np.where(np.isnan(mancritde2)==False)])))
print("Crit-nin-sw-ha-2: %.1f" % np.divide(np.nansum(manfercritsw2), np.nansum(area_araigl[np.where(np.isnan(manfercritsw2)==False)])))
print("Crit-nin-gw-ha-2: %.1f" % np.divide(np.nansum(manfercritgw2), np.nansum(area_araigl[np.where(np.isnan(manfercritgw2)==False)]))) 
print("Crit-nin-de-ha-2: %.1f" % np.divide(np.nansum(manfercritde2), np.nansum(area_araigl[np.where(np.isnan(manfercritde2)==False)])))

# Critical N inputs with cutoff @ 150 kg N ha-1 yr-1 and negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-150")
manfercritswha3 = np.copy(manfercritswha)
manfercritgwha3 = np.copy(manfercritgwha)
manfercritdeha3 = np.copy(manfercritdeha)

with np.errstate(invalid='ignore'):
    manfercritswha3[manfercritswha3<0]=0
    manfercritgwha3[manfercritgwha3<0]=0
    manfercritdeha3[manfercritdeha3<0]=0
    manfercritswha3[manfercritswha3>150]=150
    manfercritgwha3[manfercritgwha3>150]=150
    manfercritdeha3[manfercritdeha3>150]=150

#Totals
manfercritsw3 = np.multiply(manfercritswha3, area_araigl)
manfercritgw3 = np.multiply(manfercritgwha3, area_araigl)
manfercritde3 = np.multiply(manfercritdeha3, area_araigl)

#WRONG
#print("Crit-nin-sw-ha-3: %.1f" % np.nanmean(manfercritswha3))
#print("Crit-nin-gw-ha-3: %.1f" % np.nanmean(manfercritgwha3))
#print("Crit-nin-de-ha-3: %.1f" % np.nanmean(manfercritdeha3))
#RIGHT
print("Crit-nin-sw-ha-3: %.1f" % np.divide(np.nansum(manfercritsw3), np.nansum(area_araigl[np.where(np.isnan(manfercritsw3)==False)])))
print("Crit-nin-gw-ha-3: %.1f" % np.divide(np.nansum(manfercritgw3), np.nansum(area_araigl[np.where(np.isnan(manfercritgw3)==False)])))
print("Crit-nin-de-ha-3: %.1f" % np.divide(np.nansum(manfercritde3), np.nansum(area_araigl[np.where(np.isnan(manfercritde3)==False)])))

with np.errstate(invalid='ignore'):
    fercritsw3 = np.multiply(manfercritsw3,     frnfe_agri)
    mancritsw3 = np.multiply(manfercritsw3, (1.-frnfe_agri))
    fercritgw3 = np.multiply(manfercritgw3,     frnfe_agri)
    mancritgw3 = np.multiply(manfercritgw3, (1.-frnfe_agri))
    fercritde3 = np.multiply(manfercritde3,     frnfe_agri)
    mancritde3 = np.multiply(manfercritde3, (1.-frnfe_agri))
print("Crit-fer-sw-ha-3: %.1f" % np.divide(np.nansum(fercritsw3), np.nansum(area_araigl[np.where(np.isnan(fercritsw3)==False)])))
print("Crit-man-sw-ha-3: %.1f" % np.divide(np.nansum(mancritsw3), np.nansum(area_araigl[np.where(np.isnan(mancritsw3)==False)])))
print("Crit-fer-gw-ha-3: %.1f" % np.divide(np.nansum(fercritgw3), np.nansum(area_araigl[np.where(np.isnan(fercritgw3)==False)])))
print("Crit-man-gw-ha-3: %.1f" % np.divide(np.nansum(mancritgw3), np.nansum(area_araigl[np.where(np.isnan(mancritgw3)==False)])))
print("Crit-fer-de-ha-3: %.1f" % np.divide(np.nansum(fercritde3), np.nansum(area_araigl[np.where(np.isnan(fercritde3)==False)])))
print("Crit-man-de-ha-3: %.1f" % np.divide(np.nansum(mancritde3), np.nansum(area_araigl[np.where(np.isnan(mancritde3)==False)])))

#
# Critical N inputs with cutoff @ max (150, actual) and negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-MAX(150,ACT)")
manfercritswha4 = np.copy(manfercritswha)
manfercritgwha4 = np.copy(manfercritgwha)
manfercritdeha4 = np.copy(manfercritdeha)

with np.errstate(invalid='ignore'):
    manfercritswha4[manfercritswha4<0]=0
    manfercritgwha4[manfercritgwha4<0]=0
    manfercritdeha4[manfercritdeha4<0]=0
    
    print("STEP1: %i" % np.nansum(manfercritswha4))
    
    for i in range(np.shape(manferha_araigl)[0]):
        for j in range(np.shape(manferha_araigl)[1]):
            if (manfercritswha4[i,j] > manferha_araigl[i,j] and manfercritswha4[i,j] > 150):
                manfercritswha4[i,j] = max(manferha_araigl[i,j],150)
            if (manfercritgwha4[i,j] > manferha_araigl[i,j] and manfercritgwha4[i,j] > 150):
                manfercritgwha4[i,j] = max(manferha_araigl[i,j],150)
            if (manfercritdeha4[i,j] > manferha_araigl[i,j] and manfercritdeha4[i,j] > 150):
                manfercritdeha4[i,j] = max(manferha_araigl[i,j],150)
    
    print("STEP2: %i" % np.nansum(manfercritswha4))
    
#Totals
manfercritsw4 = np.multiply(manfercritswha4, area_araigl)
manfercritgw4 = np.multiply(manfercritgwha4, area_araigl)
manfercritde4 = np.multiply(manfercritdeha4, area_araigl)

#WRONG
#print("Crit-nin-sw-ha-4: %.1f" % np.nanmean(manfercritswha4))
#print("Crit-nin-gw-ha-4: %.1f" % np.nanmean(manfercritgwha4))
#print("Crit-nin-de-ha-4: %.1f" % np.nanmean(manfercritdeha4))
#RIGHT
print("Crit-nin-sw-ha-4: %.1f" % np.divide(np.nansum(manfercritsw4), np.nansum(area_araigl[np.where(np.isnan(manfercritsw4)==False)])))
print("Crit-nin-gw-ha-4: %.1f" % np.divide(np.nansum(manfercritgw4), np.nansum(area_araigl[np.where(np.isnan(manfercritgw4)==False)])))
print("Crit-nin-de-ha-4: %.1f" % np.divide(np.nansum(manfercritde4), np.nansum(area_araigl[np.where(np.isnan(manfercritde4)==False)])))

with np.errstate(invalid='ignore'):
    fercritsw4 = np.multiply(manfercritsw4,     frnfe_agri)
    mancritsw4 = np.multiply(manfercritsw4, (1.-frnfe_agri))
    fercritgw4 = np.multiply(manfercritgw4,     frnfe_agri)
    mancritgw4 = np.multiply(manfercritgw4, (1.-frnfe_agri))
    fercritde4 = np.multiply(manfercritde4,     frnfe_agri)
    mancritde4 = np.multiply(manfercritde4, (1.-frnfe_agri))
print("Crit-fer-sw-ha-4: %.1f" % np.divide(np.nansum(fercritsw4), np.nansum(area_araigl[np.where(np.isnan(fercritsw4)==False)])))
print("Crit-man-sw-ha-4: %.1f" % np.divide(np.nansum(mancritsw4), np.nansum(area_araigl[np.where(np.isnan(mancritsw4)==False)])))
print("Crit-fer-gw-ha-4: %.1f" % np.divide(np.nansum(fercritgw4), np.nansum(area_araigl[np.where(np.isnan(fercritgw4)==False)])))
print("Crit-man-gw-ha-4: %.1f" % np.divide(np.nansum(mancritgw4), np.nansum(area_araigl[np.where(np.isnan(mancritgw4)==False)])))
print("Crit-fer-de-ha-4: %.1f" % np.divide(np.nansum(fercritde4), np.nansum(area_araigl[np.where(np.isnan(fercritde4)==False)])))
print("Crit-man-de-ha-4: %.1f" % np.divide(np.nansum(mancritde4), np.nansum(area_araigl[np.where(np.isnan(mancritde4)==False)])))

# Critical N inputs with cutoff @ max (150, actual) and negative values replaced by zero + INPUTS TO EXT GR
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-MAX(150,ACT)-+-Nin,EGL")
manfercritsw5 = np.add(manfercritsw4, nman_egl)
manfercritgw5 = np.add(manfercritgw4, nman_egl)
manfercritde5 = np.add(manfercritde4, nman_egl)
print("Crit-nin-sw-5: %.1f" % np.divide(np.nansum(manfercritsw5), np.nansum(agarea[np.where(np.isnan(manfercritsw5)==False)])))
print("Crit-nin-gw-5: %.1f" % np.divide(np.nansum(manfercritgw5), np.nansum(agarea[np.where(np.isnan(manfercritgw5)==False)])))
print("Crit-nin-dw-5: %.1f" % np.divide(np.nansum(manfercritde5), np.nansum(agarea[np.where(np.isnan(manfercritde5)==False)])))

# CALCULATE fNup,max
fercritgw3 = np.copy(fercritgw2) # negative values are already set to zero
mancritgw3 = np.copy(mancritgw2) # negative values are already set to zero

for i in range(np.shape(fnup_max_gw)[0]):
    for j in range(np.shape(fnup_max_gw)[1]):
        if (fnup_max_gw[i,j] < 1 and np.isnan(fnup_max_gw[i,j])==False):
            mancritgw3[i,j] = mancritgw3[i,j]*fnup_corr_gw[i,j]
            fercritgw3[i,j] = fercritgw3[i,j]*fnup_corr_gw[i,j]
    
print("RESULTS NEW CUTOFF MANURE: %i" % np.nansum(mancritgw3))
print("RESULTS NEW CUTOFF FERTIL: %i" % np.nansum(fercritgw3))



# MINIMUM of critical N inputs
print("CRITICAL-INPUTS-MINIMUM-EXCL-EGL")
manfercritmin4X   = np.minimum(manfercritsw4, manfercritgw4)
manfercritmin4    = np.minimum(manfercritmin4X, manfercritde4)
print("Crit-nin-min-ha-4: %.1f" % np.divide(np.nansum(manfercritmin4), np.nansum(area_araigl[np.where(np.isnan(manfercritmin4)==False)])))
with np.errstate(invalid='ignore'):
    fercritmin4 = np.multiply(manfercritmin4,     frnfe_agri)
    mancritmin4 = np.multiply(manfercritmin4, (1.-frnfe_agri))
print("Crit-fer-min-ha-4: %.1f" % np.divide(np.nansum(fercritmin4), np.nansum(area_araigl[np.where(np.isnan(fercritmin4)==False)])))
print("Crit-man-min-ha-4: %.1f" % np.divide(np.nansum(mancritmin4), np.nansum(area_araigl[np.where(np.isnan(mancritmin4)==False)])))

print("CRITICAL-INPUTS-MINIMUM-INCL-EGL")
manfercritmin5X   = np.minimum(manfercritsw5, manfercritgw5)
manfercritmin5    = np.minimum(manfercritmin5X, manfercritde5)
print("Crit-nin-min-ha-5: %.1f" % np.divide(np.nansum(manfercritmin5), np.nansum(agarea[np.where(np.isnan(manfercritmin5)==False)])))
with np.errstate(invalid='ignore'):
    fercritmin5 = np.multiply(manfercritmin5,     frnfe_agri)
    mancritmin5 = np.multiply(manfercritmin5, (1.-frnfe_agri))
print("Crit-fer-min-ha-5: %.1f" % np.divide(np.nansum(fercritmin5), np.nansum(agarea[np.where(np.isnan(fercritmin5)==False)])))
print("Crit-man-min-ha-5: %.1f" % np.divide(np.nansum(mancritmin5), np.nansum(agarea[np.where(np.isnan(mancritmin5)==False)])))






# Plot critical N inputs
#plt.subplot(3, 2, 1)
#plt.imshow(manfercritswha4) # critical N inputs surface water
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - surface water")
#plt.show()

#plt.imshow(manfercritgwha4) # critical N inputs groundwater
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - groundwater")
#plt.show()

#plt.imshow(manfercritdeha4) # critical N inputs deposition
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - deposition")
#plt.show()


#cmap=matplotlib.cm.get_cmap('RdYlGn')
#cmap.set_bad(color='0.8')
#cmap.set_under('0.5')
#plt.imshow(manfercritminha, cmap=cmap)#, vmin=-0.001) # critical N inputs minimum
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - minimum")
#plt.show()

#plt.imshow(manferha_araigl) # actual N inputs to cropland + intensive grassland
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Actual N inputs manure + fertilizer")
#plt.show()

# Exceedance of critical N inputs by actual N inputs
exceedance_sw = np.subtract(manferha_araigl,manfercritswha4)
exceedance_gw = np.subtract(manferha_araigl,manfercritgwha4)
exceedance_de = np.subtract(manferha_araigl,manfercritdeha4)
exceedance_min = np.subtract(manferha_araigl, manfercritminha)

# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_min[np.isnan(agarea)]= -99999
# plot map with exceedances
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_min, cmap=cmap, vmin=-1000) # exceedance critical N inputs minimum
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs V2")
plt.show()


#plt.imshow(exceedance_sw, cmap='RdYlGn_r') # exceedance critical N inputs surface water
#plt.colorbar(extend='both')
#plt.clim(-300, 300) # different limits are possible
#plt.title("Exceedance critical N inputs - surface water")
#plt.show()

#plt.imshow(exceedance_gw, cmap='RdYlGn_r') # exceedance critical N inputs groundwater
#plt.colorbar(extend='both')
#plt.clim(-300, 300) # different limits are possible
#plt.title("Exceedance Critical N inputs - groundwater")
#plt.show()

#plt.imshow(exceedance_de, cmap='RdYlGn_r') # exceedance critical N inputs deposition
#plt.colorbar(extend='both')
#plt.clim(-300, 300) # different limits are possible
#plt.title("Exceedance Critical N inputs - deposition")
#plt.show()

plt.imshow(exceedance_min, cmap='RdYlGn_r') # exceedance critical N inputs minimum
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs V1")
plt.show()





# Critical N inputs with no cutoff value
#print("TOTAL-CRITICAL-INPUTS-WITHOUT-CUT-OFF-VALUE")
#print("Crit-fer-sw: %.2f"    % np.nansum(fercritsw))
#print("Crit-man-sw: %.2f"    % np.nansum(mancritsw))
#print("Crit-fer-gw: %.2f"    % np.nansum(fercritgw))
#print("Crit-man-gw: %.2f"    % np.nansum(mancritgw))
#print("Crit-fer-de: %.2f"    % np.nansum(fercritde))
#print("Crit-man-de: %.2f"    % np.nansum(mancritde))
#print("Ag-area: %.2f"        % np.nansum(agarea))

# per ha 1: total inputs divided by total area (but sum total area only for those grid cells where critical N inputs are not NA!)
#print("CRITICAL-INPUTS-PER-HA-I")
#print("Crit-fer-sw-ha-1: %f" % np.divide(np.nansum(fercritsw), np.nansum(agarea[np.where(np.isnan(fercritsw)==False)])))
#print("Crit-man-sw-ha-1: %f" % np.divide(np.nansum(mancritsw), np.nansum(agarea[np.where(np.isnan(mancritsw)==False)])))
#print("Crit-fer-gw-ha-1: %f" % np.divide(np.nansum(fercritgw), np.nansum(agarea[np.where(np.isnan(fercritgw)==False)])))
#print("Crit-man-gw-ha-1: %f" % np.divide(np.nansum(mancritgw), np.nansum(agarea[np.where(np.isnan(mancritgw)==False)])))
#print("Crit-fer-de-ha-1: %f" % np.divide(np.nansum(fercritde), np.nansum(agarea[np.where(np.isnan(fercritde)==False)])))
#print("Crit-man-de-ha-1: %f" % np.divide(np.nansum(mancritde), np.nansum(agarea[np.where(np.isnan(mancritde)==False)])))

# per ha 2: mean of the per-hectare values obtained by calculating inputs / area for each grid cell
#print("CRITICAL-INPUTS-PER-HA-II")
#print("Crit-fer-sw-ha-2: %f" % np.nanmean(fercritswha))
#print("Crit-man-sw-ha-2: %f" % np.nanmean(mancritswha))
#print("Crit-fer-gw-ha-2: %f" % np.nanmean(fercritgwha))
#print("Crit-man-gw-ha-2: %f" % np.nanmean(mancritgwha))
#print("Crit-fer-de-ha-2: %f" % np.nanmean(fercritdeha))
#print("Crit-man-de-ha-2: %f" % np.nanmean(mancritdeha))

# per ha 3: as (2), but with negative values removed
#print("CRITICAL-INPUTS-PER-HA-III")
#with np.errstate(invalid='ignore'):
#    print("Crit-fer-sw-ha-3: %f" % np.nanmean(fercritswha[np.where(fercritswha>0)]))
#    print("Crit-man-sw-ha-3: %f" % np.nanmean(mancritswha[np.where(mancritswha>0)]))
#    print("Crit-fer-gw-ha-3: %f" % np.nanmean(fercritgwha[np.where(fercritgwha>0)]))
#    print("Crit-man-gw-ha-3: %f" % np.nanmean(mancritgwha[np.where(mancritgwha>0)]))
#    print("Crit-fer-de-ha-3: %f" % np.nanmean(fercritdeha[np.where(fercritdeha>0)]))
#    print("Crit-man-de-ha-3: %f" % np.nanmean(mancritdeha[np.where(mancritdeha>0)]))

# per ha 4: as (2), but with negative values replaced by zero
#print("CRITICAL-INPUTS-PER-HA-VI")
#fercritswha2 = np.copy(fercritswha)
#mancritswha2 = np.copy(mancritswha)
#fercritgwha2 = np.copy(fercritgwha)
#mancritgwha2 = np.copy(mancritgwha)
#fercritdeha2 = np.copy(fercritdeha)
#mancritdeha2 = np.copy(mancritdeha)
#with np.errstate(invalid='ignore'):
#    fercritswha2[fercritswha2<0]=0
#    mancritswha2[mancritswha2<0]=0
#    fercritgwha2[fercritgwha2<0]=0
#    mancritgwha2[mancritgwha2<0]=0
#    fercritdeha2[fercritdeha2<0]=0
#    mancritdeha2[mancritdeha2<0]=0
#print("Crit-fer-sw-ha-4: %f" % np.nanmean(fercritswha2))
#print("Crit-man-sw-ha-4: %f" % np.nanmean(mancritswha2))
#print("Crit-fer-gw-ha-4: %f" % np.nanmean(fercritgwha2))
#print("Crit-man-gw-ha-4: %f" % np.nanmean(mancritgwha2))
#print("Crit-fer-de-ha-4: %f" % np.nanmean(fercritdeha2))
#print("Crit-man-de-ha-4: %f" % np.nanmean(mancritdeha2))

#nincritswha = np.add(fercritswha2,mancritswha2)
#nincritgwha = np.add(fercritgwha2,mancritgwha2)
#nincritdeha = np.add(fercritdeha2,mancritdeha2)
#print("Crit-nin-sw-ha-4: %f" % np.nanmean(nincritswha))
#print("Crit-nin-gw-ha-4: %f" % np.nanmean(nincritgwha))
#print("Crit-nin-de-ha-4: %f" % np.nanmean(nincritdeha))

# per ha 5: as (2), but with cutoff at 150
#print("CRITICAL-INPUTS-PER-HA-V")
#nincritswha2 = np.copy(nincritswha)
#nincritgwha2 = np.copy(nincritgwha)
#nincritdeha2 = np.copy(nincritdeha)

#with np.errstate(invalid='ignore'):
#    nincritswha2[nincritswha2>150]=150
#    nincritgwha2[nincritgwha2>150]=150
#    nincritdeha2[nincritdeha2>150]=150
#print("Crit-nin-sw-ha-5: %f" % np.nanmean(nincritswha2))
#print("Crit-nin-gw-ha-5: %f" % np.nanmean(nincritgwha2))
#print("Crit-nin-de-ha-5: %f" % np.nanmean(nincritdeha2))

#with np.errstate(invalid='ignore'):
#    fercritswha3 = np.multiply(nincritswha2,     frnfe)
#    mancritswha3 = np.multiply(nincritswha2, (1.-frnfe))
#    fercritgwha3 = np.multiply(nincritgwha2,     frnfe)
#    mancritgwha3 = np.multiply(nincritgwha2, (1.-frnfe))
#    fercritdeha3 = np.multiply(nincritdeha2,     frnfe)
#    mancritdeha3 = np.multiply(nincritdeha2, (1.-frnfe))
#print("Crit-fer-sw-ha-5: %f" % np.nanmean(fercritswha3))
#print("Crit-man-sw-ha-5: %f" % np.nanmean(mancritswha3))
#print("Crit-fer-gw-ha-5: %f" % np.nanmean(fercritgwha3))
#print("Crit-man-gw-ha-5: %f" % np.nanmean(mancritgwha3))
#print("Crit-fer-de-ha-5: %f" % np.nanmean(fercritdeha3))
#print("Crit-man-de-ha-5: %f" % np.nanmean(mancritdeha3))


#DOESN'T WORK YET
#print("CRITICAL-INPUTS-PER-HA-VI")
#nincritswha3 = np.copy(nincritswha)
#nincritgwha3 = np.copy(nincritgwha)
#nincritdeha3 = np.copy(nincritdeha)

#print(type(ninha))
#print(type(nincritswha3))
#print(np.shape(ninha))
#print(np.shape(nincritswha3))

#with np.errstate(invalid='ignore'):
#    for i in range(np.shape(ninha)[0]):
#        for j in range(np.shape(ninha)[1]):
#            if nincritswha3[i,j] > ninha[i,j]:
#                nincritswha3[i,j] = ninha[i,j]
#            if nincritgwha3[i,j] > ninha[i,j]:
#                nincritgwha3[i,j] = ninha[i,j]
#            if nincritdeha3[i,j] > ninha[i,j]:
#                nincritdeha3[i,j] = ninha[i,j]

 
#print("Crit-nin-sw-ha-6: %f" % np.nanmean(nincritswha3))
#print("Crit-nin-gw-ha-6: %f" % np.nanmean(nincritgwha3))
#print("Crit-nin-de-ha-6: %f" % np.nanmean(nincritdeha3))

#with np.errstate(invalid='ignore'):
#    fercritswha4 = np.multiply(nincritswha3,     frnfe)
#    mancritswha4 = np.multiply(nincritswha3, (1.-frnfe))
#    fercritgwha4 = np.multiply(nincritgwha3,     frnfe)
#    mancritgwha4 = np.multiply(nincritgwha3, (1.-frnfe))
#    fercritdeha4 = np.multiply(nincritdeha3,     frnfe)
#    mancritdeha4 = np.multiply(nincritdeha3, (1.-frnfe))
#print("Crit-fer-sw-ha-6: %f" % np.nanmean(fercritswha4))
#print("Crit-man-sw-ha-6: %f" % np.nanmean(mancritswha4))
#print("Crit-fer-gw-ha-6: %f" % np.nanmean(fercritgwha4))
#print("Crit-man-gw-ha-6: %f" % np.nanmean(mancritgwha4))
#print("Crit-fer-de-ha-6: %f" % np.nanmean(fercritdeha4))
#print("Crit-man-de-ha-6: %f" % np.nanmean(mancritdeha4))    

'''