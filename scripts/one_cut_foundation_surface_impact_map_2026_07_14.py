#!/usr/bin/env python3
"""Read-only impact map for a possible synchronized foundation cut."""

from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ONE_CUT_FOUNDATION_SURFACE_IMPACT_MAP_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CANONICAL = (
    AXIOMS,
    REGISTRY,
    ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md",
    ROOT / "scripts" / "audit_companion_minimal_axioms_clean_base_exact.py",
    ROOT / "docs" / "repo" / "CONTROLLED_VOCABULARY.md",
    ROOT / "docs" / "repo" / "controlled_vocabulary.yaml",
)
PHRASES = {
    "admissibility_exact": "There is one fixed nearest-neighbor admissibility rule",
    "availability_only": "Admissibility is not a dynamics axiom",
    "record_occurrence": "Records form.",
    "four_axiom_list": "Lattice, Qubit, Admissibility, and Record",
}
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def candidate_files():
    extensions = {".md", ".py", ".json", ".yaml", ".yml", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in extensions:
            continue
        relative = path.relative_to(ROOT)
        parts = relative.parts
        if not parts or parts[0] in {".git", "logs"}:
            continue
        if "__pycache__" in parts or "work_history" in parts:
            continue
        yield path


def scan():
    matches = defaultdict(list)
    for path in candidate_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for key, phrase in PHRASES.items():
            if phrase in text:
                matches[key].append(path)
    return matches


def category(path: Path) -> str:
    if path in CANONICAL:
        return "canonical"
    relative = path.relative_to(ROOT)
    if relative.parts[0] == "scripts":
        return "runner_or_guard"
    if relative.parts[:2] == ("docs", "audit"):
        return "audit_owned_or_policy"
    return "current_or_historical_source"


def main() -> int:
    print("=" * 79)
    print("A - Canonical synchronized surfaces")
    print("=" * 79)
    for path in CANONICAL:
        check(f"canonical source exists: {path.relative_to(ROOT)}", path.is_file())

    note = NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "")
    check("impact note is authority-free", "authority: none" in note)
    check("impact note forbids bulk replacement", "not a mechanical replacement list" in note)
    check("impact note separates audit-owned outputs", "audit-owned" in note and "must not" in note)

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check("stable minimal_axioms id remains", "minimal_axioms" in registry.get("canonical_ids", ()))
    check("current path remains the live memo", registry["nodes"]["minimal_axioms"]["current_path"] == "docs/MINIMAL_AXIOMS_2026-06-29.md")

    axioms = AXIOMS.read_text(encoding="utf-8")
    check("live axioms have no placeholder", "[CANONICAL-LAW]" not in axioms and "canonical-law" not in axioms.lower())

    print("\n" + "=" * 79)
    print("B - Exact-string impact census")
    print("=" * 79)
    matches = scan()
    minimums = {
        "admissibility_exact": 26,
        "availability_only": 16,
        "record_occurrence": 55,
        "four_axiom_list": 35,
    }
    for key, paths in matches.items():
        check(f"{key} census is at least the July-14 baseline", len(paths) >= minimums[key], str(len(paths)))
        grouped = defaultdict(list)
        for path in paths:
            grouped[category(path)].append(path.relative_to(ROOT))
        for group in sorted(grouped):
            print(f"{key} [{group}] {len(grouped[group])}")
            for relative in sorted(grouped[group]):
                print(f"  {relative}")

    print("\n" + "=" * 79)
    print("TOTAL")
    print("=" * 79)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: read-only impact map; no foundation, audit, registry, or verdict mutation")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
