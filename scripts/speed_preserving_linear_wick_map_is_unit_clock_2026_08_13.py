#!/usr/bin/env python3
"""Exact checks: speed-preserving linear Wick map is the unit clock.

Q_E = (k4^2 + k^2)/4 is independent of a. Continuation k4 = i a ω
produces Q_a = (-a^2 ω^2 + k^2)/4. Identity gates are
omega_coeff(a) = -a^2/4 and speed_preserved(a) := (a*a==1).
Speed-preservation holds iff a ∈ {+1, −1}. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SPEED_PRESERVING_LINEAR_WICK_MAP_IS_UNIT_CLOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVE_REL = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

AUDIT_INPUT_PATHS = (
    "docs/SPEED_PRESERVING_LINEAR_WICK_MAP_IS_UNIT_CLOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PRIMITIVE_PATH = ROOT / PRIMITIVE_REL

A_SAMPLES = (
    Fraction(1),
    Fraction(-1),
    Fraction(1, 2),
    Fraction(2),
    Fraction(-1, 2),
    Fraction(-2),
    Fraction(3),
    Fraction(1, 3),
    Fraction(3, 2),
)
UNIT_CLOCK = (Fraction(1), Fraction(-1))
REJECTORS = (Fraction(1, 2), Fraction(2))
SPEED_PHRASES = (
    "speed_preserved",
    "speed-preservation",
    "k4 = i a ω",
    "k4 = i a",
    "i a ω",
    "omega_coeff",
    "Q_a",
)


def omega_coeff(a: Fraction) -> Fraction:
    """Lorentzian ω^2 coefficient of Q_a: -a^2/4."""
    return -(a * a) / Fraction(4)


def speed_preserved(a: Fraction) -> bool:
    """Declared extra matching: Lorentzian null coincides with ω^2 = k^2."""
    return a * a == 1


def speed_preserved_true_for_all(_a: Fraction) -> bool:
    """Hostile mutation: replace speed_preserved by True for every a."""
    return True


def algebraic_unit_clock(a: Fraction) -> bool:
    """a = p/q lowest terms, a^2 = 1 iff |p| = q, iff a ∈ {+1, −1}."""
    return abs(a.numerator) == a.denominator


def normalize(text: str) -> str:
    return " ".join(text.split())


def as_fraction(expr: sp.Expr) -> Fraction:
    rat = sp.Rational(sp.simplify(expr))
    return Fraction(int(rat.p), int(rat.q))


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


def build_family() -> dict[str, object]:
    """Derive Q_E and Q_a by substitution. Coefficients are not preset."""
    k4, omega, kx, ky, kz = sp.symbols("k4 omega kx ky kz")
    a = sp.symbols("a", nonzero=True)
    k2 = kx**2 + ky**2 + kz**2
    q_e = (k4**2 + k2) / 4
    q_a = sp.expand(q_e.subs(k4, sp.I * a * omega))
    coeff = sp.expand(q_a).coeff(omega**2)
    spatial = sp.expand(q_a).coeff(kx**2)
    return {
        "k4": k4,
        "omega": omega,
        "kx": kx,
        "ky": ky,
        "kz": kz,
        "a": a,
        "k2": k2,
        "q_e": q_e,
        "q_a": q_a,
        "omega_coeff": coeff,
        "spatial": spatial,
    }


def derived_omega_coeff(family: dict[str, object], a_val: Fraction) -> Fraction:
    expr = family["omega_coeff"].subs(
        family["a"], sp.Rational(a_val.numerator, a_val.denominator)
    )
    return as_fraction(expr)


def inspect_identity_source() -> bool:
    text = Path(__file__).read_text(encoding="utf-8")
    return (
        "def omega_coeff(" in text
        and "def speed_preserved(" in text
        and "-a^2/4" in text
        and "a * a == 1" in text
        and "omega_coeff(" in text
        and "speed_preserved(" in text
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")
    norm_axiom = normalize(axiom)
    family = build_family()

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: axiom memo and kinetic-isotropy primitive; no observational or fitted inputs")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; no runner cache is written")
    print("negative_scope: axioms and c_t = c_s as namers of speed-preservation are rejected; a declared matching remains a live formal escape")

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and primitive",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, PRIMITIVE_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    checks.check(
        "source-primitive-ct-cs",
        "the primitive supplies the Euclidean equality c_t = c_s",
        "c_t = c_s" in primitive,
    )
    checks.check(
        "source-primitive-os0",
        "the primitive identifies that equality with OS0 kinetic normalization",
        "Osterwalder-Schrader OS0 kinetic normalization" in normalize(primitive.replace("`", "")),
    )
    checks.check(
        "source-primitive-no-axiom-amend",
        "the primitive states that it does not add or amend an axiom",
        "It does not add or amend an axiom." in primitive,
    )
    checks.check(
        "source-axiom-lattice-z3",
        "the axiom memo states that physical sites are the cubic lattice Z^3",
        "Physical sites are the points of the cubic lattice `Z^3`" in axiom,
    )
    time_metric_clause = (
        "It does not choose a Hamiltonian or transfer operator, supply "
        "transition-probability or weight values, select a scalar or nonzero "
        "kinetic branch, assert a Dirac-square carrier, define a time metric"
    )
    checks.check(
        "source-axiom-no-time-metric",
        "Admissibility is recorded as not defining a time metric",
        time_metric_clause in norm_axiom,
    )

    q_e = family["q_e"]
    k4 = family["k4"]
    a_sym = family["a"]
    checks.check(
        "theorem-1-euclidean-independent-of-a",
        "Q_E = (k4^2+k^2)/4 contains no continuation parameter a",
        a_sym not in q_e.free_symbols
        and sp.simplify(q_e - (k4**2 + family["k2"]) / 4) == 0,
        residual=q_e,
    )
    c_t = q_e.coeff(k4**2)
    c_s = q_e.coeff(family["kx"] ** 2)
    checks.check(
        "theorem-1-os0-equal-coefficients",
        "Euclidean coefficients of k4^2 and kx^2 are both 1/4, so c_t = c_s",
        as_fraction(c_t) == Fraction(1, 4)
        and as_fraction(c_s) == Fraction(1, 4)
        and sp.simplify(c_t - c_s) == 0,
        residual=(c_t, c_s),
    )

    recovered = []
    for a_val in UNIT_CLOCK + REJECTORS:
        q_cont = sp.expand(
            family["q_a"].subs(a_sym, sp.Rational(a_val.numerator, a_val.denominator))
        )
        back = sp.expand(
            q_cont.subs(
                family["omega"],
                -sp.I * k4 / sp.Rational(a_val.numerator, a_val.denominator),
            )
        )
        recovered.append(sp.simplify(back - q_e) == 0)
    sample = q_e.subs({k4: 2, family["kx"]: 3, family["ky"]: 0, family["kz"]: 0})
    checks.check(
        "theorem-1-shared-euclidean",
        "displayed continuations recover the same Q_E; sample (k4,kx)=(2,3) is 13/4",
        all(recovered) and as_fraction(sample) == Fraction(13, 4),
        residual=(recovered, sample),
    )

    expanded = sp.expand(family["q_a"])
    checks.check(
        "theorem-2-continuation",
        "substituting k4 = i a ω into Q_E yields (-a^2 ω^2 + k^2)/4",
        sp.simplify(
            expanded - ((-(a_sym**2) * family["omega"] ** 2 + family["k2"]) / 4)
        )
        == 0,
        residual=expanded,
    )

    derived = [derived_omega_coeff(family, a_val) for a_val in A_SAMPLES]
    identity = [omega_coeff(a_val) for a_val in A_SAMPLES]
    checks.check(
        "identity-omega-coeff",
        "omega_coeff(a)=-a^2/4 equals the derived [ω^2] Q_a on every sample",
        identity == derived
        and omega_coeff(Fraction(1, 2)) == Fraction(-1, 16)
        and omega_coeff(Fraction(1)) == Fraction(-1, 4)
        and omega_coeff(Fraction(-1)) == Fraction(-1, 4)
        and omega_coeff(Fraction(2)) == Fraction(-1),
        residual=(identity, derived),
    )

    spatial_vals = [
        as_fraction(
            family["spatial"].subs(
                a_sym, sp.Rational(a_val.numerator, a_val.denominator)
            )
        )
        for a_val in UNIT_CLOCK + REJECTORS
    ]
    checks.check(
        "theorem-2-spatial-unchanged",
        "the spatial coefficient remains 1/4 for every displayed a",
        spatial_vals == [Fraction(1, 4)] * 4,
        residual=spatial_vals,
    )

    preserved = {a: speed_preserved(a) for a in A_SAMPLES}
    checks.check(
        "theorem-2-speed-preservation-iff-square-one",
        "speed_preserved(a) iff a*a==1 on the rational sample",
        all(speed_preserved(a) == (a * a == 1) for a in A_SAMPLES)
        and preserved[Fraction(1)]
        and preserved[Fraction(-1)]
        and not preserved[Fraction(1, 2)]
        and not preserved[Fraction(2)],
        residual=preserved,
    )
    checks.check(
        "theorem-2-unique-up-to-orientation",
        "among the samples only a=+1 and a=-1 preserve speed, unique up to time-orientation",
        tuple(a for a in A_SAMPLES if speed_preserved(a)) == UNIT_CLOCK
        and all(algebraic_unit_clock(a) == speed_preserved(a) for a in A_SAMPLES)
        and omega_coeff(Fraction(1)) == omega_coeff(Fraction(-1)),
        residual=tuple(a for a in A_SAMPLES if speed_preserved(a)),
    )

    checks.check(
        "theorem-3-half",
        "a=1/2 gives a^2=1/4 ≠ 1 and omega_coeff=-1/16 versus spatial 1/4",
        (Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4))
        and omega_coeff(Fraction(1, 2)) == Fraction(-1, 16)
        and abs(omega_coeff(Fraction(1, 2))) != Fraction(1, 4)
        and not speed_preserved(Fraction(1, 2)),
        residual=omega_coeff(Fraction(1, 2)),
    )
    checks.check(
        "theorem-3-double",
        "a=2 gives a^2=4 ≠ 1 and omega_coeff=-1 versus spatial 1/4",
        (Fraction(2) * Fraction(2) == Fraction(4))
        and omega_coeff(Fraction(2)) == Fraction(-1)
        and abs(omega_coeff(Fraction(2))) != Fraction(1, 4)
        and not speed_preserved(Fraction(2)),
        residual=omega_coeff(Fraction(2)),
    )

    checks.check(
        "mutation-true-for-all-fails-at-half",
        "replacing speed_preserved by True-for-all-a wrongly accepts a=1/2",
        speed_preserved_true_for_all(Fraction(1, 2)) is True
        and speed_preserved(Fraction(1, 2)) is False
        and Fraction(1, 2) * Fraction(1, 2) != 1,
    )
    checks.check(
        "identity-gates-present",
        "identity gates call omega_coeff(a)=-a^2/4 and speed_preserved(a):=(a*a==1)",
        inspect_identity_source()
        and omega_coeff(Fraction(2)) == Fraction(-1)
        and speed_preserved(Fraction(1))
        and not speed_preserved(Fraction(1, 2)),
    )

    primitive_speed = [phrase for phrase in SPEED_PHRASES if phrase in primitive]
    axiom_speed = [phrase for phrase in SPEED_PHRASES if phrase in axiom]
    checks.check(
        "theorem-4-sources-do-not-name-matching",
        "neither source writes the continuation, omega_coeff, or speed_preserved",
        primitive_speed == [] and axiom_speed == [],
        residual=(primitive_speed, axiom_speed),
    )
    primitive_forces_a_1 = (
        "k4 = i" in primitive
        or "k_4 = i" in primitive
        or "forces a=1" in primitive
        or "a = 1" in primitive
    )
    checks.check(
        "theorem-4-primitive-does-not-force-a-1",
        "the primitive is c_t = c_s only and does not force a=1",
        "c_t = c_s" in primitive
        and not primitive_forces_a_1
        and "a_x = a_y = a_z" in primitive
        and "a^{-1} = M_Pl" in primitive
        and not speed_preserved(Fraction(1, 2)),
        residual=primitive_forces_a_1,
    )
    checks.check(
        "canonical-nonmutation",
        "the continuation family is absent from the canonical axiom and primitive files",
        "Q_a" not in axiom
        and "Q_a" not in primitive
        and "omega_coeff" not in axiom
        and "omega_coeff" not in primitive
        and "speed_preserved" not in axiom
        and "speed_preserved" not in primitive,
    )

    checks.check(
        "note-preserves-ct-cs",
        "the note records c_t = c_s",
        "c_t = c_s" in note,
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo and the kinetic-isotropy primitive",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "target_claim_id: speed_preserving_linear_wick_map_is_unit_clock",
                "hypothetical_axiom_status: no edit",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "note-theorem-4-noninstall",
        "the note does not install a=1 and does not claim Lorentzian closure",
        "does not install `a = 1`" in note
        and "does not claim Lorentzian closure" in note
        and "N5" in note
        and "Theorem 4" in note,
    )
    checks.check(
        "note-witnesses",
        "the note exhibits omega_coeff -1/16 versus 1/4 and unit-clock a=±1",
        "-1/16" in note
        and "omega_coeff(a) = -a^2/4" in note
        and "a * a == 1" in note
        and "a = 1/2" in note
        and "a = 2" in note,
    )

    forbidden = ("new axiom", "we adopt", "promoted", "Codex")
    retained_hits = [
        line
        for line in note.splitlines()
        if "retained" in line
        and "audit_required_before_effective_retained" not in line
        and "bare_retained_allowed" not in line
    ]
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids axiom-adoption, promotion, and executor-name rhetoric",
        all(phrase not in note for phrase in forbidden) and retained_hits == [],
        residual=retained_hits,
    )

    print("N5: Theorem 4 does not install a=1")
    print("N5: Theorem 4 does not claim Lorentzian closure")
    print("N5: speed-preservation is an extra matching, not an axiom sentence")
    print("per_element: each displayed a is tested by speed_preserved(a):=(a*a==1)")
    print("per_site: momentum-space quadratic forms; no composite carrier is asserted")
    print("per_mode: quadratic TT form only; no spectral-mode exhaustion is claimed")
    print("per_block: linear Wick family versus the extra speed matching")
    print("lattice_wide: checked and not executed — no lattice-wide Lorentzian closure is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
