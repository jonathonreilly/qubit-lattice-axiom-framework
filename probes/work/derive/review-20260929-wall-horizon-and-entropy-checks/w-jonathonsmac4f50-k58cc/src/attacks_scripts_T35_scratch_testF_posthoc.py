import numpy as np
from common import *
print("(i) R1 pole masses across shared premises (3-loop, K-series at mu*)")
for kEW in (0,1):
    for a_s in (ALPHA_S_V,0.1179):
        g=gauge_at_v(kEW,a_s)
        z=crit_yt_v(g,loop=3)
        pole,m,mu=pole_from_yt_v(z,g,kappaY0=False)
        print(f" kEW={kEW} alpha_s(v)={a_s:.4f}: yt(v)={z:.4f} pole={pole:.1f} GeV")
print("(ii) protected-ratio reading, Ward y = g3^MS(M_Pl)/C on the lane's own gauge trajectory (kEW=0, alpha_s(v)=0.1033)")
g0=gauge_at_v(0)
g3pl=up(0.95,g0,loop=3)[2]
for C2 in (6.0,3.0,2.0,1.5,1.0):
    C=np.sqrt(C2); tgt=g3pl/C
    try:
        yv=ward_yt_v(tgt,g0,loop=3,lo=0.5,hi=1.08)
    except Exception as e:
        print("C^2=",C2,"failed",e); continue
    out=[]
    for kY in (0,1):
        try:
            pole,m,mu=pole_from_yt_v(yv,g0,kappaY0=(kY==0)); out.append(f"kY={kY}: {pole:.1f}")
        except Exception:
            out.append(f"kY={kY}: tree {yv*np.sqrt((8+kY)/9)*V/np.sqrt(2):.1f} (mu* outside bracket)")
    print(f" C^2={C2}: yt(M_Pl)={tgt:.4f} yt(v)={yv:.4f}; pole GeV -> "+"; ".join(out))
