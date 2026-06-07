#!/usr/bin/env python3
"""Finite eta/spectral-flow selector no-go checks.

The target route asks whether eta or spectral flow can supply the missing
orientation/source selector by itself.  These finite checks isolate the exact
obstruction: spectral flow certifies an oriented crossing after a path
orientation or mass sign convention has been supplied.  Reversing that
orientation reverses the answer, so the invariant is not itself the canonical
selector.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Iterable


@dataclass
class Scorecard:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        status = "PASS" if condition else "FAIL"
        suffix = f" :: {detail}" if detail else ""
        print(f"[{status}] {label}{suffix}")
        if condition:
            self.passed += 1
        else:
            self.failed += 1


def sign(x: Fraction) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def eta(eigenvalues: Iterable[Fraction]) -> int:
    return sum(sign(x) for x in eigenvalues)


def scalar_spectral_flow(m0: Fraction, m1: Fraction) -> int:
    """Net upward crossings for the scalar family T(m)=[m]."""
    if m0 < 0 < m1:
        return 1
    if m1 < 0 < m0:
        return -1
    return 0


def paired_spectral_flow(m0: Fraction, m1: Fraction) -> int:
    """Net flow for the paired family diag(m,-m)."""
    return scalar_spectral_flow(m0, m1) + scalar_spectral_flow(-m0, -m1)


def scalar_eta(m: Fraction) -> int:
    return eta([m])


def paired_eta(m: Fraction) -> int:
    return eta([m, -m])


def bulk_chiral_pair_eta(gaps: Iterable[Fraction]) -> int:
    eigs: list[Fraction] = []
    for gap in gaps:
        eigs.extend([gap, -gap])
    return eta(eigs)


def finite_difference(f: Callable[[Fraction], int], x: Fraction, h: Fraction) -> Fraction:
    return Fraction(f(x + h) - f(x - h), 2) / h


def source_vector_without_cross_term() -> tuple[int, int]:
    return (1, 1)


def source_vector_with_supplied_eta_cross_term(chi: int) -> tuple[int, int]:
    return (chi, -chi)


def main() -> int:
    sc = Scorecard()

    minus = Fraction(-1, 1)
    plus = Fraction(1, 1)
    two = Fraction(2, 1)
    half = Fraction(1, 2)
    tenth = Fraction(1, 10)

    forward = scalar_spectral_flow(minus, plus)
    reverse = scalar_spectral_flow(plus, minus)
    sc.check(
        "oriented scalar crossing has positive spectral flow",
        forward == 1,
        f"sf[-1 -> +1]={forward}",
    )
    sc.check(
        "reversing the same crossing reverses spectral flow",
        reverse == -1,
        f"sf[+1 -> -1]={reverse}",
    )
    sc.check(
        "same unoriented endpoint pair carries both signs",
        {forward, reverse} == {-1, 1},
        f"possible signs={sorted({forward, reverse})}",
    )

    sc.check(
        "scalar eta jump matches twice the oriented crossing",
        scalar_eta(plus) - scalar_eta(minus) == 2 * forward,
        f"eta(+1)-eta(-1)={scalar_eta(plus)-scalar_eta(minus)}",
    )
    sc.check(
        "reverse scalar eta jump matches reversed crossing",
        scalar_eta(minus) - scalar_eta(plus) == 2 * reverse,
        f"eta(-1)-eta(+1)={scalar_eta(minus)-scalar_eta(plus)}",
    )

    gapped_forward = scalar_spectral_flow(plus, two)
    gapped_reverse = scalar_spectral_flow(two, plus)
    sc.check(
        "gapped positive deformation has zero spectral flow",
        gapped_forward == 0,
        f"sf[+1 -> +2]={gapped_forward}",
    )
    sc.check(
        "reversed gapped positive deformation also has zero spectral flow",
        gapped_reverse == 0,
        f"sf[+2 -> +1]={gapped_reverse}",
    )
    sc.check(
        "eta is locally constant on the gapped positive sector",
        scalar_eta(plus) == scalar_eta(two),
        f"eta(+1)={scalar_eta(plus)}, eta(+2)={scalar_eta(two)}",
    )
    sc.check(
        "finite difference of sign eta vanishes away from crossing",
        finite_difference(scalar_eta, plus, tenth) == 0,
        f"d_eta(+1;h=1/10)={finite_difference(scalar_eta, plus, tenth)}",
    )

    paired_forward = paired_spectral_flow(minus, plus)
    paired_reverse = paired_spectral_flow(plus, minus)
    sc.check(
        "paired chiral crossing has zero net spectral flow",
        paired_forward == 0,
        f"paired sf[-1 -> +1]={paired_forward}",
    )
    sc.check(
        "reversed paired chiral crossing remains zero",
        paired_reverse == 0,
        f"paired sf[+1 -> -1]={paired_reverse}",
    )
    sc.check(
        "paired eta vanishes on both sides of the crossing",
        (paired_eta(minus), paired_eta(plus)) == (0, 0),
        f"paired eta(-1,+1)=({paired_eta(minus)},{paired_eta(plus)})",
    )

    sc.check(
        "bulk chiral paired spectrum has zero eta",
        bulk_chiral_pair_eta([half, plus, two]) == 0,
        f"eta={{+/-1/2,+/-1,+/-2}} -> {bulk_chiral_pair_eta([half, plus, two])}",
    )
    sc.check(
        "bulk chiral paired eta stays zero under gap deformation",
        bulk_chiral_pair_eta([plus, Fraction(3, 2), two]) == 0,
        f"eta={{+/-1,+/-3/2,+/-2}} -> {bulk_chiral_pair_eta([plus, Fraction(3, 2), two])}",
    )

    # An unoriented invariant assigns the same value to a path and its reverse.
    # It cannot equal oriented spectral flow on a crossing path unless that
    # spectral flow vanishes.
    unoriented_value_forward = frozenset([minus, plus])
    unoriented_value_reverse = frozenset([plus, minus])
    sc.check(
        "unoriented path data cannot distinguish forward from reverse",
        unoriented_value_forward == unoriented_value_reverse,
        f"unoriented endpoints={sorted(unoriented_value_forward)}",
    )
    sc.check(
        "oriented spectral flow is not an unoriented path invariant",
        forward != reverse,
        f"forward={forward}, reverse={reverse}",
    )
    sc.check(
        "there is no nonzero equality to both orientations",
        not (forward == reverse and forward != 0),
        "nonzero oriented selector would require a supplied orientation",
    )

    selector_input = "start_negative_end_positive"
    selected_flow = forward if selector_input == "start_negative_end_positive" else reverse
    sc.check(
        "a supplied selector can choose the positive crossing sign",
        selected_flow == 1,
        f"selector={selector_input}, selected_flow={selected_flow}",
    )
    sc.check(
        "the selector is extra data rather than spectral flow alone",
        selector_input not in {"eta", "spectral_flow", "bulk_pairing"},
        f"selector_input={selector_input}",
    )

    retained_source = source_vector_without_cross_term()
    odd_source_plus = source_vector_with_supplied_eta_cross_term(+1)
    odd_source_minus = source_vector_with_supplied_eta_cross_term(-1)
    sc.check(
        "separable positive source stack is orientation-even",
        retained_source == (1, 1),
        f"source={retained_source}",
    )
    sc.check(
        "eta sign creates an odd source only when multiplied in",
        odd_source_plus == (1, -1) and odd_source_minus == (-1, 1),
        f"chi=+1->{odd_source_plus}, chi=-1->{odd_source_minus}",
    )
    sc.check(
        "orientation-even source is not the required odd source",
        retained_source != odd_source_plus,
        f"even={retained_source}, odd={odd_source_plus}",
    )

    no_native_selector_available = {
        "bulk_pairing": paired_eta(plus),
        "gapped_eta_derivative": finite_difference(scalar_eta, plus, tenth),
        "unoriented_crossing_signs": tuple(sorted({forward, reverse})),
    }
    sc.check(
        "native eta data expose ambiguity rather than selecting a branch",
        no_native_selector_available["bulk_pairing"] == 0
        and no_native_selector_available["gapped_eta_derivative"] == 0
        and no_native_selector_available["unoriented_crossing_signs"] == (-1, 1),
        f"native_data={no_native_selector_available}",
    )

    print(f"SCORECARD: PASS={sc.passed} FAIL={sc.failed}")
    return 0 if sc.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
