#!/usr/bin/env python3
"""Exact checks for Aut(C3)-invariant coefficient-channel partitions.

The classified labels are the group-algebra coefficient slots of a Hermitian
circulant, not its spectral PVM atoms.  Input fingerprints bind the current
axiom boundary and every load-bearing parent.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "KOIDE_C3_INVARIANT_COARSE_GRAINING_BINARY_R_SELECTOR_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CUSTODY_PATH = ROOT / "docs" / (
    "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md"
)
SPECTRUM_PATH = ROOT / "docs" / (
    "KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md"
)
FROBENIUS_PATH = ROOT / "docs" / (
    "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_"
    "THEOREM_NOTE_2026-05-10.md"
)

AUDIT_INPUT_PATHS = (
    "docs/KOIDE_C3_INVARIANT_COARSE_GRAINING_BINARY_R_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md",
    "docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md",
    "docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def freeze_partition(
    blocks: tuple[tuple[int, ...], ...],
) -> frozenset[frozenset[int]]:
    return frozenset(frozenset(block) for block in blocks)


def all_partitions(labels: tuple[int, ...]) -> list[frozenset[frozenset[int]]]:
    """Enumerate each set partition exactly once."""
    result: list[frozenset[frozenset[int]]] = []

    def visit(index: int, blocks: list[list[int]]) -> None:
        if index == len(labels):
            result.append(frozenset(frozenset(block) for block in blocks))
            return
        label = labels[index]
        for block in blocks:
            block.append(label)
            visit(index + 1, blocks)
            block.pop()
        blocks.append([label])
        visit(index + 1, blocks)
        blocks.pop()

    visit(0, [])
    return list(dict.fromkeys(result))


def swap_partition(
    partition: frozenset[frozenset[int]],
) -> frozenset[frozenset[int]]:
    action = {0: 0, 1: 2, 2: 1}
    return frozenset(
        frozenset(action[label] for label in block) for block in partition
    )


def aggregate(
    partition: frozenset[frozenset[int]], r_value: Fraction
) -> tuple[Fraction, ...]:
    powers = {0: Fraction(1), 1: r_value, 2: r_value}
    raw = tuple(
        sum(powers[label] for label in block)
        for block in sorted(partition, key=lambda block: min(block))
    )
    total = sum(raw)
    return tuple(value / total for value in raw)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    custody = CUSTODY_PATH.read_text(encoding="utf-8")
    spectrum = SPECTRUM_PATH.read_text(encoding="utf-8")
    frobenius = FROBENIUS_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current axiom wording plus three "
        "source-bound algebra/custody parents; no fitted inputs"
    )
    print(
        "construction: setwise Aut(C3) action on group-algebra coefficient "
        "labels, followed by fixed-partition Shannon uniformity"
    )
    print(
        "negative_scope: no additional nontrivial invariant set partition; "
        "no broad physical-selector or arbitrary-kernel no-go"
    )

    qualification = (
        "A choice not fixed by the supplied structure remains a named "
        "conditional or open dependency."
    )
    record_content = (
        "Only records are readable. A readout value is determined by record "
        "content alone. A site with no record cannot be read."
    )
    checks.check(
        "current-axiom-boundary",
        "Qualification and the content-only/no-record Record boundary are pinned",
        qualification in normalize(axiom)
        and qualification in normalize(note)
        and record_content in normalize(axiom)
        and all(
            phrase in normalize(note)
            for phrase in (
                "readout depends on record content alone",
                "a site with no record cannot be read",
                "finite additivity",
            )
        ),
    )
    checks.check(
        "obsolete-record-semantics-excluded",
        "the theorem imports no named scalar, additivity, or absence value",
        "finite additivity, or a value at absence" in note
        and "Record does not choose" in note,
    )

    checks.check(
        "spectrum-parent",
        "the normalized coefficient identities and Parseval relation are source-bound",
        all(
            phrase in spectrum
            for phrase in (
                "a_0 = sqrt(3) a",
                "z   = sqrt(3) b",
                "lambda_0^2 + lambda_1^2 + lambda_2^2 = a_0^2 + 2|z|^2",
            )
        ),
    )
    checks.check(
        "frobenius-parent",
        "the real-isotype powers 3a^2 and 6|b|^2 are source-bound",
        all(
            phrase in frobenius
            for phrase in (
                "pi_+(H)    :=  (tr H / 3) I  =  a I",
                "E_+(H)    :=  || pi_+(H) ||_F^2     =  3 a^2",
                "E_perp(H) :=  || pi_perp(H) ||_F^2  =  6 |b|^2",
                "circulant coefficient modes, not literal conjugation",
            )
        ),
    )
    checks.check(
        "custody-parent",
        "the Q(r) line and open selector are source-bound",
        all(
            phrase in custody
            for phrase in ("Q_H=1/3+(2/3)r", "OPEN SELECTOR", "r=1/2")
        ),
    )

    labels = (0, 1, 2)
    partitions = all_partitions(labels)
    one = freeze_partition(((0, 1, 2),))
    three = freeze_partition(((0,), (1,), (2,)))
    two = freeze_partition(((0,), (1, 2)))
    mixed_left = freeze_partition(((1,), (0, 2)))
    mixed_right = freeze_partition(((2,), (0, 1)))
    invariant = {
        partition
        for partition in partitions
        if swap_partition(partition) == partition
    }
    checks.check(
        "partition-exhaustion",
        "a three-element set has exactly the five enumerated partitions",
        len(partitions) == 5
        and set(partitions) == {one, three, two, mixed_left, mixed_right},
    )
    checks.check(
        "setwise-invariant-list",
        "exactly one-block, three-singletons, and singlet/doublet survive",
        invariant == {one, three, two}
        and swap_partition(mixed_left) == mixed_right,
    )
    blockwise = {
        partition
        for partition in partitions
        if all(
            frozenset({0: 0, 1: 2, 2: 1}[item] for item in block) == block
            for block in partition
        )
    }
    checks.check(
        "definition-sensitivity",
        "stronger blockwise invariance excludes the three-singleton partition",
        blockwise == {one, two} and three not in blockwise,
    )

    r = sp.symbols("r", nonnegative=True)
    checks.check(
        "three-channel-iff",
        "three coefficient powers are equal if and only if r=1",
        sp.solve([sp.Eq(1, r), sp.Eq(r, r)], [r], dict=True)
        == [{r: sp.Integer(1)}],
    )
    checks.check(
        "two-block-iff",
        "the trivial/doublet aggregate powers are equal if and only if r=1/2",
        sp.solve([sp.Eq(1, 2 * r)], [r], dict=True)
        == [{r: sp.Rational(1, 2)}],
    )
    checks.check(
        "normalized-points",
        "the two fixed-partition uniform vectors and r-blind one-block are exact",
        aggregate(three, Fraction(1))
        == (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
        and aggregate(two, Fraction(1, 2))
        == (Fraction(1, 2), Fraction(1, 2))
        and aggregate(one, Fraction(1, 7)) == (Fraction(1),),
    )
    checks.check(
        "global-entropy-boundary",
        "the fixed-partition maxima log(3) and log(2) are not a tied binary optimum",
        sp.log(3) > sp.log(2),
    )

    # At a=b=1, coefficient powers are (3,3,3), while H has spectral
    # eigenvalues (3,0,0). This exact witness forbids the submitted semantic
    # identification of coefficient slots with spectral PVM atoms.
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    h_witness = sp.eye(3) + cycle + cycle**2
    spectral_powers = sorted(
        [value**2 for value, multiplicity in h_witness.eigenvals().items() for _ in range(multiplicity)],
        key=str,
    )
    checks.check(
        "coefficient-is-not-spectral",
        "uniform coefficient powers need not be uniform eigenvalue/PVM powers",
        spectral_powers == [sp.Integer(0), sp.Integer(0), sp.Integer(9)]
        and spectral_powers != [sp.Integer(3)] * 3
        and "not the three spectral-projector atoms" in note,
    )

    checks.check(
        "dependency-boundary",
        "spectral, Frobenius, custody, and minimal-axiom inputs are load-bearing; adjacent chains are not",
        all(
            dependency in note
            for dependency in (
                "koide_kappa_spectrum_operator_bridge_theorem_note_2026-04-19",
                "koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10",
                "charged_lepton_koide_value_full_chain_of_custody_2026-06-02",
                "minimal_axioms",
            )
        )
        and "no load-bearing dependency" in note,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    prose_without_fields = note
    for line in allowed_retained:
        prose_without_fields = prose_without_fields.replace(line, "")
    checks.check(
        "note-contract",
        "bounded status, no-edit boundary, scope correction, and audit hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: upstream_support",
                "reachability_to_target: supports",
                'hypothetical_axiom_status: "no edit"',
                "not a binary physical selector",
                "physical charged-lepton value `r=1/2` remains open",
                "No-Go Discipline Gate",
            )
        )
        and retained_ok
        and "retained" not in prose_without_fields
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "Codex" not in note,
    )

    print(
        "per_element: all three coefficient labels and all five set partitions are enumerated"
    )
    print(
        "per_site: one abstract circulant is checked; no lattice-site statement is inferred"
    )
    print(
        "per_mode: spectral eigenmodes are explicitly separated from coefficient channels"
    )
    print(
        "per_block: setwise invariance and fixed-partition aggregation are checked exactly"
    )
    print(
        "lattice_wide: no lattice dynamics, formation process, or sector assignment is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
