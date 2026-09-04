"""T13 - diagnostics that decide whether B means anything:
 (a) PURE-GAUGE channel g_00 = 1+f(x0): flat space in disguise, R=0, S_Regge=0.
     y must then be exactly A dVol.  The residual there is the lattice's
     diffeomorphism-violation floor -- an assumption-free contamination scale.
 (b) off-span residual of the two-parameter fit vs the size of the Regge term.
 (c) linearity in the amplitude.
"""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
L=int(sys.argv[1]) if len(sys.argv)>1 else 32
TAUS=[2.7,4.0,6.0,8.0]; SET=[(t,0.0,True) for t in TAUS]
ALL={'gauge(1,0,0,0)':[1,0,0,0],'conf(1,1,1,1)':[1,1,1,1],'tran(0,1,0,0)':[0,1,0,0],
     'TT (0,1,-1,0)':[0,1,-1,0]}
S0=edge_s(L,0.0,1,[0,0,0,0]); g0=geometry(S0,L)
dW0=dW_multi(S0,L,SET,geom=g0)
print(f"T13  L={L} nk=1 amp=0.03 improved m=0")
print(f"{'pol':>16} {'tau0':>5} {'|x2|/|x1|':>10} {'S_Regge':>12} "
      f"{'|res|/|y|':>10} {'|res|/|B x2|':>12} {'B/Bpred':>9} {'A/Apred':>9}")
for nm,al in ALL.items():
    S=edge_s(L,0.03,1,al); g=geometry(S,L)
    dW=dW_multi(S,L,SET,geom=g)
    x1=(g['dVol']-g0['dVol']).ravel(); x2=(g['dReg']-g0['dReg']).ravel()
    for t,(tau0,m2,imp) in enumerate(SET):
        y=(dW[t]-dW0[t]).ravel(); A,B,pr,R2=fit2(y,x1,x2); Ap,Bp=preds(tau0,m2)
        res=y-A*x1-B*x2
        print(f"{nm:>16} {tau0:5.1f} {np.linalg.norm(x2)/np.linalg.norm(x1):10.3e} "
              f"{g['Reg']-g0['Reg']:12.4e} {np.linalg.norm(res)/np.linalg.norm(y):10.3e} "
              f"{np.linalg.norm(res)/max(np.linalg.norm(B*x2),1e-300):12.3e} {B/Bp:9.4f} {A/Ap:9.4f}")
print()
print("T13(c) amplitude linearity, conformal, tau0=4:")
for amp in (0.01,0.03,0.10):
    S=edge_s(L,amp,1,[1,1,1,1]); g=geometry(S,L); dW=dW_multi(S,L,SET,geom=g)
    x1=(g['dVol']-g0['dVol']).ravel(); x2=(g['dReg']-g0['dReg']).ravel()
    y=(dW[1]-dW0[1]).ravel(); A,B,pr,_=fit2(y,x1,x2); Ap,Bp=preds(*SET[1][:2])
    print(f"      amp={amp:5.2f}:  A/Apred={A/Ap:.5f}  B/Bpred={B/Bp:.5f}  partial r={pr:.5f}")
