#!/usr/bin/env python3
"""Exact integer checks: three-site Hilbert is C^8, not unital M_3.

Lattice+Qubit supply a one-site module C^2. The three-site tensor is
constructed by pairing basis vectors; its cardinality is computed, not
supplied. Matrix-algebra dimensions are counted from matrix units.
The false predicates 2**3 == 9 and 3|8 are required to fail.

No QCD, no PDG, no generation axiom, no runner cache.
"""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/THREE_QUBIT_HILBERT_IS_C8_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]


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


def normalize(text: str) -> str:
    return " ".join(text.split())


def tensor_basis(*factors: tuple) -> tuple:
    out = ((),)
    for factor in factors:
        out = tuple(left + (vec,) for left in out for vec in factor)
    return out


def matrix_units(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(n))


def divides(n: int, m: int) -> bool:
    return n != 0 and m % n == 0


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_n = normalize(note)
    axiom_n = normalize(axiom)

    site_basis = ((1, 0), (0, 1))
    site_dim = len(site_basis)
    checks.check(
        "one-site-module",
        "defining module of M_2(C) is C^2",
        site_dim == 2 and len(set(site_basis)) == 2,
    )

    h3_basis = tensor_basis(site_basis, site_basis, site_basis)
    h3_dim = len(h3_basis)
    two_cubed = site_dim * site_dim * site_dim
    checks.check(
        "theorem1-tensor-product",
        "dim H_3 is the product of three site dimensions",
        h3_dim == two_cubed and len(set(h3_basis)) == h3_dim,
    )
    checks.check(
        "theorem1-identity",
        "2**3 == 8",
        site_dim ** 3 == 8 and two_cubed == 8 and h3_dim == 8,
    )

    m3_units = matrix_units(3)
    m3_dim = len(m3_units)
    checks.check(
        "theorem2-m3-dim",
        "dim M_3 is the count of 3-by-3 matrix units",
        m3_dim == 3 * 3 and m3_dim == 9,
    )
    checks.check(
        "theorem2-m3-not-h3",
        "dim M_3 != dim H_3, so M_3 is not B(H_3)",
        m3_dim != h3_dim,
    )

    m8_units = matrix_units(h3_dim)
    m8_dim = len(m8_units)
    checks.check(
        "theorem2-m8-dim",
        "dim B(H_3) = dim H_3 times dim H_3",
        m8_dim == h3_dim * h3_dim and m8_dim == 64,
    )
    checks.check(
        "theorem2-m3-not-m8",
        "dim M_3 != dim M_8",
        m3_dim != m8_dim,
    )

    three_divides_eight = divides(3, h3_dim)
    checks.check(
        "theorem3-unital-nonembed",
        "3 does not divide 8, so unital M_3 does not sit in M_8",
        three_divides_eight is False and h3_dim == 8,
    )
    checks.check(
        "theorem3-native-tensor-exists",
        "the three-site Lattice+Qubit tensor is constructed and has dim 8",
        h3_dim == 8 and h3_dim != m3_dim,
    )

    mutation_cube_eq_nine = site_dim ** 3 == 9
    mutation_three_divides_eight = divides(3, 8)
    checks.check(
        "mutation-2-cubed-eq-9",
        "predicate 2**3 == 9 fails",
        mutation_cube_eq_nine is False,
    )
    checks.check(
        "mutation-3-divides-8",
        "predicate 3 divides 8 fails",
        mutation_three_divides_eight is False,
    )

    checks.check(
        "source-qubit-m2",
        "axiom memo names one-site M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "source-lattice-sites",
        "axiom memo names Lattice sites of Z^3",
        "Physical sites are the points of the cubic lattice `Z^3`" in axiom,
    )
    checks.check(
        "note-bounded-support",
        "note machine status is bounded-support",
        "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "note-type-split",
        "note displays the Hilbert-tensor versus unital-algebra type split",
        all(
            phrase in note_n
            for phrase in (
                "different types",
                "native tensor of sites",
                "Do not identify `C^8` with Standard Model generations",
                "Do not identify `M_3` with QCD",
            )
        ),
    )
    checks.check(
        "note-no-generation-axiom",
        "note refuses a generation axiom",
        "does not adopt a generation axiom" in note_n
        and "does not add a generation axiom" in note_n,
    )
    checks.check(
        "audit-inputs",
        "declared inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_QUBIT_HILBERT_IS_C8_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    # Keep axiom_n referenced so the normalized axiom text is load-bearing.
    checks.check(
        "axiom-qubit-normalized",
        "normalized axiom memo still carries the Qubit presentation",
        "algebraic presentation `M_2(C)`" in axiom_n
        or "algebraic presentation M_2(C)" in axiom_n,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
