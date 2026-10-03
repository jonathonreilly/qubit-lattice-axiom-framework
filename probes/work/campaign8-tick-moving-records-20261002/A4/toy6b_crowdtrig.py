"""Crowd-triggered formation (empty site forms with odds p only if >= z-1 = 3 neighbours are recorded) + tilted moves.
2D 128^2, 2000 ticks. Start: jam disk radius R0 at centre + vapour at rho_v. Bath-free periodic box.
Reports: holes inside the jam, total records, formations per tick, event-rate and density profiles vs r (second half)."""
import sys, numpy as np
from t1lib import tick
g=float(sys.argv[1]); p=float(sys.argv[2]); rv=float(sys.argv[3]); R0=10.0; L=128; T=2000
rng=np.random.default_rng(11)
yy,xx=np.meshgrid(np.arange(L),np.arange(L),indexing="ij"); r=np.hypot(xx-L/2+0.5,yy-L/2+0.5)
occ=rng.random((L,L))<rv; occ[r<=R0]=True
expg=np.exp(g*np.arange(5)); rb=np.floor(r).astype(int); nb=rb.max()+1; cnt=np.bincount(rb.ravel(),minlength=nb)
ra=np.zeros(nb); ea=np.zeros(nb); fa=np.zeros(nb); na=0; N0=occ.sum()
for t in range(1,T+1):
    occ,out,form=tick(occ,g,"crowdtrig",rng,dict(p=p,mtrig=int(sys.argv[4]) if len(sys.argv)>4 else 3),moves=True,expg=expg)
    if t in (1,200,500,1000,2000):
        print(f"t={t}: holes in r<={R0-2:.0f}: {(~occ[r<=R0-2]).mean():.4f}  total records {occ.sum()} (start {N0})  "
              f"vapour density r in [20,50]: {occ[(r>=20)&(r<=50)].mean():.4f}",flush=True)
    if t>T//2:
        ra+=np.bincount(rb.ravel(),weights=occ.ravel().astype(float),minlength=nb)
        ea+=np.bincount(rb.ravel(),weights=(out|form).ravel().astype(float),minlength=nb)
        fa+=np.bincount(rb.ravel(),weights=form.ravel().astype(float),minlength=nb); na+=1
rho=ra/(cnt*na); e=ea/(cnt*na); f=fa/(cnt*na)
print(" r   rho     events/site/tick  formations/site/tick")
for i in [0,3,6,8,9,10,11,12,13,14,16,20,25,30,35,40,45,50,55,60]:
    print(f"{i+0.5:5.1f} {rho[i]:.4f} {e[i]:.5f} {f[i]:.6f}")
