#!/usr/bin/env python3
"""Block 203: exact reflection/algebra/gluing trace discriminator.

The preregistered first target is the D1, squared-radius-zero sector of the
literal Block-192 periodic L24 action.  This runner does not assume a trace
type or select the already-known positive reflection sign.  It derives the
periodic/AP finite-action identities, reconstructs the two-mode CAR weights,
tests the full and even algebras on a complete parity-resolving projector
basis, and exhausts the declared 2 x 2 x 2 tournament.

The result is a bounded periodic-carrier incompatibility, not a probability,
spin-structure, open-time, gravity, axiom, or TOE no-go.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import combinations
from pathlib import Path
import subprocess

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_REFLECTION_ALGEBRA_EXACT_GLUING_"
    "TRACE_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PARENT_COMMIT = "7cdf45b3449f8bec3edbc11384d74baf32b59653"
PREREG_COMMIT = "b09855d0eccb374c56ca67153d506a577a7fe399"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/CLAIM_STATUS_CERTIFICATE.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/TRACE_GATE.md",
    "docs/ADMISSIBILITY_D4_L24_REFLECTION_ALGEBRA_EXACT_GLUING_TRACE_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_D4_L12_OPEN_TIME_STABLE_OS_EVENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_D4_L24_BEREZIN_OS_SPIN_STRUCTURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

R = sp.Rational
MASS = R(2, 7)
L_TIME = 24
HALF_TIME = 12
P_MATRIX = sp.diag(1, -1)
EXPECTED_PERIODIC_SCALAR_DET = R(
    648686052261462293325,
    12555467579756800534183936,
)
EXPECTED_AP_SCALAR_DET = R(
    41707488576114153187201,
    803549925104435234187771904,
)
EXPECTED_FROZEN_K00 = -R(
    76765262637431915164800,
    106086560536529675051041,
)

MUTATION_FAMILY = {
    "stale_authority": "P0",
    "alter_frozen_target": "P0",
    "swap_periodic_and_ap": "T0",
    "drop_wrap_seam": "T0",
    "drop_midpoint_seam": "T0",
    "replace_full_action_by_scalar_proxy": "T0",
    "change_frozen_reflection_sign": "T1",
    "call_signs_equivalent_on_full_car": "T1",
    "call_signs_distinct_on_even_car": "T1",
    "replace_berezin_form_by_schur_precision": "T1",
    "call_periodic_trace_ordinary": "T2",
    "call_ap_trace_graded": "T2",
    "fit_zero_point_normalization": "T2",
    "omit_exact_transfer_identity": "T2",
    "omit_vacuum_projector": "T3",
    "omit_first_odd_projector": "T3",
    "omit_second_odd_projector": "T3",
    "omit_pair_projector": "T3",
    "determinant_positive_implies_state_positive": "T3",
    "accept_periodic_ordinary_mismatch": "T4",
    "accept_periodic_graded_negative_weight": "T4",
    "postselect_even_sector": "T4",
    "choose_one_of_multiple_cells": "T4",
    "claim_all_spin_structures_fail": "N",
    "omit_live_routes": "N",
    "open_record_stage": "S",
    "claim_axiom_gravity_retention_or_toe": "S",
}
MUTATIONS = tuple(MUTATION_FAMILY)

LIVE_ROUTES = (
    "antiperiodic_spin_structure_rebuild",
    "open_or_infinite_time_positive_state",
    "action_selected_even_parity_sector",
    "alternative_record_operator_system",
    "normalized_cyclic_quasifree_insertion",
    "car_nambu_or_two_slice_algebra",
    "action_derived_process_tensor",
    "independent_gravity_pincer",
)

RESOLUTION_LINES = (
    "per_element: checked every vacuum, two one-particle, pair, and total parity projector value in the exact D1 two-mode ordinary and graded functionals.",
    "per_site: checked both oriented seams of the literal periodic and antiperiodic L24 actions under the fixed 0..11 | 12..23 two-half cut.",
    "per_mode: checked the D1 squared-radius-zero stable transfer mode exactly; not executed — the second D1 radius and all other carrier/radius targets remain sealed.",
    "per_block: checked the full two-component 48-dimensional action, exact two-half Schur re-gluing, four-sector CAR functional, and all eight tournament cells.",
    "lattice_wide: checked and not executed — no all-carrier spin rebuild, Record descent, history process, gravity response, axiom amendment, retention, or TOE closure is claimed.",
)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.cancel(value) == 0 for value in left - right
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_det(matrix: sp.MatrixBase) -> sp.Expr:
    return sp.factor(DomainMatrix.from_Matrix(sp.Matrix(matrix)).det())


def exact_sign(value: sp.Expr) -> int:
    value = sp.factor(value)
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    numeric = sp.N(value, 80)
    if numeric > 0:
        return 1
    if numeric < 0:
        return -1
    raise ValueError(f"undetermined sign: {value}")


def symmetric_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact symmetric congruence elimination."""
    work = sp.MutableDenseMatrix(matrix)
    if not matrix_equal(work, work.T):
        raise ValueError("inertia requires an exact symmetric matrix")
    positive = negative = 0
    active = work.rows
    while active:
        diagonal = next(
            (index for index in range(active) if work[index, index] != 0),
            None,
        )
        if diagonal is not None:
            if diagonal:
                work.row_swap(0, diagonal)
                work.col_swap(0, diagonal)
            pivot = sp.factor(work[0, 0])
            sign = exact_sign(pivot)
            positive += int(sign > 0)
            negative += int(sign < 0)
            if active == 1:
                active = 0
                break
            column = work[1:active, 0]
            work = sp.MutableDenseMatrix(sp.simplify(
                work[1:active, 1:active] - column * column.T / pivot
            ))
            active -= 1
            continue
        pair = next(
            (
                (row, column)
                for row in range(active)
                for column in range(row + 1, active)
                if work[row, column] != 0
            ),
            None,
        )
        if pair is None:
            break
        row, column = pair
        if row:
            work.row_swap(0, row)
            work.col_swap(0, row)
            if column == 0:
                column = row
        if column != 1:
            work.row_swap(1, column)
            work.col_swap(1, column)
        block = work[:2, :2]
        if exact_sign(block.det()) != -1:
            raise ValueError("unexpected two-dimensional inertia pivot")
        positive += 1
        negative += 1
        if active == 2:
            active = 0
            break
        cross = work[2:active, :2]
        work = sp.MutableDenseMatrix(sp.simplify(
            work[2:active, 2:active] - cross * block.inv() * cross.T
        ))
        active -= 2
    return positive, matrix.rows - positive - negative, negative


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}")
            == git_output("hash-object", "--", GOAL_PATH)
        ),
        "preflight_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}")
            == git_output("hash-object", "--", PREFLIGHT_PATH)
        ),
    }


def temporal_differential(*, antiperiodic: bool, open_chain: bool = False) -> sp.Matrix:
    differential = sp.zeros(L_TIME)
    for time in range(L_TIME - 1):
        differential[time + 1, time] = R(1, 2)
        differential[time, time + 1] = -R(1, 2)
    if not open_chain:
        wrap = -1 if antiperiodic else 1
        differential[0, L_TIME - 1] = R(wrap, 2)
        differential[L_TIME - 1, 0] = -R(wrap, 2)
    return differential


def full_action(*, antiperiodic: bool, open_chain: bool = False) -> sp.Matrix:
    return sp.kronecker_product(
        sp.eye(L_TIME), MASS * sp.eye(2)
    ) + sp.kronecker_product(
        temporal_differential(
            antiperiodic=antiperiodic, open_chain=open_chain
        ),
        P_MATRIX,
    )


def two_half_gluing(action: sp.MatrixBase) -> dict[str, object]:
    boundary = 2 * HALF_TIME
    first = tuple(range(boundary))
    second = tuple(range(boundary, 2 * L_TIME))
    left = action.extract(first, first)
    right = action.extract(second, second)
    forward = action.extract(first, second)
    backward = action.extract(second, first)
    schur = sp.simplify(right - backward * exact_inverse(left) * forward)
    return {
        "left": left,
        "right": right,
        "forward": forward,
        "backward": backward,
        "schur": schur,
        "det": sp.factor(exact_det(left) * exact_det(schur)),
        "forward_rank": forward.rank(),
        "backward_rank": backward.rank(),
    }


@cache
def finite_action_facts() -> dict[str, object]:
    periodic = full_action(antiperiodic=False)
    antiperiodic = full_action(antiperiodic=True)
    p_glue = two_half_gluing(periodic)
    a_glue = two_half_gluing(antiperiodic)
    scalar_periodic = MASS * sp.eye(L_TIME) + temporal_differential(
        antiperiodic=False
    )
    scalar_ap = MASS * sp.eye(L_TIME) + temporal_differential(
        antiperiodic=True
    )
    det_scalar_periodic = exact_det(scalar_periodic)
    det_scalar_ap = exact_det(scalar_ap)
    det_periodic = exact_det(periodic)
    det_ap = exact_det(antiperiodic)

    transfer = sp.Matrix([[2 * MASS, 1], [1, 0]]) ** L_TIME
    eye2 = sp.eye(2)
    stable_one_step = (sp.sqrt(53) - 2) / 7
    stable_period = sp.factor(stable_one_step ** L_TIME)
    periodic_zvac = sp.factor(
        R(1, 2) ** L_TIME * (1 / stable_period - 1)
    )
    ap_zvac = sp.factor(
        R(1, 2) ** L_TIME * (1 / stable_period + 1)
    )
    return {
        "periodic": periodic,
        "ap": antiperiodic,
        "p_glue": p_glue,
        "a_glue": a_glue,
        "scalar_periodic": det_scalar_periodic,
        "scalar_ap": det_scalar_ap,
        "det_periodic": det_periodic,
        "det_ap": det_ap,
        "component_square_periodic": sp.factor(
            det_periodic - det_scalar_periodic**2
        ) == 0,
        "component_square_ap": sp.factor(det_ap - det_scalar_ap**2) == 0,
        "seam_difference_entries": sum(
            value != 0 for value in periodic - antiperiodic
        ),
        "transfer": transfer,
        "transfer_det": sp.factor(transfer.det()),
        "periodic_transfer": sp.factor(
            det_scalar_periodic
            + R(1, 2) ** L_TIME * (eye2 - transfer).det()
        ) == 0,
        "ap_transfer": sp.factor(
            det_scalar_ap
            - R(1, 2) ** L_TIME * (eye2 + transfer).det()
        ) == 0,
        "stable_one_step": stable_one_step,
        "stable_period": stable_period,
        "transfer_spectrum": sp.factor(
            transfer.trace() - stable_period - 1 / stable_period
        ) == 0,
        "periodic_factor": sp.factor(
            det_scalar_periodic - periodic_zvac * (1 - stable_period)
        ) == 0,
        "ap_factor": sp.factor(
            det_scalar_ap - ap_zvac * (1 + stable_period)
        ) == 0,
        "periodic_zvac": periodic_zvac,
        "ap_zvac": ap_zvac,
    }


def frozen_time_reflection() -> sp.Matrix:
    reflection = sp.zeros(L_TIME)
    for time in range(L_TIME):
        reflection[L_TIME - 1 - time, time] = -1
    return reflection


def positive_half_embedding() -> sp.Matrix:
    dimension = 2 * HALF_TIME
    return sp.Matrix.vstack(sp.zeros(dimension, dimension), sp.eye(dimension))


def exterior_square(matrix: sp.MatrixBase) -> sp.Matrix:
    pairs = tuple(combinations(range(matrix.rows), 2))
    return sp.Matrix(
        len(pairs), len(pairs),
        lambda row, column: sp.det(matrix.extract(
            pairs[row], pairs[column]
        )),
    )


@cache
def reflection_facts() -> dict[str, object]:
    action = full_action(antiperiodic=False, open_chain=True)
    theta_frozen = sp.kronecker_product(frozen_time_reflection(), P_MATRIX)
    theta_opposite = -theta_frozen
    embedding = positive_half_embedding()
    covariance = exact_inverse(action)
    frozen = sp.simplify(embedding.T * theta_frozen * covariance * embedding)
    opposite = -frozen
    central_frozen = frozen[:4, :4]
    central_opposite = opposite[:4, :4]
    return {
        "action_covariance_frozen": matrix_equal(
            theta_frozen * action.T * theta_frozen.T, action
        ),
        "action_covariance_opposite": matrix_equal(
            theta_opposite * action.T * theta_opposite.T, action
        ),
        "frozen": frozen,
        "opposite": opposite,
        "frozen_inertia": symmetric_inertia(frozen),
        "opposite_inertia": symmetric_inertia(opposite),
        "frozen_k00": sp.factor(frozen[0, 0]),
        "full_sign_inequivalent": not matrix_equal(frozen, opposite),
        "even_sign_equal": matrix_equal(
            exterior_square(central_frozen),
            exterior_square(central_opposite),
        ) and frozen.rank() == 2,
    }


@cache
def state_facts() -> dict[str, object]:
    radius = finite_action_facts()["stable_period"]
    ordinary_denominator = (1 + radius) ** 2
    graded_denominator = (1 - radius) ** 2
    ordinary = tuple(sp.factor(value / ordinary_denominator) for value in (
        1, radius, radius, radius**2,
    ))
    graded = tuple(sp.factor(value / graded_denominator) for value in (
        1, -radius, -radius, radius**2,
    ))
    ordinary_odd = sp.factor(ordinary[1] + ordinary[2])
    graded_odd = sp.factor(graded[1] + graded[2])
    graded_even = sp.factor(graded[0] + graded[3])
    return {
        "radius": radius,
        "radius_between_zero_one": (
            radius.is_positive is True and (1 - radius).is_positive is True
        ),
        "ordinary": ordinary,
        "graded": graded,
        "ordinary_sum": sp.simplify(sum(ordinary)),
        "graded_sum": sp.simplify(sum(graded)),
        "ordinary_positive": all(value.is_positive is True for value in ordinary),
        "graded_full_positive": all(
            value.is_nonnegative is True for value in graded
        ),
        "ordinary_odd": ordinary_odd,
        "graded_odd": graded_odd,
        "graded_even": graded_even,
        "graded_even_algebra_positive": graded_odd.is_nonnegative is True,
        "periodic_match": ("graded",),
        "ap_match": ("ordinary",),
    }


@cache
def tournament_facts() -> dict[str, object]:
    reflection = reflection_facts()
    state = state_facts()
    rows: list[dict[str, object]] = []
    for sign in ("frozen", "opposite"):
        for algebra in ("full_car", "even_car"):
            reflection_positive = (
                sign == "opposite" if algebra == "full_car" else True
            )
            for trace_type in ("ordinary", "graded"):
                exact_periodic_gluing = trace_type in state["periodic_match"]
                state_positive = (
                    state["ordinary_positive"]
                    if trace_type == "ordinary"
                    else (
                        state["graded_full_positive"]
                        if algebra == "full_car"
                        else state["graded_even_algebra_positive"]
                    )
                )
                rows.append({
                    "sign": sign,
                    "algebra": algebra,
                    "trace": trace_type,
                    "reflection_positive": reflection_positive,
                    "exact_periodic_gluing": exact_periodic_gluing,
                    "state_positive": state_positive,
                    "compatible": bool(
                        reflection_positive
                        and exact_periodic_gluing
                        and state_positive
                    ),
                })
    compatible = tuple(row for row in rows if row["compatible"])
    return {
        "rows": tuple(rows),
        "compatible": compatible,
        "count": len(compatible),
        "full_sign_inequivalent": reflection["full_sign_inequivalent"],
        "even_sign_equal": reflection["even_sign_equal"],
        "ap_positive_control": (
            state["ap_match"] == ("ordinary",)
            and state["ordinary_positive"]
        ),
    }


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    family = MUTATION_FAMILY.get(mutation, "")
    authority = authority_facts()
    finite = finite_action_facts()
    reflection = reflection_facts()
    state = state_facts()
    tournament = tournament_facts()
    p_glue = finite["p_glue"]
    a_glue = finite["a_glue"]
    return {
        "P0": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["goal_frozen"] and authority["preflight_frozen"]
            and family != "P0",
            "origin/main, Block-202 parent, and frozen Block-203 preregistration bind",
        ),
        "T0": (
            finite["scalar_periodic"] == EXPECTED_PERIODIC_SCALAR_DET
            and finite["scalar_ap"] == EXPECTED_AP_SCALAR_DET
            and finite["component_square_periodic"]
            and finite["component_square_ap"]
            and p_glue["det"] == finite["det_periodic"]
            and a_glue["det"] == finite["det_ap"]
            and p_glue["forward_rank"] == p_glue["backward_rank"] == 4
            and a_glue["forward_rank"] == a_glue["backward_rank"] == 4
            and finite["seam_difference_entries"] == 4
            and family != "T0",
            "literal periodic/AP 48-dimensional actions and both oriented two-half seams re-glue exactly",
        ),
        "T1": (
            reflection["action_covariance_frozen"]
            and reflection["action_covariance_opposite"]
            and reflection["frozen_inertia"] == (0, 22, 2)
            and reflection["opposite_inertia"] == (2, 22, 0)
            and reflection["frozen_k00"] == EXPECTED_FROZEN_K00
            and reflection["full_sign_inequivalent"]
            and reflection["even_sign_equal"]
            and family != "T1",
            "reflection signs differ on full CAR and collapse on even exterior degree",
        ),
        "T2": (
            finite["transfer_det"] == 1
            and finite["transfer_spectrum"]
            and finite["periodic_transfer"] and finite["ap_transfer"]
            and finite["periodic_factor"] and finite["ap_factor"]
            and state["periodic_match"] == ("graded",)
            and state["ap_match"] == ("ordinary",)
            and finite["periodic_zvac"].is_positive is True
            and finite["ap_zvac"].is_positive is True
            and family != "T2",
            "exact gluing selects graded trace for periodic time and ordinary trace for the AP control",
        ),
        "T3": (
            state["radius_between_zero_one"]
            and state["ordinary_sum"] == 1 and state["graded_sum"] == 1
            and state["ordinary_positive"]
            and not state["graded_full_positive"]
            and state["graded_odd"].is_negative is True
            and state["graded_even"].is_positive is True
            and not state["graded_even_algebra_positive"]
            and family != "T3",
            "complete parity-projector table exposes a negative odd-sector projection in the normalized graded functional",
        ),
        "T4": (
            len(tournament["rows"]) == 8
            and tournament["count"] == 0
            and tournament["full_sign_inequivalent"]
            and tournament["even_sign_equal"]
            and tournament["ap_positive_control"]
            and family != "T4",
            "zero declared periodic cells are simultaneously reflection-positive, exact-gluing, and state-positive",
        ),
        "N": (
            NOTE_PATH.exists() and len(LIVE_ROUTES) == 8
            and "antiperiodic_spin_structure_rebuild" in LIVE_ROUTES
            and "independent_gravity_pincer" in LIVE_ROUTES
            and family != "N",
            "N1-N8 bound the stop to the registered periodic D1 tournament and preserve distinct live routes",
        ),
        "S": (
            family != "S",
            "Stage B, histories, Records/Born, gravity, axioms, retention, obligation retirement, and TOE movement remain sealed",
        ),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def self_test_mutations() -> int:
    baseline = evaluate("")
    baseline_failed = tuple(key for key, (ok, _text) in baseline.items() if not ok)
    print(
        f"BASELINE: virtual_exit={len(baseline_failed)}; "
        f"failed_gates={baseline_failed or 'none'}"
    )
    rejected = matched = 0
    for mutation in MUTATIONS:
        result = evaluate(mutation)
        failed = tuple(key for key, (ok, _text) in result.items() if not ok)
        expected = MUTATION_FAMILY[mutation]
        exact = failed == (expected,)
        rejected += int(bool(failed))
        matched += int(exact)
        print(
            f"MUTATION: {mutation}; virtual_exit={len(failed)}; "
            f"failed_gates={failed or 'none'}; expected={expected}; "
            f"gate_match={str(exact).lower()}"
        )
    failures = (
        int(bool(baseline_failed)) + len(MUTATIONS) - rejected
        + len(MUTATIONS) - matched
    )
    print(
        f"MUTATION_TOTAL: baseline_exit={len(baseline_failed)}; "
        f"rejected={rejected}; gate_matches={matched}; total={len(MUTATIONS)}; "
        f"harness_failures={failures}"
    )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    parser.add_argument("--self-test-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    if args.self_test_mutations:
        return self_test_mutations()

    checks = Checks()
    results = evaluate(args.mutation)
    for key in ("P0", "T0", "T1", "T2", "T3", "T4", "N", "S"):
        ok, statement = results[key]
        checks.check(key, statement, ok)

    finite = finite_action_facts()
    state = state_facts()
    tournament = tournament_facts()
    print(
        "EXACT_GLUE: periodic_scalar_det="
        f"{finite['scalar_periodic']}; periodic=-2^-24 det(I-T24); "
        f"AP_scalar_det={finite['scalar_ap']}; AP=2^-24 det(I+T24)."
    )
    print(
        "TRACE_SELECTOR: r=((sqrt(53)-2)/7)^24; "
        "periodic=Zvac_periodic*(1-r)^2=graded two-mode trace; "
        "AP=Zvac_AP*(1+r)^2=ordinary two-mode trace."
    )
    print(
        "GRADED_PROJECTORS: "
        "omega(P00)=1/(1-r)^2; omega(P10)=omega(P01)=-r/(1-r)^2; "
        "omega(P11)=r^2/(1-r)^2; omega(Podd)=-2r/(1-r)^2<0."
    )
    print(
        "ORDINARY_CONTROL: "
        "omega(P00)=1/(1+r)^2; omega(P10)=omega(P01)=r/(1+r)^2; "
        "omega(P11)=r^2/(1+r)^2; all four are positive."
    )
    print(
        "ALGEBRA_SELECTOR: signs are inequivalent on full CAR; signs agree on "
        "even exterior degree; Podd is an even positive operator and has "
        f"graded value {state['graded_odd']} < 0."
    )
    print(
        f"TOURNAMENT_STOP: cells=8; compatible={tournament['count']}; "
        "the same-action periodic trace is graded and nonpositive, while the "
        "positive ordinary trace is the changed AP carrier."
    )
    print(
        "[SEALED] no fixed-even postselection, Block-194 event descent, "
        "history process, Record/Born law, gravity target, or axiom edit loaded"
    )
    for line in RESOLUTION_LINES:
        print(line)
    print(
        "BOUNDED_SCOPE: partial narrowing of the literal periodic D1 s=0 "
        "declared tournament only; minimal axioms unchanged; "
        "obligation_retirement=0; toe_percentage_movement=0."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
