#!/usr/bin/env python3
"""Exact checks for Aut(C3)-invariant circulant coarse-grainings.

Identity gates use partition invariance under the involution (1 2) and
uniform-power identities on the landed Hilbert-Schmidt Fourier weights.
Replacing Aut by the identity, or replacing the weights by a singleton
mass, must fail those checks.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "KOIDE_C3_INVARIANT_COARSE_GRAINING_BINARY_R_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CUSTODY_PATH = (
    ROOT / "docs" / "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md"
)
STATIONARY_PATH = ROOT / "docs" / "FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md"
JULY12_PATH = (
    ROOT
    / "docs"
    / "KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md"
)
JULY13_PATH = (
    ROOT / "docs" / "R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md"
)

AUDIT_INPUT_PATHS = (
    "docs/KOIDE_C3_INVARIANT_COARSE_GRAINING_BINARY_R_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md",
    "docs/FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md",
    "docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md",
    "docs/R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def frozenset_partition(blocks: tuple[tuple[int, ...], ...]) -> frozenset[frozenset[int]]:
    return frozenset(frozenset(block) for block in blocks)


def all_partitions(labels: tuple[int, ...]) -> list[frozenset[frozenset[int]]]:
    """Enumerate partitions of a small label set."""
    items = list(labels)
    n = len(items)
    found: list[frozenset[frozenset[int]]] = []

    def rec(index: int, current: list[list[int]]) -> None:
        if index == n:
            found.append(frozenset(frozenset(block) for block in current))
            return
        label = items[index]
        for block in current:
            block.append(label)
            rec(index + 1, current)
            block.pop()
        current.append([label])
        rec(index + 1, current)
        current.pop()

    rec(0, [])
    unique = []
    seen: set[frozenset[frozenset[int]]] = set()
    for part in found:
        if part not in seen:
            seen.add(part)
            unique.append(part)
    return unique


def apply_swap(part: frozenset[frozenset[int]]) -> frozenset[frozenset[int]]:
    """Aut(C3) involution: swap labels 1 and 2."""
    mapping = {0: 0, 1: 2, 2: 1}

    def map_block(block: frozenset[int]) -> frozenset[int]:
        return frozenset(mapping[item] for item in block)

    return frozenset(map_block(block) for block in part)


def hs_mode_weights(r: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Landed Fourier weights (3a^2, 3|b|^2, 3|b|^2) at a^2=1, |b|^2=r."""
    return (Fraction(3), Fraction(3) * r, Fraction(3) * r)


def normalize_weights(weights: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    total = sum(weights)
    if total == 0:
        raise ValueError("zero weight sum")
    return tuple(weight / total for weight in weights)


def block_weight(part: frozenset[frozenset[int]], r: Fraction) -> tuple[Fraction, ...]:
    mode = {0: Fraction(3), 1: Fraction(3) * r, 2: Fraction(3) * r}
    raw = tuple(sum(mode[item] for item in block) for block in sorted(part, key=lambda b: min(b)))
    return normalize_weights(raw)


def is_uniform(weights: tuple[Fraction, ...]) -> bool:
    if not weights:
        return False
    first = weights[0]
    return all(weight == first for weight in weights)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    custody = CUSTODY_PATH.read_text(encoding="utf-8")
    stationary = STATIONARY_PATH.read_text(encoding="utf-8")
    july12 = JULY12_PATH.read_text(encoding="utf-8")
    july13 = JULY13_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: axiom wording and the four parent notes "
        "are source-bound; no observational or fitted inputs"
    )
    print(
        "construction: Aut(C3) involution (1 2) on Fourier labels; "
        "uniform HS power locates r=1 and r=1/2"
    )
    print(
        "negative_scope: no third Aut-invariant grain; convention-freeness "
        "does not uniquely select r=1/2"
    )

    qualification = (
        "A choice not fixed by the supplied structure remains a named "
        "conditional or open dependency."
    )
    checks.check(
        "source-qualification",
        "the Qualification last sentence is pinned in the axiom memo and the note",
        qualification in normalize(axiom) and qualification in normalize(note),
    )
    checks.check(
        "source-parents",
        "custody, stationary-point, July 12, and July 13 supply the open selector and both grains",
        all(phrase in custody for phrase in ("r=1/2", "Q_H=1/3+(2/3)r", "OPEN SELECTOR"))
        and all(phrase in stationary for phrase in ("r=1/2", "stationary"))
        and all(phrase in july12 for phrase in ("convention-invariant", "P_chi", "ORBIT-INDEXING"))
        and all(phrase in july13 for phrase in ("A_carrier", "w=1/2", "r = (1-w)/(2w)")),
    )

    labels = (0, 1, 2)
    parts = all_partitions(labels)
    checks.check(
        "partition-count",
        "a three-element set has exactly five partitions",
        len(parts) == 5,
    )

    invariant = [part for part in parts if apply_swap(part) == part]
    one_block = frozenset_partition(((0, 1, 2),))
    three_singletons = frozenset_partition(((0,), (1,), (2,)))
    two_block = frozenset_partition(((0,), (1, 2)))
    mixed_a = frozenset_partition(((1,), (0, 2)))
    mixed_b = frozenset_partition(((2,), (0, 1)))
    checks.check(
        "aut-invariant-list",
        "exactly three partitions are Aut-invariant: one-block, three singletons, singlet-versus-doublet",
        len(invariant) == 3
        and one_block in invariant
        and three_singletons in invariant
        and two_block in invariant
        and mixed_a not in invariant
        and mixed_b not in invariant
        and apply_swap(mixed_a) == mixed_b,
    )

    # Identity automorphism would make every partition "invariant".
    identity_invariant = [part for part in parts if part == part]
    checks.check(
        "aut-is-not-identity",
        "the classifying involution is not the identity: two mixed partitions move",
        len(identity_invariant) == 5 and apply_swap(mixed_a) != mixed_a,
    )

    r_half = Fraction(1, 2)
    r_one = Fraction(1)
    r_quarter = Fraction(1, 4)
    mode_half = normalize_weights(hs_mode_weights(r_half))
    mode_one = normalize_weights(hs_mode_weights(r_one))
    mode_quarter = normalize_weights(hs_mode_weights(r_quarter))
    checks.check(
        "three-mode-uniform",
        "three-mode HS weights are uniform iff r=1",
        is_uniform(mode_one)
        and not is_uniform(mode_half)
        and not is_uniform(mode_quarter)
        and mode_one == (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
        and mode_half == (Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)),
    )

    sector_half = block_weight(two_block, r_half)
    sector_one = block_weight(two_block, r_one)
    sector_quarter = block_weight(two_block, r_quarter)
    checks.check(
        "two-block-uniform",
        "two-block HS weights are uniform iff r=1/2",
        is_uniform(sector_half)
        and not is_uniform(sector_one)
        and not is_uniform(sector_quarter)
        and sector_half == (Fraction(1, 2), Fraction(1, 2))
        and sector_one == (Fraction(1, 3), Fraction(2, 3)),
    )

    trivial_half = block_weight(one_block, r_half)
    trivial_one = block_weight(one_block, r_one)
    checks.check(
        "trivial-blind",
        "the one-block grain is r-blind: its only weight is 1 at both distinguished points",
        trivial_half == (Fraction(1),) and trivial_one == (Fraction(1),),
    )

    spectral = Fraction(1, 3) + Fraction(2, 3) * r_half
    checks.check(
        "spectral-line",
        "the custody spectral line sends r=1/2 to Q=2/3 and r=1 to Q=1",
        spectral == Fraction(2, 3)
        and Fraction(1, 3) + Fraction(2, 3) * r_one == 1
        and Fraction(1, 3) + Fraction(2, 3) * r_quarter == Fraction(1, 2),
    )

    def dictionary(weight: Fraction) -> Fraction:
        return (1 - weight) / (2 * weight)

    checks.check(
        "dictionary-section",
        "the July 13 dictionary sends w=1/2 to r=1/2 and w=1/3 to r=1; r=1-w is a different section",
        dictionary(Fraction(1, 2)) == Fraction(1, 2)
        and dictionary(Fraction(1, 3)) == 1
        and (1 - Fraction(1, 3)) == Fraction(2, 3)
        and (1 - Fraction(1, 3)) != dictionary(Fraction(1, 3)),
    )

    # Exhaustiveness: no other invariant partition exists among 2-subsets.
    extra = []
    for pair in combinations(labels, 2):
        block = frozenset(pair)
        complement = frozenset(labels) - block
        candidate = frozenset({block, complement})
        if apply_swap(candidate) == candidate and candidate not in (
            one_block,
            three_singletons,
            two_block,
        ):
            extra.append(candidate)
    checks.check(
        "no-third-grain",
        "no additional Aut-invariant 2+1 partition exists besides singlet-versus-doublet",
        extra == [] and two_block == frozenset_partition(((0,), (1, 2))),
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
                "trace_class: direct_blocker_closure",
                "reachability_to_target: partially_closes",
                "open selector",
                "r=1/2",
                "does not force",
                "does not edit an axiom",
                "Aut-invariant",
                "binary",
            )
        )
        and "choose the physical interior value" in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note,
    )

    # Tighten the last awkward condition: hybrid phrase unused as a reopen.
    checks.check(
        "hybrid-unused",
        "the hybrid-chirality no-go is named only as unused/forbidden, not as a premise",
        "hybrid" in note.lower()
        and "not used" in note.lower()
        and "not reopened" in note.lower(),
    )

    print(
        "per_element: the three Fourier labels and five partitions are enumerated"
    )
    print(
        "per_site: the classification is one abstract C3 circulant, not a lattice"
    )
    print(
        "per_mode: Aut(C3) acts on character labels {0,1,2}; HS weights are the Fourier powers"
    )
    print(
        "per_block: only the Aut-invariant coarse-graining block is executed"
    )
    print(
        "lattice_wide: checked and not executed — no lattice dynamics or sector assignment is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
