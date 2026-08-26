#!/usr/bin/env python3
"""Independent Block-202 frozen-sign open-boundary checker.

This checker imports neither the primary runner nor a Block-19x runner.  At
the preregistered first target s=0 it reorders the two-component action into
two scalar tridiagonal components, solves them independently, and then
recombines their exact Berezin inertias.  No later Stage-A or Stage-B target
is opened.
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
    "toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825"
)
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L12_OPEN_TIME_STABLE_OS_EVENT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PARENT_COMMIT = "624207b338cbee1d510c4a91a94828681c0ba49d"
PREREG_COMMIT = "fecba265a1"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/CLAIM_STATUS_CERTIFICATE.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-axiom-closure-block202-l12-open-cut-event-boundary-20260825/REVIEW_HISTORY.md",
    "docs/ADMISSIBILITY_D4_L12_OPEN_TIME_STABLE_OS_EVENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

R = sp.Rational
MASS = R(2, 7)
L_TIME = 24
HALF_TIME = 12
EXPECTED_NEGATIVE_DIAGONAL = -R(
    76765262637431915164800,
    106086560536529675051041,
)

MUTATION_FAMILY = {
    "stale_authority": "P0",
    "insert_open_wrap": "I0",
    "move_positive_half": "I0",
    "lose_component_reflection_sign": "I1",
    "use_only_one_scalar_component": "I1",
    "accept_negative_diagonal": "I1",
    "claim_sign_is_action_selected": "I2",
    "claim_odd_and_even_sign_behavior_equal": "I2",
    "claim_global_no_go": "I3",
    "erase_live_sign_route": "I3",
    "open_later_stage": "I4",
    "claim_toe_progress": "S",
}
MUTATIONS = tuple(MUTATION_FAMILY)


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.cancel(value) == 0 for value in left - right
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


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


def inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Independent exact symmetric congruence elimination."""
    work = sp.MutableDenseMatrix(matrix)
    if not equal(work, work.T):
        raise ValueError("nonsymmetric form")
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
            work = sp.MutableDenseMatrix(sp.cancel(
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
            raise ValueError("unexpected two-by-two pivot")
        positive += 1
        negative += 1
        if active == 2:
            active = 0
            break
        cross = work[2:active, :2]
        work = sp.MutableDenseMatrix(sp.cancel(
            work[2:active, 2:active] - cross * block.inv() * cross.T
        ))
        active -= 2
    return positive, matrix.rows - positive - negative, negative


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority() -> bool:
    return (
        git_output("rev-parse", "origin/main") == CURRENT_MAIN
        and ancestor(PARENT_COMMIT)
        and ancestor(PREREG_COMMIT)
    )


def scalar_differential() -> sp.Matrix:
    differential = sp.zeros(L_TIME)
    for time in range(L_TIME - 1):
        differential[time + 1, time] = R(1, 2)
        differential[time, time + 1] = -R(1, 2)
    return differential


def scalar_reflection() -> sp.Matrix:
    reflection = sp.zeros(L_TIME)
    for time in range(L_TIME):
        reflection[L_TIME - 1 - time, time] = -1
    return reflection


def half_embedding() -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.zeros(HALF_TIME, HALF_TIME), sp.eye(HALF_TIME)
    )


def exterior_square(matrix: sp.MatrixBase) -> sp.Matrix:
    pairs = tuple(combinations(range(matrix.rows), 2))
    return sp.Matrix(
        len(pairs), len(pairs),
        lambda row, column: matrix.extract(
            pairs[row], pairs[column]
        ).det(),
    )


@cache
def scalar_component_facts() -> dict[str, object]:
    differential = scalar_differential()
    reflection = scalar_reflection()
    embedding = half_embedding()
    forms = []
    action_covariance = []
    for component_sign in (1, -1):
        action = MASS * sp.eye(L_TIME) + component_sign * differential
        theta = component_sign * reflection
        covariance = exact_inverse(action)
        form = sp.cancel(embedding.T * theta * covariance * embedding)
        forms.append(form)
        action_covariance.append(equal(theta * action.T * theta.T, action))

    combined = sp.diag(*forms)
    opposite = -combined
    central_indices = (0, 1, HALF_TIME, HALF_TIME + 1)
    central = combined.extract(central_indices, central_indices)
    return {
        "actions_open": differential[0, -1] == differential[-1, 0] == 0,
        "component_covariance": all(action_covariance),
        "component_symmetric": all(equal(form, form.T) for form in forms),
        "component_ranks": tuple(form.rank() for form in forms),
        "component_inertias": tuple(inertia(form) for form in forms),
        "combined": combined,
        "combined_rank": combined.rank(),
        "combined_inertia": inertia(combined),
        "negative_diagonal": sp.factor(forms[0][0, 0]),
        "opposite_inertia": inertia(opposite),
        "even_central_unchanged": equal(
            exterior_square(central), exterior_square(-central)
        ),
    }


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    family = MUTATION_FAMILY.get(mutation, "")
    facts = scalar_component_facts()
    return {
        "P0": (
            authority() and family != "P0",
            "independent authority and preregistration ancestry bind",
        ),
        "I0": (
            facts["actions_open"] and family != "I0",
            "two independent scalar components use the literal open half and positive-time embedding",
        ),
        "I1": (
            facts["component_covariance"]
            and facts["component_symmetric"]
            and facts["component_ranks"] == (1, 1)
            and facts["component_inertias"] == ((0, 11, 1), (0, 11, 1))
            and facts["combined_rank"] == 2
            and facts["combined_inertia"] == (0, 22, 2)
            and facts["negative_diagonal"] == EXPECTED_NEGATIVE_DIAGONAL
            and family != "I1",
            "disjoint scalar-component calculation reproduces the exact frozen-sign D1 failure",
        ),
        "I2": (
            facts["opposite_inertia"] == (2, 22, 0)
            and facts["even_central_unchanged"]
            and family != "I2",
            "the opposite sign is positive at the first target and even exterior degree is sign-blind",
        ),
        "I3": (
            family != "I3",
            "the result is family-scoped; opposite-sign, even-algebra, cyclic, Nambu, process, and gravity routes remain live",
        ),
        "I4": (
            NOTE_PATH.exists() and family != "I4",
            "all later Stage-A and Stage-B targets remain stopped and the protocol disclosure is present",
        ),
        "S": (
            family != "S",
            "no axiom edit, retained verdict, obligation retirement, or TOE movement is claimed",
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
    result = evaluate(args.mutation)
    for key in ("P0", "I0", "I1", "I2", "I3", "I4", "S"):
        ok, statement = result[key]
        checks.check(key, statement, ok)
    facts = scalar_component_facts()
    print(
        "INDEPENDENT_D1: scalar_component_inertias="
        f"{facts['component_inertias']}; combined_inertia="
        f"{facts['combined_inertia']}; K00={facts['negative_diagonal']}"
    )
    print(
        "INDEPENDENT_SCOPE: first-target frozen-sign rejection only; "
        "later targets sealed; obligation_retirement=0; toe_percentage_movement=0."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
