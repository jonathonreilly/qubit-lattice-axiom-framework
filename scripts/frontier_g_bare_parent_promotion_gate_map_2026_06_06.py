#!/usr/bin/env python3
"""Verify the branch-local g_bare parent-promotion gate map.

The runner checks source-surface predicates for the route:

    conditional algebra core + L3 invariance => parent promotion

It should fail if the active queue, parent note, or promotion-panel finding no
longer support the branch-local no-go classification.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

ACTIVE_QUEUE = ROOT / "docs" / "repo" / "ACTIVE_REVIEW_QUEUE.md"
PARENT_NOTE = ROOT / "docs" / "G_BARE_DERIVATION_NOTE.md"
PANEL_NOTE = ROOT / "docs" / "audit" / "G_BARE_PROMOTION_PANEL_FINDING_2026-05-28.md"
GATE_NOTE = ROOT / "docs" / "G_BARE_PARENT_PROMOTION_GATE_MAP_NOTE_2026-06-06.md"
RESCALING_NOTE = ROOT / "docs" / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"
CONSTRAINT_NOTE = ROOT / "docs" / "G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, ok, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title):
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def contains_all(text, snippets):
    return all(snippet in text for snippet in snippets)


active_text = ACTIVE_QUEUE.read_text()
parent_text = PARENT_NOTE.read_text()
panel_text = PANEL_NOTE.read_text()
gate_text = GATE_NOTE.read_text()

section("Part 1: active review gate is present")

check(
    "active queue contains the g_bare parent gate id",
    "2026-05-03-gbare-parent-retention-gate" in active_text,
)
check(
    "active queue scopes G_BARE_DERIVATION_NOTE and downstream g_bare surfaces",
    contains_all(active_text, ["G_BARE_DERIVATION_NOTE.md", "downstream `g_bare = 1`"]),
)
check(
    "active queue requires independent audit of both candidate rows",
    contains_all(
        active_text,
        [
            "candidate rows must be independently audited and retained",
            "retained\n  dependency closure",
        ],
    ),
)
check(
    "active queue disposition remains science-needed",
    "Disposition: `science-needed`" in active_text,
)

section("Part 2: parent note carries dependency-chain gate")

parent_required = [
    "Parent dependency-chain gate",
    "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md",
    "G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md",
    "parent re-audit required",
    "not a retained-status\npromotion",
    "canonical normalization itself remains the admitted\nupstream convention layer",
    "not a dynamical calculation",
    "not a fit",
    "not a\nfixed-point condition",
]
for snippet in parent_required:
    display_snippet = snippet.replace("\n", "\\n")
    check(f"parent note contains: {display_snippet}", snippet in parent_text)

check("rescaling repair candidate exists", RESCALING_NOTE.exists(), detail=str(RESCALING_NOTE))
check("constraint/convention repair candidate exists", CONSTRAINT_NOTE.exists(), detail=str(CONSTRAINT_NOTE))

section("Part 3: promotion panel identifies the blocking premise")

panel_required = [
    "Do NOT promote",
    "N_F = 1/2",
    "CONVENTION",
    "single load-bearing admission",
    "invariance, not uniqueness",
    "does NOT close the L3b admission",
    "per-site SU(2)",
    "gauge su(3) lives on `V_3 = C^3`",
    "staggered-Dirac realization gate",
    "conditional** algebraic core",
    "No further promotion is needed there",
]
for snippet in panel_required:
    check(f"promotion panel contains: {snippet}", snippet in panel_text)

section("Part 4: logical gate classifier")

source_state = {
    "conditional_algebra_core_available": contains_all(
        panel_text,
        ["conditional** algebraic core", "No further promotion is needed there"],
    ),
    "candidate_rows_identified": RESCALING_NOTE.exists() and CONSTRAINT_NOTE.exists(),
    "parent_reaudit_required": "parent re-audit required" in parent_text,
    "canonical_normalization_admitted": "admitted upstream convention layer" in parent_text,
    "nf_forced_by_baseline": not contains_all(
        panel_text,
        ["unconditional statement", "is not available", "`N_F` is a genuine free\nconvention"],
    ),
    "l3_invariance_implies_uniqueness": not contains_all(
        panel_text,
        ["invariance, not uniqueness", "does NOT close the L3b admission"],
    ),
    "staggered_dirac_gate_closed": not contains_all(
        panel_text,
        ["requires the staggered-Dirac\nrealization gate", "Until that gate\ncloses"],
    ),
}

parent_promotion_allowed = (
    source_state["conditional_algebra_core_available"]
    and source_state["candidate_rows_identified"]
    and not source_state["parent_reaudit_required"]
    and not source_state["canonical_normalization_admitted"]
    and source_state["nf_forced_by_baseline"]
    and source_state["l3_invariance_implies_uniqueness"]
    and source_state["staggered_dirac_gate_closed"]
)

check("conditional algebra core is available", source_state["conditional_algebra_core_available"])
check("both repair candidate files are present", source_state["candidate_rows_identified"])
check("parent re-audit is still required", source_state["parent_reaudit_required"])
check("canonical normalization is still admitted upstream", source_state["canonical_normalization_admitted"])
check("N_F forced by baseline is false on current panel surface", not source_state["nf_forced_by_baseline"])
check("L3 invariance does not imply uniqueness", not source_state["l3_invariance_implies_uniqueness"])
check("staggered-Dirac gate is not treated as closed", not source_state["staggered_dirac_gate_closed"])
check("parent promotion route is blocked", not parent_promotion_allowed)

section("Part 5: branch-local note hygiene")

gate_required = [
    "branch-local no-go gate map",
    "negative route pruning",
    "conditional algebra core + L3 invariance => parent promotion",
    "is blocked on the current surface",
    "No repo-wide audit verdict is applied here",
    "No claim is made that `g_bare = 1` is false",
]
for snippet in gate_required:
    check(f"gate note contains: {snippet}", snippet in gate_text)

banned_overclaims = [
    "retained branch-local",
    "would become retained",
    "promoted to retained",
    "retained on the actual surface",
    "full retained at this time",
]
for phrase in banned_overclaims:
    check(f"gate note avoids banned phrase: {phrase}", phrase not in gate_text)

print("\n" + "=" * 88)
print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
print("=" * 88)

sys.exit(1 if FAIL_COUNT else 0)
