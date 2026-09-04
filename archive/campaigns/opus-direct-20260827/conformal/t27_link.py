"""T27 - consistency link between the two measurements.
The per-edge gradient fit at cutoff tau0 is a WEIGHTED AVERAGE of the heat-trace
ratio r(s) = [measured a_1] / [S_Regge/3]:
      B(tau0)/B_pred = tau0 * int_{tau0}^inf r(s) s^-2 ds
because  dW/ds_e = (1/2) int_{tau0}^inf dtau  d/ds_e Tr e^{-tau Delta}  and the a_1
piece carries weight (4 pi tau)^-2 tau -> tau^-2 dtau.  Predicting the gradient fit
from the heat trace (two completely different code paths) tests both."""
import numpy as np, sys; sys.path.insert(0,".")
z=np.load("spec_L64_a0.06_nk1.npz")
lf=z['flat_lam']; Vf,Rf=z['flat_VR']; muf=lf+lf*lf/24.0
ss=np.concatenate([np.arange(2.6,10,0.2),np.arange(10,40,1.0),np.arange(40,200,4.0)])
print("T27 L=64 improved.  r(s) integrated with weight tau0/s^2 -> predicted B/B_pred")
for t in ('TT','conf'):
    lp=z[t+'_lam']; Vp,Rp=z[t+'_VR']; mu=lp+lp*lp/24.0; dV=Vp-Vf; dR=Rp-Rf
    r=np.array([((float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2-dV)/s/(dR/3)
                for s in ss])
    out=[]
    for t0 in (2.7,4.0,6.0,8.0,12.0):
        m=ss>=t0
        w=ss[m]**-2.0
        out.append(t0*np.trapezoid(r[m]*w,ss[m])+t0*(r[m][-1]/ss[m][-1]))  # tail r~const
    print(f"  {t:>5}: predicted B/B_pred at tau0=2.7,4,6,8,12 : "
          +"  ".join(f"{v:.4f}" for v in out))
