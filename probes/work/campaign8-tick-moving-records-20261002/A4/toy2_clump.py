"""Toy 2: clumping from a uniform random start under crowd-tilted moves (no formation), 2D periodic L x L.
usage: python3 toy2_clump.py rho g1,g2,... [L] [T]
Reports, at checkpoints: B = <recorded neighbours of a record>/(z rho) (1 = uniform),
S_low = structure factor averaged over the smallest k-shells / (rho(1-rho)) (1 = uniform),
f_full = fraction of records with all z neighbours recorded, Cmax = largest 4-connected cluster / records,
M = moves per site per tick.
"""
import sys, time
import numpy as np
from scipy import ndimage
from t1lib import move_phase, neighbour_count

rho = float(sys.argv[1]); gs = [float(v) for v in sys.argv[2].split(",")]
L = int(sys.argv[3]) if len(sys.argv) > 3 else 128
T = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
kx = np.fft.fftfreq(L) * L
KX, KY = np.meshgrid(kx, kx, indexing="ij")
K2 = KX ** 2 + KY ** 2
shell = (K2 > 0) & (K2 <= 4.5)  # |k| <= ~2 * 2pi/L : 12 modes
def measures(occ):
    nrec = neighbour_count(occ)
    r = occ.mean()
    B = nrec[occ].mean() / (4 * r)
    f = np.fft.fft2(occ - r)
    S = (np.abs(f) ** 2 / occ.size)[shell].mean() / (r * (1 - r))
    full = (nrec[occ] == 4).mean()
    lab, nl = ndimage.label(occ)
    cmax = np.bincount(lab.ravel())[1:].max() / occ.sum() if nl else 0
    return B, S, full, cmax
for g in gs:
    rng = np.random.default_rng(int(1000 * g) + 7)
    occ = rng.random((L, L)) < rho
    expg = np.exp(g * np.arange(5))
    t0 = time.time(); out = []
    mv = 0.0
    for t in range(1, T + 1):
        occ, moved, arr, wins = move_phase(occ, g, rng, expg)
        if t > T - 100: mv += moved.mean() / 100
        if t in (100, T // 2, T):
            out.append((t,) + measures(occ))
    s = " | ".join(f"t={t}: B={B:.3f} S_low={S:.2f} f_full={fu:.3f} Cmax={c:.3f}" for t, B, S, fu, c in out)
    print(f"rho={rho} g={g:4.2f}: {s} | M(last100)={mv:.4f} [{time.time()-t0:.1f}s]", flush=True)
