#!/usr/bin/env python3
"""Exact integer checks: no unital M_3 inside a finite tensor of M_2.

Dimensions are reconstructed here from dim_C(M_k) = k^2 and
T_n = M_2^{otimes n} ≅ M_{2^n}. A unital *-hom M_k -> M_m exists iff k | m.
No QCD import. The C2-strong leftover is displayed and not adopted.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "QUBIT_TENSOR_COMPOSITE_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/QUBIT_TENSOR_COMPOSITE_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def dim_m2() -> int:
    """Complex dimension of A2 = M_2(C), reconstructed as 2 * 2."""
    return 2 * 2


def dim_m3() -> int:
    """Complex dimension of A3 = M_3(C), reconstructed as 3 * 3."""
    return 3 * 3


def matrix_size(n: int) -> int:
    """Matrix size d_n = 2^n of T_n ≅ M_{2^n}(C)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return 2**n


def three_never_divides_power_of_two(N: int) -> bool:
    """True iff 3 does not divide 2^n for every n in 1..N."""
    if N < 1:
        raise ValueError("N must be >= 1")
    return all(matrix_size(n) % 3 != 0 for n in range(1, N + 1))


def unital_hom_exists(k: int, m: int) -> bool:
    """Unital C-linear *-hom M_k(C) -> M_m(C) exists iff k divides m."""
    return m % k == 0


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
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; dimensions reconstructed from finite matrix algebras")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer remainder; no float, no QCD import")
    print("negative_scope: unital A3 -> T_n is refused; leftover not adopted")

    checks.check(
        "theorem1-dim-m2",
        "dim_C(A2) reconstructs as 4",
        dim_m2() == 4,
    )
    checks.check(
        "theorem1-dim-m3",
        "dim_C(A3) reconstructs as 9",
        dim_m3() == 9,
    )
    sizes = tuple(matrix_size(n) for n in (1, 2, 3, 4))
    checks.check(
        "theorem1-matrix-size",
        "d_n = 2^n for n=1,2,3,4 is (2, 4, 8, 16)",
        sizes == (2, 4, 8, 16),
    )
    checks.check(
        "theorem1-tensor-dimension",
        "dim_C(T_n) = d_n^2 = 4^n for n=1..4",
        all(matrix_size(n) ** 2 == 4**n for n in (1, 2, 3, 4)),
    )

    checks.check(
        "theorem2-remainders",
        "3 does not divide 2^n for each n in {1,2,3,4}",
        all(matrix_size(n) % 3 != 0 for n in (1, 2, 3, 4)),
    )
    checks.check(
        "theorem2-no-unital-hom",
        "no unital *-hom A3 -> T_n for n=1,2,3,4",
        all(not unital_hom_exists(3, matrix_size(n)) for n in (1, 2, 3, 4)),
    )

    checks.check(
        "theorem3-n8",
        "three_never_divides_power_of_two(8) holds",
        three_never_divides_power_of_two(8) is True,
    )
    checks.check(
        "theorem3-positive-control",
        "unital A2 -> T_n exists for n=1..8 because 2 divides 2^n",
        all(unital_hom_exists(2, matrix_size(n)) for n in range(1, 9)),
    )

    three_divides_some = any(matrix_size(n) % 3 == 0 for n in range(1, 9))
    checks.check(
        "mutation-three-divides",
        "predicate '3 divides 2^n for some n in 1..8' fails",
        three_divides_some is False,
    )
    checks.check(
        "mutation-dim-a3-eq-4",
        "predicate 'dim A3 = 4' fails",
        dim_m3() != 4,
    )

    required_status = (
        'hypothetical_axiom_status: "C2-strong tensor composite: local algebra M_2; '
        'physical object may be a finite tensor of sites; not adopted"',
        "actual_current_surface_status: bounded-support",
    )
    checks.check(
        "machine-status-contract",
        "note carries the required leftover status and bounded-support surface",
        all(phrase in note for phrase in required_status),
    )
    checks.check(
        "theorem4-c2-reading",
        "note displays that 'full means local only; composites allowed' does not make color expected",
        "full means local only; composites allowed" in note
        and "does **not** by itself make color an expected construction" in note
        and "A3 remains extra" in note,
    )
    checks.check(
        "live-qubit-nonmutation",
        "live axiom memo still states one-site M_2(C) and is not rewritten",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "Do not adopt a fifth axiom named color." in note
        and "Do not identify `A3` with QCD." in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/QUBIT_TENSOR_COMPOSITE_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and 'AUDIT_INPUT_PATHS = (\n    "docs/QUBIT_TENSOR_COMPOSITE_HAS_NO_UNITAL_M3_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in self_source,
    )
    qcd_module_load = ("from " + "qcd")
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and N1-N8 gate are source-visible; no QCD module load",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and qcd_module_load not in self_source.lower()
        and qcd_module_load not in note.lower(),
    )

    print("per_element: reconstructed dims 4 and 9 and matrix sizes 2,4,8,16")
    print("per_site: one-site A2 is M_2; A3 is a comparison algebra only")
    print("per_block: unital A3 -> T_n is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide color claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
