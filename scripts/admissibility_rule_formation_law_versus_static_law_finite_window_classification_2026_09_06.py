#!/usr/bin/env python3
"""Exact checks: the formation law of a nearest-neighbor rule versus its static law.

Finite scope only.  The menu is the six Bloch-axis projectors inside M_2(C);
the windows are the three-site path, the four-site path, the four-site star,
the four-cycle (one plaquette) and the open 2x2x2 cube; the rules are the
product class (P) at declared exact weight triples and the sum rule (S) at
declared exact couplings.  The static law is the joint law whose full
conditionals are the rule with every neighbor recorded; the formation law is
the chain of the rule's conditionals along a formation order under the
records-only reading.  Theorem B (classification): the two laws coincide for
an order exactly when every site forms with at most one recorded neighbor.
Nothing infinite-volume is computed or claimed; no rule, coupling, order or
reading is selected.  Exact integer, rational and symbolic arithmetic only:
the runner scans its own source and fails if a floating-point literal or a
floating-point conversion call appears.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
UPSTREAM_BINARY_NOTE = (
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
CLAIM_ID = (
    "admissibility_rule_formation_law_versus_static_law_finite_window_"
    "classification_bounded_theorem_note_2026-09-06"
)

# ---------------------------------------------------------------- mutations
MUTATION_GATE = {
    "menu_drop_projector": "B",
    "rotation_improper": "B",
    "orbit_census_wrong": "B",
    "psi_nonconstant_passes": "B",
    "edge_flip_not_in_group": "B",
    "positivity_zero_entry_passes": "B",
    "static_mu_wrong_edge_weight": "C",
    "static_conditional_uses_two_hops": "C",
    "exterior_factor_dropped": "C",
    "compat_rank_off_by_one": "C",
    "sum_rule_pretends_consistent": "C",
    "brook_cycle_sign_flip": "C",
    "single_edge_sum_rule_inconsistent": "C",
    "formation_identity_drop_Zk": "D",
    "formation_uses_all_neighbors": "D",
    "formation_equals_static_on_cycle": "D",
    "one_neighbor_normalizer_wrong": "D",
    "fj_factorization_wrong": "D",
    "fj_j4_wrong": "D",
    "plaquette_lemma_skips_order": "D",
    "single_site_variation_constant": "D",
    "distinct_law_count_wrong": "D",
    "p4_census_wrong": "D",
    "constant_rule_varies": "D",
    "weights_collapsed_to_constant": "D",
    "menu_witness_varies_on_menu": "D",
    "asymmetric_identity_holds": "D",
    "absence_blind_nonconstant_passes": "E",
    "absence_extension_solution_forged": "E",
    "order_mixture_equals_static": "E",
    "marginal_reading_is_fixed_rule": "E",
    "marginal_chain_rule_broken": "E",
    "psi_rank_deficient": "E",
    "z2_rank_one": "E",
    "claim_rule_selected": "F",
    "claim_born_derived": "F",
    "claim_gate_explained": "F",
    "claim_infinite_volume": "F",
    "claim_action_identified": "F",
    "claim_axiom_amended": "F",
    "claim_order_physical": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


# ------------------------------------------------------------------- checks
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


# --------------------------------------------------------------------- menu
# Menu order: P(+e_x), P(-e_x), P(+e_y), P(-e_y), P(+e_z), P(-e_z).
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
MENU_LABELS = ("P(+x)", "P(-x)", "P(+y)", "P(-y)", "P(+z)", "P(-z)")
PAR, ANTI, ORTH = 0, 1, 2
ORBIT_NAMES = ("par", "anti", "orth")


def vdot(a: int, b: int) -> int:
    return sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))


def orbit(a: int, b: int) -> int:
    d = vdot(a, b)
    return PAR if d == 1 else (ANTI if d == -1 else ORTH)


def phi_table(triple):
    return tuple(tuple(triple[orbit(a, b)] for b in range(M)) for a in range(M))


TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT_TRIPLE = (2, 2, 2)
REF = 0  # the reference value P(+e_x)

# ---------------------------------------------------------------- rotations
def permutation_sign(perm) -> int:
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inv % 2 else 1


def signed_permutations(proper: bool):
    out = []
    for perm in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            det = permutation_sign(perm) * signs[0] * signs[1] * signs[2]
            if (det == 1) == proper:
                out.append((perm, signs))
    return tuple(out)


ROTATIONS = signed_permutations(True)


def rotate_vector(rot, vec):
    perm, signs = rot
    out = [0, 0, 0]
    for i in range(3):
        out[perm[i]] = signs[i] * vec[i]
    return tuple(out)


def rotate_menu(rot, a: int) -> int:
    return MENU_VECTORS.index(rotate_vector(rot, MENU_VECTORS[a]))


def compose(r1, r2):
    """r1 after r2 as signed permutations."""
    p1, s1 = r1
    p2, s2 = r2
    perm = tuple(p1[p2[i]] for i in range(3))
    signs = tuple(s2[i] * s1[p2[i]] for i in range(3))
    return (perm, signs)


# ------------------------------------------------------------------ windows
def cube_edges():
    return tuple((a, b) for a in range(8) for b in range(a + 1, 8) if bin(a ^ b).count("1") == 1)


WINDOWS = {
    "path3": ((0, 1), (1, 2)),
    "P4": ((0, 1), (1, 2), (2, 3)),
    "star4": ((0, 1), (0, 2), (0, 3)),
    "cycle4": ((0, 1), (1, 2), (2, 3), (3, 0)),
    "cube8": cube_edges(),
}
SIZES = {"path3": 3, "P4": 4, "star4": 4, "cycle4": 4, "cube8": 8}
# cycle4 exterior: two exterior neighbors per site carrying P(+e_x) and P(-e_y)
CYCLE4_EXTERIOR = {x: (0, 3) for x in range(4)}
# cube8 exterior: the exterior neighbor along axis a carries P(+e_a)
CUBE8_EXTERIOR = {x: (0, 2, 4) for x in range(8)}


def neighbors(edges, n):
    N = {i: [] for i in range(n)}
    for i, j in edges:
        N[i].append(j)
        N[j].append(i)
    return {i: tuple(sorted(v)) for i, v in N.items()}


def static_weight(v, edges, phi, exterior=None):
    w = 1
    for i, j in edges:
        w *= phi[v[i]][v[j]]
    if exterior:
        for x, vals in exterior.items():
            for o in vals:
                w *= phi[v[x]][o]
    return w


def rule_numerators(s_values, recorded_values, phi):
    """Product-rule numerators Prod_y phi(s, eta_y) for each s (psi constant)."""
    out = []
    for s in s_values:
        t = 1
        for e in recorded_values:
            t *= phi[s][e]
        out.append(t)
    return out


def formation_law(edges, n, phi, order, all_neighbors=False, drop_Zk=False):
    """mu_sigma under the records-only reading; returns dict config -> Fraction."""
    N = neighbors(edges, n)
    law = {}
    for v in product(range(M), repeat=n):
        num = 1
        den = 1
        formed = set()
        for x in order:
            A = N[x] if all_neighbors else tuple(y for y in N[x] if y in formed)
            vals = tuple(v[y] for y in A)
            num *= rule_numerators((v[x],), vals, phi)[0]
            if not drop_Zk:
                den *= sum(rule_numerators(range(M), vals, phi))
            formed.add(x)
        law[v] = Fraction(num, den)
    return law


def normalizer_product(edges, n, phi, order, v):
    N = neighbors(edges, n)
    formed = set()
    tot = 1
    for x in order:
        vals = tuple(v[y] for y in N[x] if y in formed)
        tot *= sum(rule_numerators(range(M), vals, phi))
        formed.add(x)
    return tot


def max_recorded(edges, n, order, skip_previous=False):
    N = neighbors(edges, n)
    formed = []
    mx = 0
    for x in order:
        pool = formed[:-1] if skip_previous else formed
        c = sum(1 for y in N[x] if y in pool)
        mx = max(mx, c)
        formed.append(x)
    return mx


def bareiss_rank(rows, ncols):
    """Exact rank of an integer matrix by fraction-free elimination."""
    A = [list(r) for r in rows]
    m = len(A)
    rank = 0
    prev = 1
    for col in range(ncols):
        piv = None
        for i in range(rank, m):
            if A[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        pr = A[rank]
        pv = pr[col]
        for i in range(rank + 1, m):
            ri = A[i]
            f = ri[col]
            A[i] = [(pv * a - f * b) // prev for a, b in zip(ri, pr)]
        prev = pv
        rank += 1
        if rank == ncols:
            break
    return rank


def normalize_text(text: str) -> str:
    return " ".join(text.split())


# ==================================================================== family A
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "is determined by, and varies with, the nearest-neighbor conditions",
    "Records form.",
    "records are permanent",
    "Only records are readable.",
    "A site with no record cannot be read.",
)


def family_a(checks: Checks, note_text: str, axiom_text: str) -> None:
    checks.check(
        "A1",
        all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 2,
        "both declared audit inputs (the note and the axiom memo) exist as files",
    )
    flat = normalize_text(axiom_text)
    for k, needle in enumerate(AXIOM_NEEDLES, start=2):
        checks.check(
            f"A{k}",
            needle in flat,
            f"the axiom memo contains verbatim: {needle[:60]}",
        )
    checks.check("A8", CLAIM_ID in note_text, "the note carries its claim id")
    checks.check(
        "A9",
        (ROOT / UPSTREAM_BINARY_NOTE).is_file(),
        "the upstream binary static-half note exists (presence only, no content read)",
    )


# ==================================================================== family B
def sympy_projectors():
    one = sp.Integer(1)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    half = sp.Rational(1, 2)
    P = []
    for sig in (sx, sy, sz):
        P.append(half * (ident + sig) * one)
        P.append(half * (ident - sig) * one)
    return P, (sx, sy, sz), ident


def conj_map(U, P):
    return sp.simplify(U * P * U.H)


def nullity_of_equations(eq_rows, nunk) -> int:
    rank = bareiss_rank(eq_rows, nunk) if eq_rows else 0
    return nunk - rank


def family_b(checks: Checks) -> None:
    P, (sx, sy, sz), ident = sympy_projectors()
    checks.check(
        "B1",
        all(sp.simplify(p - p.H) == sp.zeros(2) and sp.simplify(p * p - p) == sp.zeros(2) and sp.simplify(p.trace()) == 1 for p in P),
        "the six Bloch-axis projectors are Hermitian, idempotent and of trace one (sympy exact)",
    )
    menu_b = list(range(M if not mut("menu_drop_projector") else M - 1))
    census = {}
    trace_by_orbit = {}
    for a in menu_b:
        for b in menu_b:
            tr = sp.simplify((P[a] * P[b]).trace())
            o = orbit(a, b)
            if mut("orbit_census_wrong") and o == ANTI:
                o = ORTH
            census[o] = census.get(o, 0) + 1
            trace_by_orbit.setdefault(o, set()).add(tr)
    checks.check(
        "B2",
        census == {PAR: 6, ANTI: 6, ORTH: 24}
        and trace_by_orbit == {PAR: {1}, ANTI: {0}, ORTH: {sp.Rational(1, 2)}},
        f"ordered pairs fall into three orbits labelled by Tr(PP') in (1, 0, 1/2): census {tuple(census.get(o, 0) for o in (PAR, ANTI, ORTH))}",
    )
    rots_b = signed_permutations(not mut("rotation_improper"))
    dets = {permutation_sign(pm) * s[0] * s[1] * s[2] for pm, s in rots_b}
    closed = all(compose(r1, r2) in rots_b for r1 in rots_b for r2 in rots_b)
    checks.check(
        "B3",
        len(rots_b) == 24 and len(set(rots_b)) == 24 and dets == {1} and closed,
        "the 24 signed axis permutations of determinant +1 form a closed set of order 24",
    )
    images = {a: {rotate_menu(r, a) for r in rots_b} for a in menu_b}
    checks.check(
        "B4",
        all({rotate_menu(r, a) for a in menu_b} == set(menu_b) for r in rots_b)
        and all(images[a] == set(range(M)) for a in menu_b),
        "every proper rotation permutes the menu and the action is transitive",
    )
    Uz = sp.diag(sp.exp(-sp.I * sp.pi / 4), sp.exp(sp.I * sp.pi / 4))
    checks.check(
        "B5",
        conj_map(Uz, P[0]) == P[2] and conj_map(Uz, P[2]) == P[1]
        and conj_map(Uz, P[4]) == P[4] and conj_map(Uz, P[5]) == P[5]
        and sp.simplify(Uz * Uz.H) == ident,
        "U_z = diag(e^{-i pi/4}, e^{i pi/4}) maps P(e_x)->P(e_y), P(e_y)->P(-e_x) and fixes P(+-e_z)",
    )
    U3 = (ident - sp.I * (sx + sy + sz)) / 2
    checks.check(
        "B6",
        conj_map(U3, P[0]) == P[2] and conj_map(U3, P[2]) == P[4] and conj_map(U3, P[4]) == P[0]
        and sp.simplify(U3 * U3.H) == ident,
        "U_3 = (I - i(sx+sy+sz))/2 is unitary and cycles P(e_x)->P(e_y)->P(e_z)->P(e_x)",
    )
    rots_psi = rots_b[:1] if mut("psi_nonconstant_passes") else rots_b
    rows = []
    for r in rots_psi:
        for a in range(M):
            row = [0] * M
            row[a] += 1
            row[rotate_menu(r, a)] -= 1
            if any(row):
                rows.append(row)
    checks.check(
        "B7",
        nullity_of_equations(rows, M) == 1,
        "the covariance equations psi(s) = psi(R s) have a one-dimensional solution space: the site weight is constant",
    )
    idx = {(a, b): a * M + b for a in range(M) for b in range(M)}
    rows = []
    for r in rots_b:
        for a in range(M):
            for b in range(M):
                row = [0] * (M * M)
                row[idx[(a, b)]] += 1
                row[idx[(rotate_menu(r, a), rotate_menu(r, b))]] -= 1
                if any(row):
                    rows.append(row)
    for a in range(M):
        for b in range(M):
            row = [0] * (M * M)
            row[idx[(a, b)]] += 1
            row[idx[(b, a)]] -= 1
            if any(row):
                rows.append(row)
    checks.check(
        "B8",
        nullity_of_equations(rows, M * M) == 3,
        "a covariant symmetric pair weight has exactly three free orbit values (solution space dimension 3)",
    )
    R_flip = ((0, 1, 2), (-1, 1, -1)) if not mut("edge_flip_not_in_group") else ((0, 1, 2), (-1, 1, 1))
    e1 = (1, 0, 0)
    g0 = tuple(x + y for x, y in zip(rotate_vector(R_flip, (0, 0, 0)), e1))
    g1 = tuple(x + y for x, y in zip(rotate_vector(R_flip, e1), e1))
    sym_ok = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        for a in range(M):
            for b in range(M):
                ra, rb = rotate_menu(R_flip, a), rotate_menu(R_flip, b)
                sym_ok = sym_ok and phi[a][b] == phi[rb][ra] == phi[b][a]
    checks.check(
        "B9",
        R_flip in ROTATIONS and g0 == e1 and g1 == (0, 0, 0) and sym_ok,
        "the edge flip t_{e1} o R_{e2,pi} lies in the group, swaps 0 and e1, and forces phi(a,b) = phi(rho b, rho a) = phi(b,a) on all 36 pairs",
    )
    positive = True
    for triple in TRIPLES:
        phi = [list(r) for r in phi_table(triple)]
        if mut("positivity_zero_entry_passes"):
            phi[1][2] = 0
        for name in ("path3", "star4", "cycle4"):
            N = neighbors(WINDOWS[name], SIZES[name])
            for x in range(SIZES[name]):
                nb = N[x]
                for mask in range(1 << len(nb)):
                    A = [nb[i] for i in range(len(nb)) if mask >> i & 1]
                    for eta in product(range(M), repeat=len(A)):
                        nums = rule_numerators(range(M), eta, phi)
                        positive = positive and all(t > 0 for t in nums)
    checks.check(
        "B10",
        positive,
        "positivity premise: every r(s | eta) > 0 for every partial recorded set eta at the declared triples",
    )


# ==================================================================== family C
def full_conditionals_match(name, phi, configs, exterior_mu=None, exterior_rule=None, two_hops=False, bad_edge=False):
    edges = WINDOWS[name]
    n = SIZES[name]
    N = neighbors(edges, n)
    N2 = {x: tuple(sorted({z for y in N[x] for z in N[y] if z != x} | set(N[x]))) for x in range(n)}
    for v in configs:
        for x in range(n):
            ws = []
            for s in range(M):
                vs = v[:x] + (s,) + v[x + 1:]
                w = static_weight(vs, edges, phi, exterior_mu)
                if bad_edge:
                    i, j = edges[0]
                    w *= phi[vs[i]][vs[j]]
                ws.append(w)
            recorded = [v[y] for y in (N2[x] if two_hops else N[x])]
            if exterior_rule:
                recorded += list(exterior_rule[x])
            nums = rule_numerators(range(M), recorded, phi)
            Zs, Zr = sum(ws), sum(nums)
            for s in range(M):
                if Fraction(ws[s], Zs) != Fraction(nums[s], Zr):
                    return False
    return True


def cube_configuration_family():
    fam = {(REF,) * 8}
    for i in range(8):
        for s in range(M):
            if s != REF:
                v = [REF] * 8
                v[i] = s
                fam.add(tuple(v))
    for i in range(8):
        for j in range(i + 1, 8):
            for s in range(M):
                for t in range(M):
                    if s != REF and t != REF:
                        v = [REF] * 8
                        v[i], v[j] = s, t
                        fam.add(tuple(v))
    state = 20260906
    sample = []
    for _ in range(300):
        v = []
        for _k in range(8):
            state = (1103515245 * state + 12345) % (2 ** 31)
            v.append((state >> 16) % M)
        sample.append(tuple(v))
    return tuple(sorted(fam)) + tuple(sample)


def compat_rows(edges, n, numerators_of):
    """Rows of the homogeneous system mu(v) Z_x - num_x(v) sum_t mu(v^{x->t}) = 0."""
    N = neighbors(edges, n)
    configs = list(product(range(M), repeat=n))
    idx = {v: i for i, v in enumerate(configs)}
    rows = []
    for v in configs:
        for x in range(n):
            nums = numerators_of([v[y] for y in N[x]])
            Z = sum(nums)
            row = [0] * len(configs)
            row[idx[v]] += Z
            for t in range(M):
                row[idx[v[:x] + (t,) + v[x + 1:]]] -= nums[v[x]]
            rows.append(row)
    return rows, configs


def sum_rule_numerators(lam_num, lam_den):
    def f(recorded):
        nums = [lam_den + lam_num * sum(vdot(s, y) for y in recorded) for s in range(M)]
        assert all(t > 0 for t in nums), "sum rule positivity bound |lambda| < 1/deg violated"
        return nums
    return f


def brook_cycle(rule):
    """Brook cycle at sites 1-2 of path3: a=P(e_x)->a'=P(-e_x) at the end site, b=P(e_x)->b'=P(-e_x) at the middle, c=P(e_x)."""
    a, a2, b, b2, c = 0, 1, 0, 1, 0
    num = rule(a2, [b]) * rule(b2, [a2, c]) * rule(a, [b2]) * rule(b, [a, c])
    den = rule(a, [b]) * rule(b, [a2, c]) * rule(a2, [b2]) * rule(b2, [a, c])
    if mut("brook_cycle_sign_flip"):
        num, den = num * rule(a, [b]) ** 2, den * rule(a2, [b]) ** 2
    return sp.cancel(num / den)


def family_c(checks: Checks) -> None:
    cube_family = cube_configuration_family()
    ok_exh = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        for name in ("path3", "P4", "star4", "cycle4"):
            configs = list(product(range(M), repeat=SIZES[name]))
            ok_exh = ok_exh and full_conditionals_match(
                name, phi, configs,
                two_hops=mut("static_conditional_uses_two_hops"),
                bad_edge=mut("static_mu_wrong_edge_weight"),
            )
    checks.check(
        "C1",
        ok_exh,
        "Theorem A instance: the static law's full conditionals equal the product rule on path3, P4, star4, cycle4 (every configuration, site, s; both triples)",
    )
    ok_ext = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        configs = list(product(range(M), repeat=4))
        ok_ext = ok_ext and full_conditionals_match(
            "cycle4", phi, configs,
            exterior_mu=None if mut("exterior_factor_dropped") else CYCLE4_EXTERIOR,
            exterior_rule=CYCLE4_EXTERIOR,
        )
    checks.check(
        "C2",
        ok_ext,
        "the boundary-conditioned static law on cycle4 (exterior records P(+e_x), P(-e_y) at every site) has full conditionals equal to the rule with exterior records included",
    )
    ok_cube = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        ok_cube = ok_cube and full_conditionals_match("cube8", phi, cube_family)
        ok_cube = ok_cube and full_conditionals_match("cube8", phi, cube_family, exterior_mu=CUBE8_EXTERIOR, exterior_rule=CUBE8_EXTERIOR)
    checks.check(
        "C3",
        ok_cube and len(cube_family) == 1041,
        "cube8: the full-conditional identity holds on the declared configuration family (741 near-reference + 300 LCG) with and without the exterior assignment",
    )
    ok_pos = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        for name in ("path3", "P4", "star4", "cycle4"):
            ok_pos = ok_pos and all(static_weight(v, WINDOWS[name], phi) > 0 for v in product(range(M), repeat=SIZES[name]))
        ok_pos = ok_pos and all(static_weight(v, WINDOWS["cube8"], phi) > 0 for v in cube_family)
    checks.check("C4", ok_pos, "positive rule => positive static law: every mu(v) > 0 on the declared windows (cube8 on its family)")
    phi = phi_table(TRIPLES[0])
    rows, configs = compat_rows(WINDOWS["path3"], 3, lambda rec: rule_numerators(range(M), rec, phi))
    if mut("compat_rank_off_by_one"):
        rows.append([1] + [0] * (len(configs) - 1))
    witness = [static_weight(v, WINDOWS["path3"], phi) for v in configs]
    rank = bareiss_rank(rows, len(configs))
    in_null = all(sum(a * b for a, b in zip(row, witness)) == 0 for row in rows)
    checks.check(
        "C5",
        len(rows) >= 648 and len(configs) == 216 and rank == 215 and in_null and all(w > 0 for w in witness),
        f"Brook uniqueness instance on path3 at (3,1,2): the compatibility system ({len(rows)} equations, 216 unknowns) has exact rank {rank} by fraction-free elimination and mu spans its nullspace with all entries positive",
    )
    ranks = {}
    for lam in ((1, 4), (-1, 8)):
        f = (lambda rec: rule_numerators(range(M), rec, phi)) if mut("sum_rule_pretends_consistent") else sum_rule_numerators(*lam)
        rows_s, _ = compat_rows(WINDOWS["path3"], 3, f)
        ranks[lam] = bareiss_rank(rows_s, 216)
    checks.check(
        "C6",
        ranks == {(1, 4): 216, (-1, 8): 216},
        f"the sum rule is not consistent on path3: the compatibility system has full rank 216 at lambda = 1/4 and -1/8 (positivity bound |lambda| < 1/deg, deg 2), ranks {tuple(ranks.values())}",
    )
    ok_edge = True
    for lam in ((1, 4), (-1, 8)):
        edges, n = (WINDOWS["path3"], 3) if mut("single_edge_sum_rule_inconsistent") else (((0, 1),), 2)
        rows_e, configs_e = compat_rows(edges, n, sum_rule_numerators(*lam))
        nullity = len(configs_e) - bareiss_rank(rows_e, len(configs_e))
        law = [lam[1] + lam[0] * vdot(v[0], v[1]) for v in configs_e]
        in_null_e = all(sum(a * b for a, b in zip(row, law)) == 0 for row in rows_e)
        ok_edge = ok_edge and nullity == 1 and in_null_e and sum(law) == 36 * lam[1]
    checks.check(
        "C7",
        ok_edge,
        "single-edge control: the sum rule is consistent on one edge (nullity 1) with the explicit law (1 + lambda<s,t>)/36 at both couplings; the obstruction needs degree >= 2",
    )
    lam = sp.symbols("lambda")

    def rule_sum(s, rec):
        w = [1 + lam * sum(vdot(t, y) for y in rec) for t in range(M)]
        return w[s] / sum(w)

    Rl = brook_cycle(rule_sum)
    numer, denom = sp.fraction(sp.factor(Rl - 1))
    poly = sp.Poly(numer, lam)
    other_roots = [rt for rt in sp.roots(poly, lam) if rt != 0]
    checks.check(
        "C8",
        Rl.subs(lam, sp.Rational(1, 4)) == sp.Rational(27, 25)
        and sp.rem(poly, sp.Poly(lam ** 2, lam)).is_zero
        and all(abs(rt) >= sp.Rational(1, 6) for rt in other_roots)
        and denom.subs(lam, sp.Rational(1, 4)) != 0,
        f"the symbolic Brook cycle of the sum rule at sites 1-2 of path3 gives R(1/4) = 27/25 and R - 1 = {sp.factor(Rl - 1)}: lambda^2 divides the numerator and no other root lies in |lambda| < 1/6",
    )
    P_, Q_, R_ = sp.symbols("p q r", positive=True)
    phis = [[(P_, Q_, R_)[orbit(a, b)] for b in range(M)] for a in range(M)]

    def rule_prod(s, rec):
        w = [sp.Mul(*[phis[t][y] for y in rec]) if rec else sp.Integer(1) for t in range(M)]
        return w[s] / sum(w)

    checks.check(
        "C9",
        sp.simplify(brook_cycle(rule_prod) - 1) == 0,
        "the same Brook cycle for the product rule with symbolic (p, q, r) is exactly 1",
    )
