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
fegl             = np.loadtxt("fegl.asc"                 , skiprows=6)
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
nfix_egl      = np.loadtxt("nfix_grass_ext.asc"           , skiprows=6)
a_ara         = np.loadtxt("a_crop.asc"                   , skiprows=6)
a_igl         = np.loadtxt("a_gr_int.asc"                 , skiprows=6)
a_egl         = np.loadtxt("a_gr_ext.asc"                 , skiprows=6) 
nup_ara       = np.loadtxt("n_up_crops.asc"               , skiprows=6)
nup_igl       = np.loadtxt("n_up_grass_int.asc"           , skiprows=6)

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
fegl[fegl==-1]                            =np.nan
nox_em[nox_em==-1]                        =np.nan
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
nfix_igl[nfix_igl==-2]                    =np.nan
nfix_egl[nfix_egl==-2]                    =np.nan
a_ara[a_ara==-1]                          =np.nan
a_igl[a_igl==-1]                          =np.nan
a_egl[a_egl==-1]                          =np.nan
nup_ara[nup_ara==-9999]                   =np.nan
nup_igl[nup_igl==-9999]                   =np.nan

#########################
# Total actual N inputs #
#########################

ndep_fixed          = np.add(nox_em, nh3_tot_egl)
ndep_fixed_araigl   = np.multiply(ndep_fixed, fagri)
ndep_fixed_egl      = np.multiply(ndep_fixed, fegl)

ndep_var_act_araigl = np.multiply(nh3_tot_agri, fagri)
ndep_var_act_egl    = np.multiply(nh3_tot_agri, fegl)

manfer_araigl       = np.add(nfer_agri,nman_agri)
nfix_araigl         = np.add(nfix_ara,nfix_igl)
a_araigl            = np.add(a_ara, a_igl)
nup_araigl          = np.add(nup_ara, nup_igl)

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

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw)[0]):
        for j in range(np.shape(fnup_max_sw)[1]):
            if (fnup_max_sw[i,j] < 1 and np.isnan(fnup_max_sw[i,j])==False and np.isnan(fnup_corr_sw[i,j])==False):
                fercritsw3[i,j] = fercritsw3[i,j]*fnup_corr_sw[i,j]
                mancritsw3[i,j] = mancritsw3[i,j]*fnup_corr_sw[i,j]
    for i in range(np.shape(fnup_max_gw)[0]):
        for j in range(np.shape(fnup_max_gw)[1]):
            if (fnup_max_gw[i,j] < 1 and np.isnan(fnup_max_gw[i,j])==False and np.isnan(fnup_corr_gw[i,j])==False):
                fercritgw3[i,j] = fercritgw3[i,j]*fnup_corr_gw[i,j]
                mancritgw3[i,j] = mancritgw3[i,j]*fnup_corr_gw[i,j]
    for i in range(np.shape(fnup_max_de)[0]):
        for j in range(np.shape(fnup_max_de)[1]):
            if (fnup_max_de[i,j] < 1 and np.isnan(fnup_max_de[i,j])==False and np.isnan(fnup_corr_de[i,j])==False):
                fercritde3[i,j] = fercritde3[i,j]*fnup_corr_de[i,j]
                mancritde3[i,j] = mancritde3[i,j]*fnup_corr_de[i,j]

# select minimum
fercritmi3X    = np.minimum(fercritsw3, fercritgw3)
fercritmi3     = np.minimum(fercritmi3X, fercritde3)
mancritmi3X    = np.minimum(mancritsw3, mancritgw3)
mancritmi3     = np.minimum(mancritmi3X, mancritde3)

#############################################

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
ndep_var_crit_fer_mi3 = np.multiply(fercritmi3, nh3_ef_fer)
ndep_var_crit_man_mi3 = np.multiply(mancritmi3, nh3_ef_man)
ndep_var_crit_tot_mi3 = np.add(ndep_var_crit_fer_mi3, ndep_var_crit_man_mi3)

# to araigl
ndep_var_crit_sw3_araigl = np.multiply(ndep_var_crit_tot_sw3, fagri)
ndep_var_crit_gw3_araigl = np.multiply(ndep_var_crit_tot_gw3, fagri)
ndep_var_crit_de3_araigl = np.multiply(ndep_var_crit_tot_de3, fagri)
ndep_var_crit_mi3_araigl = np.multiply(ndep_var_crit_tot_mi3, fagri)

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
            if (np.isnan(nman_agri[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(nfer_agri[i,j])==True):
                sel[i,j] = 0
unique, counts = np.unique(sel, return_counts=True)
b = dict(zip(unique, counts))

# c. exclude cells where nman + nfer = 0
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(sel)[1]):
            if (manfer_araigl[i,j])==0:
                sel[i,j] = 0           
unique, counts = np.unique(sel, return_counts=True)
c = dict(zip(unique, counts))

# d. exclude cells where NUE = 0 (nup = 0 and nman+nfer >0)                
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(sel)[1]):
            if (nup_araigl[i,j] == 0 and (nfer_agri[i,j]>0 or nman_agri[i,j]>0)):
                sel[i,j] = 0 
            # artificially exclude one extra grid cell, in order to have the same population as V2.1
            if (a_ara[i,j] == a_ara.item(72197)):
                sel[i,j] = 0             
unique, counts = np.unique(sel, return_counts=True)
d = dict(zip(unique, counts))

# e. exclude cells where one of the critical inputs = NA
for i in range(np.shape(sel)[0]):
        for j in range(np.shape(sel)[1]):        
            if (np.isnan(mancritsw3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(fercritsw3[i,j])==True):
                sel[i,j] = 0   
            if (np.isnan(mancritgw3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(fercritgw3[i,j])==True):
                sel[i,j] = 0 
            if (np.isnan(mancritde3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(fercritde3[i,j])==True):
                sel[i,j] = 0 
            if (np.isnan(mancritmi3[i,j])==True):
                sel[i,j] = 0
            if (np.isnan(fercritmi3[i,j])==True):
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

# ara + igl
print("Nman_act_araigl:      %.1f"   %(np.nansum(nman_agri[np.where(sel==99)])))
print("Nfer_act_araigl:      %.1f"   %(np.nansum(nfer_agri[np.where(sel==99)])))
print("Ndep_var_act_araigl:  %.1f"   %(np.nansum(ndep_var_act_araigl[np.where(sel==99)])))
print("Ndep_fix_act_araigl:  %.1f"   %(np.nansum(ndep_fixed_araigl[np.where(sel==99)])))
print("Nfix_act_araigl:      %.1f"   %(np.nansum(nfix_araigl[np.where(sel==99)])))
print("A_araigl:             %.1f"   %(np.nansum(a_araigl[np.where(sel==99)])))
# placeholders (to make comparable with summary_output_V3.py for Model 2)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
# egl
print("Nman_act_egl:      %.1f"   %(np.nansum(nman_egl)))
print("Nfer_act_egl:      %.1f"   % 0.0)
print("Ndep_var_act_egl:  %.1f"   %(np.nansum(ndep_var_act_egl)))
print("Ndep_fix_act_egl:  %.1f"   %(np.nansum(ndep_fixed_egl)))
print("Nfix_act_egl:      %.1f"   %(np.nansum(nfix_egl)))
print("A_egl:             %.1f"   %(np.nansum(a_egl)))

# deposition - araigl
print("Nman_crit_de_araigl:            %.1f" % np.nansum(mancritde3[np.where(sel==99)]))
print("Nfer_crit_de_araigl:            %.1f" % np.nansum(fercritde3[np.where(sel==99)]))
print("Ndep_var_crit_de_araigl:        %.1f" % np.nansum(ndep_var_crit_de3_araigl[np.where(sel==99)]))
print("Ndep_fix_crit_de_araigl:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(sel==99)]))
print("Nfix_crit_de_araigl:            %.1f" % np.nansum(nfix_araigl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_de_araigl: %.1f" % np.nansum(a_araigl[np.where(sel==99)]))
# surface water - araigl
print("Nman_crit_sw_ara:            %.1f" % np.nansum(mancritsw3[np.where(sel==99)]))
print("Nfer_crit_sw_ara:            %.1f" % np.nansum(fercritsw3[np.where(sel==99)]))
print("Ndep_var_crit_sw_ara:        %.1f" % np.nansum(ndep_var_crit_sw3_araigl[np.where(sel==99)]))
print("Ndep_fix_crit_sw_ara:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(sel==99)]))
print("Nfix_crit_sw_ara:            %.1f" % np.nansum(nfix_araigl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_sw_ara: %.1f" % np.nansum(a_araigl[np.where(sel==99)]))
# groundwater - araigl
print("Nman_crit_gw_ara:            %.1f" % np.nansum(mancritgw3[np.where(sel==99)]))
print("Nfer_crit_gw_ara:            %.1f" % np.nansum(fercritgw3[np.where(sel==99)]))
print("Ndep_var_crit_gw_ara:        %.1f" % np.nansum(ndep_var_crit_gw3_araigl[np.where(sel==99)]))
print("Ndep_fix_crit_gw_ara:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(sel==99)]))
print("Nfix_crit_gw_ara:            %.1f" % np.nansum(nfix_araigl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_gw_ara: %.1f" % np.nansum(a_araigl[np.where(sel==99)]))
# minimum - araigl
print("Nman_crit_mi_ara:            %.1f" % np.nansum(mancritmi3[np.where(sel==99)]))
print("Nfer_crit_mi_ara:            %.1f" % np.nansum(fercritmi3[np.where(sel==99)]))
print("Ndep_var_crit_mi_ara:        %.1f" % np.nansum(ndep_var_crit_mi3_araigl[np.where(sel==99)]))
print("Ndep_fix_crit_mi_ara:        %.1f" % np.nansum(ndep_fixed_araigl[np.where(sel==99)]))
print("Nfix_crit_mi_ara:            %.1f" % np.nansum(nfix_araigl[np.where(sel==99)]))
print("Area-non-na-Nin_crit_mi_ara: %.1f" % np.nansum(a_araigl[np.where(sel==99)]))

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

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
    print("case-1-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==True,  np.logical_and(np.isnan(a_araigl)==False, np.logical_and(a_araigl>0, sel==99)) ))]))
    print("case-2-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de<=0, sel==99))) ]))
    print("case-3-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de>0, np.logical_and(nman_fer_crit_de<=manfer_araigl, sel==99)))) ]))
    print("case-4-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de>manfer_araigl,np.logical_and(nman_fer_crit_de<=nman_fer_crit_de_max, sel==99)))) ]))
    print("case-5-de:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_de)==False, np.logical_and(nman_fer_crit_de>manfer_araigl,np.logical_and(nman_fer_crit_de> nman_fer_crit_de_max, sel==99)))) ]))

    print("case-1-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==True,  np.logical_and(np.isnan(a_araigl)==False, np.logical_and(a_araigl>0, sel==99)) ))]))
    print("case-2-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw<=0, sel==99))) ]))
    print("case-3-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw>0, np.logical_and(nman_fer_crit_sw<=manfer_araigl, sel==99)))) ]))
    print("case-4-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw>manfer_araigl,np.logical_and(nman_fer_crit_sw<=nman_fer_crit_sw_max, sel==99)))) ]))
    print("case-5-sw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_sw)==False, np.logical_and(nman_fer_crit_sw>manfer_araigl,np.logical_and(nman_fer_crit_sw> nman_fer_crit_sw_max, sel==99)))) ]))
  
    print("case-1-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==True,  np.logical_and(np.isnan(a_araigl)==False, np.logical_and(a_araigl>0, sel==99)) ))]))
    print("case-2-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw<=0, sel==99))) ]))
    print("case-3-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw>0, np.logical_and(nman_fer_crit_gw<=manfer_araigl, sel==99)))) ]))
    print("case-4-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw>manfer_araigl,np.logical_and(nman_fer_crit_gw<=nman_fer_crit_gw_max, sel==99)))) ]))
    print("case-5-gw:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_gw)==False, np.logical_and(nman_fer_crit_gw>manfer_araigl,np.logical_and(nman_fer_crit_gw> nman_fer_crit_gw_max, sel==99)))) ]))
   
    print("case-1-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==True,  np.logical_and(np.isnan(a_araigl)==False, np.logical_and(a_araigl>0, sel==99)) ))]))
    print("case-2-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi<=0, sel==99))) ]))
    print("case-3-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi>0, np.logical_and(nman_fer_crit_mi<=manfer_araigl, sel==99)))) ]))
    print("case-4-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi>manfer_araigl,np.logical_and(nman_fer_crit_mi<=nman_fer_crit_gw_max, sel==99)))) ]))
    print("case-5-mi:  %.1f" % np.nansum(a_araigl[np.where(np.logical_and(np.isnan(nman_fer_crit_mi)==False, np.logical_and(nman_fer_crit_mi>manfer_araigl,np.logical_and(nman_fer_crit_mi> nman_fer_crit_gw_max, sel==99)))) ]))
  
# per-hectare values (to check for outliers)
nman_fer_crit_sw3 = np.add(mancritsw3,fercritsw3)
nman_fer_crit_gw3 = np.add(mancritgw3,fercritgw3)
nman_fer_crit_de3 = np.add(mancritde3,fercritde3)
nman_fer_crit_mi3 = np.add(mancritmi3,fercritmi3)

with np.errstate(invalid='ignore'):
    nman_fer_ha = np.divide(manfer_araigl, a_araigl)
    nman_fer_crit_sw3_ha = np.divide(nman_fer_crit_sw3, a_araigl)
    nman_fer_crit_gw3_ha = np.divide(nman_fer_crit_gw3, a_araigl)
    nman_fer_crit_de3_ha = np.divide(nman_fer_crit_de3, a_araigl)
    nman_fer_crit_mi3_ha = np.divide(nman_fer_crit_mi3, a_araigl)

print("nman-fer-ha-min: %.1f"         % np.nanmin(nman_fer_ha[np.where(sel==99)]))
print("nman-fer-crit-sw-ha-min: %.1f" % np.nanmin(nman_fer_crit_sw3_ha[np.where(sel==99)]))
print("nman-fer-crit-gw-ha-min: %.1f" % np.nanmin(nman_fer_crit_gw3_ha[np.where(sel==99)]))
print("nman-fer-crit-de-ha-min: %.1f" % np.nanmin(nman_fer_crit_de3_ha[np.where(sel==99)]))
print("nman-fer-crit-mi-ha-min: %.1f" % np.nanmin(nman_fer_crit_mi3_ha[np.where(sel==99)]))

print("nman-fer-ha-max: %.1f"         % np.nanmax(nman_fer_ha[np.where(sel==99)]))
print("nman-fer-crit-sw-ha-max: %.1f" % np.nanmax(nman_fer_crit_sw3_ha[np.where(sel==99)]))
print("nman-fer-crit-gw-ha-max: %.1f" % np.nanmax(nman_fer_crit_gw3_ha[np.where(sel==99)]))
print("nman-fer-crit-de-ha-max: %.1f" % np.nanmax(nman_fer_crit_de3_ha[np.where(sel==99)]))
print("nman-fer-crit-mi-ha-max: %.1f" % np.nanmax(nman_fer_crit_mi3_ha[np.where(sel==99)]))                                                                                                                                                                        