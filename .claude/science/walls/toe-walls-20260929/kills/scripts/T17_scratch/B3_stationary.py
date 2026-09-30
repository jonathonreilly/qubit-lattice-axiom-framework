"""Is the uniform measure stationary for V* (L-conserving clause) vs the original clause?  Cost of the route.
Continuous-time chain on the 4x4 torus, N records.  Rates: streaming attempt rate 1 per record (S1 move / S2 exchange
for parallel-antiparallel; perpendicular blocked in V*, exchanged in the original), plaquette class re-draw: each ordered pair
(c -> c') inside a plaquette class at rate gamma (symmetric, uniform stationary by itself).
We solve for the stationary distribution on the largest communicating class of the sector (P, Lz mod 4) with the most
states and report total-variation distance from uniform on it."""
import sys, itertools
sys.argv = ['B', '4', '4']
import importlib.util
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
spec = importlib.util.spec_from_file_location('B', 'B_ergodic_2d.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)

def stream_events(cfg, perp):
    out = []
    for s, k in cfg.items():
        x, y = B.xy(s)
        t = B.site(x + B.E[k][0], y + B.E[k][1])
        if t not in cfg:
            n = dict(cfg); del n[s]; n[t] = k; out.append(n)
        else:
            k2 = cfg[t]
            if k2 == k:
                continue
            if k2 == B.OPP[k] or perp:
                n = dict(cfg); n[s] = k2; n[t] = k; out.append(n)
    return out

def scatter_events(cfg):
    out = []
    for pl in B.PLAQ:
        sg = [B.site(*p) for p in pl]
        occ = [i for i in range(4) if sg[i] in cfg]
        if len(occ) < 2: continue
        ol = [B.LOCAL[i] for i in occ]; ct = tuple(cfg[sg[i]] for i in occ)
        for cand in B.moves_cached(ol, ct):
            n = dict(cfg)
            for i, kk in zip(occ, cand): n[sg[i]] = kk
            out.append(n)
    return out

def stationary(N, perp, gamma=1.0):
    cfgs = []
    for occ in itertools.combinations(range(B.NS), N):
        for ks in itertools.product(range(4), repeat=N):
            cfgs.append(dict(zip(occ, ks)))
    codes = {B.code(c): i for i, c in enumerate(cfgs)}
    rows, cols, rates = [], [], []
    for i, c in enumerate(cfgs):
        for n in stream_events(c, perp):
            rows.append(i); cols.append(codes[B.code(n)]); rates.append(1.0)
        for n in scatter_events(c):
            rows.append(i); cols.append(codes[B.code(n)]); rates.append(gamma)
    M = len(cfgs)
    R = sp.csr_matrix((rates, (rows, cols)), shape=(M, M))
    # components
    ncomp, lab = sp.csgraph.connected_components(R, directed=True, connection='strong')
    sizes = np.bincount(lab)
    return cfgs, R, lab, sizes

N = int(sys.argv[1]) if False else 3
for perp in (False, True):
    cfgs, R, lab, sizes = stationary(N, perp)
    # choose the largest strongly connected class that is closed (no outflow)
    order = np.argsort(-sizes)
    best = None
    for c in order:
        idx = np.where(lab == c)[0]
        sub = R[idx][:, idx]
        outflow = R[idx].sum() - sub.sum()
        if outflow == 0 and len(idx) > 500:
            best = (c, idx, sub); break
    if best is None:
        print('perp', perp, ': no large closed class found; largest sizes', sizes[order[:5]]); continue
    c, idx, sub = best
    n = len(idx)
    # generator Q = sub - diag(rowsum); solve pi Q = 0
    Q = sub - sp.diags(np.asarray(sub.sum(axis=1)).ravel())
    A = Q.T.tolil(); A[0, :] = 1.0
    b = np.zeros(n); b[0] = 1.0
    pi = spl.spsolve(A.tocsc(), b)
    u = np.full(n, 1.0 / n)
    tv = 0.5 * np.abs(pi - u).sum()
    print(f'N={N} perpendicular-exchange={perp}: closed class of {n} configurations; TV distance from uniform = {tv:.4f}; '
          f'max/min stationary weight = {pi.max()/pi.min():.3f}')
