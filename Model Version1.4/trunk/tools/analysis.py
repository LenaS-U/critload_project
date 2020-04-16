import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

# read files from input directory
os.chdir('d:\\critload_project')
os.chdir('critload')
os.chdir('trunk')
os.chdir('input')
os.chdir('2010')

area_ara  = np.loadtxt("a_crop.asc"        , skiprows=6)
area_igl  = np.loadtxt("a_gr_int.asc"      , skiprows=6)
nallo     = np.loadtxt("nallo.asc"         , skiprows=6)
nww       = np.loadtxt("nww.asc"           , skiprows=6)
naqua     = np.loadtxt("naqua.asc"         , skiprows=6)
ndep_sw   = np.loadtxt("ndep_sw.asc"       , skiprows=6)

# read files from output directory
os.chdir('d:\\critload_project')
os.chdir('critload')
os.chdir('trunk')
os.chdir('output')
os.chdir('2010')

ndepcrit  = np.loadtxt("ndep_crit_tot.asc"         , skiprows=6)
noxem     = np.loadtxt("nox_em.asc"                , skiprows=6)
nh3em_egl = np.loadtxt("nh3_tot_egl.asc"           , skiprows=6)
nload_crit = np.loadtxt("nload_crit_sw.asc"        , skiprows=6)
npoint = np.loadtxt("npoint_tot.asc"               , skiprows=6)
nero = np.loadtxt("nero_tot.asc"                   , skiprows=6)
nload_fixed_ag = np.loadtxt("nload_fixed_ag.asc"   , skiprows=6)
nload_fixed_nat = np.loadtxt("nload_fixed_nat.asc" , skiprows=6)

nle_ag_crit_gw = np.loadtxt("nle_ag_crit_gw.asc"   , skiprows=6)
nle_nfix_gw = np.loadtxt("nle_nfix_gw.asc"         , skiprows=6)
nle_nox_gw = np.loadtxt("nle_nox_gw.asc"           , skiprows=6)
nle_nh3egl_gw = np.loadtxt("nle_nh3egl_gw.asc"     , skiprows=6)


# change NA values to NaN
area_ara[area_ara==-1]                  =np.nan
area_igl[area_igl==-1]                  =np.nan
nallo[nallo==-9999]                     =np.nan 
nww[nww==-9999]                         =np.nan 
naqua[naqua==-9999]                     =np.nan 
ndep_sw[ndep_sw==-9999]                 =np.nan 
ndepcrit[ndepcrit==-9999]               =np.nan 
noxem[noxem==-1]                        =np.nan 
nh3em_egl[nh3em_egl==-9999]             =np.nan 
nload_crit[nload_crit==-9999]           =np.nan 
npoint[npoint==-9999]                   =np.nan 
nero[nero==-9999]                       =np.nan 
nload_fixed_ag[nload_fixed_ag==-9999]   =np.nan 
nload_fixed_nat[nload_fixed_nat==-9999] =np.nan 

nle_ag_crit_gw[nle_ag_crit_gw==-9999] =np.nan 
nle_nfix_gw[nle_nfix_gw==-9999] =np.nan 
nle_nox_gw[nle_nox_gw==-1] =np.nan 
nle_nh3egl_gw[nle_nh3egl_gw==-9999] =np.nan 

# calculate agricultural area
area_araigl   = np.add(area_ara, area_igl)

# calculate percentages
noxem_per = np.divide(noxem,ndepcrit)
nh3em_egl_per = np.divide(nh3em_egl,ndepcrit)
noxem_nh3em_egl = np.add(noxem,nh3em_egl)
noxem_nh3em_egl_per = np.divide(noxem_nh3em_egl,ndepcrit)

# calcualte % area for different cases
print("CASES deposition")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(area_araigl))
    print("case-1: %i" % np.nansum(area_araigl[np.where(noxem>ndepcrit)]))
    print("case-2: %i" % np.nansum(area_araigl[np.where(nh3em_egl>ndepcrit)]))
    print("case-3: %i" % np.nansum(area_araigl[np.where(noxem_nh3em_egl>ndepcrit)]))
    
# make plots
#plt.imshow(noxem_per, cmap='RdYlGn_r') # NOx em as share of critical em
#plt.colorbar(extend='both')
#plt.clim(0, 2) # different limits are possible
#plt.title("Share of NOx emission in total critical N emission")
#plt.show()

#plt.imshow(nh3em_egl_per, cmap='RdYlGn_r') # NH3 EGL em as share of critical em
#plt.colorbar(extend='both')
#plt.clim(0, 2) # different limits are possible
#plt.title("Share of NH3 emissions from ext. grassland in total critical N emission")
#plt.show()

#plt.imshow(noxem_nh3em_egl_per, cmap='RdYlGn_r') # NH3 EGL + NOx em as share of critical em
#plt.colorbar(extend='both')
#plt.clim(0, 2) # different limits are possible
#plt.title("Share of NOx emissions + NH3 emissions from ext. grassland in total critical N emission")
#plt.show()

# calculate percentages
npoint_per  = np.divide(npoint,nload_crit)
nero_per    = np.divide(nero,nload_crit)
nload_fixed_ag_per    = np.divide(nload_fixed_ag,nload_crit)    
nload_fixed_nat_per    = np.divide(nload_fixed_nat,nload_crit)

nero_npoint = np.add(nero,npoint)
nload_fixed = np.add(nload_fixed_ag,nload_fixed_nat)
nload_tot = np.add(nero_npoint,nload_fixed)

# calcualte % area for different cases
print("CASES")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(area_araigl))
    print("case-1: %i" % np.nansum(area_araigl[np.where(npoint>nload_crit)]))
    print("case-1a: %i" % np.nansum(area_araigl[np.where(nww>nload_crit)]))
    print("case-1b: %i" % np.nansum(area_araigl[np.where(naqua>nload_crit)]))
    print("case-1c: %i" % np.nansum(area_araigl[np.where(ndep_sw>nload_crit)]))
    print("case-1d: %i" % np.nansum(area_araigl[np.where(nallo>nload_crit)]))
    print("case-2: %i" % np.nansum(area_araigl[np.where(nero>nload_crit)]))
    print("case-3: %i" % np.nansum(area_araigl[np.where(nload_fixed_ag>nload_crit)]))
    print("case-4: %i" % np.nansum(area_araigl[np.where(nload_fixed_nat>nload_crit)]))
    print("case-5: %i" % np.nansum(area_araigl[np.where(nload_fixed>nload_crit)]))
    print("case-6: %i" % np.nansum(area_araigl[np.where(nero_npoint>nload_crit)]))
    print("case-7: %i" % np.nansum(area_araigl[np.where(nload_tot>nload_crit)]))
    
# make plots
#plt.imshow(npoint_per, cmap='RdYlGn_r') # n_point em as share of critical N lpad
#plt.colorbar(extend='both')
#plt.clim(0, 10) # different limits are possible
#plt.title("Share of N load from point sources in total critical N load")
#plt.show()

#plt.imshow(npoint_per, cmap='OrRd') # n_point em as share of critical N lpad
#plt.colorbar(extend='both')
#plt.clim(1, 10) # different limits are possible
#plt.title("Share of N load from point sources in total critical N load")
#plt.show()

#cmap=matplotlib.cm.get_cmap('cool')
#cmap.set_under('0.5')
#plt.imshow(npoint_per, cmap=cmap, vmin=1.0)
#plt.colorbar(extend='min')
#plt.clim(1, 10)
#plt.title("Share of N load from point sources in total critical N load")
#plt.show()

#plt.imshow(nero_per, cmap=cmap, vmin=1.0)
#plt.colorbar(extend='min')
#plt.clim(1, 10)
#plt.title("Share of N load from erosion in total critical N load")
#plt.show()

#plt.imshow(nload_fixed_ag_per, cmap=cmap, vmin=1.0)
#plt.colorbar(extend='min')
#plt.clim(1, 5)
#plt.title("Share of fixed N load from agriculture in total critical N load")
#plt.show()

#plt.imshow(nload_fixed_nat_per, cmap=cmap, vmin=1.0)
#plt.colorbar(extend='min')
#plt.clim(1, 2.5)
#plt.title("Share of fixed N load from nature in total critical N load")
#plt.show()

#plt.imshow(nero_per, cmap='RdYlGn_r') # n_ero em as share of critical N lpad
#plt.colorbar(extend='both')
#plt.clim(0, 10) # different limits are possible
#plt.title("Share of N load from erosion in total critical N load")
#plt.show()

#plt.imshow(nload_fixed_ag_per, cmap='RdYlGn_r') # nload_fixed_ag em as share of critical N lpad
#plt.colorbar(extend='both')
#plt.clim(0, 5) # different limits are possible
#plt.title("Share of fixed N load from agriculture in total critical N load")
#plt.show()

#plt.imshow(nload_fixed_nat_per, cmap='RdYlGn_r') # nload_fixed_nat em as share of critical N lpad
#plt.colorbar(extend='both')
#plt.clim(0, 2) # different limits are possible
#plt.title("Share of fixed N load from nature in total critical N load")
#plt.show()

###### GROUNDWATER ##########
nle_fix_all = np.add(nle_nfix_gw,nle_nox_gw)
nle_fix_all = np.add(nle_fix_all,nle_nh3egl_gw)
# calcualte % area for different cases
print("CASES GROUNDWATER")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(area_araigl))
    print("case-1: %i" % np.nansum(area_araigl[np.where(nle_nfix_gw   >nle_ag_crit_gw)]))
    print("case-2: %i" % np.nansum(area_araigl[np.where(nle_nox_gw    >nle_ag_crit_gw)]))
    print("case-3: %i" % np.nansum(area_araigl[np.where(nle_nh3egl_gw >nle_ag_crit_gw)]))
    print("case-4: %i" % np.nansum(area_araigl[np.where(nle_fix_all   >nle_ag_crit_gw)]))
    
# calculate percentages
nle_nfix_per        = np.divide(nle_nfix_gw,nle_ag_crit_gw)
nle_nox_per         = np.divide(nle_nox_gw,nle_ag_crit_gw)
nle_nh3egl_per      = np.divide(nle_nh3egl_gw,nle_ag_crit_gw)    
nle_fix_all_per = np.divide(nle_fix_all,nle_ag_crit_gw)

# make plots
cmap=matplotlib.cm.get_cmap('cool')
cmap.set_under('0.5')
plt.imshow(nle_nfix_per, cmap=cmap, vmin=1.0)
plt.colorbar(extend='min')
plt.clim(1, 10)
plt.title("Share of N leaching due to N fixation in total critical leaching")
plt.show()

plt.imshow(nle_nox_per, cmap=cmap, vmin=1.0)
plt.colorbar(extend='min')
plt.clim(1, 10)
plt.title("Share of N leaching due to NOx deposition in total critical leaching")
plt.show()

plt.imshow(nle_nh3egl_per, cmap=cmap, vmin=1.0)
plt.colorbar(extend='min')
plt.clim(1, 10)
plt.title("Share of N leaching due to NH3 deposition from ext grassland in total critical leaching")
plt.show()