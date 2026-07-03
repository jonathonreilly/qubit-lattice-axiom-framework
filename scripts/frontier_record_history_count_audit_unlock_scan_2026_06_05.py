#!/usr/bin/env python3
"""Record history/count audit-unlock scan verifier.

This runner verifies a branch-local support map. It does not apply audit
verdicts and does not edit audit data.

Run:
    python3 scripts/frontier_record_history_count_audit_unlock_scan_2026_06_05.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]

SUPPORT_NOTES = {
    "history_monoid": "docs/RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md",
    "finite_alphabet_dynamics": "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
}


@dataclass(frozen=True)
class Candidate:
    row_id: str
    bucket: str
    local_path: str | None
    branch_ref: str | None
    citable_support: tuple[str, ...]
    remaining_gates: tuple[str, ...]
    verdict_edit_allowed: bool = False


CANDIDATES: tuple[Candidate, ...] = (
    Candidate(
        "RECORD_GENERATION_READOUT_TWO_SECTORS",
        "cite_ready_support",
        "docs/RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md",
        None,
        ("finite_alphabet_dynamics", "history_monoid"),
        ("supplied_carrier", "fixed_K_CPT", "sector_weight_or_dial_choice"),
    ),
    Candidate(
        "FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT",
        "cite_ready_support",
        "docs/FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md",
        None,
        ("finite_alphabet_dynamics",),
        ("weight_reference_choice", "determinant_or_source_surface"),
    ),
    Candidate(
        "FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM",
        "cite_ready_support",
        "docs/FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md",
        None,
        ("finite_alphabet_dynamics",),
        ("determinant_character_authority", "source_action_coupling", "normalization"),
    ),
    Candidate(
        "FLAVOR_LOGDET_FACTOR_2_RECORD_READOUT_REALIZATION",
        "cite_ready_support",
        "docs/FLAVOR_LOGDET_FACTOR_2_RECORD_READOUT_REALIZATION_NARROW_THEOREM_NOTE_2026-06-04.md",
        None,
        ("history_monoid", "finite_alphabet_dynamics"),
        ("coupled_KS_block_decoupling", "component_factorization"),
    ),
    Candidate(
        "OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO",
        "firewall_strengthened",
        "docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md",
        None,
        ("history_monoid", "finite_alphabet_dynamics"),
        ("branch_to_scalar_map",),
    ),
    Candidate(
        "RECORD_P1_DEPENDENCY_AUDIT",
        "firewall_strengthened",
        "docs/RECORD_P1_DEPENDENCY_AUDIT_NOTE_2026-06-04.md",
        None,
        ("finite_alphabet_dynamics",),
        ("old_91_rows_need_broader_parent_content",),
    ),
    Candidate(
        "SOURCE_MEASURE_RECORD_INTERVENTION",
        "probability_or_instrument_blocked",
        "docs/SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md",
        None,
        ("history_monoid",),
        ("physical_source_as_smooth_record_probability_intervention", "independent_audit"),
    ),
    Candidate(
        "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE",
        "probability_or_instrument_blocked",
        "docs/SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md",
        None,
        ("history_monoid",),
        ("probability_geometry", "Fisher_tangent_structure"),
    ),
    Candidate(
        "PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION",
        "probability_or_instrument_blocked",
        "docs/PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md",
        None,
        ("finite_alphabet_dynamics",),
        ("Kraus_family", "Stinespring_isometry"),
    ),
    Candidate(
        "PERSISTENT_RECORD_AS_KRAUS_OPERATOR",
        "probability_or_instrument_blocked",
        "docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md",
        None,
        ("finite_alphabet_dynamics",),
        ("normalized_isometry_W",),
    ),
    Candidate(
        "DM_NEUTRINO_K00_RECORD_INVARIANCE_COMPANION",
        "record_invariant_unchanged",
        "docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md",
        None,
        ("none_needed",),
        ("observable_principle_premise", "source_amplitude_premise"),
    ),
    Candidate(
        "G_BARE_RECORD_INVARIANCE_COMPANION",
        "record_invariant_unchanged",
        "docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md",
        None,
        ("none_needed",),
        ("Ward_identity_chain", "same_1PI_cascade"),
    ),
    Candidate(
        "RECORD_FORMATION_DYNAMICS_CONSTRAINT",
        "formation_or_carrier_dynamics",
        "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        None,
        ("finite_alphabet_dynamics",),
        ("quantum_Darwinism_record_reading", "finite_model_bridge"),
    ),
    Candidate(
        "DYNAMICS_FORM_FROM_RECORD_PRESERVATION",
        "formation_or_carrier_dynamics",
        "docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        None,
        ("finite_alphabet_dynamics",),
        ("two_endpoint_Gauss_bridge", "record_formation_bridge", "couplings_and_truncation"),
    ),
)

EXPECTED_BUCKETS = {
    "cite_ready_support": 4,
    "firewall_strengthened": 2,
    "probability_or_instrument_blocked": 4,
    "record_invariant_unchanged": 2,
    "formation_or_carrier_dynamics": 2,
}


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def git_ref_exists(ref: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{ref}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def main() -> int:
    # ------------------------------------------------------------------
    # 1. Support theorem availability.
    # ------------------------------------------------------------------
    for support_id, path in SUPPORT_NOTES.items():
        check(f"S1 support note exists: {support_id}", (ROOT / path).exists(), path)

    # ------------------------------------------------------------------
    # 2. Candidate existence and branch refs.
    # ------------------------------------------------------------------
    for candidate in CANDIDATES:
        if candidate.local_path is not None:
            check(f"C2 local candidate exists: {candidate.row_id}", (ROOT / candidate.local_path).exists(), candidate.local_path)
        if candidate.branch_ref is not None:
            check(f"C2 branch candidate exists: {candidate.row_id}", git_ref_exists(candidate.branch_ref), candidate.branch_ref)

    # ------------------------------------------------------------------
    # 3. Support and residual discipline.
    # ------------------------------------------------------------------
    known_supports = set(SUPPORT_NOTES) | {"none_needed"}
    for candidate in CANDIDATES:
        check(
            f"D3 support ids known: {candidate.row_id}",
            bool(candidate.citable_support) and set(candidate.citable_support).issubset(known_supports),
            ",".join(candidate.citable_support),
        )
        check(
            f"D3 remaining gates named: {candidate.row_id}",
            bool(candidate.remaining_gates),
            ",".join(candidate.remaining_gates),
        )
        check(
            f"D3 verdict edits forbidden: {candidate.row_id}",
            candidate.verdict_edit_allowed is False,
            "support map only",
        )

    # ------------------------------------------------------------------
    # 4. Bucket accounting.
    # ------------------------------------------------------------------
    observed = {bucket: 0 for bucket in EXPECTED_BUCKETS}
    for candidate in CANDIDATES:
        observed[candidate.bucket] = observed.get(candidate.bucket, 0) + 1
    for bucket, expected in EXPECTED_BUCKETS.items():
        check(f"B4 bucket count {bucket}", observed.get(bucket) == expected, f"observed={observed.get(bucket)} expected={expected}")
    check("B4 total candidates", sum(observed.values()) == 14, f"total={sum(observed.values())}")

    # ------------------------------------------------------------------
    # 5. Migration firewall.
    # ------------------------------------------------------------------
    migrated_old_rows = [c for c in CANDIDATES if c.row_id == "RECORD_P1_DEPENDENCY_AUDIT" and c.bucket != "firewall_strengthened"]
    check("F5 old P1 dependents are not auto-migrated", not migrated_old_rows)
    check(
        "F5 no row claims audit verdict authority",
        all(not c.verdict_edit_allowed for c in CANDIDATES),
    )
    check(
        "F5 companion-only rows do not need new history/count support",
        all(c.citable_support == ("none_needed",) for c in CANDIDATES if c.bucket == "record_invariant_unchanged"),
    )

    print("\n=== Record history/count audit-unlock interpretation ===")
    print("The new history/count dynamics stack creates citation-ready support for finite append/count/coarse-graining rows.")
    print("Rows needing probability, production, source/action, Kraus instruments, or carrier dynamics remain blocked at named gates.")
    print("No audit verdicts or status fields are changed by this support map.")
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
