"""T47 C6: what a_u actually moves in the reduced projector-ray carrier. Fix the ratios at the lane's solved values and vary a_u only."""
import sys, math
sys.dont_write_bytecode=True
MAIN='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts'
sys.path.insert(0, MAIN)
import numpy as np
import frontier_quark_projector_ray_phase_completion as pr
from frontier_quark_mass_ratio_full_solve import J_ATLAS, V_CB_ATLAS, V_UB_ATLAS, V_US_ATLAS
AD=1/math.sqrt(42); PHI=-1/42
RUC, RCT = 1.681663e-3, 7.365646e-3
AU0 = 0.778175
def obs(au):
    o=pr.compute_projector_observables([RUC,RCT,au,AD,PHI],shared_phase=True)
    return np.array(o[4:8])
b=obs(AU0)
print("at a_u=%.5f: Vus,Vcb,Vub,J ="%AU0, b, " atlas:", V_US_ATLAS, V_CB_ATLAS, V_UB_ATLAS, J_ATLAS)
for au in (0.7749, 0.72, 0.85):
    o=obs(au); print(f"a_u={au:.4f}: d ln a_u = {math.log(au/AU0):+.4f};  d ln(Vus,Vcb,Vub,J) =", np.round(np.log(o/b),4))
# elasticities by finite difference
h=1e-3
e=(np.log(obs(AU0*(1+h)))-np.log(obs(AU0*(1-h))))/(math.log(1+h)-math.log(1-h))
print("elasticity d ln X / d ln a_u for (Vus,Vcb,Vub,J):", np.round(e,3))
# elasticity of the fitted ratios (from ray_blind.json)
import json
d=json.load(open('ray_blind.json'))['sens']
a=np.array([x['au'] for x in d]); ruc=np.array([x['r_uc'] for x in d]); rct=np.array([x['r_ct'] for x in d])
o=np.argsort(a); a,ruc,rct=a[o],ruc[o],rct[o]
print("elasticity of fitted r_uc, r_ct wrt a_u (0.72-0.85): %.3f, %.3f"%(np.log(ruc[-1]/ruc[0])/np.log(a[-1]/a[0]), np.log(rct[-1]/rct[0])/np.log(a[-1]/a[0])))
