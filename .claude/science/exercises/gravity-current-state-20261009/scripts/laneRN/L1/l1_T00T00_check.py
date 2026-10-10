"""Check that {T00[mu],T00[nu]} closes onto P[zeta] with zeta_j(x) = (mu_x nu_{x+e_j} - nu_x mu_{x+e_j})/2 or similar."""
import numpy as np
src = open("l1_closure_and_fermion.py").read().split('print("=== (a)')[0]
exec(src)
L = 5
V, T00, P, Om = build(L, 0.6)
rng2 = np.random.default_rng(3)
mu = rng2.standard_normal(V); nu = rng2.standard_normal(V)
Tmu = sum(mu[x] * T00[x] for x in range(V)); Tnu = sum(nu[x] * T00[x] for x in range(V))
C = pb(Tmu, Tnu, Om)
idx = np.arange(V).reshape(L, L, L)
best = None
for sgn in (+1, -1):
    for fac in (0.5, 1.0, 0.25):
        Z = 0
        for j in AX:
            mup = np.roll(mu.reshape(L, L, L), -1, axis=j).ravel(); nup = np.roll(nu.reshape(L, L, L), -1, axis=j).ravel()
            zeta = sgn * fac * (mu * nup - nu * mup)
            Z = Z + sum(zeta[x] * P[j][x] for x in range(V))
        r = abs(C - Z).max() / abs(C).max()
        print(f"sign {sgn:+d} factor {fac}: max|{{T00[mu],T00[nu]}} - P[zeta]| / max|C| = {r:.2e}")
print("max|C| =", abs(C).max())
