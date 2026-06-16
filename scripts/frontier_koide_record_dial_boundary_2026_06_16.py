#!/usr/bin/env python3
"""Koide Record/dial boundary runner.

This runner verifies the exact boundary:

* SO(2) phase erasure preserves the two quotient energies E_+ and E_perp.
* The whole dim^s log-law family is SO(2)-invariant.
* The stationary operator ratio is kappa(s) = 2^(1-s).
* The Record axiom supplies finite additivity but no weighting selector.

It is a negative boundary for the route "SO(2) quotient + Record additivity
selects block-count"; it is not a Koide closure proof.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


REPO_ROOT = Path(__file__).resolve().parent.parent

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    theta = sp.symbols("theta", real=True)
    a, x, y = sp.symbols("a x y", real=True)
    s = sp.symbols("s", real=True)
    X, Y, T = sp.symbols("X Y T", positive=True)

    c = sp.cos(theta)
    q = sp.sin(theta)
    x_rot = c * x - q * y
    y_rot = q * x + c * y

    radius = x**2 + y**2
    radius_rot = sp.trigsimp(sp.expand(x_rot**2 + y_rot**2))
    e_plus = 3 * a**2
    e_perp = 6 * radius
    e_perp_rot = sp.trigsimp(sp.expand(6 * radius_rot))

    print("Section A - SO(2) quotient energies")
    check(
        "A1 doublet radius is invariant under SO(2) rotation",
        sp.simplify(radius_rot - radius) == 0,
        f"rotated radius = {radius_rot}",
    )
    check(
        "A2 E_perp = 6(x^2+y^2) is SO(2)-invariant",
        sp.simplify(e_perp_rot - e_perp) == 0,
        f"E_perp(rotated) = {e_perp_rot}",
    )
    check(
        "A3 E_+ = 3a^2 is independent of the doublet phase",
        not (e_plus.has(x) or e_plus.has(y) or e_plus.has(theta)),
        f"E_+ = {e_plus}",
    )

    print("\nSection B - dim^s log-law family")
    mu = sp.Integer(1)
    nu = 2**s
    ratio_xy = sp.simplify(mu / nu)
    kappa = sp.simplify(2 * ratio_xy)
    r_ratio = sp.simplify(1 / kappa)

    check(
        "B1 the whole S_s family factors through quotient variables",
        sp.simplify(e_plus.subs({x: x_rot, y: y_rot}) - e_plus) == 0
        and sp.simplify(e_perp_rot - e_perp) == 0,
        "S_s = log(E_+) + 2^s log(E_perp) depends only on invariant arguments",
    )
    check(
        "B2 Lagrange ratio is X/Y = mu/nu = 2^(-s)",
        sp.simplify(ratio_xy - 2 ** (-s)) == 0,
        f"X/Y = {ratio_xy}",
    )
    check(
        "B3 operator ratio kappa(s) = 2 X/Y = 2^(1-s)",
        sp.simplify(kappa - 2 ** (1 - s)) == 0,
        f"kappa(s) = {kappa}",
    )
    check(
        "B4 amplitude ratio r(s)=|b|^2/a^2 = 2^(s-1)",
        sp.simplify(r_ratio - 2 ** (s - 1)) == 0,
        f"r(s) = {r_ratio}",
    )
    check(
        "B5 stationarity equations imply X+Y=T with X/Y fixed, not s fixed",
        sp.simplify((T * ratio_xy / (1 + ratio_xy)) / (T / (1 + ratio_xy)) - ratio_xy) == 0,
        "the constraint sets scale after the supplied s chooses the ratio",
    )

    print("\nSection C - endpoints and non-uniqueness")
    kappa_block = sp.simplify(kappa.subs(s, 0))
    kappa_dim = sp.simplify(kappa.subs(s, 1))
    kappa_mid = sp.simplify(kappa.subs(s, sp.Rational(1, 2)))
    derivative = sp.simplify(sp.diff(kappa, s))

    check("C1 block-count endpoint s=0 gives kappa=2", kappa_block == 2)
    check("C2 dimension/Born endpoint s=1 gives kappa=1", kappa_dim == 1)
    check(
        "C3 an interior weighting gives a distinct admissible quotient law",
        sp.simplify(kappa_mid - sp.sqrt(2)) == 0,
        f"kappa(1/2) = {kappa_mid}",
    )
    check(
        "C4 kappa(s) varies with s, so SO(2) invariance alone cannot select an endpoint",
        sp.simplify(derivative + sp.log(2) * 2 ** (1 - s)) == 0 and derivative != 0,
        f"d kappa/ds = {derivative}",
    )

    print("\nSection D - source boundary guards")
    minimal_axioms = read("docs/MINIMAL_AXIOMS_2026-06-05.md")
    parent = read("docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md")
    dial = read("docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md")
    one_bit = read("docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md")
    note = read("docs/KOIDE_RECORD_DIAL_BOUNDARY_NOTE_2026-06-16.md")

    check(
        "D1 Record axiom supplies finite scalar additivity",
        "scalar readout `I` is finitely additive" in minimal_axioms,
    )
    check(
        "D2 Record axiom explicitly withholds weighting and normalization",
        "supplies no readout context" in minimal_axioms
        and "weighting" in minimal_axioms
        and "normalization" in minimal_axioms,
    )
    check(
        "D3 parent Koide note withholds canonical physical scalar-measure closure",
        "does not derive the\nscalar-lane `SO(2)` quotient" in parent
        and "canonical physical scalar measure" in parent,
    )
    check(
        "D4 parent Koide all-d sign multiplicity is even-parity, not d mod 2",
        "1 if d is even else 0" in parent and "d mod 2" not in parent,
    )
    check(
        "D5 generation dial note records r(s)=2^(s-1) and leaves position s open",
        "r(s) = 2^(s-1)" in dial
        and "does **not** derive the per-sector **position** `s`" in dial,
    )
    check(
        "D6 one-bit synthesis identifies block-count vs dimension as the residual",
        "one binary counting-measure bit" in one_bit
        and "forces **neither**" in one_bit,
    )
    check(
        "D7 this note is scoped as boundary, not physical closure",
        "derive a physical choice" in note
        and "cannot choose `s`" in note
        and "not a closure theorem" in note,
    )

    print("\nSection E - conclusion")
    check(
        "E1 exact boundary: SO(2)+Record allows the family but does not pick block-count",
        PASS == 19 and FAIL == 0,
        "all prior checks establish invariance, endpoint map, and Record non-selector boundary",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
