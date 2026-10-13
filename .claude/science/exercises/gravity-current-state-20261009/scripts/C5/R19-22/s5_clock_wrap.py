"""R19-22 s5: Z_N clock in CCR scaling with EXACT stabilizer constraints (N0914:94-113): where is the wrap?

Pre-registered (06:36Z): (1) in any state invariant under the vector stabilizers (h-label shifts by G^T e_j), the
marginal of every h-slot label is uniform on Z_N (proof: each slot is shifted by +-1 by some stabilizer).
(2) Pure-gauge label configurations n = G^T lam mod N have centered labels c(n) = G^T lam - N w with integer wrap
pattern w; any operator built from an integer stencil A with A G^T = 0 (S here; R2 likewise, N0914:150) then gives
A c(n) = -N A w: values of size N, not small.  Check fraction of wrapped slots and |S c(n)|/N on random gauges.
Uses s3's stencils.
"""
import numpy as np, importlib.util, os
spec = importlib.util.spec_from_file_location("s3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "s3_hp_constraint_algebra.py"))
src = open(spec.origin).read().split("for L in [3, 4, 5]:")[0]
ns = {}; exec(src, ns); stencils = ns['stencils']
rng = np.random.default_rng(1)
L = 4; G, Sm = stencils(L)
for N in [16, 64, 256]:
    fr, mx, unif = [], [], []
    for trial in range(200):
        lam = rng.integers(0, N, size=G.shape[0])
        n = (G.T @ lam) % N
        c = np.where(n < (N+1)//2, n, n - N)
        w = (G.T @ lam - c)//N
        assert np.all(G.T @ lam - N*w == c)
        fr.append(np.mean(w != 0)); v = Sm @ c
        assert np.all(v == -N*(Sm @ w))
        mx.append(np.abs(v).max()/N)
        unif.append(n[0])
    h, _ = np.histogram(unif, bins=8, range=(0, N))
    print(f"N={N:4d}: mean fraction of wrapped slots = {np.mean(fr):.3f};  mean max|S c(n)|/N = {np.mean(mx):.2f};"
          f"  slot-0 label histogram (8 bins, 200 samples) = {h}")
print("Exact identity S c(n) = -N S w held on every sample (assert).")
