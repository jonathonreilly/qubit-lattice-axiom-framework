"""A41 d8: pi flux, theta = pi/2: zero-mode counts of H6 at the 64 points of (pi/2)Z^3 mod 2pi; which axis lines
{k_b in {0,pi}, k_c = +-pi/2, k_a free} carry two zero modes all along (121 points each); isotropy of the cone at
every isolated zero (300 directions)."""
import os, signal, itertools
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from common import *
M = M_family(np.pi / 2); rng = np.random.default_rng(31)
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
iso = []
for p in itertools.product(range(4), repeat=3):
    k = np.array(p) * np.pi / 2; e = np.linalg.eigvalsh(H6(k, M)); n0 = int(np.sum(np.abs(e) < 1e-9))
    if n0:
        sl = np.array([np.sort(np.abs(np.linalg.eigvalsh(H6(k + 1e-6 * u, M))))[:n0] / 1e-6 for u in dirs])
        iso.append((p, n0, sl.min(), sl.max()))
print(f"(pi/2)Z^3 points with H6 zero modes: {len(iso)}")
for p, n0, a, b in iso:
    print(f"   k/(pi/2) = {p}: {n0} zero modes; |slope| over 300 directions {a:.4f}..{b:.4f}")
s = np.linspace(-np.pi, np.pi, 121); lines = []
for a, b in itertools.permutations(range(3), 2):
    c = 3 - a - b
    for kb, kc in itertools.product((0.0, np.pi), (np.pi / 2, -np.pi / 2)):
        K = np.zeros((121, 3)); K[:, b] = kb; K[:, c] = kc; K[:, a] = s
        z = np.sort(np.abs(np.linalg.eigvalsh(H6(K, M))), 1)[:, 1].max()
        if z < 1e-9: lines.append((a, b, kb, c, kc))
print(f"axis lines with two zero modes all along: {len(lines)} of 24:",
      "; ".join(f"k{'xyz'[a]} free, k{'xyz'[b]}={kb/np.pi:.0f}pi, k{'xyz'[c]}={kc/np.pi:+.1f}pi" for a, b, kb, c, kc in lines))
print(f"exact constant check: 2 sqrt2/3 = {2*np.sqrt(2)/3:.6f}, sqrt6 = {np.sqrt(6):.6f}")
