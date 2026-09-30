#!/usr/bin/env python3
"""Finite BKSF sign checks and separate superlattice marker census.

Class-A finite computation.  The runner studies declared finite Pauli models
in an ambient fine cubic lattice with one qubit at each available site.  It
does not construct a nearest-neighbour framework law, choose a marker sector,
or prove formation, an infinite-volume particle, or a thermodynamic phase.
The runner establishes, exactly and without floating point:

  A  ENCODING.  The Bravyi-Kitaev superfast encoding written on the coarse
     lattice 2Z^3 sitting inside the fine lattice Z^3: roles are read off
     coordinate parity, the code qubits are the coarse edge sites, the
     direction order at every coarse vertex is -x < -y < -z < +x < +y < +z,
         A_ij = X(edge) * Z(edges ordered before it at both endpoints),
         A_ji = -A_ij,   B_i = product of the six Z's around vertex i,
         face stabilizer = the ordered product of the four A's of a plaquette.
     Relations R0-R4, prod_i B_i = +I, open-block and torus code dimensions.
  B  FINITE TRANSPORT OPERATORS.  The two Pauli components of
     T_ij = (i/2) A_ij (B_i - B_j) on 11 fine sites, all
     of them edge sites, L-infinity radius 2, along each of the three axes;
     it commutes with every face stabilizer and flips exactly B_i and B_j;
     closed three-dimensional circuits of A-string representatives are face-
     stabilizer products on the named open block.
  C  FINITE SIGN DIAGNOSTICS.  Levin-Wen T-junction and reordered-string
     signs for one endpoint type, with a bound-pair control, a commuting-X-
     string control in three dimensions, and a 2D toric-code epsilon control.
  D  SEPARATE SUPERLATTICE MARKER CONSTRAINT.  A diagonal, translation- and
     rotation-symmetrised 5x5x5 constraint whose finite-torus zero set is the 48
     role patterns (16 translates x 3 axis orientations of the period-(4,2,2)
     pattern), each with its coarse-edge bits free; incommensurate tori carry
     zero zero-penalty configurations; template-separation checks; a support-
     footprint census; and a seven-site-star bit-pattern census.
  E  TWO-DIMENSIONAL FINITE DIAGNOSTIC.  The connected one-qubit-per-site rule
     IXZZXIIII is checked on two tori and finite syndrome/string windows.
  F  THREE-DIMENSIONAL UNIT-CUBE CENSUS.  Commuting one- and two-pattern
     representatives are enumerated under the declared equivalence, proper
     one-pattern ideals receive explicit unit-coordinate zeros, and a declared
     finite-window mobile-cluster calculation is reported.

Every executed check is exact: integer and F2/Z4 bit arithmetic, exhaustive
enumeration, and exhaustive constraint propagation.  No SAT or external
solver is used.  Physical interpretation of a sign uses imported methodology
and is deliberately kept outside the executable result.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import sys
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 600

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


# ===================================================================== F2 / Z4

def pcnt(n):
    return bin(n).count("1")


class Q:
    """i^k X^x Z^z on a register of qubits indexed by bit position."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k & 3
        self.x = x
        self.z = z

    def __mul__(a, b):
        return Q(a.k + b.k + 2 * pcnt(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def neg(s):
        return Q(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def __hash__(s):
        return hash((s.k, s.x, s.z))

    def herm(s):
        return (s.k & 1) == (pcnt(s.x & s.z) & 1)

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def ismI(s):
        return s.x == 0 and s.z == 0 and s.k == 2

    def wt(s):
        return pcnt(s.x | s.z)

    def supp(s):
        m, out = s.x | s.z, []
        while m:
            b = m & -m
            out.append(b.bit_length() - 1)
            m ^= b
        return out

    def vec(s, n):
        return s.x | (s.z << n)


IDQ = Q(0, 0, 0)


def sp(a, b):
    return (pcnt(a.x & b.z) + pcnt(a.z & b.x)) & 1


def comm(a, b):
    return sp(a, b) == 0


def qprod(seq):
    o = IDQ
    for p in seq:
        o = o * p
    return o


def f2_rank(vs):
    piv = {}
    for v in vs:
        while v:
            p = v.bit_length() - 1
            if p in piv:
                v ^= piv[p]
            else:
                piv[p] = v
                break
    return len(piv)


def f2_express(target, gens):
    """Bitmask of generators whose product has the given symplectic vector."""
    piv = {}
    for i, g in enumerate(gens):
        v, c = g, 1 << i
        while v:
            p = v.bit_length() - 1
            if p in piv:
                v2, c2 = piv[p]
                v ^= v2
                c ^= c2
            else:
                piv[p] = (v, c)
                break
    v, c = target, 0
    while v:
        p = v.bit_length() - 1
        if p not in piv:
            return None
        v2, c2 = piv[p]
        v ^= v2
        c ^= c2
    return c


def solve_f2(rows, nunk):
    """rows: bits 0..nunk-1 coefficients, bit nunk the rhs. One solution or None."""
    mask = (1 << nunk) - 1
    piv, R = [], []
    for r in rows:
        for i, p in enumerate(piv):
            if (r >> p) & 1:
                r ^= R[i]
        low = r & mask
        if low == 0:
            if r:
                return None
            continue
        p = low.bit_length() - 1
        for i in range(len(R)):
            if (R[i] >> p) & 1:
                R[i] ^= r
        R.append(r)
        piv.append(p)
    sol = 0
    for i, p in enumerate(piv):
        if (R[i] >> nunk) & 1:
            sol |= 1 << p
    return sol


def nullspace_basis(rows, nunk):
    mask = (1 << nunk) - 1
    piv, R = [], []
    for r in rows:
        r &= mask
        for i, p in enumerate(piv):
            if (r >> p) & 1:
                r ^= R[i]
        if r:
            p = r.bit_length() - 1
            for i in range(len(R)):
                if (R[i] >> p) & 1:
                    R[i] ^= r
            R.append(r)
            piv.append(p)
    pivset = set(piv)
    out = []
    for f in range(nunk):
        if f in pivset:
            continue
        v = 1 << f
        for i, p in enumerate(piv):
            if (R[i] >> f) & 1:
                v |= 1 << p
        out.append(v)
    return out


def f2_intersect(U, V, n):
    """Zassenhaus: a spanning set of span(U) cap span(V) inside F_2^n."""
    mask = (1 << n) - 1
    piv, inter = {}, []
    for r in [(u << n) | u for u in U] + [(v << n) for v in V]:
        while r >> n:
            p = (r >> n).bit_length() - 1
            if p in piv:
                r ^= piv[p]
            else:
                piv[p] = r
                r = 0
                break
        if r:
            inter.append(r & mask)
    return inter


# ============================================= A. coarse lattice, BK superfast

DIRS = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
ROLE4 = {0: "vertex", 1: "edge", 2: "face", 3: "cube"}


def va(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vm(k, a):
    return (k * a[0], k * a[1], k * a[2])


def linf(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def role_of(s):
    return ROLE4[(s[0] & 1) + (s[1] & 1) + (s[2] & 1)]


class Lat:
    """Coarse cubic lattice, one code qubit per coarse edge.

    An edge key is (base vertex, axis): the endpoint from which the edge points
    in the +axis direction. Coarse vertex v sits at the fine site 2v; the edge
    (v, ax) sits at the fine site 2v + e_ax, which has exactly one odd
    coordinate, so every code qubit lives on a fine EDGE site.
    """

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.per = periodic
        Lx, Ly, Lz = dims
        self.V = [(a, b, c) for a in range(Lx) for b in range(Ly) for c in range(Lz)]
        self.nv = len(self.V)
        self.E = []
        for v in self.V:
            for ax in range(3):
                if self.step(v, EX[ax]) is not None:
                    self.E.append((v, ax))
        self.ei = {e: i for i, e in enumerate(self.E)}
        self.nq = len(self.E)
        self.inc = {}
        for v in self.V:
            d = {}
            for r in range(6):
                w = self.step(v, DIRS[r])
                if w is None:
                    continue
                key = (v, r - 3) if r >= 3 else (w, r)
                d[r] = (w, self.ei[key])
            self.inc[v] = d
        self.star = {v: sum(1 << q for (_, q) in self.inc[v].values()) for v in self.V}

    def step(self, v, d):
        w = va(v, d)
        if self.per:
            return tuple(w[i] % self.dims[i] for i in range(3))
        return w if all(0 <= w[i] < self.dims[i] for i in range(3)) else None

    def A(self, v, r):
        w, q = self.inc[v][r]
        x, z = 1 << q, 0
        for r2, (_, q2) in self.inc[v].items():
            if r2 < r:
                z ^= 1 << q2
        rb = (r + 3) % 6
        for r2, (_, q2) in self.inc[w].items():
            if r2 < rb:
                z ^= 1 << q2
        p = Q(pcnt(x & z) & 1, x, z)
        return p if r >= 3 else p.neg()

    def Aij(self, i, j):
        for r in range(6):
            if r in self.inc[i] and self.inc[i][r][0] == j:
                return self.A(i, r)
        raise KeyError("not adjacent")

    def B(self, v):
        return Q(0, 0, self.star[v])

    def Xbare(self, v, r):
        return Q(0, 1 << self.inc[v][r][1], 0)

    def loop(self, cyc):
        n = len(cyc)
        return qprod([self.Aij(cyc[a], cyc[(a + 1) % n]) for a in range(n)]).scal(n)

    def strop(self, path):
        n = len(path) - 1
        return qprod([self.Aij(path[a], path[a + 1]) for a in range(n)]).scal(n)

    def bare_str(self, path):
        ops = []
        for a in range(len(path) - 1):
            i, j = path[a], path[a + 1]
            for r in range(6):
                if r in self.inc[i] and self.inc[i][r][0] == j:
                    ops.append(self.Xbare(i, r))
                    break
        return qprod(ops)

    def faces(self):
        out = []
        for v in self.V:
            for d1 in range(3):
                for d2 in range(d1 + 1, 3):
                    a = self.step(v, EX[d1])
                    b = self.step(v, EX[d2])
                    if a is None or b is None:
                        continue
                    c = self.step(a, EX[d2])
                    if c is None:
                        continue
                    out.append((v, a, c, b))
        return out

    def Xplaq(self, f):
        x = 0
        for a in range(4):
            i, j = f[a], f[(a + 1) % 4]
            for r in range(6):
                if r in self.inc[i] and self.inc[i][r][0] == j:
                    x ^= 1 << self.inc[i][r][1]
                    break
        return Q(0, x, 0)

    def fine_q(self, q):
        v, ax = self.E[q]
        return va(vm(2, v), EX[ax])

    def mono(self, a, b, order=(0, 1, 2)):
        path, cur = [a], a
        for ax in order:
            while cur[ax] != b[ax]:
                d = 1 if b[ax] > cur[ax] else -1
                nxt = list(cur)
                nxt[ax] += d
                cur = tuple(nxt)
                path.append(cur)
        return path

    def via(self, a, wps, order=(0, 1, 2)):
        path = [a]
        for w in wps:
            path += self.mono(path[-1], w, order)[1:]
        return path


def syn_verts(L, op):
    return sorted([v for v in L.V if sp(op, L.B(v)) == 1])


def stab_k(L, gens):
    return L.nq - f2_rank([g.vec(L.nq) for g in gens])


def bk_relations(L):
    """R0-R4 and prod_i B_i = +I, by the symplectic representation with phases."""
    Eij = [(v, L.inc[v][r][0], r) for v in L.V for r in L.inc[v] if r >= 3]
    A = {(i, j, r): L.A(i, r) for (i, j, r) in Eij}
    Bv = {v: L.B(v) for v in L.V}
    ok = all(L.Aij(j, i) == A[(i, j, r)].neg() for (i, j, r) in Eij)
    ok &= all(p.herm() and (p * p).isI() for p in A.values())
    ok &= all(p.herm() and (p * p).isI() for p in Bv.values())
    ok &= all(comm(Bv[u], Bv[v]) for u, v in combinations(L.V, 2))
    for (i, j, r), p in A.items():
        for v in L.V:
            if sp(p, Bv[v]) != (1 if v in (i, j) else 0):
                ok = False
                break
    for a, b in combinations(list(A), 2):
        shared = len({a[0], a[1]} & {b[0], b[1]})
        if sp(A[a], A[b]) != (1 if shared == 1 else 0):
            ok = False
            break
    S = [L.loop(f) for f in L.faces()]
    ok &= all(s.herm() and (s * s).isI() and not s.isI() and not s.ismI() for s in S)
    ok &= all(comm(s, p) for s in S for p in A.values())
    ok &= all(comm(s, p) for s in S for p in Bv.values())
    ok &= all(comm(s, t) for s, t in combinations(S, 2))
    ok &= qprod([Bv[v] for v in L.V]).isI()
    return ok, len(A), len(S)


def wilson(L, ax):
    cyc = [tuple((k if i == ax else 0) % L.dims[i] for i in range(3))
           for k in range(L.dims[ax])]
    return L.loop(cyc)


def group_A():
    ok1 = True
    parts = []
    for dims, per, tag in [((3, 3, 3), False, "open 3x3x3"),
                           ((3, 3, 3), True, "periodic 3x3x3")]:
        L = Lat(dims, per)
        good, na, ns = bk_relations(L)
        ok1 &= good
        parts.append("%s %dA/%dF" % (tag, na, ns))
    check("A1 [exact] BK superfast on the coarse lattice 2Z^3 in Z^3, qubits on coarse "
          "edge sites, vertex order -x<-y<-z<+x<+y<+z: R0-R4 and prod_i B_i = +I hold "
          "on " + ", ".join(parts), ok1)

    rows, ok2 = [], True
    for dims in [(3, 3, 3), (4, 4, 4)]:
        L = Lat(dims, False)
        k = stab_k(L, [L.loop(f) for f in L.faces()])
        ok2 &= (k == L.nv - 1)
        rows.append("%dx%dx%d V/n/k %d/%d/%d" % (dims + (L.nv, L.nq, k)))
    check("A2 [exact] open coarse blocks, faces only: the finite stabilizer-rank count "
          "is k = V - 1 at " + ", ".join(rows), ok2)

    rows, okf, kfull = [], True, set()
    for dims in [(3, 3, 3), (4, 4, 4), (3, 3, 4)]:
        L = Lat(dims, True)
        SF = [L.loop(f) for f in L.faces()]
        W = [wilson(L, ax) for ax in range(3)]
        kf, kw = stab_k(L, SF), stab_k(L, SF + W)
        kfull.add(stab_k(L, SF + [L.B(v) for v in L.V]))
        okf &= (kf == L.nv - 1 + 3) and (kw == L.nv - 1)
        rows.append("%d/%d" % (kf, kw))
    check("A3 [exact] coarse tori 3^3, 4^3, 3x3x4 (L = 2 excluded, multigraphs): "
          "faces only give k = V - 1 + 3 and the three non-contractible Wilson loops "
          "leave k = V - 1; k_faces/k_faces+W = " + ", ".join(rows), okf)

    check("A4 [exact] faces together with every B_i on the three tested tori leave "
          "k = %s in each finite calculation" % sorted(kfull), kfull == {3})


# =================================================== B. mobility of the charge

def hop_components(L, v, ax):
    """The two Pauli components of T_ij = (i/2) A_ij (B_i - B_j) on edge (v, ax)."""
    w = L.inc[v][ax + 3][0]
    Aop = L.A(v, ax + 3)
    return Aop * L.B(v), Aop * L.B(w), w


def in_stab_with_phase(L, op, gens):
    """Is op in the group generated by gens, and with which Z4 phase?"""
    c = f2_express(op.vec(L.nq), [g.vec(L.nq) for g in gens])
    if c is None:
        return None, None
    idx = [j for j in range(len(gens)) if (c >> j) & 1]
    pr = qprod([gens[j] for j in idx])
    return len(idx), (op.k - pr.k) & 3


def group_B():
    L = Lat((5, 5, 5), False)
    SF = [L.loop(f) for f in L.faces()]
    i0 = (2, 2, 2)
    okc, rows = True, []
    for ax in range(3):
        p1, p2, w = hop_components(L, i0, ax)
        su = sorted(set(p1.supp()) | set(p2.supp()))
        sites = [L.fine_q(q) for q in su]
        mid = va(vm(2, i0), EX[ax])
        roles = sorted({role_of(s) for s in sites})
        okc &= (len(sites) == 11 and roles == ["edge"]
                and max(linf(s, mid) for s in sites) == 2)
        rows.append("%s:%d sites Linf %d" % ("xyz"[ax], len(sites),
                                             max(linf(s, mid) for s in sites)))
    check("B1 [exact] both Pauli components of T_ij = (i/2) A_ij (B_i - B_j) "
          "have a union supported on exactly 11 fine sites, all coarse-edge sites, "
          "with L-infinity radius 2 about the edge midpoint along each axis: "
          + ", ".join(rows), okc)

    npair, bad, badsyn = 0, 0, 0
    for v in L.V:
        for r in L.inc[v]:
            if r < 3:
                continue
            w = L.inc[v][r][0]
            if syn_verts(L, L.A(v, r)) != sorted([v, w]):
                badsyn += 1
            for p in (L.A(v, r) * L.B(v), L.A(v, r) * L.B(w)):
                for s in SF:
                    npair += 1
                    bad += sp(p, s)
    check("B2 [exact] open 5x5x5 coarse block, %d modes, %d qubits, %d faces: all %d "
          "(hop component, face) pairs commute, %d anticommuting, and every "
          "A_ij flips exactly B_i and B_j, %d wrong syndromes"
          % (L.nv, L.nq, len(SF), npair, bad, badsyn), bad == 0 and badsyn == 0)

    def circuit(pts, order=(0, 1, 2)):
        cy = []
        for a in range(len(pts)):
            cy += L.mono(pts[a], pts[(a + 1) % len(pts)], order)[:-1]
        return cy

    okl, rows = True, []
    cy1 = [i0, va(i0, EX[0]), va(va(i0, EX[0]), EX[1]),
           va(va(va(i0, EX[0]), EX[1]), EX[2]),
           va(va(i0, EX[1]), EX[2]), va(i0, EX[2])]
    for tag, cy in [("x,y,z,-x,-y,-z", cy1),
                    ("box circuit", circuit([(1, 1, 1), (3, 1, 1), (3, 3, 1),
                                             (3, 3, 3), (1, 3, 3), (1, 1, 3)])),
                    ("non-planar hexagon", circuit([(0, 0, 0), (3, 0, 0), (3, 3, 0),
                                                    (3, 3, 3), (0, 3, 3), (0, 0, 3)],
                                                   (2, 1, 0)))]:
        W = L.loop(cy)
        nf, ph = in_stab_with_phase(L, W, SF)
        okl &= (nf is not None and ph == 0 and syn_verts(L, W) == [])
        rows.append("%s %d/%d%s" % (tag, W.wt(), nf, "" if ph == 0 else " BAD"))
    check("B3 [exact] three closed 3D circuits of A_ij string representatives are "
          "face-stabilizer products with residual phase +1; weight/generators: "
          + "; ".join(rows), okl)


# ================================================ C. statistics of the charge

def tjunction(W1, W2, W3):
    """Levin-Wen: W1 W2 W3 = theta * W3 W2 W1, theta = (-1)^{sum of pair symplectics}."""
    F, Rv = W1 * W2 * W3, W3 * W2 * W1
    assert F.x == Rv.x and F.z == Rv.z
    th = (F.k - Rv.k) & 3
    assert th in (0, 2)
    assert (th == 2) == (((sp(W1, W2) + sp(W1, W3) + sp(W2, W3)) & 1) == 1)
    return th


class TC2D:
    """Ordinary 2D toric code on the edges of a square lattice (control C3)."""

    def __init__(self, Lx, Ly):
        self.Lx, self.Ly = Lx, Ly
        self.q = {}
        for x in range(Lx - 1):
            for y in range(Ly):
                self.q[("h", x, y)] = len(self.q)
        for x in range(Lx):
            for y in range(Ly - 1):
                self.q[("v", x, y)] = len(self.q)

    def Zq(self, k):
        return Q(0, 0, 1 << self.q[k]) if k in self.q else IDQ

    def Xq(self, k):
        return Q(0, 1 << self.q[k], 0) if k in self.q else IDQ

    def hop(self, x, y, d):
        if d == (1, 0):
            return self.Zq(("h", x, y)) * self.Xq(("v", x + 1, y))
        if d == (-1, 0):
            return self.Zq(("h", x - 1, y)) * self.Xq(("v", x, y))
        if d == (0, 1):
            return self.Zq(("v", x, y)) * self.Xq(("h", x, y + 1))
        return self.Zq(("v", x, y - 1)) * self.Xq(("h", x, y))

    def string(self, start, steps):
        p, c = IDQ, start
        for d in steps:
            p = p * self.hop(c[0], c[1], d)
            c = (c[0] + d[0], c[1] + d[1])
        return p

    def star(self, x, y):
        o = IDQ
        for k in (("h", x, y), ("h", x - 1, y), ("v", x, y), ("v", x, y - 1)):
            o = o * self.Xq(k)
        return o

    def plaq(self, x, y):
        o = IDQ
        for k in (("h", x, y), ("h", x, y + 1), ("v", x, y), ("v", x + 1, y)):
            o = o * self.Zq(k)
        return o


TJ_GEOMS = [
    ("+x,+y,+z", [(3, 0, 0), (0, 3, 0), (0, 0, 3)], [(0, 1, 2)] * 3),
    ("-x,-y,-z", [(-3, 0, 0), (0, -3, 0), (0, 0, -3)], [(0, 1, 2)] * 3),
    ("+x,-y,+z", [(3, 0, 0), (0, -3, 0), (0, 0, 3)], [(0, 1, 2)] * 3),
    ("single hops", [(1, 0, 0), (0, 1, 0), (0, 0, 1)], [(0, 1, 2)] * 3),
    ("collinear +x,-x,+y", [(3, 0, 0), (-3, 0, 0), (0, 3, 0)], [(0, 1, 2)] * 3),
    ("non-coplanar (2,2,0)(0,2,2)(2,0,2)", [(2, 2, 0), (0, 2, 2), (2, 0, 2)],
     [(0, 1, 2)] * 3),
    ("non-coplanar (3,1,1)(1,3,1)(1,1,3)", [(3, 1, 1), (1, 3, 1), (1, 1, 3)],
     [(0, 1, 2)] * 3),
    ("generic (3,2,1)(-1,3,2)(2,-1,3)", [(3, 2, 1), (-1, 3, 2), (2, -1, 3)],
     [(0, 1, 2)] * 3),
    ("same legs rerouted", [(3, 1, 1), (1, 3, 1), (1, 1, 3)],
     [(2, 1, 0), (1, 0, 2), (0, 2, 1)]),
    ("body-diagonal (3,3,3)(-3,3,-3)(3,-3,-3)",
     [(3, 3, 3), (-3, 3, -3), (3, -3, -3)], [(0, 1, 2)] * 3),
]

BRAID_GEOMS = [
    ("xy-plane triangle", (1, 1, 1), (5, 1, 1), (1, 5, 1), [(0, 1, 2)] * 3, None),
    ("xz-plane triangle", (1, 1, 1), (5, 1, 1), (1, 1, 5), [(0, 2, 1)] * 3, None),
    ("generic 3D triangle", (1, 1, 1), (5, 3, 2), (2, 1, 5), [(0, 1, 2)] * 3, None),
    ("xy triangle with all three legs detoured out of the plane",
     (1, 1, 1), (5, 1, 1), (1, 5, 1), [(2, 0, 1), (1, 2, 0), (0, 2, 1)],
     [[(1, 1, 3), (5, 1, 3)], [(5, 3, 4), (1, 3, 4)], [(3, 5, 2), (3, 1, 2)]]),
]


def group_C():
    L = Lat((7, 7, 7), False)
    SF = [L.loop(f) for f in L.faces()]
    J = (3, 3, 3)
    ths, okg = set(), True
    for _, deltas, orders in TJ_GEOMS:
        Ws, syok = [], True
        for dl, od in zip(deltas, orders):
            p = va(J, dl)
            W = L.strop(L.mono(J, p, od))
            Ws.append(W)
            syok &= (syn_verts(L, W) == sorted([J, p]))
        okg &= syok and all(comm(W, s) for W in Ws for s in SF)
        ths.add(tjunction(*Ws))
    check("C1 [exact] finite Levin-Wen T-junction sign diagnostic on the open "
          "7x7x7 block (%d faces): theta = "
          "%s over %d leg geometries, two non-coplanar and one rerouted triple among "
          "them, every leg with endpoint-only syndromes and commuting with every face"
          % (len(SF), "-1" if ths == {2} else str(ths), len(TJ_GEOMS)),
          ths == {2} and okg)

    thb, okb = set(), True
    for _, p1, p2, p3, orders, vias in BRAID_GEOMS:
        pairs = [(p1, p2), (p2, p3), (p3, p1)]
        legs = []
        for k, (a, b) in enumerate(pairs):
            path = L.via(a, vias[k] + [b], orders[k]) if (vias and vias[k]) \
                else L.mono(a, b, orders[k])
            legs.append(L.strop(path))
        t21, t32, t13 = legs
        E, Sr = t13 * t21 * t32, t13 * t32 * t21
        assert E.x == Sr.x and E.z == Sr.z
        thb.add((E.k - Sr.k) & 3)
        okb &= all(comm(o, s) for o in legs for s in SF) and \
            all(syn_verts(L, o) == sorted(pr) for o, pr in zip(legs, pairs))
    check("C2 [exact] reordered-string exchange diagnostic E = t13 t21 t32 against "
          "S = t13 t32 t21, the "
          "same operators reordered so hop phases cancel: theta = %s over %d triangles, "
          "one with all legs detoured out of the plane"
          % ("-1" if thb == {2} else str(thb), len(BRAID_GEOMS)),
          thb == {2} and okb)

    DL = [((3, 0, 0), (0, 3, 0), (0, 0, 3)), ((-3, 0, 0), (0, -3, 0), (0, 0, -3)),
          ((2, 2, 0), (0, 2, 2), (2, 0, 2)), ((3, 1, 1), (1, 3, 1), (1, 1, 3))]
    DLP = [((2, 0, 0), (0, 2, 0), (0, 0, 2)), ((-2, 0, 0), (0, -2, 0), (0, 0, -2)),
           ((2, 2, 0), (0, 2, 2), (2, 0, 2)), ((2, 1, 1), (1, 2, 1), (1, 1, 2))]
    Jc, Jp = (3, 3, 3), (4, 3, 3)
    c1 = set()
    for deltas in DLP:
        Ws = [L.strop(L.mono(Jc, va(Jc, dl))) * L.strop(L.mono(Jp, va(Jp, dl)))
              for dl in deltas]
        c1.add(tjunction(*Ws))
    XP = [L.Xplaq(f) for f in L.faces()]
    c2, okc2 = set(), True
    for deltas in DL:
        Ws = [L.bare_str(L.mono(J, va(J, dl))) for dl in deltas]
        okc2 &= all(comm(W, s) for W in Ws for s in XP)
        c2.add(tjunction(*Ws))
    T = TC2D(13, 13)
    STAB = [T.star(x, y) for x in range(13) for y in range(13)] + \
           [T.plaq(x, y) for x in range(12) for y in range(12)]
    c3, okc3 = set(), True
    for steps3 in [[[(1, 0)] * 3, [(0, 1)] * 3, [(0, -1)] * 3],
                   [[(1, 0)] * 3, [(-1, 0)] * 3, [(0, 1)] * 3],
                   [[(-1, 0)] * 2, [(0, 1)] * 2, [(0, -1)] * 2],
                   [[(1, 0), (0, 1), (1, 0)], [(0, 1), (-1, 0), (0, 1)],
                    [(0, -1), (1, 0), (0, -1)]]]:
        Ws = [T.string((6, 6), st) for st in steps3]
        okc3 &= all(sum(1 for s in STAB if sp(W, s) == 1) == 4 for W in Ws)
        c3.add(tjunction(*Ws))
    nbad = sum(1 for s in SF if sp(L.bare_str(L.mono(J, va(J, (3, 0, 0)))), s) == 1)
    check("C3 [exact] finite controls: a bound pair of adjacent endpoint types %s; "
          "a 3D commuting-X-string construction %s; the 2D toric-code epsilon "
          "construction %s against %d detectors; the bare X string anticommutes with %d "
          "superfast faces"
          % ("+1" if c1 == {0} else str(c1), "+1" if c2 == {0} else str(c2),
             "-1" if c3 == {2} else str(c3), len(STAB), nbad),
          c1 == {0} and c2 == {0} and c3 == {2} and okc2 and okc3 and nbad > 0)


# ================================== D. the superlattice role pattern on Z^3
#
# The role pattern has period (4, 2, 2) along a chosen axis.  On the fine
# lattice a site's ROLE is its coordinate parity: all even = a corner of the
# doubled lattice, exactly one odd = an edge, two odd = a face, three odd = a
# cube centre.  The pinned values are
#     corner -> (s[ax] / 2) mod 2,   face -> 0,   cube centre -> 1,
# and every edge site is FREE: it carries a code qubit.

def Pat(s, ax=0):
    w = (s[0] & 1) + (s[1] & 1) + (s[2] & 1)
    if w == 0:
        return (s[ax] // 2) & 1
    if w == 1:
        return None
    return 0 if w == 2 else 1


def PatConst(s, a, b, c):
    w = (s[0] & 1) + (s[1] & 1) + (s[2] & 1)
    return a if w == 0 else (None if w == 1 else (b if w == 2 else c))


def reps_ax(ax):
    rg = [range(2), range(2), range(2)]
    rg[ax] = range(4)
    return [(x, y, z) for x in rg[0] for y in rg[1] for z in rg[2]]


def win(r, shape="cube"):
    if shape == "cube":
        return [d for d in product(range(-r, r + 1), repeat=3) if d != (0, 0, 0)]
    return [d for d in product(range(-r, r + 1), repeat=3)
            if d != (0, 0, 0) and sum(map(abs, d)) <= r]


def contexts(patfun, r, reps, shape="cube"):
    out = {}
    for rep in reps:
        ctx = {}
        for d in win(r, shape):
            v = patfun(va(rep, d))
            if v is not None:
                ctx[d] = v
        out[rep] = (patfun(rep), ctx)
    return out


def templates(r=2):
    """The rotation-symmetrised template set: 16 translates x 3 axis orientations."""
    out = []
    for ax in range(3):
        cx = contexts(lambda s, ax=ax: Pat(s, ax), r, reps_ax(ax))
        for rep in reps_ax(ax):
            out.append((ax, rep, cx[rep][0], cx[rep][1]))
    return out


def unseparated(ctxs, reps, pins_only):
    """Class pairs an adversary controlling the free bits can make identical."""
    bad = []
    for a, b in combinations(reps, 2):
        pa, ca = ctxs[a]
        pb, cb = ctxs[b]
        if pins_only and pa == pb:
            continue
        if not any(d in cb and ca[d] != cb[d] for d in ca):
            bad.append((a, b))
    return bad


class RoleTorus:
    """The diagonal marker rule on a periodic box, as bitmask match conditions."""

    def __init__(self, dims, tmpls):
        self.dims = dims
        Lx, Ly, Lz = dims
        self.sites = [(x, y, z) for x in range(Lx) for y in range(Ly)
                      for z in range(Lz)]
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.N = len(self.sites)
        self.NC = len(tmpls)
        self.pin = [t[2] for t in tmpls]
        self.tm = tmpls
        self.mask = [[0] * self.NC for _ in range(self.N)]
        self.want = [[0] * self.NC for _ in range(self.N)]
        self.wrapbad = 0
        for t, s in enumerate(self.sites):
            for ci, (_, _, _, ctx) in enumerate(tmpls):
                m = w = 0
                for d, v in ctx.items():
                    u = self.idx[((s[0] + d[0]) % Lx, (s[1] + d[1]) % Ly,
                                  (s[2] + d[2]) % Lz)]
                    if u == t:
                        self.wrapbad += 1
                        continue
                    if ((m >> u) & 1) and (((w >> u) & 1) != v):
                        self.wrapbad += 1
                    m |= 1 << u
                    if v:
                        w |= 1 << u
                self.mask[t][ci] = m
                self.want[t][ci] = w

    def sector_partial(self, ax, sh):
        """(known, vals) of the sector: marker sites pinned, edge sites free."""
        Lx, Ly, Lz = self.dims
        known = vals = 0
        for t, s in enumerate(self.sites):
            v = Pat(vsub(s, sh), ax)
            if v is None:
                continue
            known |= 1 << t
            if v:
                vals |= 1 << t
        return known, vals

    def penalty(self, cfg):
        tot = 0
        for t in range(self.N):
            ms, any_ = 0, False
            mt, wt = self.mask[t], self.want[t]
            for ci in range(self.NC):
                if (cfg & mt[ci]) == wt[ci]:
                    any_ = True
                    ms |= 1 << ci
            if not any_:
                tot += 1
            bit = (cfg >> t) & 1
            for ci in range(self.NC):
                if ((ms >> ci) & 1 and self.pin[ci] is not None
                        and bit != self.pin[ci]):
                    tot += 1
        return tot


class RoleSolver:
    """Complete enumeration of the zero-penalty set, by branch-on-role plus
       constraint propagation.  No SAT solver: the branching is over which of
       the templates matches at site 0, then over undetermined bits."""

    def __init__(self, T):
        self.N, self.NC = T.N, T.NC
        self.mask, self.want, self.pin = T.mask, T.want, T.pin
        self.nodes = 0

    def state(self, known, vals, t, ci):
        m = self.mask[t][ci]
        if (vals ^ self.want[t][ci]) & m & known:
            return 2
        return 0 if (m & ~known) else 1

    def propagate(self, known, vals):
        changed = True
        while changed:
            changed = False
            for t in range(self.N):
                live, matched = [], []
                for ci in range(self.NC):
                    st = self.state(known, vals, t, ci)
                    if st == 2:
                        continue
                    live.append(ci)
                    if st == 1:
                        matched.append(ci)
                if not live:
                    return None
                for ci in matched:
                    p = self.pin[ci]
                    if p is None:
                        continue
                    if not (known >> t) & 1:
                        known |= 1 << t
                        if p:
                            vals |= 1 << t
                        changed = True
                    elif ((vals >> t) & 1) != p:
                        return None
                if len(live) == 1:
                    ci = live[0]
                    m, w = self.mask[t][ci], self.want[t][ci]
                    if m & ~known:
                        nk = m & ~known
                        known |= nk
                        vals = (vals & ~nk) | (w & nk)
                        changed = True
                    if (vals ^ w) & m:
                        return None
                    p = self.pin[ci]
                    if p is not None:
                        if not (known >> t) & 1:
                            known |= 1 << t
                            if p:
                                vals |= 1 << t
                            changed = True
                        elif ((vals >> t) & 1) != p:
                            return None
        return (known, vals)

    def decided(self, known, vals):
        """Zero penalty for EVERY assignment of the still-undetermined bits."""
        for t in range(self.N):
            anym = False
            for ci in range(self.NC):
                st = self.state(known, vals, t, ci)
                if st == 2:
                    continue
                p = self.pin[ci]
                if p is not None:
                    if not (known >> t) & 1:
                        return False
                    if ((vals >> t) & 1) != p:
                        return False
                if st == 1:
                    anym = True
            if not anym:
                return False
        return True

    def walk(self, known, vals, out):
        self.nodes += 1
        r = self.propagate(known, vals)
        if r is None:
            return
        known, vals = r
        if self.decided(known, vals):
            out.append((known, vals))
            return
        free = (~known) & ((1 << self.N) - 1)
        if free == 0:
            return
        i = (free & -free).bit_length() - 1
        for b in (0, 1):
            self.walk(known | (1 << i), vals | (b << i), out)

    def all_cylinders(self):
        out = []
        for ci in range(self.NC):
            self.walk(self.mask[0][ci], self.want[0][ci], out)
        return sorted(set(out))


def cylinders_pairwise_inconsistent(cylinders):
    """True exactly when every distinct cylinder pair disagrees where both bind."""
    return all(bool((v1 ^ v2) & k1 & k2)
               for (k1, v1), (k2, v2) in combinations(cylinders, 2))


def support_hull(support):
    """Return whether support fits one 7-site star and one explicit connected hull.

    Every finite support has a connected hull, so the hull is reported only as
    a transparent footprint diagnostic; it is not used to infer locality of a
    rule or factorization of an operator.
    """
    Sset = sorted(set(support))
    for c in [va(Sset[0], d) for d in [(0, 0, 0)] + DIRS]:
        if all(sum(abs(s[i] - c[i]) for i in range(3)) <= 1 for s in Sset):
            return True, len(Sset)
    hubs = set(Sset)

    def comps(hs):
        out, left = [], set(hs)
        while left:
            u = left.pop()
            c, st = {u}, [u]
            while st:
                a = st.pop()
                for d in DIRS:
                    w = va(a, d)
                    if w in left:
                        left.discard(w)
                        c.add(w)
                        st.append(w)
            out.append(c)
        return out

    cs = comps(hubs)
    guard = 0
    while len(cs) > 1 and guard < 400:
        guard += 1
        best = None
        for i, j in combinations(range(len(cs)), 2):
            for a in cs[i]:
                for b in cs[j]:
                    d = sum(abs(a[q] - b[q]) for q in range(3))
                    if best is None or d < best[0]:
                        best = (d, a, b)
        _, a, b = best
        cur = a
        while cur != b:
            for k in range(3):
                if cur[k] != b[k]:
                    nx = list(cur)
                    nx[k] += 1 if b[k] > cur[k] else -1
                    cur = tuple(nx)
                    hubs.add(cur)
                    break
        cs = comps(hubs)
    return False, len(hubs) if len(cs) == 1 else 0


def group_D():
    TM = templates(2)
    sectors = [(ax, rep) for ax in range(3) for rep in reps_ax(ax)]

    T4 = RoleTorus((4, 4, 4), TM)
    S4 = RoleSolver(T4)
    parts4 = sorted({T4.sector_partial(ax, sh) for (ax, sh) in sectors})
    okd1 = (len(parts4) == 48 and T4.wrapbad == 0
            and all(S4.decided(k, v) for (k, v) in parts4))
    nfree4 = T4.N - pcnt(parts4[0][0])
    check("D1 [exact] the symmetrised marker rule, 48 templates = 16 translates x 3 "
          "orientations of the period-(4,2,2) role pattern, 5x5x5 window: 48 sectors "
          "on the 4x4x4 torus, each of penalty 0 for all 2^%d free-bit fillings"
          % nfree4, okd1)

    cyl4 = S4.all_cylinders()
    pairwise_inconsistent = cylinders_pairwise_inconsistent(cyl4)
    mixed_guard_fixture = [(0b11, 0b00), (0b11, 0b01), (0b10, 0b00)]
    guard_rejects_partial = not cylinders_pairwise_inconsistent(mixed_guard_fixture)
    okd2 = (sorted(cyl4) == sorted(parts4) and pairwise_inconsistent
            and guard_rejects_partial and len(cyl4) == 48
            and all(pcnt(k) == T4.N - nfree4 for (k, _) in cyl4))
    check("D2 [exact] exhaustive branch-on-role propagation on the 4x4x4 torus, %d "
          "search nodes, no SAT solver: exactly %d zero-penalty cylinders, the 48 "
          "sectors, pairwise inconsistent, so the zero set is 48 x 2^%d, no junk"
          % (S4.nodes, len(cyl4), nfree4), okd2)

    T8 = RoleTorus((8, 4, 4), TM)
    S8 = RoleSolver(T8)
    parts8 = sorted({T8.sector_partial(ax, sh) for (ax, sh) in sectors})
    cyl8 = S8.all_cylinders()
    nfree8 = T8.N - pcnt(parts8[0][0])
    okd3 = (sorted(cyl8) == sorted(parts8) and len(cyl8) == 48
            and T8.wrapbad == 0)
    check("D3 [exact] the same complete search on the commensurate 8x4x4 torus, %d "
          "sites, %d nodes: again exactly the %d sectors, zero set 48 x 2^%d"
          % (T8.N, S8.nodes, len(cyl8), nfree8), okd3)

    rows, okd4 = [], True
    for dims in [(5, 4, 4), (4, 5, 4), (7, 4, 4)]:
        Ti = RoleTorus(dims, TM)
        Si = RoleSolver(Ti)
        cy = Si.all_cylinders()
        okd4 &= (len(cy) == 0)
        rows.append("%dx%dx%d %d" % (dims + (len(cy),)))
    check("D4 [exact] incommensurate tori, whose sides hold the period (4,2,2) in no "
          "orientation, carry no zero-penalty configuration; every branch closes: "
          + ", ".join(rows), okd4)

    reps16 = reps_ax(0)
    per2_fail = True
    for (a, b, c) in product((0, 1), repeat=3):
        for r in (1, 2, 3, 4):
            cx = contexts(lambda s, a=a, b=b, c=c: PatConst(s, a, b, c), r, reps16)
            if not unseparated(cx, reps16, True):
                per2_fail = False
    cx3 = contexts(Pat, 1, reps16)
    b3 = unseparated(cx3, reps16, True)
    cxall = {}
    allreps = []
    for ax in range(3):
        cxa = contexts(lambda s, ax=ax: Pat(s, ax), 2, reps_ax(ax))
        for rep in reps_ax(ax):
            cxall[(ax, rep)] = cxa[rep]
            allreps.append((ax, rep))
    b5 = unseparated(cxall, allreps, True)
    cxs = contexts(Pat, 1, reps16, "l1")
    bs = unseparated(cxs, reps16, True)
    check("D5 [exact] window minimality: the 3x3x3 window leaves %d unseparated "
          "pin-pairs and the 7-site star %d, every period-2 role assignment fails at "
          "each tested odd cubic window 3, 5, 7, 9, and the 5x5x5 window leaves %d "
          "across all 48 templates"
          % (len(b3), len(bs), len(b5)),
          len(b3) == 2 and len(bs) > 0 and per2_fail and len(b5) == 0)

    L = Lat((7, 7, 7), False)
    i0 = (3, 3, 3)
    rows = []
    for ax in range(3):
        p1, p2, w = hop_components(L, i0, ax)
        rows.append(("A_%s" % "xyz"[ax], [L.fine_q(q) for q in L.A(i0, ax + 3).supp()]))
        rows.append(("T comp A.B_i %s" % "xyz"[ax], [L.fine_q(q) for q in p1.supp()]))
        rows.append(("T comp A.B_j %s" % "xyz"[ax], [L.fine_q(q) for q in p2.supp()]))
        rows.append(("T total %s" % "xyz"[ax],
                     [L.fine_q(q) for q in sorted(set(p1.supp()) | set(p2.supp()))]))
    rows.append(("B_i", [L.fine_q(q) for q in L.B(i0).supp()]))
    for f in L.faces()[:1]:
        pass
    seen = set()
    for f in L.faces():
        kind = tuple(sorted({a for a in range(3)
                             if any(v[a] != f[0][a] for v in f)}))
        if kind in seen:
            continue
        seen.add(kind)
        rows.append(("face %s" % "".join("xyz"[a] for a in kind),
                     [L.fine_q(q) for q in L.loop(f).supp()]))
    nq_types = len(rows)
    npinned_templates = 0
    for (ax, rep, pin, ctx) in TM:
        if pin is None:
            continue
        npinned_templates += 1
        rows.append(("marker centre-penalty contribution",
                     [va(vm(2, i0), va(rep, d)) for d in ctx]
                     + [va(vm(2, i0), rep)]))
    allsup = set()
    for (_, _, _, ctx) in TM:
        allsup.update(ctx)
    rows.append(("no-role penalty",
                 [va(vm(2, i0), d) for d in allsup] + [vm(2, i0)]))
    cls = [support_hull(sup) for (_, sup) in rows]
    nstar = sum(1 for is_star, _ in cls if is_star)
    nhull = sum(1 for is_star, _ in cls if not is_star)
    maxhull = max(n for _, n in cls)
    starnames = [rows[i][0] for i in range(len(rows)) if cls[i][0]]
    check("D6 [exact] support-footprint census, not a locality theorem: %d declared "
          "BKSF/hop objects and %d actual marker-penalty contributions (%d pinned-"
          "centre templates plus the no-template contribution); %d fit one seven-site "
          "star (%s), the other %d receive explicit 6-connected hulls, largest %d hubs"
          % (nq_types, len(rows) - nq_types, npinned_templates, nstar,
             ", ".join(starnames), nhull, maxhull),
          npinned_templates == 30 and len(rows) - nq_types == 31
          and nstar == 4 and nhull == 43 and maxhull == 125)

    stars, vstars, bonds = set(), set(), set()
    sites4 = [(x, y, z) for x in range(4) for y in range(4) for z in range(4)]
    for (ax, sh) in sectors:
        base = {s: Pat(vsub(s, sh), ax) for s in sites4}
        for c in sites4:
            nb = [tuple((c[i] + d[i]) % 4 for i in range(3)) for d in DIRS]
            pinned = [base[c]] + [base[u] for u in nb]
            fidx = [i for i, v in enumerate(pinned) if v is None]
            for bits in product((0, 1), repeat=len(fidx)):
                pat = list(pinned)
                for i, b in zip(fidx, bits):
                    pat[i] = b
                stars.add(tuple(pat))
                if role_of(vsub(c, sh)) == "vertex":
                    vstars.add(tuple(pat))
            for u in nb:
                pu, pc = base[u], base[c]
                for a in ((0, 1) if pc is None else (pc,)):
                    for b in ((0, 1) if pu is None else (pu,)):
                        bonds.add((a, b))
    check("D7 [exact] finite bit-pattern census over the 48 declared sectors and all "
          "free-bit fillings: corner-centred seven-site stars realise %d of 128 "
          "patterns and adjacent pairs realise %d of 4"
          % (len(vstars), len(bonds)),
          len(vstars) == 128 and len(stars) == 128 and len(bonds) == 4)


# ================== E / F. homogeneous one-qubit-per-site rules on Z^2 and Z^3

class Op:
    """Pauli operator on named sites: i^ph (prod X)(prod Z)."""

    __slots__ = ("xs", "zs", "ph")

    def __init__(self, xs=None, zs=None, ph=0):
        self.xs = set(xs) if xs else set()
        self.zs = set(zs) if zs else set()
        self.ph = ph % 4

    def support(self):
        return self.xs | self.zs


def omul(A, B):
    return Op(A.xs ^ B.xs, A.zs ^ B.zs, (A.ph + B.ph + 2 * len(A.zs & B.xs)) % 4)


def osp(A, B):
    return (len(A.xs & B.zs) + len(A.zs & B.xs)) & 1


def vadd(a, b):
    return tuple(u + v for u, v in zip(a, b))


def vdif(a, b):
    return tuple(u - v for u, v in zip(a, b))


def vsm(k, a):
    return tuple(k * u for u in a)


PNAME = {(0, 0): "I", (1, 0): "X", (1, 1): "Y", (0, 1): "Z"}


class Rule:
    """One qubit per site of Z^d, t stabilizer patterns per cell, given as
       (mX, mZ) bit masks over a common support template `offsets`."""

    def __init__(self, dim, offsets, pats, name=""):
        self.dim = dim
        self.offsets = tuple(offsets)
        self.pats = tuple(pats)
        self.t = len(pats)
        self.name = name
        self.xoff, self.zoff, self.supp = [], [], []
        for (mx, mz) in pats:
            self.xoff.append(tuple(o for i, o in enumerate(self.offsets)
                                   if (mx >> i) & 1))
            self.zoff.append(tuple(o for i, o in enumerate(self.offsets)
                                   if (mz >> i) & 1))
            self.supp.append(tuple(o for i, o in enumerate(self.offsets)
                                   if ((mx | mz) >> i) & 1))
        self.omin = tuple(min(o[i] for o in self.offsets) for i in range(dim))
        self.omax = tuple(max(o[i] for o in self.offsets) for i in range(dim))
        self.radius = max(max(abs(q) for q in o) for o in self.offsets)
        self._gc = {}

    def gen(self, key):
        g = self._gc.get(key)
        if g is None:
            c, a = key
            xs = set(vadd(c, o) for o in self.xoff[a])
            zs = set(vadd(c, o) for o in self.zoff[a])
            g = Op(xs, zs, len(xs & zs))
            self._gc[key] = g
        return g

    def keys_touching(self, site):
        return [(vdif(site, o), a) for a in range(self.t) for o in self.supp[a]]

    def sites_in_box(self, lo, hi):
        return [tuple(p) for p in
                product(*[range(lo[i], hi[i] + 1) for i in range(self.dim)])]

    def label(self):
        return " | ".join("".join(PNAME[((mx >> i) & 1, (mz >> i) & 1)]
                                  for i in range(len(self.offsets)))
                          for (mx, mz) in self.pats)


def syndrome(rule, O):
    cand = set()
    for s in O.support():
        cand.update(rule.keys_touching(s))
    return frozenset(k for k in cand if osp(O, rule.gen(k)))


def shift_syn(rule, sigma, v):
    return frozenset((vadd(k[0], v), k[1]) for k in sigma)


class Wnd:
    """Linear algebra of all Pauli operators supported inside a finite site set."""

    def __init__(self, rule, sites):
        self.rule = rule
        self.sites = sorted(sites)
        keys = set()
        for s in self.sites:
            keys.update(rule.keys_touching(s))
        self.keys = sorted(keys)
        self.ki = {k: i for i, k in enumerate(self.keys)}
        self.keyset = set(self.keys)
        self.nunk = 2 * len(self.sites)
        rows = [0] * len(self.keys)
        for i, s in enumerate(self.sites):
            for k in rule.keys_touching(s):
                g = rule.gen(k)
                j = self.ki[k]
                if s in g.zs:
                    rows[j] ^= 1 << (2 * i)
                if s in g.xs:
                    rows[j] ^= 1 << (2 * i + 1)
        self.rows = rows
        self._conds = None

    def solve_syndrome(self, target):
        tset = set(target)
        if not tset <= self.keyset:
            return None
        rows = [self.rows[j] | ((1 << self.nunk) if k in tset else 0)
                for j, k in enumerate(self.keys)]
        sol = solve_f2(rows, self.nunk)
        if sol is None:
            return None
        xs, zs = set(), set()
        for i, s in enumerate(self.sites):
            if (sol >> (2 * i)) & 1:
                xs.add(s)
            if (sol >> (2 * i + 1)) & 1:
                zs.add(s)
        return Op(xs, zs, 0)

    def conds(self):
        if self._conds is None:
            nunk = self.nunk
            mask = (1 << nunk) - 1
            piv, R, C = [], [], []
            for j in range(len(self.keys)):
                r = self.rows[j] | (1 << (nunk + j))
                for i, p in enumerate(piv):
                    if (r >> p) & 1:
                        r ^= R[i]
                low = r & mask
                if low:
                    p = low.bit_length() - 1
                    for i in range(len(R)):
                        if (R[i] >> p) & 1:
                            R[i] ^= r
                    R.append(r)
                    piv.append(p)
                elif r:
                    C.append(r >> nunk)
            self._conds = C
        return self._conds

    def achievable(self, target):
        tset = set(target)
        if not tset <= self.keyset:
            return None
        tm = 0
        for k in tset:
            tm |= 1 << self.ki[k]
        return all(not (pcnt(c & tm) & 1) for c in self.conds())

    def syndrome_image(self, keys_zero, keys_target):
        nunk = self.nunk
        ti = {k: i for i, k in enumerate(keys_target)}
        rows = [self.rows[self.ki[k]] for k in keys_zero]
        for k in keys_target:
            rows.append(self.rows[self.ki[k]] | (1 << (nunk + ti[k])))
        mask = (1 << nunk) - 1
        piv, R, C = [], [], []
        for r in rows:
            for i, p in enumerate(piv):
                if (r >> p) & 1:
                    r ^= R[i]
            low = r & mask
            if low:
                p = low.bit_length() - 1
                for i in range(len(R)):
                    if (R[i] >> p) & 1:
                        R[i] ^= r
                R.append(r)
                piv.append(p)
            elif r:
                C.append(r >> nunk)
        return nullspace_basis(C, len(keys_target))


_WC = {}


def get_window(rule, lo, hi):
    key = (id(rule), lo, hi)
    if key not in _WC:
        _WC[key] = Wnd(rule, rule.sites_in_box(lo, hi))
    return _WC[key]


def _bbox(rule, p, q, margin):
    d = rule.dim
    return (tuple(min(p[i], q[i]) - margin for i in range(d)),
            tuple(max(p[i], q[i]) + margin for i in range(d)))


def hop(rule, sigma, p, q, margin=4):
    tgt = frozenset(shift_syn(rule, sigma, p) ^ shift_syn(rule, sigma, q))
    lo, hi = _bbox(rule, p, q, margin)
    O = get_window(rule, lo, hi).solve_syndrome(tgt)
    if O is not None:
        assert syndrome(rule, O) == tgt
    return O


def string_by_steps(rule, sg, start, step, K, margin=3):
    cur, B = start, Op()
    for _ in range(K):
        nxt = vadd(cur, step)
        h = hop(rule, sg, cur, nxt, margin)
        if h is None:
            return None
        B = omul(B, h)
        cur = nxt
    return B


def loop_by_steps(rule, sg, origin, u, w, N, margin=3):
    pts = [origin]
    for _ in range(N):
        pts.append(vadd(pts[-1], u))
    for _ in range(N):
        pts.append(vadd(pts[-1], w))
    for _ in range(N):
        pts.append(vdif(pts[-1], u))
    for _ in range(N):
        pts.append(vdif(pts[-1], w))
    W = Op()
    for i in range(len(pts) - 1):
        h = hop(rule, sg, pts[i], pts[i + 1], margin)
        if h is None:
            return None, None
        W = omul(W, h)
    return W, pts


def t_junction_multi(rule, sigma, basis, margin=2, Rs=(6, 9, 12)):
    """Levin-Wen T-junction with thin, step-wise legs; the 3-term sign is gauge
       invariant, and leg clearance is checked explicitly."""
    d = rule.dim
    u, w = basis[0], basis[1]
    nu, nw = vsm(-1, u), vsm(-1, w)
    uw = vadd(u, w)
    triples = [(u, nu, w), (w, nw, u), (u, w, vsm(-1, uw)),
               (u, nu, nw), (w, nw, nu), (nu, u, nw)]
    rho = margin + max(max(abs(q) for q in u), max(abs(q) for q in w)) \
        + rule.radius + 1
    o = (0,) * d
    signs, ngeom = set(), 0
    for (d1, d2, d3) in triples:
        for R in Rs:
            ends = [vsm(R, d1), vsm(R, d2), vsm(R, d3)]
            paths = [[vsm(s, dd) for s in range(R + 1)] for dd in (d1, d2, d3)]
            ok = True
            for i in range(3):
                for j in range(3):
                    if i != j and min(max(abs(p[q] - ends[j][q]) for q in range(d))
                                      for p in paths[i]) <= rho:
                        ok = False
            if not ok:
                continue
            T = [string_by_steps(rule, sigma, o, dd, R, margin)
                 for dd in (d1, d2, d3)]
            if any(x is None for x in T):
                continue
            ngeom += 1
            signs.add(2 * ((osp(T[0], T[1]) ^ osp(T[0], T[2])
                            ^ osp(T[1], T[2])) & 1))
    return signs, ngeom


def _segment_clearance_at_least(c2, a2, b2, reach2):
    """Exact squared-distance comparison in coordinates scaled by two.

    ``c2``, ``a2`` and ``b2`` are twice the physical coordinates, and
    ``reach2`` is twice the required clearance.  The interior-projection case
    is compared after multiplication by the integer segment length squared.
    """
    p = (b2[0] - a2[0], b2[1] - a2[1])
    w = (c2[0] - a2[0], c2[1] - a2[1])
    length2 = p[0] * p[0] + p[1] * p[1]
    radius2 = reach2 * reach2
    if length2 == 0:
        return w[0] * w[0] + w[1] * w[1] >= radius2
    dot = w[0] * p[0] + w[1] * p[1]
    if dot <= 0:
        return w[0] * w[0] + w[1] * w[1] >= radius2
    if dot >= length2:
        v = (c2[0] - b2[0], c2[1] - b2[1])
        return v[0] * v[0] + v[1] * v[1] >= radius2
    return ((w[0] * w[0] + w[1] * w[1]) * length2 - dot * dot
            >= radius2 * length2)


def braid_table(rule, named, margin=2, maxN=28, radius=1):
    """Mutual braid phases B(a,b) = (-1)^{<W_a, B_b>}, the loop grown until its
       centre is farther from the path than any hop window can reach."""
    out = []
    for tag, sa, ba in named:
        u, w = ba[0], ba[1]
        step = max(max(abs(q) for q in u), max(abs(q) for q in w))
        need = margin + step + radius + 1
        N = None
        for cand in range(4, maxN + 1, 2):
            V = [(0, 0), (cand * u[0], cand * u[1]),
                 (cand * (u[0] + w[0]), cand * (u[1] + w[1])),
                 (cand * w[0], cand * w[1])]
            c2 = (cand * (u[0] + w[0]), cand * (u[1] + w[1]))
            V2 = [(2 * q[0], 2 * q[1]) for q in V]
            if all(_segment_clearance_at_least(c2, V2[i], V2[(i + 1) % 4],
                                               2 * need)
                   for i in range(4)):
                N = cand
                break
        if N is None:
            out.append((tag, None))
            continue
        W, pts = loop_by_steps(rule, sa, (0, 0), u, w, N, margin=margin)
        if W is None or syndrome(rule, W):
            out.append((tag, None))
            continue
        cen = vadd(vsm(N // 2, u), vsm(N // 2, w))
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        row = []
        for tag2, sb, bb in named:
            phs = set()
            for st in list(bb) + [vsm(-1, q) for q in bb]:
                K = 4
                while K <= 60:
                    e = vadd(cen, vsm(K, st))
                    if (e[0] < min(xs) - margin - radius - 1
                            or e[0] > max(xs) + margin + radius + 1
                            or e[1] < min(ys) - margin - radius - 1
                            or e[1] > max(ys) + margin + radius + 1):
                        break
                    K += 2
                if K > 60:
                    continue
                B = string_by_steps(rule, sb, cen, st, K, margin=margin)
                if B is not None:
                    phs.add(osp(W, B))
            row.append("+1" if phs == {0} else ("-1" if phs == {1} else "?"))
        out.append((tag, row))
    return out


def torus_k(rule, L):
    d, t = rule.dim, rule.t
    n = L ** d

    def idx(s):
        v = 0
        for i in range(d):
            v = v * L + (s[i] % L)
        return v

    gens = []
    for c in product(range(L), repeat=d):
        for a in range(t):
            x = z = 0
            for o in rule.xoff[a]:
                x ^= 1 << idx(vadd(c, o))
            for o in rule.zoff[a]:
                z ^= 1 << idx(vadd(c, o))
            gens.append((x, z))
    bad = 0
    for i in range(len(gens)):
        x1, z1 = gens[i]
        for j in range(i + 1, len(gens)):
            x2, z2 = gens[j]
            if (pcnt(x1 & z2) + pcnt(z1 & x2)) & 1:
                bad += 1
    return n - f2_rank([x | (z << n) for x, z in gens]), bad


def charge_classes(rule, span_cells=2, pad_loc=1, cell_pad_mid=2, site_pad_far=2):
    """Superselection sectors: syndromes on a core block realisable from far
       away modulo those realisable locally."""
    d, t = rule.dim, rule.t
    core = [(c, a) for c in rule.sites_in_box((0,) * d, (span_cells - 1,) * d)
            for a in range(t)]
    coreset = set(core)
    tlo = tuple(rule.omin[i] for i in range(d))
    thi = tuple(span_cells - 1 + rule.omax[i] for i in range(d))
    Wl = Wnd(rule, rule.sites_in_box(tuple(tlo[i] - pad_loc for i in range(d)),
                                     tuple(thi[i] + pad_loc for i in range(d))))
    bloc = Wl.syndrome_image([k for k in Wl.keys if k not in coreset], core)
    mid = [(c, a) for c in rule.sites_in_box((-cell_pad_mid,) * d,
                                             (span_cells - 1 + cell_pad_mid,) * d)
           for a in range(t)]
    mlo = tuple(-cell_pad_mid + rule.omin[i] - site_pad_far for i in range(d))
    mhi = tuple(span_cells - 1 + cell_pad_mid + rule.omax[i] + site_pad_far
                for i in range(d))
    Wf = Wnd(rule, rule.sites_in_box(mlo, mhi))
    bfar = Wf.syndrome_image([k for k in mid if k not in coreset and k in Wf.ki],
                             core)
    piv = {}

    def red(v):
        while v:
            p = v.bit_length() - 1
            if p in piv:
                v ^= piv[p]
            else:
                return v, p
        return 0, None

    for v in bloc:
        r, p = red(v)
        if r:
            piv[p] = r
    extra = []
    for v in bfar:
        r, p = red(v)
        if r:
            piv[p] = r
            extra.append(v)
    reps = []
    for msk in range(1, 1 << len(extra)):
        v = 0
        for i in range(len(extra)):
            if (msk >> i) & 1:
                v ^= extra[i]
        reps.append(frozenset(k for i, k in enumerate(core) if (v >> i) & 1))
    return reps


def mobile_cluster_space(rule, v, ncell=2, margin=3):
    d, t = rule.dim, rule.t
    cells = rule.sites_in_box((0,) * d, (ncell - 1,) * d)
    C = [(c, a) for c in cells for a in range(t)]
    Ci = {c: i for i, c in enumerate(C)}
    allc = cells + [vadd(c, v) for c in cells]
    lo = tuple(min(c[i] for c in allc) + rule.omin[i] - margin for i in range(d))
    hi = tuple(max(c[i] for c in allc) + rule.omax[i] + margin for i in range(d))
    W = Wnd(rule, rule.sites_in_box(lo, hi))
    nu, ns = W.nunk, len(C)
    rows = []
    for j, k in enumerate(W.keys):
        r = W.rows[j]
        if k in Ci:
            r |= 1 << (nu + Ci[k])
        km = (vdif(k[0], v), k[1])
        if km in Ci:
            r |= 1 << (nu + Ci[km])
        rows.append(r)
    return [b >> nu for b in nullspace_basis(rows, nu + ns)], ns


def trivial_cluster_space(rule, ncell=2, pad=1):
    d, t = rule.dim, rule.t
    C = [(c, a) for c in rule.sites_in_box((0,) * d, (ncell - 1,) * d)
         for a in range(t)]
    Cs = set(C)
    lo = tuple(rule.omin[i] - pad for i in range(d))
    hi = tuple(ncell - 1 + rule.omax[i] + pad for i in range(d))
    W = Wnd(rule, rule.sites_in_box(lo, hi))
    if not Cs <= W.keyset:
        return []
    return W.syndrome_image([k for k in W.keys if k not in Cs], C)


def fully_mobile_cluster_dim(rule, ncell=2, margin=3, short=True):
    """Dimension of the space of NONTRIVIAL clusters inside an ncell^d block
       that a bounded operator can move one step along EVERY coordinate axis.
       The cluster shape is an unknown solved for together with the operator,
       so every bound state in the block is covered.  With short=True the walk
       stops as soon as the running intersection is trivial, which already
       settles the answer 0 but truncates the per-axis record."""
    d = rule.dim
    triv = trivial_cluster_space(rule, ncell)
    dtr = f2_rank(triv)
    cur, per_axis, dead = None, [], False
    for j in range(d):
        v = tuple(1 if i == j else 0 for i in range(d))
        spc, ns = mobile_cluster_space(rule, v, ncell, margin)
        per_axis.append(f2_rank(list(spc) + list(triv)) - dtr)
        if not dead:
            cur = spc if cur is None else f2_intersect(cur, spc, ns)
            if f2_rank(list(cur) + list(triv)) - dtr <= 0:
                dead = True
                if short:
                    return 0, per_axis
    if dead:
        return 0, per_axis
    return max(0, f2_rank(list(cur) + list(triv)) - dtr), per_axis


def rank_int(vs, ncol):
    M = [list(v) for v in vs]
    rk = 0
    for c in range(ncol):
        pr = None
        for r in range(rk, len(M)):
            if M[r][c] != 0:
                pr = r
                break
        if pr is None:
            continue
        M[rk], M[pr] = M[pr], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][c] != 0:
                a, b = M[rk][c], M[r][c]
                M[r] = [a * M[r][i] - b * M[rk][i] for i in range(ncol)]
        rk += 1
    return rk


def span_basis(vs, ncol):
    b = []
    for v in sorted(vs, key=lambda t: (sum(abs(x) for x in t), t)):
        if rank_int(b + [v], ncol) > len(b):
            b.append(v)
        if len(b) == ncol:
            break
    return b


def can_hop(rule, sigma, p, q, margin=4):
    tgt = frozenset(shift_syn(rule, sigma, p) ^ shift_syn(rule, sigma, q))
    lo, hi = _bbox(rule, p, q, margin)
    return bool(get_window(rule, lo, hi).achievable(tgt))


DIRS2 = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 0), (0, 2), (2, 1), (1, 2),
         (2, -1), (1, -2), (2, 2), (2, -2)]

MOORE9 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1),
          (1, -1), (1, 0), (1, 1))


def translates_commute(rule):
    """Exhaustive: every pair of generators within reach anticommutes nowhere."""
    d = rule.dim
    span = 2 * rule.radius
    ok = True
    for c in rule.sites_in_box((-span,) * d, (span,) * d):
        for a in range(rule.t):
            for b in range(rule.t):
                if c == (0,) * d and a == b:
                    continue
                if osp(rule.gen(((0,) * d, a)), rule.gen((c, b))):
                    ok = False
    return ok


def group_E():
    rule = Rule(2, MOORE9, [(0b10010, 0b1100)], "IXZZXIIII")
    okv = translates_commute(rule)
    k6, bad6 = torus_k(rule, 6)
    k8, bad8 = torus_k(rule, 8)
    reps = charge_classes(rule)
    check("E1 [exact] the connected one-qubit-per-site rule %s on Z^2, support "
          "{(-1,0), (-1,1), (0,-1), (0,0)}: all translates commute, k(6) = %d and "
          "k(8) = %d with %d non-commuting generator pairs, %d nontrivial charge classes"
          % (rule.label(), k6, k8, bad6 + bad8, len(reps)),
          okv and k6 == 2 and k8 == 2 and bad6 == 0 and bad8 == 0 and len(reps) == 3)

    named, ths = [], []
    for sg in reps:
        vsn = [v for v in DIRS2 if can_hop(rule, sg, (0, 0), v)]
        basis = span_basis(vsn, 2)
        signs, ng = t_junction_multi(rule, sg, basis)
        cells = sorted(k[0] for k in sg)
        named.append(("".join("F" if signs == {2} else "b") + str(cells), sg, basis))
        ths.append((cells, basis, signs, ng))
    nf = sum(1 for (_, _, s, _) in ths if s == {2})
    nb = sum(1 for (_, _, s, _) in ths if s == {0})
    check("E2 [exact] finite T-junction sign diagnostic on those classes, thin "
          "step-wise legs with exact clearance checked: %s -- %d negative-sign and "
          "%d positive-sign classes"
          % (", ".join("%s %s x%d"
                       % (str(c).replace(" ", ""),
                          "-1" if s == {2} else ("+1" if s == {0} else str(s)), ng)
                       for (c, b, s, ng) in ths), nf, nb),
          nf == 1 and nb == 2)

    tab = braid_table(rule, named)
    want = [["+1" if i == j else "-1" for j in range(3)] for i in range(3)]
    got = [row for (_, row) in tab]
    clearance_guard = (
        _segment_clearance_at_least((2, 2), (0, 0), (4, 0), 2)
        and not _segment_clearance_at_least((2, 2), (0, 0), (4, 0), 4)
    )
    check("E3 [exact] the finite mutual-sign table over those classes, each loop grown "
          "out of reach of any hop window and every exit route checked: %s -- equals "
          "the declared diagonal +1/off-diagonal -1 target"
          % "; ".join("".join(r) for (t, r) in tab),
          got == want and clearance_guard)


# ------------------------------------------ F. cube-rule enumeration on Z^3

CUBE8 = tuple(sorted(product((0, 1), repeat=3)))
GL2 = [((1, 0), (0, 1)), ((0, 1), (1, 0)), ((1, 1), (0, 1)),
       ((1, 0), (1, 1)), ((0, 1), (1, 1)), ((1, 1), (1, 0))]


def apply_clifford(mx, mz, g):
    (a, b), (c, dd) = g
    return ((mx if a else 0) ^ (mz if b else 0),
            (mx if c else 0) ^ (mz if dd else 0))


def permute_mask(m, perm):
    out = 0
    while m:
        b = m & -m
        out |= 1 << perm[b.bit_length() - 1]
        m ^= b
    return out


def cubic48_perms():
    """The 48 signed axis maps, as permutations of the eight cube vertices."""
    out, seen = [], set()
    for pm in permutations(range(3)):
        for sg in product((1, -1), repeat=3):
            vmap = []
            for v in CUBE8:
                c = tuple(2 * x - 1 for x in v)
                c2 = tuple(sg[i] * c[pm[i]] for i in range(3))
                vmap.append(CUBE8.index(tuple((x + 1) // 2 for x in c2)))
            tp = tuple(vmap)
            if tp not in seen:
                seen.add(tp)
                out.append(tp)
    return out


def shift_tables(offsets):
    idx = {o: i for i, o in enumerate(offsets)}
    k = len(offsets)
    ts = sorted({vdif(u, v) for u in offsets for v in offsets})
    tab = {}
    for t in ts:
        src = [idx.get(vdif(o, t)) for o in offsets]
        table = [0] * (1 << k)
        for m in range(1 << k):
            v = 0
            for i in range(k):
                j = src[i]
                if j is not None and (m >> j) & 1:
                    v |= 1 << i
            table[m] = v
        tab[t] = table
    return ts, tab


def make_valid_checkers(offsets):
    ts, tab = shift_tables(offsets)
    nz = [t for t in ts if any(t)]

    def self_ok(p):
        mx, mz = p
        for t in nz:
            T = tab[t]
            if (pcnt(mx & T[mz]) + pcnt(mz & T[mx])) & 1:
                return False
        return True

    def cross_ok(p, q):
        ax, az = p
        bx, bz = q
        for t in ts:
            T = tab[t]
            if (pcnt(ax & T[bz]) + pcnt(az & T[bx])) & 1:
                return False
        return True

    return self_ok, cross_ok


def canon_notrans(pats, perms):
    best = None
    for perm in perms:
        pp = [(permute_mask(mx, perm), permute_mask(mz, perm)) for (mx, mz) in pats]
        for g in GL2:
            cand = tuple(sorted(apply_clifford(mx, mz, g) for (mx, mz) in pp))
            if best is None or cand < best:
                best = cand
    return best


class GF:
    """GF(2^k) by carry-less multiplication modulo an irreducible polynomial."""

    POLY = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

    def __init__(self, k):
        self.k = k
        self.mod = GF.POLY[k]
        self.units = list(range(1, 1 << k))

    def mul(self, a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a >> self.k:
                a ^= self.mod
        return r

    def powr(self, a, e):
        r = 1
        for _ in range(e):
            r = self.mul(r, a)
        return r


def eval_poly(F, offsets, point):
    """Evaluate a three-variable F2 polynomial in the supplied finite field."""
    a, b, c = point
    acc = 0
    for o in offsets:
        acc ^= F.mul(F.mul(F.powr(a, o[0]), F.powr(b, o[1])),
                     F.powr(c, o[2]))
    return acc


def ideal_is_proper(fx, fz):
    """Exhibit a common zero of f_X and f_Z with all coordinates a unit, over
       GF(2^k) for k = 1..4.  Such a point proves the ideal (f_X, f_Z) of the
       Laurent ring is proper, hence the charge module R/(f_X, f_Z) is nonzero."""
    for k in (1, 2, 3, 4):
        F = GF(k)
        for a in F.units:
            for b in F.units:
                for c in F.units:
                    point = (a, b, c)
                    if not eval_poly(F, fx, point) and not eval_poly(F, fz, point):
                        return True, k, (a, b, c)
    return False, None, None


def group_F():
    perms = cubic48_perms()
    self_ok, cross_ok = make_valid_checkers(CUBE8)
    valid_all, valid_w4 = [], []
    for mx in range(256):
        for mz in range(256):
            s = mx | mz
            if s and self_ok((mx, mz)):
                valid_all.append((mx, mz))
                if pcnt(s) >= 4:
                    valid_w4.append((mx, mz))
    r_all, r_w4 = {}, {}
    for p in valid_all:
        r_all.setdefault(canon_notrans((p,), perms), []).append(p)
    for p in valid_w4:
        r_w4.setdefault(canon_notrans((p,), perms), []).append(p)
    reps1 = [sorted(v)[0] for v in r_w4.values()]
    cls2 = {}
    for P in reps1:
        for Q in valid_w4:
            if Q != P and cross_ok(P, Q):
                cls2.setdefault(canon_notrans((P, Q), perms), (P, Q))
    check("F1 [exact] census of nonidentity unit-cube-support translation-invariant "
          "one-qubit Pauli patterns on Z^3: of 4^8 - 1 patterns, %d commute with all "
          "translates, %d have support >= 4; modulo the 48 cubic vertex maps, the six "
          "common onsite Clifford relabellings, and pattern exchange, %d one-pattern "
          "(%d at support >= 1) and %d two-pattern representatives"
          % (len(valid_all), len(valid_w4), len(r_w4), len(r_all), len(cls2)),
          len(valid_all) == 1011 and len(valid_w4) == 735 and len(r_w4) == 21
          and len(r_all) == 28 and len(cls2) == 423)

    rules1 = [Rule(3, CUBE8, [p]) for p in sorted(reps1)]
    nproper, kmax = 0, 0
    for r in rules1:
        fx, fz = list(r.xoff[0]), list(r.zoff[0])
        okp, k, witness = ideal_is_proper(fx, fz)
        witness_ok = False
        if okp and k in GF.POLY and witness and all(witness):
            F = GF(k)
            witness_ok = not eval_poly(F, fx, witness) and not eval_poly(F, fz, witness)
        if witness_ok:
            nproper += 1
            kmax = max(kmax, k)
    check("F2 [exact] for the %d one-pattern representatives, each pair (f_X,f_Z) "
          "has an explicitly evaluated common zero with three nonzero coordinates over "
          "GF(2^k), k <= %d; hence each displayed Laurent ideal is proper"
          % (len(rules1), kmax), nproper == len(rules1))

    hist, worst = {}, 0
    for r in rules1:
        dfm, per_axis = fully_mobile_cluster_dim(r, ncell=2, margin=3,
                                                 short=False)
        na = sum(1 for a in per_axis if a > 0)
        hist[na] = hist.get(na, 0) + 1
        worst = max(worst, dfm)
    check("F3 [exact] declared finite-window calculation, 2x2x2 cell "
          "block, margin 3, cluster shape solved for with the operator: over the %d "
          "rules axes with some mobile cluster distribute %s, yet %d have one cluster "
          "returned mobile along all three within this window"
          % (len(rules1), " ".join("%d:%d" % kv for kv in sorted(hist.items())),
             worst), worst == 0)

    rules2 = [Rule(3, CUBE8, list(cls2[k])) for k in sorted(cls2)]
    nax2, worst2 = 0, 0
    for r in rules2:
        dfm, per_axis = fully_mobile_cluster_dim(r, ncell=2, margin=3)
        nax2 += sum(1 for a in per_axis if a > 0)
        worst2 = max(worst2, dfm)
    check("F4 [exact] the same declared 2x2x2/margin-3 calculation on all %d "
          "two-pattern representatives returns %d with a cluster mobile along all "
          "three axes within that finite window" % (len(rules2), worst2), worst2 == 0)


def main():
    for g in (group_A, group_B, group_C, group_D, group_E, group_F):
        g()
    print("SUMMARY: exact finite BKSF operator/sign checks, a separate finite marker "
          "zero-set census, a finite 2D sign table, and a bounded 3D unit-cube-rule "
          "census; no framework-law, formation, or infinite-volume conclusion.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
