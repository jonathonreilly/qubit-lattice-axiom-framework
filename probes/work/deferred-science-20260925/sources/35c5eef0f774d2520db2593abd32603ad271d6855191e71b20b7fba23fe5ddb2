#!/usr/bin/env python3
"""Exact checks: the record gas does make the chessboard when a recorded bond is expensive - at zeta = g^-3 the framed
states of block 81's record gas differ at every site by at least 82/100 in the staggered variable for g <= 9/62500 without
contents and g <= 1/100000 at (3,1,2); contents act only on the wall (a harvest block from two Grok-refereed probes attempts;
block 81 as landed supplied; not adopted).

B (T1): the gas in its unlike-bond form; complement symmetry at zeta = g^-3 without contents.
C (T2): contents act on cycles and merges only; on p + q = 2r they only add weight.
D (T3): the translation map on near-chessboard arrangements of a framed box, and the weight bound through it.
E (T4, T5): the walls (fixed polycubes to 7 cells), the tree bound and the sum at x0 = 3/250; the bond scales per triple.
Exact rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_DOES_MAKE_THE_CHESSBOARD_WHEN_A_RECORDED_BOND_COSTS_A_FACTOR_BELOW_NINE_OVER_62500_AND_THE_TWO_FRAMED_STATES_DIFFER_AT_EVERY_SITE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_record_gas_does_make_the_chessboard_when_a_recorded_bond_costs_a_factor_below_nine_over_62500_and_the_two_framed_states_differ_at_every_site_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "unlike_form_forged": "B",
    "contents_sign_forged": "C",
    "unlike_drop_forged": "D",
    "wall_count_forged": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Fr = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: one record per site, records permanent (the gas's exclusion); each site has a domain of local possibilities (the six-axis contents); Admissibility is not a dynamics axiom (the record gas and its weights are supplied clauses)")


# ============================================================================================ lattice machinery
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
CONTENTS = DIRS


def dec(q, n=6):
    """a truncated decimal string of a rational, by integer arithmetic."""
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole = q.numerator // q.denominator
    frac = ((q - whole) * 10 ** n).numerator // ((q - whole) * 10 ** n).denominator
    return f"{sign}{whole}.{str(frac).zfill(n)}"


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def is_a(s):
    return (s[0] + s[1] + s[2]) % 2 == 0


class Lcg:
    """a deterministic integer generator for sampled configurations."""

    def __init__(self, seed):
        self.s = seed

    def next(self, m):
        self.s = (self.s * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        return (self.s >> 33) % m


def m_matrix(p, q, r):
    """block 81's bond factor M(s, s') = 6 omega/(p + q + 4r): omega = p, q, r for equal, opposite, orthogonal contents."""
    tot = p + q + 4 * r
    out = {}
    for a in CONTENTS:
        for b in CONTENTS:
            dot = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
            out[(a, b)] = Fr(6 * (p if dot == 1 else (q if dot == -1 else r)), tot)
    return out


def q_factor(vertices, edges, mm, cap=7):
    """Q = E_uniform[prod over bonds of M(s_x, s_y)] (block 81's Q(G)); leaves pruned first (each leaf averages to one)."""
    nbr = {v: [] for v in vertices}
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    alive = set(vertices)
    deg = {v: len(nbr[v]) for v in vertices}
    stack = [v for v in vertices if deg[v] <= 1]
    while stack:
        v = stack.pop()
        if v not in alive:
            continue
        alive.discard(v)
        for w in nbr[v]:
            if w in alive:
                deg[w] -= 1
                if deg[w] == 1:
                    stack.append(w)
    core = sorted(alive)
    if not core:
        return Fr(1)
    if len(core) > cap:
        return None
    core_edges = [(a, b) for (a, b) in edges if a in alive and b in alive]
    pos = {v: i for i, v in enumerate(core)}
    den = 1
    for v in mm.values():
        den = den * v.denominator // gcd(den, v.denominator)
    mi = [[(mm[(a, b)] * den).numerator for b in CONTENTS] for a in CONTENTS]
    idx = [(pos[a], pos[b]) for (a, b) in core_edges]
    tot = 0
    for assign in product(range(6), repeat=len(core)):
        w = 1
        for ia, ib in idx:
            w *= mi[assign[ia]][assign[ib]]
        tot += w
    return Fr(tot, 6 ** len(core) * den ** len(core_edges))


def cycle_rank(vertices, edges):
    parent = {v: v for v in vertices}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    comps = len(vertices)
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            comps -= 1
    return len(edges) - len(vertices) + comps


# ------------------------------------------------------------------------------ the framed box
BOX_L = 4
INTERIOR = [(x, y, z) for x in range(BOX_L) for y in range(BOX_L) for z in range(BOX_L)]
INTERIOR_SET = set(INTERIOR)
FRAME = {add(s, d) for s in INTERIOR for d in DIRS} - INTERIOR_SET
SITES = INTERIOR_SET | FRAME


def chessboard():
    return {s: (1 if is_a(s) else 0) for s in SITES}


def sigma(n, s):
    return 1 if n[s] == (1 if is_a(s) else 0) else -1


def bonds_meeting_interior():
    out = []
    for s in INTERIOR:
        for d in DIRS:
            t = add(s, d)
            if t in INTERIOR_SET and s < t:
                out.append((s, t))
            elif t in FRAME:
                out.append((s, t))
    return out


BOX_BONDS = bonds_meeting_interior()


def cluster_and_fill(n, x):
    comp, stack = {x}, [x]
    while stack:
        c = stack.pop()
        for d in DIRS:
            t = add(c, d)
            if t in INTERIOR_SET and t not in comp and sigma(n, t) == -1:
                comp.add(t)
                stack.append(t)
    rng = range(-2, BOX_L + 2)
    region = {(a, b, c) for a in rng for b in rng for c in rng}
    far = (-2, -2, -2)
    reach, stack = {far}, [far]
    while stack:
        c = stack.pop()
        for d in DIRS:
            t = add(c, d)
            if t in region and t not in reach and t not in comp:
                reach.add(t)
                stack.append(t)
    return comp, region - reach


def wall(vset):
    return [(v, d) for v in vset for d in DIRS if add(v, d) not in vset]


def unlike(n):
    return sum(1 for (s, t) in BOX_BONDS if n[s] == n[t])


def translate(n, vset, d):
    moved = {add(v, d) for v in vset}
    back, front = vset - moved, moved - vset
    out = dict(n)
    for y in moved:
        out[y] = n[sub(y, d)]
    for y in back:
        out[y] = 1 if is_a(y) else 0
    return out, back, front


def near_chessboard(rng, blobs, grow):
    n = chessboard()
    for _ in range(1 + rng.next(blobs)):
        c = INTERIOR[rng.next(len(INTERIOR))]
        blob = {c}
        for _ in range(rng.next(grow)):
            b = sorted(blob)[rng.next(len(blob))]
            t = add(b, DIRS[rng.next(6)])
            if t in INTERIOR_SET:
                blob.add(t)
        for s in blob:
            n[s] = 1 - n[s]
    return n


def recorded_graph(n):
    recs = sorted(s for s in SITES if n[s] == 1)
    rs = set(recs)
    return recs, [(s, add(s, d)) for s in recs for d in DIRS[::2] if add(s, d) in rs]


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the gas in its unlike-bond form; the content-less gas is half filled at zeta = g^-3."""
    rng = Lcg(424242)
    consts = set()
    for _ in range(60):
        n = chessboard()
        for s in INTERIOR:
            n[s] = rng.next(2)
        rec_bonds = sum(1 for (s, t) in BOX_BONDS if n[s] == 1 and n[t] == 1)
        count = sum(n[s] for s in INTERIOR)
        shift = 2 if mut("unlike_form_forged") else 3
        consts.add(Fr(rec_bonds - shift * count) - Fr(unlike(n) - len(BOX_BONDS), 2))
    checks.check("B1", len(consts) == 1,
                 f"T1(a): on the framed 4^3 box (A-chessboard held outside, {len(BOX_BONDS)} bonds meeting the box), B - 3N - (#unlike - #bonds)/2 takes one value over 60 sampled arrangements, so at zeta = g^-3 H the law is H^N g^(#unlike/2) Q up to a constant (a bond is unlike when its two ends have the same occupancy)")
    side = 4
    torus = [(x, y, z) for x in range(side) for y in range(side) for z in range(side)]

    def tnb(s, d):
        return ((s[0] + d[0]) % side, (s[1] + d[1]) % side, (s[2] + d[2]) % side)
    tb = [(s, tnb(s, d)) for s in torus for d in DIRS[::2]]
    ok = True
    for _ in range(60):
        n = {s: rng.next(2) for s in torus}
        comp = {s: 1 - n[s] for s in torus}
        b_n = sum(1 for (s, t) in tb if n[s] and n[t])
        b_c = sum(1 for (s, t) in tb if comp[s] and comp[t])
        count = sum(n.values())
        ok = ok and b_c == 3 * len(torus) - 6 * count + b_n
    checks.check("B2", ok,
                 "T1(b): on the 4^3 torus the complement n -> 1 - n sends B to 3V - 6N + B (60 arrangements), so without contents the weight zeta^N g^B is complement-symmetric exactly at zeta = g^-3 and every even torus is exactly half filled there")


# ============================================================================================ family C
CUBE = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]


def cube_edges(vs):
    vv = set(vs)
    return [(a, b) for a in vs for b in vs if a < b and sum(abs(a[i] - b[i]) for i in range(3)) == 1 and a in vv]


def family_c(checks: Checks) -> None:
    """T2: what contents do - cycles and merges only."""
    triples = ((3, 1, 2), (5, 2, 4), (12, 1, 2), (9, 8, 8), (1, 3, 2))
    ok1 = True
    for p, q, r in triples:
        mm = m_matrix(p, q, r)
        tot = p + q + 4 * r
        l1, l2 = Fr(p - q, tot), Fr(p + q - 2 * r, tot)
        for (a, b), v in mm.items():
            dot = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
            ok1 = ok1 and v == 1 + 6 * l1 * Fr(dot, 2) + 6 * l2 * (Fr(dot * dot, 2) - Fr(1, 6))
        ok1 = ok1 and all(sum(mm[(a, b)] for b in CONTENTS) == 6 for a in CONTENTS)
        ok1 = ok1 and max(mm.values()) == Fr(6 * max(p, q, r), tot) and min(mm.values()) == Fr(6 * min(p, q, r), tot)
    ok2, forests, cyclic = True, 0, 0
    subsets = [list(c) for k in range(1, 7) for c in combinations(CUBE, k)]
    for p, q, r in ((3, 1, 2), (12, 1, 2)):
        mm = m_matrix(p, q, r)
        lam = max(mm.values())
        for vs in subsets:
            es = cube_edges(vs)
            qv = q_factor(vs, es, mm)
            cr = cycle_rank(vs, es)
            if cr == 0:
                ok2 = ok2 and qv == 1
                forests += 1
            else:
                ok2 = ok2 and qv <= lam ** cr
                cyclic += 1
    ok3 = True
    for p, q, r in ((3, 1, 2), (1, 3, 2)):
        mm = m_matrix(p, q, r)
        for vs in (list(c) for k in range(2, 6) for c in combinations(CUBE, k)):
            es = cube_edges(vs)
            for mask in range(1 << len(es)):
                sub_e = [e for i, e in enumerate(es) if mask >> i & 1]
                base = q_factor(vs, sub_e, mm)
                if mut("contents_sign_forged"):
                    base = 2 - base
                ok3 = ok3 and base >= 1
                for i, e in enumerate(es):
                    if not mask >> i & 1:
                        ok3 = ok3 and q_factor(vs, sub_e + [e], mm) >= base
    ok4 = True
    for p, q, r in ((3, 1, 2), (12, 1, 2)):
        mm = m_matrix(p, q, r)
        lam, low = max(mm.values()), min(mm.values())
        for vs in (list(c) for k in (3, 4, 5, 6) for c in combinations(CUBE, k)):
            es = cube_edges(vs)
            for u, v in combinations(vs, 2):
                if (u, v) in es or (v, u) in es:
                    continue
                merged = [(u if a == v else a, u if b == v else b) for (a, b) in es]
                qa, qb = q_factor(vs, es, mm), q_factor([w for w in vs if w != v], merged, mm, cap=8)
                deg_v = sum(1 for e in es if v in e)
                same = cycle_rank(vs, es + [(u, v)]) > cycle_rank(vs, es)
                ok4 = ok4 and (qb == qa if not same else qb / qa >= (low / lam) ** deg_v)
    checks.check("C1", ok1 and ok2,
                 f"T2(a): M = J + 6 lambda1 P1 + 6 lambda2 P2 with rows summing to 6, Lambda = max M = 6 max(p,q,r)/(p+q+4r), m = min M (five triples); on every set of at most 6 sites of the 2x2x2 cube at (3,1,2) and (12,1,2), Q = 1 on forests ({forests}) and Q <= Lambda^(cycle rank) otherwise ({cyclic})")
    checks.check("C2", ok3 and ok4,
                 "T2(b),(c): on p + q = 2r ((3,1,2) and (1,3,2)) every bond set on at most 5 cube sites has Q >= 1 and adding a bond never lowers Q; identifying two non-adjacent records multiplies Q by exactly 1 across components and by at least (m/Lambda)^deg within one (every pair, at most 6 sites, (3,1,2) and (12,1,2))")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the translation map."""
    rng = Lcg(20260925)
    maps, ok = 0, True
    sums_ok = True
    for _ in range(120):
        n = near_chessboard(rng, 4, 5)
        xs = [s for s in INTERIOR if sigma(n, s) == -1]
        if not xs:
            continue
        comp, vset = cluster_and_fill(n, xs[rng.next(len(xs))])
        wl = wall(vset)
        k = len(wl)
        ok = ok and all(sigma(n, v) == -1 for v in comp) and all(sigma(n, add(v, d)) == 1 for (v, d) in wl)
        runs_sum, front_sum = 0, 0
        for d in DIRS:
            m, back, front = translate(n, vset, d)
            maps += 1
            drop = unlike(n) - unlike(m)
            if mut("unlike_drop_forged"):
                drop += 1
            dn = sum(m[s] for s in SITES) - sum(n[s] for s in SITES)
            runs = sum(1 for v in vset if sub(v, d) not in vset)
            runs_sum += runs
            front_sum += sum(1 for (v, e) in wl if e == d)
            ok = ok and drop == k and dn == sum(1 for y in back if is_a(y)) - sum(1 for y in front if is_a(y)) and abs(dn) <= runs
            ok = ok and all(sigma(n, v) == -sigma(m, add(v, d)) for v in vset) and all(m[s] == (1 if is_a(s) else 0) for s in FRAME)
        sums_ok = sums_ok and runs_sum == k and front_sum == k
    checks.check("D1", ok and sums_ok,
                 f"T3(a): on near-chessboard arrangements of the framed 4^3 box ({maps} maps: 120 arrangements, six directions), every wall bond of V is unlike; the translation drops the unlike bonds by exactly |dV|; N' - N = #(back in A) - #(front in A), at most the runs of V along d; sigma = -sigma'(. + d) on V (injective at fixed (V, d)); the frame is untouched; the runs and the front sizes over the six directions each sum to |dV|")
    rng = Lcg(777)
    checked, nontrivial, ok2 = 0, 0, True
    for p, q, r in ((3, 1, 2), (12, 1, 2)):
        mm = m_matrix(p, q, r)
        lam, low = max(mm.values()), min(mm.values())
        for _ in range(150):
            n = near_chessboard(rng, 3, 6)
            xs = [s for s in INTERIOR if sigma(n, s) == -1]
            if not xs:
                continue
            comp, vset = cluster_and_fill(n, xs[rng.next(len(xs))])
            wl = wall(vset)
            k = len(wl)
            qn = q_factor(*recorded_graph(n), mm)
            if qn is None:
                continue
            occ = [(v, d) for (v, d) in wl if n[v] == 1 and n[add(v, d)] == 1]
            fronts = {d: sum(1 for (v, e) in wl if e == d) for d in DIRS}
            best = min(DIRS, key=lambda d: fronts[d])
            for d in DIRS:
                m, _, _ = translate(n, vset, d)
                qm = q_factor(*recorded_graph(m), mm)
                if qm is None:
                    continue
                f_occ = sum(1 for (v, e) in occ if e == d)
                ok2 = ok2 and qn / qm <= lam ** len(occ) * (lam / low) ** (5 * f_occ)
                if d == best:
                    ok2 = ok2 and (qn / qm) ** 6 <= lam ** (6 * k) * (lam / low) ** (5 * k)
                checked += 1
                nontrivial += qn != qm
    checks.check("D2", ok2 and nontrivial > 0,
                 f"T3(b): the content factor through the map obeys Q(n)/Q(n') <= Lambda^(|D|+|F|) (Lambda/m)^(5|F|), F the occupied wall bonds on the d-front ({checked} maps at (3,1,2) and (12,1,2), {nontrivial} with Q(n) != Q(n')); with d chosen from V alone to minimise its front, Q(n)/Q(n') <= Lambda^|dV| (Lambda/m)^(5|dV|/6), so w(n)/w(n') <= x^|dV| with x = g^(1/2) Lambda (Lambda/m)^(5/6) max(H, 1/H)^(1/6)")


# ============================================================================================ family E
def fixed_polycubes(nmax):
    """fixed polycubes up to nmax cells (enumeration in which each shape appears once, anchored at its least cell)."""
    out = {k: [] for k in range(1, nmax + 1)}
    origin = (0, 0, 0)

    def allowed(c):
        return c[2] > 0 or (c[2] == 0 and (c[1] > 0 or (c[1] == 0 and c[0] >= 0)))

    def rec(poly, untried, seen):
        untried = list(untried)
        while untried:
            c = untried.pop()
            poly.add(c)
            out[len(poly)].append(frozenset(poly))
            if len(poly) < nmax:
                new = []
                for d in DIRS:
                    y = add(c, d)
                    if allowed(y) and y not in seen:
                        new.append(y)
                        seen.add(y)
                rec(poly, untried + new, seen)
                for y in new:
                    seen.discard(y)
            poly.discard(c)
    rec(set(), [origin], {origin})
    return out


def wall_size(vset):
    return 6 * len(vset) - 2 * sum(1 for c in vset for d in DIRS[::2] if add(c, d) in vset)


def plaquettes(vset):
    out = []
    for c in vset:
        for d in DIRS:
            if add(c, d) not in vset:
                ax = [i for i in range(3) if d[i] != 0][0]
                o1, o2 = [i for i in range(3) if i != ax]
                centre = [2 * c[i] + d[i] for i in range(3)]
                verts = set()
                for sa in (-1, 1):
                    for sb in (-1, 1):
                        v = list(centre)
                        v[o1] += sa
                        v[o2] += sb
                        verts.add(tuple(v))
                out.append(frozenset(verts))
    return out


def connected_by(faces, shared):
    seen, stack = {0}, [0]
    while stack:
        i = stack.pop()
        for j in range(len(faces)):
            if j not in seen and len(faces[i] & faces[j]) >= shared:
                seen.add(j)
                stack.append(j)
    return len(seen) == len(faces)


def r_count(k):
    return 1 if k == 1 else Fr(32, k - 1) * comb(31 * k, k - 2)


X0 = Fr(3, 250)
U_PLUS = Fr(31, 1000)
SMALL_WALLS = {6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538}


def certificate():
    den = 1 - 31 * X0 * (1 + U_PLUS) ** 30
    r_prime = (1 + U_PLUS) ** 31 / den * (1 + 2 * U_PLUS)
    head = sum((Fr(k, 4) * r_count(k) * X0 ** k for k in range(1, 24)), Fr(0))
    small = sum((c * X0 ** k for k, c in SMALL_WALLS.items()), Fr(0))
    return den, small + X0 / 4 * r_prime - head


def family_e(checks: Checks) -> None:
    """T4: the walls, the tree bound and the sum; T5's numbers."""
    polys = fixed_polycubes(7)
    counts = [len(polys[k]) for k in range(1, 8)]
    around = {}
    for k in range(1, 7):
        for vset in polys[k]:
            around[wall_size(vset)] = around.get(wall_size(vset), 0) + k
    small = {w: c for w, c in around.items() if w <= 22}
    seven = min(wall_size(v) for v in polys[7])
    conn_v = conn_e = ray = True
    for k in range(1, 7):
        for vset in polys[k]:
            faces = plaquettes(vset)
            conn_v = conn_v and connected_by(faces, 1)
            conn_e = conn_e and connected_by(faces, 2)
            ks = wall_size(vset)
            for x in vset:
                mm = 0
                while add(x, (mm + 1, 0, 0)) in vset:
                    mm += 1
                ray = ray and 4 * (mm + 1) <= ks
    face0 = plaquettes({(0, 0, 0)})[0]
    near = {f for c in product(range(-2, 3), repeat=3) for f in plaquettes({c})}
    deg_v = sum(1 for f in near if f != face0 and len(f & face0) >= 1)
    deg_e = sum(1 for f in near if f != face0 and len(f & face0) >= 2)
    want = SMALL_WALLS if not mut("wall_count_forged") else {**SMALL_WALLS, 22: 2539}
    checks.check("E1", counts == [1, 3, 15, 86, 534, 3481, 23502] and small == want and seven == 24 and conn_v and conn_e and ray and (deg_v, deg_e) == (32, 12),
                 f"T4(a): fixed polycubes of 1 to 7 cells number {counts}; the regions V around a site with |dV| <= 22 number {dict(sorted(small.items()))}, and seven cells already need |dV| >= 24; every wall of at most six cells is connected through shared vertices and through shared edges; the e1 ray from x leaves V within |dV|/4 sites; a plaquette meets {deg_v} others at a vertex and {deg_e} along an edge")
    n_ser = 14
    uu = [0] * (n_ser + 1)
    for _ in range(n_ser + 1):
        base = [1] + uu[1:]
        pw = [1] + [0] * n_ser
        for _ in range(31):
            new = [0] * (n_ser + 1)
            for i, a in enumerate(pw):
                if a:
                    for j, b in enumerate(base):
                        if i + j > n_ser:
                            break
                        new[i + j] += a * b
            pw = new
        uu = [0] + pw[:n_ser]
    uu2 = [sum(uu[i] * uu[k - i] for i in range(k + 1)) for k in range(n_ser + 1)]
    series_ok = all(uu[k] + uu2[k] == r_count(k) for k in range(1, n_ser))
    den, total = certificate()
    ok_fixed = X0 < Fr(30 ** 30, 31 ** 31) and X0 * (1 + U_PLUS) ** 31 <= U_PLUS and den > 0
    checks.check("E2", series_ok and ok_fixed and total <= Fr(897, 10000) and 1 - 2 * total >= Fr(82, 100),
                 f"T4(b): r_k = (32/(k-1)) C(31k, k-2) is the k-th coefficient of U + U^2, U = x(1+U)^31 (exact to k = 13); at x0 = 3/250 < 30^30/31^31, U(x0) <= 31/1000; so the sum over V around a site of x0^|dV| is at most {dec(total, 5)} (exact small counts to |dV| = 22, the tree bound (k/4) r_k beyond), and 1 - 2 x that >= 82/100")
    rows, ok3 = [], True
    for (p, q, r), gstar in (((1, 1, 1), Fr(9, 62500)), ((3, 1, 2), Fr(1, 10 ** 5)), ((5, 2, 4), Fr(18, 10 ** 6)), ((12, 1, 2), Fr(19, 10 ** 8)), ((9, 8, 8), Fr(97, 10 ** 6))):
        mm = m_matrix(p, q, r)
        lam, low = max(mm.values()), min(mm.values())
        ok3 = ok3 and gstar ** 3 * lam ** 6 * (lam / low) ** 5 <= X0 ** 6
        rows.append(f"({p},{q},{r}): g <= {gstar}")
    checks.check("E3", ok3,
                 "T5: at zeta = g^-3 (H = 1) the certificate x <= 3/250 holds, i.e. g^3 Lambda^6 (Lambda/m)^5 <= (3/250)^6, at: " + "; ".join(rows) + " (no contents: p = q = r, M = 1)")


# ============================================================================================ family F
FENCES = (
    "This note works within block 81's record gas, as landed on main; it reports that the gas makes the chessboard of block 79 when a recorded bond is expensive, with explicit bond scales, and what contents do to that; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Peierls", "Dobrushin", "Klarner", "Mayer", "Vietoris", "Lebowitz", "Gallavotti", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - M's decomposition at five triples; Q on every subgraph of at most 6 sites of the 2x2x2 cube (forests, cycle bound, monotone on p + q = 2r, merges)",
    "per_site: executed - the unlike-bond identity on 60 framed arrangements of the 4^3 box; complement symmetry on 60 arrangements of the 4^3 torus",
    "per_mode: executed - the translation map on 720 maps (unlike drop, record count, injectivity, frame) and the content bound on 1728 maps at two triples",
    "per_block: executed - fixed polycubes to 7 cells, wall counts to |dV| = 22, wall connectedness and the ray for every region of at most six cells; the certificate at x0 = 3/250 in exact rationals",
    "lattice_wide: every framed box and every even torus; T4(b) and T5 with the imported connectedness of walls; the gas, its bond scale, activity and contents are supplied; half filling with contents and the walk's gap on the gas's arrangements are not re-run or treated",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: block 81's record gas makes the chessboard when a recorded bond is expensive - at zeta = g^-3 the framed states differ at every site by at least 0.82 in sigma for g <= 9/62500 without contents and g <= 1/100000 at (3,1,2); contents act on cycles and merges only; wall connectedness imported; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
