#!/usr/bin/env python3
"""Graph-braid Z3 anyon-exclusion dependency-surface hygiene companion.

Meta evidence only. This runner checks that the non-load-bearing
statistics-agnostic context no longer seeds a Markdown dependency, and that the
parent runner cache matches the current parent runner.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py"
PARENT_CACHE = REPO_ROOT / "logs" / "runner-cache" / "graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.txt"
COMPANION_NOTE = REPO_ROOT / "docs" / "GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"

WEAK_CONTEXT_NOTE = "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md"
WEAK_CONTEXT_STEM = "staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25"
GRADE_TOKENS = (
    "audit" + "_status",
    "effective" + "_status",
    "intrinsic" + "_status",
    "retained_" + "bounded",
    "retained_" + "no_go",
    "audited_" + "clean",
    "audited_" + "conditional",
)

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def section(text: str, start: str, end_markers: tuple[str, ...]) -> str:
    start_idx = text.find(start)
    if start_idx == -1:
        return ""
    end = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx + len(start))
        if idx != -1 and idx < end:
            end = idx
    return text[start_idx:end]


def main() -> int:
    print("=" * 72)
    print("Graph-braid Z3 anyon-exclusion dependency-surface hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md")
    print("Parent runner: scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py")
    print("Parent cache: logs/runner-cache/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.txt")
    print("Scope: meta evidence only; no new no-go, no audit verdict, no direct status change.")

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    runner_text = PARENT_RUNNER.read_text(encoding="utf-8")
    cache_text = PARENT_CACHE.read_text(encoding="utf-8")
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()

    load_bearing = section(parent_text, "## Load-Bearing Dependencies", ("\n## Non-Load-Bearing Context", "\n## Boundaries"))
    non_load_bearing = section(parent_text, "## Non-Load-Bearing Context", ("\n## Boundaries", "\n## NO NEW ADMISSIONS"))

    record("load_bearing_section_present", len(load_bearing) > 100)
    record("non_load_bearing_section_present", len(non_load_bearing) > 100)
    record("weak_context_absent_from_load_bearing_section", WEAK_CONTEXT_NOTE not in load_bearing)
    record("weak_context_present_in_non_load_bearing_section", WEAK_CONTEXT_NOTE in non_load_bearing)
    markdown_link = f"]({WEAK_CONTEXT_NOTE})"
    record("weak_context_not_markdown_linked", markdown_link not in parent_text)
    record("weak_context_plain_text_marker_present", f"`{WEAK_CONTEXT_NOTE}`" in parent_text)
    record("non_load_bearing_tier_disclaimer_present", "nothing here depends on its tier" in non_load_bearing)

    runner_hash = sha256(PARENT_RUNNER)
    hash_match = re.search(r"runner_sha256:\s*([0-9a-f]+)", cache_text)
    record("parent_cache_records_runner_hash", hash_match is not None)
    record("parent_cache_hash_matches_runner", bool(hash_match and hash_match.group(1) == runner_hash))
    record("parent_cache_exit_code_zero", "exit_code: 0" in cache_text)
    record("parent_cache_status_ok", "status: ok" in cache_text)
    record("parent_cache_scorecard_pass_25_fail_0", "SCORECARD: PASS=25 FAIL=0" in cache_text)

    for phrase in [
        "H_1 = Z^6 (+) Z_2",
        "H_1 = Z^4 (+) Z_2",
        "Z^3 cube L=3: NON-PLANAR",
        "Z^3 cube L=4: NON-PLANAR",
        "does NOT select boson vs fermion",
        "does NOT settle the open second-quantized",
    ]:
        record(f"parent_cache_contains_{re.sub(r'[^A-Za-z0-9]+', '_', phrase).strip('_')}", phrase in cache_text)

    for idx, token in enumerate(GRADE_TOKENS):
        record(f"parent_runner_source_no_grade_token_{idx}", token not in runner_text)
    record("parent_runner_source_no_weak_context_stem", WEAK_CONTEXT_STEM not in runner_text)

    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_no_go", "does not add a new no-go" in companion_text)
    record("companion_disclaims_direct_status_change", "not a direct status change" in companion_text)
    record("companion_explains_cache_reason", "lacks `networkx`" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
