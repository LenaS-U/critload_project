import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

#######################################################################################################################################################################################################    
# Read files from input / output directory and replace NA values by NaN ############################################################################################################################
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
nox_em               = np.loadtxt("nox_em.asc"                , skiprows=6)
fag                  = np.loadtxt("fag.asc"                   , skiprows=6)
fara                 = np.loadtxt("fara.asc"                  , skiprows=6)
figl                 = np.loadtxt("figl.asc"                  , skiprows=6)
fegl                 = np.loadtxt("fegl.asc"                  , skiprows=6)
# egl
nman_egl             = np.loadtxt("nman_egl.asc"              , skiprows=6)
nh3_tot_egl          = np.loadtxt("nh3_tot_egl.asc"           , skiprows=6)
# ara
nfer_ara             = np.loadtxt("nfer_ara.asc"              , skiprows=6)
nman_ara             = np.loadtxt("nman_ara.asc"              , skiprows=6)
nman_crit_sw_ara     = np.loadtxt("nman_crit_sw_ara.asc"      , skiprows=6)
nfer_crit_sw_ara     = np.loadtxt("nfer_crit_sw_ara.asc"      , skiprows=6)
nman_crit_gw_ara     = np.loadtxt("nman_crit_gw_ara.asc"      , skiprows=6)
nfer_crit_gw_ara     = np.loadtxt("nfer_crit_gw_ara.asc"      , skiprows=6)
nman_crit_de_ara     = np.loadtxt("nman_crit_dep_ara.asc"     , skiprows=6)
nfer_crit_de_ara     = np.loadtxt("nfer_crit_dep_ara.asc"     , skiprows=6)
fnup_max_sw_ara      = np.loadtxt("fnup_max_sw_ara.asc"       , skiprows=6)
fnup_max_gw_ara      = np.loadtxt("fnup_max_gw_ara.asc"       , skiprows=6)
fnup_max_de_ara      = np.loadtxt("fnup_max_dep_ara.asc"      , skiprows=6)
fnup_corr_sw_ara     = np.loadtxt("fnup_corr_sw_ara.asc"      , skiprows=6)
fnup_corr_gw_ara     = np.loadtxt("fnup_corr_gw_ara.asc"      , skiprows=6)
fnup_corr_de_ara     = np.loadtxt("fnup_corr_dep_ara.asc"     , skiprows=6)
nh3_ef_man_ara       = np.loadtxt("nh3_ef_man_ara.asc"        , skiprows=6)
nh3_ef_fer_ara       = np.loadtxt("nh3_ef_fer_ara.asc"        , skiprows=6)
nin_max_ara          = np.loadtxt("nin_max_ara.asc"           , skiprows=6)
nin_tot_crit_sw_ara  = np.loadtxt("nin_crit_sw_ara.asc"       , skiprows=6)
nin_tot_crit_gw_ara  = np.loadtxt("nin_crit_gw_ara.asc"       , skiprows=6)
nin_tot_crit_dep_ara = np.loadtxt("nin_crit_dep_ara.asc"      , skiprows=6)
nh3_stor_ara         = np.loadtxt("nh3_stor_ara.asc"          , skiprows=6)
nman_fer_crit_sw_ara = np.loadtxt("nman_fer_crit_sw_ara.asc"  , skiprows=6)
nman_fer_crit_gw_ara = np.loadtxt("nman_fer_crit_gw_ara.asc"  , skiprows=6)
nman_fer_crit_de_ara = np.loadtxt("nman_fer_crit_dep_ara.asc" , skiprows=6)
# igl
nfer_igl             = np.loadtxt("nfer_igl.asc"              , skiprows=6)
nman_igl             = np.loadtxt("nman_igl.asc"              , skiprows=6)
nman_crit_sw_igl     = np.loadtxt("nman_crit_sw_igl.asc"      , skiprows=6)
nfer_crit_sw_igl     = np.loadtxt("nfer_crit_sw_igl.asc"      , skiprows=6)
nman_crit_gw_igl     = np.loadtxt("nman_crit_gw_igl.asc"      , skiprows=6)
nfer_crit_gw_igl     = np.loadtxt("nfer_crit_gw_igl.asc"      , skiprows=6)
nman_crit_de_igl     = np.loadtxt("nman_crit_dep_igl.asc"     , skiprows=6)
nfer_crit_de_igl     = np.loadtxt("nfer_crit_dep_igl.asc"     , skiprows=6)
fnup_max_sw_igl      = np.loadtxt("fnup_max_sw_igl.asc"       , skiprows=6)
fnup_max_gw_igl      = np.loadtxt("fnup_max_gw_igl.asc"       , skiprows=6)
fnup_max_de_igl      = np.loadtxt("fnup_max_dep_igl.asc"      , skiprows=6)
fnup_corr_sw_igl     = np.loadtxt("fnup_corr_sw_igl.asc"      , skiprows=6)
fnup_corr_gw_igl     = np.loadtxt("fnup_corr_gw_igl.asc"      , skiprows=6)
fnup_corr_de_igl     = np.loadtxt("fnup_corr_dep_igl.asc"     , skiprows=6)
nh3_ef_man_igl       = np.loadtxt("nh3_ef_man_igl.asc"        , skiprows=6)
nh3_ef_fer_igl       = np.loadtxt("nh3_ef_fer_igl.asc"        , skiprows=6)
nin_max_igl          = np.loadtxt("nin_max_igl.asc"           , skiprows=6)
nin_tot_crit_sw_igl  = np.loadtxt("nin_crit_sw_igl.asc"       , skiprows=6)
nin_tot_crit_gw_igl  = np.loadtxt("nin_crit_gw_igl.asc"       , skiprows=6)
nin_tot_crit_dep_igl = np.loadtxt("nin_crit_dep_igl.asc"      , skiprows=6)
nh3_stor_igl         = np.loadtxt("nh3_stor_igl.asc"          , skiprows=6)
nman_fer_crit_sw_igl = np.loadtxt("nman_fer_crit_sw_igl.asc"  , skiprows=6)
nman_fer_crit_gw_igl = np.loadtxt("nman_fer_crit_gw_igl.asc"  , skiprows=6)
nman_fer_crit_de_igl = np.loadtxt("nman_fer_crit_dep_igl.asc" , skiprows=6)

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
nup_ara            = np.loadtxt("n_up_crops.asc"               , skiprows=6)                                                                            
nup_igl            = np.loadtxt("n_up_grass_int.asc"           , skiprows=6)                                                                            

### 1c. change NA values to NaN
#general
nox_em[nox_em==-1]                        =np.nan
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
nfix_igl[nfix_igl==-2]                       =np.nan
nfix_egl[nfix_egl==-2]                       =np.nan
nh3_spred_fer_ara[nh3_spred_fer_ara==-9999]  =np.nan
nh3_spred_fer_igl[nh3_spred_fer_igl==-9999]  =np.nan
nh3_spred_man_ara[nh3_spred_man_ara==-9999]  =np.nan
nh3_spred_man_igl[nh3_spred_man_igl==-9999]  =np.nan
nh3_graz_igl[nh3_graz_igl==-9999]            =np.nan
nup_ara[nup_ara==-9999]                      =np.nan
nup_igl[nup_igl==-9999]                      =np.nan

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

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_ara)[0]):
        for j in range(np.shape(fnup_max_sw_ara)[1]):
            if (fnup_max_sw_ara[i,j] < 1 and np.isnan(fnup_max_sw_ara[i,j])==False and np.isnan(fnup_corr_sw_ara[i,j])==False):
                nfer_crit_sw_ara3[i,j] = nfer_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
                nman_crit_sw_ara3[i,j] = nman_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
    for i in range(np.shape(fnup_max_gw_ara)[0]):
        for j in range(np.shape(fnup_max_gw_ara)[1]):
            if (fnup_max_gw_ara[i,j] < 1 and np.isnan(fnup_max_gw_ara[i,j])==False and np.isnan(fnup_corr_gw_ara[i,j])==False):
                nfer_crit_gw_ara3[i,j] = nfer_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
                nman_crit_gw_ara3[i,j] = nman_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
    for i in range(np.shape(fnup_max_de_ara)[0]):
        for j in range(np.shape(fnup_max_de_ara)[1]):
            if (fnup_max_de_ara[i,j] < 1 and np.isnan(fnup_max_de_ara[i,j])==False and np.isnan(fnup_corr_de_ara[i,j])==False):
                nfer_crit_de_ara3[i,j] = nfer_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]
                nman_crit_de_ara3[i,j] = nman_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]

# select minimum
nfer_crit_mi_ara3X    = np.minimum(nfer_crit_sw_ara3,    nfer_crit_gw_ara3)
nfer_crit_mi_ara3     = np.minimum(nfer_crit_mi_ara3X,   nfer_crit_de_ara3)
nman_crit_mi_ara3X    = np.minimum(nman_crit_sw_ara3,    nman_crit_gw_ara3)
nman_crit_mi_ara3     = np.minimum(nman_crit_mi_ara3X,   nman_crit_de_ara3)

# 1b. igl
nfer_crit_sw_igl3   = np.copy(nfer_crit_sw_igl)
nman_crit_sw_igl3   = np.copy(nman_crit_sw_igl)
nfer_crit_gw_igl3   = np.copy(nfer_crit_gw_igl)
nman_crit_gw_igl3   = np.copy(nman_crit_gw_igl)
nfer_crit_de_igl3   = np.copy(nfer_crit_de_igl)
nman_crit_de_igl3   = np.copy(nman_crit_de_igl)

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_igl)[0]):
        for j in range(np.shape(fnup_max_sw_igl)[1]):
            if (fnup_max_sw_igl[i,j] < 1 and np.isnan(fnup_max_sw_igl[i,j])==False and np.isnan(fnup_corr_sw_igl[i,j])==False):
                nfer_crit_sw_igl3[i,j] = nfer_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
                nman_crit_sw_igl3[i,j] = nman_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
    for i in range(np.shape(fnup_max_gw_igl)[0]):
        for j in range(np.shape(fnup_max_gw_igl)[1]):
            if (fnup_max_gw_igl[i,j] < 1 and np.isnan(fnup_max_gw_igl[i,j])==False and np.isnan(fnup_corr_gw_igl[i,j])==False):
                nfer_crit_gw_igl3[i,j] = nfer_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
                nman_crit_gw_igl3[i,j] = nman_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
    for i in range(np.shape(fnup_max_de_igl)[0]):
        for j in range(np.shape(fnup_max_de_igl)[1]):
            if (fnup_max_de_igl[i,j] < 1 and np.isnan(fnup_max_de_igl[i,j])==False and np.isnan(fnup_corr_de_igl[i,j])==False):
                nfer_crit_de_igl3[i,j] = nfer_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]
                nman_crit_de_igl3[i,j] = nman_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]

# select minimum
nfer_crit_mi_igl3X    = np.minimum(nfer_crit_sw_igl3,    nfer_crit_gw_igl3)
nfer_crit_mi_igl3     = np.minimum(nfer_crit_mi_igl3X,   nfer_crit_de_igl3)
nman_crit_mi_igl3X    = np.minimum(nman_crit_sw_igl3,    nman_crit_gw_igl3)
nman_crit_mi_igl3     = np.minimum(nman_crit_mi_igl3X,   nman_crit_de_igl3)

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
ndep_var_crit_fer_mi_ara3 = np.multiply(nfer_crit_mi_ara3, nh3_ef_fer_ara)
ndep_var_crit_man_mi_ara3 = np.multiply(nman_crit_mi_ara3, nh3_ef_man_ara)
ndep_var_crit_tot_mi_ara3 = np.add(ndep_var_crit_fer_mi_ara3, ndep_var_crit_man_mi_ara3)
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
ndep_var_crit_fer_mi_igl3 = np.multiply(nfer_crit_mi_igl3, nh3_ef_fer_igl)
ndep_var_crit_man_mi_igl3 = np.multiply(nman_crit_mi_igl3, nh3_ef_man_igl)
ndep_var_crit_tot_mi_igl3 = np.add(ndep_var_crit_fer_mi_igl3, ndep_var_crit_man_mi_igl3)

# total variable deposition 
ndep_var_crit_tot_sw3 = np.add(ndep_var_crit_tot_sw_ara3, ndep_var_crit_tot_sw_igl3)
ndep_var_crit_tot_gw3 = np.add(ndep_var_crit_tot_gw_ara3, ndep_var_crit_tot_gw_igl3)
ndep_var_crit_tot_de3 = np.add(ndep_var_crit_tot_de_ara3, ndep_var_crit_tot_de_igl3)
ndep_var_crit_tot_mi3 = np.add(ndep_var_crit_tot_mi_ara3, ndep_var_crit_tot_mi_igl3)

# to ara
ndep_var_crit_sw3_ara = np.multiply(ndep_var_crit_tot_sw3, fara)
ndep_var_crit_gw3_ara = np.multiply(ndep_var_crit_tot_gw3, fara)
ndep_var_crit_de3_ara = np.multiply(ndep_var_crit_tot_de3, fara)
ndep_var_crit_mi3_ara = np.multiply(ndep_var_crit_tot_mi3, fara)
# to igl
ndep_var_crit_sw3_igl = np.multiply(ndep_var_crit_tot_sw3, figl)
ndep_var_crit_gw3_igl = np.multiply(ndep_var_crit_tot_gw3, figl)
ndep_var_crit_de3_igl = np.multiply(ndep_var_crit_tot_de3, figl)
ndep_var_crit_mi3_igl = np.multiply(ndep_var_crit_tot_mi3, figl)

#####################
###SELECTION ARRAY###
#####################

# a. make selection array
sel = np.copy(a_ara)
sel.fill(99)
unique, counts = np.unique(sel, return_counts=True)
a = dict(zip(unique, counts))

# b. exclude cells where nman or nfer = NA
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(sel)[1]):
            if (np.isnan(nman_ara[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_ara[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nman_igl[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nman_igl[i,j])==True):
                sel[i,j] = 0
unique, counts = np.unique(sel, return_counts=True)
b = dict(zip(unique, counts))

# c. exclude cells where nman + nfer = 0
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(sel)[1]):
            if ((nman_fer_ara[i,j])==0 and (nman_fer_igl[i,j])==0):
                sel[i,j] = 0           
unique, counts = np.unique(sel, return_counts=True)
c = dict(zip(unique, counts))

# d. exclude cells where NUE = 0 (nup = 0 and nman+nfer >0)
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(sel)[1]):
            if (nup_ara[i,j] == 0 and (nfer_ara[i,j]>0 or nman_ara[i,j]>0)):
                sel[i,j] = 0      
            if (nup_igl[i,j] == 0 and (nfer_igl[i,j]>0 or nman_igl[i,j]>0)):
                sel[i,j] = 0            
unique, counts = np.unique(sel, return_counts=True)
d = dict(zip(unique, counts))

# e. exclude cells where one of the critical inputs = NA
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(nman_crit_sw_ara3)[1]):
            if (np.isnan(nman_crit_sw_ara3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_sw_ara3[i,j])==True):
                sel[i,j] = 0   
            if (np.isnan(nman_crit_gw_ara3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_gw_ara3[i,j])==True):
                sel[i,j] = 0 
            if (np.isnan(nman_crit_de_ara3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_de_ara3[i,j])==True):
                sel[i,j] = 0 
            if (np.isnan(nman_crit_mi_ara3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_mi_ara3[i,j])==True):
                sel[i,j] = 0                 
            if (np.isnan(nman_crit_sw_igl3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_sw_igl3[i,j])==True):
                sel[i,j] = 0   
            if (np.isnan(nman_crit_gw_igl3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_gw_igl3[i,j])==True):
                sel[i,j] = 0 
            if (np.isnan(nman_crit_de_igl3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_de_igl3[i,j])==True):
                sel[i,j] = 0 
            if (np.isnan(nman_crit_mi_igl3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_crit_mi_igl3[i,j])==True):
                sel[i,j] = 0
unique, counts = np.unique(sel, return_counts=True)
e = dict(zip(unique, counts))               

print("selected-cells-BEFORE-selection-array:")
print(a)
print("selected-cells-AFTER-excluding-nman-nfer-NA: ")
print(b)
print("selected-cells-AFTER-excluding-nmanfer-zero: ")
print(c)
print("selected-cells-AFTER-excluding-NUE-zero: ")
print(d)
print("selected-cells-AFTER-excluding-nmancrit-nfercrit-NA: ")
print(e)

# ara
print("Nman_act_ara:      %.1f"   %(np.nansum(nman_ara[np.where(sel==99)])))
print("Nfer_act_ara:      %.1f"   %(np.nansum(nfer_ara[np.where(sel==99)])))
print("Ndep_var_act_ara:  %.1f"   %(np.nansum(ndep_var_act_ara[np.where(sel==99)])))
print("Ndep_fix_act_ara:  %.1f"   %(np.nansum(ndep_fixed_ara[np.where(sel==99)])))
print("Nfix_act_ara:      %.1f"   %(np.nansum(nfix_ara[np.where(sel==99)])))
print("A_ara:             %.1f"   %(np.nansum(a_ara[np.where(sel==99)])))
# igl
print("Nman_act_igl:      %.1f"   % np.nansum(nman_igl[np.where(sel==99)]))
print("Nfer_act_igl:      %.1f"   % np.nansum(nfer_igl[np.where(sel==99)]))
print("Ndep_var_act_igl:  %.1f"   % np.nansum(ndep_var_act_igl[np.where(sel==99)]))
print("Ndep_fix_act_igl:  %.1f"   % np.nansum(ndep_fixed_igl[np.where(sel==99)]))
print("Nfix_act_igl:      %.1f"   % np.nansum(nfix_igl[np.where(sel==99)]))
print("A_igl:             %.1f"   % np.nansum(a_igl[np.where(sel==99)]))
# egl
print("Nman_act_egl:      %.1f"   % np.nansum(nman_egl))
print("Nfer_act_egl:      %.1f"   % 0.0)
print("Ndep_var_act_egl:  %.1f"   % np.nansum(ndep_var_act_egl))
print("Ndep_fix_act_egl:  %.1f"   % np.nansum(ndep_fixed_egl))
print("Nfix_act_egl:      %.1f"   % np.nansum(nfix_egl))
print("A_egl:             %.1f"   % np.nansum(a_egl))

# deposition - ara
print("Nman_crit_de_ara:            %.1f" % np.nansum(nman_crit_de_ara3[np.where(sel==99)]))
print("Nfer_crit_de_ara:            %.1f" % np.nansum(nfer_crit_de_ara3[np.where(sel==99)]))
print("Ndep_var_crit_de_ara:        %.1f" % np.nansum(ndep_var_crit_de3_ara[np.where(sel==99)]))
print("Ndep_fix_crit_de_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(sel==99)]))
print("Nfix_crit_de_ara:            %.1f" % np.nansum(nfix_ara[np.where(sel==99)]))
print("Area-non-na-Nin_crit_de_ara: %.1f" % np.nansum(a_ara[np.where(sel==99)]))
# surface water - ara
print("Nman_crit_sw_ara:            %.1f" % np.nansum(nman_crit_sw_ara3[np.where(sel==99)]))
print("Nfer_crit_sw_ara:            %.1f" % np.nansum(nfer_crit_sw_ara3[np.where(sel==99)]))
print("Ndep_var_crit_sw_ara:        %.1f" % np.nansum(ndep_var_crit_sw3_ara[np.where(sel==99)]))
print("Ndep_fix_crit_sw_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(sel==99)]))
print("Nfix_crit_sw_ara:            %.1f" % np.nansum(nfix_ara[np.where(sel==99)]))
print("Area-non-na-Nin_crit_sw_ara: %.1f" % np.nansum(a_ara[np.where(sel==99)]))
# groundwater - ara
print("Nman_crit_gw_ara:            %.1f" % np.nansum(nman_crit_gw_ara3[np.where(sel==99)]))
print("Nfer_crit_gw_ara:            %.1f" % np.nansum(nfer_crit_gw_ara3[np.where(sel==99)]))
print("Ndep_var_crit_gw_ara:        %.1f" % np.nansum(ndep_var_crit_gw3_ara[np.where(sel==99)]))
print("Ndep_fix_crit_gw_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(sel==99)]))
print("Nfix_crit_gw_ara:            %.1f" % np.nansum(nfix_ara[np.where(sel==99)]))
print("Area-non-na-Nin_crit_gw_ara: %.1f" % np.nansum(a_ara[np.where(sel==99)]))
# minimum - ara
print("Nman_crit_mi_ara:            %.1f" % np.nansum(nman_crit_mi_ara3[np.where(sel==99)]))
print("Nfer_crit_mi_ara:            %.1f" % np.nansum(nfer_crit_mi_ara3[np.where(sel==99)]))
print("Ndep_var_crit_mi_ara:        %.1f" % np.nansum(ndep_var_crit_mi3_ara[np.where(sel==99)]))
print("Ndep_fix_crit_mi_ara:        %.1f" % np.nansum(ndep_fixed_ara[np.where(sel==99)]))
print("Nfix_crit_mi_ara:            %.1f" % np.nansum(nfix_ara[np.where(sel==99)]))
print("Area-non-na-Nin_crit_mi_ara: %.1f" % np.nansum(a_ara[np.where(sel==99)]))

# deposition - igl
print("Nman_crit_de_igl:            %.1f" % np.nansum(nman_crit_de_igl3[np.where(sel==99)]))
print("Nfer_crit_de_igl:            %.1f" % np.nansum(nfer_crit_de_igl3[np.where(sel==99)]))
print("Ndep_var_crit_de_igl:        %.1f" % np.nansum(ndep_var_crit_de3_igl[np.where(sel==99)]))
print("Ndep_fix_crit_de_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(sel==99)]))
print("Nfix_crit_de_igl:            %.1f" % np.nansum(nfix_igl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_de_igl: %.1f" % np.nansum(a_igl[np.where(sel==99)]))
# surface water - igl
print("Nman_crit_sw_igl:            %.1f" % np.nansum(nman_crit_sw_igl3[np.where(sel==99)]))
print("Nfer_crit_sw_igl:            %.1f" % np.nansum(nfer_crit_sw_igl3[np.where(sel==99)]))
print("Ndep_var_crit_sw_igl:        %.1f" % np.nansum(ndep_var_crit_sw3_igl[np.where(sel==99)]))
print("Ndep_fix_crit_sw_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(sel==99)]))
print("Nfix_crit_sw_igl:            %.1f" % np.nansum(nfix_igl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_sw_igl: %.1f" % np.nansum(a_igl[np.where(sel==99)]))
# groundwater - igl
print("Nman_crit_gw_igl:            %.1f" % np.nansum(nman_crit_gw_igl3[np.where(sel==99)]))
print("Nfer_crit_gw_igl:            %.1f" % np.nansum(nfer_crit_gw_igl3[np.where(sel==99)]))
print("Ndep_var_crit_gw_igl:        %.1f" % np.nansum(ndep_var_crit_gw3_igl[np.where(sel==99)]))
print("Ndep_fix_crit_gw_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(sel==99)]))
print("Nfix_crit_gw_igl:            %.1f" % np.nansum(nfix_igl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_gw_igl: %.1f" % np.nansum(a_igl[np.where(sel==99)]))
# minimum - igl
print("Nman_crit_mi_igl:            %.1f" % np.nansum(nman_crit_mi_igl3[np.where(sel==99)]))
print("Nfer_crit_mi_igl:            %.1f" % np.nansum(nfer_crit_mi_igl3[np.where(sel==99)]))
print("Ndep_var_crit_mi_igl:        %.1f" % np.nansum(ndep_var_crit_mi3_igl[np.where(sel==99)]))
print("Ndep_fix_crit_mi_igl:        %.1f" % np.nansum(ndep_fixed_igl[np.where(sel==99)]))
print("Nfix_crit_mi_igl:            %.1f" % np.nansum(nfix_igl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_mi_igl: %.1f" % np.nansum(a_igl[np.where(sel==99)]))


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
    print("total-area: %.1f" % np.nansum(a_ara[np.where(sel==99)]))
    print("case-1-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==True,  np.logical_and(np.isnan(a_ara)==False, np.logical_and(a_ara>0, sel==99)) ))]))
    print("case-2-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara<=0, sel==99))) ]))    
    print("case-3-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara>0,np.logical_and(nman_fer_crit_de_ara<=nman_fer_ara, sel==99)))) ]))
    print("case-4-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara>nman_fer_ara,np.logical_and(nman_fer_crit_de_ara<=nman_fer_crit_de_max_ara, sel==99)))) ]))
    print("case-5-de:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_de_ara)==False, np.logical_and(nman_fer_crit_de_ara>nman_fer_ara,np.logical_and(nman_fer_crit_de_ara> nman_fer_crit_de_max_ara, sel==99)))) ]))

    print("case-1-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, np.logical_and(a_ara>0, sel==99)) ))]))
    print("case-2-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara<=0, sel==99))) ]))
    print("case-3-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara>0,np.logical_and(nman_fer_crit_sw_ara<=nman_fer_ara, sel==99)))) ]))
    print("case-4-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara>nman_fer_ara,np.logical_and(nman_fer_crit_sw_ara<=nman_fer_crit_sw_max_ara, sel==99)))) ]))
    print("case-5-sw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_ara)==False, np.logical_and(nman_fer_crit_sw_ara>nman_fer_ara,np.logical_and(nman_fer_crit_sw_ara> nman_fer_crit_sw_max_ara, sel==99)))) ]))
  
    print("case-1-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==True,  np.logical_and(np.isnan(a_ara)==False, np.logical_and(a_ara>0, sel==99)) ))]))
    print("case-2-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara<=0, sel==99))) ]))
    print("case-3-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara>0,np.logical_and(nman_fer_crit_gw_ara<=nman_fer_ara, sel==99)))) ]))
    print("case-4-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara>nman_fer_ara,np.logical_and(nman_fer_crit_gw_ara<=nman_fer_crit_gw_max_ara, sel==99)))) ]))
    print("case-5-gw:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_ara)==False, np.logical_and(nman_fer_crit_gw_ara>nman_fer_ara,np.logical_and(nman_fer_crit_gw_ara> nman_fer_crit_gw_max_ara, sel==99)))) ]))

    print("case-1-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==True,  np.logical_and(np.isnan(a_ara)==False, np.logical_and(a_ara>0, sel==99)) ))]))
    print("case-2-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara<=0, sel==99))) ]))
    print("case-3-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara>0,np.logical_and(nman_fer_crit_mi_ara<=nman_fer_ara, sel==99)))) ]))
    print("case-4-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara>nman_fer_ara,np.logical_and(nman_fer_crit_mi_ara<=nman_fer_crit_gw_max_ara, sel==99)))) ]))
    print("case-5-mi:  %.1f" % np.nansum(a_ara[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_ara)==False, np.logical_and(nman_fer_crit_mi_ara>nman_fer_ara,np.logical_and(nman_fer_crit_mi_ara> nman_fer_crit_gw_max_ara, sel==99)))) ]))

    
print("CASES----IGL")
with np.errstate(invalid='ignore'):
    print("total-area: %.1f" % np.nansum(a_igl[np.where(sel==99)]))
    print("case-1-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==True,  np.logical_and(np.isnan(a_igl)==False, np.logical_and(a_igl>0, sel==99)) ))]))
    print("case-2-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl<=0, sel==99))) ]))
    print("case-3-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl>0,np.logical_and(nman_fer_crit_de_igl<=nman_fer_igl, sel==99)))) ]))
    print("case-4-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl>nman_fer_igl,np.logical_and(nman_fer_crit_de_igl<=nman_fer_crit_de_max_igl, sel==99)))) ]))
    print("case-5-de:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_de_igl)==False, np.logical_and(nman_fer_crit_de_igl>nman_fer_igl,np.logical_and(nman_fer_crit_de_igl> nman_fer_crit_de_max_igl, sel==99)))) ]))

    print("case-1-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, np.logical_and(a_igl>0, sel==99)) ))]))
    print("case-2-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl<=0, sel==99))) ]))
    print("case-3-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl>0,np.logical_and(nman_fer_crit_sw_igl<=nman_fer_igl, sel==99)))) ]))
    print("case-4-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl>nman_fer_igl,np.logical_and(nman_fer_crit_sw_igl<=nman_fer_crit_sw_max_igl, sel==99)))) ]))
    print("case-5-sw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw_igl)==False, np.logical_and(nman_fer_crit_sw_igl>nman_fer_igl,np.logical_and(nman_fer_crit_sw_igl> nman_fer_crit_sw_max_igl, sel==99)))) ]))
  
    print("case-1-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==True,  np.logical_and(np.isnan(a_igl)==False, np.logical_and(a_igl>0, sel==99)) ))]))
    print("case-2-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl<=0, sel==99))) ]))
    print("case-3-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl>0,np.logical_and(nman_fer_crit_gw_igl<=nman_fer_igl, sel==99)))) ]))
    print("case-4-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl>nman_fer_igl,np.logical_and(nman_fer_crit_gw_igl<=nman_fer_crit_gw_max_igl, sel==99)))) ]))
    print("case-5-gw:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw_igl)==False, np.logical_and(nman_fer_crit_gw_igl>nman_fer_igl,np.logical_and(nman_fer_crit_gw_igl> nman_fer_crit_gw_max_igl, sel==99)))) ]))

    print("case-1-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==True,  np.logical_and(np.isnan(a_igl)==False, np.logical_and(a_igl>0, sel==99)) ))]))
    print("case-2-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl<=0, sel==99))) ]))
    print("case-3-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl>0,np.logical_and(nman_fer_crit_mi_igl<=nman_fer_igl, sel==99)))) ]))
    print("case-4-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl>nman_fer_igl,np.logical_and(nman_fer_crit_mi_igl<=nman_fer_crit_gw_max_igl, sel==99)))) ]))
    print("case-5-mi:  %.1f" % np.nansum(a_igl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi_igl)==False, np.logical_and(nman_fer_crit_mi_igl>nman_fer_igl,np.logical_and(nman_fer_crit_mi_igl> nman_fer_crit_gw_max_igl, sel==99)))) ]))

# per-hectare values (to check for outliers)
nman_fer_crit_sw_ara3 = np.add(nman_crit_sw_ara3,nfer_crit_sw_ara3)
nman_fer_crit_gw_ara3 = np.add(nman_crit_gw_ara3,nfer_crit_gw_ara3)
nman_fer_crit_de_ara3 = np.add(nman_crit_de_ara3,nfer_crit_de_ara3)
nman_fer_crit_mi_ara3 = np.add(nman_crit_mi_ara3,nfer_crit_mi_ara3)

nman_fer_crit_sw_igl3 = np.add(nman_crit_sw_igl3,nfer_crit_sw_igl3)
nman_fer_crit_gw_igl3 = np.add(nman_crit_gw_igl3,nfer_crit_gw_igl3)
nman_fer_crit_de_igl3 = np.add(nman_crit_de_igl3,nfer_crit_de_igl3)
nman_fer_crit_mi_igl3 = np.add(nman_crit_mi_igl3,nfer_crit_mi_igl3)

with np.errstate(invalid='ignore'):
    nman_fer_ara_ha = np.divide(nman_fer_ara, a_ara)
    nman_fer_crit_sw_ara3_ha = np.divide(nman_fer_crit_sw_ara3, a_ara)
    nman_fer_crit_gw_ara3_ha = np.divide(nman_fer_crit_gw_ara3, a_ara)
    nman_fer_crit_de_ara3_ha = np.divide(nman_fer_crit_de_ara3, a_ara)
    nman_fer_crit_mi_ara3_ha = np.divide(nman_fer_crit_mi_ara3, a_ara)

    nman_fer_igl_ha = np.divide(nman_fer_igl, a_igl)
    nman_fer_crit_sw_igl3_ha = np.divide(nman_fer_crit_sw_igl3, a_igl)
    nman_fer_crit_gw_igl3_ha = np.divide(nman_fer_crit_gw_igl3, a_igl)
    nman_fer_crit_de_igl3_ha = np.divide(nman_fer_crit_de_igl3, a_igl)
    nman_fer_crit_mi_igl3_ha = np.divide(nman_fer_crit_mi_igl3, a_igl)

print("nman-fer-ara-ha-min: %.1f"         % np.nanmin(nman_fer_ara_ha[np.where(sel==99)]))
print("nman-fer-crit-sw-ara-ha-min: %.1f" % np.nanmin(nman_fer_crit_sw_ara3_ha[np.where(sel==99)]))
print("nman-fer-crit-gw-ara-ha-min: %.1f" % np.nanmin(nman_fer_crit_gw_ara3_ha[np.where(sel==99)]))
print("nman-fer-crit-de-ara-ha-min: %.1f" % np.nanmin(nman_fer_crit_de_ara3_ha[np.where(sel==99)]))
print("nman-fer-crit-mi-ara-ha-min: %.1f" % np.nanmin(nman_fer_crit_mi_ara3_ha[np.where(sel==99)]))

print("nman-fer-igl-ha-min: %.1f"         % np.nanmin(nman_fer_igl_ha[np.where(sel==99)]))
print("nman-fer-crit-sw-igl-ha-min: %.1f" % np.nanmin(nman_fer_crit_sw_igl3_ha[np.where(sel==99)]))
print("nman-fer-crit-gw-igl-ha-min: %.1f" % np.nanmin(nman_fer_crit_gw_igl3_ha[np.where(sel==99)]))
print("nman-fer-crit-de-igl-ha-min: %.1f" % np.nanmin(nman_fer_crit_de_igl3_ha[np.where(sel==99)]))
print("nman-fer-crit-mi-igl-ha-min: %.1f" % np.nanmin(nman_fer_crit_mi_igl3_ha[np.where(sel==99)]))


print("nman-fer-ara-ha-max: %.1f"         % np.nanmax(nman_fer_ara_ha[np.where(sel==99)]))
print("nman-fer-crit-sw-ara-ha-max: %.1f" % np.nanmax(nman_fer_crit_sw_ara3_ha[np.where(sel==99)]))
print("nman-fer-crit-gw-ara-ha-max: %.1f" % np.nanmax(nman_fer_crit_gw_ara3_ha[np.where(sel==99)]))
print("nman-fer-crit-de-ara-ha-max: %.1f" % np.nanmax(nman_fer_crit_de_ara3_ha[np.where(sel==99)]))
print("nman-fer-crit-mi-ara-ha-max: %.1f" % np.nanmax(nman_fer_crit_mi_ara3_ha[np.where(sel==99)]))

print("nman-fer-igl-ha-max: %.1f"         % np.nanmax(nman_fer_igl_ha[np.where(sel==99)]))
print("nman-fer-crit-sw-igl-ha-max: %.1f" % np.nanmax(nman_fer_crit_sw_igl3_ha[np.where(sel==99)]))
print("nman-fer-crit-gw-igl-ha-max: %.1f" % np.nanmax(nman_fer_crit_gw_igl3_ha[np.where(sel==99)]))
print("nman-fer-crit-de-igl-ha-max: %.1f" % np.nanmax(nman_fer_crit_de_igl3_ha[np.where(sel==99)]))
print("nman-fer-crit-mi-igl-ha-max: %.1f" % np.nanmax(nman_fer_crit_mi_igl3_ha[np.where(sel==99)]))   