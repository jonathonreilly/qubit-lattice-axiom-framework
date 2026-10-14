"""Follow-up V2 (PREREG.md): beta_g weight robustness, (M, m) dependence, wrong-Theta negative control. G1p geometry."""
import numpy as np, sys
import lat2d as L
from lat2d import Geom, rand_half, mineig, wrap, logdet_batch, tri, interval_pieces, gl_interval
G = Geom(2, 6, False, -1); delta = 0.6; s = 0.25; k = 8
rng = np.random.default_rng(262)
sets = [[rand_half(rng, G, s, delta) for _ in range(k)] for _ in range(3)]
Fs, Bs = G.crossing_mats()
def kern(U, n, beta, op, M=1.0, m=0.05):
    Lg = np.full((k, k), -np.inf); Mt = np.zeros((k, k), complex)
    for a in range(k):
        for b in range(a, k):
            A = U[b]['x'][0] - U[a]['x'][0]; Phi = wrap(A.sum())
            lo = max(-delta, Phi - delta); hi = min(delta, Phi + delta)
            if hi <= lo: continue
            d0, w = gl_interval(interval_pieces(lo, hi, [0.0, Phi]), n)
            w = w * tri(d0, delta) * tri(Phi - d0, delta) * np.exp(beta * (np.cos(d0) + np.cos(Phi - d0)))
            ph = np.stack([np.zeros_like(d0), d0 - A[0]], 1)
            l, g = logdet_batch(G, G.D0(U[a], U[b]), Fs, Bs, ph, op, M, m)
            lm = l.real.max(); v = np.sum(w * np.exp(l - lm))
            Lg[a, b] = Lg[b, a] = lm; Mt[a, b] = v; Mt[b, a] = np.conj(v)
    d = Lg.diagonal(); md = Mt.diagonal().real
    return np.where(np.isfinite(Lg), Mt * np.exp(Lg - 0.5 * (d[:, None] + d[None, :])), 0) / np.sqrt(np.outer(md, md))
print("V2a: beta_g robustness (overlap M=1, m=0.05)")
for beta in [0.0, 1.0, 4.0, 10.0]:
    row = []
    for si in range(3):
        Zo16, Zo32 = kern(sets[si], 16, beta, 'O'), kern(sets[si], 32, beta, 'O')
        Zw = kern(sets[si], 32, beta, 'W')
        row.append(f"set{si}: O {mineig(Zo32):+.3e} (q {np.abs(Zo32-Zo16).max():.0e}) W {mineig(Zw):+.3e}")
    print(f"  beta={beta:5.1f} | " + " | ".join(row)); sys.stdout.flush()
print("V2b: (M, m) dependence on set 1 (beta = 0)")
for (M, m) in [(1.0, 0.05), (1.0, 0.3), (0.6, 0.05), (1.4, 0.05)]:
    Z16, Z32 = kern(sets[1], 16, 0.0, 'O', M, m), kern(sets[1], 32, 0.0, 'O', M, m)
    print(f"  M={M} m={m}: overlap min/max {mineig(Z32):+.3e} q {np.abs(Z32-Z16).max():.0e}"); sys.stdout.flush()
print("V2c: wrong-Theta negative control (Lambda- temporal links unconjugated), gauge-fixed kernels")
orig = Geom.links
def links_wrong(self, ua, ub):
    ax, at = orig(self, ua, ub)
    for t in range(1, self.T):
        for x in range(self.Lx): at[(x, -t)] = +ub['t'][t-1, x]
    return ax, at
rng2 = np.random.default_rng(99)
for label, fn in [("correct Theta", orig), ("WRONG Theta", links_wrong)]:
    Geom.links = fn; worst = {'W': 1, 'O': 1}; herm = {'W': 0, 'O': 0}
    for rep in range(4):
        U = [rand_half(rng2, G, 0.3, 1.5) for _ in range(k)]
        for op in ['W', 'O']:
            Lm = np.zeros((k, k), complex)
            for a in range(k):
                for b in range(k):
                    Lm[a, b] = logdet_batch(G, G.D0(U[a], U[b]), Fs, Bs, np.zeros((1, 2)), op)[0][0]
            Z = np.exp(Lm - 0.5 * (Lm.diagonal()[:, None] + Lm.diagonal()[None, :]))
            worst[op] = min(worst[op], mineig(Z)); herm[op] = max(herm[op], np.abs(Z - Z.conj().T).max())
    print(f"  {label}: Wilson gauge-fixed min/max {worst['W']:+.2e} (herm defect {herm['W']:.1e}) | overlap {worst['O']:+.2e} (herm {herm['O']:.1e})"); sys.stdout.flush()
Geom.links = orig
print("done")
