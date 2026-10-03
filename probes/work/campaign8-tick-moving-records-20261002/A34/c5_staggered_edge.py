"""A34 c5: A28's edge floor for the STAGGERED (Kogut-Susskind, pi-flux) half-filled sea.

A28 proved full rank next to a planar wall for the uniform free-fermion sea and left the staggered sea
ARGUED. Here: KS hopping signs eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^(x+y) on an Lx x L x L box,
walls (records) at x = 0 and x = Lx+1 (open), antiperiodic in y and z (avoids exact zero modes).
Half filling: all negative-energy states. Star next to the wall: site (1, y0, z0) and its five
unrecorded neighbours. Gaussian state: the 6-site marginal is full rank iff all eigenvalues nu of the
restricted correlation matrix lie strictly inside (0, 1); smallest many-body eigenvalue = prod min(nu, 1-nu).
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal, sys
import numpy as np
signal.alarm(28)

def run(Lx, L):
    sites = [(x, y, z) for x in range(1, Lx + 1) for y in range(L) for z in range(L)]
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    H = np.zeros((n, n))
    for (x, y, z), i in idx.items():
        if x + 1 <= Lx:
            j = idx[(x + 1, y, z)]; H[i, j] = H[j, i] = -1.0
        yy = (y + 1) % L; s = -1.0 if y + 1 == L else 1.0          # antiperiodic wrap
        j = idx[(x, yy, z)]; amp = -s * (-1) ** x; H[i, j] = H[j, i] = amp
        zz = (z + 1) % L; s = -1.0 if z + 1 == L else 1.0
        j = idx[(x, y, zz)]; amp = -s * (-1) ** (x + y); H[i, j] = H[j, i] = amp
    e, V = np.linalg.eigh(H)
    occ = V[:, e < 0]
    gap = np.min(np.abs(e))
    out = []
    for (y0, z0) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y0 += L // 2; z0 += L // 2
        star = [(1, y0, z0), (2, y0, z0), (1, (y0 + 1) % L, z0), (1, (y0 - 1) % L, z0), (1, y0, (z0 + 1) % L), (1, y0, (z0 - 1) % L)]
        rows = [idx[s] for s in star]
        C = occ[rows] @ occ[rows].T
        nu = np.linalg.eigvalsh(C)
        out.append((min(nu.min(), 1 - nu.max()), np.prod(np.minimum(nu, 1 - nu)), nu))
    # bulk 7-star for contrast (centre of the box)
    xc = Lx // 2; yc = zc = L // 2
    star = [(xc, yc, zc), (xc + 1, yc, zc), (xc - 1, yc, zc), (xc, yc + 1, zc), (xc, yc - 1, zc), (xc, yc, zc + 1), (xc, yc, zc - 1)]
    rows = [idx[s] for s in star]
    nu = np.linalg.eigvalsh(occ[rows] @ occ[rows].T)
    bulk = (min(nu.min(), 1 - nu.max()), np.prod(np.minimum(nu, 1 - nu)))
    return gap, out, bulk

for Lx, L in [(8, 8), (10, 10), (12, 12)]:
    gap, out, bulk = run(Lx, L)
    print(f"Lx={Lx}, L={L}: single-particle gap at E=0: {gap:.3e}")
    for k, (mn, mb, nu) in enumerate(out):
        print(f"   wall star #{k}: nu in [{nu.min():.4f}, {nu.max():.4f}], min(nu,1-nu) = {mn:.4f}, smallest many-body eigenvalue = {mb:.3e}")
    print(f"   bulk 7-star: min(nu,1-nu) = {bulk[0]:.4f}, smallest many-body eigenvalue = {bulk[1]:.3e}")
