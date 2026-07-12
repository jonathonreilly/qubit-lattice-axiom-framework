#!/usr/bin/env python3
"""Audit-prep verifier for dm_leptogenesis_exact_kernel_closure_note_2026-04-15.

Verifies docs/DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md.

Programmatic checks:
  - The parent note exists at the expected path.
  - CITED deps (>=1 hit, classification deferred to audit-lane judgment based on context).
  - NOT-CITED deps (0 hits, programmatically certain).
"""

from __future__ import annotations

import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0}

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_PATH = REPO_ROOT / "docs/DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md"
sys.path.insert(0, str(REPO_ROOT / "docs/audit/scripts"))
from audit_lint import markdown_link_targets as rendered_markdown_link_targets  # noqa: E402

CITED_DEPS = [
    "MINIMAL_AXIOMS_2026-06-29.md",
]

NOT_CITED_DEPS = [
    "dm_neutrino_codd_bosonic_normalization_theorem_note_2026-04-15",
    "dm_neutrino_veven_bosonic_normalization_theorem_note_2026-04-15",
    "dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15",
    "dm_leptogenesis_ne_active_column_axiom_boundary_note_2026-04-16",
    "dm_leptogenesis_ne_charged_source_response_reduction_note_2026-04-16",
    "dm_leptogenesis_ne_projected_source_law_derivation_note_2026-04-16",
    "dm_leptogenesis_ne_projected_source_triplet_sign_theorem_note_2026-04-16",
    "dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16",
    "dm_leptogenesis_pmns_cp_bridge_boundary_note_2026-04-16",
    "dm_leptogenesis_transport_status_note_2026-04-16",
    "dm_pmns_graph_first_ordered_chain_nonzero_current_activation_theorem_note_2026-04-21",
    "dm_wilson_to_dweh_hermitian_source_family_target_note_2026-04-18",
    "dm_wilson_to_dweh_local_chain_path_algebra_target_note_2026-04-18",
    "lepton_shared_higgs_universality_collapse_note",
    "lepton_single_higgs_pmns_triviality_note",
    "neutrino_dirac_two_higgs_canonical_reduction_note",
    "neutrino_mass_reduction_to_dirac_note",
    "neutrino_two_amplitude_last_mile_reduction_note",
    "pmns_active_four_real_source_from_transport_note",
    "pmns_c3_character_mode_reduction_note",
    "pmns_c3_nontrivial_current_boundary_note",
    "pmns_corner_transport_active_block_note",
    "pmns_current_bank_value_selection_nogo_note",
    "pmns_oriented_cycle_reduced_channel_nonselection_note",
    "pmns_selector_class_space_uniqueness_note",
    "pmns_selector_nonuniversal_support_reduction_note",
    "pmns_selector_sign_to_branch_reduction_note",
    "pmns_selector_unique_amplitude_slot_note",
    "publication.ci3_z3.publication_matrix",
]


def check(label: str, condition: bool, detail: str = "", cls: str = "B") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[cls] = CLASS_COUNTS.get(cls, 0) + 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{cls}] {status}: {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def markdown_link_targets(content: str) -> list[str]:
    surface = PARENT_PATH.relative_to(REPO_ROOT).as_posix()
    return sorted(rendered_markdown_link_targets(surface, content))


def target_key(target: str) -> str:
    path = target.strip().strip("<>").split("#", 1)[0].split("?", 1)[0]
    return Path(path).stem.lower()


def main() -> int:
    print("=" * 78)
    print("AUDIT-PREP VERIFIER — dm_leptogenesis_exact_kernel_closure_note_2026-04-15")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    targets = markdown_link_targets(content)
    target_keys = [target_key(target) for target in targets]
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")
    check(
        "Markdown parser ignores a bare filename that is not a link target",
        markdown_link_targets("MINIMAL_AXIOMS_2026-06-29.md is not cited") == [],
        cls="A",
    )
    check(
        "Markdown parser extracts a real dependency link target",
        markdown_link_targets("[axioms](MINIMAL_AXIOMS_2026-06-29.md)")
        == ["docs/MINIMAL_AXIOMS_2026-06-29.md"],
        cls="A",
    )
    check(
        "Markdown parser ignores code-fenced, inline-code, and image pseudo-links",
        markdown_link_targets(
            "`[inline](MINIMAL_AXIOMS_2026-06-29.md)`\n"
            "```md\n[fenced](MINIMAL_AXIOMS_2026-06-29.md)\n```\n"
            "![image](MINIMAL_AXIOMS_2026-06-29.md)\n"
        )
        == [],
        cls="A",
    )
    print()

    print(f"PART 1 — CITED deps (expect: >=1 hit each):")
    for dep in CITED_DEPS:
        n = target_keys.count(Path(dep).stem.lower())
        check(
            f"  {dep} IS cited (>=1 hit)",
            n >= 1,
            f"hits = {n}",
        )

    print()
    print(f"PART 2 — NOT-CITED deps (expect: 0 hits each):")
    for dep in NOT_CITED_DEPS:
        n = target_keys.count(dep.split(".")[-1].lower())
        check(
            f"  {dep} NOT cited (0 hits)",
            n == 0,
            f"hits = {n}",
        )

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    breakdown = ", ".join(f"class {key}: {value}" for key, value in sorted(CLASS_COUNTS.items()))
    print(f"CLASS BREAKDOWN: {breakdown}")
    print("=" * 78)

    if FAIL_COUNT == 0:
        print()
        print("VERIFIED")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
