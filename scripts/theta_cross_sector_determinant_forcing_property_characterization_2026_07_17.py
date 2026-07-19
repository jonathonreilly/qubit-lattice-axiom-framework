#!/usr/bin/env python3
"""Exact checks for two conditional theta phase-erasure forcing pairs."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
OBLIGATION = ROOT / "docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md"
PHASE_ERASURE_NOTE = ROOT / "docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
REGISTRABLE_NOTE = ROOT / "docs/REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"
ORBIT_BRIDGE = ROOT / "docs/KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md"


def normalized_whitespace(text):
    return " ".join(text.split())


def finite_readout(function, angles):
    return sp.simplify(sum((function(angle) for angle in angles), sp.S.Zero))


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        try:
            ok = bool(condition)
        except (TypeError, ValueError):
            ok = condition == sp.true
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def needle(self, label, path, needles):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(needles, str):
            needles = (needles,)
        self.check(
            label,
            all(normalized_whitespace(needle) in haystack for needle in needles),
        )

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def main():
    checks = CheckRunner()
    print(
        "BOUNDARY: conjugate-pair cancellation is an explicit supplied "
        "condition, not a consequence of finite Record additivity."
    )

    # Domain and common algebra.
    radius = sp.symbols("r", positive=True, real=True)
    phi = sp.symbols("phi", real=True)
    z = radius * sp.exp(sp.I * phi)
    checks.check(
        "D1 symbolic conjugation reverses the determinant phase",
        sp.simplify(sp.conjugate(z) - radius * sp.exp(-sp.I * phi)) == 0,
    )
    checks.check(
        "D2 circle witnesses are branch-independent and two-pi periodic",
        sp.simplify(sp.exp(sp.I * (phi + 2 * sp.pi)) - sp.exp(sp.I * phi)) == 0
        and sp.simplify(sp.sin(phi + 2 * sp.pi) - sp.sin(phi)) == 0
        and sp.simplify(sp.cos(phi + 2 * sp.pi) - sp.cos(phi)) == 0,
    )

    value, conjugate_value = sp.symbols("value conjugate_value")
    odd_even_solution = sp.solve(
        (
            sp.Eq(conjugate_value, -value),
            sp.Eq(conjugate_value, value),
        ),
        (value, conjugate_value),
        dict=True,
    )
    checks.check(
        "D3 odd plus even forces the real scalar phase contribution to zero",
        odd_even_solution == [{value: 0, conjugate_value: 0}],
    )

    # Conjugate-pair-cancellation route: prove the premise and its full witness.
    h_phi, h_neg_phi, h_pair, h_zero = sp.symbols(
        "h_phi h_neg_phi h_pair h_zero"
    )
    cancellation_solution = sp.solve(
        (
            sp.Eq(h_pair, h_phi + h_neg_phi),
            sp.Eq(h_pair, h_zero),
            sp.Eq(h_zero, 0),
        ),
        (h_neg_phi, h_pair, h_zero),
        dict=True,
    )
    checks.check(
        "C1 supplied conjugate-pair cancellation implies oddness",
        cancellation_solution
        == [{h_neg_phi: -h_phi, h_pair: 0, h_zero: 0}],
    )

    sine = sp.sin
    collection_a = (sp.S.Zero, sp.pi / 6, sp.pi / 2)
    collection_b = (-sp.pi / 3, sp.pi)
    checks.check(
        "C2 sine finite-record readout is additive under disjoint union",
        finite_readout(sine, collection_a + collection_b)
        == sp.simplify(
            finite_readout(sine, collection_a)
            + finite_readout(sine, collection_b)
        ),
    )
    cancellation_angles = (
        sp.S.Zero,
        sp.pi / 7,
        sp.pi / 3,
        sp.pi / 2,
        5 * sp.pi / 6,
    )
    checks.check(
        "C3 sine readout cancels every tested conjugate pair exactly",
        all(
            finite_readout(sine, (angle, -angle)) == 0
            for angle in cancellation_angles
        ),
    )
    checks.check(
        "C4 sine readout registers phase",
        finite_readout(sine, (sp.S.Zero,)) == 0
        and finite_readout(sine, (sp.pi / 2,)) == 1,
    )
    checks.check(
        "C5 sine readout is not K/CPT-orbit-constant",
        finite_readout(sine, (sp.pi / 2,))
        != finite_readout(sine, (-sp.pi / 2,)),
    )
    checks.check(
        "C6 sine witness is smooth on the phase circle",
        sp.diff(sp.sin(phi), phi) == sp.cos(phi),
    )

    # Determinant-character route.
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    b11, b12, b21, b22 = sp.symbols("b11 b12 b21 b22")
    matrix_a = sp.Matrix(((a11, a12), (a21, a22)))
    matrix_b = sp.Matrix(((b11, b12), (b21, b22)))
    checks.check(
        "H1 symbolic independent-block determinant multiplication",
        sp.expand(
            sp.diag(matrix_a, matrix_b).det()
            - matrix_a.det() * matrix_b.det()
        )
        == 0,
    )

    character_angles = (
        sp.pi / 11,
        sp.pi / 7,
        -sp.pi / 5,
        sp.pi / 3,
        sp.pi / 2,
    )
    character_product = sp.prod(sp.exp(sp.I * angle) for angle in character_angles)
    checks.check(
        "H2 k=1 character respects arbitrary finite block composition",
        sp.simplify(
            character_product - sp.exp(sp.I * sum(character_angles, sp.S.Zero))
        )
        == 0,
    )
    checks.check(
        "H3 k=1 character registers phase",
        sp.exp(sp.I * 0) == 1
        and sp.exp(sp.I * sp.pi / 2) == sp.I
        and sp.exp(sp.I * 0) != sp.exp(sp.I * sp.pi / 2),
    )
    checks.check(
        "H4 k=1 character is not K/CPT-orbit-constant",
        sp.exp(sp.I * sp.pi / 2) == sp.I
        and sp.exp(-sp.I * sp.pi / 2) == -sp.I
        and sp.exp(sp.I * sp.pi / 2) != sp.exp(-sp.I * sp.pi / 2),
    )
    checks.check(
        "H5 k=1 character is smooth and single-valued",
        sp.diff(sp.exp(sp.I * phi), phi) == sp.I * sp.exp(sp.I * phi)
        and sp.simplify(
            sp.exp(sp.I * (phi + 2 * sp.pi)) - sp.exp(sp.I * phi)
        )
        == 0,
    )

    k = sp.symbols("k", integer=True)
    character_evenness_difference = sp.exp(sp.I * k * phi) - sp.exp(
        -sp.I * k * phi
    )
    identity_coefficient = sp.diff(sp.sin(k * phi), phi).subs(phi, 0)
    checks.check(
        "H6 character orbit constancy for every phase forces k=0",
        sp.simplify(
            character_evenness_difference - 2 * sp.I * sp.sin(k * phi)
        )
        == 0
        and identity_coefficient == k
        and sp.solve(sp.Eq(identity_coefficient, 0), k) == [0],
    )

    # Orbit-constant control that lacks either route-local condition.
    cosine = sp.cos
    checks.check(
        "O1 cosine finite-record readout is additive under disjoint union",
        finite_readout(cosine, collection_a + collection_b)
        == sp.simplify(
            finite_readout(cosine, collection_a)
            + finite_readout(cosine, collection_b)
        ),
    )
    checks.check(
        "O2 cosine finite-record readout is exactly orbit-constant",
        sp.simplify(
            finite_readout(cosine, collection_a)
            - finite_readout(cosine, tuple(-angle for angle in collection_a))
        )
        == 0,
    )
    checks.check(
        "O3 cosine violates conjugate-pair cancellation",
        finite_readout(cosine, (sp.S.Zero, sp.S.Zero)) == 2,
    )
    checks.check(
        "O4 cosine violates the determinant-character product law",
        sp.cos(sp.pi) == -1
        and sp.cos(sp.pi / 2) * sp.cos(sp.pi / 2) == 0
        and sp.cos(sp.pi) != sp.cos(sp.pi / 2) * sp.cos(sp.pi / 2),
    )
    checks.check(
        "O5 cosine registers phase",
        finite_readout(cosine, (sp.S.Zero,)) == 1
        and finite_readout(cosine, (sp.pi,)) == -1,
    )
    checks.check(
        "O6 cosine witness is real, smooth, and circle-periodic",
        sp.diff(sp.cos(phi), phi) == -sp.sin(phi)
        and sp.simplify(sp.cos(phi + 2 * sp.pi) - sp.cos(phi)) == 0,
    )

    checks.check(
        "T1 route-relative minimality uses full predicates, not parity labels",
        finite_readout(sine, collection_a + collection_b)
        == finite_readout(sine, collection_a) + finite_readout(sine, collection_b)
        and all(
            finite_readout(sine, (angle, -angle)) == 0
            for angle in cancellation_angles
        )
        and finite_readout(sine, (sp.pi / 2,))
        != finite_readout(sine, (-sp.pi / 2,))
        and sp.simplify(
            character_product - sp.exp(sp.I * sum(character_angles, sp.S.Zero))
        )
        == 0
        and sp.exp(sp.I * sp.pi / 2) != sp.exp(-sp.I * sp.pi / 2)
        and finite_readout(cosine, collection_a)
        == finite_readout(cosine, tuple(-angle for angle in collection_a))
        and finite_readout(cosine, (sp.S.Zero, sp.S.Zero)) != 0,
    )

    # Source-boundary needles.
    checks.needle(
        "N1 obligation physical closure criterion",
        OBLIGATION,
        (
            "construct the quark mass/determinant carrier",
            "identify the physical readout map",
            "prove the cross-sector correspondence",
        ),
    )
    checks.needle(
        "N2 phase-erasure hostile guard",
        PHASE_ERASURE_NOTE,
        "K/CPT orbit invariance alone gives evenness, not phase erasure",
    )
    checks.needle(
        "N3 Record-additivity non-supply boundary",
        REGISTRABLE_NOTE,
        (
            "phase-group additivity from Record finite additivity",
            "Record finite additivity alone still admits K-even phase-dependent functions",
        ),
    )
    checks.needle(
        "N4 orbit bridge assigns work to the homomorphism boundary, not Record",
        ORBIT_BRIDGE,
        "The determinant-character/log-character boundary does that work, not Record",
    )
    checks.needle(
        "N5 target note carries the narrowed theorem and discipline result",
        TARGET_NOTE,
        (
            "Conjugate-pair cancellation",
            "Independent-block character law",
            "no combined-property or global exhaustion claim remains",
            "No-Go Discipline status: PASS",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
