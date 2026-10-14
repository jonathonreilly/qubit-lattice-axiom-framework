"""Cross-check for K3-T1F (not a reading): with corner balls of radius 0.6 (the shell rmax used),
no grid point outside the balls has 2eps+ < 0.1 or 2eps+ > 2pi - 0.1."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
M = -2.0
corners = np.array([[x, y, z] for x in (0, np.pi) for y in (0, np.pi) for z in (0, np.pi)])
N = 72
g1 = (np.arange(N) + 0.5) * 2 * np.pi / N
KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
kk = np.stack([KX, KY, KZ], -1).reshape(-1, 3)
c = np.cos(kk); s = np.sin(kk); m = M - c.sum(-1); a = m / np.sqrt(m**2 + (s**2).sum(-1))
ep = np.arccos(np.clip(a, -1, 1))
dist = np.min(np.linalg.norm(((kk[:, None, :] - corners[None] + np.pi) % (2*np.pi)) - np.pi, axis=-1), axis=1)
for R, w in ((0.6, 0.1), (0.6, 0.2)):
    out = dist > R
    print(f"R={R} w={w}: outside-ball min 2eps+ = {2*ep[out].min():.4f}, max = {2*ep[out].max():.4f}; clean = {(2*ep[out].min() > w) and (2*ep[out].max() < 2*np.pi - w)}")
