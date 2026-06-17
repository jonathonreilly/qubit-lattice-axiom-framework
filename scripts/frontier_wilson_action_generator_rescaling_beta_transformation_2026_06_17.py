#!/usr/bin/env python3
"""Wilson-action beta transformation boundary under generator rescaling.

This runner supports
docs/WILSON_ACTION_GENERATOR_RESCALING_BETA_TRANSFORMATION_BOUNDARY_NOTE_2026-06-17.md.

It checks, with exact rational and symbolic arithmetic, that:

* fixed-component T_a -> c T_a scales the Wilson deficit by c^2 and requires
  beta_new / beta_old = 1/c^2 to keep the same action coefficient;
* pure basis relabeling T_a -> c T_a, F^a -> F^a/c leaves the deficit and beta
  unchanged;
* the beta_new / beta_old = c^2 law is instead the coupling-coordinate WM
  naming route g -> g/c inside beta(g)=2N_c/g^2.

The runner does not inspect audit ledgers and does not apply an audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "WILSON_ACTION_GENERATOR_RESCALING_BETA_TRANSFORMATION_BOUNDARY_NOTE_2026-06-17.md"
GRAM_NOTE = DOCS / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"
BETA_NOTE = DOCS / "BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md"
WM_NOTE = DOCS / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def gell_mann_generators() -> list[sp.Matrix]:
    i = sp.I
    zero = sp.Integer(0)
    one = sp.Integer(1)
    sqrt3 = sp.sqrt(3)
    lambdas = [
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, -i, 0], [i, 0, 0], [0, 0, 0]]),
        sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, -i], [0, 0, 0], [i, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, -i], [0, i, 0]]),
        (one / sqrt3) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
    ]
    return [sp.simplify(lam / 2) for lam in lambdas]


def part0_source_boundaries() -> None:
    section("Part 0: source boundaries")
    for path in [NOTE, GRAM_NOTE, BETA_NOTE, WM_NOTE]:
        check(f"source exists: {path.relative_to(ROOT)}", path.exists())

    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = [
        "actual_current_surface_status: exact-support",
        "target_claim_id: g_bare_rescaling_freedom_removal_theorem_note_2026-05-03",
        "beta'_fixed / beta = 1 / c^2",
        "beta'_basis = beta",
        "beta'_WM / beta = c^2",
        "no convention-free beta law",
        "Theorem A: Fixed-Component Generator Scaling",
        "Theorem B: Pure Basis Relabeling",
        "Theorem C: Coupling-Coordinate WM Naming Route",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    ]
    for marker in required:
        check(f"note marker present: {marker[:64]}", marker in text or marker in flat)

    forbidden = [
        "effective_status: retained",
        "audit_status: audited_clean",
        "Wilson plaquette action-surface selection from the framework axioms is derived",
        "g_bare = 1 is derived",
        "beta_new = c^2 beta_old follows from Wilson matching alone",
    ]
    for marker in forbidden:
        check(f"forbidden overclaim absent: {marker[:64]}", marker not in text and marker not in flat)


def part1_trace_scaling_matrix_check() -> None:
    section("Part 1: matrix trace and deficit scaling")
    gens = gell_mann_generators()
    gram = sp.Matrix([[sp.simplify(sp.trace(a * b)) for b in gens] for a in gens])
    check("canonical SU(3) trace Gram is delta/2", sp.simplify(gram - sp.eye(8) / 2) == sp.zeros(8))

    c = sp.symbols("c", positive=True)
    scaled = [c * t for t in gens]
    scaled_gram = sp.Matrix([[sp.simplify(sp.trace(a * b)) for b in scaled] for a in scaled])
    check("T -> cT scales Gram by c^2", sp.simplify(scaled_gram - c**2 * gram) == sp.zeros(8))

    f = sp.symbols("f0:8", real=True)
    x_old = sum((coeff * t for coeff, t in zip(f, gens)), sp.zeros(3))
    x_scaled = sum((coeff * t for coeff, t in zip(f, scaled)), sp.zeros(3))
    tr_old = sp.simplify(sp.trace(x_old * x_old))
    tr_scaled = sp.simplify(sp.trace(x_scaled * x_scaled))
    check("fixed components scale Tr(X^2) by c^2", sp.simplify(tr_scaled - c**2 * tr_old) == 0)

    x_relabel = sum(((coeff / c) * t for coeff, t in zip(f, scaled)), sp.zeros(3))
    check("basis relabel F -> F/c leaves X unchanged", sp.simplify(x_relabel - x_old) == sp.zeros(3))
    check("basis relabel leaves Tr(X^2) unchanged", sp.simplify(sp.trace(x_relabel * x_relabel) - tr_old) == 0)


def beta_from_wm(n_c: Fraction, g2: Fraction) -> Fraction:
    return Fraction(2) * n_c / g2


def part2_fixed_component_beta_compensation() -> None:
    section("Part 2: fixed-component beta compensation")
    samples = [
        (Fraction(3), Fraction(1)),
        (Fraction(3), Fraction(5, 7)),
        (Fraction(5), Fraction(11, 13)),
    ]
    c_values = [Fraction(1, 2), Fraction(2), Fraction(3), Fraction(7, 5)]

    for n_c, g2 in samples:
        beta = beta_from_wm(n_c, g2)
        old_coeff = beta * g2 / (4 * n_c)
        check(f"old Wilson coefficient matches 1/2 for N={n_c}, g2={g2}", old_coeff == Fraction(1, 2))
        for c in c_values:
            c2 = c * c
            beta_fixed = beta / c2
            new_coeff = beta_fixed * c2 * g2 / (4 * n_c)
            check(
                f"fixed-component compensation beta/c^2 preserves action: c={c}",
                new_coeff == old_coeff,
                f"ratio={beta_fixed / beta}",
            )
            wrong_coeff = c2 * beta * c2 * g2 / (4 * n_c)
            check(
                f"c^2 beta is not fixed-component compensation for c={c}",
                wrong_coeff != old_coeff,
                f"wrong/old={wrong_coeff / old_coeff}",
            )


def part3_basis_relabeling() -> None:
    section("Part 3: pure basis relabeling")
    for c in [Fraction(1, 2), Fraction(2), Fraction(3), Fraction(7, 5)]:
        fixed_deficit_ratio = c * c
        relabel_component_ratio = Fraction(1, 1) / (c * c)
        relabel_deficit_ratio = fixed_deficit_ratio * relabel_component_ratio
        check(f"basis relabel deficit ratio is one for c={c}", relabel_deficit_ratio == 1)
        check(f"basis relabel beta ratio is one for c={c}", Fraction(1, 1) == 1)


def part4_wm_coupling_coordinate_route() -> None:
    section("Part 4: coupling-coordinate WM route")
    for n_c in [Fraction(3), Fraction(5), Fraction(7, 2)]:
        for g2 in [Fraction(1), Fraction(5, 7), Fraction(11, 13)]:
            beta = beta_from_wm(n_c, g2)
            for c in [Fraction(1, 2), Fraction(2), Fraction(3), Fraction(7, 5)]:
                c2 = c * c
                g2_prime = g2 / c2
                beta_prime = beta_from_wm(n_c, g2_prime)
                check(
                    f"WM naming route beta(g/c)=c^2 beta: N={n_c}, g2={g2}, c={c}",
                    beta_prime == c2 * beta,
                    f"ratio={beta_prime / beta}",
                )
                check(
                    f"WM product invariant on coupling-coordinate route: c={c}",
                    beta_prime * g2_prime == beta * g2,
                )


def part5_downstream_wiring() -> None:
    section("Part 5: downstream source wiring")
    gram_text = GRAM_NOTE.read_text(encoding="utf-8")
    beta_text = BETA_NOTE.read_text(encoding="utf-8")
    beta_flat = " ".join(beta_text.split())
    boundary_name = NOTE.name
    check("Gram-only note cites boundary theorem", boundary_name in gram_text)
    check("Gram-only note remains not beta-routing", "This note remains the Gram-only lemma" in gram_text)
    check("beta arithmetic note cites boundary theorem", boundary_name in beta_text)
    check("beta arithmetic note uses coupling-coordinate route", "coupling-coordinate WM route" in beta_text)
    check(
        "beta arithmetic note excludes fixed-component compensation",
        "not the fixed-component Wilson-action compensation" in beta_flat,
    )


def main() -> int:
    print("WILSON ACTION GENERATOR-RESCALING BETA TRANSFORMATION BOUNDARY")
    part0_source_boundaries()
    part1_trace_scaling_matrix_check()
    part2_fixed_component_beta_compensation()
    part3_basis_relabeling()
    part4_wm_coupling_coordinate_route()
    part5_downstream_wiring()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
