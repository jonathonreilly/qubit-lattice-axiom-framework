#!/usr/bin/env python3
"""Search for three-dimensionally mobile fermionic charges in symmetric star-supported stabilizer rules.

Site = three axis-indexed qubits; O permutes them as axes and acts on Pauli labels trivially
(unsoldered) or by the full soldered action (as in the three-axis-qubit companion runner).

1. Statistics tool: Levin-Wen T-junction sign for a point charge (product of pairwise commutation
   signs of three leg operators that move the charge pattern from 0 to 2e_x, 2e_y, 2e_z). Controls:
   2D toric code e, m (+1) and e x m (-1).
2. Alphabet lemma (finite part): for every abelian single-site alphabet A met below, A is its own
   single-site commutant and the complement of every proper subgroup of A generates A.
3. Soldered, all strings fixed by some nontrivial rotation: the survivor set (34927 strings) is
   loaded from the loop pack and every element is re-verified (fixed by C2z, C2 edge, C4z or C3;
   commutes with all translates of all rotated images). The C4/C3 and edge-C2 parts are recomputed
   from scratch; the axis-C2 part (64^5 strings) is recomputed only with --full.
   Structure: 4319 sign-consistent orbits; 4259 use only the alphabet <X_x, Y_y, Z_z>; the other 60
   lie in ten maximal commuting sets: eight valid 3-orbit sets (3L^3 - rank 48, 72) and two (43, 47
   orbits) whose unions contain -1 (3L^3 - rank 32, 48).
4. Unsoldered, C4/C3-fixed strings: the 36 valid maximal sets with equal nonzero code dimension at
   L = 4, 6 (from the loop-pack search) are re-checked: log2 dimension 24, and every same-site charge
   pattern that moves by 2e_x, 2e_y, 2e_z is a boson.
"""

from __future__ import annotations

import itertools
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1  # noqa: E402
import three_axis_qubit_site_stabilizer_rules_soldering_and_three_dimensional_charge_mobility_2026_10_17 as c3  # noqa: E402

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = (
    'docs/THREE_AXIS_QUBIT_SYMMETRIC_STABILIZER_RULES_FERMION_SEARCH_FINDS_NO_COHERENTLY_MOBILE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    '.claude/science/physics-loops/toe-campaign-20261017/c4_fermion_search/soldered_symmetric_survivors.npy',
    '.claude/science/physics-loops/toe-campaign-20261017/c4_fermion_search/unsoldered_bounded_rules.json',
)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACK = os.path.join(ROOT, '.claude/science/physics-loops/toe-campaign-20261017/c4_fermion_search')
STAR, SIDX, O = c1.STAR, c1.SIDX, c1.O
SYM = {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}


# ---------------------------------------------------------------- statistics tool
def build_box(gens, q, R):
    sites = list(itertools.product(range(-R, R + 1), repeat=3))
    sidx = {p: i for i, p in enumerate(sites)}
    nq = q * len(sites)
    inst = [(v, j) for v in sites for j, g in enumerate(gens) if all(tuple(np.add(v, p)) in sidx for p in g)]
    M = np.zeros((len(inst), 2 * nq), np.uint8)
    for r, (v, j) in enumerate(inst):
        for p, labs in gens[j].items():
            s = sidx[tuple(np.add(v, p))]
            for a, l in enumerate(labs):
                xb, zb = SYM[l]
                if zb:
                    M[r, q * s + a] ^= 1
                if xb:
                    M[r, nq + q * s + a] ^= 1
    return inst, M, nq


def solve_many(M, T):
    """Solve M w = t for each column t of T over GF(2); returns list of w or None."""
    m, n = M.shape
    A = np.concatenate([M, T], axis=1).astype(np.uint8)
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i, c]), None)
        if p is None:
            continue
        A[[r, p]] = A[[p, r]]
        rows = np.nonzero(A[:, c])[0]
        rows = rows[rows != r]
        A[rows] ^= A[r]
        piv.append(c)
        r += 1
        if r == m:
            break
    out = []
    for k in range(T.shape[1]):
        col = A[:, n + k]
        if any(col[i] for i in range(r, m)):
            out.append(None)
            continue
        w = np.zeros(n, np.uint8)
        for i, c in enumerate(piv):
            w[c] = col[i]
        out.append(w)
    return out


def symp(w1, w2, nq):
    return int((w1[:nq] @ w2[nq:] + w1[nq:] @ w2[:nq]) % 2)


def junction_signs(gens, q, patterns, legs=((2, 0, 0), (0, 2, 0), (0, 0, 2)), R=3):
    """For each charge pattern (list of (offset, generator)), the exchange sign or None if not movable."""
    inst, M, nq = build_box(gens, q, R)
    iidx = {x: i for i, x in enumerate(inst)}
    cols = []
    for pat in patterns:
        for t in legs:
            v = np.zeros(len(inst), np.uint8)
            for off, j in pat:
                v[iidx[(tuple(off), j)]] ^= 1
                v[iidx[(tuple(np.add(off, t)), j)]] ^= 1
            cols.append(v)
    sols = solve_many(M, np.stack(cols, axis=1))
    res = []
    for k in range(len(patterns)):
        W = sols[3 * k:3 * k + 3]
        if any(w is None for w in W):
            res.append(None)
        else:
            res.append((-1) ** (symp(W[0], W[1], nq) + symp(W[1], W[2], nq) + symp(W[0], W[2], nq)))
    return res


# ---------------------------------------------------------------- helpers
def dec(a):
    return [((int(a) >> (6 * i)) & 63) for i in range(7)]


def gens_of(codes):
    return [{STAR[i]: tuple((l[i] >> (2 * a)) & 3 for a in range(3)) for i in range(7) if l[i]} for l in map(dec, codes)]


MUL = {(1, 2): (3, 1), (2, 1): (3, 3), (2, 3): (1, 1), (3, 2): (1, 3), (3, 1): (2, 1), (1, 3): (2, 3)}


def torus_signed(signed, L):
    """log2 code dimension and number of inconsistent relations (-1 or +-i) on the L^3 torus."""
    n = 3 * L ** 3
    idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    rows, ops = [], []
    for v in itertools.product(range(L), repeat=3):
        for code, sg in signed:
            x = np.zeros(2 * n, np.uint8)
            op = {}
            for i, l in enumerate(dec(code)):
                if not l:
                    continue
                p = [v[j] + STAR[i][j] for j in range(3)]
                for a in range(3):
                    lab = (l >> (2 * a)) & 3
                    if not lab:
                        continue
                    qq = idx(p, a)
                    op[qq] = lab
                    if lab in (1, 2):
                        x[qq] ^= 1
                    if lab in (2, 3):
                        x[n + qq] ^= 1
            rows.append(x)
            ops.append((op, sg))
    r, N = c1.f2_rank_and_null(np.array(rows))
    bad = 0
    for c in N:
        cur, ph = {}, 0
        for k in np.nonzero(c)[0]:
            op, sg = ops[k]
            if sg < 0:
                ph += 2
            for qq, P in op.items():
                Q = cur.get(qq)
                if Q is None:
                    cur[qq] = P
                elif Q == P:
                    del cur[qq]
                else:
                    cur[qq], e = MUL[(Q, P)]
                    ph += e
        if cur or ph % 4:
            bad += 1
    return n - r, bad


def main() -> int:
    ck = c1.Checks()
    full = '--full' in sys.argv
    X, Z = 1, 3

    # ---------------- 1. statistics tool controls
    A2 = {(0, 0, 0): (X, X), (-1, 0, 0): (X, 0), (0, -1, 0): (0, X)}
    B2 = {(0, 0, 0): (Z, Z), (0, 1, 0): (Z, 0), (1, 0, 0): (0, Z)}
    legs2 = ((2, 0, 0), (0, 2, 0), (-2, -2, 0))
    s = junction_signs([A2, B2], 2, [[((0, 0, 0), 0)], [((0, 0, 0), 1)], [((0, 0, 0), 0), ((0, 0, 0), 1)]], legs=legs2, R=4)
    ck.check('statistics tool: 2D toric code e and m are bosons (+1) and e x m is a fermion (-1)', s == [1, 1, -1])

    # ---------------- 2. alphabet lemma (finite part)
    def anti(s1, s2):
        n_ = 0
        for a in range(3):
            la, lb = (s1 >> (2 * a)) & 3, (s2 >> (2 * a)) & 3
            n_ += int(la != 0 and lb != 0 and la != lb)
        return n_ % 2

    def xor_mul(a, b):   # product of 3-qubit Pauli labels, ignoring phase
        out = 0
        for q in range(3):
            la, lb = (a >> (2 * q)) & 3, (b >> (2 * q)) & 3
            xa, za = SYM[la]
            xb, zb = SYM[lb]
            out |= {(0, 0): 0, (1, 0): 1, (1, 1): 2, (0, 1): 3}[(xa ^ xb, za ^ zb)] << (2 * q)
        return out

    def span(S):
        G = {0}
        for g in S:
            G |= {xor_mul(g, h) for h in G}
        return G

    alphabets = [span([1, 2 << 2, 3 << 4])]   # <X_x, Y_y, Z_z>
    for P in (1, 2, 3):                          # <P_x, P_y, P_z>
        alphabets.append(span([P, P << 2, P << 4]))
    ok = True
    for Al in alphabets:
        Al1 = Al - {0}
        ok &= len(Al) == 8 and all(not anti(a, b) for a in Al1 for b in Al1)
        ok &= {p for p in range(1, 64) if all(not anti(p, l) for l in Al1)} == Al1
        subs = {frozenset(span(S)) for r_ in range(0, 3) for S in itertools.combinations(sorted(Al1), r_)}
        ok &= all(span(Al - set(H)) == Al for H in subs if len(H) < 8)
    ck.check('alphabet lemma, finite part: each alphabet used is abelian, is its own single-site commutant, and the complement of every proper subgroup generates it',
             ok)

    # ---------------- 3. soldered, all rotation-fixed strings
    T1 = c3.site_tables('full')
    S = np.load(os.path.join(PACK, 'soldered_symmetric_survivors.npy')).astype(np.uint64)
    ks = [c3.find(np.diag([-1, -1, 1])), c3.find(np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])),
          c3.find(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])), c3.find(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))]
    fixed = np.zeros(S.size, bool)
    for k in ks:
        fixed |= c3.transform(T1, S, k)[0] == S
    comm = c3.commutes_all(S, S)
    for kk in range(1, 24):
        comm &= c3.commutes_all(S, c3.transform(T1, S, kk)[0])
    ck.check('soldered: all 34927 loaded strings are fixed by a C2 (axis or edge), C4 or C3 rotation and commute with every translate of every rotated image',
             S.size == 34927 and fixed.all() and comm.all())
    recomputed = []
    for k in ks[1:]:
        a = c3.invariant_strings(T1, k)
        a = a[a != 0]
        a = a[c3.commutes_all(a, a)]
        for kk in range(1, 24):
            a = a[c3.commutes_all(a, c3.transform(T1, a, kk)[0])]
        recomputed.append(a)
    part = np.unique(np.concatenate(recomputed))
    ck.check('soldered: recomputed from scratch, the C4-, C3- and edge-C2-fixed survivors are all in the loaded set (axis-C2 completeness needs --full)',
             np.isin(part, S).all())
    if full:
        a = c3.invariant_strings(T1, ks[0])
        a = a[a != 0]
        keep = []
        for st in range(0, a.size, 1 << 22):
            b = a[st:st + (1 << 22)]
            b = b[c3.commutes_all(b, b)]
            for kk in range(1, 24):
                b = b[c3.commutes_all(b, c3.transform(T1, b, kk)[0])]
            keep.append(b)
        allS = np.unique(np.concatenate([part] + keep))
        ck.check('soldered (--full): the recomputed survivor set equals the loaded set', np.array_equal(allS, np.unique(S)))
    reps = np.unique(np.stack([c3.transform(T1, S, k)[0] for k in range(24)]).min(axis=0))
    TR = np.stack([c3.transform(T1, reps, k)[0] for k in range(24)])
    GR = np.stack([c3.transform(T1, reps, k)[1] for k in range(24)])
    cons = np.ones(reps.size, bool)
    for k in range(24):
        for l in range(k + 1, 24):
            cons &= (TR[k] != TR[l]) | (GR[k] == GR[l])
    reps, TR, GR = reps[cons], TR[:, cons], GR[:, cons]
    elems = [np.unique(TR[:, i]) for i in range(reps.size)]
    alph = alphabets[0]
    inA = [set(l for e in elems[i] for l in dec(e)) <= alph for i in range(reps.size)]
    ck.check('soldered: 4319 sign-consistent orbits, of which 4259 use only the alphabet <X_x, Y_y, Z_z>',
             reps.size == 4319 and sum(inA) == 4259)
    allel = np.concatenate(elems)
    owner = np.concatenate([np.full(e.size, i) for i, e in enumerate(elems)])
    outs = [i for i in range(reps.size) if not inA[i]]
    adj = {}
    nodes = set(outs)
    for i in outs:
        bad = set(owner[~c3.commutes_all(np.full(allel.shape, reps[i], np.uint64), allel)].tolist())
        adj[i] = {j for j in range(reps.size) if j != i and j not in bad}
        nodes |= adj[i]
    nodes = sorted(nodes)
    for i in nodes:
        if i not in adj:
            bad = set(owner[~c3.commutes_all(np.full(allel.shape, reps[i], np.uint64), allel)].tolist())
            adj[i] = {j for j in range(reps.size) if j != i and j not in bad}
    loc = {v: i for i, v in enumerate(nodes)}
    sadj = {loc[v]: {loc[w] for w in adj[v] if w in loc} for v in nodes}
    cls = [sorted(nodes[i] for i in c) for c in c1.maximal_cliques(len(nodes), sadj)]
    cls = [c for c in cls if any(k in outs for k in c)]
    summary = []
    for c in cls:
        signed = []
        for k in c:
            seen = {}
            for kk in range(24):
                seen[int(TR[kk, k])] = int(GR[kk, k])
            signed += list(seen.items())
        summary.append((len(c), torus_signed(signed, 4), torus_signed(signed, 6)))
    print('soldered: maximal sets containing an outsider (size, (L4 dim, bad), (L6 dim, bad)):', sorted(summary))
    ck.check('soldered: the ten maximal sets containing a non-alphabet orbit are eight valid 3-orbit sets (dims 48, 72) and two of 43 and 47 orbits that contain -1 (3L^3 - rank 32, 48)',
             sorted(x[0] for x in summary) == [3] * 8 + [43, 47]
             and all(x[1] == (48, 0) and x[2] == (72, 0) for x in summary if x[0] == 3)
             and all(x[1][0] == 32 and x[2][0] == 48 and x[1][1] > 0 for x in summary if x[0] > 3))

    # ---------------- 4. unsoldered bounded rules: bosonic statistics
    rules = json.load(open(os.path.join(PACK, 'unsoldered_bounded_rules.json')))
    T0 = c3.site_tables('trivial')
    okdim, okstat, nmob = True, True, []
    for rule in rules:
        codes = [c for orb in rule['strings'] for c in orb]
        signed = []
        for orb in rule['strings']:
            rep = np.array([min(orb)], np.uint64)
            seen = {}
            for kk in range(24):
                t, g = c3.transform(T0, rep, kk)
                seen[int(t[0])] = int(g[0])
            signed += list(seen.items())
        okdim &= torus_signed(signed, 4) == (24, 0) and torus_signed(signed, 6) == (24, 0)
        gens = gens_of(codes)
        pats = [[((0, 0, 0), j) for j in sub] for r_ in range(1, len(gens) + 1) for sub in itertools.combinations(range(len(gens)), r_)]
        sg = junction_signs(gens, 3, pats)
        mob = [x for x in sg if x is not None]
        nmob.append(len(mob))
        okstat &= len(mob) >= 1 and all(x == 1 for x in mob)
    print(f'unsoldered: {len(rules)} bounded rules; mobile same-site charge patterns per rule: {sorted(set(nmob))}')
    ck.check('unsoldered: all 36 bounded maximal rules are valid with log2 code dimension 24 at L = 4 and L = 6', len(rules) == 36 and okdim)
    ck.check('unsoldered: in every one, each same-site charge pattern that moves by 2e_x, 2e_y, 2e_z is a boson (no fermion found)', okstat)

    print('per_element: soldered survivor set re-verified element by element; axis-C2 completeness only with --full')
    print('per_site: three axis-labelled qubits per site; no dynamics')
    print('per_mode: not applicable')
    print('per_block: not applicable')
    print('lattice_wide: tori L = 4, 6; statistics on an open box R = 3')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
