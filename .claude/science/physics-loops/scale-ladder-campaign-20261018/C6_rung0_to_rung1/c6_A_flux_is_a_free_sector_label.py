#!/usr/bin/env python3
"""C6 part A: does a local fermion-to-qubit encoding of the corner graph fix the corner
model's flux background?

A1 (exact, GF(2)): the four face types generate the contractible cycle space of the corner
    graph on the L-torus; every face relation (closed surface) contains an even number of
    faces of each type, so every one of the 16 uniform Z2 flux patterns is a consistent
    sector; the space of all consistent flux configurations has dimension
    #faces - #relations = (cycle-space rank) and every such configuration is realized by a
    gauge field u.  So the BKSF Z2 gauge structure admits the corner pattern but does not
    single it out.
A2 (exact Pauli algebra, Bravyi-Kitaev superfast encoding on the corner graph, L = 3 torus):
    the flux F_C that the encoded fermion sees in the 'natural' qubit sector where every
    loop check is the bare tensor-product Pauli string with eigenvalue +1 is
    F_C = i^n (prod eps) phi_C.  It is computed for the BK canonical sign rule
    eps_jk = sign(k - j) under different vertex labellings / edge orders, and is shown to
    depend on those conventions (so 'the vacuum flux of the encoding' is not canonical).
A3 (exact): flipping the dictionary sign of one hop (A_e -> -A_e, which preserves every
    algebraic relation of the encoding) flips F on exactly the faces containing e.
A4 (exact, from the PSG of the fermion level, independent re-implementation): which
    uniform patterns meet the corner-model design targets (spin-1/2-class squares C4^4=-1
    needs square = pi; commuting translations need plaquette = square; O-fixed momenta need
    tube = pi; the triangle is free).  This is target-selection, not derivation.
"""
import itertools, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c6_corner_graph import CornerGraph, CORNERS, DIRS, gf2_rank_and_basis, gf2_solve, bits, neg

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


TYPES = ('square', 'triangle', 'plaquette', 'tube')

# ------------------------------------------------------------------ A1
print("A1: cycle space, face relations and the 16 uniform flux patterns")
for L in (3, 4, 6):
    G = CornerGraph(L)
    N = L ** 3
    fl = G.face_list()
    counts = {k: len(G.faces[k]) // N for k in TYPES}
    print(f"  L={L}: V={G.nV} E={G.nE} faces/site={counts}")
    cyc_dim = G.nE - G.nV + 1
    piv = gf2_rank_and_basis([bits(f) for _, f in fl], G.nE)
    rk = len(piv)
    # add three noncontractible loops (straight lines of link+onsite edges along each axis):
    # use any cycle with winding (1,0,0) etc: build by walking corner {x,y}@v -> {-x,y}@v+x -> onsite to {x,y}@v+x? need an on-site path
    # from {-x,y} to {x,y} at the same site: {-x,y} - {-x,z}? not adjacent to {x,y}; use {-x,y}-{y,z}-{x,y}
    def straight(axis):
        a = DIRS[2 * axis]
        b = DIRS[(2 * axis + 2) % 6]   # a perpendicular direction
        c = DIRS[(2 * axis + 4) % 6]
        seq = []
        for n in range(L):
            v = tuple(n * x for x in a)
            seq += [(v, frozenset((a, b))), ]
            # link to v+a corner {-a,b}, then on-site {-a,b} -> {b,c} -> {a,b}
            w = tuple((n + 1) * x for x in a)
            seq += [(w, frozenset((neg(a), b))), (w, frozenset((b, c)))]
        # last element returns to start corner at L*a == 0 mod L: the cycle closes through (L a, {a,b}) == start
        es = []
        pts = seq + [(tuple(L * x for x in a), frozenset((a, b)))]
        for (p1, c1), (p2, c2) in zip(pts[:-1], pts[1:]):
            v1 = tuple(x % L for x in p1)
            es.append(G.edge_between((v1, c1), tuple(y - x for x, y in zip(p1, p2)), c2))
        return es
    nonc = [straight(a) for a in range(3)]
    piv2 = gf2_rank_and_basis([bits(f) for _, f in fl] + [bits(c) for c in nonc], G.nE)
    print(f"  cycle-space dim E-V+1 = {cyc_dim}; rank(faces) = {rk}; rank(faces + 3 noncontractible) = {len(piv2)}")
    check(f"L={L}: faces generate the cycle space up to the 3 noncontractible classes (rank = E-V+1-3)",
          rk == cyc_dim - 3 and len(piv2) == cyc_dim)
    # relations: left null space of the face-edge incidence; check type parities via augmented columns
    nf = len(fl)
    # build rows = faces with tag bits for the face index, reduce, collect zero-reduced combinations
    piv = {}; rels = []
    for idx, (k, f) in enumerate(fl):
        x = bits(f) | (1 << (G.nE + idx))
        while True:
            low = x & ((1 << G.nE) - 1)
            if low == 0:
                rels.append(x >> G.nE); break
            c = low.bit_length() - 1
            if c in piv: x ^= piv[c]
            else: piv[c] = x; break
    print(f"  independent face relations: {len(rels)} (= {len(rels)/N:.3f} per site); faces - relations = {nf - len(rels)}")
    tidx = {k: [i for i, (kk, _) in enumerate(fl) if kk == k] for k in TYPES}
    ok_even = True; parity_profile = set()
    for r in rels:
        par = tuple(sum((r >> i) & 1 for i in tidx[k]) % 2 for k in TYPES)
        parity_profile.add(par)
        if any(par): ok_even = False
    if L % 2 == 0:
        check(f"L={L}: every face relation contains an even number of faces of each type (all 16 uniform patterns consistent)",
              ok_even, f"type-parity vectors of relations: {sorted(parity_profile)}")
    else:
        check(f"L={L} (odd): the only odd type-parity of a relation is (square, plaquette) = (odd, odd), a wrapped torus relation;"
              " uniform patterns with square != plaquette are then inconsistent (torus-size effect, absent for even L)",
              parity_profile == {(0, 0, 0, 0), (1, 0, 1, 0)}, f"type-parity vectors: {sorted(parity_profile)}")
    # each uniform pattern: solve gauge, verify fluxes
    ok_all = True
    for Fb in itertools.product((0, 1), repeat=4):
        F = dict(zip(TYPES, Fb))
        u = gf2_solve([f for _, f in fl], [F[k] for k, _ in fl], G.nE)
        expect = (L % 2 == 0) or (Fb[0] == Fb[2])
        if u is None:
            ok_all &= not expect; continue
        ok_all &= expect and all(int(sum(u[e] for e in f) % 2) == F[k] for k, f in fl)
    check(f"L={L}: uniform patterns realized by a gauge field u exactly as the relation parities predict"
          f" ({'all 16' if L % 2 == 0 else 'the 8 with square = plaquette'}; fluxes re-measured)", ok_all)
    # random closed flux configurations (images of random u) are also sectors: the flux configuration space
    rng = np.random.default_rng(1)
    u = rng.integers(0, 2, G.nE)
    Fr = [int(sum(u[e] for e in f) % 2) for _, f in fl]
    check(f"L={L}: a random gauge field gives a random (non-uniform) consistent flux configuration: sectors are not unique",
          gf2_solve([f for _, f in fl], Fr, G.nE) is not None and 0.3 < np.mean(Fr) < 0.7, f"mean flux {np.mean(Fr):.3f}")

# ------------------------------------------------------------------ A2: BKSF Pauli algebra
print("\nA2: Bravyi-Kitaev superfast encoding on the corner graph (L = 3): flux of the 'all bare checks +1' sector")
L = 3
G = CornerGraph(L)
nE = G.nE


class Pauli:
    """i^p X^x Z^z with x, z boolean arrays."""
    __slots__ = ('p', 'x', 'z')

    def __init__(self, p, x, z):
        self.p, self.x, self.z = p % 4, x, z

    def __mul__(self, o):
        sign = int(np.count_nonzero(self.z & o.x)) % 2
        return Pauli(self.p + o.p + 2 * sign, self.x ^ o.x, self.z ^ o.z)

    def std_phase(self):
        """operator = i^q * (tensor product of I,X,Y,Z); returns q."""
        return (self.p - int(np.count_nonzero(self.x & self.z))) % 4


def incident(G):
    inc = [[] for _ in range(G.nV)]
    for k, (i, j, _, _) in enumerate(G.edges):
        inc[i].append(k); inc[j].append(k)
    return inc


INC = incident(G)


def build_S(order):
    """order[v] = list of incident edges in the order <_v.  S_e = X_e prod_{l <_j e} Z_l prod_{l <_k e} Z_l."""
    rank = [dict((e, r) for r, e in enumerate(order[v])) for v in range(G.nV)]
    S = []
    for k, (i, j, _, _) in enumerate(G.edges):
        x = np.zeros(nE, bool); z = np.zeros(nE, bool); x[k] = True
        for v in (i, j):
            for l in order[v]:
                if rank[v][l] < rank[v][k]: z[l] ^= True
        S.append(Pauli(0, x, z))
    return S


def check_algebra(S, sample=400, rng=None):
    ok = True
    for _ in range(sample):
        a, b = rng.integers(0, nE, 2)
        if a == b: continue
        A, B = S[a], S[b]
        anti = (int(np.count_nonzero(A.x & B.z)) + int(np.count_nonzero(A.z & B.x))) % 2
        share = len({G.edges[a][0], G.edges[a][1]} & {G.edges[b][0], G.edges[b][1]}) == 1
        ok &= (anti == 1) == share
    return ok


def face_traversal(seq):
    """vertex index sequence of a face (from unwrapped (site, corner) sequence)."""
    return [G.vid[(tuple(x % L for x in p), c)] for p, c in seq]


def face_flux(S, label, kind_faces):
    """F_C = i^n prod_cyc eps * phi_C  for each face; eps_jk = +1 if label[j] < label[k]."""
    out = []
    for f, seq in kind_faces:
        vs = face_traversal(seq)
        P = Pauli(0, np.zeros(nE, bool), np.zeros(nE, bool)); eps = 1
        for e, a, b in zip(f, vs, vs[1:] + vs[:1]):
            P = P * S[e]
            eps *= 1 if label[a] < label[b] else -1
        q = P.std_phase()               # prod S = i^q * (bare Pauli loop string)
        n = len(f)
        val = (1j ** n) * eps * (1j ** q)
        assert abs(val.imag) < 1e-12 and abs(abs(val.real) - 1) < 1e-12, val
        out.append(int(round(val.real)))
    return out


rng = np.random.default_rng(2026)
faces_by_type = {k: list(zip(G.faces[k], G.face_seq[k])) for k in TYPES}
conventions = {}
for name in ('canonical', 'random-1', 'random-2'):
    if name == 'canonical':
        order = [sorted(INC[v]) for v in range(G.nV)]
        label = np.arange(G.nV)
    else:
        order = [list(rng.permutation(INC[v])) for v in range(G.nV)]
        label = rng.permutation(G.nV)
    S = build_S(order)
    alg = check_algebra(S, rng=rng)
    fl = {k: face_flux(S, label, faces_by_type[k]) for k in TYPES}
    conventions[name] = fl
    summ = {k: (sum(1 for x in v if x == -1), len(v)) for k, v in fl.items()}
    print(f"  convention {name}: hop algebra ok={alg}; (# faces with F = -1, # faces) per type: {summ}")
    check(f"BKSF hop operators under convention '{name}' anticommute exactly when edges share one vertex (400 sampled pairs)", alg)

diff = {k: sum(a != b for a, b in zip(conventions['random-1'][k], conventions['random-2'][k])) for k in TYPES}
check("the flux seen in the 'all bare loop checks = +1' sector depends on the arbitrary labelling/ordering convention",
      sum(diff.values()) > 0, f"faces whose F differs between two random conventions: {diff}")
uni = {name: {k: sorted(set(v)) for k, v in fl.items()} for name, fl in conventions.items()}
print("  values of F per type under each convention:", uni)
check("under the canonical BK convention (eps_jk = sign(k-j), index-ordered Z strings) the bare sector is not uniform per face type"
      " (so it is not the corner pattern in any sign convention)",
      any(len(set(conventions['canonical'][k])) > 1 for k in TYPES))

# ------------------------------------------------------------------ A3
print("\nA3: one dictionary sign flip A_e -> -A_e flips F on exactly the faces through e")
order = [sorted(INC[v]) for v in range(G.nV)]; label = np.arange(G.nV)
S = build_S(order)
F0 = {k: face_flux(S, label, faces_by_type[k]) for k in TYPES}
ok = True
for e in rng.integers(0, nE, 5):
    S2 = list(S); S2[e] = Pauli(2, S[e].x, S[e].z)       # -S_e
    F1 = {k: face_flux(S2, label, faces_by_type[k]) for k in TYPES}
    for k in TYPES:
        for (f, _), a, b in zip(faces_by_type[k], F0[k], F1[k]):
            ok &= (a != b) == (e in f)
check("sign flip of one hop flips exactly the fluxes of the faces containing that edge (5 random edges, all faces)", ok)

# ------------------------------------------------------------------ A4: target selection (PSG), own implementation
print("\nA4: which uniform patterns meet the corner-model design targets (fermion-level PSG, L = 4)")
L = 4
G4 = CornerGraph(L)
fl4 = G4.face_list()
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)


def vmap(f):
    return np.array([G4.vid[f(q)] for q in G4.verts])


def rot(R):
    def f(q):
        v, c = q
        return (tuple(int(x) % L for x in R @ np.array(v)), frozenset(tuple(int(x) for x in R @ np.array(d)) for d in c))
    return f


def trans(t):
    def f(q):
        v, c = q
        return (tuple((a + b) % L for a, b in zip(v, t)), c)
    return f


def unwrapped_edge_image(f, k):
    """image edge index of edge k under a site map f, comparing displacements."""
    i, j, kind, wind = G4.edges[k]
    return None


def psg(fmap, u):
    P = vmap(fmap)
    # image of edge (i,j): find edge between P[i], P[j] with matching kind; on L=4 torus vertex pairs are unique
    pair = {}
    for k, (i, j, _, _) in enumerate(G4.edges):
        pair.setdefault(frozenset((i, j)), []).append(k)
    assert all(len(v) == 1 for v in pair.values())
    rows, rhs = [], []
    for k, (i, j, _, _) in enumerate(G4.edges):
        fk = pair[frozenset((P[i], P[j]))][0]
        rows.append([i, j]); rhs.append(int(u[k]) ^ int(u[fk]))
    s = gf2_solve(rows, rhs, G4.nV)
    return P, s


def power_sign(P, s, m):
    cur = np.arange(len(P)); sign = np.zeros(len(P), np.uint8)
    for _ in range(m):
        sign ^= s[cur]; cur = P[cur]
    assert (cur == np.arange(len(P))).all()
    vals = set(sign.tolist()); assert len(vals) == 1
    return -1 if vals.pop() else 1


def fixed_momenta(u):
    E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    T = {a: psg(trans(a), u) for a in E3}

    def comp(ops):
        perm = np.arange(G4.nV); sign = np.zeros(G4.nV, np.uint8)
        for P, s in reversed(ops):
            sign = sign ^ s[perm]; perm = P[perm]
        return perm, sign

    def inv(P, s):
        Pi = np.empty(len(P), int); Pi[P] = np.arange(len(P)); return Pi, s[Pi]
    shifts = []
    for R in ROTS:
        MR = psg(rot(R), u)
        sh = np.zeros(3, int)
        for a in E3:
            Ra = tuple(int(x) for x in R @ np.array(a))
            ax = int(np.argmax(np.abs(Ra))); sgn = Ra[ax]
            Ta = T[E3[ax]] if sgn > 0 else inv(*T[E3[ax]])
            perm, sign = comp([MR, T[a], inv(*MR), inv(*Ta)])
            assert (perm == np.arange(G4.nV)).all()
            vals = set(sign.tolist()); assert len(vals) == 1
            sh += vals.pop() * np.abs(np.array(Ra))
        shifts.append(sh % 2)
    return [k for k in itertools.product(range(4), repeat=3)
            if all(((R @ np.array(k) + 2 * s - np.array(k)) % 4 == 0).all() for R, s in zip(ROTS, shifts))]


table = {}
for Fb in itertools.product((0, 1), repeat=4):
    F = dict(zip(TYPES, Fb))
    u = gf2_solve([f for _, f in fl4], [F[k] for k, _ in fl4], G4.nE)
    out = {}
    for R in ROTS:
        tr = int(np.trace(R)); m = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
        P, s = psg(rot(R), u)
        if s is None: out = None; break
        kind = {1: 'e', 3: 'C3', 4: 'C4'}.get(m)
        if m == 2: kind = 'C2axis' if np.allclose(np.abs(np.diag(R)), 1) else 'C2edge'
        out.setdefault(kind, set()).add(power_sign(P, s, m))
    (Px, sx), (Py, sy) = psg(trans((1, 0, 0)), u), psg(trans((0, 1, 0)), u)
    q = np.arange(G4.nV)
    out['TxTy'] = set(((sx[q] ^ sy[Px[q]]) ^ (sy[q] ^ sx[Py[q]])).tolist())
    commute = out['TxTy'] == {0}
    out['fixed'] = fixed_momenta(u) if commute else 'n/a (translations anticommute)'
    table[Fb] = out
    print('  ', ''.join(map(str, Fb)), {k: (sorted(v) if isinstance(v, set) else v) for k, v in out.items()})

# u-convention with H = -t1 sum u c^dag c (t1 = -1) as in the repo: corner model = (1, 0, 1, 1)
targets = [Fb for Fb, o in table.items()
           if o['C4'] == {-1} and o['C2axis'] == {-1} and o['TxTy'] == {0} and o['fixed'] not in ([], 'n/a (translations anticommute)')]
print("  patterns meeting all three targets (square C4^4 = -1, commuting translations, O-fixed momenta):", targets)
check("design targets select square = plaquette = tube = pi and leave the triangle free: exactly {1011, 1111}",
      sorted(targets) == [(1, 0, 1, 1), (1, 1, 1, 1)])
check("the O-fixed momenta of 1011 are k* = (pi/2)(1,-1,1) and -k* in this gauge family (units pi/2: (1,3,1),(3,1,3))",
      sorted(table[(1, 0, 1, 1)]['fixed']) == [(1, 3, 1), (3, 1, 3)])

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
