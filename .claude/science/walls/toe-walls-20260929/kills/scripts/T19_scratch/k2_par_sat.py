"""Kill check K2: Test A with the extra requirement that the total-parity image prod_{u!=ref} a_u is a
NON-identity Pauli (so both fermion-parity sectors are carried, i.e. exactness on the WHOLE Fock space)."""
import sys, itertools, time
from pysat.solvers import Cadical153
import sat_lemmaS as M

def solve(dims, r, require_parity=True):
    n, coords, nmaj, ref, find, union = M.build(dims, r)
    varid = {}; nv = [0]
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
        y = newvar(); clauses.extend([[-y, a], [-y, b], [y, -a, -b]]); return y
    def XOR(a, b):
        if a == 0: return b
        if b == 0: return a
        if a == b: return 0
        y = newvar(); clauses.extend([[-y, a, b], [-y, -a, -b], [y, -a, b], [y, a, -b]]); return y
    us = [u for u in range(nmaj) if u != ref]
    L = {(u, q, t): lit(u, q, t) for u in us for q in range(n) for t in (0, 1)}
    for i, u in enumerate(us):
        for v in us[i + 1:]:
            acc = 0
            for q in range(n):
                acc = XOR(acc, AND(L[(u, q, 0)], L[(v, q, 1)]))
                acc = XOR(acc, AND(L[(u, q, 1)], L[(v, q, 0)]))
            if acc == 0: return 'UNSAT(structural)'
            clauses.append([acc])
    if require_parity:
        outs = []
        for q in range(n):
            for t in (0, 1):
                s = 0
                for u in us: s = XOR(s, L[(u, q, t)])
                if s != 0: outs.append(s)
        if not outs: return 'UNSAT(parity structural)'
        clauses.append(outs)
    s = Cadical153(bootstrap_with=clauses)
    res = s.solve(); s.delete()
    return 'SAT' if res else 'UNSAT'

if __name__ == '__main__':
    for spec in sys.argv[1:]:
        dims_s, r_s = spec.split('@'); dims = tuple(int(x) for x in dims_s.split('x')); r = int(r_s)
        t0 = time.time(); st = solve(dims, r)
        print(f"{dims_s} r={r} parity-nontrivial: {st}  [{time.time()-t0:.1f}s]", flush=True)
