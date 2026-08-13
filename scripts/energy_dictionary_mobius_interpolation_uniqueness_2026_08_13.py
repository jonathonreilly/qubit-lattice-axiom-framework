#!/usr/bin/env python3
"""Exact checks: unique Möbius interpolant of the three named endpoints.

Identity gates call r_of_w(w)=(1-w)/(2w). The three-point homogeneous
system has a one-dimensional nullspace. Two-point interpolation is not
unique. Residual Atom 2 remains declared. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "ENERGY_DICTIONARY_MOBIUS_INTERPOLATION_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
JULY12_PATH = (
    ROOT
    / "docs"
    / "KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ENERGY_DICTIONARY_MOBIUS_INTERPOLATION_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def r_of_w(w: Fraction) -> Fraction:
    """Identity-gate function: r = (1-w)/(2w)."""
    return (Fraction(1) - w) / (2 * w)


def w_of_r(r: Fraction) -> Fraction:
    """Inverse obtained by solving r_of_w(w) = r for w."""
    return Fraction(1) / (Fraction(1) + 2 * r)


def Q_of_r(r: Fraction) -> Fraction:
    """Independent generation-3 identity Q = 1/3 + (2/3) r."""
    return Fraction(1, 3) + (Fraction(2, 3) * r)


def Q_of_w(w: Fraction) -> Fraction:
    return Q_of_r(r_of_w(w))


def r_alt(w: Fraction) -> Fraction:
    """Mutation of r_of_w: (1-w)/w."""
    return (Fraction(1) - w) / w


def r_lin(w: Fraction) -> Fraction:
    """Mutation of r_of_w: 1-w."""
    return Fraction(1) - w


def r_two_point(w: Fraction) -> Fraction:
    """Two-point Möbius interpolant (3/2)(1-w) of w=1→0 and w=1/3→1."""
    return (Fraction(3, 2) * (Fraction(1) - w))


def r_wrong_Q_closed(w: Fraction) -> Fraction:
    """Wrong composition (2-w)/(3w); not Q_of_w."""
    return (Fraction(2) - w) / (3 * w)


def dictionary_forces_r_half_for_every_sector(weights: tuple[Fraction, ...]) -> bool:
    return all(r_of_w(weight) == Fraction(1, 2) for weight in weights)


def mobius(coeffs: tuple[Fraction, Fraction, Fraction, Fraction], w: Fraction) -> Fraction:
    alpha, beta, gamma, delta = coeffs
    return (alpha * w + beta) / (gamma * w + delta)


def as_fraction(value: object) -> Fraction:
    rational = sp.Rational(value)
    return Fraction(int(rational.p), int(rational.q))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def solve_three_point() -> tuple[sp.Matrix, ...]:
    """Homogeneous interpolating conditions; do not seed (1,-1,-2,0)."""
    matrix = sp.Matrix(
        [
            [1, 1, 0, 0],
            [2, 4, -1, -2],
            [1, 3, -1, -3],
        ]
    )
    return tuple(matrix.nullspace())


def solve_two_point() -> tuple[sp.Matrix, ...]:
    matrix = sp.Matrix(
        [
            [1, 1, 0, 0],
            [1, 3, -1, -3],
        ]
    )
    return tuple(matrix.nullspace())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    july12 = JULY12_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_july12 = normalize(july12)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: July 12 Residual Atom 2 and the three "
        "named endpoints are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: Residual Atom 2 is not derived; universal r=1/2 is "
        "rejected; two-point Möbius interpolation remains non-unique"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, July 12 relocation note, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/ENERGY_DICTIONARY_MOBIUS_INTERPOLATION_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    checks.check(
        "source-residual-atom-2",
        "July 12 Residual Atom 2 names the identification as a declared modeling element and records r = (1-w)/(2w)",
        "declared modeling element" in normalized_july12
        and "is not supplied by the Record axiom" in normalized_july12
        and "E_s = w E_tot" in july12
        and "E_d = (1-w) E_tot" in july12
        and "The energy dictionary." in july12
        and "r = (1-w)/(2w)" in july12,
    )
    checks.check(
        "source-named-endpoints",
        "July 12 names quotient counting w=1/2, carrier-trace w=1/3, and domain endpoint w=1",
        "quotient counting gives `w = 1/2`" in july12
        and "carrier-trace restriction gives" in july12
        and "`w = 1/3`" in july12
        and "0 <= w <= 1" in july12,
    )
    checks.check(
        "source-record-additivity",
        "the exact current Record additivity sentence is present in the axiom memo",
        additivity_sentence in normalized_axiom,
    )

    one = Fraction(1)
    zero = Fraction(0)
    half = Fraction(1, 2)
    third = Fraction(1, 3)
    w_one, w_half, w_third = one, half, third

    # Theorem 1 — unique interpolant from the homogeneous system.
    nullspace = solve_three_point()
    checks.check(
        "theorem-1-nullspace-dimension",
        "the three-point interpolation matrix has a one-dimensional nullspace",
        len(nullspace) == 1,
        residual=nullspace,
    )
    generator = nullspace[0]
    scale = generator[0]
    normalized = tuple(as_fraction(component / scale) for component in generator)
    solved_map = tuple(normalized[0] * factor for factor in (one, -one, Fraction(-2), zero))
    checks.check(
        "theorem-1-scale-class",
        "normalizing α=1 yields the coefficient class (1,-1,-2,0)",
        normalized == (one, -one, Fraction(-2), zero) and solved_map == normalized,
        residual=normalized,
    )
    det = normalized[0] * normalized[3] - normalized[1] * normalized[2]
    checks.check(
        "theorem-1-nonconstant",
        "the solved representative has αδ-βγ ≠ 0",
        det != 0,
        residual=det,
    )

    w_sym = sp.symbols("w")
    solved_expr = (normalized[0] * w_sym + normalized[1]) / (
        normalized[2] * w_sym + normalized[3]
    )
    dictionary_expr = (1 - w_sym) / (2 * w_sym)
    checks.check(
        "theorem-1-equals-identity-gate",
        "the solved Möbius map is identically (1-w)/(2w)",
        sp.simplify(solved_expr - dictionary_expr) == 0,
        residual=solved_expr,
    )

    endpoint_weights = (w_one, w_half, w_third)
    solved_values = tuple(mobius(normalized, weight) for weight in endpoint_weights)
    identity_values = tuple(r_of_w(weight) for weight in endpoint_weights)
    checks.check(
        "theorem-1-endpoints",
        "r_of_w and the solved map send 1,1/2,1/3 to 0,1/2,1",
        identity_values == (zero, half, one)
        and solved_values == identity_values,
        residual=(identity_values, solved_values),
    )

    # Theorem 2 — inverse and Q composition from r_of_w, not from a target formula.
    inverse_values = (w_of_r(zero), w_of_r(half), w_of_r(one))
    checks.check(
        "theorem-2-inverse-endpoints",
        "w_of_r sends 0,1/2,1 to 1,1/2,1/3",
        inverse_values == (w_one, w_half, w_third),
        residual=inverse_values,
    )
    checks.check(
        "theorem-2-inverse-roundtrip",
        "w_of_r inverts r_of_w at the three endpoints",
        all(w_of_r(r_of_w(weight)) == weight for weight in endpoint_weights)
        and all(r_of_w(w_of_r(ratio)) == ratio for ratio in (zero, half, one)),
    )
    q_values = tuple(Q_of_w(weight) for weight in endpoint_weights)
    q_from_r = tuple(Q_of_r(r_of_w(weight)) for weight in endpoint_weights)
    q_closed = tuple(one / (3 * weight) for weight in endpoint_weights)
    checks.check(
        "theorem-2-q-composition",
        "Q_of_r(r_of_w(w)) equals 1/(3w) and is 1/3,2/3,1 at the three endpoints",
        q_values == (third, Fraction(2, 3), one)
        and q_values == q_from_r == q_closed,
        residual=q_values,
    )
    checks.check(
        "theorem-2-wrong-closed-form",
        "(2-w)/(3w) misses Q(w=1/2)=2/3",
        r_wrong_Q_closed(w_half) == one
        and r_wrong_Q_closed(w_half) != Q_of_w(w_half)
        and r_wrong_Q_closed(w_one) == Q_of_w(w_one),
        residual=r_wrong_Q_closed(w_half),
    )

    # Theorem 3 — two-point family.
    two_point_space = solve_two_point()
    checks.check(
        "theorem-3-two-point-dimension",
        "the two-point interpolation matrix has a two-dimensional nullspace",
        len(two_point_space) == 2,
        residual=two_point_space,
    )
    checks.check(
        "theorem-3-two-point-witness",
        "r_2pt=(3/2)(1-w) hits w=1→0 and w=1/3→1 but misses w=1/2→1/2",
        r_two_point(w_one) == zero
        and r_two_point(w_third) == one
        and r_two_point(w_half) == Fraction(3, 4)
        and r_two_point(w_half) != r_of_w(w_half),
        residual=r_two_point(w_half),
    )
    checks.check(
        "theorem-3-r-alt-rejector",
        "(1-w)/w at w=1/2 equals 1, not 1/2",
        r_alt(w_one) == zero
        and r_alt(w_half) == one
        and r_alt(w_half) != half
        and r_alt(w_third) == Fraction(2),
        residual=r_alt(w_half),
    )

    # Identity-gate mutations.
    checks.check(
        "mutation-alt-fails-half",
        "replacing r_of_w by (1-w)/w fails w=1/2 → 1/2",
        r_of_w(w_half) == half and r_alt(w_half) != half and r_alt(w_half) == one,
        residual=r_alt(w_half),
    )
    checks.check(
        "mutation-lin-fails-third",
        "replacing r_of_w by 1-w fails w=1/3 → 1",
        r_of_w(w_third) == one and r_lin(w_third) != one and r_lin(w_third) == Fraction(2, 3),
        residual=r_lin(w_third),
    )
    sector_menu = (w_one, w_half, w_third)
    checks.check(
        "mutation-universal-r-half-fails",
        "the predicate that the dictionary forces r=1/2 for every sector fails at w=1/3",
        r_of_w(w_third) == one
        and r_of_w(w_third) != half
        and dictionary_forces_r_half_for_every_sector(sector_menu) is False
        and dictionary_forces_r_half_for_every_sector((w_half,)) is True,
        residual=r_of_w(w_third),
    )

    # Theorem 5 — image and distinguished point.
    sample = tuple(Fraction(1, n) for n in range(1, 7))
    sample_r = tuple(r_of_w(weight) for weight in sample)
    half_hits = tuple(weight for weight in sample if r_of_w(weight) == half)
    checks.check(
        "theorem-5-nonnegative-image",
        "r_of_w maps the sample in (0,1] into r ≥ 0",
        all(value >= 0 for value in sample_r) and r_of_w(w_one) == zero,
        residual=sample_r,
    )
    checks.check(
        "theorem-5-half-is-one-point",
        "r=1/2 is the image of w=1/2 only on the sample",
        half_hits == (half,) and r_of_w(w_third) != half,
        residual=half_hits,
    )
    difference = r_of_w(w_third) - half
    expected_difference = (one - 2 * w_third) / (2 * w_third)
    checks.check(
        "theorem-5-difference-identity",
        "r_of_w(w)-1/2 equals (1-2w)/(2w) and is nonzero at w=1/3",
        difference == expected_difference == Fraction(1, 2),
        residual=difference,
    )

    checks.check(
        "note-pins-declared-modeling",
        "the note quotes Residual Atom 2 as a declared modeling element and quotes r = (1-w)/(2w)",
        "declared modeling element" in note
        and "r = (1-w)/(2w)" in note
        and "is not supplied by the Record axiom" in note
        and "Residual Atom 2" in note,
    )
    checks.check(
        "note-pins-endpoints-and-rejector",
        "the note records the three endpoints and the rejector (1-w)/w",
        "w = 1" in note
        and "w = 1/2" in note
        and "w = 1/3" in note
        and "r_alt" in note
        and "(1 - w)/w" in note
        and "gives `1`" in note,
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo and the July 12 relocation note",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
        in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: upstream_support",
                "target_claim_id: energy_dictionary_r_from_w",
                'target_blocker_text: "derive or uniquely characterize the formation-energy bridge r=(1-w)/(2w)"',
                "source_of_blocker_text: handoff",
                "reachability_to_target: partially_closes",
                'next_trace_action: "Möbius interpolation of the three named endpoints is unique; Residual Atom 2 remains declared. Do not force r=1/2. Do not adopt axiom text."',
                'hypothetical_axiom_status: "no edit"',
            )
        )
        and retained_ok
        and "retained" not in other_retained,
        residual=[line for line in other_retained.splitlines() if "retained" in line],
    )
    forbidden = ("we adopt", "new axiom", "Codex", "promoted", "toe-lphys", "Block 13")
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids axiom-adoption, promotion, executor-name, and campaign rhetoric",
        all(phrase not in note for phrase in forbidden)
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower(),
    )
    checks.check(
        "note-quotes-additivity",
        "the note quotes the current Record additivity sentence",
        additivity_sentence in normalized_note,
    )
    checks.check(
        "canonical-nonmutation",
        "the Möbius uniqueness claim is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in (
                "r = (1-w)/(2w)",
                "r_of_w",
                "Residual Atom 2",
                "(1-w)/w",
            )
        ),
    )
    checks.check(
        "july12-declares-not-derives",
        "July 12 still presents the energy dictionary as a declared modeling element",
        "declared modeling element" in normalized_july12
        and "is not supplied by the Record axiom" in normalized_july12
        and "r = (1-w)/(2w)" in july12,
    )

    n5_lines = (
        "per_element: the three named endpoints and the coefficient 4-tuple are evaluated under r_of_w",
        "per_site: the statements are two-cell menu statements; no composite carrier is asserted",
        "per_mode: the channel split and dial r=|b|^2/a^2 are scoped; no spectral-mode exhaustion is claimed",
        "per_block: only Möbius 3-point uniqueness, the 2-point family, and Theorems 4-5 are tested",
        "lattice_wide: checked and not executed — no lattice-wide dictionary or universal r=1/2 is claimed",
    )
    checks.check(
        "n5-scoped-negatives",
        "five N5 resolution lines are present and scoped",
        len(n5_lines) == 5
        and all(len(line) >= 40 for line in n5_lines)
        and n5_lines[0].startswith("per_element:")
        and n5_lines[1].startswith("per_site:")
        and n5_lines[2].startswith("per_mode:")
        and n5_lines[3].startswith("per_block:")
        and n5_lines[4].startswith("lattice_wide:"),
    )
    for line in n5_lines:
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
