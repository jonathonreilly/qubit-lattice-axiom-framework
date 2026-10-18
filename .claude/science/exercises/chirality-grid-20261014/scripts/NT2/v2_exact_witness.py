"""V2: exact rational witness for T22 (delta = 3/5). Pool of 6 admissible configurations:
checkerboard flux s in {-11/20, 0, 11/20} (plaquettes (phi00, phi10, phi01, phi11) = (-s, s, s, -s), so P = Q = 0, R = 2s)
x row Wilson lines X0 = X1 in {0, 1/20}; column Wilson lines Y0 = Y1 = 0.
Kernel (closed form, positive constant (2pi)^-3 dropped): box4(sigma; a, a, 2 delta, 2 delta), a = 2 delta - |dX0|,
sigma = (d phi10 + d phi01)/2 = ds. Exact arithmetic with Fractions; inertia by exact LDL^T; explicit rational vector."""
from fractions import Fraction as Fr
import itertools, numpy as np
from t22lib import box4, build_links, kernel_matrix_indep, kernel_matrix_closed

def box4_exact(sig, a):
    tot = Fr(0)
    for eps in itertools.product((1, -1), repeat=4):
        s = sig + sum(Fr(e) * ai for e, ai in zip(eps, a)) / 2
        if s > 0:
            tot += (eps[0] * eps[1] * eps[2] * eps[3]) * s ** 3 / 6
    return tot

d = Fr(3, 5); w = 2 * d; eps = Fr(1, 20)
S = [Fr(-11, 20), Fr(0), Fr(11, 20)]; X = [Fr(0), eps]
cfg = [(x, s) for x in X for s in S]
def K(c1, c2):
    a = w - abs(c1[0] - c2[0])
    return box4_exact(c1[1] - c2[1], [a, a, w, w]) if a > 0 else Fr(0)
Kx = [[K(c1, c2) for c2 in cfg] for c1 in cfg]
print("exact 6x6 kernel (x 1/(2pi)^3):")
for row in Kx:
    print("  ", [str(v) for v in row])
# exact LDL^T inertia
A = [row[:] for row in Kx]; n = len(A); piv = []
for k in range(n):
    p = A[k][k]; piv.append(p)
    assert p != 0
    for i in range(k + 1, n):
        f = A[i][k] / p
        for j in range(k, n):
            A[i][j] -= f * A[k][j]
print("LDL pivots (exact):", [str(p) for p in piv])
print("inertia (+, -):", sum(p > 0 for p in piv), sum(p < 0 for p in piv))
# explicit vector: antisymmetric in X (v, -v), v = (1, -2 + eta, 1) with eta chosen from first-order lemma
for eta in (Fr(0), Fr(1, 100), Fr(1, 1000), Fr(-1, 100)):
    v = [Fr(1), Fr(-2) + eta, Fr(1)]
    vec = v + [-z for z in v]
    q = sum(vec[i] * Kx[i][j] * vec[j] for i in range(n) for j in range(n))
    print(f"eta = {eta}: v^T K v = {q} = {float(q):+.6e}")
# float cross-check: closed form and independent explicit-link builder (random gauge)
rng = np.random.default_rng(5)
xs = np.array([float(c[0]) for c in cfg]); ss = np.array([float(c[1]) for c in cfg])
L = build_links(-ss, ss, ss, xs, 0 * xs, rng=rng)
Ki = kernel_matrix_indep(L, 0.6) * (2 * np.pi) ** 3; Kc = kernel_matrix_closed(L, 0.6) * (2 * np.pi) ** 3
Kf = np.array([[float(v) for v in row] for row in Kx])
print("max|exact - indep| =", np.abs(Kf - Ki).max(), " max|exact - closed| =", np.abs(Kf - Kc).max())
ev = np.linalg.eigvalsh(Kf); print("float eigenvalues:", ev, " min/max", ev[0] / ev[-1])
# first-order lemma check: B(sigma) = w^2 - sigma^2/2 on |sigma| <= w ; exact (K(0,s)-K(eps,s))/eps vs B as eps->0
for e in (Fr(1, 20), Fr(1, 200), Fr(1, 2000)):
    vals = [(box4_exact(sg, [w, w, w, w]) - box4_exact(sg, [w - e, w - e, w, w])) / e for sg in (Fr(0), Fr(11, 20), Fr(11, 10))]
    print(f"eps={e}: (K0-Keps)/eps at sigma=0, 11/20, 11/10:", [f"{float(v):.6f}" for v in vals], " B:", [f"{float(w*w - sg*sg/2):.6f}" for sg in (Fr(0), Fr(11, 20), Fr(11, 10))])
