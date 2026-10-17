#!/usr/bin/env python3
"""Exploration: a fermion on the 12 corners (perpendicular direction pairs) of every
site, hopping in a Z2 gauge field with uniform fluxes; projective symmetry group (PSG)
of the site rotation group O, its class, and the single-site shell spectrum."""
import itertools, sys
import numpy as np

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def add(v, d): return tuple((a+b) % L for a, b in zip(v, d))
def perp(d, e): return sum(a*b for a, b in zip(d, e)) == 0 and d != e
CORNERS = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if sum(a*b for a,b in zip(d,e)) == 0]
assert len(CORNERS) == 12
SITES = list(itertools.product(range(L), repeat=3))
VERTS = [(v, c) for v in SITES for c in CORNERS]
VID = {q: i for i, q in enumerate(VERTS)}

edges = {}
def add_edge(q, r, kind):
    key = frozenset((VID[q], VID[r]))
    if key not in edges:
        edges[key] = kind
for v in SITES:
    for c in CORNERS:
        d, e = tuple(c)
        for a, b in ((d, e), (e, d)):           # share a, other directions b and f perpendicular
            for f in DIRS:
                if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                    add_edge((v, c), (v, frozenset((a, f))), 'onsite')
        for a, b in ((d, e), (e, d)):
            add_edge((v, c), (add(v, a), frozenset((neg(a), b))), 'link')
EDGES = list(edges)
EID = {k: i for i, k in enumerate(EDGES)}
nE = len(EDGES)
print(f"L={L}: {len(VERTS)} vertices, {nE} edges ({sum(1 for k in edges.values() if k=='onsite')} on-site)")
deg = np.zeros(len(VERTS), int)
for k in EDGES:
    for i in k: deg[i] += 1
assert set(deg) == {6}

def eid(q, r):
    return EID[frozenset((VID[q], VID[r]))]

def cycle_edges(qs):
    return [eid(qs[i], qs[(i+1) % len(qs)]) for i in range(len(qs))]

def axes_perp(d):
    return [f for f in DIRS if perp(f, d) and f != neg(d)]

cycles = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for v in SITES:
    for d in DIRS:
        a = [f for f in DIRS if perp(f, d) and f != neg(d)]
        a0 = a[0]; b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
        ring = [a0, b0, neg(a0), neg(b0)]
        cycles['square'].append(cycle_edges([(v, frozenset((d, r))) for r in ring]))
        # tubes around edge (v, v+d): quadrants (ring[i], ring[i+1])
        for i in range(4):
            p, q = ring[i], ring[(i+1) % 4]
            w = add(v, d)
            qs = [(v, frozenset((d, p))), (w, frozenset((neg(d), p))), (w, frozenset((neg(d), q))), (v, frozenset((d, q)))]
            cycles['tube'].append(cycle_edges(qs))
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
        cycles['triangle'].append(cycle_edges([(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))]))
    for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
        qs = [(v, frozenset((d, e))), (add(v, d), frozenset((neg(d), e))),
              (add(add(v, d), e), frozenset((neg(d), neg(e)))), (add(v, e), frozenset((d, neg(e))))]
        cycles['plaquette'].append(cycle_edges(qs))


def gf2_solve(rows, rhs, n):
    """Solve A x = b over GF(2) with Python-int bitsets. Returns uint8 array or None."""
    piv = {}  # pivot column -> row bitset (bit n = rhs)
    for r, b in zip(rows, rhs):
        x = 0
        for j in r: x ^= (1 << j)
        if b: x ^= (1 << n)
        while True:
            low = x & ((1 << n) - 1)
            if low == 0:
                if x: return None
                break
            c = low.bit_length() - 1
            if c in piv: x ^= piv[c]
            else:
                piv[c] = x; break
    # back substitution: process pivots in increasing column order
    sol = 0
    for c in sorted(piv):
        x = piv[c]
        rest = (x & ((1 << c) - 1))
        val = ((x >> n) & 1) ^ (bin(rest & sol).count('1') & 1)
        if val: sol |= (1 << c)
    out = np.zeros(n, dtype=np.uint8)
    for j in range(n):
        if (sol >> j) & 1: out[j] = 1
    return out


def solve_u(F):
    rows, rhs = [], []
    for k, cs in cycles.items():
        for c in cs:
            rows.append(c); rhs.append(F[k])
    return gf2_solve(rows, rhs, nE)

# rotations about site 0
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
assert len(ROTS) == 24
def rot_dir(R, d): return tuple(int(x) for x in R @ np.array(d))
def rot_site(R, v): return tuple(int(x) % L for x in R @ np.array(v))
def rot_vert(R, q):
    v, c = q
    return (rot_site(R, v), frozenset(rot_dir(R, d) for d in c))
def trans_vert(t, q):
    v, c = q
    return (add(v, t), c)

def vperm(f):
    return np.array([VID[f(q)] for q in VERTS])

def psg_sign(f, u):
    """Find sigma (GF(2) per vertex) with sigma(q)+sigma(r) = u_e + u_{f e}."""
    P = vperm(f)
    rows, rhs = [], []
    for k in EDGES:
        i, j = tuple(k)
        fe = EID[frozenset((P[i], P[j]))]
        # sigma indexed by image vertex: c_q -> sigma(q) c_{fq}
        rows.append([i, j]); rhs.append(u[EID[k]] ^ u[fe])
    s = gf2_solve(rows, rhs, len(VERTS))
    return P, s

def mono(P, s):
    n = len(P)
    M = np.zeros((n, n))
    M[P, np.arange(n)] = (-1.0) ** s
    return M

def classify(F, verbose=True):
    u = solve_u(F)
    if u is None:
        return None
    res = {}
    Ms = []
    for R in ROTS:
        P, s = psg_sign(lambda q, R=R: rot_vert(R, q), u)
        if s is None:
            return 'not invariant'
        Ms.append((P, s))
    # squares of involutions and C4^4 via sparse application
    def apply(Ps, vec_sign):
        pass
    def power_sign(P, s, k):
        # (M)^k on basis vector q: returns sign if returns to q
        n = len(P); sign = np.zeros(n, np.uint8); idx = np.arange(n)
        cur = idx.copy()
        for _ in range(k):
            sign ^= s[cur]; cur = P[cur]
        return cur, sign
    out = {}
    for R, (P, s) in zip(ROTS, Ms):
        tr = int(np.trace(R)); order = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
        cur, sign = power_sign(P, s, order)
        assert (cur == np.arange(len(P))).all()
        vals = set(sign.tolist())
        assert len(vals) == 1, "global sign expected"
        kind = {1: 'e', 3: 'C3', 4: 'C4'}.get(order)
        if order == 2:
            kind = 'C2axis' if np.allclose(np.abs(np.diag(R)), 1) else 'C2edge'
        out.setdefault(kind, set()).add(-1 if vals.pop() else 1)
    # translations
    tr_ok = []
    for t in ((1,0,0),(0,1,0)):
        P, s = psg_sign(lambda q, t=t: trans_vert(t, q), u)
        tr_ok.append((P, s))
    (Px, sx), (Py, sy) = tr_ok
    # commutator TxTy vs TyTx on a vertex: sign
    n = len(Px); q = np.arange(n)
    a = sx[q] ^ sy[Px[q]]   # Ty Tx: apply Tx then Ty
    b = sy[q] ^ sx[Py[q]]
    comm = set((a ^ b).tolist())
    out['TxTy'] = {(-1 if c else 1) for c in comm}
    return out, u, Ms

if __name__ == '__main__':
    for F in itertools.product((0, 1), repeat=4):
        Fd = dict(zip(('square', 'triangle', 'plaquette', 'tube'), F))
        r = classify(Fd)
        if r is None:
            print(Fd, 'inconsistent'); continue
        if r == 'not invariant':
            print(Fd, 'not O-invariant'); continue
        out, u, Ms = r
        print({k: ('pi' if v else '0') for k, v in Fd.items()}, {k: sorted(v) for k, v in out.items()})
