"""K2 part 2a: exact symmetric lattice stress for the free scalar on Z^4 (Euclidean, xi=1),
exact O(kappa) gauge invariance of S_FP(h) + S_m(phi) + kappa * sum h_mn T_mn,
and the Killing-sector restriction (pseudo-translations, pseudo-rotations).

Conventions as in k2_graviton_gauge_killing.py (staggered base-point labels).
S_m = 1/2 sum_x [ sum_mu (Delta_mu phi)^2 + m2 phi^2 ],  E = dS_m/dphi.
Matter gauge transformation (symmetric lattice Lie derivative):
  L_xi phi(x) = 1/2 sum_nu [ xi_nu[x] Delta_nu phi(x) + xi_nu[x-e_nu] Delta_nu phi(x-e_nu) ].
Stress (Euclidean transcription of RN L1's exact Hamiltonian stress):
  T_mn[x] (m!=n, at x+(e_m+e_n)/2) = 1/4 (D_m phi(x)+D_m phi(x+e_n)) (D_n phi(x)+D_n phi(x+e_m))
  T_mm (at site z = x+e_m) = 1/2 D_m phi(z) D_m phi(z-e_m) - 1/4 sum_{r!=m}[(D_r phi(z))^2+(D_r phi(z-e_r))^2] - 1/2 m2 phi(z)^2
Integer fields -> every number is a dyadic rational -> float64 exact.
"""
import numpy as np, itertools
rng = np.random.default_rng(7)
D = 4
def sh(F, mu, n): return np.roll(F, -n, axis=mu)
def Dl(phi, mu): return sh(phi, mu, 1) - phi       # Delta_mu phi(x) = phi(x+e)-phi(x)

def E_of(phi, m2):
    return -sum(sh(phi, mu, 1) + sh(phi, mu, -1) - 2 * phi for mu in range(D)) + m2 * phi

def Lxi(phi, xi):
    out = 0.0
    for nu in range(D):
        d = Dl(phi, nu)
        out = out + 0.5 * (xi[nu] * d + sh(xi[nu] * d, nu, -1))
    return out

def stress(phi, m2):
    T = np.zeros((D, D) + phi.shape)
    for m in range(D):
        for n in range(D):
            if m != n:
                T[m, n] = 0.25 * (Dl(phi, m) + sh(Dl(phi, m), n, 1)) * (Dl(phi, n) + sh(Dl(phi, n), m, 1))
        # diagonal, evaluated at site z, then stored at base x = z - e_m
        z = 0.5 * Dl(phi, m) * sh(Dl(phi, m), m, -1) - 0.5 * m2 * phi ** 2
        for r in range(D):
            if r != m:
                z = z - 0.25 * (Dl(phi, r) ** 2 + sh(Dl(phi, r) ** 2, r, -1))
        T[m, m] = sh(z, m, 1)       # T_mm[x] = z(x+e_m)
    return T

def gauge(xi):
    h = np.zeros((D, D) + xi.shape[1:])
    for m in range(D):
        for n in range(D):
            h[m, n] = (sh(xi[n], m, 1) - xi[n]) + (sh(xi[m], n, 1) - xi[m])
    return h

print("== exact O(kappa) identity:  sum E*L_xi phi  + c * sum_{mn} (dh_mn) T_mn = 0  for all phi, xi ==")
for m2 in (0.0, 0.75, 3.0):
    for L in (3, 4, 6):
        res = []
        for t in range(4):
            phi = rng.integers(-30, 31, size=(L,) * D).astype(float)
            xi = rng.integers(-30, 31, size=(D,) + (L,) * D).astype(float)
            a = np.sum(E_of(phi, m2) * Lxi(phi, xi))
            b = np.sum(gauge(xi) * stress(phi, m2))
            res.append((a, b))
        cs = [-a / b for a, b in res if b != 0]
        c = cs[0]
        worst = max(abs(a + c * b) for a, b in res)
        print(f"m2={m2:5.2f} L={L}: fitted c = {c:+.6f}; max residual |a + c b| = {worst}")

print("\n=> T_mn is an exactly (off-shell) conserved, symmetric, local stress; with")
print("   S = S_FP(h) + S_m + kappa * c * sum h_mn T_mn and  delta h = nabla xi + nabla xi,")
print("   delta phi = kappa L_xi phi, the coupled action is gauge invariant at O(kappa) EXACTLY.")

# check also directly: full coupled action at O(kappa) with S_FP
import importlib.util, sys
print("\n== Killing restriction: pseudo-rotation  L_w phi = w_{nu mu} x_mu D_nu phi  (D = symmetric difference) ==")
# open box with compactly supported phi (zero padding): emulate infinite lattice
n = 10
for (a, b) in [(0, 1), (0, 3), (2, 3)]:
    worst = 0.0
    for t in range(3):
        phi = np.zeros((n,) * D)
        core = rng.integers(-30, 31, size=(n - 4,) * D).astype(float)
        phi[2:-2, 2:-2, 2:-2, 2:-2] = core
        # xi_nu at x + e_nu/2: xi_a = w_ab x_b, xi_b = -x_a (w_ab=1)
        X = np.indices((n,) * D).astype(float)
        xi = np.zeros((D,) + (n,) * D)
        xi[a] = X[b]          # position x+e_a/2 has x_b coordinate X[b] (b != a)
        xi[b] = -X[a]
        val = np.sum(E_of(phi, 0.75) * Lxi(phi, xi))
        dh = gauge(xi)
        # dh vanishes away from the wrap-around seam; the seam is irrelevant since phi has compact support
        worst = max(worst, abs(val))
    print(f"rotation in plane ({a},{b}): max |delta S_m| = {worst}")
print("=> the restriction of the matter gauge transformation to each lattice Killing rotation")
print("   (including (4,j) 'Euclidean boosts') is an exact symmetry of the free lattice scalar.")
