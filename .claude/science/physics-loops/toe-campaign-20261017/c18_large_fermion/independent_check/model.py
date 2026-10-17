"""Independent model of the corner fermion (C18 check).  Written from the note's text only.

Vertices: (n, c), n in Z^3, c = unordered pair of perpendicular unit directions (12 per site).
Edges:    on-site  {a,b} -- {a,f}   (share a; b, f perpendicular)        24 per cell
          link     (n,{a,b}) -- (n+a,{-a,b})                            12 per cell
Cycles are found by brute-force enumeration of all 3- and 4-cycles and classified by
geometry (independent of the runner's cycle lists).
Conventions (mine):
  c_{k,c} = N^-1/2 sum_n e^{-ik.n} c_{n,c};  a term z c^dag_{n+sh,c2} c_{n,c1} gives
  H(k)[c2,c1] += z e^{-ik.sh}.
  Hamiltonian H = -t1 sum_onsite u (c^dag c + h.c.) - t2 sum_links u (c^dag c + h.c.)
                 + i lam sum_{oriented triangle edges q->r} u_qr c^dag_r c_q + h.c.
  triangle orientation: counterclockwise seen from outside (along the outward octant diagonal).
"""
import itertools
import numpy as np

DV = [np.array(v) for v in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
def didx(v):
    v = tuple(int(x) for x in v)
    for i, w in enumerate(DV):
        if tuple(w) == v: return i
    raise KeyError(v)
CORN = [(i, j) for i, j in itertools.combinations(range(6), 2) if DV[i] @ DV[j] == 0]
assert len(CORN) == 12
CIDX = {c: k for k, c in enumerate(CORN)}
def cnorm(i, j): return CIDX[tuple(sorted((i, j)))]
def cpos(c):  # geometric position of a corner (for orientation only)
    i, j = CORN[c]; return (DV[i] + DV[j]) / 2.0

# ---- neighbours of (0,c): list of (c2, shift, kind)
def neighbours(c):
    out = []
    i, j = CORN[c]
    for a, b in ((i, j), (j, i)):
        for f in range(6):
            if DV[f] @ DV[a] == 0 and DV[f] @ DV[b] == 0:
                out.append((cnorm(a, f), (0, 0, 0), 'o'))
        out.append((cnorm(didx(-DV[a]), b), tuple(DV[a]), 'l'))
    return out
for c in range(12): assert len(neighbours(c)) == 6

# ---- unit-cell edge types; key (c1,c2,sh) and reversed (c2,c1,-sh)
ETYPES = []; EKEY = {}
for c in range(12):
    for c2, sh, kind in neighbours(c):
        if (c, c2, sh) in EKEY: continue
        k = len(ETYPES); ETYPES.append((c, c2, sh, kind))
        EKEY[(c, c2, sh)] = k; EKEY[(c2, c, tuple(-x for x in sh))] = k
NT = len(ETYPES)
assert NT == 36 and sum(e[3] == 'o' for e in ETYPES) == 24

def edge_type(v1, v2):
    (n1, c1), (n2, c2) = v1, v2
    return EKEY[(c1, c2, tuple(b - a for a, b in zip(n1, n2)))]

def nbrs_abs(v):
    n, c = v
    return [(tuple(a + b for a, b in zip(n, sh)), c2) for c2, sh, _ in neighbours(c)]

# ---- enumerate all simple 3- and 4-cycles through vertices of cell 0, classify
def enum_cycles():
    found = {}
    for c0 in range(12):
        start = ((0, 0, 0), c0)
        stack = [[start]]
        while stack:
            path = stack.pop()
            if len(path) > 4: continue
            for w in nbrs_abs(path[-1]):
                if w == start and len(path) >= 3:
                    cyc = path[:]
                    key = frozenset(frozenset((cyc[i], cyc[(i+1) % len(cyc)])) for i in range(len(cyc)))
                    found.setdefault(key, cyc)
                elif w not in path and len(path) < 4:
                    stack.append(path + [w])
    return list(found.values())

def classify_cycle(cyc):
    sites = {v[0] for v in cyc}
    kinds = [ETYPES[edge_type(cyc[i], cyc[(i+1) % len(cyc)])][3] for i in range(len(cyc))]
    nl = kinds.count('l')
    if len(cyc) == 3 and nl == 0: return 'triangle'
    if len(cyc) == 4 and nl == 0:
        common = set(CORN[cyc[0][1]])
        for v in cyc: common &= set(CORN[v[1]])
        return 'square' if common else 'two_triangles'
    if len(cyc) == 4 and nl == 4 and len(sites) == 4: return 'plaquette'
    if len(cyc) == 4 and nl == 2 and len(sites) == 2: return 'tube'
    return 'other:%d:%d:%d' % (len(cyc), nl, len(sites))

ALLCYC = enum_cycles()
CYCCLASS = [classify_cycle(c) for c in ALLCYC]

def cycle_types_mod2(cyc):
    x = 0
    for i in range(len(cyc)):
        x ^= 1 << edge_type(cyc[i], cyc[(i+1) % len(cyc)])
    return x

# ---- GF(2) linear solver (bitset rows); returns one solution and a nullspace basis
def gf2(rows, rhs, n):
    piv = {}
    for r, b in zip(rows, rhs):
        x = r | (b << n)
        while x & ((1 << n) - 1):
            p = (x & ((1 << n) - 1)).bit_length() - 1
            if p in piv: x ^= piv[p]
            else: piv[p] = x; break
        else:
            if x: return None, None
    # full reduction
    ps = sorted(piv)
    for p in ps:
        for q in ps:
            if q != p and (piv[q] >> p) & 1: piv[q] ^= piv[p]
    sol = [0] * n
    for p in ps: sol[p] = (piv[p] >> n) & 1
    free = [j for j in range(n) if j not in piv]
    null = []
    for f in free:
        v = [0] * n; v[f] = 1
        for p in ps:
            if (piv[p] >> f) & 1: v[p] = 1
        null.append(v)
    return sol, null

FLUXNAMES = ('square', 'triangle', 'plaquette', 'tube')
def solve_gauge(F, seed=None):
    """translation-invariant Z2 gauge field u[edge type] with flux F on every enumerated cycle."""
    rows, rhs = [], []
    for cyc, cl in zip(ALLCYC, CYCCLASS):
        rows.append(cycle_types_mod2(cyc))
        rhs.append({'square': F['square'], 'triangle': F['triangle'], 'plaquette': F['plaquette'],
                    'tube': F['tube'], 'two_triangles': 0}[cl])
    sol, null = gf2(rows, rhs, NT)
    if sol is None: return None
    if seed is not None:
        rng = np.random.default_rng(seed)
        for v in null:
            if rng.integers(2): sol = [a ^ b for a, b in zip(sol, v)]
    return np.array(sol)

# ---- triangles (oriented ccw from outside)
def triangles():
    out = []
    for s in itertools.product((1, -1), repeat=3):
        d = [didx(np.array(e) * si) for e, si in zip(((1,0,0),(0,1,0),(0,0,1)), s)]
        cs = [cnorm(d[0], d[1]), cnorm(d[1], d[2]), cnorm(d[2], d[0])]
        a, b, c = (cpos(x) for x in cs)
        if np.cross(b - a, c - b) @ np.array(s) < 0: cs = cs[::-1]
        out.append(cs)
    return out
TRIS = triangles()

def bloch(u, k, t1, t2, lam, extra=None):
    k = np.asarray(k, float)
    H = np.zeros((12, 12), complex)
    for j, (c1, c2, sh, kind) in enumerate(ETYPES):
        z = -(t1 if kind == 'o' else t2) * (-1.0) ** u[j]
        a = z * np.exp(-1j * k @ np.array(sh))
        H[c2, c1] += a; H[c1, c2] += np.conj(a)
    for cs in TRIS:
        for q, r in zip(cs, cs[1:] + cs[:1]):
            a = 1j * lam * (-1.0) ** u[EKEY[(q, r, (0, 0, 0))]]
            H[r, q] += a; H[q, r] += np.conj(a)
    if extra is not None:
        for (c1, c2, sh, z) in extra:
            a = z * np.exp(-1j * k @ np.array(sh))
            H[c2, c1] += a; H[c1, c2] += np.conj(a)
    return H

def bloch_batch(u, ks, t1, t2, lam, extra=None):
    ks = np.atleast_2d(ks)
    H = np.zeros((len(ks), 12, 12), complex)
    for j, (c1, c2, sh, kind) in enumerate(ETYPES):
        z = -(t1 if kind == 'o' else t2) * (-1.0) ** u[j]
        a = z * np.exp(-1j * ks @ np.array(sh))
        H[:, c2, c1] += a; H[:, c1, c2] += np.conj(a)
    for cs in TRIS:
        for q, r in zip(cs, cs[1:] + cs[:1]):
            a = 1j * lam * (-1.0) ** u[EKEY[(q, r, (0, 0, 0))]]
            H[:, r, q] += a; H[:, q, r] += np.conj(a)
    if extra is not None:
        for (c1, c2, sh, z) in extra:
            a = z * np.exp(-1j * ks @ np.array(sh))
            H[:, c2, c1] += a; H[:, c1, c2] += np.conj(a)
    return H

# ---- point group O (proper) and inversion
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
assert len(ROTS) == 24
def rot_corner(R, c):
    i, j = CORN[c]; return cnorm(didx(R @ DV[i]), didx(R @ DV[j]))
def w1(R):  # parity of the permutation of the six directions
    p = [didx(R @ DV[i]) for i in range(6)]; s = 0; seen = [False] * 6
    for i in range(6):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]: seen[j] = True; j = p[j]; L += 1
            s += L - 1
    return s % 2

def psg(u, R, conj=False):
    """solve sigma(n,c) = eta(c)(-1)^{s.n} with u[R e] = u[e] + sigma(i) + sigma(j)."""
    rows, rhs = [], []
    for j, (c1, c2, sh, kind) in enumerate(ETYPES):
        Rsh = tuple(int(x) for x in R @ np.array(sh))
        jR = EKEY[(rot_corner(R, c1), rot_corner(R, c2), Rsh)]
        x = (1 << c1) ^ (1 << c2)
        for a in range(3):
            if sh[a] % 2: x ^= 1 << (12 + a)
        rows.append(x); rhs.append(int(u[jR] ^ u[j]))
    sol, null = gf2(rows, rhs, 15)
    if sol is None: return None
    eta = np.array([(-1.0) ** sol[c] for c in range(12)]); s = np.array(sol[12:15])
    return eta, s

def Wmat(R, eta):
    W = np.zeros((12, 12))
    for c in range(12): W[rot_corner(R, c), c] = eta[c]
    return W
