#!/usr/bin/env python3
"""Exact checks for linear temporal reparameterization of an isotropic form."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/LINEAR_TEMPORAL_REPARAMETERIZATION_ISOTROPIC_QUADRATIC_FORM_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PRIMITIVE_REL = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
AUDIT_INPUT_PATHS = (
    "docs/LINEAR_TEMPORAL_REPARAMETERIZATION_ISOTROPIC_QUADRATIC_FORM_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

NOTE_PATH = ROOT / NOTE_REL
PRIMITIVE_PATH = ROOT / PRIMITIVE_REL


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: none; c, a, b, and the linear substitution are declared mathematical inputs")
    print("framework_role: kinetic isotropy supplies only the Euclidean equal-coefficient context c_t=c_s")
    print("claim_scope: positive coordinate-equivalence algebra; no physical clock-selection or Record no-go")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and kinetic-isotropy primitive",
        AUDIT_INPUT_PATHS == (NOTE_REL, PRIMITIVE_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "primitive-equal-form",
        "the primitive supplies c_t = c_s and calls it kinetic-form isotropy",
        "c_t = c_s" in primitive and "kinetic normalization is space-time isotropic" in primitive,
    )
    checks.check(
        "primitive-no-dynamics",
        "the primitive expressly supplies no dynamics or Lorentz-closure theorem",
        "not a new dynamics" in primitive and "full Lorentz restoration remain separate" in primitive,
    )

    c, k4, omega = sp.symbols("c k4 omega", positive=True)
    a, b = sp.symbols("a b", positive=True)
    kx, ky, kz = sp.symbols("kx ky kz", real=True)
    k2 = kx**2 + ky**2 + kz**2
    q_e = c * (k4**2 + k2)
    q_a = sp.expand(q_e.subs(k4, sp.I * a * omega))
    q_b = sp.expand(q_e.subs(k4, sp.I * b * omega))

    checks.check(
        "continued-form",
        "Q_E(i a omega,k)=c(-a^2 omega^2+|k|^2)",
        sp.simplify(q_a - c * (-(a**2) * omega**2 + k2)) == 0,
        q_a,
    )
    temporal = -q_a.coeff(omega**2)
    spatial = q_a.coeff(kx**2)
    checks.check(
        "coefficient-ratio",
        "the temporal-to-spatial quadratic coefficient ratio is a^2 and c cancels",
        sp.simplify(temporal / spatial - a**2) == 0,
        (temporal, spatial),
    )
    checks.check(
        "pairwise-equivalence",
        "Q_b((a/b)omega,k)=Q_a(omega,k) for all positive a,b",
        sp.simplify(q_b.subs(omega, (a / b) * omega) - q_a) == 0,
    )
    checks.check(
        "inverse-map",
        "the b-to-a and a-to-b frequency rescalings are mutual inverses",
        sp.simplify((b / a) * ((a / b) * omega) - omega) == 0,
    )

    d = sp.symbols("d", positive=True)
    checks.check(
        "composition-law",
        "the a-to-b and b-to-d maps compose to the direct a-to-d map",
        sp.simplify((b / d) * ((a / b) * omega) - (a / d) * omega) == 0,
    )
    Omega = sp.symbols("Omega", real=True)
    normalized = sp.expand(q_a.subs(omega, Omega / a))
    checks.check(
        "normalized-coordinate",
        "Omega=a omega removes the coordinate parameter from the form",
        sp.simplify(normalized - c * (-Omega**2 + k2)) == 0,
        normalized,
    )

    vals = (Fraction(1, 2), Fraction(1), Fraction(2))
    raw = [Fraction(1, 4) * value * value for value in vals]
    ratios = [value * value for value in vals]
    checks.check(
        "representative-coefficients",
        "at c=1/4 the raw temporal coefficients are 1/16, 1/4, and 1",
        raw == [Fraction(1, 16), Fraction(1, 4), Fraction(1)],
        raw,
    )
    checks.check(
        "representative-ratios",
        "the temporal-to-spatial ratios are 1/4, 1, and 4",
        ratios == [Fraction(1, 4), Fraction(1), Fraction(4)],
        ratios,
    )
    pair_checks = []
    for av in vals:
        for bv in vals:
            qa = q_a.subs({a: sp.Rational(av.numerator, av.denominator), c: sp.Rational(1, 4)})
            qb = q_b.subs({b: sp.Rational(bv.numerator, bv.denominator), c: sp.Rational(1, 4)})
            mapped = qb.subs(omega, sp.Rational(av.numerator * bv.denominator, av.denominator * bv.numerator) * omega)
            pair_checks.append(sp.simplify(mapped - qa) == 0)
    checks.check(
        "finite-pair-census",
        "all nine ordered pairs in the representative set satisfy the exact equivalence",
        all(pair_checks) and len(pair_checks) == 9,
        pair_checks,
    )

    wrong_direction = sp.simplify(q_b.subs(omega, (b / a) * omega) - q_a)
    checks.check(
        "wrong-direction-mutation",
        "reversing a/b to b/a is not an identity for generic positive a,b",
        wrong_direction != 0
        and sp.simplify(wrong_direction.subs({a: 2, b: 3, c: 1, omega: 1, kx: 0, ky: 0, kz: 0})) != 0,
        wrong_direction,
    )
    singular = sp.expand(q_a.subs(a, 0))
    checks.check(
        "singular-zero-mutation",
        "a=0 removes the temporal term and has no inverse frequency map",
        singular.coeff(omega**2) == 0 and sp.simplify(singular - c * k2) == 0,
        singular,
    )
    anisotropic = sp.expand(c * (2 * k4**2 + k2))
    checks.check(
        "anisotropic-mutation",
        "unequal Euclidean coefficients are outside the represented isotropic family",
        anisotropic.coeff(k4**2) != anisotropic.coeff(kx**2),
    )

    required_note_phrases = (
        "Q_b((a/b)omega,k)=Q_a(omega,k)",
        "coordinate presentations",
        "keeps `c` symbolic",
        "uses no Record functional",
        "No negative clock-selection claim lands",
        "**Type:** bounded_theorem",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "note-contract",
        "the note states the exact equivalence and bounded non-physical scope",
        all(phrase in note for phrase in required_note_phrases),
        [phrase for phrase in required_note_phrases if phrase not in note],
    )
    checks.check(
        "note-dependency",
        "the note links only the kinetic-isotropy primitive as scientific authority",
        "[ `KINETIC" not in note
        and "(KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)" in note
        and "MINIMAL_AXIOMS_2026-06-29.md](" not in note,
    )
    checks.check(
        "retired-record-semantics-absent",
        "the note does not restore scalar Record additivity or a value at absence",
        "Record supplies content-determined additive readout" not in note
        and "Record locks content and supplies additive scalar readout" not in note
        and "I(empty)=0` are not Record" not in note,
    )
    checks.check(
        "no-physical-selector-rhetoric",
        "the theorem does not label a raw coefficient as a physical discriminator",
        "physical discriminator" in note
        and "not a primitive normalization or a physical discriminator" in note
        and "distinct physical clocks" in note,
    )
    checks.check(
        "review-record",
        "the source records why the original negative framing was removed",
        "## Review Record" in note
        and "invertible frequency-coordinate rescaling" in note
        and "owner-approved 2026-08-13 premise update" in note,
    )

    print("per_element: checked — every positive parameter pair obeys the symbolic reparameterization identity exactly")
    print("per_site: checked and not executed — the theorem is a momentum-coordinate identity with no site carrier")
    print("per_mode: checked — arbitrary symbolic frequency and spatial momentum variables are retained throughout")
    print("per_block: checked — Euclidean and continued quadratic blocks are compared coefficient by coefficient")
    print("lattice_wide: checked and not executed — no lattice dynamics, reconstruction, or physical clock is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
