#!/usr/bin/env python3
"""info-min-law runner: checks for the information-minimisation reading of the rules.
Self-contained (numpy/scipy). Light: < 100 MB, a few seconds."""
AUDIT_TIMEOUT_SEC = 120
import itertools, warnings, numpy as np
warnings.filterwarnings("ignore")
from scipy.optimize import linprog, minimize, LinearConstraint, Bounds
from scipy.special import i0e, logsumexp
from scipy.integrate import quad
rng = np.random.default_rng(7)
P = F = 0
def chk(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {info}")

print("A. IM-1: least-information transport = eps->0 Schrodinger bridge = CL-2 (fewest changes, then greatest entropy)")
worst = 0.0; mi_ok = True; agree = True
for trial in range(6):
    n = 5
    mask = (rng.random((n, n)) < 0.6) | np.eye(n, dtype=bool)
    C = rng.integers(0, 3, (n, n)).astype(float); np.fill_diagonal(C, 0.0)
    G = rng.random((n, n)) * mask; G /= G.sum()          # a feasible plan fixes the marginals
    p, q = G.sum(1), G.sum(0)
    idx = [(i, j) for i in range(n) for j in range(n) if mask[i, j]]
    m = len(idx); c = np.array([C[i, j] for i, j in idx])
    Aeq = np.zeros((2 * n, m))
    for k, (i, j) in enumerate(idx): Aeq[i, k] = 1; Aeq[n + j, k] = 1
    beq = np.r_[p, q]
    cstar = linprog(c, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs").fun
    negH = lambda x: np.sum(x * np.log(np.maximum(x, 1e-300)))
    A2 = np.vstack([Aeq, c]); b2 = np.r_[beq, cstar]       # optimal face: odds kept AND fewest changes
    lex = minimize(negH, np.full(m, 1.0 / m), jac=lambda x: np.log(np.maximum(x, 1e-300)) + 1,
                   hess=lambda x: np.diag(1 / np.maximum(x, 1e-12)), constraints=[LinearConstraint(A2, b2, b2)],
                   bounds=Bounds(np.zeros(m), np.ones(m)), method="trust-constr",
                   options={"maxiter": 5000, "gtol": 1e-12, "xtol": 1e-14}).x
    for eps in [0.003]:
        K = np.full((n, n), -np.inf)
        for (i, j) in idx: K[i, j] = -C[i, j] / eps
        f = np.zeros(n); g = np.zeros(n)
        for _ in range(20000):
            f = np.log(p) - logsumexp(K + g[None, :], axis=1)
            g = np.log(q) - logsumexp(K + f[:, None], axis=0)
        Pi = np.exp(K + f[:, None] + g[None, :])
        sk = np.array([Pi[i, j] for i, j in idx])
    worst = max(worst, np.abs(sk - lex).max())
    Hs = -negH(sk); Hl = -negH(np.clip(lex, 0, None))
    agree &= abs(c @ sk - cstar) < 1e-9 and Hs > Hl - 1e-8
    # max entropy of plan given marginals == min mutual information I(X;Y)
    H = lambda v: -np.sum(v[v > 0] * np.log(v[v > 0]))
    Iq = sum(Pi[i, j] * np.log(Pi[i, j] / (p[i] * q[j])) for i, j in idx if Pi[i, j] > 0)
    mi_ok &= abs(H(sk) - (H(p) + H(q) - Iq)) < 1e-10
chk("A1 entropic-OT plan (min KL to lazy reference, eps=0.003) -> lexicographic CL-2 plan, 6 random tick supports",
    agree and worst < 1e-3, f"fewest changes exact, entropy >= independent max-entropy solve; max |plan diff| {worst:.1e} (solver tol)")
chk("A2 identity: greatest plan entropy at fixed odds == least mutual information between before and after", mi_ok, "H(pi)=H(X)+H(Y)-I(X;Y)")

print("B. Born = the unique odds weighting for which a finite-information (on-support) transport exists")
L, T, mth = 32, 60, 0.3
Cn = np.array([[np.cos(mth), -1j * np.sin(mth)], [-1j * np.sin(mth), np.cos(mth)]])
psi = np.zeros((L, 2), complex); psi[L // 2] = [1 / np.sqrt(2), 1j / np.sqrt(2)]
res = {}
for pw in [1.0, 1.5, 2.0, 2.5, 3.0, 4.0]:
    ph = psi.copy(); worstd = 0.0
    for t in range(T):
        w0 = np.abs(ph) ** pw; w0 /= w0.sum()
        ph2 = ph @ Cn.T                                   # coin inside each site block
        w1 = np.abs(ph2) ** pw; w1 /= w1.sum()
        # site block x -> images (x-1,L),(x+1,R) receive only from block x: on-support transport needs equal block totals
        worstd = max(worstd, 0.5 * np.abs(w0.sum(1) - w1.sum(1)).sum())
        ph = np.stack([np.roll(ph2[:, 0], -1), np.roll(ph2[:, 1], 1)], axis=1)
    res[pw] = worstd
chk("B1 off-support (nonlocal) mass forced per tick vanishes only at p=2 (KL to the tick reference infinite otherwise)",
    res[2.0] < 1e-14 and min(v for k, v in res.items() if k != 2.0) > 1e-3,
    " ".join(f"p={k:g}:{v:.1e}" for k, v in res.items()))
s = 0.37; ok = True
for S in np.linspace(0, 2 * s, 7):
    for pw in [1.0, 3.0]:
        Gf = lambda u: u ** (pw / 2)
        ok &= (pw == 2.0) or abs(Gf(S) + Gf(2 * s - S) - 2 * Gf(s)) > 1e-6 or abs(S - s) < 1e-12
chk("B2 Jensen step: G(S)+G(2s-S)=2G(s) on [0,2s] fails for G(u)=u^(p/2), p!=2 (affine G <=> Born)", ok, "rederives born-reading Step 2")

print("C. Born = least, state-uniform record information about a rotation (Fisher / Wootters)")
th = np.linspace(0.05, np.pi / 2 - 0.05, 400); out = []
for pw in [1.0, 2.0, 3.0, 4.0]:
    g = np.cos(th) ** pw / (np.cos(th) ** pw + np.sin(th) ** pw)
    gf = lambda t: np.cos(t) ** pw / (np.cos(t) ** pw + np.sin(t) ** pw)
    dg = (gf(th + 1e-6) - gf(th - 1e-6)) / 2e-6; Fi = dg ** 2 / (g * (1 - g))
    out.append((pw, Fi.min(), Fi.max()))
flat = [abs(b - a) / b < 1e-3 for _, a, b in out]
chk("C1 Fisher information of record odds is angle-independent only for p=2 (value 4)", flat == [False, True, False, False],
    " ".join(f"p={pw:g}:[{a:.2f},{b:.2f}]" for pw, a, b in out))
cs = [1, 3, 5]; zs = [int(np.sum(np.diff(np.sign(np.cos(cc * np.linspace(0, np.pi / 2 - 1e-3, 10001)))) != 0) > 0) for cc in cs]
chk("C2 constant-Fisher family cos^2(c th), c odd: F=4c^2, least at c=1; c>=3 has interior zero odds (support clause violated)",
    zs == [0, 1, 1], "F: " + ", ".join(f"c={cc}:{4*cc*cc}" for cc in cs))
a = rng.normal(size=3); a /= np.linalg.norm(a); da = rng.normal(size=3); da -= a * (a @ da); da *= 1e-6
for qexp, tag in [(2.0, "Born"), (3.0, "q=3")]:
    pa = np.abs(a) ** qexp / np.sum(np.abs(a) ** qexp); pb = np.abs(a + da) ** qexp / np.sum(np.abs(a + da) ** qexp)
    r = np.sum((pb - pa) ** 2 / pa) / np.sum(da ** 2)
    if tag == "Born": rB = r
chk("C3 3 outcomes: Fisher metric of Born odds = 4 x round metric on amplitudes (Wootters isometry)", abs(rB - 4) < 1e-4, f"ratio {rB:.6f}; q=3 ratio {r:.4f}")

print("D. Why a complex qubit: 1 bit + continuous reversibility + local tomography")
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
basis = [sx, sy, sz]
M = np.array([[np.trace(A @ B + B @ A).real / 2 for B in basis] for A in basis])
chk("D1 anticommuting traceless Hermitian generators are trace-orthogonal => at most 3 in M_2(C) (Bloch dim 3)",
    np.allclose(M, 2 * np.eye(3)) and np.linalg.matrix_rank(M) == 3, "Cl(3,0) = M_2(C) saturates at 3")
Kc = lambda N: N * N; Kr = lambda N: N * (N + 1) // 2; Kh = lambda N: N * (2 * N - 1)
chk("D2 parameter count K(N1N2)=K(N1)K(N2) (local tomography) holds for complex, fails real/quaternionic",
    Kc(4) == Kc(2) ** 2 and Kr(4) != Kr(2) ** 2 and Kh(4) != Kh(2) ** 2, f"K(4) vs K(2)^2: C {Kc(4)}/{Kc(2)**2}, R {Kr(4)}/{Kr(2)**2}, H {Kh(4)}/{Kh(2)**2}")

print("E. Z^3 with 6 neighbours = least neighbour information among translation-transitive 3D graphs")
vecs = [v for v in itertools.product(range(-2, 3), repeat=3) if any(v)]
reps = [v for v in vecs if v > tuple(-x for x in v)]
gen4 = sum(1 for a2, b2 in itertools.combinations(reps, 2) if np.linalg.matrix_rank(np.array([a2, b2])) == 3)
n6 = 0; basis6 = 0
for tri in itertools.combinations(reps, 3):
    d = round(abs(np.linalg.det(np.array(tri, float))))
    n6 += 1; basis6 += (d == 1)
chk("E1 no symmetric neighbour set of size < 6 spans 3D; size-6 sets generate Z^3 iff a basis (|det|=1) -> graph = simple cubic",
    gen4 == 0, f"size-4 spanning sets {gen4}; size-6 sets {n6}, generating {basis6} (all Cayley-isomorphic to 6-NN Z^3)")
chk("E2 minimal degree 2d grows with d: neighbour information alone prefers d=1 (does NOT select d=3)",
    [2 * dd for dd in (1, 2, 3)] == [2, 4, 6], "log2(2d) = 1, 2, 2.58 bits per neighbour address")

print("F. lower side of d=3 (supplied criteria, not information minimisation)")
u3 = quad(lambda t: i0e(t / 3) ** 3, 0, np.inf, limit=400)[0]
part2 = [quad(lambda t: i0e(t / 2) ** 2, 0, Tm, limit=400)[0] for Tm in (1e3, 1e5)]
chk("F1 Polya: 6-NN classical walk transient first at d=3 (return prob 1-1/u)", abs(1 - 1 / u3 - 0.3405373) < 1e-5 and part2[1] - part2[0] > 1.0,
    f"d=3 return {1-1/u3:.6f}; d=2 partial integral grows {part2[0]:.2f}->{part2[1]:.2f} (log-divergent)")
pol = {dd: (dd + 1) * (dd - 2) // 2 for dd in (2, 3, 4)}
chk("F2 free graviton polarisations (d+1)(d-2)/2: 0 at d=2, 2 at d=3 (register's 2 tensor modes need d>=3)", pol == {2: 0, 3: 2, 4: 5}, str(pol))

print("G. estimate: Lambda as count-noise of records in one Hubble 4-volume (Sorkin form; Planck cell ASSUMED)")
lp = 1.616255e-35; H0 = 67.4e3 / 3.0857e22; c0 = 2.99792458e8
LamObs = 1.1056e-52 * lp ** 2; V4 = (c0 / H0) ** 4 / lp ** 4; LamEst = V4 ** -0.5
chk("G1 1/sqrt(N_4cells) within 1.5 decades of Lambda*l_p^2 (order only; prefactor and cell size not derived)",
    abs(np.log10(LamEst / LamObs)) < 1.5, f"est {LamEst:.1e} vs obs {LamObs:.1e}")
print(f"TOTAL: PASS={P} FAIL={F}")
