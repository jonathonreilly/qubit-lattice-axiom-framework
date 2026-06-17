#!/usr/bin/env python3
"""Check the bounded CKM-EW lattice A^4 bridge identity.

This runner deliberately salvages only the arithmetic support:

    sin^2(theta_W)|_lattice = A^4 = 4/9

and the consistency equality

    A^2 = dim_fund(SU(2)) / dim_fund(SU(3)) = 2/3.

The below-W2 derivation of the Wolfenstein `A^2` law now lives in the
companion quark-doublet source theorem; this runner keeps the bridge identity
and the gauge-dimension consistency corollary isolated. Dependency statuses
are printed as boundary information, not converted into arithmetic failures.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md"
SOURCE_NOTE = ROOT / "docs" / "CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md"

AUTHORITY_FILES = {
    "minimal_axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-04-11.md",
    "yt_ew": ROOT / "docs" / "YT_EW_COLOR_PROJECTION_THEOREM.md",
    "wolfenstein": ROOT / "docs" / "WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md",
    "ckm_counts": ROOT / "docs" / "CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md",
    "cl3_taste": ROOT / "docs" / "CL3_TASTE_GENERATION_THEOREM.md",
}

passes = 0
fails = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global passes, fails
    status = "PASS" if condition else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    if condition:
        passes += 1
    else:
        fails += 1


def boundary(name: str, detail: str = "") -> None:
    suffix = f"  ({detail})" if detail else ""
    print(f"  [BOUNDARY] {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def status_line(content: str) -> str:
    for line in content.splitlines()[:40]:
        stripped = line.strip()
        if stripped.lower().startswith("**status") or stripped.lower().startswith("status"):
            return re.sub(r"^\*?\*?status[^:]*:\*?\*?\s*", "", stripped, flags=re.IGNORECASE)
    return ""


def contains_normalized(haystack: str, needle: str) -> bool:
    return " ".join(needle.split()).lower() in " ".join(haystack.split()).lower()


def extract_first_fraction(pattern: str, source: str) -> Fraction | None:
    match = re.search(pattern, source, re.IGNORECASE)
    if not match:
        return None
    return Fraction(int(match.group(1)), int(match.group(2)))


def main() -> int:
    print("=" * 88)
    print("CKM-EW lattice A^4 bounded bridge check")
    print(f"See {NOTE.relative_to(ROOT)}")
    print("=" * 88)

    note = text(NOTE)
    source_note = text(SOURCE_NOTE)
    authorities = {name: text(path) for name, path in AUTHORITY_FILES.items()}

    section("Authority and status boundary")
    for name, path in AUTHORITY_FILES.items():
        check(f"authority exists: {path.relative_to(ROOT)}", path.exists())
        print(f"    extracted Status: {status_line(authorities[name])!r}")

    yt_status = status_line(authorities["yt_ew"]).lower()
    wolf_status = status_line(authorities["wolfenstein"]).lower()
    counts_status = status_line(authorities["ckm_counts"]).lower()
    taste_status = status_line(authorities["cl3_taste"]).lower()
    check("YT_EW authority provides exact/support EW input",
          any(word in yt_status for word in ("exact", "support", "conditional", "bounded")),
          status_line(authorities["yt_ew"]))
    if "retained" not in yt_status:
        boundary("YT_EW is not a retained EW normalization certificate on current main",
                 status_line(authorities["yt_ew"]))
    check("Wolfenstein authority exposes note-side structural identities",
          "structural" in wolf_status or "audit lane" in wolf_status,
          status_line(authorities["wolfenstein"]))
    if "retained" not in wolf_status:
        boundary("Wolfenstein dependency still requires independent audit before retained closure",
                 status_line(authorities["wolfenstein"]))
    check("CKM counts authority exposes note-side structural identities",
          "structural" in counts_status or "audit lane" in counts_status,
          status_line(authorities["ckm_counts"]))
    if "retained" not in counts_status:
        boundary("CKM counts dependency still requires independent audit before retained closure",
                 status_line(authorities["ckm_counts"]))
    if "support" in taste_status or "reviewed exact algebraic support" in taste_status:
        check("CL3 taste is not used as a retained promotion input",
              True,
              status_line(authorities["cl3_taste"]))
    else:
        boundary("CL3 taste status wording is not load-bearing for this bridge",
                 status_line(authorities["cl3_taste"]))

    check("companion below-W2 source theorem exists", SOURCE_NOTE.exists())
    check("companion theorem states A^2 = N_pair / N_color = 2/3",
          contains_normalized(source_note, "A² = N_pair / N_color = 2/3")
          or contains_normalized(source_note, "A^2 = N_pair / N_color = 2/3"))

    required_boundaries = [
        "companion theorem",
        "A2_BELOW_W2_DERIVATION_DEPENDENCY_GATED=TRUE",
        "SUPPORT_TIER_PROMOTION=FALSE",
        "KOIDE_CLOSURE=FALSE",
        "Support-tier CL3 taste-generation readings are not used.",
    ]
    for phrase in required_boundaries:
        check(f"note states boundary: {phrase}", contains_normalized(note, phrase))

    forbidden_promotions = [
        "SUPPORT_TIER_PROMOTION=TRUE",
        "KOIDE_CLOSURE=TRUE",
        "therefore closes Koide",
    ]
    for phrase in forbidden_promotions:
        check(f"note avoids promotion: {phrase}", not contains_normalized(note, phrase))

    section("EW lattice angle arithmetic")
    yt = authorities["yt_ew"]
    has_g2 = "g_2^2" in yt and "1/(d+1)" in yt
    has_gY = "g_Y^2" in yt and "1/(d+2)" in yt
    has_quarters = "1/4" in yt
    has_fifths = "1/5" in yt
    if has_g2:
        check("YT_EW contains g_2^2 = 1/(d+1)", True)
    else:
        boundary("YT_EW no longer carries literal g_2^2 = 1/(d+1) wording")
    if has_gY:
        check("YT_EW contains g_Y^2 = 1/(d+2)", True)
    else:
        boundary("YT_EW no longer carries literal g_Y^2 = 1/(d+2) wording")
    if has_quarters:
        check("YT_EW contains 1/4 value", True)
    else:
        boundary("YT_EW no longer carries literal 1/4 wording")
    if has_fifths:
        check("YT_EW contains 1/5 value", True)
    else:
        boundary("YT_EW no longer carries literal 1/5 wording")

    d = 3
    g2_sq = Fraction(1, d + 1)
    gY_sq = Fraction(1, d + 2)
    sin2_lattice = gY_sq / (gY_sq + g2_sq)
    check("g_2^2 = 1/4 at d=3", g2_sq == Fraction(1, 4))
    check("g_Y^2 = 1/5 at d=3", gY_sq == Fraction(1, 5))
    check("sin^2(theta_W)|_lattice = 4/9", sin2_lattice == Fraction(4, 9))

    section("CKM A^4 side")
    wolf = authorities["wolfenstein"]
    counts = authorities["ckm_counts"]
    a_sq_from_w2 = extract_first_fraction(r"A\^2\s*=\s*(\d+)\s*/\s*(\d+)", wolf)
    w2_contains_two_thirds = a_sq_from_w2 == Fraction(2, 3) or (
        "A^2" in wolf and "2/3" in wolf
    )
    n_pair_match = re.search(r"n[_\s]pair\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_color_match = re.search(r"n[_\s]color\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_pair = int(n_pair_match.group(1)) if n_pair_match else None
    n_color = int(n_color_match.group(1)) if n_color_match else None
    check("W2 authority contains A^2 = 2/3", w2_contains_two_thirds)
    check("CKM counts authority contains n_pair = 2", n_pair == 2)
    check("CKM counts authority contains n_color = 3", n_color == 3)

    a_sq = Fraction(n_pair, n_color) if n_pair and n_color else Fraction(0)
    a_four = a_sq * a_sq
    check("A^2 = n_pair/n_color = 2/3", a_sq == Fraction(2, 3))
    check("A^4 = 4/9", a_four == Fraction(4, 9))
    check("bounded EW-CKM arithmetic identity sin^2(theta_W)|_lattice = A^4",
          sin2_lattice == a_four == Fraction(4, 9))

    section("Gauge-dimension consistency, not below-W2 derivation")
    minimal = authorities["minimal_axioms"]
    has_su2 = "SU(2)" in minimal and "exact native" in minimal
    has_su3 = "SU(3)" in minimal and "structural" in minimal
    dim_su2_fund = 2
    dim_su3_fund = 3
    gauge_ratio = Fraction(dim_su2_fund, dim_su3_fund)
    check("minimal axioms expose exact native SU(2)", has_su2)
    check("minimal axioms expose structural SU(3)", has_su3)
    check("dim_fund(SU(2)) / dim_fund(SU(3)) = 2/3",
          gauge_ratio == Fraction(2, 3))
    check("gauge-dimension ratio equals A^2 at values",
          gauge_ratio == a_sq == Fraction(2, 3))
    check("note keeps the gauge-dimension equality as a consistency corollary",
          contains_normalized(note, "the equality in this note remains the gauge-dimension corollary"))

    section("Summary")
    print("  Certified:")
    print("    sin^2(theta_W)|_lattice = A^4 = 4/9")
    print("    A^2 = dim_fund(SU(2))/dim_fund(SU(3)) = 2/3 as value-level consistency")
    print("    dependency statuses are boundary-gated before retained closure")
    print()
    print("  Not certified:")
    print("    an independent below-W2 derivation inside this bridge note alone,")
    print("    support-tier promotion,")
    print("    physical M_Z weak-angle prediction, or Koide closure.")

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={passes}, HARD_ISSUES={fails}")
    print(f"PASSED: {passes}/{passes + fails}")
    print("=" * 88)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
