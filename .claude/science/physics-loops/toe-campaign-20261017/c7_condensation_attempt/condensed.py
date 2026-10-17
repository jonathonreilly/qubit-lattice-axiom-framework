"""Four rotated BKSF copies (orbit of a D3-invariant code) with pairwise condensation of f_i f_j.
Qubits: on each edge, one per copy (key (site, 3*k + axis))."""
import itertools, sys
from collections import Counter
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
O = c1.O
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
# a D3-invariant code and its orbit
o0 = next(o for o in orders if sum(1 for M in O if H[bk.rot_order(M, o)] == H[o]) == 6)
orbit = []
for M in O:
    o = bk.rot_order(M, o0)
    if H[o] not in [H[x] for x in orbit]: orbit.append(o)
print('base ordering', o0, 'orbit codes', len(orbit))
K = len(orbit)
def lift(op, k):   # copy k: key ((p, a)) -> (p, 3k + a)
    return {(p, 3 * k + a): l for (p, a), l in op.items()}
def prod(*ops): return bk.prod(*ops)
gens = []
for k in range(K):
    for c in range(3): gens.append(lift(bk.plaq((0,0,0), c, orbit[k]), k))
for k in range(1, K):
    gens.append(prod(lift(bk.B((0,0,0)), 0), lift(bk.B((0,0,0)), k)))
    for a in range(3):
        gens.append(prod(lift(bk.A((0,0,0), a, orbit[0]), 0), lift(bk.A((0,0,0), a, orbit[k]), k)))
print('generator types per site', len(gens))
SH = list(itertools.product(range(-3, 4), repeat=3))
def shift(op, s): return {(tuple(p[i] + s[i] for i in range(3)), q): l for (p, q), l in op.items()}
comm = all(not bk.anti(gens[i], shift(gens[j], s)) for i in range(len(gens)) for j in range(i, len(gens)) for s in SH)
print('all generators commute:', comm)
Q = 3 * K
MUL = {(1,2):(3,1),(2,1):(3,3),(2,3):(1,1),(3,2):(1,3),(3,1):(2,1),(1,3):(2,3)}
def torus(gs, L):
    n = Q * L**3; idx = lambda p, q: Q * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + q
    R_, ops = [], []
    for v in itertools.product(range(L), repeat=3):
        for g in gs:
            x = np.zeros(2*n, np.uint8); op = {}
            for (p, q), l in g.items():
                i = idx([v[t] + p[t] for t in range(3)], q)
                c = op.get(i, 0); op[i] = l if c == 0 else (0 if c == l else MUL[(c, l)][0])
            op = {i: l for i, l in op.items() if l}
            for i, l in op.items():
                if l in (1, 2): x[i] ^= 1
                if l in (2, 3): x[n + i] ^= 1
            R_.append(x); ops.append(op)
    r, N = c1.f2_rank_and_null(np.array(R_))
    return n - r, r, len(N)
for L in (4,):
    print('torus L', L, '(log2 dim, rank, relations):', torus(gens, L), flush=True)
# fermion statistics with straight legs of copy-0 hopping operators
def leg(d, n):
    a, s = bk.DIRS[d]; ops = []; v = (0,0,0)
    for _ in range(n):
        if s == 1: base = v; v = tuple(v[i] + bk.E[a][i] for i in range(3))
        else: v = tuple(v[i] - bk.E[a][i] for i in range(3)); base = v
        ops.append(lift(bk.A(base, a, orbit[0]), 0))
    return prod(*ops)
# check legs are pure hopping (commute with all generators except the B-products at endpoints)
cnt = Counter()
for trip in itertools.combinations(range(6), 3):
    Ls = [leg(d, 3) for d in trip]
    cnt[(-1) ** (bk.anti(Ls[0], Ls[1]) + bk.anti(Ls[1], Ls[2]) + bk.anti(Ls[0], Ls[2]))] += 1
print('straight-leg T-junction signs (copy-0 fermion):', dict(cnt))
