#!/usr/bin/env python3
"""Referee for J:derive:source-neutral-inclusion-attraction:a2.

Independent of the author's Q(sqrt(2)) Fourier class and of their determinants.
The torus Green function is the column of (L + 11^T/N)^{-1} minus 1/N.
The interaction is the prime-logdet of the modified lattice Laplacian.
The 6x6 formula is checked against that logdet, not taken from the attempt.
Z^3 uses the Bessel integral of L^{-1}, integrated with scipy, and is checked
against G(0) - G(e1) = 1/6 and Watson's gamma product.
"""
import itertools
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.linalg import eigvalsh, inv, slogdet, solve
from scipy.integrate import quad
from scipy.special import ive

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


NBRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def laplacian(L):
    N = L ** 3
    K = np.zeros((N, N))

    def idx(x):
        return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)

    for x, y, z in itertools.product(range(L), repeat=3):
        i = idx((x, y, z))
        K[i, i] = 6
        for d in NBRS:
            K[i, idx((x + d[0], y + d[1], z + d[2]))] -= 1
    return K, idx


def logdet_prime(K):
    w = np.sort(eigvalsh(K))
    if abs(w[0]) > 1e-7 or w[1] < 1e-5:
        raise RuntimeError(f"zero mode not isolated: {w[0]} {w[1]}")
    return float(np.log(w[1:]).sum())


def bonds_of(site):
    return [(tuple(site), tuple(site[i] + d[i] for i in range(3))) for d in NBRS]


def add_eps(K, site, eps, idx, L):
    for d in NBRS:
        u = idx(site)
        v = idx(tuple((site[i] + d[i]) % L for i in range(3)))
        K[u, u] += eps
        K[v, v] += eps
        K[u, v] -= eps
        K[v, u] -= eps


def bond_set(site, idx, L):
    out = set()
    for d in NBRS:
        u = idx(site)
        v = idx(tuple((site[i] + d[i]) % L for i in range(3)))
        out.add(tuple(sorted((u, v))))
    return out


def apply_bonds(K, bonds, factor):
    for u, v in bonds:
        K[u, u] += factor
        K[v, v] += factor
        K[u, v] -= factor
        K[v, u] -= factor


def F_full(K0, idx, L, r, ex, ey, mode="disjoint"):
    y = (r, 0, 0)
    Kb, Kx, Ky = K0.copy(), K0.copy(), K0.copy()
    if mode == "mult":
        bx, by = bond_set((0, 0, 0), idx, L), bond_set(y, idx, L)
        shared = bx & by
        apply_bonds(Kb, bx - shared, ex)
        apply_bonds(Kb, by - shared, ey)
        apply_bonds(Kb, shared, (1 + ex) * (1 + ey) - 1)
        apply_bonds(Kx, bx, ex)
        apply_bonds(Ky, by, ey)
    else:
        add_eps(Kb, (0, 0, 0), ex, idx, L)
        add_eps(Kb, y, ey, idx, L)
        add_eps(Kx, (0, 0, 0), ex, idx, L)
        add_eps(Ky, y, ey, idx, L)
    return 0.5 * (logdet_prime(Kb) - logdet_prime(Kx) - logdet_prime(Ky) + logdet_prime(K0))


def green_column(K0):
    N = K0.shape[0]
    g = solve(K0 + np.ones((N, N)) / N, np.eye(1, N, 0).ravel()) - 1.0 / N
    return g


def bmat(b1, b2, Gdiff):
    (u, v), (s, t) = b1, b2

    def gg(p, q):
        return Gdiff(tuple(p[i] - q[i] for i in range(3)))

    return gg(u, s) - gg(u, t) - gg(v, s) + gg(v, t)


def F6(Gdiff, r, ex, ey):
    bx, by = bonds_of((0, 0, 0)), bonds_of((r, 0, 0))
    Ax = np.array([[bmat(a, b, Gdiff) for b in bx] for a in bx], float)
    Ay = np.array([[bmat(a, b, Gdiff) for b in by] for a in by], float)
    M = np.array([[bmat(a, b, Gdiff) for b in by] for a in bx], float)
    left = solve(np.eye(6) + ex * Ax, M)
    X = (ex * ey) * (left @ inv(np.eye(6) + ey * Ay) @ M.T)
    sign, ld = slogdet(np.eye(6) - X)
    return 0.5 * float(ld), float(sign), float(np.sum(M * M)), M, Ax


# ---------- S1. torus Green function, real-space solve, exact G(0) by Fourier ----------
L8 = 8
K8, idx8 = laplacian(L8)
g8 = green_column(K8)
N8 = L8 ** 3
Lg = K8 @ g8
s1 = (
    abs(g8[0] - 118783817 / 528855040) < 1e-12
    and abs(Lg[0] - (1 - 1 / N8)) < 1e-9
    and abs(Lg[idx8((1, 0, 0))] + 1 / N8) < 1e-9
    and abs(g8.sum()) < 1e-9
)
mp.mp.dps = 40
sG = mp.mpf(0)
for kx, ky, kz in itertools.product(range(L8), repeat=3):
    if kx == ky == kz == 0:
        continue
    lam = sum(2 - 2 * mp.cos(2 * mp.pi * k / L8) for k in (kx, ky, kz))
    sG += 1 / lam
G0_mp = sG / L8 ** 3
frac = mp.mpf(118783817) / mp.mpf(528855040)
s1 = s1 and abs(G0_mp - frac) < mp.mpf("1e-30")
ok("S1", s1,
   f"8^3 real-space (L+11^T/N)^{{-1}}: G(0) matches 118783817/528855040 to 1e-12 and by an independent "
   f"Fourier sum to 1e-30 ({mp.nstr(G0_mp, 20)}); LG = delta - 1/512; sum G = 0")


def G8(d):
    return g8[idx8(tuple(t % L8 for t in d))]


# ---------- S2. full prime-logdet versus the 6x6 formula and the printed values ----------
printed = {2: -0.0035209463, 3: -0.00020640211, 4: -4.9346887e-5}
rows, good = [], True
for r, expect in printed.items():
    full = F_full(K8, idx8, L8, r, -0.5, -0.5)
    f6, sign, _, _, _ = F6(G8, r, -0.5, -0.5)
    good &= abs(full - expect) < 5e-10 and abs(full - f6) < 1e-10 and sign == 1.0 and full < 0
    rows.append(f"r={r}: full {full:.10e} formula {f6:.10e}")
fm = F_full(K8, idx8, L8, 1, -0.5, -0.5, "mult")
fa = F_full(K8, idx8, L8, 1, -0.5, -0.5, "add")
good &= abs(fm - 0.0030438) < 5e-8 and abs(fa + 0.098304) < 5e-7
rows.append(f"r=1 multiplicative {fm:.8e}, additive {fa:.8e}")
K6, idx6 = laplacian(6)
g6 = green_column(K6)

def G6(d):
    return g6[idx6(tuple(t % 6 for t in d))]

for r in (2, 3):
    for ex, ey in ((-0.5, -0.5), (0.3, 0.3), (-0.4, 0.2), (0.5, -0.7)):
        full = F_full(K6, idx6, 6, r, ex, ey)
        f6, sign, _, _, _ = F6(G6, r, ex, ey)
        good &= abs(full - f6) < 1e-9 and sign == 1.0
ok("S2", good, "prime-logdet of the stiffness equals the 6x6 Schur formula; " + "; ".join(rows))

# ---------- S3. sign for every equal-sign pair with eps > -1, r >= 2 ----------
good = True
for r in (2, 3):
    for ex, ey in ((-0.8, -0.3), (-0.5, -0.5), (0.4, 0.9), (1.5, 0.2), (-0.6, 0.4), (0.7, -0.2)):
        full = F_full(K6, idx6, 6, r, ex, ey)
        good &= (full < 0) if ex * ey > 0 else (full > 0)
ok("S3", good, "on the 6^3 torus, r = 2, 3: F < 0 when eps_x eps_y > 0 and F > 0 when eps_x eps_y < 0 (eps > -1)")

# ---------- S4. the eps^2 coefficient is 1/2, not the task's 1/4 ----------
_, _, M2, _, _ = F6(G8, 2, 0.0, 0.0)
half = -0.5 * M2
quarter = -0.25 * M2
mp.mp.dps = 40

def coef_of(eps):
    """F/eps^2 from the 6x6 formula at equal eps, with M, A taken from the solved Green function."""
    bx = bonds_of((0, 0, 0))
    by = bonds_of((2, 0, 0))
    A = mp.matrix([[mp.mpf(bmat(p, q, G8)) for q in bx] for p in bx])
    M = mp.matrix([[mp.mpf(bmat(p, q, G8)) for q in by] for p in bx])
    e = mp.mpf(eps)
    left = (mp.eye(6) + e * A) ** -1 * M
    X = e * e * left * (mp.eye(6) + e * A) ** -1 * M.T
    return mp.log(mp.det(mp.eye(6) - X)) / 2 / e ** 2

c1, c2 = coef_of("1e-6"), coef_of("2e-6")
richard = 2 * c1 - c2
vx, vy, c = sp.symbols("vx vy c", positive=True)
a, b = sp.symbols("a b")
mgf = sp.exp(sp.Rational(1, 2) * (vx * a ** 2 + vy * b ** 2 + 2 * c * a * b))
mom44 = sp.diff(mgf, a, 4, b, 4).subs({a: 0, b: 0})
cov44 = sp.factor(sp.together(mom44 - 3 * vx ** 2 * 3 * vy ** 2))
mom22 = sp.diff(mgf, a, 2, b, 2).subs({a: 0, b: 0})
cov22 = sp.factor(mom22 - vx * vy)
wick = sp.simplify(cov44 - (24 * c ** 4 + 72 * vx * vy * c ** 2)) == 0 and sp.simplify(cov22 - 2 * c ** 2) == 0
s4 = abs(half + 0.0113672742596) < 1e-12 and abs(float(richard) - half) < 1e-12 and abs(quarter - half) > 1e-3 and wick
ok("S4", s4,
   f"r=2 on 8^3: -(1/2) sum M^2 = {half:.12f} (quoted -0.011367274260); Richardson at 1e-6, 2e-6 "
   f"{float(richard):.12f}; -(1/4) sum M^2 = {quarter:.12f} does not match. "
   f"Wick: Cov(X^2,Y^2)=2c^2 and Cov(X^4,Y^4)=24c^4+72 vx vy c^2, so the free-energy cross term is -Cov = -(eps^2/2) sum M^2")

# ---------- S5. Z^3 constant, vacancies, held tilts ----------
_gcache = {}


def GL(d):
    key = tuple(sorted(abs(int(v)) for v in d))
    if key not in _gcache:
        aa, bb, cc = key

        def f(t):
            z = t / 3.0
            return ive(aa, z) * ive(bb, z) * ive(cc, z)

        s, _ = quad(f, 0, np.inf, epsabs=1e-13, limit=500)
        _gcache[key] = s / 6.0
    return _gcache[key]


g0 = GL((0, 0, 0))
mu = g0 - GL((2, 0, 0))
alpha = 2 / (1 - mu)
Cvac = -3 / (16 * np.pi ** 2) * alpha ** 2
W6 = (mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24)
      * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)) / 6
s5 = abs(g0 - GL((1, 0, 0)) - 1 / 6) < 1e-10 and abs(g0 - float(W6)) < 1e-10
s5 = s5 and abs(mu - 0.209841695316) < 1e-10 and abs(alpha - 2.5311384) < 1e-6
s5 = s5 and abs(Cvac + 0.12171197) < 1e-7


def Fvac(r):
    bx, by = bonds_of((0, 0, 0)), bonds_of((r, 0, 0))
    A = np.array([[bmat(p, q, GL) for q in bx] for p in bx], float)
    M = np.array([[bmat(p, q, GL) for q in by] for p in bx], float)
    Q = np.zeros((6, 5))
    for j in range(5):
        v = np.zeros(6)
        v[: j + 1] = 1
        v[j + 1] = -(j + 1)
        v /= np.linalg.norm(v)
        Q[:, j] = v
    Ap, Mp = Q.T @ A @ Q, Q.T @ M @ Q
    W = inv(np.eye(5) - Ap)
    X = W @ Mp @ W @ Mp.T
    sign, ld = slogdet(np.eye(5) - X)
    return 0.5 * float(ld), float(sign), M, A


quoted_Fr = {5: -0.2371, 10: -0.1383, 20: -0.1254}
quoted_ratio = {5: 5.995e-5, 10: 1.106e-6, 20: 3.144e-8}
rows = []
prev = None
for r, expect in quoted_Fr.items():
    Fv, sign, M, A = Fvac(r)
    Ft = -GL((r, 0, 0)) / (g0 ** 2 - GL((r, 0, 0)) ** 2)
    ratio = Fv / Ft
    Fr6 = Fv * r ** 6
    good_r = sign == 1.0 and Fv < 0 and Ft < 0 and abs(Fr6 - expect) < 2e-4
    good_r = good_r and abs(ratio / quoted_ratio[r] - 1) < 1e-3
    if prev is not None:
        good_r = good_r and abs(Fr6 - Cvac) < abs(prev - Cvac)
    prev = Fr6
    s5 = s5 and good_r
    rows.append(f"r={r}: F r^6 = {Fr6:.6f}, ratio {ratio:.4e}")
target = 3 / (2 * np.pi ** 2)
tr_at = {}
for r in (10, 20):
    M = Fvac(r)[2]
    tr_at[r] = float(np.sum(M * M)) * r ** 6
s5 = s5 and abs(tr_at[20] - target) < 0.01 and abs(tr_at[20] - target) < abs(tr_at[10] - target)
# dipole eigenvalue and the kernel along (1,...,1), which the far matrix annihilates
A0 = Fvac(2)[3]
v = np.zeros(6)
v[0], v[1] = 1.0, -1.0
Av = A0 @ v
s5 = s5 and abs(Av[0] - mu) < 1e-8 and abs(Av[1] + mu) < 1e-8 and np.max(np.abs(Av[2:])) < 1e-8
s5 = s5 and np.max(np.abs(A0 @ np.ones(6) - np.ones(6))) < 1e-8
s5 = s5 and np.max(np.abs(Fvac(2)[2] @ np.ones(6))) < 1e-8
ok("S5", s5,
   f"Z^3: G(0)-G(e1)=1/6, G(0) matches Watson/6, mu={mu:.12f}, alpha={alpha:.8f}, vacancy constant {Cvac:.8f}; "
   + "; ".join(rows)
   + f"; tr(MM^T) r^6 = {tr_at[10]:.5f}, {tr_at[20]:.5f} -> 3/(2 pi^2) = {target:.5f}")

# ---------- S6. one cubic invariant, so no 1/r ----------
fixed = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        nfix = 0
        for d in NBRS:
            img = [0, 0, 0]
            for i in range(3):
                img[perm[i]] = sg[perm[i]] * d[i]
            nfix += int(tuple(img) == d)
        fixed.append(nfix)
mean_fixed = sum(fixed) / len(fixed)
# algebraic: sum of the six bond vectors at y is L e_y, and G L e_y = e_y - 1/N, whose bond differences vanish off y
ann = True
for r in (2, 3, 4):
    M = F6(G8, r, 0.0, 0.0)[3]
    ann = ann and np.max(np.abs(M @ np.ones(6))) < 1e-9
ok("S6", len(fixed) == 48 and mean_fixed == 1 and ann,
   "the 48 signed axis permutations fix one bond on average, so the invariant bond vectors are multiples of (1,...,1); "
   "M_xy annihilates that direction for r>=2, and every entry of M is a second difference of G, hence O(r^{-3}). "
   "A shift-invariant inclusion therefore interacts at O(r^{-3}), or O(r^{-6}) if it is also cubic-invariant. Never 1/r.")

print(f"cache Z^3 points {len(_gcache)}")
if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - the 6x6 formula, the coefficient 1/2, the sign, the vacancy r^{-6} constant and the absence of a 1/r channel all survive an independent Laplacian logdet, a real-space Green function, and a Z^3 Bessel quadrature.")
print("HIT: confirmed - like inclusions attract for r>=2 through F=(1/2) log det(I - eps_x eps_y (I+eps_x A)^{-1} M (I+eps_y A)^{-1} M^T), with second order -(eps^2/2) sum M^2 rather than the task's 1/4; on Z^3, F r^6 -> -(3/(16 pi^2)) eps^2 alpha^2 with alpha=2/(1+eps mu), -0.12171197 for two vacancies; ratios to two held unit tilts are 5.995e-5, 1.106e-6, 3.144e-8 at r=5, 10, 20; a shift-invariant inclusion has no 1/r, and a cubic-invariant one decays as r^{-6}.")
