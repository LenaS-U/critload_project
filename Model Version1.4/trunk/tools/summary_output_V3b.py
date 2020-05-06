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
nh3_ef_man       = np.loadtxt("nh3_ef_man_agri.asc"      , skiprows=6)
nh3_ef_fer       = np.loadtxt("nh3_ef_fert_agri.asc"     , skiprows=6)
fagri            = np.loadtxt("fagri.asc"                , skiprows=6) 
nox_em           = np.loadtxt("nox_em.asc"               , skiprows=6) 
nh3_tot_egl      = np.loadtxt("nh3_tot_egl.asc"          , skiprows=6) 
nh3_tot_agri     = np.loadtxt("nh3_tot_agri.asc"         , skiprows=6) 
fnup_max_sw      = np.loadtxt("fnup_max_sw.asc"          , skiprows=6)
fnup_max_gw      = np.loadtxt("fnup_max_gw.asc"          , skiprows=6)
fnup_max_de      = np.loadtxt("fnup_max_dep.asc"         , skiprows=6)
fnup_corr_sw     = np.loadtxt("fnup_corr_sw.asc"         , skiprows=6)
fnup_corr_gw     = np.loadtxt("fnup_corr_gw.asc"         , skiprows=6)
fnup_corr_de     = np.loadtxt("fnup_corr_dep.asc"        , skiprows=6)
nfer_agri        = np.loadtxt("n_fert_agri.asc"          , skiprows=6) 
nman_agri        = np.loadtxt("n_man_agri.asc"           , skiprows=6)
nman_egl         = np.loadtxt("nman_egl.asc"             , skiprows=6)

### 1b. Read files from *INPUT* directory
os.chdir('c:\\users')
os.chdir('schul028')
os.chdir('OneDrive - WageningenUR')
os.chdir('critload_project')
os.chdir('Model Version1.4')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

nfix_ara      = np.loadtxt("nfix_crop.asc"                , skiprows=6)
nfix_igl      = np.loadtxt("nfix_grass_int.asc"           , skiprows=6)
a_ara         = np.loadtxt("a_crop.asc"                   , skiprows=6)
a_igl         = np.loadtxt("a_gr_int.asc"                 , skiprows=6)

### 1c. change NA values to NaN
mancritsw[mancritsw==-9999]               =np.nan 
fercritsw[fercritsw==-9999]               =np.nan
mancritgw[mancritgw==-9999]               =np.nan
fercritgw[fercritgw==-9999]               =np.nan
mancritde[mancritde==-9999]               =np.nan
fercritde[fercritde==-9999]               =np.nan
nh3_ef_man[nh3_ef_man==-9999]             =np.nan
nh3_ef_fer[nh3_ef_fer==-9999]             =np.nan
fagri[fagri==-1]                          =np.nan
nox_em[nox_em==-9999]                     =np.nan
nh3_tot_egl[nh3_tot_egl==-9999]           =np.nan
fnup_max_sw[fnup_max_sw==-9999]           =np.nan
fnup_max_gw[fnup_max_gw==-9999]           =np.nan
fnup_max_de[fnup_max_de==-9999]           =np.nan
fnup_corr_sw[fnup_corr_sw==-9999]         =np.nan
fnup_corr_gw[fnup_corr_gw==-9999]         =np.nan
fnup_corr_de[fnup_corr_de==-9999]         =np.nan
nfer_agri[nfer_agri==-9999]               =np.nan
nman_agri[nman_agri==-9999]               =np.nan
nman_egl[nman_egl==-9999]                 =np.nan

nfix_ara[nfix_ara==-9999]                 =np.nan
nfix_igl[nfix_igl==-9999]                 =np.nan
a_ara[a_ara==-1]                          =np.nan
a_igl[a_igl==-1]                          =np.nan


### Actual inputs ###

manfer_araigl       = np.add(nfer_agri,nman_agri)
nfix_araigl         = np.add(nfix_ara,nfix_igl)
ndep_fixed          = np.add(nox_em, nh3_tot_egl)
ndep_fixed_araigl   = np.multiply(ndep_fixed, fagri)
ndep_var_act_araigl = np.multiply(nh3_tot_agri, fagri)
a_araigl            = np.add(a_ara, a_igl)

##########################################
# Total critical N inputs (after cutoff) #
##########################################
# 1. Cut-off at maximum N input
fercritsw3 = np.copy(fercritsw)
mancritsw3 = np.copy(mancritsw)
fercritgw3 = np.copy(fercritgw)
mancritgw3 = np.copy(mancritgw)
fercritde3 = np.copy(fercritde)
mancritde3 = np.copy(mancritde)

'''
# replace negative values by zero
with np.errstate(invalid='ignore'):
    fercritsw3[fercritsw3<0]=0
    mancritsw3[mancritsw3<0]=0
    fercritgw3[fercritgw3<0]=0
    mancritgw3[mancritgw3<0]=0
    fercritde3[fercritde3<0]=0
    mancritde3[mancritde3<0]=0
'''

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw)[0]):
        for j in range(np.shape(fnup_max_sw)[1]):
            if (fnup_max_sw[i,j] < 1 and np.isnan(fnup_max_sw[i,j])==False):
                fercritsw3[i,j] = fercritsw3[i,j]*fnup_corr_sw[i,j]
                mancritsw3[i,j] = mancritsw3[i,j]*fnup_corr_sw[i,j]
    for i in range(np.shape(fnup_max_gw)[0]):
        for j in range(np.shape(fnup_max_gw)[1]):
            if (fnup_max_gw[i,j] < 1 and np.isnan(fnup_max_gw[i,j])==False):
                fercritgw3[i,j] = fercritgw3[i,j]*fnup_corr_gw[i,j]
                mancritgw3[i,j] = mancritgw3[i,j]*fnup_corr_gw[i,j]
    for i in range(np.shape(fnup_max_de)[0]):
        for j in range(np.shape(fnup_max_de)[1]):
            if (fnup_max_de[i,j] < 1 and np.isnan(fnup_max_de[i,j])==False):
                fercritde3[i,j] = fercritde3[i,j]*fnup_corr_de[i,j]
                mancritde3[i,j] = mancritde3[i,j]*fnup_corr_de[i,j]

# select minimum
fercritmin3X    = np.minimum(fercritsw3, fercritgw3)
fercritmin3     = np.minimum(fercritmin3X, fercritde3)
mancritmin3X    = np.minimum(mancritsw3, mancritgw3)
mancritmin3     = np.minimum(mancritmin3X, mancritde3)

# variable NH3 emissions at critical N inputs (after cutoff)
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

# to araigl
ndep_var_crit_sw3_araigl = np.multiply(ndep_var_crit_tot_sw3, fagri)
ndep_var_crit_gw3_araigl = np.multiply(ndep_var_crit_tot_gw3, fagri)
ndep_var_crit_de3_araigl = np.multiply(ndep_var_crit_tot_de3, fagri)
ndep_var_crit_min3_araigl = np.multiply(ndep_var_crit_tot_min3, fagri)

# deposition - araigl
print("Nman_crit_de_araigl:            %.1f" % np.nansum(mancritde3))
print("Nfer_crit_de_araigl:            %.1f" % np.nansum(fercritde3))
print("Ndep_var_crit_de_araigl:        %.1f" % np.nansum(ndep_var_crit_de3_araigl))
print("Ndep_fix_crit_de_araigl:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(np.isnan(mancritde3) ==False)]))
print("Nfix_crit_de_araigl:            %.1f" % np.nansum(nfix_araigl[np.where(np.isnan(mancritde3) ==False)]))
print("Area-non-na-Nin_crit_de_araigl: %.1f" % np.nansum(a_araigl[np.where(np.isnan(mancritde3)==False)]))
# surface water - araigl
print("Nman_crit_sw_ara:            %.1f" % np.nansum(mancritsw3))
print("Nfer_crit_sw_ara:            %.1f" % np.nansum(fercritsw3))
print("Ndep_var_crit_sw_ara:        %.1f" % np.nansum(ndep_var_crit_sw3_araigl))
print("Ndep_fix_crit_sw_ara:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(np.isnan(mancritsw3) ==False)]))
print("Nfix_crit_sw_ara:            %.1f" % np.nansum(nfix_araigl[np.where(np.isnan(mancritsw3) ==False)]))
print("Area-non-na-Nin_crit_sw_ara: %.1f" % np.nansum(a_araigl[np.where(np.isnan(mancritsw3)==False)]))
# groundwater - araigl
print("Nman_crit_gw_ara:            %.1f" % np.nansum(mancritgw3))
print("Nfer_crit_gw_ara:            %.1f" % np.nansum(fercritgw3))
print("Ndep_var_crit_gw_ara:        %.1f" % np.nansum(ndep_var_crit_gw3_araigl))
print("Ndep_fix_crit_gw_ara:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(np.isnan(mancritgw3) ==False)]))
print("Nfix_crit_gw_ara:            %.1f" % np.nansum(nfix_araigl[np.where(np.isnan(mancritgw3) ==False)]))
print("Area-non-na-Nin_crit_gw_ara: %.1f" % np.nansum(a_araigl[np.where(np.isnan(mancritgw3)==False)]))
# minimum - araigl
print("Nman_crit_mi_ara:            %.1f" % np.nansum(mancritmin3))
print("Nfer_crit_mi_ara:            %.1f" % np.nansum(fercritmin3))
print("Ndep_var_crit_mi_ara:        %.1f" % np.nansum(ndep_var_crit_min3_araigl))
print("Ndep_fix_crit_mi_ara:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(np.isnan(mancritmin3) ==False)]))
print("Nfix_crit_mi_ara:            %.1f" % np.nansum(nfix_araigl[np.where(np.isnan(mancritmin3) ==False)]))
print("Area-non-na-Nin_crit_mi_ara: %.1f" % np.nansum(a_araigl[np.where(np.isnan(mancritmin3)==False)]))

# Critical N inputs from manure + fertilizer - ARAIGL
nman_fer_crit_sw = np.add(mancritsw, fercritsw)
nman_fer_crit_gw = np.add(mancritgw, fercritgw)
nman_fer_crit_de = np.add(mancritde, fercritde)
# Minimum N inputs from manure + fertilizer - ARA
nman_fer_crit_miX = np.minimum(nman_fer_crit_sw,  nman_fer_crit_gw)
nman_fer_crit_mi  = np.minimum(nman_fer_crit_miX, nman_fer_crit_de)
# Maximum N inputs from manure + fertilizer - ARA
nman_fer_crit_sw_max = np.multiply(nman_fer_crit_sw, fnup_corr_sw)
nman_fer_crit_gw_max = np.multiply(nman_fer_crit_gw, fnup_corr_gw)
nman_fer_crit_de_max = np.multiply(nman_fer_crit_de, fnup_corr_de)

print("CASES-FOR-*ALL*-INPUTS---ARAIGL")
with np.errstate(invalid='ignore'):
    print("total-area: %.1f"% np.nansum(a_araigl))
    print("case-1-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==True,  np.logical_and(np.isnan(a_araigl)==False, a_araigl>0)) )]))
    print("case-2-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, nman_fer_crit_de<=0)) ]))
    print("case-3-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de>0,nman_fer_crit_de<=manfer_araigl))) ]))
    print("case-4-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de>manfer_araigl,nman_fer_crit_de<=nman_fer_crit_de_max))) ]))
    print("case-5-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de>manfer_araigl,nman_fer_crit_de>nman_fer_crit_de_max))) ]))

    print("case-1-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==True,  np.logical_and(np.isnan(a_araigl)==False, a_araigl>0)) )]))
    print("case-2-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, nman_fer_crit_sw<=0)) ]))
    print("case-3-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw>0,nman_fer_crit_sw<=manfer_araigl))) ]))
    print("case-4-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw>manfer_araigl,nman_fer_crit_sw<=nman_fer_crit_sw_max))) ]))
    print("case-5-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw>manfer_araigl,nman_fer_crit_sw>nman_fer_crit_sw_max))) ]))
  
    print("case-1-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==True,  np.logical_and(np.isnan(a_araigl)==False, a_araigl>0)) )]))
    print("case-2-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, nman_fer_crit_gw<=0)) ]))
    print("case-3-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw>0,nman_fer_crit_gw<=manfer_araigl))) ]))
    print("case-4-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw>manfer_araigl,nman_fer_crit_gw<=nman_fer_crit_gw_max))) ]))
    print("case-5-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw>manfer_araigl,nman_fer_crit_gw>nman_fer_crit_gw_max))) ]))      
  
    print("case-1-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==True,  np.logical_and(np.isnan(a_araigl)==False, a_araigl>0)) )]))
    print("case-2-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, nman_fer_crit_mi<=0)) ]))
    print("case-3-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi>0,nman_fer_crit_mi<=manfer_araigl))) ]))
    print("case-4-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi>manfer_araigl,nman_fer_crit_mi<=nman_fer_crit_gw_max))) ]))
    print("case-5-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi>manfer_araigl,nman_fer_crit_mi>nman_fer_crit_gw_max))) ]))     