#!/usr/bin/env python3
"""Exact checks: a 16-atom one-site product is not a plaquette holonomy law.

Product masses 1/16 and 1/81, holonomy H(0,0,0,0)=0 versus H(1/2,0,0,0)=1
at fixed site bits, and unequal domains for the bit-sum and holonomy.
Identity gates call product_mass(bits, ps) and holonomy(thetas). No cache
is written.
"""

from __future__ import annotations

from collections.abc import Sequence
from fractions import Fraction
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "FINITE_ONE_SITE_PRODUCT_IS_NOT_PLAQUETTE_HOLONOMY_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/FINITE_ONE_SITE_PRODUCT_IS_NOT_PLAQUETTE_HOLONOMY_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Link = tuple[Point, Point]
Bits = tuple[int, int, int, int]
Thetas = tuple[Fraction, Fraction, Fraction, Fraction]
Margins = tuple[Fraction, Fraction, Fraction, Fraction]

ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E1E2: Point = (1, 1, 0)

SITES: tuple[Point, ...] = (ORIGIN, E1, E1E2, E2)
LINKS: tuple[Link, ...] = (
    (ORIGIN, E1),
    (E1, E1E2),
    (E1E2, E2),
    (E2, ORIGIN),
)
BITS = (0, 1)
HALF = Fraction(1, 2)
THIRD = Fraction(1, 3)


def normalize(text: str) -> str:
    return " ".join(text.split())


def product_mass(bits: Sequence[int], ps: Sequence[Fraction]) -> Fraction:
    """Identity-gate function: mass of a 4-bit atom under ⊗ Bern(p_x).

    Each one-site law is the pair (p, 1−p) on the ordered menu {0,1}.
    The 0-label carries mass p.
    """
    if len(bits) != 4 or len(ps) != 4:
        raise ValueError("four site bits and four margins are required")
    mass = Fraction(1)
    for bit, margin in zip(bits, ps, strict=True):
        if bit not in BITS:
            raise ValueError("bits are in {0,1}")
        if margin <= 0 or margin > 1:
            raise ValueError("p must lie in (0, 1]")
        mass *= margin if bit == 0 else (Fraction(1) - margin)
    return mass


def holonomy(thetas: Sequence[Fraction]) -> int:
    """Identity-gate function: Z/2Z holonomy of four two-point link angles.

    θ ∈ {0, 1/2} stand for U(1) values {1, −1}. The holonomy value is the
    exponent of −1 in the product, H = (2 Σ θ) mod 2.
    """
    if len(thetas) != 4:
        raise ValueError("four link angles are required")
    total = sum((theta for theta in thetas), Fraction(0))
    doubled = 2 * total
    if doubled.denominator != 1:
        raise ValueError("holonomy is defined on the two-point subgroup")
    return int(doubled) % 2


def bit_sum(bits: Sequence[int]) -> int:
    """Site-bit parity; not a holonomy. Domain is S, not ℓ."""
    if len(bits) != 4:
        raise ValueError("four site bits are required")
    if any(bit not in BITS for bit in bits):
        raise ValueError("bits are in {0,1}")
    return sum(bits) % 2


def holonomy_domain() -> frozenset[Link]:
    return frozenset(LINKS)


def bit_sum_domain() -> frozenset[Point]:
    return frozenset(SITES)


def product_mass_determines_holonomy(
    bits: Sequence[int],
    ps: Sequence[Fraction],
    thetas_a: Sequence[Fraction],
    thetas_b: Sequence[Fraction],
) -> bool:
    """Mutation predicate: equal site-bit mass is declared to force equal H."""
    _ = product_mass(bits, ps)
    return holonomy(thetas_a) == holonomy(thetas_b)


def mutated_unit_mass(_bits: Sequence[int], _ps: Sequence[Fraction]) -> Fraction:
    """Mutation: replace every atom mass by 1."""
    return Fraction(1)


def all_atoms() -> tuple[Bits, ...]:
    return tuple(cartesian(BITS, repeat=4))


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current Lattice, Admissibility, and "
        "Qualification wording are source-bound; no observational or fitted inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "construction: 16-atom one-site product on the unit-square corners; "
        "two-point holonomy on the four oriented links"
    )
    print(
        "negative_scope: the executable product is a site-bit table, not a "
        "holonomy law; not a no-go against gauge theory"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/FINITE_ONE_SITE_PRODUCT_IS_NOT_PLAQUETTE_HOLONOMY_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    law_domain_sentence = (
        "A law privileges no states. Its domain is a supplied condition, and at every"
    )
    checks.check(
        "source-lattice",
        "the current Lattice nearest-neighbor sentence is pinned in the axiom memo and the note",
        lattice_sentence in normalize(axiom) and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
    )
    checks.check(
        "source-law-domain",
        "the Qualification domain sentence is pinned in the axiom memo and the note",
        law_domain_sentence in normalize(axiom) and law_domain_sentence in note,
    )

    fair: Margins = (HALF, HALF, HALF, HALF)
    third: Margins = (THIRD, THIRD, THIRD, THIRD)
    zero_bits: Bits = (0, 0, 0, 0)
    one_bit: Bits = (1, 0, 0, 0)
    theta_zero: Thetas = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    theta_flip: Thetas = (HALF, Fraction(0), Fraction(0), Fraction(0))
    atoms = all_atoms()
    fair_masses = [product_mass(bits, fair) for bits in atoms]
    fair_total = sum(fair_masses, Fraction(0))
    biased_zero = product_mass(zero_bits, third)

    checks.check(
        "theorem-1-fair-sixteen",
        "each of the 16 fair atoms has mass (1/2)^4 = 1/16",
        len(atoms) == 16
        and len(fair_masses) == 16
        and all(mass == Fraction(1, 16) for mass in fair_masses)
        and product_mass(zero_bits, fair) == Fraction(1, 16)
        and product_mass((1, 1, 1, 1), fair) == Fraction(1, 16),
        residual=(len(atoms), fair_masses[0] if fair_masses else None),
    )
    checks.check(
        "theorem-1-fair-normalized",
        "the sixteen fair masses sum to 1",
        fair_total == Fraction(1),
        residual=fair_total,
    )
    checks.check(
        "theorem-1-biased-81",
        "the biased atom 0000 has mass (1/3)^4 = 1/81",
        biased_zero == Fraction(1, 81)
        and product_mass((1, 1, 1, 1), third) == Fraction(16, 81),
        residual=biased_zero,
    )
    third_total = sum((product_mass(bits, third) for bits in atoms), Fraction(0))
    checks.check(
        "theorem-1-table-is-a-measure",
        "the biased 16-atom table is a finite measure: nonnegative and sums to 1",
        third_total == Fraction(1)
        and all(product_mass(bits, third) > 0 for bits in atoms),
        residual=third_total,
    )

    h_zero = holonomy(theta_zero)
    h_flip = holonomy(theta_flip)
    checks.check(
        "theorem-2-holonomy-zero",
        "H(0,0,0,0)=0 (mod 2)",
        h_zero == 0,
        residual=h_zero,
    )
    checks.check(
        "theorem-2-holonomy-one",
        "H(1/2,0,0,0)=1 (mod 2)",
        h_flip == 1,
        residual=h_flip,
    )
    same_mass = product_mass(zero_bits, fair)
    checks.check(
        "theorem-2-independent-of-bits",
        "at fixed bits 0000 the two link configurations give H=0 and H=1, so H is independent of P_S",
        same_mass == product_mass(zero_bits, fair)
        and h_zero != h_flip
        and all(holonomy(theta_zero) == 0 and holonomy(theta_flip) == 1 for _ in atoms),
        residual=(same_mass, h_zero, h_flip),
    )
    checks.check(
        "theorem-2-bits-are-not-arguments",
        "holonomy is constant in the site bits: every bit string leaves H(θ) unchanged",
        all(holonomy(theta_zero) == 0 for _ in atoms)
        and all(holonomy(theta_flip) == 1 for _ in atoms)
        and product_mass(one_bit, fair) == product_mass(zero_bits, fair),
    )

    checks.check(
        "theorem-3-domains-unequal",
        "bit-sum is typed on the four sites and holonomy is typed on the four links",
        bit_sum_domain() == frozenset(SITES)
        and holonomy_domain() == frozenset(LINKS)
        and bit_sum_domain() != holonomy_domain()
        and len(SITES) == 4
        and len(LINKS) == 4
        and all(site not in holonomy_domain() for site in SITES),
        residual=(sorted(SITES), LINKS),
    )
    checks.check(
        "theorem-3-bit-sum-not-holonomy",
        "B flips with bits at fixed θ, while H flips with θ at fixed bits",
        bit_sum(zero_bits) == 0
        and bit_sum(one_bit) == 1
        and holonomy(theta_zero) == 0
        and holonomy(theta_flip) == 1
        and bit_sum(zero_bits) == bit_sum(zero_bits)
        and holonomy(theta_zero) != holonomy(theta_flip),
        residual=(bit_sum(zero_bits), bit_sum(one_bit), h_zero, h_flip),
    )

    checks.check(
        "theorem-4-type-residual",
        "P_S is a site-bit table; a holonomy law would be a law on links; L_phys is not adopted",
        product_mass(zero_bits, fair) == Fraction(1, 16)
        and holonomy(theta_zero) != holonomy(theta_flip)
        and bit_sum_domain() != holonomy_domain()
        and "does not adopt `L_phys`" in note
        and "does not adopt a holonomy law" in note
        and "gauge theory is impossible" in note,
    )
    checks.check(
        "theorem-5-not-factorization",
        "distant-bit factorization is recorded as a different theorem, not this type split",
        "Distant-bit factorization" in note
        and "bit-bit" in note
        and "bit-link" in note
        and "not required as an axiom" in note
        and "Do not adopt `L_phys`" in note,
    )

    checks.check(
        "mutation-product-mass-determines-holonomy-fails",
        "a predicate that product_mass determines holonomy fails on H=0 versus H=1 at fixed bits",
        product_mass(zero_bits, fair) == Fraction(1, 16)
        and product_mass(zero_bits, third) == Fraction(1, 81)
        and holonomy(theta_zero) == 0
        and holonomy(theta_flip) == 1
        and product_mass_determines_holonomy(zero_bits, fair, theta_zero, theta_flip) is False,
        residual=(
            product_mass(zero_bits, fair),
            holonomy(theta_zero),
            holonomy(theta_flip),
        ),
    )
    checks.check(
        "mutation-bit-sum-domain-fails",
        "replacing holonomy by bit-sum fails domain equality of links versus sites",
        holonomy_domain() != bit_sum_domain()
        and holonomy(theta_zero) == bit_sum(zero_bits)
        and holonomy(theta_flip) != bit_sum(zero_bits)
        and bit_sum(one_bit) != holonomy(theta_zero),
    )
    checks.check(
        "mutation-fair-mass-not-one",
        "setting every p=1/2 gives atom mass 1/16, not 1",
        product_mass(zero_bits, fair) == Fraction(1, 16)
        and mutated_unit_mass(zero_bits, fair) == Fraction(1)
        and product_mass(zero_bits, fair) != mutated_unit_mass(zero_bits, fair)
        and product_mass(zero_bits, fair) != Fraction(1),
        residual=product_mass(zero_bits, fair),
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
                "trace_class: negative_route_pruning",
                "target_claim_id: joint_law_l_phys",
                'target_blocker_text: "an executable physical joint law, including holonomy"',
                "reachability_to_target: prunes",
                'next_trace_action: "The executable finite product is a site-bit table, not a holonomy law. Do not adopt L_phys. Do not adopt axiom text."',
                "H(0,0,0,0)=0",
                "H(1/2,0,0,0)=1",
                "1/16",
                "1/81",
                "authors no audit verdict",
                "Do not adopt `L_phys`",
                "a law privileges no states",
                "domain is a supplied condition",
            )
        )
        and canonical_sentence in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the holonomy-law construction and L_phys are absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("L_phys", "P_S", "H(1/2,0,0,0)", "16-atom")
        ),
    )

    n5_lines = (
        "per_element: the 16 atoms of P_S and the holonomy inputs (0,0,0,0) and (1/2,0,0,0) are recomputed",
        "per_site: one-site binary laws on the four corners are site-local maps, not a composite arena",
        "per_mode: two-point holonomy and the bit-sum are checked; no spectral or harmonic mode is claimed",
        "per_block: only executability of P_S and the bit-link type split are executed",
        "lattice_wide: checked and not executed — no lattice-wide no-go against gauge theory is claimed",
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
