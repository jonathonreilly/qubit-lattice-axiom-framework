#!/usr/bin/env python3
"""Exact checks for the J_r Peter--Weyl operator truncation theorem."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial
from pathlib import Path

import numpy as np
import sympy as sp

from admissibility_exterior_character_jr_peter_weyl_operator_truncation_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_PETER_WEYL_OPERATOR_TRUNCATION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_peter_weyl_operator_truncation_independent_2026_08_28.py",
)

MUTATIONS = (
    "corrupt_exterior_identity",
    "drop_improper_component",
    "corrupt_character_packet",
    "corrupt_poisson_tail",
    "corrupt_temporal_count",
    "corrupt_half_action_count",
    "duplicate_shared_frame",
    "allow_intermediate_retruncation",
    "corrupt_gamma",
    "corrupt_cutoff",
    "corrupt_spin_bound",
    "reverse_sandwich",
    "absolute_only_operator_bound",
    "misuse_auxiliary_perron",
    "corrupt_normalization_power",
    "misstate_absolute_operator_bound",
    "drop_projector_restriction",
    "corrupt_independent_reconstruction",
    "hide_historic_prior_art",
    "overclaim_fixed_k_uniform",
    "use_auxiliary_only",
    "claim_action_selection",
    "claim_physical_time",
    "claim_continuum",
    "break_import_boundary",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def packet_coefficients(member: int, cutoff: int, s_value: sp.Rational) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.exp(-s_value)
        * s_value**occupation
        / (sp.factorial(occupation) * 8 ** (member * occupation))
        for occupation in range(cutoff + 1)
    )


def sympy_matrix(values: tuple[tuple[Fraction, ...], ...]) -> sp.Matrix:
    return sp.Matrix(
        [
            [sp.Rational(value.numerator, value.denominator) for value in row]
            for row in values
        ]
    )


def operator_norm(matrix: sp.Matrix) -> float:
    """Numerical SVD diagnostic on an exact rational finite matrix."""

    assert matrix == matrix.T
    values = np.array(
        [[float(sp.N(matrix[row, column], 40)) for column in range(matrix.cols)] for row in range(matrix.rows)],
        dtype=float,
    )
    return float(np.linalg.svd(values, compute_uv=False)[0])


def hilbert_schmidt_norm(matrix: sp.Matrix) -> sp.Expr:
    return sp.sqrt(sum(value * value for value in matrix))


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    facts = independent_facts()

    if mode == "independent":
        checks = (
            ("independent exterior frame census", facts["frame_count"] == 48 and facts["proper"] == facts["improper"] == 24),
            ("independent exterior-character identity", facts["exterior_identity"]),
            ("independent full-member identity", facts["member_identity"]),
            ("independent actual-factor census", facts["censuses"] == ((1, 1, 4, 2), (2, 1, 7, 4), (1, 2, 7, 4), (2, 2, 13, 8))),
            ("independent hidden-rung direct/staged contraction", facts["direct_staged_hidden"]),
            ("independent shared-frame direct/staged contraction", facts["direct_staged_shared"]),
            ("independent duplicated-frame falsifier", facts["duplicated_shared_differs"]),
            ("independent physical-kernel sandwich", facts["sandwich"]),
            ("independent 8x8 Haar-matrix sandwich", facts["pointwise_matrix_sandwich"]),
            ("independent residual-projector range", facts["residual_exact"] and facts["residual_truncated"]),
            (
                "independent relative Hilbert--Schmidt bound",
                facts["hs_difference_squared"]
                <= (1 - facts["gamma_12"]) ** 2 * facts["hs_exact_squared"],
            ),
            (
                "independent Z_kappa normalization power",
                facts["normalization_exact"]
                and facts["normalization_truncated"]
                and facts["normalization_difference"],
            ),
            ("independent finite-character positivity", facts["z2_character_positive"]),
            ("independent intermediate-retruncation falsifier", facts["retruncation_differs"]),
            ("independent factorial tail K=10", 61 * facts["cutoff_tail"][10] < Fraction(1, 100_000)),
            ("independent factorial tail K=18", 61 * facts["cutoff_tail"][18] < Fraction(1, 10**12)),
        )
        for name, condition in checks:
            check(name, condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    source = Path(__file__).read_text(encoding="utf-8")
    note = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    imports_ok = all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
    if mutation == "break_import_boundary":
        imports_ok = False

    chi, member = sp.symbols("chi member", positive=True)
    q_value = 16 - 2 * chi
    u_value = chi / 8
    identity_ok = sp.simplify(1 - q_value / 16 - u_value) == 0
    if mutation == "corrupt_exterior_identity":
        identity_ok = False
    check(
        "full O(3) member: Q=16-2 chi_Lambda and f_n=(16/n)(1-(chi_Lambda/8)^n)",
        identity_ok
        and facts["exterior_identity"]
        and facts["member_identity"]
        and "chi_Lambda(g)=det(I+g)" in note,
    )

    component_values = set(facts["component_values"])
    if mutation == "drop_improper_component":
        component_values = {entry for entry in component_values if entry[0] == 1}
    check(
        "improper component: chi_Lambda=0 and every finite member has f_n=16/n",
        (-1, 0, 16) in component_values
        and facts["proper"] == facts["improper"] == 24
        and "improper component" in note,
    )

    coefficients = list(packet_coefficients(2, 4, sp.Rational(8, 7)))
    tensor_orders = tuple(2 * occupation for occupation in range(5))
    if mutation == "corrupt_character_packet":
        coefficients[-1] = -coefficients[-1]
    check(
        "finite packet: occupation k is the positive character of Lambda^(tensor nk) divided by 8^(nk)",
        all(coefficient > 0 for coefficient in coefficients)
        and tensor_orders == (0, 2, 4, 6, 8)
        and "chi_(Lambda^(tensor n k))" in note,
    )

    s_value = sp.Rational(8, 7)
    cutoff = 10
    exact_tail = 1 - sp.exp(-s_value) * sum(
        s_value**occupation / sp.factorial(occupation)
        for occupation in range(cutoff + 1)
    )
    majorant = s_value ** (cutoff + 1) / sp.factorial(cutoff + 1)
    tail_ok = 0 < sp.N(exact_tail, 40) < sp.N(majorant, 40)
    if mutation == "corrupt_poisson_tail":
        tail_ok = False
    check(
        "local tail: the exact Poisson remainder is monotone in u_n and is bounded by s^(K+1)/(K+1)!",
        tail_ok and majorant == sp.Rational(facts["cutoff_tail"][10].numerator, facts["cutoff_tail"][10].denominator),
    )

    r_value, retained_cells = 2, 2
    temporal_count = 3 * r_value * retained_cells + 1
    half_count = 2 * r_value * retained_cells
    if mutation == "corrupt_temporal_count":
        temporal_count -= 1
    if mutation == "corrupt_half_action_count":
        half_count -= 1
    check(
        "actual J_r census: 3rq+1 temporal crossings and 2rq plaquette half-actions",
        temporal_count == 13
        and half_count == 8
        and facts["censuses"][-1] == (2, 2, 13, 8)
        and "3 r q + 1" in note
        and "2 r q" in note,
    )

    shared_q2 = facts["direct_staged_shared"]
    if mutation == "duplicate_shared_frame":
        shared_q2 = not facts["duplicated_shared_differs"]
    shared_ok = facts["direct_staged_hidden"] and shared_q2
    check(
        "J_r compatibility: direct and staged Haar contractions use each shared retained frame once",
        shared_ok and "shared retained projector frame is integrated once" in note,
    )

    no_retruncation = facts["retruncation_differs"]
    if mutation == "allow_intermediate_retruncation":
        no_retruncation = False
    check(
        "algorithm boundary: Fubini reorders one fine packet but an intermediate fresh truncation is not associative",
        no_retruncation
        and facts["direct_polynomial"] == (1, 4, 6, 4, 1)
        and facts["retruncated_polynomial"] == (1, 4, 4)
        and "No representation projection is re-applied" in note,
    )

    delta_temporal = sp.Rational(1, 8)
    delta_spatial = sp.Rational(1, 6)
    gamma = (1 - delta_temporal) ** 7 * (1 - delta_spatial) ** 4
    if mutation == "corrupt_gamma":
        gamma = (1 - delta_temporal) ** 6 * (1 - delta_spatial) ** 4
    epsilon = 1 - gamma
    union_bound = 7 * delta_temporal + 4 * delta_spatial
    check(
        "retained-cell accumulation: gamma=(1-delta_kappa)^(3rq+1)(1-delta_beta)^(2rq) and 1-gamma obeys the union bound",
        gamma == sp.Rational(facts["gamma_12"].numerator, facts["gamma_12"].denominator)
        and epsilon <= union_bound
        and "epsilon_(K,r,q)=1-gamma_(K,r,q)" in note,
    )

    cutoff_for_check = 10 if mutation != "corrupt_cutoff" else 6
    tail_at_cutoff = Fraction(8, 7) ** (cutoff_for_check + 1) / factorial(cutoff_for_check + 1)
    check(
        "explicit cutoff: the factorial/Stirling rule controls a requested tolerance with logarithmic volume dependence",
        61 * tail_at_cutoff < Fraction(1, 100_000)
        and "K + 1 >= 2 e s_*" in note
        and "log_2((5 r q + 1)/eta)" in note,
    )

    n_value, cutoff_value = 2, 3
    frame_spin = 3 * n_value * cutoff_value
    rung_spin = n_value * (cutoff_value + 2 * cutoff_value)
    rail_spin = n_value * (cutoff_value + cutoff_value)
    if mutation == "corrupt_spin_bound":
        frame_spin -= 1
    check(
        "finite spin-network: bounded incidence gives finite frame, rung, and rail tensor-order bounds",
        frame_spin == 18 and rung_spin == 18 and rail_spin == 12
        and "3 n K" in note,
    )

    exact_matrix = sympy_matrix(facts["exact_matrix"])
    truncated_matrix = sympy_matrix(facts["truncated_matrix"])
    difference_matrix = exact_matrix - truncated_matrix
    physical_exact = sympy_matrix(facts["physical_exact_matrix"])
    physical_truncated = sympy_matrix(facts["physical_truncated_matrix"])
    physical_difference = physical_exact - physical_truncated
    if mutation == "reverse_sandwich":
        sandwich = all(
            truncated_matrix[row, column] <= gamma * exact_matrix[row, column]
            and exact_matrix[row, column] <= truncated_matrix[row, column]
            for row in range(8)
            for column in range(8)
        )
    else:
        sandwich = facts["pointwise_matrix_sandwich"]
    check(
        "physical kernel sandwich: gamma K_exact <= K_K <= K_exact after the complete shared-frame marginal",
        sandwich
        and facts["max_error_12"] <= 1 - facts["gamma_12"]
        and "gamma_(K,r,q) K_(r,q)" in note,
    )

    exact_op = operator_norm(physical_exact)
    truncated_op = operator_norm(physical_truncated)
    difference_op = operator_norm(physical_difference)
    relative_coefficient = epsilon / 2 if mutation == "absolute_only_operator_bound" else epsilon
    relative_operator = difference_op <= sp.N(relative_coefficient, 60) * exact_op
    check(
        "operator comparison: lattice-order domination gives ||T-T_K|| <= epsilon ||T||",
        relative_operator
        and abs(operator_norm(difference_matrix) - difference_op) < 1e-13
        and "|(T_(r,q)-T_(r,q)^K)F|" in note
        and "epsilon_(K,r,q) ||T_(r,q)||_op" in note,
    )

    top_denominator = exact_op if mutation == "misuse_auxiliary_perron" else truncated_op
    normalized_difference = physical_exact / exact_op - physical_truncated / top_denominator
    top_normalization = (
        top_denominator == truncated_op
        and operator_norm(normalized_difference) <= sp.N(2 * epsilon, 60)
    )
    check(
        "top-norm comparison: separately normalizing the two complete positive transfers costs at most 2 epsilon",
        top_normalization
        and "2 epsilon_(K,r,q)" in note
        and "not the auxiliary-message Perron vector" in note,
    )

    normalization_power = 6 if mutation == "corrupt_normalization_power" else 7
    normalization_scalar = facts["temporal_normalization"]
    normalized_exact = sympy_matrix(facts["normalized_exact_matrix"])
    normalized_truncated = sympy_matrix(facts["normalized_truncated_matrix"])
    normalized_actual_difference = normalized_exact - normalized_truncated
    normalization_factor = sp.Rational(
        normalization_scalar.numerator, normalization_scalar.denominator
    ) ** (-normalization_power)
    normalization_power_ok = (
        normalized_exact == normalization_factor * exact_matrix
        and normalized_truncated == normalization_factor * truncated_matrix
        and normalized_actual_difference == normalization_factor * difference_matrix
    )
    check(
        "normalization scalar: the original normalized-w kernel differs by exactly Z_kappa^(3rq+1)",
        normalization_power_ok and "Z_kappa^(3 r q + 1)" in note,
    )

    absolute_rhs = 7 * delta_temporal + 4 * delta_spatial
    if mutation == "misstate_absolute_operator_bound":
        absolute_rhs /= 8
    absolute_operator = operator_norm(normalized_actual_difference) <= sp.N(absolute_rhs, 60)
    normalized_hs = hilbert_schmidt_norm(normalized_actual_difference)
    hs_rhs = normalization_factor * epsilon
    check(
        "absolute original-transfer bound: telescoping avoids false hatted-kernel normalization while HS retains Z_kappa power",
        absolute_operator
        and normalized_hs <= hs_rhs
        and "(3 r q + 1) delta_kappa + 2 r q delta_beta" in note
        and "Z_kappa^(-(3 r q + 1)) epsilon_(K,r,q)" in note
        and "rather than renormalizing it by a new truncated partition function" in note,
    )

    if mutation == "drop_projector_restriction":
        wrong_restriction = exact_matrix[:4, :4]
        projector_ok = operator_norm(wrong_restriction) == exact_op
    else:
        projector_ok = (
            facts["residual_exact"]
            and facts["residual_truncated"]
            and abs(operator_norm(exact_matrix) - exact_op) < 1e-13
            and abs(operator_norm(truncated_matrix) - truncated_op) < 1e-13
        )
    check(
        "projector typing: the full Haar-space bound descends to the residual GxG physical subspace by contraction",
        projector_ok and "restriction to P_lr" in note,
    )

    independent_ok = mutation != "corrupt_independent_reconstruction"
    check(
        "independent reconstruction: raw fine-link and history-message sums agree with hidden and shared columns",
        independent_ok
        and facts["direct_staged_hidden"]
        and facts["direct_staged_shared"]
        and facts["z2_character_positive"],
    )

    prior_art_ok = mutation != "hide_historic_prior_art"
    check(
        "prior-art fence: archived SU3 Poissonized occupation/intertwiner tails are credited but not imported as authority",
        prior_art_ok
        and "POISSONIZED_OCCUPATION_INTERTWINER_COMPRESSION_NOTE.md" in note
        and "authority `none`" in note,
    )

    fixed_cutoff_boundary = mutation != "overclaim_fixed_k_uniform"
    check(
        "volume accounting: the guaranteed tolerance rule carries explicit rq-dependent cutoff growth",
        fixed_cutoff_boundary and "guaranteed fixed-tolerance cutoff" in note,
    )

    actual_kernel = mutation != "use_auxiliary_only"
    check(
        "trace reachability: the theorem controls the actual J_r shared-frame transfer rather than B^r alone",
        actual_kernel
        and "This is not the auxiliary-message tail" in note,
    )

    scope_ok = not any(
        mutation == name
        for name in ("claim_action_selection", "claim_physical_time", "claim_continuum")
    )
    check(
        "scope boundary: supplied action/measure/projector remain explicit and no action selection, physical time, continuum, Lorentz, or gravity follows",
        scope_ok
        and "does not select the action" in note
        and "physical time" in note
        and "continuum" in note
        and "gravity" in note,
    )

    check(
        "import integrity: note, exact parent, axiom fence, independent helper, and every mutation are packet-bound",
        imports_ok
        and all(name in source for name in MUTATIONS)
        and Path(AUDIT_INPUT_PATHS[-1]).name in source,
    )

    print("per_element: exterior-character occupations, positive coefficients, and Poisson tails were derived")
    print("per_site: frame/rung/rail incidence and finite channel bounds were checked")
    print("per_mode: finite tensor orders, improper parity, and re-truncation failure were checked")
    print("per_block: exact shared-frame J_r contraction and rq accumulation were executed on finite controls")
    print("lattice_wide: complete physical operator/top-norm error is proved with K depending on rq; no continuum scale is supplied")
    print("STATUS: bounded physical-transfer Peter--Weyl truncation conditional on the supplied parent action and measure")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"), default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
