#!/usr/bin/env python3
"""Record formation on the emergent vacuum: parity-forced odds.

Class-A finite-cluster runner, self-contained. Qubits sit on the EDGE sites
of three finite open graphs; the sites compose ordinarily (tensor product,
operators on disjoint regions commute, no graded clause anywhere). A record
at an edge site registers a Z-value there, and the vertex-level parity
dictionary reads occupancy off those records,

    n_v = (1 - B_v) / 2,     B_v = product of the Z's on the edges at v,

so the condition at a vertex concerns the records of that one vertex's
incident edges. The update rule used throughout is Lueders conditioning on
the record's value; it is STIPULATED here, not derived, and is applied to
the state the encoding supplies. The runner establishes, on the 2x2x2 cube
graph (8 vertices, 12 edge sites), the 3x3 grid graph (9, 12) and the 3x3
grid with one pendant site at vertex 0 (10, 13):

  A  ENCODING AND VACUUM.  The Bravyi-Kitaev superfast relations R0-R4 for
         A_ij = X(edge ij) * prod Z(edges ordered before it at i and at j),
         A_ji = -A_ij,   B_v = the product of the Z's incident to v,
         S_f  = the ordered product of the A's around a face,
     the face relations, the code dimension 2^(V-1), and the emergent
     vacuum as the unique code state carrying B_v = +1 at every vertex.
  B  THE ALLOWED SET.  The vacuum's record-pattern distribution is uniform
     on a LINEAR subspace of F2^E of dimension E - V + 1, cut out by the
     single-vertex parity conditions alone; the Z-type subgroup of
     <S_f, B_v> has rank V - 1, carries sign +1 throughout, and equals
     <B_v>, so no longer-than-one-vertex Z-type condition is present.
  C  ODDS.  The odds at every site before any record are 1/2; after records
     form they are 1/2 or forced to 0 or 1, never between; and a record
     elsewhere changes them exactly when the records around one vertex
     close a parity.
  D  FORCING.  Forcing is the cocircuit structure of the graph: the minimal
     forcing record sets are the minimal cocircuits through the site, each
     deterministic and inclusion-minimal, checked exhaustively to size 3.
  E  ORDER INDEPENDENCE.  The finished set of records carries the same odds
     whatever order the records formed in, on stabilizer and on
     non-stabilizer states, because all Z_e commute.
  F  A FERMION PAIR.  B_v = -1 at two vertices gives a genuine coset of the
     vacuum's subspace, with n_v = 1 on every allowed pattern and the same
     cocircuit forcing at different forced values.
  G  COHERENCE.  Coherent superposition inside one record-number sector
     adds cancellation zeros beyond the allowed set; superposition across
     sectors adds none; and the zeros belong to the state, not to the
     energy manifold.

Groups A-F and the rational half of G are exact: Pauli algebra in the
symplectic representation with phases mod 4, F2 linear algebra, Gaussian
integers and `Fraction`. Two lines are floating-point witnesses at 1e-12 and
are labelled [numerical]. Every line is tagged [exact] or [numerical].

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from functools import reduce

import numpy as np

AUDIT_TIMEOUT_SEC = 120

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


# ============================================================== F2 linear algebra

def f2_rank(vs):
    """Rank and a reduced basis of a set of F2 vectors held as ints."""
    b = []
    for v in vs:
        for x in b:
            v = min(v, v ^ x)
        if v:
            b.append(v)
            b.sort(reverse=True)
    return len(b), b


def f2_span(basis):
    S = {0}
    for b in basis:
        S |= {s ^ b for s in S}
    return S


def f2_kernel(cols):
    """Kernel of e_j |-> cols[j] over F2, as tags (ints over j)."""
    piv = {}
    out = []
    for j in range(len(cols)):
        v, t = cols[j], 1 << j
        while v:
            h = v.bit_length() - 1
            if h in piv:
                pv, pt = piv[h]
                v ^= pv
                t ^= pt
            else:
                piv[h] = (v, t)
                t = 0
                break
        if v == 0 and t:
            out.append(t)
    return out


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
    """Superfast encoding on the edge sites of a finite open graph."""

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
        """The parity dictionary: n_v = (1 - B_v)/2 read off the edge record."""
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
    R["S_all"] = S
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
    for c in sel:
        a = pos[c]
        for g in grp:
            y, ay = pact(g, reps[c])
            assert abs(phi[y] - ay) < 1e-12
            for e in HE:
                yy, amp = E.hop_amp(hp[e][0], hp[e][1], y)
                if amp == 0:
                    continue
                assert amp.real == 0 and abs(amp.imag) == 1
                cc = cid[yy]
                if cc not in pos:
                    continue
                Hoff[pos[cc], a] += (2.0 ** (-k)) * np.conj(phi[yy]) * amp * phi[y]
    Q = Hoff * (2.0 ** k)
    exact = bool(np.all(np.abs(Q - np.round(Q.real) - 1j * np.round(Q.imag)) == 0))
    Hoff = (np.round(Q.real) + 1j * np.round(Q.imag)) / (2.0 ** k)
    return sel, pos, Hoff, exact


# ================================================== Jordan-Wigner reference

def jw_sign(S, src, dst):
    lo, hi = min(src, dst), max(src, dst)
    return (-1) ** sum(1 for kk in range(lo + 1, hi) if kk in S)


def fermi_sector(EDGES, patterns):
    """Graded (Jordan-Wigner) hopping matrix on the same occupation patterns."""
    idx = {p: i for i, p in enumerate(patterns)}
    n = len(patterns)
    T = np.zeros((n, n))
    for p in patterns:
        S = frozenset(i for i, b in enumerate(p) if b)
        i0 = idx[p]
        for (u, v) in EDGES:
            for (src, dst) in ((u, v), (v, u)):
                if src in S and dst not in S:
                    T2 = frozenset((S - {src}) | {dst})
                    tp = tuple(1 if q in T2 else 0 for q in range(len(p)))
                    T[idx[tp], i0] += -jw_sign(S, src, dst)
    assert np.array_equal(T, T.T)
    return idx, T


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


# ================================================== clusters, vacuum, odds

NAMES = ("cube", "grid3x3", "grid3x3+pendant")


def make(nm):
    if nm == "cube":
        V, E = cube_cluster()
        F = cube_faces()
    elif nm == "grid3x3":
        V, E = grid_cluster(3, 3)
        F = grid_faces(3, 3)
    else:
        V, E = grid_cluster(3, 3)
        F = grid_faces(3, 3)
        E = list(E) + [(0, 9)]
        V = 10
    return Enc(V, sorted(E), F, nm)


CL = {}
ALLOW = {}
for _nm in NAMES:
    _En = make(_nm)
    _R = audit(_En)
    _cid, _phi, _reps, _recs = code_space(_En, _R)
    CL[_nm] = (_En, _R, _cid, _phi, _reps, _recs)
    _c0 = [c for c in range(len(_reps)) if all(x == 0 for x in _recs[c])]
    ALLOW[_nm] = (_c0, [z for z in range(_En.DIM) if _cid[z] == _c0[0]])

BITS = {nm: [((np.arange(CL[nm][0].DIM) >> q) & 1) for q in range(CL[nm][0].NQ)]
        for nm in NAMES}


def odds(S, q):
    """The odds that a record forming at site q locks the value 1."""
    return Fraction(sum(1 for z in S if (z >> q) & 1), len(S))


def cond(S, q, b):
    """Lueders conditioning of the allowed set on a record of value b at q."""
    return [z for z in S if ((z >> q) & 1) == b]


def cocircuits(S, nq):
    """Cut space of the allowed set and its minimal (inclusion-minimal) cocircuits."""
    base = S[0]
    dim, basis = f2_rank([z ^ base for z in S])
    dual = [w for w in range(1 << nq) if all(pcnt(w & b) % 2 == 0 for b in basis)]
    assert len(dual) == 1 << (nq - dim)
    nz = [w for w in dual if w]
    cc = [w for w in nz if not any(v and v != w and (v & w) == v for v in nz)]
    return dim, dual, cc


def forcing_sets(cc, q):
    """The inclusion-minimal record sets that force site q."""
    sets = [w & ~(1 << q) for w in cc if (w >> q) & 1]
    sets = [s for s in sets if not any(t != s and (t & s) == t for t in sets)]
    return sorted(set(sets), key=lambda s: (pcnt(s), s))


def lueders(v, bit, b):
    w = np.where(bit == b, v, 0)
    n2 = float(np.vdot(w, w).real)
    return (None if n2 < 1e-24 else w / np.sqrt(n2)), n2


def coset_state(nm, amps):
    """Unit vector with the given complex amplitude on each named coset."""
    En, R, cid, phi, reps, recs = CL[nm]
    v = np.zeros(En.DIM, dtype=complex)
    for c, a in amps.items():
        sel = cid == c
        v[sel] = a * phi[sel]
    return v / np.sqrt(float(np.vdot(v, v).real))


def pair_ordered(nm, v):
    """Ordered-pair order-independence census on one state."""
    En = CL[nm][0]
    bits = BITS[nm]
    bad = npair = 0
    for q1, q2 in itertools.combinations(range(En.NQ), 2):
        for b1 in (0, 1):
            for b2 in (0, 1):
                npair += 1
                a = lueders(v, bits[q1], b1)[0]
                a = None if a is None else lueders(a, bits[q2], b2)[0]
                c = lueders(v, bits[q2], b2)[0]
                c = None if c is None else lueders(c, bits[q1], b1)[0]
                if (a is None) != (c is None):
                    bad += 1
                elif a is not None and np.max(np.abs(a - c)) > 1e-12:
                    bad += 1
    return npair, bad


# =============================================== the cube's two-particle states

def chi(s, u):
    return -1 if pcnt(s & u) % 2 else 1


def cube_two_particle():
    """The N = 2 sector of the cube, its gauge, and two E = -4 states."""
    nm = "cube"
    En, R, cid, phi, reps, recs = CL[nm]
    sel, pos, Hoff, exact = sector_matrix(
        En, R, cid, phi, reps, recs, lambda r: sum(r) == 2, En.EDGES)
    pats = [recs[c] for c in sel]
    idx, T = fermi_sector(En.EDGES, pats)
    assert all(idx[p] == pos[sel[a]] for a, p in enumerate(pats))
    d = gauge_match(Hoff, T)
    Ti = np.round(T).astype(np.int64)
    assert np.allclose(Ti, T)

    def slater(s, t):
        w = np.zeros(len(pats), dtype=np.int64)
        for a, p in enumerate(pats):
            u, x = [i for i, b in enumerate(p) if b]
            w[a] = chi(s, u) * chi(t, x) - chi(s, x) * chi(t, u)
        return w

    return sel, pos, pats, Hoff, Ti, d, exact, slater


def state_from_weights(sel, pos, d, w, k):
    """Unit vector and exact per-pattern probabilities of an encoded state."""
    En, R, cid, phi, reps, recs = CL["cube"]
    n2 = int(w @ w)
    amps = {sel[a]: complex(w[a]) * np.conj(d[a]) for a in range(len(sel)) if w[a]}
    v = coset_state("cube", amps)
    ex = {}
    for z in range(En.DIM):
        c = cid[z]
        ex[z] = (Fraction(int(w[pos[c]]) ** 2, n2 * (1 << k))
                 if c in pos else Fraction(0))
    assert max(abs(abs(v[z]) ** 2 - float(ex[z])) for z in range(En.DIM)) < 1e-12
    return v, ex


# ===================================================================== group A

def group_A():
    for t, nm in enumerate(NAMES):
        En, R, cid, phi, reps, recs = CL[nm]
        rel = R["relations"]
        allsix = len(rel) == 1 and rel[0][0] == tuple(range(len(R["S_all"])))
        check("A%d [exact] %s V=%d E=%d edge sites: R0-R4 pair by pair, %d face loops, %d "
              "relation%s, k=%d, no -I in the group 2^%d, code dim 2^%d/2^%d = %d = 2^(V-1)"
              % (t + 1, nm, En.V, En.NQ, len(En.FACES), len(rel),
                 " (the product of all six) = +I" if rel else "s (none)",
                 R["k"], R["k"], En.NQ, R["k"], R["code_dim"]),
              all(R[q] for q in ("R0", "R1", "R2", "R3", "R4")) and R["grp_ok"]
              and R["code_dim"] == 1 << (En.V - 1)
              and (allsix and rel[0][1] == "+I" if nm == "cube" else not rel))
    ok = True
    sizes = []
    for nm in NAMES:
        En, R = CL[nm][0], CL[nm][1]
        c0, S = ALLOW[nm]
        sizes.append(len(S))
        ok = ok and len(c0) == 1 and len(S) == 1 << R["k"]
        ok = ok and all(all(pcnt(z & En.STARMASK[v]) % 2 == 0 for v in range(En.V))
                        for z in S)
        ok = ok and sum(1 for c in range(len(CL[nm][4]))
                        if all(x == 0 for x in CL[nm][5][c])) == 1
    check("A4 [exact] the emergent vacuum is on each cluster the UNIQUE code state with B_v = +1 "
          "at every vertex: one coset of %d, %d and %d records, registering no record number"
          % tuple(sizes), ok)


# ===================================================================== group B

def group_B():
    for t, nm in enumerate(NAMES):
        En, R = CL[nm][0], CL[nm][1]
        c0, S = ALLOW[nm]
        Sset = set(S)
        lin = 0 in Sset and all((a ^ b) in Sset for a in S for b in S)
        dim = f2_rank(S)[0]
        pred = [z for z in range(En.DIM)
                if all(pcnt(z & En.STARMASK[v]) % 2 == 0 for v in range(En.V))]
        p = Fraction(1, len(S))
        check("B%d [exact] %s vacuum: allowed set uniform, %d of %d at p = %s, a LINEAR subspace "
              "of F2^E, dim %d = E - V + 1 = %d - %d + 1, exactly what the %d single-vertex "
              "conditions cut out"
              % (t + 1, nm, len(S), En.DIM, p, dim, En.NQ, En.V, En.V),
              lin and dim == En.NQ - En.V + 1 and set(pred) == Sset
              and all(odds(S, q) in (Fraction(0), Fraction(1), Fraction(1, 2))
                      for q in range(En.NQ)))
    rk, sg, eq = [], set(), True
    for nm in NAMES:
        En, R = CL[nm][0], CL[nm][1]
        G = list(R["S_all"]) + [En.B(v) for v in range(En.V)]
        Z = []
        for tag in f2_kernel([g.x for g in G]):
            q = ID
            for j in range(len(G)):
                if (tag >> j) & 1:
                    q = q * G[j]
            assert q.x == 0
            Z.append(q)
        sg |= {q.k for q in Z}
        r, bz = f2_rank([q.z for q in Z])
        rk.append(r)
        eq = eq and f2_span(bz) == f2_span(f2_rank(
            [En.STARMASK[v] for v in range(En.V)])[1]) and r == En.V - 1
    check("B4 [exact] the Z-type subgroup of <S_f, B_v> has rank V - 1 = %d, %d, %d, sign +1 "
          "throughout (phases %s), and EQUALS <B_v>: no condition wider than a vertex star"
          % (rk[0], rk[1], rk[2], sorted(sg)), eq and sg == {0})


# ===================================================================== group C

def group_C():
    En, R = CL["cube"][0], CL["cube"][1]
    S = ALLOW["cube"][1]
    half = Fraction(1, 2)
    before = all(odds(S, q) == half for q in range(En.NQ))
    same = True
    for q in range(En.NQ):
        for b in (0, 1):
            sc = cond(S, q, b)
            same = same and len(sc) == len(S) // 2 and all(
                odds(sc, r) == half for r in range(En.NQ) if r != q)
    check("C1 [exact] cube: odds at all %d sites start at 1/2, and in each of the %d (site, "
          "value) cases the allowed set stays uniform on %d and the odds at the %d other sites "
          "stay at 1/2"
          % (En.NQ, 2 * En.NQ, len(S) // 2, En.NQ - 1), before and same)

    q04 = En.EIDX[(0, 4)]
    rows = []
    rows.append(("none", odds(S, q04)))
    s1 = cond(S, En.EIDX[(0, 1)], 1)
    rows.append(("(0,1)=1", odds(s1, q04)))
    rows.append(("(6,7)=1", odds(cond(S, En.EIDX[(6, 7)], 1), q04)))
    rows.append(("(0,1)=1,(5,7)=1", odds(cond(s1, En.EIDX[(5, 7)], 1), q04)))  # no star closed
    rows.append(("(0,1)=1,(0,2)=0", odds(cond(s1, En.EIDX[(0, 2)], 0), q04)))
    rows.append(("(0,1)=1,(0,2)=1", odds(cond(s1, En.EIDX[(0, 2)], 1), q04)))
    check("C2 [exact] cube, odds at (0,4) as records form: %s -- never between, leaving 1/2 "
          "only when the star of vertex 0 closes"
          % " ".join("[%s]%s" % (a, b) for a, b in rows),
          [str(b) for _, b in rows] == ["1/2", "1/2", "1/2", "1/2", "1", "0"])

    En, R = CL["grid3x3"][0], CL["grid3x3"][1]
    S = ALLOW["grid3x3"][1]
    deg2 = [q for q, (u, v) in enumerate(En.EDGES)
            if len(En.STAR[u]) == 2 or len(En.STAR[v]) == 2]
    ok = all(odds(S, q) == half for q in range(En.NQ))
    npart = 0
    for q in range(En.NQ):
        for b in (0, 1):
            sc = cond(S, q, b)
            ch = [r for r in range(En.NQ) if r != q and odds(sc, r) != half]
            if q in deg2:
                u, v = En.EDGES[q]
                w = u if len(En.STAR[u]) == 2 else v
                partner = [r for r in En.STAR[w] if r != q]
                ok = ok and ch == partner and odds(sc, ch[0]) in (Fraction(0), Fraction(1))
                npart += 1
            else:
                ok = ok and ch == []
    check("C3 [exact] grid3x3: odds at all %d sites start at 1/2; a record at one of the %d "
          "sites at a degree-2 corner forces its partner to 0 or 1 (%d cases), nothing else; a "
          "record at the other %d changes nothing"
          % (En.NQ, len(deg2), npart, En.NQ - len(deg2)), ok)

    En, R = CL["grid3x3+pendant"][0], CL["grid3x3+pendant"][1]
    S = ALLOW["grid3x3+pendant"][1]
    qb = En.EIDX[(0, 9)]
    ok = (odds(S, qb) == Fraction(0) and cond(S, qb, 1) == []
          and all(odds(S, q) == half for q in range(En.NQ) if q != qb))
    check("C4 [exact] grid3x3+pendant: the bridge site (0,9) has odds 0 with NO record present "
          "-- vertex 9 has degree 1, so its parity condition alone forces the site: a record of "
          "value 1 never forms. The other %d start at 1/2" % (En.NQ - 1), ok)

    En = CL["cube"][0]
    S = ALLOW["cube"][1]
    tally = {}
    ok = True
    for q1, q2 in itertools.combinations(range(En.NQ), 2):
        shared = set(En.EDGES[q1]) & set(En.EDGES[q2])
        for b1 in (0, 1):
            for b2 in (0, 1):
                sc = cond(cond(S, q1, b1), q2, b2)
                ch = [r for r in range(En.NQ)
                      if r not in (q1, q2) and odds(sc, r) != half]
                key = (len(shared), len(ch))
                tally[key] = tally.get(key, 0) + 1
                if shared:
                    third = [r for r in En.STAR[list(shared)[0]] if r not in (q1, q2)]
                    ok = ok and ch == third and all(
                        odds(sc, r) in (Fraction(0), Fraction(1)) for r in ch)
                else:
                    ok = ok and ch == []
    check("C5 [exact] cube, all %d site pairs x 4 values: odds elsewhere change in exactly "
          "the %d cases where the records close a vertex star, never in the other %d; the changed "
          "site is its third edge"
          % (En.NQ * (En.NQ - 1) // 2, tally.get((1, 1), 0), tally.get((0, 0), 0)),
          ok and tally == {(1, 1): 96, (0, 0): 168})


# ===================================================================== group D

FORCE = {}


def group_D():
    mism = 0
    detmin = True
    for t, nm in enumerate(NAMES):
        En = CL[nm][0]
        S = ALLOW[nm][1]
        dim, dual, cc = cocircuits(S, En.NQ)
        assert set(dual) == f2_span(f2_rank([En.STARMASK[v]
                                             for v in range(En.V)])[1])
        F = {q: forcing_sets(cc, q) for q in range(En.NQ)}
        FORCE[nm] = F
        for q in range(En.NQ):
            for s in F[q]:
                bitsq = [r for r in range(En.NQ) if (s >> r) & 1]
                det = True
                for a in range(1 << len(bitsq)):
                    sc = S
                    for u, r in enumerate(bitsq):
                        sc = cond(sc, r, (a >> u) & 1)
                    if sc and len({(z >> q) & 1 for z in sc}) != 1:
                        det = False
                minimal = True
                for drop in bitsq:
                    rest = [r for r in bitsq if r != drop]
                    free = False
                    for a in range(1 << len(rest)):
                        sc = S
                        for u, r in enumerate(rest):
                            sc = cond(sc, r, (a >> u) & 1)
                        if sc and len({(z >> q) & 1 for z in sc}) == 2:
                            free = True
                    minimal = minimal and free
                detmin = detmin and det and minimal
        cnt = sorted({len(F[q]) for q in range(En.NQ)})
        wts = sorted({pcnt(w) for w in cc})
        extra = ""
        if nm == "cube":
            pair2 = all(set(F[q][:2]) == {En.STARMASK[u] & ~(1 << q),
                                          En.STARMASK[v] & ~(1 << q)}
                        and all(pcnt(x) == 2 for x in F[q][:2])
                        for q, (u, v) in enumerate(En.EDGES))
            extra = (", every site forced by exactly %d minimal record sets, the two smallest "
                     "its endpoints' two-record vertex stars" % cnt[0])
            detmin = detmin and pair2
        else:
            extra = ", minimal forcing-set counts per site %s" % cnt
        check("D%d [exact] %s: the allowed set's cut space has dim %d, with %d cocircuits of "
              "weights %s%s"
              % (t + 1, nm, En.NQ - dim, len(cc),
                 "-".join(str(x) for x in (wts[0], wts[-1])), extra),
              detmin and En.NQ - dim == En.V - 1)
        for q in range(En.NQ):
            others = [r for r in range(En.NQ) if r != q]
            for sz in (1, 2, 3):
                for comb in itertools.combinations(others, sz):
                    mask = reduce(lambda a, b: a | (1 << b), comb, 0)
                    det = True
                    for a in range(1 << sz):
                        sc = S
                        for u, r in enumerate(comb):
                            sc = cond(sc, r, (a >> u) & 1)
                        if sc and len({(z >> q) & 1 for z in sc}) == 2:
                            det = False
                    if det != any((s & mask) == s for s in F[q]):
                        mism += 1
    check("D4 [exact] on all three clusters every listed set is deterministic and inclusion-"
          "minimal, and an exhaustive sweep of all record sets of size <= 3 against the cocircuit "
          "prediction gives %d mismatches" % mism, detmin and mism == 0)


# ===================================================================== group E

NONSTAB = {}


def group_E():
    full = {}
    rng = np.random.default_rng(7)
    for nm in NAMES:
        En, R = CL[nm][0], CL[nm][1]
        S = ALLOW[nm][1]
        v0 = coset_state(nm, {ALLOW[nm][0][0]: 1.0})
        npair, bad = pair_ordered(nm, v0)
        ref = Fraction(1, 1 << R["k"])
        badfull = 0
        norders = 0
        for target in [S[int(x)] for x in rng.integers(len(S), size=4)]:
            for _ in range(10):
                order = list(range(En.NQ))
                rng.shuffle(order)
                v, p = v0.copy(), 1.0
                for q in order:
                    w, n2 = lueders(v, BITS[nm][q], (target >> q) & 1)
                    p *= n2 / float(np.vdot(v, v).real)
                    v = w
                norders += 1
                if abs(p - float(ref)) > 1e-12:
                    badfull += 1
        full[nm] = (npair, bad, norders, badfull, ref)
    a, b = full["cube"], full["grid3x3"]
    check("E1 [exact] cube and grid3x3: all %d and %d ordered (site,value) pairs give identical "
          "joint odds either way, %d and %d mismatches; %d and %d shuffled full orders over %d "
          "sites close on the same %s, %s"
          % (a[0], b[0], a[1], b[1], a[2], b[2], CL["cube"][0].NQ, a[4], b[4]),
          a[1] == 0 and b[1] == 0 and a[3] == 0 and b[3] == 0 and a[0] == 264 and b[0] == 264)
    c = full["grid3x3+pendant"]
    check("E2 [exact] grid3x3+pendant: all %d ordered pairs give identical joint odds, %d "
          "mismatches, and %d shuffled full orders over %d sites close on %s -- the bridge site's "
          "value is forced alike"
          % (c[0], c[1], c[2], CL["grid3x3+pendant"][0].NQ, c[4]),
          c[1] == 0 and c[3] == 0 and c[0] == 312)
    zok = all(comm(P(0, 0, 1 << q1), P(0, 0, 1 << q2))
              for nm in NAMES
              for q1, q2 in itertools.combinations(range(CL[nm][0].NQ), 2))
    ns = []
    for lab, v in NONSTAB.items():
        ns.append((lab,) + pair_ordered("cube", v))
    check("E3 [exact] every Z_e, Z_f pair commutes exactly on all three clusters, so the "
          "stipulated Lueders conditionings commute; the same %d pairs give %d and %d mismatches "
          "on group G's two NON-stabilizer states"
          % (ns[0][1], ns[0][2], ns[1][2]),
          zok and all(x[2] == 0 for x in ns) and all(x[1] == 264 for x in ns))


# ===================================================================== group F

def group_F():
    nm = "cube"
    En, R, cid, phi, reps, recs = CL[nm]
    byrec = {recs[c]: c for c in range(len(reps))}
    vac = set(ALLOW[nm][1])
    dim0, dual0, cc0 = cocircuits(sorted(vac), En.NQ)
    half = Fraction(1, 2)
    res = {}
    for (u, w), lab in (((0, 1), "adjacent"), ((0, 3), "face-diagonal"),
                        ((0, 7), "antipodal")):
        c = byrec[tuple(1 if x in (u, w) else 0 for x in range(En.V))]
        S = [z for z in range(En.DIM) if cid[z] == c]
        base = S[0]
        iscoset = sorted(z ^ base for z in S) == sorted(vac)
        par = {x: {pcnt(z & En.STARMASK[x]) % 2 for z in S} for x in range(En.V)}
        nv = all(len(par[x]) == 1 for x in range(En.V))
        nv = nv and par[u] == {1} and par[w] == {1} and all(
            par[x] == {0} for x in range(En.V) if x not in (u, w))
        oddsok = all(odds(S, q) == half for q in range(En.NQ))
        dim, dual, cc = cocircuits(S, En.NQ)
        q1, q2, q3 = En.STAR[u]
        tab = {(b1, b2): sorted({(z >> q3) & 1 for z in cond(cond(S, q1, b1), q2, b2)})
               for b1 in (0, 1) for b2 in (0, 1)}
        tabv = {(b1, b2): sorted({(z >> q3) & 1
                                  for z in cond(cond(sorted(vac), q1, b1), q2, b2)})
                for b1 in (0, 1) for b2 in (0, 1)}
        res[lab] = (len(S), iscoset, nv, oddsok, dim, len(cc),
                    sorted({pcnt(x) for x in cc}), tab, tabv)
    a = res["adjacent"]
    check("F1 [exact] cube, a fermion pair at the adjacent corners 0 and 1 (B_v = -1 there): "
          "allowed set %d of %d, a genuine coset of the vacuum's subspace, uniform at p = 1/%d, "
          "odds 1/2 at all %d sites"
          % (a[0], En.DIM, a[0], En.NQ), a[1] and a[3] and a[0] == 32)
    b, c = res["face-diagonal"], res["antipodal"]
    check("F2 [exact] the same for the face-diagonal pair (0,3) and the antipodal (0,7): %d and "
          "%d allowed patterns, both cosets of the vacuum's subspace, uniform, odds 1/2 all round"
          % (b[0], c[0]), b[1] and b[3] and c[1] and c[3] and b[0] == 32 and c[0] == 32)
    check("F3 [exact] on every allowed pattern of all three pair states the parity on star(v) is "
          "1 at both corners, so n_v = 1 EXACTLY; cut space and its %d cocircuits of weights %s "
          "are the vacuum's, only forced values differ: ((0,1),(0,2)) send (0,4) to %s not %s"
          % (a[5], "-".join(str(x) for x in (a[6][0], a[6][-1])),
             ",".join(str(a[7][k][0]) for k in sorted(a[7])),
             ",".join(str(a[8][k][0]) for k in sorted(a[8]))),
          all(r[2] for r in res.values())
          and all(r[4] == dim0 and r[5] == len(cc0) for r in res.values())
          and all(len(v) == 1 for v in a[7].values())
          and all(a[7][k][0] != a[8][k][0] for k in a[7]))


# ===================================================================== group G

G_DATA = {}


def prepare_G():
    """The cube's N = 2 sector, its gauge, and the two coherent states."""
    nm = "cube"
    En, R, cid, phi, reps, recs = CL[nm]
    sel, pos, pats, Hoff, Ti, d, exact, slater = cube_two_particle()
    k = R["k"]
    w1 = slater(0, 4)
    w2 = slater(0, 4) + slater(0, 2)
    assert np.array_equal(Ti @ w1, -4 * w1) and np.array_equal(Ti @ w2, -4 * w2)
    v1, e1 = state_from_weights(sel, pos, d, w1, k)
    v2, e2 = state_from_weights(sel, pos, d, w2, k)
    NONSTAB["slater"] = v1
    NONSTAB["mix"] = v2
    G_DATA.update(sel=sel, pos=pos, pats=pats, Hoff=Hoff, Ti=Ti, d=d,
                  exact=exact, slater=slater, w1=w1, w2=w2, e1=e1, e2=e2)


def zero_census(ex):
    """Split the zero record patterns into out-of-sector and cancellation zeros."""
    En = CL["cube"][0]
    out = canc = sup = 0
    for z in range(En.DIM):
        if ex[z] > 0:
            sup += 1
        elif sum(En.record(z)) != 2:
            out += 1
        else:
            canc += 1
    return sup, out, canc


def group_G():
    En, R, cid, phi, reps, recs = CL["cube"]
    k = R["k"]
    sel, pos, d = G_DATA["sel"], G_DATA["pos"], G_DATA["d"]
    check("G1 [exact] cube N = 2 sector, %d cosets: 2^%d H_enc is Gaussian-integer and an exact "
          "diagonal gauge in {1, i, -1, -i} carries it entrywise onto Jordan-Wigner, no residual"
          % (len(sel), k),
          d is not None and G_DATA["exact"] and len(sel) == 28)

    byrec = {recs[c]: c for c in range(len(reps))}
    c0 = ALLOW["cube"][0][0]
    c1 = byrec[tuple(1 if x in (0, 1) else 0 for x in range(En.V))]
    ok = True
    vals = []
    for (a, b) in ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 3), Fraction(2, 3))):
        v = coset_state("cube", {c0: np.sqrt(float(a)), c1: np.sqrt(float(b))})
        p = np.abs(v) ** 2
        sup = [z for z in range(En.DIM) if p[z] > 1e-15]
        ex = {c0: Fraction(a, 1 << k), c1: Fraction(b, 1 << k)}
        ok = ok and len(sup) == 2 * (1 << k)
        ok = ok and all((p[z] > 1e-15) == (cid[z] in (c0, c1)) for z in range(En.DIM))
        ok = ok and max(abs(p[z] - float(ex[cid[z]])) for z in sup) < 1e-15
        vals.append(len(sup))
    check("G2 [exact] ACROSS sectors, sqrt(a)|vacuum> + sqrt(b)|pair(0,1)> at (a,b) = (1/2,1/2) "
          "and (1/3,2/3): support exactly %d and %d = 2 cosets x %d, odds a/%d and b/%d, 0 "
          "cancellation zeros: disjoint supports"
          % (vals[0], vals[1], 1 << k, 1 << k, 1 << k), ok)

    sup, out, canc = zero_census(G_DATA["e1"])
    w1 = G_DATA["w1"]
    van = [G_DATA["pats"][a] for a in range(len(sel)) if w1[a] == 0]
    pairs = [tuple(i for i, b in enumerate(pp) if b) for pp in van]
    xface = all((u >> 2) == (v >> 2) for u, v in pairs)
    ex1 = {G_DATA["e1"][z] for z in range(En.DIM) if G_DATA["e1"][z] > 0}
    check("G3 [exact] the Slater ground state of two particles at E = -4: support %d = %d "
          "cosets, uniform at %s, %d CANCELLATION zeros = %d cosets with a legal weight-2 "
          "pattern: exactly the %d corner pairs on one x-face"
          % (sup, sup // (1 << k), sorted(str(x) for x in ex1)[0], canc, canc // (1 << k),
             len(pairs)),
          sup == 512 and canc == 384 and out == 3200 and ex1 == {Fraction(1, 512)}
          and len(pairs) == 12 and xface)

    sup2, out2, canc2 = zero_census(G_DATA["e2"])
    slater = G_DATA["slater"]
    M = np.stack([slater(0, 4), slater(0, 2), slater(0, 1)]).astype(float)
    Q = np.linalg.qr(M.T)[0]
    diag = np.diag(Q @ Q.T)
    nvan = int(np.sum(np.abs(diag) < 1e-12))
    check("G4 [exact; last clause numerical 1e-12] a coherent mix of two E = -4 states: support "
          "%d, %d cancellation zeros = %d cosets against %d = %d for the single state, while the "
          "3-fold manifold's projector has %d vanishing diagonal entries of %d: they are the "
          "state's"
          % (sup2, canc2, canc2 // (1 << k), canc, canc // (1 << k), nvan, len(sel)),
          sup2 == 640 and canc2 == 256 and nvan == 0)


def main():
    prepare_G()
    for g in (group_A, group_B, group_C, group_D, group_E, group_F, group_G):
        g()
    print("SUMMARY: the odds at a site are 1/2 or forced, never between; a record elsewhere "
          "changes them only when a vertex parity closes; the finished set carries the same odds "
          "in any order.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
