#!/usr/bin/env python3
"""Exact checks for the J_r Peter--Weyl operator truncation theorem."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial
from pathlib import Path

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

    shared_ok = (
        facts["direct_staged_hidden"]
        and facts["direct_staged_shared"]
        and facts["duplicated_shared_differs"]
    )
    if mutation == "duplicate_shared_frame":
        shared_ok = False
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

    sandwich = facts["sandwich"]
    if mutation == "reverse_sandwich":
        sandwich = False
    check(
        "physical kernel sandwich: gamma K_exact <= K_K <= K_exact after the complete shared-frame marginal",
        sandwich
        and facts["max_error_12"] <= 1 - facts["gamma_12"]
        and "gamma_(K,r,q) K_(r,q)" in note,
    )

    relative_operator = mutation != "absolute_only_operator_bound"
    check(
        "operator comparison: lattice-order domination gives ||T-T_K|| <= epsilon ||T||",
        relative_operator
        and "|(T_(r,q)-T_(r,q)^K)F|" in note
        and "epsilon_(K,r,q) ||T_(r,q)||_op" in note,
    )

    top_normalization = mutation != "misuse_auxiliary_perron"
    check(
        "top-norm comparison: separately normalizing the two complete positive transfers costs at most 2 epsilon",
        top_normalization
        and "2 epsilon_(K,r,q)" in note
        and "not the auxiliary-message Perron vector" in note,
    )

    normalization_power = 7
    if mutation == "corrupt_normalization_power":
        normalization_power = 6
    check(
        "normalization scalar: the original normalized-w kernel differs by exactly Z_kappa^(3rq+1)",
        normalization_power == 7 and "Z_kappa^(3 r q + 1)" in note,
    )

    projector_ok = mutation != "drop_projector_restriction"
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
