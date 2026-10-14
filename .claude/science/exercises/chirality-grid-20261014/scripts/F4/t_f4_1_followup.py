# Follow-up (dated 13:40Z, after seeing T-F4-1): random far-layer V at lam=3 gave k=0 sphere Chern -1 with
# a near-gapless sphere; locate the displaced mirror node and check the total with larger spheres.
import numpy as np
from t_f4_1_slab_index import slab_H, sphere_chern, G5, corner_report
L = 4
rng = np.random.default_rng(7)
A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); Vr = (A + A.conj().T) / 2; Vr /= np.linalg.norm(Vr, 2)
H = lambda k: slab_H(k, L, far_term=3.0 * Vr)
for rho in (0.2, 0.5, 0.8, 1.1):
    C, g = sphere_chern(np.zeros(3), rho, H, nth=36, nph=72)
    print(f"random V lam=3: k=0 sphere rho={rho}: Chern={None if C is None else round(C,3)} min|E|={g:.3g}")
# minimal |E| search on a coarse grid near k=0
best = (9, None)
for k1 in np.linspace(-0.8, 0.8, 33):
    for k2 in np.linspace(-0.8, 0.8, 33):
        for k3 in np.linspace(-0.8, 0.8, 33):
            e = np.min(np.abs(np.linalg.eigvalsh(H(np.array([k1, k2, k3])))))
            if e < best[0]:
                best = (e, (round(k1,3), round(k2,3), round(k3,3)))
print("min |E| on grid |k_i|<=0.8:", best)
corner_report(H, rho=0.35, label="random lam=3")
