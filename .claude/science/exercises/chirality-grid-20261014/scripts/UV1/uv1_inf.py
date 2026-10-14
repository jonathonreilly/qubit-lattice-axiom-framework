"""UV-1 follow-up F1-a: beta_g -> infinity limit comparator K_inf^(t0) (PREREG F1).
Buffer and crossing plaquettes pinned to 0 (flat continuation of the witness); torus Polyakov variable w integrated by trapezoid.
usage: python3 uv1_inf.py torus T t0 K SEED          (W-matched greedy search on the middle slices t0..T+1-t0, then levels)
       python3 uv1_inf.py open POOL.npz IDX(comma)     (Stage-B witnesses at depth 1 and depth 2, open time)"""
import numpy as np, sys, time
from uv1_lib import *
from k2b_lib import admissible, perturb, normalized
from lat2d import rand_half
from k2c_lib import max_bulk

t00 = time.time()


def extend(w, T, t0, torus):
    """witness on slices t0..(T+1-t0) [torus] or t0..T [open] -> K2-format config on slices 1..T with flat buffers."""
    Tp = w['x'].shape[0]; ux = np.zeros((T, 2)); ut = np.zeros((T - 1, 2))
    ux[t0 - 1:t0 - 1 + Tp] = w['x']; ut[t0 - 1:t0 - 1 + Tp - 1] = w['t']
    ux[:t0 - 1] = w['x'][0]
    if torus: ux[t0 - 1 + Tp:] = w['x'][-1]
    return {'x': ux, 't': ut}


def entry_inf(G, ua, ub, nw, op, Fs, Bs):
    A = ub['x'][0] - ua['x'][0]; PhiA = wrap(A.sum())
    if G.torus:
        Bo = ua['x'][G.T - 1] - ub['x'][G.T - 1]; PhiB = wrap(Bo.sum())
        assert abs(PhiA) < 1e-12 and abs(PhiB) < 1e-12, (PhiA, PhiB)
        ws = 2 * np.pi * np.arange(nw) / nw
        ph = np.stack([np.zeros(nw), np.full(nw, -A[0]), ws, ws - Bo[0]], 1)
    else:
        assert abs(PhiA) < 1e-12, PhiA
        ph = np.array([[0.0, -A[0]]])
    l, g = point_logs(G, D_links(G.D0(ua, ub), Fs, Bs, ph), op)
    lm = l.real.max(); return lm + np.log(np.mean(np.exp(l - lm)) + 0j), (np.nanmin(g) if np.any(np.isfinite(g)) else np.inf)


def kmat(G, X, nw, op, Fs, Bs):
    k = len(X); L = np.full((k, k), -np.inf + 0j); gm = np.inf
    for a in range(k):
        for b in range(a, k):
            v, g = entry_inf(G, X[a], X[b], nw, op, Fs, Bs); gm = min(gm, g)
            L[a, b] = v if a != b else v.real
            if a != b: L[b, a] = np.conj(v)
    return L, gm


def evaluate(G, X, levels, tag):
    Fs, Bs = G.crossing_mats(); out = {}
    for op in ('O', 'W'):
        Ls = [kmat(G, X, nw, op, Fs, Bs) for nw in levels]
        Z = [normalized(L) for (L, g) in Ls]; k = len(X)
        q = np.abs(Z[1] - Z[0]).max(); q3 = np.abs(Z[2] - Z[1]).max() if len(Z) > 2 else 0.0
        E = k * max(q, q3) + 1e-13; a, b, ev = lam(Z[1]); out[op] = (a, b, E)
        lab = 'INF-NEG' if a < -10 * E else 'INF-PSD(within 10E)'
        print(f"FINAL {tag} {op}: k={k} lam_min {a:+.4e} min/max {a/b:+.4e} q {q:.1e} q3 {q3:.1e} E {E:.1e} -> {lab} | lowest {np.array2string(ev[:3], precision=3)} max {b:.3f} | min|H| {min(g for (_, g) in Ls):.3f} [{time.time()-t00:.0f}s]", flush=True)
    return out


if sys.argv[1] == 'torus':
    T, t0, K, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    G = Geom(2, T, True, 1); Tp = T + 2 - 2 * t0; assert Tp >= 1
    Gw = Geom(2, max(Tp, 2), False, -1); rng = np.random.default_rng(seed); Fs, Bs = G.crossing_mats(); nwlo = 8
    print(f"# UV-1 F1-a torus Lt={G.Lt} t0={t0}: witness slices {t0}..{T+1-t0} ({Tp} slices); K={K} seed={seed}", flush=True)
    WT0 = [None]
    def match(u):
        v = {'x': u['x'] - 0.5 * u['x'][0].sum(), 't': u['t'].copy()}
        if WT0[0] is None: WT0[0] = v['x'][-1].sum()
        v['x'][-1, 0] += wrap(WT0[0] - v['x'][-1].sum())
        if Tp == 1: v['x'][0, 1] = -v['x'][0, 0]
        return v if (Tp < 2 or admissible(Geom(2, Tp, False, -1), v, DB)) else None
    def rand_w():
        for _ in range(5000):
            if Tp >= 2:
                u = rand_half(rng, Geom(2, Tp, False, -1), 0.25, DB)
            else:
                u = {'x': rng.normal(0, 0.25, (1, 2)), 't': np.zeros((0, 2))}
            v = match(u)
            if v is not None: return v
        raise RuntimeError('no witness')
    def pert_w(u, sig):
        for _ in range(200):
            v = {'x': u['x'] + rng.normal(0, sig, u['x'].shape), 't': u['t'] + rng.normal(0, sig, u['t'].shape)}
            v = match(v)
            if v is not None: return v
        return None
    def ext(w): return extend(w, T, t0, True)
    def row(Xc, x):
        r = [entry_inf(G, a, x, nwlo, 'O', Fs, Bs) for a in Xc] + [entry_inf(G, x, x, nwlo, 'O', Fs, Bs)]
        return np.array([v for v, g in r], complex)
    def bordered(L, logs):
        k = L.shape[0]; M_ = np.full((k + 1, k + 1), -np.inf + 0j); M_[:k, :k] = L
        M_[:k, k] = logs[:k]; M_[k, :k] = np.conj(logs[:k]); M_[k, k] = logs[k].real; return M_
    Wl = []; X = []; L = np.zeros((0, 0), complex)
    for _ in range(8):
        w = rand_w(); x = ext(w); L = bordered(L, row(X, x)); Wl.append(w); X.append(x)
    a, b, _ = lam(normalized(L)); print(f"start k=8: lam_min {a:+.3e} min/max {a/b:+.3e} [{time.time()-t00:.0f}s]", flush=True)
    step = 0
    while len(X) < K:
        step += 1; best = None
        cands = [rand_w() for _ in range(4)] + [pert_w(Wl[rng.integers(len(Wl))], s) for s in (0.02, 0.05, 0.1, 0.2)]
        for w in cands:
            if w is None: continue
            x = ext(w); Lb = bordered(L, row(X, x)); a, b, _ = lam(normalized(Lb))
            if best is None or a < best[0]: best = (a, b, w, x, Lb)
        L = best[4]; Wl.append(best[2]); X.append(best[3])
        print(f"step {step}: k={len(X)} lam_min {best[0]:+.3e} min/max {best[0]/best[1]:+.3e} [{time.time()-t00:.0f}s]", flush=True)
    print(f"# witnesses: max|W(slice t0)| {max(abs(wrap(x['x'][t0-1].sum())) for x in X):.1e}, max|W(slice T+1-t0) - common| {max(abs(wrap(x['x'][T-t0].sum() - X[0]['x'][T-t0].sum())) for x in X):.1e}; "
          f"max witness bulk |plaq| {max(max_bulk(G, x) for x in X):.4f}; buffer plaquettes exactly 0 by construction", flush=True)
    np.savez(f"pool_UV1_inf_torus_Lt{G.Lt}_t0{t0}_seed{seed}.npz", ux=np.array([x['x'] for x in X]), ut=np.array([x['t'] for x in X]))
    evaluate(G, X, (8, 12, 16), f"torus Lt={G.Lt} t0={t0}")
else:
    pool = sys.argv[2]; idx = [int(i) for i in sys.argv[3].split(',')]; d = np.load(pool); T = d['ux'].shape[1]
    G = Geom(2, T, False, -1)
    U1 = [{'x': d['ux'][i], 't': d['ut'][i]} for i in idx]
    UD = [{'x': u['x'][:T-1].copy(), 't': u['t'][:T-2].copy()} for u in U1]
    print(f"# UV-1 F1-a open Lt={G.Lt} Stage-B witnesses {idx}", flush=True)
    evaluate(G, U1, (1, 1, 1), "open depth1 (beta=inf)")
    evaluate(G, [extend(w, T, 2, False) for w in UD], (1, 1, 1), "open depth2 (beta=inf)")
print(f"done [{time.time()-t00:.0f}s]", flush=True)
