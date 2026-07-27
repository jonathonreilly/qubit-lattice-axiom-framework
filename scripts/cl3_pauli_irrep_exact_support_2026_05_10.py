#!/usr/bin/env python3
"""Compact exact-algebra support for the Cl(3) Pauli-irrep certificate.

This module contains only deterministic Gaussian-rational algebra helpers and
the executable N1--N8 evidence renderer.  It is statically imported by the
primary runner so the restricted audit packet includes its complete source.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import itertools
from typing import Sequence

try:
    import sympy as sp
    from sympy import I, Matrix, Rational, eye, simplify, symbols, zeros
except ImportError:
    print("FAIL: sympy is required for exact algebra")
    raise SystemExit(1)


DIM = 8
PASS = 0
FAIL = 0
VERBOSE = False
CANONICAL_MASKS = (0, 1, 2, 4, 3, 5, 6, 7)
BASIS_NAME = {
    0: "1", 1: "g1", 2: "g2", 4: "g3",
    3: "g12", 5: "g13", 6: "g23", 7: "omega",
}
RESOLUTION_CLASSES = (
    "per_element", "per_site", "per_mode", "per_block", "lattice_wide",
)


@dataclass(frozen=True)
class ResolutionRecord:
    resolution_class: str
    disposition: str
    certificate: tuple[tuple[str, object], ...]
    description: str


@dataclass(frozen=True)
class NoGoRoute:
    route_id: str
    route_class: str
    mechanism: str
    attempt: str
    outcome: str
    honesty_marker: str
    closed: bool


def make_resolution_records(
    *,
    plus_kernel_dimension: int,
    minus_kernel_dimension: int,
    plus_real_rank: int,
    minus_real_rank: int,
    central_action_count: int,
    plus_ideal_dimension: int,
    minus_ideal_dimension: int,
    combined_map_rank: int,
) -> tuple[ResolutionRecord, ...]:
    return (
        ResolutionRecord(
            "per_element", "PROVED",
            (("plus_kernel_dimension", plus_kernel_dimension),
             ("minus_kernel_dimension", minus_kernel_dimension)),
            "per_element: both irreducible complex actions have computed "
            f"opposite-ideal kernel dimensions ({plus_kernel_dimension},"
            f"{minus_kernel_dimension}).",
        ),
        ResolutionRecord(
            "per_site", "ABSTRACT_COPY_ONLY",
            (("plus_real_rank", plus_real_rank),
             ("minus_real_rank", minus_real_rank)),
            "per_site: one abstract real Cl(3,0) copy has exact image ranks "
            f"({plus_real_rank},{minus_real_rank}); no physical site is identified.",
        ),
        ResolutionRecord(
            "per_mode", "PROVED",
            (("central_action_count", central_action_count),),
            "per_mode: the central-action solve has exactly "
            f"{central_action_count} characters and a simple module selects one.",
        ),
        ResolutionRecord(
            "per_block", "PROVED",
            (("plus_ideal_dimension", plus_ideal_dimension),
             ("minus_ideal_dimension", minus_ideal_dimension),
             ("combined_map_rank", combined_map_rank)),
            "per_block: central-block dimensions are "
            f"({plus_ideal_dimension},{minus_ideal_dimension}); stacked rank is "
            f"{combined_map_rank}, while each irrep kills the other block.",
        ),
        ResolutionRecord(
            "lattice_wide", "NOT_TESTED_OUT_OF_SCOPE",
            (("resolution_tested", False), ("lattice_wide_claim_made", False)),
            "lattice_wide: NOT TESTED and outside this abstract one-algebra "
            "theorem; no lattice-wide negative assertion is made.",
        ),
    )


def resolution_records_valid(records: Sequence[ResolutionRecord]) -> bool:
    names = tuple(record.resolution_class for record in records)
    dispositions = {
        "per_element": "PROVED",
        "per_site": "ABSTRACT_COPY_ONLY",
        "per_mode": "PROVED",
        "per_block": "PROVED",
        "lattice_wide": "NOT_TESTED_OUT_OF_SCOPE",
    }
    certificates = {
        "per_element": (
            ("plus_kernel_dimension", 4), ("minus_kernel_dimension", 4),
        ),
        "per_site": (("plus_real_rank", 8), ("minus_real_rank", 8)),
        "per_mode": (("central_action_count", 2),),
        "per_block": (
            ("plus_ideal_dimension", 4), ("minus_ideal_dimension", 4),
            ("combined_map_rank", 8),
        ),
        "lattice_wide": (
            ("resolution_tested", False), ("lattice_wide_claim_made", False),
        ),
    }
    return (
        names == RESOLUTION_CLASSES
        and len(set(names)) == len(RESOLUTION_CLASSES)
        and all(
            record.disposition == dispositions[record.resolution_class]
            and record.certificate == certificates[record.resolution_class]
            for record in records
        )
    )


def emit_development_no_go_evidence(
    *,
    routes: Sequence[NoGoRoute],
    resolutions: Sequence[ResolutionRecord],
    boundaries_scoped: bool,
    prior_witness_count: int,
    combined_map_rank: int,
    combined_module_reducible: bool,
    hermitian_refinement_closes: bool,
    standard_complex_kernel_dimension: int,
    local_echo_controls_closed: int,
) -> None:
    gates = (
        len(routes) >= 5,
        len({route.route_class for route in routes}) >= 5,
        all(route.closed for route in routes),
        resolution_records_valid(resolutions),
        boundaries_scoped,
        prior_witness_count == 0,
        combined_map_rank == DIM,
        combined_module_reducible,
        hermitian_refinement_closes,
        standard_complex_kernel_dimension == 4,
        local_echo_controls_closed >= 2,
    )
    if not all(gates):
        check("N1-N8 fail-closed executable evidence gate", False)
        return

    print("N1_N8_STATUS=PASS current_execution=true")
    for route in routes:
        print(
            "N1_ROUTE "
            f"id={route.route_id}; class={route.route_class}; "
            f"marker={route.honesty_marker}; closed={str(route.closed).lower()}; "
            f"mechanism={route.mechanism}; outcome={route.outcome}"
        )
    print(
        "N2_DISPOSITION open_walls=0; the two conclusions are separately "
        "computed exact boundaries, not unresolved conditions."
    )
    print(
        "N3_DISPOSITION inputs=displayed_Clifford_relations,finite_unital_"
        "complex_modules; Hermitian generators are explicit only in the "
        "conditional unitary refinement; no carrier or imported value enters."
    )
    print(
        f"N4_DISPOSITION prior_witnesses={prior_witness_count}; all five "
        "route families are ATTEMPTED in this execution."
    )
    for record in resolutions:
        print(f"N5_RESOLUTION {record.description}")
    print(
        "N6_DISPOSITION partial_closures=faithful_reducible_direct_sum,"
        "Hermitian_same_sign_unitary_refinement; neither changes the exact "
        "irreducible complex kernel boundary."
    )
    print(
        "N7_STEELMAN_ARGUMENT stack rho_plus and rho_minus to obtain a faithful "
        "complex representation, apparently defeating nonfaithfulness."
    )
    print(
        f"N7_STEELMAN_RESOLUTION combined_rank={combined_map_rank}; "
        "faithful=true; reducible=true; invariant_summand_dimensions=2,2; "
        "each irreducible kernel_dimension=4."
    )
    print(
        f"N8_DISPOSITION prior_witnesses=0; local analogous controls closed="
        f"{local_echo_controls_closed}; repository echo indexing remains "
        "audit-orchestrator-owned."
    )


def set_verbose(value: bool) -> None:
    global VERBOSE
    VERBOSE = value


def set_active_table(table: Sequence[Sequence[tuple[int, int]]]) -> None:
    global ACTIVE_TABLE
    ACTIVE_TABLE = table


def counts() -> tuple[int, int]:
    return PASS, FAIL


def check(label: str, result: object, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(result)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    if VERBOSE or not ok:
        suffix = f" ({detail})" if detail else ""
        print(f"[{'PASS' if ok else 'FAIL'} (A)] {label}{suffix}")
    return ok


def section(title: str) -> None:
    if VERBOSE:
        print(f"\n--- {title} ---")


def blade(mask: int) -> Matrix:
    return Matrix([sp.Integer(row == mask) for row in range(DIM)])


def blade_product(left_mask: int, right_mask: int) -> tuple[int, int]:
    swaps = sum(
        1
        for left_bit in range(3)
        if left_mask & (1 << left_bit)
        for right_bit in range(left_bit)
        if right_mask & (1 << right_bit)
    )
    return (-1 if swaps % 2 else 1), left_mask ^ right_mask


PRODUCT_TABLE = [
    [blade_product(left, right) for right in range(DIM)]
    for left in range(DIM)
]
ACTIVE_TABLE = PRODUCT_TABLE


def word_product(left_mask: int, right_mask: int) -> tuple[int, int]:
    word = [bit for bit in range(3) if left_mask & (1 << bit)]
    sign = 1
    for bit in range(3):
        if not right_mask & (1 << bit):
            continue
        if sum(present > bit for present in word) % 2:
            sign = -sign
        if bit in word:
            word.remove(bit)
        else:
            word.append(bit)
            word.sort()
    return sign, sum(1 << bit for bit in word)


WORD_PRODUCT_TABLE = [
    [word_product(left, right) for right in range(DIM)]
    for left in range(DIM)
]


def algebra_product(
    left: Matrix,
    right: Matrix,
    table: Sequence[Sequence[tuple[int, int]]] | None = None,
) -> Matrix:
    table = ACTIVE_TABLE if table is None else table
    out = zeros(DIM, 1)
    for left_mask, right_mask in itertools.product(range(DIM), repeat=2):
        sign, out_mask = table[left_mask][right_mask]
        out[out_mask] += sign * left[left_mask] * right[right_mask]
    return out.applyfunc(sp.expand)


def vector_eq(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[row] - right[row]) == 0 for row in range(left.rows)
    )


def matrix_eq(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[row, col] - right[row, col]) == 0
        for row, col in itertools.product(range(left.rows), range(left.cols))
    )


def vector_rank(vectors: Sequence[Matrix]) -> int:
    return Matrix.hstack(*vectors).rank() if vectors else 0


def same_span(left: Sequence[Matrix], right: Sequence[Matrix]) -> bool:
    return vector_rank(left) == vector_rank(right) == vector_rank([*left, *right])


def in_span(vector: Matrix, spanning_vectors: Sequence[Matrix]) -> bool:
    return vector_rank([*spanning_vectors, vector]) == vector_rank(spanning_vectors)


def matrix_coordinates(matrix: Matrix) -> Matrix:
    return Matrix(list(matrix))


def real_matrix_coordinates(matrix: Matrix) -> Matrix:
    coordinates = []
    for value in matrix:
        coordinates.extend(sp.expand_complex(value).as_real_imag())
    return Matrix(coordinates)


def representation_images(sign: int, pauli: Sequence[Matrix]) -> list[Matrix]:
    images = []
    for mask in range(DIM):
        image = eye(2)
        for bit in range(3):
            if mask & (1 << bit):
                image *= sign * pauli[bit]
        images.append(image.applyfunc(sp.expand))
    return images


def representation_of_vector(vector: Matrix, images: Sequence[Matrix]) -> Matrix:
    return sum(
        (vector[mask] * images[mask] for mask in range(DIM)), zeros(2)
    ).applyfunc(sp.expand)


def homomorphism_ok(
    images: Sequence[Matrix],
    table: Sequence[Sequence[tuple[int, int]]] | None = None,
) -> bool:
    table = ACTIVE_TABLE if table is None else table
    basis = [blade(mask) for mask in range(DIM)]
    return all(
        matrix_eq(
            representation_of_vector(
                algebra_product(basis[left], basis[right], table), images
            ),
            images[left] * images[right],
        )
        for left, right in itertools.product(range(DIM), repeat=2)
    )


def table_relations_ok(
    table: Sequence[Sequence[tuple[int, int]]],
    gammas: Sequence[Matrix],
    one: Matrix,
) -> bool:
    zero = zeros(DIM, 1)
    return all(
        vector_eq(
            algebra_product(left, right, table)
            + algebra_product(right, left, table),
            2 * one if i == j else zero,
        )
        for i, left in enumerate(gammas)
        for j, right in enumerate(gammas)
    )


def idempotent_axioms_ok(
    e_plus: Matrix,
    e_minus: Matrix,
    basis: Sequence[Matrix],
    one: Matrix,
) -> bool:
    zero = zeros(DIM, 1)
    return all(
        (
            vector_eq(e_plus + e_minus, one),
            vector_eq(algebra_product(e_plus, e_minus), zero),
            vector_eq(algebra_product(e_minus, e_plus), zero),
            vector_eq(algebra_product(e_plus, e_plus), e_plus),
            vector_eq(algebra_product(e_minus, e_minus), e_minus),
        )
    ) and all(
        vector_eq(algebra_product(e, item), algebra_product(item, e))
        for e in (e_plus, e_minus)
        for item in basis
    )


def ideal_basis(idempotent: Matrix, basis: Sequence[Matrix]) -> list[Matrix]:
    return Matrix.hstack(
        *(algebra_product(item, idempotent) for item in basis)
    ).columnspace()


def print_multiplication_table(
    table: Sequence[Sequence[tuple[int, int]]],
) -> None:
    if not VERBOSE:
        return
    print("Exact multiplication table (rows multiply columns):")
    print("         " + " ".join(f"{BASIS_NAME[m]:>7}" for m in CANONICAL_MASKS))
    for left in CANONICAL_MASKS:
        entries = []
        for right in CANONICAL_MASKS:
            sign, out = table[left][right]
            entries.append(("-" if sign < 0 else "") + BASIS_NAME[out])
        print(f"{BASIS_NAME[left]:>7} " + " ".join(f"{x:>7}" for x in entries))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
    )
    parser.add_argument(
        "--inject-failure",
        choices=(
            "wrong-multiplication-sign", "quotient-only-idempotents",
            "missing-ideal", "false-faithful-extension",
            "fake-one-dimensional-simple", "fake-extra-dimensional-simple",
            "chirality-merger", "unitary-without-hermitian",
            "missing-resolution-evidence", "stale-resolution-evidence",
            "reordered-resolution-evidence", "false-resolution-evidence",
        ),
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    if args.inject_failure and args.mode != "intentional-failure":
        parser.error("--inject-failure requires --mode intentional-failure")
    return args
