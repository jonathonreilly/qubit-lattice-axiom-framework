#!/usr/bin/env python3
"""Structural scope-split verification for the native record apparatus note.

This is not a physics simulation. It is a deterministic structural audit of
the parent record apparatus note

    docs/TELEPORTATION_NATIVE_RECORD_APPARATUS_NOTE.md

and its source-theorem-note scope split

    docs/TELEPORTATION_NATIVE_RECORD_APPARATUS_SCOPE_SPLIT_SOURCE_THEOREM_NOTE_2026-05-16.md

The runner verifies that the parent note honestly factors into two disjoint
claim surfaces:

  B = bounded apparatus/carrier consistency on the cited runner certificate
  N = native-derivation closure (Bell-stabilizer transducer derivation N1,
      durable pointer irreversibility N2, derived local record-field
      carrier N3); HOLD

and that the parent note's strongest operational statement is restricted to
surface B. It also re-verifies the algebraic identities that the bounded
model relies on (Bell-projector completeness and orthogonality, length-8
codeword Hamming distance and decoding, Pauli correction inverse, Manhattan
delivery-tick identity) and re-parses the existing parent runner cache to
confirm the bounded-model magnitudes are at the recorded numerical zero.

The runner does NOT promote the teleportation lane, does NOT close any of
the three N1-N3 nature-grade bridges, and does NOT modify the canonical
harness index.
"""

from __future__ import annotations

import math
import re
import sys
from dataclasses import dataclass
from enum import Enum
from itertools import combinations
from pathlib import Path
from typing import Iterable

import numpy as np


REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_NOTE = REPO_ROOT / "docs" / "TELEPORTATION_NATIVE_RECORD_APPARATUS_NOTE.md"
SPLIT_NOTE = (
    REPO_ROOT
    / "docs"
    / "TELEPORTATION_NATIVE_RECORD_APPARATUS_SCOPE_SPLIT_SOURCE_THEOREM_NOTE_2026-05-16.md"
)
PARENT_RUNNER = (
    REPO_ROOT / "scripts" / "frontier_teleportation_native_record_apparatus.py"
)
PARENT_RUNNER_CACHE = (
    REPO_ROOT
    / "logs"
    / "runner-cache"
    / "frontier_teleportation_native_record_apparatus.txt"
)
HARNESS_INDEX = REPO_ROOT / "docs" / "CANONICAL_HARNESS_INDEX.md"


I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
OUTCOME_ORDER: tuple[tuple[int, int], ...] = ((0, 0), (1, 0), (0, 1), (1, 1))


class Verdict(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"


@dataclass(frozen=True)
class Check:
    name: str
    verdict: Verdict
    detail: str


# Three native-derivation gaps named verbatim in the parent note's
# audit-conditional perimeter and Nature-Grade Blockers section.
NATURE_GRADE_GAPS = [
    (
        "N1_bell_stabilizer_transducer_derivation",
        ["Bell-stabilizer transducer", "ideal/projective"],
    ),
    (
        "N2_durable_pointer_irreversibility",
        ["classical model of durable memory", "thermodynamic"],
    ),
    (
        "N3_local_record_field_carrier_derivation",
        ["local on a 3D+1 lattice", "field equation"],
    ),
]


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def bell_projector(z_bit: int, x_bit: int) -> np.ndarray:
    zz = np.kron(Z2, Z2)
    xx = np.kron(X2, X2)
    identity = np.eye(4, dtype=complex)
    return 0.25 * (identity + ((-1) ** x_bit) * zz) @ (
        identity + ((-1) ** z_bit) * xx
    )


def record_codeword(z_bit: int, x_bit: int) -> tuple[int, ...]:
    parity = z_bit ^ x_bit
    return (z_bit, z_bit, z_bit, x_bit, x_bit, x_bit, parity, parity)


def hamming(first: tuple[int, ...], second: tuple[int, ...]) -> int:
    return sum(int(a != b) for a, b in zip(first, second))


def all_codewords() -> dict[tuple[int, int], tuple[int, ...]]:
    return {outcome: record_codeword(*outcome) for outcome in OUTCOME_ORDER}


def decode_nearest(codeword: tuple[int, ...]) -> tuple[int, int, int]:
    distances = [
        (hamming(codeword, candidate), outcome)
        for outcome, candidate in all_codewords().items()
    ]
    distances.sort(key=lambda item: item[0])
    return distances[0][1][0], distances[0][1][1], distances[0][0]


def flip_bits(codeword: tuple[int, ...], indexes: Iterable[int]) -> tuple[int, ...]:
    bits = list(codeword)
    for index in indexes:
        bits[index] ^= 1
    return tuple(bits)


def correction_operator(z_bit: int, x_bit: int) -> np.ndarray:
    z_op = Z2 if z_bit else I2
    x_op = X2 if x_bit else I2
    return z_op @ x_op


def manhattan_distance(
    source: tuple[int, int, int], target: tuple[int, int, int]
) -> int:
    return sum(abs(a - b) for a, b in zip(source, target))


def parse_cached_magnitude(cache_text: str, label: str) -> float | None:
    """Pull a labeled `name: <number>` magnitude from the parent runner cache."""
    pattern = rf"{re.escape(label)}\s*:\s*([\-+]?[0-9.]+(?:[eE][\-+]?[0-9]+)?)"
    match = re.search(pattern, cache_text)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def structural_checks() -> list[Check]:
    parent_text = _read(PARENT_NOTE)
    split_text = _read(SPLIT_NOTE)
    parent_runner_text = _read(PARENT_RUNNER)
    harness_text = _read(HARNESS_INDEX)
    checks: list[Check] = []

    # 1. Parent note exists and is labeled planning / first-artifact.
    checks.append(
        Check(
            "parent_note_planning_status",
            Verdict.PASS
            if (
                parent_text
                and "planning / first native apparatus-carrier candidate"
                in parent_text
                and "ordinary quantum state teleportation"
                in parent_text
            )
            else Verdict.FAIL,
            "Parent note is labeled planning / first native apparatus-carrier "
            "candidate and scope-restricts to ordinary quantum state "
            "teleportation.",
        )
    )

    # 2. Parent note carries the audit-conditional perimeter paragraph and
    # names the three ideal-vs-derived gaps.
    perimeter_ok = (
        "Audit-conditional perimeter" in parent_text
        and "Bell-stabilizer transducer" in parent_text
        and "durable pointer irreversibility" in parent_text
        and "local record-field carrier" in parent_text
        and "missing_bridge_theorem" in parent_text
    )
    checks.append(
        Check(
            "parent_audit_perimeter_names_three_gaps",
            Verdict.PASS if perimeter_ok else Verdict.FAIL,
            "Parent note carries the audit-conditional perimeter paragraph "
            "naming all three ideal-vs-derived gaps verbatim from the audit.",
        )
    )

    # 3. Parent note's Nature-Grade Blockers section names each of N1-N3.
    blockers_section_idx = parent_text.find("## Nature-Grade Blockers")
    blockers_text = (
        parent_text[blockers_section_idx:] if blockers_section_idx >= 0 else ""
    )
    for label, keywords in NATURE_GRADE_GAPS:
        present = all(kw in blockers_text for kw in keywords)
        checks.append(
            Check(
                f"parent_blocker_present::{label}",
                Verdict.PASS if present else Verdict.FAIL,
                f"Parent Nature-Grade Blockers section names: {label}.",
            )
        )

    # 4. Parent note's strongest operational statement is restricted to B.
    impact_idx = parent_text.find("## Retained-Theory Impact")
    impact_text = parent_text[impact_idx:] if impact_idx >= 0 else parent_text
    checks.append(
        Check(
            "parent_strongest_statement_b_surface_only",
            Verdict.PASS
            if (
                "strongest honest statement remains planning-level" in impact_text
                or "planning-level" in impact_text
            )
            else Verdict.FAIL,
            "Parent note's strongest current statement remains planning-level "
            "(B-surface only).",
        )
    )

    # 5. Parent runner exists and is referenced by the parent note.
    checks.append(
        Check(
            "parent_runner_references_parent_note",
            Verdict.PASS
            if (
                parent_runner_text
                and "Bell-record apparatus" in parent_runner_text
                and "frontier_teleportation_native_record_apparatus.py"
                in parent_text
            )
            else Verdict.FAIL,
            "Parent runner exists and parent note explicitly cites it.",
        )
    )

    # 6. Canonical harness index already files lane under HOLD-planning.
    checks.append(
        Check(
            "harness_index_parked_hold_language",
            Verdict.PASS
            if (
                "parked bounded planning lane" in harness_text
                and "nature-grade closure HOLD" in harness_text
                and "state teleportation only" in harness_text
                and "no matter/FTL/mass/charge transfer" in harness_text
            )
            else Verdict.FAIL,
            "Canonical harness index already files the lane as parked "
            "planning with nature-grade HOLD; no index update is asserted.",
        )
    )

    # 7. Scope-split note exists and is honestly scoped.
    checks.append(
        Check(
            "split_note_planning_scope",
            Verdict.PASS
            if (
                split_text
                and "planning/conditional scope-split bridge" in split_text
                and "nature-grade-HOLD" in split_text
                and "independent_audit_required_before_effective_status: true" in split_text
                and "bare_retained_status_allowed: false" in split_text
            )
            else Verdict.FAIL,
            "Scope-split source theorem note exists and self-labels as "
            "planning bridge with nature-grade HOLD.",
        )
    )

    return checks


def algebraic_identity_checks() -> list[Check]:
    """Recompute the bounded model's algebraic / combinatorial identities."""
    checks: list[Check] = []

    # 1. Bell projectors sum to identity (completeness).
    completeness = sum(bell_projector(z, x) for z, x in OUTCOME_ORDER)
    completeness_defect = float(
        np.linalg.norm(completeness - np.eye(4, dtype=complex))
    )
    checks.append(
        Check(
            "bell_projectors_complete",
            Verdict.PASS if completeness_defect < 1e-12 else Verdict.FAIL,
            f"Sum of four Bell projectors equals identity "
            f"(defect = {completeness_defect:.3e}).",
        )
    )

    # 2. Bell projectors pairwise orthogonal.
    max_off_diagonal = 0.0
    for (z1, x1), (z2, x2) in combinations(OUTCOME_ORDER, 2):
        p1 = bell_projector(z1, x1)
        p2 = bell_projector(z2, x2)
        max_off_diagonal = max(
            max_off_diagonal, float(np.max(np.abs(p1 @ p2)))
        )
    checks.append(
        Check(
            "bell_projectors_orthogonal",
            Verdict.PASS if max_off_diagonal < 1e-12 else Verdict.FAIL,
            f"Bell projectors pairwise orthogonal "
            f"(max off-product magnitude = {max_off_diagonal:.3e}).",
        )
    )

    # 3. Each Bell projector is idempotent (P^2 = P).
    max_idempotent_defect = 0.0
    for z, x in OUTCOME_ORDER:
        p = bell_projector(z, x)
        max_idempotent_defect = max(
            max_idempotent_defect, float(np.linalg.norm(p @ p - p))
        )
    checks.append(
        Check(
            "bell_projectors_idempotent",
            Verdict.PASS if max_idempotent_defect < 1e-12 else Verdict.FAIL,
            f"Each Bell projector satisfies P^2 = P "
            f"(max defect = {max_idempotent_defect:.3e}).",
        )
    )

    # 4. Length-8 codeword Hamming distance >= 5.
    codewords = all_codewords()
    min_distance = min(
        hamming(a, b)
        for left, a in codewords.items()
        for right, b in codewords.items()
        if left != right
    )
    checks.append(
        Check(
            "codeword_min_hamming_distance_5",
            Verdict.PASS if min_distance == 5 else Verdict.FAIL,
            f"Length-8 pointer codewords have minimum Hamming distance "
            f"{min_distance} (cited 5).",
        )
    )

    # 5. Nearest-codeword decoding corrects all one-bit flips.
    one_bit_ok = True
    for outcome, codeword in codewords.items():
        for index in range(len(codeword)):
            decoded_z, decoded_x, _ = decode_nearest(flip_bits(codeword, (index,)))
            if (decoded_z, decoded_x) != outcome:
                one_bit_ok = False
                break
        if not one_bit_ok:
            break
    checks.append(
        Check(
            "codeword_corrects_all_one_bit_flips",
            Verdict.PASS if one_bit_ok else Verdict.FAIL,
            "Nearest-codeword decoding recovers the original outcome from "
            "every one-bit flip.",
        )
    )

    # 6. Nearest-codeword decoding corrects all two-bit flips.
    two_bit_ok = True
    for outcome, codeword in codewords.items():
        for indexes in combinations(range(len(codeword)), 2):
            decoded_z, decoded_x, _ = decode_nearest(flip_bits(codeword, indexes))
            if (decoded_z, decoded_x) != outcome:
                two_bit_ok = False
                break
        if not two_bit_ok:
            break
    checks.append(
        Check(
            "codeword_corrects_all_two_bit_flips",
            Verdict.PASS if two_bit_ok else Verdict.FAIL,
            "Nearest-codeword decoding recovers the original outcome from "
            "every two-bit flip.",
        )
    )

    # 7. Pauli correction operator is self-inverse up to phase.
    max_inverse_defect = 0.0
    for z, x in OUTCOME_ORDER:
        u = correction_operator(z, x)
        max_inverse_defect = max(
            max_inverse_defect, float(np.linalg.norm(u.conj().T @ u - I2))
        )
    checks.append(
        Check(
            "pauli_correction_unitary",
            Verdict.PASS if max_inverse_defect < 1e-12 else Verdict.FAIL,
            f"Retained-axis Pauli correction operator Z^z X^x is unitary "
            f"(max U^dagger U - I defect = {max_inverse_defect:.3e}).",
        )
    )

    # 8. Manhattan delivery-tick identity on the cited worldline.
    alice_site = (1, 1, 1)
    bob_site = (5, 3, 2)
    alice_tick = 4
    expected_distance = 7
    expected_delivery = 11
    distance = manhattan_distance(alice_site, bob_site)
    checks.append(
        Check(
            "manhattan_distance_identity",
            Verdict.PASS if distance == expected_distance else Verdict.FAIL,
            f"Manhattan distance from {alice_site} to {bob_site} "
            f"= {distance} (cited {expected_distance}).",
        )
    )
    checks.append(
        Check(
            "manhattan_delivery_tick_identity",
            Verdict.PASS
            if (alice_tick + distance) == expected_delivery
            else Verdict.FAIL,
            f"Delivery tick = alice_tick + L1 = {alice_tick} + {distance} = "
            f"{alice_tick + distance} (cited {expected_delivery}).",
        )
    )

    return checks


def cache_witness_checks() -> list[Check]:
    """Re-parse the parent runner cache to confirm bounded-model magnitudes."""
    cache_text = _read(PARENT_RUNNER_CACHE)
    checks: list[Check] = []

    if not cache_text:
        checks.append(
            Check(
                "parent_runner_cache_exists",
                Verdict.FAIL,
                f"Parent runner cache not found at {PARENT_RUNNER_CACHE}.",
            )
        )
        return checks

    checks.append(
        Check(
            "parent_runner_cache_exists",
            Verdict.PASS,
            "Parent runner cache file exists.",
        )
    )

    # Cache should record exit_code: 0 and the canonical runner header.
    checks.append(
        Check(
            "parent_runner_cache_exit_zero",
            Verdict.PASS if "exit_code: 0" in cache_text else Verdict.FAIL,
            "Parent runner cache records exit_code: 0.",
        )
    )
    checks.append(
        Check(
            "parent_runner_cache_header",
            Verdict.PASS
            if (
                "NATIVE BELL-RECORD APPARATUS" in cache_text
                and "trials / seed: 64 / 20260426" in cache_text
            )
            else Verdict.FAIL,
            "Parent runner cache carries the canonical 64-trial / "
            "seed 20260426 header.",
        )
    )

    # Numerical-zero magnitudes (each must be at or below 1e-12).
    numerical_zero_labels = {
        "max Bell-transducer norm error": 1e-12,
        "max record probability error from 1/4": 1e-12,
        "max pairwise record-distribution distance across inputs": 1e-12,
        "max Bob trace distance to I/2 before carrier delivery": 1e-12,
        "max pairwise pre-delivery Bob-state distance across inputs": 1e-12,
        "maximum delivered-record infidelity": 1e-12,
        "max corrected-state trace distance to input": 1e-11,
    }
    for label, threshold in numerical_zero_labels.items():
        magnitude = parse_cached_magnitude(cache_text, label)
        checks.append(
            Check(
                f"cache_magnitude::{label.replace(' ', '_').replace('/', '_')}",
                Verdict.PASS
                if (magnitude is not None and magnitude < threshold)
                else Verdict.FAIL,
                f"Cached '{label}' = {magnitude} below {threshold:.0e}.",
            )
        )

    # Minimum corrected fidelity must be at numerical 1.
    min_correct_fidelity = parse_cached_magnitude(
        cache_text, "minimum delivered-record corrected fidelity"
    )
    checks.append(
        Check(
            "cache_min_corrected_fidelity_at_one",
            Verdict.PASS
            if (
                min_correct_fidelity is not None
                and min_correct_fidelity > 1.0 - 1e-12
            )
            else Verdict.FAIL,
            f"Cached minimum corrected fidelity = {min_correct_fidelity} "
            f"is within 1e-12 of unity.",
        )
    )

    # Wrong-record mean fidelity must be at the Pauli-error value ~ 1/3.
    wrong_mean = parse_cached_magnitude(
        cache_text, "wrong-record mean fidelity control"
    )
    checks.append(
        Check(
            "cache_wrong_record_mean_at_pauli_value",
            Verdict.PASS
            if (
                wrong_mean is not None
                and abs(wrong_mean - 1.0 / 3.0) < 0.05
            )
            else Verdict.FAIL,
            f"Cached wrong-record mean fidelity = {wrong_mean} is near the "
            f"Pauli-error value 1/3 (= {1.0 / 3.0:.6f}).",
        )
    )

    # All gates must read PASS in the cache.
    expected_gates = [
        "native Bell-stabilizer transducer writes all four records: PASS",
        "redundant record code is durable through two bit flips: PASS",
        "carrier payload is derived from apparatus pointer: PASS",
        "3D+1 record-field pulses propagate locally: PASS",
        "Bob pre-delivery state is input-independent: PASS",
        "delivered native carrier restores Bob state: PASS",
        "wrong-record control remains non-teleporting: PASS",
        "claim boundary stays state-only and not FTL: PASS",
    ]
    all_gates_present = all(line in cache_text for line in expected_gates)
    checks.append(
        Check(
            "cache_all_bounded_gates_pass",
            Verdict.PASS if all_gates_present else Verdict.FAIL,
            "Parent runner cache reports PASS on all eight bounded acceptance "
            "gates.",
        )
    )

    return checks


def split_disjointness_checks() -> list[Check]:
    """Sanity checks on the structural disjointness of surfaces B and N."""
    split_text = _read(SPLIT_NOTE)
    checks: list[Check] = []

    checks.append(
        Check(
            "split_names_surface_b_and_n",
            Verdict.PASS
            if (
                "Bounded apparatus/carrier consistency surface" in split_text
                and "Native-derivation closure surface" in split_text
            )
            else Verdict.FAIL,
            "Scope-split note explicitly names surfaces B and N.",
        )
    )

    checks.append(
        Check(
            "split_enumerates_three_gaps",
            Verdict.PASS
            if (
                "**N1.**" in split_text
                and "**N2.**" in split_text
                and "**N3.**" in split_text
            )
            else Verdict.FAIL,
            "Scope-split note enumerates the three N1-N3 native-derivation "
            "gaps.",
        )
    )

    checks.append(
        Check(
            "split_does_not_claim_n_closure",
            Verdict.PASS
            if (
                "Surface `N` remains HOLD" in split_text
                and "Nothing about surface `N` is closed here" in split_text
            )
            else Verdict.FAIL,
            "Scope-split note does not claim any native-derivation closure.",
        )
    )

    checks.append(
        Check(
            "split_does_not_promote_lane",
            Verdict.PASS
            if (
                "teleportation lane is not promoted" in split_text
                and "No new physics axiom" in split_text
            )
            else Verdict.FAIL,
            "Scope-split note explicitly declines lane promotion and adds "
            "no new physics axiom.",
        )
    )

    return checks


def print_table(checks: Iterable[Check]) -> None:
    for check in checks:
        print(f"{check.verdict.value:4s}  {check.name}: {check.detail}")


def main() -> int:
    all_checks: list[Check] = []
    all_checks.extend(structural_checks())
    all_checks.extend(algebraic_identity_checks())
    all_checks.extend(cache_witness_checks())
    all_checks.extend(split_disjointness_checks())

    print_table(all_checks)

    n_pass = sum(1 for c in all_checks if c.verdict == Verdict.PASS)
    n_fail = sum(1 for c in all_checks if c.verdict == Verdict.FAIL)
    total = len(all_checks)

    print()
    print(f"SUMMARY: PASS={n_pass} FAIL={n_fail} TOTAL={total}")
    print()
    print("SCOPE: This runner verifies the structural scope split between")
    print("  B = bounded apparatus/carrier consistency on the parent runner")
    print("      certificate (Bell projectors, length-8 codeword, Manhattan")
    print("      worldline, Pauli correction), and")
    print("  N = native-derivation closure (Bell-stabilizer transducer N1,")
    print("      durable pointer irreversibility N2, derived local")
    print("      record-field carrier N3); HOLD.")
    print("It does NOT promote the teleportation lane, does NOT close any of")
    print("the three N1-N3 nature-grade bridges, and does NOT modify the")
    print("canonical harness index. The parent note remains at planning /")
    print("first native apparatus-carrier candidate status.")

    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
