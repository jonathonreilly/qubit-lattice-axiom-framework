"""Kill check K3: independent re-implementation of Test A (no union-find, direct per-bit variables,
different solver).  Variables x[u][q], z[u][q] for every Majorana u != ref (a_ref = 0).
Locality: for every NN Majorana pair (u,v) and every qubit q OUTSIDE the box of radius r around the
bounding box of the two sites:  x[u][q]==x[v][q] and z[u][q]==z[v][q]   (image a_u+a_v vanishes there).
Exactness: omega(a_u,a_v) = 1 for all u != v, both != ref.  (Optionally parity image nontrivial.)"""
import sys, itertools, time
from pysat.solvers import Solver

def run(dims, r, solver='glucose4', ref_site=0, parity=False):
    coords = list(itertools.product(*[range(d) for d in dims])); n = len(coords)
    idx = {c: i for i, c in enumerate(coords)}
    D = len(dims); nmaj = 2 * n; ref = 2 * ref_site
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    clauses = []
    X = {}; Z = {}
    for u in range(nmaj):
        for q in range(n):
            X[u, q] = new(); Z[u, q] = new()
            if u == ref:
                clauses.append([-X[u, q]]); clauses.append([-Z[u, q]])
    def eq(a, b): clauses.extend([[-a, b], [a, -b]])
    gens = []
    for s, c in enumerate(coords):
        gens.append((2 * s, 2 * s + 1, [c, c]))
        for ax in range(D):
            c2 = list(c); c2[ax] += 1; c2 = tuple(c2)
            if c2 in idx:
                t = idx[c2]
                for i in (0, 1):
                    for j in (0, 1): gens.append((2 * s + i, 2 * t + j, [c, c2]))
    for (u, v, cs) in gens:
        lo = [min(c[k] for c in cs) - r for k in range(D)]; hi = [max(c[k] for c in cs) + r for k in range(D)]
        for q, cq in enumerate(coords):
            if not all(lo[k] <= cq[k] <= hi[k] for k in range(D)):
                eq(X[u, q], X[v, q]); eq(Z[u, q], Z[v, q])
    def AND(a, b):
        y = new(); clauses.extend([[-y, a], [-y, b], [y, -a, -b]]); return y
    def XOR(a, b):
        y = new(); clauses.extend([[-y, a, b], [-y, -a, -b], [y, -a, b], [y, a, -b]]); return y
    us = [u for u in range(nmaj) if u != ref]
    for i, u in enumerate(us):
        for v in us[i + 1:]:
            terms = []
            for q in range(n):
                terms.append(AND(X[u, q], Z[v, q])); terms.append(AND(Z[u, q], X[v, q]))
            acc = terms[0]
            for t in terms[1:]: acc = XOR(acc, t)
            clauses.append([acc])
    if parity:
        outs = []
        for q in range(n):
            for W in (X, Z):
                acc = W[us[0], q]
                for u in us[1:]: acc = XOR(acc, W[u, q])
                outs.append(acc)
        clauses.append(outs)
    s = Solver(name=solver, bootstrap_with=clauses)
    t0 = time.time(); res = s.solve(); s.delete()
    return ('SAT' if res else 'UNSAT'), time.time() - t0, nv[0], len(clauses)

if __name__ == '__main__':
    solver = sys.argv[1]
    for spec in sys.argv[2:]:
        d, r = spec.split('@'); dims = tuple(int(x) for x in d.split('x')); r = int(r)
        ref_site = 0
        st, dt, nv, nc = run(dims, r, solver=solver)
        print(f"[{solver}] {d} r={r}: {st}  [{dt:.1f}s vars={nv} clauses={nc}]", flush=True)
