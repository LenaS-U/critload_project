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


# calculate current and critical inputs per hectare
# all agricultural land
manha         = np.divide(nman, agarea)
ferha         = np.divide(nfer, agarea)
manfer        = np.add(nman, nfer)
manferha      = np.divide(manfer, agarea)
# cropland
manha_ara     = np.divide(nman_ara, area_ara)
ferha_ara     = np.divide(nfer_ara, area_ara)
manfer_ara    = np.add(nman_ara, nfer_ara)
manferha_ara  = np.divide(manfer_ara, area_ara)
# grassland
ferha_igl     = np.divide(nfer_igl, area_igl)
manha_igl     = np.divide(nman_igl, area_igl)
manha_egl     = np.divide(nman_egl, area_egl)
manfer_igl    = np.add(nman_igl, nfer_igl)
manferha_igl  = np.divide(manfer_igl, area_igl)
# cropland + intensive grassland
fer_araigl      = np.add(nfer_ara, nfer_igl)
man_araigl      = np.add(nman_ara, nman_igl)
manfer_araigl   = np.add(fer_araigl,man_araigl)
area_araigl     = np.add(area_ara, area_igl)
ferha_araigl    = np.divide(fer_araigl, area_araigl)
manha_araigl    = np.divide(man_araigl, area_araigl)
manferha_araigl = np.divide(manfer_araigl, area_araigl)

###critical inputs 
#fertilizer
fercritswha = np.divide(fercritsw, area_araigl)
fercritgwha = np.divide(fercritgw, area_araigl)
fercritdeha = np.divide(fercritde, area_araigl)
#manure
mancritswha = np.divide(mancritsw, area_araigl)
mancritgwha = np.divide(mancritgw, area_araigl)
mancritdeha = np.divide(mancritde, area_araigl)
# totals
manfercritsw = np.add(mancritsw,fercritsw)
manfercritgw = np.add(mancritgw,fercritgw)
manfercritde = np.add(mancritde,fercritde)
manfercritswha = np.divide(manfercritsw, area_araigl)
manfercritgwha = np.divide(manfercritgw, area_araigl)
manfercritdeha = np.divide(manfercritde, area_araigl)

# -> it is possible (8684 times) that mancritsw/mancritgw <> NA but area_araigl = 0. In those cases, I want to get a na.
#mancritswha[np.isinf(mancritswha)]       = np.nan
#fercritswha[np.isinf(fercritswha)]       = np.nan
mancritgwha[np.isinf(mancritgwha)]       = np.nan
fercritgwha[np.isinf(fercritgwha)]       = np.nan
#manfercritswha[np.isinf(manfercritswha)] = np.nan
manfercritgwha[np.isinf(manfercritgwha)] = np.nan

#nin         = np.add(nman,nfer)
#ninha       = np.divide(nin,agarea)

### Print actual and critical N inputs
# Areas
print("AREAS-PER-LAND-USE")
print("ag:  %i ha" %(np.nansum(agarea)))
print("ara:  %i ha" %(np.nansum(area_ara)))
print("igl:  %i ha" %(np.nansum(area_igl)))
print("egl:  %i ha" %(np.nansum(area_egl)))
print("ara-igl:  %i ha" %(np.nansum(area_araigl)))
# Actual N inputs
print("TOTAL-ACTUAL-INPUTS")
print("Act-fer-tot-all:  %i kgNyr-1" %(np.nansum(nfer)))
print("Act-fer-tot-ara:  %i kgNyr-1" %(np.nansum(nfer_ara)))
print("Act-fer-tot-igl:  %i kgNyr-1" %(np.nansum(nfer_igl)))
print("Act-fer-tot-egl:  %i kgNyr-1" % 0.0)
print("Act-man-tot-all:  %i kgNyr-1" %(np.nansum(nman)))
print("Act-man-tot-ara:  %i kgNyr-1" %(np.nansum(nman_ara)))
print("Act-man-tot-igl:  %i kgNyr-1" %(np.nansum(nman_igl)))
print("Act-man-tot-egl:  %i kgNyr-1" %(np.nansum(nman_egl)))

print("ACTUAL-INPUTS-PER-HA")
#WRONG
#print("Act-fer-ha-all:     %i kgNha-1yr-1" %(np.nanmean(ferha)))
#print("Act-fer-ha-ara:     %i kgNha-1yr-1" %(np.nanmean(ferha_ara)))
#print("Act-fer-ha-igl:     %i kgNha-1yr-1" %(np.nanmean(ferha_igl)))
#print("Act-fer-ha-egl:     %i kgNha-1yr-1" % 0.0)
#print("Act-fer-ha-araigl:  %i kgNha-1yr-1" %(np.nanmean(ferha_araigl)))
#RIGHT
print("Act-fer-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer), np.nansum(agarea[np.where(np.isnan(nfer)==False)])))
print("Act-fer-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_ara), np.nansum(area_ara[np.where(np.isnan(nfer_ara)==False)])))
print("Act-fer-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nfer_igl), np.nansum(area_igl[np.where(np.isnan(nfer_igl)==False)])))
print("Act-fer-ha-egl:     %.1f kgNha-1yr-1" % 0.0)
print("Act-fer-ha-araigl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(fer_araigl), np.nansum(area_araigl[np.where(np.isnan(fer_araigl)==False)])))
#WRONG
#print("Act-man-ha-all:     %i kgNha-1yr-1" %(np.nanmean(manha)))
#print("Act-man-ha-ara:     %i kgNha-1yr-1" %(np.nanmean(manha_ara)))
#print("Act-man-ha-igl:     %i kgNha-1yr-1" %(np.nanmean(manha_igl)))
#print("Act-man-ha-egl:     %i kgNha-1yr-1" %(np.nanmean(manha_egl)))
#print("Act-man-ha-araigl:  %i kgNha-1yr-1" %(np.nanmean(manha_araigl)))
#RIGHT
print("Act-man-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nman), np.nansum(agarea[np.where(np.isnan(nman)==False)])))
print("Act-man-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_ara), np.nansum(area_ara[np.where(np.isnan(nman_ara)==False)])))
print("Act-man-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_igl), np.nansum(area_igl[np.where(np.isnan(nman_igl)==False)])))
print("Act-man-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_egl), np.nansum(area_egl[np.where(np.isnan(nman_egl)==False)])))
print("Act-man-ha-araigl:  %.1f kgNha-1yr-1" % np.divide(np.nansum(man_araigl), np.nansum(area_araigl[np.where(np.isnan(man_araigl)==False)])))
#WRONG
#print("Act-fer-man-ha-all:     %i kgNha-1yr-1" %(np.nanmean(manferha)))
#print("Act-fer-man-ha-ara:     %i kgNha-1yr-1" %(np.nanmean(manferha_ara)))
#print("Act-fer-man-ha-igl:     %i kgNha-1yr-1" %(np.nanmean(manferha_igl)))
#print("Act-fer-man-ha-egl:     %i kgNha-1yr-1" %(np.nanmean(manha_egl)))
#print("Act-fer-man-ha-araigl:  %i kgNha-1yr-1" %(np.nanmean(manferha_araigl)))
#RIGHT
print("Act-fer-man-ha-all:     %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer), np.nansum(agarea[np.where(np.isnan(manfer)==False)])))
print("Act-fer-man-ha-ara:     %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_ara), np.nansum(area_ara[np.where(np.isnan(manfer_ara)==False)])))
print("Act-fer-man-ha-igl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_igl), np.nansum(area_igl[np.where(np.isnan(manfer_igl)==False)])))
print("Act-fer-man-ha-egl:     %.1f kgNha-1yr-1" % np.divide(np.nansum(nman_egl), np.nansum(area_egl[np.where(np.isnan(nman_egl)==False)])))
print("Act-fer-man-ha-araigl:  %.1f kgNha-1yr-1" % np.divide(np.nansum(manfer_araigl), np.nansum(area_araigl[np.where(np.isnan(manfer_araigl)==False)])))

# Critical N inputs per hectare, no cut-off value
print("CRITICAL-INPUTS-PER-HA")
#WRONG
#print("Crit-fer-sw-ha-1: %.1f" % np.nanmean(fercritswha))
#print("Crit-man-sw-ha-1: %.1f" % np.nanmean(mancritswha))
#print("Crit-fer-gw-ha-1: %.1f" % np.nanmean(fercritgwha))
#print("Crit-man-gw-ha-1: %.1f" % np.nanmean(mancritgwha))
#print("Crit-fer-de-ha-1: %.1f" % np.nanmean(fercritdeha))
#print("Crit-man-de-ha-1: %.1f" % np.nanmean(mancritdeha))
#print("Crit-nin-sw-ha-1: %.1f" % np.nanmean(manfercritswha))
#print("Crit-nin-gw-ha-1: %.1f" % np.nanmean(manfercritgwha))
#print("Crit-nin-de-ha-1: %.1f" % np.nanmean(manfercritdeha))
#RIGHT
print("Crit-fer-sw-ha-1: %.1f" % np.divide(np.nansum(fercritsw), np.nansum(area_araigl[np.where(np.isnan(fercritsw)==False)])))
print("Crit-man-sw-ha-1: %.1f" % np.divide(np.nansum(mancritsw), np.nansum(area_araigl[np.where(np.isnan(mancritsw)==False)])))
print("Crit-fer-gw-ha-1: %.1f" % np.divide(np.nansum(fercritgw), np.nansum(area_araigl[np.where(np.isnan(fercritgw)==False)])))
print("Crit-man-gw-ha-1: %.1f" % np.divide(np.nansum(mancritgw), np.nansum(area_araigl[np.where(np.isnan(mancritgw)==False)])))
print("Crit-fer-de-ha-1: %.1f" % np.divide(np.nansum(fercritde), np.nansum(area_araigl[np.where(np.isnan(fercritde)==False)])))
print("Crit-man-de-ha-1: %.1f" % np.divide(np.nansum(mancritde), np.nansum(area_araigl[np.where(np.isnan(mancritde)==False)])))
print("Crit-nin-sw-ha-1: %.1f" % np.divide(np.nansum(manfercritsw), np.nansum(area_araigl[np.where(np.isnan(manfercritsw)==False)])))
print("Crit-nin-gw-ha-1: %.1f" % np.divide(np.nansum(manfercritgw), np.nansum(area_araigl[np.where(np.isnan(manfercritgw)==False)]))) 
print("Crit-nin-de-ha-1: %.1f" % np.divide(np.nansum(manfercritde), np.nansum(area_araigl[np.where(np.isnan(manfercritde)==False)])))

# Critical N inputs with no cutoff value but negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO")
fercritsw2 = np.copy(fercritsw)
mancritsw2 = np.copy(mancritsw)
fercritgw2 = np.copy(fercritgw)
mancritgw2 = np.copy(mancritgw)
fercritde2 = np.copy(fercritde)
mancritde2 = np.copy(mancritde)
manfercritsw2 = np.copy(manfercritsw)
manfercritgw2 = np.copy(manfercritgw)
manfercritde2 = np.copy(manfercritde)

with np.errstate(invalid='ignore'):
    fercritsw2[fercritsw2<0]=0
    mancritsw2[mancritsw2<0]=0
    fercritgw2[fercritgw2<0]=0
    mancritgw2[mancritgw2<0]=0
    fercritde2[fercritde2<0]=0
    mancritde2[mancritde2<0]=0
    manfercritsw2[manfercritsw2<0]=0
    manfercritgw2[manfercritgw2<0]=0
    manfercritde2[manfercritde2<0]=0

print("Crit-fer-sw-ha-2: %.1f" % np.divide(np.nansum(fercritsw2), np.nansum(area_araigl[np.where(np.isnan(fercritsw2)==False)])))
print("Crit-man-sw-ha-2: %.1f" % np.divide(np.nansum(mancritsw2), np.nansum(area_araigl[np.where(np.isnan(mancritsw2)==False)])))
print("Crit-fer-gw-ha-2: %.1f" % np.divide(np.nansum(fercritgw2), np.nansum(area_araigl[np.where(np.isnan(fercritgw2)==False)])))
print("Crit-man-gw-ha-2: %.1f" % np.divide(np.nansum(mancritgw2), np.nansum(area_araigl[np.where(np.isnan(mancritgw2)==False)])))
print("Crit-fer-de-ha-2: %.1f" % np.divide(np.nansum(fercritde2), np.nansum(area_araigl[np.where(np.isnan(fercritde2)==False)])))
print("Crit-man-de-ha-2: %.1f" % np.divide(np.nansum(mancritde2), np.nansum(area_araigl[np.where(np.isnan(mancritde2)==False)])))
print("Crit-nin-sw-ha-2: %.1f" % np.divide(np.nansum(manfercritsw2), np.nansum(area_araigl[np.where(np.isnan(manfercritsw2)==False)])))
print("Crit-nin-gw-ha-2: %.1f" % np.divide(np.nansum(manfercritgw2), np.nansum(area_araigl[np.where(np.isnan(manfercritgw2)==False)]))) 
print("Crit-nin-de-ha-2: %.1f" % np.divide(np.nansum(manfercritde2), np.nansum(area_araigl[np.where(np.isnan(manfercritde2)==False)])))

# Critical N inputs with cutoff @ 150 kg N ha-1 yr-1 and negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-150")
manfercritswha3 = np.copy(manfercritswha)
manfercritgwha3 = np.copy(manfercritgwha)
manfercritdeha3 = np.copy(manfercritdeha)

with np.errstate(invalid='ignore'):
    manfercritswha3[manfercritswha3<0]=0
    manfercritgwha3[manfercritgwha3<0]=0
    manfercritdeha3[manfercritdeha3<0]=0
    manfercritswha3[manfercritswha3>150]=150
    manfercritgwha3[manfercritgwha3>150]=150
    manfercritdeha3[manfercritdeha3>150]=150

#Totals
manfercritsw3 = np.multiply(manfercritswha3, area_araigl)
manfercritgw3 = np.multiply(manfercritgwha3, area_araigl)
manfercritde3 = np.multiply(manfercritdeha3, area_araigl)

#WRONG
#print("Crit-nin-sw-ha-3: %.1f" % np.nanmean(manfercritswha3))
#print("Crit-nin-gw-ha-3: %.1f" % np.nanmean(manfercritgwha3))
#print("Crit-nin-de-ha-3: %.1f" % np.nanmean(manfercritdeha3))
#RIGHT
print("Crit-nin-sw-ha-3: %.1f" % np.divide(np.nansum(manfercritsw3), np.nansum(area_araigl[np.where(np.isnan(manfercritsw3)==False)])))
print("Crit-nin-gw-ha-3: %.1f" % np.divide(np.nansum(manfercritgw3), np.nansum(area_araigl[np.where(np.isnan(manfercritgw3)==False)])))
print("Crit-nin-de-ha-3: %.1f" % np.divide(np.nansum(manfercritde3), np.nansum(area_araigl[np.where(np.isnan(manfercritde3)==False)])))

with np.errstate(invalid='ignore'):
    fercritsw3 = np.multiply(manfercritsw3,     frnfe_agri)
    mancritsw3 = np.multiply(manfercritsw3, (1.-frnfe_agri))
    fercritgw3 = np.multiply(manfercritgw3,     frnfe_agri)
    mancritgw3 = np.multiply(manfercritgw3, (1.-frnfe_agri))
    fercritde3 = np.multiply(manfercritde3,     frnfe_agri)
    mancritde3 = np.multiply(manfercritde3, (1.-frnfe_agri))
print("Crit-fer-sw-ha-3: %.1f" % np.divide(np.nansum(fercritsw3), np.nansum(area_araigl[np.where(np.isnan(fercritsw3)==False)])))
print("Crit-man-sw-ha-3: %.1f" % np.divide(np.nansum(mancritsw3), np.nansum(area_araigl[np.where(np.isnan(mancritsw3)==False)])))
print("Crit-fer-gw-ha-3: %.1f" % np.divide(np.nansum(fercritgw3), np.nansum(area_araigl[np.where(np.isnan(fercritgw3)==False)])))
print("Crit-man-gw-ha-3: %.1f" % np.divide(np.nansum(mancritgw3), np.nansum(area_araigl[np.where(np.isnan(mancritgw3)==False)])))
print("Crit-fer-de-ha-3: %.1f" % np.divide(np.nansum(fercritde3), np.nansum(area_araigl[np.where(np.isnan(fercritde3)==False)])))
print("Crit-man-de-ha-3: %.1f" % np.divide(np.nansum(mancritde3), np.nansum(area_araigl[np.where(np.isnan(mancritde3)==False)])))

#
# Critical N inputs with cutoff @ max (150, actual) and negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-MAX(150,ACT)")
manfercritswha4 = np.copy(manfercritswha)
manfercritgwha4 = np.copy(manfercritgwha)
manfercritdeha4 = np.copy(manfercritdeha)

with np.errstate(invalid='ignore'):
    manfercritswha4[manfercritswha4<0]=0
    manfercritgwha4[manfercritgwha4<0]=0
    manfercritdeha4[manfercritdeha4<0]=0
    
    print("STEP1: %i" % np.nansum(manfercritswha4))
    
    for i in range(np.shape(manferha_araigl)[0]):
        for j in range(np.shape(manferha_araigl)[1]):
            if (manfercritswha4[i,j] > manferha_araigl[i,j] and manfercritswha4[i,j] > 150):
                manfercritswha4[i,j] = max(manferha_araigl[i,j],150)
            if (manfercritgwha4[i,j] > manferha_araigl[i,j] and manfercritgwha4[i,j] > 150):
                manfercritgwha4[i,j] = max(manferha_araigl[i,j],150)
            if (manfercritdeha4[i,j] > manferha_araigl[i,j] and manfercritdeha4[i,j] > 150):
                manfercritdeha4[i,j] = max(manferha_araigl[i,j],150)
    
    print("STEP2: %i" % np.nansum(manfercritswha4))
    
#Totals
manfercritsw4 = np.multiply(manfercritswha4, area_araigl)
manfercritgw4 = np.multiply(manfercritgwha4, area_araigl)
manfercritde4 = np.multiply(manfercritdeha4, area_araigl)

#WRONG
#print("Crit-nin-sw-ha-4: %.1f" % np.nanmean(manfercritswha4))
#print("Crit-nin-gw-ha-4: %.1f" % np.nanmean(manfercritgwha4))
#print("Crit-nin-de-ha-4: %.1f" % np.nanmean(manfercritdeha4))
#RIGHT
print("Crit-nin-sw-ha-4: %.1f" % np.divide(np.nansum(manfercritsw4), np.nansum(area_araigl[np.where(np.isnan(manfercritsw4)==False)])))
print("Crit-nin-gw-ha-4: %.1f" % np.divide(np.nansum(manfercritgw4), np.nansum(area_araigl[np.where(np.isnan(manfercritgw4)==False)])))
print("Crit-nin-de-ha-4: %.1f" % np.divide(np.nansum(manfercritde4), np.nansum(area_araigl[np.where(np.isnan(manfercritde4)==False)])))

with np.errstate(invalid='ignore'):
    fercritsw4 = np.multiply(manfercritsw4,     frnfe_agri)
    mancritsw4 = np.multiply(manfercritsw4, (1.-frnfe_agri))
    fercritgw4 = np.multiply(manfercritgw4,     frnfe_agri)
    mancritgw4 = np.multiply(manfercritgw4, (1.-frnfe_agri))
    fercritde4 = np.multiply(manfercritde4,     frnfe_agri)
    mancritde4 = np.multiply(manfercritde4, (1.-frnfe_agri))
print("Crit-fer-sw-ha-4: %.1f" % np.divide(np.nansum(fercritsw4), np.nansum(area_araigl[np.where(np.isnan(fercritsw4)==False)])))
print("Crit-man-sw-ha-4: %.1f" % np.divide(np.nansum(mancritsw4), np.nansum(area_araigl[np.where(np.isnan(mancritsw4)==False)])))
print("Crit-fer-gw-ha-4: %.1f" % np.divide(np.nansum(fercritgw4), np.nansum(area_araigl[np.where(np.isnan(fercritgw4)==False)])))
print("Crit-man-gw-ha-4: %.1f" % np.divide(np.nansum(mancritgw4), np.nansum(area_araigl[np.where(np.isnan(mancritgw4)==False)])))
print("Crit-fer-de-ha-4: %.1f" % np.divide(np.nansum(fercritde4), np.nansum(area_araigl[np.where(np.isnan(fercritde4)==False)])))
print("Crit-man-de-ha-4: %.1f" % np.divide(np.nansum(mancritde4), np.nansum(area_araigl[np.where(np.isnan(mancritde4)==False)])))

# Critical N inputs with cutoff @ max (150, actual) and negative values replaced by zero + INPUTS TO EXT GR
print("CRITICAL-INPUTS-PER-HA-NEG-SET-TO-ZERO-AND-CUTOFF-AT-MAX(150,ACT)-+-Nin,EGL")
manfercritsw5 = np.add(manfercritsw4, nman_egl)
manfercritgw5 = np.add(manfercritgw4, nman_egl)
manfercritde5 = np.add(manfercritde4, nman_egl)
print("Crit-nin-sw-5: %.1f" % np.divide(np.nansum(manfercritsw5), np.nansum(agarea[np.where(np.isnan(manfercritsw5)==False)])))
print("Crit-nin-gw-5: %.1f" % np.divide(np.nansum(manfercritgw5), np.nansum(agarea[np.where(np.isnan(manfercritgw5)==False)])))
print("Crit-nin-dw-5: %.1f" % np.divide(np.nansum(manfercritde5), np.nansum(agarea[np.where(np.isnan(manfercritde5)==False)])))

# MINIMUM of critical N inputs
print("CRITICAL-INPUTS-MINIMUM-EXCL-EGL")
manfercritmin4X   = np.minimum(manfercritsw4, manfercritgw4)
manfercritmin4    = np.minimum(manfercritmin4X, manfercritde4)
print("Crit-nin-min-ha-4: %.1f" % np.divide(np.nansum(manfercritmin4), np.nansum(area_araigl[np.where(np.isnan(manfercritmin4)==False)])))
with np.errstate(invalid='ignore'):
    fercritmin4 = np.multiply(manfercritmin4,     frnfe_agri)
    mancritmin4 = np.multiply(manfercritmin4, (1.-frnfe_agri))
print("Crit-fer-min-ha-4: %.1f" % np.divide(np.nansum(fercritmin4), np.nansum(area_araigl[np.where(np.isnan(fercritmin4)==False)])))
print("Crit-man-min-ha-4: %.1f" % np.divide(np.nansum(mancritmin4), np.nansum(area_araigl[np.where(np.isnan(mancritmin4)==False)])))

print("CRITICAL-INPUTS-MINIMUM-INCL-EGL")
manfercritmin5X   = np.minimum(manfercritsw5, manfercritgw5)
manfercritmin5    = np.minimum(manfercritmin5X, manfercritde5)
print("Crit-nin-min-ha-5: %.1f" % np.divide(np.nansum(manfercritmin5), np.nansum(agarea[np.where(np.isnan(manfercritmin5)==False)])))
with np.errstate(invalid='ignore'):
    fercritmin5 = np.multiply(manfercritmin5,     frnfe_agri)
    mancritmin5 = np.multiply(manfercritmin5, (1.-frnfe_agri))
print("Crit-fer-min-ha-5: %.1f" % np.divide(np.nansum(fercritmin5), np.nansum(agarea[np.where(np.isnan(fercritmin5)==False)])))
print("Crit-man-min-ha-5: %.1f" % np.divide(np.nansum(mancritmin5), np.nansum(agarea[np.where(np.isnan(mancritmin5)==False)])))


manfercritminX   = np.minimum(manfercritsw, manfercritgw)
manfercritmin    = np.minimum(manfercritminX, manfercritde)


#####
#AREAS
#####
print("CASES")
with np.errstate(invalid='ignore'):
    print("total-area: %i"% np.nansum(area_araigl))
    print("case-1-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, manfercritsw<0)) ]))
    print("case-3-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw>0,manfercritsw<=manfer_araigl))) ]))
    print("case-4-sw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritsw)==False, np.logical_and(manfercritsw>0,manfercritsw> manfer_araigl))) ]))
  
    print("case-1-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, manfercritgw<0)) ]))
    print("case-3-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw>0,manfercritgw<=manfer_araigl))) ]))
    print("case-4-gw: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritgw)==False, np.logical_and(manfercritgw>0,manfercritgw> manfer_araigl))) ]))
    
    print("case-1-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, manfercritde<0)) ]))
    print("case-3-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde>0,manfercritde<=manfer_araigl))) ]))
    print("case-4-de: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritde)==False, np.logical_and(manfercritde>0,manfercritde> manfer_araigl))) ]))
    
    print("case-1-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin)==True,  np.logical_and(np.isnan(area_araigl)==False, area_araigl>0)) )]))
    print("case-2-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin)==False, manfercritmin<0)) ]))
    print("case-3-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin)==False, np.logical_and(manfercritmin>0,manfercritmin<=manfer_araigl))) ]))
    print("case-4-mi: %i" % np.nansum(area_araigl[np.where(np.logical_and(np.isnan(manfercritmin)==False, np.logical_and(manfercritmin>0,manfercritmin> manfer_araigl))) ]))
    
    print("case-1-mi2: %i" % np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin5)==True,  np.logical_and(np.isnan(agarea)==False, agarea>0)) )]))
    print("case-2-mi2: %i" % np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin5)==False, manfercritmin5<=0)) ]))
    print("case-3-mi2: %i" % np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin5)==False, np.logical_and(manfercritmin5>0,manfercritmin5<=manfer))) ]))
    print("case-4-mi2: %i" % np.nansum(agarea[np.where(np.logical_and(np.isnan(manfercritmin5)==False, np.logical_and(manfercritmin5>0,manfercritmin5> manfer))) ]))

# Plot critical N inputs
#plt.subplot(3, 2, 1)
#plt.imshow(manfercritswha4) # critical N inputs surface water
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - surface water")
#plt.show()

#plt.imshow(manfercritgwha4) # critical N inputs groundwater
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - groundwater")
#plt.show()

#plt.imshow(manfercritdeha4) # critical N inputs deposition
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - deposition")
#plt.show()


#cmap=matplotlib.cm.get_cmap('RdYlGn')
#cmap.set_bad(color='0.8')
#cmap.set_under('0.5')
#plt.imshow(manfercritminha, cmap=cmap)#, vmin=-0.001) # critical N inputs minimum
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Critical N inputs manure + fertilizer - minimum")
#plt.show()

#plt.imshow(manferha_araigl) # actual N inputs to cropland + intensive grassland
#plt.colorbar(extend='both')
#plt.clim(0, 200) # can go up to 400, but that distorts scale too much
#plt.title("Actual N inputs manure + fertilizer")
#plt.show()

# Exceedance of critical N inputs by actual N inputs
exceedance_sw = np.subtract(manferha_araigl,manfercritswha4)
exceedance_gw = np.subtract(manferha_araigl,manfercritgwha4)
exceedance_de = np.subtract(manferha_araigl,manfercritdeha4)
exceedance_min = np.subtract(manferha_araigl, manfercritminha)

# give cells with no land default value (for different color)
with np.errstate(invalid='ignore'):
    exceedance_min[np.isnan(agarea)]= -99999
# plot map with exceedances
cmap=matplotlib.cm.get_cmap('RdYlGn_r')
cmap.set_bad(color='0.95')
cmap.set_under(color='0.5')
plt.imshow(exceedance_min, cmap=cmap, vmin=-1000) # exceedance critical N inputs minimum
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs V2")
plt.show()


#plt.imshow(exceedance_sw, cmap='RdYlGn_r') # exceedance critical N inputs surface water
#plt.colorbar(extend='both')
#plt.clim(-300, 300) # different limits are possible
#plt.title("Exceedance critical N inputs - surface water")
#plt.show()

#plt.imshow(exceedance_gw, cmap='RdYlGn_r') # exceedance critical N inputs groundwater
#plt.colorbar(extend='both')
#plt.clim(-300, 300) # different limits are possible
#plt.title("Exceedance Critical N inputs - groundwater")
#plt.show()

#plt.imshow(exceedance_de, cmap='RdYlGn_r') # exceedance critical N inputs deposition
#plt.colorbar(extend='both')
#plt.clim(-300, 300) # different limits are possible
#plt.title("Exceedance Critical N inputs - deposition")
#plt.show()

plt.imshow(exceedance_min, cmap='RdYlGn_r') # exceedance critical N inputs minimum
cbar=plt.colorbar(extend='both')
cbar.set_label(r"kg N ha-1 yr-1")
cbar.ax.tick_params(labelsize=10) 
plt.clim(-300, 300) # different limits are possible
plt.title("Exceedance Critical N inputs by actual N inputs V1")
plt.show()





# Critical N inputs with no cutoff value
#print("TOTAL-CRITICAL-INPUTS-WITHOUT-CUT-OFF-VALUE")
#print("Crit-fer-sw: %.2f"    % np.nansum(fercritsw))
#print("Crit-man-sw: %.2f"    % np.nansum(mancritsw))
#print("Crit-fer-gw: %.2f"    % np.nansum(fercritgw))
#print("Crit-man-gw: %.2f"    % np.nansum(mancritgw))
#print("Crit-fer-de: %.2f"    % np.nansum(fercritde))
#print("Crit-man-de: %.2f"    % np.nansum(mancritde))
#print("Ag-area: %.2f"        % np.nansum(agarea))

# per ha 1: total inputs divided by total area (but sum total area only for those grid cells where critical N inputs are not NA!)
#print("CRITICAL-INPUTS-PER-HA-I")
#print("Crit-fer-sw-ha-1: %f" % np.divide(np.nansum(fercritsw), np.nansum(agarea[np.where(np.isnan(fercritsw)==False)])))
#print("Crit-man-sw-ha-1: %f" % np.divide(np.nansum(mancritsw), np.nansum(agarea[np.where(np.isnan(mancritsw)==False)])))
#print("Crit-fer-gw-ha-1: %f" % np.divide(np.nansum(fercritgw), np.nansum(agarea[np.where(np.isnan(fercritgw)==False)])))
#print("Crit-man-gw-ha-1: %f" % np.divide(np.nansum(mancritgw), np.nansum(agarea[np.where(np.isnan(mancritgw)==False)])))
#print("Crit-fer-de-ha-1: %f" % np.divide(np.nansum(fercritde), np.nansum(agarea[np.where(np.isnan(fercritde)==False)])))
#print("Crit-man-de-ha-1: %f" % np.divide(np.nansum(mancritde), np.nansum(agarea[np.where(np.isnan(mancritde)==False)])))

# per ha 2: mean of the per-hectare values obtained by calculating inputs / area for each grid cell
#print("CRITICAL-INPUTS-PER-HA-II")
#print("Crit-fer-sw-ha-2: %f" % np.nanmean(fercritswha))
#print("Crit-man-sw-ha-2: %f" % np.nanmean(mancritswha))
#print("Crit-fer-gw-ha-2: %f" % np.nanmean(fercritgwha))
#print("Crit-man-gw-ha-2: %f" % np.nanmean(mancritgwha))
#print("Crit-fer-de-ha-2: %f" % np.nanmean(fercritdeha))
#print("Crit-man-de-ha-2: %f" % np.nanmean(mancritdeha))

# per ha 3: as (2), but with negative values removed
#print("CRITICAL-INPUTS-PER-HA-III")
#with np.errstate(invalid='ignore'):
#    print("Crit-fer-sw-ha-3: %f" % np.nanmean(fercritswha[np.where(fercritswha>0)]))
#    print("Crit-man-sw-ha-3: %f" % np.nanmean(mancritswha[np.where(mancritswha>0)]))
#    print("Crit-fer-gw-ha-3: %f" % np.nanmean(fercritgwha[np.where(fercritgwha>0)]))
#    print("Crit-man-gw-ha-3: %f" % np.nanmean(mancritgwha[np.where(mancritgwha>0)]))
#    print("Crit-fer-de-ha-3: %f" % np.nanmean(fercritdeha[np.where(fercritdeha>0)]))
#    print("Crit-man-de-ha-3: %f" % np.nanmean(mancritdeha[np.where(mancritdeha>0)]))

# per ha 4: as (2), but with negative values replaced by zero
#print("CRITICAL-INPUTS-PER-HA-VI")
#fercritswha2 = np.copy(fercritswha)
#mancritswha2 = np.copy(mancritswha)
#fercritgwha2 = np.copy(fercritgwha)
#mancritgwha2 = np.copy(mancritgwha)
#fercritdeha2 = np.copy(fercritdeha)
#mancritdeha2 = np.copy(mancritdeha)
#with np.errstate(invalid='ignore'):
#    fercritswha2[fercritswha2<0]=0
#    mancritswha2[mancritswha2<0]=0
#    fercritgwha2[fercritgwha2<0]=0
#    mancritgwha2[mancritgwha2<0]=0
#    fercritdeha2[fercritdeha2<0]=0
#    mancritdeha2[mancritdeha2<0]=0
#print("Crit-fer-sw-ha-4: %f" % np.nanmean(fercritswha2))
#print("Crit-man-sw-ha-4: %f" % np.nanmean(mancritswha2))
#print("Crit-fer-gw-ha-4: %f" % np.nanmean(fercritgwha2))
#print("Crit-man-gw-ha-4: %f" % np.nanmean(mancritgwha2))
#print("Crit-fer-de-ha-4: %f" % np.nanmean(fercritdeha2))
#print("Crit-man-de-ha-4: %f" % np.nanmean(mancritdeha2))

#nincritswha = np.add(fercritswha2,mancritswha2)
#nincritgwha = np.add(fercritgwha2,mancritgwha2)
#nincritdeha = np.add(fercritdeha2,mancritdeha2)
#print("Crit-nin-sw-ha-4: %f" % np.nanmean(nincritswha))
#print("Crit-nin-gw-ha-4: %f" % np.nanmean(nincritgwha))
#print("Crit-nin-de-ha-4: %f" % np.nanmean(nincritdeha))

# per ha 5: as (2), but with cutoff at 150
#print("CRITICAL-INPUTS-PER-HA-V")
#nincritswha2 = np.copy(nincritswha)
#nincritgwha2 = np.copy(nincritgwha)
#nincritdeha2 = np.copy(nincritdeha)

#with np.errstate(invalid='ignore'):
#    nincritswha2[nincritswha2>150]=150
#    nincritgwha2[nincritgwha2>150]=150
#    nincritdeha2[nincritdeha2>150]=150
#print("Crit-nin-sw-ha-5: %f" % np.nanmean(nincritswha2))
#print("Crit-nin-gw-ha-5: %f" % np.nanmean(nincritgwha2))
#print("Crit-nin-de-ha-5: %f" % np.nanmean(nincritdeha2))

#with np.errstate(invalid='ignore'):
#    fercritswha3 = np.multiply(nincritswha2,     frnfe)
#    mancritswha3 = np.multiply(nincritswha2, (1.-frnfe))
#    fercritgwha3 = np.multiply(nincritgwha2,     frnfe)
#    mancritgwha3 = np.multiply(nincritgwha2, (1.-frnfe))
#    fercritdeha3 = np.multiply(nincritdeha2,     frnfe)
#    mancritdeha3 = np.multiply(nincritdeha2, (1.-frnfe))
#print("Crit-fer-sw-ha-5: %f" % np.nanmean(fercritswha3))
#print("Crit-man-sw-ha-5: %f" % np.nanmean(mancritswha3))
#print("Crit-fer-gw-ha-5: %f" % np.nanmean(fercritgwha3))
#print("Crit-man-gw-ha-5: %f" % np.nanmean(mancritgwha3))
#print("Crit-fer-de-ha-5: %f" % np.nanmean(fercritdeha3))
#print("Crit-man-de-ha-5: %f" % np.nanmean(mancritdeha3))


#DOESN'T WORK YET
#print("CRITICAL-INPUTS-PER-HA-VI")
#nincritswha3 = np.copy(nincritswha)
#nincritgwha3 = np.copy(nincritgwha)
#nincritdeha3 = np.copy(nincritdeha)

#print(type(ninha))
#print(type(nincritswha3))
#print(np.shape(ninha))
#print(np.shape(nincritswha3))

#with np.errstate(invalid='ignore'):
#    for i in range(np.shape(ninha)[0]):
#        for j in range(np.shape(ninha)[1]):
#            if nincritswha3[i,j] > ninha[i,j]:
#                nincritswha3[i,j] = ninha[i,j]
#            if nincritgwha3[i,j] > ninha[i,j]:
#                nincritgwha3[i,j] = ninha[i,j]
#            if nincritdeha3[i,j] > ninha[i,j]:
#                nincritdeha3[i,j] = ninha[i,j]

 
#print("Crit-nin-sw-ha-6: %f" % np.nanmean(nincritswha3))
#print("Crit-nin-gw-ha-6: %f" % np.nanmean(nincritgwha3))
#print("Crit-nin-de-ha-6: %f" % np.nanmean(nincritdeha3))

#with np.errstate(invalid='ignore'):
#    fercritswha4 = np.multiply(nincritswha3,     frnfe)
#    mancritswha4 = np.multiply(nincritswha3, (1.-frnfe))
#    fercritgwha4 = np.multiply(nincritgwha3,     frnfe)
#    mancritgwha4 = np.multiply(nincritgwha3, (1.-frnfe))
#    fercritdeha4 = np.multiply(nincritdeha3,     frnfe)
#    mancritdeha4 = np.multiply(nincritdeha3, (1.-frnfe))
#print("Crit-fer-sw-ha-6: %f" % np.nanmean(fercritswha4))
#print("Crit-man-sw-ha-6: %f" % np.nanmean(mancritswha4))
#print("Crit-fer-gw-ha-6: %f" % np.nanmean(fercritgwha4))
#print("Crit-man-gw-ha-6: %f" % np.nanmean(mancritgwha4))
#print("Crit-fer-de-ha-6: %f" % np.nanmean(fercritdeha4))
#print("Crit-man-de-ha-6: %f" % np.nanmean(mancritdeha4))    

