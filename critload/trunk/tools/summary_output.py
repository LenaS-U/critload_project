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
mancritde[mancritde==-9999]    =np.nan
fercritde[fercritde==-9999]    =np.nan
fgwrecag[fgwrecag==-9999]  =np.nan
fgwrecna[fgwrecna==-9999]  =np.nan
agarea[agarea==-1]         =np.nan
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
nin         = np.add(nman,nfer)
ninha       = np.divide(nin,agarea)

### Print actual and critical N inputs
# Actual N inputs
print("ACTUAL INPUTS")
print("The total N fertilizer gift for the reference year is %i kg N yr-1" %(np.nansum(nfer)))
print("The average N fertilizer gift for the reference year is %i kg N ha-1 yr-1" %(np.nansum(nfer)/np.nansum(agarea)))
print("The total N manure gift for the reference year is %i kg N yr-1" % (np.nansum(nman)))
print("The average N manure gift for the reference year is %i kg N ha-1 yr-1" %(np.nansum(nman)/np.nansum(agarea)))

# Critical N inputs with no cutoff value
print("TOTAL-CRITICAL-INPUTS-WITHOUT-CUT-OFF-VALUE")
print("Crit-fer-sw: %.2f"    % np.nansum(fercritsw))
print("Crit-man-sw: %.2f"    % np.nansum(mancritsw))
print("Crit-fer-gw: %.2f"    % np.nansum(fercritgw))
print("Crit-man-gw: %.2f"    % np.nansum(mancritgw))
print("Crit-fer-de: %.2f"    % np.nansum(fercritde))
print("Crit-man-de: %.2f"    % np.nansum(mancritde))
print("Ag-area: %.2f"        % np.nansum(agarea))

# per ha 1: total inputs divided by total area (but sum total area only for those grid cells where critical N inputs are not NA!)
print("CRITICAL-INPUTS-PER-HA-I")
print("Crit-fer-sw-ha-1: %f" % np.divide(np.nansum(fercritsw), np.nansum(agarea[np.where(np.isnan(fercritsw)==False)])))
print("Crit-man-sw-ha-1: %f" % np.divide(np.nansum(mancritsw), np.nansum(agarea[np.where(np.isnan(mancritsw)==False)])))
print("Crit-fer-gw-ha-1: %f" % np.divide(np.nansum(fercritgw), np.nansum(agarea[np.where(np.isnan(fercritgw)==False)])))
print("Crit-man-gw-ha-1: %f" % np.divide(np.nansum(mancritgw), np.nansum(agarea[np.where(np.isnan(mancritgw)==False)])))
print("Crit-fer-de-ha-1: %f" % np.divide(np.nansum(fercritde), np.nansum(agarea[np.where(np.isnan(fercritde)==False)])))
print("Crit-man-de-ha-1: %f" % np.divide(np.nansum(mancritde), np.nansum(agarea[np.where(np.isnan(mancritde)==False)])))

# per ha 2: mean of the per-hectare values obtained by calculating inputs / area for each grid cell
print("CRITICAL-INPUTS-PER-HA-II")
print("Crit-fer-sw-ha-2: %f" % np.nanmean(fercritswha))
print("Crit-man-sw-ha-2: %f" % np.nanmean(mancritswha))
print("Crit-fer-gw-ha-2: %f" % np.nanmean(fercritgwha))
print("Crit-man-gw-ha-2: %f" % np.nanmean(mancritgwha))
print("Crit-fer-de-ha-2: %f" % np.nanmean(fercritdeha))
print("Crit-man-de-ha-2: %f" % np.nanmean(mancritdeha))

# per ha 3: as (2), but with negative values removed
print("CRITICAL-INPUTS-PER-HA-III")
with np.errstate(invalid='ignore'):
    print("Crit-fer-sw-ha-3: %f" % np.nanmean(fercritswha[np.where(fercritswha>0)]))
    print("Crit-man-sw-ha-3: %f" % np.nanmean(mancritswha[np.where(mancritswha>0)]))
    print("Crit-fer-gw-ha-3: %f" % np.nanmean(fercritgwha[np.where(fercritgwha>0)]))
    print("Crit-man-gw-ha-3: %f" % np.nanmean(mancritgwha[np.where(mancritgwha>0)]))
    print("Crit-fer-de-ha-3: %f" % np.nanmean(fercritdeha[np.where(fercritdeha>0)]))
    print("Crit-man-de-ha-3: %f" % np.nanmean(mancritdeha[np.where(mancritdeha>0)]))

# per ha 4: as (2), but with negative values replaced by zero
print("CRITICAL-INPUTS-PER-HA-VI")
fercritswha2 = np.copy(fercritswha)
mancritswha2 = np.copy(mancritswha)
fercritgwha2 = np.copy(fercritgwha)
mancritgwha2 = np.copy(mancritgwha)
fercritdeha2 = np.copy(fercritdeha)
mancritdeha2 = np.copy(mancritdeha)
with np.errstate(invalid='ignore'):
    fercritswha2[fercritswha2<0]=0
    mancritswha2[mancritswha2<0]=0
    fercritgwha2[fercritgwha2<0]=0
    mancritgwha2[mancritgwha2<0]=0
    fercritdeha2[fercritdeha2<0]=0
    mancritdeha2[mancritdeha2<0]=0
print("Crit-fer-sw-ha-4: %f" % np.nanmean(fercritswha2))
print("Crit-man-sw-ha-4: %f" % np.nanmean(mancritswha2))
print("Crit-fer-gw-ha-4: %f" % np.nanmean(fercritgwha2))
print("Crit-man-gw-ha-4: %f" % np.nanmean(mancritgwha2))
print("Crit-fer-de-ha-4: %f" % np.nanmean(fercritdeha2))
print("Crit-man-de-ha-4: %f" % np.nanmean(mancritdeha2))

nincritswha = np.add(fercritswha2,mancritswha2)
nincritgwha = np.add(fercritgwha2,mancritgwha2)
nincritdeha = np.add(fercritdeha2,mancritdeha2)
print("Crit-nin-sw-ha-4: %f" % np.nanmean(nincritswha))
print("Crit-nin-gw-ha-4: %f" % np.nanmean(nincritgwha))
print("Crit-nin-de-ha-4: %f" % np.nanmean(nincritdeha))

# per ha 5: as (2), but with cutoff at 150
print("CRITICAL-INPUTS-PER-HA-V")
nincritswha2 = np.copy(nincritswha)
nincritgwha2 = np.copy(nincritgwha)
nincritdeha2 = np.copy(nincritdeha)

with np.errstate(invalid='ignore'):
    nincritswha2[nincritswha2>150]=150
    nincritgwha2[nincritgwha2>150]=150
    nincritdeha2[nincritdeha2>150]=150
print("Crit-nin-sw-ha-5: %f" % np.nanmean(nincritswha2))
print("Crit-nin-gw-ha-5: %f" % np.nanmean(nincritgwha2))
print("Crit-nin-de-ha-5: %f" % np.nanmean(nincritdeha2))

with np.errstate(invalid='ignore'):
    fercritswha3 = np.multiply(nincritswha2,     frnfe)
    mancritswha3 = np.multiply(nincritswha2, (1.-frnfe))
    fercritgwha3 = np.multiply(nincritgwha2,     frnfe)
    mancritgwha3 = np.multiply(nincritgwha2, (1.-frnfe))
    fercritdeha3 = np.multiply(nincritdeha2,     frnfe)
    mancritdeha3 = np.multiply(nincritdeha2, (1.-frnfe))
print("Crit-fer-sw-ha-5: %f" % np.nanmean(fercritswha3))
print("Crit-man-sw-ha-5: %f" % np.nanmean(mancritswha3))
print("Crit-fer-gw-ha-5: %f" % np.nanmean(fercritgwha3))
print("Crit-man-gw-ha-5: %f" % np.nanmean(mancritgwha3))
print("Crit-fer-de-ha-5: %f" % np.nanmean(fercritdeha3))
print("Crit-man-de-ha-5: %f" % np.nanmean(mancritdeha3))


#DOESN'T WORK YET
print("CRITICAL-INPUTS-PER-HA-VI")
nincritswha3 = np.copy(nincritswha)
nincritgwha3 = np.copy(nincritgwha)
nincritdeha3 = np.copy(nincritdeha)

#print(type(ninha))
#print(type(nincritswha3))
#print(np.shape(ninha))
#print(np.shape(nincritswha3))

with np.errstate(invalid='ignore'):
    for i in range(np.shape(ninha)[0]):
        for j in range(np.shape(ninha)[1]):
            if nincritswha3[i,j] > ninha[i,j]:
                nincritswha3[i,j] = ninha[i,j]
            if nincritgwha3[i,j] > ninha[i,j]:
                nincritgwha3[i,j] = ninha[i,j]
            if nincritdeha3[i,j] > ninha[i,j]:
                nincritdeha3[i,j] = ninha[i,j]

 
print("Crit-nin-sw-ha-6: %f" % np.nanmean(nincritswha3))
print("Crit-nin-gw-ha-6: %f" % np.nanmean(nincritgwha3))
print("Crit-nin-de-ha-6: %f" % np.nanmean(nincritdeha3))

with np.errstate(invalid='ignore'):
    fercritswha4 = np.multiply(nincritswha3,     frnfe)
    mancritswha4 = np.multiply(nincritswha3, (1.-frnfe))
    fercritgwha4 = np.multiply(nincritgwha3,     frnfe)
    mancritgwha4 = np.multiply(nincritgwha3, (1.-frnfe))
    fercritdeha4 = np.multiply(nincritdeha3,     frnfe)
    mancritdeha4 = np.multiply(nincritdeha3, (1.-frnfe))
print("Crit-fer-sw-ha-6: %f" % np.nanmean(fercritswha4))
print("Crit-man-sw-ha-6: %f" % np.nanmean(mancritswha4))
print("Crit-fer-gw-ha-6: %f" % np.nanmean(fercritgwha4))
print("Crit-man-gw-ha-6: %f" % np.nanmean(mancritgwha4))
print("Crit-fer-de-ha-6: %f" % np.nanmean(fercritdeha4))
print("Crit-man-de-ha-6: %f" % np.nanmean(mancritdeha4))    

