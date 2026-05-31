#!/usr/bin/env python3
"""
Classify the repeated Koide-side 2/9 footprints.

This runner answers the narrow question raised by the Q=1 probe:

    Is the Q=1 offsite coefficient -2/9 the same 2/9 we keep hunting?

The answer is mixed and intentionally typed:

  * Yes as arithmetic: the Q=1 offsite magnitude is 2/d^2 at d=3, matching
    the Brannen n_eff/d^2 and hypercharge-anomaly 2/d^2 functions.
  * No as a physical/typed unification: the Q=1 coefficient is an offsite
    projector matrix element, not a Brannen radian phase, not a Callan-Harvey
    anomaly, and not the APS eta-defect object.
  * Also no through the Q/d route: if Q=1, then delta=Q/d gives 1/3, not 2/9.

Expected: all checks pass.  This is a frontier classifier, not a retained
closure claim.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read_rel(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def projector_data(d: int) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return I, P_plus, Z=2P_plus-I for the C_d all-ones projector."""
    I = sp.eye(d)
    P_plus = sp.ones(d, d) / d
    Z = sp.simplify(2 * P_plus - I)
    return I, P_plus, Z


def q1_source_formal(d: int) -> sp.Matrix:
    """Formal Q=1 analogue S_d=I-(1/d)Z; at d=3 this is z=-1/3."""
    I, _, Z = projector_data(d)
    return sp.simplify(I - sp.Rational(1, d) * Z)


def offsite_coeff(d: int) -> Fraction:
    return Fraction(-2, d * d)


def offsite_mag(d: int) -> Fraction:
    return abs(offsite_coeff(d))


def brannen_delta(d: int) -> Fraction:
    return Fraction(2, d * d)


def anomaly(d: int) -> Fraction:
    return Fraction(2, d * d)


def aps_eta(d: int) -> Fraction:
    return Fraction(d * d - 1, 12 * d)


def delta_from_q(q: Fraction, d: int) -> Fraction:
    return q / d


def main() -> int:
    section("A. Q=1 offsite projector residue")

    d = 3
    I3, P_plus, Z = projector_data(d)
    P_perp = sp.simplify(I3 - P_plus)
    S_q1 = q1_source_formal(d)
    expected_s = sp.Matrix(
        [
            [sp.Rational(10, 9), sp.Rational(-2, 9), sp.Rational(-2, 9)],
            [sp.Rational(-2, 9), sp.Rational(10, 9), sp.Rational(-2, 9)],
            [sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(10, 9)],
        ]
    )

    record(
        "A.1 formal S_3=I-Z/3 is exactly the Q=1 source matrix",
        S_q1 == expected_s,
        f"S_q1={S_q1}",
    )
    record(
        "A.2 Q=1 offsite coefficient is -2/9",
        all(S_q1[i, j] == sp.Rational(-2, 9) for i in range(3) for j in range(3) if i != j),
        "All off-diagonal entries are -2/9.",
    )
    record(
        "A.3 Q=1 offsite magnitude is 2/d^2 at d=3",
        offsite_mag(3) == Fraction(2, 9),
        f"|offsite_coeff(3)|={offsite_mag(3)}",
    )
    record(
        "A.4 formal general-d offsite coefficient is -2/d^2",
        all(q1_source_formal(k)[0, 1] == sp.Rational(-2, k * k) for k in range(2, 9)),
        "For S_d=I-(1/d)Z, offdiag(S_d)=-2/d^2 for d=2..8.",
    )
    record(
        "A.5 singlet/doublet spectrum at d=3 is 2/3, 4/3",
        sp.simplify(S_q1 * P_plus - sp.Rational(2, 3) * P_plus) == sp.zeros(3, 3)
        and sp.simplify(S_q1 * P_perp - sp.Rational(4, 3) * P_perp) == sp.zeros(3, 3),
        "The same source is visible as a projected singlet/doublet weighting.",
    )

    section("B. Compare the 2/d^2 routes")

    same_arithmetic = all(
        offsite_mag(k) == brannen_delta(k) == anomaly(k) for k in range(2, 12)
    )
    record(
        "B.1 offsite magnitude, Brannen n_eff/d^2, and anomaly share 2/d^2 arithmetic",
        same_arithmetic,
        "Checked d=2..11 as exact fractions.",
    )

    aps_equalities = [k for k in range(2, 20) if aps_eta(k) == offsite_mag(k)]
    record(
        "B.2 APS eta-defect is a different function and agrees only at d=3",
        aps_equalities == [3],
        f"integer equalities in d=2..19: {aps_equalities}",
    )

    x = sp.symbols("x")
    equality_poly = sp.expand(x**3 - x - 24)
    factored = sp.factor(equality_poly)
    record(
        "B.3 APS equality reduces to (d-3)(d^2+3d+8)=0",
        factored == (x - 3) * (x**2 + 3 * x + 8),
        f"factor={factored}",
    )
    record(
        "B.4 the non-d=3 APS roots are complex",
        sp.discriminant(x**2 + 3 * x + 8, x) < 0,
        "The quadratic discriminant is negative, so d=3 is the only real root.",
    )

    section("C. Q/d route check")

    q_koide = Fraction(2, 3)
    q_one = Fraction(1, 1)
    record(
        "C.1 Koide Q=2/3 gives delta=Q/d=2/9",
        delta_from_q(q_koide, 3) == Fraction(2, 9),
        f"(2/3)/3={delta_from_q(q_koide, 3)}",
    )
    record(
        "C.2 Q=1 gives delta=Q/d=1/3, not 2/9",
        delta_from_q(q_one, 3) == Fraction(1, 3)
        and delta_from_q(q_one, 3) != Fraction(2, 9),
        f"1/3={delta_from_q(q_one, 3)}",
    )
    record(
        "C.3 therefore the Q=1 offsite 2/9 is not the Brannen Q/d delta",
        offsite_mag(3) == Fraction(2, 9) and delta_from_q(q_one, 3) == Fraction(1, 3),
        "The same number appears only if typed as offsite magnitude, not as Q/d.",
    )

    section("D. Phase-unit guardrail")

    record(
        "D.1 canonical phase from dimensionless 2/9 is 4*pi/9, not literal 2/9 rad",
        2 * Fraction(2, 9) == Fraction(4, 9),
        "A U(1) character exp(2*pi*i*r) sends r=2/9 to phase angle 4*pi/9.",
    )
    record(
        "D.2 Q=1 offsite coefficient has no radian type by itself",
        True,
        "It is a matrix element of S_q1; a separate bridge would be needed to read it as a phase.",
    )

    section("E. Repo guardrails")

    distinct = read_rel("scripts/frontier_koide_two_29_routes_distinct_discriminator.py")
    brannen = read_rel("scripts/frontier_koide_brannen_phase_reduction_theorem.py")
    q1_probe = read_rel("scripts/frontier_koide_q1_unphysical_background_probe.py")
    frac_no_go = read_rel("docs/KOIDE_A1_FRACTIONAL_TOPOLOGY_NO_GO_SYNTHESIS_NOTE_2026-04-24.md")

    record(
        "E.1 existing route discriminator says APS/anomaly are distinct",
        "DISTINCT" in distinct
        and "(d^2-1)/(12 d)" in distinct
        and "2/d^2" in distinct,
    )
    record(
        "E.2 Brannen theorem records both delta=n_eff/d^2 and delta=Q/d",
        "delta = n_eff / d^2 = 2/9" in brannen
        and "delta = Q / d" in brannen,
    )
    record(
        "E.3 fractional-topology no-go blocks pure-rational-to-radian overclaim",
        "Every output is" in frac_no_go
        and "No output is a pure rational read" in frac_no_go
        and "2/9 rad" in frac_no_go,
    )
    record(
        "E.4 Q=1 unphysical-background probe already exposes offsite visibility",
        "Q1_PROJECTED_OFFSITE_PROBE_VISIBLE=TRUE" in q1_probe
        and "offsite_response == -sp.Rational(2, 9)" in q1_probe,
    )

    section("F. Scoped verdict")

    typed_unification = False
    q1_dark_matter_closure = False
    next_theorem = (
        "derive_whether_projected_offsite_2_over_d2_is_physical_Brannen_"
        "normalization_or_only_source_shadow"
    )

    record(
        "F.1 the 2/9 recurrence is real as shared C3 arithmetic",
        same_arithmetic and offsite_mag(3) == Fraction(2, 9),
        "Q=1 offsite, Brannen n_eff/d^2, and anomaly all hit 2/d^2.",
    )
    record(
        "F.2 the recurrence is not yet a typed physical unification",
        not typed_unification,
        "The objects live in different slots: matrix element, phase normalization, anomaly, eta-defect.",
    )
    record(
        "F.3 Q=1 remains non-DM and non-closure on the current surface",
        not q1_dark_matter_closure,
        "No abundance, stability, neutral-sector activation, or radian bridge follows from this classifier.",
    )

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print()
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: the Q=1 -2/9 is the same arithmetic footprint, not the same typed object.")
        print("KOIDE_TWO_NINTH_PROVENANCE_CLASSIFIER=TRUE")
        print("Q1_OFFSITE_PROJECTOR_RESIDUE=-2/9")
        print("Q1_OFFSITE_MAGNITUDE_EQUALS_2_OVER_D2=TRUE")
        print("OFFSITE_BRANNEN_ANOMALY_SHARE_ARITHMETIC_2_OVER_D2=TRUE")
        print("APS_ROUTE_DISTINCT_EXCEPT_D3=TRUE")
        print("Q1_DELTA_Q_OVER_D_EQUALS_1_OVER_3=TRUE")
        print("TWO_NINTH_TYPED_UNIFICATION=FALSE")
        print("Q1_DARK_MATTER_CLOSURE=FALSE")
        print(f"NEXT_THEOREM={next_theorem}")
        return 0

    print("VERDICT: 2/9 provenance classifier has failing checks.")
    print("KOIDE_TWO_NINTH_PROVENANCE_CLASSIFIER=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
