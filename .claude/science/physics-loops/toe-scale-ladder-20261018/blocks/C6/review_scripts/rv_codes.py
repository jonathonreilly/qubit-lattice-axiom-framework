"""Reviewer's independent builders (own reading of the definitions in NOTE.md section 0 and the repo notes).
Conventions deliberately differ from c6_lib (qubit indexing, direction labels, Majorana<->qubit map, loop
orientation), so only convention-independent quantities (k, TQO counts, exchange sign) are compared."""
import itertools
import numpy as np
from rv_gf2 import Pauli, Xs, Z_on, Y_on, prod

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
# my direction labels: 0..5 = +x,+y,+z,-x,-y,-z
D6 = [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]

def shift(v, a, s, L):
    w = list(v); w[a] = (w[a] + s) % L; return tuple(w)

class Code:
    def __init__(self, name, n, gens, site_of_qubit, L, **meta):
        self.name, self.n, self.gens, self.site, self.L = name, n, gens, site_of_qubit, L
        self.meta = meta

# ------------------------------------------------------------- cubic BKSF (F1) and toric control
def bksf(L, order, flux=(0, 0, 0), twisted=True):
    S = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(S)}
    n = 3 * len(S)
    def e(v, a): return idx[v] + len(S) * a          # different indexing from c6_lib
    rank_of = {d: order.index(d) for d in range(6)}
    def edge(v, d):
        a, s = D6[d]
        return e(v, a) if s == 1 else e(shift(v, a, -1, L), a)
    def A(v, a):
        w = shift(v, a, 1, L)
        P = Xs(n, [e(v, a)])
        if twisted:
            dp, dm = a, a + 3
            zs = [edge(v, d) for d in range(6) if rank_of[d] < rank_of[dp]] + \
                 [edge(w, d) for d in range(6) if rank_of[d] < rank_of[dm]]
            P = P * Z_on(n, zs)
        return P
    def B(v): return Z_on(n, [edge(v, d) for d in range(6)])
    def plaq(v, c):
        a, b = [k for k in range(3) if k != c]
        # orientation: v -> v+a -> v+a+b -> v+b -> v  (product order differs from c6_lib)
        P = prod([A(v, b), A(shift(v, b, 1, L), a), A(shift(v, a, 1, L), b), A(v, a)], n)
        P.ph = (P.ph + 2 * flux[c]) % 4
        return P
    gens = [B(v) for v in S] + [plaq(v, c) for v in S for c in range(3)]
    site = [S[q % len(S)] for q in range(n)]
    def hop(v, d):
        a, s = D6[d]
        return A(v, a) if s == 1 else A(shift(v, a, -1, L), a)
    return Code('F1' if twisted else 'toric', n, gens, site, L, hop=hop, B=B, plaq=plaq)

# ------------------------------------------------------------- Majorana families (F3, F4)
def majorana_ops(n, base, nq, k):
    """Own JW per site with REVERSED qubit order: gamma_{2j} = Z_{>j} X_j, gamma_{2j+1} = Z_{>j} Y_j,
    where qubit j means base + (nq-1-j)."""
    j = k // 2
    qs = [base + (nq - 1 - i) for i in range(j)]
    P = Z_on(n, qs)
    q = base + (nq - 1 - j)
    return P * (Xs(n, [q]) if k % 2 == 0 else Y_on(n, q))

def mpd(L, flux=(0, 0, 0), spinful=False):
    S = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(S)}
    nq = 5 if spinful else 3
    n = nq * len(S)
    perm = [3, 0, 4, 1, 5, 2]           # direction -> Majorana index (differs from c6_lib)
    def g(v, k): return majorana_ops(n, nq * idx[v], nq, k)
    def gd(v, d): return g(v, perm[d])
    def A(v, a):
        return gd(v, a) * gd(shift(v, a, 1, L), a + 3)
    def hermitize(P):
        if not P.hermitian(): P.ph = (P.ph + 1) % 4
        return P
    def B(v):
        P = prod([g(v, k) for k in range(2 * nq)], n); P = hermitize(P)
        return P
    gens = [B(v) for v in S]
    if spinful:
        for v in S:
            gens.append(hermitize(g(v, 6) * g(v, 7)))
            gens.append(hermitize(g(v, 8) * g(v, 9)))
    def plaq(v, c):
        a, b = [k for k in range(3) if k != c]
        P = prod([A(v, b), A(shift(v, b, 1, L), a), A(shift(v, a, 1, L), b), A(v, a)], n)
        P = hermitize(P); P.ph = (P.ph + 2 * flux[c]) % 4
        return P
    gens += [plaq(v, c) for v in S for c in range(3)]
    site = [S[q // nq] for q in range(n)]
    def hop(v, d):
        a, s = D6[d]
        return A(v, a) if s == 1 else A(shift(v, a, -1, L), a)
    return Code('F4' if spinful else 'F3', n, gens, site, L, hop=hop, B=B, plaq=plaq)

# ------------------------------------------------------------- corner code (F5), own construction
UNIT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def ng(d): return tuple(-x for x in d)
def dt(a, b): return sum(x * y for x, y in zip(a, b))
CN = [frozenset(p) for p in itertools.combinations(UNIT, 2) if dt(*p) == 0]   # 12 corners

def corner_code(L, vertex_order_seed=0):
    import random
    S = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(S)}
    def add(v, d): return tuple((v[i] + d[i]) % L for i in range(3))
    # on-site edges: corners sharing exactly one vector, other vectors perpendicular
    ons = [frozenset((c1, c2)) for c1, c2 in itertools.combinations(CN, 2)
           if len(c1 & c2) == 1 and dt(next(iter(c1 - c2)), next(iter(c2 - c1))) == 0]
    assert len(ons) == 24
    halves = [(c, a) for c in CN for a in c]       # half-link at corner c pointing along a
    lab = {('o', o): i for i, o in enumerate(ons)}
    lab.update({('h', h): 24 + i for i, h in enumerate(halves)})
    n = 48 * len(S)
    def qb(v, l): return 48 * idx[v] + lab[l]
    # incident edges of vertex (v, c) as (neighbor, edge-id, representative-qubit-at-this-end, X-qubits)
    def other(c, a): return next(iter(c - {a}))
    def inc(v, c):
        out = []
        for o in ons:
            if c in o:
                c2 = next(iter(o - {c}))
                out.append(((v, c2), ('o', v, o), qb(v, ('o', o)), [qb(v, ('o', o))], ('o', tuple(sorted(c2)))))
        for a in c:
            w = add(v, a); c2 = frozenset((ng(a), other(c, a)))
            h1, h2 = qb(v, ('h', (c, a))), qb(w, ('h', (c2, ng(a))))
            out.append(((w, c2), ('l', min(h1, h2), max(h1, h2)), h1, [h1, h2], ('l', a)))
        return out
    INC = {(v, c): inc(v, c) for v in S for c in CN}
    rng = random.Random(vertex_order_seed)
    allkeys = sorted({t[4] for lst in INC.values() for t in lst}, key=str)
    rng.shuffle(allkeys)
    rank = {k: i for i, k in enumerate(allkeys)}
    ORD = {q: {t[1]: rank[t[4]] for t in lst} for q, lst in INC.items()}
    def A(q, r):
        v, c = q
        it = [t for t in INC[q] if t[0] == r]
        assert len(it) == 1
        nb, eid, rq, xq, _k = it[0]
        zs = [t[2] for t in INC[q] if ORD[q][t[1]] < ORD[q][eid]] + \
             [t[2] for t in INC[r] if ORD[r][t[1]] < ORD[r][eid]]
        return Xs(n, xq) * Z_on(n, zs)
    def B(q): return Z_on(n, [t[2] for t in INC[q]])
    gens = [B((v, c)) for v in S for c in CN]
    seenl = set()
    for v in S:
        for c in CN:
            for t in INC[(v, c)]:
                if t[1][0] == 'l' and t[1] not in seenl:
                    seenl.add(t[1]); gens.append(Z_on(n, t[3]))
    cells = []
    for v in S:
        # 6 squares of the cuboctahedron: corners containing a fixed vector d, cyclically ordered
        for d in UNIT:
            ring = [r for r in UNIT if dt(r, d) == 0]
            # cyclic order: r0, r1 perpendicular to r0, -r0, -r1
            r0 = ring[0]; r1 = [r for r in ring if dt(r, r0) == 0][0]
            cyc = [r0, r1, ng(r0), ng(r1)]
            cells.append([(v, frozenset((d, r))) for r in cyc])
        # 8 triangles
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
            cells.append([(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))])
        # tubes: only along +a (each lattice edge once)
        for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            ring = [r for r in UNIT if dt(r, d) == 0]
            r0 = ring[0]; r1 = [r for r in ring if dt(r, r0) == 0][0]
            cyc = [r0, r1, ng(r0), ng(r1)]
            w = add(v, d)
            for i in range(4):
                p, q = cyc[i], cyc[(i + 1) % 4]
                cells.append([(v, frozenset((d, p))), (w, frozenset((ng(d), p))), (w, frozenset((ng(d), q))), (v, frozenset((d, q)))])
        # plaquettes: 4 links
        for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
            cells.append([(v, frozenset((d, e))), (add(v, d), frozenset((ng(d), e))),
                          (add(add(v, d), e), frozenset((ng(d), ng(e)))), (add(v, e), frozenset((d, ng(e))))])
    for cyc in cells:
        P = prod([A(cyc[i], cyc[(i + 1) % len(cyc)]) for i in range(len(cyc))], n)
        gens.append(P)
    site = [S[q // 48] for q in range(n)]
    return Code('F5', n, gens, site, L, A=A, B=B, INC=INC, cells=cells)
