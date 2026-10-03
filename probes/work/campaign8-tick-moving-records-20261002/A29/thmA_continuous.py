#!/usr/bin/env python3
"""A29 check: does A25's Theorem A (collocated, covariant, exactly gauge-invariant spin-2 => doubler at
(pi,pi,pi)) bite in CONTINUOUS time, i.e. in A27's Option R setting with no ticks for the field?

Continuous-time linear field: H = 1/2 pi.M.pi + 1/2 h.V(k).h, so omega^2 = eig(M V(k)) (no time step at all).
Collocated layout: every component at the site, gauge generator dh = g xi^T + xi g^T with a 2pi-periodic,
O_h-covariant symbol g(k).  Potential: the gauge-invariant EH form built from g, V_g = 1/2 inc_g,
inc_g(h)_ij = -eps_ikl eps_jmn g_k g_m h_ln (gauge-invariant for ANY g, since eps_ikl g_k g_l = 0).
Staggered control: g = 2 sin(k/2) (A25's half-step layout, roles).

Prints, for several covariant collocated families:
  (a) |g(K)| and max|V(K)| at K = (pi,pi,pi);
  (b) the continuous-time omega^2 spectrum at K + q for shrinking q: two nonzero values -> 0 like |q|^2,
      i.e. a second massless graviton (omega ~ |q|) -- a doubler with no time step involved;
  (c) the staggered control at K: omega^2 = s^2 = 12 (gapped, no doubler).
Tiny: 6x6 matrices only.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np

EPS3 = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    EPS3[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])

B = []
for i in range(3):
    E = np.zeros((3, 3)); E[i, i] = 1; B.append(E.ravel())
for i, j in ((0, 1), (0, 2), (1, 2)):
    E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1 / np.sqrt(2); B.append(E.ravel())
B = np.array(B).T  # 9 x 6

Mfull = 2 * np.eye(9) - np.outer(np.eye(3).ravel(), np.eye(3).ravel())   # DeWitt: hdot = 2 pi - delta tr pi
M = B.T @ Mfull @ B


def V_of(g):
    inc = -np.einsum('ikl,jmn,k,m->ijln', EPS3, EPS3, g, g).reshape(9, 9)
    return B.T @ (0.5 * inc) @ B


def D_of(g):
    D = np.zeros((9, 3))
    for i in range(3):
        for j in range(3):
            D[3 * i + j, j] += g[i]; D[3 * i + j, i] += g[j]
    return B.T @ D


def fam(a, b, c):
    """O_h-covariant collocated generator: g_j = sin k_j (1 + a cos k_j + b(cos k_j+1 + cos k_j+2) + c cos k_j+1 cos k_j+2)"""
    def g(k):
        cs = np.cos(k)
        out = np.zeros(3)
        for j in range(3):
            o1, o2 = cs[(j + 1) % 3], cs[(j + 2) % 3]
            out[j] = np.sin(k[j]) * (1 + a * cs[j] + b * (o1 + o2) + c * o1 * o2)
        return out
    return g


def covariance_residual(g, rng):
    # check g(R k) = R g(k) for all 48 signed permutations
    worst = 0.0
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for r, (p, s) in enumerate(zip(perm, signs)):
                R[r, p] = s
            for _ in range(5):
                k = rng.uniform(-np.pi, np.pi, 3)
                worst = max(worst, np.abs(g(R @ k) - R @ g(k)).max())
    return worst


rng = np.random.default_rng(7)
K = np.array([np.pi] * 3)
families = {
    "central sin k": fam(0.0, 0.0, 0.0),
    "a=0.4 b=-0.3 c=0.2": fam(0.4, -0.3, 0.2),
    "a=-0.7 b=0.25 c=-0.5": fam(-0.7, 0.25, -0.5),
}
print("Continuous-time collocated spin-2 (no time step).  K = (pi,pi,pi)")
for name, g in families.items():
    cov = covariance_residual(g, rng)
    gK = g(K); VK = V_of(gK)
    print(f"\n[{name}] O_h covariance residual {cov:.1e};  |g(K)| = {np.linalg.norm(gK):.1e};  max|V(K)| = {np.abs(VK).max():.1e}")
    for eps in (1e-1, 1e-2, 1e-3):
        q = eps * np.array([0.6, -0.3, 0.74]) / np.linalg.norm([0.6, -0.3, 0.74])
        k = K + q
        gk = g(k); Vk = V_of(gk); Dk = D_of(gk)
        w2 = np.sort(np.linalg.eigvals(M @ Vk).real)
        nz = w2[np.abs(w2) > 1e-14 * max(1, np.abs(w2).max())]
        gauge = np.abs(Vk @ Dk).max()
        print(f"   |q|={eps:.0e}: omega^2 = {np.array2string(w2, precision=3, floatmode='maxprec')}  "
              f"nonzero/|q|^2 = {np.array2string(nz / eps**2, precision=4)}  |V D| = {gauge:.1e}  min omega^2 = {w2.min():.1e}")

# staggered control (A25 layout): g = 2 sin(k/2) is NOT 2pi-periodic per component -> needs half-shifted (role) positions
s = 2 * np.sin(K / 2)
w2 = np.sort(np.linalg.eigvals(M @ V_of(s)).real)
print(f"\n[staggered control, s = 2 sin(k/2)] at K: omega^2 = {np.array2string(w2, precision=6)}  (s^2 = {s @ s:.6f}): gapped, no doubler")
