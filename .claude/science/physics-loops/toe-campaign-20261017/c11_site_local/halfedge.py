"""BKSF codes with six direction-labelled qubits per site (half-edges): site-local, translation- and
site-rotation covariant realization. Check: commuting, code dimension, orbit structure under the
framework site action (permute sites and the six direction labels), equality with edge-action orbits."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from collections import Counter, defaultdict
O = c1.O; E = bk.E; DIRS = bk.DIRS
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
n = 6 * L ** 3
def hq(v, d): return 6 * (((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)) + d
def half_op(op, zat):
    """Map an edge-qubit Pauli dict to half-edge qubits. X on edge -> X on both halves; Z on edge -> Z on the
    half at vertex zat[(edge)] (the vertex whose ordering string produced it)."""
    raise NotImplementedError
def A_half(v, a, order):
    """Half-edge version of the BKSF edge operator: X on both halves of edge (v,a); Z on v's half-edges ordered
    before +a; Z on (v+a)'s half-edges ordered before -a."""
    x = np.zeros(n, np.uint8); z = np.zeros(n, np.uint8)
    w = tuple(v[i] + E[a][i] for i in range(3))
    dp, dm = DIRS.index((a, 1)), DIRS.index((a, -1))
    x[hq(v, dp)] ^= 1; x[hq(w, dm)] ^= 1
    pos = {d: i for i, d in enumerate(order)}
    for d in range(6):
        if pos[d] < pos[dp]: z[hq(v, d)] ^= 1
        if pos[d] < pos[dm]: z[hq(w, d)] ^= 1
    return np.concatenate([x, z])
def B_half(v):
    z = np.zeros(n, np.uint8)
    for d in range(6): z[hq(v, d)] = 1
    return np.concatenate([np.zeros(n, np.uint8), z])
def rep(v, a):
    z = np.zeros(n, np.uint8); w = tuple(v[i] + E[a][i] for i in range(3))
    z[hq(v, DIRS.index((a, 1)))] = 1; z[hq(w, DIRS.index((a, -1)))] = 1
    return np.concatenate([np.zeros(n, np.uint8), z])
V = list(itertools.product(range(L), repeat=3))
def plaq_half(v, c, order):
    a, b = [t for t in range(3) if t != c]
    va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
    return A_half(v, a, order) ^ A_half(va, b, order) ^ A_half(vb, a, order) ^ A_half(v, b, order)
def code(order):
    return np.array([B_half(v) for v in V] + [rep(v, a) for v in V for a in range(3)] + [plaq_half(v, c, order) for v in V for c in range(3)])
def site_perm(M):
    perm = np.zeros(n, int)
    for v in V:
        w = tuple(int(x) for x in M @ np.array(v))
        for d in range(6):
            a, s = DIRS[d]; dv = M @ (s * np.array(E[a])); b = int(np.nonzero(dv)[0][0])
            perm[hq(v, d)] = hq(w, DIRS.index((b, int(dv[b]))))
    return perm
def act(R, perm):
    out = np.zeros_like(R); out[:, perm] = R[:, :n]; out[:, n + perm] = R[:, n:]; return out
sym = lambda X, Y: (X[:, :n].astype(np.int32) @ Y[:, n:].T.astype(np.int32) + X[:, n:].astype(np.int32) @ Y[:, :n].T.astype(np.int32)) % 2
orders = list(itertools.permutations(range(6)))
Hedge = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[Hedge[o]].append(o)
perms = {id(M): site_perm(M) for M in O}
comm_ok, dims, orb = True, Counter(), Counter()
exact = True
for h, ords in classes.items():
    o = ords[0]; C = code(o)
    comm_ok &= not sym(C, C).any()
    r = c1.f2_rank_and_null(C)[0] if L == 4 else None
    if r is not None: dims[n - r] += 1
    hh = bk.span_hash(C)
    st = [M for M in O if bk.span_hash(act(C, perms[id(M)])) == hh]
    st_edge = [M for M in O if Hedge[bk.rot_order(M, o)] == h]
    orb[(24 // len(st), len(st) == len(st_edge) and all(any(M is N_ for N_ in st_edge) for M in st))] += 1
    # exact intertwining: site action maps A_half(v,a,o) to A_half of the rotated edge with ordering Ro
    for M in O[:6]:
        for a in range(3):
            img = act(A_half((0, 0, 0), a, o)[None, :], perms[id(M)])[0]
            d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
            base = (0, 0, 0) if d[b] == 1 else tuple(-E[b][t] for t in range(3))
            exact &= bool((img == A_half(base, b, bk.rot_order(M, o))).all())
print('L', L, 'all 60 half-edge codes commuting:', comm_ok, ' log2 code dims:', dict(dims))
print('orbit sizes under the framework site action (size, stabilizer equals the edge-action stabilizer): count', dict(orb))
print('site action maps A_half(o) to A_half(Ro) exactly:', exact)
