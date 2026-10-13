"""R19-9: why the fibre identification I(k1,k2) is needed: with I = 1 the dust kernel is not continuous across BZ faces
(the rotated frame's twist T_l); with the site-averaged I it is. Both satisfy W1 pointwise (W1 is blind to I)."""
import numpy as np, lib199 as L
rng = np.random.default_rng(5); r = 0.1
def jump(off=1e-9):
    mx = 0.0; w1 = 0.0
    for _ in range(60):
        l = rng.integers(0, 3); k1 = rng.uniform(-np.pi, np.pi, 3); k1[l] = np.pi - off; k2 = rng.uniform(-np.pi, np.pi, 3)
        k1b = k1.copy(); k1b[l] = -np.pi + off
        T = np.ones(6); T[l] = -1; T[3:] = -1; T[3+l] = 1
        Ma = L.glued(k1, k2, r); Mb = L.glued(k1b, k2, r)
        mx = max(mx, np.abs(Ma - np.einsum('a,mnab->mnab', T, Mb)).max())
        w1 = max(w1, max(x[1] for x in L.w1_resid(Ma, k1, k2)))
    return mx, w1
orig = L.fiber_id
print('site-averaged I: face jump %.2e, W1 rel %.2e' % jump())
L.fiber_id = lambda k1, k2: np.eye(6)
print('I = 1          : face jump %.2e, W1 rel %.2e' % jump())
