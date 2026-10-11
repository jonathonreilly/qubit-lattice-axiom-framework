"""Exact Pauli-string algebra for translation-invariant (TI) operators on infinite 2D lattices with sublattices.
A TI operator O = sum_x T_x (sum_a c_a a) is stored as its density {canonical string: coeff}.
A string is a tuple sorted of ((x, y, s), p), p in {1,2,3} = X,Y,Z. Canonical: min site shifted to cell (0,0).
"""
import numpy as np
from collections import defaultdict

# single-site products: P_a P_b = ph * P_c
_mul = {}
for a in range(4):
    for b in range(4):
        if a == 0: _mul[(a, b)] = (1, b); continue
        if b == 0: _mul[(a, b)] = (1, a); continue
        if a == b: _mul[(a, b)] = (1, 0); continue
        c = 6 - a - b
        # eps: (1,2,3) cyclic -> +i
        ph = 1j if (a, b) in [(1, 2), (2, 3), (3, 1)] else -1j
        _mul[(a, b)] = (ph, c)

def smul(s1, s2):
    d = dict(s1); ph = 1
    for site, p in s2:
        if site in d:
            f, c = _mul[(d[site], p)]
            ph *= f
            if c == 0: del d[site]
            else: d[site] = c
        else:
            d[site] = p
    return ph, tuple(sorted(d.items()))

def anticommute(s1, s2):
    d = dict(s1); n = 0
    for site, p in s2:
        q = d.get(site)
        if q is not None and q != p: n += 1
    return n % 2 == 1

def shift(s, t):
    return tuple(sorted((((x + t[0], y + t[1], k), p) for (x, y, k), p in s)))

def canon(s):
    if not s: return s, (0, 0)
    (x0, y0, k0), _ = min(s)
    return shift(s, (-x0, -y0)), (x0, y0)

class Lat:
    def __init__(self, a1, a2, subpos):
        self.a1 = np.array(a1, float); self.a2 = np.array(a2, float); self.sub = [np.array(v, float) for v in subpos]
    def pos(self, site):
        x, y, k = site
        return x*self.a1 + y*self.a2 + self.sub[k]
    def centroid(self, s):
        return np.mean([self.pos(site) for site, _ in s], axis=0)

def comm_density(A, B):
    """density of [sum A, sum B]"""
    C = defaultdict(complex)
    for a, ca in A.items():
        asites = set(site for site, _ in a)
        for b, cb in B.items():
            bsites = [site for site, _ in b]
            ts = set()
            for (xa, ya, ka) in asites:
                for (xb, yb, kb) in bsites:
                    if ka == kb: ts.add((xa - xb, ya - yb))
            for t in ts:
                bt = shift(b, t)
                if anticommute(a, bt):
                    ph, s = smul(a, bt)
                    cs, _ = canon(s)
                    C[cs] += 2*ph*ca*cb
    return {k: v for k, v in C.items() if abs(v) > 1e-13}

def energy_current(H, lat, comp=0):
    """J^comp = (i/2) sum_{x,y} (r_y - r_x)[h_x, h_y], each Pauli term of H its own energy density at its centroid."""
    C = defaultdict(complex)
    for a, ca in H.items():
        asites = set(site for site, _ in a); ra = lat.centroid(a)
        for b, cb in H.items():
            bsites = [site for site, _ in b]
            ts = set()
            for (xa, ya, ka) in asites:
                for (xb, yb, kb) in bsites:
                    if ka == kb: ts.add((xa - xb, ya - yb))
            for t in ts:
                bt = shift(b, t)
                if anticommute(a, bt):
                    d = (lat.centroid(bt) - ra)[comp]
                    if abs(d) < 1e-14: continue
                    ph, s = smul(a, bt)
                    cs, _ = canon(s)
                    C[cs] += 0.5j*d*2*ph*ca*cb
    return {k: v for k, v in C.items() if abs(v) > 1e-13}

def norm2(A):
    return sum(abs(v)**2 for v in A.values())

def add(A, B, cb=1.0):
    C = defaultdict(complex, A)
    for k, v in B.items(): C[k] += cb*v
    return {k: v for k, v in C.items() if abs(v) > 1e-13}

def patch_basis(cells, nsub, maxsupport=None):
    """all canonical strings supported on sites of the given cells (list of (x,y)), all sublattices"""
    import itertools
    sites = [(x, y, k) for (x, y) in cells for k in range(nsub)]
    out = set()
    n = len(sites)
    for mask_vals in itertools.product(range(4), repeat=n):
        if all(v == 0 for v in mask_vals): continue
        s = tuple(sorted((sites[i], mask_vals[i]) for i in range(n) if mask_vals[i] != 0))
        if maxsupport and len(s) > maxsupport: continue
        out.add(canon(s)[0])
    return sorted(out)

def improvement_search(H, J, basis, verbose=False):
    """min_beta || [H, J + i [H, sum beta_i b_i]] || over real beta; returns (||[H,J]||, min residual, ||J||)."""
    T = comm_density(H, J)
    cols = []
    for b in basis:
        Bi = {b: 1.0}
        C1 = comm_density(H, Bi)
        C2 = comm_density(H, C1)
        cols.append({k: 1j*v for k, v in C2.items()})
    keys = sorted(set(T.keys()).union(*[set(c.keys()) for c in cols]))
    kidx = {k: i for i, k in enumerate(keys)}
    M = np.zeros((len(keys), len(cols)), complex)
    for j, c in enumerate(cols):
        for k, v in c.items(): M[kidx[k], j] = v
    t = np.zeros(len(keys), complex)
    for k, v in T.items(): t[kidx[k]] = v
    # real beta: stack real and imaginary parts
    Mr = np.vstack([M.real, M.imag]); tr = np.concatenate([t.real, t.imag])
    beta, *_ = np.linalg.lstsq(Mr, -tr, rcond=None)
    res = np.linalg.norm(Mr@beta + tr)
    return np.sqrt(norm2(T)), res, np.linalg.matrix_rank(Mr), len(basis)
