#!/usr/bin/env python3
"""Verify e = g sin(θ_W) = g' cos(θ_W) from EWSB pattern."""

AUDIT_INPUT_PATHS = ["docs/EM_COUPLING_FROM_EWSB_NOTE_2026-05-02.md"]

AUDIT_TIMEOUT_SEC = 300

from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "EM_COUPLING_FROM_EWSB_NOTE_2026-05-02.md"

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


section("Part 1: documentary note structure")
note_text = NOTE_PATH.read_text()
required = [
    "Electromagnetic Coupling e = g sin(θ_W) = g' cos(θ_W)",
    "EWSB Pattern",
    "tan(θ_W) = g'/g",
    "Z_μ coupling",
    "T_3 − Q sin²(θ_W)",
    "proposal_allowed: false",
]
for s in required:
    check(f"contains: {s!r}", s in note_text)


section("Part 2: finite squared identity g sin(θ_W) = g' cos(θ_W)")
# At exact rational level, with tan²θ_W = g'²/g²:
test_cases = [
    (Fraction(1), Fraction(2)),    # g²=1, g'²=2 → tan²=2 → sin²=2/3, cos²=1/3
    (Fraction(3), Fraction(5)),
    (Fraction(2), Fraction(1)),
]
all_ok = True
for g2, gp2 in test_cases:
    tan2 = gp2 / g2
    sin2 = gp2 / (g2 + gp2)
    cos2 = g2 / (g2 + gp2)
    # e² = g² sin²(θ_W) = g'² cos²(θ_W)
    e2_from_g = g2 * sin2
    e2_from_gp = gp2 * cos2
    if e2_from_g != e2_from_gp:
        all_ok = False
        break
check("e² = g² sin²θ_W = g'² cos²θ_W (finite squared checks at exact Fraction)",
      all_ok,
      detail=f"tested {len(test_cases)} (g²,g'²) cases")


section("Part 3: tan(θ_W) = g'/g consistency")
for g2, gp2 in test_cases:
    tan2_check = gp2 / g2  # tan² = g'²/g²
    sin2 = gp2 / (g2 + gp2)
    cos2 = g2 / (g2 + gp2)
    tan2_from_sincos = sin2 / cos2
    check(f"tan²θ_W = g'²/g² = sin²/cos² for g²={g2}, g'²={gp2}",
          tan2_check == tan2_from_sincos,
          detail=f"tan²={tan2_check}")


section("Part 3b: finite signed photon and Z coefficient controls")
for g, gp, norm in [(Fraction(3), Fraction(4), Fraction(5)),
                    (Fraction(5), Fraction(12), Fraction(13))]:
    sn, cs = gp / norm, g / norm
    e = g * sn
    check("signed photon coefficients on positive rational fixture",
          g * sn == gp * cs == e and e > 0)
    check("both Z coefficients agree without division by T3",
          g * cs == (g / cs) * (1 - sn * sn)
          and -gp * sn == -(g / cs) * sn * sn)
    t3, yhalf = Fraction(0), Fraction(1)
    check("Z expression remains defined at T3=0",
          g * t3 * cs - gp * yhalf * sn
          == (g / cs) * (t3 - (t3 + yhalf) * sn * sn))
    check("wrong-sign photon rejected despite equal squared values",
          (-g * sn) ** 2 == (gp * cs) ** 2 and -g * sn != gp * cs)


section("Part 4: supplied 3/8 and conditional mass-law illustration")
# At GUT scale (cycle 19): sin²θ_W = 3/8, cos²θ_W = 5/8
sin2_GUT = Fraction(3, 8)
cos2_GUT = Fraction(5, 8)
# tan²θ_W^GUT = 3/5 (cycle 19)
tan2_GUT = sin2_GUT / cos2_GUT
check("tan²θ_W^GUT = sin²/cos² = 3/5 (supplied illustration only)",
      tan2_GUT == Fraction(3, 5),
      detail=f"tan²_GUT = {tan2_GUT}")

# At cycle 21: M_W²/M_Z² = cos²θ_W identity
# at GUT: M_W²/M_Z² = 5/8
mass_ratio_GUT = cos2_GUT
check("M_W²/M_Z²^GUT = cos²θ_W^GUT = 5/8 (supplied angle plus assumed mass law)",
      mass_ratio_GUT == Fraction(5, 8),
      detail=f"M_W²/M_Z² at GUT = {mass_ratio_GUT}")


print(f"\n{'='*88}\n  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}\n{'='*88}")
sys.exit(1 if FAIL_COUNT > 0 else 0)
