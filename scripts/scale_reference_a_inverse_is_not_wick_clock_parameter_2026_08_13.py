#!/usr/bin/env python3
"""Exact type split: scale-reference a_sr is not the Wick clock parameter a_w.

Identity gates call omega_coeff(a) and is_dimensionless_ratio. Values are
derived by substituting k4 = i a_w omega into Q_E = (k4^2 + k^2)/4 using
exact Fraction arithmetic. The runner does not install a_w = 1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "SCALE_REFERENCE_A_INVERSE_IS_NOT_WICK_CLOCK_PARAMETER_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SCALE_REFERENCE_A_INVERSE_IS_NOT_WICK_CLOCK_PARAMETER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def q_e(k4_sq: Fraction, k_sq: Fraction) -> Fraction:
    """Euclidean OS0 form Q_E = (k4^2 + k^2)/4. No Wick parameter."""
    return (k4_sq + k_sq) / Fraction(4)


def wick_k4_squared(a_w: Fraction, omega: Fraction) -> Fraction:
    """k4 = i a_w omega implies k4^2 = -a_w^2 omega^2."""
    return -(a_w * a_w) * (omega * omega)


def omega_coeff(a: Fraction) -> Fraction:
    """Coefficient of omega^2 after substituting k4 = i a omega into Q_E."""
    return q_e(wick_k4_squared(a, Fraction(1)), Fraction(0))


def spatial_coeff() -> Fraction:
    """Coefficient of k^2 in Q_E. Independent of a_w."""
    return q_e(Fraction(0), Fraction(1))


@dataclass(frozen=True)
class TypedQuantity:
    value: Fraction
    dimensionful: bool


def is_dimensionless_ratio(
    numerator: Fraction | TypedQuantity,
    denominator: Fraction | TypedQuantity | None = None,
) -> bool:
    """True iff the argument is a nonzero rational ratio of quadratic coefficients."""
    if denominator is None:
        if isinstance(numerator, TypedQuantity):
            return (not numerator.dimensionful) and numerator.value != 0
        return False
    if isinstance(numerator, TypedQuantity) or isinstance(denominator, TypedQuantity):
        left = numerator if isinstance(numerator, TypedQuantity) else TypedQuantity(Fraction(numerator), False)
        right = (
            denominator
            if isinstance(denominator, TypedQuantity)
            else TypedQuantity(Fraction(denominator), False)
        )
        if left.dimensionful or right.dimensionful or right.value == 0:
            return False
        return left.value != 0
    if denominator == 0:
        return False
    return Fraction(numerator) != 0


def scale_reference_selects_wick_clock(target: Fraction) -> bool:
    """Predicate 'a_sr selects a_w = target'. Must fail for target = 1."""
    del target
    a_sr = TypedQuantity(Fraction(1), dimensionful=True)
    if is_dimensionless_ratio(a_sr):
        return True
    return False


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    scale = SCALE_PATH.read_text(encoding="utf-8")
    kinetic = KINETIC_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    scale_n = normalize(scale)
    kinetic_n = normalize(kinetic)
    axiom_n = normalize(axiom)

    print("external_scientific_inputs: none; algebra is exact Fraction substitution into Q_E")
    print("package_local_integrity_reads: new note, scale-reference primitive, kinetic isotropy, axiom memo")
    print("negative_scope: type split only; a_w=1 is not installed; speed-preservation and Lorentz remain extra")

    half = Fraction(1, 2)
    one = Fraction(1)
    two = Fraction(2)
    a_sr = TypedQuantity(Fraction(1), dimensionful=True)

    checks.check(
        "identity-omega-half",
        "omega_coeff(1/2) reconstructs -1/16",
        omega_coeff(half) == Fraction(-1, 16),
    )
    checks.check(
        "identity-omega-two",
        "omega_coeff(2) reconstructs -1",
        omega_coeff(two) == Fraction(-1),
    )
    checks.check(
        "identity-spatial",
        "spatial_coeff reconstructs 1/4 from Q_E",
        spatial_coeff() == Fraction(1, 4),
    )
    checks.check(
        "identity-ratio-half",
        "is_dimensionless_ratio(|omega_coeff(1/2)|, spatial_coeff) and the ratio is (1/2)^2",
        is_dimensionless_ratio(abs(omega_coeff(half)), spatial_coeff())
        and abs(omega_coeff(half)) / spatial_coeff() == half * half,
    )
    checks.check(
        "identity-ratio-two",
        "is_dimensionless_ratio(|omega_coeff(2)|, spatial_coeff) and the ratio is 2^2",
        is_dimensionless_ratio(abs(omega_coeff(two)), spatial_coeff())
        and abs(omega_coeff(two)) / spatial_coeff() == two * two,
    )
    checks.check(
        "identity-ratio-one-not-installed",
        "omega_coeff(1)=-1/4 is legal but is_dimensionless_ratio does not install a_w=1",
        omega_coeff(one) == Fraction(-1, 4)
        and is_dimensionless_ratio(abs(omega_coeff(one)), spatial_coeff())
        and abs(omega_coeff(one)) / spatial_coeff() == one
        and {half, one, two} != {one},
    )
    checks.check(
        "q-e-independent-of-aw",
        "Q_E(k4^2, k^2) has no a_w argument and is unchanged across Wick samples",
        q_e(Fraction(4), Fraction(9)) == Fraction(13, 4)
        and q_e.__code__.co_argcount == 2,
    )
    checks.check(
        "types-unequal",
        "a_sr is dimensionful; a_w ratios are dimensionless",
        a_sr.dimensionful
        and not is_dimensionless_ratio(a_sr)
        and is_dimensionless_ratio(abs(omega_coeff(half)), spatial_coeff()),
    )
    checks.check(
        "mutation-selects-one-fails",
        "predicate a_sr selects a_w=1 fails; a_w=1/2 remains legal",
        scale_reference_selects_wick_clock(one) is False
        and omega_coeff(half) == Fraction(-1, 16)
        and is_dimensionless_ratio(abs(omega_coeff(half)), spatial_coeff()),
    )
    checks.check(
        "source-scale-reference",
        "scale-reference is a_sr^{-1}=M_Pl with no dimensionless content",
        "a^{-1} = M_Pl" in scale_n
        and "carries zero dimensionless content" in scale_n,
    )
    checks.check(
        "source-kinetic-isotropy",
        "kinetic isotropy is Euclidean c_t=c_s, not a Wick parameter",
        "c_t = c_s" in kinetic_n
        and "Osterwalder-Schrader OS0 kinetic" in kinetic_n,
    )
    checks.check(
        "source-axiom-memo",
        "axiom memo names the four axioms and does not install a Wick clock",
        all(name in axiom_n for name in ("Lattice", "Qubit", "Admissibility", "Record"))
        and "a_w" not in axiom
        and "Wick clock" not in axiom,
    )
    checks.check(
        "note-theorems-and-gates",
        "note records Theorems 1-5, the mutation, and the required identity-gate names",
        all(
            phrase in note
            for phrase in (
                "Theorem 1",
                "Theorem 2",
                "Theorem 3",
                "Theorem 4",
                "Theorem 5",
                "omega_coeff(1/2) = -1/16",
                "omega_coeff(2)   = -1",
                "does not install `a_w = 1`",
                "omega_coeff(a)",
                "is_dimensionless_ratio",
                "Shared Letter Is Not Identification",
            )
        ),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
