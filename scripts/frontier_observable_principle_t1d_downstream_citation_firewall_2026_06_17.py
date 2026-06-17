#!/usr/bin/env python3
"""Source-side citation firewall for the observable-principle T1-d boundary."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"

PASS = 0
FAIL = 0

FORBIDDEN = [
    "retained observable principle",
    "retained log|det|",
    "retained `log|det|",
    "retained scalar observable principle",
    "retained axiom-native scalar generator",
    "THE retained additive CPT-even",
    "Observable-principle (retained)",
    "retained observable-principle authority",
]

REQUIRED_FILES = [
    "docs/NEUTRINO_MAJORANA_CURRENT_ATLAS_NONREALIZATION_NOTE.md",
    "docs/SIGNED_GRAVITY_CL3Z3_SOURCE_CHARACTER_DERIVATION_NOTE.md",
    "docs/SIGNED_GRAVITY_NATURALLY_HOSTED_ORIENTATION_LINE_NOTE.md",
    "docs/SIGNED_GRAVITY_SOURCE_CHARACTER_UNIQUENESS_THEOREM_NOTE.md",
    "docs/DM_NEUTRINO_SOURCE_SURFACE_PERTURBATIVE_UNIQUENESS_THEOREM_NOTE_2026-04-17.md",
    "docs/KOIDE_A1_PROBE_RP_FROBENIUS_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe1.md",
    "docs/HIGHER_ORDER_STRUCTURAL_THEOREMS_NOTE.md",
    "docs/KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md",
    "docs/SCALAR_SELECTOR_REVIEWER_PACKAGE_2026-04-20.md",
    "scripts/frontier_koide_a1_block_democracy_max_entropy.py",
    "scripts/frontier_koide_cone_variational_principle_survey.py",
    "scripts/frontier_koide_moment_ratio_uniformity_theorem.py",
    "scripts/frontier_koide_a1_quartic_potential_derivation.py",
    "scripts/frontier_koide_cone_real_irrep_democracy.py",
    "scripts/frontier_koide_a1_physical_bridge_attempt_nogo_2026_04_22.py",
    "scripts/signed_gravity_cl3z3_source_character_derivation.py",
]


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name}")
    if detail:
        print(f"      {detail}")
    PASS += int(condition)
    FAIL += int(not condition)
    return condition


def source_files() -> list[Path]:
    files: list[Path] = []
    for root in [DOCS, SCRIPTS]:
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("docs/audit/"):
                continue
            if rel.startswith("docs/ai_methodology/raw/"):
                continue
            if rel.startswith("docs/publication/"):
                continue
            if rel == "docs/OBSERVABLE_PRINCIPLE_T1D_DOWNSTREAM_CITATION_FIREWALL_2026-06-17.md":
                continue
            if rel == "scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py":
                continue
            if path.suffix not in {".md", ".py"}:
                continue
            files.append(path)
    return files


def part0_parent_boundary() -> None:
    print("\n== Part 0: parent boundary is still conditional ==")
    parent = (DOCS / "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md").read_text(encoding="utf-8")
    no_go = (DOCS / "OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md").read_text(
        encoding="utf-8"
    )
    note = (DOCS / "OBSERVABLE_PRINCIPLE_T1D_DOWNSTREAM_CITATION_FIREWALL_2026-06-17.md").read_text(
        encoding="utf-8"
    )

    check("parent declares T1-d as a Boundary", "Boundary (declared bridge premise, T1-d)" in parent)
    check("parent says T1-d is not derivable from minimal_axioms", "not derivable" in parent and "minimal_axioms" in parent)
    check("T1-d no-go says consumers must not treat T1-d as Record-derived", "must not treat T1-d as Record-derived" in no_go)
    check("firewall note says it does not add an axiom or retag audit rows", "does not derive T1-d" in note and "retag any audit row" in note)


def part1_required_files_scoped() -> None:
    print("\n== Part 1: targeted source consumers are scoped ==")
    for rel in REQUIRED_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        check(f"{rel} contains conditional T1-d wording", "conditional T1-d" in text)
        for phrase in FORBIDDEN:
            check(f"{rel} avoids forbidden phrase: {phrase}", phrase not in text)


def part2_repo_scan() -> None:
    print("\n== Part 2: current source scan excludes retained-logdet laundering ==")
    hits: list[str] = []
    for path in source_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT).as_posix()
        for phrase in FORBIDDEN:
            if phrase in text:
                hits.append(f"{rel}: {phrase}")
    check("no current non-audit/non-publication source file uses forbidden retained observable/logdet phrases", not hits, "\n".join(hits[:20]))

    raw = DOCS / "ai_methodology/raw/claude_subagent_dispatches.md"
    raw_text = raw.read_text(encoding="utf-8")
    check(
        "archival raw dispatch text is intentionally excluded from source firewall",
        "retained observable principle" in raw_text,
        "raw transcript remains historical, not source authority",
    )


def main() -> int:
    print("OBSERVABLE-PRINCIPLE T1-d DOWNSTREAM CITATION FIREWALL")
    part0_parent_boundary()
    part1_required_files_scoped()
    part2_repo_scan()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: observable-principle T1-d downstream citation firewall passes.")
        return 0
    print("VERDICT: observable-principle T1-d downstream citation firewall FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
