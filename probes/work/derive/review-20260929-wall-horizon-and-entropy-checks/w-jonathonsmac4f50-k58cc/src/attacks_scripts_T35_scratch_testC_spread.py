import numpy as np, itertools, json
from common import *

def up_safe(yt_v,g,loop):
    try: return up(yt_v,g,loop=loop,lam_v=0.13)
    except Exception: return up(yt_v,g,loop=loop,lam_v=0.0)

def ward_scan(target,g,loop,lo=0.55,hi=1.25):
    f=lambda yt: up_safe(yt,g,loop)[3]-target
    return brentq(f,lo,hi,xtol=1e-9)

def crit_scan(g,loop,lam_pl,lo=0.80,hi=1.05):
    def f(yt):
        ypl=up_safe(yt,g,loop)
        y=[ypl[0],ypl[1],ypl[2],ypl[3],lam_pl]
        return H.beta_full(t_pl,y,n_f=6,loop_order=loop)[4]
    return brentq(f,lo,hi,xtol=1e-9)

shared=[]
for kEW in (0,1):
    for a_s in (ALPHA_LM, ALPHA_S_V, 0.1179):
        shared.append((kEW,a_s))

rows=[]
ward_vals=[]; crit_vals=[]
for kEW,a_s in shared:
    g=gauge_at_v(kEW,a_s)
    # R1 corners
    for loop in (2,3):
        for lam_pl in (-1e-3,0.0,1e-3):
            try:
                z=crit_scan(g,loop,lam_pl)
            except Exception as e:
                z=np.nan
            crit_vals.append(z)
            rows.append(("R1",kEW,round(a_s,4),f"loop{loop}",f"lam_pl={lam_pl:+.0e}",z))
    # Ward corners
    for bc in (1/np.sqrt(6), np.sqrt(4*PI*ALPHA_LM)/np.sqrt(6)):
        for dR in (-0.5,0.0,0.5):
            for kY in (0,1):
                loop=3
                try:
                    z=ward_scan(bc*(1+dR),g,loop)
                except Exception as e:
                    z=np.nan
                zphys=z*np.sqrt((8+kY)/9) if np.isfinite(z) else np.nan
                ward_vals.append(zphys)
                rows.append(("Ward",kEW,round(a_s,4),f"bc={bc:.4f}",f"dR={dR:+.1f},kY={kY}",zphys))
def spread(v):
    v=np.array([x for x in v if np.isfinite(x)])
    return v.max()/v.min()-1, v.min(), v.max(), len(v)
print("R1  y_t(v) spread over shared+R1 corners: ",spread(crit_vals))
print("Ward y_t(v) spread over shared+Ward corners:",spread(ward_vals))
# restrict to shared premises only at their lane-central values for the route-specific ones
crit_shared=[r[-1] for r in rows if r[0]=="R1" and r[3]=="loop3" and r[4]=="lam_pl=+0e+00"]
ward_shared=[r[-1] for r in rows if r[0]=="Ward" and r[3].startswith("bc=0.4358") and r[4]=="dR=+0.0,kY=0"]
print("R1 over SHARED premises only (loop3, lam=0):",spread(crit_shared))
print("Ward over SHARED only (lifted BC, dR=0, kY=0):",spread(ward_shared))
# lane-only corners: R1 route-specific with shared fixed at lane central
c0=[r[-1] for r in rows if r[0]=="R1" and r[1]==0 and r[2]==round(ALPHA_S_V,4)]
w0=[r[-1] for r in rows if r[0]=="Ward" and r[1]==0 and r[2]==round(ALPHA_S_V,4)]
print("R1 route-specific only:",spread(c0)); print("Ward route-specific only:",spread(w0))
json.dump([[str(x) for x in r] for r in rows],open("testC_rows.json","w"))
for r in rows:
    if (r[1]==0 and r[2]==round(ALPHA_S_V,4)) or r[0]=="R1" and r[3]=="loop3" and r[4]=="lam_pl=+0e+00":
        print(r)
