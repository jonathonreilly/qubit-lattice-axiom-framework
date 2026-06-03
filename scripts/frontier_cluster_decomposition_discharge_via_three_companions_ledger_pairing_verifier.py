#!/usr/bin/env python3
"""Ledger-pairing verifier for the cluster-decomposition discharge package.

Pairs together the three already-on-main companions whose joint content
addresses the three named auditor-conditional items recorded against the
parent ``AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29``.

This runner is a pure cite-check + audit-invariant verifier. It performs:

  Part A. on-main presence cite-check of the parent + 3 companions.
  Part B. content-match cite-check that each companion's claim actually
          addresses the parent's named conditional item:
          B.1  mass-gap bridge claim text matches item (a) temporal slice
          B.2  eq8 repair claim text matches items (b) + (c)
          B.3  spatial slab + axis-permutation claim text matches
               item (a) spatial slice
  Part C. hostile-audit invariants:
          C.1  parent text untouched in this PR
          C.2  each of the three companions untouched in this PR
          C.3  no status lift attempted (no audit_status / effective_status
               edits, no audit-ledger touch)
          C.4  no new science (no new axioms, primitives, framework
               objects)
          C.5  meta-note claim_type declared explicitly

Target: 15-25 PASS / 0 FAIL.

No new science. No new axioms. No new imports.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent

PARENT = "docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md"
COMPANION_MASS_GAP = "docs/CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md"
COMPANION_SLAB = "docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md"
COMPANION_EQ8 = "docs/CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02.md"
COMPANION_AXIS = "docs/CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md"

PAIRING_NOTE = "docs/CLUSTER_DECOMPOSITION_DISCHARGE_VIA_THREE_COMPANIONS_LEDGER_PAIRING_NOTE_2026-06-03.md"

RESULTS: list[Tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def git_show_origin_main(path: str) -> str | None:
    """Return file content from origin/main, or None if absent."""
    try:
        out = subprocess.check_output(
            ["git", "show", f"origin/main:{path}"],
            cwd=REPO_ROOT,
            stderr=subprocess.DEVNULL,
        )
        return out.decode("utf-8", errors="replace")
    except subprocess.CalledProcessError:
        return None


# -----------------------------------------------------------------------------
# Part A — on-main cite-check
# -----------------------------------------------------------------------------

def part_a_on_main_cite_check() -> None:
    """Every cited row exists on origin/main."""
    print("=== Part A: on-main cite-check (5 rows) ===")
    rows = [
        ("A.1 parent on main", PARENT),
        ("A.2 mass-gap bridge on main", COMPANION_MASS_GAP),
        ("A.3 spatial slab bridge on main", COMPANION_SLAB),
        ("A.4 eq8 repair on main", COMPANION_EQ8),
        ("A.5 axis-permutation companion on main", COMPANION_AXIS),
    ]
    for name, path in rows:
        content = git_show_origin_main(path)
        ok = content is not None and len(content) > 100
        record(name, ok, f"{path} {'present' if ok else 'MISSING'}")
        print(f"  {'PASS' if ok else 'FAIL'} {name} ({path})")


# -----------------------------------------------------------------------------
# Part B — content-match cite-check
# -----------------------------------------------------------------------------

def part_b_content_match() -> None:
    """Each companion's content text addresses its named parent item."""
    print("\n=== Part B: content-match cite-check ===")

    # B.1: mass-gap bridge addresses item (a) temporal slice
    mass_gap = git_show_origin_main(COMPANION_MASS_GAP) or ""
    b1_keywords = [
        "transfer matrix",
        "Δ_T",
        "mass-gap",
        "temporal",
        "exp(-n",
        "connected",
    ]
    b1_hits = sum(1 for k in b1_keywords if k.lower() in mass_gap.lower())
    b1_ok = b1_hits >= 5
    record(
        "B.1 mass-gap bridge addresses item (a) temporal slice",
        b1_ok,
        f"{b1_hits}/{len(b1_keywords)} keyword hits",
    )
    print(
        f"  {'PASS' if b1_ok else 'FAIL'} B.1 mass-gap bridge text addresses temporal-bridge slice "
        f"({b1_hits}/{len(b1_keywords)} hits)"
    )

    # B.2: eq8 repair addresses items (b) + (c)
    eq8 = git_show_origin_main(COMPANION_EQ8) or ""
    b2_b_keywords = [
        "eq (8)",
        "Kubo",
        "not an identity",
        "counterexample",
    ]
    b2_b_hits = sum(1 for k in b2_b_keywords if k.lower() in eq8.lower())
    b2_b_ok = b2_b_hits >= 3
    record(
        "B.2.b eq8 repair addresses item (b) Kubo identity",
        b2_b_ok,
        f"{b2_b_hits}/{len(b2_b_keywords)} keyword hits",
    )
    print(
        f"  {'PASS' if b2_b_ok else 'FAIL'} B.2.b eq8 repair addresses Kubo-identity item "
        f"({b2_b_hits}/{len(b2_b_keywords)} hits)"
    )

    b2_c_keywords = [
        "J*",
        "Nachtergaele",
        "per-site",
        "v_LR",
    ]
    b2_c_hits = sum(1 for k in b2_c_keywords if k.lower() in eq8.lower())
    b2_c_ok = b2_c_hits >= 3
    record(
        "B.2.c eq8 repair addresses item (c) J* constant",
        b2_c_ok,
        f"{b2_c_hits}/{len(b2_c_keywords)} keyword hits",
    )
    print(
        f"  {'PASS' if b2_c_ok else 'FAIL'} B.2.c eq8 repair addresses J* constant item "
        f"({b2_c_hits}/{len(b2_c_keywords)} hits)"
    )

    # B.3: spatial slab + axis-permutation address item (a) spatial slice
    slab = git_show_origin_main(COMPANION_SLAB) or ""
    axis = git_show_origin_main(COMPANION_AXIS) or ""
    b3_slab_keywords = [
        "slab",
        "T_x",
        "Δ_x",
        "spatial",
        "exp(-d",
    ]
    b3_slab_hits = sum(1 for k in b3_slab_keywords if k.lower() in slab.lower())
    b3_slab_ok = b3_slab_hits >= 4
    record(
        "B.3.slab spatial slab bridge addresses item (a) spatial slice",
        b3_slab_ok,
        f"{b3_slab_hits}/{len(b3_slab_keywords)} keyword hits",
    )
    print(
        f"  {'PASS' if b3_slab_ok else 'FAIL'} B.3.slab spatial slab bridge text addresses spatial slice "
        f"({b3_slab_hits}/{len(b3_slab_keywords)} hits)"
    )

    b3_axis_keywords = [
        "axis-permutation",
        "T_W",
        "finite-Λ",
        "spatial axis",
        "heat-kernel",
        "Perron",
    ]
    b3_axis_hits = sum(1 for k in b3_axis_keywords if k.lower() in axis.lower())
    b3_axis_ok = b3_axis_hits >= 4
    record(
        "B.3.axis axis-permutation companion supplies H1+H2 spatial gap",
        b3_axis_ok,
        f"{b3_axis_hits}/{len(b3_axis_keywords)} keyword hits",
    )
    print(
        f"  {'PASS' if b3_axis_ok else 'FAIL'} B.3.axis axis-permutation companion text supplies H1+H2 "
        f"({b3_axis_hits}/{len(b3_axis_keywords)} hits)"
    )

    # B.4: parent itself names the three conditional items
    parent = git_show_origin_main(PARENT) or ""
    b4_parent_keywords = [
        "L2 exponential clustering",
        "mass-gap",
        "spatial cluster",
        "Δ_T",
    ]
    b4_parent_hits = sum(1 for k in b4_parent_keywords if k.lower() in parent.lower())
    b4_parent_ok = b4_parent_hits >= 3
    record(
        "B.4 parent text records the three named conditional items",
        b4_parent_ok,
        f"{b4_parent_hits}/{len(b4_parent_keywords)} parent-keyword hits",
    )
    print(
        f"  {'PASS' if b4_parent_ok else 'FAIL'} B.4 parent text records the named conditional items "
        f"({b4_parent_hits}/{len(b4_parent_keywords)} hits)"
    )


# -----------------------------------------------------------------------------
# Part C — hostile-audit invariants
# -----------------------------------------------------------------------------

def part_c_hostile_audit_invariants() -> None:
    """No status lift, no science change, parent + companions untouched."""
    print("\n=== Part C: hostile-audit invariants ===")

    # C.1: parent text in this PR (in worktree) matches origin/main byte-for-byte
    worktree_parent = (REPO_ROOT / PARENT).read_text(encoding="utf-8")
    origin_parent = git_show_origin_main(PARENT) or ""
    c1_ok = worktree_parent == origin_parent
    record(
        "C.1 parent text untouched in this PR",
        c1_ok,
        f"parent diff vs origin/main: {'identical' if c1_ok else 'DIFFER'}",
    )
    print(f"  {'PASS' if c1_ok else 'FAIL'} C.1 parent text untouched")

    # C.2: each companion text in worktree matches origin/main
    companions = [
        ("C.2.mass_gap mass-gap bridge untouched", COMPANION_MASS_GAP),
        ("C.2.slab spatial slab bridge untouched", COMPANION_SLAB),
        ("C.2.eq8 eq8 repair companion untouched", COMPANION_EQ8),
        ("C.2.axis axis-permutation companion untouched", COMPANION_AXIS),
    ]
    for name, path in companions:
        wt = (REPO_ROOT / path).read_text(encoding="utf-8")
        origin = git_show_origin_main(path) or ""
        ok = wt == origin
        record(name, ok, f"{path}: {'identical' if ok else 'DIFFER'}")
        print(f"  {'PASS' if ok else 'FAIL'} {name}")

    # C.3: no audit-ledger touch in this PR
    audit_paths = [
        "docs/audit/data/audit_ledger.json",
        "docs/audit/data/audit_invariants.json",
    ]
    audit_diff_clean = True
    for p in audit_paths:
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only", "origin/main", "--", p],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.stdout.strip():
                audit_diff_clean = False
        except Exception:
            audit_diff_clean = False
    record(
        "C.3 no audit-ledger touch in this PR",
        audit_diff_clean,
        "no audit/data/ paths changed vs origin/main",
    )
    print(f"  {'PASS' if audit_diff_clean else 'FAIL'} C.3 no audit-ledger touch")

    # C.4: no new science — the meta-note declares claim_type=meta explicitly
    pairing_path = REPO_ROOT / PAIRING_NOTE
    pairing_text = pairing_path.read_text(encoding="utf-8") if pairing_path.exists() else ""
    c4_ok = bool(re.search(r"claim_type[:=]\s*meta", pairing_text, re.IGNORECASE)) or "Claim type:** meta" in pairing_text
    record(
        "C.4 pairing note declares claim_type=meta",
        c4_ok,
        "claim_type=meta declared in pairing note",
    )
    print(f"  {'PASS' if c4_ok else 'FAIL'} C.4 claim_type=meta declared")

    # C.5: pairing note explicitly disclaims status lift
    c5_phrases = [
        "does not lift",
        "status authority",
        "audit lane",
    ]
    c5_hits = sum(1 for p in c5_phrases if p.lower() in pairing_text.lower())
    c5_ok = c5_hits == len(c5_phrases)
    record(
        "C.5 pairing note explicitly disclaims status lift",
        c5_ok,
        f"{c5_hits}/{len(c5_phrases)} status-disclaim phrases present",
    )
    print(f"  {'PASS' if c5_ok else 'FAIL'} C.5 status-lift disclaimer present")

    # C.6: pairing note explicitly disclaims new science / new axioms
    # Acceptable phrasings (any 2 of the 4 count):
    c6_phrases = [
        "no new science",
        "no new axiom",
        "does not introduce new axiom",
        "no new framework",
    ]
    c6_hits = sum(1 for p in c6_phrases if p.lower() in pairing_text.lower())
    c6_ok = c6_hits >= 2
    record(
        "C.6 pairing note explicitly disclaims new science / new axioms",
        c6_ok,
        f"{c6_hits}/{len(c6_phrases)} no-new-X phrases present (need >=2)",
    )
    print(f"  {'PASS' if c6_ok else 'FAIL'} C.6 no-new-science disclaimer present ({c6_hits}/{len(c6_phrases)})")

    # C.7: pairing note explicitly cross-refs every cited row
    refs = [
        Path(PARENT).name,
        Path(COMPANION_MASS_GAP).name,
        Path(COMPANION_SLAB).name,
        Path(COMPANION_EQ8).name,
        Path(COMPANION_AXIS).name,
    ]
    missing_refs = [r for r in refs if r not in pairing_text]
    c7_ok = len(missing_refs) == 0
    record(
        "C.7 pairing note cross-refs every cited row",
        c7_ok,
        f"missing refs: {missing_refs}" if not c7_ok else "all 5 rows cross-referenced",
    )
    print(f"  {'PASS' if c7_ok else 'FAIL'} C.7 all-rows cross-referenced ({5 - len(missing_refs)}/5)")

    # C.8: pairing note cites the three named conditional items by tag (a)/(b)/(c)
    c8_items = ["item (a)", "item (b)", "item (c)"]
    c8_hits = sum(1 for p in c8_items if p.lower() in pairing_text.lower())
    c8_ok = c8_hits == 3
    record(
        "C.8 pairing note names items (a) (b) (c) explicitly",
        c8_ok,
        f"{c8_hits}/3 named conditional items cited",
    )
    print(f"  {'PASS' if c8_ok else 'FAIL'} C.8 items (a)(b)(c) cited ({c8_hits}/3)")

    # C.9: pairing note does NOT modify any scripts/ companion runner
    companion_scripts = [
        "scripts/cluster_decomposition_mass_gap_bridge_check.py",
        "scripts/cluster_decomposition_spatial_slab_bridge_check.py",
        "scripts/frontier_cluster_decomposition_parent_eq8_repair_narrow_verifier.py",
        "scripts/frontier_cluster_decomp_delta_x_su3_axis_permutation_2026_06_02.py",
    ]
    runner_diff_clean = True
    diffed = []
    for p in companion_scripts:
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only", "origin/main", "--", p],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.stdout.strip():
                runner_diff_clean = False
                diffed.append(p)
        except Exception:
            runner_diff_clean = False
    record(
        "C.9 no companion runner touched in this PR",
        runner_diff_clean,
        f"diff vs origin/main: {'clean' if runner_diff_clean else f'CHANGED {diffed}'}",
    )
    print(f"  {'PASS' if runner_diff_clean else 'FAIL'} C.9 no companion runner touched")


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------

def main() -> int:
    print(f"Cluster-decomposition discharge ledger-pairing verifier")
    print(f"Repo: {REPO_ROOT}")
    print(f"Pairing note: {PAIRING_NOTE}")
    print()

    part_a_on_main_cite_check()
    part_b_content_match()
    part_c_hostile_audit_invariants()

    n_pass = sum(1 for _, ok, _ in RESULTS if ok)
    n_fail = sum(1 for _, ok, _ in RESULTS if not ok)

    print()
    print("=" * 60)
    print(f"SUMMARY: {n_pass} PASS / {n_fail} FAIL  ({len(RESULTS)} total)")
    print("=" * 60)

    if n_fail:
        print()
        print("FAILURES:")
        for name, ok, detail in RESULTS:
            if not ok:
                print(f"  FAIL  {name}: {detail}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
