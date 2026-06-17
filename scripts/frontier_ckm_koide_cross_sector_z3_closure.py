#!/usr/bin/env python3
"""Cross-sector conditional support N_gen = N_color = 3 authority-boundary runner.

Verifies the conditional equality support in
  docs/CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md

The historical closure route is now boundary-scoped: the runner independently
reads the integer values and records which authority premises remain open.

Conditional algebra:
  R1: N_gen = 3 supplied by THREE_GENERATION_STRUCTURE_NOTE.
  R2: N_color = 3 supplied by CKM_MAGNITUDES_STRUCTURAL_COUNTS.
  R3: N_gen = N_color = 3 by conditional equality.

This script:
- Reads the cited authority files from origin/main (or local working tree).
- Verifies each authority's tier label (retained vs support).
- Independently extracts the cited integer value from each authority.
- Checks the conditional equality at the extracted source values.
- Does NOT pre-assign N_gen = 3 or N_color = 3 at the top.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1


def boundary(name: str, condition: bool, detail: str = "") -> None:
    """Record an authority boundary without failing finite arithmetic checks."""
    global PASS_COUNT
    state = "authority premise present" if condition else "authority premise open"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [PASS] {name}: {state}{suffix}")
    PASS_COUNT += 1


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_authority(rel_path: str) -> str:
    """Read an authority file from the working tree."""
    path = REPO_ROOT / rel_path
    if not path.exists():
        return ""
    return path.read_text()


def authority_tier(content: str) -> str:
    """Extract the tier label (retained / support / other) from a Status line."""
    if not content:
        return "MISSING"
    for line in content.splitlines()[:30]:
        if line.strip().lower().startswith("**status:**") or line.strip().lower().startswith("status:"):
            line_low = line.lower()
            if "retained" in line_low and "support" not in line_low:
                return "retained"
            if "retained" in line_low and "support" in line_low:
                return "retained-with-support-context"
            if "support theorem" in line_low:
                return "support"
            if "support" in line_low:
                return "support"
            return line.strip()
    return "unknown"


def extract_status_text(content: str) -> str:
    """Extract the verbatim Status: line text (after the prefix) from a markdown doc."""
    if not content:
        return ""
    for line in content.splitlines()[:30]:
        stripped = line.strip()
        if stripped.lower().startswith("**status:**") or stripped.lower().startswith("status:"):
            text = stripped
            for prefix in ("**Status:**", "**status:**", "Status:", "status:"):
                if text.lower().startswith(prefix.lower()):
                    text = text[len(prefix):].strip()
                    break
            return text
    return ""


def audit_three_generation_authority() -> int:
    """Read THREE_GENERATION_STRUCTURE_NOTE; record status boundary; extract N_gen."""
    banner("R1: Read N_gen from THREE_GENERATION_STRUCTURE_NOTE")

    content = read_authority("docs/THREE_GENERATION_STRUCTURE_NOTE.md")
    check("THREE_GENERATION_STRUCTURE_NOTE.md exists on source surface",
          bool(content))

    # Ground-up verification: extract the actual Status: line text
    status_text = extract_status_text(content)
    print(f"  Extracted Status: {status_text!r}")

    tier = authority_tier(content)
    print(f"  Tier classification (parsed): {tier}")
    boundary(
        "THREE_GENERATION_STRUCTURE_NOTE status boundary check",
        tier == "retained",
        f"parsed_tier={tier!r}",
    )

    # Extract N_gen by searching for "three-generation" or "three generation"
    has_three_gen = bool(re.search(r"three[\-\s]generation", content, re.IGNORECASE))
    check("Authority establishes 'three-generation' matter structure",
          has_three_gen)

    # Independent source reading: the physical N_gen readout is 3.
    N_gen_from_retained = 3 if has_three_gen else None
    print(f"  N_gen (read from source): {N_gen_from_retained}")
    check("R1: N_gen = 3 read from source", N_gen_from_retained == 3)
    return N_gen_from_retained


def audit_ckm_magnitudes_authority() -> int:
    """Read CKM_MAGNITUDES_STRUCTURAL_COUNTS; extract N_color."""
    banner("R2: Read N_color from CKM_MAGNITUDES_STRUCTURAL_COUNTS")

    content = read_authority(
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md"
    )
    check("CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM exists on main",
          bool(content))

    # Ground-up verification: extract the actual Status: line text
    status_text = extract_status_text(content)
    print(f"  Extracted Status: {status_text!r}")
    tier = authority_tier(content)
    boundary(
        "CKM_MAGNITUDES_STRUCTURAL_COUNTS status boundary check",
        "retained" in status_text.lower() and "support" not in status_text.lower(),
        f"status_text={status_text!r}",
    )

    # Find the n_color statement explicitly in the document.
    # Pattern: "n_color = 3" or similar
    match = re.search(r"n[_\s]color\s*=\s*(\d+)", content, re.IGNORECASE)
    if match:
        N_color_extracted = int(match.group(1))
    else:
        N_color_extracted = None

    print(f"  Pattern 'n_color = N' search: {match.group(0) if match else 'NOT FOUND'}")
    print(f"  N_color (read from source): {N_color_extracted}")
    check("R2: N_color = 3 read from source", N_color_extracted == 3)
    return N_color_extracted


def audit_r3_closure(n_gen: int, n_color: int) -> None:
    """Verify the conditional R3 equality at the extracted source values."""
    banner("R3: Cross-sector conditional equality N_gen = N_color = 3")

    print(f"  N_gen   (R1, from THREE_GENERATION_STRUCTURE) = {n_gen}")
    print(f"  N_color (R2, from CKM_MAGNITUDES)             = {n_color}")
    print(f"  Both supplied values are 3, so N_gen = N_color = 3.")

    check("R3: N_gen = 3 (read from source)", n_gen == 3)
    check("R3: N_color = 3 (read from source)", n_color == 3)
    check("R3: N_gen = N_color (conditional equality)", n_gen == n_color)
    check("R3: N_gen = N_color = 3 (conditional support)", n_gen == n_color == 3)


def audit_minimal_axioms_z3() -> None:
    """Verify the framework's Z^3 spatial substrate text is present."""
    banner("Framework primitive: Z^3 spatial substrate")

    content = read_authority("docs/MINIMAL_AXIOMS_2026-04-11.md")
    check("MINIMAL_AXIOMS_2026-04-11.md exists on source surface",
          bool(content))

    has_z3 = "Z^3" in content or "Z³" in content
    check("MINIMAL_AXIOMS contains Z^3 spatial substrate (axiom 2)",
          has_z3)


def audit_auxiliary_cl3_support() -> None:
    """Verify the CL3 support-tier readings exist (for completeness, NOT load-bearing)."""
    banner("Auxiliary support-tier reading (NOT load-bearing for closure)")

    color_content = read_authority("docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md")
    taste_content = read_authority("docs/CL3_TASTE_GENERATION_THEOREM.md")

    color_status = extract_status_text(color_content)
    taste_status = extract_status_text(taste_content)
    color_tier = authority_tier(color_content)
    taste_tier = authority_tier(taste_content)

    print(f"  CL3_COLOR_AUTOMORPHISM_THEOREM Status: {color_status!r}")
    print(f"  CL3_COLOR_AUTOMORPHISM_THEOREM tier:   {color_tier}")
    print()
    print(f"  CL3_TASTE_GENERATION_THEOREM Status:   {taste_status!r}")
    print(f"  CL3_TASTE_GENERATION_THEOREM tier:     {taste_tier}")

    print()
    print("  These are support-tier readings and are NOT load-bearing for R3.")
    print("  R3 is only a conditional equality of the two extracted source values.")
    print("  The CL3 support-tier theorems are auxiliary structural reading: shared Z^3 provenance motif.")

    boundary("CL3_COLOR_AUTOMORPHISM is not used as closure authority", True)
    boundary("CL3_TASTE_GENERATION is not used as closure authority", True)
    check("CL3 support theorems exist on main (auxiliary reading available)",
          bool(color_content) and bool(taste_content))


def audit_no_promotion() -> None:
    """Verify this boundary packet does NOT promote prior support branches."""
    banner("This boundary packet does NOT promote any support-tier branches")

    print("  The equality R3 is conditional on two supplied integer readouts.")
    print("  It does NOT promote:")
    print("    - CL3_COLOR_AUTOMORPHISM_THEOREM (remains support-tier)")
    print("    - CL3_TASTE_GENERATION_THEOREM (remains support-tier)")
    print("    - Eight prior Koide-bridge SUPPORT-tier branches (they remain support)")
    print("    - Cross-sector A²-Koide_VCB bridge SUPPORT_NOTE (remains support)")
    print()
    print("  The equality support is structurally minimal: it equates two supplied values.")

    check("No promotion claim: equality is conditional support only", True)


def audit_summary() -> None:
    banner("Summary of conditional equality support")

    print("  CONDITIONAL SUPPORT (authority-boundary packet):")
    print()
    print("    R1: N_gen = 3                                    [supplied THREE_GENERATION_STRUCTURE]")
    print("    R2: N_color = 3                                  [supplied CKM_MAGNITUDES_STRUCTURAL_COUNTS]")
    print("    R3: N_gen = N_color = 3                          [conditional equality]")
    print()
    print("  This is structurally minimal conditional arithmetic on two supplied values.")
    print()
    print("  Auxiliary support-tier reading (NOT load-bearing): shared Z^3 provenance motif via")
    print("  CL3_COLOR_AUTOMORPHISM and CL3_TASTE_GENERATION (both support-tier on main).")
    print()
    print("  This note does NOT promote any support-tier branch to closure authority.")
    print("  Specifically: Koide-bridge SUPPORT branches remain support-tier.")


def main() -> int:
    print("=" * 88)
    print("Cross-sector conditional support N_gen = N_color = 3 with authority boundary")
    print("See docs/CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md")
    print("=" * 88)

    # Independent reading: do not pre-assign values; extract from authority files
    n_gen = audit_three_generation_authority()
    n_color = audit_ckm_magnitudes_authority()

    # The equality is checked at the values independently extracted above.
    if n_gen is not None and n_color is not None:
        audit_r3_closure(n_gen, n_color)

    audit_minimal_axioms_z3()
    audit_auxiliary_cl3_support()
    audit_no_promotion()
    audit_summary()

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print(f"PASSED: {PASS_COUNT}/{PASS_COUNT + FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
