"""T47 Test C: in the repo's reduced projector-ray carrier (a_d=1/sqrt42, phi=-1/42 supplied), remove the OBSERVED up-ratio residuals
and ask what CKM(+J) alone say about (m_u/m_c, m_c/m_t) when a_u is the RPSR value vs nearby values."""
import sys, math, json
sys.dont_write_bytecode=True
MAIN='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts'
sys.path.insert(0, MAIN)
import numpy as np
from scipy.optimize import minimize
import frontier_quark_projector_ray_phase_completion as pr
from frontier_quark_mass_ratio_full_solve import J_ATLAS, R_CT_OBS, R_UC_OBS, V_CB_ATLAS, V_UB_ATLAS, V_US_ATLAS
AD = 1/math.sqrt(42); PHI = -1/42
AU_RPSR = math.sqrt(5/6)*(1-48/(49*math.sqrt(42)))
print("RPSR a_u =", AU_RPSR, " observed-ratio targets:", R_UC_OBS, R_CT_OBS)
SC = np.array([1e-4,1e-4,1e-4,2e-6])
def ckm_res(x_log, au, with_mass=False, ad=AD, phi=PHI):
    r_uc, r_ct = math.exp(x_log[0]), math.exp(x_log[1])
    try:
        out = pr.compute_projector_observables([r_uc, r_ct, au, ad, phi], shared_phase=True)
    except ValueError:
        return None
    vus,vcb,vub,J = out[4],out[5],out[6],out[7]
    res = [(vus-V_US_ATLAS)/1e-4,(vcb-V_CB_ATLAS)/1e-4,(vub-V_UB_ATLAS)/1e-4,(J-J_ATLAS)/2e-6]
    if with_mass:
        res += [(r_uc-R_UC_OBS)/1e-4,(r_ct-R_CT_OBS)/1e-4]
    return np.array(res)
def fit(au, with_mass=False, seeds=None, ad=AD, phi=PHI):
    best=None
    seeds = seeds or [(1.7e-3,7.4e-3),(1e-3,5e-3),(3e-3,1e-2),(1e-2,2e-2),(5e-4,2e-2),(2e-2,5e-2),(1e-4,3e-3)]
    for s in seeds:
        f=lambda x: (1e12 if ckm_res(x,au,with_mass,ad,phi) is None else float(np.sum(ckm_res(x,au,with_mass,ad,phi)**2)))
        r=minimize(f, np.log(s), method='Nelder-Mead', options=dict(xatol=1e-7,fatol=1e-10,maxiter=1500))
        if best is None or r.fun<best.fun: best=r
    return math.exp(best.x[0]), math.exp(best.x[1]), best.fun

print("\nC0: reproduce the lane's anchored solve (with observed ratios as fit targets), a_u free-ish:")
# scan a_u to find the lane's solved value: minimize over au too
from scipy.optimize import minimize_scalar
def prof(au):
    return fit(au, with_mass=True)[2]
res = minimize_scalar(prof, bounds=(0.70,0.85), method='bounded', options=dict(xatol=1e-6))
au_solved = res.x
ruc,rct,obj = fit(au_solved, with_mass=True)
print(f"  solved a_u = {au_solved:.6f} (lane: 0.778262), r_uc={ruc:.6e} r_ct={rct:.6e}, chi2={obj:.3g}")

print("\nC1: CKM-only (no observed masses) inversion at a_u = RPSR:")
ruc,rct,obj = fit(AU_RPSR, with_mass=False)
print(f"  r_uc={ruc:.4e} (obs {R_UC_OBS:.4e}, {100*(ruc/R_UC_OBS-1):+.1f}%)  r_ct={rct:.4e} (obs {R_CT_OBS:.4e}, {100*(rct/R_CT_OBS-1):+.1f}%)  CKM chi2={obj:.3g}")
print("  with observed masses as fit targets at a_u = RPSR:")
r2=fit(AU_RPSR, with_mass=True); print(f"  r_uc={r2[0]:.4e} r_ct={r2[1]:.4e} chi2={r2[2]:.3g}")

print("\nC2: sensitivity: CKM-only inversion vs a_u")
tab=[]
for au in [0.72,0.74,0.76,0.77,AU_RPSR,0.7783,0.79,0.80,0.82,0.85]:
    ruc,rct,obj = fit(au, with_mass=False)
    print(f"  a_u={au:.4f}: r_uc={ruc:.4e} ({100*(ruc/R_UC_OBS-1):+7.1f}%)  r_ct={rct:.4e} ({100*(rct/R_CT_OBS-1):+7.1f}%)  CKM chi2={obj:.3g}")
    tab.append(dict(au=au,r_uc=ruc,r_ct=rct,chi2=obj))

print("\nC3: how much chi2 do the observed ratios cost at a_u = RPSR, versus at solved a_u (CKM+mass fit):")
for au in (AU_RPSR, au_solved):
    ruc,rct,obj=fit(au,with_mass=True); print(f"  a_u={au:.5f}: chi2 (CKM+mass residuals) = {obj:.3g}  r_uc={ruc:.4e} r_ct={rct:.4e}")

print("\nC4: free a_d, phi too (5 free params, CKM 4 targets): is the ratio pair pinned at all? scan a_d at fixed a_u=RPSR, phi=-1/42:")
for ad in (0.12,0.14,AD,0.17,0.19):
    ruc,rct,obj=fit(AU_RPSR,with_mass=False,ad=ad)
    print(f"  a_d={ad:.4f}: r_uc={ruc:.4e} ({100*(ruc/R_UC_OBS-1):+7.1f}%) r_ct={rct:.4e} ({100*(rct/R_CT_OBS-1):+7.1f}%) chi2={obj:.3g}")
json.dump(dict(au_rpsr=AU_RPSR, au_solved=au_solved, sens=tab), open('ray_blind.json','w'), indent=1, default=float)
