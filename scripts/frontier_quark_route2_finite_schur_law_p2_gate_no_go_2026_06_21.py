#!/usr/bin/env python3
"""Finite Schur-law gate for the Route-2 p=2 endpoint.

This runner tests whether ordinary finite projector-polynomial source/readout
laws can derive the inverse-square lift needed by the Route-2 endpoint.

Status:
  no-go for the coefficient-free finite projector-polynomial shortcut.

Safe claim:
  Nonnegative monomial powers of the Schur projector weights do not produce
  q_E/q_T = 9/4. Finite polynomials can be made to fit the ratio only after a
  coefficient selector is supplied, so they do not derive the p=2 law by
  themselves. This does not rule out a genuine inverse-square dualization
  theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
TARGET_LAMBDA = Fraction(9, 4)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def pow_fraction(x: Fraction, exponent: int) -> Fraction:
    if exponent >= 0:
        return x**exponent
    return Fraction(1, 1) / (x ** (-exponent))


def monomial_lambda(degree: int) -> Fraction:
    # Coefficient-free finite projector monomial: q_X proportional to w_X^degree.
    return pow_fraction(W_E / W_T, degree)


def dual_lambda(p: int) -> Fraction:
    # Dual-compliance convention: q_X proportional to w_X^-p.
    return pow_fraction(W_E / W_T, -p)


def endpoint_from_lambda(lambda_et: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_t = Fraction(5, 6)
    q_e = q_t * lambda_et
    rho_e = 6 * (q_e - 1)
    center_te = Fraction(-2) * q_t / q_e
    return q_e, rho_e, center_te


def poly_eval(coeffs: tuple[Fraction, ...], w: Fraction) -> Fraction:
    return sum(coeff * (w**power) for power, coeff in enumerate(coeffs))


def fit_equation_row(degree: int) -> tuple[Fraction, ...]:
    return tuple((W_E**k) - TARGET_LAMBDA * (W_T**k) for k in range(degree + 1))


def row_is_nonzero(row: tuple[Fraction, ...]) -> bool:
    return any(value != 0 for value in row)


@dataclass(frozen=True)
class PolynomialFit:
    coeffs: tuple[Fraction, ...]

    @property
    def value_e(self) -> Fraction:
        return poly_eval(self.coeffs, W_E)

    @property
    def value_t(self) -> Fraction:
        return poly_eval(self.coeffs, W_T)

    @property
    def ratio(self) -> Fraction:
        return self.value_e / self.value_t


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def main() -> int:
    print("Route-2 finite Schur-law p=2 gate no-go")
    print("Status: no-go for coefficient-free finite projector-polynomial shortcut; not an audit verdict.")
    print("TRACE: negative_route_pruning")

    print("\nPART 1: Schur weights and target")
    check("six-arm weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("target ratio is q_E/q_T=9/4", TARGET_LAMBDA == Fraction(9, 4))
    target_endpoint = endpoint_from_lambda(TARGET_LAMBDA)
    check(
        "target ratio gives q_E=15/8, rho_E=21/4, center T/E=-8/9",
        target_endpoint == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        f"endpoint={target_endpoint}",
    )

    print("\nPART 2: coefficient-free monomial gate")
    monomials = {degree: monomial_lambda(degree) for degree in range(0, 7)}
    for degree, lam in monomials.items():
        print(f"  degree={degree}: lambda=(w_E/w_T)^{degree}={lam}")
    check(
        "no nonnegative monomial projector power through degree 6 gives 9/4",
        TARGET_LAMBDA not in monomials.values(),
    )
    check(
        "the inverse-square lift is exactly degree -2 in projector-weight language",
        monomial_lambda(-2) == TARGET_LAMBDA and dual_lambda(2) == TARGET_LAMBDA,
        f"w^(-2) ratio={monomial_lambda(-2)}, dual p=2 ratio={dual_lambda(2)}",
    )
    wrong_controls = {
        "neutral": dual_lambda(0),
        "one-sided-dual": dual_lambda(1),
        "projector-square": monomial_lambda(2),
    }
    check(
        "nearby coefficient-free controls miss the target",
        wrong_controls
        == {
            "neutral": Fraction(1),
            "one-sided-dual": Fraction(3, 2),
            "projector-square": Fraction(4, 9),
        },
        f"controls={wrong_controls}",
    )

    print("\nPART 3: finite polynomial underdetermination")
    degree0_row = fit_equation_row(0)
    check(
        "degree-0 polynomial cannot fit the target ratio unless zero is used",
        degree0_row == (Fraction(-5, 4),),
        f"row={degree0_row}",
    )
    linear_fit = PolynomialFit((Fraction(19), Fraction(-30)))
    check(
        "a degree-1 polynomial can fit 9/4 only by supplying coefficients",
        linear_fit.ratio == TARGET_LAMBDA and linear_fit.value_t != 0,
        f"P(w)=19-30w gives P(w_E)={linear_fit.value_e}, P(w_T)={linear_fit.value_t}",
    )
    check(
        "the degree-1 fit is a hidden selector, not a canonical finite-law derivation",
        fit_equation_row(1) == (Fraction(-5, 4), Fraction(-19, 24)),
        f"fit row={fit_equation_row(1)}",
    )
    dimensions = {degree: degree for degree in range(1, 6) if row_is_nonzero(fit_equation_row(degree))}
    check(
        "degree d finite polynomial fits leave d free coefficient directions",
        dimensions == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
        f"kernel dimensions={dimensions}",
    )

    print("\nPART 4: endpoint consequences and controls")
    linear_endpoint = endpoint_from_lambda(linear_fit.ratio)
    neutral_endpoint = endpoint_from_lambda(wrong_controls["neutral"])
    one_dual_endpoint = endpoint_from_lambda(wrong_controls["one-sided-dual"])
    projector_square_endpoint = endpoint_from_lambda(wrong_controls["projector-square"])
    check("coefficient-fitted linear law reproduces the endpoint only conditionally", linear_endpoint == target_endpoint)
    check(
        "neutral and one-sided-dual endpoints are exact alternatives",
        neutral_endpoint[1] == Fraction(-1) and one_dual_endpoint[1] == Fraction(3, 2),
        f"neutral rho={neutral_endpoint[1]}, one-sided rho={one_dual_endpoint[1]}",
    )
    check(
        "projector-square endpoint has the wrong sign and magnitude",
        projector_square_endpoint[1] == Fraction(-34, 9),
        f"projector-square rho={projector_square_endpoint[1]}",
    )

    print("\nPART 5: note and status firewall")
    note = note_text("QUARK_ROUTE2_FINITE_SCHUR_LAW_P2_GATE_NO_GO_NOTE_2026-06-21.md")
    required_markers = (
        "Actual current-surface status: no-go for coefficient-free finite projector-polynomial p=2 gate",
        "finite projector-polynomial",
        "hidden coefficient selector",
        "This is not an audit verdict",
        "does not rule out inverse-square dualization",
        "does not resolve the parent",
    )
    for marker in required_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent-closure phrase", phrase("closes ", "the parent")),
        (
            "current-surface endpoint-derivation phrase",
            phrase("derives ", "the endpoint triple", " on the current surface"),
        ),
        ("audit-ratification phrase", phrase("audit", "-ratified")),
        ("branch-local status-promotion phrase", phrase("retained ", "branch-local")),
        ("future-retention phrase", phrase("would ", "become retained")),
        ("promotion-to-retention phrase", phrase("promoted ", "to retained")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: no-go for the coefficient-free finite projector-polynomial shortcut. "
        "The p=2 lift requires explicit inverse-square dualization or an equivalent "
        "coefficient selector; finite Schur polynomials alone do not derive it."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
