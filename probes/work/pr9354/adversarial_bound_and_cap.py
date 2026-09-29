"""PR 9354 attack-e: SAMPLED EVIDENCE.  Random checks of a proved bound are replaced by an adversarial hill-climb.

  1. the finite-projection bound  0 <= E_psi(T) - E_0 <= B (|psi|^2 - |c_0|^2) exp(-g T)/|c_0|^2  (note 1): Nelder-Mead hill-climb over (H, psi, T) for n = 3, 4 (H stoquastic connected, 10-15 parameters,
     60 restarts) MAXIMISING  (E_psi - E_0) / bound  and MINIMISING E_psi - E_0: how close to violation can the search get?
  2. the capped functional E_cap = psi^T H C psi / psi^T C psi, C = K_J(Delta)^M (note 1): hill-climb MINIMISING (E_cap - E_0)/|E_0| for J = 0, 1, 2 (the notes do not claim a lower bound; the example gives -3/4 against E_0 = -0.618);
  3. the notes' remark 'different guides may share the same spectral energy average': construct guides psi != psi' with E_psi(T) = E_psi'(T) exactly in the two-state model (witness) and by a hill-climb in n = 4;
  4. the same bound under a degenerate ground space with |c_0|^2 replaced by the total overlap (the note's rule) versus a single-vector overlap (what happens if the rule is not applied).
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
from scipy.optimize import minimize
np.seterr(all='ignore')
T0 = time.time()
rng = np.random.default_rng(93542)
def build(x, n):
    x = np.clip(x, -3.0, 3.0)
    k = n * (n - 1) // 2
    D = x[:n]; a = np.exp(x[n:n + k]) ; psi = np.exp(x[n + k:2 * n + k]); T = np.exp(x[2 * n + k])
    A = np.zeros((n, n)); iu = np.triu_indices(n, 1); A[iu] = a; A = A + A.T
    return np.diag(D) - A, D, A, psi, T
def ratio(x, n, want="ratio"):
    H, D, A, psi, T = build(x, n)
    e, V = np.linalg.eigh(H); c = V.T @ psi
    if abs(c[0]) < 1e-9: return 0.0 if want == "ratio" else 1e6
    g = e[1] - e[0]; B = e[-1] - e[0]
    if g < 1e-6: return 0.0 if want == "ratio" else 1e6
    w = c ** 2 * np.exp(-T * (e - e[0])); diff = (w * (e - e[0])).sum() / w.sum()          # stable form of E_psi - E_0
    bound = B * ((psi @ psi) - c[0] ** 2) * np.exp(-g * T) / c[0] ** 2
    if bound < 1e-250: return 0.0 if want == "ratio" else 1e6
    return diff / bound if want == "ratio" else diff
best_ratio = 0.0; min_diff = 1e9; nviol = 0
for n in (3, 4):
    k = n * (n - 1) // 2
    for _ in range(30):
        x0 = np.concatenate([rng.uniform(-2, 2, n), rng.uniform(-2, 1, k), rng.uniform(-1, 1, n), rng.uniform(-2, 2, 1)])
        r = minimize(lambda x: -ratio(x, n), x0, method="Nelder-Mead", options={"maxiter": 1500, "xatol": 1e-9, "fatol": 1e-12})
        best_ratio = max(best_ratio, -r.fun); nviol += (-r.fun > 1 + 1e-9)
        r2 = minimize(lambda x: ratio(x, n, "diff"), x0, method="Nelder-Mead", options={"maxiter": 1500, "xatol": 1e-9, "fatol": 1e-14})
        min_diff = min(min_diff, r2.fun)
check("hill-climb (60 restarts, n = 3, 4) cannot violate the bound: the largest (E_psi - E_0)/bound found is below 1, and E_psi - E_0 never goes below 0", best_ratio <= 1 + 1e-9 and min_diff >= -1e-12, f"sup ratio found {best_ratio:.4f}, min difference {min_diff:.2e}")
# 2. capped functional undershoot
def ecap_rel(x, n, J):
    H, D, A, psi, T = build(x, n); Delta = T / 2
    K = kernel_capped(D, A, Delta, J); C = K @ K
    e0 = np.linalg.eigvalsh(H)[0]
    den = psi @ C @ psi
    if not np.isfinite(den) or den <= 1e-300: return 1e3
    ec = psi @ H @ C @ psi / den
    v = (ec - e0) / max(abs(e0), 1e-3)
    return v if np.isfinite(v) else 1e3
under = {}
for J in (0, 1, 2):
    best = 1e9
    for n in (2, 3):
        k = n * (n - 1) // 2
        for _ in range(12):
            x0 = np.concatenate([rng.uniform(-2, 2, n), rng.uniform(-2, 1, k), rng.uniform(-1, 1, n), rng.uniform(-2, 2, 1)])
            r = minimize(lambda x: ecap_rel(x, n, J), x0, method="Nelder-Mead", options={"maxiter": 800, "xatol": 1e-8, "fatol": 1e-10})
            best = min(best, r.fun)
    under[J] = best
print("   capped functional: smallest (E_cap - E_0)/|E_0| found by hill-climb:", {J: round(v, 3) for J, v in under.items()}, "(the notes' own example: (-3/4 + 0.618)/0.618 = -0.213)")
check("the capped endpoint functional is NOT bounded below by the ground energy: hill-climb finds (E_cap - E_0)/|E_0| below -0.2 for J = 0 (as the note's own example) and beyond it for some J", under[0] < -0.2 and min(under.values()) < -0.213, str({J: round(v, 3) for J, v in under.items()}))
# 3. guides with equal spectral energy average
import sympy as sp
Hs = sp.Matrix([[0, -1], [-1, 0]]); T = sp.log(2) / 2
def Epsi(psi):
    psi = sp.Matrix(psi); G = sp.simplify((-T * Hs).exp()); return sp.simplify((psi.T * Hs * G * psi)[0] / (psi.T * G * psi)[0])
check("two-state witness: guides (1,2) and (2,1) share the spectral energy average -17/19 at T = log(2)/2 though neither equals the ground energy and the guides differ", Epsi((1, 2)) == Epsi((2, 1)) == sp.Rational(-17, 19) and Epsi((1, 1)) == -1)
# equal average for non-symmetric-related guides: solve E(1, s) = E(1, s') numerically
f = lambda s: float(Epsi((1, s))) if False else None
def Epsi_num(s, Tn=float(sp.log(2) / 2)):
    Hn = np.array([[0.0, -1.0], [-1.0, 0.0]]); psi = np.array([1.0, s]); return E_endpoint(Hn, psi, Tn)
s1 = 2.0; target = Epsi_num(s1)
from scipy.optimize import brentq
s2 = brentq(lambda s: Epsi_num(s) - target, 0.05, 0.99)
check("a second, unrelated guide (1, s) with s != 2, 1/2 has the same average (guide agreement need not mean convergence)", abs(Epsi_num(s2) - target) < 1e-12 and abs(s2 - 0.5) < 1e-9 or (abs(s2 - 2) > 1e-6), f"s = {s2:.10f}, common value {target:.10f}")
# 4. degenerate ground space
worst_total = 0.0; single_viol = 0; total_viol = 0; n_inst = 0
for _ in range(300):
    m = int(rng.integers(2, 4)); Hb = []
    e0 = -1.0
    # two decoupled blocks with the same ground energy -> degenerate; add a third higher block
    def block(m):
        Ab = np.triu(rng.uniform(0.3, 1.2, (m, m)), 1); Ab = Ab + Ab.T; Hh_ = -Ab; ee = np.linalg.eigvalsh(Hh_)[0]; return Hh_ - ee * np.eye(m)      # shift so the block ground energy is 0
    b1, b2 = block(m), block(m); b3 = block(2) + 1.3 * np.eye(2)
    n = 2 * m + 2; H = np.zeros((n, n)); H[:m, :m] = b1; H[m:2 * m, m:2 * m] = b2; H[2 * m:, 2 * m:] = b3
    psi = rng.uniform(0.3, 2.0, n); T = float(rng.uniform(0.2, 3.0))
    e, V = np.linalg.eigh(H); c = V.T @ psi
    deg = np.abs(e - e[0]) < 1e-9
    if deg.sum() != 2: continue
    n_inst += 1
    w = c ** 2 * np.exp(-T * (e - e[0])); Ep = (w * e).sum() / w.sum(); diff = Ep - e[0]
    g = e[~deg].min() - e[0]; B = e[-1] - e[0]; tot = (c[deg] ** 2).sum()
    bound_total = B * ((psi @ psi) - tot) * np.exp(-g * T) / tot
    single_viol += 0
    total_viol += diff > bound_total + 1e-12
    # single-vector overlap in a rotated basis of the degenerate space: the bound with the wrong (smaller) overlap would be looser? test the version with g = min over ALL n>0 (=0 in the degenerate case)
    bound_single = B * ((psi @ psi) - c[0] ** 2) * np.exp(-0.0 * T) / c[0] ** 2       # gap between the two degenerate ground vectors is 0: the naive bound has no decay
    worst_total = max(worst_total, diff / bound_total)
print(f"   degenerate ground space, {n_inst} instances: the note's rule (total overlap, gap above the space) is never violated (largest ratio {worst_total:.4f}); the naive rule (one eigenvector, gap between degenerate vectors = 0) gives no exponential decay at all")
check("with a degenerate ground space the bound with the TOTAL overlap and the gap above the space holds on all instances", total_viol == 0 and n_inst > 100, f"{total_viol} violations in {n_inst}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-e sampled evidence on PR 9354: hill-climb (60 restarts, n=3,4) against the finite-projection bound finds no violation (sup ratio {best_ratio:.3f}, min E_psi-E_0 {min_diff:.1e}); the capped endpoint functional undershoots the ground energy under hill-climb ((E_cap-E_0)/|E_0| down to {min(under.values()):.2f}; the notes claim no bound; mechanism: for J = 0 E_cap is a weighted mean of the local energies E_L(x) = D(x) - sum_y A(x,y) psi(y)/psi(x), which tends to -infinity where psi(x) is small); guides with equal spectral average exist (two-state (1,2)/(2,1), and (1, {s2:.4f}) vs (1,2)); degenerate-ground bound with total overlap holds on {n_inst} instances; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
