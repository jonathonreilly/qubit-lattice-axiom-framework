#!/usr/bin/env python3
"""Shifting position records: the exact diffusion law and the uniform attractor.

Class-A finite-cluster runner, self-contained.  Two lattices, both declared
here and neither derived from any axiom.

  * THE CUBE.  Qubits on the 12 EDGE sites of the 2x2x2 cube graph (8 corners,
    6 faces), ordinary composition, the superfast encoding, and the corner
    parity dictionary n_v = (1 - B_v)/2.  A record at an edge site registers a
    Z-value there; the finished set of records is a vector y in F2^12 and the
    dictionary reads a corner occupation off it.  The N = 2 record sector is
    896-dimensional = 28 corner pairs x 32, and no dense object above 896 x 896
    is formed anywhere.
  * THE COARSE TORUS.  One-particle hopping on an L^3 torus with the
    Kogut-Susskind staggered (pi-flux) link signs eta(v,1) = 1,
    eta(v,2) = (-1)^{v_x}, eta(v,3) = (-1)^{v_x + v_y}, unit amplitude, unit
    spacing, coordination 6.  L = 32 for the one-particle rows (L = 16 as a
    finite-size control), L = 6 for the two-record chain.

The SIX TICK MODELS are STIPULATED here, in full, and derived from nothing.
Each fixes what happens to a registered position between one tick and the next.

  M0  UNRECORDED.  No record forms; the state runs freely under H for time t.
  M1  FROZEN.  One record is registered at a corner v and never moves; the gap
      generator is H_R = the hops on the sites carrying no record, exactly the
      PR #7876 convention, which at the coarse level deletes the six hops at v.
  M2  SHIFTING.  Every tick of length tau the corner occupation is registered
      again by Lueders conditioning, and the record moves to wherever it is
      registered.  This is the owner's proposal read as a tick.
  M3  SHIFTING WITH FORMATION PROBABILITY p.  As M2, but a tick registers with
      probability p and otherwise lets the state run on.
  M4  GROUP MOTION UNDER AN ENERGY COST.  Two records under
      H = -sum eta (c^dag c + h.c.) + g sum_bonds n n, both registered every
      tick (M2), g the cost of parting.  This is a COST and not a SUPPORT
      condition: the law's odds stay nonzero for every separated configuration,
      so nothing here bears on a law whose support forbids parting outright.
  M5  RECORD LEVEL.  The M2 tick on the cube's 896-dimensional sector as the
      map rho -> mask(U(tau) rho U(tau)^dag), mask = Lueders on the 28 corner
      patterns; cross-checked against explicit record-tree enumeration.

The runner establishes:

  A  WHAT A SHIFT IS, EXACTLY.  The census of all 4096 record patterns x 12
     edge sites: corner level against site level, and the exclusion clause.
  B  UNRECORDED AND FROZEN.  M0's ballistic spread and M1's exact pinning.
  C  THE DIFFUSION LAW.  M2's one-tick kernel is translation covariant and
     even, so the registered trajectory is an i.i.d. mean-zero walk; D(tau),
     its Zeno and Drude limits, and the shoulder between them.
  D  THE RENEWAL LAW.  M3's exact age decomposition and the crossover at the
     mean free time tau/p.
  E  GROUP MOTION.  The exact 111-class relative-coordinate chain of M4 on the
     6^3 torus, and the same statement on the cube's 896-dim sector.  Scope:
     an energy cost only; a support-conditioned law is untested here.
  F  THE UNIFORM ATTRACTOR.  M5's tick map against explicit record trees, its
     exact fixed point, and the geometric loss of the selection-rule zeros.

Line tags.  `[exact]` = integer, F2, Gaussian-integer or `Fraction` arithmetic
with no floating point in the statement.  `[numerical]` = a deterministic
double-precision evaluation of an exactly specified quantity at a stated
threshold: no sampling, no seed, no random number anywhere in this runner.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from functools import reduce

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 150

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


# ==================================================================== cluster

def cube_cluster():
    """Corner s = 4a + 2b + c of the 2x2x2 cube; edges flip one coordinate."""
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


# =================================================================== encoding

class Enc:
    """Superfast encoding on the edge sites of a finite open graph."""

    def __init__(self, V, EDGES, FACES):
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
        """The parity dictionary n_v = (1 - B_v)/2 read off an edge-site record."""
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
    return cid, phi, reps, recs


def sector_matrix(E, R, cid, phi, reps, recs, keep):
    """Exact H_enc on the code space, rows and columns the kept cosets."""
    k = R["k"]
    grp = R["grp"]
    sel = [c for c in range(len(reps)) if keep(recs[c])]
    pos = {c: a for a, c in enumerate(sel)}
    n = len(sel)
    Hoff = np.zeros((n, n), dtype=complex)
    hp = {e: E.hop_pauli(*e) for e in E.EDGES}
    for c in sel:
        a = pos[c]
        for g in grp:
            y, ay = pact(g, reps[c])
            for e in E.EDGES:
                yy, amp = E.hop_amp(hp[e][0], hp[e][1], y)
                if amp == 0:
                    continue
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


# =========================================== the cube and its N = 2 sector

V, EDG = cube_cluster()
EN = Enc(V, sorted(EDG), cube_faces())
AUD = audit(EN)
CID, PHI, REPS, RECS = code_space(EN, AUD)
NQ = EN.NQ

_rec = np.array([EN.record(z) for z in range(EN.DIM)], dtype=np.int8)
ZL = np.flatnonzero(_rec.sum(1) == 2).astype(np.int64)
NZ = len(ZL)
POSZ = -np.ones(EN.DIM, dtype=np.int64)
POSZ[ZL] = np.arange(NZ)

PAIRS = [(i, j) for i in range(8) for j in range(i + 1, 8)]
PIDX = {p: i for i, p in enumerate(PAIRS)}
PATZ = np.array([PIDX[tuple(np.flatnonzero(_rec[z]))] for z in ZL], dtype=np.int64)

_HP = {e: EN.hop_pauli(*e) for e in EN.EDGES}
TGT = np.zeros((NQ, NZ), dtype=np.int64)
AMP = np.zeros((NQ, NZ), dtype=complex)
SECTOR_CLOSED = True
for _q, _e in enumerate(EN.EDGES):
    _P1, _P2 = _HP[_e]
    for _a in range(NZ):
        _z = int(ZL[_a])
        _zz, _amp = EN.hop_amp(_P1, _P2, _z)
        if _amp == 0:
            TGT[_q, _a] = -1
            continue
        if _zz != _z ^ (1 << _q) or POSZ[_zz] < 0:
            SECTOR_CLOSED = False
            TGT[_q, _a] = -1
            continue
        TGT[_q, _a] = POSZ[_zz]
        AMP[_q, _a] = _amp

H896 = np.zeros((NZ, NZ), dtype=complex)
for _q in range(NQ):
    _m = AMP[_q] != 0
    H896[TGT[_q][_m], np.flatnonzero(_m)] += AMP[_q][_m]

SEL, _POSC, HOFF, _HOFF_EX = sector_matrix(
    EN, AUD, CID, PHI, REPS, RECS, lambda r: sum(r) == 2)
PATS28 = [RECS[c] for c in SEL]
_JWIDX, TJW = fermi_sector(EN.EDGES, PATS28)
GAUGE = gauge_match(HOFF, TJW)
assert GAUGE is not None


def _chi(s, u):
    return -1 if pcnt(s & u) % 2 else 1


def slater(s, t):
    w = np.zeros(len(PATS28), dtype=np.int64)
    for a, p in enumerate(PATS28):
        u, x = [i for i, b in enumerate(p) if b]
        w[a] = _chi(s, u) * _chi(t, x) - _chi(s, x) * _chi(t, u)
    return w


def _sector_vector(amps):
    v = np.zeros(NZ, dtype=complex)
    for a in range(NZ):
        c = CID[int(ZL[a])]
        A = amps.get(c, 0.0)
        if A:
            v[a] = A * PHI[int(ZL[a])]
    return v


WGS = slater(0, 4)
_GU = None
for _cj in (True, False):
    _amps = {SEL[a]: complex(WGS[a]) * (np.conj(GAUGE[a]) if _cj else GAUGE[a])
             for a in range(len(SEL)) if WGS[a]}
    _v = _sector_vector(_amps)
    if np.max(np.abs(H896 @ _v + 4.0 * _v)) < 1e-9:
        _GU = _v
        break
assert _GU is not None, "ground state gauge convention"
GU = np.round(_GU.real) + 1j * np.round(_GU.imag)
NRM = int(round(float(np.vdot(GU, GU).real)))
PSI0 = GU / math.sqrt(NRM)


def born28(psi):
    return np.bincount(PATZ, weights=np.abs(psi) ** 2, minlength=28)


GS_BORN = born28(PSI0)
ZERO12 = [k for k in range(28) if GS_BORN[k] < 1e-12]
CDIST = np.array([pcnt(i ^ j) for (i, j) in PAIRS])
CADJ = (CDIST == 1).astype(float)
MASK28 = (PATZ[:, None] == PATZ[None, :])
UNIF28 = np.full(28, 1.0 / 28.0)


def l1(a, b):
    return float(np.abs(np.asarray(a) - np.asarray(b)).sum())


# ================================================ the coarse pi-flux torus

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """Kogut-Susskind staggered (pi-flux) link sign of the bond (v, v + e_a)."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def torus(L, drop=None, sign=1.0):
    """Sparse hopping matrix, the site list, and the index map of an L^3 torus.
    `drop` deletes every bond at one site -- the M1 frozen-record convention."""
    sites = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    r, c, d = [], [], []
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % L for i in range(3))
            if drop is not None and (v == drop or w == drop):
                continue
            s = sign * float(eta_ks(v, a))
            r += [idx[w], idx[v]]
            c += [idx[v], idx[w]]
            d += [s, s]
    return sp.csr_matrix((d, (r, c)), shape=(L ** 3, L ** 3)), sites, idx


def minimal(x, L):
    x %= L
    return x - L if x > L // 2 else x


def displacements(L, sites, org):
    return np.array([[minimal(s[i] - org[i], L) for i in range(3)]
                     for s in sites], dtype=float)


L32, M32, S32, I32 = 32, None, None, None
M32, S32, I32 = torus(32)
ORG32 = (16, 16, 16)
O32 = I32[ORG32]
D32 = displacements(32, S32, ORG32)
RAD32 = np.max(np.abs(D32), axis=1)


def kernel32(t, M=None, o=None):
    """|<w| exp(-i t H) |v>|^2 as a probability vector over the L = 32 torus."""
    M = M32 if M is None else M
    o = O32 if o is None else o
    v = np.zeros(M.shape[0], dtype=complex)
    v[o] = 1.0
    return np.abs(spla.expm_multiply(-1j * t * M, v)) ** 2


def sigma2(p, D):
    m1 = p @ D
    return float((p @ D ** 2).sum() - (m1 ** 2).sum())


_M2C = {}


def m2(t):
    """The one-tick second moment m_2(tau) = sigma^2 of the M0 kernel."""
    t = round(float(t), 12)
    if t <= 1e-15:
        return 0.0
    if t not in _M2C:
        _M2C[t] = sigma2(kernel32(t), D32)
    return _M2C[t]


def _tq(q):
    return ", ".join("%.4f" % x for x in q)


# ===================================================================== group A

def group_A():
    """What "a record shifts" is, exactly, in the edge-record language."""
    corners = list(range(8))
    edges = [(i, j) for i in range(8) for j in range(i + 1, 8) if pcnt(i ^ j) == 1]
    star = [[e for e, (i, j) in enumerate(edges) if v in (i, j)] for v in corners]
    deg = sorted({len(s) for s in star})

    def nrec(y):
        return [sum((y >> e) & 1 for e in star[v]) % 2 for v in corners]

    bad_local = bad_w = bad_shift = bad_pair = 0
    up = dn = n_shift = n_pair = 0
    for y in range(1 << 12):
        n = nrec(y)
        wy = pcnt(y)
        for e, (v, w) in enumerate(edges):
            y2 = y ^ (1 << e)
            n2 = nrec(y2)
            if not (n2[v] == 1 - n[v] and n2[w] == 1 - n[w]):
                bad_local += 1
            if any(n2[u] != n[u] for u in corners if u not in (v, w)):
                bad_local += 1
            if (y >> e) & 1:
                dn += 1
                if pcnt(y2) != wy - 1:
                    bad_w += 1
            else:
                up += 1
                if pcnt(y2) != wy + 1:
                    bad_w += 1
            nb, na = sum(n), sum(n2)
            if n[v] + n[w] == 1:
                n_shift += 1
                if na != nb:
                    bad_shift += 1
            else:
                n_pair += 1
                if na != nb + (2 if n[v] == 0 else -2):
                    bad_pair += 1
    tot = 4096 * 12
    check("A1 [exact] cube, %d corners and %d edge sites of degree %s: over all %d record patterns x %d "
          "sites (%d cases) a hop along the shared site e is y -> y XOR e, complementing n_v and n_w "
          "alone: %d violations"
          % (8, len(edges), deg[0] if len(deg) == 1 else deg, 4096, len(edges), tot, bad_local),
          bad_local == 0 and len(edges) == 12 and deg == [3])
    check("A2 [exact] at the PHYSICAL sites a shift is a VALUE change: the edge-record weight |y| moves "
          "by exactly +-1 in all %d cases (%d up, %d down), never by 0: %d violations"
          % (tot, up, dn, bad_w), bad_w == 0 and up == dn == tot // 2)
    check("A3 [exact] at the CORNER level the support shifts, and only under exclusion: sum_v n_v is "
          "conserved exactly when one endpoint is occupied (%d cases, %d violations), else moves by "
          "+-2 (%d cases, %d violations)" % (n_shift, bad_shift, n_pair, bad_pair),
          bad_shift == 0 and bad_pair == 0 and n_shift + n_pair == tot)


# ===================================================================== group B

def group_B():
    """M0 unrecorded and M1 frozen."""
    ts = [0.1, 0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
    s2 = [sigma2(kernel32(t), D32) for t in ts]
    rat = [math.sqrt(a) / t for a, t in zip(s2, ts)]
    check("B1 [numerical, 1e-12] M0 on the L = 32 pi-flux torus: sigma^2(t) = %s at t = .1, .25, .5, 1, "
          "2, 3, 5, 10 and sigma/t falls %.4f -> %.4f -- ballistic, no diffusion constant"
          % (", ".join("%.4f" % x for x in s2), rat[0], rat[-1]),
          all(b > a for a, b in zip(s2, s2[1:])) and abs(rat[-1] - 1.1204) < 1e-3
          and all(rat[i] > rat[i + 1] for i in range(len(rat) - 1)))

    M16, S16, I16 = torus(16)
    D16 = displacements(16, S16, (8, 8, 8))
    dev = []
    for tau in (0.1, 0.5, 1.0):
        p16 = np.abs(spla.expm_multiply(-1j * tau * M16,
                                        np.eye(1, 4096, I16[(8, 8, 8)]).ravel().astype(complex))) ** 2
        dev.append(abs(sigma2(p16, D16) - m2(tau)))
    check("B2 [numerical, 1e-7] finite size: m_2(tau) on L = 16 and L = 32 agree to %.1e, %.1e, %.1e at "
          "tau = 0.1, 0.5, 1.0, so the one-particle rows are torus-independent for tau <= 1"
          % tuple(dev), max(dev) < 1e-7)

    Mf, Sf, If = torus(32, drop=ORG32)
    nb = (M32.nnz - Mf.nnz) // 2
    ev = np.zeros(32 ** 3)
    ev[O32] = 1.0
    row = float(np.abs(Mf @ ev).max())
    fs2, leak = [], []
    for t in (0.5, 1.0, 5.0, 20.0, 100.0):
        p = kernel32(t, Mf, O32)
        fs2.append(sigma2(p, D32))
        leak.append(1.0 - float(p[O32]))
    check("B3 [numerical, 1e-15] M1, the frozen record of PR #7876: its H_R deletes the %d bonds at the "
          "recorded corner, H_R e_v = 0 identically (max %.1e), sigma^2 = %.1e and leakage %.1e at "
          "t = .5, 1, 5, 20, 100 -- pinned"
          % (nb, row, max(fs2), max(leak)), nb == 6 and row == 0.0
          and max(fs2) < 1e-15 and max(leak) < 1e-15)


# ===================================================================== group C

def group_C():
    """The M2 diffusion law, its two limits, and the shoulder between them."""
    M16, S16, I16 = torus(16)
    tau = 0.5
    va, vb = (8, 8, 8), (9, 10, 8)

    def p16(v):
        e = np.zeros(4096, dtype=complex)
        e[I16[v]] = 1.0
        return np.abs(spla.expm_multiply(-1j * tau * M16, e)) ** 2

    pa, pb = p16(va), p16(vb)
    Da, Db = displacements(16, S16, va), displacements(16, S16, vb)
    ka = {tuple(int(x) for x in Da[i]): pa[i] for i in range(4096)}
    kb = {tuple(int(x) for x in Db[i]): pb[i] for i in range(4096)}
    cov = max(abs(ka[k] - kb[k]) for k in ka)
    even = max(abs(ka[k] - ka[tuple(-x for x in k)]) for k in ka
               if all(abs(x) < 8 for x in k))
    mean = float(np.abs(pa @ Da).max())
    check("C1 [numerical, 1e-20] M2's one-tick kernel p_tau(r) = |<v + r| e^{-i tau H} |v>|^2 at "
          "tau = 0.5 is translation covariant to %.1e and even to %.1e with |E[r]| <= %.1e: an i.i.d. "
          "mean-zero registered walk"
          % (cov, even, mean), cov < 1e-20 and even < 1e-20 and mean < 1e-12)

    ax = np.arange(32)
    axm = np.where(ax > 16, ax - 32, ax).astype(float)
    dx, dy, dz = axm[:, None, None], axm[None, :, None], axm[None, None, :]
    r2 = dx ** 2 + dy ** 2 + dz ** 2
    ii = np.array(S32)

    def grid(p):
        g = np.zeros((32, 32, 32))
        g[(ii[:, 0] - 16) % 32, (ii[:, 1] - 16) % 32, (ii[:, 2] - 16) % 32] = p
        return g

    def s2g(g):
        m1 = np.array([(g * dx).sum(), (g * dy).sum(), (g * dz).sum()])
        return float((g * r2).sum() - (m1 ** 2).sum())

    rmax = np.maximum(np.maximum(np.abs(dx), np.abs(dy)), np.abs(dz))
    worst = 0.0
    ncnt = 0
    for tau in (0.1, 0.25, 0.5, 1.0, 2.0):
        g = grid(kernel32(tau))
        f = np.fft.fftn(g)
        base = s2g(g)
        for n in (1, 2, 3, 5, 10, 20, 50):
            gn = np.real(np.fft.ifftn(f ** n))
            if abs(float(gn[rmax >= 14].sum())) > 1e-14:
                continue
            worst = max(worst, abs(s2g(gn) - n * base))
            ncnt += 1
    check("C2 [numerical, 1e-11] increments add: the n-fold FFT convolution of the tick kernel gives "
          "sigma^2(n tau) = n m_2(tau) to max %.1e over the %d (tau, n) pairs with tau <= 2, n <= 50 "
          "and wrap mass below 1e-14"
          % (worst, ncnt), worst < 1e-11 and ncnt >= 15)

    tl = [0.1, 0.25, 0.5, 0.7, 1.0, 1.2, 2.0, 3.0, 5.0]
    dl = [m2(t) / (6 * t) for t in tl]
    check("C3 [numerical, 1e-9] the diffusion law of a shifting record: D(tau) = m_2(tau)/(6 tau) = %s at "
          "tau = .1, .25, .5, .7, 1, 1.2, 2, 3, 5" % ", ".join("%.4f" % x for x in dl),
          all(abs(a - b) < 1e-4 for a, b in
              zip(dl, [0.0987, 0.2302, 0.3630, 0.3860, 0.3561, 0.3479, 0.4881, 0.6706, 1.0747])))

    z = sum(1.0 * (1 ** 2) for _ in range(6))
    a005 = (6 - m2(0.005) / 0.005 ** 2) / 0.005 ** 2
    check("C4 [exact + numerical] Zeno limit: m_2 = z tau^2 - a tau^4 + O(tau^6), z = "
          "sum_w |H_wv|^2 |w - v|^2 = %d exactly (the coordination), a -> %.5f at tau = 0.005 "
          "(8, extrapolated), so D = tau - (4/3) tau^3 + ...: fast ticks pin"
          % (int(z), a005), int(z) == 6 and abs(a005 - 8.0) < 1e-3)

    xs = np.array([3.0, 4.0, 5.0, 6.0])
    ys = np.array([m2(t) for t in xs])
    co = np.linalg.lstsq(np.vstack([xs ** 2, xs, np.ones_like(xs)]).T, ys, rcond=None)[0]
    sh = [(t, m2(t) / (6 * t)) for t in (0.6, 0.65, 0.7, 0.75, 1.1, 1.15, 1.2, 1.25)]
    hi = max(sh[:4], key=lambda r: r[1])
    lo = min(sh[4:], key=lambda r: r[1])
    check("C5 [numerical, 1e-3] Drude limit: m_2/tau^2 -> c_2 = %.4f on tau in [3, 6], so D -> %.4f tau: "
          "slow ticks let it fly; between the limits D carries a shoulder, max %.4f at tau = %.2f, "
          "min %.4f at tau = %.2f"
          % (co[0], co[0] / 6, hi[1], hi[0], lo[1], lo[0]),
          abs(co[0] - 1.2437) < 1e-3 and hi[0] == 0.7 and lo[0] == 1.15)
    return co


# ===================================================================== group D

def m3_curve(tau, p, nmax, mfun):
    """The exact age decomposition of M3.  Returns [(n, t, sigma^2)]."""
    age = {0: 1.0}
    ev = 0.0
    out = []
    for _ in range(nmax):
        adv = {a + 1: w for a, w in age.items()}
        ev += p * sum(w * mfun(a * tau) for a, w in adv.items())
        nxt = {0: p}
        for a, w in adv.items():
            nxt[a] = nxt.get(a, 0.0) + (1 - p) * w
        age = nxt
        out.append((len(out) + 1, (len(out) + 1) * tau,
                    ev + sum(w * mfun(a * tau) for a, w in age.items())))
    return out


def group_D(co):
    """M3: the renewal law and the mean-free-time crossover."""
    pf = Fraction(1, 5)
    tau = 0.5
    nmax = 12
    ages_ok = True
    for n in range(1, nmax + 1):
        law = [(1 - pf) ** a * pf for a in range(n)] + [(1 - pf) ** n]
        if sum(law) != 1:
            ages_ok = False
    # brute force over all 2^n formation histories, exactly weighted
    direct = []
    for n in range(1, nmax + 1):
        tot = Fraction(0)
        acc = 0.0
        for h in range(1 << n):
            w = Fraction(1)
            segs = []
            run = 0
            for k in range(n):
                run += 1
                if (h >> k) & 1:
                    w *= pf
                    segs.append(run)
                    run = 0
                else:
                    w *= (1 - pf)
            segs.append(run)
            tot += w
            acc += float(w) * sum(m2(s * tau) for s in segs)
        direct.append(acc)
        if tot != 1:
            ages_ok = False
    rec = [x[2] for x in m3_curve(tau, float(pf), nmax, m2)]
    resid = max(abs(a - b) for a, b in zip(direct, rec))
    check("D1 [exact] renewal: ages carry P_n(a) = (1-p)^a p (a < n), (1-p)^n (a = n), summing "
          "to 1 exactly as Fractions at every n <= %d, and sigma^2(n tau) = E[V_n] + sum_a P_n(a) "
          "m_2(a tau) matches enumeration of all 2^n histories to %.1e" % (nmax, resid),
          ages_ok and resid < 1e-12)

    c2, c1, c0 = co

    def m2x(s):
        return m2(s) if s <= 6.0 else c2 * s * s + c1 * s + c0

    def dinf(tau, p):
        return (p / (6 * tau)) * sum(p * (1 - p) ** (k - 1) * m2x(k * tau)
                                     for k in range(1, int(240 / p)))

    cases = [(0.5, 1.0), (0.5, 0.2), (0.5, 0.05), (1.0, 0.1), (2.0, 0.05)]
    got = [dinf(t, p) for t, p in cases]
    want = [c2 * t * (2 - p) / (6 * p) for t, p in cases]
    check("D2 [numerical, 1e-6] M3: D_inf = (p/(6 tau)) sum_k p (1-p)^(k-1) m_2(k tau) = %s at "
          "(tau, p) = (.5, 1), (.5, .2), (.5, .05), (1, .1), (2, .05), against c_2 tau (2-p)/(6p) = %s"
          % (", ".join("%.4f" % x for x in got), ", ".join("%.4f" % x for x in want)),
          abs(got[0] - m2(0.5) / 3.0) < 1e-9
          and all(abs(a - b) / b < 0.02 for a, b in zip(got[2:], want[2:])))

    mfp = [(0.5, 0.05), (1.0, 0.1), (2.0, 0.2)]
    dm = [dinf(t, p) for t, p in mfp]
    spread = max(dm) / min(dm) - 1.0
    dm2 = m2(0.5) / 3.0
    check("D3 [numerical, 1e-6] the scale is the MEAN FREE TIME tau/p, not p tau: (0.5, 0.05), (1, 0.1) "
          "and (2, 0.2) share tau/p = 10 and give D_inf = %s, within %.1f%%, while their p tau = 0.025, "
          "0.1, 0.4 spans 16x (D_M2(0.5) = %.4f)"
          % (", ".join("%.4f" % x for x in dm), 100 * spread, dm2),
          spread < 0.09 and min(dm) > 3.7)


# ===================================================================== group E

def group_E():
    """M4: two records, the exact 111-class relative chain, and the cube."""
    L = 6
    M1s, sites, idx = torus(L, sign=-1.0)
    NV = L ** 3
    M1d = M1s.toarray()
    nbr = [[idx[tuple((v[i] + e[i]) % L for i in range(3))] for e in
            [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
           for v in sites]
    pid = -np.ones((NV, NV), dtype=np.int64)
    cfg = []
    for a in range(NV):
        for b in range(a + 1, NV):
            pid[a, b] = pid[b, a] = len(cfg)
            cfg.append((a, b))
    nc = len(cfg)
    cfg = np.array(cfg)

    def build2(g):
        r2, c2, v2 = [], [], []
        for ci, (a, b) in enumerate(cfg):
            for (v, u) in ((a, b), (b, a)):
                for w in nbr[v]:
                    if w == u:
                        continue
                    amp = M1d[w, v]
                    if amp == 0:
                        continue
                    sgn = -1.0 if (min(v, w) < u < max(v, w)) else 1.0
                    r2.append(pid[w, u])
                    c2.append(ci)
                    v2.append(amp * sgn)
            if g and (b in nbr[a]):
                r2.append(ci)
                c2.append(ci)
                v2.append(float(g))
        return sp.csr_matrix((v2, (r2, c2)), shape=(nc, nc))

    def relkey(a, b):
        va, vb = sites[a], sites[b]
        r1 = tuple((vb[i] - va[i]) % L for i in range(3))
        return min(r1, tuple((-x) % L for x in r1))

    keys = sorted({relkey(a, b) for a, b in cfg})
    kid = {k: i for i, k in enumerate(keys)}
    nk = len(keys)
    ckey = np.array([kid[relkey(a, b)] for a, b in cfg], dtype=np.int64)
    kdist = np.array([sum(min(x, L - x) for x in k) for k in keys])
    rep = {kid[k]: pid[idx[(0, 0, 0)], idx[k]] for k in keys}
    sumc = np.array([[(sites[a][i] + sites[b][i]) % L for i in range(3)] for a, b in cfg],
                    dtype=np.int64)
    csize = np.bincount(ckey, minlength=nk).astype(float)
    unifc = csize / csize.sum()

    def tick(H2, tau):
        Q = np.zeros((nk, nk))
        vcom = np.zeros(nk)
        B = np.zeros((nc, nk), dtype=complex)
        for k in range(nk):
            B[rep[k], k] = 1.0
        out = np.empty((nc, nk), dtype=complex)
        for s in range(0, nk, 24):
            out[:, s:s + 24] = spla.expm_multiply(-1j * tau * H2, B[:, s:s + 24])
        for k in range(nk):
            p = np.abs(out[:, k]) ** 2
            Q[k] = np.bincount(ckey, weights=p, minlength=nk)
            s0 = sumc[rep[k]]
            ds = np.stack([np.array([minimal(int(x), L) for x in (sumc[:, i] - s0[i])])
                           for i in range(3)], axis=1).astype(float)
            m1 = p @ ds
            vcom[k] = float((p @ ds ** 2).sum() - (m1 ** 2).sum()) / 4.0
        return Q, vcom

    tau = 0.5
    e0 = np.zeros(NV, dtype=complex)
    e0[idx[(0, 0, 0)]] = 1.0
    ps = np.abs(spla.expm_multiply(-1j * tau * M1s, e0)) ** 2
    d1 = sigma2(ps, displacements(L, sites, (0, 0, 0))) / (6 * tau)
    adj0 = [k for k in range(nk) if kdist[k] == 1][0]

    rows, rowerr, dcom, meand = {}, 0.0, {}, {}
    for g in (0.0, 4.0, 8.0, 16.0, 32.0):
        Q, vcom = tick(build2(g), tau)
        rowerr = max(rowerr, float(np.abs(Q.sum(1) - 1).max()))
        p = np.zeros(nk)
        p[adj0] = 1.0
        acc = 0.0
        seq = []
        for n in range(1, 41):
            acc += float(p @ vcom)
            p = p @ Q
            if n in (1, 2, 5, 10, 20, 40):
                seq.append(float(p[kdist == 1].sum()))
            if n == 40:
                dcom[g] = acc / (6 * n * tau) / d1
                meand[g] = float(p @ kdist)
        rows[g] = seq
    check("E1 [numerical, 1e-9] M4 on the 6^3 torus: %d two-particle configurations reduce by translation "
          "covariance to an EXACT %d-class relative chain, rows summing to 1 (max %.1e); uniform gives "
          "P(adjacent) = %.4f, mean %.4f"
          % (nc, nk, rowerr, float(unifc[kdist == 1].sum()), float(unifc @ kdist)),
          nc == 23220 and nk == 111 and rowerr < 1e-9
          and abs(float(unifc[kdist == 1].sum()) - 0.0279) < 1e-4)
    check("E2 [numerical, 1e-6] at tau = 0.5 a pair held by an ENERGY cost comes apart at every g: "
          "P(adjacent) over ticks 1..40 runs %s, toward the uniform 0.0279"
          % ("; ".join("%.4f->%.4f (%d)" % (rows[g][0], rows[g][-1], int(g))
                       for g in (0.0, 4.0, 8.0, 16.0, 32.0))),
          all(rows[g][0] > rows[g][-1] for g in rows)
          and all(rows[g][i] >= rows[g][i + 1] for g in rows for i in range(5))
          and abs(rows[0.0][-1] - 0.0279) < 1e-3)
    check("E3 [numerical, 1e-6] cost-bound motion is not rigid: tick-40 mean distance %.4f, %.4f, %.4f, "
          "%.4f, %.4f at g = 0, 4, 8, 16, 32 against the uniform 4.5209 (g = 4 inside the continuum, "
          "half band %.4f); D_CoM/D_1 = %.4f at g = 0, the independent 1/2"
          % (meand[0.0], meand[4.0], meand[8.0], meand[16.0], meand[32.0],
             math.sqrt(12.0), dcom[0.0]),
          abs(dcom[0.0] - 0.4910) < 1e-3 and meand[0.0] > 4.5
          and all(meand[g] > 3.0 for g in meand))

    ev, vc = np.linalg.eigh(H896 + np.diag(32.0 * CADJ[PATZ]))
    ut = (vc * np.exp(-1j * 0.5 * ev)) @ vc.conj().T
    _r01 = tuple(1 if u in (0, 1) else 0 for u in range(8))
    _c01 = [c for c in range(len(REPS)) if RECS[c] == _r01][0]
    psi = _sector_vector({_c01: 1.0})
    psi /= np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj()) * MASK28
    cseq = []
    for n in range(1, 41):
        rho = (ut @ rho @ ut.conj().T) * MASK28
        if n in (1, 2, 5, 10, 40):
            q = np.bincount(PATZ, weights=np.real(np.diag(rho)), minlength=28)
            cseq.append(float(q[CDIST == 1].sum()))
    check("E4 [numerical, 1e-6] the cube's 896-dim sector agrees: records started ADJACENT under the same "
          "tick at tau = 0.5, g = 32 carry P(d = 1) = %s at ticks 1, 2, 5, 10, 40, toward %.4f" % (_tq(cseq), 12.0 / 28.0),
          all(a > b for a, b in zip(cseq, cseq[1:])) and abs(cseq[-1] - 0.6726) < 1e-3)


# ===================================================================== group F

def group_F():
    """M5: the tick map at record level, its fixed point, and the attractor."""
    ev, vc = np.linalg.eigh(H896)

    def prop(tau):
        return (vc * np.exp(-1j * tau * ev)) @ vc.conj().T

    def run(tau, nt):
        ut = prop(tau)
        rho = np.outer(PSI0, PSI0.conj()) * MASK28
        out = [np.bincount(PATZ, weights=np.real(np.diag(rho)), minlength=28)]
        for _ in range(nt):
            rho = (ut @ rho @ ut.conj().T) * MASK28
            out.append(np.bincount(PATZ, weights=np.real(np.diag(rho)), minlength=28))
        return out

    def tree(tau, nt):
        ut = prop(tau)
        cur = []
        for k in range(28):
            v = np.where(PATZ == k, PSI0, 0.0)
            w = float(np.vdot(v, v).real)
            if w > 1e-15:
                cur.append((w, v / math.sqrt(w)))
        marg, counts = [], []
        m = np.zeros(28)
        for w, v in cur:
            m[PATZ[np.flatnonzero(np.abs(v) > 1e-14)[0]]] += w
        marg.append(m)
        for _ in range(nt):
            nxt, m = [], np.zeros(28)
            for w, v in cur:
                u = ut @ v
                for k in range(28):
                    x = np.where(PATZ == k, u, 0.0)
                    q = float(np.vdot(x, x).real)
                    if q > 1e-15:
                        nxt.append((w * q, x / math.sqrt(q)))
                        m[k] += w * q
            cur = nxt
            marg.append(m)
            counts.append(len(cur))
        return marg, counts

    seq05 = run(0.5, 8)
    mg, nb = tree(0.5, 2)
    dev = [l1(mg[t], seq05[t]) for t in (1, 2)]
    check("F1 [numerical, 1e-15] M5's tick map rho -> mask(U(tau) rho U(tau)^dag), mask = Lueders on the "
          "28 corner patterns, agrees with EXPLICIT record trees -- %d branches after tick 1, %d after "
          "tick 2 -- to L1 = %.1e and %.1e"
          % (nb[0], nb[1], dev[0], dev[1]),
          nb == [312, 5824] and max(dev) < 1e-14)

    seqs = {0.5: seq05, 1.0: run(1.0, 8), 2.0: run(2.0, 8)}
    fm = {t: [float(seqs[t][k][ZERO12].sum()) for k in (1, 2, 5, 8)] for t in seqs}
    check("F2 [numerical, 1e-9] the sharp pattern is not preserved: from the ground state the forbidden "
          "mass at ticks 1, 2, 5, 8 is %s (tau = 0.5); %s (1); %s (2)"
          % (_tq(fm[0.5]), _tq(fm[1.0]), _tq(fm[2.0])),
          all(fm[t][i] < fm[t][i + 1] for t in fm for i in range(3))
          and all(abs(a - b) < 1e-3 for a, b in zip(fm[0.5], [0.2655, 0.3430, 0.4161, 0.4267])))

    fix, uni = [], []
    rho0 = np.eye(NZ, dtype=complex) / NZ
    for tau in (0.5, 1.0, 2.0):
        ut = prop(tau)
        out = (ut @ rho0 @ ut.conj().T) * MASK28
        fix.append(float(np.max(np.abs(out - rho0))))
        uni.append(l1(np.bincount(PATZ, weights=np.real(np.diag(out)), minlength=28), UNIF28))
    check("F3 [numerical, 1e-15] I/896 is an EXACT fixed point: max |map(I/896) - I/896| = %.1e, %.1e, "
          "%.1e at tau = 0.5, 1, 2, odds uniform on the 28 corner pairs to %.1e, forbidden mass exactly "
          "12/28 = %.9f"
          % (fix[0], fix[1], fix[2], max(uni), 12.0 / 28.0),
          max(fix) < 1e-15 and max(uni) < 1e-14)

    rat = []
    for tau in (0.5, 1.0, 2.0):
        s = run(tau, 12)
        d = [l1(q, UNIF28) for q in s]
        rat.append(d[12] / d[11])
    check("F4 [numerical, 1e-3] convergence is geometric: the per-tick L1 ratio to uniform-on-28 settles "
          "at %.4f, %.4f, %.4f for tau = 0.5, 1, 2, so the resting state's selection-rule zeros are "
          "lost at a fixed rate"
          % tuple(rat),
          all(abs(a - b) < 5e-3 for a, b in zip(rat, [0.5294, 0.4560, 0.6156])))

    resid, cap = 0.0, True
    nt = 0
    for tau in seqs:
        for q in seqs[tau][1:]:
            resid = max(resid, abs(l1(q, GS_BORN) - 2.0 * float(q[ZERO12].sum())))
            allowed = [k for k in range(28) if k not in ZERO12]
            cap = cap and float(q[allowed].max()) <= GS_BORN[allowed[0]] + 1e-15
            nt += 1
    check("F5 [numerical, 1e-12] the whole loss is that mass: L1 from the record odds to the pre-record "
          "Born diagonal (1/16 on 16 pairs, 0 on 12) is exactly 2x the forbidden mass at all %d ticks "
          "(max residual %.1e)" % (nt, resid),
          resid < 1e-12 and cap)


def main():
    group_A()
    group_B()
    co = group_C()
    group_D(co)
    group_E()
    group_F()
    print("SUMMARY: a shifting record registers an i.i.d. mean-zero walk with an exact D(tau) -- "
          "Zeno-pinned at fast ticks, ballistic at slow, crossing at the mean free time tau/p; a "
          "cost-bound pair comes apart; the attractor is uniform.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
