"""T5 -- L=32 diagnostics: n=2, eps and C-evaluation robustness, wrong-vs-right c,
and a zero-curvature control."""
import numpy as np, math
from meas import report, fits, heat_diff
import cont

SV = [2,3,4,5,6,8,10,13,16,20,25]

print("############ T5a  n=2 at L=32 (Regge term 4x larger relative to dVol) ############")
for P,name in (((0,1,-1,0),"TRACELESS n=2"), ((1,1,1,1),"CONFORMAL n=2")):
    r = report(32, P, name, eps=0.05, n=2, svals=SV); fits(r,4,16); print()

print("############ T5b  conformal at L=32: c = 0 (none), 1/24 (wrong), tr g/96 ############")
for cov,imp,lab in ((None,False,"c = 0  (unimproved)"),(False,True,"c = 1/24  (WRONG)"),
                    (True,True,"c = tr g/96  (right)")):
    r = report(32,(1,1,1,1),f"CONFORMAL, {lab}",eps=0.05,n=1,svals=SV,
               cov=(cov if cov is not None else False), improve=imp, do_lda=False)
    fits(r,4,16); print()

print("############ T5c  amplitude and C-evaluation-point robustness (conformal, L=32) ###")
for eps in (0.025,0.05,0.10):
    r = report(32,(1,1,1,1),f"CONFORMAL eps={eps}",eps=eps,n=1,svals=[4,6,8,10,13,16,20],do_lda=True)
    print(f"      dVol/eps^2 = {r['dV']/eps**2:.3f}   dS/eps^2 = {r['dS']/eps**2:.3f}"); print()
r = report(32,(1,1,1,1),"CONFORMAL, C at edge midpoints",eps=0.05,n=1,
           svals=[4,6,8,10,13,16,20],cpoint='edge'); print()

print("############ T5d  ZERO-CURVATURE control: constant conformal metric ############")
for eps in (0.05,0.10):
    acc,rp,rf,el = heat_diff(32,eps,(1,1,1,1),0,[4,6,8,10,16,25])
    sv=np.array([4,6,8,10,16,25],float); F=(4*np.pi*sv)**2*acc
    dV=rp['vol']-rf['vol']; dS=rp['S']-rf['S']
    print(f"  eps={eps}: dVol={dV:.5f} (exact {((1+eps)**2-1)*32**4:.5f})  dS_Regge={dS:.3e}")
    print("     s:  " + "  ".join(f"{s:.0f}:{f/dV-1:+.2e}" for s,f in zip(sv,F))
          + "     <- [(4pi s)^2 dK]/dVol - 1")
