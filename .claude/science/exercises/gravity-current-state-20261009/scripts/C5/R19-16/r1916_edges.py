"""R19-16: exact special points of the REPAIRED kernel.  Each leg's components drawn from {0, +-1e-300, +-b, +-pi, -pi + 0, +-(pi - b)/2
+ b, random}, all 9^3 = 729 legs paired with 3 partners each (special, random hard, small).  Finiteness with warnings as
errors; W1 on the physical block (a zero leg: full soft side, as in r1916_seam_zero Z1).  r = 0.1 and 0.05."""
import itertools, warnings, numpy as np
import lib1916 as R
L = R.L
warnings.simplefilter('error')
rng = np.random.default_rng(1916777)
b = R.BG
vals = [0.0, 1e-300, -1e-300, b, -b, np.pi, -np.pi, b + 0.5*(np.pi - b), None]
def leg(c):
    return np.array([rng.uniform(-np.pi, np.pi) if v is None else v for v in c])
def resid(M, k1, k2):
    s1, s2 = L.sig(k1), L.sig(k2)          # a leg whose omega^2 underflows (e.g. 1e-300 components) is checked as a zero leg
    z1, z2 = (s1 @ s1) == 0.0, (s2 @ s2) == 0.0
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2)); d = L.dsym(L.wrap(k1 - k2))
    P1 = np.eye(6) if z1 else L.projs(k1)[4]; P2 = np.eye(6) if z2 else L.projs(k2)[4]
    return max(np.abs(P1 @ (h1 @ M[0, nu] - M[0, nu] @ h2 - np.einsum('j,jab->ab', d, M[1:, nu])) @ P2).max() for nu in range(4))
for r in (0.1, 0.05):
    mx = 0.0; n = 0; cnt = {}
    for c in itertools.product(vals, repeat=3):
        k1 = leg(c)
        partners = [leg(c[::-1]), rng.uniform(-np.pi, np.pi, 3), rng.normal(size=3)*r*rng.uniform(0.01, 1.5)]
        for k2 in partners:
            for (a1, a2) in ((k1, k2), (k2, k1)):
                M, used, _ = L.glued(a1, a2, r, parts=True)
                assert np.isfinite(M).all(), (a1, a2)
                for u in used: cnt[u] = cnt.get(u, 0) + 1
                mx = max(mx, resid(M, a1, a2)); n += 1
    print(f'r={r}: {n} kernels at exact special points (0, +-1e-300, +-b, +-pi, mid-transition, random): all finite, no warnings;'
          f' pieces {cnt}; max W1 abs residual {mx:.2e}')
