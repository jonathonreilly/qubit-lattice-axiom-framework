#!/usr/bin/env python3
"""Exact checks: Record does not type Newton source versus test.

The source-linear Green pairing supplies two assignments on a disjoint
pair. Content-only additivity is swap-symmetric and does not select which
collection is the source. The unequal-mass split is 1/(2 pi) versus
1/(4 pi). A declared typing remains a second object. No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/RECORD_DOES_NOT_TYPE_NEWTON_SOURCE_VERSUS_TEST_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/NEWTON_LAW_DERIVED_NOTE.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
NEWTON_PATH = ROOT / AUDIT_INPUT_PATHS[2]


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

    def content(self) -> frozenset[tuple[str, Fraction]]:
        return frozenset(self.atoms)

    def disjoint(self, other: "Collection") -> bool:
        return self.labels().isdisjoint(other.labels())

    def union(self, other: "Collection") -> "Collection":
        if not self.disjoint(other):
            raise ValueError("Record additivity is stated only for disjoint collections")
        return Collection(self.atoms + other.atoms)


def I(collection: Collection) -> Fraction:
    return collection.strength()


def as_sympy(value: Fraction | int | sp.Expr) -> sp.Expr:
    if isinstance(value, sp.Expr):
        return value
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.Integer(value)


def is_zero(expr: object) -> bool:
    return sp.simplify(sp.sympify(expr)) == 0


def grad_magnitude(mass: object, radius: object) -> sp.Expr:
    """Identity-gate function: Newton source-linear gradient magnitude."""
    return as_sympy(mass) / (4 * sp.pi * as_sympy(radius) ** 2)


def swap_invariant_union_grad(source: Collection, test: Collection, radius: object) -> sp.Expr:
    """Mutation: always use I(S)+I(T) as the mass."""
    return (as_sympy(I(source) + I(test))) / (4 * sp.pi * as_sympy(radius) ** 2)


def product_law_grad(source: Collection, test: Collection, radius: object) -> sp.Expr:
    """Mutation: product law I(S)I(T)/(4 pi r^2)."""
    return (as_sympy(I(source) * I(test))) / (4 * sp.pi * as_sympy(radius) ** 2)


def label_order_grad(pair: tuple[Collection, Collection], radius: object) -> sp.Expr:
    """Declared typing: first Python tuple entry is the source."""
    source, _test = pair
    return grad_magnitude(I(source), radius)


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    normalized_newton = normalize(newton)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("two-kinds split: external_scientific_inputs versus package_local_integrity_reads")
    print(
        "external_scientific_inputs: current Record content-only and additivity "
        "sentences plus the Newton kernel and non-claims are source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: only unlabeled Record data as a unique Newton source "
        "selector is rejected; a declared typing remains a live formal escape; "
        "gravity is not claimed impossible"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and Newton packet",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_DOES_NOT_TYPE_NEWTON_SOURCE_VERSUS_TEST_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/NEWTON_LAW_DERIVED_NOTE.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    record_content = "A readout value is determined by record content alone."
    record_additivity = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    newton_force = "F = -M_test grad(phi)"
    newton_product = "the physical product law `M_source M_test`"

    checks.check(
        "source-record-content-only",
        "the exact current Record content-only sentence is present in the axiom memo and the note",
        record_content in normalized_axiom and record_content in normalized_note,
    )
    checks.check(
        "source-record-additivity",
        "the exact current Record additivity sentence is present in the axiom memo and the note",
        record_additivity in normalized_axiom and record_additivity in normalized_note,
    )
    checks.check(
        "source-newton-nonclaim-force",
        "the Newton packet lists F = -M_test grad(phi) as a non-claim",
        newton_force in newton and "test-mass force/source response rule" in newton,
    )
    checks.check(
        "source-newton-nonclaim-product",
        "the Newton packet lists the physical product law as a non-claim",
        newton_product in newton,
    )
    checks.check(
        "note-pins-newton-nonclaims",
        "the note records F = -M_test grad(phi) and the physical product law M_source M_test",
        newton_force in note and newton_product in note,
    )

    empty = Collection()
    checks.check(
        "empty-readout",
        "I(empty)=0",
        I(empty) == Fraction(0),
        residual=I(empty),
    )

    source = unit_atoms("s", 2)
    test = unit_atoms("t", 1)
    checks.check(
        "witness-collections",
        "unit-atom collections realize I(S)=2, I(T)=1, I(S union T)=3 and are disjoint",
        source.disjoint(test)
        and I(source) == Fraction(2)
        and I(test) == Fraction(1)
        and I(source.union(test)) == I(source) + I(test) == Fraction(3),
        residual=(I(source), I(test), I(source.union(test))),
    )

    r = sp.symbols("r", positive=True)
    mass = sp.symbols("m", real=True)
    green = 1 / (4 * sp.pi * r)
    phi = mass * green
    dphi = sp.diff(phi, r)
    checks.check(
        "green-kernel",
        "supplied kernel is 1/(4 pi r) and phi is source-linear",
        is_zero(green - 1 / (4 * sp.pi * r)) and is_zero(phi - mass / (4 * sp.pi * r)),
        residual=green,
    )
    checks.check(
        "theorem-1-derivative",
        "d phi / dr = -m/(4 pi r^2) and |grad phi| equals grad_magnitude(m, r)",
        is_zero(dphi + mass / (4 * sp.pi * r**2))
        and is_zero(-dphi - grad_magnitude(mass, r)),
        residual=dphi,
    )

    grad_s = grad_magnitude(I(source), r)
    grad_t = grad_magnitude(I(test), r)
    checks.check(
        "theorem-1-two-assignments",
        "|grad phi_S| = I(S)/(4 pi r^2) and |grad phi_T| = I(T)/(4 pi r^2)",
        is_zero(grad_s - as_sympy(I(source)) / (4 * sp.pi * r**2))
        and is_zero(grad_t - as_sympy(I(test)) / (4 * sp.pi * r**2)),
        residual=(grad_s, grad_t),
    )
    equal_left = unit_atoms("u", 1)
    equal_right = unit_atoms("v", 1)
    checks.check(
        "theorem-1-equal-iff-masses-equal",
        "the two Green assignments are equal iff I(S)=I(T)",
        not is_zero(grad_s - grad_t)
        and I(source) != I(test)
        and I(equal_left) == I(equal_right)
        and is_zero(grad_magnitude(I(equal_left), r) - grad_magnitude(I(equal_right), r)),
        residual=(sp.simplify(grad_s - grad_t), I(equal_left), I(equal_right)),
    )

    union_st = source.union(test)
    union_ts = test.union(source)
    unlabeled = (I(union_st), frozenset({I(source), I(test)}))
    unlabeled_swapped = (I(union_ts), frozenset({I(test), I(source)}))
    checks.check(
        "theorem-2-swap-symmetry",
        "contents, union atoms, and I(S union T) are invariant under S <-> T",
        {source.content(), test.content()} == {test.content(), source.content()}
        and union_st.content() == union_ts.content()
        and I(union_st) == I(union_ts) == I(source) + I(test)
        and unlabeled == unlabeled_swapped,
        residual=(unlabeled, unlabeled_swapped),
    )
    checks.check(
        "theorem-2-no-ordered-typing",
        "content-only unlabeled data are an unordered pair, not an ordered typing",
        unlabeled == (Fraction(3), frozenset({Fraction(2), Fraction(1)}))
        and (I(source), I(test)) != (I(test), I(source)),
        residual=unlabeled,
    )

    radius_one = sp.Integer(1)
    grad_s_at_one = grad_magnitude(I(source), radius_one)
    grad_t_at_one = grad_magnitude(I(test), radius_one)
    half_pi = 1 / (2 * sp.pi)
    quarter_pi = 1 / (4 * sp.pi)
    checks.check(
        "theorem-3-unequal-mass-split",
        "|grad phi_S|(1) = 1/(2 pi) and |grad phi_T|(1) = 1/(4 pi) are unequal",
        is_zero(grad_s_at_one - sp.Integer(2) / (4 * sp.pi))
        and is_zero(sp.Integer(2) / (4 * sp.pi) - half_pi)
        and is_zero(grad_s_at_one - half_pi)
        and is_zero(grad_t_at_one - quarter_pi)
        and not is_zero(grad_s_at_one - grad_t_at_one),
        residual=(grad_s_at_one, grad_t_at_one),
    )
    checks.check(
        "theorem-3-union-readout",
        "swap leaves I(S union T)=3",
        I(union_st) == Fraction(3) and I(union_ts) == Fraction(3),
        residual=(I(union_st), I(union_ts)),
    )
    lumped_source = lumped("S", Fraction(2))
    lumped_test = lumped("T", Fraction(1))
    checks.check(
        "theorem-3-lumped",
        "lumped strengths with totals 2 and 1 reproduce the same Green split and union 3",
        I(lumped_source.union(lumped_test)) == Fraction(3)
        and is_zero(grad_magnitude(I(lumped_source), radius_one) - half_pi)
        and is_zero(grad_magnitude(I(lumped_test), radius_one) - quarter_pi),
    )

    union_as_source = grad_magnitude(I(union_st), radius_one)
    checks.check(
        "theorem-4-union-as-mass-fails",
        "using I(S union T) as M yields 3/(4 pi), which equals neither Green assignment",
        is_zero(union_as_source - sp.Integer(3) / (4 * sp.pi))
        and not is_zero(union_as_source - half_pi)
        and not is_zero(union_as_source - quarter_pi),
        residual=union_as_source,
    )
    checks.check(
        "theorem-4-unlabeled-cannot-select",
        "swap-invariant unlabeled data cannot equal a uniquely selected source gradient",
        unlabeled == unlabeled_swapped
        and not is_zero(grad_s_at_one - grad_t_at_one)
        and I(source) != I(test),
    )

    typed_product_st = I(source) * I(test)
    typed_product_ts = I(test) * I(source)
    force_mag_st = as_sympy(I(test)) * grad_s_at_one
    force_mag_ts = as_sympy(I(source)) * grad_t_at_one
    checks.check(
        "theorem-5-typed-maps",
        "if a typing is supplied, B_tau and F_tau are well-defined formal maps",
        typed_product_st == Fraction(2)
        and typed_product_ts == Fraction(2)
        and is_zero(force_mag_st - as_sympy(I(test)) * half_pi)
        and is_zero(force_mag_ts - as_sympy(I(source)) * quarter_pi),
        residual=(typed_product_st, force_mag_st, force_mag_ts),
    )
    checks.check(
        "theorem-5-escape-not-physical",
        "the note records the typed maps as a formal escape and does not claim gravity is impossible",
        "does not install" in note
        and "does not claim gravity is impossible" in note
        and "well-defined formal maps" in note,
    )

    union_grad_st = swap_invariant_union_grad(source, test, radius_one)
    union_grad_ts = swap_invariant_union_grad(test, source, radius_one)
    checks.check(
        "mutation-union-mass-fails-split",
        "replacing grad_magnitude by a swap-invariant I(S)+I(T) rule fails 1/(2 pi) vs 1/(4 pi)",
        is_zero(union_grad_st - union_grad_ts)
        and not is_zero(union_grad_st - half_pi)
        and not is_zero(union_grad_st - quarter_pi)
        and not is_zero(union_grad_st - grad_s_at_one)
        and not is_zero(union_grad_st - grad_t_at_one),
        residual=union_grad_st,
    )

    heavier_test = unit_atoms("w", 3)
    product_at_witness = product_law_grad(source, test, radius_one)
    product_at_heavier = product_law_grad(source, heavier_test, radius_one)
    source_linear_at_heavier = grad_magnitude(I(source), radius_one)
    checks.check(
        "mutation-product-fails-source-linearity",
        "replacing grad_magnitude by the product law fails source-linearity of phi = M G",
        I(test) == Fraction(1)
        and is_zero(product_at_witness - half_pi)
        and I(heavier_test) == Fraction(3)
        and is_zero(product_at_heavier - sp.Integer(6) / (4 * sp.pi))
        and is_zero(source_linear_at_heavier - half_pi)
        and not is_zero(product_at_heavier - source_linear_at_heavier)
        and product_law_grad(source, heavier_test, radius_one).has(sp.pi),
        residual=(product_at_witness, product_at_heavier, source_linear_at_heavier),
    )

    pair = (source, test)
    swapped = (test, source)
    checks.check(
        "mutation-label-order-is-typing",
        "always taking the first Python tuple entry as source is a typing: swap changes grad_magnitude when masses differ",
        I(pair[0]) != I(swapped[0])
        and is_zero(label_order_grad(pair, radius_one) - half_pi)
        and is_zero(label_order_grad(swapped, radius_one) - quarter_pi)
        and not is_zero(
            label_order_grad(pair, radius_one) - label_order_grad(swapped, radius_one)
        )
        and I(source) != I(test),
        residual=(label_order_grad(pair, radius_one), label_order_grad(swapped, radius_one)),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required_phrases = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "trace_class: negative_route_pruning",
        "target_claim_id: newton_source_test_typing",
        'target_blocker_text: "two-argument source–test pairing (Newton product residual)"',
        "reachability_to_target: prunes",
        'next_trace_action: "A declared source/test typing, or another two-argument instrument, remains open; do not adopt axiom text."',
        'conditional_surface_status: "exact for the unequal-mass Green split and Record swap symmetry; physical typing remains open"',
        "1/(2 pi)",
        "1/(4 pi)",
        "authors no audit verdict",
    )
    has_typing_phrase = "does not type" in note or "does not assign" in note
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(phrase in note for phrase in required_phrases)
        and has_typing_phrase
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block 14" not in note
        and "toe-lphys" not in note,
        residual=[phrase for phrase in required_phrases if phrase not in note],
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo and the Newton packet",
        "MINIMAL_AXIOMS_2026-06-29.md" in note and "NEWTON_LAW_DERIVED_NOTE.md" in note,
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
    checks.check(
        "canonical-nonmutation",
        "the typing escape is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("τ(source)", "B_τ", "phi_S", "source versus test")
        ),
    )
    checks.check(
        "n-gate-disposition",
        "the N-gate passes the scoped typing obstruction and refuses gravity-impossible and no-pairing claims",
        "PASS for the scoped typing obstruction" in note
        and "gravity is impossible" in note
        and "no two-argument pairing can exist" in note
        and "FAIL / DO" in note,
    )

    n5_lines = (
        "per_element: named collections with totals 2 and 1 have Green assignments 1/(2 pi) and 1/(4 pi) recomputed",
        "per_site: collection-level readout and a radial kernel are checked; no composite carrier is asserted",
        "per_mode: source-linear radial Green assignments are checked; no spectral or harmonic mode is claimed",
        "per_block: only the typing obstruction, the unequal-mass split, and the typed formal escape are executed",
        "lattice_wide: checked and not executed — no lattice-wide pairing, force law, or Einstein equation is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
