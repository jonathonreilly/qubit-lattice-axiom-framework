import numpy as np
from common import *
g0=gauge_at_v(0)
print("lane inputs at v: g1,g2,g3 =",g0, " V=",V)
res={}
for L in (1,2,3):
    z=crit_yt_v(g0,loop=L)
    b,ypl=beta_lam_at_pl(z,g0,loop=L)
    res[L]=z
    print(f"loop {L}: critical yt(v)={z:.5f}  yt(M_Pl)={ypl[3]:.5f}  g(M_Pl)=({ypl[0]:.4f},{ypl[1]:.4f},{ypl[2]:.4f}) beta_lam={b:.2e}")
ward=0.9176
print("Ward-chain yt(v) (kappa_Y=0)=0.9176 ; diff loop3: %.3f%%, loop2: %.3f%%"%((res[3]/ward-1)*100,(res[2]/ward-1)*100))
print("2-loop vs 3-loop crit: %.3f%%"%((res[2]/res[3]-1)*100))
# the lane's Ward chain backward scan: BC yt(M_Pl)=g_lat/sqrt6
for lab,bc in (("bare 1/sqrt6",1/np.sqrt(6)),("tadpole-lifted g_LM/sqrt6",np.sqrt(4*PI*ALPHA_LM)/np.sqrt(6))):
    for L in (2,3):
        y=ward_yt_v(bc,g0,loop=L)
        print(f"Ward BC {lab} = {bc:.4f}; loop {L}: yt(v)={y:.5f} ; with sqrt(8/9): {y*np.sqrt(8/9):.5f}")
# MPP-implied yt(M_Pl) formula 1-loop with the lattice bare EW couplings (g2^2=1/4, gY^2=1/5)
g2sq,gYsq=0.25,0.2
y4=(2*g2sq**2+(g2sq+gYsq)**2)/16
print("1-loop critical yt(M_Pl) with bare lattice EW couplings = %.5f  (=(131/6400)^(1/4)=%.5f); Ward core 1/sqrt6=%.5f; ratio %.4f"%(y4**0.25,(131/6400)**0.25,1/np.sqrt(6),y4**0.25*np.sqrt(6)))
# pole masses
for lab,ytv,k0 in (("R1 crit (no kappa_Y)",res[3],False),("Ward tadpole-lifted, kappa_Y=0",ward_yt_v(np.sqrt(4*PI*ALPHA_LM)/np.sqrt(6),g0),True),("Ward tadpole-lifted, kappa_Y=1",ward_yt_v(np.sqrt(4*PI*ALPHA_LM)/np.sqrt(6),g0),False)):
    pole,m,mu=pole_from_yt_v(ytv,g0,kappaY0=k0)
    print(f"{lab}: yt(v)={ytv:.5f}{' x sqrt(8/9)' if k0 else ''} -> mbar(m)={m:.2f} at mu*={mu:.1f} -> pole(K=1.0619)={pole:.2f} GeV")
