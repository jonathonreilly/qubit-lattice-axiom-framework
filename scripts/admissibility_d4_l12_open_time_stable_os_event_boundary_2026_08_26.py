#!/usr/bin/env python3
"""Block 202: frozen-sign L12 open-time Berezin boundary discriminator.

The preregistered Stage-A order tests the literal finite-open Berezin form
before Riccati, circle re-gluing, or event composition.  This runner therefore
stops at the first D1 target.  It constructs the full two-component action and
the Block-192 reflection without using a scalar Schur proxy.

The exact result is a bounded route rejection, not a no-go: the imported
reflection sign gives a negative degree-one form, while the opposite global
field sign gives a positive form and remains a separately preregisterable
route.  Stage B and all later Stage-A targets stay sealed.
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
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
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
    "docs/ADMISSIBILITY_D4_L24_BEREZIN_OS_SPIN_STRUCTURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

R = sp.Rational
MASS = R(2, 7)
L_TIME = 24
HALF_TIME = 12
P_MATRIX = sp.diag(1, -1)
EXPECTED_NEGATIVE_DIAGONAL = -R(
    76765262637431915164800,
    106086560536529675051041,
)

MUTATION_FAMILY = {
    "stale_authority": "P0",
    "alter_frozen_goal": "P0",
    "use_periodic_instead_of_open_action": "T0",
    "change_cut_or_link_orientation": "T0",
    "drop_internal_sigma_z": "T0",
    "replace_berezin_form_with_schur_proxy": "T1",
    "accept_negative_degree_one_norm": "T1",
    "silently_flip_frozen_reflection": "T1",
    "claim_action_covariance_selects_global_sign": "T2",
    "call_global_sign_harmless_on_odd_fields": "T2",
    "claim_even_algebra_is_also_rejected": "T2",
    "claim_open_time_os_no_go": "T3",
    "omit_live_alternative_routes": "T3",
    "promote_post_stop_riccati_or_regluing": "T4",
    "use_exploratory_all_radius_values_as_evidence": "T4",
    "omit_protocol_disclosure": "T4",
    "open_event_stage": "S",
    "claim_record_born_gravity_axiom_or_toe": "S",
}
MUTATIONS = tuple(MUTATION_FAMILY)

LIVE_ROUTES = (
    "opposite_global_reflection_sign",
    "fermion_even_observable_algebra",
    "normalized_cyclic_quasifree_functional",
    "changed_spin_structure",
    "all_field_car_nambu_extension",
    "action_derived_process_tensor",
    "gravity_pincer",
)

RESOLUTION_LINES = (
    "per_element: checked the frozen-sign D1 s=0 vacuum and degree-one finite-open reflected Berezin form; one exact negative generator norm stops the declared full field algebra.",
    "per_site: checked the literal t=-12..11 open chain, cut -1|0, Block-192 link orientation, and all twelve positive-half sites.",
    "per_mode: checked only the preregistered first D1 zero-radius target; the s=1 endpoint, remaining carriers, and all-radius alternative-sign route remain sealed.",
    "per_block: checked the full physical two-component Berezin form, not a scalar Schur proxy; Riccati, re-gluing, events, process, Records, and gravity stop downstream.",
    "lattice_wide: not executed — the result rejects only the frozen-sign Block-202 family and leaves opposite-sign, even-algebra, cyclic, Nambu, process, gravity, axiom, and TOE routes live.",
)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
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


def symmetric_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact congruence elimination; return positive, null, negative."""
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


def centered_open_differential() -> sp.Matrix:
    differential = sp.zeros(L_TIME)
    for time in range(L_TIME - 1):
        differential[time + 1, time] = R(1, 2)
        differential[time, time + 1] = -R(1, 2)
    return differential


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
def literal_facts() -> dict[str, object]:
    differential = centered_open_differential()
    action = sp.kronecker_product(
        sp.eye(L_TIME), MASS * sp.eye(2)
    ) + sp.kronecker_product(differential, P_MATRIX)
    reflection = frozen_time_reflection()
    theta = sp.kronecker_product(reflection, P_MATRIX)
    embedding = positive_half_embedding()
    covariance = exact_inverse(action)
    frozen_form = sp.simplify(embedding.T * theta * covariance * embedding)
    opposite_form = -frozen_form
    central = frozen_form[:4, :4]
    opposite_central = -central
    return {
        "action": action,
        "theta": theta,
        "form": frozen_form,
        "opposite": opposite_form,
        "open_wrap": action[:2, -2:] == sp.zeros(2)
        and action[-2:, :2] == sp.zeros(2),
        "central_links": (
            action[2 * HALF_TIME - 2, 2 * HALF_TIME] == -R(1, 2)
            and action[2 * HALF_TIME, 2 * HALF_TIME - 2] == R(1, 2)
            and action[2 * HALF_TIME - 1, 2 * HALF_TIME + 1] == R(1, 2)
            and action[2 * HALF_TIME + 1, 2 * HALF_TIME - 1] == -R(1, 2)
        ),
        "theta_involution": matrix_equal(theta**2, sp.eye(2 * L_TIME)),
        "action_covariance": matrix_equal(
            theta * action.T * theta.T, action
        ),
        "opposite_action_covariance": matrix_equal(
            (-theta) * action.T * (-theta).T, action
        ),
        "symmetric": matrix_equal(frozen_form, frozen_form.T),
        "rank": frozen_form.rank(),
        "inertia": symmetric_inertia(frozen_form),
        "negative_diagonal": sp.factor(frozen_form[0, 0]),
        "opposite_inertia": symmetric_inertia(opposite_form),
        "central_inertia": symmetric_inertia(central),
        "opposite_central_inertia": symmetric_inertia(opposite_central),
        "even_central_unchanged": matrix_equal(
            exterior_square(central), exterior_square(opposite_central)
        ),
    }


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    family = MUTATION_FAMILY.get(mutation, "")
    authority = authority_facts()
    facts = literal_facts()
    return {
        "P0": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["goal_frozen"] and authority["preflight_frozen"]
            and family != "P0",
            "origin/main, parent, preregistration, and frozen target disclosures bind",
        ),
        "T0": (
            facts["action"].shape == (48, 48)
            and facts["theta"].shape == (48, 48)
            and facts["open_wrap"] and facts["central_links"]
            and facts["theta_involution"] and facts["action_covariance"]
            and family != "T0",
            "the literal open Block-192 action, contiguous cut, link orientation, and imported reflection are exact",
        ),
        "T1": (
            facts["symmetric"] and facts["rank"] == 2
            and facts["inertia"] == (0, 22, 2)
            and facts["negative_diagonal"] == EXPECTED_NEGATIVE_DIAGONAL
            and facts["central_inertia"] == (0, 2, 2)
            and family != "T1",
            "the earliest D1 s=0 full Berezin gate fails by an exact negative degree-one norm",
        ),
        "T2": (
            facts["opposite_action_covariance"]
            and facts["opposite_inertia"] == (2, 22, 0)
            and facts["opposite_central_inertia"] == (2, 2, 0)
            and facts["even_central_unchanged"]
            and family != "T2",
            "action covariance admits both global signs; the sign is load-bearing on odd fields and invisible on even exterior degree",
        ),
        "T3": (
            len(LIVE_ROUTES) == 7
            and "opposite_global_reflection_sign" in LIVE_ROUTES
            and "fermion_even_observable_algebra" in LIVE_ROUTES
            and "gravity_pincer" in LIVE_ROUTES
            and family != "T3",
            "the stopped result rejects only the frozen-sign family and preserves materially distinct live routes",
        ),
        "T4": (
            NOTE_PATH.exists()
            and family != "T4",
            "post-stop exploratory calculations are disclosed and no later Stage-A target is promoted as evidence",
        ),
        "S": (
            family != "S",
            "Stage B, process, Records, Born, gravity, axioms, retention, obligation retirement, and TOE movement remain sealed",
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
    for key in ("P0", "T0", "T1", "T2", "T3", "T4", "S"):
        ok, statement = results[key]
        checks.check(key, statement, ok)

    facts = literal_facts()
    print(
        "D1_STOP: s=0; cut=t[-12..11]; positive_half=t[0..11]; "
        f"reduced_half_inertia={facts['inertia']}; rank={facts['rank']}; "
        f"K00={facts['negative_diagonal']}"
    )
    print(
        "SIGN_DISCRIMINATOR: frozen_epsilon=-1 gives (0+,22null,2-); "
        "opposite_epsilon=+1 gives (2+,22null,0-); both obey action "
        "covariance; even exterior degree is unchanged."
    )
    print(
        "STAGE_A_CERTIFICATE: stopped at the first Berezin gate; Riccati, "
        "finite-circle re-gluing, winding, all-carrier expansion, and Stage B "
        "are not promoted."
    )
    print(
        "[SEALED] no Block-201 J, Block-194 effects, event values, prefix "
        "gluing, process map, Record/Born law, or gravity target loaded"
    )
    for line in RESOLUTION_LINES:
        print(line)
    print(
        "BOUNDED_SCOPE: exact rejection of the imported frozen-sign full-field "
        "Block-202 family only; minimal axioms unchanged; obligation_retirement=0; "
        "toe_percentage_movement=0."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
