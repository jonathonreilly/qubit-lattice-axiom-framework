#!/usr/bin/env python3
"""Exact checks: kinetic isotropy does not fix the Lorentzian clock map.

Euclidean TT form Q_E = (k4^2 + k^2)/4 is independent of a. Continuation
k4 = i a ω produces Q_a = (-a^2 ω^2 + k^2)/4. The values a = 1/2, 1, 2
give Lorentzian ω^2 coefficients 1/16, 1/4, 1. The primitive supplies
c_t = c_s, not a. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/KINETIC_ISOTROPY_DOES_NOT_FIX_LORENTZIAN_CLOCK_MAP_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PRIMITIVE_REL = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_DOES_NOT_FIX_LORENTZIAN_CLOCK_MAP_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
PRIMITIVE_PATH = ROOT / PRIMITIVE_REL
AXIOM_PATH = ROOT / AXIOM_REL

A_VALUES = (Fraction(1, 2), Fraction(1), Fraction(2))
CLOCK_MAP_PHRASES = (
    "k4 = i a ω",
    "k4 = i a",
    "k_4 = i a",
    "i a ω",
    "clock map a",
    "Q_a",
)


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
    kappa = -sp.expand(q_a).coeff(omega**2)
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
        "kappa": kappa,
        "spatial": spatial,
    }


def continued_form(family: dict[str, object], a_val: Fraction) -> sp.Expr:
    return sp.expand(family["q_a"].subs(family["a"], sp.Rational(a_val.numerator, a_val.denominator)))


def kappa_at(family: dict[str, object], a_val: Fraction) -> Fraction:
    return as_fraction(family["kappa"].subs(family["a"], sp.Rational(a_val.numerator, a_val.denominator)))


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    norm_primitive = normalize(primitive)
    norm_axiom = normalize(axiom)
    family = build_family()

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: kinetic-isotropy primitive and the four-axiom memo; no observational or fitted inputs")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; no runner cache is written")
    print("negative_scope: only Euclidean OS0 as a selector of a is rejected; a declared continuation remains a live formal escape")

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, primitive, and axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, PRIMITIVE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    ct_cs_block = "c_t = c_s"
    os0_sentence = "Osterwalder-Schrader OS0 kinetic normalization"
    no_amend_sentence = "It does not add or amend an axiom."
    checks.check(
        "source-primitive-ct-cs",
        "the primitive supplies the Euclidean equality c_t = c_s",
        ct_cs_block in primitive,
    )
    checks.check(
        "source-primitive-os0",
        "the primitive identifies that equality with OS0 kinetic normalization",
        os0_sentence in normalize(primitive.replace("`", "")),
    )
    checks.check(
        "source-primitive-no-axiom-amend",
        "the primitive states that it does not add or amend an axiom",
        no_amend_sentence in primitive,
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
    kx = family["kx"]
    a = family["a"]
    c_t = q_e.coeff(k4**2)
    c_s = q_e.coeff(kx**2)
    checks.check(
        "theorem-1-euclidean-independent-of-a",
        "Q_E = (k4^2+k^2)/4 contains no continuation parameter a",
        a not in q_e.free_symbols
        and sp.simplify(q_e - (k4**2 + family["k2"]) / 4) == 0,
        residual=q_e,
    )
    checks.check(
        "theorem-1-os0-equal-coefficients",
        "Euclidean coefficients of k4^2 and kx^2 are both 1/4, so c_t = c_s",
        as_fraction(c_t) == Fraction(1, 4)
        and as_fraction(c_s) == Fraction(1, 4)
        and sp.simplify(c_t - c_s) == 0,
        residual=(c_t, c_s),
    )

    sample = q_e.subs({k4: 2, family["kx"]: 3, family["ky"]: 0, family["kz"]: 0})
    recovered = []
    for a_val in A_VALUES:
        q_cont = continued_form(family, a_val)
        back = sp.expand(
            q_cont.subs(
                family["omega"],
                -sp.I * k4 / sp.Rational(a_val.numerator, a_val.denominator),
            )
        )
        recovered.append(sp.simplify(back - q_e) == 0)
    checks.check(
        "theorem-1-shared-euclidean-values",
        "all three continuations recover the same Q_E; sample (k4,k)=(2,3) is 13/4",
        all(recovered) and as_fraction(sample) == Fraction(13, 4),
        residual=(recovered, sample),
    )

    expanded = sp.expand(family["q_a"])
    checks.check(
        "theorem-2-continuation-identity",
        "substituting k4 = i a ω into Q_E yields (-a^2 ω^2 + k^2)/4",
        sp.simplify(expanded - ((-(a**2) * family["omega"] ** 2 + family["k2"]) / 4)) == 0,
        residual=expanded,
    )

    computed = [kappa_at(family, a_val) for a_val in A_VALUES]
    checks.check(
        "theorem-2-three-coefficients",
        "a = 1/2, 1, 2 give Lorentzian ω^2 coefficients 1/16, 1/4, 1",
        computed == [Fraction(1, 16), Fraction(1, 4), Fraction(1)],
        residual=computed,
    )
    checks.check(
        "theorem-2-distinct",
        "the three Lorentzian coefficients are pairwise distinct",
        len(set(computed)) == 3,
        residual=computed,
    )
    spatial_vals = [
        as_fraction(family["spatial"].subs(a, sp.Rational(a_val.numerator, a_val.denominator)))
        for a_val in A_VALUES
    ]
    checks.check(
        "theorem-2-spatial-coeff-unchanged",
        "the spatial coefficient remains 1/4 for every displayed a",
        spatial_vals == [Fraction(1, 4), Fraction(1, 4), Fraction(1, 4)],
        residual=spatial_vals,
    )
    checks.check(
        "theorem-2-euclidean-recovery",
        "ω = -i k4 / a returns Q_E on each displayed row",
        all(recovered),
    )

    no_a_form = sp.expand(q_e.subs(k4, sp.I * family["omega"]))
    no_a_kappa = [-as_fraction(no_a_form.coeff(family["omega"] ** 2)) for _ in A_VALUES]
    checks.check(
        "discriminating-a-less-wick",
        "dropping a and writing k4 = i ω collapses every coefficient to 1/4",
        no_a_kappa == [Fraction(1, 4), Fraction(1, 4), Fraction(1, 4)]
        and no_a_kappa != computed,
        residual=no_a_kappa,
    )

    half_form = (k4**2 + family["k2"]) / 2
    half_cont = sp.expand(half_form.subs(k4, sp.I * a * family["omega"]))
    half_kappa = [
        as_fraction((-half_cont.coeff(family["omega"] ** 2)).subs(a, sp.Rational(av.numerator, av.denominator)))
        for av in A_VALUES
    ]
    checks.check(
        "discriminating-half-normalization",
        "replacing the TT factor 1/4 by 1/2 moves the triple to 1/8, 1/2, 2",
        half_kappa == [Fraction(1, 8), Fraction(1, 2), Fraction(2)]
        and half_kappa != computed,
        residual=half_kappa,
    )

    eucl_with_a = (a**2 * k4**2 + family["k2"]) / 4
    eucl_ct = [
        as_fraction(eucl_with_a.coeff(k4**2).subs(a, sp.Rational(av.numerator, av.denominator)))
        for av in A_VALUES
    ]
    checks.check(
        "discriminating-a-in-euclidean",
        "putting a into Q_E makes the Euclidean temporal coefficient a-dependent",
        eucl_ct == [Fraction(1, 16), Fraction(1, 4), Fraction(1)]
        and len(set(eucl_ct)) == 3
        and a in eucl_with_a.free_symbols
        and a not in q_e.free_symbols
        and as_fraction(c_t) == Fraction(1, 4),
        residual=eucl_ct,
    )

    checks.check(
        "note-preserves-ct-cs",
        "the note records c_t = c_s",
        "c_t = c_s" in note,
    )
    checks.check(
        "note-links-parents",
        "the note links the primitive and the axiom memo",
        "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md" in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note,
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
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                "hypothetical_axiom_status: no edit",
            )
        ),
    )
    checks.check(
        "note-three-a-values",
        "the note exhibits a=1/2,1,2 and coefficients 1/16, 1/4, 1",
        "1/16" in note and "a = 1/2" in note and "a = 2" in note and "κ(a) = a^2/4" in note,
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

    primitive_clock = [phrase for phrase in CLOCK_MAP_PHRASES if phrase in primitive]
    axiom_clock = [phrase for phrase in CLOCK_MAP_PHRASES if phrase in axiom]
    checks.check(
        "sources-do-not-name-clock-map-a",
        "neither source note writes the continuation k4 = i a ω or the family Q_a",
        primitive_clock == [] and axiom_clock == [],
        residual=(primitive_clock, axiom_clock),
    )
    checks.check(
        "canonical-nonmutation",
        "the continuation family is absent from the canonical axiom and primitive files",
        "Q_a" not in axiom
        and "Q_a" not in primitive
        and "κ(a)" not in axiom
        and "κ(a)" not in primitive,
    )
    checks.check(
        "primitive-a-uses-are-spacing-or-scale",
        "primitive uses of a are a_x = a_y = a_z and a^{-1} = M_Pl only",
        "a_x = a_y = a_z" in primitive
        and "a^{-1} = M_Pl" in primitive
        and "k4" not in primitive
        and "ω" not in primitive,
    )

    print("per_element: each a in {1/2, 1, 2} is continued from the same Q_E")
    print("per_site: the statements are momentum-space quadratic forms; no composite carrier is asserted")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: only Euclidean OS0 versus the linear clock map a is tested")
    print("lattice_wide: checked and not executed — no lattice-wide Lorentz restoration is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
