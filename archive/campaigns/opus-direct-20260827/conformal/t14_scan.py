"""T14 - (L, tau0, nk, polarisation) scan.  nk is varied so the derivative-expansion
error (relative order tau0 k^2, k = 2 pi nk / L) can be extrapolated to k -> 0, and
tau0 is varied so the lattice/diffeo contamination (empirically ~ 1/tau0^2 relative
to the Einstein term) can be extrapolated to tau0 -> inf."""
import numpy as np, sys, time, json; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import dW_multi
L=int(sys.argv[1]); TAUS=[float(x) for x in sys.argv[2].split(',')]
NKS=[int(x) for x in sys.argv[3].split(',')]
POLS={'conf':[1,1,1,1],'tran':[0,1,0,0],'TT':[0,1,-1,0]}
if len(sys.argv)>4: POLS={k:POLS[k] for k in sys.argv[4].split(',')}
AMP=0.03; SET=[(t,0.0,True) for t in TAUS]
t0=time.time()
S0=edge_s(L,0.0,1,[0,0,0,0]); g0=geometry(S0,L)
dW0=dW_multi(S0,L,SET,geom=g0); print(f"# flat pass {time.time()-t0:.0f}s",flush=True)
rows=[]
print(f"# T14 L={L} amp={AMP} improved m=0")
print(f"{'pol':>5} {'nk':>3} {'tau0':>6} {'tau0k2':>7} {'A/Ap':>8} {'B/Bp':>8} "
      f"{'part r':>8} {'corr12':>7} {'res/y':>9} {'res/Bx2':>9}")
for nm,al in POLS.items():
    for nk in NKS:
        S=edge_s(L,AMP,nk,al); g=geometry(S,L); dW=dW_multi(S,L,SET,geom=g)
        x1=(g['dVol']-g0['dVol']).ravel(); x2=(g['dReg']-g0['dReg']).ravel()
        c12=float(x1@x2/np.sqrt((x1@x1)*(x2@x2)))
        for t,(tau0,m2,imp) in enumerate(SET):
            y=(dW[t]-dW0[t]).ravel(); A,B,pr,R2=fit2(y,x1,x2); Ap,Bp=preds(tau0,m2)
            res=y-A*x1-B*x2
            r=dict(L=L,pol=nm,nk=nk,tau0=tau0,tk2=tau0*(2*np.pi*nk/L)**2,Ar=A/Ap,Br=B/Bp,
                   pr=pr,c12=c12,resy=float(np.linalg.norm(res)/np.linalg.norm(y)),
                   resB=float(np.linalg.norm(res)/np.linalg.norm(B*x2)))
            rows.append(r)
            print(f"{nm:>5} {nk:>3} {tau0:6.2f} {r['tk2']:7.3f} {r['Ar']:8.4f} {r['Br']:8.4f} "
                  f"{pr:8.4f} {c12:7.4f} {r['resy']:9.3e} {r['resB']:9.3e}",flush=True)
json.dump(rows,open(f"t14_L{L}.json","w"),indent=0)
print(f"# total {time.time()-t0:.0f}s")
