"""A34 c12: is A39 c1's 72% (excited vacuum) vs 100% (calmest-state control) a fair comparison? (own code)

A39 c1's control makes |0>^N the lowest state by adding a field (W + 0.5) * N to the pi-flux hopping, which also opens
a gap of 0.5 per flip. Here: the same 4x3 pi-flux torus (12 qubits) and the same slow on-off cycle of delta * sum X,
delta(t) = delta * sin^2(pi t / 400), dt = 0.5, with the control field set to W + 0.5 (A39's control, replicated),
W + 0.1 (smaller gap) and exactly W (|0>^N still a lowest state, but gapless: the one-flip band bottom sits at 0).
Usage: python c12_fragility_control.py <field offset or 'none'> <delta>
Prints: states within 0.05 of E_Omega (all flip-number blocks), back-to-vacuum probability, flip density.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys, signal, time
import numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
signal.alarm(28)
t0 = time.time()
Lx, Ly = 4, 3
N = Lx * Ly; D = 1 << N
idx = lambda x, y: (x % Lx) + Lx * (y % Ly)
bonds = []
for y in range(Ly):
    for x in range(Lx):
        bonds.append((idx(x, y), idx(x + 1, y), 1.0))
        bonds.append((idx(x, y), idx(x, y + 1), (-1.0) ** x))
states = np.arange(D, dtype=np.int64)
nflip = np.array([bin(s).count("1") for s in range(D)], dtype=float)
rows, cols, vals = [], [], []
for (i, j, e) in bonds:
    m = ((states >> i) & 1) != ((states >> j) & 1)
    s = states[m]; rows.append(s ^ ((1 << i) | (1 << j))); cols.append(s); vals.append(np.full(s.size, -e))
Hpi = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(D, D))
X = sp.csr_matrix((np.ones(N * D), (np.concatenate([states ^ (1 << i) for i in range(N)]), np.tile(states, N))),
                  shape=(D, D))
one = [1 << i for i in range(N)]
e1 = np.linalg.eigvalsh(Hpi[one][:, one].toarray()); W = -e1.min()
off, delta = sys.argv[1], float(sys.argv[2])
H = Hpi if off == "none" else (Hpi + (W + float(off)) * sp.diags(nflip)).tocsr()
res = 0; emin = np.inf
for n in range(1, N + 1):
    sel = np.where(nflip == n)[0]
    ev = np.linalg.eigvalsh(H[sel][:, sel].toarray()); res += int((np.abs(ev) < 0.05).sum()); emin = min(emin, ev.min())
v = np.zeros(D, complex); v[0] = 1.0
Ttot, dt = 400.0, 0.5
for k in range(int(Ttot / dt)):
    d = delta * np.sin(np.pi * (k + 0.5) * dt / Ttot) ** 2
    v = expm_multiply(-1j * dt * (H + d * X), v)
p = np.abs(v) ** 2
lab = "pi-flux, no field (Omega not lowest)" if off == "none" else f"pi-flux + field W{float(off):+.2f} (Omega lowest)"
print(f"{lab}: lowest excitation above E_Omega {emin:+.4f}; states within 0.05 of E_Omega {res}; "
      f"delta={delta}: back-to-vacuum {p[0]:.4f}, flip density {p @ nflip / N:.2e}  [{time.time() - t0:.1f} s]")
