#!/usr/bin/env python3
"""Exact checks: Record additivity does not force the energy dictionary.

Declared shares invert to r=(1-w)/(2w). Equal-share, carrier-dimension, and
inverse-share maps disagree. I on the disjoint union is 1 at every w and
cannot select D_*. No cache is written.
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
    / "FORMATION_ENERGY_DICTIONARY_NOT_FORCED_BY_RECORD_ADDITIVITY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
JULY12_PATH = (
    ROOT
    / "docs"
    / "KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)

AUDIT_INPUT_PATHS = (
    "docs/FORMATION_ENERGY_DICTIONARY_NOT_FORCED_BY_RECORD_ADDITIVITY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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


def cell_s(weight: Fraction) -> Collection:
    return Collection((("s", weight),))


def cell_d(weight: Fraction) -> Collection:
    return Collection((("d", Fraction(1) - weight),))


def declared_shares(w: Fraction, e_tot: Fraction) -> tuple[Fraction, Fraction]:
    """Identity-gate function: D_*(w, E_tot) = (w E_tot, (1-w) E_tot)."""
    return (w * e_tot, (Fraction(1) - w) * e_tot)


def equal_shares(_w: Fraction, e_tot: Fraction) -> tuple[Fraction, Fraction]:
    """Rejector D_eq: (E_tot/2, E_tot/2)."""
    half = e_tot / 2
    return (half, half)


def dim_shares(_w: Fraction, e_tot: Fraction) -> tuple[Fraction, Fraction]:
    """Rejector D_dim: (E_tot/3, 2 E_tot/3)."""
    return (e_tot / 3, (2 * e_tot) / 3)


def inv_shares(w: Fraction, e_tot: Fraction) -> tuple[Fraction, Fraction]:
    """Rejector D_inv: ((1-w) E_tot, w E_tot)."""
    return ((Fraction(1) - w) * e_tot, w * e_tot)


def r_from_energies(e_s: Fraction, e_d: Fraction) -> Fraction:
    """Identity-gate function: r := E_d / (2 E_s)."""
    if e_s == 0:
        raise ZeroDivisionError("r_from_energies requires E_s > 0")
    return e_d / (2 * e_s)


def constant_half(_e_s: Fraction, _e_d: Fraction) -> Fraction:
    """Mutation of r_from_energies: ignore the energies and return 1/2."""
    return Fraction(1, 2)


def channel_from_shares(e_s: Fraction, e_d: Fraction) -> tuple[Fraction, Fraction]:
    """Invert the channel split: a^2 = E_s/3, |b|^2 = E_d/6."""
    return (e_s / 3, e_d / 6)


def declared_r(w: Fraction) -> Fraction:
    return (Fraction(1) - w) / (2 * w)


def inverse_r(w: Fraction) -> Fraction:
    return w / (2 * (Fraction(1) - w))


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
    july12 = JULY12_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    normalized_july12 = normalize(july12)

    print(
        "external_scientific_inputs: current Record additivity and the July 12 "
        "Residual Atom 2 declaration are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: only I-on-the-union as a selector of D_* is rejected; "
        "a later dynamics bridge remains live; no dictionary is claimed impossible"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and July 12 relocation note",
        AUDIT_INPUT_PATHS
        == (
            "docs/FORMATION_ENERGY_DICTIONARY_NOT_FORCED_BY_RECORD_ADDITIVITY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
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
        "source-residual-atom-2",
        "July 12 Residual Atom 2 names the identification as a declared modeling element not supplied by the Record axiom",
        "declared modeling element" in july12
        and "is not supplied by the Record axiom" in normalize(july12)
        and "E_s = w E_tot" in july12
        and "E_d = (1-w) E_tot" in july12
        and "Residual Atom" in july12,
    )

    # Residual Atom 2 is written as a numbered item, not the literal heading
    # "Residual Atom 2". Pin the actual Residual Atoms section and Atom 2 body.
    checks.check(
        "source-july12-atom-2-body",
        "July 12 Residual Atoms section contains the energy-dictionary declaration",
        "Residual Atoms" in july12
        and "The energy dictionary." in july12
        and "this note's own declared modeling element" in normalized_july12,
    )

    empty = Collection()
    checks.check(
        "empty-readout",
        "I(empty)=0",
        I(empty) == Fraction(0),
        residual=I(empty),
    )

    one = Fraction(1)
    w_third = Fraction(1, 3)
    w_half = Fraction(1, 2)
    lawful = (w_third, w_half)

    # Theorem 1 — declared solve via identity-gate functions.
    declared_images = {}
    for weight in lawful:
        e_s, e_d = declared_shares(weight, one)
        a2, b2 = channel_from_shares(e_s, e_d)
        ratio = r_from_energies(e_s, e_d)
        declared_images[weight] = ratio
        checks.check(
            "declared-channel-split",
            "3 a^2 and 6 |b|^2 recover the declared shares",
            3 * a2 == e_s and 6 * b2 == e_d and e_s + e_d == one,
            residual=(e_s, e_d, a2, b2),
        )
        checks.check(
            "declared-r-identity",
            "r_from_energies on declared_shares equals (1-w)/(2w) and |b|^2/a^2",
            ratio == declared_r(weight) == b2 / a2,
            residual=(ratio, declared_r(weight), b2 / a2),
        )
        inverted = one / (one + 2 * ratio)
        checks.check(
            "declared-inverse",
            "w = 1/(1+2r) inverts the declared image",
            inverted == weight,
            residual=(weight, inverted, ratio),
        )

    checks.check(
        "theorem-1-special-points",
        "declared_shares at w=1/3 gives r=1 and at w=1/2 gives r=1/2",
        declared_images[w_third] == one
        and declared_images[w_half] == w_half
        and declared_shares(w_third, one) == (w_third, Fraction(2, 3))
        and declared_shares(w_half, one) == (w_half, w_half),
        residual=declared_images,
    )
    checks.check(
        "theorem-1-amplitudes",
        "a^2 = w E_tot/3 and |b|^2 = (1-w) E_tot/6 at the two lawful w",
        channel_from_shares(*declared_shares(w_third, one))
        == (Fraction(1, 9), Fraction(1, 9))
        and channel_from_shares(*declared_shares(w_half, one))
        == (Fraction(1, 6), Fraction(1, 12)),
    )

    # Theorem 2 — alternative dictionaries.
    table = {
        "star": {weight: r_from_energies(*declared_shares(weight, one)) for weight in lawful},
        "eq": {weight: r_from_energies(*equal_shares(weight, one)) for weight in lawful},
        "dim": {weight: r_from_energies(*dim_shares(weight, one)) for weight in lawful},
        "inv": {weight: r_from_energies(*inv_shares(weight, one)) for weight in lawful},
    }
    checks.check(
        "theorem-2-table",
        "r table is 1 vs 1/2 for D_*, 1/2 constantly for D_eq, 1 constantly for D_dim, and 1/4 vs 1/2 for D_inv",
        table["star"] == {w_third: one, w_half: w_half}
        and table["eq"] == {w_third: Fraction(1, 2), w_half: Fraction(1, 2)}
        and table["dim"] == {w_third: one, w_half: one}
        and table["inv"] == {w_third: Fraction(1, 4), w_half: w_half}
        and equal_shares(w_third, one) == (w_half, w_half)
        and dim_shares(w_third, one) == (w_third, Fraction(2, 3))
        and inv_shares(w_third, one) == (Fraction(2, 3), w_third),
        residual=table,
    )
    checks.check(
        "theorem-2-not-bijections",
        "D_eq and D_dim are constant in w; D_inv equals D_* only at w=1/2",
        table["eq"][w_third] == table["eq"][w_half]
        and table["dim"][w_third] == table["dim"][w_half]
        and table["inv"][w_half] == table["star"][w_half]
        and table["inv"][w_third] != table["star"][w_third]
        and inverse_r(w_third) == Fraction(1, 4)
        and inverse_r(w_half) == w_half
        and declared_r(w_third) != inverse_r(w_third),
        residual=(table["eq"], table["dim"], table["inv"]),
    )

    # Theorem 3 — union scalar is constantly 1.
    union_values = []
    for weight in lawful:
        source = cell_s(weight)
        doublet = cell_d(weight)
        checks.check(
            "cells-disjoint",
            "the two formation cells are pairwise disjoint",
            source.disjoint(doublet),
        )
        union_values.append(I(source.union(doublet)))
        checks.check(
            "union-sum-only",
            "I({s,d}) equals I(s)+I(d) and equals 1",
            I(source.union(doublet)) == I(source) + I(doublet) == one,
            residual=(weight, I(source), I(doublet), I(source.union(doublet))),
        )
    checks.check(
        "theorem-3-union-constant",
        "I({s,d})=1 at both lawful w and cannot distinguish them",
        union_values == [one, one] and len(set(union_values)) == 1,
        residual=union_values,
    )
    checks.check(
        "theorem-3-cannot-match-declared",
        "the constant union scalar cannot equal the declared pair 1 and 1/2",
        len(set(union_values)) == 1
        and len({table["star"][w_third], table["star"][w_half]}) == 2
        and table["star"][w_third] != table["eq"][w_third],
        residual=(union_values, table["star"], table["eq"]),
    )

    # Theorem 4 — no function of I(union) equals declared r(w).
    checks.check(
        "theorem-4-no-function",
        "no function of the single scalar I({s,d}) equals declared r on {1/3,1/2}",
        len(set(union_values)) == 1 and table["star"][w_third] != table["star"][w_half],
        residual=(union_values, table["star"]),
    )

    # Identity-gate mutations.
    checks.check(
        "mutation-eq-fails-w-third",
        "replacing declared_shares by D_eq fails the w=1/3 => r=1 identity",
        r_from_energies(*declared_shares(w_third, one)) == one
        and r_from_energies(*equal_shares(w_third, one)) != one
        and r_from_energies(*equal_shares(w_third, one)) == Fraction(1, 2),
    )
    checks.check(
        "mutation-dim-fails-w-half",
        "replacing declared_shares by D_dim fails the w=1/2 => r=1/2 identity",
        r_from_energies(*declared_shares(w_half, one)) == w_half
        and r_from_energies(*dim_shares(w_half, one)) != w_half
        and r_from_energies(*dim_shares(w_half, one)) == one,
    )
    checks.check(
        "mutation-constant-r-fails-w-third",
        "replacing r_from_energies by the constant 1/2 fails the w=1/3 declared image",
        r_from_energies(*declared_shares(w_third, one)) == one
        and constant_half(*declared_shares(w_third, one)) == w_half
        and constant_half(*declared_shares(w_third, one))
        != r_from_energies(*declared_shares(w_third, one)),
    )

    checks.check(
        "note-preserves-empty",
        "the note records I(empty)=0",
        "I(empty)=0" in note,
    )
    checks.check(
        "note-preserves-additivity-sentence",
        "the note quotes the current Record additivity sentence",
        additivity_sentence in normalized_note,
    )
    checks.check(
        "note-pins-declared-modeling-element",
        "the note quotes Residual Atom 2 as a declared modeling element",
        "declared modeling element" in note
        and "is not supplied by the Record axiom" in note,
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo and the July 12 relocation note",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
        in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
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
                "target_claim_id: koide_energy_dictionary_r_from_w",
                "reachability_to_target: prunes",
                'next_trace_action: "A physical formation-to-energy bridge remains open; do not adopt the declared dictionary or axiom text."',
                'conditional_surface_status: "exact for alternative-dictionary rejectors and the I-union obstruction; a later dynamics bridge remains live"',
                "r=(1-w)/(2w)",
                "1/4",
                "not a physical energy dictionary",
                "authors no audit verdict",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block 13" not in note
        and "toe-lphys" not in note,
        residual=[line for line in other_retained.splitlines() if "retained" in line],
    )
    checks.check(
        "canonical-nonmutation",
        "the alternative dictionaries are absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("D_*", "D_eq", "D_dim", "D_inv", "r=(1-w)/(2w)")),
    )
    checks.check(
        "july12-declares-not-derives",
        "July 12 still presents the energy dictionary as a declared modeling element",
        "declared modeling element" in normalized_july12
        and "is not supplied by the Record axiom" in normalized_july12,
    )

    n5_lines = (
        "per_element: the two cells {s,d} and the four share maps are evaluated under r_from_energies and I(union)",
        "per_site: the statements are two-cell menu statements; no composite carrier is asserted",
        "per_mode: the channel split E_s=3 a^2, E_d=6 |b|^2 is checked; no spectral-mode exhaustion is claimed",
        "per_block: only the declared solve, alternative-dictionary table, and I-union obstruction are tested",
        "lattice_wide: checked and not executed — no lattice-wide formation law or energy dictionary is claimed",
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
