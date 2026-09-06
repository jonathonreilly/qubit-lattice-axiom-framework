#!/usr/bin/env python3
"""Exact checks: the row-sweep formation law versus the static law on an infinite strip.

Scope.  The menu is the six Bloch-axis projectors inside M_2(C); the rule is
the covariant positive product rule with orbit weights (p, q, r) at the declared
exact triples (3, 1, 2) and (5, 2, 4).  Three exact objects: (C) the family of
finite-window static laws with exterior records is consistent (the conditional
of a sub-window is the sub-window's own static law with the adjacent records as
exterior), executed on the open 2x2x2 cube and the plaquette; (E) on the strips
of width W (rows of W sites, nearest-neighbor edges) the row sweep under the
records-only reading has an exactly solvable formation law: every row has the
path static law p_0, and every horizontal or vertical nearest-neighbor pair has
the single-edge law, executed at widths 2, 3 and 4 and proved for every width
and length by a telescoping identity; (F) the static law of the width-2 and
width-3 strips has a center-row pair-parallel probability s_inf enclosed in an
exact rational interval by transfer-matrix symmetry reduction and algebraic
root isolation; the interval excludes the formation value p/(p+q+4r).  Nothing
is claimed about the plane's static law, about uniqueness of an infinite-volume
static law on the cubic lattice, or about any three-recorded-neighbor sweep; no
order is selected as physical.  Exact integer, rational and symbolic arithmetic
only: the runner scans its own source and fails if a floating-point literal or
a floating-point conversion call appears.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from math import lcm, prod
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
PARENT_NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[2]
CLAIM_ID = (
    "admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_"
    "bounded_theorem_note_2026-09-06"
)
PARENT_CLAIM_ID = (
    "admissibility_rule_formation_law_versus_static_law_finite_window_"
    "classification_bounded_theorem_note_2026-09-06"
)
PARENT_FRAGMENT = "equals its static law exactly when every record forms with at most one recorded neighbor"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "records are permanent",
    "Only records are readable.",
    "A site with no record cannot be read.",
)

# ---------------------------------------------------------------- mutations
MUTATION_GATE = {
    "kernel_not_doubly_stochastic": "B",
    "z2_identity_wrong_power": "B",
    "path_law_not_formation": "B",
    "spec_conditional_ignores_exterior": "C",
    "spec_conditional_two_hop": "C",
    "spec_face_wrong_subwindow": "C",
    "row_kernel_formula_wrong_denominator": "D",
    "row_kernel_drops_left_neighbor": "D",
    "invariance_forced_true": "D",
    "pair_law_wrong_column": "D",
    "direct_strip_law_mismatch": "D",
    "asymmetric_control_passes": "D",
    "constant_rule_not_uniform": "D",
    "three_neighbor_witness_forced": "D",
    "orbit_count_wrong": "E",
    "quotient_not_commuting": "E",
    "charpoly_coefficient_off": "E",
    "perron_interval_wrong_root": "E",
    "eigvec_residual_nonzero": "E",
    "limit_law_uses_rho_not_squared": "E",
    "s_inf_enclosure_contains_formation_value": "E",
    "finite_n_sequence_shuffled": "E",
    "second_eigenvalue_bound_too_small": "E",
    "claim_order_selected": "F",
    "claim_plane_static": "F",
    "claim_z3_uniqueness": "F",
    "claim_washout": "F",
    "claim_gate_fired": "F",
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


def normalize_text(text: str) -> str:
    return " ".join(text.split())


# --------------------------------------------------------------------- menu
# Menu order: P(+e_x), P(-e_x), P(+e_y), P(-e_y), P(+e_z), P(-e_z); rebuilt here, not imported.
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
PAR, ANTI, ORTH = 0, 1, 2
TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT_TRIPLE = (2, 2, 2)


def vdot(a: int, b: int) -> int:
    return sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))


def orbit(a: int, b: int) -> int:
    d = vdot(a, b)
    return PAR if d == 1 else (ANTI if d == -1 else ORTH)


def phi_table(triple):
    return tuple(tuple(triple[orbit(a, b)] for b in range(M)) for a in range(M))


def permutation_sign(perm) -> int:
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inv % 2 else 1


def proper_rotations():
    out = []
    for perm in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] == 1:
                out.append((perm, signs))
    return tuple(out)


ROTATIONS = proper_rotations()


def rotate_menu(rot, a: int) -> int:
    perm, signs = rot
    v = MENU_VECTORS[a]
    out = [0, 0, 0]
    for i in range(3):
        out[perm[i]] = signs[i] * v[i]
    return MENU_VECTORS.index(tuple(out))


# ------------------------------------------------------------------- rule
def rule(s: int, recorded, phi) -> Fraction:
    """r(s | recorded neighbors) for the product rule with constant site weight (records-only reading)."""
    num = prod(phi[s][e] for e in recorded)
    den = sum(prod(phi[t][e] for e in recorded) for t in range(M))
    return Fraction(num, den)


def one_edge_kernel(phi):
    z1 = sum(phi[0])
    return [[Fraction(phi[a][s], z1) for s in range(M)] for a in range(M)]


def formation_law_on_graph(n: int, nbrs, order, phi, all_neighbors: bool = False):
    """Block 01's definition: mu_sigma(v) = prod_k r(v_{x_k} | records on A_k)."""
    law = {}
    for v in product(range(M), repeat=n):
        w = Fraction(1)
        formed: set = set()
        for x in order:
            A = nbrs[x] if all_neighbors else tuple(y for y in nbrs[x] if y in formed)
            w *= rule(v[x], tuple(v[y] for y in A), phi)
            formed.add(x)
        law[v] = w
    return law


# ==================================================================== family A
def family_a(checks: Checks, note_text: str, axiom_text: str, parent_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3, "the three declared audit inputs exist")
    flat = normalize_text(axiom_text)
    checks.check("A2", all(n in flat for n in AXIOM_NEEDLES[:2]), "axiom memo: both Admissibility sentences verbatim")
    checks.check("A3", all(n in flat for n in AXIOM_NEEDLES[2:]), "axiom memo: the four Record sentences verbatim")
    checks.check("A4", PARENT_CLAIM_ID in parent_text and PARENT_FRAGMENT in normalize_text(parent_text), "parent note carries its claim id and the parent theorem sentence")
    checks.check("A5", CLAIM_ID in note_text, "this note carries its claim id")


# ==================================================================== family B
def family_b(checks: Checks) -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    tr = (p, q, r)
    phi = [[tr[orbit(a, b)] for b in range(M)] for a in range(M)]
    z1 = sum(phi[0][s] for s in range(M))
    K = [[phi[s][a] / z1 for s in range(M)] for a in range(M)]
    if mut("kernel_not_doubly_stochastic"):
        K[0][1] = K[0][1] + sp.Rational(1, 7)
    sym = all(sp.simplify(K[a][s] - K[s][a]) == 0 for a in range(M) for s in range(M))
    rows_one = all(sp.simplify(sum(K[a][s] for s in range(M)) - 1) == 0 for a in range(M))
    cols_one = all(sp.simplify(sum(K[a][s] for a in range(M)) - 1) == 0 for s in range(M))
    checks.check("B1", sym and rows_one and cols_one and sp.expand(z1 - (p + q + 4 * r)) == 0, "K = phi/Z_1 symmetric, rows and columns sum to one (symbolic), Z_1 = p+q+4r")
    power = 3 if mut("z2_identity_wrong_power") else 2
    e1 = all(sp.expand(sum(phi[s][a] * phi[s][b] for s in range(M)) - z1**power * sum(K[a][s] * K[s][b] for s in range(M))) == 0 for a in range(M) for b in range(M))
    checks.check("B2", e1, "E1: Z_2(a,b) = Z_1^2 (K^2)(a,b) symbolic for all 36 pairs")
    unif = all(sp.simplify(sum(sp.Rational(1, 6) * K[a][s] for a in range(M)) - sp.Rational(1, 6)) == 0 for s in range(M))
    checks.check("B3", unif, "the uniform law is K-invariant (symbolic)")
    # path static law p_0 equals the formation law of the path swept from an end (block 01 Theorem B instance)
    ok = True
    for triple in TRIPLES:
        ph = phi_table(triple)
        Kn = one_edge_kernel(ph)
        for W in (2, 3):
            nbrs = {j: tuple(k for k in (j - 1, j + 1) if 0 <= k < W) for j in range(W)}
            order = (0, 2, 1) if (mut("path_law_not_formation") and W == 3) else tuple(range(W))
            law = formation_law_on_graph(W, nbrs, order, ph)
            for rho in product(range(M), repeat=W):
                p0 = Fraction(1, 6) * prod((Kn[rho[j - 1]][rho[j]] for j in range(1, W)), start=Fraction(1))
                if law[rho] != p0:
                    ok = False
    checks.check("B4", ok, "p_0 = (1/6) prod K equals the end-swept path formation law, W = 2, 3, both triples")


# ==================================================================== family C
def cube_edges():
    return tuple((a, b) for a in range(8) for b in range(a + 1, 8) if bin(a ^ b).count("1") == 1)


CUBE_EDGES = cube_edges()
# site index i = x + 2y + 4z; the exterior neighbor along axis a carries P(+e_a): menu 0, 2, 4
CUBE_EXTERIOR = {x: (0, 2, 4) for x in range(8)}
CYCLE_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
CYCLE_EXTERIOR = {x: (0, 3) for x in range(4)}


def neighbors_of(edges, n):
    N = {i: [] for i in range(n)}
    for i, j in edges:
        N[i].append(j)
        N[j].append(i)
    return {i: tuple(sorted(v)) for i, v in N.items()}


def static_table(n, edges, exterior, phi):
    """Static weight of every configuration, indexed by the base-6 code with site 0 most significant."""
    out = []
    for v in product(range(M), repeat=n):
        out.append(prod(phi[v[i]][v[j]] for i, j in edges) * prod(phi[v[x]][o] for x in range(n) for o in exterior[x]))
    return out


def subwindow_law(delta, edges, exterior, phi, comp_sites, comp_vals, n):
    """mu_Delta^{omega'}: internal edges of Delta, exterior records of Lambda at Delta, records of Lambda\\Delta adjacent to Delta."""
    N = neighbors_of(edges, n)
    dpos = {x: i for i, x in enumerate(delta)}
    internal = [(dpos[a], dpos[b]) for a, b in edges if a in dpos and b in dpos]
    if mut("spec_face_wrong_subwindow") and len(delta) == 4:
        internal = [(0, 1), (1, 2), (2, 3), (3, 0)]
    cval = dict(zip(comp_sites, comp_vals))
    ext = {i: [] for i in range(len(delta))}
    for x in delta:
        if not mut("spec_conditional_ignores_exterior"):
            ext[dpos[x]].extend(exterior[x])
        for y in N[x]:
            if y in cval:
                ext[dpos[x]].append(cval[y])
        if mut("spec_conditional_two_hop"):
            for y in N[x]:
                for z in N[y]:
                    if z in cval and z not in N[x] and z != x:
                        ext[dpos[x]].append(cval[z])
    law = []
    for u in product(range(M), repeat=len(delta)):
        law.append(prod(phi[u[a]][u[b]] for a, b in internal) * prod(phi[u[i]][o] for i in range(len(delta)) for o in ext[i]))
    return law


def conditional_matches(n, edges, exterior, phi, delta, table):
    """C1 on one sub-window (Delta = the leading sites 0..k-1 in index order): every complement configuration."""
    k = len(delta)
    comp = tuple(range(k, n))
    block = M ** (n - k)
    ok = True
    N = neighbors_of(edges, n)
    adjacent = tuple(y for y in comp if any(y in N[x] for x in delta))
    groups: dict = {}
    for c_code, cv in enumerate(product(range(M), repeat=n - k)):
        full = [table[d * block + c_code] for d in range(M ** k)]
        sub = subwindow_law(delta, edges, exterior, phi, comp, cv, n)
        sf, ss = sum(full), sum(sub)
        if any(full[d] * ss != sub[d] * sf for d in range(M ** k)):
            ok = False
            break
        key = tuple(cv[comp.index(y)] for y in adjacent)
        if key in groups:
            g = groups[key]
            if any(full[d] * g[1] != g[0][d] * sf for d in range(M ** k)):
                ok = False
                break
        else:
            groups[key] = (full, sf)
    return ok, len(groups), len(comp) - len(adjacent)


def family_c(checks: Checks) -> None:
    res = {}
    for triple in TRIPLES:
        phi = phi_table(triple)
        tab = static_table(8, CUBE_EDGES, CUBE_EXTERIOR, phi)
        res[("cube", triple)] = {k: conditional_matches(8, CUBE_EDGES, CUBE_EXTERIOR, phi, tuple(range(k)), tab) for k in (4, 2, 1)}
        del tab
        tab = static_table(4, CYCLE_EDGES, CYCLE_EXTERIOR, phi)
        res[("cycle", triple)] = {k: conditional_matches(4, CYCLE_EDGES, CYCLE_EXTERIOR, phi, tuple(range(k)), tab) for k in (2, 1)}
    face = all(res[("cube", t)][4][0] for t in TRIPLES)
    checks.check("C1", face, "cube face (sites 0-3): conditional = mu_Delta^{omega'} for all 6^4 complements, both triples")
    checks.check("C2", all(res[("cube", t)][2][0] for t in TRIPLES), "cube edge (sites 0,1): all 6^6 complements, both triples")
    checks.check("C3", all(res[("cube", t)][1][0] for t in TRIPLES), "cube site 0: all 6^7 complements, both triples")
    checks.check("C4", all(res[("cycle", t)][2][0] for t in TRIPLES), "plaquette edge with exterior (P(e_x), P(-e_y)): all 36 complements, both triples")
    checks.check("C5", all(res[("cycle", t)][1][0] for t in TRIPLES), "plaquette site with exterior: all 216 complements, both triples")
    grp = res[("cube", TRIPLES[0])]
    fr = grp[2][1] == 6 ** 4 and grp[2][2] == 2 and grp[1][1] == 6 ** 3 and grp[1][2] == 3 and res[("cycle", TRIPLES[0])][1][2] == 1
    checks.check("C6", fr, "finite range: cube edge 1296 adjacent-record classes (2 non-adjacent sites), site 216 classes (3), plaquette site (1)")


# ==================================================================== family D
def strip_rows(W):
    return list(product(range(M), repeat=W))


def row_law_p0(rows, K):
    return [Fraction(1, 6) * prod((K[r[j - 1]][r[j]] for j in range(1, len(r))), start=Fraction(1)) for r in rows]


def row_kernel_definition(rows, phi, drop_left=False):
    W = len(rows[0])
    out = []
    for b in rows:
        line = []
        for a in rows:
            w = Fraction(1)
            for j in range(W):
                rec = (b[j],) + (() if (j == 0 or drop_left) else (a[j - 1],))
                w *= rule(a[j], rec, phi)
            line.append(w)
        out.append(line)
    return out


def row_kernel_formula(rows, K, wrong_den=False):
    W = len(rows[0])
    K2 = [[sum(K[a][s] * K[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
    out = []
    for b in rows:
        line = []
        for a in rows:
            w = K[b[0]][a[0]]
            for j in range(1, W):
                den = K2[a[j - 1]][a[j]] if wrong_den else K2[a[j - 1]][b[j]]
                w *= K[a[j - 1]][a[j]] * K[a[j]][b[j]] / den
            line.append(w)
        out.append(line)
    return out


def invariant(p0, P) -> int:
    """Number of row states alpha with (p0 P)(alpha) != p0(alpha)."""
    if mut("invariance_forced_true"):
        return 0
    R = len(p0)
    return sum(1 for k in range(R) if sum(p0[i] * P[i][k] for i in range(R)) != p0[k])


def strip_edges(W, n):
    edges = []
    for i in range(n):
        for j in range(W):
            if j + 1 < W:
                edges.append((i * W + j, i * W + j + 1))
            if i + 1 < n:
                edges.append((i * W + j, (i + 1) * W + j))
    return tuple(edges)


def family_d(checks: Checks, report: dict) -> None:
    d1 = d2 = d3 = d4 = True
    for triple in TRIPLES:
        phi = phi_table(triple)
        K = one_edge_kernel(phi)
        K2 = [[sum(K[a][s] * K[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
        for W in (2, 3):
            rows = strip_rows(W)
            R = len(rows)
            p0 = row_law_p0(rows, K)
            P = row_kernel_definition(rows, phi, drop_left=mut("row_kernel_drops_left_neighbor"))
            Pf = row_kernel_formula(rows, K, wrong_den=mut("row_kernel_formula_wrong_denominator"))
            d1 = d1 and P == Pf and all(sum(P[i]) == 1 for i in range(R))
            d2 = d2 and invariant(p0, P) == 0
            report[("P", triple, W)] = (rows, p0, P)
            joint = {(i, k): p0[i] * P[i][k] for i in range(R) for k in range(R)}
            for j in range(W):
                jj = j + 1 if (mut("pair_law_wrong_column") and j + 1 < W) else j
                vert = {}
                for (i, k), w in joint.items():
                    key = (rows[i][j], rows[k][jj])
                    vert[key] = vert.get(key, Fraction(0)) + w
                d3 = d3 and all(vert[(a, b)] == Fraction(1, 6) * K[a][b] for a in range(M) for b in range(M))
                if j >= 1:
                    hor = {}
                    for (i, k), w in joint.items():
                        key = (rows[k][j - 1], rows[k][j])
                        hor[key] = hor.get(key, Fraction(0)) + w
                    d3 = d3 and all(hor[(a, b)] == Fraction(1, 6) * K[a][b] for a in range(M) for b in range(M))
            # the telescoping premise on the strip: joint law of (alpha_0, beta_1) is (1/6) K^2
            if W >= 2:
                diag = {}
                for (i, k), w in joint.items():
                    key = (rows[k][0], rows[i][1])
                    diag[key] = diag.get(key, Fraction(0)) + w
                d3 = d3 and all(diag[(a, b)] == Fraction(1, 6) * K2[a][b] for a in range(M) for b in range(M))
            # direct finite-strip formation law from block 01's definition versus p0 P^(n-1)
            for n in ((2, 3) if W == 2 else (2,)):
                edges = strip_edges(W, n)
                nbrs = neighbors_of(edges, W * n)
                law = formation_law_on_graph(W * n, nbrs, tuple(range(W * n)), phi, all_neighbors=mut("direct_strip_law_mismatch"))
                marg = [dict() for _ in range(n)]
                pair = {}
                for v, w in law.items():
                    for i in range(n):
                        key = v[i * W:(i + 1) * W]
                        marg[i][key] = marg[i].get(key, Fraction(0)) + w
                    key = (v[(n - 2) * W:(n - 1) * W], v[(n - 1) * W:])
                    pair[key] = pair.get(key, Fraction(0)) + w
                law_i = list(p0)
                chain_rows = [law_i]
                for i in range(1, n):
                    law_i = [sum(law_i[a] * P[a][k] for a in range(R)) for k in range(R)]
                    chain_rows.append(law_i)
                for i in range(n):
                    d4 = d4 and all(marg[i][rows[k]] == chain_rows[i][k] for k in range(R))
                d4 = d4 and all(pair[(rows[a], rows[k])] == chain_rows[n - 2][a] * P[a][k] for a in range(R) for k in range(R))
    checks.check("D1", d1, "E2 row kernel from the formula equals the kernel from the definition entrywise, W = 2, 3, both triples; rows sum to one")
    checks.check("D2", d2, "E3: p_0 P = p_0 exactly for W = 2, 3, both triples (all 6^W row states)")
    checks.check("D3", d3, "E4: every vertical and horizontal nearest-neighbor pair has law (1/6) K; the diagonal pair (alpha_0, beta_1) has law (1/6) K^2")
    checks.check("D4", d4, "direct finite-strip formation law (W=2: n=2,3; W=3: n=2) = p_0 P^(n-1) on every row marginal and row-pair joint")
