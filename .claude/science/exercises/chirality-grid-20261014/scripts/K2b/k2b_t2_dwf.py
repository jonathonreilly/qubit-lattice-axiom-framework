"""K2b-T2 (PREREG.md): domain-wall control. Per pool, seven gauge-invariant kernels from the SAME quadrature points:
W (Wilson), O (Neuberger overlap), SH (Shamir overlap = L_s -> inf), D5_4 / D5_8 (bare 5D det, proved PSD by OS),
DWF_4 / DWF_8 (PV-subtracted det D5(mf)/det D5(1)).
usage: python3 k2b_t2_dwf.py POOL   with POOL in g1p_262_s0 g1p_262_s1 g1p_262_s2 v6_9010_s1 g3p_565_s0 or an npz file"""
import numpy as np, sys, time
from lat2d import Geom, rand_half, nodes
from k2b_lib import *

name = sys.argv[1]; delta = 0.6; t00 = time.time()
if name.endswith('.npz'):
    d = np.load(name); torus = '_torus_' in name; T = d['ux'].shape[1]
    G = Geom(2, T, torus, 1 if torus else -1); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]
else:
    tag, seed, si = name.split('_'); seed = int(seed); si = int(si[1:])
    G = {'g1p': Geom(2, 6, False, -1), 'v6': Geom(2, 10, False, -1), 'g3p': Geom(2, 6, True, 1)}[tag]
    rng = np.random.default_rng(seed)
    sets = [[rand_half(rng, G, 0.25, delta) for _ in range(8)] for _ in range(si + 1)]; U = sets[si]
qlo, qhi = ((4, 4), (6, 6)) if G.torus else ((16, None), (32, None))
OPS = ['W', 'O', 'SH', 'D5_4', 'DWF_4', 'D5_8', 'DWF_8']
print(f"# K2b-T2 pool {name}: Lx={G.Lx} Lt={G.Lt} torus={G.torus} k={len(U)} quad lo={qlo} hi={qhi}", flush=True)
Fs, Bs = G.crossing_mats()


def point_logs(Db):
    out = {}
    out['W'], _ = logdet_op(G, Db, 'W')
    out['O'], g1 = logdet_op(G, Db, 'O')
    out['SH'], g2 = logdet_op(G, Db, 'SH')
    for Ls in (4, 8):
        a, _ = logdet_op(G, Db, 'D5', Ls); one, _ = logdet_op(G, Db, 'D5ONE', Ls)
        out[f'D5_{Ls}'] = a; out[f'DWF_{Ls}'] = a - one
    return out, min(np.nanmin(g1), np.nanmin(g2))


def kernels(n, nw):
    k = len(U); L = {op: np.full((k, k), -np.inf + 0j) for op in OPS}; gm = np.inf
    for a in range(k):
        for b in range(a, k):
            ph, w = nodes(G, U[a], U[b], delta, n, 'tri', nw)
            if len(w) == 0 or w.sum() <= 0: continue
            D0 = G.D0(U[a], U[b]); acc = {op: [] for op in OPS}
            ck = max(1, 1024 // (8 * G.N))
            for c in range(0, len(w), ck):
                o, g = point_logs(D_batch(G, D0, Fs, Bs, ph[c:c+ck])); gm = min(gm, g)
                for op in OPS: acc[op].append(o[op])
            for op in OPS:
                l = np.concatenate(acc[op]); lm = l.real.max(); v = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
                L[op][a, b] = v; L[op][b, a] = np.conj(v)
    for op in OPS:
        for a in range(k): L[op][a, a] = L[op][a, a].real
    return {op: normalized(L[op]) for op in OPS}, gm


Zlo, glo = kernels(*qlo); Zhi, ghi = kernels(*qhi); k = len(U)
print(f"min|eig H| over all points (Neuberger H_W and Shamir H_T): {min(glo, ghi):.3f}  [{time.time()-t00:.0f}s]")
for op in OPS:
    q = np.abs(Zhi[op] - Zlo[op]).max(); E = k * q + 1e-13; a, b, ev = lam(Zhi[op])
    print(f"{op:6s}: lam_min {a:+.4e} min/max {a/b:+.4e} q {q:.1e} E {E:.1e} certified-negative {a < -10*E} PSD-within-error {a > -10*E}"
          f" | lowest eigs {np.array2string(ev[:3], precision=3)}", flush=True)
print(f"done [{time.time()-t00:.0f}s]")
