"""KILL extra: feed the historic lattice-'Derived' NNI coefficients (archive_unlanded ... 178_CKM_CLEAN_DERIVATION_NOTE.md, 193_...) into the minimal Schur-NNI inversion."""
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
SEEDS=[(1.7e-3,7.4e-3),(1e-3,5e-3),(3e-3,1e-2),(1e-2,2e-2),(5e-4,2e-2),(2e-2,5e-2)]
def invert(c):
    for k,v in c.items(): setattr(fs,k,v)
    best=None
    for s in SEEDS:
        r=minimize(obj,np.log(s),method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-11,maxiter=1500))
        if best is None or r.fun<best.fun: best=r
    return math.exp(best.x[0]),math.exp(best.x[1]),best.fun
for label,c in [("fitted (lane)",dict(C12_U=1.48,C23_U=0.65,C12_D=0.91,C23_D=0.65)),
                ("theorem-note c23 (0.672,0.663)",dict(C12_U=1.48,C23_U=0.672,C12_D=0.91,C23_D=0.663)),
                ("historic lattice-derived A (1.14,0.40,0.93,0.72)",dict(C12_U=1.14,C23_U=0.40,C12_D=0.93,C23_D=0.72)),
                ("historic lattice-derived B (1.14,1.01,0.93,0.72)",dict(C12_U=1.14,C23_U=1.01,C12_D=0.93,C23_D=0.72))]:
    ruc,rct,o=invert(c)
    print(f"{label:52s} r_uc={ruc:.3e} ({100*(ruc/fs.R_UC_OBS-1):+8.1f}%)  r_ct={rct:.3e} ({100*(rct/fs.R_CT_OBS-1):+8.1f}%)  CKM obj={o:.3g}")
