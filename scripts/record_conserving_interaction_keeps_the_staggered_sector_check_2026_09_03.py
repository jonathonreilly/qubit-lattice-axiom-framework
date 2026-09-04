#!/usr/bin/env python3
"""A record-conserving interaction keeps the staggered sector at half filling.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3, one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding
written on it.  Transport of one encoded excitation around a coarse face
equals that face's stabilizer S_f, so a choice of eigenvalue +-1 per face --
a flux sector -- is exactly a Z2 gauge class of nearest-neighbour link signs.
The all-(+1) sector is the plain hopping; the all-(-1) sector is the
framework's staggered (Kawamoto-Smit) kinetic form
    eta_1 = 1,  eta_2(x) = (-1)^{x_1},  eta_3(x) = (-1)^{x_1+x_2}.
A separate result shows that the FREE hopping energy at half filling picks the
all-(-1) sector, and names as an open interface the question of what an
interaction does.  This runner answers that question for one declared family,
the record-conserving nearest-neighbour law

    H(t, V) = -t sum_bonds eta_ij (c_i^dag c_j + c_j^dag c_i) + V sum_bonds n_i n_j,

read at t = 1 with the single ratio g = V/t, on the many-body ground state at
fixed particle number N -- not on a filled one-particle ladder.

  A  EXHAUSTIVE CUBE AT HALF FILLING.  Open 2x2x2 coarse cube, N = 4, the
     70-dimensional sector.  All 32 consistent flux sectors, every g on a
     declared list: the all-(-1) sector is the unique many-body minimiser.
     Exact over Z at twelve integer g by minimal polynomials of E_0 and a
     CRootOf comparison with no floating point anywhere.
  B  AWAY FROM HALF FILLING.  The same cube at N = 2 and N = 6.  Here the
     interaction DOES reorder: the two-flux class wins at every g and the
     uniform pair crosses at exactly g_c = 2 sqrt3.
  C  EXHAUSTIVE 2x2x3 BLOCK AT HALF FILLING.  N = 6, the 924-dimensional
     sector, all 512 consistent sectors, repulsive and attractive g.
  D  FIRST ORDER ON TORI.  First-order perturbation theory in V about the
     twist-minimised free half-filled sea on 4^3 ... 12^3.  The first-order
     coefficient also favours the staggered sector, exactly on 4^3.
  E  LARGE COUPLING.  Both sectors freeze to the same Neel doublet, the
     t^2/V exchange is sector-independent, and the whole surviving difference
     is a plaquette ring exchange at order t^4/V^3.

Group A's integer-g content, the whole of B's exact item and D's 4^3 item are
exact -- sympy charpolys of integer matrices, symbolic g, surds, CRootOf
comparison, F2/Z4 symplectic bit arithmetic, exhaustive enumeration.  Items
tagged [numerical] are floating-point statements at the stated tolerance.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
from collections import deque
from fractions import Fraction

import mpmath as mp
import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg as sparse_linalg
import sympy as sp

AUDIT_TIMEOUT_SEC = 180

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


# ================================================ coarse lattice and KS phases

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a); axes 0,1,2 = 1,2,3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def wrap(v, dims):
    return tuple(v[i] % dims[i] for i in range(3))


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

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def ismI(s):
        return s.x == 0 and s.z == 0 and s.k == 2

    def vec(s, n):
        return s.x | (s.z << n)


IDQ = Q(0, 0, 0)


def qprod(seq):
    o = IDQ
    for p in seq:
        o = o * p
    return o


class Lat:
    """Coarse cubic block or torus with the BK superfast encoding on its edges."""

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.per = periodic
        self.V = list(itertools.product(*(range(d) for d in dims)))
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
                d[r] = (w, self.ei[(v, r - 3) if r >= 3 else (w, r)])
            self.inc[v] = d
        self.star = {v: sum(1 << q for (_, q) in self.inc[v].values()) for v in self.V}
        self.idx = {v: i for i, v in enumerate(self.V)}
        self.rows = np.array([self.idx[self.step(v, EX[ax])] for (v, ax) in self.E])
        self.cols = np.array([self.idx[v] for (v, ax) in self.E])

    def step(self, v, d):
        w = va(v, d)
        if self.per:
            return wrap(w, self.dims)
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

    def loop(self, cyc):
        n = len(cyc)
        return qprod([self.Aij(cyc[a], cyc[(a + 1) % n]) for a in range(n)]).scal(n)

    def mat(self, s):
        """Real symmetric hopping matrix of the link-sign vector s (edge order)."""
        M = np.zeros((self.nv, self.nv))
        np.add.at(M, (self.rows, self.cols), np.asarray(s, dtype=float))
        return M + M.T

    def imat(self, s):
        """Integer hopping matrix of the link-sign vector s."""
        M = np.zeros((self.nv, self.nv), dtype=np.int64)
        np.add.at(M, (self.rows, self.cols), np.asarray(s, dtype=np.int64))
        return M + M.T


def transport(L, path):
    """Ordered product of the encoded hops T_{i_{k+1} i_k} = (i/2) A (B - B).

    On any configuration where every step is legal -- source occupied, target
    empty -- each factor contributes (i/2)(+1 - (-1)) = i, hence the i^n.
    """
    n = len(path) - 1
    ops = [L.Aij(path[k + 1], path[k]) for k in range(n)]
    return qprod(ops[::-1]).scal(n)


def f2_pivots(gens):
    piv = {}
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
    return piv


def f2_express(target, piv):
    v, c = target, 0
    while v:
        p = v.bit_length() - 1
        if p not in piv:
            return None
        pv, pc = piv[p]
        v ^= pv
        c ^= pc
    return c


def f2_relations(gens):
    piv, rel = {}, []
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
        if v == 0:
            rel.append(c)
    return rel, len(piv)


def bits(m):
    out = []
    while m:
        b = m & -m
        out.append(b.bit_length() - 1)
        m ^= b
    return out


def sector_eta(L, face_vals, wilson=(1, 1, 1)):
    """Link-sign field realising the flux sector S_f = face_vals[f] on Lat L.

    Spanning-tree gauge fixing, then fundamental-cycle transport with the
    residual Z4 phase read off, exactly as in the face-transport theorem;
    the face eigenvalues are supplied rather than fixed at -1.  Returns
    (eta, consistent); eta is None when the sector is inconsistent.
    """
    root = L.V[0]
    par = {root: None}
    dq = deque([root])
    while dq:
        v = dq.popleft()
        for r in range(6):
            if r not in L.inc[v]:
                continue
            w = L.inc[v][r][0]
            if w not in par:
                par[w] = v
                dq.append(w)
    tree = {frozenset((v, w)) for w, v in par.items() if v is not None}

    def tpath(v):
        p = [v]
        while par[p[-1]] is not None:
            p.append(par[p[-1]])
        return p[::-1]

    F = L.faces()
    gens = [L.loop(f) for f in F]
    vals = list(face_vals)
    if L.per:
        for ax in range(3):
            cyc = [wrap(tuple((k if i == ax else 0) for i in range(3)), L.dims)
                   for k in range(L.dims[ax])]
            gens.append(transport(L, cyc + [cyc[0]]))
        vals += list(wilson)
    gv = [g.vec(L.nq) for g in gens]
    piv = f2_pivots(gv)
    rels, _ = f2_relations(gv)
    for r in rels:
        idxs = bits(r)
        pr = qprod([gens[j] for j in idxs])
        eps = 1 if pr.isI() else (-1 if pr.ismI() else 0)
        pv = 1
        for j in idxs:
            pv *= vals[j]
        if eps == 0 or pv != eps:
            return None, False
    eta = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        if frozenset((v, w)) in tree:
            eta[(v, ax)] = 1
            continue
        op = transport(L, tpath(v) + [w] + tpath(w)[::-1][1:])
        c = f2_express(op.vec(L.nq), piv)
        if c is None:
            return None, False
        idxs = bits(c)
        resid = (op.k - qprod([gens[j] for j in idxs]).k) & 3
        if resid not in (0, 2):
            return None, False
        e = 1 if resid == 0 else -1
        for j in idxs:
            e *= vals[j]
        eta[(v, ax)] = e
    return eta, True


def hol_list(L, eta):
    """Plaquette holonomy of the sign field eta, one entry per face."""
    out = []
    for (v, a, c, b) in L.faces():
        pr = 1
        for (p, q) in ((v, a), (a, c), (b, c), (v, b)):
            for ax in range(3):
                if L.step(p, EX[ax]) == q and (p, ax) in eta:
                    pr *= eta[(p, ax)]
                    break
                if L.step(q, EX[ax]) == p and (q, ax) in eta:
                    pr *= eta[(q, ax)]
                    break
        out.append(pr)
    return out


def vec_of(L, eta):
    return np.array([eta[(v, ax)] for (v, ax) in L.E], dtype=float)



# ============================================ the record-conserving many-body law


def bond_list(L):
    """[(i, j, key)] site-index pairs and edge key for every coarse bond."""
    return [(L.idx[v], L.idx[L.step(v, EX[ax])], (v, ax)) for (v, ax) in L.E]


def basis(nv, N):
    """All nv-bit patterns with N bits set, sorted, plus the index map."""
    st = sorted(sum(1 << o for o in occ) for occ in itertools.combinations(range(nv), N))
    return st, {s: k for k, s in enumerate(st)}


def hop(state, i, j):
    """c_i^dag c_j |state>: returns (new state, Jordan-Wigner sign) or None."""
    if not (state >> j) & 1:
        return None
    s1 = bin(state & ((1 << j) - 1)).count("1")
    s = state ^ (1 << j)
    if (s >> i) & 1:
        return None
    s2 = bin(s & ((1 << i) - 1)).count("1")
    return (s | (1 << i)), (1 if (s1 + s2) % 2 == 0 else -1)


class Sector:
    """The N-particle record-number sector of one cluster, as sparse structure.

    `rows`, `cols`, `bidx`, `sgn` hold the hopping graph once; a link-sign
    vector and a coupling g then assemble H without re-walking the basis.
    """

    def __init__(self, L, N):
        self.L, self.N = L, N
        self.bl = bond_list(L)
        self.st, self.ix = basis(L.nv, N)
        self.D = len(self.st)
        rows, cols, bidx, sgn = [], [], [], []
        self.nn = np.zeros(self.D)
        self.occ = np.zeros((self.D, L.nv))
        for k, s in enumerate(self.st):
            for i in range(L.nv):
                self.occ[k, i] = (s >> i) & 1
            d = 0
            for bi, (i, j, key) in enumerate(self.bl):
                if ((s >> i) & 1) and ((s >> j) & 1):
                    d += 1
                for (a, b) in ((i, j), (j, i)):
                    r = hop(s, a, b)
                    if r is None:
                        continue
                    ns, sg = r
                    rows.append(self.ix[ns])
                    cols.append(k)
                    bidx.append(bi)
                    sgn.append(sg)
            self.nn[k] = d
        self.rows = np.array(rows)
        self.cols = np.array(cols)
        self.bidx = np.array(bidx)
        self.sgn = np.array(sgn, dtype=float)

    def vec(self, eta):
        """Link-sign vector in bond order from an eta dict."""
        return np.array([eta[key] for (_, _, key) in self.bl], dtype=float)

    def dense(self, v, g):
        H = np.zeros((self.D, self.D))
        np.add.at(H, (self.rows, self.cols), -v[self.bidx] * self.sgn)
        H[np.arange(self.D), np.arange(self.D)] += g * self.nn
        return H

    def idense(self, v, g):
        """Exact integer H, for integer link signs and integer g."""
        H = np.zeros((self.D, self.D), dtype=np.int64)
        np.add.at(H, (self.rows, self.cols),
                  -np.asarray(v, dtype=np.int64)[self.bidx] * self.sgn.astype(np.int64))
        H[np.arange(self.D), np.arange(self.D)] += int(g) * self.nn.astype(np.int64)
        return H

    def sym(self, v, gsym):
        """Exact sympy H with a symbolic coupling."""
        H = sp.zeros(self.D, self.D)
        for r, c, b, s in zip(self.rows, self.cols, self.bidx, self.sgn):
            H[int(r), int(c)] += -int(v[b]) * int(s)
        for k in range(self.D):
            H[k, k] += gsym * int(self.nn[k])
        return H

    def sp(self, v, g):
        M = sparse.coo_matrix((-v[self.bidx] * self.sgn, (self.rows, self.cols)),
                              shape=(self.D, self.D)).tocsr()
        return (M + sparse.diags(g * self.nn)).tocsr()

    def low(self, v, g, k=3, tol=1e-12):
        """The k lowest levels; Lanczos when it pays, dense otherwise."""
        if self.D <= 200:
            return np.linalg.eigvalsh(self.dense(v, g))[:k]
        w = sparse_linalg.eigsh(self.sp(v, g), k=k, which="SA", tol=tol,
                                return_eigenvectors=False)
        return np.sort(w)


def sectors_of(L):
    """Every consistent flux sector of L as (face values, link vector, flux count)."""
    F = L.faces()
    out = []
    for fv in itertools.product([1, -1], repeat=len(F)):
        eta, ok = sector_eta(L, fv)
        if ok:
            out.append((fv, eta, sum(1 for x in fv if x == -1)))
    return out


# =============================================== group A: exhaustive cube, N = 4

X = sp.Symbol("x")
GSYM = sp.Symbol("g")

CUBE = Lat((2, 2, 2), False)
CSECT = sectors_of(CUBE)
CFLUX = sorted({s[2] for s in CSECT})
IM = [k for k, s in enumerate(CSECT) if all(x == -1 for x in s[0])][0]
IP = [k for k, s in enumerate(CSECT) if all(x == 1 for x in s[0])][0]
HOL_OK = all(list(hol_list(CUBE, e)) == list(fv) for (fv, e, _) in CSECT)
_, CRANK = f2_relations([CUBE.loop(f).vec(CUBE.nq) for f in CUBE.faces()])
check(
    "A1 [exact] open 2x2x2 cube, 6 faces of F2 rank %d: exactly %d of 64 face assignments are consistent "
    "sectors, flux counts %s, each realised by a link field of that holonomy" % (CRANK, len(CSECT), "/".join(str(c) for c in CFLUX)),
    len(CSECT) == 32 and CRANK == 5 and CFLUX == [0, 2, 4, 6] and HOL_OK,
)

S4 = Sector(CUBE, 4)
CVEC = [S4.vec(e) for (_, e, _) in CSECT]
GA = [-2, -1, -0.5, 0, 0.5, 1, 2, 4, 8]
AROW = []
for g in GA:
    E0 = np.array([S4.low(v, float(g), k=1)[0] for v in CVEC])
    o = np.argsort(E0)
    emin = E0[o[0]]
    nmin = int(np.sum(E0 < emin + 1e-10))
    AROW.append((g, emin, nmin, int(o[0]), E0[o][nmin] - emin, E0[IM] - E0[IP]))
print("   A2 cube N=4, g:margin of all-(-1) to the next sector -- "
      + " ".join("%g:%.3f" % (r[0], r[4]) for r in AROW))
AUNIQ = all(r[2] == 1 and r[3] == IM for r in AROW)
check(
    "A2 [numerical, 1e-10] cube N = 4 (70-dim), H(g) = -sum eta_ij (c^dag c + h.c.) + g sum n_i n_j: all-(-1) "
    "is the UNIQUE minimiser of all 32 at each g above",
    AUNIQ and all(r[5] < -1e-9 for r in AROW),
)

GZ = [-8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 32, 64]
MINPOLY, EXROOT = {}, {}
for lab, si in (("+", IP), ("-", IM)):
    v = np.rint(CVEC[si]).astype(np.int64)
    for g in GZ:
        H = S4.idense(v, g)
        poly = sp.Poly(sp.Matrix(H.tolist()).charpoly(X).as_expr(), X)
        roots = sp.real_roots(poly)
        e0 = min(roots)
        EXROOT[(lab, g)] = e0
        MINPOLY[(lab, g)] = sp.Poly(sp.minimal_polynomial(e0, X), X)
print("   A3 min poly of E_0 over Z, plain g=2: %s ; staggered g=0: %s"
      % (MINPOLY[("+", 2)].as_expr(), MINPOLY[("-", 0)].as_expr()))
print("     deg +: " + "".join(str(MINPOLY[("+", g)].degree()) for g in GZ)
      + " deg -: " + "".join(str(MINPOLY[("-", g)].degree()) for g in GZ)
      + " at g = " + ",".join(str(g) for g in GZ))
check(
    "A3 [exact, sympy over Z] the 70x70 integer characteristic polynomials at those twelve g give minimal "
    "polynomials of E_0 over Z for both uniform sectors, degrees above",
    MINPOLY[("+", 2)].as_expr() == X ** 3 - 10 * X ** 2 - 16 * X + 48
    and MINPOLY[("-", 0)].as_expr() == X ** 2 - 48
    and all(MINPOLY[(l, g)].domain == sp.ZZ for l in "+-" for g in GZ),
)

LT = [bool(EXROOT[("-", g)] < EXROOT[("+", g)]) for g in GZ]
EQ = [bool(sp.Eq(EXROOT[("-", g)], EXROOT[("+", g)])) for g in GZ]
check(
    "A4 [exact, CRootOf comparison, no floating point] E_0(-) < E_0(+) strictly at all %d, 0 ties: the "
    "ordering is exact over Z, not a tolerance" % sum(LT),
    all(LT) and not any(EQ),
)


# ========================================= group B: the cube away from half filling

BROW = {}
for N in (2, 6):
    S = Sector(CUBE, N)
    vv = [S.vec(e) for (_, e, _) in CSECT]
    rows = []
    for g in GA:
        E0 = np.array([S.low(v, float(g), k=1)[0] for v in vv])
        o = np.argsort(E0)
        emin = E0[o[0]]
        nmin = int(np.sum(E0 < emin + 1e-10))
        fl = sorted({CSECT[k][2] for k in np.where(E0 < emin + 1e-10)[0]})
        rows.append((g, nmin, fl, int(np.where(o == IM)[0][0]), E0[IM] - E0[IP]))
    BROW[N] = rows
print("   B1 cube N=2, g:minimiser flux class/rank of all-(-1) of 32 -- "
      + " ".join("%g:%d/%d" % (r[0], r[2][0], r[3]) for r in BROW[2]))
BOK = all(r[1] == 3 and r[2] == [2] and r[3] > 0 for N in (2, 6) for r in BROW[N])
check(
    "B1 [numerical, 1e-10] the same cube off half filling, N = 2 and N = 6 (28-dim): the minimiser is the "
    "two-flux class (3 tied) at every g above, never all-(-1)",
    BOK,
)

S2 = Sector(CUBE, 2)
FACP = sp.factor_list(S2.sym(np.rint(CVEC[IP]).astype(int), GSYM).charpoly(X).as_expr(), X)[1]
FACM = sp.factor_list(S2.sym(np.rint(CVEC[IM]).astype(int), GSYM).charpoly(X).as_expr(), X)[1]
PSET = {sp.expand(f.as_expr() if isinstance(f, sp.Poly) else f) for f, _ in FACP}
MSET = {sp.expand(f.as_expr() if isinstance(f, sp.Poly) else f) for f, _ in FACM}
PLAIN_CUBIC = X ** 3 - GSYM * X ** 2 - 16 * X + 8 * GSYM
E0M = -2 * sp.sqrt(3)
E0P = min(r for r in sp.real_roots(sp.Poly(PLAIN_CUBIC.subs(GSYM, 0), X)))
CROSS = sp.solve(sp.Eq(PLAIN_CUBIC.subs(X, E0M), 0), GSYM)
print("   B2 cube N=2 charpoly factors -- plain %s ; staggered %s"
      % (PLAIN_CUBIC, X ** 2 - 12))
check(
    "B2 [exact, sympy, symbolic g] cube N = 2: the staggered factor x^2 - 12 is g-free, so E_0(-) = -2 sqrt3 at "
    "EVERY g and the pair crosses exactly at g_c = 2 sqrt3",
    (X ** 2 - 12) in MSET and PLAIN_CUBIC in PSET and CROSS == [2 * sp.sqrt(3)]
    and bool(E0P < E0M),
)


# ========================================= group C: the exhaustive 2x2x3 block

BLK = Lat((2, 2, 3), False)
BSECT = sectors_of(BLK)
_, BRANK = f2_relations([BLK.loop(f).vec(BLK.nq) for f in BLK.faces()])
S6 = Sector(BLK, 6)
BVEC = [S6.vec(e) for (_, e, _) in BSECT]
JM = [k for k, s in enumerate(BSECT) if all(x == -1 for x in s[0])][0]
JP = [k for k, s in enumerate(BSECT) if all(x == 1 for x in s[0])][0]
check(
    "C1 [exact] open 2x2x3 block, 12 sites, 20 bonds, %d faces of F2 rank %d: exactly %d of %d assignments are "
    "consistent sectors; the N = 6 sector has dimension %d"
    % (len(BLK.faces()), BRANK, len(BSECT), 2 ** len(BLK.faces()), S6.D),
    len(BLK.faces()) == 11 and BRANK == 9 and len(BSECT) == 512 and S6.D == 924,
)


def scan(g):
    """E_0 of all 512 sectors at coupling g, plus the two uniform gaps."""
    E0 = np.empty(len(BSECT))
    for k, v in enumerate(BVEC):
        E0[k] = sparse_linalg.eigsh(S6.sp(v, g), k=1, which="SA", tol=1e-12,
                                    return_eigenvectors=False)[0]
    o = np.argsort(E0)
    emin = E0[o[0]]
    nmin = int(np.sum(E0 < emin + 1e-9))
    return dict(
        g=g, E0=E0, emin=emin, nmin=nmin, arg=int(o[0]),
        margin=float(E0[o][nmin] - emin) if nmin < len(E0) else float("nan"),
        minflux=sorted({BSECT[k][2] for k in np.where(E0 < emin + 1e-9)[0]}),
        rank_m=int(np.where(o == JM)[0][0]), rank_p=int(np.where(o == JP)[0][0]),
        dE=float(E0[JM] - E0[JP]),
        deg_m=int(np.sum(S6.low(BVEC[JM], g, k=3) < E0[JM] + 1e-9)),
        deg_p=int(np.sum(S6.low(BVEC[JP], g, k=3) < E0[JP] + 1e-9)),
    )


GC = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
CR = [scan(g) for g in GC]
print("   C2 2x2x3 N=6, 512 sectors, g:margin/plain rank/degeneracies -- "
      + " ".join("%g:%.3g/%d/%d/%d" % (r["g"], r["margin"], r["rank_p"], r["deg_m"], r["deg_p"])
                 for r in CR))
check(
    "C2 [numerical, 1e-9] 2x2x3, N = 6 (924-dim), all 512 sectors: all-(-1) is the UNIQUE minimiser at every g "
    "above, non-degenerate, the plain sector 2-fold throughout",
    all(r["nmin"] == 1 and r["arg"] == JM and r["dE"] < -1e-9 and r["deg_m"] == 1 and r["deg_p"] == 2
        for r in CR),
)

GN = [-1.0, -2.0, -2.3, -2.4]
CN = [scan(g) for g in GN]
print("   C3 attractive, g:tied minimisers/flux count/rank of all-(-1) -- "
      + " ".join("%g:%d/%d/%d" % (r["g"], r["nmin"], r["minflux"][0], r["rank_m"]) for r in CN))
FLIP = [r for r in CN if not (r["nmin"] == 1 and r["arg"] == JM)]
check(
    "C3 [numerical, 1e-9] attractive side (above): all-(-1) is still unique at g = -1, -2, -2.3, but at -2.4 "
    "an 8-flux class of %d tied sectors takes over -- flip window -2.4 < g_c < -2.3" % CN[-1]["nmin"],
    all(r["nmin"] == 1 and r["arg"] == JM for r in CN[:3])
    and CN[-1]["nmin"] == 8 and CN[-1]["minflux"] == [8] and CN[-1]["rank_m"] > 0,
)

GW = [-64.0, -32.0, -16.0, -8.0, -4.0, -2.0, -1.0, 0.0, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
WPAIR = [(g, float(S6.low(BVEC[JM], g, k=1)[0] - S6.low(BVEC[JP], g, k=1)[0])) for g in GW]
check(
    "C4 [numerical, 1e-9] the uniform PAIR never crosses on [-64, 64]: E_0(-) - E_0(+) < 0 at all %d couplings "
    "there, largest %.2e -- the -2.4 flip is a third sector passing both" % (len(GW), max(d for _, d in WPAIR)),
    all(d < -1e-9 for _, d in WPAIR),
)


# ================================= group D: first order in V on the coarse tori


def twisted(L, kind, tw):
    """Link-sign field of a uniform sector with the three Wilson twists tw."""
    eta = {}
    for (v, ax) in L.E:
        e = 1 if kind == "+" else eta_ks(v, ax)
        if v[ax] == L.dims[ax] - 1:
            e *= tw[ax]
        eta[(v, ax)] = e
    return eta


def sea(L, eta):
    """Twist-minimised free half-filled sea: energy, closed-shell gap, A."""
    w, C = np.linalg.eigh(-L.mat(vec_of(L, eta)))
    Nh = L.nv // 2
    P = C[:, :Nh] @ C[:, :Nh].T
    A = float(sum(P[i, i] * P[j, j] - P[i, j] ** 2 for (i, j, _) in bond_list(L)))
    return float(np.sum(w[:Nh])), float(w[Nh] - w[Nh - 1]), A, P


DROW = {}
for Lz in (4, 6, 8, 10, 12):
    T = Lat((Lz, Lz, Lz), True)
    for kind in ("+", "-"):
        best = None
        for tw in itertools.product([1, -1], repeat=3):
            r = sea(T, twisted(T, kind, tw))
            if best is None or r[0] < best[0] - 1e-11:
                best = r + (tw,)
        DROW[(Lz, kind)] = best
LS = (4, 6, 8, 10, 12)
print("   D1 tori L = 4, 6, 8, 10, 12; e_free/V: "
      + " ".join("%.4f/%.4f" % (DROW[(L, "+")][0] / L ** 3, DROW[(L, "-")][0] / L ** 3) for L in LS))
print("      gap: " + " ".join("%.2f/%.2f" % (DROW[(L, "+")][1], DROW[(L, "-")][1]) for L in LS)
      + " ; A/V: " + " ".join("%.5f/%.5f" % (DROW[(L, "+")][2] / L ** 3, DROW[(L, "-")][2] / L ** 3)
                              for L in LS))
DGC = {}
for Lz in (4, 6, 8, 10, 12):
    V = Lz ** 3
    de = (DROW[(Lz, "-")][0] - DROW[(Lz, "+")][0]) / V
    da = (DROW[(Lz, "-")][2] - DROW[(Lz, "+")][2]) / V
    DGC[Lz] = (de, da, -de / da)
check(
    "D1 [numerical, 1e-9] first order in V about the twist-minimised free sea, tori 4^3 ... 12^3, A = sum_bonds "
    "(P_ii P_jj - P_ij^2) by Wick (above): A/V is SMALLER in the staggered sector at every L",
    all(DGC[L][1] < -1e-12 and DGC[L][0] < -1e-12 for L in DGC)
    and all(DROW[(L, k)][1] > 1e-6 for L in (4, 6, 8, 10, 12) for k in "+-"),
)

T4 = Lat((4, 4, 4), True)
M4P = T4.imat(vec_of(T4, twisted(T4, "+", (-1, -1, -1))))
M4M = T4.imat(vec_of(T4, twisted(T4, "-", (-1, -1, -1))))
I64 = np.eye(64, dtype=np.int64)
P2 = M4P @ M4P
P3 = P2 @ M4P
P4 = P2 @ P2
CERT_P = np.array_equal(P4 @ P2 - 52 * P4 + 676 * P2, 1152 * I64)
CERT_M = np.array_equal(M4M @ M4M, 6 * I64)
# X = (13 M - M^3 / 2) / (12 sqrt2) squares to the identity above, so
# P = (I + X)/2 is the exact occupied projector; every P_ij^2 is rational.
A2, AB2, B2 = Fraction(169, 288), Fraction(-13, 288), Fraction(1, 1152)
AEX = {"+": Fraction(0), "-": Fraction(0)}
for (i, j, _) in bond_list(T4):
    mp_, m3 = int(M4P[i, j]), int(P3[i, j])
    AEX["+"] += Fraction(1, 4) - (A2 * mp_ * mp_ + AB2 * mp_ * m3 + B2 * m3 * m3) / 4
    AEX["-"] += Fraction(1, 4) - Fraction(int(M4M[i, j]) ** 2, 24)
DIAG_OK = all(P3[i, i] == 0 for i in range(64)) and all(M4P[i, i] == 0 for i in range(64))
R2, R6 = sp.sqrt(2), sp.sqrt(6)
DEEX = sp.simplify(48 * R2 - 32 * R6)
GCEX = sp.simplify(-DEEX / sp.Rational(AEX["-"] - AEX["+"]))
print("   D2 4^3 exact: A(+) = %s = %s/site, A(-) = %s = %s/site, dE_free = %s, g_c = %s"
      % (AEX["+"], Fraction(AEX["+"], 64), AEX["-"], Fraction(AEX["-"], 64), DEEX, GCEX))
check(
    "D2 [exact, integer certificates + surds] on 4^3 at the optimal twist M^6 - 52 M^4 + 676 M^2 = 1152 I and "
    "M^2 = 6 I, so both projectors are polynomials in M with rational squared entries: the values above are "
    "exact",
    CERT_P and CERT_M and DIAG_OK and AEX["+"] == 42 and AEX["-"] == 40
    and GCEX == 24 * R2 - 16 * R6 and abs(float(GCEX) - DGC[4][2]) < 1e-9,
)

QUAD = []
for Mg in (200, 400, 800):
    v = np.cos(2 * np.pi * (np.arange(Mg) + 0.5) / Mg)
    S2 = v[:, None] + v[None, :]
    ep = cp = em = cm = 0.0
    for i in range(Mg):
        s = v[i] + S2
        occ = s < 0
        ep += float(np.sum(np.abs(2 * s)))
        cp += float(np.sum(np.where(occ, v[i], 0.0)))
        rt = np.sqrt(np.maximum(6 + 2 * s, 0.0))
        em += float(np.sum(rt))
        cm += float(np.sum((1 + v[i]) / np.maximum(rt, 1e-300)))
    n = Mg ** 3
    QUAD.append((Mg, -ep / (2 * n), cp / n, -em / (2 * n), cm / (2 * n)))
_, EPI, CPI, EMI, CMI = QUAD[-1]
API, AMI = 0.75 - 3 * CPI ** 2, 0.75 - 3 * CMI ** 2
GCI = -(EMI - EPI) / (AMI - API)
print("   D3 BZ quadrature M=%d: e/V = %.8f, %.8f; A/V = %.6f, %.6f; g_c = %.4f"
      % (QUAD[-1][0], EPI, EMI, API, AMI, GCI))
check(
    "D3 [numerical, converged quadrature] the closed forms P_ij = <cos q_1>_occ and P_ij = +-(h(0) + h(2e_1))/2 "
    "with h = (6 + W)^(-1/2) give the limiting A/V above: one crossing, attractive",
    abs(API - 0.66626) < 3e-4 and abs(AMI - 0.6312) < 3e-4 and AMI < API
    and -5.6 < GCI < -5.3 and abs(QUAD[1][4] - QUAD[2][4]) < 1e-5,
)

W4 = np.zeros((64, 64))
for (i, j, _) in bond_list(T4):
    W4[i, j] = W4[j, i] = 1.0
C2 = {}
for kind in ("+", "-"):
    w, C = np.linalg.eigh(-T4.mat(vec_of(T4, twisted(T4, kind, (-1, -1, -1)))))
    No = 32
    Y = np.einsum("mi,ma->iam", C[:, :No], C[:, No:])
    Yf = Y.reshape(No * (64 - No), 64)
    Mm = (Yf @ W4 @ Yf.T).reshape(No, 64 - No, No, 64 - No)
    anti = Mm - np.transpose(Mm, (0, 3, 2, 1))
    eo, ev = w[:No], w[No:]
    den = (eo[:, None, None, None] - ev[None, :, None, None]
           + eo[None, None, :, None] - ev[None, None, None, :])
    C2[kind] = 0.25 * float(np.sum(anti ** 2 / den))
QA = C2["-"] - C2["+"]
QB = float(AEX["-"] - AEX["+"])
QC = float(DEEX)
DISC = QB * QB - 4 * QA * QC
ROOTS = sorted([(-QB + np.sqrt(DISC)) / (2 * QA), (-QB - np.sqrt(DISC)) / (2 * QA)])
print("   D4 4^3 MBPT2 dE(g) = %+.5f %+.5f g %+.5f g^2, roots %.4f and %.4f"
      % (QC, QB, QA, ROOTS[0], ROOTS[1]))
check(
    "D4 [numerical, caution only] the MBPT2 truncation above has a positive root g = %.2f predicting a "
    "repulsive flip; REFUTED by the exact cube (A3, A4) and the 2x2x3 block (C2)" % ROOTS[1],
    QA > 0 and 7.0 < ROOTS[1] < 8.2 and ROOTS[0] < 0,
)


# ======================================== group E: the large-coupling structure


def order(S, L, v, g, tol=1e-9):
    """Degeneracy-averaged density, staggered moment and Neel weight."""
    w, U = np.linalg.eigh(S.dense(v, g))
    d = int(np.sum(w < w[0] + tol))
    diag = np.sum(U[:, :d] ** 2, axis=1) / d
    n = diag @ S.occ
    sgn3 = np.array([1 - 2 * ((x + y + z) & 1) for (x, y, z) in L.V], dtype=float)
    mvec = (S.occ - 0.5) @ sgn3 / L.nv
    neel = float(np.sum(diag[np.abs(np.abs(mvec) - 0.5) < 1e-12]))
    return w[0], d, float(n.min()), float(n.max()), float(diag @ mvec ** 2), neel


GE = [4.0, 8.0, 16.0, 32.0]
EROW = {}
for lab, si in (("+", IP), ("-", IM)):
    for g in GE:
        EROW[(lab, g)] = order(S4, CUBE, CVEC[si], g)
print("   E1 cube N=4, g: m^2 then Neel weight, (+,-) each, against 1/4 and 1 -- "
      + " | ".join("%g: %.4f %.4f %.4f %.4f"
                   % (g, EROW[("+", g)][4], EROW[("-", g)][4],
                      EROW[("+", g)][5], EROW[("-", g)][5]) for g in GE))
BROWE = {}
for lab, si in (("+", JP), ("-", JM)):
    for g in GE:
        BROWE[(lab, g)] = order(S6, BLK, BVEC[si], g)
check(
    "E1 [numerical, 1e-9] both sectors freeze into the SAME Neel doublet (above): <n_i> = 1/2 on every cube "
    "site in both to %.0e, m^2 and the Neel weight rising together, here and on 2x2x3"
    % max(max(abs(r[2] - 0.5), abs(r[3] - 0.5)) for r in EROW.values()),
    all(abs(r[2] - 0.5) < 1e-9 and abs(r[3] - 0.5) < 1e-9 for r in EROW.values())
    and all(EROW[(l, 32.0)][4] > 0.2494 and EROW[(l, 32.0)][5] > 0.996 for l in "+-")
    and all(BROWE[(l, 32.0)][4] > 0.2494 for l in "+-")
    and all(EROW[(l, g)][4] < EROW[(l, h)][4] for l in "+-" for g, h in zip(GE, GE[1:]))
    and all(BROWE[(l, g)][4] < BROWE[(l, h)][4] for l in "+-" for g, h in zip(GE, GE[1:])),
)

GT = [64.0, 128.0, 256.0]
TROW = []
for g in GT:
    ep = float(S4.low(CVEC[IP], g, k=1)[0])
    em = float(S4.low(CVEC[IM], g, k=1)[0])
    TROW.append((g, g * ep, g * em, g * g * (em - ep)))
print("   E2 cube, g: g E_0 (+,-) then g^2 dE -- "
      + " | ".join("%g: %.4f %.4f %.4f" % r for r in TROW))
check(
    "E2 [numerical, converged in 1/g] the t^2/V exchange is sector-INDEPENDENT (above): g E_0 -> -6 in both "
    "sectors, g^2 (E_0(-) - E_0(+)) -> 0",
    all(abs(r[1] + 6) < 0.01 and abs(r[2] + 6) < 0.01 for r in TROW)
    and abs(TROW[-1][3]) < abs(TROW[0][3]) < 1.0 and abs(TROW[-1][3]) < 0.25,
)

mp.mp.dps = 60
IVP = np.rint(CVEC[IP]).astype(np.int64)
IVM = np.rint(CVEC[IM]).astype(np.int64)


def e0_mp(v, g):
    return min(mp.eigsy(mp.matrix(S4.idense(v, g).tolist()), eigvals_only=True))


GH = [64, 128, 256, 512]
HR = [(g, (e0_mp(IVM, g) - e0_mp(IVP, g)) * g ** 3) for g in GH]
EXPO = [float(mp.log(HR[k][1] / HR[k + 1][1]) / mp.log(2)) + 3 for k in range(len(HR) - 1)]
AMAT = mp.matrix([[mp.mpf(1), mp.mpf(1) / g ** 2, mp.mpf(1) / g ** 3, mp.mpf(1) / g ** 4] for g in GH])
C3 = mp.lu_solve(AMAT, mp.matrix([r[1] for r in HR]))[0]
print("   E3 cube g^3 dE: " + " ".join("%d:%s" % (g, mp.nstr(s, 12)) for g, s in HR)
      + "; exponents " + " ".join("%.5f" % e for e in EXPO)
      + "; Richardson limit " + mp.nstr(C3, 12))
check(
    "E3 [numerical, mpmath 60 digits] the surviving difference is order t^4/V^3 (above): E_0(-) - E_0(+) = "
    "-27 t^4/V^3 on the cube -- a ring exchange of 9/4 a face carrying the sign S_f",
    all(s < 0 for _, s in HR) and abs(EXPO[-1] - 3) < 2e-3
    and abs(float(C3) + 27) < 1e-6 and abs(float(HR[-1][1]) + 27) < 1e-3,
)

GB = [16.0, 32.0, 64.0, 128.0, 256.0]
BR = [(g, g ** 3 * float(S6.low(BVEC[JM], g, k=1)[0] - S6.low(BVEC[JP], g, k=1)[0])) for g in GB]
print("   E4 2x2x3 g^3 dE: " + " ".join("%g:%.5f" % r for r in BR))
check(
    "E4 [numerical, converged in 1/g] the same ring exchange on 2x2x3 with its own coefficient (above), near "
    "%.4f ~ -320/27: that number is cluster data, its SIGN is what is shared" % BR[-1][1],
    all(s < 0 for _, s in BR) and abs(BR[-1][1] + 320 / 27) < 5e-3
    and abs(BR[-1][1] - BR[-2][1]) < abs(BR[1][1] - BR[0][1]),
)

print(
    "SUMMARY: with this interaction present the staggered sector stays the unique many-body ground sector at "
    "half filling on both exhaustive clusters at every repulsive coupling tested, the last difference to "
    "survive being a ring exchange that prefers the minus sign."
)
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
