import sys, math
sys.dont_write_bytecode=True
MAIN='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts'
sys.path.insert(0, MAIN)
import numpy as np
from scipy.optimize import minimize
import frontier_quark_mass_ratio_full_solve as fs
TARGET=np.array([fs.V_US_ATLAS, fs.V_CB_ATLAS, fs.V_UB_ATLAS])
def obj(x):
    r_uc,r_ct=math.exp(x[0]),math.exp(x[1])
    if r_uc*r_ct>=1: return 1e12
    v=fs.compute_ckm_observables(r_uc,r_ct,fs.DELTA_STD,fs.DELTA_STD)[:3]
    return float(np.sum(((np.array(v)-TARGET)/np.array([1e-3,1e-3,5e-4]))**2))
SEEDS=[(1.7e-3,7.4e-3),(1e-3,5e-3),(3e-3,1e-2),(1e-2,2e-2),(5e-4,2e-2),(2e-2,5e-2),(2e-3,3.7e-3),(2e-3,1e-3)]
def invert():
    best=None
    for s in SEEDS:
        r=minimize(obj,np.log(s),method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-11,maxiter=1500))
        if best is None or r.fun<best.fun: best=r
    return math.exp(best.x[0]),math.exp(best.x[1]),best.fun
print("mixed convention (lane):  R_SB=%.5f R_DB=%.3e"%(fs.R_SB,fs.R_DB), " ->", invert())
R_DS=fs.R_DS
for label,rsb in [("common-scale m_s/m_b = 0.01887 (T46)",0.01887),("common-scale, -1.2% (1 sigma)",0.01887*(1-0.012)),("common-scale, +1.2%",0.01887*1.012)]:
    fs.R_SB=rsb; fs.R_DB=R_DS*rsb
    ruc,rct,o=invert()
    print(f"{label}: r_uc={ruc:.4e} ({100*(ruc/1.975e-3-1):+.1f}% vs common 1.975e-3; {100*(ruc/fs.R_UC_OBS-1):+.1f}% vs lane comparator)  r_ct={rct:.4e} ({100*(rct/3.71e-3-1):+.1f}% vs common 3.71e-3; {100*(rct/fs.R_CT_OBS-1):+.1f}% vs lane)  obj={o:.3g}")
