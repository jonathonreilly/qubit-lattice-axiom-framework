"""K2c follow-up V7 (PREREG.md): bare dense D5 (L_s = 4, 8) + hard weight on the W-matched torus pool."""
import numpy as np, sys, time
from k2c_lib import *
POOL = 'pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz'
d = np.load(POOL); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]; k = len(U); T = d['ux'].shape[1]
G = Geom(2, T, True, 1); Fs, Bs = G.crossing_mats(); t00 = time.time()
def ent(a, b, n, nw, Ls):
    ph, w = nodes(G, U[a], U[b], DELTA, n, 'hard', nw); D0 = G.D0(U[a], U[b]); ls = []
    for c in range(0, len(w), 8):
        l, _ = logdet_op(G, D_batch(G, D0, Fs, Bs, ph[c:c+8]), 'D5', Ls); ls.append(l)
    l = np.concatenate(ls); lm = l.real.max(); return lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
for Ls in (4, 8):
    L = np.zeros((k, k), complex)
    for a in range(k):
        for b in range(a, k):
            L[a, b] = ent(a, b, 6, 4, Ls); L[b, a] = np.conj(L[a, b])
    for a in range(k): L[a, a] = L[a, a].real
    Z = normalized(L); lo, hi, ev = lam(Z)
    rs = np.random.default_rng(7); sub = sorted({(int(min(p)), int(max(p))) for p in rs.integers(0, k, (14, 2)) if p[0] != p[1]})[:10]
    dd = np.array([ent(i, i, 8, 6, Ls).real for i in range(k)]); ch = 0.0
    for (a, b) in sub:
        v = ent(a, b, 8, 6, Ls); ch = max(ch, abs(np.exp(v - 0.5 * (dd[a] + dd[b])) - Z[a, b]))
    E = k * ch + 1e-13
    print(f"V7 D5_{Ls} (torus, hard, (6,4)): lam_min {lo:+.4e} min/max {lo/hi:+.4e} | subset change to (8,6) {ch:.1e} -> E {E:.1e} | certified-negative {lo < -10*E} PSD-within-error {lo > -10*E} | lowest {np.array2string(ev[:3], precision=3)} [{time.time()-t00:.0f}s]", flush=True)
print("done")
