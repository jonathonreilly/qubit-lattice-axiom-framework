"""Lane G check 1: exact Z^3 lattice Green function and lump charges.

G solves -Delta G = delta on Z^3, Delta f(x) = sum_{y~x} (f(y) - f(x)).
Integral representation: G(x) = int_0^inf prod_i ive(x_i, 2t) dt.
Validated against Watson's constant and the discrete equation.

Then, exactly on Z^3 (no box):
  * capacity of a set B: Cap(B) = 1^T G_BB^{-1} 1 (perfect absorber);
  * transparent volume absorber of strength q per record:
      Q(q) = 1^T (G_BB + I/q)^{-1} 1   (Dyson; Phi = -G sigma, sigma = q n (1+Phi));
  * dilated set D = B + exterior contact shell (carriers excluded from records,
    perfect capture on contact).
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import time
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

t0 = time.time()
PREF = (4 * np.pi) ** -1.5
_cache = {}


def G(x):
    a, b, c = sorted(abs(int(v)) for v in x)
    key = (a, b, c)
    if key in _cache:
        return _cache[key]
    r2 = a * a + b * b + c * c
    T = max(4000.0, 60.0 * r2)
    f = lambda t: ive(a, 2 * t) * ive(b, 2 * t) * ive(c, 2 * t)
    edges = [0.0] + list(np.geomspace(0.25, T, 24))
    val = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        v, _ = quad(f, lo, hi, limit=200, epsabs=1e-15, epsrel=1e-12)
        val += v
    s = (4 * a * a - 1) + (4 * b * b - 1) + (4 * c * c - 1)
    tail = PREF * (2 * T ** -0.5 - (s / 16.0) * (2.0 / 3.0) * T ** -1.5)
    _cache[key] = val + tail
    return _cache[key]


def lapG(x):
    x = np.array(x)
    tot = -6 * G(x)
    for d in range(3):
        for s in (1, -1):
            y = x.copy(); y[d] += s
            tot += G(y)
    return tot


print("== A. Green function validation ==")
W = 1.516386059151978  # Watson simple-cubic integral (normalized walk)
print(f"G(0) = {G((0,0,0)):.12f}   Watson/6 = {W/6:.12f}   diff = {G((0,0,0))-W/6:.2e}")
print(f"G(1,0,0) = {G((1,0,0)):.12f}  G(0)-1/6 = {G((0,0,0))-1/6:.12f}")
for x in [(0, 0, 0), (1, 1, 0), (2, 1, 0), (3, 2, 1), (5, 0, 0)]:
    print(f"  -Delta G at {x}: {-lapG(x):+.3e}  (target {1 if x==(0,0,0) else 0})")

print("\n== A2. tail: 4 pi |x| G(x) along axis / face diag / body diag ==")
print(" n   axis(n,0,0)   face(n,n,0)   body(n,n,n)")
for n in [1, 2, 3, 5, 8, 12, 20, 30]:
    ax = 4 * np.pi * n * G((n, 0, 0))
    fa = 4 * np.pi * n * np.sqrt(2) * G((n, n, 0))
    bo = 4 * np.pi * n * np.sqrt(3) * G((n, n, n))
    print(f"{n:2d}   {ax:.6f}      {fa:.6f}      {bo:.6f}")


def cube(s):
    r = range(s)
    return [(i, j, k) for i in r for j in r for k in r]


def dilate(B):
    Bs = set(B)
    D = set(B)
    for (i, j, k) in B:
        for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            y = (i + d[0], j + d[1], k + d[2])
            if y not in Bs:
                D.add(y)
    return sorted(D)


def Gmat(B):
    P = np.array(B)
    n = len(B)
    M = np.empty((n, n))
    for i in range(n):
        dif = P - P[i]
        for j in range(n):
            M[i, j] = G(dif[j])
    return M


print("\n== B. lump charges exactly on Z^3 ==")
print("single record: Q(q) = q/(1+q G(0)); Cap({0}) = 1/G(0) =", f"{1/G((0,0,0)):.6f}")
for q in [0.01, 0.1, 1.0, 10.0]:
    print(f"  q={q:5}: Q = {q/(1+q*G((0,0,0))):.6f}   Q/q = {1/(1+q*G((0,0,0))):.6f}")

print("\n s    N   Cap(B)    Cap/s   Cap/N^(1/3)  Cap(dilated)  Capdil/(s+2)")
caps = {}
for s in [1, 2, 3, 4, 5, 6]:
    B = cube(s)
    M = Gmat(B)
    one = np.ones(len(B))
    cap = one @ np.linalg.solve(M, one)
    D = dilate(B)
    MD = Gmat(D)
    capd = np.ones(len(D)) @ np.linalg.solve(MD, np.ones(len(D)))
    caps[s] = (M, cap)
    print(f"{s:2d} {s**3:4d}  {cap:8.4f}  {cap/s:7.4f}  {cap/s:10.4f}   {capd:9.4f}    {capd/(s+2):7.4f}")
print("   (continuum cube: Cap ~ 4 pi * 0.6607 * side = 8.302 * side)")

print("\n== B2. transparent volume absorber: Q(q)/(q N) (1 = additive) ==")
print(" s    N   q=0.001    q=0.01    q=0.1     q=1      q=10     Q(q=10)/Cap")
for s in [1, 2, 3, 4, 5, 6]:
    M, cap = caps[s]
    n = s ** 3
    one = np.ones(n)
    row = []
    for q in [0.001, 0.01, 0.1, 1.0, 10.0]:
        Q = one @ np.linalg.solve(M + np.eye(n) / q, one)
        row.append(Q / (q * n))
    Q10 = one @ np.linalg.solve(M + np.eye(n) / 10.0, one)
    print(f"{s:2d} {n:4d}  " + "  ".join(f"{v:7.4f}" for v in row) + f"   {Q10/cap:7.4f}")

print("\n== B3. second-order (shadowing) expansion Q = qN - q^2 1'G1 + O(q^3), s=4 ==")
M, cap = caps[4]
one = np.ones(64)
for q in [1e-3, 1e-2]:
    Q = one @ np.linalg.solve(M + np.eye(64) / q, one)
    approx = q * 64 - q * q * (one @ M @ one)
    print(f"  q={q}: exact {Q:.10f}  2nd-order {approx:.10f}  rel diff {abs(Q-approx)/Q:.2e}")
print(f"\nelapsed {time.time()-t0:.1f} s, distinct G values {len(_cache)}")
