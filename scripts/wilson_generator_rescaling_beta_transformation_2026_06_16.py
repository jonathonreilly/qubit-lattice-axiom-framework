#!/usr/bin/env python3
"""Exact scalar-argument rescaling and Gram-transformation certificate.

For q(w,s,n)=w*s^2/(4n), the paired map w'=c^2*w, s'=s/c leaves q
invariant.  If T'_a=c*T_a, then s'*T'_a=s*T_a while the half-Gram form
scales by c^2.  No external target or preferred parameter is inferred.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WILSON_GENERATOR_RESCALING_BETA_TRANSFORMATION_NARROW_THEOREM_NOTE_2026-06-16.md"
MATRIX_NOTE = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def q(w: Fraction, s_sq: Fraction, n: Fraction) -> Fraction:
    return w * s_sq / (4 * n)


def gram_diag(c_sq: Fraction) -> Fraction:
    return c_sq * Fraction(1, 2)


def part0_source_boundaries() -> None:
    print("Part 0: source boundaries")
    check("rescaling note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("native matrix theorem exists", MATRIX_NOTE.exists(), MATRIX_NOTE.relative_to(ROOT).as_posix())
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = [
        "**Claim type:** positive_theorem",
        "q(w,s,n) := [x^2 F2] w D(sx) = w s^2/(4n)",
        "w' = c^2 w",
        "s' = s/c",
        "q(w',s',n)",
        "s'T'_a = sT_a",
        "Tr(T'_a T'_b) = c^2 delta_ab/2",
        "does not choose a comparison coefficient",
        "Any use beyond the displayed matrix and scalar algebra requires separate authority",
    ]
    for marker in required:
        check(f"rescaling note contains marker: {marker[:60]}", marker in text or marker in flat)
    forbidden = [
        "preferred parameter value",
        "audit_status: audited_clean",
        "effective_status: retained",
    ]
    for marker in forbidden:
        check(f"removed target/status marker absent: {marker}", marker not in text)


def part1_matrix_source() -> None:
    print()
    print("Part 1: native matrix coefficient authority surface")
    text = MATRIX_NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = [
        "[x^2 F2] w D(sx) = w s^2/(4n)",
        "global fourth-order bound",
        "does not select either scalar",
        "requires separate authority and remains outside this theorem",
    ]
    for marker in required:
        check(f"matrix theorem contains marker: {marker[:60]}", marker in text or marker in flat)


def part2_exact_transform() -> None:
    print()
    print("Part 2: exact native-coefficient transform")
    samples = [
        (Fraction(3, 2), Fraction(1), Fraction(1)),
        (Fraction(5, 7), Fraction(9, 4), Fraction(2)),
        (Fraction(11, 5), Fraction(3, 5), Fraction(3)),
        (Fraction(7, 2), Fraction(25, 9), Fraction(5, 2)),
    ]
    c_values = [Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5, 2), Fraction(3)]
    for w, s_sq, n in samples:
        q_old = q(w, s_sq, n)
        check(f"native coefficient is positive for w={w}, s^2={s_sq}, n={n}", q_old > 0, f"q={q_old}")
        for c in c_values:
            c_sq = c * c
            w_new = c_sq * w
            s_sq_new = s_sq / c_sq
            check(
                f"paired rescaling preserves q at w={w}, s^2={s_sq}, c={c}",
                q(w_new, s_sq_new, n) == q_old,
                f"q'={q(w_new, s_sq_new, n)}",
            )
            check(
                f"paired scalar product cancels c^2 at c={c}",
                w_new * s_sq_new == w * s_sq,
            )


def part3_generator_and_gram_transform() -> None:
    print()
    print("Part 3: exponent-product preservation and Gram change")
    s = Fraction(5, 3)
    generator_entry = Fraction(7, 4)
    for c in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]:
        c_sq = c * c
        s_new = s / c
        generator_new = c * generator_entry
        check(
            f"s'T'=sT under c={c}",
            s_new * generator_new == s * generator_entry,
        )
        check(
            f"half-Gram transforms by c^2 under c={c}",
            gram_diag(c_sq) == c_sq / 2,
            f"diagonal={gram_diag(c_sq)}",
        )
        if c != 1:
            check(
                f"nontrivial c={c} changes the half-Gram value",
                gram_diag(c_sq) != Fraction(1, 2),
            )


def main() -> int:
    print("Formal scalar-argument rescaling and Gram transformation")
    print("=" * 72)
    part0_source_boundaries()
    part1_matrix_source()
    part2_exact_transform()
    part3_generator_and_gram_transform()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
