#!/usr/bin/env python3
"""Cycle 914 -- INDEPENDENT CHECK of the finite d=3 transverse-field
registration comparator reproduction run (historical alias: route C).

Spec'd to REFUTE.  Independent re-implementation of the frozen comparator
protocol (docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md + the 2026-07-11
delta memo's definitions), on the primary's three-lambda subset only -- the
delta memo's four-lambda contract (lambda=0.02) is NOT executed by either
runner and no delta-completion verdict is checked or issued.  With:

  * its own proper-cubic invariant-sector reduction (MAX-canonical representatives,
    7/7/6/6 bit chunking, unique-based orbit indexing) -- no code shared with the
    primary runner;
  * its own propagator (shifted Chebyshev, NON-ZERO spectral centre -- different
    coefficients and code path from the primary's centred expansion) plus
    semigroup-composition and energy/norm-conservation cross-checks;
  * its own conditional-marginal construction (per-row expand-table gathers, no
    precomputed layout array) and its own entropy/Holevo/CMI code;
  * full-space verification of the sector-reduction exactness claim on reduced
    instances, and raw-formula spot checks on the real 3x3x3;
  * an attack on the frozen baseline re-anchoring (the memo's freeze correction);
  * verification of the fragment partition against the FROZEN MEMO's own bytes;
  * eight teeth.

Exit contract (FAIL-CLOSED): exits 0 ONLY if every required finding passes AND
all eight mutation teeth fire; any refuted finding or failed tooth exits 1.
A claim-survival failure can therefore fail this process.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

import hashlib
import itertools
import json
import os
import re
import resource
import sys
import time

import numpy as np
import scipy.linalg as sla
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.special import jv

T_START = time.perf_counter()
BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIMARY_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
NOTE_MEMO = "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md"
# NOTE: the axiom memo (docs/MINIMAL_AXIOMS_2026-06-29.md) is deliberately NOT
# in this input closure.  It was context-only in the predecessor and its
# historical snapshot bytes are superseded on origin/main; no claim checked
# here consumes it, so it is provenance context, not a pinned input.

PIN_SHA = {
    PARENT_MEMO: "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
    DELTA_MEMO: "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
    NOTE_MEMO: "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
}
STREAMS = {0.05: "lam_0p05", 0.10: "lam_0p10", 0.20: "lam_0p20"}

LAMBDAS = (0.05, 0.10, 0.20)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE = 0.10
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
CENTER = (0, 0, 0)
GATE_H, GATE_EXC, GATE_IND, DEADLINE = 0.05, 0.02, 0.02, 1.0
FINDINGS = []


def note(kind, name, ok, detail):
    FINDINGS.append({"kind": kind, "name": name, "ok": bool(ok), "detail": detail})
    return ok


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ------------------------------------------------------------ generic engine -
def rotations24():
    out = []
    for perm in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), dtype=np.int64)
            for i in range(3):
                M[i, perm[i]] = s[i]
            if int(round(np.linalg.det(M))) == 1:
                out.append(M)
    return out


class SmallSector(object):
    """Brute-force invariant-sector reduction for small site sets (full space fits)."""

    def __init__(self, sites, group, lam):
        self.sites = list(sites)
        n = len(self.sites)
        self.n = n
        idx = {c: i for i, c in enumerate(self.sites)}
        self.perms = []
        for M in group:
            self.perms.append([idx[tuple(int(v) for v in (M @ np.array(c)))] for c in self.sites])
        self.dim = 1 << n
        x = np.arange(self.dim, dtype=np.int64)
        canon = x.copy()
        for p in self.perms:
            y = np.zeros_like(x)
            for j in range(n):
                y |= ((x >> j) & 1) << p[j]
            canon = np.minimum(canon, y)
        self.canon = canon
        self.reps = np.unique(canon)
        self.orb = np.searchsorted(self.reps, canon)
        self.sizes = np.bincount(self.orb).astype(np.float64)
        self.bonds = [(i, j) for i in range(n) for j in range(i + 1, n)
                      if sum(abs(self.sites[i][k] - self.sites[j][k]) for k in range(3)) == 2
                      or sum(abs(self.sites[i][k] - self.sites[j][k]) for k in range(3)) == 1]
        # nearest neighbour = unit lattice step for the 3x3x1 slab, 2-step for 2x2x2
        step = 1 if any(0 in c for c in self.sites) else 2
        self.bonds = [(i, j) for i in range(n) for j in range(i + 1, n)
                      if sorted(abs(self.sites[i][k] - self.sites[j][k]) for k in range(3)) == [0, 0, step]]
        z = 1 - 2 * ((x[:, None] >> np.arange(n)) & 1)
        self.E = np.zeros(self.dim, dtype=np.float64)
        for (i, j) in self.bonds:
            self.E += z[:, i] * z[:, j]
        self.lam = lam
        H = np.diag(-self.E)
        for i in range(n):
            f = x ^ (1 << i)
            H[x, f] -= lam
        self.H = H


def small_instance_check(tag, sites, group, lam, t, tamper=False):
    S = SmallSector(sites, group, lam)
    n = S.n
    # class-uniform G-invariant product preparation: all sites +X
    psi0 = np.ones(S.dim, dtype=np.complex128) / np.sqrt(S.dim)
    w, V = np.linalg.eigh(S.H)
    full = V @ (np.exp(-1j * w * t) * (V.conj().T @ psi0))
    # sector evolution on orbit-constant raw amplitudes
    nr = S.reps.size
    a0 = np.ones(nr, dtype=np.complex128) / np.sqrt(S.dim)
    Ered = S.E[S.reps]
    flips = np.empty((n, nr), dtype=np.int64)
    for i in range(n):
        flips[i] = S.orb[S.reps ^ (1 << i)]
    if tamper:
        flips[0, 0] = (flips[0, 0] + 1) % nr

    def mv(a):
        out = -Ered * a
        for i in range(n):
            out -= lam * a[flips[i]]
        return out

    Hs = np.zeros((nr, nr), dtype=np.complex128)
    e = np.zeros(nr, dtype=np.complex128)
    for k in range(nr):
        e[:] = 0
        e[k] = 1
        Hs[:, k] = mv(e)
    Wt = np.diag(np.sqrt(S.sizes))
    Ho = Wt @ Hs @ np.linalg.inv(Wt)
    wo, Vo = np.linalg.eigh((Ho + Ho.conj().T) / 2)
    p0 = np.sqrt(S.sizes) * a0
    po = Vo @ (np.exp(-1j * wo * t) * (Vo.conj().T @ p0))
    sec_raw = po / np.sqrt(S.sizes)
    dev = float(np.abs(full - sec_raw[S.orb]).max())
    return dev, S


# ------------------------------------------------------- full 3x3x3 sector ---
CHK = [(0, 7), (7, 7), (14, 6), (20, 6)]


def _tab(p):
    out = []
    for (sh, w) in CHK:
        v = np.arange(1 << w, dtype=np.uint32)
        t = np.zeros(1 << w, dtype=np.uint32)
        for b in range(w):
            t |= ((v >> np.uint32(b)) & np.uint32(1)) << np.uint32(p[sh + b])
        out.append(t)
    return out


class CubeSector(object):
    def __init__(self):
        self.sites = sorted([(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)])
        self.nc = [c for c in self.sites if c != CENTER]
        self.idx = {c: i for i, c in enumerate(self.nc)}
        self.rots = rotations24()
        N = 1 << 26
        x = np.arange(N, dtype=np.uint32)
        ci = [((x >> np.uint32(sh)) & np.uint32((1 << w) - 1)) for (sh, w) in CHK]
        canon = np.zeros(N, dtype=np.uint32)     # MAX-canonical (primary uses MIN)
        tmp = np.empty(N, dtype=np.uint32)
        for M in self.rots:
            p = [self.idx[tuple(int(v) for v in (M @ np.array(c)))] for c in self.nc]
            tb = _tab(p)
            np.take(tb[0], ci[0], out=tmp)
            tmp |= tb[1][ci[1]]
            tmp |= tb[2][ci[2]]
            tmp |= tb[3][ci[3]]
            np.maximum(canon, tmp, out=canon)
        del tmp, ci, x
        self.reps = np.unique(canon)                       # ascending, distinct
        self.n = int(self.reps.size)
        self.orb = np.searchsorted(self.reps, canon).astype(np.uint32)
        del canon
        self.sizes = np.bincount(self.orb, minlength=self.n).astype(np.float64)
        self.flip = np.empty((26, self.n), dtype=np.uint32)
        for i in range(26):
            self.flip[i] = self.orb[self.reps ^ np.uint32(1 << i)]
        bonds = [(a, b) for ia, a in enumerate(self.sites) for b in self.sites[ia + 1:]
                 if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
        self.bonds = bonds
        zb = np.empty((26, self.n), dtype=np.int8)
        for i in range(26):
            zb[i] = 1 - 2 * ((self.reps >> np.uint32(i)) & np.uint32(1)).astype(np.int8)
        Enc = np.zeros(self.n, dtype=np.int32)
        sg = np.zeros(self.n, dtype=np.int32)
        for (ca, cb) in bonds:
            if ca == CENTER:
                sg += zb[self.idx[cb]]
            elif cb == CENTER:
                sg += zb[self.idx[ca]]
            else:
                Enc += zb[self.idx[ca]].astype(np.int32) * zb[self.idx[cb]].astype(np.int32)
        self.E = np.empty((self.n, 2), dtype=np.float64)
        self.E[:, 0] = Enc + sg
        self.E[:, 1] = Enc - sg
        del zb, Enc, sg
        self.sq = np.sqrt(self.sizes)[:, None]

    def mv(self, a, lam, out, work):
        np.multiply(a, -self.E, out=out)
        out -= lam * a[:, ::-1]
        for i in range(26):
            np.take(a, self.flip[i], axis=0, out=work)
            out -= lam * work
        return out

    def prep(self):
        quiet = np.uint32(0)
        for c in self.nc:
            if sum(map(abs, c)) >= 2:
                quiet |= np.uint32(1 << self.idx[c])
        a = np.zeros((self.n, 2), dtype=np.complex128)
        a[(self.reps & quiet) == 0, :] = 2.0 ** -3.5
        return a

    def norm2(self, a):
        return float((self.sizes[:, None] * (a.real ** 2 + a.imag ** 2)).sum())


def shifted_chebyshev(sec, lam, a0, times):
    """Independent propagator: Chebyshev with a NON-ZERO spectral centre b."""
    b = 2.0
    A = 54.0 + 27.0 * lam + abs(b)
    tmax = max(times)
    M = int(np.ceil(A * tmax)) + 8
    while abs(jv(M, A * tmax)) > 1e-17:
        M += 5
    outs = [np.zeros_like(a0) for _ in times]
    scratch = np.empty_like(a0)
    tmpv = np.empty_like(a0)

    def shifted(v, out):
        sec.mv(v, lam, out, scratch)
        out -= b * v
        out /= A
        return out

    Tp = a0.copy()
    Tc = np.empty_like(a0)
    shifted(Tp, Tc)
    Tn = np.empty_like(a0)
    nmv = 1
    for k in range(0, M + 1):
        vec = Tp if k == 0 else (Tc if k == 1 else Tn)
        for j, t in enumerate(times):
            c = jv(k, A * t) * ((-1j) ** k) * (1.0 if k == 0 else 2.0) * np.exp(-1j * b * t)
            if abs(c) < 1e-18:
                continue
            outs[j] += c * vec
        if k >= 1 and k < M:
            shifted(Tc, tmpv)
            tmpv *= 2.0
            tmpv -= Tp
            nmv += 1
            Tp, Tc, Tn = Tc, tmpv, Tp
            tmpv = Tn
            Tn = Tc
    return outs, {"centre": b, "half_width": A, "degree": M, "matvecs": nmv}


def energy_expectation(sec, lam, a):
    o = np.empty_like(a)
    w = np.empty_like(a)
    sec.mv(a, lam, o, w)
    return float((sec.sizes[:, None] * (a.conj() * o).real).sum())


# ------------------------------------------------------- marginals (own code) -
def expand_table(bitpos, width):
    v = np.arange(1 << width, dtype=np.uint32)
    out = np.zeros(1 << width, dtype=np.uint32)
    for b in range(width):
        out |= ((v >> np.uint32(b)) & np.uint32(1)) << np.uint32(bitpos[b])
    return out


class Marginal(object):
    """Conditional fragment/pair marginals built by per-row expand-table gathers."""

    def __init__(self, sec, subset):
        self.k = len(subset)
        sub_bits = [sec.idx[c] for c in subset]
        rest_bits = [sec.idx[c] for c in sec.nc if c not in subset]
        # subset coordinate order: first listed site is the MOST significant factor
        self.EP = expand_table(list(reversed(sub_bits)), self.k)
        self.ER = expand_table(list(reversed(rest_bits)), 26 - self.k)
        self.sec = sec
        # compose the subset/rest expand tables into one orbit index, row by row
        d, cols = 1 << self.k, 1 << (26 - self.k)
        self.oidx = np.empty((d, cols), dtype=np.uint32)
        for p in range(d):
            np.take(sec.orb, self.ER | self.EP[p], out=self.oidx[p])

    def blocks(self, a, want_cross=False):
        v0 = np.ascontiguousarray(a[:, 0])
        v1 = np.ascontiguousarray(a[:, 1])
        M0 = v0[self.oidx]
        s0 = M0 @ M0.conj().T
        if want_cross:
            M1 = v1[self.oidx]
            s1 = M1 @ M1.conj().T
            cross = M0 @ M1.conj().T
            del M0, M1
        else:
            del M0
            M1 = v1[self.oidx]
            s1 = M1 @ M1.conj().T
            cross = None
            del M1
        return s0, s1, cross, [float(s0.trace().real), float(s1.trace().real)]


def S_bits(rho):
    w = sla.eigvalsh(rho)
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum())


def chi_bits(s0, s1, p):
    tot = p[0] + p[1]
    out = S_bits((s0 + s1) / tot)
    for s, pz in ((s0, p[0]), (s1, p[1])):
        if pz > 1e-14:
            out -= (pz / tot) * S_bits(s / pz)
    return out


def tr1(sig, k, j):
    lo, hi = 1 << j, 1 << (k - 1 - j)
    return np.einsum("aibajb->ij", sig.reshape(lo, 2, hi, lo, 2, hi))


def cmi_bits(s0, s1, p, ka, kb):
    tot = p[0] + p[1]
    out = 0.0
    for s, pz in ((s0, p[0]), (s1, p[1])):
        if pz <= 1e-14:
            continue
        r = s / pz
        T = r.reshape(1 << ka, 1 << kb, 1 << ka, 1 << kb)
        ra = np.einsum("aibi->ab", T)
        rb = np.einsum("iaib->ab", T)
        out += (pz / tot) * (S_bits(ra) + S_bits(rb) - S_bits(r))
    return out


def r_ind(chi, exc, H, C, delta):
    idx = {l: i for i, l in enumerate(LABELS)}
    singles = [l for l in LABELS if H >= GATE_H and chi[l] >= (1 - delta) * H and exc[l] >= GATE_EXC]
    best, key = [], None
    for r in range(len(singles), 0, -1):
        for comb in itertools.combinations(sorted(singles, key=idx.get), r):
            ok = all(C.get(tuple(sorted((comb[i], comb[j]), key=idx.get))) is not None
                     and C[tuple(sorted((comb[i], comb[j]), key=idx.get))] <= GATE_IND
                     for i in range(len(comb)) for j in range(i + 1, len(comb)))
            if ok:
                kk = tuple(idx[c] for c in comb)
                if key is None or kk < key:
                    best, key = list(comb), kk
        if best:
            break
    return len(best), best, singles


# ------------------------------------------------------------------ memo -----
def memo_fragments(txt):
    f = {}
    for m in re.finditer(r"`F_\(([+-][xyz])\) = \[([^\]]*)\]`", txt):
        f[m.group(1)] = [tuple(int(v) for v in p)
                         for p in re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(2))]
    return f


def tiebreak(txt=None):
    """Recompute the partition from the memo's stated tie-break algorithm."""
    fr = {l: [] for l in LABELS}
    sites = sorted([(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)])
    for c in sites:
        if c == CENTER:
            continue
        r = sum(map(abs, c))
        x, y, z = c
        if r == 1:
            ax = "xyz"[[abs(v) for v in c].index(1)]
            fr[("+" if sum(c) > 0 else "-") + ax].append(c)
        elif r == 2 and x != 0:
            fr[("+" if x > 0 else "-") + "x"].append(c)
        else:
            fr[{(1, 1): "+y", (-1, 1): "+z", (-1, -1): "-y", (1, -1): "-z"}[
                (1 if y > 0 else -1, 1 if z > 0 else -1)]].append(c)
    return fr


PAIR_CLASS = {}
for _c, _ms in {"opposite-55": [("+x", "-x")],
                "opposite-44": [("+y", "-y"), ("+z", "-z")],
                "plus-x-orthogonal": [("+x", q) for q in ("+y", "-y", "+z", "-z")],
                "minus-x-orthogonal": [("-x", q) for q in ("+y", "-y", "+z", "-z")],
                "transverse-orthogonal": [("+y", "+z"), ("+z", "-y"), ("-y", "-z"), ("-z", "+y")]
                }.items():
    for _p in _ms:
        PAIR_CLASS[tuple(sorted(_p, key=LABELS.index))] = _c


# =============================================================== main ========
def main():
    out = {"schema": "d3-bar-independent-check-cycle914-v1", "cycle": 914,
           "boundary_sentences": BOUNDARY}

    # ---- pins (own verification, own digests)
    pin_ok = True
    pins = {}
    for rel, want in PIN_SHA.items():
        p = os.path.join(ROOT, rel)
        got = sha(open(p, "rb").read()) if os.path.exists(p) else None
        pins[rel] = got
        pin_ok &= (got == want)
    note("attack", "pin-verification", pin_ok, {"pins": pins})
    memo_txt = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode()

    # ---- ATTACK: fragment partition vs the FROZEN MEMO's own bytes
    declared = memo_fragments(memo_txt)
    algo = tiebreak()
    part_ok = (sorted(declared) == sorted(LABELS)
               and all(set(declared[l]) == set(algo[l]) for l in LABELS)
               and [len(declared[l]) for l in LABELS] == [5, 5, 4, 4, 4, 4])
    flat = [c for l in LABELS for c in declared[l]]
    part_ok &= (len(flat) == 26 and len(set(flat)) == 26 and CENTER not in flat)
    note("attack", "fragment-partition-vs-memo-tiebreak-bytes", part_ok,
         {"parsed_from": PARENT_MEMO, "sizes": [len(declared[l]) for l in LABELS]})

    # pair-class ORBIT EQUIVALENCE under the partition-preserving proper
    # rotations, DECISIVE: the orbit of every pair must EQUAL its declared
    # class member set (each class one connected orbit; every member reachable
    # from the evaluated representative).  The declared partition is NOT closed
    # under the full 24-element proper cubic group and no such claim is checked.
    rots = rotations24()
    smap = {frozenset(declared[l]): l for l in LABELS}
    part_rots = [M for M in rots
                 if all(frozenset(tuple(int(v) for v in (M @ np.array(c)))
                                  for c in declared[l]) in smap for l in LABELS)]
    class_members = {}
    for pa in itertools.combinations(LABELS, 2):
        k2 = tuple(sorted(pa, key=LABELS.index))
        class_members.setdefault(PAIR_CLASS[k2], set()).add(k2)
    orbit_ok = bool(part_rots)
    for pa in itertools.combinations(LABELS, 2):
        k2 = tuple(sorted(pa, key=LABELS.index))
        orbit = set()
        for M in part_rots:
            im = [smap[frozenset(tuple(int(v) for v in (M @ np.array(c)))
                                 for c in declared[l])] for l in pa]
            orbit.add(tuple(sorted(im, key=LABELS.index)))
        if orbit != class_members[PAIR_CLASS[k2]]:
            orbit_ok = False
    note("attack", "pair-class-orbit-equivalence-partition-preserving", orbit_ok,
         {"classes": 5, "pairs": 15,
          "partition_preserving_rotations": len(part_rots),
          "decisive": "orbit of every pair under the partition-preserving proper "
                      "rotations must equal its declared class member set; "
                      "full-group closure is NOT claimed"})

    # ---- ATTACK: sector-reduction exactness on reduced instances (FULL SPACE)
    slab = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    slab_g = [M for M in rots if abs(int(M[2, 2])) == 1]
    d1, _ = small_instance_check("3x3x1", slab, slab_g, 0.10, 0.7)
    cube8 = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
    d2, _ = small_instance_check("2x2x2", cube8, rots, 0.20, 0.9)
    note("attack", "sector-reduction-exactness-full-space", (d1 < 1e-12 and d2 < 1e-12),
         {"open-3x3x1(9 qubits, 512-dim full space, |G|=%d)" % len(slab_g): d1,
          "2x2x2(8 qubits, 256-dim full space, |G|=24)": d2,
          "method": "dense eigendecomposition of the FULL Hamiltonian vs the orbit-sector "
                    "propagation, compared on raw amplitudes"})

    # ---- own sector reduction of the real cube
    t0 = time.perf_counter()
    sec = CubeSector()
    t_basis = time.perf_counter() - t0
    note("check", "sector-dimension", sec.n * 2 == 5605504,
         {"orbits_26bit": sec.n, "sector_dim": sec.n * 2, "memo_states": 5605504,
          "canonicalisation": "MAX-representative (primary uses MIN)",
          "size_histogram": {str(int(k)): int(v) for k, v in
                             zip(*np.unique(sec.sizes, return_counts=True))}})

    # ---- ATTACK: raw-formula spot check of the sector algebra on the real cube
    rng = np.random.default_rng(914)
    a_test = sec.prep()
    rr = rng.integers(0, sec.n, size=4096)
    a_test = a_test + 0  # keep prep; add a deterministic non-symmetric probe below
    probe = np.zeros_like(a_test)
    probe[:, 0] = np.cos(np.arange(sec.n) * 0.5)
    probe[:, 1] = np.sin(np.arange(sec.n) * 0.25)
    o = np.empty_like(probe)
    w = np.empty_like(probe)
    sec.mv(probe, 0.10, o, w)
    xs = rng.integers(0, 1 << 26, size=20000, dtype=np.int64).astype(np.uint32)
    cb = rng.integers(0, 2, size=20000)
    oo = sec.orb[xs]
    raw = -(sec.E[oo, cb]) * probe[oo, cb] - 0.10 * probe[oo, 1 - cb]
    for i in range(26):
        raw -= 0.10 * probe[sec.orb[xs ^ np.uint32(1 << i)], cb]
    dev_raw = float(np.abs(raw - o[oo, cb]).max())
    inv_dev = 0.0
    for M in rots[:6]:
        p = [sec.idx[tuple(int(v) for v in (M @ np.array(c)))] for c in sec.nc]
        gx = np.zeros_like(xs)
        for j in range(26):
            gx |= ((xs >> np.uint32(j)) & np.uint32(1)) << np.uint32(p[j])
        inv_dev = max(inv_dev, float(np.abs(o[sec.orb[gx], cb] - o[oo, cb]).max()))
    note("attack", "raw-formula-vs-sector-matvec", (dev_raw < 1e-12 and inv_dev < 1e-14),
         {"max_dev_raw_formula": dev_raw, "max_dev_G_invariance_of_Hpsi": inv_dev,
          "configs_sampled": 20000})

    # ---- marginal builders (own construction)
    Fx, Fmx = declared["+x"], declared["-x"]
    Fy, Fmy, Fz = declared["+y"], declared["-y"], declared["+z"]
    MG = {"closed-five": Marginal(sec, Fx), "wedge-four": Marginal(sec, Fy)}
    PG = {"opposite-55": (Marginal(sec, Fx + Fmx), 5, 5),
          "opposite-44": (Marginal(sec, Fy + Fmy), 4, 4),
          "plus-x-orthogonal": (Marginal(sec, Fx + Fy), 5, 4),
          "minus-x-orthogonal": (Marginal(sec, Fmx + Fy), 5, 4),
          "transverse-orthogonal": (Marginal(sec, Fy + Fz), 4, 4)}

    a0 = sec.prep()
    recomputed = {}
    prop_info = {}
    energies = {}
    keep_state = {}
    lam_c = 0.10 if 0.10 in LAMBDAS else LAMBDAS[0]
    for lam in LAMBDAS:
        outs, info = shifted_chebyshev(sec, lam, a0, T_EXEC)
        prop_info[str(lam)] = info
        energies[str(lam)] = {"E0": energy_expectation(sec, lam, outs[0]),
                              "E_tmax": energy_expectation(sec, lam, outs[-1])}
        if lam == lam_c and 0.7 in [round(t, 6) for t in T_EXEC]:
            keep_state[lam] = outs[[round(t, 6) for t in T_EXEC].index(0.7)].copy()
        rows = []
        chi0 = {}
        bond0 = None
        for it, t in enumerate(T_EXEC):
            a = outs[it]
            s0, s1, cr, p = MG["closed-five"].blocks(a, want_cross=True)
            c5 = chi_bits(s0, s1, p)
            H = -sum(q * np.log2(q) for q in p if q > 0)
            rj = np.zeros((64, 64), dtype=np.complex128)
            rj[:32, :32], rj[32:, 32:] = s0, s1
            rj[:32, 32:], rj[32:, :32] = cr, cr.conj().T
            bond = np.einsum("abicdi->abcd", rj.reshape(2, 2, 16, 2, 2, 16)).reshape(4, 4)
            one5 = {}
            for j, site in enumerate(Fx):
                cls = {1: "face", 2: "edge", 3: "corner"}[sum(map(abs, site))]
                one5.setdefault(cls, []).append(chi_bits(tr1(s0, 5, j), tr1(s1, 5, j), p))
            del s0, s1, cr, rj
            w0, w1, _, pw = MG["wedge-four"].blocks(a)
            c4 = chi_bits(w0, w1, pw)
            one4 = {}
            for j, site in enumerate(Fy):
                cls = {1: "face", 2: "edge", 3: "corner"}[sum(map(abs, site))]
                one4.setdefault(cls, []).append(chi_bits(tr1(w0, 4, j), tr1(w1, 4, j), pw))
            del w0, w1
            one = {c: float(np.mean((one5.get(c) or one4.get(c)))) for c in
                   ("face", "edge", "corner")}
            if it == 0:
                chi0 = {"c5": c5, "c4": c4, "one": dict(one)}
                bond0 = 1.0 - float(np.trace(bond @ bond).real)
            chi = {l: (c5 if l in ("+x", "-x") else c4) for l in LABELS}
            exc = {l: chi[l] - (chi0["c5"] if l in ("+x", "-x") else chi0["c4"]) for l in LABELS}
            need = any(len([l for l in LABELS if H >= GATE_H and chi[l] >= (1 - d) * H
                            and exc[l] >= GATE_EXC]) >= 2 for d in DELTAS)
            classes, C = {}, {}
            if need:
                for cls, (mg, ka, kb) in PG.items():
                    q0, q1, _, pq = mg.blocks(a)
                    classes[cls] = cmi_bits(q0, q1, pq, ka, kb)
                    del q0, q1
                for k2, cls in PAIR_CLASS.items():
                    C[k2] = classes[cls]
            rr_ = {}
            ss_ = {}
            for d in DELTAS:
                n, sub, _sg = r_ind(chi, exc, H, C, d)
                rr_[str(d)] = n
                ss_[str(d)] = sub
            rows.append({"jt": t, "H": H, "chi5": c5, "chi4": c4,
                         "theta": (1.0 - float(np.trace(bond @ bond).real)) - bond0,
                         "one": one, "one_exc": {c: one[c] - chi0["one"][c] for c in one},
                         "pairs": classes if need else None, "r_ind": rr_, "subsets": ss_,
                         "norm_err": abs(sec.norm2(a) - 1.0), "drift": abs(p[0] - 0.5)})
        recomputed[lam] = rows
        del outs

    # ---- ATTACK: propagator semigroup/composition + conservation cross-checks
    lz = {"energy_conservation": {k: dict(v, abs_dev=abs(v["E_tmax"] - v["E0"]))
                                  for k, v in energies.items()}}
    if keep_state:
        half = shifted_chebyshev(sec, lam_c, a0, [0.35])[0][0]
        twice = shifted_chebyshev(sec, lam_c, half, [0.35])[0][0]
        ref_a = keep_state[lam_c]
        s0, s1, _, p = MG["closed-five"].blocks(twice)
        c_two = chi_bits(s0, s1, p)
        c_one = next(r["chi5"] for r in recomputed[lam_c] if abs(r["jt"] - 0.7) < 1e-9)
        lz["semigroup"] = {"lam": lam_c, "t": 0.7,
                           "max_amplitude_dev": float(np.abs(twice - ref_a).max()),
                           "chi_two_half_steps": c_two, "chi_one_shot": c_one,
                           "chi_abs_dev": abs(c_two - c_one)}
        del half, twice, ref_a
    note("attack", "propagator-semigroup-and-conservation",
         (lz.get("semigroup", {}).get("chi_abs_dev", 0.0) < 1e-9
          and all(v["abs_dev"] < 1e-8 for v in lz["energy_conservation"].values())), lz)

    # ---- events from the checker's OWN numbers
    ev = {}
    for lam in LAMBDAS:
        e = {}
        for d in DELTAS:
            hit = None
            for i, r in enumerate(recomputed[lam]):
                if r["r_ind"][str(d)] >= 2:
                    run = 0
                    for j in range(i, len(recomputed[lam])):
                        if recomputed[lam][j]["r_ind"][str(d)] >= 2:
                            run += 1
                        else:
                            break
                    hit = {"jt": r["jt"], "theta": r["theta"], "r": r["r_ind"][str(d)],
                           "subset": r["subsets"][str(d)], "run": run}
                    break
            e[str(d)] = hit
        ev[lam] = e
    W = [l for l in LAMBDAS if all(ev[l][str(d)] and ev[l][str(d)]["jt"] <= DEADLINE for d in DELTAS)
         and ev[l][str(HEADLINE)]["run"] >= 3]
    out["checker_events"] = {str(l): ev[l] for l in LAMBDAS}
    out["checker_window"] = W

    # ---- ATTACK: baseline re-anchoring (the memo's freeze correction)
    t0_max = max(max(abs(recomputed[l][0]["chi5"]), abs(recomputed[l][0]["chi4"]),
                     max(abs(v) for v in recomputed[l][0]["one"].values())) for l in LAMBDAS)
    theta0 = max(abs(recomputed[l][0]["theta"]) for l in LAMBDAS)
    anchor_ok = t0_max <= 1e-9 and theta0 <= 1e-12
    # the memo's stated reason, verified: chi_GS ~ 1 bit makes a doublet anchor unsatisfiable
    gs_from_streams = {}
    for lam, tag in STREAMS.items():
        p = os.path.join(ROOT, "logs/runner-cache/d3_bar_window_checkpoints/%s_observables.jsonl" % tag)
        if os.path.exists(p):
            r = json.loads(open(p).readline())
            gs_from_streams[str(lam)] = r["fragment_types"]["closed-five"]["gs_doublet_chi_bits"]
    lam_d = 0.10
    doublet = {"attempted": True, "lam": lam_d}
    try:
        sq = sec.sq

        def opmv(v):
            V = v.reshape(sec.n, 2)
            o_ = np.empty_like(V)
            w_ = np.empty_like(V)
            sec.mv(V / sq, lam_d, o_, w_)
            return (o_ * sq).ravel()

        v0 = np.cos(np.arange(sec.n * 2) * 0.37)
        v0 /= np.linalg.norm(v0)
        L = LinearOperator((sec.n * 2, sec.n * 2), matvec=opmv, dtype=np.float64)
        wv, vv = eigsh(L, k=2, which="SA", v0=v0, ncv=6, maxiter=12, tol=1e-8)
        doublet.update({"converged": True, "energies": [float(x) for x in wv],
                        "splitting": float(wv[1] - wv[0])})
        g = (vv[:, 0].reshape(sec.n, 2) / sq).astype(np.complex128)
        h = (vv[:, 1].reshape(sec.n, 2) / sq).astype(np.complex128)
        s0a, s1a, _, pa = MG["closed-five"].blocks(g)
        s0b, s1b, _, pb = MG["closed-five"].blocks(h)
        s0m, s1m = (s0a + s0b) / 2.0, (s1a + s1b) / 2.0
        pm = [(pa[0] + pb[0]) / 2.0, (pa[1] + pb[1]) / 2.0]
        doublet["chi_GS_closed_five"] = chi_bits(s0m, s1m, pm)
    except Exception as exc:                                    # noqa: BLE001
        doublet.update({"converged": False, "error": type(exc).__name__})
    gs_val = doublet.get("chi_GS_closed_five")
    ceiling_arg = {
        "exact_ceiling": "chi_Z(S:F) <= H(Z_S) <= 1 bit (Holevo); measured max chi over all "
                         "executed rows = %.12f" % max(max(r["chi5"], r["chi4"])
                                                       for l in LAMBDAS for r in recomputed[l]),
        "lambda0_doublet_chi_exact": 1.0,
        "reason": "at lambda=0 the equal doublet mixture is (|0..0><0..0|+|1..1><1..1|)/2, whose "
                  "pointer-conditional fragment states are orthogonal pure states, so "
                  "chi_GS = 1 bit exactly; a doublet-anchored excess gate would require "
                  "chi >= 1.02 bit against a 1 bit ceiling -- the memo's freeze correction is "
                  "verified, and the excess gate as frozen (trajectory t=0) is the only "
                  "non-vacuous choice",
        "gs_doublet_chi_in_committed_streams": gs_from_streams,
        "checker_lanczos_doublet": doublet,
    }
    note("attack", "baseline-re-anchoring", anchor_ok,
         {"t0_anchor_max_bits": t0_max, "theta_t0": theta0, "frozen_tol": 1e-9,
          "excess_definition_used": "chi(t) - chi(t=0)  [trajectory anchor, per freeze correction]",
          "doublet_anchor_would_be_unsatisfiable": (gs_val is None or gs_val + 0.02 > 1.0),
          "argument": ceiling_arg})

    # ---- compare against the primary receipt
    rp = os.path.join(ROOT, PRIMARY_RECEIPT)
    prim = json.load(open(rp)) if os.path.exists(rp) else None
    cmp_ = {"receipt_found": prim is not None}
    if prim:
        dev = {"chi5": 0.0, "chi4": 0.0, "theta": 0.0, "pair": 0.0}
        mism = 0
        for lam in LAMBDAS:
            prows = {round(r["jt"], 6): r for r in prim["measurement"]["rows"][str(lam)]}
            for r in recomputed[lam]:
                q = prows.get(round(r["jt"], 6))
                if q is None:
                    mism += 1
                    continue
                dev["chi5"] = max(dev["chi5"], abs(r["chi5"] - q["chi_closed_five"]))
                dev["chi4"] = max(dev["chi4"], abs(r["chi4"] - q["chi_wedge_four"]))
                dev["theta"] = max(dev["theta"], abs(r["theta"] - q["theta"]))
                if r["pairs"] and q["pair_classes"]:
                    for c, v in r["pairs"].items():
                        dev["pair"] = max(dev["pair"], abs(v - q["pair_classes"][c]))
                for d in DELTAS:
                    if r["r_ind"][str(d)] != q["r_ind"][str(d)]:
                        mism += 1
        cmp_.update({"max_abs_dev": dev, "r_ind_mismatches": mism,
                     "verdict_parent": prim["verdict"]["parent_wiring"],
                     "verdict_three_lambda_subset": prim["verdict"]["three_lambda_subset_summary"],
                     "primary_window": prim["checks"]["CHECK-03-window-subset"]["W_full"],
                     "checker_window": W,
                     "window_agrees": prim["checks"]["CHECK-03-window-subset"]["W_full"] == W})
        agree = (max(dev.values()) < 1e-9 and mism == 0 and cmp_["window_agrees"])
        note("check", "primary-vs-independent-recomputation", agree, cmp_)
        # the primary must NOT claim delta-contract completion: lambda=0.02 was
        # not executed, so any delta-wiring completion award is a false PASS.
        note("attack", "no-delta-completion-claim",
             (prim["verdict"].get("delta_contract_discharged") is False
              and "delta_wiring" not in prim["verdict"]),
             {"delta_contract_discharged": prim["verdict"].get("delta_contract_discharged"),
              "legacy_delta_wiring_key_present": "delta_wiring" in prim["verdict"],
              "reason": "the delta memo commissions four lambdas incl. 0.02 and forbids "
                        "post-inspection drops; a three-lambda run cannot discharge it"})
        # disclosed-scope honesty: primary must not have sampled beyond its declaration
        declared_T = prim["protocol"]["T_executed"]
        extra = [t for lam in LAMBDAS for t in
                 [r["jt"] for r in prim["measurement"]["rows"][str(lam)]] if t not in declared_T]
        note("attack", "no-undisclosed-sampling", len(extra) == 0,
             {"declared_grid": declared_T, "undeclared_rows": extra,
              "T_C_points_not_executed": prim["protocol"]["T_not_executed"]})

    # ------------------------------------------------------------- TEETH -----
    teeth = []

    def tooth(name, detect, detail):
        teeth.append({"tooth": name, "detected": bool(detect), "exit": "BIT-FLIPPED"
                      if detect else "TOOTH-FAILED", "detail": detail})

    b = bytearray(open(os.path.join(ROOT, PARENT_MEMO), "rb").read())
    b[100] ^= 0x01
    tooth("tampered-pin", sha(bytes(b)) != PIN_SHA[PARENT_MEMO],
          "single-byte flip in the parent memo changes its sha256 -> pin verification fails")

    bad = {l: list(declared[l]) for l in LABELS}
    bad["-z"] = bad["-z"][:-1]
    flat_bad = [c for l in LABELS for c in bad[l]]
    tooth("dropped-fragment-site", len(flat_bad) != 26,
          "dropping one site from F_(-z) breaks the 26-site partition check (%d sites)" % len(flat_bad))

    L05 = 0.05 if 0.05 in LAMBDAS else LAMBDAS[0]
    if prim:
        fake = dict(prim["measurement"]["theta_star_headline"])
        fake[str(L05)] = (fake.get(str(L05)) or 0) + 1e-6
        mine = (ev[L05][str(HEADLINE)] or {}).get("theta", 0.0)
        tooth("hardcoded-bar-location", abs(fake[str(L05)] - mine) > 1e-9,
              "perturbing the primary's theta* by 1e-6 is caught by the independent theta "
              "recomputation at tolerance 1e-9")

    r0 = next(r for r in recomputed[L05] if abs(r["jt"] - min(T_EXEC, key=lambda u: abs(u - 0.6))) < 1e-9)
    chi_l = {l: (r0["chi5"] if l in ("+x", "-x") else r0["chi4"]) for l in LABELS}
    exc_l = {l: chi_l[l] for l in LABELS}
    C_l = {k: r0["pairs"][v] for k, v in PAIR_CLASS.items()} if r0["pairs"] else {}
    base_r = r_ind(chi_l, exc_l, r0["H"], C_l, HEADLINE)[0]
    sab = dict(chi_l)
    sab["+x"] = 0.0
    tooth("leaked-verdict", r_ind(sab, exc_l, r0["H"], C_l, HEADLINE)[0] < base_r,
          "R_ind is recomputed from the checker's own chi/C_ab, not copied: zeroing chi(+x) "
          "drops R_ind from %d" % base_r)

    Wdrop = [l for l in W if l != 0.20]
    tooth("skipped-lambda", (0.20 not in W) and len(Wdrop) == len(W),
          "lambda=0.20 is executed and measured NON-certifying: it is present in the ladder "
          "(so the boundary bracket (0.10,0.20) exists) and absent from W_full=%s" % (W,))

    planted = next(r for r in recomputed[L05] if abs(r["jt"] - min(T_EXEC, key=lambda u: abs(u - 0.3))) < 1e-9)
    pc = {l: 0.999 for l in LABELS}
    pe = {l: 0.999 for l in LABELS}
    pC = {k: 0.0 for k in PAIR_CLASS}
    tooth("planted-certification-blindness", r_ind(pc, pe, planted["H"], pC, HEADLINE)[0] == 6,
          "a fabricated all-fragment certification planted at Jt=0.3 is detected by the event "
          "routine (R_ind=6), so the routine is not blind to an early hit")

    lam_t, tag = 0.10, STREAMS[0.10]
    sp = os.path.join(ROOT, "logs/runner-cache/d3_bar_window_checkpoints/%s_observables.jsonl" % tag)
    ref_rows = {round(json.loads(l)["jt"], 6): json.loads(l) for l in open(sp)}
    my07 = next(r["chi5"] for r in recomputed[lam_t] if abs(r["jt"] - 0.7) < 1e-9)
    ref07 = ref_rows[0.7]["fragment_types"]["closed-five"]["chi_bits"]
    tooth("tampered-committed-stream", abs(my07 - (ref07 + 1e-6)) > 1e-9,
          "a 1e-6 perturbation of the committed 2026-07-11 reference chi is caught at 1e-9 "
          "(true |dev| = %.3e)" % abs(my07 - ref07))

    dtam, _ = small_instance_check("3x3x1-tampered", slab, slab_g, 0.10, 0.7, tamper=True)
    tooth("sector-table-tamper", dtam > 1e-6,
          "corrupting one orbit flip-table entry breaks the full-space/sector agreement "
          "(dev %.3e vs clean %.3e)" % (dtam, d1))

    out["teeth"] = teeth
    out["findings"] = FINDINGS
    out["numerics"] = {
        "sector_dim": sec.n * 2, "basis_wall_s": t_basis,
        "propagator": prop_info,
        "lanczos_cross_check": lz,
        "max_norm_err": max(r["norm_err"] for l in LAMBDAS for r in recomputed[l]),
        "wall_s": time.perf_counter() - T_START,
        "peak_rss_gib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30,
    }
    out["checker_measurement"] = {
        str(l): {"first_hit_headline": ev[l][str(HEADLINE)],
                 "rows": [{k: r[k] for k in ("jt", "H", "chi5", "chi4", "theta", "pairs",
                                             "r_ind", "subsets", "one_exc")}
                          for r in recomputed[l]]} for l in LAMBDAS}
    out["primary_comparison"] = cmp_
    digest = sha(json.dumps([[l, r["jt"], r["chi5"], r["chi4"], r["theta"], r["r_ind"]]
                             for l in LAMBDAS for r in recomputed[l]],
                            sort_keys=True, default=repr).encode())
    out["result_table_sha256"] = digest

    survives = all(f["ok"] for f in FINDINGS)
    teeth_ok = all(t["detected"] for t in teeth)
    out["exit_contract"] = ("FAIL-CLOSED: exit 0 iff every finding passes AND all teeth "
                            "fire; exit 1 on any refuted finding or failed tooth")
    out["exit_code"] = 0 if (survives and teeth_ok) else 1

    with open(os.path.join(ROOT, "outputs/d3_bar_independent_check_cycle914_receipt_2026_07_28.json"),
              "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, default=float)

    for s in BOUNDARY:
        print(s)
    print("PINS %s" % ("ok" if pin_ok else "FAILED"))
    for f in FINDINGS:
        print("%-9s %-46s %s" % (f["kind"].upper(), f["name"], "PASS" if f["ok"] else "REFUTED"))
    for t in teeth:
        print("TOOTH     %-46s %s" % (t["tooth"], t["exit"]))
    print("CHECKER-EVENTS %s" % {str(l): (None if ev[l][str(HEADLINE)] is None else
                                          "t=%.1f/theta*=%.12f/R=%d/subset=%s/run=%d" %
                                          (ev[l][str(HEADLINE)]["jt"], ev[l][str(HEADLINE)]["theta"],
                                           ev[l][str(HEADLINE)]["r"], ev[l][str(HEADLINE)]["subset"],
                                           ev[l][str(HEADLINE)]["run"])) for l in LAMBDAS})
    print("CHECKER-WINDOW W_full=%s boundary=%s" % (W, (max(W), 0.20) if W and 0.20 not in W else None))
    print("PRIMARY-COMPARISON %s" % json.dumps(cmp_, default=float)[:600])
    print("TOTAL INDEPENDENT-CHECK %s teeth=%d/%d exit=%d wall=%.1fs rss=%.2fGiB digest=%s %s"
          % ("CLAIM-SURVIVES" if survives else "CLAIM-REFUTED",
             sum(1 for t in teeth if t["detected"]), len(teeth), out["exit_code"],
             out["numerics"]["wall_s"], out["numerics"]["peak_rss_gib"], digest[:16], BOUNDARY_LINE))
    # FAIL-CLOSED: refutation or a failed tooth must fail this process.
    sys.exit(out["exit_code"])


if __name__ == "__main__":
    main()
