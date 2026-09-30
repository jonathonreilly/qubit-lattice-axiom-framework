"""T58 chain test. Own re-implementation of the lane's one-flavour leptogenesis chain
(scripts/dm_leptogenesis_exact_common.py, read-only import for a cross-check only).
Pre-registration: PREREG.md in this folder (written before this script was run).
Run: PYTHONDONTWRITEBYTECODE=1 python3 t58_chain_test.py
"""
import math, sys, itertools, json
import numpy as np
from scipy import integrate, special, optimize

MAIN = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts"
sys.dont_write_bytecode = True
PI = math.pi
ZETA3 = 1.2020569031595942
M_PL = 1.2209e19
ETA_OBS = 6.12e-10
u0 = 0.5934 ** 0.25
ALPHA = (1.0 / (4 * PI)) / u0            # alpha_LM
C_APBC = (7 / 8) ** 0.25
V_EW = M_PL * C_APBC * ALPHA ** 16
G_S_TODAY = 2 + (7 / 8) * 6 * (4 / 11)
S_OVER_NG = (PI ** 4 / (45 * ZETA3)) * G_S_TODAY

BASE = dict(g_weak=0.653, kA=7, kB=8, eps_scale=1.0, gamma=0.5, E1=math.sqrt(8 / 3),
            E2=math.sqrt(8) / 3, gstar=28 + 7 / 8 * 90, csph=28 / 79, Mscale=1.0, K00=2.0)

def g_self(x): return math.sqrt(x) / (x - 1)
def f_vert(x): return 0.5 if abs(x - 1) < 1e-6 else math.sqrt(x) * (1 - (1 + x) * math.log((1 + x) / x))
def f_tot(x): return g_self(x) + f_vert(x)

def n_eq(z): return 0.5 * z * z * float(special.kv(2, z))

_kappa_cache = {}
def kappa_ode(K):
    key = round(K, 9)
    if key in _kappa_cache: return _kappa_cache[key]
    def rhs(z, s):
        nN, nB = s
        d = K * z * float(special.kv(1, z) / special.kv(2, z))
        w = 0.25 * K * z ** 3 * float(special.kv(1, z))
        return [-d * (nN - n_eq(z)), d * (nN - n_eq(z)) - w * nB]
    sol = integrate.solve_ivp(rhs, (1e-3, 35.0), (n_eq(1e-3), 0.0), method="BDF", rtol=1e-10, atol=1e-12)
    v = abs(float(sol.y[1, -1]))
    _kappa_cache[key] = v
    return v

def chain(p, raw_sign=False):
    p = {**BASE, **p}
    Y0 = p["g_weak"] ** 2 / 64.0
    a_mr = p["Mscale"] * M_PL * ALPHA ** p["kA"]
    b_mr = p["Mscale"] * M_PL * ALPHA ** p["kB"]
    e = p["eps_scale"] * ALPHA / 2
    m1, m2, m3 = b_mr * (1 - e), b_mr * (1 + e), a_mr
    x23, x3 = (m2 / m1) ** 2, (m3 / m1) ** 2
    cp1 = -2 * p["gamma"] * p["E1"] / 3
    cp2 = 2 * p["gamma"] * p["E2"] / 3
    eps_raw = (1 / (8 * PI)) * Y0 ** 2 * (cp1 * f_tot(x23) + cp2 * f_tot(x3)) / p["K00"]
    h_coef = math.sqrt(4 * PI ** 3 * p["gstar"] / 45) / M_PL
    m_tilde = p["K00"] * Y0 ** 2 * V_EW ** 2 / m1 * 1e9
    m_star = 8 * PI * V_EW ** 2 * h_coef * 1e9
    K = m_tilde / m_star
    kap = kappa_ode(K)
    d_th = 135 * ZETA3 / (4 * PI ** 4 * p["gstar"])
    eta = S_OVER_NG * p["csph"] * d_th * abs(eps_raw) * kap / ETA_OBS
    m3_light_eV = Y0 ** 2 * V_EW ** 2 / m1 * 1e9
    out = dict(eta=eta, eps=eps_raw, K=K, kappa=kap, x23=x23, x3=x3, M1=m1, m3_light_eV=m3_light_eV)
    return out

def dlog(param, rel=0.01):
    b = BASE[param]
    up = chain({param: b * (1 + rel)})["eta"]; dn = chain({param: b * (1 - rel)})["eta"]
    return (math.log(up) - math.log(dn)) / (math.log(1 + rel) - math.log(1 - rel))

res = {}
print("=== S0 reproduction ===")
r0 = chain({})
target = 0.188785929502
print(f"my eta/eta_obs = {r0['eta']:.12f}  cache = {target}  rel diff = {abs(r0['eta']-target)/target:.2e}")
print(f"K = {r0['K']:.6f}  kappa = {r0['kappa']:.9f}  eps1 = {r0['eps']:.6e} (signed)  x23 = {r0['x23']:.5f}  x3 = {r0['x3']:.3f}")
try:
    sys.path.insert(0, MAIN)
    import dm_leptogenesis_exact_common as C
    pk = C.exact_package()
    kd, kf = C.kappa_axiom_reference(pk.k_decay_exact)
    eta_repo = C.S_OVER_NGAMMA_EXACT * C.C_SPH * C.D_THERMAL_EXACT * pk.epsilon_1 * kd / C.ETA_OBS
    print(f"repo helper eta/eta_obs = {eta_repo:.12f}; |mine-repo|/repo = {abs(r0['eta']-eta_repo)/eta_repo:.2e}")
    res["repo_helper_eta"] = eta_repo
except Exception as ex:
    print("repo helper import failed:", ex)
res["S0"] = dict(mine=r0["eta"], cache=target, rel=abs(r0["eta"] - target) / target)

print("\n=== S1 log-sensitivities d ln eta / d ln p ===")
S1 = {}
for prm in ["g_weak", "Mscale", "gamma", "eps_scale", "gstar", "csph", "E1", "E2"]:
    S1[prm] = dlog(prm)
    print(f"  {prm:10s} {S1[prm]:+.4f}")
res["S1"] = S1

print("\n=== S2 cost to reach eta/eta_obs = 1, one input at a time (factor on the base value) ===")
S2 = {}
for prm, lo, hi in [("gamma", 0.5, 200), ("E1", 0.5, 200), ("Mscale", 0.05, 200), ("eps_scale", 1e-3, 1.0), ("g_weak", 0.05, 20), ("gstar", 1, 427 / 4)]:
    f = lambda lx: math.log(chain({prm: BASE[prm] * math.exp(lx)})["eta"])
    grid = np.linspace(math.log(lo), math.log(hi), 41)
    vals = [f(x) for x in grid]
    root = None
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            root = optimize.brentq(f, grid[i], grid[i + 1], xtol=1e-6); break
    S2[prm] = None if root is None else math.exp(root)
    print(f"  {prm:10s} factor on base for eta=eta_obs: {S2[prm]}   (scan range x{lo}..x{hi}; eta at ends {math.exp(vals[0]):.3g}, {math.exp(vals[-1]):.3g})")
res["S2"] = S2

print("\n=== S3 ladder (kA = kB - 1) ===")
S3 = {}
for kB in [6, 7, 8, 9, 10]:
    r = chain({"kB": kB, "kA": kB - 1})
    S3[kB] = dict(eta=r["eta"], K=r["K"], M1=r["M1"], m3_eV=r["m3_light_eV"])
    print(f"  kB={kB}: eta/eta_obs={r['eta']:.4g}  K={r['K']:.3g}  M1={r['M1']:.3g} GeV  m3=Y0^2 v^2/M1 = {r['m3_light_eV']:.4g} eV")
res["S3"] = S3

print("\n=== S4 sign structure ===")
S4 = {}
for sg, s1, s2 in itertools.product([1, -1], repeat=3):
    r = chain({"gamma": 0.5 * sg, "E1": BASE["E1"] * s1, "E2": BASE["E2"] * s2})
    S4[f"gamma{sg:+d}_E1{s1:+d}_E2{s2:+d}"] = dict(eps_raw=r["eps"], eta_abs=r["eta"])
    print(f"  sign(gamma,E1,E2)=({sg:+d},{s1:+d},{s2:+d})  raw eps1 = {r['eps']:+.4e}  |eta|/eta_obs = {r['eta']:.6f}")
res["S4_patterns"] = S4

# chart: sin(delta_CP) for gamma = +-1/2 across the chamber (L10 chart, copied; repo untouched)
GAMMA = 0.5; E1 = math.sqrt(8 / 3); E2 = math.sqrt(8) / 3
T_M = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
T_D = np.array([[0, -1, 1], [-1, 1, 0], [1, 0, -1]], dtype=complex)
T_Q = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=complex)
PERM = (2, 1, 0)
def Hm(g, m, d, q):
    HB = np.array([[0, E1, -E1 - 1j * g], [E1, 0, -E2], [-E1 + 1j * g, -E2, 0]], dtype=complex)
    return HB + m * T_M + d * T_D + q * T_Q
def J_and_sind(H):
    w, V = np.linalg.eigh(H); o = np.argsort(w.real); V = V[:, o]; P = V[list(PERM), :]
    s13 = abs(P[0, 2]) ** 2; c13 = 1 - s13; s12 = abs(P[0, 1]) ** 2 / c13; s23 = abs(P[1, 2]) ** 2 / c13
    J = (P[0, 0] * np.conj(P[0, 1]) * np.conj(P[1, 0]) * P[1, 1]).imag
    den = math.sqrt(max(s12 * (1 - s12) * s23 * (1 - s23) * s13 * c13 * c13, 1e-300))
    return J, J / den, (s12, s13, s23)
rng = np.random.default_rng(1)
lo = np.array([-1.5, 0.0, 0.0]); hi = np.array([3.5, 2.6, 3.0])
n = 0; neg = 0; pos = 0; flip_ok = 0; near0 = 0
for _ in range(20000):
    m, d, q = lo + (hi - lo) * rng.random(3)
    if q + d - math.sqrt(8 / 3) < 0: continue
    Jp, sp, _a = J_and_sind(Hm(+GAMMA, m, d, q)); Jm, sm, _b = J_and_sind(Hm(-GAMMA, m, d, q))
    n += 1
    if abs(sp) < 1e-6: near0 += 1
    neg += sp < 0; pos += sp > 0
    flip_ok += (abs(sp + sm) < 1e-9)
print(f"  chamber samples {n}: gamma=+1/2 gives sin(dCP)<0 in {neg} ({neg/n:.3f}), >0 in {pos} ({pos/n:.3f}); gamma->-gamma flips exactly in {flip_ok}/{n}")
J0, s0, ang = J_and_sind(Hm(+GAMMA, 2 / 3, 0.933051059, 0.714501806))
print(f"  at the L10 pin (m,d,q)=(2/3,0.933051,0.714502): J={J0:+.5f}, sin(dCP)={s0:+.5f}, angles={tuple(round(a,4) for a in ang)}")
res["S4_chart"] = dict(n=n, frac_neg_at_gamma_plus=neg / n, frac_pos=pos / n, flip_exact=flip_ok, pin_sind=s0)

json.dump(res, open("t58_chain_test_out.json", "w"), indent=1, default=float)
print("\nwrote t58_chain_test_out.json")
