import numpy as np
from common import *
g0=gauge_at_v(0)
zc=crit_yt_v(g0,loop=3)
ypl_c=up(zc,g0,loop=3)
print(f"R1: yt(v)={zc:.5f}, yt(M_Pl)={ypl_c[3]:.5f}")
lift=np.sqrt(4*PI*ALPHA_LM)/np.sqrt(6); bare=1/np.sqrt(6)
for kY,lab in ((0,"kappa_Y=0"),(1,"kappa_Y=1")):
    s=np.sqrt((8+kY)/9)
    # need run-value yt(v)_run = zc/s
    ypl_needed=None
    f=lambda yv: yv*s-zc
    yv_run=zc/s
    ypl=up(yv_run,g0,loop=3)[3]
    print(f"{lab}: run-value yt(v)={yv_run:.5f} <-> yt(M_Pl)={ypl:.5f}; implied 1+Delta_R vs lifted {lift:.4f}: {ypl/lift:.4f}; vs bare {bare:.4f}: {ypl/bare:.4f}")
# Scenario A on the lane's own trajectory: Ward partner = RG-consistent g3(M_Pl) from alpha_s(v)=0.1033
ypl0=up(0.95,g0,loop=3)
g3pl=ypl0[2]; print("g3(M_Pl) from alpha_s(v)=0.1033 run up:",g3pl, " g_lat=",np.sqrt(4*PI*ALPHA_LM), " ratio g_lat/g3(M_Pl)=",np.sqrt(4*PI*ALPHA_LM)/g3pl)
tgt=g3pl/np.sqrt(6)
for L in (3,):
    yv=ward_yt_v(tgt,g0,loop=L,lo=0.55,hi=0.95)
    for kY in (0,1):
        yphys=yv*np.sqrt((8+kY)/9)
        tree=yphys*V/np.sqrt(2)
        print(f"Scenario A (Ward partner g3^MS(M_Pl)={g3pl:.4f}): yt(M_Pl)={tgt:.4f} -> yt(v)={yv:.4f}; kappa_Y={kY}: tree m=yt(v)*v/sqrt2={tree:.1f} GeV (x~1.08 = {1.08*tree:.0f} GeV pole-scale, order of magnitude)")
# one-loop Landau-pole / confinement scale implied by g_lat at the Planck lattice (pure statement of T30)
b0=7/(16*PI**2)
a=np.sqrt(4*PI*ALPHA_LM)
for gg,lab in ((a,"g_LM=1.068"),(1.0,"g_bare=1")):
    Lam=MPL*np.exp(-1/(2*b0*gg**2))
    print(f"one-loop Lambda for {lab}, b0=7/(16pi^2): {Lam:.3e} GeV")
