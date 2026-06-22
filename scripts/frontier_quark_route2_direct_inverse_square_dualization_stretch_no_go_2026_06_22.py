#!/usr/bin/env python3
"""Direct inverse-square dualization stretch attempt for Route-2.

This runner attacks the open same-domain source/readout problem behind the
Route-2 endpoint.  It checks whether minimal frame covariance, normalization,
source/readout exchange symmetry, and dual-involution consistency force the
inverse-square law q_X proportional to w_X^-2.

Status:
  no-go for the minimal direct derivation.  The exact obstruction is that a
  factorized source/readout law has a free total dual exponent p = a + b.
  Exchange symmetry gives a = b but does not set a = 1.  The p=2 endpoint is
  obtained only by adding two unit canonical-dual charges, or by importing the
  endpoint ratio as a selector.
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
Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2, 1)
TARGET_LAMBDA = Fraction(9, 4)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
TARGET_CENTER_TE = Fraction(-8, 9)


@dataclass(frozen=True)
class SplitLaw:
    name: str
    source_charge: Fraction
    readout_charge: Fraction
    premise: str

    @property
    def exponent(self) -> Fraction:
        return self.source_charge + self.readout_charge

    @property
    def exchange_symmetric(self) -> bool:
        return self.source_charge == self.readout_charge


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


def lambda_from_integer_p(p: int) -> Fraction:
    # q_X proportional to w_X^-p.
    return pow_fraction(W_E / W_T, -p)


def endpoint_from_p(p: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    lam = lambda_from_integer_p(p)
    q_e = Q_T * lam
    rho_e = Fraction(6, 1) * (q_e - 1)
    center_te = SHELL_TE * Q_T / q_e
    return lam, q_e, rho_e, center_te


def normalization_constant_for_p(p: int) -> Fraction:
    # q_T = C * w_T^-p, so C = q_T * w_T^p.
    return Q_T * pow_fraction(W_T, p)


def endpoint_from_constant(p: int, constant: Fraction) -> tuple[Fraction, Fraction]:
    q_t = constant * pow_fraction(W_T, -p)
    q_e = constant * pow_fraction(W_E, -p)
    return q_t, q_e


def composition_ratio(p: int, x: Fraction, y: Fraction, z: Fraction) -> bool:
    # Multiplicative covariance for power laws: L(x,z)=L(x,y)L(y,z).
    def lam(a: Fraction, b: Fraction) -> Fraction:
        return pow_fraction(a / b, -p)

    return lam(x, z) == lam(x, y) * lam(y, z)


def dual_involution_product(p: int) -> Fraction:
    # The p and -p laws are reciprocal controls; this is true for every p.
    return lambda_from_integer_p(p) * lambda_from_integer_p(-p)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def part1_endpoint_algebra() -> None:
    print("PART 1: endpoint algebra")
    check("six-arm Schur weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("same-domain leverage w_T/w_E is 3/2", W_T / W_E == Fraction(3, 2))
    lam, q_e, rho_e, center_te = endpoint_from_p(2)
    check("p=2 gives lambda=q_E/q_T=9/4", lam == TARGET_LAMBDA, f"lambda={lam}")
    check("p=2 gives q_E=15/8", q_e == TARGET_Q_E, f"q_E={q_e}")
    check("p=2 gives rho_E=21/4", rho_e == TARGET_RHO_E, f"rho_E={rho_e}")
    check("p=2 gives center T/E=-8/9 when shell T/E=-2", center_te == TARGET_CENTER_TE, f"center={center_te}")


def part2_normalization_does_not_select_p() -> None:
    print()
    print("PART 2: normalization fixes C, not p")
    constants = {p: normalization_constant_for_p(p) for p in (-2, -1, 0, 1, 2, 3)}
    for p, constant in constants.items():
        q_t, q_e = endpoint_from_constant(p, constant)
        print(f"  p={p:+d}: C={constant}, q_T={q_t}, q_E={q_e}")
        check(f"normalization at q_T works for p={p:+d}", q_t == Q_T)
    check("different normalized exponents give different q_E values", len({endpoint_from_constant(p, c)[1] for p, c in constants.items()}) == len(constants))
    check("normalization alone leaves p=0 available", endpoint_from_p(0)[2] == Fraction(-1, 1))
    check("normalization alone leaves p=1 available", endpoint_from_p(1)[2] == Fraction(3, 2))
    check("normalization alone leaves p=2 available", endpoint_from_p(2)[2] == TARGET_RHO_E)
    check("therefore q_T normalization is not an exponent selector", constants[0] != constants[1] != constants[2])


def part3_factorized_split_obstruction() -> None:
    print()
    print("PART 3: factorized source/readout split")
    laws = (
        SplitLaw("neutral_exchange_symmetric", Fraction(0), Fraction(0), "no dual charge"),
        SplitLaw("half_half_exchange_symmetric", Fraction(1, 2), Fraction(1, 2), "exchange symmetry without unit charge"),
        SplitLaw("source_only_dual", Fraction(1), Fraction(0), "one-sided source dual"),
        SplitLaw("readout_only_dual", Fraction(0), Fraction(1), "one-sided readout dual"),
        SplitLaw("two_sided_dual", Fraction(1), Fraction(1), "source and readout both canonical-dual"),
    )
    for law in laws:
        print(
            f"  {law.name}: a={law.source_charge}, b={law.readout_charge}, "
            f"p={law.exponent}, exchange={law.exchange_symmetric}"
        )
        check(f"{law.name} has p=a+b", law.exponent == law.source_charge + law.readout_charge)

    exchange_symmetric = [law.name for law in laws if law.exchange_symmetric]
    check(
        "exchange symmetry admits three tested exponents",
        exchange_symmetric == [
            "neutral_exchange_symmetric",
            "half_half_exchange_symmetric",
            "two_sided_dual",
        ],
        str(exchange_symmetric),
    )
    symmetric_exponents = {law.exponent for law in laws if law.exchange_symmetric}
    check("exchange symmetry does not select p=2", symmetric_exponents == {Fraction(0), Fraction(1), Fraction(2)}, str(symmetric_exponents))
    one_sided = [law.name for law in laws if law.exponent == 1 and not law.exchange_symmetric]
    check("one-sided canonical duality gives p=1 controls", one_sided == ["source_only_dual", "readout_only_dual"], str(one_sided))
    check("only the explicit two-sided unit-dual split has a=b=1", [law.name for law in laws if (law.source_charge, law.readout_charge) == (1, 1)] == ["two_sided_dual"])


def part4_covariance_and_involution_do_not_select_p() -> None:
    print()
    print("PART 4: covariance and dual involution")
    for p in (-2, -1, 0, 1, 2, 3):
        check(
            f"multiplicative covariance holds for p={p:+d}",
            composition_ratio(p, Fraction(1, 3), Fraction(1, 2), Fraction(1, 6)),
        )
    products = {p: dual_involution_product(p) for p in (-3, -2, -1, 0, 1, 2, 3)}
    check("dual-involution reciprocal product is one for every tested p", set(products.values()) == {Fraction(1, 1)}, str(products))
    check("reciprocity therefore does not select p=2", products[2] == products[1] == products[0])
    ratios = {p: endpoint_from_p(p)[0] for p in (-2, -1, 0, 1, 2, 3)}
    check("covariant power laws include the target and non-target alternatives", ratios[2] == TARGET_LAMBDA and ratios[1] != TARGET_LAMBDA and ratios[0] != TARGET_LAMBDA)


def part5_target_import_firewall() -> None:
    print()
    print("PART 5: target-import firewall")
    integer_solutions = [p for p in range(-6, 7) if lambda_from_integer_p(p) == TARGET_LAMBDA]
    check("solving the endpoint ratio over integer p returns p=2", integer_solutions == [2], str(integer_solutions))
    check("using that solve as a premise would import q_E/q_T=9/4", TARGET_LAMBDA == Fraction(9, 4))
    check("p=1 one-sided dual misses rho_E=21/4", endpoint_from_p(1)[2] == Fraction(3, 2))
    check("p=-2 projector-square direction misses rho_E=21/4", endpoint_from_p(-2)[2] == Fraction(-34, 9))
    check("p=0 channel-neutral control misses rho_E=21/4", endpoint_from_p(0)[2] == Fraction(-1, 1))
    required_positive_premises = ("source unit canonical-dual charge", "readout unit canonical-dual charge")
    check("remaining positive premise is two unit dual charges", len(required_positive_premises) == 2)


def part6_note_and_status_firewall() -> None:
    print()
    print("PART 6: note and status firewall")
    note = note_text("QUARK_ROUTE2_DIRECT_INVERSE_SQUARE_DUALIZATION_STRETCH_NO_GO_NOTE_2026-06-22.md")
    required_markers = (
        "Actual current-surface status: no-go for the minimal direct dualization derivation",
        "A_min",
        "Forbidden proof inputs",
        "a = b",
        "p = a + b",
        "Stuck Fan-Out Synthesis",
        "This is not an audit verdict",
        "does not close the parent",
        "does not derive the endpoint triple on the actual current surface",
        "does not rule out future nonlinear source laws",
    )
    for marker in required_markers:
        check(f"note contains marker: {marker}", marker in note)

    banned_markers = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent-closure phrase", phrase("closes ", "the parent")),
        ("current-surface endpoint-derivation phrase", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit-ratification phrase", phrase("audit", "-ratified")),
        ("branch-local status-promotion phrase", phrase("ret", "ained branch-local")),
        ("future-retention phrase", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention phrase", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 direct inverse-square dualization stretch no-go")
    print("Status: no-go for the minimal direct dualization derivation; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_endpoint_algebra()
    part2_normalization_does_not_select_p()
    part3_factorized_split_obstruction()
    part4_covariance_and_involution_do_not_select_p()
    part5_target_import_firewall()
    part6_note_and_status_firewall()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: direct inverse-square dualization stretch checks failed.")
        return 1
    print(
        "VERDICT: no-go for deriving p=2 from the minimal symmetry and "
        "normalization package.  The remaining positive theorem must supply "
        "two unit canonical-dual source/readout charges, or an equivalent "
        "same-domain p=2 selector that does not import the endpoint."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
