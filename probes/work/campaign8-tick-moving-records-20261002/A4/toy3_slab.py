"""Coexistence of a flat jam slab with its vapour under crowd-tilted moves (no formation).
usage: python3 toy3_slab.py D g1,g2,... [T]
2D: 64 x 64; 3D: 32 x 24 x 24. Slab = middle half along axis 0. Gas pre-seeded at e^{-zg/2}, slab holes at e^{-zg/2}.
Measures, averaged over the second half of the run:
  rho_v  = record density in the gas core (columns >= 6 from the initial interfaces),
  h_l    = hole density in the slab core,
  M_gas, M_slab = moves per site per tick in the two cores,
  net    = drift of the slab-core record count (should be ~0 at coexistence).
"""
import sys, time
import numpy as np
from t1lib import move_phase
D = int(sys.argv[1]); gs = [float(v) for v in sys.argv[2].split(",")]
T = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
shape = (64, 64) if D == 2 else (32, 24, 24)
L0 = shape[0]; z = 2 * D
lo, hi = L0 // 4, 3 * L0 // 4
x = np.arange(L0)
gas_core = (x < lo - 6) | (x >= hi + 6)
slab_core = (x >= lo + 6) & (x < hi - 6)
for g in gs:
    rng = np.random.default_rng(int(100 * g) + D)
    guess = np.exp(-z * g / 2)
    occ = rng.random(shape) < guess
    sl = [slice(None)] * D; sl[0] = slice(lo, hi)
    occ[tuple(sl)] = rng.random(occ[tuple(sl)].shape) >= guess
    expg = np.exp(g * np.arange(z + 1))
    t0 = time.time(); acc = []
    for t in range(1, T + 1):
        occ, mv, arr, w = move_phase(occ, g, rng, expg)
        if t > T // 2 and t % 10 == 0:
            ax = tuple(range(1, D))
            col = occ.mean(axis=ax); colm = mv.mean(axis=ax)
            acc.append((col[gas_core].mean(), 1 - col[slab_core].mean(), colm[gas_core].mean(), colm[slab_core].mean()))
    a = np.array(acc); m = a.mean(axis=0); se = a.std(axis=0) / np.sqrt(len(a) / 10)  # ~10-sample blocks correlated
    print(f"D={D} g={g:4.2f}: rho_v={m[0]:.5f}(+-{se[0]:.5f}) h_l={m[1]:.5f}(+-{se[1]:.5f}) ratio h_l/rho_v={m[1]/m[0]:.3f} "
          f"| e^(-zg/2)={guess:.5f} rho_v/e^(-zg/2)={m[0]/guess:.3f} | M_gas={m[2]:.5f} M_slab={m[3]:.5f} [{time.time()-t0:.1f}s]", flush=True)
