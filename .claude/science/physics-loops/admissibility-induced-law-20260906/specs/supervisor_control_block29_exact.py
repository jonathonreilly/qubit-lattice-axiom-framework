"""Control (exact parts) for block 29: (1) the quadratic transverse model on a small torus: <|theta_hat(k)|^2> = 1/(beta E(k)) exactly
(the precision matrix's inverse in Fourier space); (2) the single-site transverse sum rule beta h E[(s^1)^2] = E[s^3] for the exponential
law with concentration beta h (symbolic); (3) Parseval on random configurations (exact rationals)."""
import sympy as sp, numpy as np
from fractions import Fraction as F
# (1) on the L=4 torus in one dimension x three (use a 4x4x4 torus): precision P = beta * Laplacian; Fourier diagonalisation
L = 4; beta = sp.symbols("beta", positive=True)
import itertools
N = L**3; sites = list(itertools.product(range(L), repeat=3)); index = {s: i for i, s in enumerate(sites)}
Lap = sp.zeros(N, N)
for s in sites:
    i = index[s]
    for ax in range(3):
        for sh in (1, -1):
            t = list(s); t[ax] = (t[ax] + sh) % L; j = index[tuple(t)]
            Lap[i, i] += 1; Lap[i, j] -= 1
ok = True
for kk in [(1, 0, 0), (2, 0, 0), (1, 1, 0), (1, 2, 3)]:
    k = [2*sp.pi*n/L for n in kk]
    v = sp.Matrix([sp.exp(sp.I*sum(kj*sj for kj, sj in zip(k, s))) for s in sites])
    E = 2*sum(1 - sp.cos(kj) for kj in k)
    ok = ok and sp.simplify(Lap*v - E*v) == sp.zeros(N, 1)
print("(1) the torus Laplacian has the plane waves as eigenvectors with eigenvalue E(k) = 2 sum (1 - cos k_j):", ok, "-> for the Gaussian law with precision beta*Lap the k-mode variance is 1/(beta E(k)) per component")
# (2) single-site sum rule
kap, w = sp.symbols("kappa w", positive=True)
Z = sp.integrate(sp.exp(kap*w), (w, -1, 1)); Ew = sp.integrate(w*sp.exp(kap*w), (w, -1, 1))/Z; Ew2 = sp.integrate(w**2*sp.exp(kap*w), (w, -1, 1))/Z
E_s1sq = (1 - Ew2)/2   # transverse component squared, by symmetry
print("(2) kappa * E[(s^1)^2] - E[s^3] =", sp.simplify((kap*E_s1sq - Ew).rewrite(sp.exp)), "(kappa = beta h)")
# (3) Parseval: (1/N) sum_k |f_hat(k)|^2 = sum_x |f_x|^2 with f_hat(k) = sum_x f_x e^{-ikx}; exact on a 4-site ring with rational f via the DFT identity
rng = np.random.default_rng(1)
f = [F(int(x), 7) for x in rng.integers(-9, 10, 4)]
# use the exact DFT with roots of unity via sympy
Fk = [sum(f[x]*sp.exp(-2*sp.pi*sp.I*k*x/4) for x in range(4)) for k in range(4)]
lhs = sp.nsimplify(sp.simplify(sum(sp.Abs(Fk[k])**2 for k in range(4))/4)); rhs = sum(fx*fx for fx in f)
print("(3) Parseval on a 4-site ring with rational data:", sp.simplify(lhs - rhs) == 0)
