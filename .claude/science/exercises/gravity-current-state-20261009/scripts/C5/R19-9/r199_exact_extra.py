"""R19-9 (a) extra checks: (i) Gauss-law scope: the continuum Maxwell kernel (and the glued kernel) satisfy W1 only on the
physical (transverse) block, as in the continuum (conservation uses div E = 0); (ii) reality: the reflected-transposed kernel
M'(k1,k2) = M(-k2,-k1)^T, which defines the same operator for a real field, also satisfies W1 (so the symmetrized kernel does);
(iii) the time components are NOT VW-independent data: the pair-block P1 time components equal d.V/(w1+w2) (spot check)."""
import numpy as np, lib199 as L
rng = np.random.default_rng(7); r = 0.1
def full_resid(M, k1, k2):
    h1 = L.hmat(L.sig(k1)); h2 = L.hmat(L.sig(k2)); d = L.dsym(L.wrap(k1 - k2)); out = 0.0; sc = 0.0
    for nu in range(4):
        lhs = h1 @ M[0, nu] - M[0, nu] @ h2; rhs = np.einsum('j,jab->ab', d, M[1:, nu])
        out = max(out, np.abs(lhs - rhs).max()); sc = max(sc, np.abs(lhs).max(), np.abs(rhs).max())
    return out/sc
mx = 0.0
for _ in range(100):
    v1, v2 = rng.normal(size=3), rng.normal(size=3); k1 = v1/np.linalg.norm(v1)*r*rng.uniform(); k2 = v2/np.linalg.norm(v2)*r*rng.uniform()
    mx = max(mx, full_resid(L.continuum(k1, k2), k1, k2))
print(f'(i) continuum Maxwell kernel, W1 on the FULL 6x6 field space (no Gauss projection): max relative residual {mx:.2f} '
      f'(physical block: ~3e-15, r199_exact.out) -> exactness is on the constraint surface, as in the continuum')
mx = 0.0; mxp = 0.0
for _ in range(400):
    if rng.uniform() < 0.5:
        k1, k2 = rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)
    else:
        v1, v2 = rng.normal(size=3), rng.normal(size=3); k1 = v1/np.linalg.norm(v1)*2*r*rng.uniform(); k2 = v2/np.linalg.norm(v2)*2*r*rng.uniform()
    Mr = np.transpose(L.glued(-k2, -k1, r), (0, 1, 3, 2))
    mx = max(mx, max(x[1] for x in L.w1_resid(Mr, k1, k2)))
print(f'(ii) reflected-transposed kernel M(-k2,-k1)^T: max relative W1 residual (physical block) over 400 pairs {mx:.2e}')
