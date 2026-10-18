"""K2b follow-up V3 (PREREG.md): PV-subtracted Shamir DWF kernel vs L_s on given pools, via the transfer-matrix formula
det D5(mf)/det D5(1) = det[(1+mf)/2 + (1-mf)/2 g5 (1 - T^Ls)/(1 + T^Ls)], T = (1 - H_T)/(1 + H_T), H_T = g5 A (2+A)^{-1}.
The formula is first checked against the dense 5D determinant ratio (k2b_lib 'D5PV') at L_s = 4, 8 (required < 1e-10).
usage: python3 k2b_v3_dwf_Ls.py POOL [POOL ...]  (npz pool files, or g1p_262_s1-style names)"""
import numpy as np, sys, time
from lat2d import Geom, rand_half, nodes
from k2b_lib import *

LS = [4, 6, 8, 12, 16, 24, 32, 48]; delta = 0.6


def load(name):
    if name.endswith('.npz'):
        d = np.load(name); torus = '_torus_' in name; T = d['ux'].shape[1]
        G = Geom(2, T, torus, 1 if torus else -1); return G, [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]
    tag, seed, si = name.split('_'); si = int(si[1:])
    G = {'g1p': Geom(2, 6, False, -1), 'v6': Geom(2, 10, False, -1), 'g3p': Geom(2, 6, True, 1)}[tag]
    rng = np.random.default_rng(int(seed)); sets = [[rand_half(rng, G, 0.25, delta) for _ in range(8)] for _ in range(si + 1)]
    return G, sets[si]


def formula_logs(G, Db):
    N = G.N; Id = np.eye(N); g5 = G.g5d
    Am = Db - M0 * Id[None]
    H = g5[None, :, None] * (Am @ np.linalg.inv(2 * Id[None] + Am)); H = 0.5 * (H + np.conj(np.swapaxes(H, 1, 2)))
    w, V = np.linalg.eigh(H); t = (1 - w) / (1 + w); out = {}
    for Ls in LS + ['inf']:
        if Ls == 'inf':
            eps = np.sign(w)
        else:
            with np.errstate(over='ignore', divide='ignore', invalid='ignore'):
                small = np.abs(t) <= 1; ti = np.where(small, 1.0, 1.0 / np.where(t == 0, 1.0, t))
                eps = np.where(small, (1 - t ** Ls) / (1 + t ** Ls), (ti ** Ls - 1) / (ti ** Ls + 1))
        S = (V * eps[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
        A = 0.5 * (1 + MF) * Id[None] + 0.5 * (1 - MF) * g5[None, :, None] * S
        sg, ld = np.linalg.slogdet(A); out[Ls] = ld + np.log(sg.astype(complex))
    return out, np.abs(w).min(1)


t00 = time.time()
for name in sys.argv[1:]:
    G, U = load(name); Fs, Bs = G.crossing_mats(); k = len(U)
    qlo, qhi = ((4, 4), (6, 6)) if G.torus else ((16, None), (32, None))
    # formula check against dense 5D ratio on 3 points of pair (0, 1)
    ph, w = nodes(G, U[0], U[1], delta, 4, 'tri', 4 if G.torus else None); Db = D_batch(G, G.D0(U[0], U[1]), Fs, Bs, ph[:3])
    f, _ = formula_logs(G, Db); chk = max(np.abs(f[Ls] - logdet_op(G, Db, 'D5PV', Ls)[0]).max() for Ls in (4, 8))
    print(f"# V3 pool {name}: Lt={G.Lt} torus={G.torus} k={k}; formula vs dense D5PV (L_s=4,8): max|d logdet| {chk:.1e}", flush=True)
    if chk > 1e-10: print("FORMULA CHECK FAILED: skipped"); continue
    res = {}
    for (n, nw) in (qlo, qhi):
        L = {Ls: np.full((k, k), -np.inf + 0j) for Ls in LS + ['inf']}; gm = np.inf
        for a in range(k):
            for b in range(a, k):
                ph, w = nodes(G, U[a], U[b], delta, n, 'tri', nw)
                if len(w) == 0 or w.sum() <= 0: continue
                D0 = G.D0(U[a], U[b]); acc = {Ls: [] for Ls in L}
                for c in range(0, len(w), 32):
                    o, g = formula_logs(G, D_batch(G, D0, Fs, Bs, ph[c:c+32])); gm = min(gm, g.min())
                    for Ls in L: acc[Ls].append(o[Ls])
                for Ls in L:
                    l = np.concatenate(acc[Ls]); lm = l.real.max(); v = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
                    L[Ls][a, b] = v; L[Ls][b, a] = np.conj(v)
        for Ls in L:
            for a in range(k): L[Ls][a, a] = L[Ls][a, a].real
        res[(n, nw)] = ({Ls: normalized(L[Ls]) for Ls in L}, gm)
    lo, hi = res[qlo][0], res[qhi][0]
    print(f"   min|eig H_T| {min(res[qlo][1], res[qhi][1]):.3f}  [{time.time()-t00:.0f}s]")
    for Ls in LS + ['inf']:
        q = np.abs(hi[Ls] - lo[Ls]).max(); E = k * q + 1e-13; a, b, ev = lam(hi[Ls])
        print(f"   DWF L_s={str(Ls):4s}: lam_min {a:+.4e} min/max {a/b:+.4e} E {E:.1e} certified-negative {a < -10*E}", flush=True)
print(f"done [{time.time()-t00:.0f}s]")
