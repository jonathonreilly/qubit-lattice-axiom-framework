import numpy as np, sys
sys.path.insert(0, '.')
from rge import *
LT = np.log(MPL/MZ)
mt = 172.7
# fermion-only U(1): d(1/alpha)/dln(mu) = -(2/3pi) * sum N_c Q^2  (Dirac fermions)
sumNQ2 = 3*1 + 3*3*(4/9) + 3*3*(1/9)      # 3 leptons + 3 up-type*3 colours + 3 down-type*3 colours = 8
sum_noT = sumNQ2 - 3*(4/9)                 # top inactive between M_Z and m_t
run_f = (2/(3*PI))*(sumNQ2*LT - (sumNQ2-sum_noT)*np.log(mt/MZ))
print(f"sum N_c Q^2 = {sumNQ2:.3f};  fermion-only screening M_Pl -> M_Z: {run_f:.2f} units of 1/alpha")
# full SM: 1/alpha_em = 1/alpha_2 + 1/alpha_Y, 1-loop, b_2=-19/6, b_Y=41/6 (Y/2 norm)
run_sm = (( -(-19/6) - (41/6))/(2*PI))*(-LT)*(-1)   # placeholder replaced below
d_sm = (-(-19/6) - (41/6))/(2*PI)           # d(1/a_em)/dln mu = (19/6 - 41/6)/(2pi) = -0.584
run_sm = -d_sm*LT                            # 1/a_em(M_Z) - 1/a_em(M_Pl) = -d*... 
# 1/a(MZ) = 1/a(MPl) - d*LT  (since d = d(1/a)/dlnmu, going down by LT)
print(f"full-SM (SU(2)xU(1), 1-loop) shift of 1/alpha_em from M_Pl to M_Z: {-d_sm*LT:+.2f} (i.e. 1/alpha_em(MZ) = 1/alpha_em(MPl) + {-d_sm*LT:.2f}); check with 2-loop SM run: ", end="")
o = observables(up_from_mz(MPL, 2)); print(f"{AEM_INV_MZ - o['aem_inv']:.2f}")
print("\nUV alpha_G (unit-charge coupling at M_Pl) -> IR 1/alpha_em(M_Z):")
print(f"{'alpha_G':>10s} {'1/aG':>7s} | fermion-only  ratio to 127.95 | full-SM sum  ratio | (raw lane comparison 1/aG vs 137)")
for aG, lab in ((0.37, 'ring 4^3 flux'), (0.30, 'ring ~mid'), (0.278, 'ring 8^3 flux'), (1/(4*PI*5), '1/(20 pi) [g_Y^2=1/5]'), (1/(16*PI), '1/(16 pi) [g_2^2=1/4]'), (1/60., '1/60')):
    f = 1/aG + run_f; s = 1/aG + (-d_sm*LT)
    print(f"{aG:10.4f} {1/aG:7.2f} | {f:8.2f}  {AEM_INV_MZ/f:5.2f}x            | {s:8.2f}  {AEM_INV_MZ/s:5.2f}x    ({137.036*aG:5.1f}x)  {lab}")
# sensitivity: IR spread over UV 1/alpha in [3,63]
for nm, r in (('fermion-only', run_f), ('full SM', -d_sm*LT)):
    lo, hi = 3 + r, 63 + r
    print(f"{nm}: IR 1/alpha over UV 1/alpha in [3,63]: [{lo:.1f}, {hi:.1f}]  spread factor {hi/lo:.2f}")
# taste multiplication of the fermion loop: n_t extra copies massless over the top W e-folds of running
print("\nIf tastes replicate the charged fermions (T24/T30): extra screening = (n_extra) * (2/3pi)*8 * W, W e-folds of massless tastes")
for nx, W in ((15, 1.2), (15, 4.8), (15, LT)):
    add = nx*(2/(3*PI))*sumNQ2*W
    print(f"   {nx} extra copies over {W:.1f} e-folds: +{add:.1f} units of 1/alpha  -> 1/alpha_UV needed for 127.95: {AEM_INV_MZ - run_f - add:.1f}")
