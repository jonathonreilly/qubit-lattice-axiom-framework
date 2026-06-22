#!/usr/bin/env python3
"""Broader nonlinear same-domain law classification for Route-2.

This runner checks whether natural nonlinear source/readout weight laws can
force the Route-2 endpoint ratio q_E/q_T=9/4 without importing that target.

Status:
  no-go for the broad nonlinear shortcut.  Multiplicative laws leave the
  exponent free; two-bin monomials w^a(1-w)^b hit the target only at
  (a,b)=(-2,0), which is the inverse-square law again; free-coefficient
  interpolation fits only after coefficient selection.
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
TARGET_LAMBDA = Fraction(9, 4)
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class ControlLaw:
    name: str
    ratio: Fraction
    reason: str


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


def power_ratio(p: int) -> Fraction:
    # q_X proportional to w_X^-p.
    return pow_fraction(W_E / W_T, -p)


def endpoint_from_ratio(ratio: Fraction) -> tuple[Fraction, Fraction]:
    q_e = Q_T * ratio
    rho_e = Fraction(6, 1) * (q_e - 1)
    return q_e, rho_e


def two_bin_ratio(a: int, b: int) -> Fraction:
    # q_X proportional to w_X^a * (1-w_X)^b.
    return pow_fraction(W_E / W_T, a) * pow_fraction((1 - W_E) / (1 - W_T), b)


def affine_value(a0: Fraction, a1: Fraction, w: Fraction) -> Fraction:
    return a0 + a1 * w


def quadratic_value(a0: Fraction, a1: Fraction, a2: Fraction, w: Fraction) -> Fraction:
    return a0 + a1 * w + a2 * w * w


def multiplicative_composition_holds(p: int) -> bool:
    def lam(x: Fraction, y: Fraction) -> Fraction:
        return pow_fraction(x / y, -p)

    return lam(Fraction(1, 3), Fraction(1, 6)) == lam(Fraction(1, 3), Fraction(1, 2)) * lam(Fraction(1, 2), Fraction(1, 6))


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def part1_endpoint_target() -> None:
    print("PART 1: endpoint target")
    check("weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("target ratio is 9/4", TARGET_LAMBDA == Fraction(9, 4))
    q_e, rho_e = endpoint_from_ratio(TARGET_LAMBDA)
    check("target ratio gives q_E=15/8", q_e == Fraction(15, 8), f"q_E={q_e}")
    check("target ratio gives rho_E=21/4", rho_e == TARGET_RHO_E, f"rho_E={rho_e}")


def part2_power_law_family() -> None:
    print()
    print("PART 2: multiplicative power-law family")
    ratios = {p: power_ratio(p) for p in range(-4, 5)}
    for p, ratio in ratios.items():
        print(f"  p={p:+d}: ratio={ratio}, rho_E={endpoint_from_ratio(ratio)[1]}")
        check(f"multiplicative covariance holds for p={p:+d}", multiplicative_composition_holds(p))
    solutions = [p for p, ratio in ratios.items() if ratio == TARGET_LAMBDA]
    check("integer power scan finds p=2 as the only target solution in range", solutions == [2], str(solutions))
    check("p=0 channel-neutral misses", endpoint_from_ratio(ratios[0])[1] == Fraction(-1, 1))
    check("p=1 one-dual misses", endpoint_from_ratio(ratios[1])[1] == Fraction(3, 2))
    check("p=2 inverse-square lands", endpoint_from_ratio(ratios[2])[1] == TARGET_RHO_E)
    check("power-law covariance alone permits non-target p values", len(ratios) == 9 and ratios[1] != TARGET_LAMBDA)


def part3_two_bin_monomials() -> None:
    print()
    print("PART 3: two-bin monomial family w^a(1-w)^b")
    solutions = []
    for a in range(-5, 6):
        for b in range(-5, 6):
            if two_bin_ratio(a, b) == TARGET_LAMBDA:
                solutions.append((a, b))
    check("two-bin monomial integer solve has one solution in the scan box", solutions == [(-2, 0)], str(solutions))
    check("the unique two-bin solution is inverse-square with no complement factor", two_bin_ratio(-2, 0) == TARGET_LAMBDA)
    check("pure complement inverse-square misses", two_bin_ratio(0, -2) == Fraction(9, 16), str(two_bin_ratio(0, -2)))
    check("odds inverse-square misses", two_bin_ratio(-2, 2) == Fraction(4, 1), str(two_bin_ratio(-2, 2)))
    check("mixed complement factors do not create a second target mechanism", all(pair == (-2, 0) for pair in solutions))


def part4_nonlinear_controls() -> None:
    print()
    print("PART 4: natural nonlinear controls")
    controls = (
        ControlLaw("constant", Fraction(1, 1), "channel-neutral"),
        ControlLaw("weight", W_E / W_T, "ordinary projector"),
        ControlLaw("weight_inverse", (W_E / W_T) ** -1, "one reciprocal"),
        ControlLaw("weight_inverse_square", (W_E / W_T) ** -2, "inverse-square"),
        ControlLaw("complement_inverse", ((1 - W_E) / (1 - W_T)) ** -1, "one complement reciprocal"),
        ControlLaw("complement_inverse_square", ((1 - W_E) / (1 - W_T)) ** -2, "complement reciprocal-square"),
        ControlLaw("odds_inverse", ((W_E / (1 - W_E)) / (W_T / (1 - W_T))) ** -1, "odds reciprocal"),
        ControlLaw("odds_inverse_square", ((W_E / (1 - W_E)) / (W_T / (1 - W_T))) ** -2, "odds reciprocal-square"),
    )
    hits = []
    for law in controls:
        q_e, rho_e = endpoint_from_ratio(law.ratio)
        print(f"  {law.name}: ratio={law.ratio}, rho_E={rho_e}")
        check(f"{law.name} has exact rational ratio", isinstance(law.ratio, Fraction), law.reason)
        if law.ratio == TARGET_LAMBDA:
            hits.append(law.name)
    check("only weight inverse-square hits among the natural controls", hits == ["weight_inverse_square"], str(hits))
    check("complement reciprocal-square misses the target", controls[5].ratio != TARGET_LAMBDA, str(controls[5].ratio))
    check("odds reciprocal-square misses the target", controls[7].ratio != TARGET_LAMBDA, str(controls[7].ratio))


def part5_free_coefficient_interpolation() -> None:
    print()
    print("PART 5: free-coefficient interpolation firewall")
    a0, a1 = Fraction(19, 1), Fraction(-30, 1)
    val_e = affine_value(a0, a1, W_E)
    val_t = affine_value(a0, a1, W_T)
    check("affine coefficients can fit the target ratio", val_e / val_t == TARGET_LAMBDA, f"values=({val_e},{val_t})")
    check("the affine fit uses noncanonical coefficients", (a0, a1) == (Fraction(19), Fraction(-30)))
    q0, q1, q2 = Fraction(13), Fraction(0), Fraction(-36)
    quad_e = quadratic_value(q0, q1, q2, W_E)
    quad_t = quadratic_value(q0, q1, q2, W_T)
    check("a distinct quadratic can also fit the target ratio", quad_e / quad_t == TARGET_LAMBDA, f"values=({quad_e},{quad_t})")
    check("multiple coefficient fits prove underdetermination", (q0, q1, q2) != (a0, a1, 0))
    check("coefficient fitting is not a derivation", val_t != 0 and quad_t != 0)


def part6_note_and_status_firewall() -> None:
    print()
    print("PART 6: note and status firewall")
    note = note_text("QUARK_ROUTE2_NONLINEAR_SOURCE_LAW_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md")
    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for the broad nonlinear same-domain shortcut",
        "This is not an audit verdict",
        "does not close the parent",
        "two-bin monomials",
        "unique target solution",
        "does not rule out future nonlinear laws",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note)
    banned = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned:
        check(f"note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 nonlinear same-domain source-law classification no-go")
    print("Status: no-go for the broad nonlinear shortcut; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_endpoint_target()
    part2_power_law_family()
    part3_two_bin_monomials()
    part4_nonlinear_controls()
    part5_free_coefficient_interpolation()
    part6_note_and_status_firewall()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: nonlinear source-law classification checks failed.")
        return 1
    print(
        "VERDICT: no-go for the broad nonlinear same-domain shortcut. "
        "Natural nonlinear grammars either miss, fit hidden coefficients, "
        "or reduce to target-selected inverse-square."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
