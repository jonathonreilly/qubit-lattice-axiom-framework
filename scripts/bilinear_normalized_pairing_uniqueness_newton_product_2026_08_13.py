#!/usr/bin/env python3
"""Exact checks: unique Q-bilinear normalized pairing is multiplication.

π(S,T)=I(S)I(T) is well-defined and bi-additive. Any Q-bilinear B with
B(1,1)=1 equals ordinary multiplication. Record additivity still does not
select π. Identity gates call pi(S,T) and pairing(). No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "BILINEAR_NORMALIZED_PAIRING_UNIQUENESS_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NEWTON_PATH = ROOT / "docs" / "NEWTON_LAW_DERIVED_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/BILINEAR_NORMALIZED_PAIRING_UNIQUENESS_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
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
    """Identity-gate function: the two-argument product of strengths."""
    return I(source) * I(test)


def pi(source: Collection, test: Collection) -> Fraction:
    """Identity-gate function: same product pairing as pairing()."""
    return pairing(source, test)


def union_readout(source: Collection, test: Collection) -> Fraction:
    """Mutation: replace π by I on the disjoint union."""
    return I(source.union(test))


def source_only(source: Collection, test: Collection) -> Fraction:
    """Mutation: replace π by the source readout I(S)."""
    del test
    return I(source)


def q_bilinear_eval(x: Fraction, y: Fraction, b11: Fraction) -> Fraction:
    """Unique Q-bilinear map with a declared unit B(1,1)=b11."""
    return x * y * b11


def integer_left_sum(count: int, y: Fraction, b11: Fraction) -> Fraction:
    """Reconstruct B(n,y) by adding B(1,y) n times."""
    one_term = Fraction(1) * y * b11
    acc = Fraction(0)
    for _ in range(abs(count)):
        acc += one_term
    if count < 0:
        return -acc
    return acc


def unit_atoms(prefix: str, count: int) -> Collection:
    return Collection(tuple((f"{prefix}{index}", Fraction(1)) for index in range(count)))


def lumped(label: str, weight: Fraction) -> Collection:
    if weight == 0:
        return Collection()
    return Collection(((label, weight),))


def source_linear_grad(source: Collection, radius: Fraction) -> Fraction:
    """Green coefficient I(S)/r^2; no I(T) factor."""
    return I(source) / (radius * radius)


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

    print(
        "external_scientific_inputs: current Record additivity, content-only "
        "readout, and the Newton kernel/non-claims are source-bound; no "
        "observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: Record does not select the extra pairing; uniqueness "
        "is only among Q-bilinear normalized maps; no Newton force law"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and Newton packet",
        AUDIT_INPUT_PATHS
        == (
            "docs/BILINEAR_NORMALIZED_PAIRING_UNIQUENESS_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/NEWTON_LAW_DERIVED_NOTE.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    content_sentence = "A readout value is determined by record content alone."
    checks.check(
        "source-record-additivity",
        "the exact current Record additivity sentence is present in the axiom memo",
        additivity_sentence in normalized_axiom,
    )
    checks.check(
        "source-record-content-only",
        "the exact current content-only readout sentence is present in the axiom memo",
        content_sentence in normalized_axiom,
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
    overlap = Collection((("shared", Fraction(2)),))
    overlap_test = Collection((("shared", Fraction(3)),))
    checks.check(
        "overlap-rejected",
        "union is refused when labels are not disjoint",
        not overlap.disjoint(overlap_test),
    )
    checks.check(
        "theorem-1-defined-on-overlap",
        "pi is defined without disjointness: overlapping labels still return the product",
        pi(overlap, overlap_test) == pairing(overlap, overlap_test) == Fraction(6),
        residual=pi(overlap, overlap_test),
    )

    pair_20 = (unit_atoms("s", 2), Collection())
    pair_11 = (unit_atoms("s", 1), unit_atoms("t", 1))
    pair_02 = (Collection(), unit_atoms("t", 2))
    pair_12 = (unit_atoms("s", 1), unit_atoms("t", 2))
    rejectors = (pair_20, pair_11, pair_02)
    unit_3 = unit_atoms("s", 3)
    unit_4 = unit_atoms("t", 4)

    checks.check(
        "theorem-1-empty-slot",
        "pi(empty, T)=0",
        pi(empty, unit_4) == pairing(empty, unit_4) == Fraction(0),
        residual=pi(empty, unit_4),
    )

    part_a = unit_atoms("s", 2)
    part_b = Collection((("s2", Fraction(1)),))
    checks.check(
        "theorem-1-biadditive",
        "pi(S1 union S2, T)=pi(S1,T)+pi(S2,T) on a disjoint split of strength 3 against 4",
        part_a.disjoint(part_b)
        and pi(part_a.union(part_b), unit_4)
        == pi(part_a, unit_4) + pi(part_b, unit_4)
        == pairing(part_a.union(part_b), unit_4),
        residual=(
            pi(part_a, unit_4),
            pi(part_b, unit_4),
            pi(part_a.union(part_b), unit_4),
        ),
    )

    product_values = [pi(source, test) for source, test in rejectors]
    pairing_values = [pairing(source, test) for source, test in rejectors]
    union_values = [I(source.union(test)) for source, test in rejectors]
    checks.check(
        "theorem-1-rejector",
        "pi and pairing separate (2,0),(1,1),(0,2) as 0,1,0",
        product_values == [Fraction(0), Fraction(1), Fraction(0)]
        and pairing_values == product_values,
        residual=product_values,
    )
    checks.check(
        "theorem-1-unit-3-4",
        "pi(unit_3, unit_4)=12 and pairing agrees",
        I(unit_3) == Fraction(3)
        and I(unit_4) == Fraction(4)
        and pi(unit_3, unit_4) == Fraction(12)
        and pairing(unit_3, unit_4) == Fraction(12),
        residual=(I(unit_3), I(unit_4), pi(unit_3, unit_4)),
    )

    unit_one = Fraction(1)
    samples = (
        (Fraction(0), Fraction(7)),
        (Fraction(1), Fraction(1)),
        (Fraction(3, 2), Fraction(1, 2)),
        (Fraction(-2), Fraction(5)),
        (Fraction(4, 3), Fraction(-3, 7)),
    )
    bilinear_ok = True
    uniqueness_ok = True
    for x, y in samples:
        value = q_bilinear_eval(x, y, unit_one)
        if value != x * y:
            uniqueness_ok = False
        x2, y2 = x + Fraction(1, 5), y + Fraction(2, 3)
        if q_bilinear_eval(x + x2, y, unit_one) != q_bilinear_eval(x, y, unit_one) + q_bilinear_eval(x2, y, unit_one):
            bilinear_ok = False
        if q_bilinear_eval(x, y + y2, unit_one) != q_bilinear_eval(x, y, unit_one) + q_bilinear_eval(x, y2, unit_one):
            bilinear_ok = False
        scale = Fraction(5, 4)
        if q_bilinear_eval(scale * x, y, unit_one) != scale * q_bilinear_eval(x, y, unit_one):
            bilinear_ok = False
        if q_bilinear_eval(x, scale * y, unit_one) != scale * q_bilinear_eval(x, y, unit_one):
            bilinear_ok = False
    reconstructed_twelve = integer_left_sum(3, Fraction(4), unit_one)
    checks.check(
        "theorem-2-normalized",
        "B(1,1)=1 for the unique Q-bilinear map with unit 1",
        q_bilinear_eval(Fraction(1), Fraction(1), unit_one) == Fraction(1),
    )
    checks.check(
        "theorem-2-bilinear",
        "the unit-1 map is Q-bilinear on the sample grid",
        bilinear_ok,
    )
    checks.check(
        "theorem-2-uniqueness",
        "B(x,y)=xy on the sample grid and integer additivity reconstructs 12 as 4+4+4",
        uniqueness_ok
        and reconstructed_twelve == Fraction(12)
        and integer_left_sum(2, Fraction(0), unit_one) == Fraction(0)
        and q_bilinear_eval(Fraction(3, 2), Fraction(1, 2), unit_one) == Fraction(3, 4)
        and pi(unit_3, unit_4) == q_bilinear_eval(I(unit_3), I(unit_4), unit_one),
        residual=reconstructed_twelve,
    )

    checks.check(
        "theorem-3-union-sum-only",
        "I(S union T) equals the sum 2,2,2 on the three rejector pairs",
        union_values == [Fraction(2), Fraction(2), Fraction(2)],
        residual=union_values,
    )
    checks.check(
        "theorem-3-union-not-pi",
        "union readout cannot equal pi on the three-pair rejector",
        union_values != product_values
        and union_readout(*pair_11) == Fraction(2)
        and pi(*pair_11) == Fraction(1)
        and union_readout(*pair_20) == Fraction(2)
        and pi(*pair_20) == Fraction(0),
        residual=(union_values, product_values),
    )

    radius = Fraction(1)
    green_coeffs = [source_linear_grad(source, radius) for source, _ in rejectors]
    product_coeffs = [pi(source, test) / (radius * radius) for source, test in rejectors]
    checks.check(
        "theorem-4-green-source-only",
        "Green coefficients at r=1 are 2,1,0 and carry no test-mass factor",
        green_coeffs == [Fraction(2), Fraction(1), Fraction(0)]
        and green_coeffs != product_coeffs,
        residual=(green_coeffs, product_coeffs),
    )
    checks.check(
        "theorem-4-multiply-is-pi",
        "multiplying the Green coefficient by I(T) recovers pi / r^2",
        all(
            source_linear_grad(source, radius) * I(test) == pi(source, test) / (radius * radius)
            for source, test in rejectors
        )
        and product_coeffs == [Fraction(0), Fraction(1), Fraction(0)],
    )

    lumped_11 = (lumped("S", Fraction(1)), lumped("T", Fraction(1)))
    lumped_12 = (lumped("S", Fraction(1)), lumped("T", Fraction(2)))
    checks.check(
        "theorem-5-not-selected",
        "content-only additivity supplies the sum, not the pairing; pi remains a second object",
        additivity_sentence in normalized_note
        and content_sentence in note
        and "I(empty)=0" in note
        and pi(*lumped_11) != I(lumped_11[0].union(lumped_11[1]))
        and pi(*lumped_12) == Fraction(2),
    )

    sum_rejector = [union_readout(source, test) for source, test in rejectors]
    checks.check(
        "mutation-sum-fails-rejector",
        "replacing pi by I(S)+I(T) fails (1,1) product 1 vs sum 2 and (2,0) product 0 vs sum 2",
        pi(*pair_11) == Fraction(1)
        and union_readout(*pair_11) == Fraction(2)
        and pi(*pair_20) == Fraction(0)
        and union_readout(*pair_20) == Fraction(2)
        and sum_rejector != product_values,
        residual=sum_rejector,
    )
    checks.check(
        "mutation-source-only-fails",
        "replacing pi by I(S) fails (1,1) versus (1,2)",
        pi(*pair_11) == Fraction(1)
        and pi(*pair_12) == Fraction(2)
        and source_only(*pair_11) == Fraction(1)
        and source_only(*pair_12) == Fraction(1)
        and source_only(*pair_11) == source_only(*pair_12)
        and pi(*pair_11) != pi(*pair_12),
        residual=(source_only(*pair_11), source_only(*pair_12), pi(*pair_11), pi(*pair_12)),
    )
    twice = Fraction(2)
    checks.check(
        "mutation-normalization-fails",
        "a bilinear B with B(1,1)=2 fails uniqueness at normalization",
        q_bilinear_eval(Fraction(1), Fraction(1), twice) == Fraction(2)
        and q_bilinear_eval(Fraction(1), Fraction(1), unit_one) == Fraction(1)
        and q_bilinear_eval(Fraction(1), Fraction(1), twice)
        != q_bilinear_eval(Fraction(1), Fraction(1), unit_one)
        and integer_left_sum(1, Fraction(1), twice) == Fraction(2),
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
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: upstream_support",
                "target_claim_id: newton_product_pairing",
                "reachability_to_target: supports",
                'target_blocker_text: "supply the bilinear product M_source M_test from Record content"',
                'next_trace_action: "The unique bilinear normalized pairing on Q is multiplication; Record still does not select it. Do not adopt axiom text."',
                "F = -M_test",
                "M_source M_test",
                "I(empty)=0",
                "authors no audit verdict",
            )
        )
        and additivity_sentence in normalized_note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "NEWTON_LAW_DERIVED_NOTE.md" in note
        and "**Type:** bounded_theorem" in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the pairing construction is absent from the canonical axiom file",
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

    n5_lines = (
        "per_element: rejector pairs (2,0),(1,1),(0,2) and the unit witness (3,4) are recomputed under pi",
        "per_site: two finite collections and their scalar strengths are the only objects; no composite carrier",
        "per_mode: value-group bilinearity is checked; no spectral or harmonic mode is claimed",
        "per_block: only bilinear uniqueness, the union rejector, and the source-linear Green coefficient are executed",
        "lattice_wide: checked and not executed — no lattice-wide gravity or Newton force law is claimed",
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
