"""Energy-based formation effect in the half-filled staggered sea (supplied toy).
F_x = (h_star - lambda_min) / (lambda_max - lambda_min), h_star = hopping on the 6 bonds of x's star.
Vacuum rate = <F_x> in the sea. Also the per-bond version. Dense L=8 antiperiodic torus (512 modes)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import itertools
import numpy as np
L = 8; N = L ** 3
idx = lambda x1, x2, x3: ((x1 % L) * L + (x2 % L)) * L + (x3 % L)
for m in (0.0, 0.5):
    h = np.zeros((N, N), complex)
    bonds = {}
    for x1, x2, x3 in itertools.product(range(L), repeat=3):
        i = idx(x1, x2, x3); eta = (1, (-1) ** x1, (-1) ** (x1 + x2))
        h[i, i] += m * (-1) ** (x1 + x2 + x3)
        for mu, st in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
            y = (x1 + st[0], x2 + st[1], x3 + st[2]); s = -1.0 if y[mu] == L else 1.0
            j = idx(*y); amp = 0.5j * eta[mu] * s
            h[j, i] += amp; h[i, j] += np.conj(amp); bonds[(i, j)] = amp
    e, v = np.linalg.eigh(h); P = v[:, e < 0] @ v[:, e < 0].conj().T
    c0 = idx(L // 2, L // 2, L // 2)
    star_b = [(i, j) for (i, j) in bonds if c0 in (i, j)]
    hs = np.zeros((N, N), complex)
    for (i, j) in star_b:
        hs[j, i] += bonds[(i, j)]; hs[i, j] += np.conj(bonds[(i, j)])
    E_star = np.trace(P @ hs).real
    sites = sorted({k for b in star_b for k in b})
    eps1 = np.linalg.eigvalsh(hs[np.ix_(sites, sites)])
    lam_min = eps1[eps1 < 0].sum(); lam_max = eps1[eps1 > 0].sum()
    # single bond
    i, j = star_b[0]; hb = np.zeros((N, N), complex); hb[j, i] = bonds[(i, j)]; hb[i, j] = np.conj(bonds[(i, j)])
    E_b = np.trace(P @ hb).real
    print(f"m={m}: E0/site = {np.sum(e[e<0])/N:.5f}; star energy {E_star:.5f} vs star min {lam_min:.5f} "
          f"(frustration {E_star-lam_min:.5f}; normalised vacuum rate {(E_star-lam_min)/(lam_max-lam_min):.5f}); "
          f"bond energy {E_b:.5f} vs bond min -0.5 (normalised vacuum rate {(E_b+0.5)/1.0:.5f})")
