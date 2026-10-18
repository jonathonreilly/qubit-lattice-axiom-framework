"""NT-1 diagnostic D1' (PREREG follow-up F1): flux insertion at a middle slice; does the current K(s) stay local?
Adds 0.05 to both x-links of every slice t >= t0 (W(t) += 0.1 there; only the plaquettes between t0-1 and t0 change).
usage: python3 nt1_d1p.py POOL.npz T t0"""
import numpy as np, sys
from nt1_lib import *
from lat2d import Geom, nodes
fn, T, t0 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); G = Geom(2, T, False, -1); LK = Links(G)
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
cfg = []
for (a, b) in [(0, 1), (2, 3), (4, 5)]:
    ph, w = nodes(G, U[a], U[b], 0.6, 16, 'hard'); i = len(w) // 3; cfg.append(LK.joined(U[a], U[b], ph[i:i+1]))
A = np.concatenate(cfg); Ab = A.copy()
for t in range(t0, T + 1):
    for x in range(2): Ab[:, LK.key[('x', x, t)]] += 0.05
print(f"# D1' pool={fn} Lt={G.Lt} flux insertion between slices t={t0-1} and t={t0} (slice index {t0-1+T-1}|{t0+T-1}); K(s) = current through slice boundary s -> s+1")
for mdl in ('11112', 'L1', '345'):
    CH = Chiral(LK, mdl, Ns=32, sk=-1); _, Pa = CH.logrho(A, parts=True); _, Pb = CH.logrho(Ab, parts=True)
    dK = (Pb['K'] - Pa['K']).mean(0); coef = sum(m * e * e * (1 if c == 'L' else -1) for (e, c, m) in MODELS[mdl])
    print(f"[{mdl}] sum_L e^2 - sum_R e^2 = {coef}; min|H| {min(Pa['gmin'], Pb['gmin']):.3f}; mean dK(s), s = 0..Lt-1:")
    print("   " + " ".join(f"{v:+.2e}" for v in dK))
    print(f"   prediction for a pure (coef/2pi) F/2 flux term on the far side: {coef * (-0.1) / (2 * np.pi) / 2:+.3e}")
