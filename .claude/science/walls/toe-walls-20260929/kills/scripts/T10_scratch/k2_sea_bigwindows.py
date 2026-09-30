import numpy as np, json, beam_vs_sea as b
from numbound import scan_num, disjoint
out={}
def sea(L,T,g,coup):
    h=b.chain_h(L); j0=L//2
    e,U=np.linalg.eigh(h); Phi0=U[:,:L//2]
    Vu,Vd=(g,0.0) if coup=='proj' else (g,-g)
    Pu=b.evolve(h,j0,Vu,Phi0,T); Pd=b.evolve(h,j0,Vd,Phi0,T)
    return b.corr(Pu),b.corr(Pd),j0
for (L,T) in [(120,15.0),(240,30.0)]:
  for g,coup in [(20.0,'proj'),(3.0,'sym')]:
    Du,Dd,j0=sea(L,T,g,coup)
    r=int(2*T+14); lo,hi=max(1,j0-r),min(L-1,j0+r)
    for cap in (8,18,36,60):
        tab=scan_num(Du,Dd,lo,hi,cap)
        # exclude windows containing the pointer site itself (contact) and report both
        away={k:v for k,v in tab.items() if not (k[0]<=j0<k[0]+k[1])}
        row=dict(L=L,T=T,g=g,coup=coup,cap=cap,maxchi_all=round(max(tab.values()),3),maxchi_away=round(max(away.values()),3),
                 R09=len(disjoint(tab,0.9)),R05=len(disjoint(tab,0.5)),R05_away=len(disjoint(away,0.5)),R03_away=len(disjoint(away,0.3)))
        print(row,flush=True); out[f"{L}_{g}_{coup}_{cap}"]=row
json.dump(out,open('k2_sea_bigwindows.json','w'),indent=1)
