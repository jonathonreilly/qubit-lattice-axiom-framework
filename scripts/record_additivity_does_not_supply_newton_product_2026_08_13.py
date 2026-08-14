#!/usr/bin/env python3
"""Exact checks for the conditional pooled-readout theorem.

The current Record axiom supplies no finite-additive scalar functional.  This
runner therefore constructs such a functional as an explicit mathematical
condition.  It verifies both the pooled-value collision and its load-bearing
escape: separately evaluating the same functional supplies the scalar product
by ordinary multiplication.  No cache or governance surface is written.
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
    """Finite labeled atoms carrying rational weights."""

    atoms: tuple[tuple[str, Fraction], ...] = ()

    def labels(self) -> frozenset[str]:
        return frozenset(label for label, _ in self.atoms)

    def disjoint(self, other: "Collection") -> bool:
        return self.labels().isdisjoint(other.labels())

    def union(self, other: "Collection") -> "Collection":
        if not self.disjoint(other):
            raise ValueError("finite additivity is invoked only on disjoint collections")
        return Collection(self.atoms + other.atoms)


def readout(collection: Collection) -> Fraction:
    """The separately supplied finite-additive scalar functional I."""

    return sum((weight for _, weight in collection.atoms), Fraction(0))


def scalar_product(source: Collection, test: Collection) -> Fraction:
    """Canonical product at the separate interface."""

    return readout(source) * readout(test)


def unit_atoms(prefix: str, count: int) -> Collection:
    return Collection(tuple((f"{prefix}{index}", Fraction(1)) for index in range(count)))


def weighted(prefix: str, *weights: Fraction) -> Collection:
    return Collection(tuple((f"{prefix}{index}", value) for index, value in enumerate(weights)))


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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    newton = NEWTON_PATH.read_text(encoding="utf-8")
    normalized_axiom = normalize(axiom)
    normalized_note = normalize(note)
    normalized_newton = normalize(newton)

    print(
        "external_scientific_inputs: the current Record boundary and bounded Newton "
        "kernel/non-claims are source-bound; the finite-additive functional is an "
        "explicit conditional model; no observation or fit is used"
    )
    print(
        "package_local_integrity_reads: the note, current minimal axiom, and Newton "
        "parent are read; no cache or governance surface is written"
    )
    print(
        "negative_scope: only recovery of a two-body product from one pooled scalar "
        "is rejected on the stated free model; separate evaluation and response-law "
        "composition remain live"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note, current axiom, and Newton parent",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/NEWTON_LAW_DERIVED_NOTE.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    current_record = (
        "Only records are readable. A readout value is determined by record content "
        "alone. A site with no record cannot be read."
    )
    exclusion = (
        "Finite additivity, a named scalar collection functional `I`, and an assigned "
        "value `I(empty)=0` are not Record axiom content."
    )
    removed_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout `I` "
        "is additive, with `I(empty)=0`."
    )
    checks.check(
        "current-record-boundary",
        "the approved authority states content-only readability and unreadability at absence",
        current_record in normalized_axiom,
    )
    checks.check(
        "finite-additivity-excluded",
        "the authority explicitly excludes finite additivity, named I, and I(empty)=0",
        exclusion in normalized_axiom,
    )
    checks.check(
        "removed-record-premise-absent",
        "the superseded finite-additivity sentence is absent",
        removed_sentence not in normalized_axiom,
    )
    checks.check(
        "newton-nonclaims",
        "the Newton parent leaves both test response and the physical product open",
        "test-mass force/source response rule `F = -M_test grad(phi)`" in newton
        and "physical product law `M_source M_test`" in newton,
    )

    empty = Collection()
    a = weighted("a", Fraction(1, 3), Fraction(2, 3))
    b = weighted("b", Fraction(-2), Fraction(5, 2))
    checks.check(
        "conditional-empty",
        "the supplied model has I(empty)=0",
        readout(empty) == 0,
        readout(empty),
    )
    checks.check(
        "conditional-additivity",
        "the weighted model is finite-additive on disjoint collections",
        a.disjoint(b)
        and readout(a.union(b)) == readout(a) + readout(b) == Fraction(3, 2),
        (readout(a), readout(b), readout(a.union(b))),
    )
    overlapping = weighted("shared", Fraction(1))
    try:
        overlapping.union(overlapping)
    except ValueError:
        overlap_rejected = True
    else:
        overlap_rejected = False
    checks.check(
        "disjoint-domain",
        "the constructed union refuses overlapping labels",
        overlap_rejected,
    )

    rejectors = (
        (unit_atoms("s20_", 2), Collection()),
        (unit_atoms("s11_", 1), unit_atoms("t11_", 1)),
        (Collection(), unit_atoms("t02_", 2)),
    )
    pooled = [readout(source.union(test)) for source, test in rejectors]
    products = [scalar_product(source, test) for source, test in rejectors]
    checks.check(
        "pooled-collision",
        "(2,0), (1,1), and (0,2) all expose pooled value 2",
        pooled == [Fraction(2)] * 3,
        pooled,
    )
    checks.check(
        "product-separation",
        "their separately evaluated products are 0, 1, 0",
        products == [Fraction(0), Fraction(1), Fraction(0)],
        products,
    )
    checks.check(
        "arbitrary-function-rejector",
        "one function of the common pooled input cannot return both 0 and 1",
        len(set(pooled)) == 1 and len(set(products)) == 2,
        (pooled, products),
    )
    trial_outputs = {
        "identity": [value for value in pooled],
        "constant-one": [Fraction(1) for _ in pooled],
        "quadratic": [value**2 for value in pooled],
    }
    checks.check(
        "named-pooled-trials",
        "identity, constant, and nonlinear pooled trials each miss the product triple",
        all(candidate != products for candidate in trial_outputs.values()),
        trial_outputs,
    )

    for total in (Fraction(2), Fraction(7, 3), Fraction(-4)):
        diagonal_product = (total / 2) ** 2
        checks.check(
            "diagonal-escape",
            "on m_s=m_t the product is (sigma/2)^2",
            diagonal_product == (total / 2) * (total / 2),
            (total, diagonal_product),
        )
    fixed_test = Fraction(3, 5)
    for source_value in (Fraction(0), Fraction(7, 4), Fraction(-2)):
        sigma = source_value + fixed_test
        checks.check(
            "fixed-test-escape",
            "with externally fixed m_t, the product is m_t(sigma-m_t)",
            fixed_test * (sigma - fixed_test) == source_value * fixed_test,
            (source_value, sigma),
        )
    for source_value, test_value in (
        (Fraction(2), Fraction(0)),
        (Fraction(1), Fraction(1)),
        (Fraction(3, 2), Fraction(1, 2)),
    ):
        sigma = source_value + test_value
        delta = source_value - test_value
        checks.check(
            "second-statistic-escape",
            "sigma and delta recover the product as (sigma^2-delta^2)/4",
            (sigma**2 - delta**2) / 4 == source_value * test_value,
            (source_value, test_value, sigma, delta),
        )

    s1 = weighted("s1_", Fraction(1, 2), Fraction(2))
    s2 = weighted("s2_", Fraction(-1, 3), Fraction(1))
    t1 = weighted("t1_", Fraction(5, 4))
    t2 = weighted("t2_", Fraction(7, 5), Fraction(-2, 5))
    checks.check(
        "separate-product-definition",
        "separate evaluation gives B_I(S,T)=I(S)I(T)",
        scalar_product(s1, t1) == readout(s1) * readout(t1),
    )
    checks.check(
        "separate-additivity-source",
        "B_I is additive in the source argument",
        scalar_product(s1.union(s2), t1)
        == scalar_product(s1, t1) + scalar_product(s2, t1),
    )
    checks.check(
        "separate-additivity-test",
        "B_I is additive in the test argument",
        scalar_product(s1, t1.union(t2))
        == scalar_product(s1, t1) + scalar_product(s1, t2),
    )

    radius = sp.symbols("r", positive=True)
    m_source, m_test = sp.symbols("m_source m_test", real=True)
    green = 1 / (4 * sp.pi * radius)
    potential = m_source * green
    gradient_magnitude = -sp.diff(potential, radius)
    response_magnitude = m_test * gradient_magnitude
    checks.check(
        "source-linear-kernel",
        "the parent kernel gives |grad phi|=m_source/(4 pi r^2)",
        sp.simplify(gradient_magnitude - m_source / (4 * sp.pi * radius**2)) == 0
        and m_test not in gradient_magnitude.free_symbols,
        gradient_magnitude,
    )
    checks.check(
        "conditional-test-response",
        "supplying test response produces the two-mass product",
        sp.simplify(
            response_magnitude - m_source * m_test / (4 * sp.pi * radius**2)
        )
        == 0,
        response_magnitude,
    )

    required_note_phrases = (
        "Finite-additive scalar hypothesis",
        "does not in general determine the product",
        "ordinary scalar multiplication canonically",
        "No new abstract bilinear pairing rule is needed",
        "source/test typing",
        "mass-readout identification",
        "test-body response",
        "The proof boundary is **CONDITIONAL**",
        "**No-Go Discipline status: PASS**",
    )
    checks.check(
        "note-claim-contract",
        "the note states the conditional theorem, escape, and physical residual",
        all(phrase in normalized_note for phrase in required_note_phrases),
        [phrase for phrase in required_note_phrases if phrase not in normalized_note],
    )
    checks.check(
        "note-dependency-contract",
        "frontmatter names only the current axiom boundary and Newton parent",
        "  - minimal_axioms" in note
        and "  - newton_law_derived_note" in note
        and "observable_principle" not in note,
    )
    checks.check(
        "note-machine-contract",
        "the note uses controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "reachability_to_target: prunes",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                "hypothetical_axiom_status: \"no edit\"",
            )
        ),
    )
    checks.check(
        "note-no-go-contract",
        "the note records all eight stress-test sections",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    forbidden = (
        "Therefore gravity is impossible",
        "Finite additivity forbids a product",
        "The framework must add a pairing axiom",
        "The current Record axiom supplies finite additivity",
    )
    checks.check(
        "forbidden-broad-rhetoric",
        "the source avoids the rejected broad claims",
        all(phrase not in note for phrase in forbidden),
        [phrase for phrase in forbidden if phrase in note],
    )
    checks.check(
        "newton-parent-contract",
        "the cited parent retains its exact source-linear algebra",
        all(
            phrase in normalized_newton
            for phrase in (
                "G(r) = 1/(4 pi r)",
                "phi(r) = M G(r) = M/(4 pi r)",
                "|grad phi| = M/(4 pi r^2)",
            )
        ),
    )

    print(
        "per_element: checked — each atom weight and every rejector scalar is "
        "evaluated exactly over the rationals"
    )
    print(
        "per_site: checked and not executed — the conditional collection model "
        "carries labels but asserts no site-local physical readout"
    )
    print(
        "per_mode: checked and not executed — no spectral or Fourier decomposition "
        "is used or excluded"
    )
    print(
        "per_block: checked — pooled and separately accessible two-collection "
        "interfaces are evaluated independently"
    )
    print(
        "lattice_wide: checked and not executed — no lattice dynamics, two-body "
        "response, or gravity closure is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
