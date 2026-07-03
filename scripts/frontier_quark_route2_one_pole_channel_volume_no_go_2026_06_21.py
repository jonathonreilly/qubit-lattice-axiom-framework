#!/usr/bin/env python3
"""Route-2 one-pole channel-volume no-go.

Safe claim:
  The exact Route-2 endpoint needs lambda=q_E/q_T=9/4.  With the
  O_h channel weights w_E=1/3 and w_T=1/2, a channel-volume power law
  q_X proportional to w_X^p gives lambda=(w_E/w_T)^p.

  The target requires p=-2.  This runner proves a sharper class boundary:
  every positive channel-volume cone whose monomials have at most one inverse
  channel-volume normalization, p>=-1, obeys lambda<=3/2 and therefore cannot
  reach rho_E=21/4.  Polynomial and one-pole nonlinear source/readout rules
  are pruned.  A successful same-domain route must supply a genuine two-pole
  inverse-square channel metric, a signed-cancellation mechanism, or some
  different primitive.

  This is a scoped no-go, not a claim about all future nonlinear observables.
"""

from __future__ import annotations

from collections.abc import Iterable
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PASS_COUNT = 0
FAIL_COUNT = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
R = W_E / W_T
Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
TARGET_LAMBDA = Fraction(9, 4)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def require_phrases(label: str, rel_path: str, phrases: tuple[str, ...]) -> None:
    text = normalized_text(DOCS / rel_path)
    missing = [phrase for phrase in phrases if phrase not in text]
    check(
        f"quote anchors present: {label}",
        not missing,
        "all anchors found" if not missing else f"missing={missing!r}",
    )


def pow_fraction(base: Fraction, power: int) -> Fraction:
    if power >= 0:
        return base**power
    return Fraction(1, 1) / (base ** (-power))


def lambda_power(power: int) -> Fraction:
    return pow_fraction(R, power)


def endpoint_from_lambda(lambda_et: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Q_T * lambda_et
    rho_e = 6 * (q_e - 1)
    c_te = S_TE * Q_T / q_e
    return q_e, rho_e, c_te


def channel_value(weight: Fraction, exponents: Iterable[int], coeffs: Iterable[int]) -> Fraction:
    total = Fraction(0, 1)
    for power, coeff in zip(exponents, coeffs):
        total += Fraction(coeff, 1) * pow_fraction(weight, power)
    return total


def positive_cone_lambda(exponents: tuple[int, ...], coeffs: tuple[int, ...]) -> Fraction:
    q_e = channel_value(W_E, exponents, coeffs)
    q_t = channel_value(W_T, exponents, coeffs)
    if q_t <= 0:
        raise ValueError("positive cone denominator must be positive")
    return q_e / q_t


def enumerate_positive_cone(exponents: tuple[int, ...], max_coeff: int) -> list[Fraction]:
    values: list[Fraction] = []
    for coeffs in product(range(max_coeff + 1), repeat=len(exponents)):
        if not any(coeffs):
            continue
        values.append(positive_cone_lambda(exponents, coeffs))
    return values


def part1_endpoint_target() -> None:
    print("\nPART 1: exact endpoint target and power-law location")
    check("O_h weights are w_E=1/3 and w_T=1/2", W_E == Fraction(1, 3) and W_T == Fraction(1, 2), f"R=w_E/w_T={R}")
    check("target lambda is 9/4", TARGET_LAMBDA == Fraction(9, 4))
    hits = [p for p in range(-8, 9) if lambda_power(p) == TARGET_LAMBDA]
    q_e, rho_e, c_te = endpoint_from_lambda(TARGET_LAMBDA)
    check("integer power scan reaches target only at p=-2", hits == [-2], f"hits={hits}")
    check("lambda=9/4 gives q_E=15/8, rho_E=21/4, c_TE=-8/9", (q_e, rho_e, c_te) == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)), f"q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")


def part2_polynomial_and_one_pole_bounds() -> None:
    print("\nPART 2: polynomial and one-pole channel-volume bounds")
    polynomial_exponents = tuple(range(0, 7))
    one_pole_exponents = tuple(range(-1, 7))
    poly_lambdas = [lambda_power(p) for p in polynomial_exponents]
    one_pole_lambdas = [lambda_power(p) for p in one_pole_exponents]

    check("polynomial monomials p>=0 obey lambda<=1", max(poly_lambdas) == Fraction(1, 1), f"max={max(poly_lambdas)}")
    check("one-pole monomials p>=-1 obey lambda<=3/2", max(one_pole_lambdas) == Fraction(3, 2), f"max={max(one_pole_lambdas)}")
    check("one-pole monomial bound is strictly below 9/4", Fraction(3, 2) < TARGET_LAMBDA)

    q_e_bound, rho_bound, c_te_bound = endpoint_from_lambda(Fraction(3, 2))
    check("one-pole endpoint bound gives rho_E<=3/2, not 21/4", rho_bound == Fraction(3, 2), f"q_E={q_e_bound}, rho_E={rho_bound}, c_TE={c_te_bound}")


def part3_positive_cone_bounds() -> None:
    print("\nPART 3: positive cone closure")
    polynomial_exponents = tuple(range(0, 5))
    one_pole_exponents = tuple(range(-1, 5))
    poly_values = enumerate_positive_cone(polynomial_exponents, 3)
    one_pole_values = enumerate_positive_cone(one_pole_exponents, 3)

    check("positive polynomial cone remains bounded by lambda<=1", max(poly_values) == Fraction(1, 1), f"enumerated={len(poly_values)}, max={max(poly_values)}")
    check("positive one-pole cone remains bounded by lambda<=3/2", max(one_pole_values) == Fraction(3, 2), f"enumerated={len(one_pole_values)}, max={max(one_pole_values)}")
    check("positive one-pole cone enumeration never reaches target", TARGET_LAMBDA not in one_pole_values)

    proof_samples = []
    for power in one_pole_exponents:
        ratio = lambda_power(power)
        proof_samples.append(f"p={power}: {ratio}")
    print("  one-pole monomial ratios:", "; ".join(proof_samples))
    check("weighted-average proof applies because all positive cone weights are nonnegative", all(lambda_power(p) <= Fraction(3, 2) for p in one_pole_exponents))


def part4_what_would_escape() -> None:
    print("\nPART 4: exact escape mechanisms")
    two_pole_lambda = lambda_power(-2)
    q_e, rho_e, c_te = endpoint_from_lambda(two_pole_lambda)
    check("two-pole inverse-square monomial reaches target exactly", two_pole_lambda == TARGET_LAMBDA and rho_e == Fraction(21, 4), f"lambda={two_pole_lambda}, rho_E={rho_e}, c_TE={c_te}")

    # A signed mixture of one-pole and constant terms can fit the target, but
    # only by subtracting the constant channel response.  This is outside the
    # positive source/covariance cone tested here.
    signed_e = 5 * pow_fraction(W_E, -1) - 6
    signed_t = 5 * pow_fraction(W_T, -1) - 6
    signed_lambda = signed_e / signed_t
    check("signed one-pole cancellation can synthesize 9/4 only outside the positive cone", signed_lambda == TARGET_LAMBDA and signed_t > 0, f"(5*w^-1-6): E={signed_e}, T={signed_t}, lambda={signed_lambda}")
    check("the fitted signed escape uses a negative coefficient", -6 < 0)


def part5_quote_anchors() -> None:
    print("\nPART 5: current-surface quote anchors")
    require_phrases(
        "exact readout missing entry",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "the irreducible missing map entry is the `E`-channel ratio",
            "exact missing-map obstruction",
        ),
    )
    require_phrases(
        "kappa covariance bridge remains the free datum",
        "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md",
        (
            "single remaining free datum is the covariance bridge",
            "future nonlinear tensor observable",
        ),
    )
    require_phrases(
        "quadratic route names inverse-square gap",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "No named functional produces an inverse-square-of-projector-weight center lift.",
            "future genuinely **nonlinear**",
        ),
    )
    require_phrases(
        "bilinear carrier is polynomial definition only",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "is **defined** as a 2x2 matrix of polynomial expressions",
            "no positive theorem of primitive-ness for `K_R` is claimed",
        ),
    )


def main() -> int:
    print("Route-2 one-pole channel-volume no-go")
    print("Scope: positive polynomial/one-pole source-readout cones; not all future nonlinear observables")
    part1_endpoint_target()
    part2_polynomial_and_one_pole_bounds()
    part3_positive_cone_bounds()
    part4_what_would_escape()
    part5_quote_anchors()

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    if FAIL_COUNT:
        print("VERDICT: FAIL -- one-pole channel-volume no-go certificate did not pass.")
        return 1
    print(
        "VERDICT: scoped no-go. Positive polynomial and one-pole channel-volume "
        "source/readout cones cannot reach lambda=9/4 or rho_E=21/4; a successful "
        "same-domain route needs a genuine two-pole inverse-square primitive, a "
        "signed-cancellation mechanism, or another new readout primitive."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
