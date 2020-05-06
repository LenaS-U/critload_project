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
nox_em           = np.loadtxt("nox_em.asc"               , skiprows=6)
fag              = np.loadtxt("fag.asc"                  , skiprows=6)
fara             = np.loadtxt("fara.asc"                 , skiprows=6)
figl             = np.loadtxt("figl.asc"                 , skiprows=6)
fegl             = np.loadtxt("fegl.asc"                 , skiprows=6)
# egl
nman_egl             = np.loadtxt("nman_egl.asc"            , skiprows=6)
nh3_tot_egl          = np.loadtxt("nh3_tot_egl.asc"         , skiprows=6)
# ara
nfer_ara             = np.loadtxt("nfer_ara.asc"            , skiprows=6)
nman_ara             = np.loadtxt("nman_ara.asc"            , skiprows=6)
nman_crit_sw_ara     = np.loadtxt("nman_crit_sw_ara.asc"    , skiprows=6)
nfer_crit_sw_ara     = np.loadtxt("nfer_crit_sw_ara.asc"    , skiprows=6)
nman_crit_gw_ara     = np.loadtxt("nman_crit_gw_ara.asc"    , skiprows=6)
nfer_crit_gw_ara     = np.loadtxt("nfer_crit_gw_ara.asc"    , skiprows=6)
nman_crit_de_ara     = np.loadtxt("nman_crit_dep_ara.asc"   , skiprows=6)
nfer_crit_de_ara     = np.loadtxt("nfer_crit_dep_ara.asc"   , skiprows=6)
fnup_max_sw_ara      = np.loadtxt("fnup_max_sw_ara.asc"     , skiprows=6)
fnup_max_gw_ara      = np.loadtxt("fnup_max_gw_ara.asc"     , skiprows=6)
fnup_max_de_ara      = np.loadtxt("fnup_max_dep_ara.asc"    , skiprows=6)
fnup_corr_sw_ara     = np.loadtxt("fnup_corr_sw_ara.asc"    , skiprows=6)
fnup_corr_gw_ara     = np.loadtxt("fnup_corr_gw_ara.asc"    , skiprows=6)
fnup_corr_de_ara     = np.loadtxt("fnup_corr_dep_ara.asc"   , skiprows=6)
nh3_ef_man_ara       = np.loadtxt("nh3_ef_man_ara.asc"      , skiprows=6)
nh3_ef_fer_ara       = np.loadtxt("nh3_ef_fer_ara.asc"      , skiprows=6)
nin_max_ara          = np.loadtxt("nin_max_ara.asc"         , skiprows=6)
nin_tot_crit_sw_ara  = np.loadtxt("nin_crit_sw_ara.asc"     , skiprows=6)
nin_tot_crit_gw_ara  = np.loadtxt("nin_crit_gw_ara.asc"     , skiprows=6)
nin_tot_crit_dep_ara = np.loadtxt("nin_crit_dep_ara.asc"    , skiprows=6)
nh3_stor_ara         = np.loadtxt("nh3_stor_ara.asc"        , skiprows=6)
nman_fer_crit_sw_ara = np.loadtxt("nman_fer_crit_sw_ara.asc"        , skiprows=6)
nman_fer_crit_gw_ara = np.loadtxt("nman_fer_crit_gw_ara.asc"        , skiprows=6)
nman_fer_crit_de_ara = np.loadtxt("nman_fer_crit_dep_ara.asc"       , skiprows=6)
# igl
nfer_igl             = np.loadtxt("nfer_igl.asc"            , skiprows=6)
nman_igl             = np.loadtxt("nman_igl.asc"            , skiprows=6)
nman_crit_sw_igl     = np.loadtxt("nman_crit_sw_igl.asc"    , skiprows=6)
nfer_crit_sw_igl     = np.loadtxt("nfer_crit_sw_igl.asc"    , skiprows=6)
nman_crit_gw_igl     = np.loadtxt("nman_crit_gw_igl.asc"    , skiprows=6)
nfer_crit_gw_igl     = np.loadtxt("nfer_crit_gw_igl.asc"    , skiprows=6)
nman_crit_de_igl     = np.loadtxt("nman_crit_dep_igl.asc"   , skiprows=6)
nfer_crit_de_igl     = np.loadtxt("nfer_crit_dep_igl.asc"   , skiprows=6)
fnup_max_sw_igl      = np.loadtxt("fnup_max_sw_igl.asc"     , skiprows=6)
fnup_max_gw_igl      = np.loadtxt("fnup_max_gw_igl.asc"     , skiprows=6)
fnup_max_de_igl      = np.loadtxt("fnup_max_dep_igl.asc"    , skiprows=6)
fnup_corr_sw_igl     = np.loadtxt("fnup_corr_sw_igl.asc"    , skiprows=6)
fnup_corr_gw_igl     = np.loadtxt("fnup_corr_gw_igl.asc"    , skiprows=6)
fnup_corr_de_igl     = np.loadtxt("fnup_corr_dep_igl.asc"   , skiprows=6)
nh3_ef_man_igl       = np.loadtxt("nh3_ef_man_igl.asc"      , skiprows=6)
nh3_ef_fer_igl       = np.loadtxt("nh3_ef_fer_igl.asc"      , skiprows=6)
nin_max_igl          = np.loadtxt("nin_max_igl.asc"         , skiprows=6)
nin_tot_crit_sw_igl  = np.loadtxt("nin_crit_sw_igl.asc"     , skiprows=6)
nin_tot_crit_gw_igl  = np.loadtxt("nin_crit_gw_igl.asc"     , skiprows=6)
nin_tot_crit_dep_igl = np.loadtxt("nin_crit_dep_igl.asc"    , skiprows=6)
nh3_stor_igl         = np.loadtxt("nh3_stor_igl.asc"        , skiprows=6)
nman_fer_crit_sw_igl = np.loadtxt("nman_fer_crit_sw_igl.asc"        , skiprows=6)
nman_fer_crit_gw_igl = np.loadtxt("nman_fer_crit_gw_igl.asc"        , skiprows=6)
nman_fer_crit_de_igl = np.loadtxt("nman_fer_crit_dep_igl.asc"       , skiprows=6)

### 1b. Read files from *INPUT* directory
os.chdir('c:\\users')
os.chdir('schul028')
os.chdir('OneDrive - WageningenUR')
os.chdir('critload_project')
os.chdir('critload')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

a_ara              = np.loadtxt("a_crop.asc"                   , skiprows=6)
a_igl              = np.loadtxt("a_gr_int.asc"                 , skiprows=6)
a_egl              = np.loadtxt("a_gr_ext.asc"                 , skiprows=6) 
nfix_ara           = np.loadtxt("nfix_crop.asc"                , skiprows=6)
nfix_igl           = np.loadtxt("nfix_grass_int.asc"           , skiprows=6)
nfix_egl           = np.loadtxt("nfix_grass_ext.asc"           , skiprows=6)
nh3_spred_fer_ara  = np.loadtxt("nh3_spread_fe_crops.asc"      , skiprows=6)
nh3_spred_fer_igl  = np.loadtxt("nh3_spread_fe_grass_int.asc"  , skiprows=6)
nh3_spred_man_ara  = np.loadtxt("nh3_spread_man_crops.asc"     , skiprows=6)
nh3_spred_man_igl  = np.loadtxt("nh3_spread_man_grass_int.asc" , skiprows=6)
nh3_graz_igl       = np.loadtxt("nh3_graz_int.asc"             , skiprows=6)

### 1c. change NA values to NaN
#general
nox_em[nox_em==-9999]                     =np.nan
fag[fag==-1]                              =np.nan
fara[fara==-1]                            =np.nan
figl[figl==-1]                            =np.nan
fegl[fegl==-1]                            =np.nan

# egl
nman_egl[nman_egl==-9999]                 =np.nan
nh3_tot_egl[nh3_tot_egl==-9999]           =np.nan

# ara
nfer_ara[nfer_ara==-9999]                         =np.nan
nman_ara[nman_ara==-9999]                         =np.nan
nman_crit_sw_ara[nman_crit_sw_ara==-9999]         =np.nan 
nfer_crit_sw_ara[nfer_crit_sw_ara==-9999]         =np.nan
nman_crit_gw_ara[nman_crit_gw_ara==-9999]         =np.nan
nfer_crit_gw_ara[nfer_crit_gw_ara==-9999]         =np.nan
nman_crit_de_ara[nman_crit_de_ara==-9999]         =np.nan
nfer_crit_de_ara[nfer_crit_de_ara==-9999]         =np.nan
fnup_max_sw_ara[fnup_max_sw_ara==-9999]           =np.nan
fnup_max_gw_ara[fnup_max_gw_ara==-9999]           =np.nan
fnup_max_de_ara[fnup_max_de_ara==-9999]           =np.nan
fnup_corr_sw_ara[fnup_corr_sw_ara==-9999]         =np.nan
fnup_corr_gw_ara[fnup_corr_gw_ara==-9999]         =np.nan
fnup_corr_de_ara[fnup_corr_de_ara==-9999]         =np.nan
nh3_ef_man_ara[nh3_ef_man_ara==-9999]             =np.nan
nh3_ef_fer_ara[nh3_ef_fer_ara==-9999]             =np.nan
nin_max_ara[nin_max_ara==-9999]                   =np.nan
nin_tot_crit_sw_ara[nin_tot_crit_sw_ara==-9999]   =np.nan
nin_tot_crit_gw_ara[nin_tot_crit_gw_ara==-9999]   =np.nan
nin_tot_crit_dep_ara[nin_tot_crit_dep_ara==-9999] =np.nan
nh3_stor_ara[nh3_stor_ara==-9999]                 =np.nan
nman_fer_crit_sw_ara[nman_fer_crit_sw_ara==-9999] =np.nan
nman_fer_crit_gw_ara[nman_fer_crit_gw_ara==-9999] =np.nan
nman_fer_crit_de_ara[nman_fer_crit_de_ara==-9999] =np.nan
# igl
nfer_igl[nfer_igl==-9999]                         =np.nan
nman_igl[nman_igl==-9999]                         =np.nan
nman_crit_sw_igl[nman_crit_sw_igl==-9999]         =np.nan 
nfer_crit_sw_igl[nfer_crit_sw_igl==-9999]         =np.nan
nman_crit_gw_igl[nman_crit_gw_igl==-9999]         =np.nan
nfer_crit_gw_igl[nfer_crit_gw_igl==-9999]         =np.nan
nman_crit_de_igl[nman_crit_de_igl==-9999]         =np.nan
nfer_crit_de_igl[nfer_crit_de_igl==-9999]         =np.nan
fnup_max_sw_igl[fnup_max_sw_igl==-9999]           =np.nan
fnup_max_gw_igl[fnup_max_gw_igl==-9999]           =np.nan
fnup_max_de_igl[fnup_max_de_igl==-9999]           =np.nan
fnup_corr_sw_igl[fnup_corr_sw_igl==-9999]         =np.nan
fnup_corr_gw_igl[fnup_corr_gw_igl==-9999]         =np.nan
fnup_corr_de_igl[fnup_corr_de_igl==-9999]         =np.nan
nh3_ef_man_igl[nh3_ef_man_igl==-9999]             =np.nan
nh3_ef_fer_igl[nh3_ef_fer_igl==-9999]             =np.nan
nin_max_igl[nin_max_igl==-9999]                   =np.nan
nin_tot_crit_sw_igl[nin_tot_crit_sw_igl==-9999]   =np.nan
nin_tot_crit_gw_igl[nin_tot_crit_gw_igl==-9999]   =np.nan
nin_tot_crit_dep_igl[nin_tot_crit_dep_igl==-9999] =np.nan
nh3_stor_igl[nh3_stor_igl==-9999]                 =np.nan
nman_fer_crit_sw_igl[nman_fer_crit_sw_igl==-9999] =np.nan
nman_fer_crit_gw_igl[nman_fer_crit_gw_igl==-9999] =np.nan
nman_fer_crit_de_igl[nman_fer_crit_de_igl==-9999] =np.nan

a_ara[a_ara==-1]                             =np.nan
a_igl[a_igl==-1]                             =np.nan
a_egl[a_egl==-1]                             =np.nan
nfix_ara[nfix_ara==-9999]                    =np.nan
nfix_igl[nfix_igl==-9999]                    =np.nan
nfix_egl[nfix_egl==-9999]                    =np.nan
nh3_spred_fer_ara[nh3_spred_fer_ara==-9999]  =np.nan
nh3_spred_fer_igl[nh3_spred_fer_igl==-9999]  =np.nan
nh3_spred_man_ara[nh3_spred_man_ara==-9999]  =np.nan
nh3_spred_man_igl[nh3_spred_man_igl==-9999]  =np.nan
nh3_graz_igl[nh3_graz_igl==-9999]            =np.nan



#########################
# Total actual N inputs #
#########################

# 1. Calculate CURRENT inputs from deposition due to NOx and NH3_egl (fixed deposition)
ndep_fixed      = np.add(nox_em, nh3_tot_egl)
ndep_fixed_ag   = np.multiply(ndep_fixed, fag)
ndep_fixed_ara  = np.multiply(ndep_fixed, fara)
ndep_fixed_igl  = np.multiply(ndep_fixed, figl)
ndep_fixed_egl  = np.multiply(ndep_fixed, fegl)

# 2. Calculate CURRENT inputs from deposition due to NH3_ara and NH3_igl (variable deposition) 
ndep_var_act = np.add(nh3_spred_fer_ara, nh3_spred_fer_igl)
ndep_var_act = np.add(ndep_var_act, nh3_spred_man_ara)
ndep_var_act = np.add(ndep_var_act, nh3_spred_man_igl)
ndep_var_act = np.add(ndep_var_act, nh3_graz_igl)
ndep_var_act = np.add(ndep_var_act, nh3_stor_ara)    
ndep_var_act = np.add(ndep_var_act, nh3_stor_igl)

ndep_var_act_ag  = np.multiply(ndep_var_act, fag)
ndep_var_act_ara = np.multiply(ndep_var_act, fara)
ndep_var_act_igl = np.multiply(ndep_var_act, figl)
ndep_var_act_egl = np.multiply(ndep_var_act, fegl)

# 3. Calculate CURRENT total N inputs
nman_fer_ara = np.add(nman_ara, nfer_ara)
nin_tot_ara = np.add(nman_fer_ara, ndep_var_act_ara)
nin_tot_ara = np.add(nin_tot_ara, ndep_fixed_ara)
nin_tot_ara = np.add(nin_tot_ara, nfix_ara)
nman_fer_igl = np.add(nman_igl, nfer_igl)
nin_tot_igl = np.add(nman_fer_igl, ndep_var_act_igl)
nin_tot_igl = np.add(nin_tot_igl, ndep_fixed_igl)
nin_tot_igl = np.add(nin_tot_igl, nfix_igl)

# ara
print("Nman_act_ara:      %.1f"   %(np.nansum(nman_ara)))
print("Nfer_act_ara:      %.1f"   %(np.nansum(nfer_ara)))
print("Ndep_var_act_ara:  %.1f"   %(np.nansum(ndep_var_act_ara)))
print("Ndep_fix_act_ara:  %.1f"   %(np.nansum(ndep_fixed_ara)))
print("Nfix_act_ara:      %.1f"   %(np.nansum(nfix_ara)))
print("A_ara:             %.1f"   %(np.nansum(a_ara)))
# igl
print("Nman_act_igl:      %.1f"   %(np.nansum(nman_igl)))
print("Nfer_act_igl:      %.1f"   %(np.nansum(nfer_igl)))
print("Ndep_var_act_igl:  %.1f"   %(np.nansum(ndep_var_act_igl)))
print("Ndep_fix_act_igl:  %.1f"   %(np.nansum(ndep_fixed_igl)))
print("Nfix_act_igl:      %.1f"   %(np.nansum(nfix_igl)))
print("A_igl:             %.1f"   %(np.nansum(a_igl)))
# egl
print("Nman_act_egl:      %.1f"   %(np.nansum(nman_egl)))
print("Nfer_act_egl:      %.1f"   % 0.0)
print("Ndep_var_act_egl:  %.1f"   %(np.nansum(ndep_var_act_egl)))
print("Ndep_fix_act_egl:  %.1f"   %(np.nansum(ndep_fixed_egl)))
print("Nfix_act_egl:      %.1f"   %(np.nansum(nfix_egl)))
print("A_egl:             %.1f"   %(np.nansum(a_egl)))

''' #Non-NA areas are always the same for each input type, so we can calculate per-hectare inputs by dividing total N inputs by total area.
# areas-ara
print("Area-non-na-Nman_act_ara:     %i"   % np.nansum(a_ara[np.where(np.isnan(nman_ara)==False)]))
print("Area-non-na-Nfer_act_ara:     %i"   % np.nansum(a_ara[np.where(np.isnan(nfer_ara)==False)]))
print("Area-non-na-Ndep_var_act_ara: %i"   % np.nansum(a_ara[np.where(np.isnan(ndep_var_act_ara)==False)]))
print("Area-non-na-Ndep_fix_act_ara: %i"   % np.nansum(a_ara[np.where(np.isnan(ndep_fixed_ara)==False)]))
print("Area-non-na-Nfix_act_ara:     %i"   % np.nansum(a_ara[np.where(np.isnan(nfix_ara)==False)]))
print("Area-non-na-Nin_act_ara:      %i"    % np.nansum(a_ara[np.where(np.isnan(nin_tot_ara)==False)]))
# areas-igl
print("Area-non-na-Nman_act_igl:     %i"   % np.nansum(a_igl[np.where(np.isnan(nman_igl)==False)]))
print("Area-non-na-Nfer_act_igl:     %i"   % np.nansum(a_igl[np.where(np.isnan(nfer_igl)==False)]))
print("Area-non-na-Ndep_var_act_igl: %i"   % np.nansum(a_igl[np.where(np.isnan(ndep_var_act_igl)==False)]))
print("Area-non-na-Ndep_fix_act_igl: %i"   % np.nansum(a_igl[np.where(np.isnan(ndep_fixed_igl)==False)]))
print("Area-non-na-Nfix_act_igl:     %i"   % np.nansum(a_igl[np.where(np.isnan(nfix_igl)==False)]))
print("Area-non-na-Nin_act_igl:      %i"    % np.nansum(a_igl[np.where(np.isnan(nin_tot_igl)==False)]))
# areas-egl
print("Area-non-na-Nman_act_egl:     %i"   % np.nansum(a_egl[np.where(np.isnan(nman_egl)==False)]))
print("Area-non-na-Nfer_act_egl:     %i"   % 0.0)
print("Area-non-na-Ndep_var_act_egl: %i"   % np.nansum(a_egl[np.where(np.isnan(ndep_var_act_egl)==False)]))
print("Area-non-na-Ndep_fix_act_egl: %i"   % np.nansum(a_egl[np.where(np.isnan(ndep_fixed_egl)==False)]))
print("Area-non-na-Nfix_act_egl:     %i"   % np.nansum(a_egl[np.where(np.isnan(nfix_egl)==False)]))
print("Area-non-na-Nin_act_egl:      %i"    % np.nansum(a_egl[np.where(np.isnan(nin_tot_egl)==False)]))
'''

##########################################
# Total critical N inputs (after cutoff) #
##########################################
# 1. Cut-off at maximum N input
# 1a. ara
nfer_crit_sw_ara3   = np.copy(nfer_crit_sw_ara)
nman_crit_sw_ara3   = np.copy(nman_crit_sw_ara)
nfer_crit_gw_ara3   = np.copy(nfer_crit_gw_ara)
nman_crit_gw_ara3   = np.copy(nman_crit_gw_ara)
nfer_crit_de_ara3   = np.copy(nfer_crit_de_ara)
nman_crit_de_ara3   = np.copy(nman_crit_de_ara)


'''
# replace negative values by zero
with np.errstate(invalid='ignore'):
    nfer_crit_sw_ara3[nfer_crit_sw_ara3<0]=0
    nman_crit_sw_ara3[nman_crit_sw_ara3<0]=0
    nfer_crit_gw_ara3[nfer_crit_gw_ara3<0]=0
    nman_crit_gw_ara3[nman_crit_gw_ara3<0]=0
    nfer_crit_de_ara3[nfer_crit_de_ara3<0]=0
    nman_crit_de_ara3[nman_crit_de_ara3<0]=0
'''
    # replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_ara)[0]):
        for j in range(np.shape(fnup_max_sw_ara)[1]):
            if (fnup_max_sw_ara[i,j] < 1 and np.isnan(fnup_max_sw_ara[i,j])==False):
                nfer_crit_sw_ara3[i,j] = nfer_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
                nman_crit_sw_ara3[i,j] = nman_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
    for i in range(np.shape(fnup_max_gw_ara)[0]):
        for j in range(np.shape(fnup_max_gw_ara)[1]):
            if (fnup_max_gw_ara[i,j] < 1 and np.isnan(fnup_max_gw_ara[i,j])==False):
                nfer_crit_gw_ara3[i,j] = nfer_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
                nman_crit_gw_ara3[i,j] = nman_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
    for i in range(np.shape(fnup_max_de_ara)[0]):
        for j in range(np.shape(fnup_max_de_ara)[1]):
            if (fnup_max_de_ara[i,j] < 1 and np.isnan(fnup_max_de_ara[i,j])==False):
                nfer_crit_de_ara3[i,j] = nfer_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]
                nman_crit_de_ara3[i,j] = nman_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]

# select minimum
nfer_crit_min_ara3X    = np.minimum(nfer_crit_sw_ara3,     nfer_crit_gw_ara3)
nfer_crit_min_ara3     = np.minimum(nfer_crit_min_ara3X,   nfer_crit_de_ara3)
nman_crit_min_ara3X    = np.minimum(nman_crit_sw_ara3,     nman_crit_gw_ara3)
nman_crit_min_ara3     = np.minimum(nman_crit_min_ara3X,   nman_crit_de_ara3)

# 1b. igl
nfer_crit_sw_igl3   = np.copy(nfer_crit_sw_igl)
nman_crit_sw_igl3   = np.copy(nman_crit_sw_igl)
nfer_crit_gw_igl3   = np.copy(nfer_crit_gw_igl)
nman_crit_gw_igl3   = np.copy(nman_crit_gw_igl)
nfer_crit_de_igl3   = np.copy(nfer_crit_de_igl)
nman_crit_de_igl3   = np.copy(nman_crit_de_igl)

# replace negative values by zero
'''
with np.errstate(invalid='ignore'):
    nfer_crit_sw_igl3[nfer_crit_sw_igl3<0]=0
    nman_crit_sw_igl3[nman_crit_sw_igl3<0]=0
    nfer_crit_gw_igl3[nfer_crit_gw_igl3<0]=0
    nman_crit_gw_igl3[nman_crit_gw_igl3<0]=0
    nfer_crit_de_igl3[nfer_crit_de_igl3<0]=0
    nman_crit_de_igl3[nman_crit_de_igl3<0]=0
'''

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_igl)[0]):
        for j in range(np.shape(fnup_max_sw_igl)[1]):
            if (fnup_max_sw_igl[i,j] < 1 and np.isnan(fnup_max_sw_igl[i,j])==False):
                nfer_crit_sw_igl3[i,j] = nfer_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
                nman_crit_sw_igl3[i,j] = nman_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
    for i in range(np.shape(fnup_max_gw_igl)[0]):
        for j in range(np.shape(fnup_max_gw_igl)[1]):
            if (fnup_max_gw_igl[i,j] < 1 and np.isnan(fnup_max_gw_igl[i,j])==False):
                nfer_crit_gw_igl3[i,j] = nfer_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
                nman_crit_gw_igl3[i,j] = nman_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
    for i in range(np.shape(fnup_max_de_igl)[0]):
        for j in range(np.shape(fnup_max_de_igl)[1]):
            if (fnup_max_de_igl[i,j] < 1 and np.isnan(fnup_max_de_igl[i,j])==False):
                nfer_crit_de_igl3[i,j] = nfer_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]
                nman_crit_de_igl3[i,j] = nman_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]

# select minimum
nfer_crit_min_igl3X    = np.minimum(nfer_crit_sw_igl3,     nfer_crit_gw_igl3)
nfer_crit_min_igl3     = np.minimum(nfer_crit_min_igl3X,   nfer_crit_de_igl3)
nman_crit_min_igl3X    = np.minimum(nman_crit_sw_igl3,     nman_crit_gw_igl3)
nman_crit_min_igl3     = np.minimum(nman_crit_min_igl3X,   nman_crit_de_igl3)

#############################################



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
ndep_var_crit_sw3_ara = np.multiply(ndep_var_crit_tot_sw3, fara)
ndep_var_crit_gw3_ara = np.multiply(ndep_var_crit_tot_gw3, fara)
ndep_var_crit_de3_ara = np.multiply(ndep_var_crit_tot_de3, fara)
ndep_var_crit_min3_ara = np.multiply(ndep_var_crit_tot_min3, fara)
# to igl
ndep_var_crit_sw3_igl = np.multiply(ndep_var_crit_tot_sw3, figl)
ndep_var_crit_gw3_igl = np.multiply(ndep_var_crit_tot_gw3, figl)
ndep_var_crit_de3_igl = np.multiply(ndep_var_crit_tot_de3, figl)
ndep_var_crit_min3_igl = np.multiply(ndep_var_crit_tot_min3, figl)


# deposition - ara
print("Nman_crit_de_ara:            %.1f" % np.nansum(nman_crit_de_ara3))
print("Nfer_crit_de_ara:            %.1f" % np.nansum(nfer_crit_de_ara3))
print("Ndep_var_crit_de_ara:        %.1f" % np.nansum(ndep_var_crit_de3_ara))
print("Ndep_fix_crit_de_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(np.isnan(nman_crit_de_ara3) ==False)]))
print("Nfix_crit_de_ara:            %.1f" % np.nansum(nfix_ara[np.where(np.isnan(nman_crit_de_ara3) ==False)]))
print("Area-non-na-Nin_crit_de_ara: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_de_ara3)==False)]))
# surface water - ara
print("Nman_crit_sw_ara:            %.1f" % np.nansum(nman_crit_sw_ara3))
print("Nfer_crit_sw_ara:            %.1f" % np.nansum(nfer_crit_sw_ara3))
print("Ndep_var_crit_sw_ara:        %.1f" % np.nansum(ndep_var_crit_sw3_ara))
print("Ndep_fix_crit_sw_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(np.isnan(nman_crit_sw_ara3) ==False)]))
print("Nfix_crit_sw_ara:            %.1f" % np.nansum(nfix_ara[np.where(np.isnan(nman_crit_sw_ara3) ==False)]))
print("Area-non-na-Nin_crit_sw_ara: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_sw_ara3)==False)]))
# groundwater - ara
print("Nman_crit_gw_ara:            %.1f" % np.nansum(nman_crit_gw_ara3))
print("Nfer_crit_gw_ara:            %.1f" % np.nansum(nfer_crit_gw_ara3))
print("Ndep_var_crit_gw_ara:        %.1f" % np.nansum(ndep_var_crit_gw3_ara))
print("Ndep_fix_crit_gw_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(np.isnan(nman_crit_gw_ara3) ==False)]))
print("Nfix_crit_gw_ara:            %.1f" % np.nansum(nfix_ara[np.where(np.isnan(nman_crit_gw_ara3) ==False)]))
print("Area-non-na-Nin_crit_gw_ara: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_gw_ara3)==False)]))
# minimum - ara
print("Nman_crit_mi_ara:            %.1f" % np.nansum(nman_crit_min_ara3))
print("Nfer_crit_mi_ara:            %.1f" % np.nansum(nfer_crit_min_ara3))
print("Ndep_var_crit_mi_ara:        %.1f" % np.nansum(ndep_var_crit_min3_ara))
print("Ndep_fix_crit_mi_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(np.isnan(nman_crit_min_ara3) ==False)]))
print("Nfix_crit_mi_ara:            %.1f" % np.nansum(nfix_ara[np.where(np.isnan(nman_crit_min_ara3) ==False)]))
print("Area-non-na-Nin_crit_mi_ara: %.1f" % np.nansum(a_ara[np.where(np.isnan(nman_crit_min_ara3)==False)]))

# deposition - igl
print("Nman_crit_de_igl:            %.1f" % np.nansum(nman_crit_de_igl3))
print("Nfer_crit_de_igl:            %.1f" % np.nansum(nfer_crit_de_igl3))
print("Ndep_var_crit_de_igl:        %.1f" % np.nansum(ndep_var_crit_de3_igl))
print("Ndep_fix_crit_de_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(np.isnan(nman_crit_de_igl3) ==False)]))
print("Nfix_crit_de_igl:            %.1f" % np.nansum(nfix_igl[np.where(np.isnan(nman_crit_de_igl3) ==False)]))
print("Area-non-na-Nin_crit_de_igl: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_de_igl3)==False)]))
# surface water - igl
print("Nman_crit_sw_igl:            %.1f" % np.nansum(nman_crit_sw_igl3))
print("Nfer_crit_sw_igl:            %.1f" % np.nansum(nfer_crit_sw_igl3))
print("Ndep_var_crit_sw_igl:        %.1f" % np.nansum(ndep_var_crit_sw3_igl))
print("Ndep_fix_crit_sw_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(np.isnan(nman_crit_sw_igl3) ==False)]))
print("Nfix_crit_sw_igl:            %.1f" % np.nansum(nfix_igl[np.where(np.isnan(nman_crit_sw_igl3) ==False)]))
print("Area-non-na-Nin_crit_sw_igl: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_sw_igl3)==False)]))
# groundwater - igl
print("Nman_crit_gw_igl:            %.1f" % np.nansum(nman_crit_gw_igl3))
print("Nfer_crit_gw_igl:            %.1f" % np.nansum(nfer_crit_gw_igl3))
print("Ndep_var_crit_gw_igl:        %.1f" % np.nansum(ndep_var_crit_gw3_igl))
print("Ndep_fix_crit_gw_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(np.isnan(nman_crit_gw_igl3) ==False)]))
print("Nfix_crit_gw_igl:            %.1f" % np.nansum(nfix_igl[np.where(np.isnan(nman_crit_gw_igl3) ==False)]))
print("Area-non-na-Nin_crit_gw_igl: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_gw_igl3)==False)]))
# minimum - igl
print("Nman_crit_mi_igl:            %.1f" % np.nansum(nman_crit_min_igl3))
print("Nfer_crit_mi_igl:            %.1f" % np.nansum(nfer_crit_min_igl3))
print("Ndep_var_crit_mi_igl:        %.1f" % np.nansum(ndep_var_crit_min3_igl))
print("Ndep_fix_crit_mi_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(np.isnan(nman_crit_min_igl3) ==False)]))
print("Nfix_crit_mi_igl:            %.1f" % np.nansum(nfix_igl[np.where(np.isnan(nman_crit_min_igl3) ==False)]))
print("Area-non-na-Nin_crit_mi_igl: %.1f" % np.nansum(a_igl[np.where(np.isnan(nman_crit_min_igl3)==False)]))


# Minimum N inputs from manure + fertilizer - ARA
nman_fer_crit_mi_araX = np.minimum(nman_fer_crit_sw_ara,  nman_fer_crit_gw_ara)
nman_fer_crit_mi_ara  = np.minimum(nman_fer_crit_mi_araX, nman_fer_crit_de_ara)
# Maximum N inputs from manure + fertilizer - ARA
nman_fer_crit_sw_max_ara = np.multiply(nman_fer_crit_sw_ara, fnup_corr_sw_ara)
nman_fer_crit_gw_max_ara = np.multiply(nman_fer_crit_gw_ara, fnup_corr_gw_ara)
nman_fer_crit_de_max_ara = np.multiply(nman_fer_crit_de_ara, fnup_corr_de_ara)

# Minimum N inputs from manure + fertilizer - IGL
nman_fer_crit_mi_iglX = np.minimum(nman_fer_crit_sw_igl,  nman_fer_crit_gw_igl)
nman_fer_crit_mi_igl  = np.minimum(nman_fer_crit_mi_iglX, nman_fer_crit_de_igl)
# Maximum N inputs from manure + fertilizer - IGL
nman_fer_crit_sw_max_igl = np.multiply(nman_fer_crit_sw_igl, fnup_corr_sw_igl)
nman_fer_crit_gw_max_igl = np.multiply(nman_fer_crit_gw_igl, fnup_corr_gw_igl)
nman_fer_crit_de_max_igl = np.multiply(nman_fer_crit_de_igl, fnup_corr_de_igl)


print("CASES----ARA")
with np.errstate(invalid='ignore'):
    print("total-area: %.1f"% np.nansum(a_ara))
    print("case-1-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, nman_fer_crit_de_ara<=0)) ]))
    print("case-3-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara>0,nman_fer_crit_de_ara<=nman_fer_ara))) ]))
    print("case-4-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara>nman_fer_ara,nman_fer_crit_de_ara<=nman_fer_crit_de_max_ara))) ]))
    print("case-5-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara>nman_fer_ara,nman_fer_crit_de_ara>nman_fer_crit_de_max_ara))) ]))

    print("case-1-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, nman_fer_crit_sw_ara<=0)) ]))
    print("case-3-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara>0,nman_fer_crit_sw_ara<=nman_fer_ara))) ]))
    print("case-4-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara>nman_fer_ara,nman_fer_crit_sw_ara<=nman_fer_crit_sw_max_ara))) ]))
    print("case-5-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara>nman_fer_ara,nman_fer_crit_sw_ara>nman_fer_crit_sw_max_ara))) ]))
  
    print("case-1-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, nman_fer_crit_gw_ara<=0)) ]))
    print("case-3-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara>0,nman_fer_crit_gw_ara<=nman_fer_ara))) ]))
    print("case-4-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara>nman_fer_ara,nman_fer_crit_gw_ara<=nman_fer_crit_gw_max_ara))) ]))
    print("case-5-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara>nman_fer_ara,nman_fer_crit_gw_ara>nman_fer_crit_gw_max_ara))) ]))      
  
    print("case-1-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==True,  np.logical_and(np.isnan(a_ara)==False, a_ara>0)) )]))
    print("case-2-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, nman_fer_crit_mi_ara<=0)) ]))
    print("case-3-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara>0,nman_fer_crit_mi_ara<=nman_fer_ara))) ]))
    print("case-4-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara>nman_fer_ara,nman_fer_crit_mi_ara<=nman_fer_crit_gw_max_ara))) ]))
    print("case-5-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara>nman_fer_ara,nman_fer_crit_mi_ara>nman_fer_crit_gw_max_ara))) ]))      
  
    
print("CASES----IGL")
with np.errstate(invalid='ignore'):
    print("total-area: %.1f"% np.nansum(a_igl))
    print("case-1-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, nman_fer_crit_de_igl<=0)) ]))
    print("case-3-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl>0,nman_fer_crit_de_igl<=nman_fer_igl))) ]))
    print("case-4-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl>nman_fer_igl,nman_fer_crit_de_igl<=nman_fer_crit_de_max_igl))) ]))
    print("case-5-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl>nman_fer_igl,nman_fer_crit_de_igl>nman_fer_crit_de_max_igl))) ]))

    print("case-1-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, nman_fer_crit_sw_igl<=0)) ]))
    print("case-3-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl>0,nman_fer_crit_sw_igl<=nman_fer_igl))) ]))
    print("case-4-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl>nman_fer_igl,nman_fer_crit_sw_igl<=nman_fer_crit_sw_max_igl))) ]))
    print("case-5-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl>nman_fer_igl,nman_fer_crit_sw_igl>nman_fer_crit_sw_max_igl))) ]))
  
    print("case-1-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, nman_fer_crit_gw_igl<=0)) ]))
    print("case-3-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl>0,nman_fer_crit_gw_igl<=nman_fer_igl))) ]))
    print("case-4-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl>nman_fer_igl,nman_fer_crit_gw_igl<=nman_fer_crit_gw_max_igl))) ]))
    print("case-5-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl>nman_fer_igl,nman_fer_crit_gw_igl>nman_fer_crit_gw_max_igl))) ]))      
  
    print("case-1-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==True,  np.logical_and(np.isnan(a_igl)==False, a_igl>0)) )]))
    print("case-2-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, nman_fer_crit_mi_igl<=0)) ]))
    print("case-3-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl>0,nman_fer_crit_mi_igl<=nman_fer_igl))) ]))
    print("case-4-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl>nman_fer_igl,nman_fer_crit_mi_igl<=nman_fer_crit_gw_max_igl))) ]))
    print("case-5-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl>nman_fer_igl,nman_fer_crit_mi_igl>nman_fer_crit_gw_max_igl))) ]))   