"""UV-1 F2-b (descriptive): time locality of the free Neuberger overlap (M = 1), torus Lt = 20, Lx = 2, all links 1."""
import numpy as np
from lat2d import Geom
T = 10; G = Geom(2, T, True, 1); N = G.N
ua = {'x': np.zeros((T, 2)), 't': np.zeros((T - 1, 2))}
D = G.full_D(ua, ua, np.zeros(4))
H = G.g5d[:, None] * (D - np.eye(N)); w, V = np.linalg.eigh(H)
S = (V * np.sign(w)) @ V.conj().T; Dov = np.eye(N) + G.g5d[:, None] * S
print(f"# free overlap, torus Lt={G.Lt}, Lx=2, M=1; min|eig H_W| {np.abs(w).min():.3f}")
src = G.idx(0, 1); rows = []
for dt in range(0, T + 1):
    t1 = 1 + dt
    if t1 > T: t1 -= 2 * T
    nb = max(np.linalg.norm(Dov[src:src+2, G.idx(x, t1):G.idx(x, t1)+2], 2) for x in range(2))
    rows.append(nb); print(f"dt {dt:2d}: max block norm {nb:.3e}")
r = np.array(rows); k = np.arange(len(r)); sel = (k >= 2) & (k <= 7)
nu = -np.polyfit(k[sel], np.log(r[sel]), 1)[0]
print(f"fitted decay rate nu (dt = 2..7) = {nu:.3f} per lattice spacing; e^nu = {np.exp(nu):.2f}")
