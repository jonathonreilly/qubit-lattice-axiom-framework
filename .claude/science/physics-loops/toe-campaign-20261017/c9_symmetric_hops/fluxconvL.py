"""Search for a D3-invariant flux convention F = span(S^o_p * beta_c(p)) in a D3 BKSF code, and clean hops."""
import sys, itertools, time
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from quad import rref_rank
O = c1.O; E = bk.E; L = int(__import__("os").environ.get("LL", "4"))
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
o0 = next(o for o in orders if sum(1 for M in O if H[bk.rot_order(M, o)] == H[o]) == 6)
stab = [M for M in O if H[bk.rot_order(M, o0)] == H[o0]]
gensD3 = [M for M in stab if bk.kind(M) in ('C3', 'C2edge')]
def rot_op(M, op):
    out = {}
    for (p, a), l in op.items():
        w = tuple(int(x) for x in M @ np.array(p)); d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
        q = w if d[b] == 1 else tuple(w[t] - (1 if t == b else 0) for t in range(3))
        out[(q, b)] = l
    return out
def corners(c):
    a, b = [t for t in range(3) if t != c]
    return [(0, 0, 0), tuple(E[a]), tuple(E[b]), tuple(np.add(E[a], E[b]))]
def Fgens(beta):
    gs = []
    for c in range(3):
        g = bk.plaq((0, 0, 0), c, o0)
        for u in beta[c]: g = bk.prod(g, bk.B(u))
        gs.append(g)
    return gs
def span_rows(gs): return bk.torus_rows(gs, L)
t0 = time.time(); found = []
subsets = [list(s) for k in range(5) for s in itertools.combinations(range(4), k)]
for bs in itertools.product(subsets, repeat=3):
    beta = [[corners(c)[i] for i in bs[c]] for c in range(3)]
    gs = Fgens(beta)
    R0 = span_rows(gs); r0, b0 = rref_rank(R0)
    ok = True
    for M in gensD3:
        # rotated generators (all translates are covered since torus_rows translates them)
        Rr = span_rows([rot_op(M, g) for g in gs])
        if rref_rank(np.vstack([b0, Rr]))[0] != r0: ok = False; break
    if ok: found.append(bs)
print('corner-supported beta choices giving a D3-invariant flux subgroup:', len(found), 'of', len(subsets) ** 3, round(time.time() - t0), 's')
print(found[:10])
