#!/usr/bin/env python3
"""C6 library: exact Pauli / GF(2) tools and builders for the five supplied code families.

Pauli convention (same as the repo corner runner): (x, z, p) = i^p X^x Z^z with x, z python ints
(bit q = qubit q).  All linear algebra is exact over GF(2) on python-int bitsets.

Families (supplied premises, definitions transcribed from the 2026-10-17 notes / runners):
  F1 edge BKSF        : qubit per edge of Z^3, ordering of six directions, 8 flux sectors
  F2 six-direction    : six half-edge qubits per site, R = ZZ repetition, same ordering
  F3 MPD              : three qubits per site = six Majoranas gamma_{v,d} (on-site JW), 8 sign sectors
  F4 spinful MPD      : five qubits per site = six link + four matter Majoranas
  F5 corner           : BKSF on the corner graph, 48 qubits per site (repetition halves), 16 flux patterns
"""
from __future__ import annotations
import itertools

# ---------------------------------------------------------------- Pauli algebra
def pc(v):
    return bin(v).count('1')


def pmul(a, b):
    return (a[0] ^ b[0], a[1] ^ b[1], (a[2] + b[2] + 2 * pc(a[1] & b[0])) % 4)


def pcomm(a, b):
    return (pc(a[0] & b[1]) + pc(a[1] & b[0])) % 2 == 0


def herm(a):
    return (a[2] - pc(a[0] & a[1])) % 2 == 0


def pinv(P):
    return (P[0], P[1], (-P[2] - 2 * pc(P[0] & P[1])) % 4)


def Xs(qs):
    x = 0
    for q in qs:
        x ^= 1 << q
    return (x, 0, 0)


def Zs(qs):
    z = 0
    for q in qs:
        z ^= 1 << q
    return (0, z, 0)


def prod(ops, start=(0, 0, 0)):
    P = start
    for o in ops:
        P = pmul(P, o)
    return P


def support(P):
    return P[0] | P[1]


def bits(v):
    out = []
    while v:
        b = v & -v
        out.append(b.bit_length() - 1)
        v ^= b
    return out


# ---------------------------------------------------------------- GF(2) with sign tracking
class Group:
    """Incremental elimination of Paulis on n qubits; tracks products so that -I can be detected."""

    def __init__(self, n, phases=True):
        self.n = n
        self.piv = {}
        self.phases = phases
        self.neg_identity = False

    def vec(self, P):
        return P[0] | (P[1] << self.n)

    def add(self, P):
        v = self.vec(P)
        comb = P
        while v:
            c = v.bit_length() - 1
            if c in self.piv:
                pv, pP = self.piv[c]
                v ^= pv
                if self.phases:
                    comb = pmul(comb, pP)
            else:
                self.piv[c] = (v, comb)
                return True
        if self.phases and comb[2] % 4 != 0:
            self.neg_identity = True   # a product of generators equals a nontrivial phase times I
        return False

    def contains(self, P):
        v = self.vec(P)
        while v:
            c = v.bit_length() - 1
            if c not in self.piv:
                return False
            v ^= self.piv[c][0]
        return True

    @property
    def rank(self):
        return len(self.piv)


class Basis:
    """Plain GF(2) basis of python ints (no phases)."""

    def __init__(self):
        self.piv = {}

    def reduce(self, v):
        while v:
            c = v.bit_length() - 1
            if c in self.piv:
                v ^= self.piv[c]
            else:
                return v
        return 0

    def add(self, v):
        r = self.reduce(v)
        if r:
            self.piv[r.bit_length() - 1] = r
            return True
        return False

    @property
    def rank(self):
        return len(self.piv)


def nullspace(rows, ncols):
    """Basis of {x in GF(2)^ncols : <row, x> = 0 for all rows}; rows are ints over ncols bits."""
    # column-echelon via elimination on rows (RREF), then read off nullspace
    piv = {}            # pivot column -> row (fully reduced)
    for r in rows:
        for c, pr in piv.items():
            if (r >> c) & 1:
                r ^= pr
        if r:
            c = r.bit_length() - 1
            for c2 in list(piv):
                if (piv[c2] >> c) & 1:
                    piv[c2] ^= r
            piv[c] = r
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
        x = 1 << f
        for c, pr in piv.items():
            if (pr >> f) & 1:
                x |= 1 << c
        out.append(x)
    return out


def symp_swap(P, n):
    """Return the int w with <w, vec(Q)> = commutation bit of P and Q (vec = x | z<<n)."""
    return P[1] | (P[0] << n)


# ---------------------------------------------------------------- generic code container
class Code:
    def __init__(self, name, L, n, gens, qsite, meta=None):
        self.name, self.L, self.n, self.gens, self.qsite = name, L, n, gens, qsite
        self.meta = meta or {}
        self.gsite = []          # list of site-sets each generator touches
        for g in gens:
            self.gsite.append({qsite[q] for q in bits(support(g))})

    def group(self, phases=True):
        G = Group(self.n, phases)
        for g in self.gens:
            G.add(g)
        return G


def tadd(v, d, L):
    return tuple((v[i] + d[i]) % L for i in range(3))


E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS6 = [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]   # (axis, sign), as in the repo edge-BKSF runner


def dvec(d):
    a, s = DIRS6[d]
    return tuple(s * E3[a][i] for i in range(3))


def sites(L):
    return list(itertools.product(range(L), repeat=3))


def sid(v, L):
    return (v[0] * L + v[1]) * L + v[2]


# ---------------------------------------------------------------- F1: edge BKSF
def edge_bksf(L, order, flux=(0, 0, 0), twisted=True):
    """Qubit 3*sid(v)+a on edge v -> v+e_a.  A_(v,a) = X_e Z(edges at v before +a) Z(edges at v+e_a before -a).
    B_v = Z on six edges at v.  S_p (plane normal c) = (-1)^flux[c] A(v,a) A(v+a,b) A(v+b,a) A(v,b)."""
    S = sites(L)
    n = 3 * L ** 3
    pos = {d: i for i, d in enumerate(order)}

    def q(v, a):
        return 3 * sid(v, L) + a

    def edge_at(v, d):
        a, s = DIRS6[d]
        return q(v, a) if s == 1 else q(tadd(v, tuple(-x for x in E3[a]), L), a)

    def A(v, a):
        w = tadd(v, E3[a], L)
        P = Xs([q(v, a)])
        if not twisted:
            return P
        dp, dm = DIRS6.index((a, 1)), DIRS6.index((a, -1))
        zs = [edge_at(v, d) for d in range(6) if pos[d] < pos[dp]] + [edge_at(w, d) for d in range(6) if pos[d] < pos[dm]]
        Z = 0
        for z in zs:
            Z ^= 1 << z
        return pmul(P, (0, Z, 0))

    def B(v):
        return Zs([edge_at(v, d) for d in range(6)])

    def plaq(v, c):
        a, b = [k for k in range(3) if k != c]
        P = prod([A(v, a), A(tadd(v, E3[a], L), b), A(tadd(v, E3[b], L), a), A(v, b)])
        return (P[0], P[1], (P[2] + 2 * flux[c]) % 4)

    gens = [B(v) for v in S] + [plaq(v, c) for v in S for c in range(3)]
    qsite = [S[i // 3] for i in range(n)]
    meta = dict(A=A, B=B, q=q, kind='edge')
    return Code(f'F1 edge-BKSF order={order} flux={flux}', L, n, gens, qsite, meta)


# ---------------------------------------------------------------- F2: six-direction site-local
def sixdir_bksf(L, order, flux=(0, 0, 0)):
    S = sites(L)
    n = 6 * L ** 3
    pos = {d: i for i, d in enumerate(order)}

    def q(v, d):
        return 6 * sid(v, L) + d

    def A(v, a):
        w = tadd(v, E3[a], L)
        dp, dm = DIRS6.index((a, 1)), DIRS6.index((a, -1))
        P = Xs([q(v, dp), q(w, dm)])
        zs = [q(v, d) for d in range(6) if pos[d] < pos[dp]] + [q(w, d) for d in range(6) if pos[d] < pos[dm]]
        return pmul(P, Zs(zs))

    def B(v):
        return Zs([q(v, d) for d in range(6)])

    def R(v, a):
        return Zs([q(v, DIRS6.index((a, 1))), q(tadd(v, E3[a], L), DIRS6.index((a, -1)))])

    def plaq(v, c):
        a, b = [k for k in range(3) if k != c]
        P = prod([A(v, a), A(tadd(v, E3[a], L), b), A(tadd(v, E3[b], L), a), A(v, b)])
        return (P[0], P[1], (P[2] + 2 * flux[c]) % 4)

    gens = [B(v) for v in S] + [R(v, a) for v in S for a in range(3)] + [plaq(v, c) for v in S for c in range(3)]
    qsite = [S[i // 6] for i in range(n)]
    return Code(f'F2 six-direction order={order} flux={flux}', L, n, gens, qsite, dict(A=A, B=B, q=q, kind='sixdir'))


# ---------------------------------------------------------------- Majorana helpers (on-site Jordan-Wigner)
def majorana(site_index, k, nq_per_site):
    """gamma_k on a site with nq qubits: gamma_{2j} = Z_<j X_j, gamma_{2j+1} = Z_<j Y_j  (Y = i X Z)."""
    base = nq_per_site * site_index
    j = k // 2
    P = Zs([base + i for i in range(j)])
    if k % 2 == 0:
        return pmul(P, Xs([base + j]))
    return pmul(P, (1 << (base + j), 1 << (base + j), 1))


def maj_word(ms):
    return prod(ms)


# ---------------------------------------------------------------- F3: Majorana per direction
def mpd(L, flux=(0, 0, 0)):
    """gamma_{v,d}, d in DIRS6 index order, Majorana index k = d.  B_v = (-i)^3 g0..g5 = Z Z Z,
    A_(v,a) = gamma_{v,+a} gamma_{v+e_a,-a},  S_p = (-1)^flux[c] A(v,a) A(v+a,b) A(v+b,a) A(v,b)."""
    S = sites(L)
    n = 3 * L ** 3

    def g(v, d):
        return majorana(sid(v, L), d, 3)

    def A(v, a):
        return pmul(g(v, DIRS6.index((a, 1))), g(tadd(v, E3[a], L), DIRS6.index((a, -1))))

    def B(v):
        P = prod([g(v, d) for d in range(6)], start=(0, 0, 0))
        return (P[0], P[1], (P[2] - 3) % 4)

    def plaq(v, c):
        a, b = [k for k in range(3) if k != c]
        P = prod([A(v, a), A(tadd(v, E3[a], L), b), A(tadd(v, E3[b], L), a), A(v, b)])
        return (P[0], P[1], (P[2] + 2 * flux[c]) % 4)

    gens = [B(v) for v in S] + [plaq(v, c) for v in S for c in range(3)]
    qsite = [S[i // 3] for i in range(n)]
    return Code(f'F3 MPD flux={flux}', L, n, gens, qsite, dict(A=A, B=B, g=g, kind='mpd'))


# ---------------------------------------------------------------- F4: spinful MPD
def spinful_mpd(L, flux=(0, 0, 0)):
    """Ten Majoranas per site (5 qubits): link b_d = gamma_d (d=0..5), matter gamma_6..gamma_9.
    D_v = (-i)^5 gamma_0..gamma_9 (total parity), P_up = -i g6 g7, P_dn = -i g8 g9,
    W_p = (-1)^flux[c] prod of u_e = b_{v,+a} b_{v+e_a,-a} around p."""
    S = sites(L)
    n = 5 * L ** 3

    def g(v, k):
        return majorana(sid(v, L), k, 5)

    def A(v, a):
        return pmul(g(v, DIRS6.index((a, 1))), g(tadd(v, E3[a], L), DIRS6.index((a, -1))))

    def D(v):
        P = prod([g(v, k) for k in range(10)])
        return (P[0], P[1], (P[2] - 5) % 4)

    def Pm(v, k):
        P = pmul(g(v, k), g(v, k + 1))
        return (P[0], P[1], (P[2] - 1) % 4)

    def plaq(v, c):
        a, b = [k for k in range(3) if k != c]
        P = prod([A(v, a), A(tadd(v, E3[a], L), b), A(tadd(v, E3[b], L), a), A(v, b)])
        return (P[0], P[1], (P[2] + 2 * flux[c]) % 4)

    gens = [D(v) for v in S] + [Pm(v, 6) for v in S] + [Pm(v, 8) for v in S] + [plaq(v, c) for v in S for c in range(3)]
    qsite = [S[i // 5] for i in range(n)]
    return Code(f'F4 spinful-MPD flux={flux}', L, n, gens, qsite, dict(A=A, B=D, g=g, kind='spinful'))


# ---------------------------------------------------------------- F5: corner code (transcribed from the repo runner)
def corner_code(L, FLUX=None):
    """Faithful transcription of scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py
    generator definitions (corner graph BKSF, 48 qubits/site, B_q, R, signed loops i^n F prod A)."""
    if FLUX is None:
        FLUX = dict(square=1, triangle=0, plaquette=1, tube=0)
    DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def neg(d): return tuple(-x for x in d)
    def dot(a, b): return sum(x * y for x, y in zip(a, b))
    def perp(d, e): return dot(d, e) == 0 and d != e
    def add(v, d): return tuple((a + b) % L for a, b in zip(v, d))
    def corner(*ds): return tuple(sorted(ds))
    CORN = sorted([tuple(sorted((d, e))) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0])
    SITES = sites(L)
    SID = {v: i for i, v in enumerate(SITES)}
    VERTS = [(v, c) for v in SITES for c in CORN]
    ONS = []
    for c1, c2 in itertools.combinations(CORN, 2):
        s = set(c1) & set(c2)
        if len(s) == 1:
            a = s.pop(); b1 = [d for d in c1 if d != a][0]; b2 = [d for d in c2 if d != a][0]
            if perp(b1, b2) and b1 != neg(b2):
                ONS.append((c1, c2))
    assert len(ONS) == 24
    HALF = [(c, a) for c in CORN for a in c]
    LOC = {('o', p): i for i, p in enumerate(ONS)}
    LOC.update({('h', h): 24 + i for i, h in enumerate(HALF)})
    NQ = 48 * len(SITES)
    def qb(v, lab): return 48 * SID[v] + LOC[lab]

    def incident(q):
        v, c = q
        out = []
        for p in ONS:
            if c in p:
                other = p[1] if p[0] == c else p[0]
                out.append((('o', other), ('onsite', p), (v, other)))
        for a in c:
            b = [d for d in c if d != a][0]
            out.append((('l', a), ('link', (c, a)), (add(v, a), corner(neg(a), b))))
        return out
    def keyord(k): return (0, k[1]) if k[0] == 'o' else (1, k[1])
    def edge_qubits(q, ekind, edata):
        v, c = q
        if ekind == 'onsite':
            return [qb(v, ('o', edata))]
        cc, a = edata
        b = [d for d in cc if d != a][0]
        w = add(v, a); c2 = corner(neg(a), b)
        return [qb(v, ('h', (cc, a))), qb(w, ('h', (c2, neg(a))))]
    def edge_zqubit(q, ekind, edata):
        v, c = q
        if ekind == 'onsite':
            return qb(v, ('o', edata))
        return qb(v, ('h', edata))
    INC = {q: incident(q) for q in VERTS}
    def canon_first(q, r):
        if q[0] == r[0]:
            return CORN.index(q[1]) < CORN.index(r[1])
        for k, (ek, ed), nb in INC[q]:
            if nb == r and ek == 'link':
                return sum(ed[1]) > 0
        raise KeyError
    def A(q, r):
        if not canon_first(q, r):
            x, z, p = A(r, q); return (x, z, (p + 2) % 4)
        for k, (ek, ed), nb in INC[q]:
            if nb == r: break
        else:
            raise KeyError
        kq = k
        for k2, (ek2, ed2), nb2 in INC[r]:
            if nb2 == q: kr = k2; break
        zq = [edge_zqubit(q, e2k, e2d) for k2, (e2k, e2d), _ in INC[q] if keyord(k2) < keyord(kq)]
        zr = [edge_zqubit(r, e2k, e2d) for k2, (e2k, e2d), _ in INC[r] if keyord(k2) < keyord(kr)]
        return pmul(Xs(edge_qubits(q, ek, ed)), Zs(zq + zr))
    def Bop(q): return Zs([edge_zqubit(q, ek, ed) for _, (ek, ed), _ in INC[q]])
    def Rop(v, h):
        c, a = h; b = [d for d in c if d != a][0]
        return Zs([qb(v, ('h', h)), qb(add(v, a), ('h', (corner(neg(a), b), neg(a))))])
    def cycles():
        out = []
        for v in SITES:
            for d in DIRS:
                a = [f for f in DIRS if perp(f, d) and f != neg(d)]
                a0 = a[0]; b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
                ring = [a0, b0, neg(a0), neg(b0)]
                out.append(('square', [(v, corner(d, r)) for r in ring]))
                for i in range(4):
                    p, q = ring[i], ring[(i + 1) % 4]; w = add(v, d)
                    out.append(('tube', [(v, corner(d, p)), (w, corner(neg(d), p)), (w, corner(neg(d), q)), (v, corner(d, q))]))
            for s in itertools.product((1, -1), repeat=3):
                x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
                out.append(('triangle', [(v, corner(x, y)), (v, corner(y, z)), (v, corner(z, x))]))
            for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
                out.append(('plaquette', [(v, corner(d, e)), (add(v, d), corner(neg(d), e)),
                                          (add(add(v, d), e), corner(neg(d), neg(e))), (add(v, e), corner(d, neg(e)))]))
        return out
    def loop_op(seq, F):
        n = len(seq); P = (0, 0, n % 4)
        for i in range(n):
            P = pmul(P, A(seq[i], seq[(i + 1) % n]))
        if F: P = (P[0], P[1], (P[2] + 2) % 4)
        return P
    gens = [Bop(q) for q in VERTS] + [Rop(v, h) for v in SITES for h in HALF if (h[1][0] + h[1][1] + h[1][2]) > 0]
    CYC = cycles()
    loops = [loop_op(seq, FLUX[kind]) for kind, seq in CYC]
    gens = gens + loops
    qsite = [SITES[i // 48] for i in range(NQ)]
    meta = dict(A=A, B=Bop, INC=INC, VERTS=VERTS, CYC=CYC, kind='corner', qb=qb, HALF=HALF, add=add, corner=corner, neg=neg)
    return Code(f'F5 corner flux={FLUX}', L, NQ, gens, qsite, meta)
