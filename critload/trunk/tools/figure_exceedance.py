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


# ara
nfer_ara             = np.loadtxt("nfer_ara.asc"            , skiprows=6)
nman_ara             = np.loadtxt("nman_ara.asc"            , skiprows=6)
fnup_max_sw_ara      = np.loadtxt("fnup_max_sw_ara.asc"     , skiprows=6)
fnup_max_gw_ara      = np.loadtxt("fnup_max_gw_ara.asc"     , skiprows=6)
fnup_max_de_ara      = np.loadtxt("fnup_max_dep_ara.asc"    , skiprows=6)
fnup_corr_sw_ara     = np.loadtxt("fnup_corr_sw_ara.asc"    , skiprows=6)
fnup_corr_gw_ara     = np.loadtxt("fnup_corr_gw_ara.asc"    , skiprows=6)
fnup_corr_de_ara     = np.loadtxt("fnup_corr_dep_ara.asc"   , skiprows=6)
nman_fer_crit_sw_ara = np.loadtxt("nman_fer_crit_sw_ara.asc"        , skiprows=6)
nman_fer_crit_gw_ara = np.loadtxt("nman_fer_crit_gw_ara.asc"        , skiprows=6)
nman_fer_crit_de_ara = np.loadtxt("nman_fer_crit_dep_ara.asc"       , skiprows=6)
# igl
nfer_igl             = np.loadtxt("nfer_igl.asc"            , skiprows=6)
nman_igl             = np.loadtxt("nman_igl.asc"            , skiprows=6)
fnup_max_sw_igl      = np.loadtxt("fnup_max_sw_igl.asc"     , skiprows=6)
fnup_max_gw_igl      = np.loadtxt("fnup_max_gw_igl.asc"     , skiprows=6)
fnup_max_de_igl      = np.loadtxt("fnup_max_dep_igl.asc"    , skiprows=6)
fnup_corr_sw_igl     = np.loadtxt("fnup_corr_sw_igl.asc"    , skiprows=6)
fnup_corr_gw_igl     = np.loadtxt("fnup_corr_gw_igl.asc"    , skiprows=6)
fnup_corr_de_igl     = np.loadtxt("fnup_corr_dep_igl.asc"   , skiprows=6)
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


### 1c. change NA values to NaN
# ara
nfer_ara[nfer_ara==-9999]                         =np.nan
nman_ara[nman_ara==-9999]                         =np.nan
fnup_max_sw_ara[fnup_max_sw_ara==-9999]           =np.nan
fnup_max_gw_ara[fnup_max_gw_ara==-9999]           =np.nan
fnup_max_de_ara[fnup_max_de_ara==-9999]           =np.nan
fnup_corr_sw_ara[fnup_corr_sw_ara==-9999]         =np.nan
fnup_corr_gw_ara[fnup_corr_gw_ara==-9999]         =np.nan
fnup_corr_de_ara[fnup_corr_de_ara==-9999]         =np.nan
nman_fer_crit_sw_ara[nman_fer_crit_sw_ara==-9999] =np.nan
nman_fer_crit_gw_ara[nman_fer_crit_gw_ara==-9999] =np.nan
nman_fer_crit_de_ara[nman_fer_crit_de_ara==-9999] =np.nan
# igl
nfer_igl[nfer_igl==-9999]                         =np.nan
nman_igl[nman_igl==-9999]                         =np.nan
fnup_max_sw_igl[fnup_max_sw_igl==-9999]           =np.nan
fnup_max_gw_igl[fnup_max_gw_igl==-9999]           =np.nan
fnup_max_de_igl[fnup_max_de_igl==-9999]           =np.nan
fnup_corr_sw_igl[fnup_corr_sw_igl==-9999]         =np.nan
fnup_corr_gw_igl[fnup_corr_gw_igl==-9999]         =np.nan
fnup_corr_de_igl[fnup_corr_de_igl==-9999]         =np.nan
nman_fer_crit_sw_igl[nman_fer_crit_sw_igl==-9999] =np.nan
nman_fer_crit_gw_igl[nman_fer_crit_gw_igl==-9999] =np.nan
nman_fer_crit_de_igl[nman_fer_crit_de_igl==-9999] =np.nan

a_ara[a_ara==-1]                             =np.nan
a_igl[a_igl==-1]                             =np.nan

##########################################
# Total critical N inputs (after cutoff) #
##########################################
# 1. Cut-off at maximum N input
# 1a. ara
nman_fer_crit_sw_ara3   = np.copy(nman_fer_crit_sw_ara)
nman_fer_crit_gw_ara3   = np.copy(nman_fer_crit_gw_ara)
nman_fer_crit_de_ara3   = np.copy(nman_fer_crit_de_ara)

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_ara)[0]):
        for j in range(np.shape(fnup_max_sw_ara)[1]):
            if (fnup_max_sw_ara[i,j] < 1 and np.isnan(fnup_max_sw_ara[i,j])==False):
                nman_fer_crit_sw_ara3[i,j] = nman_fer_crit_sw_ara3[i,j]*fnup_corr_sw_ara[i,j]
    for i in range(np.shape(fnup_max_gw_ara)[0]):
        for j in range(np.shape(fnup_max_gw_ara)[1]):
            if (fnup_max_gw_ara[i,j] < 1 and np.isnan(fnup_max_gw_ara[i,j])==False):
                nman_fer_crit_gw_ara3[i,j] = nman_fer_crit_gw_ara3[i,j]*fnup_corr_gw_ara[i,j]
    for i in range(np.shape(fnup_max_de_ara)[0]):
        for j in range(np.shape(fnup_max_de_ara)[1]):
            if (fnup_max_de_ara[i,j] < 1 and np.isnan(fnup_max_de_ara[i,j])==False):
                nman_fer_crit_de_ara3[i,j] = nman_fer_crit_de_ara3[i,j]*fnup_corr_de_ara[i,j]

# select minimum
nman_fer_crit_mi_ara3X  = np.minimum(nman_fer_crit_sw_ara3,  nman_fer_crit_gw_ara3)
nman_fer_crit_mi_ara3   = np.minimum(nman_fer_crit_mi_ara3X, nman_fer_crit_de_ara3)

# 1b. igl
nman_fer_crit_sw_igl3   = np.copy(nman_fer_crit_sw_igl)
nman_fer_crit_gw_igl3   = np.copy(nman_fer_crit_gw_igl)
nman_fer_crit_de_igl3   = np.copy(nman_fer_crit_de_igl)

# replace critical N inputs > Nin,max with Nin,max
with np.errstate(invalid='ignore'):
    for i in range(np.shape(fnup_max_sw_igl)[0]):
        for j in range(np.shape(fnup_max_sw_igl)[1]):
            if (fnup_max_sw_igl[i,j] < 1 and np.isnan(fnup_max_sw_igl[i,j])==False):
                nman_fer_crit_sw_igl3[i,j] = nman_fer_crit_sw_igl3[i,j]*fnup_corr_sw_igl[i,j]
    for i in range(np.shape(fnup_max_gw_igl)[0]):
        for j in range(np.shape(fnup_max_gw_igl)[1]):
            if (fnup_max_gw_igl[i,j] < 1 and np.isnan(fnup_max_gw_igl[i,j])==False):
                nman_fer_crit_gw_igl3[i,j] = nman_fer_crit_gw_igl3[i,j]*fnup_corr_gw_igl[i,j]
    for i in range(np.shape(fnup_max_de_igl)[0]):
        for j in range(np.shape(fnup_max_de_igl)[1]):
            if (fnup_max_de_igl[i,j] < 1 and np.isnan(fnup_max_de_igl[i,j])==False):
                nman_fer_crit_de_igl3[i,j] = nman_fer_crit_de_igl3[i,j]*fnup_corr_de_igl[i,j]

# select minimum
nman_fer_crit_mi_igl3X  = np.minimum(nman_fer_crit_sw_igl3,  nman_fer_crit_gw_igl3)
nman_fer_crit_mi_igl3   = np.minimum(nman_fer_crit_mi_igl3X, nman_fer_crit_de_igl3)


# CALCULATIONS
# current inputs
nman_fer_ara    = np.add(nman_ara, nfer_ara)
nman_fer_igl    = np.add(nman_igl, nfer_igl)
nman_fer_araigl = np.add(nman_fer_ara, nman_fer_igl)
# areas
a_araigl = np.add(a_ara, a_igl)
# Critical inputs ara+igl
nman_fer_crit_sw_araigl3 = np.add(nman_fer_crit_sw_ara3,nman_fer_crit_sw_igl3)
nman_fer_crit_gw_araigl3 = np.add(nman_fer_crit_gw_ara3,nman_fer_crit_gw_igl3)
nman_fer_crit_de_araigl3 = np.add(nman_fer_crit_de_ara3,nman_fer_crit_de_igl3)

# MINIMUM CRITICAL N INPUTS MANURE + FERTILIZER
# 'araigl'
nman_fer_crit_mi_araigl3X = np.minimum(nman_fer_crit_sw_araigl3,  nman_fer_crit_gw_araigl3)
nman_fer_crit_mi_araigl3  = np.minimum(nman_fer_crit_mi_araigl3X, nman_fer_crit_de_araigl3)

#PLOTS

# Exceedance of critical N inputs by actual N inputs
# ara
exceedance_sw_ara = np.subtract(nman_fer_ara, nman_fer_crit_sw_ara3)
exceedance_gw_ara = np.subtract(nman_fer_ara, nman_fer_crit_gw_ara3)
exceedance_de_ara = np.subtract(nman_fer_ara, nman_fer_crit_de_ara3)
exceedance_mi_ara = np.subtract(nman_fer_ara, nman_fer_crit_mi_ara3)
with np.errstate(invalid='ignore'): 
    exceedance_sw_ha_ara = np.divide(exceedance_sw_ara, a_ara)
    exceedance_gw_ha_ara = np.divide(exceedance_gw_ara, a_ara)
    exceedance_de_ha_ara = np.divide(exceedance_de_ara, a_ara)
    exceedance_mi_ha_ara = np.divide(exceedance_mi_ara, a_ara)

#igl
exceedance_sw_igl = np.subtract(nman_fer_igl, nman_fer_crit_sw_igl3)
exceedance_gw_igl = np.subtract(nman_fer_igl, nman_fer_crit_gw_igl3)
exceedance_de_igl = np.subtract(nman_fer_igl, nman_fer_crit_de_igl3)
exceedance_mi_igl = np.subtract(nman_fer_igl, nman_fer_crit_mi_igl3)
with np.errstate(invalid='ignore'): 
    exceedance_sw_ha_igl = np.divide(exceedance_sw_igl, a_igl)
    exceedance_gw_ha_igl = np.divide(exceedance_gw_igl, a_igl)
    exceedance_de_ha_igl = np.divide(exceedance_de_igl, a_igl)
    exceedance_mi_ha_igl = np.divide(exceedance_mi_igl, a_igl)

# araigl
exceedance_sw_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_sw_araigl3)
exceedance_gw_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_gw_araigl3)
exceedance_de_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_de_araigl3)
exceedance_mi_araigl = np.subtract(nman_fer_araigl, nman_fer_crit_mi_araigl3)
exceedance_sw_ha_araigl = np.divide(exceedance_sw_araigl, a_araigl)
exceedance_gw_ha_araigl = np.divide(exceedance_gw_araigl, a_araigl)
exceedance_de_ha_araigl = np.divide(exceedance_de_araigl, a_araigl)
exceedance_mi_ha_araigl = np.divide(exceedance_mi_araigl, a_araigl)


# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_de_ha_araigl[np.isnan(a_ara)]= -99999


# plot map with exceedances

# ara
# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_mi_ha_ara[np.isnan(a_ara)]= -99999
    
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_mi_ha_ara, cmap=cmap, vmin=-1000) # exceedance critical N inputs 
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs [minimum - ara]")
plt.show()

# igl
# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_mi_ha_igl[np.isnan(a_igl)]= -99999
    
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_mi_ha_igl, cmap=cmap, vmin=-1000) # exceedance critical N inputs 
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs [minimum - igl]")
plt.show()

# araigl
# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_mi_ha_araigl[np.isnan(a_ara)]= -99999
    
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_mi_ha_araigl, cmap=cmap, vmin=-1000) # exceedance critical N inputs 
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs [minimum - ara+igl]")
plt.show()









