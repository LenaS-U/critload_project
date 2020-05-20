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
fnup_max_sw      = np.loadtxt("fnup_max_sw.asc"          , skiprows=6)
fnup_max_gw      = np.loadtxt("fnup_max_gw.asc"          , skiprows=6)
fnup_max_de      = np.loadtxt("fnup_max_dep.asc"         , skiprows=6)
fnup_corr_sw     = np.loadtxt("fnup_corr_sw.asc"         , skiprows=6)
fnup_corr_gw     = np.loadtxt("fnup_corr_gw.asc"         , skiprows=6)
fnup_corr_de     = np.loadtxt("fnup_corr_dep.asc"        , skiprows=6)
nfer_agri        = np.loadtxt("n_fert_agri.asc"          , skiprows=6) 
nman_agri        = np.loadtxt("n_man_agri.asc"           , skiprows=6)

### 1b. Read files from *INPUT* directory
os.chdir('c:\\users')
os.chdir('schul028')
os.chdir('OneDrive - WageningenUR')
os.chdir('critload_project')
os.chdir('Model Version1.4')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

a_ara         = np.loadtxt("a_crop.asc"                   , skiprows=6)
a_igl         = np.loadtxt("a_gr_int.asc"                 , skiprows=6)

### 1c. change NA values to NaN
mancritsw[mancritsw==-9999]               =np.nan 
fercritsw[fercritsw==-9999]               =np.nan
mancritgw[mancritgw==-9999]               =np.nan
fercritgw[fercritgw==-9999]               =np.nan
mancritde[mancritde==-9999]               =np.nan
fercritde[fercritde==-9999]               =np.nan
fnup_max_sw[fnup_max_sw==-9999]           =np.nan
fnup_max_gw[fnup_max_gw==-9999]           =np.nan
fnup_max_de[fnup_max_de==-9999]           =np.nan
fnup_corr_sw[fnup_corr_sw==-9999]         =np.nan
fnup_corr_gw[fnup_corr_gw==-9999]         =np.nan
fnup_corr_de[fnup_corr_de==-9999]         =np.nan
nfer_agri[nfer_agri==-9999]               =np.nan
nman_agri[nman_agri==-9999]               =np.nan

a_ara[a_ara==-1]                          =np.nan
a_igl[a_igl==-1]                          =np.nan

##########################################
# Total critical N inputs (after cutoff) #
##########################################
# add fert+mancritde
nman_fer_crit_sw = np.add(mancritsw,fercritsw)
nman_fer_crit_gw = np.add(mancritgw,fercritgw)
nman_fer_crit_de = np.add(mancritde,fercritde)

# 1. Cut-off at maximum N input
nman_fer_crit_sw3   = np.copy(nman_fer_crit_sw)
nman_fer_crit_gw3   = np.copy(nman_fer_crit_gw)
nman_fer_crit_de3   = np.copy(nman_fer_crit_de)

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw)[0]):
        for j in range(np.shape(fnup_max_sw)[1]):
            if (fnup_max_sw[i,j] < 1 and np.isnan(fnup_max_sw[i,j])==False):
                nman_fer_crit_sw3[i,j] = nman_fer_crit_sw3[i,j]*fnup_corr_sw[i,j]
    for i in range(np.shape(fnup_max_gw)[0]):
        for j in range(np.shape(fnup_max_gw)[1]):
            if (fnup_max_gw[i,j] < 1 and np.isnan(fnup_max_gw[i,j])==False):
                nman_fer_crit_gw3[i,j] = nman_fer_crit_gw3[i,j]*fnup_corr_gw[i,j]
    for i in range(np.shape(fnup_max_de)[0]):
        for j in range(np.shape(fnup_max_de)[1]):
            if (fnup_max_de[i,j] < 1 and np.isnan(fnup_max_de[i,j])==False):
                nman_fer_crit_de3[i,j] = nman_fer_crit_de3[i,j]*fnup_corr_de[i,j]

# select minimum
nman_fer_crit_mi3X  = np.minimum(nman_fer_crit_sw3,  nman_fer_crit_gw3)
nman_fer_crit_mi3   = np.minimum(nman_fer_crit_mi3X, nman_fer_crit_de3)

# CALCULATIONS
# current inputs
nman_fer_araigl    = np.add(nman_agri, nfer_agri)

# areas
a_araigl = np.add(a_ara, a_igl)


#PLOTS

# araigl
exceedance_sw_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_sw3)
exceedance_gw_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_gw3)
exceedance_de_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_de3)
exceedance_mi_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_mi3)
exceedance_sw_ha_araigl = np.divide(exceedance_sw_araigl, a_araigl)
exceedance_gw_ha_araigl = np.divide(exceedance_gw_araigl, a_araigl)
exceedance_de_ha_araigl = np.divide(exceedance_de_araigl, a_araigl)
exceedance_mi_ha_araigl = np.divide(exceedance_mi_araigl, a_araigl)


# plot map with exceedances
# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_mi_ha_araigl[np.isnan(a_ara)]= -99999
    
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_mi_ha_araigl, cmap=cmap, vmin=-1000) # exceedance critical N inputs minimum
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs [minimum - ara+igl (old)]")
plt.show()









