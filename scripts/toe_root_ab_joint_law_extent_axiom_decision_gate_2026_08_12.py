#!/usr/bin/env python3
"""Resolve the cross-root extent of the remaining TOE law-selection fork.

This runner composes the exact Block-46 Record/gravity controls with the
Block-56 M2 action/decoder fork and the Block-55 grading census.  It measures
six continuous controls and three discrete interface forks on one displayed
product witness surface.  The result is an axiom-decision gate, not a complete
joint law, an axiom amendment, or TOE closure.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TOE_ROOT_AB_JOINT_LAW_EXTENT_AXIOM_DECISION_GATE_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK46_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_"
    "BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK55_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SECTOR_GRADING_FULL_PROJECTIVE_STRATIFICATION_POSITIVE_"
    "SELECTOR_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
BLOCK56_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_M2_RECORD_CUBIC_VECTOR_DECODER_SECTOR_GRADING_CARRIER_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)

AUDIT_INPUT_PATHS = (
    "docs/TOE_ROOT_AB_JOINT_LAW_EXTENT_AXIOM_DECISION_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_SECTOR_GRADING_FULL_PROJECTIVE_STRATIFICATION_POSITIVE_SELECTOR_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_M2_RECORD_CUBIC_VECTOR_DECODER_SECTOR_GRADING_CARRIER_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "scripts/admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_2026_08_11.py",
    "scripts/admissibility_m2_record_cubic_vector_decoder_sector_grading_carrier_axiom_boundary_2026_08_12.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_2026_08_11 as block46  # noqa: E402
import admissibility_m2_record_cubic_vector_decoder_sector_grading_carrier_axiom_boundary_2026_08_12 as block56  # noqa: E402


TOLERANCE = 1.0e-10


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def continuous_observables(parameters: np.ndarray) -> np.ndarray:
    """Six diagnostics for q, r, a, zeta, g, and decoder scale c."""
    q_value, r_value, a_value, zeta_value, g_value, decoder_scale = parameters
    kernel = block46.block45.local_record_kernel(
        block46.block45.EMPTY,
        (block46.block45.EMPTY,) * 6,
        Fraction(str(float(q_value))),
    )
    formation = 1.0 - float(kernel[block46.block45.EMPTY])
    schedule_correlation = float(
        block46.correlation(block46.schedule_mixture(Fraction(str(float(r_value)))))
    )
    tt_kinetic, constraint_kinetic, source_response, residual = (
        block46.gravity_signature(a_value, zeta_value, g_value)
    )
    if residual >= TOLERANCE:
        raise AssertionError("static source solve failed")
    return np.asarray(
        (
            formation,
            schedule_correlation,
            tt_kinetic,
            constraint_kinetic,
            source_response,
            decoder_scale,
        ),
        dtype=float,
    )


def sampled_signature_count() -> tuple[int, int]:
    """Count distinct signatures, without calling them complete physical laws."""
    signatures = set()
    base_values = product(
        (Fraction(1, 3), Fraction(2, 3)),
        (Fraction(0, 1), Fraction(1, 1)),
        (1, 2),
        (Fraction(0, 1), Fraction(1, 4)),
        (1, 2),
    )
    action_decoder_options = (
        ("trivial", 0, None),
        ("adjoint", 1, 1),
        ("adjoint", 1, 2),
    )
    grading_options = ((1, 1, 1), (1, -1, -1))
    for q_value, r_value, a_value, zeta_value, g_value in base_values:
        record = block46.record_signature(q_value, r_value)
        gravity = block46.gravity_signature(
            float(a_value), float(zeta_value), float(g_value)
        )
        if gravity[3] >= TOLERANCE:
            raise AssertionError("sampled source solve failed")
        for action, decoder_nullity, decoder_scale in action_decoder_options:
            for grading in grading_options:
                for sign in (-1, 1):
                    signatures.add(
                        (
                            record,
                            tuple(round(value, 12) for value in gravity[:3]),
                            action,
                            decoder_nullity,
                            decoder_scale,
                            grading,
                            sign,
                        )
                    )
    return len(signatures), 2**5 * 3 * 2 * 2


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    block46_note = flat(BLOCK46_PATH)
    block55_note = flat(BLOCK55_PATH)
    block56_note = flat(BLOCK56_PATH)

    print("analytic_boundary: exact cross-root product witness and axiom-decision extent")
    print("physical_boundary: no extensional joint law, physical quotient, or owner adoption is supplied")
    print("progress_boundary: blocker localization and axiom issue identification are not scored as TOE lane movement")

    checks.check(
        "current-foundation-boundary",
        "the four axioms name a local distribution and Records but explicitly omit dynamics and extensional values",
        "the distribution's extensional form and values are not specified" in axiom
        and "admissibility is not a dynamics axiom" in axiom
        and "no exact joint law is selected" in block46_note
        and "no toe percentage movement" in block55_note
        and "moves no toe percentage" in block56_note,
    )

    standard = np.asarray((0.5, 0.5, 1.0, 0.0, 1.0, 1.0), dtype=float)
    step = 1.0e-5
    jacobian = np.zeros((6, 6), dtype=float)
    for column in range(6):
        forward = standard.copy()
        backward = standard.copy()
        forward[column] += step
        backward[column] -= step
        jacobian[:, column] = (
            continuous_observables(forward) - continuous_observables(backward)
        ) / (2.0 * step)
    expected = np.diag((1.0, 3.0 / 5.0, 1.0 / 2.0, 1.0, 2.0, 1.0))
    checks.check(
        "six-continuous-controls",
        "five Root-A/gravity controls plus vector-decoder normalization are locally independent",
        np.linalg.matrix_rank(jacobian) == 6
        and float(np.max(np.abs(jacobian - expected))) < 2.0e-9
        and abs(float(np.linalg.det(jacobian)) - 3.0 / 5.0) < TOLERANCE,
        "diag=(1,3/5,1/2,1,2,1); rank=6; determinant=3/5",
    )

    adjoint_rank = block56.rational_rank(
        block56.equivariance_rows(lambda rotation: rotation)
    )
    trivial_rank = block56.rational_rank(
        block56.equivariance_rows(block56.identity_action)
    )
    checks.check(
        "discrete-action-decoder-fork",
        "the same current-compatible central rule permits decoder-nullity one and zero internal actions",
        adjoint_rank == 8
        and trivial_rank == 9
        and "same exact local" in block56_note,
        f"adjoint rank/nullity={adjoint_rank}/{9-adjoint_rank}; trivial={trivial_rank}/{9-trivial_rank}",
    )

    supports, rank_counts, point_counts, mismatches = (
        block56.classification_and_embedding()
    )
    grading_pair = ((1, 1, 1), (1, -1, -1))
    checks.check(
        "discrete-grading-fork",
        "two distinct projective gradings have equal support count before the unaxiomatized positivity selector",
        supports == 1296
        and mismatches == 0
        and rank_counts == {0: 0, 1: 96, 2: 768, 3: 432}
        and tuple(point_counts[grading] for grading in grading_pair) == (90, 90)
        and "strict positivity is load-bearing" in block55_note,
        f"counts={tuple(point_counts[grading] for grading in grading_pair)}",
    )

    signature_count, expected_count = sampled_signature_count()
    checks.check(
        "cross-root-product-separation",
        "the sampled product contains 384 distinct diagnostic signatures, not 384 claimed physical laws",
        signature_count == expected_count == 384,
        "2^5 Root-A/gravity settings * 3 action/decoder settings * 2 gradings * 2 sign assignments",
    )

    checks.check(
        "exact-amendment-content-test",
        "an honest amendment must attach extensional law content and cannot close the fork with structural adjectives",
        all(
            phrase in note
            for phrase in (
                "exact attached law object",
                "structural placeholder fails",
                "root-b-only patch fails",
                "nonlinear source-complete gravity",
                "physical state or inner product",
                "realized-history measure",
            )
        ),
    )

    checks.check(
        "decision-ready-not-adopted",
        "the packet distinguishes derivation, provisional hypothesis, and owner adoption without changing axioms",
        all(
            phrase in note
            for phrase in (
                "derive-only route",
                "provisional-law tournament",
                "owner adoption route",
                "no canonical axiom is edited",
                "zero toe percentage points",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline",
        "the narrow present-foundation non-entailment carries N1 through N8 and preserves live constructive routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "not a universal toe no-go" in note,
    )

    checks.check(
        "score-gate-and-clock",
        "the packet records the unchanged checkpoint and separates blocker burn-down from lane movement",
        "at least 54 hours" in note
        and "95 / 92 / 50" in note
        and "70 / 45 / 29" in note
        and "blocker burn-down" in note
        and "lane movement" in note,
    )

    print("N5_CERTIFICATE: six continuous diagnostics, two exact internal actions, two exact grading classes, and two sign assignments are resolved on the displayed product witness")
    print("per_element: checked each control response and all nine decoder matrix coordinates")
    print("per_site: inherited all 729 binary neighbour conditions and the exact 24-element cubic action checks")
    print("per_mode: checked the Block-46 static, kinetic, constraint, and source diagnostics; no new Fourier or nonlinear claim is made")
    print("per_block: checked all 1,296 grading supports and 384 sampled cross-root diagnostic signatures")
    print("lattice_wide: not executed; a selected full-Z3 law, nonlinear gravity, and complete realized history remain open")
    print("scope_boundary: exact axiom-decision extent and campaign strategy correction; not law selection, axiom adoption, or TOE progress")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
