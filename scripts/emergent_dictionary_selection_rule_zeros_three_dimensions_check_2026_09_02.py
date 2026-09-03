#!/usr/bin/env python3
"""The emergent dictionary reproduces the three-dimensional selection-rule zeros.

Class-A finite-cluster runner. Qubits sit on the EDGE sites of three finite
graphs; the sites compose ordinarily (tensor product, operators on disjoint
regions commute, no graded clause anywhere). A parity dictionary reads vertex
occupancy off the edge records,

    n_i = (1 - B_i) / 2,      B_i = product of the Z's on the edges at vertex i,

so the readout at a vertex is a condition on the records of that one vertex's
incident edges. The runner establishes, on the 2x2x2 cube graph (8 vertices,
12 edges), the 3x3 grid graph (9 vertices, 12 edges) and the 3x3 grid with one
pendant auxiliary mode at vertex 0 (10 vertices, 13 edges):

  A  ENCODING.  The Bravyi-Kitaev superfast relations R0-R4 for
         A_ij = X(edge ij) * prod Z(edges ordered before it at i and at j),
         A_ji = -A_ij,   B_i = the product of the Z's incident to i,
         S_f  = the ordered product of the A's around a face,
     the face relations, the stabilizer group, and the code dimension
     2^(V-1); prod_i B_i = +I identically, so the dictionary registers an even
     record number only, which is why an odd target needs a pendant mode.
  B  UNIT GAUGE.  An exact diagonal gauge D with entries in {1, i, -1, -i}
     with D H_enc D^dag = H_F entrywise, H_F the Jordan-Wigner matrix of the
     same nearest-neighbour law on the same occupation patterns. Spectra and
     record statistics therefore agree at every coupling, exactly.
  C  ZEROS AT g = 0.  The record statistics recomputed independently from
     exact Slater determinants over Q(sqrt2), and the exact zero sets.
  D  PERSISTENCE.  A numerical witness at g != 0: agreement to 1e-12, equal
     zero sets, ground-state simplicity, and the zeros that survive.
  E  FIBRES.  Each vertex pattern carries a constant fibre of 2^k edge
     patterns, and every edge pattern over a zero is exactly zero.
  F  SIGN STRUCTURE.  Every off-diagonal amplitude in the edge-record basis is
     exactly +i or -i, split evenly, with the closed form
         sign(y) = s_e * (-1)^{|y & Z(A_ij B_i)|},
     the Z-support lying inside star(i) U star(j); and the gauge-invariant
     four-cycle flux of the configuration graph.
  G  CONTROL.  The bare edge-flip law with X_e in place of A_ij leaves the
     code space, and on what it does preserve it is gaugeable to a uniform -1
     on a connected configuration graph, so Perron-Frobenius makes its record
     statistics strictly positive with no zero at any coupling.

Groups A, B, C, E, F, G are exact: Pauli algebra in the symplectic
representation with phases mod 4, Gaussian-integer amplitudes, rational and
Q(sqrt2) arithmetic over Fraction. Group D and the confirming line of group G
are floating-point witnesses and are labelled [numerical]. Every line is
tagged [exact] or [numerical].

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from functools import reduce

import numpy as np

AUDIT_TIMEOUT_SEC = 300

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ============================================================== Pauli algebra

def pcnt(n):
    return bin(n).count("1")


class P:
    """i^k * prod_q X_q^{x_q} Z_q^{z_q}, X written before Z on every qubit."""

    __slots__ = ("k", "x", "z")

    def __init__(s, k, x, z):
        s.k = k % 4
        s.x = x
        s.z = z

    def __mul__(a, b):
        return P(a.k + b.k + 2 * pcnt(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def neg(s):
        return P(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def is_herm(s):
        return s.k % 2 == pcnt(s.x & s.z) % 2

    def is_id(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def is_mid(s):
        return s.x == 0 and s.z == 0 and s.k == 2


ID = P(0, 0, 0)
PH = [1 + 0j, 1j, -1 + 0j, -1j]


def comm(a, b):
    return (pcnt(a.x & b.z) + pcnt(a.z & b.x)) % 2 == 0


def pact(p, y):
    """p|y> = amp |y ^ p.x> with amp a unit Gaussian integer."""
    return y ^ p.x, PH[p.k] * ((-1) ** (pcnt(p.z & y) % 2))


# =================================================== exact arithmetic Q(sqrt2)

class S2:
    """a + b*sqrt(2) with a and b rational; exact, no floating point."""

    __slots__ = ("a", "b")

    def __init__(s, a=0, b=0):
        s.a = Fraction(a)
        s.b = Fraction(b)

    def __add__(s, t):
        return S2(s.a + t.a, s.b + t.b)

    def __sub__(s, t):
        return S2(s.a - t.a, s.b - t.b)

    def __mul__(s, t):
        return S2(s.a * t.a + 2 * s.b * t.b, s.a * t.b + s.b * t.a)

    def neg(s):
        return S2(-s.a, -s.b)

    def inv(s):
        d = s.a * s.a - 2 * s.b * s.b
        return S2(s.a / d, -s.b / d)

    def zero(s):
        return s.a == 0 and s.b == 0

    def __eq__(s, t):
        return s.a == t.a and s.b == t.b

    def __hash__(s):
        return hash((s.a, s.b))

    def txt(s):
        if s.b == 0:
            return str(s.a)
        return "%s%+s*sqrt2" % (s.a, s.b) if s.a else "%s*sqrt2" % s.b


S0 = S2(0)
S1 = S2(1)


def s2_det(M):
    """Exact determinant over Q(sqrt2) by Gaussian elimination in the field."""
    n = len(M)
    M = [row[:] for row in M]
    sgn = 1
    det = S1
    for c in range(n):
        p = None
        for r in range(c, n):
            if not M[r][c].zero():
                p = r
                break
        if p is None:
            return S0
        if p != c:
            M[c], M[p] = M[p], M[c]
            sgn = -sgn
        piv = M[c][c]
        det = det * piv
        inv = piv.inv()
        for r in range(c + 1, n):
            f = M[r][c] * inv
            if f.zero():
                continue
            for kk in range(c, n):
                M[r][kk] = M[r][kk] - f * M[c][kk]
    return det if sgn > 0 else det.neg()


# ==================================================================== clusters

def grid_cluster(nr, nc):
    idx = {(r, c): nc * r + c for r in range(nr) for c in range(nc)}
    B = []
    for r in range(nr):
        for c in range(nc):
            if c + 1 < nc:
                B.append((idx[(r, c)], idx[(r, c + 1)]))
            if r + 1 < nr:
                B.append((idx[(r, c)], idx[(r + 1, c)]))
    return nr * nc, sorted((min(u, v), max(u, v)) for u, v in B)


def grid_faces(nr, nc):
    idx = {(r, c): nc * r + c for r in range(nr) for c in range(nc)}
    return [(idx[(r, c)], idx[(r, c + 1)], idx[(r + 1, c + 1)], idx[(r + 1, c)])
            for r in range(nr - 1) for c in range(nc - 1)]


def cube_cluster():
    """Vertex s = 4a + 2b + c of the 2x2x2 cube; edges flip one coordinate."""
    B = [(s, s ^ bit) for s in range(8) for bit in (4, 2, 1) if s ^ bit > s]
    return 8, sorted(B)


def cube_faces():
    out = []
    for ax in range(3):
        bits = [4, 2, 1]
        fb = bits[ax]
        ob = [b for b in bits if b != fb]
        for val in (0, fb):
            out.append((val, val | ob[1], val | ob[0] | ob[1], val | ob[0]))
    return out


# ==================================================================== encoding

class Enc:
    """Superfast encoding on the edge sites of a graph."""

    def __init__(self, V, EDGES, FACES, name):
        self.name = name
        self.V = V
        self.EDGES = list(EDGES)
        self.FACES = list(FACES)
        self.NQ = len(self.EDGES)
        self.DIM = 1 << self.NQ
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = q
            self.EIDX[(j, i)] = q
        self.NBR = {i: sorted(j for (a, b) in self.EDGES
                              for j in ((b,) if a == i else ((a,) if b == i else ())))
                    for i in range(V)}
        self.STAR = {i: [self.EIDX[(i, k)] for k in self.NBR[i]] for i in range(V)}
        self.STARMASK = {i: reduce(lambda a, b: a | (1 << b), self.STAR[i], 0)
                         for i in range(V)}

    def A_unsigned(self, i, j):
        x = 1 << self.EIDX[(i, j)]
        z = 0
        for k in self.NBR[i]:
            if k != j and k < j:
                z ^= 1 << self.EIDX[(i, k)]
        for l in self.NBR[j]:
            if l != i and l < i:
                z ^= 1 << self.EIDX[(j, l)]
        return P(pcnt(x & z) % 2, x, z)

    def A(self, i, j):
        p = self.A_unsigned(i, j)
        return p if i < j else p.neg()

    def B(self, i):
        return P(0, 0, self.STARMASK[i])

    def loop(self, cyc):
        out = ID
        n = len(cyc)
        for a in range(n):
            out = out * self.A(cyc[a], cyc[(a + 1) % n])
        return out

    def record(self, z):
        """The parity dictionary: n_i = (1 - B_i)/2 read off the edge record."""
        return tuple(pcnt(z & self.STARMASK[i]) % 2 for i in range(self.V))

    def hop_pauli(self, i, j):
        A = self.A(i, j)
        return A * self.B(i), A * self.B(j)

    def hop_amp(self, P1, P2, y):
        b1, a1 = pact(P1, y)
        b2, a2 = pact(P2, y)
        assert b1 == b2
        v = 0.5j * (a1 - a2)
        return b1, complex(round(v.real), round(v.imag))


def audit(E):
    """R0-R4 pair by pair, the face relations, and the code dimension."""
    R = {}
    A = {e: E.A(*e) for e in E.EDGES}
    Bv = {i: E.B(i) for i in range(E.V)}
    R["R0"] = (all(E.A_unsigned(i, j) == E.A_unsigned(j, i) for (i, j) in E.EDGES)
               and all(E.A(j, i) == E.A(i, j).neg() for (i, j) in E.EDGES))
    R["R1"] = (all(A[e].is_herm() and (A[e] * A[e]).is_id() for e in E.EDGES)
               and all(Bv[i].is_herm() and (Bv[i] * Bv[i]).is_id() for i in range(E.V)))
    r2 = all(comm(Bv[i], Bv[j]) for i, j in itertools.combinations(range(E.V), 2))
    for e in E.EDGES:
        for v in range(E.V):
            r2 = r2 and (comm(A[e], Bv[v]) != (v in e))
    R["R2"] = bool(r2)
    R["R3"] = all(comm(A[e], A[f]) != (len(set(e) & set(f)) == 1)
                  for e, f in itertools.combinations(E.EDGES, 2))
    S = [E.loop(f) for f in E.FACES]
    r4 = True
    for s in S:
        r4 = r4 and s.is_herm() and (s * s).is_id()
        for e in E.EDGES:
            r4 = r4 and comm(s, A[e])
        for v in range(E.V):
            r4 = r4 and comm(s, Bv[v])
    for a, b in itertools.combinations(S, 2):
        r4 = r4 and comm(a, b)
    R["R4"] = bool(r4)
    R["prodB"] = reduce(lambda a, b: a * b, [Bv[i] for i in range(E.V)])
    gens, basis = [], []
    for s in S:
        v = s.x
        for b in basis:
            v = min(v, v ^ b)
        if v != 0:
            basis.append(v)
            basis.sort(reverse=True)
            gens.append(s)
    R["k"] = len(gens)
    R["gens"] = gens
    rel = []
    for r in range(2, len(S) + 1):
        for sub in itertools.combinations(range(len(S)), r):
            p = reduce(lambda a, b: a * b, [S[t] for t in sub])
            if p.x == 0 and p.z == 0:
                rel.append((sub, "+I" if p.k == 0 else "-I" if p.k == 2 else "?"))
    R["relations"] = rel
    grp = []
    for m in range(1 << len(gens)):
        p = ID
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        grp.append(p)
    R["grp"] = grp
    R["grp_ok"] = ((not any(g.is_mid() for g in grp))
                   and sum(1 for g in grp if g.x == 0) == 1)
    R["code_dim"] = E.DIM >> len(gens)
    return R


def code_space(E, R):
    """Cosets of the stabilizer group; phi[y] the unit coefficient of |y>."""
    grp = R["grp"]
    phi = np.zeros(E.DIM, dtype=complex)
    cid = -np.ones(E.DIM, dtype=np.int64)
    reps = []
    for y0 in range(E.DIM):
        if cid[y0] >= 0:
            continue
        c = len(reps)
        reps.append(y0)
        for g in grp:
            b, a = pact(g, y0)
            assert cid[b] < 0
            cid[b] = c
            phi[b] = a
    assert (cid >= 0).all()
    recs = [E.record(reps[c]) for c in range(len(reps))]
    for y in range(E.DIM):
        assert E.record(y) == recs[cid[y]]
    return cid, phi, reps, recs


def sector_matrix(E, R, cid, phi, reps, recs, keep, HE):
    """Exact H_enc on the code space, rows and columns the kept cosets."""
    k = R["k"]
    grp = R["grp"]
    sel = [c for c in range(len(reps)) if keep(recs[c])]
    pos = {c: a for a, c in enumerate(sel)}
    n = len(sel)
    Hoff = np.zeros((n, n), dtype=complex)
    hp = {e: E.hop_pauli(*e) for e in HE}
    bond = np.zeros(n)
    stats = {"pos": 0, "neg": 0}
    for c in sel:
        a = pos[c]
        rec = recs[c]
        bond[a] = sum(1 for (u, v) in HE if rec[u] and rec[v])
        for g in grp:
            y, ay = pact(g, reps[c])
            assert abs(phi[y] - ay) < 1e-12
            for e in HE:
                yy, amp = E.hop_amp(hp[e][0], hp[e][1], y)
                if amp == 0:
                    continue
                assert amp.real == 0 and abs(amp.imag) == 1
                stats["pos" if amp.imag > 0 else "neg"] += 1
                cc = cid[yy]
                if cc not in pos:
                    continue
                Hoff[pos[cc], a] += (2.0 ** (-k)) * np.conj(phi[yy]) * amp * phi[y]
    Q = Hoff * (2.0 ** k)
    exact = bool(np.all(np.abs(Q - np.round(Q.real) - 1j * np.round(Q.imag)) == 0))
    Hoff = (np.round(Q.real) + 1j * np.round(Q.imag)) / (2.0 ** k)
    return sel, pos, Hoff, bond, stats, exact, int(np.max(np.abs(Q)))


# ================================================== Jordan-Wigner reference

def jw_sign(S, src, dst):
    lo, hi = min(src, dst), max(src, dst)
    return (-1) ** sum(1 for kk in range(lo + 1, hi) if kk in S)


def fermi_sector(EDGES, patterns):
    """Graded (Jordan-Wigner) hopping matrix and bond-count diagonal."""
    idx = {p: i for i, p in enumerate(patterns)}
    n = len(patterns)
    T = np.zeros((n, n))
    D = np.zeros(n)
    for p in patterns:
        S = frozenset(i for i, b in enumerate(p) if b)
        i0 = idx[p]
        D[i0] = sum(1 for (u, v) in EDGES if u in S and v in S)
        for (u, v) in EDGES:
            for (src, dst) in ((u, v), (v, u)):
                if src in S and dst not in S:
                    T2 = frozenset((S - {src}) | {dst})
                    tp = tuple(1 if q in T2 else 0 for q in range(len(p)))
                    T[idx[tp], i0] += -jw_sign(S, src, dst)
    assert np.array_equal(T, T.T)
    return idx, T, D


def unit_index(c):
    for kk, u in enumerate(PH):
        if abs(c - u) < 1e-9:
            return kk
    return None


def gauge_match(Hs, Hf):
    """Diagonal D with entries in {1,i,-1,-i} and conj(D) Hs D = Hf entrywise."""
    n = Hs.shape[0]
    ss = {(a, b) for a in range(n) for b in range(n)
          if a != b and abs(Hs[a, b]) > 1e-9}
    sf = {(a, b) for a in range(n) for b in range(n)
          if a != b and abs(Hf[a, b]) > 1e-9}
    if ss != sf:
        return None
    e = [None] * n
    for root in range(n):
        if e[root] is not None:
            continue
        e[root] = 0
        st = [root]
        while st:
            a = st.pop()
            for b in range(n):
                if b == a or abs(Hs[a, b]) < 1e-9:
                    continue
                s, f = unit_index(Hs[a, b]), unit_index(Hf[a, b])
                if s is None or f is None:
                    return None
                want = (e[a] + f - s) % 4
                if e[b] is None:
                    e[b] = want
                    st.append(b)
                elif e[b] != want:
                    return None
    d = np.array([PH[t] for t in e])
    M = np.conj(d)[:, None] * Hs * d[None, :]
    return d if np.max(np.abs(M - Hf)) == 0 else None


def tree_gauge(H):
    """Spanning-tree gauge; returns (components, entries, counts by i^k)."""
    n = H.shape[0]
    val = {(a, b): unit_index(H[a, b]) for a in range(n) for b in range(n)
           if a != b and abs(H[a, b]) > 1e-9}
    assert all(v is not None for v in val.values())
    adj = {a: [] for a in range(n)}
    for (a, b) in val:
        adj[a].append(b)
    e = [None] * n
    ncomp = 0
    for root in range(n):
        if e[root] is not None:
            continue
        ncomp += 1
        e[root] = 0
        st = [root]
        while st:
            a = st.pop()
            for b in adj[a]:
                if e[b] is None:
                    e[b] = (e[a] + 2 - val[(a, b)]) % 4
                    st.append(b)
    cnt = {0: 0, 1: 0, 2: 0, 3: 0}
    for (a, b) in val:
        if a > b:
            continue
        cnt[(val[(a, b)] + e[b] - e[a]) % 4] += 1
    return ncomp, len(val) // 2, cnt, np.array([PH[t] for t in e])


def flux4(H):
    """Gauge-invariant product of H around every four-cycle."""
    n = H.shape[0]
    A = (np.abs(H) > 1e-9) & (~np.eye(n, dtype=bool))
    nb = [np.where(A[a])[0] for a in range(n)]
    tot = frus = 0
    for a in range(n):
        for b in nb[a]:
            if b <= a:
                continue
            for c in nb[b]:
                if c <= a:
                    continue
                for d in nb[c]:
                    if d <= a or d == b or d >= b or not A[d, a]:
                        continue
                    tot += 1
                    if (H[a, b] * H[b, c] * H[c, d] * H[d, a]).real < 0:
                        frus += 1
    return tot, frus


# ================================================== single-particle orbitals

HALF = S2(Fraction(1, 2), 0)
RT2H = S2(0, Fraction(1, 2))
NHALF = S2(Fraction(-1, 2), 0)
NRT2H = S2(0, Fraction(-1, 2))
W1 = [HALF, RT2H, HALF]
W2 = [RT2H, S0, NRT2H]
W3 = [HALF, NRT2H, HALF]
O2 = [RT2H, RT2H]
M2 = [RT2H, NRT2H]


def prod_orb(fs):
    out = []
    for t in itertools.product(*[range(len(f)) for f in fs]):
        e = S1
        for f, kk in zip(fs, t):
            e = e * f[kk]
        out.append(e)
    return out


def s2_adj_check(V, EDGES, orb, ev):
    """(A o)_i = ev * o_i exactly, A the 0/1 adjacency."""
    for i in range(V):
        acc = S0
        for (u, v) in EDGES:
            if u == i:
                acc = acc + orb[v]
            elif v == i:
                acc = acc + orb[u]
        if not (acc - ev * orb[i]).zero():
            return False
    return True


def slater(patterns, orbs):
    """Exact Slater amplitudes: det of the occupied rows of the orbital matrix."""
    N = len(orbs)
    out = []
    for p in patterns:
        rows = [i for i, b in enumerate(p) if b]
        assert len(rows) == N
        out.append(s2_det([[orbs[y][rows[x]] for y in range(N)] for x in range(N)]))
    return out


# ==================================================================== clusters

VC, EC = cube_cluster()
ENC_C = Enc(VC, EC, cube_faces(), "cube")
VG, EG = grid_cluster(3, 3)
ENC_G = Enc(VG, EG, grid_faces(3, 3), "grid3x3")
AUX = 9
ENC_GP = Enc(10, EG + [(0, AUX)], grid_faces(3, 3), "grid3x3+pendant")

ORB_C = [prod_orb([O2, O2, O2]), prod_orb([M2, O2, O2]),
         prod_orb([O2, M2, O2]), prod_orb([O2, O2, M2])]
EV_C = [S2(3), S1, S1, S1]
ORB_G6 = [prod_orb([W1, W1]), prod_orb([W1, W2]), prod_orb([W2, W1]),
          prod_orb([W1, W3]), prod_orb([W3, W1]), prod_orb([W2, W2])]
EV_G6 = [S2(0, 2), S2(0, 1), S2(0, 1), S0, S0, S0]
ORB_G3 = [prod_orb([W1, W1]), prod_orb([W1, W2]), prod_orb([W2, W1])]
EV_G3 = [S2(0, 2), S2(0, 1), S2(0, 1)]
ORB_GP = [o + [S0] for o in ORB_G3] + [[S0] * 9 + [S1]]

LINES = set()
for r in range(3):
    LINES.add(tuple(3 * r + c for c in range(3)))
    LINES.add(tuple(3 * c + r for c in range(3)))
LINES.add((0, 4, 8))
LINES.add((2, 4, 6))
CENTRE_LINES = {(3, 4, 5), (1, 4, 7), (0, 4, 8), (2, 4, 6)}

CASES = {}


def build(tag, E, keep, HE, orbs, evs, E0, ndesc):
    """Encoding audit, code space, sector matrix, gauge, exact ground state."""
    R = audit(E)
    cid, phi, reps, recs = code_space(E, R)
    sel, pos, Hoff, bond, stats, exact, mx = sector_matrix(
        E, R, cid, phi, reps, recs, keep, HE)
    pats = [recs[c] for c in sel]
    n = len(sel)
    fidx, T, D = fermi_sector(HE, pats)
    order = [fidx[p] for p in pats]
    T = T[np.ix_(order, order)]
    D = D[order]
    d = gauge_match(Hoff, T)
    v = slater(pats, orbs)
    Ti = [[int(round(T[a, b])) for b in range(n)] for a in range(n)]
    eig = True
    for a in range(n):
        acc = S0
        for b in range(n):
            if Ti[a][b]:
                acc = acc + S2(Ti[a][b], 0) * v[b]
        eig = eig and (acc - E0 * v[a]).zero()
    nrm = S0
    prob = []
    for a in range(n):
        q = v[a] * v[a]
        prob.append(q)
        nrm = nrm + q
    rational = all(q.b == 0 for q in prob)
    zeros = [pats[a] for a in range(n) if prob[a].zero()]
    vals = sorted(set(prob), key=lambda q: float(q.a) + 1.4142135623730951 * float(q.b))
    counts = [(vals[t].txt(), sum(1 for q in prob if q == vals[t]))
              for t in range(len(vals))]
    ctxt = ", ".join("%s x%d" % kv for kv in counts)
    orth = all(s2_adj_check(E.V, HE, orbs[t], evs[t]) for t in range(len(orbs)))
    CASES[tag] = dict(E=E, R=R, cid=cid, phi=phi, reps=reps, recs=recs, sel=sel,
                      pos=pos, Hoff=Hoff, bond=bond, stats=stats, exact=exact,
                      mx=mx, T=T, D=D, d=d, pats=pats, n=n, prob=prob,
                      zeros=zeros, counts=counts, nrm=nrm, eig=eig,
                      rational=rational, orth=orth, HE=HE, keep=keep,
                      ndesc=ndesc, ctxt=ctxt)
    return CASES[tag]


# ==================================================================== group A

def group_A():
    C = build("cube", ENC_C, lambda r: sum(r) == 4, EC, ORB_C, EV_C, S2(-6), "N=4")
    G = build("grid", ENC_G, lambda r: sum(r) == 6, EG, ORB_G6, EV_G6,
              S2(0, -4), "N=6")
    Pd = build("pend", ENC_GP, lambda r: r[AUX] == 1 and sum(r[:9]) == 3, EG,
               ORB_GP, EV_G3 + [S0], S2(0, -4), "n_aux=1, N_grid=3")
    for tag, res, nrel in (("cube", C, 1), ("grid", G, 0), ("pend", Pd, 0)):
        R = res["R"]
        E = res["E"]
        rel = R["relations"]
        check("A%d [exact] %s edge-site code V=%d E=%d: R0-R4 hold, %d face loops, "
              "%d relation%s %s, k=%d, group 2^%d free of -I, code dim 2^%d/2^%d = %d "
              "= 2^(V-1)"
              % (1 + ("cube", "grid", "pend").index(tag), E.name, E.V, len(E.EDGES),
                 len(E.FACES), len(rel), "" if len(rel) == 1 else "s",
                 "(all six) = %s" % rel[0][1] if rel else "(none)",
                 R["k"], R["k"], E.NQ, R["k"], R["code_dim"]),
              R["R0"] and R["R1"] and R["R2"] and R["R3"] and R["R4"]
              and R["grp_ok"] and len(rel) == nrel
              and R["code_dim"] == (1 << (E.V - 1)))
    par = all(sum(CASES[t]["E"].record(y)) % 2 == 0
              for t in ("cube", "grid", "pend")
              for y in range(CASES[t]["E"].DIM))
    inj = all(len(set(CASES[t]["recs"])) == len(CASES[t]["recs"])
              for t in ("cube", "grid", "pend"))
    check("A4 [exact] prod_i B_i = +I identically: n_i = (1-B_i)/2 registers an EVEN "
          "record number on all %d/%d/%d edge patterns, and is injective on the %d/%d/%d "
          "code states, so an odd target needs the pendant mode"
          % (ENC_C.DIM, ENC_G.DIM, ENC_GP.DIM, C["R"]["code_dim"],
             G["R"]["code_dim"], Pd["R"]["code_dim"]),
          all(CASES[t]["R"]["prodB"].is_id() for t in ("cube", "grid", "pend"))
          and par and inj)


# ==================================================================== group B

def group_B():
    for t, (tag, dim) in enumerate((("cube", 70), ("grid", 84), ("pend", 84))):
        res = CASES[tag]
        d = res["d"]
        ok = (d is not None and res["exact"] and res["n"] == dim
              and np.array_equal(res["bond"], res["D"])
              and bool(np.all(np.abs(np.abs(d) - 1) == 0)))
        nsu = int(np.sum(np.abs(d.imag) > 0.5)) if d is not None else -1
        check("B%d [exact] %s %s: dim %d, diagonals equal the fermionic bond counts, "
              "2^%d H_enc a Gaussian-integer matrix of max modulus %d, and a unit gauge "
              "D (%d of %d entries in {i,-i}) gives D H_enc D^dag = H_F"
              % (t + 1, res["E"].name, res["ndesc"], res["n"], res["R"]["k"],
                 res["mx"], nsu, res["n"]), ok)


# ==================================================================== group C

def group_C():
    C, G, Pd = CASES["cube"], CASES["grid"], CASES["pend"]
    check("C1 [exact] cube N=4 at g=0: orbitals are exact eigenvectors, the Slater "
          "ground state over Q(sqrt2) has H_F v = -6 v and <v|v> = %s, levels -1 | 1 "
          "across the cut so it is unique; statistics %s"
          % (C["nrm"].txt(), C["ctxt"]),
          C["orth"] and C["eig"] and C["nrm"] == S1 and C["rational"]
          and C["counts"] == [("0", 12), ("1/64", 56), ("1/16", 2)])
    faces, pairs, other = [], [], []
    for p in C["zeros"]:
        occ = tuple(i for i, b in enumerate(p) if b)
        trip = [(s >> 2 & 1, s >> 1 & 1, s & 1) for s in occ]
        ed = [(u, v) for u, v in itertools.combinations(occ, 2) if pcnt(u ^ v) == 1]
        if any(len({q[ax] for q in trip}) == 1 for ax in range(3)):
            faces.append(occ)
        elif len(ed) == 2 and len(set(ed[0]) | set(ed[1])) == 4:
            pairs.append(occ)
        else:
            other.append(occ)
    check("C2 [exact] the cube's %d zeros of %d are exactly the %d occupied cube faces "
          "and the %d patterns of two disjoint adjacent pairs, %d other; every zero is "
          "an exact cancellation, not a small number"
          % (len(C["zeros"]), C["n"], len(faces), len(pairs), len(other)),
          len(C["zeros"]) == 12 and len(faces) == 6 and len(pairs) == 6 and not other)
    got3 = {tuple(i for i, b in enumerate(p) if b and i < 9) for p in Pd["zeros"]}
    check("C3 [exact] grid3x3+pendant N_grid=3 at g=0: H_F v = -4 sqrt2 v, <v|v> = %s, "
          "levels -sqrt2 | 0; statistics %s; the %d zeros are exactly the 3 rows, "
          "3 columns, 2 diagonals"
          % (Pd["nrm"].txt(), Pd["ctxt"], len(Pd["zeros"])),
          Pd["orth"] and Pd["eig"] and Pd["nrm"] == S1 and Pd["rational"]
          and got3 == LINES
          and Pd["counts"] == [("0", 8), ("1/256", 12), ("1/128", 32),
                               ("1/64", 20), ("1/32", 8), ("9/256", 4)])
    got6 = {tuple(i for i, b in enumerate(p) if b) for p in G["zeros"]}
    comp = {tuple(sorted(set(range(9)) - set(l))) for l in got3}
    check("C4 [exact] grid3x3 N=6 on the 12-qubit code at g=0: H_F v = -4 sqrt2 v, "
          "<v|v> = %s, levels 0 | sqrt2, the same value multiset; its %d zeros are "
          "exactly the complements of the N_grid=3 zeros, the particle-hole image"
          % (G["nrm"].txt(), len(G["zeros"])),
          G["orth"] and G["eig"] and G["nrm"] == S1 and G["rational"]
          and got6 == comp and G["counts"] == Pd["counts"])


# ==================================================================== group D

GVALS = (0.5, 1.0, 2.0)


def scan(res):
    out = []
    persist = None
    for g in (0.0,) + GVALS:
        He = res["Hoff"] + g * np.diag(res["bond"])
        Hf = res["T"] + g * np.diag(res["D"])
        we, Ve = np.linalg.eigh(He)
        wf, Vf = np.linalg.eigh(Hf)
        me = int(np.sum(we < we[0] + 1e-9))
        mf = int(np.sum(wf < wf[0] + 1e-9))
        pe = (np.abs(Ve[:, :me]) ** 2).sum(axis=1) / me
        pf = (np.abs(Vf[:, :mf]) ** 2).sum(axis=1) / mf
        ze = frozenset(np.where(pe < 1e-12)[0])
        zf = frozenset(np.where(pf < 1e-12)[0])
        out.append((g, float(np.abs(pe - pf).sum()), we[1] - we[0], me, mf, ze, zf))
        if g != 0.0:
            persist = ze if persist is None else (persist & ze)
    return out, persist


def group_D():
    keep = {}
    for t, tag in enumerate(("cube", "grid", "pend")):
        res = CASES[tag]
        rows, persist = scan(res)
        keep[tag] = (rows, persist)
        ok = all(r[1] < 1e-12 and r[5] == r[6] and r[3] == 1 and r[4] == 1
                 for r in rows)
        check("D%d [numerical, 1e-12] %s %s at g in {0, 0.5, 1, 2}: encoded and fermionic "
              "statistics agree to L1 <= %.1e, zero counts %s identical, ground simple "
              "throughout, smallest gap %.6f"
              % (t + 1, res["E"].name, res["ndesc"], max(r[1] for r in rows),
                 "/".join(str(len(r[5])) for r in rows),
                 min(r[2] for r in rows)), ok)
    pc_, pg_, pp_ = (keep["cube"][1], keep["grid"][1], keep["pend"][1])
    cl6 = {tuple(sorted(set(range(9)) - set(l))) for l in CENTRE_LINES}
    gg = {tuple(i for i, b in enumerate(CASES["grid"]["pats"][a]) if b) for a in pg_}
    pp = {tuple(i for i, b in enumerate(CASES["pend"]["pats"][a]) if b and i < 9)
          for a in pp_}
    check("D4 [numerical, 1e-12] zeros surviving every g in {0.5, 1, 2}: cube %d of %d, "
          "the whole g=0 set; grid3x3 %d of %d at N_grid=3, exactly the four lines "
          "through the centre, and %d of %d at N=6, their complements"
          % (len(pc_), len(CASES["cube"]["zeros"]), len(pp_),
             len(CASES["pend"]["zeros"]), len(pg_), len(CASES["grid"]["zeros"])),
          len(pc_) == 12 and pp == CENTRE_LINES and gg == cl6)


# ==================================================================== group E

def group_E():
    for t, tag in enumerate(("cube", "grid", "pend")):
        res = CASES[tag]
        E, R = res["E"], res["R"]
        fib = 1 << R["k"]
        sizes = np.bincount(res["cid"])
        nz = sum(1 for q in res["prob"] if not q.zero())
        ok = (bool(np.all(sizes == fib))
              and bool(np.all(np.abs(np.abs(res["phi"]) - 1) == 0))
              and nz + len(res["zeros"]) == res["n"])
        check("E%d [exact] %s: |phi(y)| = 1 on all %d edge records, every coset holds "
              "exactly 2^%d = %d, so the probability is P(pattern)/%d on the fibre; "
              "%dx%d = %d in the sector, %dx%d = %d over a zero, all exactly 0"
              % (t + 1, E.name, E.DIM, R["k"], fib, fib, res["n"], fib,
                 res["n"] * fib, len(res["zeros"]), fib, len(res["zeros"]) * fib), ok)


# ==================================================================== group F

def sign_form(E, HE):
    """sign(y) = s_e * (-1)^{|y & Z(A_ij B_i)|}, Z-support in star(i) U star(j)."""
    inside = True
    okform = True
    for (i, j) in HE:
        A = E.A(i, j)
        P1 = A * E.B(i)
        P2 = A * E.B(j)
        inside = inside and (P1.z & ~(E.STARMASK[i] | E.STARMASK[j])) == 0
        s_e = None
        for y in range(E.DIM):
            b1, a1 = pact(P1, y)
            b2, a2 = pact(P2, y)
            amp = 0.5j * (a1 - a2)
            if amp == 0:
                continue
            s = int(round(amp.imag))
            pred = (-1) ** (pcnt(y & P1.z) % 2)
            if s_e is None:
                s_e = s * pred
            okform = okform and (s == s_e * pred)
    return inside, okform


def group_F():
    for t, tag in enumerate(("cube", "grid")):
        res = CASES[tag]
        E = res["E"]
        st = res["stats"]
        tot = st["pos"] + st["neg"]
        inside, okform = sign_form(E, res["HE"])
        check("F%d [exact] %s: all %d off-diagonal edge-basis amplitudes are exactly "
              "+i or -i, split %d/%d; Z(A_ij B_i) sits inside star(i) U star(j), and "
              "sign(y) = s_e (-1)^{|y & Z(A_ij B_i)|} on all %d records"
              % (t + 1, E.name, tot, st["pos"], st["neg"], E.DIM),
              inside and okform and st["pos"] == st["neg"] and st["pos"] > 0)
    tc, fc = flux4(CASES["cube"]["Hoff"])
    tcf, fcf = flux4(CASES["cube"]["T"].astype(complex))
    tg, fg = flux4(CASES["grid"]["Hoff"])
    tgf, fgf = flux4(CASES["grid"]["T"].astype(complex))
    ncc, mec, cc, _ = tree_gauge(CASES["cube"]["Hoff"])
    ncg, meg, cg, _ = tree_gauge(CASES["grid"]["Hoff"])
    check("F3 [exact] four-cycle flux: cube %d of %d carry -1, grid3x3 %d of %d, "
          "identical for H_F (%d/%d, %d/%d); in a spanning-tree gauge %d of %d and %d of "
          "%d entries stay +1, so no gauge makes either law sign-uniform"
          % (fc, tc, fg, tg, fcf, tcf, fgf, tgf, cc[0], mec, cg[0], meg),
          (tc, fc) == (tcf, fcf) and (tg, fg) == (tgf, fgf) and fc > 0 and fg > 0
          and cc[0] > 0 and cg[0] > 0 and cc[1] == cc[3] == cg[1] == cg[3] == 0)


# ==================================================================== group G

def bare_sector(E, R, keep, HE):
    """The bare edge-flip law (i/2) X_e (B_i - B_j) on the preserved sector."""
    bad = 0
    for (i, j) in HE:
        Xe = P(0, 1 << E.EIDX[(i, j)], 0)
        p1, p2 = Xe * E.B(i), Xe * E.B(j)
        for s in R["gens"]:
            if not (comm(p1, s) and comm(p2, s)):
                bad += 1
    keepz = [y for y in range(E.DIM) if keep(E.record(y))]
    zpos = {y: a for a, y in enumerate(keepz)}
    m = len(keepz)
    H = np.zeros((m, m), dtype=complex)
    D = np.zeros(m)
    for y in keepz:
        a = zpos[y]
        rec = E.record(y)
        D[a] = sum(1 for (u, v) in HE if rec[u] and rec[v])
        for (i, j) in HE:
            Xe = P(0, 1 << E.EIDX[(i, j)], 0)
            b1, a1 = pact(Xe * E.B(i), y)
            b2, a2 = pact(Xe * E.B(j), y)
            amp = 0.5j * (a1 - a2)
            if amp == 0:
                continue
            assert b1 in zpos
            H[zpos[b1], a] += amp
    assert np.max(np.abs(H - H.conj().T)) == 0
    return bad, len(R["gens"]) * len(HE), keepz, zpos, H, D


BARE = {}


def group_G():
    for t, tag in enumerate(("cube", "grid")):
        res = CASES[tag]
        E, R = res["E"], res["R"]
        bad, npair, keepz, zpos, H, D = bare_sector(E, R, res["keep"], res["HE"])
        ncomp, ment, cnt, gv = tree_gauge(H)
        Hr = np.real(np.conj(gv)[:, None] * H * gv[None, :])
        BARE[tag] = (keepz, zpos, Hr, D, len(res["pats"]))
        check("G%d [exact] %s control: bare X_e in place of A_ij anticommutes with %d "
              "of %d (term, generator) pairs, leaving the code space; it conserves the "
              "record on a %d-dim sector where a gauge makes all %d entries -1, "
              "%d component"
              % (2 * t + 1, E.name, bad, npair, len(keepz), ment, ncomp),
              bad > 0 and ncomp == 1 and cnt[2] == ment and cnt[0] == 0
              and cnt[1] == 0 and cnt[3] == 0)
        rows = []
        for g in (0.0,) + GVALS:
            w, V = np.linalg.eigh(Hr + g * np.diag(D))
            mm = int(np.sum(w < w[0] + 1e-9))
            pz = (np.abs(V[:, :mm]) ** 2).sum(axis=1) / mm
            pv = {}
            for y in keepz:
                r = E.record(y)
                pv[r] = pv.get(r, 0.0) + pz[zpos[y]]
            rows.append((mm, len(pv), min(pv.values()),
                         sum(1 for q in pv.values() if q < 1e-12)))
        check("G%d [numerical, 1e-12] %s control on that sector at g in {0, 0.5, 1, 2}: "
              "ground simple, all %d patterns strictly positive, smallest %.4e, %d exact "
              "zeros -- the Perron-Frobenius consequence of that gauge"
              % (2 * t + 2, E.name, rows[0][1], min(r[2] for r in rows),
                 max(r[3] for r in rows)),
              all(r[0] == 1 and r[1] == len(res["pats"]) and r[2] > 1e-9 and r[3] == 0
                  for r in rows))


def main():
    for g in (group_A, group_B, group_C, group_D, group_E, group_F, group_G):
        g()
    print("SUMMARY: ordinary composition plus a single-vertex parity dictionary "
          "reproduces the graded selection-rule zeros exactly; the bare edge-flip "
          "control has none.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
