#!/usr/bin/env python3
"""p5 (lane E, session 5): linearised dilution of the S4' centre plaquette, DIL-L sampled checks, arithmetic.
Criteria: checks/p5_criteria.md (written before this script). Prints < 6000 chars."""
import itertools
import math
import random
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog

AUDIT_TIMEOUT_SEC = 600
D, L = 4, 3
MU, NU = 0, 1
RESULTS = {}


def e(a):
    v = [0] * D
    v[a] = 1
    return tuple(v)


def add(s, t, k=1):
    return tuple(si + k * ti for si, ti in zip(s, t))


def centre(X):
    return tuple(L * xi + 1 for xi in X)


def axial(sigma, start, end):
    """complete axial path start -> end moving coordinates in the order sigma; list of (site, dir, sign)."""
    steps, cur = [], list(start)
    for a in sigma:
        while cur[a] != end[a]:
            if end[a] > cur[a]:
                steps.append((tuple(cur), a, +1))
                cur[a] += 1
            else:
                cur[a] -= 1
                steps.append((tuple(cur), a, -1))
    return steps


def reverse(steps):
    return [(s, a, -sg) for (s, a, sg) in reversed(steps)]


def contours(X, alpha):
    cX, cY = centre(X), centre(add(X, e(alpha)))
    out = []
    for sigma in itertools.permutations(range(D)):
        for off in itertools.product(range(L), repeat=D):
            y = tuple(L * xi + o for xi, o in zip(X, off))
            leg = [(add(y, e(alpha), k), alpha, +1) for k in range(L)]
            far = axial(sigma, cY, add(y, e(alpha), L))
            out.append(axial(sigma, cX, y) + leg + reverse(far))
    return out


def coarse_functional(X, alpha):
    cs = contours(X, alpha)
    n = len(cs)
    A, f = {}, {}
    for c in cs:
        for (s, a, sg) in c:
            A[(s, a)] = A.get((s, a), Fraction(0)) + Fraction(sg, n)
            f[(s, a)] = f.get((s, a), Fraction(0)) + Fraction(1, n)
    return A, f, cs


blocks = {"X": (0, 0, 0, 0), "X+mu": e(MU), "X+nu": e(NU), "X+mu+nu": add(e(MU), e(NU))}
links_c = [(blocks["X"], MU, +1), (blocks["X+mu"], NU, +1), (blocks["X+nu"], MU, -1), (blocks["X"], NU, -1)]
W, Fc, fam = {}, [], {}
for (X, alpha, sgn) in links_c:
    A, f, cs = coarse_functional(X, alpha)
    fam[(X, alpha)] = (f, cs)
    Fc.append(sum(v * v for v in f.values()))
    for k, v in A.items():
        W[k] = W.get(k, Fraction(0)) + sgn * v
W = {k: v for k, v in W.items() if v != 0}
F_star = max(Fc)


def in_block(s, X):
    return all(L * xi <= si <= L * xi + L - 1 for si, xi in zip(s, X))


# B1 gauge invariance (zero divergence)
div = {}
for (s, a), v in W.items():
    div[s] = div.get(s, 0) + v
    t = add(s, e(a))
    div[t] = div.get(t, 0) - v
B1 = all(v == 0 for v in div.values())
# B2 locality
ends = [(blocks["X"], blocks["X+mu"]), (blocks["X+mu"], blocks["X+mu+nu"]), (blocks["X+nu"], blocks["X+mu+nu"]),
        (blocks["X"], blocks["X+nu"])]
B2 = all(any(all(in_block(p, X1) or in_block(p, X2) for p in (s, add(s, e(a)))) for (X1, X2) in ends)
         for (s, a) in W)
# B3 uniform field
F_unif = sum(v * (-s[NU]) for (s, a), v in W.items() if a == MU)
B3 = (F_unif == 9)
# B4 random gauge in block X
rng = random.Random(5)
B4 = True
for _ in range(10):
    chi = {}
    for off in itertools.product(range(L), repeat=D):
        chi[off] = rng.randint(-7, 7)
    val = sum(v * (chi.get(add(s, e(a)), 0) - chi.get(s, 0)) for (s, a), v in W.items())
    B4 &= (val == 0)
print(f"B1 div-free={B1}  B2 local={B2}  B3 F_P(uniform b=1)={F_unif} pass={B3}  B4 gauge->0 {B4}")
print(f"   |supp W|={len(W)}  F_c={[float(x) for x in Fc]}  F_*={float(F_star):.6f}")


def int_links(Xs):
    out = []
    for X in Xs:
        for off in itertools.product(range(L), repeat=D):
            s = tuple(L * xi + o for xi, o in zip(X, off))
            for a in range(D):
                if in_block(add(s, e(a)), X):
                    out.append((s, a))
    return out


def plaq_matrix(lk):
    idx = {l: i for i, l in enumerate(lk)}
    # enumerate plaquettes by base site and plane, keep those touching lk
    plaqs = set()
    for (s, a) in lk:
        for b in range(D):
            if b == a:
                continue
            for base in (s, add(s, e(b), -1)):
                p, q = min(a, b), max(a, b)
                plaqs.add((base, p, q))
    M = []
    for (base, p, q) in sorted(plaqs):
        r = np.zeros(len(lk))
        for (site, dirn, sg) in ((base, p, 1), (add(base, e(p)), q, 1), (add(base, e(q)), p, -1), (base, q, -1)):
            if (site, dirn) in idx:
                r[idx[(site, dirn)]] += sg
        M.append(r)
    return np.array(M)


def dilution(Xs, Wvec_fn=None):
    lk = int_links(Xs)
    B = plaq_matrix(lk)
    w = np.array([float(W.get(l, 0)) for l in lk]) if Wvec_fn is None else Wvec_fn(lk)
    A_ub = np.vstack([B, -B])
    b_ub = np.ones(2 * B.shape[0])
    res = linprog(-w, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * len(lk), method="highs")
    if res.status != 0:
        return dict(status=res.status, msg=res.message, n=len(lk))
    primal = -res.fun
    dual = -float(b_ub @ res.ineqlin.marginals)
    viol = float(np.max(np.abs(B @ res.x)) - 1)
    y, *_ = np.linalg.lstsq(B.T, w, rcond=None)
    resid = float(np.linalg.norm(B.T @ y - w))
    return dict(status=0, R_inf=primal, dual=dual, viol=viol, R_2=float(np.linalg.norm(y)), resid=resid,
                wmax=float(np.max(np.abs(w))), wnorm=float(np.linalg.norm(w)), n=len(lk), m=B.shape[0])


B5 = True
out = {}
for name, X in blocks.items():
    r = dilution([X])
    out[name] = r
    ok = r["status"] == 0 and abs(r["R_inf"] - r["dual"]) <= 1e-7 * max(1, abs(r["R_inf"])) and r["viol"] <= 1e-9 \
        and r["resid"] <= 1e-9 * max(1e-300, r["wnorm"])
    B5 &= ok
    print(f"B5 {name:8s} n={r['n']} m={r['m']} R_inf={r['R_inf']:.6f} (dual {r['dual']:.6f}) R_2={r['R_2']:.6f} "
          f"max|W|={r['wmax']:.6f} resid={r['resid']:.1e} ok={ok}")
r4 = dilution(list(blocks.values()))
ok4 = r4["status"] == 0 and abs(r4["R_inf"] - r4["dual"]) <= 1e-7 * max(1, abs(r4["R_inf"])) and r4["viol"] <= 1e-9 \
    and r4["resid"] <= 1e-9 * max(1e-300, r4["wnorm"])
B5 &= ok4
print(f"B5 U4       n={r4['n']} m={r4['m']} R_inf={r4['R_inf']:.6f} (dual {r4['dual']:.6f}) R_2={r4['R_2']:.6f} "
      f"max|W|={r4['wmax']:.6f} ok={ok4}")
R = r4["R_inf"]
s_ = 1 / math.sqrt(24)
rule = "simple split viable" if R < 0.25 else ("refined split only" if R < 1 - s_ - 0.05 else "NP-F5 MET (linear order)")
print(f"B6 rule on R_inf(U4)={R:.6f}: {rule}")


# B7 negative control: straight transporter c_X -> c_X + 3 e_mu, not gauge invariant
def straight_w(lk):
    cX = centre(blocks["X"])
    st = {(add(cX, e(MU), k), MU) for k in range(L)}
    return np.array([1.0 if l in st else 0.0 for l in lk])


r7 = dilution([blocks["X"]], straight_w)
B7 = (r7["status"] != 0) or (r7.get("R_inf", 0) >= 10)
print(f"B7 non-gauge-invariant functional: status={r7['status']} value={r7.get('R_inf')} pass={B7}")


# C. sampled SU(2) (quaternions; ||q1 - q2||_op = Euclidean norm for real combinations of SU(2))
def qmul(p, q):
    a1, b1, c1, d1 = p[..., 0], p[..., 1], p[..., 2], p[..., 3]
    a2, b2, c2, d2 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return np.stack([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2], axis=-1)


def qconj(q):
    return q * np.array([1, -1, -1, -1])


nrng = np.random.default_rng(55)
f1, cs1 = fam[(blocks["X"], MU)]
lk1 = sorted(f1.keys())
li = {l: i for i, l in enumerate(lk1)}
NS = 300


def haar(n, k):
    q = nrng.normal(size=(n, k, 4))
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


def near1(n, k, eps):
    v = nrng.normal(size=(n, k, 3)) * eps
    q = np.concatenate([np.ones((n, k, 1)), v], axis=-1)
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


U = np.concatenate([haar(NS // 2, len(lk1)), near1(NS - NS // 2, len(lk1), 0.15)], axis=0)
U0 = U.copy()
mask = nrng.random((NS, len(lk1))) < nrng.random((NS, 1)) * 0.3
repl = np.concatenate([haar(NS // 2, len(lk1)), near1(NS - NS // 2, len(lk1), 0.15)], axis=0)
U0[mask] = repl[mask]


def mean_transport(F):
    acc = np.zeros((NS, 4))
    for c in cs1:
        T = np.tile(np.array([1.0, 0, 0, 0]), (NS, 1))
        for (s, a, sg) in c:
            g = F[:, li[(s, a)], :]
            T = qmul(T, g if sg > 0 else qconj(g))
        acc += T
    return acc / len(cs1)


M, M0 = mean_transport(U), mean_transport(U0)
lhs = np.linalg.norm(M - M0, axis=1)
fv = np.array([float(f1[l]) for l in lk1])
rhs = (np.linalg.norm(U - U0, axis=2) * fv).sum(axis=1)
C1 = int(np.sum(lhs > rhs + 1e-12)) == 0
C1n = int(np.sum(lhs > rhs / 2 + 1e-12)) > 0
print(f"C1 DIL-L(i) violations={int(np.sum(lhs > rhs + 1e-12))}/{NS} max lhs/rhs={float(np.max(lhs / np.maximum(rhs, 1e-300))):.4f} "
      f"pass={C1};  C1n(f/2) violated in {int(np.sum(lhs > rhs / 2 + 1e-12))} pass={C1n}")


def su2(q):
    a, b, c, d = q
    return np.array([[a + 1j * d, c + 1j * b], [-c + 1j * b, a - 1j * d]])


worst2, worst3 = 0.0, -1.0
for _ in range(20000):
    w = su2(haar(1, 1)[0, 0]); v = su2(haar(1, 1)[0, 0]); r = nrng.random() + 1e-9
    Mm = r * w
    phi = r - 0.5 * np.real(np.trace(np.linalg.inv(v) @ Mm))
    worst2 = max(worst2, abs(phi - r * np.linalg.norm(v - w, 2) ** 2 / 2))
    Ws = [su2(q) for q in haar(1, 4)[0]]
    Wo = [x @ su2(q) for x, q in zip(Ws, near1(1, 4, nrng.random())[0])]
    hol = lambda Z: Z[0] @ Z[1] @ np.linalg.inv(Z[2]) @ np.linalg.inv(Z[3])
    I2 = np.eye(2)
    gap = abs(np.linalg.norm(I2 - hol(Ws), 2) - np.linalg.norm(I2 - hol(Wo), 2)) - sum(
        np.linalg.norm(a - b, 2) for a, b in zip(Ws, Wo))
    worst3 = max(worst3, gap)
C2, C3 = worst2 <= 1e-12, worst3 <= 1e-12
print(f"C2 max|phi - r d^2/2|={worst2:.1e} pass={C2};  C3 max(lhs-rhs)={worst3:.1e} pass={C3}")

# A. arithmetic
A1 = Fraction(5, 256) == Fraction(5, 8) * Fraction(1, 16) / 2
c_pr = Fraction(1, 1797760)
theta, lam, rstar = Fraction(1, 24), Fraction(1, 2), Fraction(1, 2)
kappa_eg = theta * c_pr * 2 * F_star / (lam * rstar * Fraction(5, 256) ** 2)
print(f"A1 {A1};  A2 kappa_eg={float(kappa_eg):.6e} (F_*={float(F_star):.6f})")
for tau in (0.05, 0.1, 0.2):
    print(f"A3 tau={tau}: gamma=(1-tau-1/sqrt24)/R={(1 - tau - s_) / R:.6f}")
allpass = all([B1, B2, B3, B4, B5, B7, C1, C1n, C2, C3, A1])
print("SUMMARY:", "ALL PASS" if allpass else "FAIL: " + ",".join(
    n for n, v in zip(["B1", "B2", "B3", "B4", "B5", "B7", "C1", "C1n", "C2", "C3", "A1"],
                      [B1, B2, B3, B4, B5, B7, C1, C1n, C2, C3, A1]) if not v))
