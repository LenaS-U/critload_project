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
os.chdir('critload')
os.chdir('trunk')
os.chdir('output')
os.chdir('2010')

# general
nfer_ag          = np.loadtxt("nfer_ag.asc"              , skiprows=6)
nman_ag          = np.loadtxt("nman_ag.asc"              , skiprows=6)
nox_em           = np.loadtxt("nox_em.asc"               , skiprows=6)
fag              = np.loadtxt("fag.asc"                  , skiprows=6)
fara             = np.loadtxt("fara.asc"                 , skiprows=6)
figl             = np.loadtxt("figl.asc"                 , skiprows=6)
fegl             = np.loadtxt("fegl.asc"                 , skiprows=6)

# egl
nman_egl             = np.loadtxt("nman_egl.asc"            , skiprows=6)
nh3_tot_egl          = np.loadtxt("nh3_tot_egl.asc"         , skiprows=6)
nh3_stor_egl         = np.loadtxt("nh3_stor_egl.asc"        , skiprows=6)

# ara
nfer_ara             = np.loadtxt("nfer_ara.asc"            , skiprows=6)
nman_ara             = np.loadtxt("nman_ara.asc"            , skiprows=6)
nman_crit_sw_ara     = np.loadtxt("nman_crit_sw_ara.asc"    , skiprows=6)
nfer_crit_sw_ara     = np.loadtxt("nfer_crit_sw_ara.asc"    , skiprows=6)
nman_crit_gw_ara     = np.loadtxt("nman_crit_gw_ara.asc"    , skiprows=6)
nfer_crit_gw_ara     = np.loadtxt("nfer_crit_gw_ara.asc"    , skiprows=6)
nman_crit_de_ara     = np.loadtxt("nman_crit_dep_ara.asc"   , skiprows=6)
nfer_crit_de_ara     = np.loadtxt("nfer_crit_dep_ara.asc"   , skiprows=6)
frnfe_ara            = np.loadtxt("frnfe_ara.asc"           , skiprows=6)
nup_max_ara          = np.loadtxt("nup_max_ara.asc"         , skiprows=6)
nup_crit_sw_ara      = np.loadtxt("nup_crit_sw_ara.asc"     , skiprows=6)
nup_crit_gw_ara      = np.loadtxt("nup_crit_gw_ara.asc"     , skiprows=6)
nup_crit_dep_ara     = np.loadtxt("nup_crit_dep_ara.asc"    , skiprows=6)
fnup_max_sw_ara      = np.loadtxt("fnup_max_sw_ara.asc"     , skiprows=6)
fnup_max_gw_ara      = np.loadtxt("fnup_max_gw_ara.asc"     , skiprows=6)
fnup_max_de_ara      = np.loadtxt("fnup_max_dep_ara.asc"    , skiprows=6)
fnup_corr_sw_ara     = np.loadtxt("fnup_corr_sw_ara.asc"    , skiprows=6)
fnup_corr_gw_ara     = np.loadtxt("fnup_corr_gw_ara.asc"    , skiprows=6)
fnup_corr_de_ara     = np.loadtxt("fnup_corr_dep_ara.asc"   , skiprows=6)
nue_ara              = np.loadtxt("nue_ara.asc"             , skiprows=6)
nh3_ef_man_ara       = np.loadtxt("nh3_ef_man_ara.asc"      , skiprows=6)
nh3_ef_fer_ara       = np.loadtxt("nh3_ef_fer_ara.asc"      , skiprows=6)
nin_max_ara          = np.loadtxt("nin_max_ara.asc"         , skiprows=6)
nin_tot_crit_sw_ara  = np.loadtxt("nin_crit_sw_ara.asc"     , skiprows=6)
nin_tot_crit_gw_ara  = np.loadtxt("nin_crit_gw_ara.asc"     , skiprows=6)
nin_tot_crit_dep_ara = np.loadtxt("nin_crit_dep_ara.asc"    , skiprows=6)
nh3_stor_ara         = np.loadtxt("nh3_stor_ara.asc"        , skiprows=6)

# igl
nfer_igl             = np.loadtxt("nfer_igl.asc"            , skiprows=6)
nman_igl             = np.loadtxt("nman_igl.asc"            , skiprows=6)
nman_crit_sw_igl     = np.loadtxt("nman_crit_sw_igl.asc"    , skiprows=6)
nfer_crit_sw_igl     = np.loadtxt("nfer_crit_sw_igl.asc"    , skiprows=6)
nman_crit_gw_igl     = np.loadtxt("nman_crit_gw_igl.asc"    , skiprows=6)
nfer_crit_gw_igl     = np.loadtxt("nfer_crit_gw_igl.asc"    , skiprows=6)
nman_crit_de_igl     = np.loadtxt("nman_crit_dep_igl.asc"   , skiprows=6)
nfer_crit_de_igl     = np.loadtxt("nfer_crit_dep_igl.asc"   , skiprows=6)
frnfe_igl            = np.loadtxt("frnfe_igl.asc"           , skiprows=6)
nup_max_igl          = np.loadtxt("nup_max_igl.asc"         , skiprows=6)
nup_crit_sw_igl      = np.loadtxt("nup_crit_sw_igl.asc"     , skiprows=6)
nup_crit_gw_igl      = np.loadtxt("nup_crit_gw_igl.asc"     , skiprows=6)
nup_crit_dep_igl     = np.loadtxt("nup_crit_dep_igl.asc"    , skiprows=6)
fnup_max_sw_igl      = np.loadtxt("fnup_max_sw_igl.asc"     , skiprows=6)
fnup_max_gw_igl      = np.loadtxt("fnup_max_gw_igl.asc"     , skiprows=6)
fnup_max_de_igl      = np.loadtxt("fnup_max_dep_igl.asc"    , skiprows=6)
fnup_corr_sw_igl     = np.loadtxt("fnup_corr_sw_igl.asc"    , skiprows=6)
fnup_corr_gw_igl     = np.loadtxt("fnup_corr_gw_igl.asc"    , skiprows=6)
fnup_corr_de_igl     = np.loadtxt("fnup_corr_dep_igl.asc"   , skiprows=6)
nue_igl              = np.loadtxt("nue_igl.asc"             , skiprows=6)
nh3_ef_man_igl       = np.loadtxt("nh3_ef_man_igl.asc"      , skiprows=6)
nh3_ef_fer_igl       = np.loadtxt("nh3_ef_fer_igl.asc"      , skiprows=6)
nin_max_igl          = np.loadtxt("nin_max_igl.asc"         , skiprows=6)
nin_tot_crit_sw_igl  = np.loadtxt("nin_crit_sw_igl.asc"     , skiprows=6)
nin_tot_crit_gw_igl  = np.loadtxt("nin_crit_gw_igl.asc"     , skiprows=6)
nin_tot_crit_dep_igl = np.loadtxt("nin_crit_dep_igl.asc"    , skiprows=6)
nh3_stor_igl         = np.loadtxt("nh3_stor_igl.asc"        , skiprows=6)

### 1b. Read files from *INPUT* directory
os.chdir('c:\\users')
os.chdir('schul028')
os.chdir('OneDrive - WageningenUR')
os.chdir('critload_project')
os.chdir('critload')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

a_ag               = np.loadtxt("a_ag.asc"                     , skiprows=6)
a_ara              = np.loadtxt("a_crop.asc"                   , skiprows=6)
a_igl              = np.loadtxt("a_gr_int.asc"                 , skiprows=6)
a_egl              = np.loadtxt("a_gr_ext.asc"                 , skiprows=6) 
nfix_ag            = np.loadtxt("nfix_ag.asc"                  , skiprows=6)
nfix_ara           = np.loadtxt("nfix_crop.asc"                , skiprows=6)
nfix_igl           = np.loadtxt("nfix_grass_int.asc"           , skiprows=6)
nfix_egl           = np.loadtxt("nfix_grass_ext.asc"           , skiprows=6)
fgw_rec_ag         = np.loadtxt("fgw_rec_ag.asc"               , skiprows=6)
fgw_rec_nat        = np.loadtxt("fgw_rec_nat.asc"              , skiprows=6)
ndep               = np.loadtxt("ndep.asc"                     , skiprows=6)
nh3_spred_fer      = np.loadtxt("nh3_spread_fe.asc"            , skiprows=6)
nh3_spred_fer_ara  = np.loadtxt("nh3_spread_fe_crops.asc"      , skiprows=6)
nh3_spred_fer_igl  = np.loadtxt("nh3_spread_fe_grass_int.asc"  , skiprows=6)
nh3_spred_man      = np.loadtxt("nh3_spread_man.asc"           , skiprows=6)
nh3_spred_man_ara  = np.loadtxt("nh3_spread_man_crops.asc"     , skiprows=6)
nh3_spred_man_igl  = np.loadtxt("nh3_spread_man_grass_int.asc" , skiprows=6)
nh3_stor           = np.loadtxt("nh3_stor.asc"                 , skiprows=6)
nh3_graz           = np.loadtxt("nh3_graz.asc"                 , skiprows=6)
nh3_graz_igl       = np.loadtxt("nh3_graz_int.asc"             , skiprows=6)
regions            = np.loadtxt("image_region28.asc"           , skiprows=6)

### 1c. change NA values to NaN
#general
nfer_ag[nfer_ag==-9999]                   =np.nan
nman_ag[nman_ag==-9999]                   =np.nan
nox_em[nox_em==-9999]                     =np.nan
fag[fag==-1]                              =np.nan
fara[fara==-1]                            =np.nan
figl[figl==-1]                            =np.nan
fegl[fegl==-1]                            =np.nan

# egl
nman_egl[nman_egl==-9999]                 =np.nan
nh3_tot_egl[nh3_tot_egl==-9999]           =np.nan
nh3_stor_egl[nh3_stor_egl==-9999]         =np.nan

# ara
nfer_ara[nfer_ara==-9999]                         =np.nan
nman_ara[nman_ara==-9999]                         =np.nan
nman_crit_sw_ara[nman_crit_sw_ara==-9999]         =np.nan 
nfer_crit_sw_ara[nfer_crit_sw_ara==-9999]         =np.nan
nman_crit_gw_ara[nman_crit_gw_ara==-9999]         =np.nan
nfer_crit_gw_ara[nfer_crit_gw_ara==-9999]         =np.nan
nman_crit_de_ara[nman_crit_de_ara==-9999]         =np.nan
nfer_crit_de_ara[nfer_crit_de_ara==-9999]         =np.nan
frnfe_ara[frnfe_ara==-9999]                       =np.nan
nup_max_ara[nup_max_ara==-9999]                   =np.nan
nup_crit_sw_ara[nup_crit_sw_ara==-9999]           =np.nan
nup_crit_gw_ara[nup_crit_gw_ara==-9999]           =np.nan
nup_crit_dep_ara[nup_crit_dep_ara==-9999]         =np.nan
fnup_max_sw_ara[fnup_max_sw_ara==-9999]           =np.nan
fnup_max_gw_ara[fnup_max_gw_ara==-9999]           =np.nan
fnup_max_de_ara[fnup_max_de_ara==-9999]           =np.nan
fnup_corr_sw_ara[fnup_corr_sw_ara==-9999]         =np.nan
fnup_corr_gw_ara[fnup_corr_gw_ara==-9999]         =np.nan
fnup_corr_de_ara[fnup_corr_de_ara==-9999]         =np.nan
nue_ara[nue_ara==-9999]                           =np.nan
nh3_ef_man_ara[nh3_ef_man_ara==-9999]             =np.nan
nh3_ef_fer_ara[nh3_ef_fer_ara==-9999]             =np.nan
nin_max_ara[nin_max_ara==-9999]                   =np.nan
nin_tot_crit_sw_ara[nin_tot_crit_sw_ara==-9999]   =np.nan
nin_tot_crit_gw_ara[nin_tot_crit_gw_ara==-9999]   =np.nan
nin_tot_crit_dep_ara[nin_tot_crit_dep_ara==-9999] =np.nan
nh3_stor_ara[nh3_stor_ara==-9999]         =np.nan

# igl
nfer_igl[nfer_igl==-9999]                         =np.nan
nman_igl[nman_igl==-9999]                         =np.nan
nman_crit_sw_igl[nman_crit_sw_igl==-9999]         =np.nan 
nfer_crit_sw_igl[nfer_crit_sw_igl==-9999]         =np.nan
nman_crit_gw_igl[nman_crit_gw_igl==-9999]         =np.nan
nfer_crit_gw_igl[nfer_crit_gw_igl==-9999]         =np.nan
nman_crit_de_igl[nman_crit_de_igl==-9999]         =np.nan
nfer_crit_de_igl[nfer_crit_de_igl==-9999]         =np.nan
frnfe_igl[frnfe_igl==-9999]                       =np.nan
nup_max_igl[nup_max_igl==-9999]                   =np.nan
nup_crit_sw_igl[nup_crit_sw_igl==-9999]           =np.nan
nup_crit_gw_igl[nup_crit_gw_igl==-9999]           =np.nan
nup_crit_dep_igl[nup_crit_dep_igl==-9999]         =np.nan
fnup_max_sw_igl[fnup_max_sw_igl==-9999]           =np.nan
fnup_max_gw_igl[fnup_max_gw_igl==-9999]           =np.nan
fnup_max_de_igl[fnup_max_de_igl==-9999]           =np.nan
fnup_corr_sw_igl[fnup_corr_sw_igl==-9999]         =np.nan
fnup_corr_gw_igl[fnup_corr_gw_igl==-9999]         =np.nan
fnup_corr_de_igl[fnup_corr_de_igl==-9999]         =np.nan
nue_igl[nue_igl==-9999]                           =np.nan
nh3_ef_man_igl[nh3_ef_man_igl==-9999]             =np.nan
nh3_ef_fer_igl[nh3_ef_fer_igl==-9999]             =np.nan
nin_max_igl[nin_max_igl==-9999]                   =np.nan
nin_tot_crit_sw_igl[nin_tot_crit_sw_igl==-9999]   =np.nan
nin_tot_crit_gw_igl[nin_tot_crit_gw_igl==-9999]   =np.nan
nin_tot_crit_dep_igl[nin_tot_crit_dep_igl==-9999] =np.nan
nh3_stor_igl[nh3_stor_igl==-9999]         =np.nan

a_ag[a_ag==-1]                               =np.nan
a_ara[a_ara==-1]                             =np.nan
a_igl[a_igl==-1]                             =np.nan
a_egl[a_egl==-1]                             =np.nan
nfix_ag[nfix_ag==-9999]                            =np.nan
nfix_ara[nfix_ara==-9999]                    =np.nan
nfix_igl[nfix_igl==-9999]                    =np.nan
nfix_egl[nfix_egl==-9999]                    =np.nan
fgw_rec_ag[fgw_rec_ag==-9999]                =np.nan
fgw_rec_nat[fgw_rec_nat==-9999]              =np.nan
ndep[ndep==-1]                               =np.nan
nh3_spred_fer[nh3_spred_fer==-9999]          =np.nan
nh3_spred_fer_ara[nh3_spred_fer_ara==-9999]  =np.nan
nh3_spred_fer_igl[nh3_spred_fer_igl==-9999]  =np.nan
nh3_spred_man[nh3_spred_man==-9999]          =np.nan
nh3_spred_man_ara[nh3_spred_man_ara==-9999]  =np.nan
nh3_spred_man_igl[nh3_spred_man_igl==-9999]  =np.nan
nh3_stor[nh3_stor==-9999]                    =np.nan
nh3_graz[nh3_graz==-9999]                    =np.nan
nh3_graz_igl[nh3_graz_igl==-9999]            =np.nan
regions[regions==-9999]                      =np.nan

#######################################################################################################################################################################################################
# 2. Calculate CURRENT inputs from manure and fertilizer per hectare for each grid cell ###############################################################################################################
#######################################################################################################################################################################################################
 
with np.errstate(invalid='ignore'):
### 2a. all agricultural land
    manha_ag      = np.divide(nman_ag, a_ag)
    ferha_ag      = np.divide(nfer_ag, a_ag)
    manfer_ag     = np.add(nman_ag, nfer_ag)
    manferha_ag   = np.divide(manfer_ag, a_ag)
### 2b. cropland
    manha_ara     = np.divide(nman_ara, a_ara)
    ferha_ara     = np.divide(nfer_ara, a_ara)
    manfer_ara    = np.add(nman_ara, nfer_ara)
    manferha_ara  = np.divide(manfer_ara, a_ara)
### 2c. intensive + extensive grassland
    ferha_igl     = np.divide(nfer_igl, a_igl)
    manha_igl     = np.divide(nman_igl, a_igl)
    manha_egl     = np.divide(nman_egl, a_egl)
    manfer_igl    = np.add(nman_igl, nfer_igl)
    manferha_igl  = np.divide(manfer_igl, a_igl)

#######################################################################################################################################################################################################
# 3. Calculate CURRENT inputs from deposition due to NOx and NH3_egl for each grid cell ###############################################################################################################
#######################################################################################################################################################################################################
ndep_fixed      = np.add(nox_em, nh3_tot_egl)
ndep_fixed_ara  = np.multiply(ndep_fixed, fara)
ndep_fixed_igl  = np.multiply(ndep_fixed, figl)
ndep_fixed_egl  = np.multiply(ndep_fixed, fegl)
ndep_fixed_ag   = np.multiply(ndep_fixed, fag)

#######################################################################################################################################################################################################
# 4. Calculate maximum inputs from fertilizer and manure, and sum of the two for each grid cell #######################################################################################################
#######################################################################################################################################################################################################
# ara
print("nin_crit_max_1_ara:  %i kg N yr-1" %(np.nansum(nin_max_ara)))
# surface water
nman_crit_sw_max_ara = np.multiply(nman_crit_sw_ara, fnup_corr_sw_ara) 
nfer_crit_sw_max_ara = np.multiply(nfer_crit_sw_ara, fnup_corr_sw_ara) 
manfer_crit_sw_max_ara = np.add(nman_crit_sw_max_ara, nfer_crit_sw_max_ara)
# groundwater
nman_crit_gw_max_ara = np.multiply(nman_crit_gw_ara, fnup_corr_gw_ara) 
nfer_crit_gw_max_ara = np.multiply(nfer_crit_gw_ara, fnup_corr_gw_ara) 
manfer_crit_gw_max_ara = np.add(nman_crit_gw_max_ara, nfer_crit_gw_max_ara)
# deposition
nman_crit_de_max_ara = np.multiply(nman_crit_de_ara, fnup_corr_de_ara) 
nfer_crit_de_max_ara = np.multiply(nfer_crit_de_ara, fnup_corr_de_ara) 
manfer_crit_de_max_ara = np.add(nman_crit_de_max_ara, nfer_crit_de_max_ara)

# igl
print("nin_crit_max_1_igl:  %i kg N yr-1" %(np.nansum(nin_max_igl)))
# surface water
nman_crit_sw_max_igl = np.multiply(nman_crit_sw_igl, fnup_corr_sw_igl) 
nfer_crit_sw_max_igl = np.multiply(nfer_crit_sw_igl, fnup_corr_sw_igl) 
manfer_crit_sw_max_igl = np.add(nman_crit_sw_max_igl, nfer_crit_sw_max_igl)
# groundwater
nman_crit_gw_max_igl = np.multiply(nman_crit_gw_igl, fnup_corr_gw_igl) 
nfer_crit_gw_max_igl = np.multiply(nfer_crit_gw_igl, fnup_corr_gw_igl) 
manfer_crit_gw_max_igl = np.add(nman_crit_gw_max_igl, nfer_crit_gw_max_igl)
# deposition
nman_crit_de_max_igl = np.multiply(nman_crit_de_igl, fnup_corr_de_igl) 
nfer_crit_de_max_igl = np.multiply(nfer_crit_de_igl, fnup_corr_de_igl) 
manfer_crit_de_max_igl = np.add(nman_crit_de_max_igl, nfer_crit_de_max_igl)

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
with np.errstate(invalid='ignore'):
# ara
# fertilizer
    nfer_crit_sw_ara_ha = np.divide(nfer_crit_sw_ara, a_ara)
    nfer_crit_gw_ara_ha = np.divide(nfer_crit_gw_ara, a_ara)
    nfer_crit_de_ara_ha = np.divide(nfer_crit_de_ara, a_ara)
# manure
    nman_crit_sw_ara_ha = np.divide(nman_crit_sw_ara, a_ara)
    nman_crit_gw_ara_ha = np.divide(nman_crit_gw_ara, a_ara)
    nman_crit_de_ara_ha = np.divide(nman_crit_de_ara, a_ara)
# fertilizer+manure
    manfer_crit_sw_ara = np.add(nman_crit_sw_ara,nfer_crit_sw_ara)
    manfer_crit_gw_ara = np.add(nman_crit_gw_ara,nfer_crit_gw_ara)
    manfer_crit_de_ara = np.add(nman_crit_de_ara,nfer_crit_de_ara)
    manfer_crit_sw_ara_ha = np.divide(manfer_crit_sw_ara, a_ara)
    manfer_crit_gw_ara_ha = np.divide(manfer_crit_gw_ara, a_ara)
    manfer_crit_de_ara_ha = np.divide(manfer_crit_de_ara, a_ara)
# igl
# fertilizer
    nfer_crit_sw_igl_ha = np.divide(nfer_crit_sw_igl, a_igl)
    nfer_crit_gw_igl_ha = np.divide(nfer_crit_gw_igl, a_igl)
    nfer_crit_de_igl_ha = np.divide(nfer_crit_de_igl, a_igl)
# manure
    nman_crit_sw_igl_ha = np.divide(nman_crit_sw_igl, a_igl)
    nman_crit_gw_igl_ha = np.divide(nman_crit_gw_igl, a_igl)
    nman_crit_de_igl_ha = np.divide(nman_crit_de_igl, a_igl)
# fertilizer+manure
    manfer_crit_sw_igl = np.add(nman_crit_sw_igl,nfer_crit_sw_igl)
    manfer_crit_gw_igl = np.add(nman_crit_gw_igl,nfer_crit_gw_igl)
    manfer_crit_de_igl = np.add(nman_crit_de_igl,nfer_crit_de_igl)
    manfer_crit_sw_igl_ha = np.divide(manfer_crit_sw_igl, a_igl)
    manfer_crit_gw_igl_ha = np.divide(manfer_crit_gw_igl, a_igl)
    manfer_crit_de_igl_ha = np.divide(manfer_crit_de_igl, a_igl)


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
# ara
print("CASES-ARA")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(a_ara))
    print("case-1-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, manfer_crit_sw_ara<=0)) ]))
    print("case-3-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara>0,manfer_crit_sw_ara<=manfer_ara))) ]))
    print("case-4-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara>manfer_ara,manfer_crit_sw_ara<=manfer_crit_sw_max_ara))) ]))
    print("case-5-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara>manfer_ara,manfer_crit_sw_ara>manfer_crit_sw_max_ara))) ]))
  
    print("case-1-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, manfer_crit_gw_ara<=0)) ]))
    print("case-3-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara>0,manfer_crit_gw_ara<=manfer_ara))) ]))
    print("case-4-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara>manfer_ara,manfer_crit_gw_ara<=manfer_crit_gw_max_ara))) ]))
    print("case-5-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara>manfer_ara,manfer_crit_gw_ara>manfer_crit_gw_max_ara))) ]))
    
    print("case-1-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, manfer_crit_de_ara<=0)) ]))
    print("case-3-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara>0,manfer_crit_de_ara<=manfer_ara))) ]))
    print("case-4-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara>manfer_ara,manfer_crit_de_ara<=manfer_crit_de_max_ara))) ]))
    print("case-5-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara>manfer_ara,manfer_crit_de_ara>manfer_crit_de_max_ara))) ]))
    
    print("case-1-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_sw_ara<manfer_crit_de_ara, manfer_crit_sw_ara<=0)))) ]))
    print("case-3-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_sw_ara<manfer_crit_de_ara, np.logical_and(manfer_crit_sw_ara>0,manfer_crit_sw_ara<=manfer_ara))))) ]))
    print("case-4-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_sw_ara<manfer_crit_de_ara, np.logical_and(manfer_crit_sw_ara>manfer_ara,manfer_crit_sw_ara<=manfer_crit_sw_max_ara))))) ]))
    print("case-5-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_sw_ara)==False, np.logical_and(manfer_crit_sw_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_sw_ara<manfer_crit_de_ara, np.logical_and(manfer_crit_sw_ara>manfer_ara,manfer_crit_sw_ara>manfer_crit_sw_max_ara))))) ]))
    
    print("case-1-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_gw_ara<manfer_crit_de_ara, manfer_crit_gw_ara<=0)))) ]))
    print("case-3-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_gw_ara<manfer_crit_de_ara, np.logical_and(manfer_crit_gw_ara>0,manfer_crit_gw_ara<=manfer_ara))))) ]))
    print("case-4-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_gw_ara<manfer_crit_de_ara, np.logical_and(manfer_crit_gw_ara>manfer_ara,manfer_crit_gw_ara<=manfer_crit_gw_max_ara))))) ]))
    print("case-5-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_gw_ara)==False, np.logical_and(manfer_crit_gw_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_gw_ara<manfer_crit_de_ara, np.logical_and(manfer_crit_gw_ara>manfer_ara,manfer_crit_gw_ara>manfer_crit_gw_max_ara))))) ]))

    print("case-1-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_de_ara<manfer_crit_gw_ara, manfer_crit_de_ara<=0)))) ]))
    print("case-3-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_de_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_de_ara>0,manfer_crit_de_ara<=manfer_ara))))) ]))
    print("case-4-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_de_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_de_ara>manfer_ara,manfer_crit_de_ara<=manfer_crit_de_max_ara))))) ]))
    print("case-5-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(manfer_crit_de_ara)==False, np.logical_and(manfer_crit_de_ara<manfer_crit_sw_ara, np.logical_and(manfer_crit_de_ara<manfer_crit_gw_ara, np.logical_and(manfer_crit_de_ara>manfer_ara,manfer_crit_de_ara>manfer_crit_de_max_ara))))) ]))

# igl
print("CASES-IGL")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(a_igl))
    print("case-1-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, manfer_crit_sw_igl<=0)) ]))
    print("case-3-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl>0,manfer_crit_sw_igl<=manfer_igl))) ]))
    print("case-4-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl>manfer_igl,manfer_crit_sw_igl<=manfer_crit_sw_max_igl))) ]))
    print("case-5-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl>manfer_igl,manfer_crit_sw_igl>manfer_crit_sw_max_igl))) ]))
  
    print("case-1-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, manfer_crit_gw_igl<=0)) ]))
    print("case-3-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl>0,manfer_crit_gw_igl<=manfer_igl))) ]))
    print("case-4-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl>manfer_igl,manfer_crit_gw_igl<=manfer_crit_gw_max_igl))) ]))
    print("case-5-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl>manfer_igl,manfer_crit_gw_igl>manfer_crit_gw_max_igl))) ]))
    
    print("case-1-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, manfer_crit_de_igl<=0)) ]))
    print("case-3-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl>0,manfer_crit_de_igl<=manfer_igl))) ]))
    print("case-4-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl>manfer_igl,manfer_crit_de_igl<=manfer_crit_de_max_igl))) ]))
    print("case-5-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl>manfer_igl,manfer_crit_de_igl>manfer_crit_de_max_igl))) ]))
    
    print("case-1-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_sw_igl<manfer_crit_de_igl, manfer_crit_sw_igl<=0)))) ]))
    print("case-3-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_sw_igl<manfer_crit_de_igl, np.logical_and(manfer_crit_sw_igl>0,manfer_crit_sw_igl<=manfer_igl))))) ]))
    print("case-4-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_sw_igl<manfer_crit_de_igl, np.logical_and(manfer_crit_sw_igl>manfer_igl,manfer_crit_sw_igl<=manfer_crit_sw_max_igl))))) ]))
    print("case-5-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_sw_igl)==False, np.logical_and(manfer_crit_sw_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_sw_igl<manfer_crit_de_igl, np.logical_and(manfer_crit_sw_igl>manfer_igl,manfer_crit_sw_igl>manfer_crit_sw_max_igl))))) ]))
    
    print("case-1-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_gw_igl<manfer_crit_de_igl, manfer_crit_gw_igl<=0)))) ]))
    print("case-3-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_gw_igl<manfer_crit_de_igl, np.logical_and(manfer_crit_gw_igl>0,manfer_crit_gw_igl<=manfer_igl))))) ]))
    print("case-4-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_gw_igl<manfer_crit_de_igl, np.logical_and(manfer_crit_gw_igl>manfer_igl,manfer_crit_gw_igl<=manfer_crit_gw_max_igl))))) ]))
    print("case-5-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_gw_igl)==False, np.logical_and(manfer_crit_gw_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_gw_igl<manfer_crit_de_igl, np.logical_and(manfer_crit_gw_igl>manfer_igl,manfer_crit_gw_igl>manfer_crit_gw_max_igl))))) ]))

    print("case-1-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_de_igl<manfer_crit_gw_igl, manfer_crit_de_igl<=0)))) ]))
    print("case-3-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_de_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_de_igl>0,manfer_crit_de_igl<=manfer_igl))))) ]))
    print("case-4-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_de_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_de_igl>manfer_igl,manfer_crit_de_igl<=manfer_crit_de_max_igl))))) ]))
    print("case-5-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(manfer_crit_de_igl)==False, np.logical_and(manfer_crit_de_igl<manfer_crit_sw_igl, np.logical_and(manfer_crit_de_igl<manfer_crit_gw_igl, np.logical_and(manfer_crit_de_igl>manfer_igl,manfer_crit_de_igl>manfer_crit_de_max_igl))))) ]))    


#######################################################################################################################################################################################################
# 7. Print land areas + actual N inputs from fertilizer and manure ####################################################################################################################################
#######################################################################################################################################################################################################

### 7a. Areas
print("AREAS-PER-LAND-USE")
print("ag:       %i ha" %(np.nansum(a_ag)))
print("ara:      %i ha" %(np.nansum(a_ara)))
print("igl:      %i ha" %(np.nansum(a_igl)))
print("egl:      %i ha" %(np.nansum(a_egl)))
### 7b. Actual N inputs (totals)
print("TOTAL-ACTUAL-INPUTS")
print("Act-fer-tot-all:  %i kgNyr-1" %(np.nansum(nfer_ag)))
print("Act-fer-tot-ara:  %i kgNyr-1" %(np.nansum(nfer_ara)))
print("Act-fer-tot-igl:  %i kgNyr-1" %(np.nansum(nfer_igl)))
print("Act-fer-tot-egl:  %i kgNyr-1" % 0.0)
print("Act-man-tot-all:  %i kgNyr-1" %(np.nansum(nman_ag)))
print("Act-man-tot-ara:  %i kgNyr-1" %(np.nansum(nman_ara)))
print("Act-man-tot-igl:  %i kgNyr-1" %(np.nansum(nman_igl)))
print("Act-man-tot-egl:  %i kgNyr-1" %(np.nansum(nman_egl)))
print("Act-fer-man-tot-all:  %i kgNyr-1" %(np.nansum(manfer_ag)))
print("Act-fer-man-tot-ara:  %i kgNyr-1" %(np.nansum(manfer_ara)))
print("Act-fer-man-tot-igl:  %i kgNyr-1" %(np.nansum(manfer_igl)))
### 7c. Actual N inputs (per hectare)
print("ACTUAL-INPUTS-PER-HA")
print("Act-fer-ha-all:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_ag), np.nansum(a_ag[np.where(np.isnan(nfer_ag)==False)])))
print("Act-fer-ha-ara:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_ara), np.nansum(a_ara[np.where(np.isnan(nfer_ara)==False)])))
print("Act-fer-ha-igl:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_igl), np.nansum(a_igl[np.where(np.isnan(nfer_igl)==False)])))
print("Act-fer-ha-egl:        %.1f kgNha-1yr-1" % 0.0)
print("Act-man-ha-all:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_ag), np.nansum(a_ag[np.where(np.isnan(nman_ag)==False)])))
print("Act-man-ha-ara:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_ara), np.nansum(a_ara[np.where(np.isnan(nman_ara)==False)])))
print("Act-man-ha-igl:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_igl), np.nansum(a_igl[np.where(np.isnan(nman_igl)==False)])))
print("Act-man-ha-egl:        %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_egl), np.nansum(a_egl[np.where(np.isnan(nman_egl)==False)])))
print("Act-fer-man-ha-all:    %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_ag), np.nansum(a_ag[np.where(np.isnan(manfer_ag)==False)])))
print("Act-fer-man-ha-ara:    %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_ara), np.nansum(a_ara[np.where(np.isnan(manfer_ara)==False)])))
print("Act-fer-man-ha-igl:    %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_igl), np.nansum(a_igl[np.where(np.isnan(manfer_igl)==False)])))
print("Act-fer-man-ha-egl:    %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_egl), np.nansum(a_egl[np.where(np.isnan(nman_egl)==False)])))

'''

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

'''

# 2. for cut-off at maximum N input
# ara
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-NIN,MAX---ARA")
nfer_crit_sw_ara3 = np.copy(nfer_crit_sw_ara)
nman_crit_sw_ara3 = np.copy(nman_crit_sw_ara)
nfer_crit_gw_ara3 = np.copy(nfer_crit_gw_ara)
nman_crit_gw_ara3 = np.copy(nman_crit_gw_ara)
nfer_crit_de_ara3 = np.copy(nfer_crit_de_ara)
nman_crit_de_ara3 = np.copy(nman_crit_de_ara)
manfer_crit_sw_ara3 = np.copy(manfer_crit_sw_ara)
manfer_crit_gw_ara3 = np.copy(manfer_crit_gw_ara)
manfer_crit_de_ara3 = np.copy(manfer_crit_de_ara)

# replace negative values by zero
with np.errstate(invalid='ignore'):
    nfer_crit_sw_ara3[nfer_crit_sw_ara3<0]=0
    nman_crit_sw_ara3[nman_crit_sw_ara3<0]=0
    nfer_crit_gw_ara3[nfer_crit_gw_ara3<0]=0
    nman_crit_gw_ara3[nman_crit_gw_ara3<0]=0
    nfer_crit_de_ara3[nfer_crit_de_ara3<0]=0
    nman_crit_de_ara3[nman_crit_de_ara3<0]=0
    manfer_crit_sw_ara3[manfer_crit_sw_ara3<0]=0
    manfer_crit_gw_ara3[manfer_crit_gw_ara3<0]=0
    manfer_crit_de_ara3[manfer_crit_de_ara3<0]=0

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_ara)[0]):
        for j in range(np.shape(fnup_max_sw_ara)[1]):
            if (fnup_max_sw_ara[i,j] < 1 and np.isnan(fnup_max_sw_ara[i,j])==False):
                nfer_crit_sw_ara3[i,j] = nfer_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
                nman_crit_sw_ara3[i,j] = nman_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
                manfer_crit_sw_ara3[i,j] = nfer_crit_sw_ara3[i,j]+nman_crit_sw_ara3[i,j]       
    for i in range(np.shape(fnup_max_gw_ara)[0]):
        for j in range(np.shape(fnup_max_gw_ara)[1]):
            if (fnup_max_gw_ara[i,j] < 1 and np.isnan(fnup_max_gw_ara[i,j])==False):
                nfer_crit_gw_ara3[i,j] = nfer_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
                nman_crit_gw_ara3[i,j] = nman_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
                manfer_crit_gw_ara3[i,j] = nfer_crit_gw_ara3[i,j]+nman_crit_gw_ara3[i,j] 
    for i in range(np.shape(fnup_max_de_ara)[0]):
        for j in range(np.shape(fnup_max_de_ara)[1]):
            if (fnup_max_de_ara[i,j] < 1 and np.isnan(fnup_max_de_ara[i,j])==False):
                nfer_crit_de_ara3[i,j] = nfer_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]
                nman_crit_de_ara3[i,j] = nman_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]
                manfer_crit_de_ara3[i,j] = nfer_crit_de_ara3[i,j]+nman_crit_de_ara3[i,j] 

# select minimum
nfer_crit_min_ara3X    = np.minimum(nfer_crit_sw_ara3,     nfer_crit_gw_ara3)
nfer_crit_min_ara3     = np.minimum(nfer_crit_min_ara3X,   nfer_crit_de_ara3)
nman_crit_min_ara3X    = np.minimum(nman_crit_sw_ara3,     nman_crit_gw_ara3)
nman_crit_min_ara3     = np.minimum(nman_crit_min_ara3X,   nman_crit_de_ara3)
manfer_crit_min_ara3X  = np.minimum(manfer_crit_sw_ara3,   manfer_crit_gw_ara3)
manfer_crit_min_ara3   = np.minimum(manfer_crit_min_ara3X, manfer_crit_de_ara3)
# totals
print("Crit-fer-sw-3: %.1f" % np.nansum(nfer_crit_sw_ara3))
print("Crit-man-sw-3: %.1f" % np.nansum(nman_crit_sw_ara3))
print("Crit-fer-gw-3: %.1f" % np.nansum(nfer_crit_gw_ara3))
print("Crit-man-gw-3: %.1f" % np.nansum(nman_crit_gw_ara3))
print("Crit-fer-de-3: %.1f" % np.nansum(nfer_crit_de_ara3))
print("Crit-man-de-3: %.1f" % np.nansum(nman_crit_de_ara3))
print("Crit-nin-sw-3: %.1f" % np.nansum(manfer_crit_sw_ara3))
print("Crit-nin-gw-3: %.1f" % np.nansum(manfer_crit_gw_ara3)) 
print("Crit-nin-de-3: %.1f" % np.nansum(manfer_crit_de_ara3))
print("Crit-fer-mi-3: %.1f" % np.nansum(nfer_crit_min_ara3))
print("Crit-man-mi-3: %.1f" % np.nansum(nman_crit_min_ara3))
print("Crit-nin-mi-3: %.1f" % np.nansum(manfer_crit_min_ara3))
# areas
print("Crit-fer-sw-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nfer_crit_sw_ara3)    ==False)]))
print("Crit-man-sw-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_sw_ara3)    ==False)]))
print("Crit-fer-gw-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nfer_crit_gw_ara3)    ==False)]))
print("Crit-man-gw-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_gw_ara3)    ==False)]))
print("Crit-fer-de-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nfer_crit_de_ara3)    ==False)]))
print("Crit-man-de-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_de_ara3)    ==False)]))
print("Crit-nin-sw-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(manfer_crit_sw_ara3)  ==False)]))
print("Crit-nin-gw-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(manfer_crit_gw_ara3)  ==False)]))
print("Crit-nin-de-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(manfer_crit_de_ara3)  ==False)]))
print("Crit-fer-mi-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nfer_crit_min_ara3)   ==False)]))
print("Crit-man-mi-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_min_ara3)   ==False)]))
print("Crit-nin-mi-3-area: %.1f" % np.nansum(a_ara[np.where(np.isnan(manfer_crit_min_ara3) ==False)]))
# per hectare
print("Crit-fer-sw-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_sw_ara3),    np.nansum(a_ara[np.where(np.isnan(nfer_crit_sw_ara3)    ==False)])))
print("Crit-man-sw-ha-3: %.1f" % np.divide(np.nansum(nman_crit_sw_ara3),    np.nansum(a_ara[np.where(np.isnan(nman_crit_sw_ara3)    ==False)])))
print("Crit-fer-gw-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_gw_ara3),    np.nansum(a_ara[np.where(np.isnan(nfer_crit_gw_ara3)    ==False)])))
print("Crit-man-gw-ha-3: %.1f" % np.divide(np.nansum(nman_crit_gw_ara3),    np.nansum(a_ara[np.where(np.isnan(nman_crit_gw_ara3)    ==False)])))
print("Crit-fer-de-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_de_ara3),    np.nansum(a_ara[np.where(np.isnan(nfer_crit_de_ara3)    ==False)])))
print("Crit-man-de-ha-3: %.1f" % np.divide(np.nansum(nman_crit_de_ara3),    np.nansum(a_ara[np.where(np.isnan(nman_crit_de_ara3)    ==False)])))
print("Crit-nin-sw-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_sw_ara3),  np.nansum(a_ara[np.where(np.isnan(manfer_crit_sw_ara3)  ==False)])))
print("Crit-nin-gw-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_gw_ara3),  np.nansum(a_ara[np.where(np.isnan(manfer_crit_gw_ara3)  ==False)]))) 
print("Crit-nin-de-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_de_ara3),  np.nansum(a_ara[np.where(np.isnan(manfer_crit_de_ara3)  ==False)])))
print("Crit-fer-mi-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_min_ara3),   np.nansum(a_ara[np.where(np.isnan(nfer_crit_min_ara3)   ==False)])))
print("Crit-man-mi-ha-3: %.1f" % np.divide(np.nansum(nman_crit_min_ara3),   np.nansum(a_ara[np.where(np.isnan(nman_crit_min_ara3)   ==False)])))
print("Crit-nin-mi-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_min_ara3), np.nansum(a_ara[np.where(np.isnan(manfer_crit_min_ara3) ==False)])))

# igl
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-NIN,MAX---IGL")
nfer_crit_sw_igl3 = np.copy(nfer_crit_sw_igl)
nman_crit_sw_igl3 = np.copy(nman_crit_sw_igl)
nfer_crit_gw_igl3 = np.copy(nfer_crit_gw_igl)
nman_crit_gw_igl3 = np.copy(nman_crit_gw_igl)
nfer_crit_de_igl3 = np.copy(nfer_crit_de_igl)
nman_crit_de_igl3 = np.copy(nman_crit_de_igl)
manfer_crit_sw_igl3 = np.copy(manfer_crit_sw_igl)
manfer_crit_gw_igl3 = np.copy(manfer_crit_gw_igl)
manfer_crit_de_igl3 = np.copy(manfer_crit_de_igl)

# replace negative values by zero
with np.errstate(invalid='ignore'):
    nfer_crit_sw_igl3[nfer_crit_sw_igl3<0]=0
    nman_crit_sw_igl3[nman_crit_sw_igl3<0]=0
    nfer_crit_gw_igl3[nfer_crit_gw_igl3<0]=0
    nman_crit_gw_igl3[nman_crit_gw_igl3<0]=0
    nfer_crit_de_igl3[nfer_crit_de_igl3<0]=0
    nman_crit_de_igl3[nman_crit_de_igl3<0]=0
    manfer_crit_sw_igl3[manfer_crit_sw_igl3<0]=0
    manfer_crit_gw_igl3[manfer_crit_gw_igl3<0]=0
    manfer_crit_de_igl3[manfer_crit_de_igl3<0]=0

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_igl)[0]):
        for j in range(np.shape(fnup_max_sw_igl)[1]):
            if (fnup_max_sw_igl[i,j] < 1 and np.isnan(fnup_max_sw_igl[i,j])==False):
                nfer_crit_sw_igl3[i,j] = nfer_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
                nman_crit_sw_igl3[i,j] = nman_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
                manfer_crit_sw_igl3[i,j] = nfer_crit_sw_igl3[i,j]+nman_crit_sw_igl3[i,j]       
    for i in range(np.shape(fnup_max_gw_igl)[0]):
        for j in range(np.shape(fnup_max_gw_igl)[1]):
            if (fnup_max_gw_igl[i,j] < 1 and np.isnan(fnup_max_gw_igl[i,j])==False):
                nfer_crit_gw_igl3[i,j] = nfer_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
                nman_crit_gw_igl3[i,j] = nman_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
                manfer_crit_gw_igl3[i,j] = nfer_crit_gw_igl3[i,j]+nman_crit_gw_igl3[i,j] 
    for i in range(np.shape(fnup_max_de_igl)[0]):
        for j in range(np.shape(fnup_max_de_igl)[1]):
            if (fnup_max_de_igl[i,j] < 1 and np.isnan(fnup_max_de_igl[i,j])==False):
                nfer_crit_de_igl3[i,j] = nfer_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]
                nman_crit_de_igl3[i,j] = nman_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]
                manfer_crit_de_igl3[i,j] = nfer_crit_de_igl3[i,j]+nman_crit_de_igl3[i,j] 

# select minimum
nfer_crit_min_igl3X    = np.minimum(nfer_crit_sw_igl3,     nfer_crit_gw_igl3)
nfer_crit_min_igl3     = np.minimum(nfer_crit_min_igl3X,   nfer_crit_de_igl3)
nman_crit_min_igl3X    = np.minimum(nman_crit_sw_igl3,     nman_crit_gw_igl3)
nman_crit_min_igl3     = np.minimum(nman_crit_min_igl3X,   nman_crit_de_igl3)
manfer_crit_min_igl3X  = np.minimum(manfer_crit_sw_igl3,   manfer_crit_gw_igl3)
manfer_crit_min_igl3   = np.minimum(manfer_crit_min_igl3X, manfer_crit_de_igl3)

# totals
print("Crit-fer-sw-3: %.1f" % np.nansum(nfer_crit_sw_igl3))
print("Crit-man-sw-3: %.1f" % np.nansum(nman_crit_sw_igl3))
print("Crit-fer-gw-3: %.1f" % np.nansum(nfer_crit_gw_igl3))
print("Crit-man-gw-3: %.1f" % np.nansum(nman_crit_gw_igl3))
print("Crit-fer-de-3: %.1f" % np.nansum(nfer_crit_de_igl3))
print("Crit-man-de-3: %.1f" % np.nansum(nman_crit_de_igl3))
print("Crit-nin-sw-3: %.1f" % np.nansum(manfer_crit_sw_igl3))
print("Crit-nin-gw-3: %.1f" % np.nansum(manfer_crit_gw_igl3)) 
print("Crit-nin-de-3: %.1f" % np.nansum(manfer_crit_de_igl3))
print("Crit-fer-mi-3: %.1f" % np.nansum(nfer_crit_min_igl3))
print("Crit-man-mi-3: %.1f" % np.nansum(nman_crit_min_igl3))
print("Crit-nin-mi-3: %.1f" % np.nansum(manfer_crit_min_igl3))
# areas
print("Crit-fer-sw-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nfer_crit_sw_igl3)    ==False)]))
print("Crit-man-sw-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_sw_igl3)    ==False)]))
print("Crit-fer-gw-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nfer_crit_gw_igl3)    ==False)]))
print("Crit-man-gw-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_gw_igl3)    ==False)]))
print("Crit-fer-de-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nfer_crit_de_igl3)    ==False)]))
print("Crit-man-de-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_de_igl3)    ==False)]))
print("Crit-nin-sw-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(manfer_crit_sw_igl3)  ==False)]))
print("Crit-nin-gw-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(manfer_crit_gw_igl3)  ==False)]))
print("Crit-nin-de-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(manfer_crit_de_igl3)  ==False)]))
print("Crit-fer-mi-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nfer_crit_min_igl3)   ==False)]))
print("Crit-man-mi-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_min_igl3)   ==False)]))
print("Crit-nin-mi-3-area: %.1f" % np.nansum(a_igl[np.where(np.isnan(manfer_crit_min_igl3) ==False)]))
# per hectare
print("Crit-fer-sw-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_sw_igl3),    np.nansum(a_igl[np.where(np.isnan(nfer_crit_sw_igl3)    ==False)])))
print("Crit-man-sw-ha-3: %.1f" % np.divide(np.nansum(nman_crit_sw_igl3),    np.nansum(a_igl[np.where(np.isnan(nman_crit_sw_igl3)    ==False)])))
print("Crit-fer-gw-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_gw_igl3),    np.nansum(a_igl[np.where(np.isnan(nfer_crit_gw_igl3)    ==False)])))
print("Crit-man-gw-ha-3: %.1f" % np.divide(np.nansum(nman_crit_gw_igl3),    np.nansum(a_igl[np.where(np.isnan(nman_crit_gw_igl3)    ==False)])))
print("Crit-fer-de-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_de_igl3),    np.nansum(a_igl[np.where(np.isnan(nfer_crit_de_igl3)    ==False)])))
print("Crit-man-de-ha-3: %.1f" % np.divide(np.nansum(nman_crit_de_igl3),    np.nansum(a_igl[np.where(np.isnan(nman_crit_de_igl3)    ==False)])))
print("Crit-nin-sw-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_sw_igl3),  np.nansum(a_igl[np.where(np.isnan(manfer_crit_sw_igl3)  ==False)])))
print("Crit-nin-gw-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_gw_igl3),  np.nansum(a_igl[np.where(np.isnan(manfer_crit_gw_igl3)  ==False)]))) 
print("Crit-nin-de-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_de_igl3),  np.nansum(a_igl[np.where(np.isnan(manfer_crit_de_igl3)  ==False)])))
print("Crit-fer-mi-ha-3: %.1f" % np.divide(np.nansum(nfer_crit_min_igl3),   np.nansum(a_igl[np.where(np.isnan(nfer_crit_min_igl3)   ==False)])))
print("Crit-man-mi-ha-3: %.1f" % np.divide(np.nansum(nman_crit_min_igl3),   np.nansum(a_igl[np.where(np.isnan(nman_crit_min_igl3)   ==False)])))
print("Crit-nin-mi-ha-3: %.1f" % np.divide(np.nansum(manfer_crit_min_igl3), np.nansum(a_igl[np.where(np.isnan(manfer_crit_min_igl3) ==False)])))


# add N fixation and N deposition to output
## actual N fixation
#totals
print("Act-fix-tot-all:  %i kgNyr-1" %(np.nansum(nfix_ag)))
print("Act-fix-tot-ara:  %i kgNyr-1" %(np.nansum(nfix_ara)))
print("Act-fix-tot-igl:  %i kgNyr-1" %(np.nansum(nfix_igl)))
print("Act-fix-tot-egl:  %i kgNyr-1" %(np.nansum(nfix_egl)))
# per ha
print("Act-fix-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_ag),  np.nansum(a_ag[np.where(np.isnan(nfix_ag)==False)])))
print("Act-fix-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_ara), np.nansum(a_ara[np.where(np.isnan(nfix_ara)==False)])))
print("Act-fix-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_igl), np.nansum(a_igl[np.where(np.isnan(nfix_igl)==False)])))
print("Act-fix-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfix_egl), np.nansum(a_egl[np.where(np.isnan(nfix_egl)==False)])))
## actual N deposition from NOx emissions and NH3 from extensive grazing
#totals
print("Act-dep-fixed-tot-all:  %i kgNyr-1" %(np.nansum(ndep_fixed_ag)))
print("Act-dep-fixed-tot-ara:  %i kgNyr-1" %(np.nansum(ndep_fixed_ara)))
print("Act-dep-fixed-tot-igl:  %i kgNyr-1" %(np.nansum(ndep_fixed_igl)))
print("Act-dep-fixed-tot-egl:  %i kgNyr-1" %(np.nansum(ndep_fixed_egl)))
# per ha
print("Act-dep-fixed-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_ag),  np.nansum(a_ag[np.where(np.isnan(ndep_fixed_ag)==False)])))
print("Act-dep-fixed-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_ara), np.nansum(a_ara[np.where(np.isnan(ndep_fixed_ara)==False)])))
print("Act-dep-fixed-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_igl), np.nansum(a_igl[np.where(np.isnan(ndep_fixed_igl)==False)])))
print("Act-dep-fixed-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_fixed_egl), np.nansum(a_egl[np.where(np.isnan(ndep_fixed_egl)==False)])))


## Variable N deposition at actual and critical N inputs (for cutoff @ Nup,max)
# totals
ndep_var_act = np.add(nh3_spred_fer_ara, nh3_spred_fer_igl)
ndep_var_act = np.add(ndep_var_act, nh3_spred_man_ara)
ndep_var_act = np.add(ndep_var_act, nh3_spred_man_igl)
ndep_var_act = np.add(ndep_var_act, nh3_graz_igl)
ndep_var_act = np.add(ndep_var_act, nh3_stor_ara)    
ndep_var_act = np.add(ndep_var_act, nh3_stor_igl)

ndep_var_act_ag = np.multiply(ndep_var_act, fag)
ndep_var_act_ara = np.multiply(ndep_var_act, fara)
ndep_var_act_igl = np.multiply(ndep_var_act, figl)
ndep_var_act_egl = np.multiply(ndep_var_act, fegl)

print("Act-dep-var-tot-all:  %i kgNyr-1" %(np.nansum(ndep_var_act_ag)))
print("Act-dep-var-tot-ara:  %i kgNyr-1" %(np.nansum(ndep_var_act_ara)))
print("Act-dep-var-tot-igl:  %i kgNyr-1" %(np.nansum(ndep_var_act_igl)))
print("Act-dep-var-tot-egl:  %i kgNyr-1" %(np.nansum(ndep_var_act_egl)))
# per ha
print("Act-dep-var-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_ag),  np.nansum(a_ag[np.where(np.isnan(ndep_var_act_ag)==False)])))
print("Act-dep-var-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_ara), np.nansum(a_ara[np.where(np.isnan(ndep_var_act_ara)==False)])))
print("Act-dep-var-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_igl), np.nansum(a_igl[np.where(np.isnan(ndep_var_act_igl)==False)])))
print("Act-dep-var-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(ndep_var_act_egl), np.nansum(a_egl[np.where(np.isnan(ndep_var_act_egl)==False)])))

# variable NH3 emissions at critical N inputs (after cutoff)
# ara
ndep_var_crit_fer_sw_ara3 = np.multiply(nfer_crit_sw_ara3, nh3_ef_fer_ara)
ndep_var_crit_man_sw_ara3 = np.multiply(nman_crit_sw_ara3, nh3_ef_man_ara)
ndep_var_crit_tot_sw_ara3 = np.add(ndep_var_crit_fer_sw_ara3, ndep_var_crit_man_sw_ara3)
ndep_var_crit_fer_gw_ara3 = np.multiply(nfer_crit_gw_ara3, nh3_ef_fer_ara)
ndep_var_crit_man_gw_ara3 = np.multiply(nman_crit_gw_ara3, nh3_ef_man_ara)
ndep_var_crit_tot_gw_ara3 = np.add(ndep_var_crit_fer_gw_ara3, ndep_var_crit_man_gw_ara3)
ndep_var_crit_fer_de_ara3 = np.multiply(nfer_crit_de_ara3, nh3_ef_fer_ara)
ndep_var_crit_man_de_ara3 = np.multiply(nman_crit_de_ara3, nh3_ef_man_ara)
ndep_var_crit_tot_de_ara3 = np.add(ndep_var_crit_fer_de_ara3, ndep_var_crit_man_de_ara3)
ndep_var_crit_fer_min_ara3 = np.multiply(nfer_crit_min_ara3, nh3_ef_fer_ara)
ndep_var_crit_man_min_ara3 = np.multiply(nman_crit_min_ara3, nh3_ef_man_ara)
ndep_var_crit_tot_min_ara3 = np.add(ndep_var_crit_fer_min_ara3, ndep_var_crit_man_min_ara3)
# igl
ndep_var_crit_fer_sw_igl3 = np.multiply(nfer_crit_sw_igl3, nh3_ef_fer_igl)
ndep_var_crit_man_sw_igl3 = np.multiply(nman_crit_sw_igl3, nh3_ef_man_igl)
ndep_var_crit_tot_sw_igl3 = np.add(ndep_var_crit_fer_sw_igl3, ndep_var_crit_man_sw_igl3)
ndep_var_crit_fer_gw_igl3 = np.multiply(nfer_crit_gw_igl3, nh3_ef_fer_igl)
ndep_var_crit_man_gw_igl3 = np.multiply(nman_crit_gw_igl3, nh3_ef_man_igl)
ndep_var_crit_tot_gw_igl3 = np.add(ndep_var_crit_fer_gw_igl3, ndep_var_crit_man_gw_igl3)
ndep_var_crit_fer_de_igl3 = np.multiply(nfer_crit_de_igl3, nh3_ef_fer_igl)
ndep_var_crit_man_de_igl3 = np.multiply(nman_crit_de_igl3, nh3_ef_man_igl)
ndep_var_crit_tot_de_igl3 = np.add(ndep_var_crit_fer_de_igl3, ndep_var_crit_man_de_igl3)
ndep_var_crit_fer_min_igl3 = np.multiply(nfer_crit_min_igl3, nh3_ef_fer_igl)
ndep_var_crit_man_min_igl3 = np.multiply(nman_crit_min_igl3, nh3_ef_man_igl)
ndep_var_crit_tot_min_igl3 = np.add(ndep_var_crit_fer_min_igl3, ndep_var_crit_man_min_igl3)

# total variable deposition 
ndep_var_crit_tot_sw3 = np.add(ndep_var_crit_tot_sw_ara3, ndep_var_crit_tot_sw_igl3)
ndep_var_crit_tot_gw3 = np.add(ndep_var_crit_tot_gw_ara3, ndep_var_crit_tot_gw_igl3)
ndep_var_crit_tot_de3 = np.add(ndep_var_crit_tot_de_ara3, ndep_var_crit_tot_de_igl3)
ndep_var_crit_tot_min3 = np.add(ndep_var_crit_tot_min_ara3, ndep_var_crit_tot_min_igl3)

# to ara
ndep_var_crit_tot_sw3_ara = np.multiply(ndep_var_crit_tot_sw3, fara)
ndep_var_crit_tot_gw3_ara = np.multiply(ndep_var_crit_tot_gw3, fara)
ndep_var_crit_tot_de3_ara = np.multiply(ndep_var_crit_tot_de3, fara)
ndep_var_crit_tot_min3_ara = np.multiply(ndep_var_crit_tot_min3, fara)
# to igl
ndep_var_crit_tot_sw3_igl = np.multiply(ndep_var_crit_tot_sw3, figl)
ndep_var_crit_tot_gw3_igl = np.multiply(ndep_var_crit_tot_gw3, figl)
ndep_var_crit_tot_de3_igl = np.multiply(ndep_var_crit_tot_de3, figl)
ndep_var_crit_tot_min3_igl = np.multiply(ndep_var_crit_tot_min3, figl)

print("Crit-dep-var-sw-3-ara: %.1f" % np.nansum(ndep_var_crit_tot_sw3_ara))
print("Crit-dep-var-gw-3-ara: %.1f" % np.nansum(ndep_var_crit_tot_gw3_ara))
print("Crit-dep-var-de-3-ara: %.1f" % np.nansum(ndep_var_crit_tot_de3_ara))
print("Crit-dep-var-mi-3-ara: %.1f" % np.nansum(ndep_var_crit_tot_min3_ara))

print("Crit-dep-var-sw-3-igl: %.1f" % np.nansum(ndep_var_crit_tot_sw3_igl))
print("Crit-dep-var-gw-3-igl: %.1f" % np.nansum(ndep_var_crit_tot_gw3_igl))
print("Crit-dep-var-de-3-igl: %.1f" % np.nansum(ndep_var_crit_tot_de3_igl))
print("Crit-dep-var-mi-3-igl: %.1f" % np.nansum(ndep_var_crit_tot_min3_igl))

print("Crit-dep-var-sw-ha-3-ara: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_sw3_ara), np.nansum(a_ara[np.where(np.isnan(ndep_var_crit_tot_sw3_ara)==False)])))
print("Crit-dep-var-gw-ha-3-ara: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_gw3_ara), np.nansum(a_ara[np.where(np.isnan(ndep_var_crit_tot_gw3_ara)==False)])))
print("Crit-dep-var-de-ha-3-ara: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_de3_ara), np.nansum(a_ara[np.where(np.isnan(ndep_var_crit_tot_de3_ara)==False)])))
print("Crit-dep-var-mi-ha-3-ara: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_min3_ara), np.nansum(a_ara[np.where(np.isnan(ndep_var_crit_tot_min3_ara)==False)])))

print("Crit-dep-var-sw-ha-3-igl: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_sw3_igl), np.nansum(a_igl[np.where(np.isnan(ndep_var_crit_tot_sw3_igl)==False)])))
print("Crit-dep-var-gw-ha-3-igl: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_gw3_igl), np.nansum(a_igl[np.where(np.isnan(ndep_var_crit_tot_gw3_igl)==False)])))
print("Crit-dep-var-de-ha-3-igl: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_de3_igl), np.nansum(a_igl[np.where(np.isnan(ndep_var_crit_tot_de3_igl)==False)])))
print("Crit-dep-var-mi-ha-3-igl: %.1f" % np.divide(np.nansum(ndep_var_crit_tot_min3_igl), np.nansum(a_igl[np.where(np.isnan(ndep_var_crit_tot_min3_igl)==False)])))

# Total actual N inputs 
# ara
nin_tot_ara = np.add(manfer_ara, nfix_ara)
nin_tot_ara = np.add(nin_tot_ara, ndep_fixed_ara)
nin_tot_ara = np.add(nin_tot_ara, ndep_var_act_ara)
# igl
nin_tot_igl = np.add(manfer_igl, nfix_igl)
nin_tot_igl = np.add(nin_tot_igl, ndep_fixed_igl)
nin_tot_igl = np.add(nin_tot_igl, ndep_var_act_igl)

# Total critical N inputs after cutoff
# ara
nin_tot_crit_sw_cutoff_ara = np.add(nfer_crit_sw_ara3, nman_crit_sw_ara3)
nin_tot_crit_sw_cutoff_ara = np.add(nin_tot_crit_sw_cutoff_ara, nfix_ara)
nin_tot_crit_sw_cutoff_ara = np.add(nin_tot_crit_sw_cutoff_ara, ndep_fixed_ara)
nin_tot_crit_sw_cutoff_ara = np.add(nin_tot_crit_sw_cutoff_ara, ndep_var_crit_tot_sw3_ara)
nin_tot_crit_gw_cutoff_ara = np.add(nfer_crit_gw_ara3, nman_crit_gw_ara3)
nin_tot_crit_gw_cutoff_ara = np.add(nin_tot_crit_gw_cutoff_ara, nfix_ara)
nin_tot_crit_gw_cutoff_ara = np.add(nin_tot_crit_gw_cutoff_ara, ndep_fixed_ara)
nin_tot_crit_gw_cutoff_ara = np.add(nin_tot_crit_gw_cutoff_ara, ndep_var_crit_tot_gw3_ara)
nin_tot_crit_de_cutoff_ara = np.add(nfer_crit_de_ara3, nman_crit_de_ara3)
nin_tot_crit_de_cutoff_ara = np.add(nin_tot_crit_de_cutoff_ara, nfix_ara)
nin_tot_crit_de_cutoff_ara = np.add(nin_tot_crit_de_cutoff_ara, ndep_fixed_ara)
nin_tot_crit_de_cutoff_ara = np.add(nin_tot_crit_de_cutoff_ara, ndep_var_crit_tot_de3_ara)
nin_tot_crit_min_cutoff_ara = np.add(nfer_crit_min_ara3, nman_crit_min_ara3)
nin_tot_crit_min_cutoff_ara = np.add(nin_tot_crit_min_cutoff_ara, nfix_ara)
nin_tot_crit_min_cutoff_ara = np.add(nin_tot_crit_min_cutoff_ara, ndep_fixed_ara)
nin_tot_crit_min_cutoff_ara = np.add(nin_tot_crit_min_cutoff_ara, ndep_var_crit_tot_min3_ara)

print("CASES-FOR-*ALL*-INPUTS---ARA")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(a_ara))
    print("case-1-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, nin_tot_crit_sw_ara<=0)) ]))
    print("case-3-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara>0,nin_tot_crit_sw_ara<=nin_tot_ara))) ]))
    print("case-4-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara>nin_tot_ara,nin_tot_crit_sw_ara<=nin_max_ara))) ]))
    print("case-5-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara>nin_tot_ara,nin_tot_crit_sw_ara>nin_max_ara))) ]))
  
    print("case-1-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, nin_tot_crit_gw_ara<=0)) ]))
    print("case-3-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara>0,nin_tot_crit_gw_ara<=nin_tot_ara))) ]))
    print("case-4-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara>nin_tot_ara,nin_tot_crit_gw_ara<=nin_max_ara))) ]))
    print("case-5-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara>nin_tot_ara,nin_tot_crit_gw_ara>nin_max_ara))) ]))
      
    print("case-1-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, nin_tot_crit_dep_ara<=0)) ]))
    print("case-3-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara>0,nin_tot_crit_dep_ara<=nin_tot_ara))) ]))
    print("case-4-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara>nin_tot_ara,nin_tot_crit_dep_ara<=nin_max_ara))) ]))
    print("case-5-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara>nin_tot_ara,nin_tot_crit_dep_ara>nin_max_ara))) ]))

    print("case-1-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_dep_ara, nin_tot_crit_sw_ara<=0)))) ]))
    print("case-3-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_dep_ara, np.logical_and(nin_tot_crit_sw_ara>0,nin_tot_crit_sw_ara<=nin_tot_ara))))) ]))
    print("case-4-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_dep_ara, np.logical_and(nin_tot_crit_sw_ara>nin_tot_ara,nin_tot_crit_sw_ara<=nin_max_ara))))) ]))
    print("case-5-mi-sw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_ara)==False, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_sw_ara<nin_tot_crit_dep_ara, np.logical_and(nin_tot_crit_sw_ara>nin_tot_ara,nin_tot_crit_sw_ara>nin_max_ara))))) ]))
    
    print("case-1-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_dep_ara, nin_tot_crit_gw_ara<=0)))) ]))
    print("case-3-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_dep_ara, np.logical_and(nin_tot_crit_gw_ara>0,nin_tot_crit_gw_ara<=nin_tot_ara))))) ]))
    print("case-4-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_dep_ara, np.logical_and(nin_tot_crit_gw_ara>nin_tot_ara,nin_tot_crit_gw_ara<=nin_max_ara))))) ]))
    print("case-5-mi-gw: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_ara)==False, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_gw_ara<nin_tot_crit_dep_ara, np.logical_and(nin_tot_crit_gw_ara>nin_tot_ara,nin_tot_crit_gw_ara>nin_max_ara))))) ]))

    print("case-1-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_gw_ara, nin_tot_crit_dep_ara<=0)))) ]))
    print("case-3-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_dep_ara>0,nin_tot_crit_dep_ara<=nin_tot_ara))))) ]))
    print("case-4-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_dep_ara>nin_tot_ara,nin_tot_crit_dep_ara<=nin_max_ara))))) ]))
    print("case-5-mi-de: %i" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_ara)==False, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_sw_ara, np.logical_and(nin_tot_crit_dep_ara<nin_tot_crit_gw_ara, np.logical_and(nin_tot_crit_dep_ara>nin_tot_ara,nin_tot_crit_dep_ara>nin_max_ara))))) ]))

# igl
nin_tot_crit_sw_cutoff_igl = np.add(nfer_crit_sw_igl3, nman_crit_sw_igl3)
nin_tot_crit_sw_cutoff_igl = np.add(nin_tot_crit_sw_cutoff_igl, nfix_igl)
nin_tot_crit_sw_cutoff_igl = np.add(nin_tot_crit_sw_cutoff_igl, ndep_fixed_igl)
nin_tot_crit_sw_cutoff_igl = np.add(nin_tot_crit_sw_cutoff_igl, ndep_var_crit_tot_sw3_igl)
nin_tot_crit_gw_cutoff_igl = np.add(nfer_crit_gw_igl3, nman_crit_gw_igl3)
nin_tot_crit_gw_cutoff_igl = np.add(nin_tot_crit_gw_cutoff_igl, nfix_igl)
nin_tot_crit_gw_cutoff_igl = np.add(nin_tot_crit_gw_cutoff_igl, ndep_fixed_igl)
nin_tot_crit_gw_cutoff_igl = np.add(nin_tot_crit_gw_cutoff_igl, ndep_var_crit_tot_gw3_igl)
nin_tot_crit_de_cutoff_igl = np.add(nfer_crit_de_igl3, nman_crit_de_igl3)
nin_tot_crit_de_cutoff_igl = np.add(nin_tot_crit_de_cutoff_igl, nfix_igl)
nin_tot_crit_de_cutoff_igl = np.add(nin_tot_crit_de_cutoff_igl, ndep_fixed_igl)
nin_tot_crit_de_cutoff_igl = np.add(nin_tot_crit_de_cutoff_igl, ndep_var_crit_tot_de3_igl)
nin_tot_crit_min_cutoff_igl = np.add(nfer_crit_min_igl3, nman_crit_min_igl3)
nin_tot_crit_min_cutoff_igl = np.add(nin_tot_crit_min_cutoff_igl, nfix_igl)
nin_tot_crit_min_cutoff_igl = np.add(nin_tot_crit_min_cutoff_igl, ndep_fixed_igl)
nin_tot_crit_min_cutoff_igl = np.add(nin_tot_crit_min_cutoff_igl, ndep_var_crit_tot_min3_igl)

print("CASES-FOR-*ALL*-INPUTS---ARA")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(a_igl))
    print("case-1-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, nin_tot_crit_sw_igl<=0)) ]))
    print("case-3-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl>0,nin_tot_crit_sw_igl<=nin_tot_igl))) ]))
    print("case-4-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl>nin_tot_igl,nin_tot_crit_sw_igl<=nin_max_igl))) ]))
    print("case-5-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl>nin_tot_igl,nin_tot_crit_sw_igl>nin_max_igl))) ]))
  
    print("case-1-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, nin_tot_crit_gw_igl<=0)) ]))
    print("case-3-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl>0,nin_tot_crit_gw_igl<=nin_tot_igl))) ]))
    print("case-4-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl>nin_tot_igl,nin_tot_crit_gw_igl<=nin_max_igl))) ]))
    print("case-5-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl>nin_tot_igl,nin_tot_crit_gw_igl>nin_max_igl))) ]))
      
    print("case-1-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, nin_tot_crit_dep_igl<=0)) ]))
    print("case-3-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl>0,nin_tot_crit_dep_igl<=nin_tot_igl))) ]))
    print("case-4-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl>nin_tot_igl,nin_tot_crit_dep_igl<=nin_max_igl))) ]))
    print("case-5-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl>nin_tot_igl,nin_tot_crit_dep_igl>nin_max_igl))) ]))

    print("case-1-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_dep_igl, nin_tot_crit_sw_igl<=0)))) ]))
    print("case-3-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_dep_igl, np.logical_and(nin_tot_crit_sw_igl>0,nin_tot_crit_sw_igl<=nin_tot_igl))))) ]))
    print("case-4-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_dep_igl, np.logical_and(nin_tot_crit_sw_igl>nin_tot_igl,nin_tot_crit_sw_igl<=nin_max_igl))))) ]))
    print("case-5-mi-sw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_sw_igl)==False, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_sw_igl<nin_tot_crit_dep_igl, np.logical_and(nin_tot_crit_sw_igl>nin_tot_igl,nin_tot_crit_sw_igl>nin_max_igl))))) ]))
    
    print("case-1-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_dep_igl, nin_tot_crit_gw_igl<=0)))) ]))
    print("case-3-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_dep_igl, np.logical_and(nin_tot_crit_gw_igl>0,nin_tot_crit_gw_igl<=nin_tot_igl))))) ]))
    print("case-4-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_dep_igl, np.logical_and(nin_tot_crit_gw_igl>nin_tot_igl,nin_tot_crit_gw_igl<=nin_max_igl))))) ]))
    print("case-5-mi-gw: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_gw_igl)==False, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_gw_igl<nin_tot_crit_dep_igl, np.logical_and(nin_tot_crit_gw_igl>nin_tot_igl,nin_tot_crit_gw_igl>nin_max_igl))))) ]))

    print("case-1-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_gw_igl, nin_tot_crit_dep_igl<=0)))) ]))
    print("case-3-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_dep_igl>0,nin_tot_crit_dep_igl<=nin_tot_igl))))) ]))
    print("case-4-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_dep_igl>nin_tot_igl,nin_tot_crit_dep_igl<=nin_max_igl))))) ]))
    print("case-5-mi-de: %i" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nin_tot_crit_dep_igl)==False, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_sw_igl, np.logical_and(nin_tot_crit_dep_igl<nin_tot_crit_gw_igl, np.logical_and(nin_tot_crit_dep_igl>nin_tot_igl,nin_tot_crit_dep_igl>nin_max_igl))))) ]))





