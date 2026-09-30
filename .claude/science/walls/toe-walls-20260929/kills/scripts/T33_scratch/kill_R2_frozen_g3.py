"""R2 in the lane's own frame: SU(3) does not run between M_Pl and v (CMT rule), so g_3 is frozen in the 2-loop EW terms.
Compare R2 pair and counting pair with g_3 frozen at 1.0, 1.14 (lane's alpha_bare/u0^2 -> g^2 = 1/0.7704), and SM-running g_3."""
import sys, numpy as np
from scipy.integrate import solve_ivp
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T33_scratch')
from rge import *
up = up_from_mz(MPL,2)
def rhs_frozen(t,y):
    d=rhs(t,y,2); d[2]=0.0   # freeze g3
    # yt: keep its own running with frozen g3 (yt effect tiny)
    return d
def run_frozen(g22,gp2,g32,yt=0.42):
    y0=np.array([np.sqrt(5/3*gp2),np.sqrt(g22),np.sqrt(g32),yt])
    sol=solve_ivp(rhs_frozen,[np.log(MPL),np.log(MZ)],y0,rtol=1e-10,atol=1e-12,method='DOP853')
    return observables(sol.y[:,-1])
for g32 in (1.0, 1/0.5934**0.5, 0.2375):
    for nm,pair in (('counting',(0.25,0.2)),('R2 PS',(0.25,3/14)),('universal 1/4',(0.25,0.25))):
        o=run_frozen(*pair,g32)
        print(f"g3^2 frozen={g32:.3f} {nm:14s} sin2={o['s2']:.4f} ({(o['s2']/S2W_MZ-1)*100:+.1f}%) 1/aem={o['aem_inv']:.2f} ({(o['aem_inv']/AEM_INV_MZ-1)*100:+.1f}%)")
