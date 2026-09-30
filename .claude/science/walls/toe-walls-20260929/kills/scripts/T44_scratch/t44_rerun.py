#!/usr/bin/env python3
"""T44 attack test: scoring, alpha_s scheme, category swap, look-elsewhere, commuting lemma.
Pre-registered in PREREG.md. Run: python3 t44_test.py  (writes results.txt, results.json)."""
import json, math, sys, io
import numpy as np

out = io.StringIO()
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

# ---------------------------------------------------------------- data (PDG 2024, review text in scratch)
D = dict(
    s12=(0.22501, 0.00068, 0.00068),
    s23=(0.04183, 0.00079, 0.00069),
    s13=(0.003732, 0.000090, 0.000085),
    delta_rad=(1.147, 0.026, 0.026),
    J=(3.12e-5, 0.13e-5, 0.12e-5),
    alpha_deg=(84.1, 4.5, 3.8),
    gamma_deg=(65.7, 3.0, 3.0),
    sin2b=(0.709, 0.011, 0.011),
)
lam_d = D['s12'][0]
A_d = D['s23'][0] / lam_d**2
r_d = D['s13'][0] / (D['s23'][0] * lam_d)
del_d = math.degrees(D['delta_rad'][0])
# relative sigma of r and A (independent-error approximation; s13,s23 correlation not in the review text)
relA = math.hypot(D['s23'][1] / D['s23'][0], 2 * D['s12'][1] / D['s12'][0])
relr = math.hypot(D['s13'][1] / D['s13'][0], D['s23'][1] / D['s23'][0], D['s12'][1] / D['s12'][0])
P("== data (PDG 2024) ==")
P(f"lambda={lam_d:.5f}  A={A_d:.4f} (PDG fit 0.826)  r=sqrt(rho^2+eta^2)={r_d:.4f}  delta={del_d:.2f} deg")
P(f"approx rel. errors: A {relA*100:.1f}%  r {relr*100:.1f}%")

def std_ckm(s12, s23, s13, d):
    c12, c23, c13 = (math.sqrt(1 - x * x) for x in (s12, s23, s13))
    e = np.exp(1j * d)
    return np.array([
        [c12 * c13, s12 * c13, s13 / e],
        [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])

def jarl(V):
    return float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))

P0 = 0.5934
alpha = 1 / (4 * math.pi * math.sqrt(P0))
# ---------------------------------------------------------------- S1 scoring
P("\n== S1 scoring of the atlas as a zero-theory-error formula ==")
lam_a = math.sqrt(alpha / 2); A_a = math.sqrt(2 / 3); r_a = 1 / math.sqrt(6)
del_a = math.degrees(math.atan(math.sqrt(5)))
s12a, s23a, s13a = lam_a, A_a * lam_a**2, A_a * lam_a**3 * r_a
Va = std_ckm(s12a, s23a, s13a, math.radians(del_a))
J_a = jarl(Va)
# unitarity-triangle angles from the atlas's exact standard matrix
def ut_angles(V):
    alpha_ = math.degrees(np.angle(-V[2, 0] * np.conj(V[2, 2]) / (V[0, 0] * np.conj(V[0, 2]))))
    beta_ = math.degrees(np.angle(-V[1, 0] * np.conj(V[1, 2]) / (V[2, 0] * np.conj(V[2, 2]))))
    gamma_ = math.degrees(np.angle(-V[0, 0] * np.conj(V[0, 2]) / (V[1, 0] * np.conj(V[1, 2]))))
    return alpha_ % 360, beta_ % 360, gamma_ % 360
alp_a, bet_a, gam_a = ut_angles(Va)
def pull(x, c, sp, sm):
    return (x - c) / (sp if x >= c else sm)
rows = [
    ("lambda=s12", lam_a, *D['s12']),
    ("s23", s23a, *D['s23']),
    ("s13", s13a, *D['s13']),
    ("delta deg", del_a, math.degrees(D['delta_rad'][0]), math.degrees(D['delta_rad'][1]), math.degrees(D['delta_rad'][2])),
    ("J", J_a, *D['J']),
    ("alpha_UT deg", alp_a, *D['alpha_deg']),
    ("gamma_UT deg", gam_a, *D['gamma_deg']),
]
res = {}
for n, x, c, sp, sm in rows:
    pl = pull(x, c, sp, sm)
    P(f"{n:14s} atlas {x:.6g}  PDG {c:.6g}  dev {100*(x/c-1):+.2f}%  pull {pl:+.2f} sigma")
    res[n] = dict(atlas=x, pdg=c, dev_pct=100 * (x / c - 1), pull=pl)
P(f"A_atlas={A_a:.4f} vs {A_d:.4f}: dev {100*(A_a/A_d-1):+.2f}%  pull {(A_a-A_d)/(relA*A_d):+.2f}")
P(f"r_atlas={r_a:.4f} vs {r_d:.4f}: dev {100*(r_a/r_d-1):+.2f}%  pull {(r_a-r_d)/(relr*r_d):+.2f}")
P(f"atlas beta_UT={bet_a:.2f} deg -> sin2beta={math.sin(math.radians(2*bet_a)):.4f} vs 0.709+-0.011")
res['lambda_pull'] = res['lambda=s12']['pull']
# how much theory error would make lambda pass at 1 sigma-equivalent
P(f"alpha_s needed for exact lambda: {2*lam_d**2:.5f} (atlas input {alpha:.5f}, {100*(alpha/(2*lam_d**2)-1):+.2f}%)")

# ---------------------------------------------------------------- S1b joint score (added after run 1; not pre-registered)
P("\n== S1b joint score of the four Wolfenstein numbers (lambda, A, rho_bar, eta_bar), correlations ignored ==")
from math import erf, sqrt as _sq
rho_b_a = (4 - alpha) / 24; eta_b_a = math.sqrt(5) * (4 - alpha) / 24     # atlas NLO barred apex (CKM_ATLAS note: 214-215)
pdg = dict(lam=(0.22501, 0.00068, 0.00068), A=(0.826, 0.016, 0.015), rho=(0.1591, 0.0094, 0.0094), eta=(0.3523, 0.0073, 0.0071))
atl = dict(lam=lam_a, A=A_a, rho=rho_b_a, eta=eta_b_a)
chi = 0.0; chi_th = 0.0
for k, (c, sp, sm) in pdg.items():
    pl = pull(atl[k], c, sp, sm); chi += pl * pl
    # add a 1% relative theory error on lambda only (quadrature) to see what would make it pass
    sp2 = math.hypot(sp, 0.01 * c) if k == 'lam' else sp; sm2 = math.hypot(sm, 0.01 * c) if k == 'lam' else sm
    pl2 = pull(atl[k], c, sp2, sm2); chi_th += pl2 * pl2
    P(f"  {k:4s} atlas {atl[k]:.5f} PDG {c:.5f}  pull {pl:+.2f}")
from math import exp
def chi2_sf4(x):  # survival function, 4 dof: exp(-x/2)(1+x/2)
    return exp(-x / 2) * (1 + x / 2)
P(f"  chi2 = {chi:.2f} (4 dof) -> p = {chi2_sf4(chi):.4f};   with a 1% theory error on lambda: chi2 = {chi_th:.2f} -> p = {chi2_sf4(chi_th):.3f}")
res['chi2_4'] = chi; res['p_chi2_4'] = chi2_sf4(chi)
cd = math.cos(math.radians(del_d))
P(f"  Thales check on data: cos(delta)={cd:.4f} vs r={r_d:.4f}: diff {cd-r_d:+.4f} (+-{r_d*relr:.4f} from r alone) ; |z-1/2| with PDG barred apex = {math.hypot(0.1591-0.5,0.3523):.4f} vs 0.5")

# ---------------------------------------------------------------- S2 alpha_s scheme
P("\n== S2 alpha_s(v): MS-bar 2-loop from alpha_s(MZ)=0.1180 ==")
def run(a0, mu0, mu1, nf, steps=20000):
    b0 = 11 - 2 * nf / 3; b1 = 102 - 38 * nf / 3
    def f(a): return -(b0 / (4 * math.pi)) * a**2 - (b1 / (4 * math.pi)**2) * a**3   # d a / d ln mu^2
    t0, t1 = math.log(mu0**2), math.log(mu1**2); h = (t1 - t0) / steps; a = a0
    for _ in range(steps):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a
v = 246.282818290129
for aMZ in (0.1171, 0.1180, 0.1189):
    a_mt = run(aMZ, 91.1876, 172.57, 5)
    a_v = run(a_mt, 172.57, v, 6)
    P(f"alpha_s(MZ)={aMZ}: alpha_s(mt)={a_mt:.5f} alpha_s(v)={a_v:.5f}  lambda=sqrt(alpha/2)={math.sqrt(a_v/2):.5f} ({100*(math.sqrt(a_v/2)/lam_d-1):+.2f}% vs PDG)")
    if aMZ == 0.1180: res['alpha_s_v_msbar'] = a_v
P(f"plaquette alpha_s(v)={alpha:.5f}; repo C1 claims MZ={0.118233}")
P("lambda sensitivity: d ln lambda / d ln alpha = 1/2 (exact)")

# ---------------------------------------------------------------- S3 category swap
P("\n== S3 put the 1+n weight on n=3 (generation space) instead of n=6 ==")
for n in (3, 6):
    r_n = 1 / math.sqrt(n); d_n = math.degrees(math.acos(1 / math.sqrt(n)))
    s13n = A_a * lam_a**3 * r_n
    P(f"n={n}: r={r_n:.4f} delta={d_n:.2f} deg |Vub|=s13={s13n:.6f}  vs PDG {D['s13'][0]}: {100*(s13n/D['s13'][0]-1):+.1f}%, pull {(s13n-D['s13'][0])/D['s13'][1]:+.1f} sigma ; delta pull {(d_n-del_d)/math.degrees(D['delta_rad'][1]):+.1f} sigma")
    res[f'swap_n{n}'] = dict(r=r_n, delta=d_n, s13=s13n, s13_dev_pct=100 * (s13n / D['s13'][0] - 1))

# ---------------------------------------------------------------- S4 look-elsewhere
P("\n== S4 look-elsewhere ==")
rng = np.random.default_rng(44)
N = 400_000
def grammar(S):
    lam = np.array(sorted({math.sqrt(alpha / a) for a in S}))
    Av = np.array(sorted({round(math.sqrt(p / q), 9) for p in S for q in S}))
    rv = np.array(sorted({1 / math.sqrt(b) for b in S}))
    dv = {c: math.degrees(math.acos(1 / math.sqrt(c))) for c in S}
    return lam, Av, rv, dv
def hits(vals, x, tau):
    # vals (G,), x (N,) -> bool (N,) any |v/x-1|<=tau
    m = np.zeros(x.shape, bool)
    for v_ in vals:
        m |= np.abs(v_ / x - 1) <= tau
    return m
def worlds(kind):
    if kind == 'broad':
        lam = np.exp(rng.uniform(math.log(0.05), math.log(0.5), N))
        A = rng.uniform(0.4, 1.4, N)
        r = np.exp(rng.uniform(math.log(0.1), 0.0, N))
        d = rng.uniform(20, 90, N)
    else:  # jitter around the real values
        f = lambda: np.exp(rng.uniform(-math.log(1.5), math.log(1.5), N))
        lam = lam_d * f(); A = A_d * f(); r = np.minimum(r_d * f(), 1.0); d = np.clip(del_d * f(), 20, 90)
    return lam, A, r, d
SETS = {'S_SM{2,3,6}': [2, 3, 6], 'S_6{1..6}': list(range(1, 7)), 'S_12{1..12}': list(range(1, 13))}
taus = [0.015, 0.03, 0.05]
table = {}
for kind in ('broad', 'jitter'):
    lam, A, r, d = worlds(kind)
    for sname, S in SETS.items():
        gl, gA, gr, gd = grammar(S)
        for tau in taus:
            for lam_tol_name, lam_tol in (('lam=tau', tau), ('lam=10%', 0.10)):
                hl = hits(gl, lam, lam_tol); hA = hits(gA, A, tau); hr = hits(gr, r, tau)
                hd = np.zeros(N, bool)
                for c, dv in gd.items():
                    if dv > 0: hd |= np.abs(dv / d - 1) <= tau
                p_ind = float(np.mean(hl & hA & hr & hd))
                # tied: same b for r and cos^2 delta (Thales tie of the atlas)
                ht = np.zeros(N, bool)
                for c in S:
                    ht |= (np.abs(1 / math.sqrt(c) / r - 1) <= tau) & (np.abs(gd[c] / d - 1) <= tau if gd[c] > 0 else False)
                p_tied = float(np.mean(hl & hA & ht))
                key = f"{kind}|{sname}|tau={tau}|{lam_tol_name}"
                table[key] = dict(p_indep=p_ind, p_tied=p_tied,
                                  slot=dict(lam=float(hl.mean()), A=float(hA.mean()), r=float(hr.mean()), delta=float(hd.mean())))
# real-data multiplicity
P("real-data hits (number of grammar members matching the PDG values), tau=3%:")
for sname, S in SETS.items():
    gl, gA, gr, gd = grammar(S); tau = 0.03
    nl = int(sum(abs(v_ / lam_d - 1) <= tau for v_ in gl)); nA = int(sum(abs(v_ / A_d - 1) <= tau for v_ in gA))
    nr = int(sum(abs(v_ / r_d - 1) <= tau for v_ in gr)); nd = int(sum(abs(dv / del_d - 1) <= tau for dv in gd.values() if dv > 0))
    P(f"  {sname}: lambda {nl}, A {nA}, r {nr}, delta {nd}  -> product {nl*nA*nr*nd}")
    table[f"real|{sname}"] = dict(lam=nl, A=nA, r=nr, delta=nd)
# with tau=3% is the atlas itself a member? (r deviation +2.9%)
P(f"atlas deviations: lambda {100*(lam_a/lam_d-1):+.2f}%  A {100*(A_a/A_d-1):+.2f}%  r {100*(r_a/r_d-1):+.2f}%  delta {100*(del_a/del_d-1):+.2f}%")
P("\nlook-elsewhere probabilities (fraction of mock worlds where SOME grammar member hits all four):")
P(f"{'null':7s} {'grammar':13s} {'tau':5s} {'lam tol':8s} {'p_indep':>9s} {'p_tied':>9s}   slot hit rates (lam,A,r,delta)")
for k, v in table.items():
    if k.startswith('real'): continue
    kind, sname, tau, lt = k.split('|')
    s = v['slot']
    P(f"{kind:7s} {sname:13s} {tau[4:]:5s} {lt:8s} {v['p_indep']:9.5f} {v['p_tied']:9.5f}   {s['lam']:.3f} {s['A']:.3f} {s['r']:.3f} {s['delta']:.3f}")

# ---------------------------------------------------------------- S5 commuting lemma
P("\n== S5 commuting lemma: H_u=f(K), H_d=g(K) give a permutation |V| ==")
worst = 0.0
rng2 = np.random.default_rng(5)
for _ in range(1000):
    X = rng2.normal(size=(3, 3)) + 1j * rng2.normal(size=(3, 3)); K = X + X.conj().T
    cu, cd = rng2.normal(size=3), rng2.normal(size=3)
    Hu = cu[0] * np.eye(3) + cu[1] * K + cu[2] * K @ K
    Hd = cd[0] * np.eye(3) + cd[1] * K + cd[2] * K @ K
    _, Uu = np.linalg.eigh(Hu); _, Ud = np.linalg.eigh(Hd)
    M = np.abs(Uu.conj().T @ Ud)
    worst = max(worst, float(np.max(np.minimum(M, 1 - M))))
P(f"max over 1000 cases of min(|V_ij|, 1-|V_ij|) = {worst:.2e}  (0 means every entry is 0 or 1)")
res['commuting_worst'] = worst

# ---------------------------------------------------------------- S6 runner inspection (static)
P("\n== S6 runner inspection ==")
P("scripts/frontier_ckm_atlas_axiom_closure.py:141-143  QUARK_BLOCK_DIM = 2*3 ; CENTER_EXCESS_WEIGHT = 1.0/QUARK_BLOCK_DIM ; ORTHOGONAL_PHASE_WEIGHT = 1-...")
P("scripts/...:244  delta_std = atan2(sqrt(ORTHOGONAL_PHASE_WEIGHT), sqrt(CENTER_EXCESS_WEIGHT)); :270-272 radial_theorem = 1/sqrt(6); rho, eta from those weights")
P("delta_A1 (support_delta, :255) appears only in scalar-compare outputs (:256, :274-275, :302)")

json.dump(dict(results=res, table=table), open('results.json', 'w'), indent=1, default=float)
open('results.txt', 'w').write(out.getvalue())
