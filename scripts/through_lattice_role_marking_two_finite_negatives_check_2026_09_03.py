#!/usr/bin/env python3
"""Through-lattice role marking: two finite negative results on named classes.

PR #7834 leaves one item open in its Proof boundary: whether a rule whose
direct dependence is on adjacent sites only -- longer reach arising through
chains of adjacent conditions -- can select a superlattice role pattern with
free code sites.  Its Theorem 3 item 2 answers "no" for value-reading star
rules at spacing 2, by a vacuity argument: every corner site has six free code
neighbours there, so the corner star realises all 128 value patterns and the
maximal star rule accepts everything.

This runner tests the two named classes of star-local rule on clusters where
that vacuity argument does not apply.

  A  STAR PATTERNS.  The 24 proper rotations and the 48-element full cubic
     group induce the same 20 orbits on the 128 seven-bit star patterns, with
     identical canonical representatives, so every rotation-invariant star
     rule is automatically inversion-invariant.  The spacing-2 vacuity of
     PR #7834 restated and recomputed.

  B  VALUE-READING STAR RULES ON SPACED SUPERLATTICES.  A rule is a predicate
     on the seven Z-values of a site's star, invariant under the 24 proper
     rotations.  On a spaced superlattice with coarse spacing s and one code
     site per coarse edge at position p, the marker values are covariant under
     the space-group stabiliser of the code sublattice; the MAXIMAL rule
     accepts exactly the star patterns realised in the intended configurations
     over every code filling.  Junk = a zero-penalty configuration on the
     torus whose markers are not a translate or rotation of the intended
     pattern.  Exhaustive over every covariant assignment at s = 3 (both code
     positions) and s = 4 midpoint; the junk witness is found by exhaustive
     branch-on-first-undetermined-site constraint propagation with backtracking
     and an explicit node count.  No SAT solver and no external solver is used
     anywhere.

  C  STATE-READING FRUSTRATION-FREE STAR TEMPLATES.  A rule is a PSD operator
     h on the seven-site star, identical at every site, with the intended
     role-star states in its kernel K; the canonical maximal choice is
     h = 1 - Pi_K.  The zero space of H = sum_s h_s is the intersection of the
     star kernels.  Aliasing lemma for tori with a side of length 2; exact
     dense results on the 2D 4x2 torus and for the 7-qubit 3D star; matrix-free
     alternating projections on the 16-qubit 2D 4x4 and 3D 4x2x2 tori, with
     Hutchinson nullity estimates; the character of the junk; and the 1D
     contrast, which is junk-free.

Group A and group B are exact: integer and bit arithmetic, exhaustive
enumeration, exhaustive constraint propagation.  Group C mixes exact linear
algebra (dense, on 8-qubit and 7-qubit spaces) with matrix-free numerical
statements on 16-qubit tori; every numerical line is tagged, carries its
converged residual, and fixes its seed.  Every array is at most 65536 x 16.

These are finite negative results on two named classes over named finite
clusters.  Nothing here says a nearby-only rule of some other kind is
unavailable, and nothing here is derived from the framework axioms.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter

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


# ============================================================ cubic group, stars

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
DIDX = {d: i for i, d in enumerate(DIRS)}


def _mats():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                M[i][perm[i]] = sg[i]
            out.append(tuple(tuple(r) for r in M))
    return out


ALL48 = _mats()


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


ROT24 = [M for M in ALL48 if det3(M) == 1]


def mvec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1] + M[0][2] * v[2],
            M[1][0] * v[0] + M[1][1] * v[1] + M[1][2] * v[2],
            M[2][0] * v[0] + M[2][1] * v[1] + M[2][2] * v[2])


def mtrans(M):
    return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))


DP24 = sorted(set(tuple(DIDX[mvec(M, d)] for d in DIRS) for M in ROT24))
DP48 = sorted(set(tuple(DIDX[mvec(M, d)] for d in DIRS) for M in ALL48))


def canon_table(perms):
    """Canonical representative of every 7-bit star pattern under `perms`."""
    T = np.zeros(128, dtype=np.int64)
    for p in range(128):
        c = (p >> 6) & 1
        best = 999
        for pm in perms:
            q = 0
            for i in range(6):
                if (p >> i) & 1:
                    q |= 1 << pm[i]
            best = min(best, q)
        T[p] = (c << 6) | best
    return T


CANON24 = canon_table(DP24)
CANON48 = canon_table(DP48)


# ---- propagation tables over 7-slot star patterns (built once, globally) ----
MSET = {}
for _km in range(128):
    for _kv in range(128):
        if (_kv & _km) != _kv:
            continue
        _m = 0
        for _p in range(128):
            if (_p & _km) == _kv:
                _m |= 1 << _p
        MSET[(_km, _kv)] = _m
BIT1 = [sum(1 << p for p in range(128) if (p >> b) & 1) for b in range(7)]
BIT0 = [sum(1 << p for p in range(128) if not ((p >> b) & 1)) for b in range(7)]


def star_codes(cfg):
    """The 7-bit star pattern at every site of a periodic 0/1 configuration."""
    q = cfg.astype(np.int64) << 6
    for i, d in enumerate(DIRS):
        q |= (np.roll(cfg, shift=(-d[0], -d[1], -d[2]),
                      axis=(0, 1, 2)).astype(np.int64) << i)
    return q


def penalty(cfg, acc):
    return int(np.count_nonzero(~acc[star_codes(cfg)]))


# =========================================================== A: star patterns

def role_of(c):
    """0 corner, 1 edge, 2 face, 3 cube centre, by coordinate parity."""
    return sum(x & 1 for x in c)


def spacing2_templates(L=4):
    """The 48 templates of the period-(4,2,2) role pattern on the LxLxL torus.

    Value -1 marks a free (code) site: the coarse edge sites.
    """
    out = []
    for ax in range(3):
        for t in itertools.product(range(L), repeat=3):
            V = np.zeros((L, L, L), dtype=np.int8)
            for c in itertools.product(range(L), repeat=3):
                u = tuple((c[i] + t[i]) % L for i in range(3))
                r = role_of(u)
                if r == 0:
                    V[c] = (u[ax] // 2) % 2
                elif r == 1:
                    V[c] = -1
                elif r == 2:
                    V[c] = 0
                else:
                    V[c] = 1
            out.append((ax, V))
    uniq = {}
    for ax, V in out:
        uniq[(ax, V.tobytes())] = V
    return [uniq[k] for k in sorted(uniq)]


def group_A():
    same_partition = (len(set(CANON24.tolist())) == len(set(CANON48.tolist()))
                      == 20 and np.array_equal(CANON24, CANON48))
    check("A1 [exact] the 24 proper rotations and the full 48-element cubic group "
          "induce the SAME %d orbits on the 128 seven-bit star patterns, with "
          "identical canonical representatives, so every rotation-invariant "
          "value-reading star rule is inversion-invariant and no such rule encodes "
          "a chirality" % len(set(CANON24.tolist())), same_partition)

    T = spacing2_templates(4)
    L = 4
    seen = set()
    pairs = set()
    maxnb = 0
    for V in T:
        for c in itertools.product(range(L), repeat=3):
            nb = [tuple((c[i] + d[i]) % L for i in range(3)) for d in DIRS]
            maxnb = max(maxnb, sum(1 for x in nb if V[x] < 0))
            if V[c] < 0:
                continue
            free = [j for j, x in enumerate(nb) if V[x] < 0]
            if len(free) != 6:
                continue
            for r in range(64):
                seen.add((int(V[c]) << 6) | r)
            for x in nb:
                for b in (0, 1):
                    pairs.add((int(V[c]), b))
    check("A2 [exact] spacing 2, the vertex-star argument of PR #7834 recomputed: on "
          "the 4x4x4 torus the %d templates (16 translates x 3 orientations of "
          "period (4,2,2)) give every corner six free code neighbours, and corner "
          "stars realise all %d of the 128 value patterns and %d of the 4 adjacent "
          "pairs, so the maximal value-reading star rule is vacuous there"
          % (len(T), len(seen), len(pairs)),
          len(T) == 48 and len(seen) == 128 and len(pairs) == 4 and maxnb == 6)


# ============================== B: value-reading rules on spaced superlattices

class Geom:
    """One spaced superlattice: coarse spacing s, code site at offset p."""

    def __init__(self, s, p):
        self.s, self.p = s, p
        self.cell = [(x, y, z) for x in range(s) for y in range(s)
                     for z in range(s)]
        self.fidx = {c: i for i, c in enumerate(self.cell)}
        self.C = frozenset([(p % s, 0, 0), (0, p % s, 0), (0, 0, p % s)])
        G = []
        for R in ROT24:
            for t in self.cell:
                img = frozenset(tuple((mvec(R, c)[i] + t[i]) % s for i in range(3))
                                for c in self.C)
                if img == self.C:
                    G.append((R, t))
        self.G = G
        self.point_part = sorted(set(R for R, _ in G))
        orb_id, orbits = {}, []
        for x in self.cell:
            if x in orb_id:
                continue
            o = sorted(set(tuple((mvec(R, x)[i] + t[i]) % s for i in range(3))
                           for (R, t) in G))
            k = len(orbits)
            orbits.append(o)
            for y in o:
                orb_id[y] = k
        self.orbits, self.orb_id = orbits, orb_id
        self.morb = [k for k, o in enumerate(orbits) if o[0] not in self.C]
        assert all(y not in self.C for k in self.morb for y in orbits[k])
        self.n = len(self.morb)
        self.mpos = {k: i for i, k in enumerate(self.morb)}
        M = -np.ones((s, s, s), dtype=np.int64)
        for x in self.cell:
            if orb_id[x] in self.mpos:
                M[x] = self.mpos[orb_id[x]]
        self.MORB = M
        masks = set()
        for c in self.cell:
            m = 0
            for sl in [c] + [tuple((c[i] + d[i]) % s for i in range(3))
                             for d in DIRS]:
                if orb_id[sl] in self.mpos:
                    m |= 1 << self.mpos[orb_id[sl]]
            masks.add(m)
        self.masks = sorted(masks)
        idx = np.arange(s ** 3).reshape(s, s, s)
        self.slotidx = [idx] + [np.roll(idx, shift=(-d[0], -d[1], -d[2]),
                                        axis=(0, 1, 2)) for d in DIRS]
        self.PRE24 = self._pre(ROT24)
        cen = {}
        for c in self.cell:
            cen.setdefault(orb_id[c], sum(
                1 for d in DIRS
                if tuple((c[i] + d[i]) % s for i in range(3)) in self.C))
        self.maxcodenb = max(cen.values())
        self.codeidx = [self.fidx[c] for c in sorted(self.C)]

    def _pre(self, rots):
        """Index maps realising m_g(x) = m(R^{-1}(x - t) mod s) for all (R, t)."""
        s = self.s
        rows = []
        for R in rots:
            Ri = mtrans(R)
            for t in self.cell:
                row = np.empty(s ** 3, dtype=np.int32)
                for x in self.cell:
                    y = mvec(Ri, tuple((x[i] - t[i]) % s for i in range(3)))
                    row[self.fidx[x]] = self.fidx[tuple(y[i] % s for i in range(3))]
                rows.append(row)
        return np.array(rows, dtype=np.int32)

    def val_cell(self, a):
        """Assignment bitmask over marker orbits -> cell values, -1 on code."""
        bits = np.array([(int(a) >> i) & 1 for i in range(self.n)], dtype=np.int8)
        return np.where(self.MORB >= 0, bits[np.maximum(self.MORB, 0)],
                        -1).astype(np.int8)


def accepted_raw(g, valcell):
    """The maximal rule: accept every star class realised in an intended config."""
    v = valcell.ravel().astype(np.int64)
    base = np.zeros(g.s ** 3, dtype=np.int64)
    free = np.zeros(g.s ** 3, dtype=np.int64)
    for j, si in enumerate(g.slotidx):
        bit = (1 << 6) if j == 0 else (1 << (j - 1))
        vv = v[si.ravel()]
        base |= np.where(vv == 1, bit, 0)
        free |= np.where(vv < 0, bit, 0)
    acc = np.zeros(128, dtype=bool)
    for k in np.unique(base * 128 + free).tolist():
        b, f = k // 128, k % 128
        fb = [bit for bit in ((1 << 6) if i == 0 else (1 << (i - 1))
                              for i in range(7)) if f & bit]
        for r in range(1 << len(fb)):
            q = b
            for i, bit in enumerate(fb):
                if (r >> i) & 1:
                    q |= bit
            acc[CANON24[q]] = True
    return acc[CANON24]


def torus_stars(L):
    idx = np.arange(L ** 3).reshape(L, L, L)
    sl = [idx] + [np.roll(idx, shift=(-d[0], -d[1], -d[2]), axis=(0, 1, 2))
                  for d in DIRS]
    S = np.stack([x.ravel() for x in sl], axis=1)
    return [tuple(int(u) for u in row) for row in S]


def dpll_junk(acc, N, stars, site_stars, intended, cap=2000000):
    """Lexicographically least zero-penalty configuration that is not intended.

    Exhaustive: branch on the first undetermined site, propagate every star
    constraint to a fixed point, backtrack on conflict.  Returns
    (configuration or None, node count).  No SAT solver.
    """
    accbits = 0
    for p in range(128):
        if acc[p]:
            accbits |= 1 << p
    assign = [-1] * N
    nodes = [0]

    def propagate(queue, trail):
        while queue:
            s0 = queue.pop()
            for si in site_stars[s0]:
                slots = stars[si]
                km = kv = 0
                for j, site in enumerate(slots):
                    v = assign[site]
                    if v >= 0:
                        bit = (1 << 6) if j == 0 else (1 << (j - 1))
                        km |= bit
                        if v == 1:
                            kv |= bit
                cons = accbits & MSET[(km, kv)]
                if cons == 0:
                    return False
                if km == 127:
                    continue
                for j, site in enumerate(slots):
                    if assign[site] >= 0:
                        continue
                    b = 6 if j == 0 else (j - 1)
                    if cons & BIT1[b] == 0:
                        val = 0
                    elif cons & BIT0[b] == 0:
                        val = 1
                    else:
                        continue
                    assign[site] = val
                    trail.append(site)
                    queue.append(site)
        return True

    def rec():
        k = -1
        for i in range(N):
            if assign[i] < 0:
                k = i
                break
        if k < 0:
            cfg = list(assign)
            return cfg if not intended(cfg) else None
        nodes[0] += 1
        if nodes[0] > cap:
            raise RuntimeError("node cap")
        for val in (0, 1):
            trail = [k]
            assign[k] = val
            if propagate([k], trail):
                r = rec()
                if r is not None:
                    for s0 in trail:
                        assign[s0] = -1
                    return r
            for s0 in trail:
                assign[s0] = -1
        return None

    sys.setrecursionlimit(20000)
    return rec(), nodes[0]


def intended_rows(g, L):
    """Every intended marker pattern on the L-torus: (site index, values)."""
    s = g.s
    rep = L // s
    rows = np.unique(g._base[g.PRE24], axis=0)
    out = []
    for row in rows:
        full = np.tile(row.reshape(s, s, s), (rep, rep, rep)).ravel()
        keep = np.flatnonzero(full >= 0)
        out.append((keep, full[keep].astype(np.int8)))
    return out


def periods_of(cfg, L):
    A = np.array(cfg).reshape(L, L, L)
    per = []
    for ax in range(3):
        for k in range(1, L + 1):
            if L % k == 0 and np.array_equal(A, np.roll(A, k, axis=ax)):
                per.append(k)
                break
        else:
            per.append(L)
    return tuple(sorted(per))


def sweep_superlattice(g, nsample):
    """Exhaustive sweep over every covariant assignment on one superlattice.

    Acceptance and covariance: the base intended configuration with every code
    filling is checked for every assignment; the full rotation-and-translation
    orbit of the intended configuration, again with every code filling, is
    checked on `nsample` evenly spaced assignments.
    """
    s = g.s
    L = s
    N = L ** 3
    stars = torus_stars(L)
    site_stars = [[] for _ in range(N)]
    for si, sl in enumerate(stars):
        for site in set(sl):
            site_stars[site].append(si)
    tot = 1 << g.n
    npass = sum(1 for a in range(tot)
                if all((a & m) != 0 and (a & m) != m for m in g.masks))
    accsz = []
    cnt = Counter()
    njunk = nvac = nlift = 0
    totnodes = maxnodes = 0
    covar_ok = True
    fill = list(itertools.product((0, 1), repeat=len(g.codeidx)))
    step = max(1, tot // nsample)
    sample = set(range(0, tot, step))
    for a in range(tot):
        g._base = g.val_cell(a).ravel()
        acc = accepted_raw(g, g.val_cell(a))
        accsz.append(int(acc.sum()))
        if acc.all():
            nvac += 1
        rows = (np.unique(g._base[g.PRE24], axis=0) if a in sample
                else g._base.reshape(1, -1))
        for row in rows:
            free = np.flatnonzero(row < 0)
            for bits in fill:
                cfg = row.copy()
                cfg[free] = np.array(bits, dtype=np.int8)[:len(free)]
                if penalty(cfg.reshape(s, s, s), acc) != 0:
                    covar_ok = False
        IR = intended_rows(g, L)

        def is_int(cfg, IR=IR):
            c = np.array(cfg, dtype=np.int8)
            return any(np.array_equal(c[k], v) for k, v in IR)

        cfg, nodes = dpll_junk(acc, N, stars, site_stars, is_int)
        totnodes += nodes
        maxnodes = max(maxnodes, nodes)
        if cfg is None:
            continue
        njunk += 1
        assert penalty(np.array(cfg).reshape(L, L, L), acc) == 0
        cnt[periods_of(cfg, L)] += 1
        big = np.tile(np.array(cfg).reshape(L, L, L), (2, 2, 2))
        IR2 = intended_rows(g, 2 * L)
        bb = big.ravel()
        if penalty(big, acc) == 0 and not any(
                np.array_equal(bb[k], v) for k, v in IR2):
            nlift += 1
    return dict(tot=tot, npass=npass, accsz=accsz, cnt=cnt, njunk=njunk,
                nvac=nvac, nlift=nlift, nodes=totnodes, maxnodes=maxnodes,
                covar=covar_ok, nsample=len(sample), nimg=len(g.PRE24))


def group_B():
    cases = [(3, 1), (3, 2), (4, 2)]
    geoms = {c: Geom(*c) for c in cases}
    res = {}
    for c in cases:
        res[c] = sweep_superlattice(geoms[c], 16)

    geo = " ; ".join(
        "s=%d p=%d |G_pt|=%d orbits=%d masks=%d code_nbrs<=%d"
        % (c[0], c[1], len(geoms[c].point_part), geoms[c].n,
           len(geoms[c].masks), geoms[c].maxcodenb) for c in cases)
    check("B1 [exact] zoom-out lemma: %s -- no site has an all-code star, the count "
          "being 1 or 3, never 6, so the spacing-2 vacuity of A2 is defeated at every "
          "spacing tested and any failure below has another mechanism" % geo,
          all(geoms[c].maxcodenb in (1, 3) for c in cases))

    check("B2 [exact] the maximal rule accepts its own intended configurations and is "
          "covariant: penalty 0 for all %d + %d + %d assignments with every code "
          "filling, and for %d sampled ones over every rotation and translate too; "
          "accepted sizes |A| of 128 span %d-%d, %d-%d, %d-%d, and %d are vacuous"
          % (res[(3, 1)]["tot"], res[(3, 2)]["tot"], res[(4, 2)]["tot"],
             sum(res[c]["nsample"] for c in cases),
             min(res[(3, 1)]["accsz"]), max(res[(3, 1)]["accsz"]),
             min(res[(3, 2)]["accsz"]), max(res[(3, 2)]["accsz"]),
             min(res[(4, 2)]["accsz"]), max(res[(4, 2)]["accsz"]),
             sum(res[c]["nvac"] for c in cases)),
          all(res[c]["covar"] for c in cases)
          and sum(res[c]["nvac"] for c in cases) == 0)

    check("B3 [exact] the uniform-configuration filter is sound -- if some intended "
          "star can be made all-0 or all-1 by the code bits, that uniform "
          "configuration has penalty 0 and is no translate -- with pass counts "
          "%d/%d, %d/%d, %d/%d"
          % (res[(3, 1)]["npass"], res[(3, 1)]["tot"],
             res[(3, 2)]["npass"], res[(3, 2)]["tot"],
             res[(4, 2)]["npass"], res[(4, 2)]["tot"]),
          res[(3, 1)]["npass"] == 282 and res[(3, 2)]["npass"] == 282
          and res[(4, 2)]["npass"] == 32)

    def cen(r):
        return " ".join("%dx%d%d%d" % (v, k[0], k[1], k[2])
                        for k, v in sorted(r["cnt"].items(), key=lambda kv: -kv[1]))

    r1, r2, r3 = res[(3, 1)], res[(3, 2)], res[(4, 2)]
    check("B4 [exact, exhaustive propagation, no SAT] s=3, both code positions, all "
          "%d assignments each: %d and %d admit junk, %d are junk-free; the period "
          "multiset census of the lexicographically least junk witness is the same "
          "for both, count x abc = %s (intended 333); %d branch nodes, %d at worst"
          % (r1["tot"], r1["njunk"], r2["njunk"],
             r1["tot"] - r1["njunk"] + r2["tot"] - r2["njunk"], cen(r1),
             r1["nodes"] + r2["nodes"], max(r1["maxnodes"], r2["maxnodes"])),
          r1["njunk"] == r1["tot"] and r2["njunk"] == r2["tot"]
          and cen(r1) == cen(r2))
    check("B5 [exact, exhaustive propagation, no SAT] s=4 midpoint, all %d "
          "assignments: %d admit junk, %d junk-free; census count x abc = %s "
          "(intended 444); %d branch nodes, %d at worst"
          % (r3["tot"], r3["njunk"], r3["tot"] - r3["njunk"], cen(r3),
             r3["nodes"], r3["maxnodes"]), r3["njunk"] == r3["tot"])

    tot = sum(res[c]["njunk"] for c in cases)
    lift = sum(res[c]["nlift"] for c in cases)
    check("B6 [exact] each of the %d witnesses tiles to the 2s-torus (6^3 and 8^3) "
          "with penalty 0, still no translate or rotation of the intended pattern, so "
          "junk survives the doubled box, %d of %d: no covariant maximal "
          "value-reading star rule tested is junk-free"
          % (tot, lift, tot), lift == tot and tot == 2560)


# ================================= C: state-reading star templates (quantum)

R2 = 1.0 / np.sqrt(2.0)
PST = {"0": np.array([1, 0], dtype=complex),
       "1": np.array([0, 1], dtype=complex),
       "+": np.array([R2, R2], dtype=complex),
       "-": np.array([R2, -R2], dtype=complex),
       "i": np.array([R2, 1j * R2], dtype=complex),
       "j": np.array([R2, -1j * R2], dtype=complex)}
NAMES = ["0", "1", "+", "-", "i", "j"]


def kron_list(vs):
    out = np.array([1.0 + 0j])
    for v in vs:
        out = np.kron(out, v)
    return out


def eb(b):
    return PST["0"] if b == 0 else PST["1"]


def K_basis_2d(v, f, variant):
    """Intended role-star states, 2D: slots c, +x, -x, +y, -y."""
    V = []
    for bits in itertools.product((0, 1), repeat=4):
        if variant == "EVEN" and sum(bits) % 2:
            continue
        V.append(kron_list([v] + [eb(b) for b in bits]))
    for bits in itertools.product((0, 1), repeat=4):
        V.append(kron_list([f] + [eb(b) for b in bits]))
    for cb in (0, 1):
        V.append(kron_list([eb(cb), v, v, f, f]))
        V.append(kron_list([eb(cb), f, f, v, v]))
    return np.array(V)


def K_basis_3d(v, f, c, variant):
    V = []
    for bits in itertools.product((0, 1), repeat=6):
        if variant == "EVEN" and sum(bits) % 2:
            continue
        V.append(kron_list([v] + [eb(b) for b in bits]))
    V.append(kron_list([c] + [f] * 6))
    for ax in range(3):
        for bits in itertools.product((0, 1), repeat=4):
            nb = [None] * 6
            it = iter(bits)
            for a in range(3):
                if a == ax:
                    nb[2 * a] = c
                    nb[2 * a + 1] = c
                else:
                    nb[2 * a] = eb(next(it))
                    nb[2 * a + 1] = eb(next(it))
            V.append(kron_list([f] + nb))
    for ax in range(3):
        for cb in (0, 1):
            nb = []
            for a in range(3):
                nb += [v, v] if a == ax else [f, f]
            V.append(kron_list([eb(cb)] + nb))
    return np.array(V)


def K_basis_1d(v, variant):
    V = []
    for bits in itertools.product((0, 1), repeat=2):
        if variant == "EVEN" and sum(bits) % 2:
            continue
        V.append(kron_list([v, eb(bits[0]), eb(bits[1])]))
    for cb in (0, 1):
        V.append(kron_list([eb(cb), v, v]))
    return np.array(V)


def projector(rows, tol=1e-9):
    M = np.array(rows).T
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    r = int((s > tol * max(1.0, s[0])).sum())
    B = U[:, :r]
    return B @ B.conj().T, r


def lattice(shape):
    dim = len(shape)
    coords = list(itertools.product(*[range(L) for L in shape]))
    index = {c: i for i, c in enumerate(coords)}
    stars = []
    for c in coords:
        slots = [c]
        for a in range(dim):
            p = list(c)
            p[a] = (c[a] + 1) % shape[a]
            slots.append(tuple(p))
            m = list(c)
            m[a] = (c[a] - 1) % shape[a]
            slots.append(tuple(m))
        stars.append([index[t] for t in slots])
    return coords, index, stars


def compress(Pi, slots, nslots):
    """Pull Pi back through the diagonal isometry V of the repeated slots."""
    dist = sorted(set(slots))
    k = len(dist)
    pos = {s: j for j, s in enumerate(dist)}
    idx = np.zeros(2 ** k, dtype=int)
    for p in range(2 ** k):
        bits = [(p >> (k - 1 - j)) & 1 for j in range(k)]
        si = 0
        for i, s in enumerate(slots):
            si |= bits[pos[s]] << (nslots - 1 - i)
        idx[p] = si
    return dist, Pi[np.ix_(idx, idx)]


def star_projectors(shape, Pi, nslots):
    coords, index, stars = lattice(shape)
    out = []
    aliased = False
    for slots in stars:
        if len(set(slots)) == nslots:
            out.append((list(slots), Pi))
            continue
        aliased = True
        dist, A = compress(Pi, slots, nslots)
        w, U = np.linalg.eigh(A)
        sel = w > 1 - 1e-9
        out.append((dist, U[:, sel] @ U[:, sel].conj().T))
    return coords, len(coords), out, aliased


def apply_local(M, sites, n, X):
    m = X.shape[1]
    k = len(sites)
    T = X.reshape([2] * n + [m])
    T = np.moveaxis(T, sites, range(k))
    sh = T.shape
    T = (M @ T.reshape(2 ** k, -1)).reshape(sh)
    T = np.moveaxis(T, range(k), sites)
    return T.reshape(2 ** n, m)


def energy(projs, n, X):
    Y = np.zeros_like(X)
    for ax, Q in projs:
        Y += X - apply_local(Q, ax, n, X)
    return np.real(np.einsum("ij,ij->j", X.conj(), Y))


def intended_products(shape, pins, variant):
    """The intended global states as lists of single-site factors."""
    dim = len(shape)
    coords, index, stars = lattice(shape)
    out = []
    for off in itertools.product((0, 1), repeat=dim):
        roles = [sum((c[a] + off[a]) % 2 for a in range(dim)) for c in coords]
        edges = [i for i, r in enumerate(roles) if r == 1]
        epos = {s: j for j, s in enumerate(edges)}
        cons = []
        if variant == "EVEN":
            for i, r in enumerate(roles):
                if r:
                    continue
                cntd = {}
                for s in stars[i][1:]:
                    cntd[s] = cntd.get(s, 0) + 1
                mask = [epos[s] for s, ct in cntd.items() if ct % 2]
                if mask:
                    cons.append(mask)
        for bits in itertools.product((0, 1), repeat=len(edges)):
            if any(sum(bits[j] for j in cs) % 2 for cs in cons):
                continue
            out.append([eb(bits[epos[i]]) if roles[i] == 1 else pins[roles[i]]
                        for i in range(len(coords))])
    return out


def span_tools(pl):
    """Rank and pseudo-inverse Gram of the intended span, without materialising it."""
    N = len(pl)
    G = np.ones((N, N), dtype=complex)
    for i in range(len(pl[0])):
        col = np.array([p[i] for p in pl])
        G *= col.conj() @ col.T
    w, U = np.linalg.eigh(G)
    keep = w > 1e-8 * max(w.max(), 1.0)
    r = int(keep.sum())
    return r, (U[:, keep] * (1.0 / w[keep])) @ U[:, keep].conj().T


def overlaps(pl, X):
    C = np.empty((len(pl), X.shape[1]), dtype=complex)
    for a, p in enumerate(pl):
        C[a] = kron_list(p).conj() @ X
    return C


def intended_err(projs, n, pl, seed=3, k=4):
    idx = np.random.default_rng(seed).choice(len(pl), size=min(k, len(pl)),
                                             replace=False)
    Y = np.array([kron_list(pl[i]) for i in idx]).T.copy()
    return float(np.abs(energy(projs, n, Y)).max())


def dense_case(shape, Kb, pins, variant, nslots):
    """Exact dense nullity on a small torus (at most 8 qubits)."""
    Pi, dimK = projector(Kb)
    if dimK == 2 ** nslots:
        return dict(dimK=dimK, vacuous=True)
    coords, n, projs, aliased = star_projectors(shape, Pi, nslots)
    d = 2 ** n
    H = np.zeros((d, d), dtype=complex)
    I = np.eye(d, dtype=complex)
    for ax, Q in projs:
        H += I - apply_local(Q, ax, n, I)
    w = np.linalg.eigvalsh(H)
    pl = intended_products(shape, pins, variant)
    r, _ = span_tools(pl)
    return dict(dimK=dimK, vacuous=False, nullity=int((w < 1e-9).sum()),
                expected=r, ierr=intended_err(projs, n, pl), aliased=aliased)


def pocs_case(shape, Kb, pins, variant, nslots, M=4, maxsweeps=400,
              tol=1e-13, seed=20260903):
    """Matrix-free: alternating projections onto the intersection of star kernels."""
    Pi, dimK = projector(Kb)
    coords, n, projs, aliased = star_projectors(shape, Pi, nslots)
    pl = intended_products(shape, pins, variant)
    r, Ginv = span_tools(pl)
    rng = np.random.default_rng(seed)
    X = (rng.standard_normal((2 ** n, M))
         + 1j * rng.standard_normal((2 ** n, M))) / np.sqrt(2.0)
    X0 = X.copy()
    it = 0
    while it < maxsweeps:
        for ax, Q in projs:
            X = apply_local(Q, ax, n, X)
        it += 1
        if it % 10 == 0:
            nrm2 = np.maximum(np.linalg.norm(X, axis=0) ** 2, 1e-300)
            if (energy(projs, n, X) / nrm2).max() < tol:
                break
    nrm2 = np.maximum(np.linalg.norm(X, axis=0) ** 2, 1e-300)
    resid = float((energy(projs, n, X) / nrm2).max())
    ov = np.real(np.einsum("ij,ij->j", X0.conj(), X))
    C = overlaps(pl, X)
    inside = np.real(np.einsum("ai,ab,bi->i", C.conj(), Ginv, C)) / nrm2
    return dict(dimK=dimK, expected=r, resid=resid, sweeps=it,
                est=float(ov.mean()), se=float(ov.std(ddof=1) / np.sqrt(M)),
                jlo=float(1 - inside.max()), jhi=float(1 - inside.min()),
                ierr=intended_err(projs, n, pl))


def junk_character(shape, Kb, pins, variant, nslots, seed=5, sweeps=200,
                   tol=1e-13):
    Pi, dimK = projector(Kb)
    coords, n, projs, aliased = star_projectors(shape, Pi, nslots)
    pl = intended_products(shape, pins, variant)
    r, Ginv = span_tools(pl)
    rng = np.random.default_rng(seed)
    x = (rng.standard_normal((2 ** n, 1))
         + 1j * rng.standard_normal((2 ** n, 1))) / np.sqrt(2.0)
    it = 0
    while it < sweeps:
        for ax, Q in projs:
            x = apply_local(Q, ax, n, x)
        it += 1
        if it % 10 == 0:
            if float(energy(projs, n, x)[0]) / max(
                    float(np.linalg.norm(x) ** 2), 1e-300) < tol:
                break
    a = Ginv @ overlaps(pl, x)
    proj = np.zeros_like(x)
    for i, p in enumerate(pl):
        proj[:, 0] += a[i, 0] * kron_list(p)
    v = x - proj
    v /= np.linalg.norm(v)
    E = float(energy(projs, n, v)[0])
    C = overlaps(pl, v)
    ins = float(np.real(C.conj().T @ Ginv @ C)[0, 0])
    T = v.reshape([2] * n)
    half = n // 2
    sv = np.linalg.svd(T.reshape(2 ** half, 2 ** half), compute_uv=False)
    sr = int((sv > 1e-8 * sv[0]).sum())
    pur = []
    for i in range(n):
        A = np.moveaxis(T, i, 0).reshape(2, -1)
        rho = A @ A.conj().T
        pur.append(float(np.real(np.trace(rho @ rho))))
    return dict(E=E, inside=ins, rank=sr, dim=2 ** half, maxpur=max(pur))


def group_C():
    diag = np.array([[1, 0], [0, 0], [0, 0], [0, 1]], dtype=complex).T
    ok = True
    for nm in NAMES:
        p = PST[nm]
        w = np.kron(p, p)
        res = np.linalg.norm(w - diag.T @ (diag.conj() @ w))
        if (res < 1e-12) != (nm in "01"):
            ok = False
    check("C1 [exact] aliasing lemma, algebraic half: a side of length 2 identifies "
          "the two +- neighbour slots on that axis, so the star term is the pullback "
          "h = 1 - V^dag Pi_K V and the image of the diagonal isometry V on that pair "
          "is span{|00>,|11>}, holding the pinned product |p>|p> exactly when ab = 0 "
          "for |p> = a|0> + b|1>, a Z eigenstate; on all %d pins"
          % len(NAMES), ok)

    rows = {}
    nvac = nfaith = nunf = 0
    unf_nonZ = True
    for vn in NAMES:
        for fn in NAMES:
            for var in ("EVEN", "FULL"):
                r = dense_case((4, 2), K_basis_2d(PST[vn], PST[fn], var),
                               {0: PST[vn], 2: PST[fn]}, var, 5)
                if r["vacuous"]:
                    nvac += 1
                    if not (var == "FULL" and vn != fn):
                        unf_nonZ = False
                    continue
                if r["ierr"] < 1e-9:
                    nfaith += 1
                    rows[(vn, fn, var)] = r
                else:
                    nunf += 1
                    if vn in "01" or fn in "01":
                        unf_nonZ = False
    jz = [rows[k]["nullity"] - rows[k]["expected"]
          for k in [("0", "0", "EVEN"), ("0", "0", "FULL"), ("0", "1", "EVEN")]]
    check("C2 [exact] aliasing lemma, computed half, 2D 4x2 torus in full: of the 72 "
          "(pin pair, variant) cases %d are vacuous -- exactly FULL at all 30 pairs "
          "with v != f -- and of the %d live cases %d are faithful and %d not, the "
          "unfaithful being exactly those with neither pin a Z eigenstate"
          % (nvac, nfaith + nunf, nfaith, nunf),
          nvac == 30 and nfaith == 22 and nunf == 20 and unf_nonZ)

    check("C3 [exact] 2D 4x2 torus, faithful Z-pin rows: v=f=|0> gives dim K = %d, "
          "nullity %d against %d intended, so %d junk zero modes in EVEN and %d in "
          "FULL; v=|0> f=|1> gives dim K = %d, nullity %d against %d, so %d junk. No "
          "faithful pin choice on this torus is junk-free"
          % (rows[("0", "0", "EVEN")]["dimK"], rows[("0", "0", "EVEN")]["nullity"],
             rows[("0", "0", "EVEN")]["expected"], jz[0], jz[1],
             rows[("0", "1", "EVEN")]["dimK"], rows[("0", "1", "EVEN")]["nullity"],
             rows[("0", "1", "EVEN")]["expected"], jz[2]),
          jz == [12, 4, 36] and all(rows[k]["nullity"] > rows[k]["expected"]
                                    for k in rows))

    dk = {"EVEN": [], "FULL": []}
    zfaith = True
    for vn in "01+-":
        for fn in "01+-":
            for cn in "01+-":
                for var in ("EVEN", "FULL"):
                    Kb = K_basis_3d(PST[vn], PST[fn], PST[cn], var)
                    Pi, d = projector(Kb)
                    dk[var].append(d)
                    if vn in "01" and fn in "01" and cn in "01":
                        coords, n, projs, al = star_projectors((4, 2, 2), Pi, 7)
                        pl = intended_products(
                            (4, 2, 2), {0: PST[vn], 2: PST[fn], 3: PST[cn]}, var)
                        if intended_err(projs, n, pl) > 1e-9:
                            zfaith = False
    check("C4 [exact] 3D seven-site star, all 64 pin triples from {0,1,+,-} and both "
          "variants: dim K runs %d-%d of 128 in EVEN and %d-%d in FULL, so no "
          "template is vacuous, and all 16 all-Z triples are faithful on the 4x2x2 "
          "torus -- which is why the 3D rows use Z pins only"
          % (min(dk["EVEN"]), max(dk["EVEN"]), min(dk["FULL"]), max(dk["FULL"])),
          min(dk["EVEN"]) == 51 and max(dk["EVEN"]) == 76
          and min(dk["FULL"]) == 65 and max(dk["FULL"]) == 105
          and max(dk["EVEN"] + dk["FULL"]) < 128 and zfaith)

    c2d = [(("+", "+"), "EVEN"), (("+", "+"), "FULL"), (("0", "1"), "EVEN"),
           (("+", "-"), "EVEN"), (("0", "+"), "EVEN")]
    r2d = {}
    for (vn, fn), var in c2d:
        r2d[(vn, fn, var)] = pocs_case(
            (4, 4), K_basis_2d(PST[vn], PST[fn], var),
            {0: PST[vn], 2: PST[fn]}, var, 5)
    frs = [(r2d[k]["jlo"], r2d[k]["jhi"]) for k in r2d]
    txt = " ; ".join("%s%s %s %.2f-%.2f" % (k[0], k[1], k[2][0], v["jlo"], v["jhi"])
                     for k, v in r2d.items())
    check("C5 [numerical, matrix-free, seed fixed] 2D 4x4 torus, no aliasing, state "
          "vectors of length 65536: alternating projections from a random start reach "
          "residual energy at most %.0e and carry junk fraction (weight outside the "
          "intended span) %s"
          % (max(v["resid"] for v in r2d.values()), txt),
          max(v["resid"] for v in r2d.values()) < 1e-12
          and min(f[0] for f in frs) > 0.25 and max(v["ierr"] for v in r2d.values()) < 1e-9)

    est = " ; ".join("%s%s %s %.0f+-%.0f vs %d intended"
                     % (k[0], k[1], k[2][0], v["est"], v["se"], v["expected"])
                     for k, v in r2d.items())
    check("C6 [numerical, stochastic, seed fixed] the same runs give Hutchinson trace "
          "estimates of the kernel dimension, %d probes, one standard error: %s -- "
          "each far above its intended count" % (4, est),
          all(v["est"] - 3 * v["se"] > v["expected"] for v in r2d.values()))

    c3d = [(("0", "0", "0"), "EVEN"), (("0", "0", "0"), "FULL"),
           (("0", "1", "0"), "EVEN"), (("0", "1", "1"), "EVEN")]
    r3d = {}
    for (vn, fn, cn), var in c3d:
        r3d[(vn, fn, cn, var)] = pocs_case(
            (4, 2, 2), K_basis_3d(PST[vn], PST[fn], PST[cn], var),
            {0: PST[vn], 2: PST[fn], 3: PST[cn]}, var, 7)
    t3 = " ; ".join("%s%s%s %s dimK=%d junkfrac %.2f-%.2f est %.0f+-%.0f vs %d"
                    % (k[0], k[1], k[2], k[3][0], v["dimK"], v["jlo"], v["jhi"],
                       v["est"], v["se"], v["expected"]) for k, v in r3d.items())
    check("C7 [numerical, matrix-free, seed fixed] 3D 4x2x2 torus, Z pins, the "
          "faithful case: %s; residual energy at most %.0e, intended-state energy at "
          "most %.0e" % (t3, max(v["resid"] for v in r3d.values()),
                         max(v["ierr"] for v in r3d.values())),
          max(v["resid"] for v in r3d.values()) < 1e-12
          and min(v["jlo"] for v in r3d.values()) > 0.4
          and all(v["est"] - 3 * v["se"] > v["expected"] for v in r3d.values()))

    j2 = junk_character((4, 4), K_basis_2d(PST["+"], PST["+"], "EVEN"),
                        {0: PST["+"], 2: PST["+"]}, "EVEN", 5)
    j3 = junk_character((4, 2, 2), K_basis_3d(PST["0"], PST["0"], PST["0"], "EVEN"),
                        {0: PST["0"], 2: PST["0"], 3: PST["0"]}, "EVEN", 7)
    check("C8 [numerical, matrix-free, seed fixed] the junk is a superposition of "
          "role assignments, not a rival pattern: the extracted vector has energy at "
          "most %.0e, weight inside the intended span at most %.0e, Schmidt rank %d "
          "and %d across a half cut of %d, every single-site reduced state mixed with "
          "purity at most %.3f and %.3f -- no site is pinned"
          % (max(j2["E"], j3["E"]), max(j2["inside"], j3["inside"]), j2["rank"],
             j3["rank"], j2["dim"], j2["maxpur"], j3["maxpur"]),
          max(j2["E"], j3["E"]) < 1e-12 and max(j2["inside"], j3["inside"]) < 1e-12
          and j2["rank"] > 1 and j3["rank"] > 1
          and max(j2["maxpur"], j3["maxpur"]) < 0.8)

    out = []
    jf = []
    for var in ("EVEN", "FULL"):
        for vn in "01+-":
            r = dense_case((8,), K_basis_1d(PST[vn], var), {0: PST[vn]}, var, 3)
            j = r["nullity"] - r["expected"]
            out.append((vn, var, r["dimK"], r["nullity"], r["expected"], j))
            if j == 0 and r["ierr"] < 1e-9:
                jf.append((vn, var))
    check("C9 [exact] the one-dimensional contrast, three-site stars on an 8-ring: Z "
          "pins in the EVEN variant are junk-free, dim K = 3 and nullity 3 equal to "
          "the 3 intended states, while |+> and |-> in EVEN give nullity 9 against 4 "
          "and every FULL choice 47 against 31; %d of 8 junk-free, so the failure "
          "above is no artefact of the construction" % len(jf),
          sorted(jf) == [("0", "EVEN"), ("1", "EVEN")]
          and [o[3:] for o in out if o[1] == "EVEN" and o[0] == "0"] == [(3, 3, 0)])


def main():
    group_A()
    group_B()
    group_C()
    print("SUMMARY: on the classes and clusters tested no junk-free star-local rule "
          "of either kind was found; value-reading rules fail by period collapse, "
          "state-reading ones by superposition junk.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
