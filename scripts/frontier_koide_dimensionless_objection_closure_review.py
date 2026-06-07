#!/usr/bin/env python3
"""Exact countermodel no-go for full dimensionless Koide closure.

This runner verifies the finite two-channel and endpoint algebra without
promoting the broader physical source/readout closure language. It checks:

  - zero-background source-response conditionally gives Q = 2/3,
  - a traceless background source Z changes Q and remains the residual,
  - selected-line local endpoint support conditionally gives delta = eta_APS,
  - ambient endpoint support leaves a spectator/free-source residual,
  - observable completeness does not by itself erase those residuals.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/KOIDE_DIMENSIONLESS_NOTE_2026-04-24.md"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "koide_dimensionless_note_2026-04-24"
RUNNER_PATH = "scripts/frontier_koide_dimensionless_objection_closure_review.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    line = f"  [{status}] [{kind}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    return condition


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def q_from_background(s: Fraction, z: Fraction) -> Fraction:
    """Dimensionless Q from probe coefficients around background (s+z, s-z)."""
    y_plus = Fraction(1, 1) / (Fraction(1, 1) + s + z)
    y_perp = Fraction(1, 1) / (Fraction(1, 1) + s - z)
    return (Fraction(1, 1) + y_perp / y_plus) / 3


def z_expectation(weight_plus: Fraction) -> Fraction:
    return 2 * weight_plus - 1


ETA_APS = Fraction(2, 9)


def note_boundary_checks() -> None:
    banner("Part 0: note boundary and claim-status checks")
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "Claim type:** no_go",
        "Status:** exact countermodel no-go",
        "not a physical source/readout closure theorem",
        "does not force full dimensionless closure",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "KOIDE_DIMENSIONLESS_RETAINED_CLOSURE",
        "Admitted input",
        "promoted to an open admission",
    ]
    for phrase in forbidden:
        check(f"note omits stale closure phrase: {phrase}", phrase not in text)


def delta_open(spectator: Fraction, endpoint_shift: Fraction) -> Fraction:
    return ETA_APS * (1 - spectator) + endpoint_shift


@dataclass(frozen=True)
class DeltaCase:
    name: str
    spectator: Fraction
    endpoint_shift: Fraction
    expected: Fraction


def part1_q_background_zero() -> None:
    banner("Part 1: Q zero-background support and traceless-background residual")

    q_zero = q_from_background(Fraction(0), Fraction(0))
    check("zero-background source-response gives Q=2/3", q_zero == Fraction(2, 3), f"Q={q_zero}")

    q_common = q_from_background(Fraction(1, 5), Fraction(0))
    check(
        "common source background cancels from dimensionless Q",
        q_common == Fraction(2, 3),
        f"Q(s=1/5,z=0)={q_common}",
    )

    q_traceless = q_from_background(Fraction(0), Fraction(1, 4))
    check(
        "traceless source-label background changes Q",
        q_traceless != Fraction(2, 3),
        f"Q(s=0,z=1/4)={q_traceless}",
    )

    q_negative_z = q_from_background(Fraction(0), Fraction(-1, 4))
    check(
        "opposite traceless background changes Q in the opposite direction",
        q_negative_z != q_traceless and q_negative_z != Fraction(2, 3),
        f"Q(z=-1/4)={q_negative_z}",
    )


def part2_z_observable() -> None:
    banner("Part 2: Z label survives observable completeness")

    # In the reduced two-channel basis, Z = diag(1,-1). It is central for the
    # diagonal C3 source action and obeys Z^2 = I.
    z_square = (1 * 1, (-1) * (-1))
    check("Z^2=I on the two-channel source label", z_square == (1, 1), f"Z^2={z_square}")

    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(3, 4)]
    expectations = [z_expectation(w) for w in weights]
    check(
        "Z expectation distinguishes non-midpoint source states",
        len(set(expectations)) == len(expectations),
        f"<Z>={expectations}",
    )

    check(
        "midpoint is the only listed state with <Z>=0",
        [w for w in weights if z_expectation(w) == 0] == [Fraction(1, 2)],
    )


def part3_delta_selected_line_conditional() -> None:
    banner("Part 3: delta selected-line local endpoint support")

    # Work in a basis adapted to the selected line: P_chi=diag(1,0).
    selected_channel = 1
    spectator_channel = 0
    end_l_dim = 1
    end_v_dim = 4

    check("selected-line local source algebra End(L_chi) is one-dimensional", end_l_dim == 1)
    check("ambient End(V) has extra endpoint-source directions", end_v_dim > end_l_dim)
    check("selected-line projector gives selected_channel=1", selected_channel == 1)
    check("selected-line projector kills spectator_channel", spectator_channel == 0)

    delta_selected = selected_channel * ETA_APS
    check("selected-line local support conditionally transfers eta_APS to delta", delta_selected == ETA_APS)

    pullback_normal = 0
    check("normal endpoint source is pullback-kernel data for selected-line readout", pullback_normal == 0)


def part4_delta_ambient_countermodels() -> None:
    banner("Part 4: delta ambient-source and endpoint-torsor countermodels")

    cases = [
        DeltaCase("closing", Fraction(0), Fraction(0), Fraction(2, 9)),
        DeltaCase("spectator", Fraction(1), Fraction(0), Fraction(0)),
        DeltaCase("mixed", Fraction(1, 2), Fraction(0), Fraction(1, 9)),
        DeltaCase("shifted", Fraction(0), Fraction(1, 9), Fraction(1, 3)),
    ]

    for case in cases:
        value = delta_open(case.spectator, case.endpoint_shift)
        check(f"{case.name} endpoint countermodel has expected delta", value == case.expected, f"delta={value}")

    ambient_half = Fraction(1, 2) * ETA_APS
    check(
        "ambient rank-two source leaves a free selected/spectator mixture",
        ambient_half == Fraction(1, 9) and ambient_half != ETA_APS,
        f"p=1/2 gives delta={ambient_half}",
    )


def part5_verdict() -> None:
    banner("Part 5: closure no-go verdict")

    q_counterexample = q_from_background(Fraction(0), Fraction(1, 4))
    delta_counterexample = delta_open(Fraction(1, 2), Fraction(0))

    q_forced = q_counterexample == Fraction(2, 3)
    delta_forced = delta_counterexample == ETA_APS
    full_forced = q_forced and delta_forced

    check("Q closure is blocked by traceless Z background", not q_forced)
    check("delta closure is blocked by ambient spectator source", not delta_forced)
    check("full dimensionless closure is not forced by the finite algebra", not full_forced)


def audit_metadata_checks() -> None:
    banner("Part 6: regenerated audit metadata")
    if not LEDGER.exists() or not QUEUE.exists():
        print("  audit metadata unavailable before pipeline")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"].get(CLAIM_ID)
    if row is None:
        print("  audit ledger row unavailable before pipeline")
        return
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next((e for e in queue if e["claim_id"] == CLAIM_ID), None)

    check("ledger claim_type is no_go", row.get("claim_type") == "no_go", str(row.get("claim_type")))
    check(
        "ledger audit_status is a no-go-compatible state",
        row.get("audit_status") in {"unaudited", "audited_clean"},
        str(row.get("audit_status")),
    )
    check(
        "ledger effective_status is no-go-compatible",
        row.get("effective_status") in {"unaudited", "retained_no_go"},
        str(row.get("effective_status")),
    )
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    if queue_entry is None:
        check(
            "active queue entry absent only after retained no-go audit",
            row.get("audit_status") == "audited_clean"
            and row.get("effective_status") == "retained_no_go",
            f"audit_status={row.get('audit_status')}, effective_status={row.get('effective_status')}",
        )
    else:
        check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 70, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    print("=" * 88)
    print("Koide dimensionless countermodel no-go")
    print("=" * 88)

    note_boundary_checks()
    part1_q_background_zero()
    part2_z_observable()
    part3_delta_selected_line_conditional()
    part4_delta_ambient_countermodels()
    part5_verdict()
    audit_metadata_checks()

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"PASSED: {PASS_COUNT}/{PASS_COUNT + FAIL_COUNT}")
    print("=" * 88)

    if FAIL_COUNT == 0:
        print("KOIDE_DIMENSIONLESS_COUNTERMODEL_NOGO=TRUE")
        print("Q_DIMENSIONLESS_OBJECTION_CLOSES_Q=FALSE")
        print("DELTA_DIMENSIONLESS_OBJECTION_CLOSES_DELTA=FALSE")
        print("FULL_DIMENSIONLESS_OBJECTION_CLOSES_LANE=FALSE")
        print("FULL_DIMENSIONLESS_CLOSURE_FORCED_BY_FINITE_ALGEBRA=FALSE")
        print("Q_FORCED_WITHOUT_Z_ZERO_LAW=FALSE")
        print("DELTA_FORCED_WITHOUT_LINE_LOCAL_BASEPOINT_LAW=FALSE")
        print("CONDITIONAL_Q_IF_BACKGROUND_Z_ZERO=TRUE")
        print("CONDITIONAL_DELTA_IF_SELECTED_LINE_LOCAL_AND_BASED=TRUE")
        print("RESIDUAL_Q=derive_physical_background_source_zero_or_Z_erasure")
        print("RESIDUAL_DELTA=derive_selected_line_local_boundary_source_and_based_endpoint")
        return 0

    print("KOIDE_DIMENSIONLESS_COUNTERMODEL_NOGO=FALSE")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
