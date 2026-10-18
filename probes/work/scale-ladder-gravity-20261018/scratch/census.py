"""Symmetry + redundancy census for quadratic spin-2 (and spin-1, scalar) forms on (t,x,y,z).

A form is a polynomial F(h,k) = Q(k)[h,h], degree 2 in the field and n in momentum.
Counts: forms invariant under a point group G; of those, gauge-invariant ones
(F(h + k xi^T + xi k^T, k) = F(h,k)); then on-shell TT content at n = 4.
Groups (index 0 = tick):
  B4      signed permutations of all four axes (384)
  B4+     proper part (192)
  K48     the Kuhn path complex's isometries: S4 x {+-1}  (48)
  OhT     spatial O_h x tick reversal (96)
  OT      spatial proper O x tick reversal (48)
  K12T    Kuhn spatial part S3 x {+-1} x tick reversal (24)
"""
import itertools, numpy as np
np.random.seed(1)

def perm_mats(n_axes_perm, signs):
    out = []
    for p in itertools.permutations(range(4)):
        if p not in n_axes_perm: continue
        for s in signs:
            M = np.zeros((4, 4))
            for i in range(4): M[p[i], i] = s[i]
            out.append(M)
    return out

allp = set(itertools.permutations(range(4)))
spatialp = {p for p in allp if p[0] == 0}
allsigns = list(itertools.product([1, -1], repeat=4))
G = {
    'B4': perm_mats(allp, allsigns),
    'K48': perm_mats(allp, [(1,)*4, (-1,)*4]),
    'OhT': perm_mats(spatialp, allsigns),
    'K12T': perm_mats(spatialp, [(1,)*4, (-1,)*4, (-1,1,1,1), (1,-1,-1,-1)]),
}
G['B4+'] = [g for g in G['B4'] if np.linalg.det(g) > 0]
G['OT'] = [g for g in G['OhT'] if np.linalg.det(g[1:, 1:]) > 0]

def monos(nvar, deg):
    return [c for c in itertools.combinations_with_replacement(range(nvar), deg)]

SYM = [(a, b) for a in range(4) for b in range(a, 4)]  # 10 components

def field_vec(h, spin):
    if spin == 2: return np.array([h[a, b] for a, b in SYM])
    if spin == 1: return h            # vector A_mu
    return np.array([h])              # scalar

def basis(spin, n):
    nf = {2: 10, 1: 4, 0: 1}[spin]
    return [(fm, km) for fm in monos(nf, 2) for km in monos(4, n)]

def evalF(B, hv, k):
    return np.array([np.prod(hv[list(fm)]) * np.prod(k[list(km)]) for fm, km in B])

def act(g, h, spin):
    if spin == 2: return g @ h @ g.T
    if spin == 1: return g @ h
    return h

def rand_field(spin, cplx=False):
    if spin == 2:
        a = np.random.randn(4, 4); return a + a.T
    if spin == 1: return np.random.randn(4)
    return np.random.randn()

def gauge_shift(h, k, spin):
    xi = np.random.randn(4)
    if spin == 2: return h + np.outer(k, xi) + np.outer(xi, k)
    if spin == 1: return h + k * np.random.randn()
    return h

def nullspace(rows, tol=1e-9):
    A = np.array(rows)
    A /= np.maximum(np.linalg.norm(A, axis=1, keepdims=True), 1e-300)
    u, s, vt = np.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum())
    gap = (s[r-1], s[r] if r < len(s) else 0.0)
    return vt[r:].T, gap

def census(spin, n, gname, gauge=True, nrows_factor=3):
    B = basis(spin, n); N = len(B)
    gens = G[gname]
    rows = []
    # invariance rows: use all group elements on random points (overkill but cheap)
    for _ in range(nrows_factor * N // len(gens) + 2):
        h = rand_field(spin); k = np.random.randn(4)
        f0 = evalF(B, field_vec(h, spin), k)
        for g in gens:
            rows.append(evalF(B, field_vec(act(g, h, spin), spin), g @ k) - f0)
    Vinv, gapi = nullspace(rows)
    out = {'N': N, 'inv': Vinv.shape[1], 'gap_inv': gapi}
    if gauge and spin > 0:
        grows = []
        for _ in range(nrows_factor * Vinv.shape[1] + 10):
            h = rand_field(spin); k = np.random.randn(4)
            hp = gauge_shift(h, k, spin)
            grows.append((evalF(B, field_vec(hp, spin), k) - evalF(B, field_vec(h, spin), k)) @ Vinv)
        W, gapg = nullspace(grows) if Vinv.shape[1] else (np.zeros((0, 0)), None)
        out['gauge_inv'] = W.shape[1]; out['gap_g'] = gapg
        out['basis'] = (B, Vinv @ W)
    else:
        out['basis'] = (B, Vinv)
    return out

if __name__ == '__main__':
    print({g: len(v) for g, v in G.items()})
    for spin, n in [(0, 2), (1, 2), (2, 2), (2, 0)]:
        for gname in ['B4', 'B4+', 'K48', 'OhT', 'OT', 'K12T']:
            r = census(spin, n, gname)
            print(f"spin={spin} n={n} {gname:5s} forms={r['N']:4d} invariant={r['inv']:3d}"
                  + (f" gauge-invariant={r['gauge_inv']}" if 'gauge_inv' in r else ''),
                  ' gaps', np.format_float_scientific(r['gap_inv'][1], 1) if r['gap_inv'] else '')
