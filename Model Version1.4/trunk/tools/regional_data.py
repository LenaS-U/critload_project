import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
    
# read files from *OUTPUT* directory
os.chdir('d:\\critload_project')
os.chdir('critload')
os.chdir('trunk')
os.chdir('output')
os.chdir('2010')

mancritsw = np.loadtxt("nman_crit_sw.asc"  , skiprows=6)
fercritsw = np.loadtxt("nfert_crit_sw.asc" , skiprows=6)
mancritgw = np.loadtxt("nman_crit_gw.asc"  , skiprows=6)
fercritgw = np.loadtxt("nfert_crit_gw.asc" , skiprows=6)
mancritde = np.loadtxt("nman_crit_dep.asc" , skiprows=6)
fercritde = np.loadtxt("nfert_crit_dep.asc", skiprows=6)
frnfe_agri= np.loadtxt("frnfe_agri.asc"    , skiprows=6)

# read files from *INPUT* directory
os.chdir('d:\\critload_project')
os.chdir('critload')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

agarea    = np.loadtxt("a_ag.asc"          , skiprows=6)
area_ara  = np.loadtxt("a_crop.asc"        , skiprows=6)
area_igl  = np.loadtxt("a_gr_int.asc"      , skiprows=6)
area_egl  = np.loadtxt("a_gr_ext.asc"      , skiprows=6) 
nfer      = np.loadtxt("n_fe_eff.asc"      , skiprows=6)
nfer_ara  = np.loadtxt("n_fe_eff_crop.asc" , skiprows=6)
nfer_igl  = np.loadtxt("n_fe_eff_grass.asc"      , skiprows=6)
nman      = np.loadtxt("n_man_eff.asc"           , skiprows=6)
nman_ara  = np.loadtxt("n_man_eff_crops.asc"     , skiprows=6)
nman_igl  = np.loadtxt("n_man_eff_grass_int.asc" , skiprows=6)
nman_egl  = np.loadtxt("n_man_eff_grass_ext.asc" , skiprows=6)
fgwrecag  = np.loadtxt("fgw_rec_ag.asc"    , skiprows=6)
fgwrecna  = np.loadtxt("fgw_rec_nat.asc"   , skiprows=6)
ndep      = np.loadtxt("ndep.asc"          , skiprows=6)
nh3emfert = np.loadtxt("nh3_spread_fe.asc" , skiprows=6)
nh3emappl = np.loadtxt("nh3_spread_man.asc", skiprows=6)
nh3emstor = np.loadtxt("nh3_stor.asc"      , skiprows=6)
nh3emgraz = np.loadtxt("nh3_graz.asc"      , skiprows=6)
nup_ara  = np.loadtxt("n_up_crops.asc"     , skiprows=6)
nup_igl  = np.loadtxt("n_up_grass_int.asc" , skiprows=6)
nup_egl  = np.loadtxt("n_up_grass_ext.asc" , skiprows=6)
regions   = np.loadtxt("image_region28.asc", skiprows=6)

# change NA values to NaN
mancritsw[mancritsw==-9999]   =np.nan 
fercritsw[fercritsw==-9999]   =np.nan
mancritgw[mancritgw==-9999]   =np.nan
fercritgw[fercritgw==-9999]   =np.nan
mancritde[mancritde ==-9999]   =np.nan
fercritde[fercritde==-9999]   =np.nan
fgwrecag[fgwrecag==-9999]     =np.nan
fgwrecna[fgwrecna==-9999]     =np.nan
agarea[agarea==-1]            =np.nan
area_ara[area_ara==-1]        =np.nan
area_igl[area_igl==-1]        =np.nan
area_egl[area_egl==-1]        =np.nan
nfer[nfer==-9999]             =np.nan
nfer_ara[nfer_ara==-9999]     =np.nan
nfer_igl[nfer_igl==-9999]     =np.nan
nman[nman==-9999]             =np.nan
nman_ara[nman_ara==-9999]     =np.nan
nman_igl[nman_igl==-9999]     =np.nan
nman_egl[nman_egl==-9999]     =np.nan
frnfe_agri[frnfe_agri==-9999] =np.nan
ndep[ndep==-1]                =np.nan
nh3emfert[nh3emfert==-9999]   =np.nan
nh3emappl[nh3emappl==-9999]   =np.nan
nh3emstor[nh3emstor==-9999]   =np.nan
nh3emgraz[nh3emgraz==-9999]   =np.nan
nup_ara[nup_ara==-9999]       =np.nan
nup_igl[nup_igl==-9999]       =np.nan
nup_egl[nup_egl==-9999]       =np.nan
regions[regions==-9999]       =np.nan

# calculate sum of variable per regions
x = np.copy(nup_igl)

print("nup_igl")

print("region-01:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==1)]))
print("region-02:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==2)]))
print("region-03:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==3)]))
print("region-04:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==4)]))
print("region-05:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==5)]))
print("region-06:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==6)]))
print("region-07:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==7)]))
print("region-08:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==8)]))
print("region-09:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==9)]))
print("region-10:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==10)]))
print("region-11:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==11)]))
print("region-12:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==12)]))
print("region-13:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==13)]))
print("region-14:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==14)]))
print("region-15:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==15)]))
print("region-16:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==16)]))
print("region-17:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==17)]))
print("region-18:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==18)]))
print("region-19:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==19)]))
print("region-20:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==20)]))
print("region-21:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==21)]))
print("region-22:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==22)]))
print("region-23:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==23)]))
print("region-24:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==24)]))
print("region-25:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==25)]))
print("region-26:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==26)]))
print("region-27:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==27)]))
print("region-28:     %.1f kgNyr-1" % np.nansum(x[np.where(regions==28)]))

# calculate mean value per hectare for variable
z = np.copy(nup_igl)
y = np.copy(area_igl)

print("nup_igl per ha")
print("global:        %.1f kgNyr-1" % np.divide(np.nansum(z), np.nansum(y[np.where(np.isnan(z)==False)])))
print("region-01:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==1)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==1))])))
print("region-02:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==2)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==2))])))
print("region-01:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==3)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==3))])))
print("region-04:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==4)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==4))])))
print("region-05:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==5)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==5))])))
print("region-06:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==6)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==6))])))
print("region-07:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==7)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==7))])))
print("region-08:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==8)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==8))])))
print("region-09:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==9)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==9))])))
print("region-10:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==10)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==10))])))
print("region-11:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==11)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==11))])))
print("region-12:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==12)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==12))])))
print("region-13:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==13)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==13))])))
print("region-14:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==14)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==14))])))
print("region-15:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==15)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==15))])))
print("region-16:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==16)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==16))])))
print("region-17:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==17)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==17))])))
print("region-18:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==18)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==18))])))
print("region-19:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==19)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==19))])))
print("region-20:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==20)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==20))])))
print("region-21:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==21)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==21))])))
print("region-22:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==22)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==22))])))
print("region-23:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==23)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==23))])))
print("region-24:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==24)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==24))])))
print("region-25:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==25)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==25))])))
print("region-26:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==26)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==26))])))
#print("region-27:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==1)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==27))])))
#print("region-28:     %.1f kgNyr-1" % np.divide(np.nansum(z[np.where(regions==1)]), np.nansum(y[np.where(np.logical_and(np.isnan(z)==False, regions==28))])))

