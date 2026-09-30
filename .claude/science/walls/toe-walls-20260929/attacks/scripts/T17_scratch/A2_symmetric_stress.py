"""Every N,P,L-preserving event on a cluster: does a compactly supported SYMMETRIC lattice stress exist with
   Delta pi_j(x) = sum_i [Theta_ij(x) - Theta_ij(x - e_i)] ?   (exact linear algebra, residual test)
Controls: the original clause's exchange of a PERPENDICULAR neighbour pair (changes L) must have no symmetric solution.
Also: non-symmetric solution always exists (a control for the solver)."""
import itertools, sys
import numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
from A_cluster_classes import CLUSTERS, E3, E2, cross, add

def solve_stress(dim, sites, dpi, margin=2, symmetric=True):
    """sites: list of positions (3-tuples), dpi: dict pos->3-vector (only dim components used)."""
    lo = [min(s[a] for s in sites) - margin for a in range(dim)]
    hi = [max(s[a] for s in sites) + margin for a in range(dim)]
    pts = list(itertools.product(*[range(lo[a], hi[a] + 1) for a in range(dim)]))
    pid = {p: i for i, p in enumerate(pts)}
    comps = [(i, j) for i in range(dim) for j in range(i, dim)] if symmetric else [(i, j) for i in range(dim) for j in range(dim)]
    cid = {c: k for k, c in enumerate(comps)}
    nvar = len(pts) * len(comps)
    def var(p, i, j):
        if symmetric and i > j: i, j = j, i
        return pid[p] * len(comps) + cid[(i, j)]
    rows = []; rhs = []
    # equations at every point of the box extended by 1 (outside the box Theta = 0)
    ext = list(itertools.product(*[range(lo[a], hi[a] + 2) for a in range(dim)]))
    for x in ext:
        for j in range(dim):
            row = np.zeros(nvar)
            for i in range(dim):
                if x in pid: row[var(x, i, j)] += 1.0
                xm = tuple(x[a] - (1 if a == i else 0) for a in range(dim)) + (0,) * (3 - dim)
                xm = xm[:dim]
                if xm in pid: row[var(xm, i, j)] -= 1.0
            rows.append(row)
            x3 = tuple(x) + (0,) * (3 - dim)
            rhs.append(dpi.get(x3, (0, 0, 0))[j])
    A = np.array(rows); b = np.array(rhs, dtype=float)
    sol, res, rk, sv = np.linalg.lstsq(A, b, rcond=None)
    return np.abs(A @ sol - b).max()

def events(cname_sites, contents):
    """all (config, config') pairs with same class, for the occupied subset; returns list of (xs, cfg, cfg2)."""
    xs = cname_sites
    configs = list(itertools.product(contents, repeat=len(xs)))
    classes = defaultdict(list)
    for c in configs:
        P = (0,0,0); L = (0,0,0)
        for x, ci in zip(xs, c):
            P = add(P, ci); L = add(L, cross(x, ci))
        classes[(P, L)].append(c)
    out = []
    for key, mem in classes.items():
        for c2 in mem[1:]:
            out.append((xs, mem[0], c2))
    return out

def dpi_of(xs, c1, c2):
    d = {}
    for x, a, b in zip(xs, c1, c2):
        d[x] = tuple(b[i] - a[i] for i in range(3))
    return d

worst = defaultdict(float); count = defaultdict(int)
for name in ('bond', 'diag2d', 'ltriple', 'plaquette'):
    sites = CLUSTERS[name]
    for contents, dim, tag in ((E2, 2, '2D'),):
        n = len(sites)
        for mask in range(1, 1 << n):
            xs = [sites[i] for i in range(n) if mask >> i & 1]
            if len(xs) < 2: continue
            for xs_, c1, c2 in events(xs, contents):
                r = solve_stress(dim, xs_, dpi_of(xs_, c1, c2), symmetric=True)
                worst[(name, tag)] = max(worst[(name, tag)], r); count[(name, tag)] += 1
for k in sorted(worst):
    print('conserving events', k, ': count', count[k], ' worst residual of symmetric-stress solve', f'{worst[k]:.2e}')

# controls: perpendicular neighbour exchange (original clause): (e_x at (0,0), e_y at (1,0)) -> contents swapped
xs = [(0,0,0), (1,0,0)]
c1 = ((1,0,0), (0,1,0)); c2 = ((0,1,0), (1,0,0))
r_sym = solve_stress(2, xs, dpi_of(xs, c1, c2), symmetric=True)
r_gen = solve_stress(2, xs, dpi_of(xs, c1, c2), symmetric=False)
print(f'control: perpendicular pass-through exchange: symmetric-stress residual {r_sym:.3f} (must be >0); general-stress residual {r_gen:.2e} (must be ~0)')
