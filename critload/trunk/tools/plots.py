import os
import numpy as np
import matplotlib.pyplot as plt

# read files from output directory
os.chdir('d:\\critload_project')
os.chdir('critload2')
os.chdir('trunk')
os.chdir('output')
os.chdir('1999')

mancritsw = np.loadtxt("nman_crit_sw.asc"  , skiprows=6)
fercritsw = np.loadtxt("nfert_crit_sw.asc" , skiprows=6)
mancritgw = np.loadtxt("nman_crit_gw.asc"  , skiprows=6)
fercritgw = np.loadtxt("nfert_crit_gw.asc" , skiprows=6)
mancritde = np.loadtxt("nman_crit_dep.asc" , skiprows=6)
fercritde = np.loadtxt("nfert_crit_dep.asc", skiprows=6)
frnfe     = np.loadtxt("frnfe.asc"         , skiprows=6)

# read files from input directory
os.chdir('d:\\critload_project')
os.chdir('critload2')
os.chdir('trunk')
os.chdir('input')
os.chdir('1999')

agarea    = np.loadtxt("a_ag.asc"          , skiprows=6)
nfer      = np.loadtxt("n_fe_eff.asc"      , skiprows=6)
nman      = np.loadtxt("n_man_eff.asc"     , skiprows=6)
fgwrecag  = np.loadtxt("fgw_rec_ag.asc"    , skiprows=6)
fgwrecna  = np.loadtxt("fgw_rec_nat.asc"   , skiprows=6)
ndep      = np.loadtxt("ndep.asc"          , skiprows=6)
nh3emfert = np.loadtxt("nh3_spread_fe.asc" , skiprows=6)
nh3emappl = np.loadtxt("nh3_spread_man.asc", skiprows=6)
nh3emstor = np.loadtxt("nh3_stor.asc"      , skiprows=6)
nh3emgraz = np.loadtxt("nh3_graz.asc"      , skiprows=6)

# change NA values to NaN
mancritsw[mancritsw==-9999]=np.nan 
fercritsw[fercritsw==-9999]=np.nan
mancritgw[mancritgw==-1]   =np.nan
fercritgw[fercritgw==-1]   =np.nan
mancritde[mancritde==0]    =np.nan
fercritde[fercritde==0]    =np.nan
fgwrecag[fgwrecag==-9999]  =np.nan
fgwrecna[fgwrecna==-9999]  =np.nan
agarea[agarea==-2]         =np.nan
nfer[nfer==-9999]          =np.nan
nman[nman==-9999]          =np.nan
frnfe[frnfe==-9999]        =np.nan
ndep[ndep==-1]             =np.nan
nh3emfert[nh3emfert==-9999]=np.nan
nh3emappl[nh3emappl==-9999]=np.nan
nh3emstor[nh3emstor==-9999]=np.nan
nh3emgraz[nh3emgraz==-9999]=np.nan

# calculate current and critical inputs per hectare
manha       = np.divide(nman, agarea)
ferha       = np.divide(nfer, agarea)
mancritswha = np.divide(mancritsw, agarea)
fercritswha = np.divide(fercritsw, agarea)
mancritgwha = np.divide(mancritgw, agarea)
fercritgwha = np.divide(fercritgw, agarea)
mancritdeha = np.divide(mancritde, agarea)
fercritdeha = np.divide(fercritde, agarea)

### Plot current and critical N inputs per hectare
# Current inputs 
plt.subplot(1,2,1)
plt.imshow(ferha)
plt.colorbar()
plt.title(" N inputs from fertilizer (kg N ha-1 yr-1)")

plt.subplot(1,2,2)
plt.imshow(manha)
plt.colorbar()
plt.title(" N inputs from manure (kg N ha-1 yr-1)")

plt.show()

# Critical inputs
plt.subplot(3, 2, 1)
plt.imshow(mancritswha)
plt.colorbar(extend='both')
plt.clim(0, 350)
plt.title("Manure - surface water quality")

plt.subplot(3, 2, 2)
plt.imshow(fercritswha)
plt.colorbar(extend='both')
plt.clim(0, 350)
plt.title("Fertilizer - surface water quality")

plt.subplot(3, 2, 3)
plt.imshow(mancritgwha)
plt.colorbar(extend='both')
plt.clim(0, 350)
plt.title("Manure - groundwater quality")

plt.subplot(3, 2, 4)
plt.imshow(fercritgwha)
plt.colorbar(extend='both')
plt.clim(0, 350)
plt.title("Fertilizer - groundwater quality")

plt.subplot(3, 2, 5)
plt.imshow(mancritdeha)
plt.colorbar(extend='both')
plt.clim(0, 350)
plt.title("Manure - N deposition")

plt.subplot(3, 2, 6)
plt.imshow(fercritdeha)
plt.colorbar(extend='both')
plt.clim(0, 350)
plt.title("Fertilizer - N deposition")

plt.show()
