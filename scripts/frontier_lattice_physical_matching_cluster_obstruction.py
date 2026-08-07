#!/usr/bin/env python3
"""Verify the lattice→physical matching cluster obstruction synthesis."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md"

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


section("Part 1: cluster note structure")
note_text = NOTE_PATH.read_text()
required = [
    "Lattice → Physical Matching Cluster Obstruction Theorem",
    "named-obstruction synthesis theorem",
    "yt_ew matching rule M",
    "gauge-scalar observable bridge",
    "Higgs mass from axiom",
    "(O1) Schwinger-Dyson",
    "(O2) Effective-action",
    "(O3) Renormalization-group",
    "Nature-grade target",
    "proposal_allowed: false",
]
for s in required:
    check(f"contains: {s!r}", s in note_text)

section("Part 2: 3 sister cycles cited")
sister_prs = ["#260", "#268", "#271"]
for pr in sister_prs:
    check(f"sister PR: {pr}", pr in note_text)

sister_cycles = ["Cycle 5", "Cycle 9", "Cycle 11"]
for c in sister_cycles:
    check(f"sister cycle: {c}", c in note_text)

section("Part 3: 3 resolution routes documented")
resolutions = [
    "Resolution A:",
    "Resolution B:",
    "Resolution C:",
    "novel non-perturbative matching theorem",
    "renormalization-scheme classification",
    "lattice MC computation",
]
for r in resolutions:
    check(f"resolution path: {r}",
          r in note_text)

section("Part 4: A_min and forbidden imports")
amin = [
    "graph-first SU(N_c) integration",
    "Wilson gauge action",
    "1/N_c topological expansion",
    "Fierz identity",
    "OZI rule",
]
for a in amin:
    check(f"A_min: {a}", a in note_text)

forbidden = [
    "PDG observed values",
    "Lattice MC empirical",
    "Fitted matching coefficients",
]
for f in forbidden:
    check(f"forbidden: {f}", f in note_text)

section("Part 5: N5 execution certificate (print-only; adds no check)")

print(
    "  Nature of this runner: it is a synthesis verifier for the cluster note.\n"
    "  Every one of its checks is a substring-presence test against\n"
    "  docs/LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md.\n"
    "  It constructs no matrix, no field, no lattice, and evaluates no\n"
    "  amplitude at any granularity. The five lines below record that\n"
    "  honestly rather than implying resolution the runner does not perform.\n"
)
print(
    "per_element: checked and not executed - the runner never builds an "
    "operator or a kernel, so there is no matrix element to evaluate; its "
    "checks read text. The element-level object the cluster would need is "
    "exactly route (O1), and the note's own finding is that the kernel-level "
    "identities (Fierz, K_O reduction, dimensional analysis) do not by "
    "themselves give the operator-level relation."
)
print(
    "per_site: checked and not executed - no site-resolved field is "
    "instantiated; the runner opens one markdown file and asserts the presence "
    "of fixed strings. A site-resolved quantity here would have to come from "
    "the lattice MC of route (O3) / Resolution C, and lattice MC empirical "
    "measurements are listed among this note's forbidden imports, allowed only "
    "as audit comparators."
)
print(
    "per_mode: checked and not executed - nothing in this runner forms a mode, "
    "a momentum or a harmonic. The only expansion the cluster carries is the "
    "'t Hooft 1/N_c topological expansion, which is organized by genus rather "
    "than by mode and is cited in the note as prose (bounded support at "
    "O(1/N_c^4), about 1.2% at N_c = 3) rather than evaluated anywhere here."
)
print(
    "per_block: checked and not executed as an operator-block resolution - no "
    "colour, flavour or isotype block is ever constructed. The only counting "
    "the runner does is documentary: 3 sister cycles (5, 9, 11), 3 sister PRs "
    "(#260, #268, #271), 3 failure routes (O1, O2, O3), 3 resolution routes "
    "(A, B, C), 5 A_min premises and 3 forbidden imports, all confirmed by "
    "string presence in the note and not by any computation on a block."
)
print(
    "lattice_wide: checked and not executed - despite the word Lattice in the "
    "title no lattice is instantiated and no extensive expectation is formed; "
    "<P> and beta_eff occur only as characters inside the note text. That is "
    "the point of the cluster obstruction: the exact bridge "
    "<P>_full = R_O(beta_eff) is precisely what route (O3) says requires "
    "lattice MC at the relevant beta, so this runner deliberately computes no "
    "lattice-wide quantity."
)

print(f"\n{'='*88}\n  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}\n{'='*88}")
sys.exit(1 if FAIL_COUNT > 0 else 0)
