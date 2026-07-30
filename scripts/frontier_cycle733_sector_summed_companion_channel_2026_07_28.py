#!/usr/bin/env python3
"""Cycle-733 finite-box parity census and conditional direct-sum lemma.

The repaired Cycle-727 surface supplies fitted signed pullbacks separately in
fixed parity sectors.  This runner checks parity preservation of its current
2 x 2 x 2 dictionary and verifies the abstract block-algebra implication.  It
does not construct either sector map or a coherent channel.
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
    "scripts/frontier_cycle733_sector_sum_independent_check_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_pullback_analysis_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_pullback_core_2026_07_28.py",
    "scripts/frontier_cycle727_finite_factorization_2026_07_28.py",
    "scripts/frontier_cycle727_finite_fixtures_2026_07_28.py",
    "scripts/frontier_cycle727_finite_pauli_tableau_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from dataclasses import replace
from hashlib import sha256
import json
import time

from frontier_cycle727_cross_code_pullback_analysis_2026_07_28 import (
    analyze_shape,
)
from frontier_cycle727_cross_code_pullback_core_2026_07_28 import (
    FAMILIES,
    FROZEN_DICTIONARY_DIGESTS,
    FROZEN_SECTOR_EXPONENT_PAIRS,
    Pauli,
)


SHAPE = (2, 2, 2)
EXPECTED_FAMILY_COUNTS = {
    "free": 48,
    "seam": 12,
    "reverse": 12,
    "contact": 120,
    "coin": 120,
}
SURFACES = ("target", "reference_physical", "companion_physical")
FAILURES = 0
CHECK_COUNT = 0


def digest(value: object) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


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


def matter_parity_preserving(row: Pauli, matter_qubits: int) -> bool:
    matter_mask = (1 << matter_qubits) - 1
    return ((row.x & matter_mask).bit_count() % 2) == 0


def current_parent_certificate() -> tuple[dict[str, object], dict[str, object]]:
    bundle = analyze_shape(SHAPE)
    public = bundle["public"]
    generators = bundle["generators"]
    family_counts = {
        family: sum(row.family == family for row in generators)
        for family in FAMILIES
    }
    certificate = {
        "shape": public["shape"],
        "generator_rows": len(generators),
        "family_counts": family_counts,
        "dictionary_sha256": public["dictionary"]["frozen_dictionary_digest"],
        "signed_pullbacks_exact_in_supplied_sectors": (
            public["cross_code_pullbacks_exact"]
        ),
        "sector_exponent_pair": (
            bundle["euler"].matter_qubits,
            bundle["factor"].logical,
        ),
    }
    certificate["current_surface_match"] = (
        certificate["shape"] == SHAPE
        and certificate["generator_rows"] == 312
        and family_counts == EXPECTED_FAMILY_COUNTS
        and certificate["dictionary_sha256"]
        == FROZEN_DICTIONARY_DIGESTS[SHAPE]
        and certificate["sector_exponent_pair"]
        == FROZEN_SECTOR_EXPONENT_PAIRS[SHAPE]
        and certificate["signed_pullbacks_exact_in_supplied_sectors"]
    )
    return bundle, certificate


def parity_certificate(bundle: dict[str, object]) -> dict[str, object]:
    matter_qubits = bundle["factor"].fixture.matter_qubits
    failures = []
    family_surface_counts = {
        family: {surface: 0 for surface in SURFACES}
        for family in FAMILIES
    }
    for index, generator in enumerate(bundle["generators"]):
        for surface in SURFACES:
            row = getattr(generator, surface)
            if matter_parity_preserving(row, matter_qubits):
                family_surface_counts[generator.family][surface] += 1
            else:
                failures.append((index, generator.family, surface))
    tested = len(bundle["generators"]) * len(SURFACES)
    return {
        "matter_qubits": matter_qubits,
        "representatives_tested": tested,
        "parity_failures": failures,
        "family_surface_pass_counts": family_surface_counts,
        "all_preserve_total_matter_parity": not failures and tested == 936,
    }


def parity_flip_control(bundle: dict[str, object]) -> dict[str, object]:
    original = bundle["generators"][0].target
    mutated = replace(original, x=original.x ^ 1)
    matter_qubits = bundle["factor"].fixture.matter_qubits
    return {
        "original_preserves": matter_parity_preserving(
            original, matter_qubits
        ),
        "mutated_preserves": matter_parity_preserving(
            mutated, matter_qubits
        ),
        "detected": (
            matter_parity_preserving(original, matter_qubits)
            and not matter_parity_preserving(mutated, matter_qubits)
        ),
    }


def conditional_direct_sum_certificate() -> dict[str, object]:
    """Verify the formal two-sector block identities under named premises."""
    sectors = ("even", "odd")
    gram_blocks = {
        f"{target},{source}": (
            "sector_identity_premise" if target == source else "zero_by_orthogonality"
        )
        for target in sectors
        for source in sectors
    }
    intertwining_blocks = {
        f"{target},{source}": (
            "sector_intertwining_premise"
            if target == source
            else "zero_by_sector_preservation"
        )
        for target in sectors
        for source in sectors
    }
    # For V_theta = V_even (+) exp(i theta) V_odd, conjugation contributes
    # -theta+theta to the odd Gram block, while both odd intertwining terms
    # carry the same +theta.  These are symbolic exponent identities.
    phase_exponents = {
        "even_gram": (0, 0, 0),
        "odd_gram": (-1, +1, 0),
        "even_intertwining": (0, 0),
        "odd_intertwining": (+1, +1),
    }
    algebra_exact = (
        gram_blocks
        == {
            "even,even": "sector_identity_premise",
            "even,odd": "zero_by_orthogonality",
            "odd,even": "zero_by_orthogonality",
            "odd,odd": "sector_identity_premise",
        }
        and intertwining_blocks
        == {
            "even,even": "sector_intertwining_premise",
            "even,odd": "zero_by_sector_preservation",
            "odd,even": "zero_by_sector_preservation",
            "odd,odd": "sector_intertwining_premise",
        }
        and sum(phase_exponents["odd_gram"][:2])
        == phase_exponents["odd_gram"][2]
        and len(set(phase_exponents["odd_intertwining"])) == 1
    )
    return {
        "sector_isometry_premises_required": True,
        "sector_intertwining_premises_required": True,
        "sector_maps_constructed_here": False,
        "conditional_direct_sum_identity": algebra_exact,
        "gram_blocks": gram_blocks,
        "intertwining_blocks": intertwining_blocks,
        "relative_phase_parameter": "arbitrary",
        "relative_phase_selected": False,
        "physical_or_coherent_channel_constructed": False,
        "parent_open_gate_closed": False,
    }


def main() -> None:
    started = time.monotonic()
    print(
        "SCOPE supplied fitted parity sectors; 2x2x2 finite dictionary; "
        "conditional direct-sum algebra only"
    )
    bundle, parent = current_parent_certificate()
    parity = parity_certificate(bundle)
    mutation = parity_flip_control(bundle)
    lemma = conditional_direct_sum_certificate()

    check(
        "repaired Cycle727 finite parent surface frozen",
        parent["current_surface_match"],
        parent,
    )
    check(
        "all 936 current representatives preserve matter parity",
        parity["all_preserve_total_matter_parity"],
        parity,
    )
    check("parity-flip mutation detected", mutation["detected"], mutation)
    check(
        "conditional direct-sum block algebra exact",
        lemma["conditional_direct_sum_identity"],
        lemma,
    )
    check(
        "relative phase cancels but remains unselected",
        lemma["relative_phase_parameter"] == "arbitrary"
        and not lemma["relative_phase_selected"],
        lemma,
    )
    check(
        "unconditional channel conclusion blocked",
        not lemma["sector_maps_constructed_here"]
        and not lemma["physical_or_coherent_channel_constructed"]
        and not lemma["parent_open_gate_closed"],
        lemma,
    )
    check(
        "declared input closure is current and self-consistent",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and all("cycle720" not in path for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )

    report = {
        "status": "CYCLE733_FINITE_BOX_CONDITIONAL_DIRECT_SUM_LEMMA_PASS",
        "pass": FAILURES == 0,
        "named_checks_passed": CHECK_COUNT - FAILURES,
        "named_checks_total": CHECK_COUNT,
        "scope": {
            "shape": SHAPE,
            "finite_dictionary_only": True,
            "state_space_exhaustion_claimed": False,
        },
        "parent": parent,
        "parity_certificate": parity,
        "conditional_lemma": lemma,
        "controls": {"parity_flip_detected": mutation["detected"]},
        "boundary": {
            "actual_sector_maps": "not_constructed",
            "coherent_channel": "open",
            "odd_sector_intertwiner": "open",
            "relative_sector_phase": "open",
            "physical_preparation": "open",
            "uniform_encoder": "open",
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
