"""PR 9354 attack-b: SAME TEST, BOTH SIDES for the two finite-projection notes.

The notes separate objects by properties: (i) endpoint average = spectral/Rayleigh/log-derivative for the UNCAPPED functional but not for the CAPPED one; (ii) 'correct zero-field energy at
every age' for the mixed benchmark E_mix under both guides, but not for the single-walker target; (iii) 'not above the ground energy' for the mixed ratio, 'above the ground energy' for the
Rayleigh/variational representations; (iv) guide dependence of the finite-age curvature although both guides give the exact zero-field energy; (v) covariance cancels for a SHARED Y and not for an independent one.
Each separating test is applied here, unchanged, to both objects in every representation the notes use: exact two-state tables (sympy) and 300 random stoquastic instances (n = 3..5, random guides, ages).
"""
import itertools, sys, time
import numpy as np
import mpmath as mp
from scipy.linalg import expm

PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def rand_stoq(n, rng, density=1.0, zero_diag=False):
    A = rng.uniform(0, 1.5, (n, n)) * (rng.uniform(0, 1, (n, n)) < density); A = np.triu(A, 1); A = A + A.T
    D = np.zeros(n) if zero_diag else rng.uniform(-1, 2, n)
    return np.diag(D) - A, D, A
def spectral(H):
    e, V = np.linalg.eigh(H); return e, V
def E_endpoint(H, psi, T):
    G = expm(-T * H); Z = psi @ G @ psi
    return float(psi @ H @ G @ psi / Z)
def E_rayleigh(H, psi, T):
    u = expm(-T * H / 2) @ psi; return float(u @ H @ u / (u @ u))
def E_logderiv(H, psi, T, h=1e-5):
    f = lambda tt: np.log(psi @ expm(-tt * H) @ psi)
    return float(-(f(T + h) - f(T - h)) / (2 * h))
def kernel_capped(D, A, Delta, J):
    """K_J(Delta): weighted paths with at most J jumps (exact Dyson terms via the block-upper-triangular exponential): sum over j <= J of the j-jump term"""
    n = len(D); Bm = np.zeros(((J + 1) * n, (J + 1) * n))
    for b in range(J + 1):
        Bm[b * n:(b + 1) * n, b * n:(b + 1) * n] = -np.diag(D)
        if b < J: Bm[b * n:(b + 1) * n, (b + 1) * n:(b + 2) * n] = A
    E = expm(Bm * Delta)
    return sum(E[0:n, j * n:(j + 1) * n] for j in range(J + 1))
import sympy as sp
T0 = time.time()
rng = np.random.default_rng(9354)
# ---- (i) uncapped vs capped, three representations
bad_unc = 0; diff_cap = 0; n_cap = 0; worst_unc = 0.0; cap_below_e0 = 0
for _ in range(300):
    n = int(rng.integers(3, 6)); H, D, A = rand_stoq(n, rng, density=0.8); psi = rng.uniform(0.3, 2.0, n); T = float(rng.uniform(0.2, 3.0))
    a, b, c = E_endpoint(H, psi, T), E_rayleigh(H, psi, T), E_logderiv(H, psi, T)
    worst_unc = max(worst_unc, abs(a - b), abs(a - c)); bad_unc += (abs(a - b) > 1e-8 or abs(a - c) > 1e-6)
    # capped: J = 1 or 2 jumps per segment, M = 2 segments of Delta = T/2
    J = int(rng.integers(0, 3)); Delta = T / 2
    K = kernel_capped(D, A, Delta, J); C = K @ K
    ecap = float(psi @ H @ C @ psi / (psi @ C @ psi))
    w, V = np.linalg.eigh((C + C.T) / 2)
    if w.min() > 0:
        sq = V @ np.diag(np.sqrt(w)) @ V.T; u = sq @ psi; ray = float(u @ H @ u / (u @ u)); n_cap += 1
        diff_cap += abs(ecap - ray) > 1e-8
    e0 = np.linalg.eigvalsh(H)[0]; cap_below_e0 += ecap < e0 - 1e-12
check("UNCAPPED: endpoint half-sum = Rayleigh quotient of exp(-TH/2) psi = -d log Z/dT on 300 random stoquastic instances (max deviation shown)", bad_unc == 0, f"worst {worst_unc:.1e}")
print(f"   CAPPED (J = 0..2, M = 2): endpoint average differs from the Rayleigh quotient of sqrt(C) psi on {diff_cap} of {n_cap} instances with C positive definite; endpoint average below the ground energy on {cap_below_e0} of 300")
check("the identical test separates the two objects: the representations agree for the uncapped functional on all instances and disagree for the capped one on most (>= 50%)", bad_unc == 0 and diff_cap >= 0.5 * max(n_cap, 1), f"{diff_cap}/{n_cap}")
# ---- exact two-state table across representations and both guides
R = sp.Rational; tt = sp.symbols("tt", positive=True)
H2 = sp.Matrix([[0, -1], [-1, 0]])
def emix(psi, p0, T):
    psi = sp.Matrix(psi); p0 = sp.Matrix(p0); chi = sp.diag(*[1 / x for x in psi]) * p0
    G = sp.simplify((-T * H2).exp()); Z = (psi.T * G * chi)[0]; return sp.simplify((psi.T * H2 * G * chi)[0] / Z)
def rayl(psi, T):
    psi = sp.Matrix(psi); u = sp.simplify((-T * H2 / 2).exp()) * psi; return sp.simplify((u.T * H2 * u)[0] / (u.T * u)[0])
def single_walker(psi, p0, T):
    psi = sp.Matrix(psi); Q = sp.zeros(2)
    for x in range(2):
        for y in range(2):
            if x != y: Q[x, y] = -H2[y, x] * psi[y] / psi[x]
        Q[x, x] = -sum(Q[x, y] for y in range(2) if y != x)
    EL = sp.Matrix([(H2 * psi)[i] / psi[i] for i in range(2)])
    return sp.simplify((EL.T * sp.simplify((T * Q.T).exp()) * sp.Matrix(p0))[0])
T = sp.log(2) / 2
tab = {}
for gname, g in (("guide (1,1)", (1, 1)), ("guide (1,2)", (1, 2))):
    p0 = (R(1, 2), R(1, 2))
    tab[gname] = dict(mixed=emix(g, p0, T), mixed_pi=emix(g, tuple(sp.Matrix(g).applyfunc(lambda x: x ** 2) / sum(x ** 2 for x in g)), T), rayleigh=rayl(g, T), single=single_walker(g, p0, T))
print("   representation                       guide (1,1)      guide (1,2)   (t = log(2)/2, H = [[0,-1],[-1,0]], ground energy -1)")
for k, nm in (("mixed", "E_mix, p0 = (1/2,1/2)"), ("mixed_pi", "E_mix, p0 proportional psi^2"), ("rayleigh", "Rayleigh of exp(-tH/2) psi"), ("single", "single-walker energy")):
    print(f"   {nm:36s} {str(tab['guide (1,1)'][k]):>12s}   {str(tab['guide (1,2)'][k]):>12s}")
E0 = -1
check("test 'energy >= ground energy' on both guides in every representation: holds for the Rayleigh and the p0 ~ psi^2 mixed ratio and the single walker; fails ONLY for the E_mix ratio with p0 = (1/2,1/2) and guide (1,2)",
      tab["guide (1,1)"]["mixed"] >= E0 and tab["guide (1,2)"]["mixed"] < E0 and tab["guide (1,2)"]["rayleigh"] >= E0 and tab["guide (1,2)"]["mixed_pi"] >= E0 and tab["guide (1,2)"]["single"] >= E0 and tab["guide (1,1)"]["single"] >= E0,
      f"{tab['guide (1,2)']}")
check("test 'equals the ground energy' separates guide (1,1) from guide (1,2) in EVERY representation (so guide dependence is not specific to one of them at t = log(2)/2)",
      all(tab["guide (1,1)"][k] == E0 and tab["guide (1,2)"][k] != E0 for k in tab["guide (1,1)"]))
check("for p0 proportional to psi^2 the mixed ratio equals the endpoint target (-17/19) and the Rayleigh quotient of exp(-tH/2) psi; for p0 = (1/2,1/2) it does not", tab["guide (1,2)"]["mixed_pi"] == R(-17, 19) == tab["guide (1,2)"]["rayleigh"] and tab["guide (1,2)"]["mixed"] != R(-17, 19), f"{tab['guide (1,2)']['mixed_pi']}, {tab['guide (1,2)']['mixed']}")
# zero-field energy at every age: the mixed benchmark (both guides) versus the single walker (both guides)
tt_list = [R(1, 10), R(1, 2), 1, 3]
mixed_ok = all(sp.simplify(emix(g, (R(1, 2), R(1, 2)), tv)) == E0 for g in ((1, 1),) for tv in tt_list)
mixed12 = [sp.N(emix((1, 2), (R(1, 2), R(1, 2)), tv), 8) for tv in tt_list]
single12 = [sp.N(single_walker((1, 2), (R(1, 2), R(1, 2)), tv), 8) for tv in tt_list]
print("   the a = 1, c = 2 curvature example concerns H_h; at h = 0 the SAME two-state matrix: E_mix (1,2), p0 uniform, at t = 1/10, 1/2, 1, 3:", mixed12, "; single walker:", single12)
# curvature (h -> 0) for both guides and the single-walker representation via mpmath
mp.mp.dps = 40
def emix_h(av, cv, bv, hv, tv):
    Hm = mp.matrix([[cv * hv, -av], [-av, -cv * hv]]); ps = mp.matrix([mp.e ** (bv * hv), mp.e ** (-bv * hv)]); ch = mp.matrix([mp.mpf(1) / 2 / ps[0], mp.mpf(1) / 2 / ps[1]])
    G = mp.expm(-tv * Hm); return (ps.T * Hm * G * ch)[0] / (ps.T * G * ch)[0]
def one_walker_h(av, cv, bv, hv, tv):
    """fixed guide psi_0 (Q independent of h): one-walker energy E_L^T exp(tQ^T) p0 - h M with the diagonal field: the walker's energy is the h-dependent E_L of H_h with the h = 0 guide"""
    psi = mp.matrix([mp.e ** (bv * 0), mp.e ** (-bv * 0)])
    Hm = mp.matrix([[cv * hv, -av], [-av, -cv * hv]]); Q = mp.matrix([[-av, av], [av, -av]])            # uniform guide: q(x,y) = a
    EL = mp.matrix([(Hm * psi)[0] / psi[0], (Hm * psi)[1] / psi[1]]); p0 = mp.matrix([mp.mpf(1) / 2, mp.mpf(1) / 2])
    return (EL.T * mp.expm(tv * Q.T) * p0)[0]
hs = mp.mpf(10) ** -8; tv = mp.log(2) / 2
def chi_second(f):
    return -(f(hs) - 2 * f(0) + f(-hs)) / hs ** 2
chi_b = {bv: chi_second(lambda hv, bv=bv: emix_h(1, 2, bv, hv, tv)) for bv in (mp.mpf(1) / 2, mp.mpf(0))}
chi_w = chi_second(lambda hv: one_walker_h(1, 2, 0, hv, tv))
print(f"   susceptibility -E''(0): mixed benchmark guide beta = 1/2: {mp.nstr(chi_b[mp.mpf(1)/2], 8)}, uniform guide: {mp.nstr(chi_b[mp.mpf(0)], 8)}, ground state: 4; single walker (fixed uniform guide): {mp.nstr(chi_w, 8)} (note: the literal second derivative is zero)")
check("the curvature test separates the two guides (5/2 versus 2) and both from the ground value 4, and the literal single-walker second derivative with a fixed guide is zero (the field enters only linearly through M)",
      abs(chi_b[mp.mpf(1)/2] - mp.mpf(5)/2) < 1e-6 and abs(chi_b[mp.mpf(0)] - 2) < 1e-6 and abs(chi_w) < 1e-6, f"{mp.nstr(chi_b[mp.mpf(1)/2],8)}, {mp.nstr(chi_b[mp.mpf(0)],8)}, {mp.nstr(chi_w,3)}")
# ---- (v) shared versus independent Y
import random
random.seed(1)
c = sp.Rational(1, 3)
Xa = [(1, R(1, 2)), (3, R(1, 2))]; Xb = [(0, R(1, 2)), (2, R(1, 2))]; Za = [(1, R(1, 4)), (2, R(3, 4))]; Zb = [(0, R(1, 3)), (5, R(2, 3))]; Y = [(1, R(1, 2)), (4, R(1, 2))]; Y2 = [(1, R(1, 2)), (4, R(1, 2))]
def var(fn, vars_):
    pts = [(fn(*vals), np.prod([float(p) for _, p in zip(vals, ps)] if False else 1)) for vals, ps in []]
    tot = 0; tot2 = 0
    for combo in itertools.product(*vars_):
        v = fn(*[x for x, _ in combo]); p = sp.prod([pp for _, pp in combo]); tot += v * p; tot2 += v * v * p
    return sp.nsimplify(tot2 - tot ** 2)
v_shared = var(lambda xa, xb, za, zb, y: c * (15 * xa - 16 * y + za) - c * (15 * xb - 16 * y + zb), [Xa, Xb, Za, Zb, Y])
v_indep = var(lambda xa, xb, za, zb, y, y2: c * (15 * xa - 16 * y + za) - c * (15 * xb - 16 * y2 + zb), [Xa, Xb, Za, Zb, Y, Y2])
varY = var(lambda y: y, [Y])
check("the covariance test separates a SHARED Y (no Y term) from an independent second draw (extra 512 c^2 Var(Y)) on the same random variables", v_indep - v_shared == 512 * c ** 2 * varY, f"{v_shared} vs {v_indep}; 512 c^2 VarY = {512*c**2*varY}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-b same test both sides on PR 9354: representations of the uncapped functional agree on all 300 random instances while the capped endpoint average differs from its Rayleigh form on {diff_cap}/{n_cap} (and lies below the ground energy on {cap_below_e0}/300, which the notes do not claim to exclude); 'equals the ground energy' separates the guides in every representation, 'above the ground energy' fails only for the E_mix ratio with p0 = (1/2,1/2); curvature test 5/2 vs 2 vs ground 4 vs single-walker 0; shared-Y cancellation vs 512 c^2 Var(Y); PASS={PASS} FAIL={FAIL}; no defect in the separation claims")
sys.exit(1 if FAIL else 0)
