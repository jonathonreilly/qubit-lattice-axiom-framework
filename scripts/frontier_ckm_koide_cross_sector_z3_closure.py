#!/usr/bin/env python3
"""Conditional count equality on two supplied mathematical surfaces.
The hw=1 Wilson corner orbit has three labels; the CKM structural-count
surface supplies n_color=3. Equality of these integers does not identify
physical generations, color, or a common origin. Status strings are printed
as documentary metadata, never consumed as conditional source.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md', 'docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md', 'docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md', 'docs/CL3_TASTE_GENERATION_THEOREM.md', 'docs/MINIMAL_AXIOMS_2026-04-11.md', 'docs/THREE_GENERATION_STRUCTURE_NOTE.md')


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
    """Read the conditional orbit count, without physical-generation identification."""
    banner("R1: Read N_gen from THREE_GENERATION_STRUCTURE_NOTE (conditional source)")

    content = read_authority("docs/THREE_GENERATION_STRUCTURE_NOTE.md")
    check("THREE_GENERATION_STRUCTURE_NOTE.md exists as an input",
          bool(content))

    # Ground-up verification: extract the actual Status: line text
    status_text = extract_status_text(content)
    print(f"  Extracted Status: {status_text!r}")

    tier = authority_tier(content)
    print(f"  Tier classification (parsed): {tier}")
    check("Generation source explicitly excludes physical-species and SM-generation identification",
          "physical-species interpretation, SM-generation identification" in " ".join(content.split())
          and "This row does not claim that the `hw=1` triplet is physically realized" in " ".join(content.split()))

    # Extract the stated hw=1 table degeneracy, not a physical species count.
    match = re.search(r"^\|\s*1\s*\|\s*(\d+)\s*\|\s*2\s*\|", content, re.MULTILINE)
    orbit_count = int(match.group(1)) if match else None
    check("Conditional hw=1 orbit count read from the Wilson-corner table", orbit_count == 3)
    return orbit_count


def audit_ckm_magnitudes_authority() -> int:
    """Read CKM_MAGNITUDES_STRUCTURAL_COUNTS; extract N_color."""
    banner("R2: Read N_color from CKM_MAGNITUDES_STRUCTURAL_COUNTS (conditional source)")

    content = read_authority(
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md"
    )
    check("CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM exists on main",
          bool(content))

    # Ground-up verification: extract the actual Status: line text
    status_text = extract_status_text(content)
    print(f"  Extracted Status: {status_text!r}")
    tier = authority_tier(content)
    check("CKM source declares conditional structural-count algebra, not upstream closure",
          "The conditional surface is:" in " ".join(content.split())
          and "is owned by the upstream-audit lane and is not asserted" in " ".join(content.split()))

    # Read the supplied n_color statement explicitly in the document
    # Pattern: "n_color = 3" or similar
    match = re.search(r"n[_\s]color\s*=\s*(\d+)", content, re.IGNORECASE)
    if match:
        N_color_extracted = int(match.group(1))
    else:
        N_color_extracted = None

    print(f"  Pattern 'n_color = N' search: {match.group(0) if match else 'NOT FOUND'}")
    print(f"  N_color (read from conditional source): {N_color_extracted}")
    check("R2: N_color = 3 read from conditional source", N_color_extracted == 3)
    return N_color_extracted


def audit_r3_closure(n_gen: int, n_color: int) -> None:
    """Verify the closure R3 by direct equality at the verified supplied mathematical values."""
    banner("R3: Cross-sector closure N_gen = N_color = 3 by conditional integer equality")

    print(f"  N_gen   (R1, orbit count from THREE_GENERATION_STRUCTURE) = {n_gen}")
    print(f"  N_color (R2, supplied count from CKM_MAGNITUDES)             = {n_color}")
    print(f"  Both supplied mathematical values are 3, so N_gen = N_color = 3.")

    check("R3: N_gen = 3 (read from conditional source)", n_gen == 3)
    check("R3: N_color = 3 (read from conditional source)", n_color == 3)
    check("R3: N_gen = N_color (conditional integer equality)", n_gen == n_color)
    check("R3: N_gen = N_color = 3 (closure)", n_gen == n_color == 3)


def audit_minimal_axioms_z3() -> None:
    """Verify the framework's Z^3 spatial substrate axiom is retained."""
    banner("Historical input memo: Z^3 spatial substrate (documentary presence only)")

    content = read_authority("docs/MINIMAL_AXIOMS_2026-04-11.md")
    check("MINIMAL_AXIOMS_2026-04-11.md exists as an input",
          bool(content))

    has_z3 = "Z^3" in content or "Z³" in content
    check("Historical memo names Z^3 spatial substrate",
          has_z3)


def audit_auxiliary_cl3_support() -> None:
    """Verify the CL3 support-tier readings exist (for completeness, NOT load-bearing)."""
    banner("Auxiliary abstract constructions (NOT load-bearing for equality)")

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
    print("  The color construction is conditional on a supplied carrier and is NOT load-bearing for closure R3.")
    print("  The R1/R2 scope contracts do not establish physical interpretation or audit authority.")
    print("  These separate supplied constructions establish no shared physical origin.")

    check("CL3_COLOR_AUTOMORPHISM states supplied finite carrier and open physical identification",
          "Supplied finite carrier only." in color_content
          and "The physical identification of any of these groups remains open." in color_content)
    check("Taste source is abstract representation theory without physical-family identification",
          "not a framework carrier theorem and not a physical-family theorem" in " ".join(taste_content.split())
          and "admitted abstract" in taste_content)
    check("CL3 construction notes exist (auxiliary reading available)",
          bool(color_content) and bool(taste_content))


def audit_no_promotion() -> None:
    """Verify this closure does NOT promote prior support branches to retained."""
    banner("This closure does NOT promote any support-tier branches to retained")

    print("  Conditional equality is separate from establishing the physical input values.")
    print("  It does NOT promote:")
    print("    - CL3_COLOR_AUTOMORPHISM_THEOREM (supplied finite carrier; physical identification open)")
    print("    - CL3_TASTE_GENERATION_THEOREM (abstract representation only)")
    print("    - Eight prior Koide-bridge SUPPORT-tier branches (they remain support)")
    print("    - Cross-sector A²-Koide_VCB bridge SUPPORT_NOTE (remains support)")
    print()
    print("  Physical input identification is not established by a documentary contract.")

    check("No auxiliary color promotion: supplied physical-identification boundary remains open",
          "The physical identification of any of these groups remains open." in read_authority("docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md"))


def audit_summary() -> None:
    banner("Conditional arithmetic and current authority boundary")
    print("If N_gen=3 and N_color=3 are supplied, their integer equality follows.")
    print("Status-string checks are documentary contracts, not physical proof.")
    print("Any failed scope or integer-extraction contract fails this conditional diagnostic. Physical closure remains open even when it passes.")
    print("The auxiliary color carrier supplies no physical identification.")


def main() -> int:
    print("=" * 88)
    print("Cross-sector closure N_gen = N_color = 3 via supplied count inputs")
    print("See docs/CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md")
    print("=" * 88)

    # Independent reading: do not pre-assign values; extract from authority files
    n_gen = audit_three_generation_authority()
    n_color = audit_ckm_magnitudes_authority()

    # The closure is established at the values independently extracted above
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
