#!/usr/bin/env python3
"""Exact checks: the Markov graph of the three-dimensional monotone formation law, the eight corner laws, the sweep's imprint.

Scope.  The six Bloch-axis menu with the covariant positive product rule (p, q, r), the records-only reading, the monotone
class with corner kappa in {+1,-1}^3, in block 08's region.  R1: the full conditional at a site depends on the twelve
sites of the graph G_kappa (six axial, six face-diagonal x + kappa_i e_i - kappa_j e_j) and genuinely on the face-diagonal
ones (exact witness).  R2: the third difference of log K_3 is nonzero at the declared nonconstant triples (the hypothesis
under which the law is not nearest-neighbor Markov and not a static law).  R3: the eight corners' dependency sets pair
up under the point reflection, the triple groupings are all distinct, and within a pair the conditionals differ (exact
witness); the 24 proper rotations act transitively on the corners.  R4: on the 2x2 column the two-plane joint law of the
stationary plane chain is not its transpose (exact total variation; zero at the constant rule), the one-plane law is not
invariant under the in-plane reflection, and the eight predecessor structures give four one-plane laws.  Exact rational
arithmetic only; the runner scans its own source for floating-point literals.  No order or corner is selected as physical;
no arrow of time is derived.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_MARKOV_GRAPH_EIGHT_CORNER_LAWS_SWEEP_IMPRINT_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK08_PATH = ROOT / AUDIT_INPUT_PATHS[2]
BLOCK02_PATH = ROOT / AUDIT_INPUT_PATHS[3]
PLANE_PATH = ROOT / AUDIT_INPUT_PATHS[4]
CLAIM_ID = "admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15"
BLOCK08_CLAIM_ID = "admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15"
BLOCK08_FRAGMENT = "the three-body normalizer is irreducible"
BLOCK02_CLAIM_ID = "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06"
PLANE_CLAIM_ID = "admissibility_plane_formation_diagonal_interaction_note_2026-09-08"
PLANE_FRAGMENT = "the two diagonal classes differ for every nonconstant orbit triple"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "No possibility is privileged.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "diagonal_dependence_denied": "B",
    "excluded_site_dependence_claimed": "B",
    "third_difference_forged": "B",
    "dependency_sets_all_distinct_claimed": "C",
    "groupings_coincide_claimed": "C",
    "pair_witness_denied": "C",
    "rotation_orbit_wrong": "C",
    "joint_law_symmetric_claimed": "D",
    "constant_rule_irreversible_claimed": "D",
    "inplane_reflection_invariance_claimed": "D",
    "one_plane_law_count_wrong": "D",
    "column_laws_not_distinct_claimed": "D",
    "claim_physical_order": "F",
    "claim_arrow_of_time": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


F = Fraction


def dec(x: Fraction, n: int = 8) -> str:
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


# ------------------------------------------------------------------ the rule and kernels (self-contained)
AXES = ("+x", "-x", "+y", "-y", "+z", "-z")
M = 6


def orbit_type(s: int, t: int) -> str:
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


class Rule:
    def __init__(self, tr) -> None:
        p, q, r = tr
        w = {"p": p, "q": q, "r": r}
        self.tr = tr
        self.phi = [[w[orbit_type(s, t)] for t in range(M)] for s in range(M)]
        self.Z1 = sum(self.phi[0])
        self.K = [[F(self.phi[s][a], self.Z1) for s in range(M)] for a in range(M)]
        self.Z2 = {(a, b): sum(self.phi[s][a] * self.phi[s][b] for s in range(M)) for a in range(M) for b in range(M)}
        self.Z3 = {(a, b, c): sum(self.phi[s][a] * self.phi[s][b] * self.phi[s][c] for s in range(M))
                   for a in range(M) for b in range(M) for c in range(M)}
        self.K2 = {k: F(v, self.Z1 ** 2) for k, v in self.Z2.items()}
        self.K3 = {k: F(v, self.Z1 ** 3) for k, v in self.Z3.items()}
        self._cond: dict = {}

    def cond(self, rec: tuple) -> list:
        if rec in self._cond:
            return self._cond[rec]
        k = len(rec)
        if k == 0:
            out = [F(1, M)] * M
        elif k == 1:
            out = [self.K[rec[0]][s] for s in range(M)]
        elif k == 2:
            out = [F(self.phi[s][rec[0]] * self.phi[s][rec[1]], self.Z2[rec]) for s in range(M)]
        else:
            out = [F(self.phi[s][rec[0]] * self.phi[s][rec[1]] * self.phi[s][rec[2]], self.Z3[rec]) for s in range(M)]
        self._cond[rec] = out
        return out


def tv(u, v) -> Fraction:
    return sum(abs(x - y) for x, y in zip(u, v)) / 2


# ------------------------------------------------------------------ the full conditional of a corner class
CORNERS = tuple(product((1, -1), repeat=3))
PAIR_KEYS = tuple((i, j) for i in range(3) for j in range(3) if i != j)  # offset x + kappa_i e_i - kappa_j e_j


def grouping(kappa):
    """The three triples containing x, as pairs of offset keys (i, j) with common first index i."""
    return tuple(tuple(sorted((i, j) for j in range(3) if j != i)) for i in range(3))


def dep_offsets(kappa):
    out = set()
    for (i, j) in PAIR_KEYS:
        off = [0, 0, 0]
        off[i] += kappa[i]
        off[j] -= kappa[j]
        out.add(tuple(off))
    return frozenset(out)


def grouping_offsets(kappa):
    groups = []
    for i in range(3):
        g = []
        for j in range(3):
            if j == i:
                continue
            off = [0, 0, 0]
            off[i] += kappa[i]
            off[j] -= kappa[j]
            g.append(tuple(off))
        groups.append(tuple(sorted(g)))
    return tuple(sorted(groups))


def full_conditional(rule: Rule, kappa, axial: list, diag: dict) -> list:
    """gamma^kappa_x(s | omega) for axial values (list of six) and diagonal values diag[(i, j)] at x + kappa_i e_i - kappa_j e_j.
    The kernel groups the diagonal sites by the first index of the offset: the triple of y = x + kappa_i e_i."""
    ws = []
    for s in range(M):
        w = F(1)
        for a in axial:
            w *= rule.K[a][s]
        for i in range(3):
            js = [j for j in range(3) if j != i]
            w /= rule.K3[(s, diag[(i, js[0])], diag[(i, js[1])])]
        ws.append(w)
    Z = sum(ws)
    return [x / Z for x in ws]


def full_conditional_by_offset(rule: Rule, kappa, axial: list, values_at_offset: dict) -> list:
    """The same kernel, but the diagonal values are given per lattice offset (so that two corners sharing the
    dependency set can be compared on the same configuration)."""
    diag = {}
    for (i, j) in PAIR_KEYS:
        off = [0, 0, 0]
        off[i] += kappa[i]
        off[j] -= kappa[j]
        diag[(i, j)] = values_at_offset[tuple(off)]
    return full_conditional(rule, kappa, axial, diag)


# ------------------------------------------------------------------ the 2x2 column (block 08's machinery, self-contained)
def plane_transfer_class(rule: Rule, signs, w, v) -> Fraction:
    s2, s3 = signs[1], signs[2]
    idx = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
    pr = F(1)
    for (a, b), k in idx.items():
        rec = [w[k]]
        p2 = (a - s2, b)
        p3 = (a, b - s3)
        if p2 in idx:
            rec.append(v[idx[p2]])
        if p3 in idx:
            rec.append(v[idx[p3]])
        pr *= rule.cond(tuple(rec))[v[k]]
    return pr


def group48():
    axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    idx = {a: i for i, a in enumerate(axes)}
    elems = set()
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            mp = []
            for a in axes:
                b = [0, 0, 0]
                for i in range(3):
                    b[perm[i]] = signs[i] * a[i]
                mp.append(idx[tuple(b)])
            elems.add(tuple(mp))
    return sorted(elems)


def solve_stationary(Q):
    n = len(Q)
    A = [[Q[j][i] - (F(1) if i == j else F(0)) for j in range(n)] for i in range(n)]
    A[n - 1] = [F(1)] * n
    b = [F(0)] * (n - 1) + [F(1)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        b[col], b[piv] = b[piv], b[col]
        inv = 1 / A[col][col]
        A[col] = [x * inv for x in A[col]]
        b[col] *= inv
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
                b[r] -= f * b[col]
    return b


def stationary_plane_law(rule: Rule, signs):
    """Exact stationary law of the 2x2 plane transfer of the class with signs (s1 irrelevant), by orbit reduction under
    the internal group of order 48."""
    states = list(product(range(M), repeat=4))
    G = group48()
    orbit_of, reps = {}, []
    for s in states:
        if s in orbit_of:
            continue
        o = len(reps)
        reps.append(s)
        orbit_of[s] = o
        for g in G:
            orbit_of[tuple(g[x] for x in s)] = o
    sizes = [0] * len(reps)
    for s in states:
        sizes[orbit_of[s]] += 1
    n = len(reps)
    Q = [[F(0)] * n for _ in range(n)]
    for o, w in enumerate(reps):
        for v in states:
            Q[o][orbit_of[v]] += plane_transfer_class(rule, signs, w, v)
    pi_orb = solve_stationary(Q)
    assert all(x > 0 for x in pi_orb) and sum(pi_orb) == 1
    return states, {s: pi_orb[orbit_of[s]] / sizes[orbit_of[s]] for s in states}


def irreversibility(rule: Rule, signs, states, pi) -> Fraction:
    """TV(J, J^T) with J(w, v) = pi(w) P(w, v): half the sum over ordered pairs of |J(w,v) - J(v,w)|."""
    total = F(0)
    for w in states:
        pw = pi[w]
        for v in states:
            if v <= w:
                continue
            total += abs(pw * plane_transfer_class(rule, signs, w, v) - pi[v] * plane_transfer_class(rule, signs, v, w))
    return total  # unordered pairs counted once = ordered-pair sum / 2


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b08: str, b02: str, plane: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 5,
                 "the five declared inputs exist (this note, the axiom memo, block 08, block 02, the plane-law note)")
    flat_ax = normalize_text(axiom_text)
    checks.check("A2", all(n in flat_ax for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    f08, f02, fpl = normalize_text(b08).lower(), normalize_text(b02).lower(), normalize_text(plane).lower()
    checks.check("A3", BLOCK08_CLAIM_ID in f08 and BLOCK08_FRAGMENT in f08 and BLOCK02_CLAIM_ID in f02 and PLANE_CLAIM_ID in fpl and PLANE_FRAGMENT in fpl,
                 "the parents' claim ids and the cited fragments (block 08's three-body term; the plane-law note's two classes) are present")
    flat = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
DEP_WITNESS_312 = F(793975879125, 24719290847393)


def family_b(checks: Checks, report: dict) -> None:
    rule = Rule((3, 1, 2))
    kappa = (1, 1, 1)
    axial = [0] * 6
    base = {k: 0 for k in PAIR_KEYS}
    c0 = full_conditional(rule, kappa, axial, base)
    best = F(0)
    for v12 in range(M):
        d = dict(base)
        d[(0, 1)] = v12
        best = max(best, tv(c0, full_conditional(rule, kappa, axial, d)))
    if mut("diagonal_dependence_denied"):
        best = F(0)
    checks.check("B1", best == DEP_WITNESS_312 and best > 0,
                 f"R1: at (3,1,2) with all twelve sites at +x, changing the face-diagonal site x+e1-e2 moves the full conditional by TV {best} = {dec(best)} (maximum over its six values)")
    # B2: the kernel formula involves exactly the twelve sites: the six axial and the six offsets kappa_i e_i - kappa_j e_j; the
    # offsets e_i + e_j and -e_i - e_j do not occur (structural: dep_offsets has six elements, none of that form)
    offs = dep_offsets(kappa)
    plus = {(1, 1, 0), (1, 0, 1), (0, 1, 1), (-1, -1, 0), (-1, 0, -1), (0, -1, -1)}
    structural = len(offs) == 6 and not (offs & plus) and all(sum(abs(c) for c in o) == 2 and sum(o) == 0 for o in offs)
    if mut("excluded_site_dependence_claimed"):
        structural = not structural
    checks.check("B2", structural, "R1: the dependency set of x is six face-diagonal offsets of the form kappa_i e_i - kappa_j e_j (coordinate sum zero); the offsets e_i + e_j and -e_i - e_j are not among them")
    ratios = {}
    for tr in ((3, 1, 2), (5, 2, 4), (2, 2, 2)):
        r3 = Rule(tr).K3
        x, y, z = 0, 2, 4
        num = r3[(x, x, x)] * r3[(y, y, x)] * r3[(y, x, z)] * r3[(x, y, z)]
        den = r3[(y, x, x)] * r3[(x, y, x)] * r3[(x, x, z)] * r3[(y, y, z)]
        ratios[tr] = num / den
    if mut("third_difference_forged"):
        ratios[(5, 2, 4)] = F(1)
    checks.check("B3", ratios[(3, 1, 2)] == F(2160, 2197) and ratios[(5, 2, 4)] == F(686196, 704969) and ratios[(2, 2, 2)] == 1,
                 f"R2's hypothesis: the third-difference ratio of K_3 is {ratios[(3, 1, 2)]} at (3,1,2), {ratios[(5, 2, 4)]} at (5,2,4), 1 at the constant rule")
    # B4: the dependence on the diagonal site vanishes at the constant rule (the kernel is uniform)
    rc = Rule((2, 2, 2))
    c0 = full_conditional(rc, kappa, axial, base)
    d = dict(base)
    d[(0, 1)] = 1
    checks.check("B4", tv(c0, full_conditional(rc, kappa, axial, d)) == 0 and all(x == F(1, 6) for x in c0),
                 "control: at the constant rule the full conditional is uniform and does not depend on any site")


# ============================================================================================ family C
PAIR_WITNESS_312 = F(1646222697, 263752139417)


def family_c(checks: Checks, report: dict) -> None:
    sets = {k: dep_offsets(k) for k in CORNERS}
    groups = {k: grouping_offsets(k) for k in CORNERS}
    pairs_ok = all((sets[k] == sets[k2]) == (k2 == k or k2 == tuple(-c for c in k)) for k in CORNERS for k2 in CORNERS)
    if mut("dependency_sets_all_distinct_claimed"):
        pairs_ok = len(set(sets.values())) == 8
    checks.check("C1", pairs_ok and len(set(sets.values())) == 4, "R3a: the eight corners' dependency sets coincide exactly for point-reflection pairs (four distinct sets)")
    groups_ok = len(set(groups.values())) == 8
    if mut("groupings_coincide_claimed"):
        groups_ok = len(set(groups.values())) == 4
    checks.check("C2", groups_ok, "R3a: the eight triple groupings of the dependency set are pairwise distinct")
    rule = Rule((3, 1, 2))
    axial = [0] * 6
    offsets = sorted(sets[(1, 1, 1)])
    best = F(0)
    best_cfg = None
    for vals in product(range(M), repeat=6):
        va = dict(zip(offsets, vals))
        d = tv(full_conditional_by_offset(rule, (1, 1, 1), axial, va), full_conditional_by_offset(rule, (-1, -1, -1), axial, va))
        if d > best:
            best, best_cfg = d, vals
    if mut("pair_witness_denied"):
        best = F(0)
    checks.check("C3", best == PAIR_WITNESS_312 and best > 0,
                 f"R3b: at (3,1,2) the (+++) and (---) full conditionals differ on the same twelve-site configuration by TV {best} = {dec(best)} (maximum over the 6^6 diagonal assignments, axial values +x)")
    # C4: the 24 proper rotations act transitively on the 8 corners (signed permutations with determinant +1)
    rots = []
    for perm in permutations(range(3)):
        sign_perm = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if perm[i] > perm[j]:
                    sign_perm = -sign_perm
        for signs in product((1, -1), repeat=3):
            det = sign_perm * signs[0] * signs[1] * signs[2]
            if det == 1:
                rots.append((perm, signs))
    def act(rot, kappa):
        perm, signs = rot
        out = [0, 0, 0]
        for i in range(3):
            out[perm[i]] = signs[i] * kappa[i]
        return tuple(out)
    orbit = {act(r, (1, 1, 1)) for r in rots}
    stab = [r for r in rots if act(r, (1, 1, 1)) == (1, 1, 1)]
    n_rots = len(rots) + (1 if mut("rotation_orbit_wrong") else 0)
    checks.check("C4", n_rots == 24 and orbit == set(CORNERS) and len(stab) == 3,
                 f"R3c: the {len(rots)} proper rotations act transitively on the eight corners; the stabilizer of a corner has order {len(stab)} (the rotations about its body diagonal)")


# ============================================================================================ family D
IRR_312 = F(20050159445052753287345872554551877965270917971807795389873, 406357621088602935950245331407424044758618443589923499955200)
R2TV_312 = F(11555202353859801661076434687858214316334786981223, 530762821621220762616238380264013135814921940979920)


def family_d(checks: Checks, report: dict, exact: bool) -> None:
    irr = {}
    r2tv = {}
    laws = {}
    for tr in ((3, 1, 2), (5, 2, 4), (2, 2, 2)):
        rule = Rule(tr)
        states, pi = stationary_plane_law(rule, (1, 1, 1))
        irr[tr] = irreversibility(rule, (1, 1, 1), states, pi)
        r2tv[tr] = sum(abs(pi[v] - pi[(v[2], v[3], v[0], v[1])]) for v in states) / 2
        if tr == (3, 1, 2):
            for signs in CORNERS:
                laws[signs] = stationary_plane_law(rule, signs)[1]
    report["irr"] = irr
    sym_claim = (irr[(3, 1, 2)] == 0) if mut("joint_law_symmetric_claimed") else (irr[(3, 1, 2)] > 0 and irr[(5, 2, 4)] > 0)
    checks.check("D1", sym_claim and irr[(3, 1, 2)] == IRR_312,
                 f"R4b: on the 2x2 column TV(J, J^T) = {dec(irr[(3, 1, 2)])} at (3,1,2) and {dec(irr[(5, 2, 4)])} at (5,2,4): the plane chain is not reversible (exact literals under --exact)")
    const_ok = irr[(2, 2, 2)] == 0 and r2tv[(2, 2, 2)] == 0
    if mut("constant_rule_irreversible_claimed"):
        const_ok = irr[(2, 2, 2)] > 0
    checks.check("D2", const_ok, "control: at the constant rule the joint law is symmetric and the one-plane law is reflection-invariant")
    refl_ok = r2tv[(3, 1, 2)] > 0 and r2tv[(3, 1, 2)] == R2TV_312
    if mut("inplane_reflection_invariance_claimed"):
        refl_ok = r2tv[(3, 1, 2)] == 0
    checks.check("D3", refl_ok, f"R4b: TV(pi, pi∘R_2) = {dec(r2tv[(3, 1, 2)])} at (3,1,2): the in-plane reflection of the corner changes the one-plane law")
    distinct = []
    for k in CORNERS:
        if not any(laws[k] == laws[d] for d in distinct):
            distinct.append(k)
    pairing = all(laws[k] == laws[(-k[0], k[1], k[2])] for k in CORNERS)
    n_distinct = len(distinct) + (1 if mut("one_plane_law_count_wrong") else 0)
    checks.check("D4", n_distinct == 4 and pairing, f"R4b: the eight predecessor structures give {len(distinct)} distinct one-plane laws on the 2x2 column, paired by the sweep direction")
    # D5: the eight column laws are pairwise distinct: the four one-plane laws split by the joint law's asymmetry (irr > 0 for each in-plane structure)
    irr_all = {signs: irreversibility(Rule((3, 1, 2)), signs, list(product(range(M), repeat=4)), laws[signs]) for signs in distinct}
    col_ok = all(v > 0 for v in irr_all.values())
    if mut("column_laws_not_distinct_claimed"):
        col_ok = not col_ok
    checks.check("D5", col_ok, "R4b: for each of the four in-plane structures the joint law is asymmetric, so the eight column laws are pairwise distinct at (3,1,2)")
    if exact:
        print(f"exact TV(J, J^T) at (3,1,2) = {irr[(3, 1, 2)]}")
        print(f"exact TV(pi, pi∘R_2) at (3,1,2) = {r2tv[(3, 1, 2)]}")


# ============================================================================================ family F
FENCES = (
    "This note describes the monotone class with a corner on `Z^3` in block 08's region; it states nothing about the static law's uniqueness, nothing for `c ≥ 1/3`, nothing about a physical order or corner, and derives no arrow of time — the imprint of the sweep is that of a supplied order.",
    "No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "no value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "the physical order", "arrow of time is derived", "derives an arrow", "for every coupling", "selects the",
    "the static law of Z^3 is unique", "fires wake condition", "the Bridge weights", "the Bridge conjecture",
    "certified", "phase transition", "several static laws", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {
    "claim_physical_order": "The corner (+,+,+) is the physical order.",
    "claim_arrow_of_time": "Hence the arrow of time is derived from the axioms.",
}
CLASSICAL_NAMES = ("Dobrushin", "Lanford", "Ruelle", "Kolmogorov", "Perron", "Frobenius", "Pickard", "Hammersley", "Clifford", "Birkhoff")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    nsimp = "nsimp" + "lify("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln or nsimp in ln]
    checks.check("F3", not bad and len(scan) > 250, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.splitlines()[0].strip()
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem R2"):
            body = body + " (as Dobrushin showed)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the six values of the face-diagonal site for the dependence witness; the 6^6 diagonal assignments for the pair witness; the third-difference ratio at three triples",
    "per_site: executed — the twelve dependency sites of x and the excluded offsets; the eight corners' sets and groupings",
    "per_mode: executed — the 24 proper rotations on the eight corners and the stabilizer; the four one-plane laws of the 2x2 column",
    "per_block: executed — the 2x2 column's joint law against its transpose over all 1296^2 ordered pairs at three triples; the in-plane reflection of the one-plane law",
    "lattice_wide: proved from L1–L2 in block 08's region at triples with nonzero third difference; executed only at (3,1,2) and (5,2,4); nothing claimed elsewhere",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    exact = "--exact" in argv
    checks = Checks()
    texts = [(ROOT / p).read_text(encoding="utf-8") if (ROOT / p).is_file() else "" for p in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the Markov graph of the 3D monotone law (face-diagonal dependence witness), the eight corner laws (sets, groupings, pair witness, rotation orbit), the sweep's imprint on the 2x2 column (irreversibility, in-plane reflection, four one-plane laws); exact; no order selected")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts[0], texts[1], texts[2], texts[3], texts[4])
    family_b(checks, report)
    family_c(checks, report)
    family_d(checks, report, exact)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
