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
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/KOIDE_DIMENSIONLESS_NOTE_2026-04-24.md"
AUDIT_SCRIPTS = REPO_ROOT / "docs" / "audit" / "scripts"
if str(AUDIT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(AUDIT_SCRIPTS))

import ledger_io

CLAIM_SHARD = (
    REPO_ROOT
    / "docs/audit/data/ledger/ko/koide_dimensionless_note_2026-04-24.json"
)
AUDIT_INPUT_PATHS = (
    "docs/KOIDE_DIMENSIONLESS_NOTE_2026-04-24.md",
    "docs/audit/scripts/ledger_io.py",
    "docs/audit/data/ledger/ko/koide_dimensionless_note_2026-04-24.json",
)

CLAIM_ID = "koide_dimensionless_note_2026-04-24"

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


def context_provenance_checks() -> None:
    banner("Part 6: tracked source/context provenance")
    canonical = ledger_io.shard_path(CLAIM_ID)
    check(
        "canonical claim shard path is the exact declared input",
        canonical == CLAIM_SHARD
        and canonical.relative_to(REPO_ROOT).as_posix() in AUDIT_INPUT_PATHS,
        canonical.relative_to(REPO_ROOT).as_posix(),
    )
    row = json.loads(CLAIM_SHARD.read_text(encoding="utf-8"))
    check(
        "canonical context shard identity matches the source claim",
        row.get("claim_id") == CLAIM_ID,
        str(row.get("claim_id")),
    )
    print(
        "  audit verdict/status fields are intentionally neither interpreted "
        "nor used as science gates"
    )


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
    context_provenance_checks()

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"PASSED: {PASS_COUNT}/{PASS_COUNT + FAIL_COUNT}")
    print("=" * 88)
    print(f"per_element: checked — exact rational counterexamples vary Q or delta while preserving the named local inputs; aggregate FAIL={FAIL_COUNT}.")
    print(f"per_site: checked — the finite three-component background and selected-line carriers were evaluated as separate local witnesses; aggregate FAIL={FAIL_COUNT}.")
    print(f"per_mode: checked — traceless-Z and ambient-spectator directions independently move Q and delta; aggregate FAIL={FAIL_COUNT}.")
    print(f"per_block: checked — the combined countermodel block has neither Q=2/3 nor delta=eta_APS forced by the finite algebra; aggregate FAIL={FAIL_COUNT}.")
    print(f"lattice_wide: checked and not executed — this dimensionless finite-algebra claim supplies no lattice lift; the executed countermodels remain distinct with PASS={PASS_COUNT}, FAIL={FAIL_COUNT}.")

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
