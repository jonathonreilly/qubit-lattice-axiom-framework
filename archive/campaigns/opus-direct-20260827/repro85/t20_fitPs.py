"""T20 - windowed fits of P(s) = [K_pert(s)-K_flat(s)](4 pi s)^2.
Model: P(s) = c_{-1}/s + c0 + c1 s + c2 s^2 (+ c3 s^3)
   c_{-1} : residual lattice error of the a_0 term (Symanzik-improved: O(a^4/s))
   c0     : Delta Vol            -- must equal the geometric value
   c1     : Delta int a_1 = Delta S_Regge / 3   <-- THE EINSTEIN COEFFICIENT
   c2,c3  : a_2, a_3 (derivative-expansion tail, relative size ~ s k^2)
"""
import numpy as np, sys, os; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]); AMP=float(sys.argv[2]); NKW=int(sys.argv[3])
IMP = (len(sys.argv)<5) or sys.argv[4]!='plain'
fn=f"spec_L{L}_a{AMP}_nk{NKW}.npz"
POLS=['gauge','TT','conf','tran']
if os.path.exists(fn):
    z=np.load(fn); spec={t:(z[t+'_lam'],*z[t+'_VR']) for t in ['flat']+POLS}
else:
    AL={'gauge':[1,0,0,0],'TT':[0,1,-1,0],'conf':[1,1,1,1],'tran':[0,1,0,0],'flat':[0,0,0,0]}
    spec={}; out={}
    for tag in ['flat']+POLS:
        S=edge_s(L,0.0 if tag=='flat' else AMP,NKW,AL[tag]); g=geometry(S,L)
        _,lam=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
        spec[tag]=(np.sort(lam),g['Vol'],g['Reg'])
        out[tag+'_lam']=np.sort(lam); out[tag+'_VR']=np.array([g['Vol'],g['Reg']])
    np.savez_compressed(fn,**out)
lf,Vf,Rf=spec['flat']; muf=lf+lf*lf/24.0 if IMP else lf
k2=(2*np.pi*NKW/L)**2
print(f"T20  L={L} amp={AMP} nk={NKW} operator={'improved' if IMP else 'plain'}  k^2={k2:.5f}")
print(f"{'pol':>6} {'window':>14} {'basis':>10} {'c0/dVol':>9} {'c1':>12} {'dS/3':>12} "
      f"{'c1/(dS/3)':>10} {'s*k2 max':>9} {'resid':>9}")
for tag in POLS:
    lp,Vp,Rp=spec[tag]; dV=Vp-Vf; dR=Rp-Rf; mu=lp+lp*lp/24.0 if IMP else lp
    for (s0,s1) in [(3,10),(4,14),(5,20),(6,30),(8,40),(10,60)]:
        if s1*k2>1.2: continue
        ss=np.linspace(s0,s1,60)
        P=np.array([(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2 for s in ss])
        for pw in ([-1,0,1,2],[-1,0,1,2,3],[-2,-1,0,1,2,3]):
            M=np.stack([ss**float(j) for j in pw],1)
            c,*_=np.linalg.lstsq(M,P,rcond=None)
            i0=pw.index(0); i1=pw.index(1)
            r=np.linalg.norm(P-M@c)/np.linalg.norm(P)
            print(f"{tag:>6} [{s0:>3},{s1:>3}]{'':>6} {str(pw[0])+'..'+str(pw[-1]):>10} "
                  f"{c[i0]/dV if dV else np.nan:9.4f} {c[i1]:12.5f} {dR/3:12.5f} "
                  f"{c[i1]/(dR/3) if abs(dR)>1e-6 else np.nan:10.4f} {s1*k2:9.3f} {r:9.1e}")
    print()
