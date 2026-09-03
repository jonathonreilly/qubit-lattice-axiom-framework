#!/usr/bin/env python3
"""The vacuum question is one coefficient of the law.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3, one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding
written on it.  The law declared by the existence note carries B_i -- the
product of the Z's on the edges incident to a coarse site -- as a term type
with no coefficient attached.  Give it one: add

    -J_B sum_i B_i

to the free nearest-neighbour hopping and ask what the ground state is as a
function of the single dimensionless number J_B/t.

  A  OCCUPANCY TERM.  Exact Pauli-string arithmetic: sum_i B_i commutes with
     every hop T_ij while a single B_i does not, and (V I - sum_i B_i)/2 is
     the number operator.  So -J_B sum_i B_i = -J_B V + 2 J_B N is a pure
     chemical potential of 2 J_B per fermion and nothing else.
  B  J_B = 0.  Every cluster here is bipartite with all degrees 6, so its
     spectrum is symmetric about 0 and min_N E_N = E_{V/2} for every
     link-sign field.  The global minimum over sectors and record numbers is
     the half-filled staggered sea: exhaustively on the 2x2x2 cube, by the
     Cauchy-Schwarz certificate on the 4^3 torus, by search elsewhere.
  C  W(J_B).  The ground state as a function of J_B, twist-minimised at each
     J_B; the crossover J_B* where the plain sector overtakes the staggered
     one; the emptying thresholds |eps_min|/2.
  D  EXTENDED CERTIFICATE.  W(J) >= min_m [-sqrt(3 V m) + 2 J m] for ANY
     link-sign field, and the 4^3 flat-twist staggered sea attains it for
     every J_B <= sqrt(3/8).
  E  HALF FILLING.  How long exactly half filling survives, and the gapless
     thermodynamic limit where it survives only at J_B = 0.
  F  LIMIT.  Bloch quadrature: the tables, J_B* and the thresholds at L=224.

Group A is exact symplectic/dense Pauli arithmetic, the surd statements of
B, C and D are exact in sympy, and the items tagged [numerical] are
floating-point at the stated tolerance.  The global-minimum statements are
theorems on the cube (exhaustion) and on 4^3 (certificate); elsewhere they
are search results and are labelled so.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
import time
from collections import deque

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

PASS = 0
FAIL = 0
T0 = time.time()


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# =========================================== coarse lattice and the encoding

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


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)


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


def sgn(p, q):
    """+1 if the two Pauli strings commute, -1 if they anticommute."""
    return -1 if ((pcnt(p.x & q.z) + pcnt(p.z & q.x)) & 1) else 1


class Lat:
    """Coarse cubic block or torus with the BK superfast encoding on its edges."""

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.per = periodic
        self.V = [v for v in itertools.product(*(range(d) for d in dims))]
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

    def B(self, v):
        return Q(0, 0, self.star[v])

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


def transport(L, path):
    """Ordered product of the encoded hops T_{i_{k+1} i_k} along a path."""
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
    """Link-sign field realising the flux sector S_f = face_vals[f], or None."""
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
        pr = qprod([gens[j] for j in idxs])
        resid = (op.k - pr.k) & 3
        if resid not in (0, 2):
            return None, False
        e = 1 if resid == 0 else -1
        for j in idxs:
            e *= vals[j]
        eta[(v, ax)] = e
    return eta, True


def holonomies(L, eta):
    out = set()
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
        out.add(pr)
    return out


def one_particle(L, eta):
    idx = {v: i for i, v in enumerate(L.V)}
    M = np.zeros((L.nv, L.nv))
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        M[idx[w], idx[v]] += eta[(v, ax)]
        M[idx[v], idx[w]] += eta[(v, ax)]
    return M


def levels(L, eta):
    return np.sort(np.linalg.eigvalsh(one_particle(L, eta)))


# ------------------------------------------------------ the energy functional
#
# With the occupancy term the total ground-state energy at record number N is
# E_N - J_B (V - 2N), so relative to the empty vacuum -J_B V it is
#     W(J_B) = min_N [ E_N + 2 J_B N ] = sum over levels eps < -2 J_B of
#              (eps + 2 J_B).

def Wm(ev, J):
    """W(J) and the record number attaining it; 1e-9 guards the eigensolver noise."""
    ev = np.sort(np.asarray(ev))
    m = int(np.searchsorted(ev, -2.0 * J - 1e-9, "left"))
    return float(np.sum(ev[:m]) + 2.0 * J * m), m


TOL = 1e-9
S2, S3, S6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)

print("=" * 62)
print("A  THE OCCUPANCY TERM IS A PURE CHEMICAL POTENTIAL [exact]")
print("=" * 62)

sq_ok = comm_ok = True
wrong = 0
bsq = 0
pairs = 0
for dims, per in (((2, 2, 2), False), ((3, 3, 3), False), ((3, 3, 3), True), ((4, 4, 4), True)):
    L = Lat(dims, per)
    Bs = {v: L.B(v) for v in L.V}
    sq_ok &= all((Bs[v] * Bs[v]).isI() for v in L.V)
    comm_ok &= all(sgn(Bs[u], Bs[v]) == 1 for u in L.V for v in L.V)
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        A = L.Aij(v, w)
        for k in L.V:
            pairs += 1
            if sgn(Bs[k], A) != (-1 if k in (v, w) else 1):
                wrong += 1
        if not (Bs[v] * Bs[v] == Bs[w] * Bs[w]):
            bsq += 1
print("  clusters: open 2x2x2, open 3x3x3, torus 3^3, torus 4^3")
check("A1 B_i^2 = I and all B_i mutually commute on all four clusters", sq_ok and comm_ok)
check("A2 A_ij anticommutes with exactly B_i, B_j: %d wrong of %d (hop, site) pairs" % (wrong, pairs),
      wrong == 0 and pairs == 16029)
check("A3 [sum_k B_k, T_ij] = -i (B_i^2 - B_j^2) A_ij = 0: %d failures" % bsq,
      bsq == 0)

Ld = Lat((2, 2, 1), False)
n = Ld.nq


def dense(p):
    M = np.array([[1.0 + 0j]])
    for b in range(n):
        m = np.eye(2, dtype=complex)
        if (p.x >> b) & 1:
            m = m @ SX
        if (p.z >> b) & 1:
            m = m @ SZ
        M = np.kron(m, M)
    return (1j ** p.k) * M


SB = sum(dense(Ld.B(v)) for v in Ld.V)
tot, ind, herm = 0.0, 0.0, True
for (v, ax) in Ld.E:
    w = Ld.step(v, EX[ax])
    A, Bv, Bw = dense(Ld.Aij(v, w)), dense(Ld.B(v)), dense(Ld.B(w))
    T = 0.5j * (A @ (Bv - Bw))
    herm &= bool(np.allclose(T, T.conj().T))
    tot = max(tot, float(np.max(np.abs(SB @ T - T @ SB))))
    ind = max(ind, float(np.max(np.abs(Bv @ T - T @ Bv))))
Nop = (Ld.nv * np.eye(2 ** n) - SB) / 2.0
nspec = np.round(np.linalg.eigvalsh(Nop), 12)
print("  dense 16-dim block: ||[sum B, T]|| = %.2e, ||[B_i, T]|| = %.2e" % (tot, ind))
check("A4 sum_i B_i commutes with every hop; a single B_i does not (norm 2)",
      tot == 0.0 and abs(ind - 2.0) < 1e-12 and herm)
check("A5 (V I - sum_i B_i)/2 = N, integer spectrum in [0, V]: %s"
      % ",".join("%g" % x for x in sorted(set(nspec.tolist()))),
      np.all(np.abs(nspec - np.round(nspec)) < 1e-12) and nspec.min() >= -1e-12
      and nspec.max() <= Ld.nv + 1e-12)
print("  so -J_B sum_i B_i = -J_B V + 2 J_B N: 2 J_B per fermion, nothing else")

print()
print("=" * 62)
print("B  AT J_B = 0: THE HALF-FILLED STAGGERED SEA")
print("=" * 62)

DATA = {}


def twisted(dims):
    L = Lat(dims, True)
    cuts = [np.array([1.0 if not (a == ax and v[ax] == dims[ax] - 1) else -1.0
                      for (v, a) in L.E]) for ax in range(3)]
    ks = np.array([eta_ks(v, ax) for (v, ax) in L.E], float)
    assert holonomies(L, {e: int(s) for e, s in zip(L.E, ks)}) == {-1}
    assert holonomies(L, {e: 1 for e in L.E}) == {1}
    idx = {v: i for i, v in enumerate(L.V)}

    def mat(s):
        M = np.zeros((L.nv, L.nv))
        for k, (v, ax) in enumerate(L.E):
            w = L.step(v, EX[ax])
            M[idx[w], idx[v]] += s[k]
            M[idx[v], idx[w]] += s[k]
        return M

    res = {}
    for tag, base in (("plain", np.ones(L.nq)), ("stag", ks)):
        for tw in itertools.product([0, 1], repeat=3):
            s = base.copy()
            for ax in range(3):
                if tw[ax]:
                    s = s * cuts[ax]
            res[(tag, tw)] = np.sort(np.linalg.eigvalsh(mat(s)))
    return L, res, mat


for dims in ((4, 4, 4), (6, 6, 6), (8, 8, 8)):
    L, res, mt = twisted(dims)
    DATA["t%d" % dims[0]] = res
    if dims[0] == 4:
        L4, mat4 = L, mt

L3 = Lat((3, 3, 3), False)
DATA["o333"] = {("plain", ()): levels(L3, {e: 1 for e in L3.E}),
                ("stag", ()): levels(L3, {(v, a): eta_ks(v, a) for (v, a) in L3.E})}

Lc = Lat((2, 2, 2), False)
FC = Lc.faces()
cube = {}
for s in itertools.product([1, -1], repeat=len(FC)):
    eta, ok = sector_eta(Lc, s)
    if ok:
        cube[s] = levels(Lc, eta)

sym = 0.0
bad_half = 0
ties = {}
for key in ("t4", "t6", "t8", "o333"):
    for k, ev in DATA[key].items():
        V = len(ev)
        sym = max(sym, float(np.max(np.abs(ev + ev[::-1]))))
        lad = np.concatenate(([0.0], np.cumsum(ev)))
        if abs(lad.min() - lad[V // 2]) > TOL:
            bad_half += 1
        nneg = int(np.sum(ev < -TOL))
        nz = int(np.sum(np.abs(ev) <= TOL))
        tie = [int(i) for i in np.flatnonzero(lad < lad.min() + TOL)]
        if [tie[0], tie[-1]] != [nneg, nneg + nz]:
            bad_half += 1
        ties[(key, k)] = (nneg, nz)
for k, ev in cube.items():
    sym = max(sym, float(np.max(np.abs(ev + ev[::-1]))))
    lad = np.concatenate(([0.0], np.cumsum(ev)))
    if abs(lad.min() - lad[4]) > TOL:
        bad_half += 1
check("B1 [numerical, 4e-14] spectra symmetric about 0: max |eps + rev| = %.1e" % sym,
      sym < 4e-14)
check("B2 min_N E_N = E_{V/2}, ties [#neg, #neg+#zero]; plain 4^3 %d zero modes, "
      "ties N in [%d, %d]"
      % (ties[("t4", ("plain", (0, 0, 0)))][1], ties[("t4", ("plain", (0, 0, 0)))][0],
         sum(ties[("t4", ("plain", (0, 0, 0)))])),
      bad_half == 0 and ties[("t4", ("plain", (0, 0, 0)))] == (22, 20))

cmin = {k: float(np.sum(v[v < 0])) for k, v in cube.items()}
gm = min(cmin.values())
winners = [k for k in cmin if cmin[k] < gm + TOL]
allm = tuple([-1] * 6)
margin = sorted(set(round(x, 9) for x in cmin.values()))[1] - gm
check("B3 cube exhaustive: %d sectors; min over (sector, N) at J_B = 0 is %.6f = "
      "-4 sqrt3, unique all-(-1) at N = 4, margin %.6f"
      % (len(cube), gm, margin),
      len(cube) == 32 and winners == [allm] and abs(gm + 4 * float(S3)) < 1e-12
      and abs(margin - 0.456067275) < 1e-8)

struct = {}
for nm_, fn in (
        ("xy", lambda p: p == (0, 1)), ("xz", lambda p: p == (0, 2)),
        ("yz", lambda p: p == (1, 2)), ("xy alt", None), ("xz+yz", lambda p: p in ((0, 2), (1, 2)))):
    vals = []
    for f in L4.faces():
        v, a, c, b = f
        d1 = [i for i in range(3) if ((a[i] - v[i]) % 4) in (1, 3)][0]
        d2 = [i for i in range(3) if ((b[i] - v[i]) % 4) in (1, 3)][0]
        p = tuple(sorted((d1, d2)))
        if nm_ == "xy alt":
            vals.append(-1 if (p == (0, 1) and v[0] % 2 == 0) else 1)
        else:
            vals.append(-1 if fn(p) else 1)
    eta, ok = sector_eta(L4, vals)
    struct[nm_] = levels(L4, eta) if ok else None

rng = np.random.default_rng(20260903)
rand4 = np.array([np.sort(np.linalg.eigvalsh(mat4(rng.choice([-1.0, 1.0], L4.nq))))
                  for _ in range(1000)])
L6 = Lat((6, 6, 6), True)
idx6 = {v: i for i, v in enumerate(L6.V)}


def mat6(s):
    M = np.zeros((216, 216))
    for k, (v, ax) in enumerate(L6.E):
        w = L6.step(v, EX[ax])
        M[idx6[w], idx6[v]] += s[k]
        M[idx6[v], idx6[w]] += s[k]
    return M


rand6 = np.array([np.sort(np.linalg.eigvalsh(mat6(rng.choice([-1.0, 1.0], L6.nq))))
                  for _ in range(300)])
DATA["r4"], DATA["r6"], DATA["s4"] = rand4, rand6, struct

E0 = lambda ev: float(np.sum(np.asarray(ev)[np.asarray(ev) < 0]))
b4 = min([E0(ev) for ev in DATA["t4"].values()] + [E0(ev) for ev in rand4]
         + [E0(v) for v in struct.values() if v is not None])
b6 = min([E0(ev) for ev in DATA["t6"].values()] + [E0(ev) for ev in rand6])
b8 = min(E0(ev) for ev in DATA["t8"].values())
floor4 = -64 * float(sp.sqrt(sp.Rational(3, 2)))
print("  4^3, 16 twisted uniform + 5 structured + 1000 random: %.9f = -32 sqrt6" % b4)
print("  6^3, 16 + 300 random (best random %.2f): %.6f ; 8^3: %.6f"
      % (min(E0(ev) for ev in rand6), b6, b8))
check("B4 4^3 minimum at J_B = 0 is -32 sqrt6, the Cauchy-Schwarz floor over ALL "
      "link-sign fields", abs(b4 - floor4) < 1e-9 and abs(b4 + 32 * float(S6)) < 1e-9)
check("B5 [search] 6^3 %.6f, 8^3 %.6f, open 3x3x3 %.6f stag vs %.6f plain"
      % (b6, b8, E0(DATA["o333"][("stag", ())]), E0(DATA["o333"][("plain", ())])),
      abs(b6 + 258.857540) < 1e-5 and abs(b8 + 611.811768) < 1e-5
      and abs(E0(DATA["o333"][("stag", ())]) + 26.040600) < 1e-5
      and abs(E0(DATA["o333"][("plain", ())]) + 21.213203) < 1e-5)

print()
print("=" * 62)
print("C  THE GROUND STATE AS A FUNCTION OF J_B (twist-minimised)")
print("=" * 62)


def best(key, sec, J):
    return min((Wm(ev, J) + (tw,)) for (s, tw), ev in DATA[key].items() if s == sec)


JT = [0.0, 0.5, 0.823267476, float(S3) / 2, float(S6) / 2, float(S3), 3.0]
print("  4^3 (V=64), w = W/V per site, n = N/V:")
print("      J_B  |  w plain    n plain  twist |   w stag     n stag  twist | lower")
tw_seen = set()
for J in JT:
    wp, mp, tp = best("t4", "plain", J)
    wm, mm, tm = best("t4", "stag", J)
    tw_seen.add(tm)
    print("  %8.6f | %9.6f %8.5f  %s | %9.6f %8.5f  %s | %s"
          % (J, wp / 64, mp / 64, "".join(map(str, tp)), wm / 64, mm / 64,
             "".join(map(str, tm)),
             "stag" if wm < wp - TOL else ("plain" if wp < wm - TOL else "tie")))
check("C1 [numerical, 1e-9] the optimal twist changes with J_B: %d distinct staggered "
      "twists in the 4^3 table" % len(tw_seen), len(tw_seen) >= 2)

J = sp.Symbol("J", positive=True)
w_stag = -24 - 24 * S2 - 8 * S3 + 56 * J
w_plain = -24 - 24 * S2 + 40 * J
spec_s = [(0, 8), (2, 12), (-2, 12), (2 * S2, 12), (-2 * S2, 12), (2 * S3, 4), (-2 * S3, 4)]
spec_p = [(0, 16), (2, 8), (-2, 8), (2 * S2, 8), (-2 * S2, 8),
          (2 + 2 * S2, 4), (-2 - 2 * S2, 4), (2 - 2 * S2, 4), (2 * S2 - 2, 4)]
Jx = S3 / 2
ok_s = sp.simplify(sum(c * (v + 2 * Jx) for v, c in spec_s if v < -2 * Jx) - w_stag.subs(J, Jx)) == 0
ok_p = sp.simplify(sum(c * (v + 2 * Jx) for v, c in spec_p if v < -2 * Jx) - w_plain.subs(J, Jx)) == 0
num_s = np.sort(np.concatenate([[float(v)] * c for v, c in spec_s]))
num_p = np.sort(np.concatenate([[float(v)] * c for v, c in spec_p]))
wit = max(float(np.max(np.abs(num_s - DATA["t4"][("stag", (0, 0, 0))]))),
          float(np.max(np.abs(num_p - DATA["t4"][("plain", (0, 1, 1))]))))
diff = sp.expand(w_stag - w_plain)
check("C2 [exact] 4^3: stag KS W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J vs plain (0,1,1) "
      "-24 - 24 sqrt2 + 40 J; difference %s" % sp.sstr(diff),
      ok_s and ok_p and wit < 1e-13 and diff == 16 * J - 8 * S3
      and sp.solve(sp.Eq(diff, 0), J) == [S3 / 2])


def crossover(key):
    lo, hi = 0.0, 3.5
    f = lambda x: best(key, "stag", x)[0] - best(key, "plain", x)[0]
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


x4, x6, x8 = crossover("t4"), crossover("t6"), crossover("t8")
check("C3 [numerical, 1e-9] J_B* = sqrt3/2 = %.9f (4^3), %.6f (6^3), %.6f (8^3)"
      % (x4, x6, x8),
      abs(x4 - float(S3) / 2) < 1e-8 and abs(x6 - 0.849332) < 1e-5
      and abs(x8 - 0.867676) < 1e-5)

emp = {}
for key in ("t4", "t6", "t8"):
    for sec in ("plain", "stag"):
        emp[(key, sec)] = -min(ev[0] for (s, tw), ev in DATA[key].items() if s == sec) / 2
op = -DATA["o333"][("plain", ())][0] / 2
os_ = -DATA["o333"][("stag", ())][0] / 2
cempty = max(-min(ev[0] for ev in cube.values()) / 2, 0.0)
tie32 = all(abs(Wm(v, 1.5 + 1e-9)[0]) < 1e-12 for v in cube.values())
print("  emptying thresholds J_B >= |eps_min|/2: plain 3, staggered sqrt3, all tori;")
print("  open 3x3x3 %.6f = 3 sqrt2/2 and %.6f = sqrt6/2; cube %.4f, all 32 tie at W = 0"
      % (op, os_, cempty))
check("C4 [exact where surds] plain empties at J_B = 3, staggered at sqrt3, all tori",
      all(abs(emp[(k, "plain")] - 3.0) < 1e-9 for k in ("t4", "t6", "t8"))
      and all(abs(emp[(k, "stag")] - float(S3)) < 1e-9 for k in ("t4", "t6", "t8"))
      and abs(op - 3 * float(S2) / 2) < 1e-9 and abs(os_ - float(S6) / 2) < 1e-9
      and abs(cempty - 1.5) < 1e-9 and tie32)

lo, hi = 0.0, 3.5
for _ in range(200):
    mid = (lo + hi) / 2
    vals = {k: Wm(v, mid)[0] for k, v in cube.items()}
    if vals[allm] < min(vals[k] for k in vals if k != allm) - 1e-12:
        lo = mid
    else:
        hi = mid
jcube = (lo + hi) / 2
check("C5 [exact] on the cube all-(-1) loses to the 2-flux class at "
      "sqrt3 - (1 + sqrt2)/2 = %.6f" % jcube,
      abs(jcube - float(S3 - (1 + S2) / 2)) < 1e-8)

print()
print("=" * 62)
print("D  THE EXTENDED CERTIFICATE ON 4^3, J_B <= sqrt(3/8) [exact]")
print("=" * 62)


def floorW(V, Jv):
    r = np.sqrt(3.0 / 8.0)
    return (-V * np.sqrt(1.5) + Jv * V) if Jv <= r else -3.0 * V / (8.0 * Jv)


Dcol = np.diag([(-1.0) ** sum(v) for v in L4.V])
trm, invol = True, True
for f in list(DATA["t4"].values())[:4] + [rand4[i] for i in range(4)]:
    trm &= abs(float(np.sum(f ** 2)) - 6 * 64) < 1e-9
for _ in range(8):
    M = mat4(rng.choice([-1.0, 1.0], L4.nq))
    invol &= bool(np.allclose(Dcol @ M @ Dcol, -M))
Jgrid = np.linspace(0.0, float(sp.sqrt(sp.Rational(3, 8))), 25)
flat = DATA["t4"][("stag", (1, 1, 1))]
slack = max(Wm(flat, Jv)[0] - floorW(64, Jv) for Jv in Jgrid)
viol = 0
allf = ([ev for ev in DATA["t4"].values()] + [v for v in struct.values() if v is not None]
        + list(rand4))
for Jv in np.linspace(0.0, 1.5, 16):
    fl = floorW(64, Jv)
    viol += sum(1 for ev in allf if Wm(ev, Jv)[0] < fl - 1e-9)
Wexact = sp.expand(32 * (2 * J - S6))
print("  tr M^2 = 6V, D M D = -M for any field, so sum_occ eps^2 <= 3V and W(J) >=")
print("  min_m [-sqrt(3 V m) + 2 J m] = -V sqrt(3/2) + J V for J <= sqrt(3/8) = %.6f,"
      % np.sqrt(3.0 / 8.0))
print("  and -3V/(8J) above it")
check("D1 [exact] bipartite degree-6 premises: tr M^2 = 384 and D M D = -M",
      trm and invol)
check("D2 [exact] the 4^3 flat-twist staggered sea has W = %s and attains the floor "
      "at every J_B <= sqrt(3/8): slack <= %.1e" % (sp.sstr(Wexact), slack),
      slack <= 7e-15 and sp.simplify(Wexact - (64 * J - 32 * S6)) == 0)
check("D3 [numerical, 1e-9] the floor holds for all %d fields at 16 values of J_B: "
      "%d violations" % (len(allf), viol), viol == 0)

print()
print("=" * 62)
print("E  HOW LONG EXACTLY HALF FILLING SURVIVES")
print("=" * 62)


def persist(key, V):
    lo, hi = 0.0, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if best(key, "stag", mid)[1] == V // 2:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


p4, p6, p8 = persist("t4", 64), persist("t6", 216), persist("t8", 512)
gap4 = -flat[int(np.sum(flat < 0)) - 1] / 2
check("E1 [exact] 4^3 half filled for J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = %.6f, and "
      "< sqrt6/2 = %.6f within its own twist" % (p4, gap4),
      abs(p4 - float(4 * S6 - 3 - 3 * S2 - S3)) < 1e-8 and abs(gap4 - float(S6) / 2) < 1e-9)
check("E2 [numerical, 1e-8] 6^3 half filled for J_B < 2 sqrt3 - 3 = %.6f, 8^3 for "
      "J_B < %.6f" % (p6, p8),
      abs(p6 - float(2 * S3 - 3)) < 1e-8 and abs(p8 - 0.306846) < 1e-5)

print()
print("=" * 62)
print("F  THE THERMODYNAMIC LIMIT [Bloch quadrature, L = 224]")
print("=" * 62)


def plain_levels(Lb):
    c = 2 * np.cos(2 * np.pi * np.arange(Lb) / Lb)
    return np.sort((c[:, None, None] + c[None, :, None] + c[None, None, :]).ravel())


def pi_levels(Lb):
    h = Lb // 2
    c = np.cos(2 * np.pi * np.arange(h) / h)
    s = np.sqrt(np.maximum(6 + 2 * (c[:, None, None] + c[None, :, None] + c[None, None, :]), 0)).ravel()
    return np.sort(np.repeat(np.concatenate([-s, s]), 4))


bl = 0.0
for Lb, key in ((4, "t4"), (6, "t6"), (8, "t8")):
    bl = max(bl, float(np.max(np.abs(plain_levels(Lb) - DATA[key][("plain", (0, 0, 0))]))),
             float(np.max(np.abs(pi_levels(Lb) - DATA[key][("stag", (0, 0, 0))]))))
check("F1 [numerical, 1e-9] Bloch 2 sum cos q_a and +-sqrt(6 + 2 sum cos q_a) match "
      "real space at L = 4, 6, 8 to %.1e" % bl, bl < 1e-9)

LB = 224
pl, pim = plain_levels(LB), pi_levels(LB)


def w_of(ev, Js):
    cs = np.concatenate(([0.0], np.cumsum(ev)))
    Js = np.asarray(Js, float)
    m = np.searchsorted(ev, -2.0 * Js, "left")
    return (cs[m] + 2.0 * Js * m) / len(ev), m / len(ev)


JL = np.array([0.0, 0.4, 0.8654003, 1.2, float(S3), 3.0])
wpv, npv = w_of(pl, JL)
wmv, nmv = w_of(pim, JL)
print("      J_B  |   w plain     n plain |    w stag      n stag | lower")
for i, Jv in enumerate(JL):
    print("  %8.6f | %10.7f %9.6f | %10.7f %9.6f | %s"
          % (Jv, wpv[i], npv[i], wmv[i], nmv[i],
             "stag" if wmv[i] < wpv[i] - 1e-12 else ("plain" if wpv[i] < wmv[i] - 1e-12 else "tie")))
lo, hi = 0.0, float(S3)
for _ in range(80):
    mid = (lo + hi) / 2
    if w_of(pim, np.array([mid]))[0][0] - w_of(pl, np.array([mid]))[0][0] < 0:
        lo = mid
    else:
        hi = mid
Jl = (lo + hi) / 2
ns = w_of(pim, np.array([Jl]))[1][0]
nq = w_of(pl, np.array([Jl]))[1][0]
check("F2 [numerical] J_B* = %.7f +- 3e-6 in the limit, fillings %.4f staggered "
      "and %.4f plain there" % (Jl, ns, nq),
      abs(Jl - 0.8654003) < 3e-6 and abs(ns - 0.4417) < 5e-4 and abs(nq - 0.2521) < 5e-4)

# The staggered band eps = -sqrt(6 + 2 sum_a cos q_a) vanishes at q = (pi, pi, pi)
# and nowhere else, and near it 6 + 2 sum_a cos q_a = |k|^2 + O(|k|^4).  So for any
# J_B > 0 the emptied set {|k| < 2 J_B} has positive measure: exactly half filling
# survives only at J_B = 0, with 1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3.
kk = sp.symbols("k1 k2 k3", real=True)
ser = sp.series(6 + 2 * sum(sp.cos(sp.pi + k) for k in kk), kk[0], 0, 4).removeO()
gapless = sp.simplify(ser - (kk[0] ** 2 + 2 * sp.cos(sp.pi + kk[1]) + 2 * sp.cos(sp.pi + kk[2]) + 4)
                      ) == 0
asym = [(0.5 - w_of(pim, np.array([Jv]))[1][0]) / (2.0 / (3 * np.pi ** 2) * Jv ** 3)
        for Jv in (0.15, 0.2, 0.3)]
n001 = w_of(pim, np.array([0.001]))[1][0]
print("  (1/2 - n(J)) / ((2/(3 pi^2)) J^3) at J = 0.15, 0.2, 0.3: %.4f, %.4f, %.4f"
      % (asym[0], asym[1], asym[2]))
print("  at J = 0.001 the emptied ball |k| < 2J is finer than the grid: n = %.7f" % n001)
check("F3 [exact + numerical] gapless at (pi, pi, pi), so any J_B > 0 dopes the sea: "
      "1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3",
      gapless and all(abs(a - 1.0) < 0.06 for a in asym) and n001 <= 0.5)
check("F4 [exact] in the limit plain empties at J_B = 3 (bottom -6), staggered at "
      "sqrt3 (bottom -2 sqrt3)",
      abs(w_of(pl, np.array([3.0]))[1][0]) < 1e-12
      and abs(w_of(pim, np.array([float(S3)]))[1][0]) < 1e-12
      and w_of(pl, np.array([2.999]))[1][0] > 0 and w_of(pim, np.array([1.731]))[1][0] > 0)

print()
print("runtime %.1f s (budget %d s)" % (time.time() - T0, AUDIT_TIMEOUT_SEC))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
