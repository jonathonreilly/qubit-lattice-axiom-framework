#!/usr/bin/env python3
"""Verify the Kubo Fam2 possible-obstruction inventory note.

This runner intentionally checks both the open-gate prose boundary and the
data-producing refinement packet that supports the Recorded Finite Data table.
"""

from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KUBO_FAM2_NON_CONVERGENCE_NOTE_2026-05-02.md"
REFINEMENT_NOTE_PATH = ROOT / "docs" / "KUBO_FAM2_REFINEMENT_NOTE.md"
REFINEMENT_RUNNER_PATH = ROOT / "scripts" / "kubo_fam2_refinement.py"
REFINEMENT_CACHE_PATH = ROOT / "logs" / "runner-cache" / "kubo_fam2_refinement.txt"
LEGACY_LOG_PATH = ROOT / "logs" / "2026-04-07-kubo-fam2-refinement.txt"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, ok, detail=""):
    global PASS_COUNT, FAIL_COUNT
    tag = "PASS (A)" if ok else "FAIL (A)"
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{tag}] {label}  ({detail})")


def section(title):
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def cache_header(cache_text: str) -> dict[str, str]:
    header, _, _stdout = cache_text.partition("----- stdout -----")
    out: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


section("Part 1: open-gate inventory structure")
note_text = NOTE_PATH.read_text()
refinement_note_text = REFINEMENT_NOTE_PATH.read_text()
refinement_runner_text = REFINEMENT_RUNNER_PATH.read_text()
refinement_cache_text = REFINEMENT_CACHE_PATH.read_text()
legacy_log_text = LEGACY_LOG_PATH.read_text()
required = [
    "Kubo Fam2 Non-Convergence Possible-Obstruction Inventory",
    "open-gate inventory",
    "Source Boundary",
    "Recorded Finite Data",
    "Minimal Local Premises",
    "Forbidden Imports",
    "Claim Boundary",
    "Fam2",
    "Fam1",
    "Fam3",
    "(O1)",
    "(O2)",
    "(O3)",
    "not exhaustive",
    "not a positive convergence theorem",
    "not a no-go theorem",
]
for s in required:
    check(f"contains: {s!r}", s in note_text)

section("Part 2: 3 possible obstruction routes documented")
obstructions = [
    "Parameter-dependent microscopic dynamics",
    "Critical or near-critical parameter regime",
    "Fam2-specific discretization interaction",
]
for o in obstructions:
    check(f"obstruction: {o[:50]}",
          o in note_text)

section("Part 3: Fam parameters enumerated")
fam_params = [
    "drift=0.20, restore=0.70",  # Fam1
    "drift=0.05, restore=0.30",  # Fam2
    "drift=0.50, restore=0.90",  # Fam3
]
for fp in fam_params:
    check(f"family parameter: {fp}", fp in note_text)

section("Part 4: explicit non-closure and non-exhaustiveness")
non_closures = [
    "does not resolve Fam2 non-convergence",
    "does not prove an exhaustive obstruction trichotomy",
    "does not prove a continuum limit for Fam2",
    "does not alter the status of any parent Kubo-family evidence",
]
for nc in non_closures:
    check(f"non-closure: {nc}", nc in note_text)

section("Part 5: open-gate closeout labels")
closeout_requirements = [
    "**Type:** open_gate",
    "This is an open gate for future Kubo Fam2 work",
    "unique Fam2 mechanism",
]
for label in closeout_requirements:
    check(f"status label: {label}", label in note_text)

section("Part 6: data-producing refinement packet exposed")
path_requirements = [
    "scripts/kubo_fam2_refinement.py",
    "logs/runner-cache/kubo_fam2_refinement.txt",
    "logs/2026-04-07-kubo-fam2-refinement.txt",
    "docs/KUBO_FAM2_REFINEMENT_NOTE.md",
]
for rel in path_requirements:
    check(f"note links data path: {rel}", rel in note_text)

source_markers = [
    "AUDIT_TIMEOUT_SEC = 1800",
    "from kubo_continuum_limit import",
    "grow, true_kubo_at_H, finite_diff_dM",
    "def measure(H_val)",
    "measure(0.20)",
]
for marker in source_markers:
    check(f"refinement source marker: {marker}", marker in refinement_runner_text)

header = cache_header(refinement_cache_text)
current_sha = sha256_file(REFINEMENT_RUNNER_PATH)
check(
    "refinement cache runner",
    header.get("runner") == "scripts/kubo_fam2_refinement.py",
    header.get("runner", ""),
)
check(
    "refinement cache SHA fresh",
    header.get("runner_sha256") == current_sha,
    f"cache={header.get('runner_sha256')} current={current_sha}",
)
check(
    "refinement cache exit ok",
    header.get("exit_code") == "0" and header.get("status") == "ok",
    f"exit_code={header.get('exit_code')} status={header.get('status')}",
)

section("Part 7: Recorded Finite Data table supported by refinement output")
data_requirements = [
    ("Fam2 H=0.50", "H=0.500  kubo_true = +6.6588", "+6.6588` at `H=0.50`"),
    ("Fam2 H=0.35", "H=0.350  kubo_true = +6.3168", "+6.3168` at `H=0.35`"),
    ("Fam2 H=0.25", "H=0.250  kubo_true = +7.0883", "+7.0883` at `H=0.25`"),
    ("Fam2 H=0.20", "H=0.200  NL=75  n_nodes=275355  kubo_true = +4.5082", "+4.5082` at `H=0.20`"),
    ("Fam1/Fam3 comparator", "Fam1/Fam3 converged value (H=0.25): ~+5.97", "settles near `+5.97`"),
    ("Fam1/Fam3 deviation", "Fam2 deviation from Fam1/Fam3 target: 1.4618 (24.5%)", "Fam1/Fam3 sampled value"),
]
for label, cache_snippet, note_snippet in data_requirements:
    check(f"cache supports {label}", cache_snippet in refinement_cache_text or cache_snippet in legacy_log_text)
    check(f"note records {label}", note_snippet in note_text)

refinement_note_requirements = [
    "Full Fam2 series across four refinements",
    "Fam2 at H=0.20",
    "The Fam2 series is",
    "does **not** prove literal divergence",
]
for req in refinement_note_requirements:
    check(f"refinement note contains: {req}", req in refinement_note_text)

section("Part 8: re-audit trigger guard")
note_flat = " ".join(note_text.split())
trigger_guard_requirements = [
    "Re-Audit Trigger Guard",
    "source-bound to the two current Kubo parent/context packets",
    "SHA-pinned Fam2 refinement cache",
    "KUBO_CONTINUUM_LIMIT_FAMILIES_NOTE.md",
    "KUBO_FAM2_REFINEMENT_NOTE.md",
    "scripts/kubo_fam2_refinement.py",
    "logs/runner-cache/kubo_fam2_refinement.txt",
    "effective retained_bounded status",
    "requires re-audit before downstream use",
]
for req in trigger_guard_requirements:
    check(f"re-audit trigger guard contains: {req}", req in note_flat)

freshness_boundary_requirements = [
    "stale, refreshed, or",
    "no longer supports the finite Fam2 values recorded here",
    "does not promote the row",
    "parent/context movement or cached-data movement",
]
for req in freshness_boundary_requirements:
    check(f"freshness boundary contains: {req}", req in note_flat)

print(f"\n{'='*88}\n  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}\n{'='*88}")
if FAIL_COUNT == 0:
    print("KUBO_FAM2_POSSIBLE_OBSTRUCTION_INVENTORY=TRUE")
    print("OPEN_GATE_DOCUMENTED=TRUE")
    print("EXHAUSTIVE_TRICHOTOMY_CLAIMED=FALSE")
    print("FAM2_NON_CONVERGENCE_RESOLVED=FALSE")
    print("OBSERVED_OR_FITTED_TARGET_CONSUMED=FALSE")
sys.exit(1 if FAIL_COUNT > 0 else 0)
