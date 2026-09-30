"""Test A: exact one-qubit-per-mode Pauli embedding of the even Majorana algebra on a grid.

Unknowns: a_u in F_2^{2n} (Pauli up to phase) for every Majorana u != ref, a_ref = 0.
a_u = image of (gamma_u gamma_ref). Bilinear gamma_u gamma_v maps to a_u + a_v.
Exactness (commutation of bilinears) <=> omega(a_u, a_v) = 1 for all u != v (both != ref).
r-locality: for every nearest-neighbour Majorana pair (u,v) (same site or adjacent sites),
a_u + a_v is supported inside the Chebyshev box of radius r around the two sites.
Usage: python3 sat_lemmaS.py L1 [L2 [L3]] r
"""
import sys, itertools, time
from pysat.solvers import Cadical153

def build(dims, r, ref=0):
    n = 1
    for d in dims: n *= d
    coords = list(itertools.product(*[range(d) for d in dims]))
    idx = {c: i for i, c in enumerate(coords)}
    nmaj = 2 * n
    # union-find over (u, q, t) with t in {0:x,1:z}; ZERO node = -1
    parent = {}
    def key(u, q, t): return (u, q, t)
    def find(k):
        while parent.setdefault(k, k) != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    def union(k1, k2):
        a, b = find(k1), find(k2)
        if a == b: return
        # keep ZERO as root
        if a == 'ZERO': parent[b] = a
        elif b == 'ZERO': parent[a] = b
        else: parent[a] = b
    parent['ZERO'] = 'ZERO'
    for q in range(n):
        for t in (0, 1):
            union(key(ref, q, t), 'ZERO')
    def site(u): return coords[u // 2]
    def box(cs):  # Chebyshev box radius r around bbox of sites cs
        lo = [min(c[i] for c in cs) - r for i in range(len(dims))]
        hi = [max(c[i] for c in cs) + r for i in range(len(dims))]
        return lo, hi
    def inbox(c, lo, hi): return all(lo[i] <= c[i] <= hi[i] for i in range(len(dims)))
    pairs = []
    for s, c in enumerate(coords):
        pairs.append((2 * s, 2 * s + 1))
        for ax in range(len(dims)):
            c2 = list(c); c2[ax] += 1; c2 = tuple(c2)
            if c2 in idx:
                t = idx[c2]
                for i in (0, 1):
                    for j in (0, 1):
                        pairs.append((2 * s + i, 2 * t + j))
    for (u, v) in pairs:
        lo, hi = box([site(u), site(v)])
        for q, cq in enumerate(coords):
            if not inbox(cq, lo, hi):
                for t in (0, 1):
                    union(key(u, q, t), key(v, q, t))
    return n, coords, nmaj, ref, find, union

def solve(dims, r, verbose=True, tlimit=None, ref=0, solver='cadical'):
    n, coords, nmaj, ref, find, union = build(dims, r, ref)
    varid = {}
    nv = [0]
    def newvar():
        nv[0] += 1; return nv[0]
    def lit(u, q, t):
        root = find((u, q, t))
        if root == 'ZERO': return 0
        if root not in varid: varid[root] = newvar()
        return varid[root]
    clauses = []
    def AND(a, b):
        if a == 0 or b == 0: return 0
        if a == b: return a
        y = newvar()
        clauses.extend([[-y, a], [-y, b], [y, -a, -b]])
        return y
    def XOR(a, b):
        if a == 0: return b
        if b == 0: return a
        if a == b: return 0
        y = newvar()
        clauses.extend([[-y, a, b], [-y, -a, -b], [y, -a, b], [y, a, -b]])
        return y
    us = [u for u in range(nmaj) if u != ref]
    L = {(u, q, t): lit(u, q, t) for u in us for q in range(n) for t in (0, 1)}
    npair = 0
    for i, u in enumerate(us):
        for v in us[i + 1:]:
            acc = 0
            for q in range(n):
                acc = XOR(acc, AND(L[(u, q, 0)], L[(v, q, 1)]))
                acc = XOR(acc, AND(L[(u, q, 1)], L[(v, q, 0)]))
            if acc == 0:
                return ('UNSAT', 0, 0, None)  # constant-0 symplectic product: cannot equal 1
            clauses.append([acc])
            npair += 1
    from pysat.solvers import Solver
    s = Solver(name={'cadical':'cadical153','glucose':'glucose4','minisat':'minisat22'}[solver], bootstrap_with=clauses)
    t0 = time.time()
    res = s.solve()
    dt = time.time() - t0
    model = None
    if res:
        m = set(x for x in s.get_model() if x > 0)
        model = {(u, q, t): (L[(u, q, t)] in m if L[(u, q, t)] else False) for u in us for q in range(n) for t in (0, 1)}
    s.delete()
    return ('SAT' if res else 'UNSAT', nv[0], len(clauses), model, dt)

if __name__ == '__main__':
    args = [int(a) for a in sys.argv[1:]]
    r = args[-1]; dims = tuple(args[:-1])
    out = solve(dims, r)
    print(dims, 'r=%d' % r, out[0], 'vars=%s clauses=%s' % (out[1], out[2]), 'time=%.1fs' % (out[4] if len(out) > 4 else 0))
