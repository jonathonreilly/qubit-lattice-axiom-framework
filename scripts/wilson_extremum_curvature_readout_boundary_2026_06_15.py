#!/usr/bin/env python3
"""Wilson extremum curvature readout boundary certificate runner.

Verifies docs/WILSON_EXTREMUM_CURVATURE_READOUT_BOUNDARY_CERTIFICATE_2026-06-15.md.
The runner checks the native Wilson curvature normalization and the
Taylor-residual certificate while keeping the physical Higgs-pole
reading and the numerical Wilson coefficient outside the claim.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import math
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "WILSON_EXTREMUM_CURVATURE_READOUT_BOUNDARY_CERTIFICATE_2026-06-15.md"

PASS = 0
FAIL = 0

BINOM_4 = [1, 4, 6, 4, 1]
U0 = Fraction(8776, 10000)
N_TASTE = Fraction(16)


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(f" {title}")
    print("-" * 88)


NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
NOTE_FLAT = re.sub(r"\s+", " ", NOTE_TEXT)


def all_orders_curv_scale_sq_over_v_sq(r: Fraction, u0: Fraction = U0) -> Fraction:
    """All-orders diagnostic (m_curv,W/v)^2 from the centered Wilson form."""
    u0sq = u0 * u0
    rsq = r * r
    total = Fraction(0)
    for k, mult in enumerate(BINOM_4):
        x = (k - 2) ** 2 * rsq
        total += mult * (u0sq - x) / ((x + u0sq) ** 2)
    return total / 64


def leading_curv_scale_sq_over_v_sq(r: Fraction, u0: Fraction = U0) -> Fraction:
    return Fraction(1, 4) / (u0 * u0) - Fraction(3, 4) * (r * r) / (u0 ** 4)


def part1_note_structure() -> None:
    section("Part 1: note structure and boundaries")
    markers = [
        ("claim type", "Claim type:** bounded_theorem"),
        ("status authority", "independent audit lane only"),
        ("closed native layer", "Closed native layer"),
        ("declared diagnostic layer", "Declared diagnostic layer"),
        ("open physical layer", "Open physical layer"),
        ("staircase normalization", "W(hw) = 2 r hw"),
        ("diagnostic count", "N_taste = 16"),
        ("not a Higgs pole", "physical Higgs pole"),
        ("no Wilson coefficient derivation", "does not derive the numerical Wilson coefficient"),
        ("Taylor expansion", "sqrt(1 - x) = 1 - x/2 - x^2/8 + O(x^3)"),
        ("all-orders context", "WILSON_M_H_TREE_AT_EXTREMUM_ALL_ORDERS_BOUNDED_NOTE_2026-05-08"),
        ("channel boundary dependency", "HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08"),
        ("verification section", "## Verification"),
    ]
    for label, marker in markers:
        check(f"contains {label}", marker in NOTE_TEXT or marker in NOTE_FLAT, repr(marker))


def part2_binomial_and_normalization() -> None:
    section("Part 2: binomial staircase and Wilson normalization")
    check("sum binom(4,k) = 16", sum(BINOM_4) == 16)
    raw_second = sum(mult * k * k for k, mult in enumerate(BINOM_4))
    first = sum(mult * k for k, mult in enumerate(BINOM_4))
    centered = sum(mult * (k - 2) ** 2 for k, mult in enumerate(BINOM_4))
    check("sum binom(4,k) k = 32", first == 32, str(first))
    check("sum binom(4,k) k^2 = 80", raw_second == 80, str(raw_second))
    check("sum binom(4,k)(k-2)^2 = 16", centered == 16, str(centered))

    # The Wilson coefficient normalization is symbolic: the mass shift is 2 r hw.
    r = Fraction(7, 100)
    shifts = [2 * r * k for k in range(5)]
    expected = [Fraction(0), Fraction(14, 100), Fraction(28, 100), Fraction(42, 100), Fraction(56, 100)]
    check("Wilson shift law W(hw)=2 r hw evaluated symbolically", shifts == expected, str(shifts))


def part3_leading_curvature_readout() -> None:
    section("Part 3: leading curvature-scale readout")
    # Total curvature magnitude from the upstream leading extremum note:
    # K_total = 4/u0^2 - 12 r^2/u0^4 + O(r^4).
    # Diagnostic per-channel scale divides by N_taste=16.
    r = Fraction(3, 100)
    u0sq = U0 * U0
    total_mag_leading = Fraction(4, 1) / u0sq - Fraction(12, 1) * r * r / (u0sq * u0sq)
    per_channel = total_mag_leading / N_TASTE
    formula = Fraction(1, 4) / u0sq * (1 - 3 * r * r / u0sq)
    check("total leading curvature divided by 16 equals formula (1)", per_channel == formula)

    coeff = (Fraction(1, 4) / u0sq - formula) / (r * r / (u0sq * u0sq))
    check("leading r^2 coefficient in (m_curv,W/v)^2 is -3/4 u0^-4", coeff == Fraction(3, 4), str(coeff))


def part4_all_orders_residual_scaling() -> None:
    section("Part 4: all-orders closed form vs leading Taylor residual")
    residuals: list[Fraction] = []
    for r in [Fraction(1, 20), Fraction(1, 40), Fraction(1, 80)]:
        closed = all_orders_curv_scale_sq_over_v_sq(r)
        leading = leading_curv_scale_sq_over_v_sq(r)
        residual = abs(closed - leading)
        residuals.append(residual)
        print(
            f"  r={float(r):.5f}: closed={float(closed):.10f}, "
            f"leading={float(leading):.10f}, residual={float(residual):.3e}"
        )
    ratios = [float(residuals[i] / residuals[i + 1]) for i in range(len(residuals) - 1)]
    # Halving r should shrink the O(r^4) residual by about 16. Allow a
    # broad exact-computation window because higher powers are present.
    check("closed-minus-leading residual has O(r^4) scaling under r halving", all(10.0 < q < 25.0 for q in ratios), str(ratios))


def part5_mass_taylor_residuals() -> None:
    section("Part 5: square-root Taylor residual check")
    rows = []
    for r in [0.01, 0.02, 0.04]:
        x = 3.0 * r * r / float(U0 * U0)
        closed = math.sqrt(1.0 - x)
        t1 = 1.0 - x / 2.0
        t2 = 1.0 - x / 2.0 - x * x / 8.0
        e1 = abs(closed - t1)
        e2 = abs(closed - t2)
        rows.append((x, e1, e2))
        print(f"  r={r:.3f}, x={x:.6e}, closed={closed:.12f}, e1={e1:.3e}, e2={e2:.3e}")

    check("second Taylor truncation improves over first at all sampled r", all(e2 < e1 for _, e1, e2 in rows))
    coeffs1 = [e1 / (x * x) for x, e1, _ in rows]
    coeffs2 = [e2 / (x * x * x) for x, _, e2 in rows]
    check("first residual coefficient is near 1/8", all(0.11 < c < 0.14 for c in coeffs1), str(coeffs1))
    check("second residual coefficient is near 1/16", all(0.055 < c < 0.075 for c in coeffs2), str(coeffs2))


def part6_forbidden_imports_and_scope() -> None:
    section("Part 6: import and scope guard")
    runner_text = Path(__file__).read_text(encoding="utf-8")
    import_lines = [
        ln.strip() for ln in runner_text.splitlines()
        if ln.strip().startswith("import ") or ln.strip().startswith("from ")
    ]
    allowed = {"__future__", "fractions", "pathlib", "math", "re", "sys"}
    bad = []
    for line in import_lines:
        mod = line.split()[1].split(".")[0]
        if mod not in allowed:
            bad.append(line)
    check("stdlib-only imports", not bad, str(bad) if bad else "clean")

    forbidden_claims = [
        "derives the physical Higgs pole",
        "derives r",
        "retained by this source note",
    ]
    for token in forbidden_claims:
        check(f"forbidden overclaim absent: {token}", token not in NOTE_TEXT)


def main() -> int:
    print("=" * 88)
    print(" wilson_extremum_curvature_readout_boundary_2026_06_15.py")
    print("=" * 88)
    part1_note_structure()
    part2_binomial_and_normalization()
    part3_leading_curvature_readout()
    part4_all_orders_residual_scaling()
    part5_mass_taylor_residuals()
    part6_forbidden_imports_and_scope()
    print()
    print("=" * 88)
    print(f" TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    if FAIL == 0:
        print(" VERDICT: Wilson extremum curvature readout boundary certified; native")
        print(" leading coefficient and Taylor residuals verified, with physical")
        print(" Higgs-pole and Wilson-coefficient readings explicitly outside scope.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
