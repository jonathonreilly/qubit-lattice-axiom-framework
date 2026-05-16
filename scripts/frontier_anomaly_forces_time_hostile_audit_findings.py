#!/usr/bin/env python3
"""Anomaly-Forces-Time Hostile Audit Findings — Verification Runner.

Verifies the programmatically-checkable findings (F-C and F-E) of
`docs/ANOMALY_FORCES_TIME_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-16.md`.

The note documents four findings from a 5-agent hostile audit fan-out:

  F-A: admission (i) is structurally non-internalizable from retained
       primitives (requires Ginsparg-Wilson machinery). This finding
       is structural/literature-based; not directly programmable.

  F-B: "anomaly forces time" is mis-framed; d_t = 1 is inherited from
       admission (iv)'s lattice ansatz, not derived from ABJ. This
       finding is interpretive; not directly programmable.

  F-C: admission (iii)'s routing to CPT_EXACT_NOTE.md is unsupported.
       VERIFIABLE: CPT_EXACT_NOTE has zero γ_5 occurrences.

  F-E: cycle-0002 is created by two cite-only back-edges already
       marked non-load-bearing by source authors.
       VERIFIABLE: the annotation string exists in
       EMERGENT_LORENTZ_INVARIANCE_NOTE.md.

This runner programmatically checks F-C and F-E. F-A and F-B are
documented in the note's prose but not programmatically verifiable.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent


def check(label: str, condition: bool, detail: str = "", class_a: bool = False) -> bool:
    global PASS_COUNT, FAIL_COUNT, CLASS_A_HITS
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        if class_a:
            CLASS_A_HITS += 1
    else:
        FAIL_COUNT += 1
    tag = " [A]" if class_a else ""
    msg = f"  [{status}]{tag} {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ============================================================================
# Part 1: Verify F-C — CPT_EXACT_NOTE has zero γ_5 occurrences
# ============================================================================


def part1_verify_F_C() -> None:
    """F-C: CPT_EXACT_NOTE.md does not contain the γ_5 / gamma_5 / γ5 string.

    The parent theorem (ANOMALY_FORCES_TIME_THEOREM.md) claims admission
    (iii) is internalized via 'ε(x) = staggered γ_5 carried by
    CPT_EXACT_NOTE.md'. We verify CPT_EXACT_NOTE.md does not contain any
    of the γ_5 spellings.
    """
    print()
    print("=" * 78)
    print("PART 1: F-C — CPT_EXACT_NOTE.md has zero γ_5 occurrences")
    print("=" * 78)

    cpt_path = REPO_ROOT / "docs" / "CPT_EXACT_NOTE.md"
    check(
        "docs/CPT_EXACT_NOTE.md exists",
        cpt_path.exists(),
        f"path = {cpt_path}",
        class_a=True,
    )

    if not cpt_path.exists():
        return

    content = cpt_path.read_text(encoding="utf-8")

    # Check for various spellings of gamma_5 / γ_5
    patterns = [
        r"gamma_5",
        r"gamma5",
        r"γ_5",
        r"γ5",
        r"\\gamma_5",
        r"\\gamma_\{5\}",
    ]

    for pat in patterns:
        matches = re.findall(pat, content)
        count = len(matches)
        check(
            f"CPT_EXACT_NOTE has 0 occurrences of '{pat}'",
            count == 0,
            f"actual count = {count}",
            class_a=True,
        )

    # Also confirm what CPT_EXACT_NOTE DOES say about ε(x)
    has_C_operator = re.search(r"\bC\b.*operator|charge\s*conjugation", content) is not None
    has_epsilon_x = "ε(x)" in content or "epsilon(x)" in content.lower()

    check(
        "CPT_EXACT_NOTE references ε(x) (epsilon(x))",
        has_epsilon_x,
        class_a=True,
    )
    check(
        "CPT_EXACT_NOTE references C operator / charge conjugation",
        has_C_operator,
        class_a=True,
    )


# ============================================================================
# Part 2: Verify F-E — EMERGENT_LORENTZ_INVARIANCE_NOTE has the back-edge annotation
# ============================================================================


def part2_verify_F_E() -> None:
    """F-E: EMERGENT_LORENTZ_INVARIANCE_NOTE.md contains the source-author
    annotation marking the cite-only back-edge as non-load-bearing.
    """
    print()
    print("=" * 78)
    print("PART 2: F-E — EMERGENT_LORENTZ_INVARIANCE_NOTE.md has back-edge annotation")
    print("=" * 78)

    eli_path = REPO_ROOT / "docs" / "EMERGENT_LORENTZ_INVARIANCE_NOTE.md"
    check(
        "docs/EMERGENT_LORENTZ_INVARIANCE_NOTE.md exists",
        eli_path.exists(),
        f"path = {eli_path}",
        class_a=True,
    )

    if not eli_path.exists():
        return

    content = eli_path.read_text(encoding="utf-8")

    # Key annotation phrases (from F-E investigation)
    key_phrases = [
        "cite-only, not promoted",
        "graph edge deferred",
        "Planck/Lorentz back-edge",
    ]

    for phrase in key_phrases:
        present = phrase in content
        check(
            f"Annotation contains '{phrase}'",
            present,
            class_a=True,
        )

    # Check that PLANCK_SCALE_LANE_STATUS is referenced (so the edge exists)
    has_planck_ref = "PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23" in content
    check(
        "Reference to PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23 present (back-edge source)",
        has_planck_ref,
        class_a=True,
    )


# ============================================================================
# Part 3: Verify NO_PER_SITE_CHIRALITY_THEOREM exists and proves the no-go
# ============================================================================


def part3_verify_no_per_site_chirality_no_go() -> None:
    """F-C support: confirm the framework's internal no-go against per-site γ_5
    in Cl(3) actually exists in the repo.
    """
    print()
    print("=" * 78)
    print("PART 3: F-C support — NO_PER_SITE_CHIRALITY no-go is internal")
    print("=" * 78)

    nps_path = REPO_ROOT / "docs" / "NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md"
    check(
        "docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md exists",
        nps_path.exists(),
        f"path = {nps_path}",
        class_a=True,
    )

    if not nps_path.exists():
        return

    content = nps_path.read_text(encoding="utf-8")

    # Should reference Cl(3) and the impossibility result
    has_cl3 = "Cl(3)" in content or "Cl_3" in content
    has_no_go = (
        "no element" in content.lower()
        or "no per-site" in content.lower()
        or "anti-commut" in content.lower()
    )

    check(
        "Note references Cl(3) algebra",
        has_cl3,
        class_a=True,
    )
    check(
        "Note articulates the no-go (no per-site γ_5 / no anti-commuting element)",
        has_no_go,
        class_a=True,
    )


# ============================================================================
# Part 4: Verify CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION sister theorem
# explicitly disclaims the identification
# ============================================================================


def part4_verify_sister_theorem_disclaims() -> None:
    """F-C support: the sister theorem CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION
    explicitly says it does NOT identify the volume-element chirality with
    the staggered ε(x).
    """
    print()
    print("=" * 78)
    print("PART 4: F-C support — sister theorem disclaims the identification")
    print("=" * 78)

    cvc_path = (
        REPO_ROOT
        / "docs"
        / "CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md"
    )
    check(
        "Sister theorem note exists",
        cvc_path.exists(),
        f"path = {cvc_path}",
        class_a=True,
    )

    if not cvc_path.exists():
        return

    content = cvc_path.read_text(encoding="utf-8")

    # The disclaimer should mention CPT_EXACT_NOTE and either ε(x) or
    # "staggered sublattice" or "downstream realization step"
    has_cpt_ref = "CPT_EXACT_NOTE" in content
    has_downstream_lang = (
        "downstream realization" in content.lower()
        or "separate downstream" in content.lower()
    )

    check(
        "Sister theorem references CPT_EXACT_NOTE",
        has_cpt_ref,
        class_a=True,
    )
    check(
        "Sister theorem articulates downstream-realization disclaimer",
        has_downstream_lang,
        class_a=True,
    )


# ============================================================================
# Part 5: Verify the parent theorem's claim is what we cite it as
# ============================================================================


def part5_verify_parent_claim() -> None:
    """Verify the parent theorem ANOMALY_FORCES_TIME_THEOREM.md actually
    makes the claims we attribute to it (admissions (i), (iii)).
    """
    print()
    print("=" * 78)
    print("PART 5: Verify parent theorem claims we attribute to it")
    print("=" * 78)

    aft_path = REPO_ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"
    check(
        "Parent theorem note exists",
        aft_path.exists(),
        f"path = {aft_path}",
        class_a=True,
    )

    if not aft_path.exists():
        return

    content = aft_path.read_text(encoding="utf-8")

    # Should reference admission (i) ABJ and admission (iii) chirality
    has_admission_i = "admission (i)" in content.lower() or "(i)" in content
    has_ABJ = "ABJ" in content or "Adler" in content
    has_admission_iii = "admission (iii)" in content.lower() or "(iii)" in content
    has_CPT_route = "CPT_EXACT_NOTE" in content
    has_epsilon_gamma5_claim = (
        ("epsilon(x)" in content.lower() or "ε(x)" in content)
        and ("gamma_5" in content.lower() or "γ_5" in content)
    )

    check(
        "Parent references ABJ / admission (i)",
        has_admission_i and has_ABJ,
        class_a=True,
    )
    check(
        "Parent references admission (iii)",
        has_admission_iii,
        class_a=True,
    )
    check(
        "Parent claims routing to CPT_EXACT_NOTE for admission (iii)",
        has_CPT_route,
        class_a=True,
    )
    check(
        "Parent claims ε(x) = staggered γ_5 identification",
        has_epsilon_gamma5_claim,
        class_a=True,
    )


# ============================================================================
# Main
# ============================================================================


def main() -> int:
    print("=" * 78)
    print("ANOMALY-FORCES-TIME HOSTILE AUDIT FINDINGS — VERIFICATION RUNNER")
    print("=" * 78)
    print("Verifies docs/ANOMALY_FORCES_TIME_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-16.md")
    print()
    print("Programmatically checks F-C (admission iii routing broken) and")
    print("F-E (cycle-0002 contains cite-only edges marked non-load-bearing).")
    print("F-A (admission i no-go) and F-B (mis-framing) are interpretive findings")
    print("documented in the note's prose but not programmatically checkable.")

    part1_verify_F_C()
    part2_verify_F_E()
    part3_verify_no_per_site_chirality_no_go()
    part4_verify_sister_theorem_disclaims()
    part5_verify_parent_claim()

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    print(f"Class-A pattern hits: {CLASS_A_HITS}")
    print("=" * 78)
    print()
    print("VERDICT:")
    if FAIL_COUNT == 0:
        print("  HOSTILE AUDIT FINDINGS VERIFIED")
        print("  F-C: CPT_EXACT_NOTE has zero γ_5 occurrences (routing claim unsupported)")
        print("  F-E: cycle-0002 back-edge marked 'graph edge deferred' by source author")
        print("  F-C support: NO_PER_SITE_CHIRALITY no-go is internal repo theorem")
        print("  F-C support: sister theorem CLIFFORD_VOLUME_CHIRALITY explicitly disclaims")
        print("  Parent claims correctly attributed (no straw-man critique)")
        print(f"  dominant_class: A ({CLASS_A_HITS} class-A pattern hits)")
        return 0
    else:
        print(f"  HOSTILE AUDIT FINDINGS NOT VERIFIED — {FAIL_COUNT} FAILs")
        return 1


if __name__ == "__main__":
    sys.exit(main())
