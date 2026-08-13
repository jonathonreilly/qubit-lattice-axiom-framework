#!/usr/bin/env python3
"""Exact checks: Record additivity does not supply the Newton product.

I on a disjoint union is the sum. The triples (2,0), (1,1), (0,2) share
that sum and do not share the product m_s m_t. The Newton Green pairing
is source-linear and has no test-mass factor. A two-argument pairing
B=I(S)I(T) does produce the product. No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NEWTON_PATH = ROOT / "docs" / "NEWTON_LAW_DERIVED_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/NEWTON_LAW_DERIVED_NOTE.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Collection:
    """Finite labeled record collection with rational strengths."""

    atoms: tuple[tuple[str, Fraction], ...] = ()

    def strength(self) -> Fraction:
        return sum((weight for _, weight in self.atoms), Fraction(0))

    def labels(self) -> frozenset[str]:
        return frozenset(label for label, _ in self.atoms)

    def disjoint(self, other: "Collection") -> bool:
        return self.labels().isdisjoint(other.labels())

    def union(self, other: "Collection") -> "Collection":
        if not self.disjoint(other):
            raise ValueError("Record additivity is stated only for disjoint collections")
        return Collection(self.atoms + other.atoms)


def I(collection: Collection) -> Fraction:
    return collection.strength()


def pairing(source: Collection, test: Collection) -> Fraction:
    return I(source) * I(test)


def unit_atoms(prefix: str, count: int) -> Collection:
    return Collection(tuple((f"{prefix}{index}", Fraction(1)) for index in range(count)))


def lumped(label: str, weight: Fraction) -> Collection:
    if weight == 0:
        return Collection()
    return Collection(((label, weight),))


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    newton = NEWTON_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    normalized_newton = normalize(newton)

    print("external_scientific_inputs: current Record additivity and the Newton kernel/non-claims are source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; no runner cache is written")
    print("negative_scope: only I-on-the-union as a product law is rejected; a two-argument pairing remains a live formal escape; gravity is not claimed impossible")

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and Newton packet",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/NEWTON_LAW_DERIVED_NOTE.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    checks.check(
        "source-record-additivity",
        "the exact current Record additivity sentence is present in the axiom memo",
        additivity_sentence in normalized_axiom,
    )
    checks.check(
        "source-newton-nonclaim-product",
        "the Newton packet lists the physical product law as a non-claim",
        "the physical product law `M_source M_test`" in newton,
    )
    checks.check(
        "source-newton-nonclaim-force",
        "the Newton packet lists F = -M_test grad(phi) as a non-claim",
        "F = -M_test grad(phi)" in newton
        and "test-mass force/source response rule" in newton,
    )

    empty = Collection()
    checks.check(
        "empty-readout",
        "I(empty)=0",
        I(empty) == Fraction(0),
        residual=I(empty),
    )

    left = unit_atoms("a", 2)
    right = unit_atoms("b", 3)
    checks.check(
        "disjoint-additivity",
        "I(A union B)=I(A)+I(B) on disjoint unit-atom collections",
        left.disjoint(right) and I(left.union(right)) == I(left) + I(right) == Fraction(5),
        residual=(I(left), I(right), I(left.union(right))),
    )
    overlap = Collection((("shared", Fraction(1)),))
    checks.check(
        "overlap-rejected",
        "union is refused when labels are not disjoint",
        not overlap.disjoint(overlap),
    )

    pair_20 = (unit_atoms("s", 2), Collection())
    pair_11 = (unit_atoms("s", 1), unit_atoms("t", 1))
    pair_02 = (Collection(), unit_atoms("t", 2))
    rejectors = (pair_20, pair_11, pair_02)

    union_values = []
    product_values = []
    for source, test in rejectors:
        checks.check(
            "rejector-disjoint",
            "each rejector pair is pairwise disjoint",
            source.disjoint(test),
        )
        union_values.append(I(source.union(test)))
        product_values.append(pairing(source, test))

    checks.check(
        "union-sum-only",
        "I(S union T) equals the sum m_s+m_t on the three rejector pairs",
        union_values
        == [
            I(pair_20[0]) + I(pair_20[1]),
            I(pair_11[0]) + I(pair_11[1]),
            I(pair_02[0]) + I(pair_02[1]),
        ]
        == [Fraction(2), Fraction(2), Fraction(2)],
        residual=union_values,
    )
    checks.check(
        "union-cannot-distinguish",
        "I(S union T) cannot distinguish (2,0), (1,1), (0,2)",
        len(set(union_values)) == 1 and union_values[0] == Fraction(2),
        residual=union_values,
    )

    computed_products = [
        I(pair_20[0]) * I(pair_20[1]),
        I(pair_11[0]) * I(pair_11[1]),
        I(pair_02[0]) * I(pair_02[1]),
    ]
    checks.check(
        "product-from-factors",
        "m_s m_t recomputed from the two readouts is 0, 1, 0",
        computed_products == [Fraction(0), Fraction(1), Fraction(0)]
        and product_values == computed_products,
        residual=computed_products,
    )
    checks.check(
        "product-distinguishes",
        "m_s m_t distinguishes (1,1) from (2,0) and from (0,2)",
        computed_products[1] != computed_products[0]
        and computed_products[1] != computed_products[2]
        and computed_products[0] == computed_products[2] == Fraction(0),
        residual=computed_products,
    )
    checks.check(
        "no-function-of-the-sum",
        "no function of the single scalar I(S union T) can equal the three products",
        len(set(union_values)) == 1 and len(set(computed_products)) > 1,
        residual=(union_values, computed_products),
    )

    identity_trial = list(union_values)
    constant_trial = [Fraction(1), Fraction(1), Fraction(1)]
    quadratic_trial = [sigma * (sigma - 2) for sigma in union_values]
    checks.check(
        "trial-maps-fail",
        "identity, constant-1, and sigma(sigma-2) all miss the product triple",
        identity_trial != computed_products
        and constant_trial != computed_products
        and quadratic_trial != computed_products
        and set(quadratic_trial) == {Fraction(0)},
        residual=(identity_trial, constant_trial, quadratic_trial),
    )

    lumped_pairs = (
        (lumped("S", Fraction(2)), lumped("T", Fraction(0))),
        (lumped("S", Fraction(1)), lumped("T", Fraction(1))),
        (lumped("S", Fraction(0)), lumped("T", Fraction(2))),
        (lumped("S", Fraction(3, 2)), lumped("T", Fraction(1, 2))),
    )
    lumped_unions = [I(source.union(test)) for source, test in lumped_pairs]
    lumped_products = [I(source) * I(test) for source, test in lumped_pairs]
    checks.check(
        "lumped-and-rational",
        "lumped (2,0),(1,1),(0,2),(3/2,1/2) keep union sum 2 and products 0,1,0,3/4",
        lumped_unions == [Fraction(2)] * 4
        and lumped_products
        == [Fraction(0), Fraction(1), Fraction(0), Fraction(3, 4)],
        residual=(lumped_unions, lumped_products),
    )

    r = sp.symbols("r", positive=True)
    m_s, m_t = sp.symbols("m_s m_t", real=True)
    green = 1 / (4 * sp.pi * r)
    phi = m_s * green
    dphi = sp.diff(phi, r)
    grad_mag = -dphi
    product_force = m_s * m_t / (4 * sp.pi * r**2)
    checks.check(
        "green-kernel",
        "supplied kernel is 1/(4 pi r) and phi is source-linear",
        sp.simplify(green - 1 / (4 * sp.pi * r)) == 0
        and sp.simplify(phi - m_s / (4 * sp.pi * r)) == 0,
    )
    checks.check(
        "green-gradient-source-only",
        "d phi / dr = -m_s/(4 pi r^2) with no m_t factor",
        sp.simplify(dphi + m_s / (4 * sp.pi * r**2)) == 0
        and sp.simplify(grad_mag - m_s / (4 * sp.pi * r**2)) == 0
        and m_t not in grad_mag.free_symbols,
        residual=grad_mag,
    )

    triple = ((2, 0), (1, 1), (0, 2))
    grad_coeffs = [sp.simplify(grad_mag.subs({m_s: source, m_t: test}) * (4 * sp.pi * r**2)) for source, test in triple]
    product_coeffs = [
        sp.simplify(product_force.subs({m_s: source, m_t: test}) * (4 * sp.pi * r**2)) for source, test in triple
    ]
    checks.check(
        "green-misses-product",
        "Green |grad phi| coefficients are 2,1,0; product-law coefficients are 0,1,0",
        grad_coeffs == [sp.Integer(2), sp.Integer(1), sp.Integer(0)]
        and product_coeffs == [sp.Integer(0), sp.Integer(1), sp.Integer(0)]
        and grad_coeffs != product_coeffs,
        residual=(grad_coeffs, product_coeffs),
    )
    checks.check(
        "pairing-is-bilinear",
        "B(S,T)=I(S)I(T) returns the product triple and is not I on the union",
        product_values == [Fraction(0), Fraction(1), Fraction(0)]
        and product_values != union_values
        and pairing(pair_11[0], pair_11[1]) != I(pair_11[0].union(pair_11[1])),
        residual=(product_values, union_values),
    )

    checks.check(
        "note-preserves-empty",
        "the note records I(empty)=0",
        "I(empty)=0" in note,
    )
    checks.check(
        "note-preserves-force-and-product",
        "the note records F = -M_test and M_source M_test",
        "F = -M_test" in note and "M_source M_test" in note,
    )
    checks.check(
        "note-preserves-additivity-sentence",
        "the note quotes the current Record additivity sentence",
        additivity_sentence in normalized_note,
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo and the Newton packet",
        "MINIMAL_AXIOMS_2026-06-29.md" in note and "NEWTON_LAW_DERIVED_NOTE.md" in note,
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
        "note-three-pair-rejector",
        "the note exhibits (2,0), (1,1), (0,2) and I(S∪T)",
        "(2,0)" in note and "(1,1)" in note and "(0,2)" in note and "I(S∪T)" in note,
    )
    checks.check(
        "note-does-not-forbid-gravity",
        "the note states the scoped gap and does not claim gravity is impossible",
        "does not say gravity is impossible" in note
        or "does not:" in note and "gravity is impossible" in note,
    )

    forbidden = ("new axiom", "we adopt", "promoted", "Codex", "Einstein derived")
    retained_hits = [
        line
        for line in note.splitlines()
        if "retained" in line
        and "audit_required_before_effective_retained" not in line
        and "bare_retained_allowed" not in line
    ]
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids axiom-adoption, promotion, executor-name, and Einstein-derived rhetoric",
        all(phrase not in note for phrase in forbidden) and retained_hits == [],
        residual=retained_hits,
    )
    checks.check(
        "canonical-nonmutation",
        "the pairing escape is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("π(S,T)", "B(S,T)", "m_s m_t", "I(S)I(T)")),
    )
    checks.check(
        "newton-kernel-bound",
        "the Newton packet still states the source-linear kernel algebra",
        all(
            phrase in normalized_newton
            for phrase in (
                "G(r) = 1/(4 pi r)",
                "phi(r) = M G(r) = M/(4 pi r)",
                "|grad phi| = M/(4 pi r^2)",
            )
        ),
    )

    print("per_element: each rejector pair is evaluated under I(union) and under I(S)I(T)")
    print("per_site: the statements are collection-level; no composite carrier is asserted")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: only additivity-versus-product versus the Green pairing is tested")
    print("lattice_wide: checked and not executed — no lattice-wide gravity or Einstein equation is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
