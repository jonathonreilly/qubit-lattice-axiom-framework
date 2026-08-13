#!/usr/bin/env python3
"""Exact checks: the M_2 tensor/sum class hosts no unital M_3.

The runner computes matrix dimensions, tensor sizes, and integer remainders.
It does not adopt the generated class as a Qubit rewrite and does not import
QCD.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/M2_TENSOR_SUM_CLASS_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/M2_TENSOR_SUM_CLASS_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def dim_matrix(size: int) -> int:
    return size * size


def dim_m2() -> int:
    return dim_matrix(2)


def dim_m3() -> int:
    return dim_matrix(3)


def tensor_matrix_size(left: int, right: int) -> int:
    return left * right


def direct_sum_dim(sizes: tuple[int, ...]) -> int:
    return sum(dim_matrix(size) for size in sizes)


def is_power_of_two(value: int) -> bool:
    return value >= 2 and value.bit_count() == 1


def divides(divisor: int, dividend: int) -> bool:
    return dividend % divisor == 0


def unital_matrix_hom_exists(source_size: int, target_size: int) -> bool:
    return divides(source_size, target_size)


def unital_m3_into_summands(sizes: tuple[int, ...]) -> bool:
    return any(unital_matrix_hom_exists(3, size) for size in sizes)


def three_divides_some_power_of_two(k_max: int) -> bool:
    return any(divides(3, 2**k) for k in range(1, k_max + 1))


def m2_oplus_m2_isomorphic_to_m3() -> bool:
    return direct_sum_dim((2, 2)) == dim_m3()


def tensor_exponents(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a in left for b in right)


def sum_exponents(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return left + right


def sizes_from_exponents(exponents: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(2**k for k in exponents)


@dataclass(frozen=True)
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> "Checks":
        result = bool(condition)
        if result:
            object.__setattr__(self, "passed", self.passed + 1)
        else:
            object.__setattr__(self, "failed", self.failed + 1)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        return self

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )
    print(
        "negative_scope: unital M_3 into the generated tensor/sum class is "
        "rejected; a declared larger carrier remains a different type"
    )

    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-qubit",
        "the current Qubit sentence names M_2(C) as the one-site algebra",
        qubit_sentence in axiom,
    )

    d2 = dim_m2()
    d3 = dim_m3()
    checks.check(
        "identity-dims",
        f"dim_C(M_2)={d2} and dim_C(M_3)={d3}",
        d2 == 4 and d3 == 9,
    )

    gen = (1,)
    tensor_two = tensor_exponents(gen, gen)
    sum_two = sum_exponents(gen, gen)
    mixed = sum_exponents(tensor_two, gen)
    witnesses = (
        ("M_2", gen),
        ("M_2⊗M_2", tensor_two),
        ("M_2⊕M_2", sum_two),
        ("M_4⊕M_2", mixed),
    )
    witness_sizes = tuple(sizes_from_exponents(exponents) for _, exponents in witnesses)
    concatenated = tuple(size for sizes in witness_sizes for size in sizes)

    checks.check(
        "theorem1-tensor-witness",
        f"M_2⊗M_2 has size {tensor_matrix_size(2, 2)} and exponents {tensor_two}",
        tensor_two == (2,) and tensor_matrix_size(2, 2) == 4 and witness_sizes[1] == (4,),
    )
    checks.check(
        "theorem1-sum-witnesses",
        f"M_2⊕M_2 dim={direct_sum_dim(witness_sizes[2])}; "
        f"M_4⊕M_2 dim={direct_sum_dim(witness_sizes[3])}",
        witness_sizes[2] == (2, 2)
        and witness_sizes[3] == (4, 2)
        and direct_sum_dim(witness_sizes[2]) == 8
        and direct_sum_dim(witness_sizes[3]) == 20,
    )
    checks.check(
        "theorem1-power-of-two-summands",
        f"concatenated summand sizes {concatenated} are powers of two",
        concatenated == (2, 4, 2, 2, 4, 2)
        and all(is_power_of_two(size) for size in concatenated),
    )

    listed = witness_sizes[0] + witness_sizes[1] + (witness_sizes[2][0],) + witness_sizes[3]
    checks.check(
        "theorem2-listed-sizes",
        f"3 divides none of listed sizes {listed}",
        listed == (2, 4, 2, 4, 2) and all(not divides(3, size) for size in listed),
    )
    checks.check(
        "theorem2-no-unital-m3",
        "no unital M_3 into any of the four witnesses",
        all(not unital_m3_into_summands(sizes) for sizes in witness_sizes),
    )

    k_max = 8
    remainders = tuple((2**k) % 3 for k in range(1, k_max + 1))
    checks.check(
        "theorem3-universal-division",
        f"3 divides none of 2^k for k=1..{k_max}; remainders={remainders}",
        all(rem != 0 for rem in remainders) and not three_divides_some_power_of_two(k_max),
    )
    checks.check(
        "theorem3-class-form",
        "every generated witness is a sum of M_{2^{k}} with k>=1",
        all(min(exponents) >= 1 for _, exponents in witnesses)
        and all(all(is_power_of_two(size) for size in sizes) for sizes in witness_sizes),
    )

    checks.check(
        "mutation-three-divides-power-of-two",
        "predicate '3 divides 2^k for some k=1..8' fails",
        three_divides_some_power_of_two(8) is False,
    )
    sum_dim = direct_sum_dim((2, 2))
    checks.check(
        "mutation-sum-not-m3",
        f"predicate 'M_2⊕M_2 ≅ M_3' fails ({sum_dim}!={d3})",
        m2_oplus_m2_isomorphic_to_m3() is False and sum_dim != d3,
    )

    required_status = (
        'hypothetical_axiom_status: "C2-strong: composites are the class '
        'generated from M_2 by finite tensor and finite direct sum; not adopted"',
        "actual_current_surface_status: bounded-support",
    )
    checks.check(
        "machine-status-contract",
        "the note carries the required C2-strong and bounded-support fields",
        all(phrase in note for phrase in required_status),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "non-adoption-surface",
        "the leftover declaration is displayed and QCD is refused",
        all(
            phrase in normalize(note)
            for phrase in (
                "declared larger carrier",
                "not adopted",
                "QCD is not imported",
                "Unital `M_3` is not an expected construction on this class",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )
    checks.check(
        "declared-inputs",
        "AUDIT_INPUT_PATHS names the new note and the axiom memo, both present",
        AUDIT_INPUT_PATHS
        == (
            "docs/M2_TENSOR_SUM_CLASS_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "canonical-nonmutation",
        "the generated class notation is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("S''", "generated class `C`", "M_{2^{k_1}}")),
    )

    print("per_element: four witnesses and the listed summand sizes {2,4,2,4,2}")
    print("per_site: local algebra remains M_2; no multi-site dynamics claimed")
    print("per_mode: k=1..8 powers of two checked against division by 3")
    print("per_block: unital M_3 into the generated tensor/sum class only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
