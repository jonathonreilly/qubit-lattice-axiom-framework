#!/usr/bin/env python3
"""Exact checks: record accumulation count does not fix the Wick clock map.

N(R) is the locked-site count and is independent of a. Continuation
k_4 = i a ω of Q_E = (k_4^2 + k^2)/4 produces omega_coeff(a) = -a^2/4.
The values a = 1/2, 1, 2 give -1/16, -1/4, -1. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/RECORD_ACCUMULATION_COUNT_DOES_NOT_FIX_WICK_CLOCK_MAP_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVE_REL = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_ACCUMULATION_COUNT_DOES_NOT_FIX_WICK_CLOCK_MAP_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL
PRIMITIVE_PATH = ROOT / PRIMITIVE_REL

A_VALUES = (Fraction(1, 2), Fraction(1), Fraction(2))
OMEGA_TRIPLE = (Fraction(-1, 16), Fraction(-1, 4), Fraction(-1))
CLOCK_MAP_PHRASES = (
    "k_4 = i a ω",
    "k4 = i a ω",
    "k_4 = i a",
    "k4 = i a",
    "i a ω",
    "clock map a",
    "omega_coeff",
    "Q_a",
)

SITE_0 = "0"
SITE_E1 = "e1"
WINDOW = frozenset({SITE_0, SITE_E1, "2e1", "3e1"})
EMPTY = frozenset()
R1 = frozenset({SITE_0})
R2 = frozenset({SITE_0, SITE_E1})
CHAIN = (EMPTY, R1, R2)


def N(record: frozenset[str]) -> int:
    """Accumulation count: number of locked sites. Independent of a."""
    if not record.issubset(WINDOW):
        raise ValueError("configuration is not a subset of the finite window")
    return len(record)


def omega_coeff(a: Fraction) -> Fraction:
    """Lorentzian ω^2 coefficient of Q_a: -a^2/4."""
    return -(a * a) / Fraction(4)


def I_unit(record: frozenset[str]) -> Fraction:
    """Unit content-only readout: each locked site contributes 1."""
    return Fraction(N(record))


def N_depends_on_a(record: frozenset[str], a_values: tuple[Fraction, ...]) -> bool:
    """Hostile predicate: the count changes with a. Identity N forbids this."""
    counts = {a: N(record) for a in a_values}
    return len(set(counts.values())) > 1


def omega_coeff_constant(_a: Fraction) -> Fraction:
    """Hostile mutation: replace omega_coeff by a constant independent of a."""
    return Fraction(-1, 4)


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
    print("negative_scope: Record counts and Euclidean OS0 as selectors of a are rejected; a declared continuation remains a live formal escape")

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
        "source-emergent-time",
        "the primitive states that time remains emergent and derived",
        "the framework's time remains emergent and derived" in normalize(primitive),
    )
    checks.check(
        "source-axiom-I-empty",
        "the axiom memo states I(empty)=0",
        "`I` is additive, with `I(empty)=0`" in axiom,
    )
    checks.check(
        "source-axiom-records-form",
        "the axiom memo states Records form",
        "Records form." in axiom,
    )
    checks.check(
        "source-axiom-content-only",
        "the axiom memo states readout is determined by record content alone",
        "A readout value is determined by record content alone." in norm_axiom,
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

    checks.check(
        "window-card",
        "the finite window has n=4 sites",
        len(WINDOW) == 4,
        residual=len(WINDOW),
    )
    checks.check(
        "theorem-1-chain",
        "empty subset {0} subset {0,e1} is monotone with N=0,1,2",
        EMPTY < R1 < R2
        and N(EMPTY) == 0
        and N(R1) == 1
        and N(R2) == 2
        and [N(record) for record in CHAIN] == [0, 1, 2],
        residual=[N(record) for record in CHAIN],
    )

    counts_by_a = {a: tuple(N(record) for record in CHAIN) for a in A_VALUES}
    checks.check(
        "theorem-1-a-blind",
        "the same chain has counts 0,1,2 for every a in {1/2,1,2}",
        all(counts == (0, 1, 2) for counts in counts_by_a.values())
        and len(set(counts_by_a.values())) == 1,
        residual=counts_by_a,
    )
    checks.check(
        "theorem-1-N-depends-on-a-fails",
        "predicate N_depends_on_a is false on every displayed configuration",
        not any(N_depends_on_a(record, A_VALUES) for record in CHAIN),
    )

    q_e = family["q_e"]
    k4 = family["k4"]
    a_sym = family["a"]
    checks.check(
        "theorem-2-Q-E-independent",
        "Q_E = (k_4^2+k^2)/4 contains no continuation parameter a",
        a_sym not in q_e.free_symbols
        and sp.simplify(q_e - (k4**2 + family["k2"]) / 4) == 0,
        residual=q_e,
    )
    c_t = q_e.coeff(k4**2)
    c_s = q_e.coeff(family["kx"] ** 2)
    checks.check(
        "theorem-2-os0",
        "Euclidean coefficients of k_4^2 and kx^2 are both 1/4, so c_t = c_s",
        as_fraction(c_t) == Fraction(1, 4)
        and as_fraction(c_s) == Fraction(1, 4)
        and sp.simplify(c_t - c_s) == 0,
        residual=(c_t, c_s),
    )

    expanded = sp.expand(family["q_a"])
    checks.check(
        "theorem-2-continuation",
        "substituting k_4 = i a ω into Q_E yields (-a^2 ω^2 + k^2)/4",
        sp.simplify(
            expanded - ((-(a_sym**2) * family["omega"] ** 2 + family["k2"]) / 4)
        )
        == 0,
        residual=expanded,
    )

    derived = [derived_omega_coeff(family, a_val) for a_val in A_VALUES]
    identity = [omega_coeff(a_val) for a_val in A_VALUES]
    checks.check(
        "theorem-2-omega-coeff",
        "omega_coeff(1/2,1,2) = -1/16, -1/4, -1 equals the derived [ω^2] Q_a",
        identity == list(OMEGA_TRIPLE) and derived == identity,
        residual=(identity, derived),
    )
    checks.check(
        "theorem-2-distinct",
        "the three Lorentzian ω^2 coefficients are pairwise distinct",
        omega_coeff(Fraction(1, 2)) != omega_coeff(Fraction(1))
        and omega_coeff(Fraction(1)) != omega_coeff(Fraction(2))
        and len(set(identity)) == 3,
        residual=identity,
    )

    recovered = []
    for a_val in A_VALUES:
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
        "theorem-2-shared-euclidean",
        "all three continuations recover the same Q_E; sample (k4,kx)=(2,3) is 13/4",
        all(recovered) and as_fraction(sample) == Fraction(13, 4),
        residual=(recovered, sample),
    )

    mutated = [omega_coeff_constant(a_val) for a_val in A_VALUES]
    checks.check(
        "mutation-constant-omega-fails",
        "replacing omega_coeff by a constant collapses -1/16 vs -1/4",
        mutated == [Fraction(-1, 4)] * 3
        and mutated != identity
        and omega_coeff(Fraction(1, 2)) != omega_coeff(Fraction(1)),
        residual=mutated,
    )

    i_values = [I_unit(record) for record in CHAIN]
    checks.check(
        "theorem-4-I-equals-N",
        "unit I(R)=N(R) gives 0,1,2 and I(empty)=0",
        i_values == [Fraction(0), Fraction(1), Fraction(2)]
        and I_unit(EMPTY) == Fraction(0)
        and all(I_unit(record) == Fraction(N(record)) for record in CHAIN),
        residual=i_values,
    )
    i_by_a = {a: tuple(I_unit(record) for record in CHAIN) for a in A_VALUES}
    checks.check(
        "theorem-4-I-a-blind",
        "unit I is the same triple for every displayed a",
        all(values == (Fraction(0), Fraction(1), Fraction(2)) for values in i_by_a.values()),
        residual=i_by_a,
    )

    primitive_clock = [phrase for phrase in CLOCK_MAP_PHRASES if phrase in primitive]
    axiom_clock = [phrase for phrase in CLOCK_MAP_PHRASES if phrase in axiom]
    checks.check(
        "theorem-3-sources-do-not-name-a",
        "neither source writes the continuation k_4 = i a ω or omega_coeff",
        primitive_clock == [] and axiom_clock == [],
        residual=(primitive_clock, axiom_clock),
    )
    primitive_forces_a_1 = (
        "k4 = i" in primitive
        or "k_4 = i" in primitive
        or "forces a=1" in primitive
        or "a = 1" in primitive
    )
    checks.check(
        "mutation-primitive-forces-a-1-fails",
        "the primitive is c_t = c_s only and does not force a=1",
        "c_t = c_s" in primitive
        and not primitive_forces_a_1
        and "a_x = a_y = a_z" in primitive
        and "a^{-1} = M_Pl" in primitive
        and omega_coeff(Fraction(1, 2)) != omega_coeff(Fraction(1)),
        residual=primitive_forces_a_1,
    )

    checks.check(
        "identity-gates-present",
        "identity gates N(R) and omega_coeff(a)=-a^2/4 are the called maps",
        N.__doc__ is not None
        and "Independent of a" in (N.__doc__ or "")
        and omega_coeff(Fraction(2)) == Fraction(-1)
        and inspect_identity_source(),
    )

    checks.check(
        "note-preserves-ct-cs-and-I-empty",
        "the note records c_t = c_s and I(empty)=0",
        "c_t = c_s" in note and "I(empty)=0" in note,
    )
    checks.check(
        "note-quotes-emergent-time",
        "the note quotes that time remains emergent and derived",
        "time remains emergent and derived" in note,
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
                "target_claim_id: wick_clock_map_a",
                'target_blocker_text: "fix the Lorentzian/Wick clock map a from axioms or primitives"',
                "reachability_to_target: prunes",
                "next_trace_action: \"Record counts and kinetic isotropy both leave a free. Do not adopt axiom text.\"",
                'hypothetical_axiom_status: "no edit"',
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "note-witnesses",
        "the note exhibits N=0,1,2 and omega_coeff -1/16, -1/4, -1",
        "N(empty)" in note
        and "-1/16" in note
        and "omega_coeff(a) = -a^2/4" in note
        and "a = 1/2" in note,
    )
    checks.check(
        "note-scoped-residual",
        "the note does not install a and does not claim Lorentzian closure",
        "does not install a value of `a`" in note
        and "does not claim Lorentzian closure" in note,
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

    print("per_element: each a in {1/2, 1, 2} is tested against the same N-chain and the same Q_E")
    print("per_site: locked-site cardinality on a four-site window; no composite carrier is asserted")
    print("per_mode: quadratic TT form only; no spectral-mode exhaustion is claimed")
    print("per_block: Record count and Euclidean OS0 versus the linear clock map a")
    print("lattice_wide: checked and not executed — no lattice-wide Lorentzian closure is claimed")
    return checks.finish()


def inspect_identity_source() -> bool:
    text = Path(__file__).read_text(encoding="utf-8")
    return "def N(" in text and "def omega_coeff(" in text and "-a^2/4" in text


if __name__ == "__main__":
    raise SystemExit(main())
