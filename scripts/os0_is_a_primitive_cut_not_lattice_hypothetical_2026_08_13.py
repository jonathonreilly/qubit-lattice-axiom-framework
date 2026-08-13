#!/usr/bin/env python3
"""Exact checks: OS0 Euclidean isotropy is a primitive cut, not Lattice.

Q_E and the displayed Q_lopsided are a-free Euclidean quadratics.
Speed-preservation selects a^2=1 on Q_E and a^2=1/4 on Q_lopsided.
Identity gates call omega_coeff_E(a) and omega_coeff_lop(a).
OS0 is not moved into Lattice and is not dropped. a=1 is not installed.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "OS0_IS_A_PRIMITIVE_CUT_NOT_LATTICE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/OS0_IS_A_PRIMITIVE_CUT_NOT_LATTICE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

I_SQUARED = Fraction(-1)


def Q_E_coefficients() -> dict[tuple[str, str], Fraction]:
    """Euclidean OS0 quadratic: both coefficients 1/4. No Wick symbol a."""
    return {
        ("k4", "k4"): Fraction(1, 4),
        ("k", "k"): Fraction(1, 4),
    }


def Q_lopsided_coefficients() -> dict[tuple[str, str], Fraction]:
    """Displayed lopsided cut: temporal coeff 1, spatial coeff 1/4. No a."""
    return {
        ("k4", "k4"): Fraction(1),
        ("k", "k"): Fraction(1, 4),
    }


def Q_E(k4: Fraction, k: Fraction) -> Fraction:
    coeffs = Q_E_coefficients()
    return coeffs[("k4", "k4")] * k4 * k4 + coeffs[("k", "k")] * k * k


def Q_lopsided(k4: Fraction, k: Fraction) -> Fraction:
    coeffs = Q_lopsided_coefficients()
    return coeffs[("k4", "k4")] * k4 * k4 + coeffs[("k", "k")] * k * k


def polynomial_names_a(coefficients: dict[tuple[str, str], Fraction]) -> bool:
    return any(symbol == "a" for monomial in coefficients for symbol in monomial)


def q_e_names_a() -> bool:
    return polynomial_names_a(Q_E_coefficients())


def q_lopsided_names_a() -> bool:
    return polynomial_names_a(Q_lopsided_coefficients())


def wick_k4_squared(a: Fraction, omega: Fraction) -> Fraction:
    """k4 = i a ω, so k4² = i² a² ω² = −a² ω²."""
    return I_SQUARED * a * a * omega * omega


def omega_coeff_E(a: Fraction) -> Fraction:
    return (wick_k4_squared(a, Fraction(1)) + Fraction(0)) / 4


def omega_coeff_lop(a: Fraction) -> Fraction:
    return (4 * wick_k4_squared(a, Fraction(1)) + Fraction(0)) / 4


def spatial_coeff_E() -> Fraction:
    return Q_E(Fraction(0), Fraction(1))


def spatial_coeff_lop() -> Fraction:
    return Q_lopsided(Fraction(0), Fraction(1))


def speed_preserving_a_squared_E() -> Fraction:
    """|omega_coeff_E(a)| = a²/4 equals spatial 1/4 iff a² = 1."""
    return spatial_coeff_E() / Fraction(1, 4)


def speed_preserving_a_squared_lop() -> Fraction:
    """|omega_coeff_lop(a)| = a² equals spatial 1/4 iff a² = 1/4."""
    return spatial_coeff_lop()


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


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    kinetic = KINETIC_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("AUDIT_INPUT_PATHS: " + ", ".join(AUDIT_INPUT_PATHS))
    print(
        "external_scientific_inputs: current Lattice wording and the "
        "kinetic-isotropy primitive are source-bound; no observational "
        "or fitted inputs are used"
    )
    print("Q_lopsided adoption: displayed only; a=1 is not installed; OS0 is not dropped")

    a_half = Fraction(1, 2)
    a_one = Fraction(1)
    a_two = Fraction(2)

    checks.check(
        "q-e-coefficients",
        "Q_E has quadratic coefficients 1/4 and 1/4",
        Q_E_coefficients() == {("k4", "k4"): Fraction(1, 4), ("k", "k"): Fraction(1, 4)}
        and Q_E(Fraction(2), Fraction(2)) == Fraction(2),
    )
    checks.check(
        "q-lopsided-coefficients",
        "Q_lopsided has temporal coefficient 1 and spatial coefficient 1/4",
        Q_lopsided_coefficients()
        == {("k4", "k4"): Fraction(1), ("k", "k"): Fraction(1, 4)}
        and Q_lopsided(Fraction(1), Fraction(2)) == Fraction(2),
    )
    checks.check(
        "mutation-q-e-names-a",
        "predicate Q_E names a fails",
        q_e_names_a() is False and q_lopsided_names_a() is False,
    )
    checks.check(
        "identity-omega-coeff-E",
        "identity gate omega_coeff_E(a) equals -a^2/4",
        omega_coeff_E(a_half) == -a_half * a_half / 4
        and omega_coeff_E(a_one) == -a_one * a_one / 4
        and omega_coeff_E(a_two) == -a_two * a_two / 4,
    )
    checks.check(
        "identity-omega-coeff-lop",
        "identity gate omega_coeff_lop(a) equals -a^2",
        omega_coeff_lop(a_half) == -a_half * a_half
        and omega_coeff_lop(a_one) == -a_one * a_one
        and omega_coeff_lop(a_two) == -a_two * a_two,
    )
    checks.check(
        "reconstructed-omega-values",
        "omega_coeff_E(1)=-1/4, omega_coeff_E(1/2)=-1/16, omega_coeff_lop(1)=-1, omega_coeff_lop(1/2)=-1/4",
        omega_coeff_E(a_one) == Fraction(-1, 4)
        and omega_coeff_E(a_half) == Fraction(-1, 16)
        and omega_coeff_lop(a_one) == Fraction(-1)
        and omega_coeff_lop(a_half) == Fraction(-1, 4),
    )
    checks.check(
        "speed-preservation-Q-E",
        "speed-preservation on Q_E is a^2=1",
        abs(omega_coeff_E(a_one)) == spatial_coeff_E()
        and spatial_coeff_E() == Fraction(1, 4)
        and speed_preserving_a_squared_E() == Fraction(1)
        and abs(omega_coeff_E(a_half)) != spatial_coeff_E(),
    )
    checks.check(
        "speed-preservation-Q-lopsided",
        "speed-preservation on Q_lopsided is a^2=1/4, a=±1/2",
        abs(omega_coeff_lop(a_half)) == spatial_coeff_lop()
        and spatial_coeff_lop() == Fraction(1, 4)
        and speed_preserving_a_squared_lop() == Fraction(1, 4)
        and abs(omega_coeff_lop(a_one)) != spatial_coeff_lop(),
    )
    checks.check(
        "mutation-same-wick-a",
        "predicate speed-preservation selects the same a for Q_E and Q_lopsided fails (1 vs 1/2)",
        speed_preserving_a_squared_E() != speed_preserving_a_squared_lop()
        and speed_preserving_a_squared_E() == Fraction(1)
        and speed_preserving_a_squared_lop() == Fraction(1, 4),
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
        "adjacency, standard translations, and proper cubic rotations about each site."
    )
    checks.check(
        "source-lattice",
        "Lattice names Z^3, nearest-neighbor adjacency, and proper cubic rotations",
        lattice_sentence in normalized_axiom,
    )
    checks.check(
        "source-lattice-no-clock",
        "Lattice does not name a Euclidean tick, c_t, OS0, or Wick a",
        "c_t" not in axiom
        and "OS0" not in axiom
        and "Euclidean tick" not in axiom
        and "k4" not in axiom,
    )
    checks.check(
        "source-kinetic-isotropy",
        "the kinetic-isotropy primitive supplies c_t = c_s rather than deriving it",
        "c_t = c_s" in kinetic
        and "is supplied rather than derived" in kinetic
        and "It does not add or amend an axiom." in kinetic,
    )
    checks.check(
        "machine-status-contract",
        "the note carries the required C5 primitive-cut and bounded-support status lines",
        'hypothetical_axiom_status: "C5: OS0 Euclidean isotropy is a primitive cut; not moved into Lattice; not dropped"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "theorem-surface",
        "the note locates the clock wall in the primitive cut and refuses a=1, Q_lopsided, L_phys, and r=1/2",
        all(
            phrase in normalized_note
            for phrase in (
                "The clock wall therefore lives in the *primitive cut*, not in Lattice.",
                "Display `Q_lopsided`; do not adopt it.",
                "Do not drop OS0.",
                "Do not install `a=1`.",
                "does not dissolve formation occupancy `o`",
                "Newton pairing",
                "color algebra `M_3`",
                "does not force `r=1/2`",
                "does not adopt `L_phys`",
            )
        )
        and "github.com" not in note,
    )
    checks.check(
        "parents-and-paths",
        "AUDIT_INPUT_PATHS are the new note, kinetic isotropy, and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/OS0_IS_A_PRIMITIVE_CUT_NOT_LATTICE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and KINETIC_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print(
        "per_element: identity gates call omega_coeff_E(a) and omega_coeff_lop(a) "
        "at a=1/2, 1, and 2; Euclidean polynomials are reconstructed without a"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
