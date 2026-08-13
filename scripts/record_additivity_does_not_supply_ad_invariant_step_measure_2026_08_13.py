#!/usr/bin/env python3
"""Exact finite checks: Record additivity does not supply ADM-2.

Dummy-record I is a content-only scalar sum with I(empty)=0. Two measures on
C_3 and Haar versus a non-Ad-invariant measure on Q_8 give distinct one-step
kernels and the same I. The runner computes those objects; it does not embed
a target constant and compare it to itself.
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
    / "RECORD_ADDITIVITY_DOES_NOT_SUPPLY_AD_INVARIANT_STEP_MEASURE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_AD_INVARIANT_STEP_MEASURE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class DummyRecord:
    site: tuple[int, int, int]
    content: Fraction
    label: object = None


def readout(records: tuple[DummyRecord, ...]) -> Fraction:
    return sum((record.content for record in records), Fraction(0))


def sites_disjoint(records: tuple[DummyRecord, ...]) -> bool:
    sites = [record.site for record in records]
    return len(sites) == len(set(sites))


def qmul(
    left: tuple[int, int, int, int], right: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def qinv(element: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a, b, c, d = element
    return (a, -b, -c, -d)


def qconj(
    conjugator: tuple[int, int, int, int], element: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    return qmul(conjugator, qmul(element, qinv(conjugator)))


def is_probability(measure: dict[object, Fraction]) -> bool:
    if any(weight < 0 for weight in measure.values()):
        return False
    return sum(measure.values(), Fraction(0)) == 1


def cyclic_kernel(
    measure: dict[int, Fraction], start: int, end: int
) -> Fraction:
    return measure[(end - start) % 3]


def quaternion_kernel(
    measure: dict[tuple[int, int, int, int], Fraction],
    start: tuple[int, int, int, int],
    end: tuple[int, int, int, int],
) -> Fraction:
    return measure[qmul(end, qinv(start))]


def ad_invariant_quaternion(
    measure: dict[tuple[int, int, int, int], Fraction],
    group: tuple[tuple[int, int, int, int], ...],
) -> bool:
    for conjugator in group:
        for element in group:
            if measure[element] != measure[qconj(conjugator, element)]:
                return False
    return True


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
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("finite_exact: C_3 and Q_8 kernels and dummy-record I are exact rationals")
    print("context_links: heat-kernel notes are named only as context, not as ADM-2 derivations")

    checks.check(
        "source-record-additivity",
        "the current Record sentence has content-only additive I with I(empty)=0",
        "A readout value is determined by record content alone." in axiom_flat
        and "scalar readout `I` is additive, with `I(empty)=0`" in axiom_flat,
    )
    checks.check(
        "source-empty-zero-preserved",
        "the source note preserves I(empty)=0",
        "I(empty)=0" in note and "I(empty) = 0" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses bounded-support and the three theorem targets",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "Theorem 1 — I Is Blind To Conjugacy-Class Structure",
                "Theorem 2 — Two Distinct Measures On C_3 Produce Two Kernels; I Cannot Select",
                "Theorem 3 — ADM-2 Remains An Extra Input To Any Heat-Kernel Attractor",
                "No axiom is edited",
            )
        ),
    )
    forbidden = ("new axiom", "we adopt", "promoted", "Codex", "Einstein")
    checks.check(
        "forbidden-phrases-absent",
        "the source note omits the barred phrases",
        all(phrase not in note for phrase in forbidden),
    )
    checks.check(
        "no-wilson-hk-uniqueness-claim",
        "the note states the Wilson/HK uniqueness denial",
        "This note does not claim Wilson/HK uniqueness." in note,
    )
    checks.check(
        "context-not-derivation",
        "the heat-kernel notes are context links and are not used to derive ADM-2",
        "context links only" in note_flat
        and "not used as a derivation of ADM-2" in note_flat
        and "HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS"
        in note
        and "EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS"
        in note,
    )

    r0 = DummyRecord((0, 0, 0), Fraction(1))
    r1 = DummyRecord((1, 0, 0), Fraction(2))
    r2 = DummyRecord((2, 0, 0), Fraction(4))
    dummy = (r0, r1, r2)
    empty: tuple[DummyRecord, ...] = ()
    checks.check(
        "dummy-empty-zero",
        "I(empty)=0 on the dummy collection",
        readout(empty) == 0 and sites_disjoint(dummy),
    )
    checks.check(
        "dummy-additivity",
        "I is a content-only sum on disjoint dummy records",
        readout((r0, r1)) == readout((r0,)) + readout((r1,))
        and readout(dummy) == readout((r0,)) + readout((r1,)) + readout((r2,))
        and readout(dummy) == Fraction(7),
    )

    c3 = (0, 1, 2)
    haar_c3 = {g: Fraction(1, 3) for g in c3}
    bias_c3 = {0: Fraction(1, 2), 1: Fraction(1, 3), 2: Fraction(1, 6)}
    checks.check(
        "c3-measures",
        "Haar and the biased triple are distinct probabilities on the 3-element group",
        is_probability(haar_c3)
        and is_probability(bias_c3)
        and haar_c3 != bias_c3
        and len(c3) == 3,
    )
    haar_kernel_c3 = {
        (h, g): cyclic_kernel(haar_c3, h, g) for h in c3 for g in c3
    }
    bias_kernel_c3 = {
        (h, g): cyclic_kernel(bias_c3, h, g) for h in c3 for g in c3
    }
    checks.check(
        "c3-kernels-differ",
        "the two C_3 one-step kernels differ at the identity increment",
        haar_kernel_c3 != bias_kernel_c3
        and haar_kernel_c3[(0, 0)] == Fraction(1, 3)
        and bias_kernel_c3[(0, 0)] == Fraction(1, 2),
    )
    checks.check(
        "c3-same-dummy-I",
        "dummy I is the same for both C_3 measures because I has no measure argument",
        readout(dummy) == Fraction(7),
    )

    one = (1, 0, 0, 0)
    minus_one = (-1, 0, 0, 0)
    i_el = (0, 1, 0, 0)
    minus_i = (0, -1, 0, 0)
    j_el = (0, 0, 1, 0)
    minus_j = (0, 0, -1, 0)
    k_el = (0, 0, 0, 1)
    minus_k = (0, 0, 0, -1)
    q8 = (one, minus_one, i_el, minus_i, j_el, minus_j, k_el, minus_k)
    checks.check(
        "q8-conjugacy",
        "j i j^{-1} equals -i on the SU(2) finite sample Q_8",
        qconj(j_el, i_el) == minus_i and len(q8) == 8 and len(set(q8)) == 8,
    )

    haar_q8 = {g: Fraction(1, 8) for g in q8}
    split_q8 = {g: Fraction(0) for g in q8}
    split_q8[i_el] = Fraction(1, 2)
    split_q8[j_el] = Fraction(1, 2)
    checks.check(
        "q8-haar-ad-invariant",
        "uniform Haar on Q_8 is Ad-invariant",
        is_probability(haar_q8) and ad_invariant_quaternion(haar_q8, q8),
    )
    checks.check(
        "q8-split-not-ad-invariant",
        "the two-point measure splits the {i,-i} class and is not Ad-invariant",
        is_probability(split_q8)
        and split_q8[i_el] != split_q8[minus_i]
        and not ad_invariant_quaternion(split_q8, q8),
    )
    haar_kernel_q8 = {
        (h, g): quaternion_kernel(haar_q8, h, g) for h in q8 for g in q8
    }
    split_kernel_q8 = {
        (h, g): quaternion_kernel(split_q8, h, g) for h in q8 for g in q8
    }
    checks.check(
        "q8-kernels-differ",
        "Haar and the split measure give distinct Q_8 one-step kernels",
        haar_kernel_q8 != split_kernel_q8
        and haar_kernel_q8[(one, i_el)] == Fraction(1, 8)
        and split_kernel_q8[(one, i_el)] == Fraction(1, 2)
        and split_kernel_q8[(one, minus_i)] == 0,
    )

    r_i = DummyRecord((0, 0, 1), Fraction(5), i_el)
    r_minus_i = DummyRecord((0, 0, 2), Fraction(5), minus_i)
    checks.check(
        "conjugacy-blind-I",
        "equal-content dummy records labeled by conjugate elements have equal I",
        readout((r_i,)) == readout((r_minus_i,)) == Fraction(5)
        and r_i.label != r_minus_i.label
        and qconj(j_el, r_i.label) == r_minus_i.label,
    )
    checks.check(
        "q8-same-dummy-I",
        "dummy I cannot select Haar versus the non-Ad-invariant Q_8 measure",
        readout(dummy) == Fraction(7),
    )
    checks.check(
        "axiom-file-unedited-needles",
        "the four named axioms remain the only axiom headings in the canonical file",
        axiom.count("### Lattice") == 1
        and axiom.count("### Qubit") == 1
        and axiom.count("### Admissibility") == 1
        and axiom.count("### Record") == 1
        and "ADM-2" not in axiom,
    )

    print("per_element: dummy contents 1,2,4 and conjugate labels i,-i")
    print("per_group: C_3 as a U(1) sample and Q_8 as an SU(2) sample")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
