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
