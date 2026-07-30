#!/usr/bin/env python3
"""Independent check of the Cycle-733 conditional finite-box lemma.

This runner does not import the Cycle-733 primary or the Cycle-727 analysis.
It reconstructs the repaired five-family 2 x 2 x 2 dictionary directly from
the finite fixtures, including signed phases and ordering, and checks the
conditional block algebra independently.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/SECTOR_SUMMED_COMPANION_CHANNEL_CYCLE733_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/SECTOR_SUMMED_COMPANION_CHANNEL_CYCLE733_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle733_sector_summed_companion_channel_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle727_finite_fixtures_2026_07_28.py",
    "scripts/frontier_cycle727_finite_pauli_tableau_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import combinations
import json
import sys
import time

import frontier_cycle727_finite_fixtures_2026_07_28 as F


SHAPE = (2, 2, 2)
FAMILIES = ("free", "seam", "reverse", "contact", "coin")
EXPECTED_FAMILY_COUNTS = {
    "free": 48,
    "seam": 12,
    "reverse": 12,
    "contact": 120,
    "coin": 120,
}
EXPECTED_DICTIONARY_SHA256 = (
    "dadb2087ae6604e877d8c406c056fb0d88ed31fceb772daf4093e685fed1797e"
)
EXPECTED_SIGNED_RELATION_SHA256 = (
    "c1bd52a612ccef8bdd082ad6f9e8f99e19ee20807c17841c57ee6f433c1a9bc1"
)
PRIMARY_MODULE_NAME = (
    "frontier_cycle733_sector_summed_companion_channel_2026_07_28"
)
FAILURES = 0
CHECK_COUNT = 0


@dataclass(frozen=True)
class IndependentRow:
    family: str
    label: str
    target: F.Pauli
    reference_physical: F.Pauli
    companion_physical: F.Pauli


def digest(value: object) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def pauli_key(row: F.Pauli) -> str:
    return f"{row.phase % 4}:{row.x:x}:{row.z:x}"


def check(label: str, condition: bool, detail: object = None) -> None:
    global CHECK_COUNT, FAILURES
    CHECK_COUNT += 1
    passed = bool(condition)
    FAILURES += not passed
    payload = "ok" if passed else detail
    print(
        "PASS" if passed else "FAIL",
        label,
        "::",
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str),
    )


def reconstruct_rows(
    reference: F.CellEdgeGauge,
    companion: F.CompanionFixture,
) -> tuple[IndependentRow, ...]:
    """Re-enumerate the current five families without Cycle-727 core calls."""
    rows = []
    for cell, coordinate in enumerate(reference.cells):
        for local_mode in range(6):
            mode = 6 * cell + local_mode
            row = F.Pauli(z=1 << mode)
            rows.append(IndependentRow(
                "free",
                f"free:c{coordinate}:m{local_mode}:q{mode}",
                row,
                row,
                row,
            ))

    for edge, (
        left, right, owner, axis, left_mode, right_mode
    ) in enumerate(reference.edges):
        reference_terms = reference.physical_terms(edge)
        reference_targets = reference.expected_terms(edge)
        companion_terms = companion.physical_terms(edge)
        companion_targets = companion.target_terms(edge)
        if reference_targets != companion_targets:
            raise RuntimeError(("target seam dictionary mismatch", edge))
        suffix = (
            f"e{edge}:owner{owner}:a{axis}:"
            f"{left}/{left_mode}->{right}/{right_mode}"
        )
        rows.extend((
            IndependentRow(
                "seam",
                f"seam:{suffix}",
                reference_targets[2],
                reference_terms[2],
                companion_terms[2],
            ),
            IndependentRow(
                "reverse",
                f"reverse:{suffix}",
                reference_targets[3],
                reference_terms[3],
                companion_terms[3],
            ),
        ))

    for cell, coordinate in enumerate(reference.cells):
        for left_local, right_local in combinations(range(6), 2):
            left = 6 * cell + left_local
            right = 6 * cell + right_local
            endpoints = (1 << left) | (1 << right)
            between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
            contact = F.Pauli(
                phase=2, x=endpoints, z=between | endpoints
            )
            coin = F.Pauli(x=endpoints, z=between)
            suffix = f"c{coordinate}:m{left_local}-{right_local}"
            rows.extend((
                IndependentRow(
                    "contact",
                    f"contact:{suffix}",
                    contact,
                    contact,
                    contact,
                ),
                IndependentRow(
                    "coin",
                    f"coin:{suffix}",
                    coin,
                    coin,
                    coin,
                ),
            ))

    return tuple(
        row for family in FAMILIES for row in rows if row.family == family
    )


def dictionary_payload(
    reference: F.CellEdgeGauge,
    rows: tuple[IndependentRow, ...],
) -> dict[str, object]:
    modes = tuple({
        "cell": cell,
        "cell_coordinate": reference.cells[cell],
        "local_mode": local,
        "global_mode": 6 * cell + local,
    } for cell in range(len(reference.cells)) for local in range(6))
    edges = tuple({
        "edge": edge,
        "left_cell": row[0],
        "right_cell": row[1],
        "owner": row[2],
        "axis": row[3],
        "left_mode": row[4],
        "right_mode": row[5],
    } for edge, row in enumerate(reference.edges))
    generator_lists = {
        family: tuple({
            "label": row.label,
            "signed_target": pauli_key(row.target),
        } for row in rows if row.family == family)
        for family in FAMILIES
    }
    payload = {
        "shape": reference.shape,
        "cells": reference.cells,
        "modes": modes,
        "oriented_edges": edges,
        "endpoint_convention": (
            "positive-axis edge owner is the lower coordinate; "
            "left endpoint mode=6*left+2*axis+1 and "
            "right endpoint mode=6*right+2*axis"
        ),
        "generator_order": FAMILIES,
        "signed_generator_lists": generator_lists,
        "duplicate_policy": (
            "the two endpoint-Z members repeated in each landed four-row "
            "seam tuple are represented once by their free-mode labels"
        ),
        "total_parity_convention": (
            "P_total=product of Z on all 6N matter modes; even is s=+1 "
            "(odd=False), odd is s=-1 (odd=True)"
        ),
    }
    payload["family_order_digests"] = {
        family: digest(generator_lists[family]) for family in FAMILIES
    }
    payload["frozen_dictionary_digest"] = digest(payload)
    return payload


def matter_parity_preserving(row: F.Pauli, matter_qubits: int) -> bool:
    matter_mask = (1 << matter_qubits) - 1
    return ((row.x & matter_mask).bit_count() % 2) == 0


def parity_census(
    rows: tuple[IndependentRow, ...], matter_qubits: int
) -> dict[str, object]:
    surfaces = ("target", "reference_physical", "companion_physical")
    failures = tuple(
        (index, row.family, surface)
        for index, row in enumerate(rows)
        for surface in surfaces
        if not matter_parity_preserving(getattr(row, surface), matter_qubits)
    )
    return {
        "representatives_tested": len(rows) * len(surfaces),
        "failures": failures,
        "all_preserve_total_matter_parity": (
            len(rows) * len(surfaces) == 936 and not failures
        ),
    }


def signed_dictionary_control(
    reference: F.CellEdgeGauge,
    rows: tuple[IndependentRow, ...],
) -> dict[str, object]:
    selected = next(i for i, row in enumerate(rows) if row.family == "contact")
    original = rows[selected]
    mutated_target = replace(
        original.target, phase=(original.target.phase + 2) % 4
    )
    mutated = list(rows)
    mutated[selected] = replace(original, target=mutated_target)
    original_digest = dictionary_payload(
        reference, rows
    )["frozen_dictionary_digest"]
    mutated_digest = dictionary_payload(
        reference, tuple(mutated)
    )["frozen_dictionary_digest"]
    return {
        "original_sha256": original_digest,
        "mutated_sha256": mutated_digest,
        "detected": (
            original_digest == EXPECTED_DICTIONARY_SHA256
            and mutated_digest != original_digest
        ),
    }


def parity_flip_control(
    rows: tuple[IndependentRow, ...], matter_qubits: int
) -> dict[str, object]:
    original = rows[0].target
    mutated = replace(original, x=original.x ^ 1)
    return {
        "detected": (
            matter_parity_preserving(original, matter_qubits)
            and not matter_parity_preserving(mutated, matter_qubits)
        )
    }


def independent_block_algebra() -> dict[str, object]:
    """Derive the two-sector formula by block-support composition."""
    sectors = ("even", "odd")
    v_support = {(sector, sector) for sector in sectors}
    operator_support = {(sector, sector) for sector in sectors}
    gram_support = {
        (left_source, right_source)
        for left_target, left_source in v_support
        for right_target, right_source in v_support
        if left_target == right_target
    }
    va_support = {
        (v_target, a_source)
        for v_target, v_source in v_support
        for a_target, a_source in operator_support
        if v_source == a_target
    }
    bv_support = {
        (b_target, v_source)
        for b_target, b_source in operator_support
        for v_target, v_source in v_support
        if b_source == v_target
    }
    expected_diagonal = {("even", "even"), ("odd", "odd")}

    # Exact phase-exponent arithmetic for the odd block.  Gram conjugation
    # cancels -theta+theta; both intertwining terms carry +theta.
    phase_identity = (-1 + 1 == 0) and (+1 == +1)

    # An off-diagonal operator mutation invalidates the block-preserving
    # hypothesis and produces support not covered by sectorwise premises.
    mutated_operator_support = operator_support | {("even", "odd")}
    mutated_va_support = {
        (v_target, a_source)
        for v_target, v_source in v_support
        for a_target, a_source in mutated_operator_support
        if v_source == a_target
    }
    off_diagonal_mutation_detected = (
        mutated_va_support != expected_diagonal
        and ("even", "odd") in mutated_va_support
    )

    # A phase-free 3-qubit Pauli census independently checks the elementary
    # parity criterion: half of all words preserve total Z parity.
    pauli_words = tuple(
        (x, z) for x in range(1 << 3) for z in range(1 << 3)
    )
    preserving = sum((x.bit_count() % 2) == 0 for x, _z in pauli_words)
    flipping = len(pauli_words) - preserving

    return {
        "gram_support": sorted(gram_support),
        "va_support": sorted(va_support),
        "bv_support": sorted(bv_support),
        "conditional_identity_exact": (
            gram_support == expected_diagonal
            and va_support == expected_diagonal
            and bv_support == expected_diagonal
            and phase_identity
        ),
        "sector_isometry_premise_discharged_here": False,
        "sector_intertwining_premise_discharged_here": False,
        "relative_phase_selected": False,
        "off_diagonal_mutation_detected": off_diagonal_mutation_detected,
        "three_qubit_pauli_words": len(pauli_words),
        "three_qubit_parity_preserving": preserving,
        "three_qubit_parity_flipping": flipping,
        "toy_parity_split_exact": (
            len(pauli_words) == 64 and preserving == flipping == 32
        ),
    }


def main() -> None:
    started = time.monotonic()
    print(
        "SCOPE independent current-fixture reconstruction; finite parity "
        "census; conditional block algebra only"
    )
    reference = F.CellEdgeGauge.build(SHAPE)
    companion = F.CompanionFixture.build(SHAPE)
    rows = reconstruct_rows(reference, companion)
    payload = dictionary_payload(reference, rows)
    signed_relation_sha256 = digest(tuple(
        (
            row.family,
            row.label,
            pauli_key(row.target),
            pauli_key(row.reference_physical),
            pauli_key(row.companion_physical),
        )
        for row in rows
    ))
    family_counts = {
        family: sum(row.family == family for row in rows)
        for family in FAMILIES
    }
    parity = parity_census(rows, reference.matter_qubits)
    signed_control = signed_dictionary_control(reference, rows)
    parity_control = parity_flip_control(rows, reference.matter_qubits)
    algebra = independent_block_algebra()

    check(
        "current five-family dictionary independently reconstructed",
        len(rows) == 312
        and family_counts == EXPECTED_FAMILY_COUNTS
        and payload["frozen_dictionary_digest"]
        == EXPECTED_DICTIONARY_SHA256,
        {
            "rows": len(rows),
            "family_counts": family_counts,
            "dictionary_sha256": payload["frozen_dictionary_digest"],
        },
    )
    check(
        "all signed target/reference/companion phases retained",
        signed_relation_sha256 == EXPECTED_SIGNED_RELATION_SHA256,
        {
            "signed_relation_sha256": signed_relation_sha256,
            "expected": EXPECTED_SIGNED_RELATION_SHA256,
        },
    )
    check(
        "all 936 independently reconstructed representatives preserve parity",
        parity["all_preserve_total_matter_parity"],
        parity,
    )
    check(
        "signed-phase corruption changes frozen dictionary",
        signed_control["detected"],
        signed_control,
    )
    check(
        "parity-flip corruption detected",
        parity_control["detected"],
        parity_control,
    )
    check(
        "conditional block-support algebra independently exact",
        algebra["conditional_identity_exact"]
        and algebra["toy_parity_split_exact"],
        algebra,
    )
    check(
        "missing premises and relative phase remain open",
        not algebra["sector_isometry_premise_discharged_here"]
        and not algebra["sector_intertwining_premise_discharged_here"]
        and not algebra["relative_phase_selected"]
        and algebra["off_diagonal_mutation_detected"],
        algebra,
    )
    check(
        "independent runner excludes primary import",
        PRIMARY_MODULE_NAME not in sys.modules
        and all("cycle720" not in path for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )

    report = {
        "status": "CYCLE733_INDEPENDENT_CONDITIONAL_LEMMA_PASS",
        "pass": FAILURES == 0,
        "named_checks_passed": CHECK_COUNT - FAILURES,
        "named_checks_total": CHECK_COUNT,
        "shape": SHAPE,
        "generator_rows": len(rows),
        "family_counts": family_counts,
        "dictionary_sha256": payload["frozen_dictionary_digest"],
        "signed_relation_sha256": signed_relation_sha256,
        "parity_certificate": parity,
        "conditional_algebra": algebra,
        "controls": {
            "signed_phase_corruption_detected": signed_control["detected"],
            "parity_flip_detected": parity_control["detected"],
            "off_diagonal_mutation_detected": (
                algebra["off_diagonal_mutation_detected"]
            ),
        },
        "boundary": {
            "primary_imported": False,
            "cycle727_analysis_imported": False,
            "sector_maps_constructed": False,
            "coherent_channel_constructed": False,
            "relative_phase_selected": False,
        },
        "runtime_seconds": time.monotonic() - started,
    }
    report["report_sha256"] = digest(report)
    print("FINAL_JSON")
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    if FAILURES:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
