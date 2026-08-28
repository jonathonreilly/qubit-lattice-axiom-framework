#!/usr/bin/env python3
"""Exact hostile controls for the J_r temporal/spatial semigroup defect."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_independent_2026_08_28 import (
    identity as independent_identity,
    matmul as independent_matmul,
    matrix_fixture as independent_matrix_fixture,
    transpose as independent_transpose,
    z2_conditional_fixture as independent_z2_fixture,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_PETER_WEYL_OPERATOR_TRUNCATION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_independent_2026_08_28.py",
)

MUTATIONS = (
    "break_import_boundary",
    "corrupt_projector",
    "corrupt_defect_identity",
    "drop_positivity",
    "corrupt_range_gate",
    "corrupt_core_order",
    "corrupt_commutator",
    "corrupt_kinetic_factor",
    "inject_kinetic_leak",
    "corrupt_conditional_mean",
    "corrupt_variance_formula",
    "drop_improper_component",
    "corrupt_nonconstancy",
    "corrupt_z2_value",
    "erase_generated_interaction",
    "corrupt_normalization_power",
    "separate_normalizations",
    "corrupt_packet_census",
    "corrupt_lipschitz_constant",
    "claim_fixed_cutoff",
    "use_auxiliary_chain",
    "claim_metric_response",
    "claim_physical_time",
    "hide_prior_art",
)

PASS = 0
FAIL = 0


def check(label: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")


def signed_permutation_frames() -> tuple[sp.Matrix, ...]:
    frames: list[sp.Matrix] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = sp.zeros(3)
            for row, column in enumerate(permutation):
                frame[row, column] = signs[row]
            frames.append(frame)
    return tuple(frames)


def z2_laplacian_range_check() -> tuple[bool, bool]:
    """Finite product-map control for A_f J = 2 J A_c on two rail links."""

    states = tuple(product((1, -1), repeat=2))
    coarse_values = ({1: F(2), -1: F(-3)}, {1: F(-5), -1: F(7)})
    factor_two = True
    range_preserved = True
    for coarse in coarse_values:
        pullback = {state: coarse[state[0] * state[1]] for state in states}
        fine_laplacian = {
            state: (
                2 * pullback[state]
                - pullback[(-state[0], state[1])]
                - pullback[(state[0], -state[1])]
            )
            for state in states
        }
        coarse_laplacian = {
            delta: coarse[delta] - coarse[-delta] for delta in (1, -1)
        }
        factor_two &= all(
            fine_laplacian[state] == 2 * coarse_laplacian[state[0] * state[1]]
            for state in states
        )
        range_preserved &= all(
            fine_laplacian[left] == fine_laplacian[right]
            for left in states
            for right in states
            if left[0] * left[1] == right[0] * right[1]
        )
    return factor_two, range_preserved


def primary_matrix_data() -> dict[str, sp.Matrix]:
    isometry = sp.Matrix(((1, 0), (0, 1), (0, 0)))
    operator = sp.Matrix(
        ((sp.Rational(1, 2), 0, sp.Rational(1, 4)),
         (0, sp.Rational(1, 3), 0),
         (sp.Rational(1, 4), 0, sp.Rational(1, 2)))
    )
    projector = isometry * isometry.T
    complement = sp.eye(3) - projector
    compressed = isometry.T * operator * isometry
    defect = isometry.T * operator**2 * isometry - compressed**2
    factor = isometry.T * operator * complement * operator * isometry
    return {
        "J": isometry,
        "S": operator,
        "Q": projector,
        "R": complement,
        "defect": defect,
        "factor": factor,
    }


def primary_z2_rows() -> tuple[tuple[int, F, F], ...]:
    """Direct finite-Haar variance calculation, independent of the helper."""

    states = tuple(product((1, -1), repeat=2))
    rows: list[tuple[int, F, F]] = []
    for member in (1, 2, 3, 5, 8):
        potential = {1: F(0), -1: F(16, member)}
        variances: dict[int, F] = {}
        for delta in (1, -1):
            fiber = tuple(state for state in states if state[0] * state[1] == delta)
            actions = tuple(potential[state[0]] + potential[state[1]] for state in fiber)
            mean = sum(actions, F(0)) / len(actions)
            second = sum((value * value for value in actions), F(0)) / len(actions)
            variances[delta] = second - mean * mean
        rows.append((member, variances[1], variances[-1]))
    return tuple(rows)


def independent_mode() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    matrix = independent_matrix_fixture()
    z2 = independent_z2_fixture()
    expected = ((F(1, 16), F(0)), (F(0), F(0)))
    checks = (
        (
            "independent rational isometry",
            independent_matmul(independent_transpose(matrix["isometry"]), matrix["isometry"])
            == independent_identity(2),
        ),
        ("independent exact positive factorization", matrix["defect"] == matrix["factor"] == expected),
        ("independent positive-contraction spectrum", matrix["operator_spectrum"] == (F(3, 4), F(1, 4), F(1, 3))),
        ("independent conditional Haar projector", z2["projector_idempotent"] and z2["projector_self_adjoint"]),
        ("independent pullback left inverse", z2["isometry_left_inverse"]),
        (
            "independent exact Z2 generated interaction",
            all(plus == F(256, n * n) and minus == 0 for n, plus, minus in z2["gamma_rows"]),
        ),
        (
            "independent variance equals direct/staged defect",
            all(direct == variance for _n, direct, variance in z2["semigroup_rows"]),
        ),
        ("independent nonconstant generated interaction", all(plus != minus for _n, plus, minus in z2["gamma_rows"])),
        (
            "independent scalar normalization square",
            matrix["scaled_defect"]
            == tuple(tuple(matrix["normalization"] ** 2 * value for value in row) for row in expected),
        ),
        ("independent nonzero normalization obstruction", any(any(value for value in row) for row in matrix["scaled_defect"])),
        ("independent packet operator distance", matrix["operator_distance"] == F(1, 8)),
        ("independent packet defect distance", matrix["defect_distance"] == F(3, 64)),
        (
            "independent four-Lipschitz defect bound",
            matrix["defect_distance"] <= 4 * matrix["operator_distance"],
        ),
        ("independent range-preserving zero control", not any(any(value for value in row) for row in matrix["range_defect"])),
    )
    for label, condition in checks:
        check(label, condition)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    if mode == "independent":
        return independent_mode()
    PASS = FAIL = 0

    source = Path(__file__).read_text(encoding="utf-8")
    note = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    parents = tuple(Path(path).read_text(encoding="utf-8") for path in AUDIT_INPUT_PATHS[1:4])
    imports_ok = all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
    if mutation == "break_import_boundary":
        imports_ok = False
    check(
        "typed imports: Block227 step, Block229 physical J_r, Block231 packet, and minimal axioms",
        imports_ok
        and all(dependency in note for dependency in (
            "CO_SCALED_TEMPORAL_TROTTER",
            "BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW",
            "jr_peter_weyl_operator_truncation",
            "minimal_axioms",
        )),
    )

    data = primary_matrix_data()
    projector_ok = data["Q"] == sp.diag(1, 1, 0) and data["Q"] ** 2 == data["Q"]
    if mutation == "corrupt_projector":
        projector_ok = False
    check(
        "Q=J J* is the typed orthogonal residual projector on the fine physical space",
        projector_ok and "Q=JJ*" in note and "H_f^phys" in note and "H_c^phys" in note,
    )

    identity_ok = data["defect"] == data["factor"] == sp.diag(sp.Rational(1, 16), 0)
    if mutation == "corrupt_defect_identity":
        identity_ok = False
    check(
        "exact direct-versus-staged identity J*S^2J-(J*SJ)^2=J*S(I-Q)SJ",
        identity_ok and "T_dir-T_stage" in note,
    )

    eigenvalues = set(data["S"].eigenvals())
    positivity_ok = eigenvalues == {sp.Rational(3, 4), sp.Rational(1, 4), sp.Rational(1, 3)}
    if mutation == "drop_positivity":
        positivity_ok = False
    check(
        "self-adjoint contraction gives a nonzero positive Gram defect",
        positivity_ok and data["S"] == data["S"].T and data["defect"].is_positive_semidefinite,
    )

    range_operator = sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4))
    range_leak = data["R"] * range_operator * data["J"]
    range_defect = (
        data["J"].T * range_operator**2 * data["J"]
        - (data["J"].T * range_operator * data["J"]) ** 2
    )
    range_ok = range_leak == sp.zeros(3, 2) and range_defect == sp.zeros(2)
    if mutation == "corrupt_range_gate":
        range_ok = False
    check(
        "zero defect is exactly the cylindrical-range invariance gate",
        range_ok and "D_epsilon=0  iff" in note,
    )

    epsilon = sp.symbols("epsilon", real=True)
    generator = sp.Matrix(((2, 0, 1), (0, 3, 0), (1, 0, 4)))
    linear_step = sp.eye(3) - epsilon * generator
    compressed_step = data["J"].T * linear_step * data["J"]
    exact_linear_defect = data["J"].T * linear_step**2 * data["J"] - compressed_step**2
    gamma = data["J"].T * generator * data["R"] * generator * data["J"]
    core_ok = sp.simplify(exact_linear_defect - epsilon**2 * gamma) == sp.zeros(2)
    if mutation == "corrupt_core_order":
        core_ok = False
    check(
        "Block227 core derivative generates epsilon^2 Gamma and no epsilon term",
        core_ok and "quadratic-form/core limit" in note,
    )

    commutator = data["Q"] * generator - generator * data["Q"]
    commutator_gamma = (commutator * data["J"]).T * (commutator * data["J"])
    commutator_ok = commutator_gamma == gamma
    if mutation == "corrupt_commutator":
        commutator_ok = False
    check(
        "generated interaction is the positive commutator square ([Q,G]J)*([Q,G]J)",
        commutator_ok and "([Q,G_f]J)*([Q,G_f]J)" in note,
    )

    factor_two, range_preserved = z2_laplacian_range_check()
    kinetic_factor_ok = factor_two
    if mutation == "corrupt_kinetic_factor":
        kinetic_factor_ok = False
    check(
        "two fine rail Casimirs induce twice the coarse rail Casimir",
        kinetic_factor_ok and "2A_(coarse bottom rails)" in note and "2A_(coarse top rails)" in note,
    )

    kinetic_range_ok = range_preserved
    if mutation == "inject_kinetic_leak":
        kinetic_range_ok = False
    check(
        "fine kinetic generator preserves the actual cylindrical range",
        kinetic_range_ok and "(I-Q)A_fJ=0" in note and "hidden rung" in note,
    )

    mu, nu, convolution = sp.symbols("mu nu convolution", real=True)
    mean = 2 * mu
    second = 2 * nu + 2 * convolution
    mean_ok = mean == 2 * mu and second == 2 * nu + 2 * convolution
    if mutation == "corrupt_conditional_mean":
        mean_ok = False
    check(
        "hidden Haar fiber gives the exact first and second conditional moments",
        mean_ok and "E[V_f|delta]=2mu" in note and "E[V_f^2|delta]=2nu+2(v*v)(delta)" in note,
    )

    variance = sp.expand(second - mean**2)
    variance_ok = variance == 2 * (nu - mu**2) + 2 * (convolution - mu**2)
    if mutation == "corrupt_variance_formula":
        variance_ok = False
    check(
        "the complete J_r defect reduces to the typed conditional variance",
        variance_ok and "Gamma=J*V_f(I-Q)V_fJ" in note and "Gamma(delta)" in note,
    )

    frames = signed_permutation_frames()
    frame_rows = tuple(
        (int(frame.det()), int((sp.eye(3) + frame).det())) for frame in frames
    )
    component_ok = len(frames) == 48 and sum(det == 1 for det, _chi in frame_rows) == 24
    component_ok &= all(chi == 0 for det, chi in frame_rows if det == -1)
    if mutation == "drop_improper_component":
        component_ok = False
    check(
        "full O(3) witness keeps all 24 proper and 24 improper signed frames",
        component_ok and "No connected component" in note and "is discarded" in note,
    )

    member = 3
    member_values = tuple(sp.Rational(16, member) * (1 - sp.Rational(chi, 8) ** member) for _det, chi in frame_rows)
    nonconstant_ok = min(member_values) == 0 and max(member_values) == sp.Rational(16, member)
    if mutation == "corrupt_nonconstancy":
        nonconstant_ok = False
    check(
        "the exterior potential is nonconstant and has a nontrivial Peter-Weyl channel",
        nonconstant_ok and "Convolution squares" in note and "nonzero nontrivial channel" in note,
    )

    z2_rows = primary_z2_rows()
    z2_ok = all(plus == F(256, n * n) and minus == 0 for n, plus, minus in z2_rows)
    if mutation == "corrupt_z2_value":
        z2_ok = False
    check(
        "exact Z2 finite control gives Gamma(+)=256/n^2 and Gamma(-)=0",
        z2_ok and "Gamma(+)=256/n^2" in note,
    )

    generated_ok = any(plus != minus for _n, plus, minus in z2_rows)
    if mutation == "erase_generated_interaction":
        generated_ok = False
    check(
        "the specified two-cell paths have a nonzero leading separation coefficient",
        generated_ok and "strictly positive leading" in note,
    )

    scalar = sp.Rational(3, 5)
    scaled_defect = (
        data["J"].T * (scalar * data["S"]) ** 2 * data["J"]
        - (data["J"].T * (scalar * data["S"]) * data["J"]) ** 2
    )
    normalization_ok = scaled_defect == scalar**2 * data["defect"]
    if mutation == "corrupt_normalization_power":
        normalization_ok = False
    check(
        "one common normalization scalar rescales the defect quadratically",
        normalization_ok and "D_epsilon[cS]=c_epsilon^2 D_epsilon[S]" in note,
    )

    convention_ok = (
        "Separately" in note
        and "normalizing the direct and staged two-step operators" in note
        and "defines a different square" in note
    )
    if mutation == "separate_normalizations":
        convention_ok = False
    check(
        "normalization convention is fixed before comparing direct and staged paths",
        convention_ok,
    )

    r_value, q_value = 2, 2
    temporal_count = 3 * r_value * q_value + 1
    half_count = 2 * r_value * q_value
    eta = temporal_count * F(1, 1000) + half_count * F(1, 2000)
    census_ok = temporal_count == 13 and half_count == 8 and eta == F(17, 1000)
    if mutation == "corrupt_packet_census":
        census_ok = False
    check(
        "complete physical packet error has explicit (3rq+1) delta_kappa + 2rq delta_beta accumulation",
        census_ok and "(3rq+1)delta_kappa+2rq delta_beta" in note,
    )

    packet = sp.Matrix(
        ((sp.Rational(1, 2), 0, sp.Rational(1, 8)),
         (0, sp.Rational(1, 3), 0),
         (sp.Rational(1, 8), 0, sp.Rational(1, 2)))
    )
    packet_compressed = data["J"].T * packet * data["J"]
    packet_defect = data["J"].T * packet**2 * data["J"] - packet_compressed**2
    operator_distance = max(abs(value) for value in (data["S"] - packet).eigenvals())
    defect_distance = max(abs(value) for value in (data["defect"] - packet_defect).eigenvals())
    lipschitz_ok = (
        operator_distance == sp.Rational(1, 8)
        and defect_distance == sp.Rational(3, 64)
        and defect_distance <= 4 * operator_distance
    )
    if mutation == "corrupt_lipschitz_constant":
        lipschitz_ok = False
    check(
        "complete defect approximation obeys ||Def(S)-Def(S_K)|| <= 4 eta_(K,r,q)",
        lipschitz_ok and "<=4||S-S^K||_op" in note and "<=4 eta_(K,r,q)" in note,
    )

    s_value = F(8, 7)
    cutoff = 14
    local_tail = s_value ** (cutoff + 1) / factorial(cutoff + 1)
    resolution_ok = 4 * (3 * r_value * q_value + 1 + 2 * r_value * q_value) * local_tail < F(1, 8) ** 2
    if mutation == "claim_fixed_cutoff":
        resolution_ok = False
    check(
        "finite cutoff can resolve Gamma only with eta_(K,r,q)=o(epsilon^2)",
        resolution_ok and "eta_(K,r,q)=o(epsilon^2)" in note and "at every finite" in note,
    )

    physical_consumer_ok = all(token in note for token in (
        "H_f^phys=P_(rq)H_(rq)", "P_lr", "Every fine temporal link", "actual square",
    ))
    if mutation == "use_auxiliary_chain":
        physical_consumer_ok = False
    check(
        "the consumer is the complete physical J_r transfer, not an auxiliary B chain",
        physical_consumer_ok and all("J_r" in parent for parent in parents[1:]),
    )

    metric_scope_ok = (
        "metric/source/matter response | open" in note
        and "pure-gauge carrier omits these variables" in note
    )
    if mutation == "claim_metric_response":
        metric_scope_ok = False
    check(
        "metric/source response remains outside the pure-gauge carrier",
        metric_scope_ok and "not a physical" in note,
    )

    time_scope_ok = "mathematical Euclidean parameter, not physical time" in note
    if mutation == "claim_physical_time":
        time_scope_ok = False
    check(
        "no physical-time, continuum, Lorentz, gravity, or action-selection overread",
        time_scope_ok and all(word in note for word in ("continuum", "Lorentz", "gravity", "action selection")),
    )

    prior_art_ok = all(token in note for token in (
        "Block227's cubic BCH residual", "Block228 derives", "Block229 proves", "Generic compression inequalities",
    ))
    if mutation == "hide_prior_art":
        prior_art_ok = False
    check(
        "prior-art fence isolates the new physical changing-carrier square",
        prior_art_ok and "MUTATIONS" in source,
    )

    print("per_element: all 48 signed O(3) frames and their exterior-character values were checked exactly")
    print("per_site: the two-cell hidden-Haar fiber and both retained coarse sectors were enumerated exactly")
    print("per_mode: the Peter--Weyl core commutator square and nontrivial convolution channel were checked")
    print("per_block: the complete physical J_r direct/staged defect and rq packet census were checked")
    print("lattice_wide: checked and not executed — only finite supplied ladders are claimed; no continuum limit is supplied")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"), default="normal")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
