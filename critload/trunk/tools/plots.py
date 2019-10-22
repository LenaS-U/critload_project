import os
import numpy as np
import matplotlib.pyplot as plt

# read files from output directory
os.chdir('d:\\critload_project')
os.chdir('critload')
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
os.chdir('critload')
os.chdir('trunk')
os.chdir('input')
os.chdir('1999')

agarea    = np.loadtxt("a_ag.asc"                , skiprows=6)
area_ara  = np.loadtxt("a_crop.asc"              , skiprows=6)
area_igl  = np.loadtxt("a_gr_int.asc"            , skiprows=6)
area_egl  = np.loadtxt("a_gr_ext.asc"            , skiprows=6) 
nfer      = np.loadtxt("n_fe_eff.asc"            , skiprows=6)
nman      = np.loadtxt("n_man_eff.asc"           , skiprows=6)
nfer_ara  = np.loadtxt("n_fe_eff_crop.asc"       , skiprows=6)
nman_ara  = np.loadtxt("n_man_eff_crops.asc"     , skiprows=6)
nfer_grass= np.loadtxt("n_fe_eff_grass.asc"      , skiprows=6)
nman_igl  = np.loadtxt("n_man_eff_grass_int.asc" , skiprows=6)
nman_egl  = np.loadtxt("n_man_eff_grass_ext.asc" , skiprows=6)
fgwrecag  = np.loadtxt("fgw_rec_ag.asc"          , skiprows=6)
fgwrecna  = np.loadtxt("fgw_rec_nat.asc"         , skiprows=6)
ndep      = np.loadtxt("ndep.asc"                , skiprows=6)
nh3emfert = np.loadtxt("nh3_spread_fe.asc"       , skiprows=6)
nh3emappl = np.loadtxt("nh3_spread_man.asc"      , skiprows=6)
nh3emstor = np.loadtxt("nh3_stor.asc"            , skiprows=6)
nh3emgraz = np.loadtxt("nh3_graz.asc"            , skiprows=6)

# change NA values to NaN
mancritsw[mancritsw==-9999]   =np.nan 
fercritsw[fercritsw==-9999]   =np.nan
mancritgw[mancritgw==-9999]   =np.nan
fercritgw[fercritgw==-9999]   =np.nan
mancritde[mancritde==-9999]   =np.nan
fercritde[fercritde==-9999]   =np.nan
fgwrecag[fgwrecag==-9999]     =np.nan
fgwrecna[fgwrecna==-9999]     =np.nan
agarea[agarea==-1]            =np.nan
area_ara[area_ara==-1]        =np.nan
area_igl[area_igl==-1]        =np.nan
area_egl[area_egl==-1]        =np.nan
nfer[nfer==-9999]             =np.nan
nfer_ara[nfer_ara==-9999]     =np.nan
nfer_grass[nfer_grass==-9999] =np.nan
nman[nman==-9999]             =np.nan
nman_ara[nman_ara==-9999]     =np.nan
nman_igl[nman_igl==-9999]     =np.nan
nman_egl[nman_egl==-9999]     =np.nan
frnfe[frnfe==-9999]           =np.nan
ndep[ndep==-1]                =np.nan
nh3emfert[nh3emfert==-9999]   =np.nan
nh3emappl[nh3emappl==-9999]   =np.nan
nh3emstor[nh3emstor==-9999]   =np.nan
nh3emgraz[nh3emgraz==-9999]   =np.nan

### calculate current and critical inputs per hectare
# all agricultural land
manha       = np.divide(nman, agarea)
ferha       = np.divide(nfer, agarea)
# cropland
manha_ara = np.divide(nman_ara, area_ara)
ferha_ara = np.divide(nfer_ara, area_ara)
manfer_ara = np.add(nman_ara, nfer_ara)
manferha_ara = np.divide(manfer_ara, area_ara)
# grassland
ferha_grass = np.divide(nfer_grass, area_igl)
manha_igl   = np.divide(nman_igl, area_igl)
manha_egl   = np.divide(nman_egl, area_egl)
manfer_igl = np.add(nman_igl, nfer_grass)
manferha_igl = np.divide(manfer_igl, area_igl)

mancritswha = np.divide(mancritsw, agarea)
fercritswha = np.divide(fercritsw, agarea)
mancritgwha = np.divide(mancritgw, agarea)
fercritgwha = np.divide(fercritgw, agarea)
mancritdeha = np.divide(mancritde, agarea)
fercritdeha = np.divide(fercritde, agarea)

### Plot current and critical N inputs per hectare
# Current inputs - fertilizer
#plt.subplot(1,2,1)
plt.imshow(ferha_ara)
plt.colorbar()
plt.title("N inputs from fertilizer on cropland (kg N ha-1 yr-1)")
#plt.show()
#plt.subplot(1,2,2)
plt.imshow(ferha_grass)
plt.colorbar()
plt.title("N inputs from fertilizer on grassland (kg N ha-1 yr-1)")
#plt.show()

##
# Current inputs - manure
#plt.subplot(1,3,1)
plt.imshow(manha_ara)
plt.colorbar()
plt.title("N inputs from manure on cropland (kg N ha-1 yr-1)")
#plt.show()
#plt.subplot(1,3,2)
plt.imshow(manha_igl)
plt.colorbar()
plt.title("N inputs from manure on intensive grassland (kg N ha-1 yr-1)")
#plt.show()
#plt.subplot(1,3,3)
plt.imshow(manha_egl)
plt.colorbar()
plt.title("N inputs from manure on extensive grassland (kg N ha-1 yr-1)")
#plt.show()

##
# Current inputs - all inputs 
#plt.subplot(1,3,1)
plt.imshow(manferha_ara)
plt.colorbar()
plt.title("N inputs from manure+fertilizer on cropland (kg N ha-1 yr-1)")
#plt.show()
#plt.subplot(1,3,2)
plt.imshow(manferha_igl)
plt.colorbar()
plt.title("N inputs from manure+fertilizer on intensive grassland (kg N ha-1 yr-1)")
#plt.show()
#plt.subplot(1,3,3)
plt.imshow(manha_egl)
plt.colorbar()
plt.title("N inputs from manure on extensive grassland (kg N ha-1 yr-1)")
#plt.show()
##

##
plt.subplot(1,2,1)
plt.imshow(ferha)
plt.colorbar()
plt.title(" N inputs from fertilizer (kg N ha-1 yr-1)")

plt.subplot(1,2,2)
plt.imshow(manha)
plt.colorbar()
plt.title(" N inputs from manure (kg N ha-1 yr-1)")

#plt.show()

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

#plt.show()
