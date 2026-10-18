"""NT-1' diagnostic (descriptive): where do the monopole defects m_p and the Wilson-line response h(x) of 11112 sit?
m_p per plaquette row (time) at the full field (u = 1), h(x) per slice; scaling with the field amplitude.  usage: Lx T model"""
import numpy as np, sys
from nt1p_lib import *
from lat2d import Geom, rand_half
Lx, T, model = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
S = Strip(Lx, T); G = Geom(Lx, T, False, -1); rng = np.random.default_rng(301); MS = Measure(S, model)
ua = rand_half(rng, G, 0.25, 0.55); ub = rand_half(rng, G, 0.25, 0.55); ph = rng.normal(0, 0.25, (1, Lx))
A0 = S.canon(S.joined(ua, ub, ph)); F, W = S.FW(A0)
print(f"# {model} Lx={Lx} Lt={2*T}; Wilson lines per slice: " + " ".join(f"{w:+.3f}" for w in W[0]))
for amp in (0.25, 0.5, 1.0):
    A = amp * A0; r = {}
    out = []
    for e in MS.charges:
        w, V = eig_H(S, e * A); out.append((e, w, V))
    R = sum(MS.coef[e] * e * dq_dA(S, e * A, w, V) for (e, w, V) in out)
    gup = np.einsum('pxl,ql->pqx', R, S.Sup); gdn = np.einsum('pxl,ql->pqx', R, S.Sdn)
    g = np.where(S.use_up[None], gup, gdn); m = g.sum(-1)[0].reshape(2 * T - 1, Lx); h = (R @ S.Wunif)[0].reshape(2 * T, Lx)
    print(f"amp {amp}: m_p by plaquette row (mean over x): " + " ".join(f"{v:+.2e}" for v in m.mean(1)) + f" | spread over x {np.abs(m - m.mean(1, keepdims=True)).max():.1e}")
    print(f"          h(x) summed per slice: " + " ".join(f"{v:+.2e}" for v in h.sum(1)) + f"; sum {h.sum():+.1e}")
