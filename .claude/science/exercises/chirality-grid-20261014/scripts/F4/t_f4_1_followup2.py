# Follow-up 2 (13:42Z): random far V, lam=3 -> the mirror is an omega=0 Fermi pocket. Map the pocket radius
# along many directions, then take a sphere just outside it and compute the enclosed Chern number.
import numpy as np
from t_f4_1_slab_index import slab_H, sphere_chern
L = 4
rng = np.random.default_rng(7)
A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); Vr = (A + A.conj().T) / 2; Vr /= np.linalg.norm(Vr, 2)
H = lambda k: slab_H(k, L, far_term=3.0 * Vr)
rs = np.linspace(0.02, 1.6, 400)
radii = []
rng2 = np.random.default_rng(1)
for _ in range(60):
    d = rng2.normal(size=3); d /= np.linalg.norm(d)
    n = [np.sum(np.linalg.eigvalsh(H(r * d)) < 0) for r in rs]
    ch = [rs[i] for i in range(1, len(rs)) if n[i] != n[i - 1]]
    radii.append(max(ch) if ch else 0.0)
print("pocket outer radius over 60 random directions: min %.3f max %.3f" % (min(radii), max(radii)))
for rho in (max(radii) + 0.1, max(radii) + 0.25):
    C, g = sphere_chern(np.zeros(3), rho, H, nth=40, nph=80)
    print(f"sphere rho={rho:.3f}: Chern={None if C is None else round(C,3)} min|E|={g:.3g}")
# layer weight of the zero-energy pocket states
d = np.array([1.0, 0, 0]); 
for r in rs:
    w, v = np.linalg.eigh(H(r * d)); i = np.argmin(np.abs(w))
    if abs(w[i]) < 0.01:
        wt = [np.sum(np.abs(v[4*s:4*s+4, i])**2) for s in range(L)]
        print("pocket state on (1,0,0) at |k|=%.3f E=%.4f layer weights" % (r, w[i]), np.round(wt, 3)); break
