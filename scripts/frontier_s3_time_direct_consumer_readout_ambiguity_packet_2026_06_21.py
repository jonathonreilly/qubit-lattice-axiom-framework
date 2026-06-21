#!/usr/bin/env python3
"""Direct-consumer readout ambiguity packet for the S3-time Route-2 gate.

This runner classifies the immediate S3-time consumers of the Route-2 readout
map.  It separates rho_E-blind structural support from E-center-sensitive
consumer claims, so downstream work can cite the conditional family and
factor-rigidity pieces without smuggling in the missing E-center selector.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
)
from frontier_quark_route2_exact_time_coupling import (
    route2_slice_backbone,
    v_r,
    xi_p,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class Consumer:
    claim_id: str
    note: str
    dependency_class: str
    safe_use: str
    blocked_use: str


CONSUMERS: tuple[Consumer, ...] = (
    Consumer(
        "s3_time_theta_to_slice_coupling_note",
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        "e_center_sensitive_open_gate",
        "exact conditional family for supplied P_R",
        "unique Theta_R -> Lambda_R law before P_R selection",
    ),
    Consumer(
        "s3_time_theta_to_slice_coupling_factor_rigidity_note_2026-05-17",
        "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        "rho_independent_structural_support",
        "time-channel universality and rank-1 spatial prefactor localization",
        "endpoint triple selection",
    ),
    Consumer(
        "s3_time_readout_primitive_bridge_assessment_2026-06-12",
        "S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md",
        "membership_not_selector",
        "eta-floor membership in the restricted bright class",
        "physical/canonical readout primitive selection",
    ),
    Consumer(
        "s3_time_primitive_chain_note",
        "S3_TIME_PRIMITIVE_CHAIN_NOTE.md",
        "p2_readout_map_open",
        "exact stack through carrier, slice semigroup, and conditional P_R use",
        "final unique readout-to-slice theorem before E-channel entry selection",
    ),
)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def doc(name: str) -> str:
    path = DOCS / name
    check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def matrix_rank(matrix: np.ndarray, tol: float = 1.0e-10) -> int:
    return int(np.sum(np.linalg.svd(matrix, compute_uv=False) > tol))


def main() -> int:
    print("S3-time direct-consumer readout ambiguity packet")
    print("=" * 78)

    new_note = doc("S3_TIME_DIRECT_CONSUMER_READOUT_AMBIGUITY_PACKET_NOTE_2026-06-21.md")
    s3_gate = doc("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    rigidity = doc("S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md")
    bridge = doc("S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md")
    primitive_chain = doc("S3_TIME_PRIMITIVE_CHAIN_NOTE.md")
    exact_readout = doc("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    exact_time = doc("QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md")

    print()
    print("A. Consumer anchors")
    print("-" * 78)
    check(
        "new note records the direct-consumer dependency split",
        all(
            phrase in flat(new_note)
            for phrase in (
                "direct-consumer readout ambiguity packet",
                "rho_E-blind structural support",
                "E-center-sensitive consumer claims",
                "membership-not-selector",
                "does not close the endpoint",
            )
        ),
    )
    check(
        "S3 gate is conditional on supplied P_R",
        "Xi_P(t ; c) = (P_R c) \u2297 V_R(t)" in s3_gate
        and "readout-map endpoint triple" in s3_gate
        and "not derived by the current exact stack" in s3_gate,
    )
    check(
        "factor-rigidity consumer localizes ambiguity to spatial prefactor",
        "structurally localized in the spatial prefactor" in rigidity
        and "time-channel structure is universal" in rigidity,
    )
    check(
        "bridge-assessment consumer is membership not uniqueness",
        "membership-but-not-uniqueness" in bridge
        and "selection/identification theorem for the readout map" in flat(bridge),
    )
    check(
        "primitive-chain consumer keeps P2 readout map open",
        "Primitive P2: exact readout map" in primitive_chain
        and "exact theorem still open" in primitive_chain,
    )
    check(
        "exact readout and time authorities provide the two ingredients",
        "any admissible bright-preserving linear readout" in exact_readout
        and "Given any admissible readout map `P_R`" in exact_time,
    )

    print()
    print("B. Exact rho_E sensitivity by carrier column")
    print("-" * 78)
    data = restricted_readout_data()
    backbone = route2_slice_backbone()
    v = v_r(backbone, 1.0)
    p_zero = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_target = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)
    delta_p = p_target - p_zero

    columns = (
        ("E-shell", data.carrier_e_shell, False),
        ("E-center", data.carrier_e_center, True),
        ("T-shell", data.carrier_t_shell, False),
        ("T-center", data.carrier_t_center, False),
    )
    for label, column, should_depend in columns:
        xi_zero = xi_p(p_zero, column, v)
        xi_target = xi_p(p_target, column, v)
        delta = xi_target - xi_zero
        expected_delta = xi_p(delta_p, column, v)
        norm = float(np.linalg.norm(delta))
        rank = matrix_rank(delta)
        check(
            f"{label} dependency classification is exact",
            (norm > EXACT_TOL) == should_depend
            and float(np.max(np.abs(delta - expected_delta))) < EXACT_TOL,
            f"delta_norm={norm:.6e}, rank={rank}",
        )
    e_center_delta = xi_p(p_target, data.carrier_e_center, v) - xi_p(p_zero, data.carrier_e_center, v)
    check(
        "E-center ambiguity is rank-1 along the time trajectory",
        matrix_rank(e_center_delta) == 1,
        f"rank={matrix_rank(e_center_delta)}",
    )
    check(
        "universal time factor is nonzero, so E-center prefactor ambiguity reaches the consumer",
        float(np.linalg.norm(v)) > 0.0 and float(np.linalg.norm(e_center_delta)) > 0.0,
        f"||V_R||={np.linalg.norm(v):.6e}, ||delta||={np.linalg.norm(e_center_delta):.6e}",
    )

    print()
    print("C. Consumer classification table")
    print("-" * 78)
    note_bank = {
        consumer.note: doc(consumer.note)
        for consumer in CONSUMERS
    }
    for consumer in CONSUMERS:
        text = note_bank[consumer.note]
        check(
            f"{consumer.claim_id} note contains safe-use anchor",
            any(token in text for token in consumer.safe_use.split()[:3]),
            consumer.dependency_class,
        )
        check(
            f"{consumer.claim_id} is represented in the new dependency table",
            consumer.claim_id in new_note
            and consumer.dependency_class in new_note
            and consumer.safe_use in new_note
            and consumer.blocked_use in new_note,
        )

    print()
    print("D. Direct-consumer consequence")
    print("-" * 78)
    check(
        "rho_E-blind consumers may use the conditional family without endpoint selection",
        "rho_independent_structural_support" in new_note
        and "time-channel universality" in new_note,
    )
    check(
        "E-center-sensitive consumers remain blocked at P_R selection",
        "e_center_sensitive_open_gate" in new_note
        and "unique Theta_R -> Lambda_R law before P_R selection" in new_note,
    )
    check(
        "membership-only eta-floor result is not a selector",
        "membership_not_selector" in new_note
        and "physical/canonical readout primitive selection" in new_note,
    )
    check(
        "packet leaves the positive target explicit",
        "E-center endpoint ratio" in new_note
        and "source-domain rule" in new_note
        and "stronger readout-map theorem" in new_note,
    )

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: direct S3-time consumers split into rho_E-blind structural support and E-center-sensitive open claims.")
        return 0
    print("VERDICT: direct-consumer ambiguity checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
