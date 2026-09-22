#!/usr/bin/env python3
"""Exact checks: the three-dimensional formation law of the monotone class.

Scope.  The six Bloch-axis menu with the covariant positive product rule of orbit weights (p, q, r), the records-only
reading, and the monotone class (every linear extension of the product order) on boxes of Z^3.  Q1: one law per box,
internal covariance, axis symmetry, down-set consistency, the product form with the three-body normalizer K_3 and its
irreducibility (third difference).  Q2: the first plane cannot be summed out -- reduced to the invariance of the 2D law
under the plane transfer, refuted exactly on the 2x2 cross-section at (3,1,2) and (5,2,4) (all 1296 states), with the
constant rule as the control; the 2D translate consistency re-executed on 2x3.  Q3: the plane transfer is a strictly
positive stochastic matrix; its orbit quotient (32 orbits) and exact stationary law; the coordinate-line pairs stay
K-pairs, the interior pair does not.  Q4: the one-neighbor sensitivities c_1, c_2, c_3 exactly at eight triples, the
region 3c < 1, the influence bound N c^d against the exact cube influence, the sector contraction against theta^n.
Exact rational arithmetic only (fractions and integers); the runner scans its own source for floating-point literals and
conversion calls.  No order or corner is selected as physical; nothing about the static law of Z^3.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK02_PATH = ROOT / AUDIT_INPUT_PATHS[2]
BLOCK05_PATH = ROOT / AUDIT_INPUT_PATHS[3]
CLAIM_ID = "admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15"
BLOCK02_CLAIM_ID = "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06"
BLOCK02_FRAGMENT = "the row sweep is exactly solvable"
BLOCK05_CLAIM_ID = "admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07"
BLOCK05_FRAGMENT = "every linear extension gives the same formation law"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "extensions_recorded_sets_wrong": "B",
    "pair_type_constancy_broken": "B",
    "axis_symmetry_broken": "B",
    "downset_marginal_forged": "B",
    "product_form_wrong": "B",
    "three_body_ratio_forged": "B",
    "transfer_invariance_claimed": "C",
    "transfer_tv_literal_off": "C",
    "constant_control_broken": "C",
    "sub_rectangle_consistency_broken": "C",
    "boundary_pair_claim_wrong": "C",
    "transfer_row_sums_off": "D",
    "orbit_count_wrong": "D",
    "stationary_solve_forged": "D",
    "coordinate_line_pair_wrong": "D",
    "stationary_tv_literal_off": "D",
    "sensitivity_literal_off": "E",
    "region_membership_flipped": "E",
    "influence_bound_reversed": "E",
    "rectangle_influence_bound_off": "E",
    "sector_contraction_forged": "E",
    "covariance_bound_denied": "E",
    "two_dimensional_region_off": "E",
    "claim_for_every_coupling": "F",
    "claim_physical_order": "F",
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
    """Exact decimal expansion of a nonnegative rational, truncated to n digits; integer arithmetic only."""
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


# ------------------------------------------------------------------ the menu, the rule, the kernels
AXES = ("+x", "-x", "+y", "-y", "+z", "-z")
M = 6
TRIPLES = ((3, 1, 2), (5, 2, 4), (7, 3, 5), (2, 1, 2), (3, 2, 2), (5, 4, 4), (11, 10, 10), (2, 2, 2))


def orbit_type(s: int, t: int) -> str:
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


class Rule:
    """phi (integers), Z_k tables (integers), K and the k-neighbor kernels (fractions)."""

    def __init__(self, tr) -> None:
        p, q, r = tr
        w = {"p": p, "q": q, "r": r}
        self.tr = tr
        self.phi = [[w[orbit_type(s, t)] for t in range(M)] for s in range(M)]
        self.Z1 = sum(self.phi[0])
        self.K = [[F(self.phi[s][a], self.Z1) for s in range(M)] for a in range(M)]  # K[a][s]
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


def sensitivities(rule: Rule) -> dict:
    out = {}
    for k in (1, 2, 3):
        best = F(0)
        for rec in product(range(M), repeat=k):
            base = rule.cond(rec)
            for i in range(k):
                for a2 in range(M):
                    if a2 == rec[i]:
                        continue
                    rec2 = list(rec)
                    rec2[i] = a2
                    d = tv(base, rule.cond(tuple(rec2)))
                    if d > best:
                        best = d
        out[k] = best
    return out


# ------------------------------------------------------------------ boxes, predecessor sets, laws
def box_sites(dims):
    return list(product(*[range(n) for n in dims]))


def preds(x):
    return [tuple(x[i] - (1 if j == i else 0) for i in range(len(x))) for j in range(len(x)) if x[j] > 0]


def linear_extensions(sites):
    remaining = set(sites)

    def rec(chosen):
        if not remaining:
            yield tuple(chosen)
            return
        for x in sorted(remaining):
            if all(p in chosen for p in preds(x)):
                remaining.remove(x)
                chosen.append(x)
                yield from rec(chosen)
                chosen.pop()
                remaining.add(x)
    return list(rec([]))


def law_by_conditionals(rule: Rule, sites, v: dict) -> Fraction:
    w = F(1)
    for x in sites:
        w *= rule.cond(tuple(v[y] for y in preds(x)))[v[x]]
    return w


def law_by_product_form(rule: Rule, sites, v: dict) -> Fraction:
    w = F(1, M)
    for x in sites:
        A = preds(x)
        for y in A:
            w *= rule.K[v[y]][v[x]]
        if len(A) == 2:
            w /= rule.K2[(v[A[0]], v[A[1]])]
        elif len(A) == 3:
            w /= rule.K3[(v[A[0]], v[A[1]], v[A[2]])]
    return w


def rectangle_law(rule: Rule, dims):
    """Dictionary law of the 2D monotone class on a rectangle (rows x cols)."""
    sites = box_sites(dims)
    law = {}
    for vals in product(range(M), repeat=len(sites)):
        v = dict(zip(sites, vals))
        law[vals] = law_by_conditionals(rule, sites, v)
    return sites, law


def cube_pass(rule: Rule):
    """One integer-weighted pass over the 6^8 configurations of the 2x2x2 box: one-site marginals, pair marginals, the
    marginal on the down-set x3 = 0, the conditional laws of v_111 given v_000, and a sample check of the product form."""
    sites = box_sites((2, 2, 2))
    idx = {s: i for i, s in enumerate(sites)}
    edges = [(idx[y], idx[x]) for x in sites for y in preds(x)]
    two = [(idx[x], idx[preds(x)[0]], idx[preds(x)[1]]) for x in sites if len(preds(x)) == 2]
    three = [(idx[x], idx[preds(x)[0]], idx[preds(x)[1]], idx[preds(x)[2]]) for x in sites if len(preds(x)) == 3]
    n_one = sum(1 for x in sites if len(preds(x)) == 1)  # one-predecessor sites carry the kernel phi/Z_1
    from math import lcm
    l2 = 1
    for v in rule.Z2.values():
        l2 = lcm(l2, v)
    l3 = 1
    for v in rule.Z3.values():
        l3 = lcm(l3, v)
    # every configuration's denominator 6 Z_1^{n_one} prod Z_2 prod Z_3 divides this common multiple
    L = M * rule.Z1 ** n_one * l2 ** len(two) * l3 ** len(three)
    phi = rule.phi
    Z2, Z3 = rule.Z2, rule.Z3
    one = [[0] * M for _ in sites]
    pair = {(i, j): [[0] * M for _ in range(M)] for i in range(8) for j in range(i + 1, 8)}
    ds_idx = [idx[(0, 0, 0)], idx[(0, 1, 0)], idx[(1, 0, 0)], idx[(1, 1, 0)]]  # (x1, x2) as (row, col): 00, 01, 10, 11
    ds = {}
    cond111 = [[0] * M for _ in range(M)]  # [s000][s111]
    i000, i111 = idx[(0, 0, 0)], idx[(1, 1, 1)]
    total = 0
    for v in product(range(M), repeat=8):
        num = 1
        for a, b in edges:
            num *= phi[v[b]][v[a]]
        den = M * rule.Z1 ** n_one
        for x, a, b in two:
            den *= Z2[(v[a], v[b])]
        for x, a, b, c in three:
            den *= Z3[(v[a], v[b], v[c])]
        W = num * (L // den)
        total += W
        for i in range(8):
            one[i][v[i]] += W
        for (i, j), tab in pair.items():
            tab[v[i]][v[j]] += W
        key = (v[ds_idx[0]], v[ds_idx[1]], v[ds_idx[2]], v[ds_idx[3]])
        ds[key] = ds.get(key, 0) + W
        cond111[v[i000]][v[i111]] += W
    assert total == L
    return dict(L=L, one=one, pair=pair, ds=ds, cond111=cond111, sites=sites, idx=idx)


# ------------------------------------------------------------------ the 2x2 plane transfer and its orbit quotient
PLANE_SITES = ((0, 0), (0, 1), (1, 0), (1, 1))  # (x2, x3)


def plane_transfer(rule: Rule, w, v) -> Fraction:
    """P(w -> v) on the 2x2 cross-section: v00 records w00; v01 records w01, v00; v10 records w10, v00; v11 records w11, v01, v10."""
    w00, w01, w10, w11 = w
    v00, v01, v10, v11 = v
    K, K2, K3 = rule.K, rule.K2, rule.K3
    return (K[w00][v00]
            * K[w01][v01] * K[v00][v01] / K2[(w01, v00)]
            * K[w10][v10] * K[v00][v10] / K2[(w10, v00)]
            * K[w11][v11] * K[v01][v11] * K[v10][v11] / K3[(w11, v01, v10)])


def mu_2x2(rule: Rule) -> dict:
    K, K2 = rule.K, rule.K2
    return {v: F(1, M) * K[v[0]][v[1]] * K[v[0]][v[2]] * K[v[1]][v[3]] * K[v[2]][v[3]] / K2[(v[1], v[2])]
            for v in product(range(M), repeat=4)}


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


def orbits_2x2():
    states = list(product(range(M), repeat=4))
    G = group48()
    orbit_of, reps = {}, []
    for s in states:
        if s in orbit_of:
            continue
        o = len(reps)
        reps.append(s)
        stack = [s]
        orbit_of[s] = o
        while stack:
            u = stack.pop()
            for g in G:
                gu = tuple(g[x] for x in u)
                for cand in (gu, (gu[0], gu[2], gu[1], gu[3])):
                    if cand not in orbit_of:
                        orbit_of[cand] = o
                        stack.append(cand)
    sizes = [0] * len(reps)
    for s in states:
        sizes[orbit_of[s]] += 1
    return states, orbit_of, reps, sizes


def solve_stationary(Q):
    """Exact stationary row vector of a stochastic matrix Q (fractions) by Gaussian elimination on (Q^T - I) with the
    normalization row; returns the vector."""
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


def pair_law(law: dict, i: int, j: int) -> dict:
    out = {}
    for v, w in law.items():
        out[(v[i], v[j])] = out.get((v[i], v[j]), F(0)) + w
    return out


def is_K_pair(rule: Rule, pl: dict) -> bool:
    return all(pl[(a, b)] == F(1, M) * rule.K[a][b] for a in range(M) for b in range(M))


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b02_text: str, b05_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, block 02, block 05)")
    flat_ax = normalize_text(axiom_text)
    checks.check("A2", all(n in flat_ax for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    f02, f05 = normalize_text(b02_text).lower(), normalize_text(b05_text).lower()
    checks.check("A3", BLOCK02_CLAIM_ID in f02 and BLOCK02_FRAGMENT in f02 and BLOCK05_CLAIM_ID in f05 and BLOCK05_FRAGMENT in f05,
                 "the parents' claim ids and the cited fragments (the row sweep; one law per linear extension) are present")
    flat = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")
    checks.check("A5", not any(t in p for p in AUDIT_INPUT_PATHS for t in ("UNIQUENESS_REGION", "TWO_SITE", "WIDTHS_4_5", "HERMITIAN_GAUSSIAN")),
                 "blocks 03, 04, 06, 07 are not inputs")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    rule = Rule((3, 1, 2))
    sites = box_sites((2, 2, 2))
    exts = linear_extensions(sites)
    families = set()
    for e in exts:
        pos = {s: t for t, s in enumerate(e)}
        fam = tuple(tuple(sorted(y for y in sites if sum(abs(a - b) for a, b in zip(x, y)) == 1 and pos[y] < pos[x])) for x in sites)
        families.add(fam)
    expected = tuple(tuple(sorted(preds(x))) for x in sites)
    n_ext = len(exts) + (1 if mut("extensions_recorded_sets_wrong") else 0)
    checks.check("B1", n_ext == 48 and len(families) == 1 and expected in families,
                 f"Q1a: the {len(exts)} linear extensions of the 2x2x2 product order share one recorded-set family, the predecessor sets")
    cp = cube_pass(rule)
    report["cube"] = cp
    L = cp["L"]
    uniform = all(x * M == L for row in cp["one"] for x in row)
    type_const = True
    for (i, j), tab in cp["pair"].items():
        by_type = {}
        for a in range(M):
            for b in range(M):
                by_type.setdefault(orbit_type(a, b), set()).add(tab[a][b])
        if mut("pair_type_constancy_broken"):
            by_type["r"].add(-1)
        type_const = type_const and all(len(s) == 1 for s in by_type.values())
    checks.check("B2", uniform and type_const, "Q1b: on the cube every one-site marginal is 1/6 and every pair marginal is constant on each of the three pair types (28 pairs x 36 entries)")
    idx = cp["idx"]
    axis_ok = True
    for perm in permutations(range(3)):
        for (i, j), tab in cp["pair"].items():
            x, y = sites[i], sites[j]
            px, py = tuple(x[k] for k in perm), tuple(y[k] for k in perm)
            a, b = idx[px], idx[py]
            tab2 = cp["pair"][(a, b)] if a < b else [[cp["pair"][(b, a)][s][t] for s in range(M)] for t in range(M)]
            if mut("axis_symmetry_broken") and perm == (1, 0, 2):
                tab2 = [[tab2[s][t] + 1 for t in range(M)] for s in range(M)]
            axis_ok = axis_ok and tab == tab2
    checks.check("B3", axis_ok, "Q1c: the cube's pair marginals are invariant under the six permutations of the axes")
    mu = mu_2x2(rule)
    ds_ok = all(F(cp["ds"].get(v, 0), L) == mu[v] for v in mu)
    if mut("downset_marginal_forged"):
        ds_ok = not ds_ok
    checks.check("B4", ds_ok, "Q1d: the cube law's marginal on the down-set x3 = 0 is the 2D 2x2 monotone law (all 1296 entries)")
    ok_pf = True
    for dims in ((1, 2, 2), (2, 2, 1)):
        ss = box_sites(dims)
        for vals in product(range(M), repeat=len(ss)):
            v = dict(zip(ss, vals))
            if law_by_conditionals(rule, ss, v) != law_by_product_form(rule, ss, v):
                ok_pf = False
                break
    seed = 20260915
    for _ in range(2000):
        seed = (1103515245 * seed + 12345) % 2 ** 31
        vals = [(seed >> (3 * k)) % M for k in range(8)]
        v = dict(zip(sites, vals))
        lhs, rhs = law_by_conditionals(rule, sites, v), law_by_product_form(rule, sites, v)
        if mut("product_form_wrong"):
            rhs *= 2
        if lhs != rhs:
            ok_pf = False
            break
    checks.check("B5", ok_pf, "Q1e: the product form (1/6) prod K / prod K_2 / prod K_3 equals the product of conditionals on all configurations of 1x2x2 and 2x2x1 and on 2000 sampled cube configurations")
    ratios = {}
    for tr in ((3, 1, 2), (5, 2, 4), (2, 2, 2)):
        r3 = Rule(tr).K3
        x, y, z = 0, 2, 4
        num = r3[(x, x, x)] * r3[(y, y, x)] * r3[(y, x, z)] * r3[(x, y, z)]
        den = r3[(y, x, x)] * r3[(x, y, x)] * r3[(x, x, z)] * r3[(y, y, z)]
        ratios[tr] = num / den
    if mut("three_body_ratio_forged"):
        ratios[(3, 1, 2)] = F(1)
    checks.check("B6", ratios[(3, 1, 2)] == F(2160, 2197) and ratios[(5, 2, 4)] == F(686196, 704969) and ratios[(2, 2, 2)] == 1,
                 f"Q1f: the third-difference ratio of K_3 is {ratios[(3, 1, 2)]} at (3,1,2) and {ratios[(5, 2, 4)]} at (5,2,4) (pair-additive would give 1); 1 at the constant rule")


# ============================================================================================ family C
TRANSFER_TV = {(3, 1, 2): F(356696849, 806187919680), (5, 2, 4): F(17075751317037722924, 75640257098415067067163)}


def family_c(checks: Checks, report: dict, exact: bool) -> None:
    states = list(product(range(M), repeat=4))
    results = {}
    for tr in ((3, 1, 2), (5, 2, 4), (2, 2, 2)):
        rule = Rule(tr)
        mu = mu_2x2(rule)
        nu = {v: F(0) for v in states}
        row_min, rows_ok = None, True
        for w in states:
            rs = F(0)
            mw = mu[w]
            for v in states:
                pv = plane_transfer(rule, w, v)
                rs += pv
                nu[v] += mw * pv
                if row_min is None or pv < row_min:
                    row_min = pv
            rows_ok = rows_ok and rs == 1
        diff = sum(1 for v in states if nu[v] != mu[v])
        tvd = sum(abs(nu[v] - mu[v]) for v in states) / 2
        results[tr] = dict(nu=nu, mu=mu, diff=diff, tv=tvd, row_min=row_min, rows_ok=rows_ok, rule=rule)
    report["transfer"] = results
    r312, r524, r222 = results[(3, 1, 2)], results[(5, 2, 4)], results[(2, 2, 2)]
    inv_claim = (r312["diff"] == 0) if mut("transfer_invariance_claimed") else (r312["diff"] == 1296 and r524["diff"] == 1296)
    checks.check("C1", inv_claim, f"Q2d: the 2x2 plane transfer moves the 2D law on {r312['diff']}/1296 states at (3,1,2) and {r524['diff']}/1296 at (5,2,4)")
    tv_ok = r312["tv"] == TRANSFER_TV[(3, 1, 2)] and r524["tv"] == TRANSFER_TV[(5, 2, 4)]
    if mut("transfer_tv_literal_off"):
        tv_ok = r312["tv"] == TRANSFER_TV[(3, 1, 2)] + F(1, 10 ** 12)
    checks.check("C2", tv_ok, f"Q2d: TV(mu P, mu) = {r312['tv']} = {dec(r312['tv'], 10)} at (3,1,2); {dec(r524['tv'], 10)} at (5,2,4) (exact literal under --exact)")
    const_ok = (r222["diff"] == 0 and r222["tv"] == 0)
    if mut("constant_control_broken"):
        const_ok = r222["diff"] > 0
    checks.check("C3", const_ok, "Q2d control: at the constant rule (2,2,2) the transfer leaves the (uniform) 2D law fixed on all 1296 states")
    rule = r312["rule"]
    sites23, law23 = rectangle_law(rule, (2, 3))
    sub_ok = True
    for sub in (((0, 0), (0, 1), (1, 0), (1, 1)), ((0, 1), (0, 2), (1, 1), (1, 2))):
        sub_idx = [sites23.index(s) for s in sub]
        marg = {}
        for v, w in law23.items():
            key = tuple(v[i] for i in sub_idx)
            marg[key] = marg.get(key, F(0)) + w
        mu = mu_2x2(rule)
        sub_ok = sub_ok and all(marg[v] == mu[v] for v in mu)
    row1 = [sites23.index((1, j)) for j in range(3)]
    marg = {}
    for v, w in law23.items():
        key = tuple(v[i] for i in row1)
        marg[key] = marg.get(key, F(0)) + w
    chain_ok = all(marg[(a, b, c)] == F(1, M) * rule.K[a][b] * rule.K[b][c] for a in range(M) for b in range(M) for c in range(M))
    if mut("sub_rectangle_consistency_broken"):
        chain_ok = not chain_ok
    checks.check("C4", sub_ok and chain_ok, "Q2b: the 2x3 law's marginals on both 2x2 sub-rectangles are the 2x2 law and its second row is the K-chain (translate consistency in two dimensions)")
    nu = r312["nu"]
    bnd = is_K_pair(rule, pair_law(nu, 0, 2)) and is_K_pair(rule, pair_law(nu, 0, 1))
    inner = is_K_pair(rule, pair_law(nu, 1, 3)) or is_K_pair(rule, pair_law(nu, 2, 3))
    anti = all(pair_law(nu, 1, 2)[(a, b)] == F(1, M) * rule.K2[(a, b)] for a in range(M) for b in range(M))
    uni = all(sum(w for v, w in nu.items() if v[i] == s) == F(1, M) for i in range(4) for s in range(M))
    if mut("boundary_pair_claim_wrong"):
        inner = True
    checks.check("C5", bnd and not inner and not anti and uni, "Q2d: after one transfer at (3,1,2) the coordinate-line pairs stay (1/6)K-pairs and the one-site marginals uniform, while the interior pairs are not (1/6)K-pairs and the anti-diagonal is not a (1/6)K^2-pair")
    if exact:
        print(f"exact TV(mu P, mu) at (5,2,4) = {r524['tv']}")


# ============================================================================================ family D
STATIONARY_TV_312 = F(53632625669348618474616527326865874982994562247, 117947293693604613914719640058669585736649320217760)


def family_d(checks: Checks, report: dict, exact: bool) -> None:
    res = report["transfer"][(3, 1, 2)]
    rule = res["rule"]
    rows_ok, row_min = res["rows_ok"], res["row_min"]
    if mut("transfer_row_sums_off"):
        rows_ok = False
    checks.check("D1", rows_ok and row_min > 0, f"Q3a: P on the 2x2 cross-section is stochastic (all 1296 rows sum to one) and strictly positive (minimal entry {row_min})")
    states, orbit_of, reps, sizes = orbits_2x2()
    n = len(reps)
    Q = [[F(0)] * n for _ in range(n)]
    for o, w in enumerate(reps):
        for v in states:
            Q[o][orbit_of[v]] += plane_transfer(rule, w, v)
    rep_ok = True
    for o in range(n):
        members = [s for s in states if orbit_of[s] == o]
        w = members[-1]
        row = [F(0)] * n
        for v in states:
            row[orbit_of[v]] += plane_transfer(rule, w, v)
        rep_ok = rep_ok and row == Q[o]
    n_rep = n + (1 if mut("orbit_count_wrong") else 0)
    checks.check("D2", n_rep == 32 and rep_ok and all(sum(r) == 1 for r in Q), f"Q3e: the internal group (48) with the plane transpose gives {n} orbits of the 1296 plane states; the quotient rows are representative-independent (last member of every orbit) and stochastic")
    pi_orb = solve_stationary(Q)
    if mut("stationary_solve_forged"):
        pi_orb = [F(1, n)] * n
    stat = all(sum(pi_orb[i] * Q[i][j] for i in range(n)) == pi_orb[j] for j in range(n))
    pos = all(x > 0 for x in pi_orb) and sum(pi_orb) == 1
    checks.check("D3", stat and pos, "Q3a/e: the exact stationary law of the quotient solves pi Q = pi, is positive and sums to one (unique by the strict positivity of P)")
    pi = {s: pi_orb[orbit_of[s]] / sizes[orbit_of[s]] for s in states}
    report["pi"] = pi
    line_ok = is_K_pair(rule, pair_law(pi, 0, 2)) and is_K_pair(rule, pair_law(pi, 0, 1))
    uni = all(sum(w for v, w in pi.items() if v[i] == s) == F(1, M) for i in range(4) for s in range(M))
    if mut("coordinate_line_pair_wrong"):
        line_ok = not line_ok
    checks.check("D4", line_ok and uni, "Q3c: under the stationary 2x2 plane law the two coordinate-line pairs are (1/6)K-pairs and the one-site marginals are uniform")
    mu = res["mu"]
    tvd = sum(abs(pi[v] - mu[v]) for v in states) / 2
    inner = pair_law(pi, 1, 3)
    inner_pp = inner[(0, 0)]
    tv_ok = tvd == STATIONARY_TV_312
    if mut("stationary_tv_literal_off"):
        tv_ok = tvd == STATIONARY_TV_312 + F(1, 10 ** 30)
    checks.check("D5", tv_ok and inner_pp != F(1, 24) and not is_K_pair(rule, inner),
                 f"Q3e: TV(pi_2, mu_2D) = {dec(tvd, 10)} at (3,1,2) (exact literal under --exact); the interior pair ((0,1),(1,1)) has P(+x,+x) = {dec(inner_pp, 10)} against (1/6)K(+x,+x) = {dec(F(1, 24), 10)}: not a K-pair")
    report["Q"] = Q
    if exact:
        print(f"exact TV(pi_2, mu_2D) = {tvd}")
        print("stationary orbit masses: " + " ".join(f"{sizes[o]}:{pi_orb[o]}" for o in range(n)))


# ============================================================================================ family E
SENS = {
    (3, 1, 2): (F(1, 6), F(30, 143), F(27, 110)),
    (5, 2, 4): (F(3, 23), F(65, 434), F(10650, 63407)),
    (7, 3, 5): (F(2, 15), F(910, 5609), F(5782, 30885)),
    (2, 1, 2): (F(1, 11), F(1, 10), F(1, 9)),
    (3, 2, 2): (F(1, 13), F(39, 406), F(234, 2077)),
    (5, 4, 4): (F(1, 25), F(25, 546), F(500, 9701)),
    (11, 10, 10): (F(1, 61), F(671, 38502), F(73810, 3994861)),
    (2, 2, 2): (F(0), F(0), F(0)),
}
CUBE_INFLUENCE_312 = F(273651254, 10658734515)


def family_e(checks: Checks, report: dict, exact: bool) -> None:
    computed = {tr: sensitivities(Rule(tr)) for tr in TRIPLES}
    lit_ok = all((computed[tr][1], computed[tr][2], computed[tr][3]) == SENS[tr] for tr in TRIPLES)
    if mut("sensitivity_literal_off"):
        lit_ok = computed[(3, 1, 2)][3] == SENS[(3, 1, 2)][2] + F(1, 1000)
    c = {tr: max(computed[tr].values()) for tr in TRIPLES}
    checks.check("E1", lit_ok, "Q4: c_1, c_2, c_3 at the eight triples equal the note's exact literals; " + "; ".join(f"{tr}: c={c[tr]}" for tr in TRIPLES[:3]))
    inside = {tr: 3 * c[tr] < 1 for tr in TRIPLES}
    region_ok = all(inside.values()) and 3 * c[(2, 1, 2)] == F(1, 3)
    if mut("region_membership_flipped"):
        region_ok = not inside[(3, 1, 2)]
    checks.check("E1b", region_ok, f"Q4 region: 3c < 1 at all eight triples (3c = 1/3 at (2,1,2)); at the silent triples 3c = {3 * c[(3, 1, 2)]}, {3 * c[(5, 2, 4)]}, {3 * c[(7, 3, 5)]}")
    cp = report["cube"]
    L = cp["L"]
    cond = cp["cond111"]
    best = F(0)
    for s in range(M):
        for s2 in range(s + 1, M):
            ls = [F(cond[s][t] * M, L) for t in range(M)]
            ls2 = [F(cond[s2][t] * M, L) for t in range(M)]
            best = max(best, tv(ls, ls2))
    bound = 6 * c[(3, 1, 2)] ** 3
    infl_ok = best == CUBE_INFLUENCE_312 and best <= bound
    if mut("influence_bound_reversed"):
        infl_ok = best >= bound
    checks.check("E2", infl_ok, f"Q4a: on the cube at (3,1,2) the exact influence of v_000 on v_111 is {best} = {dec(best)} <= N c^3 = 6 (27/110)^3 = {bound} = {dec(bound)}")
    rule = Rule((3, 1, 2))
    c2d = max(computed[(3, 1, 2)][1], computed[(3, 1, 2)][2])
    sites23, law23 = rectangle_law(rule, (2, 3))
    i00, i12 = sites23.index((0, 0)), sites23.index((1, 2))
    best2 = F(0)
    for s in range(M):
        for s2 in range(s + 1, M):
            ls = [F(0)] * M
            ls2 = [F(0)] * M
            for v, w in law23.items():
                if v[i00] == s:
                    ls[v[i12]] += w
                if v[i00] == s2:
                    ls2[v[i12]] += w
            best2 = max(best2, tv([x * M for x in ls], [x * M for x in ls2]))
    bound2 = 3 * c2d ** 3
    rect_ok = best2 <= bound2
    if mut("rectangle_influence_bound_off"):
        rect_ok = best2 <= bound2 / 10
    checks.check("E3", rect_ok, f"Q4a (two dimensions): on 2x3 at (3,1,2) the exact influence of v_00 on v_12 is {dec(best2)} <= N c^3 = 3 (30/143)^3 = {dec(bound2)}")
    Q = report["Q"]
    n = len(Q)
    theta = c[(3, 1, 2)] / (1 - 2 * c[(3, 1, 2)])
    Qn = [row[:] for row in Q]
    sector_ok = True
    labels = []
    for step in range(1, 7):
        d = max(sum(abs(Qn[o1][o] - Qn[o2][o]) for o in range(n)) / 2 for o1 in range(n) for o2 in range(n))
        th = theta ** step
        if mut("sector_contraction_forged"):
            d = th * 2
        sector_ok = sector_ok and d <= th
        labels.append(f"n={step}: {dec(d, 6)} <= {dec(th, 6)}")
        Qn = [[sum(Qn[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    checks.check("E5", sector_ok and theta == F(27, 56), "Q4c: the maximal TV between rows of the quotient's n-th power is below theta^n (theta = 27/56) for n = 1..6; " + "; ".join(labels[:3]))
    cov_ok = True
    worst = F(0)
    sites = cp["sites"]
    for (i, j), tab in cp["pair"].items():
        x, y = sites[i], sites[j]
        meet = tuple(min(a, b) for a, b in zip(x, y))
        rho = max(sum(a - m for a, m in zip(x, meet)), sum(b - m for b, m in zip(y, meet)))
        bnd = 4 * (3 * c[(3, 1, 2)]) ** (rho - 1)
        for a in range(M):
            for b in range(M):
                cov = F(tab[a][b], L) - F(1, 36)
                worst = max(worst, abs(cov))
                cov_ok = cov_ok and abs(cov) <= bnd
    if mut("covariance_bound_denied"):
        cov_ok = worst > 4
    checks.check("E6", cov_ok, f"Q4b: every axis-indicator covariance of every cube pair (largest {dec(worst)}) satisfies |Cov| <= 4 (3c)^(rho-1); the bound is not informative at cube distances and is recorded as such")
    two_d = 2 * c2d
    if mut("two_dimensional_region_off"):
        two_d = F(1)
    checks.check("E7", two_d == F(60, 143) and two_d < 1, f"Q4 (two dimensions): 2 max(c_1, c_2) = {two_d} < 1 at (3,1,2): the plane law's correlations decay exponentially there")
    if exact:
        for tr in TRIPLES:
            print(f"exact sensitivities {tr}: c1={computed[tr][1]} c2={computed[tr][2]} c3={computed[tr][3]}")


# ============================================================================================ family F
FENCES = (
    "This note describes the monotone class of formation orders on boxes, columns and `Z^3` for the declared rule; it states nothing about the static law of `Z^3` beyond citing block 03's region and the silent triples, nothing about any order or corner being physical, nothing for `c ≥ 1/3` beyond the finite-box bounds, and nothing about the distinctness of the eight corner laws on `Z^3`.",
    "No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "the probability theorems listed under Imports are mathematical inputs, not physical premises.",
)
FORBIDDEN = (
    "the physical order", "for every coupling", "unique on Z^3", "long-range order exists", "Coulomb phase",
    "the static law of Z^3 is", "selects the", "fires wake condition", "the Bridge weights", "the Bridge conjecture",
    "certified", "phase transition", "several static laws", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {
    "claim_for_every_coupling": "The decay holds for every coupling.",
    "claim_physical_order": "The monotone class is the physical order.",
}
CLASSICAL_NAMES = ("Doeblin", "Kolmogorov", "Krylov", "Bogolyubov", "Perron", "Frobenius", "Dobrushin", "Pickard", "Vasershtein", "Toom")
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
    checks.check("F3", not bad and len(scan) > 300, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.splitlines()[0].strip()
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem Q3"):
            body = body + " (this is the Doeblin bound)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — every one of the 1296 plane states under the 2x2 transfer at (3,1,2), (5,2,4) and the constant rule; every (s, s') for the cube influence; every axis-indicator pair on the cube; the third-difference ratio",
    "per_site: executed — the recorded set of every site of every one of the 48 extensions; the one-site marginals of every cube site and of every plane site under mu P and under pi_2",
    "per_mode: executed — the quotient's 32 orbits and its n-th powers for n = 1..6 against theta^n; the three sensitivities c_1, c_2, c_3 at eight triples over all one-entry changes",
    "per_block: executed — the 2x2 stationary plane law by orbit reduction; the 2x3 rectangle's sub-rectangle marginals and its second row; the cube's down-set marginal on x3 = 0; the 1x2x2 and 2x2x1 product forms",
    "lattice_wide: proved for c < 1/3 (Q4e), executed only through the region membership of eight triples; nothing for c >= 1/3 beyond the finite-box bounds; nothing about the static law of Z^3",
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
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8") if AXIOM_PATH.is_file() else ""
    b02_text = BLOCK02_PATH.read_text(encoding="utf-8") if BLOCK02_PATH.is_file() else ""
    b05_text = BLOCK05_PATH.read_text(encoding="utf-8") if BLOCK05_PATH.is_file() else ""
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the 3D monotone formation law — the box law and its three-body term; the first plane cannot be summed out (2x2 witness); the plane chain's exact stationary 2x2 law; the sensitivities, the region 3c < 1, the influence bound; exact; no order selected")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text, b02_text, b05_text)
    family_b(checks, report)
    family_c(checks, report, exact)
    family_d(checks, report, exact)
    family_e(checks, report, exact)
    family_f(checks, note_text)
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
