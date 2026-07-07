#!/usr/bin/env python3
"""Conditional exact evaluation of supplied QCD beta0/beta1 templates."""

from __future__ import annotations

from fractions import Fraction
from math import isclose, pi
from pathlib import Path


NOTE_PATH = Path("docs/ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md")
PARENT_PATH = Path("docs/ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop.md")
EXPECTED_SUMMARY = "SUMMARY: PASS=30 FAIL=0"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" :: {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def close(a: float, b: float, rel: float = 1e-12, abs_: float = 1e-12) -> bool:
    return isclose(a, b, rel_tol=rel, abs_tol=abs_)


def su3_surface() -> tuple[Fraction, Fraction, Fraction]:
    """Return C_F, C_A, T_F for the declared SU(3) Gell-Mann surface."""
    n = Fraction(3, 1)
    c_f = (n * n - 1) / (2 * n)
    c_a = n
    t_f = Fraction(1, 2)
    return c_f, c_a, t_f


def beta0(n_f: int) -> Fraction:
    c_f, c_a, t_f = su3_surface()
    del c_f
    return Fraction(11, 3) * c_a - Fraction(4, 3) * t_f * n_f


def beta1(n_f: int) -> Fraction:
    c_f, c_a, t_f = su3_surface()
    return (
        Fraction(34, 3) * c_a * c_a
        - 4 * c_f * t_f * n_f
        - Fraction(20, 3) * c_a * t_f * n_f
    )


def beta_alpha_two_loop(alpha: float, n_f: int) -> float:
    """d alpha_s / d ln(mu) through the universal two-loop kernel."""
    b0 = float(beta0(n_f))
    b1 = float(beta1(n_f))
    return -b0 * alpha * alpha / (2.0 * pi) - b1 * alpha**3 / (8.0 * pi**2)


def beta_g_two_loop(g: float, n_f: int) -> float:
    """dg / d ln(mu) through the universal two-loop kernel."""
    b0 = float(beta0(n_f))
    b1 = float(beta1(n_f))
    return -b0 * g**3 / (16.0 * pi**2) - b1 * g**5 / (16.0 * pi**2) ** 2


def beta_a_two_loop(a: float, n_f: int) -> float:
    """da / d ln(mu) for a = alpha_s/(4 pi)."""
    b0 = float(beta0(n_f))
    b1 = float(beta1(n_f))
    return -2.0 * b0 * a * a - 2.0 * b1 * a**3


def main() -> int:
    print("=== Source-boundary checks ===")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    parent_text = PARENT_PATH.read_text(encoding="utf-8")
    required = [
        "**Claim type:** bounded_theorem",
        "**Type:** bounded_theorem",
        "bounded algebra/convention kernel conditional on supplied universal",
        "This note does not derive the universal `beta_0` or `beta_1` loop coefficient",
        "conditional on those supplied templates",
        "This note does not derive beta_2, beta_3, MSbar counterterms, or four-loop running.",
        "This note does not derive physical threshold masses.",
        "This note does not promote any downstream alpha_s(M_Z) value to retained status.",
    ]
    for phrase in required:
        check(f"note declares boundary: {phrase}", phrase in note_text)
    check(
        "parent alpha_s 4-loop partial note points to this standalone kernel",
        "ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md" in parent_text,
    )

    print("\n=== SU(3) surface and exact coefficients ===")
    c_f, c_a, t_f = su3_surface()
    check("C_F = (N^2 - 1)/(2N) = 4/3 at N=3", c_f == Fraction(4, 3))
    check("C_A = N = 3 at N=3", c_a == Fraction(3, 1))
    check("T_F = 1/2 on the Gell-Mann trace normalization", t_f == Fraction(1, 2))
    check("beta0(n_f) simplifies to 11 - 2 n_f / 3", all(beta0(nf) == Fraction(33 - 2 * nf, 3) for nf in range(17)))
    check("beta1(n_f) simplifies to 102 - 38 n_f / 3", all(beta1(nf) == Fraction(306 - 38 * nf, 3) for nf in range(17)))

    print("\n=== Active-flavor values ===")
    check("beta0(6) = 7", beta0(6) == Fraction(7, 1))
    check("beta0(5) = 23/3", beta0(5) == Fraction(23, 3))
    check("beta1(6) = 26", beta1(6) == Fraction(26, 1))
    check("beta1(5) = 116/3", beta1(5) == Fraction(116, 3))
    check("beta1(4) = 154/3", beta1(4) == Fraction(154, 3))
    check("beta1(3) = 64", beta1(3) == Fraction(64, 1))

    print("\n=== Structural properties ===")
    check("beta0 drops by 2/3 per active flavor", all(beta0(nf) - beta0(nf - 1) == Fraction(-2, 3) for nf in range(1, 17)))
    check("beta1 drops by 38/3 per active flavor", all(beta1(nf) - beta1(nf - 1) == Fraction(-38, 3) for nf in range(1, 17)))
    check("beta0 is positive through the asymptotic-freedom window n_f <= 16", all(beta0(nf) > 0 for nf in range(17)))
    check("beta1 sign transition is explicit: positive through n_f=8, negative from n_f=9", all(beta1(nf) > 0 for nf in range(9)) and beta1(9) < 0)

    print("\n=== Convention checks ===")
    alpha = 0.1
    g = (4.0 * pi * alpha) ** 0.5
    d_alpha_from_g = g * beta_g_two_loop(g, 5) / (2.0 * pi)
    check("g-convention beta converts to the alpha_s convention", close(d_alpha_from_g, beta_alpha_two_loop(alpha, 5)))
    a = alpha / (4.0 * pi)
    check("a = alpha_s/(4pi) convention gives da/dlnmu = -2 b0 a^2 - 2 b1 a^3", close(beta_alpha_two_loop(alpha, 5) / (4.0 * pi), beta_a_two_loop(a, 5)))
    term1 = abs(float(beta0(5)) * alpha * alpha / (2.0 * pi))
    term2 = abs(float(beta1(5)) * alpha**3 / (8.0 * pi**2))
    check("two-loop term is a bounded correction at alpha_s=0.1, n_f=5", term2 / term1 < 0.05, f"ratio={term2 / term1:.6f}")

    print("\n=== Falsifiers ===")
    wrong_beta1_no_cf = Fraction(34, 3) * c_a * c_a - Fraction(20, 3) * c_a * t_f * 6
    check("falsifier detects omission of the C_F term at n_f=6", wrong_beta1_no_cf != beta1(6), f"wrong={wrong_beta1_no_cf}, correct={beta1(6)}")
    wrong_tf = Fraction(1, 1)
    wrong_beta0 = Fraction(11, 3) * c_a - Fraction(4, 3) * wrong_tf * 6
    check("falsifier detects trace-normalization drift T_F=1", wrong_beta0 != beta0(6), f"wrong={wrong_beta0}, correct={beta0(6)}")
    wrong_nf = 3 * 3
    check("falsifier detects using generation count as active quark flavor count", beta0(wrong_nf) != beta0(6), f"wrong_nf={wrong_nf}")

    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    actual = f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}"
    if actual != EXPECTED_SUMMARY:
        print(f"EXPECTED_SUMMARY mismatch: {EXPECTED_SUMMARY}")
        return 1
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
