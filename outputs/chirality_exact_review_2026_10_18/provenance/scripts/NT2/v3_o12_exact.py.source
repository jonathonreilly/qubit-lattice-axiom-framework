"""V3: exact rational witness for the open 1x2 strip slice O12 (no holonomies), delta = 3/5.
Pool: 4x4 grid of plaquette pairs (phi1, phi2), phi in {-11/20, -11/60, 11/60, 11/20} (all |phi| <= delta - 1/20).
h(F1, F2) = int_{-d}^{d} T3(F1 - e) T3(F2 + e) de, T3 = 3-fold convolution of the box of width 2d (exact signed
truncated powers); the integrand is a polynomial of degree <= 4 on each breakpoint piece, integrated exactly by Boole's
rule (exact to degree 5) in rational arithmetic. Inertia by exact LDL^T. Float cross-check vs o12.h_exact."""
from fractions import Fraction as Fr
import itertools, numpy as np, sys
d = Fr(3, 5); w = 2 * d
def T3(x):
    tot = Fr(0)
    for eps in itertools.product((1, -1), repeat=3):
        s = x + w * sum(eps) / 2
        if s > 0: tot += eps[0] * eps[1] * eps[2] * s * s
    return tot / 2
def h(F1, F2):
    bp = {-d, d}
    for c in (-3 * d, -d, d, 3 * d):
        bp.add(min(max(F1 + c, -d), d)); bp.add(min(max(-F2 + c, -d), d))
    bp = sorted(bp); tot = Fr(0)
    for a, b in zip(bp[:-1], bp[1:]):
        if b == a: continue
        xs = [a + (b - a) * k / 4 for k in range(5)]
        f = [T3(F1 - x) * T3(F2 + x) for x in xs]
        tot += (b - a) / 90 * (7 * f[0] + 32 * f[1] + 12 * f[2] + 32 * f[3] + 7 * f[4])
    return tot
ax = [Fr(-11, 20), Fr(-11, 60), Fr(11, 60), Fr(11, 20)]
P = [(x, y) for x in ax for y in ax]; n = len(P)
K = [[h(p[0] - q[0], p[1] - q[1]) for q in P] for p in P]
A = [row[:] for row in K]; piv = []
for k in range(n):
    pk = A[k][k]; piv.append(pk); assert pk != 0
    for i in range(k + 1, n):
        f = A[i][k] / pk
        for j in range(k, n): A[i][j] -= f * A[k][j]
print("exact LDL pivots (float view):", [f"{float(p):+.4e}" for p in piv])
print("inertia (+, -):", sum(p > 0 for p in piv), sum(p < 0 for p in piv))
Kf = np.array([[float(v) for v in r] for r in K]); ev, V = np.linalg.eigh(Kf)
print(f"float eigen: lam_min {ev[0]:+.6e} lam_max {ev[-1]:.6e} rel {ev[0]/ev[-1]:+.4e}")
# explicit rational vector: round the float eigenvector, evaluate exactly
v = [Fr(round(z * 1000)) for z in V[:, 0]]
q = sum(v[i] * K[i][j] * v[j] for i in range(n) for j in range(n))
print("rounded eigenvector (x1000):", [int(z) for z in v]); print(f"v^T K v exact = {float(q):+.6e}  (negative: {q < 0})")
sys.argv = ['o12.py', 'grid', '2']; src = open('o12.py').read().split("t0 = time.time()")[0]; exec(src)
Kg = np.array([[h_exact(float(p[0] - q_[0]), float(p[1] - q_[1])) for q_ in P] for p in P])
print("max |exact rational - o12.h_exact (GL float)| =", np.abs(Kf - Kg).max())
