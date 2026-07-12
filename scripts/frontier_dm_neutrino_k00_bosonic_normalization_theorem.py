#!/usr/bin/env python3
"""Exact restricted-packet identifiability test for DM-neutrino K00.

The runner does not assign ``K00 = 2`` or ``tau_E = tau_T = 1/2``.  It
constructs the most general swap-even bright-ray source deformation and solves
the scalar-baseline response-matching equation symbolically.  The result is

    K00 = c * tau_plus,

where ``c`` is the unprovided source-operator embedding scale.  It also shows
that swap symmetry fixes only ``tau_E = tau_T``, not their common magnitude.

The negative conclusion is deliberately restricted to the supplied 2x2/3x3
packet.  A future source-action theorem that constructs both ``c = 2`` and
``tau_plus = 1`` would falsify the obstruction and recover ``K00 = 2``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] [A] {name}{suffix}")


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def normalized_determinant_ratio(matrix: sp.Matrix, mass: sp.Symbol) -> sp.Expr:
    dimension = matrix.rows
    return sp.factor(matrix.det() / mass**dimension)


def part1_exact_target_and_source_rays() -> tuple[sp.Matrix, sp.Matrix, sp.Symbol]:
    print("\n" + "=" * 88)
    print("PART 1: THE EXPLICIT TARGET AND SOURCE OBJECTS FIX RAYS, NOT COEFFICIENTS")
    print("=" * 88)

    kappa, a = sp.symbols("kappa a", real=True)
    f00 = sp.ones(3) / 3
    p_plus = sp.ones(2) / 2
    swap = sp.Matrix([[0, 1], [1, 0]])

    check(
        "F00 = J3/3 is an exact rank-one projector",
        matrix_zero(f00 * f00 - f00) and f00.rank() == 1 and sp.trace(f00) == 1,
    )
    check(
        "P_plus = J2/2 is an exact swap-even rank-one projector",
        matrix_zero(p_plus * p_plus - p_plus)
        and p_plus.rank() == 1
        and matrix_zero(swap * p_plus - p_plus),
    )

    h_kappa = kappa * f00
    uniform_target = sp.ones(3, 1) / sp.sqrt(3)
    check(
        "The aligned family H_kappa = kappa F00 has both the heavy bright entry and trace-dual K00 equal to kappa",
        sp.simplify((uniform_target.T * h_kappa * uniform_target)[0] - kappa) == 0
        and sp.simplify(sp.trace(h_kappa * f00) - kappa) == 0,
        "kappa remains a free real symbol",
    )

    tau = sp.Matrix([a, a])
    check(
        "The complete swap-fixed source-vector family is tau = a(1,1)",
        matrix_zero(swap * tau - tau)
        and (swap - sp.eye(2)).nullspace() == [sp.Matrix([1, 1])],
        "swap symmetry fixes direction but not a",
    )

    projector_column = p_plus[:, 0]
    unit_bright_vector = sp.Matrix([1 / sp.sqrt(2), 1 / sp.sqrt(2)])
    check(
        "Projector-column and unit-vector normalizations select different coordinates on the same ray",
        projector_column == sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
        and sp.simplify(projector_column[0] / unit_bright_vector[0] - 1 / sp.sqrt(2)) == 0
        and projector_column != unit_bright_vector,
        "(1/2,1/2) versus (1/sqrt(2),1/sqrt(2))",
    )

    return f00, p_plus, kappa


def part2_solve_the_response_matching_equation(
    f00: sp.Matrix, p_plus: sp.Matrix, kappa: sp.Symbol
) -> tuple[sp.Symbol, sp.Symbol]:
    print("\n" + "=" * 88)
    print("PART 2: EXACT RESPONSE MATCHING LEAVES THE SOURCE-EMBEDDING SCALE FREE")
    print("=" * 88)

    mass = sp.Symbol("m", nonzero=True, real=True)
    tau_plus, c = sp.symbols("tau_plus c", real=True)
    target_block = mass * sp.eye(3) + kappa * f00
    source_block = mass * sp.eye(2) + c * tau_plus * p_plus

    target_ratio = normalized_determinant_ratio(target_block, mass)
    source_ratio = normalized_determinant_ratio(source_block, mass)
    response_residual = sp.factor(target_ratio - source_ratio)

    check(
        "The target normalized determinant is 1 + K00/m",
        sp.simplify(target_ratio - (1 + kappa / mass)) == 0,
        str(target_ratio),
    )
    check(
        "The general bright-ray source normalized determinant is 1 + c tau_plus/m",
        sp.simplify(source_ratio - (1 + c * tau_plus / mass)) == 0,
        str(source_ratio),
    )
    check(
        "Equal scalar-baseline response is equivalent to K00 = c tau_plus",
        sp.factor(mass * response_residual) == kappa - c * tau_plus
        and sp.solve(sp.Eq(response_residual, 0), kappa) == [c * tau_plus],
        f"residual={response_residual}",
    )
    logabs_polynomial_coefficients = sp.Poly(
        sp.expand((mass + kappa) ** 2 - (mass + c * tau_plus) ** 2),
        mass,
    ).all_coeffs()
    check(
        "Equality of log-absolute responses on every common nonsingular interval has no extra sign branch",
        sp.solve(logabs_polynomial_coefficients, [kappa], dict=True)
        == [{kappa: c * tau_plus}],
        "squared determinant polynomials force the same coefficient law",
    )
    check(
        "The advertised coefficient law is recovered only at the extra choice c = 2",
        sp.simplify((c * tau_plus).subs(c, 2) - 2 * tau_plus) == 0,
        "c=2 is the embedding tau_plus J2 = 2 tau_plus P_plus",
    )

    return tau_plus, c


def part3_countermodels_show_both_walls_are_independent(
    f00: sp.Matrix,
    p_plus: sp.Matrix,
    kappa: sp.Symbol,
    tau_plus: sp.Symbol,
    c: sp.Symbol,
) -> None:
    print("\n" + "=" * 88)
    print("PART 3: COUNTERMODELS ISOLATE TWO INDEPENDENT NORMALIZATION WALLS")
    print("=" * 88)

    mass = sp.Symbol("m", positive=True)

    def matched_ratios(t_value: sp.Expr, c_value: sp.Expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        k_value = sp.simplify(t_value * c_value)
        target = normalized_determinant_ratio(
            mass * sp.eye(3) + k_value * f00, mass
        )
        source = normalized_determinant_ratio(
            mass * sp.eye(2) + c_value * t_value * p_plus, mass
        )
        return k_value, target, source

    k_projector, target_projector, source_projector = matched_ratios(1, 1)
    k_rowsum, target_rowsum, source_rowsum = matched_ratios(1, 2)

    check(
        "At fixed tau_plus = 1, projector and row-sum embeddings both match response but give different K00",
        sp.simplify(target_projector - source_projector) == 0
        and sp.simplify(target_rowsum - source_rowsum) == 0
        and k_projector == 1
        and k_rowsum == 2,
        "c=1 gives K00=1; c=2 gives K00=2",
    )

    k_half, target_half, source_half = matched_ratios(sp.Rational(1, 2), 2)
    k_one, target_one, source_one = matched_ratios(1, 2)
    check(
        "At fixed row-sum embedding c = 2, two swap-even source magnitudes give different K00",
        sp.simplify(target_half - source_half) == 0
        and sp.simplify(target_one - source_one) == 0
        and k_half == 1
        and k_one == 2,
        "tau_plus=1/2 gives K00=1; tau_plus=1 gives K00=2",
    )

    check(
        "The response equation contains no condition that sets tau_plus = 1",
        tau_plus in (c * tau_plus).free_symbols
        and sp.solve(sp.Eq(kappa, c * tau_plus), tau_plus) == [kappa / c],
        "tau_plus remains an independent symbol",
    )


def part4_framework_dependency_guard() -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE APPROVED PREMISE SURFACE DOES NOT SUPPLY THE MISSING MAP")
    print("=" * 88)

    registry_path = ROOT / "docs/audit/data/axiom_premise_nodes.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    minimal_node = registry["nodes"]["minimal_axioms"]
    minimal_path = ROOT / minimal_node["current_path"]
    minimal_text = minimal_path.read_text(encoding="utf-8")

    check(
        "The approved premise registry contains only the four named foundation/primitive nodes",
        registry["canonical_ids"]
        == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
    )
    check(
        "The minimal-axiom memo explicitly leaves source/action and observable identification outside its content",
        "source/action and physical-observable identification" in minimal_text
        and "log-det" in minimal_text
        and "Further physical" in minimal_text
        and "structure requires" in minimal_text,
        minimal_node["current_path"],
    )

    primitive_needles = {
        "scale_reference_primitive": ("units conversion", "selector"),
        "kinetic_isotropy_primitive": ("c_t = c_s", "readout bridge"),
        "realized_state_primitive": ("pointwise", "normalization rule"),
    }
    primitive_scopes_ok = True
    for node_id, needles in primitive_needles.items():
        node = registry["nodes"][node_id]
        source = (ROOT / node["current_path"]).read_text(encoding="utf-8")
        primitive_scopes_ok &= all(needle in source for needle in needles)
        primitive_scopes_ok &= "K00" not in source and "tau_plus" not in source
    check(
        "Each approved primitive source keeps normalization/readout physics outside its granted scope",
        primitive_scopes_ok,
    )


def main() -> int:
    print("=" * 88)
    print("DM NEUTRINO K00 RESTRICTED-PACKET NORMALIZATION IDENTIFIABILITY NO-GO")
    print("=" * 88)

    f00, p_plus, kappa = part1_exact_target_and_source_rays()
    tau_plus, c = part2_solve_the_response_matching_equation(f00, p_plus, kappa)
    part3_countermodels_show_both_walls_are_independent(
        f00, p_plus, kappa, tau_plus, c
    )
    part4_framework_dependency_guard()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("RESULT: exact negative boundary on the restricted packet; positive K00=2 remains open")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
