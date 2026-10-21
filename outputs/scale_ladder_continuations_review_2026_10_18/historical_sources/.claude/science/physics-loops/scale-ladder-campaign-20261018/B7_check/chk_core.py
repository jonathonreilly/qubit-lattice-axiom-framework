#!/usr/bin/env python3
"""Independent re-construction of the corner-fermion model (no import of the repo model or b7_model).

Model (from the docs / definitions): 12 corners {d,e} (perpendicular unit directions) per cubic site.
  onsite edges: {a,b} -- {a,f}, f = +-(third axis);  link edges: (v,{a,b}) -- (v+a,{-a,b}).
  Z2 fluxes: square (4 corners around one direction) = pi, triangle (octant) = 0,
             plaquette (cube face, 4 links) = pi, tube (around a link, 2 links + 2 onsite) = pi.
Own GF(2) solver; own translation-invariant gauge; own brute-force PSG (lam, tau) per O_h element.
Conventions: G_g |v,c> = (-1)^(lam.v + tau(c)) |R v, R c>;  H = sum_{v,d} |v+d><v| (x) h_d;
             H(k) = sum_d h_d e^{-i k.d};  fibre map k -> R k + pi R lam.
"""
import itertools
import numpy as np

DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def vadd(a, b): return tuple(x+y for x, y in zip(a, b))
CORN = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0]
CI = {c: i for i, c in enumerate(CORN)}
assert len(CORN) == 12
Z = (0, 0, 0)

def third(a, b):
    return [f for f in DIRS if dot(f, a) == 0 and dot(f, b) == 0]

# ---- edge list on the infinite lattice, as (corner1, site-offset 0) -- (corner2, offset s)
def edge_key(c1, c2, s):
    k1 = (CI[c1], CI[c2], tuple(s)); k2 = (CI[c2], CI[c1], neg(s))
    return min(k1, k2)
ETYPES = {}
for c in CORN:
    a, b = tuple(c)
    for x, y in ((a, b), (b, a)):
        for f in third(x, y):
            ETYPES.setdefault(edge_key(c, frozenset((x, f)), Z), len(ETYPES))
        ETYPES.setdefault(edge_key(c, frozenset((neg(x), y)), x), len(ETYPES))
NT = len(ETYPES)
assert NT == 36, NT
ELIST = sorted(ETYPES, key=ETYPES.get)

def gf2_solve(A, b):
    """A: (m, n) 0/1, b: (m,). Returns one solution x or None."""
    A = (np.array(A, np.uint8) % 2).copy(); b = (np.array(b, np.uint8) % 2).copy()
    m, n = A.shape; M = np.concatenate([A, b[:, None]], 1); r = 0; piv = []
    for col in range(n):
        rows = np.nonzero(M[r:, col])[0]
        if len(rows) == 0: continue
        p = r + rows[0]; M[[r, p]] = M[[p, r]]
        for i in range(m):
            if i != r and M[i, col]: M[i] ^= M[r]
        piv.append(col); r += 1
        if r == m: break
    if M[r:, n].any(): return None
    x = np.zeros(n, np.uint8)
    for i, col in enumerate(piv): x[col] = M[i, n]
    return x

def cyc_row(seq):
    """seq: list of (corner, site) around a closed loop -> GF(2) row over edge types."""
    row = np.zeros(NT, np.uint8)
    for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1]):
        row[ETYPES[edge_key(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]] ^= 1
    return row

def ring(d):
    a = [f for f in DIRS if dot(f, d) == 0]
    a0 = a[0]; b0 = [f for f in a if dot(f, a0) == 0][0]
    return [a0, b0, neg(a0), neg(b0)]

CYC = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for d in DIRS:
    rg = ring(d)
    CYC['square'].append(cyc_row([(frozenset((d, r)), Z) for r in rg]))
    for i in range(4):
        p, q = rg[i], rg[(i+1) % 4]
        CYC['tube'].append(cyc_row([(frozenset((d, p)), Z), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z)]))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    CYC['triangle'].append(cyc_row([(frozenset((x, y)), Z), (frozenset((y, z)), Z), (frozenset((z, x)), Z)]))
for d, e in itertools.permutations([(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)], 2):
    if dot(d, e) != 0: continue
    # all face orientations (not only the positive quadrant) -- over-determined, a consistency test
    CYC['plaquette'].append(cyc_row([(frozenset((d, e)), Z), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
FLUX = dict(square=1, triangle=0, plaquette=1, tube=1)
rows = []; rhs = []
for k, rs in CYC.items():
    for r in rs: rows.append(r); rhs.append(FLUX[k])
u = gf2_solve(rows, rhs)
assert u is not None
FLUX_OK = all(int(r @ u % 2) == FLUX[k] for k, rs in CYC.items() for r in rs)

# ---- O_h about site 0
OH = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        OH.append(M)
OH.sort(key=lambda M: (round(np.linalg.det(M)) != 1))   # proper first
PROPER = list(range(24)); ALL = list(range(48))
def rdir(M, d): return tuple(int(x) for x in M @ np.array(d))
def rcorn(M, c): return frozenset(rdir(M, d) for d in c)

def psg(M):
    """brute force (lam, tau) in GF(2)^3 x GF(2)^12 with sigma(q)+sigma(r) = u_e + u_{Me} on every edge type."""
    sols = []
    allbits = np.array(list(itertools.product((0, 1), repeat=15)), np.uint8)   # 32768 x 15
    lamb, taub = allbits[:, :3], allbits[:, 3:]
    ok = np.ones(len(allbits), bool)
    for (i1, i2, s) in ELIST:
        c1, c2 = CORN[i1], CORN[i2]
        ue = u[ETYPES[(i1, i2, s)]]
        ume = u[ETYPES[edge_key(rcorn(M, c1), rcorn(M, c2), rdir(M, s))]]
        lhs = (taub[:, i1] + lamb @ np.array(s) % 2 + taub[:, i2]) % 2
        ok &= lhs == (ue ^ ume)
    good = allbits[ok]
    return good
LAM, TAU, UF = [], [], []
for M in OH:
    good = psg(M)
    assert len(good) == 2, len(good)    # unique up to the global sign flip
    lam, tau = good[0][:3].astype(int), good[0][3:].astype(int)
    U = np.zeros((12, 12))
    for c in CORN: U[CI[rcorn(M, c)], CI[c]] = (-1.0) ** tau[CI[c]]
    LAM.append(lam); TAU.append(tau); UF.append(U)

def fibre_image(g, k):
    return OH[g] @ k + np.pi * (OH[g] @ LAM[g])

def wrap(k):
    return (np.asarray(k) + np.pi) % (2 * np.pi) - np.pi

def same_k(a, b, tol=1e-9):
    return np.allclose(wrap(np.asarray(a) - np.asarray(b)), 0, atol=tol)

# ---- real-space torus operators (L even: lam.v sign is periodic)
def torus_ops(L):
    sites = list(itertools.product(range(L), repeat=3)); si = {v: i for i, v in enumerate(sites)}
    n = 12 * len(sites)
    def G(g):
        A = np.zeros((n, n))
        for v in sites:
            w = tuple(int(x) % L for x in OH[g] @ np.array(v)); s = (-1.0) ** int(LAM[g] @ np.array(v))
            A[12*si[w]:12*si[w]+12, 12*si[v]:12*si[v]+12] = s * UF[g]
        return A
    def T(a):
        A = np.zeros((n, n))
        for v in sites:
            w = tuple((x + y) % L for x, y in zip(v, a)); A[12*si[w]:12*si[w]+12, 12*si[v]:12*si[v]+12] = np.eye(12)
        return A
    def from_blocks(h):
        A = np.zeros((n, n), complex)
        for v in sites:
            for d, B in h.items():
                w = tuple((x + y) % L for x, y in zip(v, d)); A[12*si[w]:12*si[w]+12, 12*si[v]:12*si[v]+12] += B
        return A
    def to_blocks(A, r=1):
        h = {}
        for d in itertools.product(range(-r, r+1), repeat=3):
            w = tuple(x % L for x in d); h[d] = A[12*si[w]:12*si[w]+12, 0:12].copy()
        return h
    def bloch(k):
        B = np.zeros((n, 12), complex)
        for v in sites:
            B[12*si[v]:12*si[v]+12, :] = np.exp(1j * np.dot(k, v)) * np.eye(12) / np.sqrt(len(sites))
        return B
    return dict(sites=sites, si=si, n=n, G=G, T=T, from_blocks=from_blocks, to_blocks=to_blocks, bloch=bloch)

def Hk(h, ks):
    ks = np.atleast_2d(ks); out = np.zeros((len(ks), 12, 12), complex)
    for d, B in h.items(): out += np.exp(-1j * ks @ np.array(d, float))[:, None, None] * B[None]
    return out

def mults(ev, tol=1e-7):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j+1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out

def find(M):
    return [g for g in ALL if (OH[g] == np.array(M)).all()][0]
