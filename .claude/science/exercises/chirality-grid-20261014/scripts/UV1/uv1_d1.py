"""UV-1 depth-1 kernels (PREREG §4-5): one determinant pass per (level, op), all (arm, beta_g) from shared nodes.
usage: python3 uv1_d1.py POOL.npz torus|open [SUBSET(comma idx)|-] [EIGVEC_KEY arm:beta to save eigvec]"""
import numpy as np, sys, time
from uv1_lib import *
from k2c_lib import max_bulk

pool, gname = sys.argv[1], sys.argv[2]
subset = sys.argv[3] if len(sys.argv) > 3 else '-'
evkey = sys.argv[4] if len(sys.argv) > 4 else None
d = np.load(pool); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]
if subset != '-': U = [U[int(i)] for i in subset.split(',')]
k = len(U); T = d['ux'].shape[1]
if gname == 'torus':
    G = Geom(2, T, True, 1); lev = {'lo': (4, 4), 'hi': (6, 6), 'third': (8, 8)}
else:
    G = Geom(2, T, False, -1); lev = {'lo': (8, None), 'hi': (12, None), 'third': (16, None)}
Fs, Bs = G.crossing_mats(); t00 = time.time()
W1 = max(abs(wrap(u['x'][0].sum())) for u in U)
WT = (max(abs(wrap(u['x'][T-1].sum() - U[0]['x'][T-1].sum())) for u in U)) if G.torus else 0.0
print(f"# UV-1 depth-1 pool {pool} subset {subset} {gname} Lx=2 Lt={G.Lt} k={k} delta={DELTA} betas={BETAS} levels={lev}", flush=True)
print(f"# W-match: max|W1| {W1:.1e} max|W_T - W_T(0)| {WT:.1e}; max bulk |plaq| {max(max_bulk(G, u) for u in U):.4f}", flush=True)

rs = np.random.default_rng(99); pairs = set()
while len(pairs) < min(24, k * (k - 1) // 2):
    a_ = int(rs.integers(k)); b_ = int(rs.integers(k))
    if a_ != b_: pairs.add((min(a_, b_), max(a_, b_)))
pairs = sorted(pairs)


def logmats(n, nw, op, which):
    L = {key: np.full((k, k), -np.inf + 0j) for key in ARMS}; gm = np.inf
    for (a, b) in which:
        vals, g = entry_d1(G, U[a], U[b], n, nw, op, Fs, Bs); gm = min(gm, g)
        for key in ARMS:
            L[key][a, b] = vals[key]
            if a != b: L[key][b, a] = np.conj(vals[key])
            else: L[key][a, a] = vals[key].real
    return L, gm


allpairs = [(a, b) for a in range(k) for b in range(a, k)]
sub = sorted(set(pairs) | {(i, i) for i in range(k)})
res = {}
for op in ('O', 'W', 'PG'):
    Llo, glo = logmats(*lev['lo'], op, allpairs)
    Lhi, ghi = logmats(*lev['hi'], op, allpairs)
    L3, g3 = logmats(*lev['third'], op, sub)
    print(f"[{op} levels done {time.time()-t00:.0f}s; min|H| lo {glo:.3f} hi {ghi:.3f} third {g3:.3f}]", flush=True)
    for key in ARMS:
        Zlo = normalized(Llo[key]); Zhi = normalized(Lhi[key])
        d3 = L3[key].diagonal().real
        q = np.abs(Zhi - Zlo).max()
        q3 = max(abs(np.exp(L3[key][a, b] - 0.5 * (d3[a] + d3[b])) - Zhi[a, b]) for (a, b) in pairs)
        E = k * max(q, q3) + 1e-13; a, b, ev = lam(Zhi)
        res[(op, key)] = (a, b, E, ev)
        tag = 'NEG(conv)' if a < -10 * E else 'PSD-within-10E'
        print(f"FINAL {op:2s} arm={key[0]:4s} beta={key[1]:3.0f}: lam_min {a:+.4e} min/max {a/b:+.4e} q {q:.1e} q3 {q3:.1e} E {E:.1e} -> {tag} | lowest {np.array2string(ev[:3], precision=3)} max {b:.3f}", flush=True)
        if evkey and op == 'O' and f"{key[0]}:{key[1]:g}" == evkey:
            w_, V = np.linalg.eigh(Zhi); v = np.abs(V[:, 0]); order = np.argsort(-v)
            print(f"   eigvec |v| order (largest first): {','.join(str(i) for i in order)}; |v| {np.array2string(v[order], precision=3)}", flush=True)
    print(flush=True)
print("SUMMARY (O lam_min/max | E | W lam_min | PG lam_min):")
for key in ARMS:
    a, b, E, _ = res[('O', key)]; aw, _, Ew, _ = res[('W', key)]; ap, _, Ep, _ = res[('PG', key)]
    print(f"  {key[0]:4s} beta={key[1]:3.0f}: O {a:+.4e} ({a/b:+.3e}) E {E:.1e} {'NEG' if a < -10*E else 'psd'} | W {aw:+.2e} (E {Ew:.0e}) {'NEG!' if aw < -10*Ew else 'psd'} | PG {ap:+.2e} {'NEG!' if ap < -10*Ep else 'psd'}")
print(f"done [{time.time()-t00:.0f}s]", flush=True)
