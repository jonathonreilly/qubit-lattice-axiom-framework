#!/usr/bin/env python3
"""Finite cube edge-qubit conditioning, schedules, and equality kernel.

This self-contained runner studies an abstract 2x2x2 cube graph with one qubit
on each of its 12 edges.  Vertex parity and occupation are basis labels only.
No physical-site, measurement, record-formation, or framework interpretation is
made.

The runner establishes six bounded results in the 896-dimensional weight-two
parity sector:

  A  exact encoding relations, sector closure, spectrum, and a chosen -4
     eigenvector with 384 coordinate zeros;
  B  the coordinate Born law and order independence of commuting masks;
  C  exact local leakage coefficients for a declared conditioned generator;
  D  a zero common action-equality kernel for explicitly stated equations;
  E  five deterministic distributions for one state, tau=0.5, and five named
     masking/evolution schedules with the same terminal coordinate support;
  F  the exact completion law for 12 independent geometric clocks, 0<p<=1.

`[exact]` lines use integer, binary, Gaussian-integer, or Fraction arithmetic.
`[numerical]` lines are deterministic double-precision evaluations pinned at
the displayed precision. Output is fail-closed: one PASS/FAIL line per check,
then `TOTAL: PASS=N FAIL=M`; exit code is nonzero iff any check fails.
"""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from functools import reduce

import numpy as np

AUDIT_TIMEOUT_SEC = 120

PASS = 0
FAIL = 0


def check(label, cond):
    """Evaluate and print one fail-closed check."""
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

    def parity(self, z):
        """The vertex-parity dictionary n_v = (1 - B_v)/2 for a bit string."""
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
    recs = [E.parity(reps[c]) for c in range(len(reps))]
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
KST = AUD["k"]

# the weight-two parity sector: 896 bit strings whose vertex-parity vector has weight two
_rec = np.array([EN.parity(z) for z in range(EN.DIM)], dtype=np.int8)
ZL = np.flatnonzero(_rec.sum(1) == 2).astype(np.int64)
NZ = len(ZL)
POSZ = -np.ones(EN.DIM, dtype=np.int64)
POSZ[ZL] = np.arange(NZ)

PAIRS = [(i, j) for i in range(8) for j in range(i + 1, 8)]
PIDX = {p: i for i, p in enumerate(PAIRS)}
PATZ = np.array([PIDX[tuple(np.flatnonzero(_rec[z]))] for z in ZL], dtype=np.int64)

# the hop terms, carried onto the sector.  Each is a signed partial permutation.
_HP = {e: EN.hop_pauli(*e) for e in EN.EDGES}
TGT = np.zeros((NQ, NZ), dtype=np.int64)
AMP = np.zeros((NQ, NZ), dtype=complex)
SECTOR_CLOSED = True
AMPS_UNIT = True
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
        if _amp.real != 0 or abs(_amp.imag) != 1:
            AMPS_UNIT = False
        TGT[_q, _a] = POSZ[_zz]
        AMP[_q, _a] = _amp

H896 = np.zeros((NZ, NZ), dtype=complex)
for _q in range(NQ):
    _m = AMP[_q] != 0
    H896[TGT[_q][_m], np.flatnonzero(_m)] += AMP[_q][_m]
H_HERM = bool(np.max(np.abs(H896 - H896.conj().T)) == 0)
FREEQ = [np.array([q for q in range(NQ) if not (mask >> q) & 1], dtype=np.int64)
         for mask in range(1 << NQ)]

# the 28 code cosets of the sector, the exact gauge, and the E = -4 ground state
SEL, _POSC, HOFF, HOFF_EXACT = sector_matrix(
    EN, AUD, CID, PHI, REPS, RECS, lambda r: sum(r) == 2)
PATS28 = [RECS[c] for c in SEL]
_JWIDX, TJW = fermi_sector(EN.EDGES, PATS28)
GAUGE = gauge_match(HOFF, TJW)
TINT = np.round(TJW).astype(np.int64)
SPEC28 = [-4, -2, 0, 2, 4]


def _chi(s, u):
    return -1 if pcnt(s & u) % 2 else 1


def slater(s, t):
    w = np.zeros(len(PATS28), dtype=np.int64)
    for a, p in enumerate(PATS28):
        u, x = [i for i, b in enumerate(p) if b]
        w[a] = _chi(s, u) * _chi(t, x) - _chi(s, x) * _chi(t, u)
    return w


_SLATER_PAIRS = list(itertools.combinations(range(8), 2))
_SLATER_VECTORS = [slater(s, t) for s, t in _SLATER_PAIRS]
_SLATER_GRAM = np.stack(_SLATER_VECTORS, axis=1).T @ np.stack(_SLATER_VECTORS, axis=1)
SLATER_BASIS_EXACT = bool(
    np.array_equal(_SLATER_GRAM, np.diag(np.diag(_SLATER_GRAM)))
    and np.all(np.diag(_SLATER_GRAM) > 0)
)
SLATER_EIGENVALUES = []
for _v in _SLATER_VECTORS:
    _matches = [_e for _e in SPEC28 if np.array_equal(TINT @ _v, _e * _v)]
    SLATER_EIGENVALUES.append(_matches[0] if len(_matches) == 1 else None)
SPEC28_EXACT = SLATER_BASIS_EXACT and sorted(set(SLATER_EIGENVALUES)) == SPEC28


WGS = slater(0, 4)
assert GAUGE is not None


def _sector_vector(amps):
    v = np.zeros(NZ, dtype=complex)
    for a in range(NZ):
        c = CID[int(ZL[a])]
        A = amps.get(c, 0.0)
        if A:
            v[a] = A * PHI[int(ZL[a])]
    return v


_GU = None
for _cj in (True, False):
    _amps = {SEL[a]: complex(WGS[a]) * (np.conj(GAUGE[a]) if _cj else GAUGE[a])
             for a in range(len(SEL)) if WGS[a]}
    _v = _sector_vector(_amps)
    if np.max(np.abs(H896 @ _v + 4.0 * _v)) < 1e-9:
        _GU = _v
        break
assert _GU is not None, "ground state gauge convention"

# the chosen state, held exactly as a Gaussian-integer vector over sqrt(NRM)
GU = np.round(_GU.real) + 1j * np.round(_GU.imag)
GU_EXACT = bool(np.max(np.abs(GU - _GU)) == 0)
NRM = int(round(float(np.vdot(GU, GU).real)))
PSI0 = GU / math.sqrt(NRM)
GS_EIG = bool(np.array_equal(H896 @ GU, -4 * GU))


def born28(psi):
    """The odds over the 28-pattern dictionary carried by a sector state."""
    return np.bincount(PATZ, weights=np.abs(psi) ** 2, minlength=28)


def born28_exact(u, nrm):
    """Exact `Fraction` odds of a Gaussian-integer sector vector u / sqrt(nrm)."""
    num = np.bincount(PATZ, weights=np.abs(u) ** 2, minlength=28)
    return [Fraction(int(round(x)), nrm) for x in num]


GS_BORN = born28(PSI0)
GS_BORN_EX = born28_exact(GU, NRM)
ZERO12 = [k for k in range(28) if GS_BORN_EX[k] == 0]
QMASK = np.isin(PATZ, ZERO12)
UNIF28 = np.full(28, 1.0 / 28.0)

# the 4 cross-face edge sites (bit 4 -- they join the two x-faces) and the 8 in-face
CROSS = [q for q, (i, j) in enumerate(EN.EDGES) if (i ^ j) == 4]
INFACE = [q for q in range(NQ) if q not in CROSS]


def l1(a, b):
    return float(np.abs(np.asarray(a) - np.asarray(b)).sum())


# ======================================================= conditioned blocks

BCACHE = {}
CACHE_LEVEL = 3
_LOC = -np.ones(NZ, dtype=np.int64)


def block_index(Rmask, wbits):
    return np.flatnonzero((ZL & Rmask) == wbits)


def block_matrix(I, Rmask):
    """H_R restricted to the block: the terms on unmasked edge coordinates."""
    d = len(I)
    _LOC[I] = np.arange(d)
    Hb = np.zeros((d, d), dtype=complex)
    cols = np.arange(d)
    for q in FREEQ[Rmask]:
        a = AMP[q][I]
        m = a != 0
        if m.any():
            Hb[_LOC[TGT[q][I][m]], cols[m]] = a[m]
    _LOC[I] = -1
    return Hb


def get_block(Rmask, wbits):
    """(index set, eigenvalues, eigenvectors) of H_R on the conditioned block."""
    key = (Rmask, wbits)
    v = BCACHE.get(key)
    if v is not None:
        return v
    I = block_index(Rmask, wbits)
    d = len(I)
    if d == 1:
        res = (I, np.zeros(1), np.ones((1, 1), dtype=complex))
    else:
        Ev, Vc = np.linalg.eigh(block_matrix(I, Rmask))
        res = (I, Ev, Vc)
    if pcnt(Rmask) <= CACHE_LEVEL:
        BCACHE[key] = res
    return res


def evolve(psi, Ev, Vc, t):
    if psi.shape[0] == 1 or t == 0:
        return psi
    return Vc @ (np.exp(-1j * t * Ev) * (Vc.conj().T @ psi))


# ===================================================== exact fixed schedules

def exact_schedule(psi0, stages, tau):
    """The deterministic terminal distribution for a declared schedule.

    ``stages`` lists ``(gap, coordinates masked)`` pairs.  The complete
    conditioning tree is enumerated; there is no sampling.
    """
    nodes = [(0, 0, get_block(0, 0), psi0, 1.0)]
    for gap, sites in stages:
        Smask = 0
        for q in sites:
            Smask |= 1 << q
        out = []
        for Rmask, wbits, blk, psi, pr in nodes:
            I, Ev, Vc = blk
            if gap > 0:
                psi = evolve(psi, Ev, Vc, gap * tau)
            keys = ZL[I] & Smask
            w = np.abs(psi) ** 2
            uk, inv = np.unique(keys, return_inverse=True)
            wk = np.bincount(inv, weights=w)
            for a in range(len(uk)):
                if wk[a] < 1e-14:
                    continue
                nR, nw = Rmask | Smask, wbits | int(uk[a])
                blk2 = get_block(nR, nw)
                sub = psi[np.searchsorted(I, blk2[0])]
                out.append((nR, nw, blk2, sub / np.linalg.norm(sub), pr * wk[a]))
        nodes = out
    res = np.zeros(28)
    for Rmask, wbits, blk, psi, pr in nodes:
        res[PATZ[blk[0][0]]] += pr
    return res


SCHED = {
    "A all 12 at tick 1": [(0, list(range(12)))],
    "B one per tick, 0..11": [(0, [0])] + [(1, [q]) for q in range(1, 12)],
    "C one per tick, 11..0": [(0, [11])] + [(1, [q]) for q in range(10, -1, -1)],
    "D one every 5 ticks": [(0, [0])] + [(5, [q]) for q in range(1, 12)],
    "E two per tick, 6 ticks": [(0, [0, 1])] + [(1, [2 * i, 2 * i + 1]) for i in range(1, 6)],
}
SRES = {}

# ===================================================================== group A


def group_A():
    check("A1 [exact] cube 2x2x2, 8 corners / %d edge sites / 6 faces: superfast relations R0-R4 "
          "hold pair by pair, no -I in the face group, k = %d, code dim 2^%d/2^%d = %d"
          % (NQ, KST, NQ, KST, AUD["code_dim"]),
          all(AUD[t] for t in ("R0", "R1", "R2", "R3", "R4", "grp_ok"))
          and KST == 5 and AUD["code_dim"] == 128)
    check("A2 [exact] the weight-two parity sector is %d-dimensional = %d vertex pairs x %d, and every "
          "one of the %d hop terms carries it onto itself with unit Gaussian-integer amplitudes"
          % (NZ, 28, 1 << KST, NQ),
          NZ == 896 and len(set(PATZ.tolist())) == 28
          and all(int((PATZ == k).sum()) == 32 for k in range(28))
          and SECTOR_CLOSED and AMPS_UNIT and H_HERM)
    check("A3 [exact] the code sector of the %d cosets: 2^%d H_enc is Gaussian-integer, an exact "
          "diagonal gauge in {1, i, -1, -i} carries it entrywise onto the reference matrix, and "
          "28 mutually orthogonal integer Slater vectors give the complete spectrum %s"
          % (len(SEL), KST, SPEC28),
          len(SEL) == 28 and HOFF_EXACT and GAUGE is not None and SPEC28_EXACT
          and SPEC28 == [-4, -2, 0, 2, 4])
    pairs = [PAIRS[k] for k in ZERO12]
    check("A4 [exact] the E = -4 ground state is an exact eigenvector, its amplitudes are "
          "Gaussian integers over sqrt(%d), and it carries %d cancellation zeros = %d corner "
          "pairs x %d, exactly the pairs sharing an x-face"
          % (NRM, int(QMASK.sum()), len(ZERO12), 1 << KST),
          GS_EIG and GU_EXACT and int(QMASK.sum()) == 384 and len(ZERO12) == 12
          and all((u >> 2) == (v >> 2) for u, v in pairs))
    check("A5 [exact] the %d cross-face sites %s are the edge sites joining the two x-faces; the "
          "other %d lie inside one x-face"
          % (len(CROSS), [EN.EDGES[q] for q in CROSS], len(INFACE)),
          len(CROSS) == 4 and len(INFACE) == 8
          and all((EN.EDGES[q][0] >> 2) != (EN.EDGES[q][1] >> 2) for q in CROSS)
          and all((EN.EDGES[q][0] >> 2) == (EN.EDGES[q][1] >> 2) for q in INFACE))


# ===================================================================== group B

def group_B():
    SRES["A all 12 at tick 1"] = exact_schedule(PSI0, SCHED["A all 12 at tick 1"], 0.5)
    ex = [Fraction(0)] * 28
    for a in range(NZ):
        ex[PATZ[a]] += Fraction(int(round(abs(GU[a]) ** 2)), NRM)
    check("B1 [exact] a full coordinate measurement before evolution reproduces the basis Born law: "
          "the aggregated 28-outcome distribution has 16 entries 1/16 and %d zeros, total %s"
          % (sum(1 for x in ex if x == 0), sum(ex)),
          ex == GS_BORN_EX and sum(ex) == 1
          and ex.count(Fraction(1, 16)) == 16 and ex.count(Fraction(0)) == 12
          and l1(SRES["A all 12 at tick 1"], GS_BORN) < 1e-12)
    zc = True
    for q1, q2 in itertools.combinations(range(NQ), 2):
        a = P(0, 0, 1 << q1)
        b = P(0, 0, 1 << q2)
        zc = zc and (a * b) == (b * a)
    bad = npair = 0
    for q1, q2 in itertools.combinations(range(NQ), 2):
        for b1 in (0, 1):
            for b2 in (0, 1):
                npair += 1
                m1 = ((ZL >> q1) & 1) == b1
                m2 = ((ZL >> q2) & 1) == b2
                u = GU * m1 * m2
                w = GU * m2 * m1
                if not np.array_equal(u, w):
                    bad += 1
    check("B2 [exact] coordinate-mask order leaves no trace: all %d Z_e pairs commute in the "
          "symplectic representation, and over all %d ordered (site, value) comparisons the two "
          "conditioned states agree entrywise -- %d mismatches"
          % (NQ * (NQ - 1) // 2, npair, bad), zc and bad == 0 and npair == 264)
    ords = 0
    good = True
    nz = np.flatnonzero(GU != 0)
    targets = [int(ZL[a]) for a in (nz[0], nz[len(nz) // 3], nz[-1])]
    for seed in range(20):
        order = [int(x) for x in np.random.default_rng(seed).permutation(NQ)]
        ords += 1
        for z in targets:
            live = np.ones(NZ, dtype=bool)
            den = Fraction(NRM)
            joint = Fraction(1)
            for q in order:
                nxt = live & ((((ZL >> q) & 1) == ((z >> q) & 1)))
                num = int(round(float((np.abs(GU[nxt]) ** 2).sum())))
                joint *= Fraction(num, den)
                den = Fraction(num)
                live = nxt
            good = good and joint == Fraction(int(round(abs(GU[POSZ[z]]) ** 2)), NRM)
    check("B3 [exact] walking the chain rule along %d shuffled full mask orders, on three "
          "target bit patterns each, closes every time on the Born value of that pattern: "
          "%d products, all equal as Fractions" % (ords, ords * len(targets)),
          good and ords == 20)


# ===================================================================== group C

def _gauss(v):
    """Assert a Gaussian-integer vector and return exact |v|^2 as an int."""
    r = np.round(v.real) + 1j * np.round(v.imag)
    assert np.max(np.abs(r - v)) < 1e-9
    return int(round(float(np.vdot(r, r).real))), r


def group_C():
    var_R, var_H, leak, cubic, wts = {}, {}, {}, {}, {}
    for q in range(NQ):
        for b in (0, 1):
            u = GU * (((ZL >> q) & 1) == b)
            n2, u = _gauss(u)
            HR = H896.copy()
            m = AMP[q] != 0
            HR[TGT[q][m], np.flatnonzero(m)] -= AMP[q][m]
            h = HR @ u
            hn2, h = _gauss(h)
            e1 = Fraction(int(round(float(np.vdot(u, h).real))), n2)
            var_R[(q, b)] = Fraction(hn2, n2) - e1 * e1
            hf = H896 @ u
            hfn2, hf = _gauss(hf)
            ef = Fraction(int(round(float(np.vdot(u, hf).real))), n2)
            var_H[(q, b)] = Fraction(hfn2, n2) - ef * ef
            qn2, _ = _gauss(h * QMASK)
            leak[(q, b)] = Fraction(qn2, n2)
            h2n, h2 = _gauss(HR @ h)
            del h2n
            cubic_num = int(round(float(np.vdot(h * QMASK, h2 * QMASK).imag)))
            cubic[(q, b)] = Fraction(cubic_num, n2)
            wts[(q, b)] = Fraction(n2, NRM)
    vin = {var_R[(q, b)] for q in INFACE for b in (0, 1)}
    vcr = {var_R[(q, b)] for q in CROSS for b in (0, 1)}
    check("C1 [exact] one coordinate mask breaks the eigenvector property: conditioning the chosen "
          "state on either outcome at one edge coordinate gives var(H_R) = %s on the %d in-face "
          "coordinates and %s on the %d cross-face coordinates, never 0"
          % (vin.pop() if len(vin) == 1 else sorted(map(str, vin)), len(INFACE),
             vcr.pop() if len(vcr) == 1 else sorted(map(str, vcr)), len(CROSS)),
          {var_R[(q, b)] for q in INFACE for b in (0, 1)} == {Fraction(1, 4)}
          and {var_R[(q, b)] for q in CROSS for b in (0, 1)} == {Fraction(3, 8)}
          and all(v != 0 for v in var_R.values()))
    vh = set(var_H.values())
    check("C2 [exact] the chosen state is an exact eigenvector of H (var = 0), while every "
          "one of the %d coordinate-conditioned states has var(H) = %s"
          % (len(var_H), sorted(map(str, vh))[0]),
          vh == {Fraction(3, 4)} and all(v == Fraction(1, 2) for v in wts.values()))
    lin = {leak[(q, b)] for q in INFACE for b in (0, 1)}
    lcr = {leak[(q, b)] for q in CROSS for b in (0, 1)}
    coef = sum(wts[(q, b)] * leak[(q, b)] for q in range(NQ) for b in (0, 1)) / NQ
    check("C3 [exact] ||Q H_R |g_b>||^2 = %s on the in-face sites and %s on the cross-face sites, "
          "so the generator carries the conditioned state OUT of the zero set at first order in "
          "tau" % (sorted(map(str, lin))[0], sorted(map(str, lcr))[0]),
          lin == {Fraction(0)} and lcr == {Fraction(3, 8)})
    check("C4 [exact] the averaged projected mass after one mask and one evolution interval is "
          "m(t) = c t^2 + O(t^4): c = (1/%d) sum_e sum_b w_eb ||Q H_R |g_eb>||^2 = %s, "
          "and every one of the 24 exact cubic coefficients is zero"
          % (NQ, coef), coef == Fraction(1, 8) and set(cubic.values()) == {Fraction(0)})
    times = (0.01, 0.1, 0.5, 2.0)
    vals = []
    for t in times:
        tot = 0.0
        for q in range(NQ):
            for b in (0, 1):
                I, Ev, Vc = get_block(1 << q, b << q)
                v = PSI0[I]
                w = float(np.vdot(v, v).real)
                v = evolve(v / math.sqrt(w), Ev, Vc, t)
                tot += (w / NQ) * float((np.abs(v[QMASK[I]]) ** 2).sum())
        vals.append(tot)
    expected = np.array([
        1.2499583337962187e-05,
        0.0012458378813747014,
        0.028693840474726454,
        0.11867214924360606,
    ])
    check("C5 [numerical, abs<=1e-12] m(t) at pinned t = 0.01, 0.1, 0.5, 2.0 is %s; "
          "m(0.01)/0.01^2 = %.5f against c = 0.125"
          % (", ".join("%.6f" % x for x in vals), vals[0] / 1e-4),
          times == (0.01, 0.1, 0.5, 2.0)
          and np.max(np.abs(np.asarray(vals) - expected)) <= 1e-12)


# ===================================================================== group D

def group_D():
    dead = int(sum(1 for a in range(NZ) if all(AMP[q][a] == 0 for q in range(NQ))))
    # Common action-equality kernel of {H_R - H_R'} and {H_R - H}: each condition couples two
    # coordinates by a unit ratio, so union-find with a phase in Z4 is exact.
    par = list(range(NZ))
    pot = [0] * NZ
    zero = [False] * NZ

    def froot(a):
        s = 0
        while par[a] != a:
            s = (s + pot[a]) % 4
            a = par[a]
        return a, s

    def unite(i1, i2, ph):
        r1, s1 = froot(i1)
        r2, s2 = froot(i2)
        if r1 == r2:
            if (s1 - s2 - ph) % 4 != 0:
                zero[r1] = True
            return
        par[r1] = r2
        pot[r1] = (ph + s2 - s1) % 4
        if zero[r1]:
            zero[r2] = True

    def mark(i):
        r, _ = froot(i)
        zero[r] = True

    conds = 0
    for b in range(NZ):
        # (T_q v)[b] = AMP[q, b^q] v[b^q]: the source index and its unit amplitude
        src = []
        for q in range(NQ):
            zb = int(ZL[b]) ^ (1 << q)
            a = POSZ[zb]
            if a >= 0 and AMP[q][a] != 0 and TGT[q][a] == b:
                src.append((int(a), AMP[q][a]))
            else:
                src.append((-1, 0j))
        for q in range(NQ):
            i1, c1 = src[q]
            # H_R - H = -T_q : the condition (T_q v)[b] = 0
            conds += 1
            if c1 != 0:
                mark(i1)
        for q1, q2 in itertools.combinations(range(NQ), 2):
            i1, c1 = src[q1]
            i2, c2 = src[q2]
            conds += 1
            if c1 == 0 and c2 == 0:
                continue
            if c1 == 0:
                mark(i2)
            elif c2 == 0:
                mark(i1)
            else:
                ph = unit_index(c2 / c1)
                unite(i1, i2, ph)
    for a in range(NZ):
        r, _ = froot(a)
        if zero[r]:
            zero[a] = True
    comps = {}
    for a in range(NZ):
        r, _ = froot(a)
        comps.setdefault(r, []).append(a)
    dim = sum(1 for r, mem in comps.items() if not zero[r])
    check("D1 [exact] every one of the %d sector basis patterns is acted on by at least one term: "
          "%d are annihilated by all %d of them, so the joint kernel of {H_R - H} over the "
          "%d single-coordinate masks is already 0" % (NZ, dead, NQ, NQ), dead == 0)
    check("D2 [exact] the common action-equality kernel of {H_R - H_R'} over all %d pairs of "
          "single-coordinate masks, together with {H_R - H}, has dimension %d on the "
          "%d-dimensional sector -- %d unit-ratio conditions closed by union-find in Z4"
          % (NQ * (NQ - 1) // 2, dim, NZ, conds), dim == 0)
    comms = [H896 @ Tq - Tq @ H896 for Tq in (_tq(q) for q in range(NQ))]
    norm2 = [int(np.max(np.round(C.real) ** 2 + np.round(C.imag) ** 2)) for C in comms]
    exact_comms = all(
        np.array_equal(C.real, np.round(C.real))
        and np.array_equal(C.imag, np.round(C.imag)) for C in comms
    )
    check("D3 [exact] every one of the %d term matrices has nonzero commutator with H; "
          "each entrywise squared maximum is 1" % NQ,
          exact_comms and norm2 == [1] * NQ)


def _tq(q):
    T = np.zeros((NZ, NZ), dtype=complex)
    m = AMP[q] != 0
    T[TGT[q][m], np.flatnonzero(m)] = AMP[q][m]
    return T


# ===================================================================== group E

def group_E():
    tau = 0.5
    for k, s in SCHED.items():
        if k not in SRES:
            SRES[k] = exact_schedule(PSI0, s, tau)
    keys = list(SCHED)
    fm = [float(SRES[k][ZERO12].sum()) for k in keys]
    dg = [l1(SRES[k], GS_BORN) for k in keys]
    expected_fm = np.array([
        0.0, 0.5351269054666328, 0.3337405248788735,
        0.14798987244388517, 0.2603867692315665,
    ])
    expected_dg = np.array([
        0.0, 1.1023355969148596, 0.7704538825748932,
        0.6919682523557236, 0.5513993863148097,
    ])
    check("E1 [numerical, abs<=1e-12] tau = 0.5 and five named schedules with the same terminal "
          "12-coordinate support give projected masses %s"
          % ", ".join("%.6f" % x for x in fm),
          tau == 0.5 and np.max(np.abs(np.asarray(fm) - expected_fm)) <= 1e-12)
    check("E2 [numerical, abs<=1e-12] their L1 distances to the chosen state's aggregated "
          "basis Born law are %s" % ", ".join("%.4f" % x for x in dg),
          np.max(np.abs(np.asarray(dg) - expected_dg)) <= 1e-12)
    ab = l1(SRES[keys[0]], SRES[keys[1]])
    bc = l1(SRES[keys[1]], SRES[keys[2]])
    mn = min(l1(SRES[a], SRES[b]) for a, b in itertools.combinations(keys, 2))
    check("E3 [numerical, abs<=1e-12] pairwise L1(A,B) = %.4f, L1(B,C) = %.4f, and the "
          "smallest of all ten pairwise distances is %.4f"
          % (ab, bc, mn),
          abs(ab - 1.1023355969148596) <= 1e-12
          and abs(bc - 0.9027794461083645) <= 1e-12
          and abs(mn - 0.5513993863148097) <= 1e-12)


# ===================================================================== group F

def group_F():
    rows = []
    ok = True
    for p in (Fraction(1), Fraction(1, 2), Fraction(1, 5), Fraction(1, 20), Fraction(1, 100)):
        q = 1 - p
        ex = sum(Fraction((-1) ** (j + 1) * math.comb(12, j)) / (1 - q ** j)
                 for j in range(1, 13))
        # exact finite cross-check of the inclusion-exclusion identity: the partial sum
        # of P(T > t) plus its exact remainder must reproduce the closed form
        Tt = 8
        ser = sum(1 - (1 - q ** t) ** 12 for t in range(Tt))
        rem = sum(Fraction((-1) ** (j + 1) * math.comb(12, j)) * q ** (j * Tt) / (1 - q ** j)
                  for j in range(1, 13))
        ok = ok and ser + rem == ex and all(
            (1 - q ** t) ** 12 >= (1 - q ** (t - 1)) ** 12 for t in range(1, 9))
        rows.append((p, ex))
    expected = [
        Fraction(1),
        Fraction(203832594062416, 40955189998905),
        Fraction(19410853937858690418616567026118915,
                 1347340588032364928168995722610899),
        Fraction(1806702053597737741454779841482864335766928719474635681799326160,
                 29618384818426198324210669167860314389050213947312879104906669),
        Fraction(6853014768829291665870583913742115754746362709960333836541185991904889289383269907581677173098800,
                 22158904100321171765429654907053489398811258558366417681966701227794876576051780341081131714799),
    ]
    check("F1 [exact] for 0<p<=1, each of 12 independent coordinates activates with probability "
          "p per integer tick, so completion T=max(T_1,...,T_12) has "
          "P(T <= t) = (1 - (1-p)^t)^12 "
          "and E[T] = sum_j (-1)^(j+1) C(12,j)/(1 - (1-p)^j), cross-checked exactly against the "
          "partial sum of P(T > t) plus its exact remainder, at all %d values of p"
          % len(rows), ok and [x for _, x in rows] == expected)
    check("F2 [exact values; decimal display] E[T] at p = 1, 1/2, 1/5, 1/20, 1/100 is "
          "approximately %s"
          % ", ".join("%.3f" % float(e) for _, e in rows),
          [x for _, x in rows] == expected)
    p = Fraction(1, 2)
    cdf = [(1 - (1 - p) ** t) ** 12 for t in (1, 3, 5, 7)]
    expected_cdf = [
        Fraction(1, 4096),
        Fraction(13841287201, 68719476736),
        Fraction(787662783788549761, 1152921504606846976),
        Fraction(17605349516220764271966721, 19342813113834066795298816),
    ]
    check("F3 [exact values; decimal display] at p = 1/2, P(T<=t) for integer "
          "t = 1, 3, 5, 7 is approximately %s"
          % ", ".join("%.5f" % float(x) for x in cdf),
          cdf == expected_cdf)


def main():
    for g in (group_A, group_B, group_C, group_D, group_E, group_F):
        g()
    print("SUMMARY: six bounded results for an abstract finite edge-qubit model: exact sector "
          "algebra, mask conditioning, local projected leakage, a common action-equality kernel, "
          "five pinned schedule distributions, and an independent geometric-clock law.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
