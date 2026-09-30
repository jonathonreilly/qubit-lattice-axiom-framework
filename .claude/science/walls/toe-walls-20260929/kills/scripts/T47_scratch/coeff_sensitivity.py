"""T47 Test B: is the 'up ratios inverted from CKM magnitudes' edge predictive, or carried by the four calibrated NNI coefficients?
Imports the repo's minimal Schur-NNI full-solve module read-only and re-runs its magnitude inversion with perturbed coefficients."""
import sys, math, json
sys.dont_write_bytecode = True
MAIN='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts'
sys.path.insert(0, MAIN)
import numpy as np
from scipy.optimize import minimize
import frontier_quark_mass_ratio_full_solve as fs

C0 = dict(C12_U=fs.C12_U, C23_U=fs.C23_U, C12_D=fs.C12_D, C23_D=fs.C23_D)
TARGET = np.array([fs.V_US_ATLAS, fs.V_CB_ATLAS, fs.V_UB_ATLAS])
print("atlas |Vus|,|Vcb|,|Vub| =", TARGET, " R_DB,R_SB =", fs.R_DB, fs.R_SB)
print("observed comparators r_uc,r_ct =", fs.R_UC_OBS, fs.R_CT_OBS)

def set_coeffs(c):
    for k,v in c.items(): setattr(fs, k, v)

def obj_log(x):
    r_uc, r_ct = math.exp(x[0]), math.exp(x[1])
    if r_uc*r_ct >= 1: return 1e12
    vus, vcb, vub, _ = fs.compute_ckm_observables(r_uc, r_ct, fs.DELTA_STD, fs.DELTA_STD)
    res = (np.array([vus,vcb,vub]) - TARGET) / np.array([1e-3,1e-3,5e-4])
    return float(np.sum(res**2))

SEEDS = [(1.7e-3,7.4e-3),(1e-3,5e-3),(3e-3,1e-2),(1e-2,2e-2),(5e-4,2e-2),(2e-2,5e-2)]
def invert(c, seeds=SEEDS):
    set_coeffs(c)
    best=None
    for s in seeds:
        r = minimize(obj_log, np.log(s), method='Nelder-Mead', options=dict(xatol=1e-6,fatol=1e-10,maxiter=600))
        if best is None or r.fun < best.fun: best=r
    r_uc, r_ct = math.exp(best.x[0]), math.exp(best.x[1])
    vus,vcb,vub,J = fs.compute_ckm_observables(r_uc, r_ct, fs.DELTA_STD, fs.DELTA_STD)
    return dict(r_uc=r_uc, r_ct=r_ct, obj=best.fun, vus=vus, vcb=vcb, vub=vub)

out = {}
base = invert(C0); out['baseline']=base
print("BASELINE", base, " r_uc/obs-1 = %+.2f%%  r_ct/obs-1 = %+.2f%%"%(100*(base['r_uc']/fs.R_UC_OBS-1),100*(base['r_ct']/fs.R_CT_OBS-1)))

# B1: +-5% one-at-a-time
print("\nB1 one-at-a-time +-5% coefficient perturbations")
b1=[]
for k in C0:
    for sgn in (+1,-1):
        c = dict(C0); c[k] = C0[k]*(1+0.05*sgn)
        d = invert(c)
        dl_uc = 100*(d['r_uc']/base['r_uc']-1); dl_ct = 100*(d['r_ct']/base['r_ct']-1)
        ok = d['obj']<1.0
        print(f"  {k} {sgn*5:+d}%: r_uc {dl_uc:+7.1f}%  r_ct {dl_ct:+7.1f}%  fit-obj {d['obj']:.3g} (CKM reproduced: {ok})  |Vus|={d['vus']:.4f} |Vcb|={d['vcb']:.4f} |Vub|={d['vub']:.5f}")
        b1.append(dict(coef=k,sgn=sgn,d_uc_pct=dl_uc,d_ct_pct=dl_ct,obj=d['obj']))
out['B1']=b1
set_coeffs(C0)

# B2: coefficient-blind prior
print("\nB2 log-uniform coefficient prior [0.5,2]^4, keep samples that reproduce atlas CKM magnitudes")
rng = np.random.default_rng(47)
N=int(sys.argv[1]) if len(sys.argv)>1 else 1500
rows=[]
for i in range(N):
    c = {k: math.exp(rng.uniform(math.log(0.5), math.log(2.0))) for k in C0}
    d = invert(c, seeds=SEEDS[:4]); d.update(c); rows.append(d)
set_coeffs(C0)
good = [r for r in rows if r['obj'] < 4.0]   # all three magnitudes within ~2 scale units in quadrature
print(f"  samples {N}, CKM reproduced (obj<4): {len(good)}")
if good:
    ruc = np.array([g['r_uc'] for g in good]); rct = np.array([g['r_ct'] for g in good])
    def frac(tol):
        return np.mean((abs(ruc/fs.R_UC_OBS-1)<tol)&(abs(rct/fs.R_CT_OBS-1)<tol))
    for tol in (0.02,0.05,0.10,0.30):
        print(f"  fraction of CKM-reproducing samples with BOTH ratios within {int(tol*100)}% of observed: {frac(tol):.3f}")
    print("  r_uc percentiles 5/25/50/75/95:", np.percentile(ruc,[5,25,50,75,95]))
    print("  r_ct percentiles 5/25/50/75/95:", np.percentile(rct,[5,25,50,75,95]))
    print("  observed r_uc, r_ct:", fs.R_UC_OBS, fs.R_CT_OBS)
    out['B2']=dict(N=N, n_good=len(good), frac2=frac(.02), frac5=frac(.05), frac10=frac(.10), frac30=frac(.30),
        ruc_pct=list(np.percentile(ruc,[5,25,50,75,95])), rct_pct=list(np.percentile(rct,[5,25,50,75,95])))
json.dump(out, open('coeff_sensitivity.json','w'), indent=1, default=float)
