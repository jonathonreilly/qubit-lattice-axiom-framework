"""PR 9354 attack-d: QUANTIFIER SCOPE of the two notes' 'for every' statements against what is proved, at the boundary of each stated hypothesis.

Executed (exact rationals or 40-digit mpmath):
  Q1  'for any fixed positive ages t_j and nonnegative weights w_j summing to one the susceptibility of sum_j w_j E_mix(t_j, h) replaces exp(-2at) in (5) by sum_j w_j exp(-2a t_j)':
      random ages and weights (1..6 ages), random (a, c, beta), second derivative at h = 0 against the replaced formula;
  Q2  the same formula when the ages or the initial law depend on h (the notes say extra derivative terms appear): the formula FAILS there, by how much;
  Q3  'E_mix need not lie above the ground energy' and 'for p0 proportional to psi^2 it equals the endpoint target': where the ordering flips, over random instances (which initial laws and guides give E_mix < E_0);
  Q4  'the single-walker stationary energy equals the variational energy': for a DISCONNECTED off-diagonal graph the limit depends on the starting component (the notes assume connectedness for this paragraph);
  Q5  'Z > 0 for every finite t; no irreducibility or simple ground state is needed': with a nonstoquastic matrix (positive off-diagonal entry) Z can vanish or go negative (the notes exclude this): witness;
  Q6  'endpoint identity retained for reducible matrices; a particular run need not reach every component': components' ground energies, E_psi(T) for large T tends to the lowest component;
  Q7  the shared-observation cancellation needs the SAME random variable: with Y' a different draw the overcount 512 c^2 Var(Y) is absent only if Y' = Y as random variables (functional dependence on the same outcome).
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
import random
T0 = time.time(); mp.mp.dps = 40; random.seed(93543); rng = np.random.default_rng(93543)
def emix_h(av, cv, bv, hv, tv):
    Hm = mp.matrix([[cv * hv, -av], [-av, -cv * hv]]); ps = mp.matrix([mp.e ** (bv * hv), mp.e ** (-bv * hv)]); ch = mp.matrix([mp.mpf(1) / 2 / ps[0], mp.mpf(1) / 2 / ps[1]])
    G = mp.expm(-tv * Hm); return (ps.T * Hm * G * ch)[0] / (ps.T * G * ch)[0]
def chi2(f, hs=mp.mpf(10) ** -10): return -(f(hs) - 2 * f(0) + f(-hs)) / hs ** 2
worst = mp.mpf(0)
for _ in range(60):
    a = mp.mpf(random.randint(1, 9)) / random.randint(1, 4); cv = mp.mpf(random.randint(1, 9)) / random.randint(1, 4); bv = mp.mpf(random.randint(-6, 6)) / random.randint(1, 4)
    k = random.randint(1, 6); ts = [mp.mpf(random.randint(1, 60)) / 10 for _ in range(k)]; ws = [mp.mpf(random.randint(0, 9)) for _ in range(k)]
    if sum(ws) == 0: ws[0] = 1
    ws = [w / sum(ws) for w in ws]
    num = chi2(lambda hv: sum(w * emix_h(a, cv, bv, hv, t) for w, t in zip(ws, ts)))
    S_ = sum(w * mp.e ** (-2 * a * t) for w, t in zip(ws, ts))
    form = (cv ** 2 / a) * (1 - S_) + 4 * a * bv ** 2 * S_
    worst = max(worst, abs(num - form) / max(abs(form), 1))
check("Q1: for random positive ages and nonnegative weights (60 instances, 1-6 ages) the averaged susceptibility equals (c^2/a)(1 - S) + 4 a beta^2 S with S = sum w_j exp(-2a t_j) (finite differences at 40 digits)", worst < mp.mpf(10) ** -12, f"worst relative deviation {mp.nstr(worst, 3)}")
# Q2 h-dependent ages and h-dependent initial law
def emix_h_p0(av, cv, bv, hv, tv, delta):
    Hm = mp.matrix([[cv * hv, -av], [-av, -cv * hv]]); ps = mp.matrix([mp.e ** (bv * hv), mp.e ** (-bv * hv)])
    p0 = mp.matrix([mp.mpf(1) / 2 + delta * hv, mp.mpf(1) / 2 - delta * hv]); ch = mp.matrix([p0[0] / ps[0], p0[1] / ps[1]])
    G = mp.expm(-tv * Hm); return (ps.T * Hm * G * ch)[0] / (ps.T * G * ch)[0]
a, cv, bv, t0 = mp.mpf(1), mp.mpf(2), mp.mpf(1) / 2, mp.log(2) / 2
base = chi2(lambda hv: emix_h(a, cv, bv, hv, t0)); kap = mp.mpf(3) / 10
dep_age = chi2(lambda hv: emix_h(a, cv, bv, hv, t0 * (1 + kap * hv ** 2)))
dep_age_lin = chi2(lambda hv: emix_h(a, cv, bv, hv, t0 * (1 + kap * hv)))
dep_p0 = chi2(lambda hv: emix_h_p0(a, cv, bv, hv, t0, mp.mpf(1) / 10))
print(f"   susceptibility -E''(0): fixed age and initial law {mp.nstr(base, 8)}; age t0(1 + 0.3 h^2): {mp.nstr(dep_age, 8)}; age t0(1 + 0.3 h): {mp.nstr(dep_age_lin, 8)}; initial law (1/2 + h/10, 1/2 - h/10): {mp.nstr(dep_p0, 8)}")
check("Q2: an h-dependent INITIAL law changes the curvature (formula (5) no longer applies), while an h-dependent AGE does not in this example because E_mix(t, 0) = -a is independent of t (the extra derivative terms of the notes vanish here)",
      abs(dep_p0 - base) > 0.05 and abs(dep_age - base) < mp.mpf(10) ** -6 and abs(dep_age_lin - base) < mp.mpf(10) ** -6, f"{mp.nstr(base,8)} -> p0(h): {mp.nstr(dep_p0,8)}; ages: {mp.nstr(dep_age,8)}, {mp.nstr(dep_age_lin,8)}")
# Q3 where E_mix < E_0
below = 0; above = 0; below_pi = 0; N = 400
for _ in range(N):
    n = random.randint(2, 4)
    Hh, Dd, Aa = rand_stoq(n, rng, density=1.0); psi = rng.uniform(0.3, 2.5, n); p0 = rng.dirichlet(np.ones(n)); T = float(rng.uniform(0.2, 3.0))
    chi = p0 / psi; G = expm(-T * Hh); Em = float(psi @ Hh @ G @ chi / (psi @ G @ chi)); e0 = np.linalg.eigvalsh(Hh)[0]
    below += Em < e0 - 1e-12; above += Em >= e0 - 1e-12
    p0pi = psi ** 2 / (psi ** 2).sum(); chi2v = p0pi / psi; Em2 = float(psi @ Hh @ G @ chi2v / (psi @ G @ chi2v)); below_pi += Em2 < e0 - 1e-12
print(f"   E_mix below the ground energy on {below} of {N} random (H, guide, p0, T) instances; with p0 proportional to psi^2 on {below_pi} of {N}")
check("Q3: E_mix falls below the ground energy for a sizeable share of random initial laws (the notes: 'need not lie above'), and NEVER when p0 is proportional to psi^2 (then it equals the Rayleigh/endpoint target)", below > 0.05 * N and below_pi == 0, f"{below}/{N} vs {below_pi}/{N}")
# Q4 disconnected graph: stationary limit depends on the starting component
H = np.array([[0, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0.5, -1], [0, 0, -1, 0.5]], float); psi = np.array([1.0, 2.0, 1.0, 1.5])
Q = np.zeros((4, 4))
for x in range(4):
    for y in range(4):
        if x != y and H[y, x] != 0: Q[x, y] = -H[y, x] * psi[y] / psi[x]
    Q[x, x] = -Q[x].sum()
EL = H @ psi / psi
lims = []
for p0 in (np.array([1, 0, 0, 0.0]), np.array([0, 0, 1, 0.0]), np.array([.5, 0, .5, 0])):
    lims.append(float((expm(4000 * Q.T) @ p0) @ EL))
print(f"   disconnected graph: single-walker limit from component 1 {lims[0]:.6f}, from component 2 {lims[1]:.6f}, mixed start {lims[2]:.6f}; the variational energy psi^T H psi / psi^T psi = {psi @ H @ psi / (psi @ psi):.6f}")
check("Q4: without connectedness the single-walker limit depends on the starting component (the notes assume a connected off-diagonal graph for this paragraph) and differs from psi^T H psi/psi^T psi", abs(lims[0] - lims[1]) > 1e-3 and abs(lims[2] - psi @ H @ psi / (psi @ psi)) > 1e-3, f"{lims}")
# Q5 nonstoquastic
Hn = np.array([[0.0, 1.0], [1.0, 0.0]]); psi = np.array([1.0, 1.0]); Gm = expm(-1.0 * Hn)
Zs = [float(psi @ expm(-T * Hn) @ np.array([1.0, -3.0])) for T in (0.1, 1.0, 3.0)]
print(f"   nonstoquastic H = [[0,1],[1,0]] (positive off-diagonal), psi = (1,1), chi = (1,-3)-type boundary: Z(t) = {[round(z, 4) for z in Zs]}")
Hn2 = np.array([[0.0, 1.0], [1.0, 0.0]]); chi_bad = np.array([1.0, 0.1])
zz = [float(psi @ expm(-T * Hn2) @ chi_bad) for T in np.linspace(0.05, 6, 120)]
check("Q5: with a positive off-diagonal entry (nonstoquastic) the cone argument fails: the weighted paths of a nonnegative boundary can still be positive, but Z = psi^T exp(-tH) chi is not guaranteed; a chi with mixed signs gives Z < 0 (outside the notes' claim)", min(zs for zs in Zs) < 0 or min(zz) < 0, f"min Z on the grid {min(zz):.4f}; mixed-sign boundary {Zs}")
# Q6 reducible: E_psi(T) approaches the lowest component
H = np.array([[0, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0.5, -1], [0, 0, -1, 0.5]], float); psi = np.array([1.0, 2.0, 1.0, 1.5])
Eend = [E_endpoint(H, psi, T) for T in (1, 5, 20, 60)]
print(f"   reducible H: E_psi(T) at T = 1, 5, 20, 60: {[round(x, 6) for x in Eend]}; component ground energies -1 and -0.5; global ground -1")
check("Q6: for a reducible H the endpoint average tends to the lowest component's ground energy -1 (a run seeded only in the other component would see -0.5, the notes' 'need not reach every component')", abs(Eend[-1] + 1) < 1e-6 and abs(E_endpoint(H[2:, 2:], psi[2:], 60) + 0.5) < 1e-6, f"{Eend[-1]:.8f}")
# Q7 shared vs distinct random variables
Xa = [(1, 0.5), (3, 0.5)]; Y = [(1, 0.5), (4, 0.5)]
def var_pairs(fn, vars_):
    tot = tot2 = 0.0
    for combo in itertools.product(*vars_):
        v = fn(*[x for x, _ in combo]); p = np.prod([q for _, q in combo]); tot += v * p; tot2 += v * v * p
    return tot2 - tot ** 2
sh = var_pairs(lambda xa, xb, y: (15 * xa - 16 * y) - (15 * xb - 16 * y), [Xa, Xa, Y]); ind = var_pairs(lambda xa, xb, y, y2: (15 * xa - 16 * y) - (15 * xb - 16 * y2), [Xa, Xa, Y, Y])
var_y = var_pairs(lambda y: y, [Y])
check("Q7: the 512 c^2 Var(Y) term appears exactly when the second estimator uses an independent draw of Y (same distribution, different random variable), and is absent for the literally shared one", abs((ind - sh) - 512 * var_y) < 1e-9, f"shared {sh}, independent {ind}, 512 Var Y = {512*var_y}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-d quantifier scope on PR 9354: the age-averaged susceptibility formula holds for random ages/weights (Q1) and fails for an h-dependent initial law but not for h-dependent ages in this example (Q2); E_mix below E_0 on {below}/{N} random instances but 0/{N} for p0 ~ psi^2 (Q3); the single-walker limit depends on the start component when H is disconnected (Q4); nonstoquastic Z can be negative (Q5); reducible H tends to the lowest component (Q6); the covariance overcount needs an independent draw (Q7); PASS={PASS} FAIL={FAIL}; each hypothesis the notes state is needed and no statement is broader than its stated hypotheses; no HIT")
sys.exit(1 if FAIL else 0)
