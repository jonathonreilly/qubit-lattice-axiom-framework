#!/usr/bin/env python3
"""Cycle 812 independent adversarial check of the W7 mixed-input ruling.

The seven declared sources are SHA-pinned text/AST evidence only.  In
particular, neither the Cycle-812 primary nor either Cycle-803 module is
imported or executed.  All exact algebra below is a stdlib reimplementation.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Iterable


STARTED = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024

# Literal worktree-relative packet: exactly seven files, all read as bytes/text.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle803_decoder_derivation_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
    AUDIT_INPUT_PATHS[1]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[2]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[3]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[4]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[5]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[6]:
        "df3287bd2aa0fdfc3361551894760f04d3ebb60ba6214fe83f005056e8aec0ab",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle812_mixed_input_response_2026_07_28",
    "frontier_cycle803_decoder_derivation_2026_07_28",
    "frontier_cycle803_decoder_independent_check_2026_07_28",
)

QUBITS = 15
HILBERT_DIMENSION = 1 << QUBITS
W7_DIMENSION = 6
OUTPUT_MASK = (1 << 6) - 1
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
REVERSE = (1, 0, 3, 2, 5, 4)

Gaussian = tuple[Fraction, Fraction]
Vector = tuple[Fraction, Fraction, Fraction]
Response = tuple[Vector, Vector, Vector]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def sha256_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def line_of(text: str, fragment: str) -> int:
    offset = text.find(fragment)
    if offset < 0:
        raise ValueError(f"missing defining fragment: {fragment!r}")
    return text.count("\n", 0, offset) + 1


def literal_input_paths() -> tuple[str, ...]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    if len(assignments) != 1 or not isinstance(assignments[0].value, ast.Tuple):
        return ()
    values = assignments[0].value.elts
    if not all(
        isinstance(node, ast.Constant) and isinstance(node.value, str)
        for node in values
    ):
        return ()
    return tuple(node.value for node in values)


def own_import_firewall() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    imports = tuple(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    )
    forbidden = tuple(
        name
        for name in imports
        if any(
            name == blocked or name.startswith(blocked + ".")
            for blocked in BLOCKLISTED_MODULES
        )
    )
    loaded = {
        name: name in sys.modules for name in BLOCKLISTED_MODULES
    }
    return {
        "forbidden_static_imports": forbidden,
        "sys_modules": loaded,
        "text_ast_only": not forbidden and not any(loaded.values()),
    }


def git_head(directory: Path) -> str:
    result = subprocess.run(
        ("git", "-C", str(directory), "rev-parse", "HEAD"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "UNAVAILABLE"


def read_source_packet() -> tuple[
    dict[str, bytes], dict[str, str], dict[str, ast.Module]
]:
    raw = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    texts = {path: data.decode("utf-8") for path, data in raw.items()}
    trees = {
        path: ast.parse(text, filename=path) for path, text in texts.items()
    }
    return raw, texts, trees


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one function {name!r}")
    return matches[0]


def source_evidence(
    raw: dict[str, bytes],
    texts: dict[str, str],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    citations = (
        (
            AUDIT_INPUT_PATHS[1],
            "recoil_coefficients=(Fraction(1), Fraction(1), Fraction(1))",
            "Cycle-749 identity pullback uses the unit recoil kernel",
        ),
        (
            AUDIT_INPUT_PATHS[2],
            'candidate_composition": "K=R*R=I"',
            "Cycle-768 derives the unit adjoint-pullback candidate",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "tuple(value / weight for value in matter)",
            "Cycle-771 conditions each pure-column response by branch weight",
        ),
        (
            AUDIT_INPUT_PATHS[4],
            "cross_term = coherent_probability - mixture_probability",
            "Cycle-774 computes the coherent cross term explicitly",
        ),
        (
            AUDIT_INPUT_PATHS[4],
            "(matter,mediator,auxiliary)=(REVERSE[d],d,d)",
            "Cycle-774 records disjoint branch support by source label",
        ),
        (
            AUDIT_INPUT_PATHS[5],
            "composition_row = add_response_rows(input_rows)",
            "Cycle-778 composes declared identity columns additively",
        ),
        (
            AUDIT_INPUT_PATHS[6],
            "return U320.LinkState({ORIGIN: vector}, {})",
            "Cycle-803 has a direction-to-basis-LinkState helper only",
        ),
        (
            AUDIT_INPUT_PATHS[6],
            "raise DecoderSemanticGap({",
            "Cycle-803's big-sector decoder candidate stops without a map",
        ),
    )
    decoder = named_function(
        trees[AUDIT_INPUT_PATHS[6]], "decode_companion_choi_to_linkstate"
    )
    decoder_returns = [
        node for node in ast.walk(decoder) if isinstance(node, ast.Return)
    ]
    decoder_raises = [
        node for node in ast.walk(decoder) if isinstance(node, ast.Raise)
    ]
    lineage_paths = AUDIT_INPUT_PATHS[1:]
    landed_transform_tokens = (
        "partial_trace",
        "trace_out",
        "ptrace",
        "postselect",
        "sector_restriction",
        "compress_to_linkstate",
    )
    token_hits = {
        path: tuple(
            token for token in landed_transform_tokens if token in texts[path]
        )
        for path in lineage_paths
    }
    return {
        "citations": tuple({
            "path": path,
            "line": line_of(texts[path], fragment),
            "defining_code": fragment,
            "meaning": meaning,
        } for path, fragment, meaning in citations),
        "lineage_big_to_six_transform_token_hits": token_hits,
        "cycle803_decoder_ast": {
            "function": decoder.name,
            "return_count": len(decoder_returns),
            "raise_count": len(decoder_raises),
            "constructs_a_map": bool(decoder_returns),
        },
        "lineage_finding": (
            "The corpus contains identity_link_state(direction), which maps a "
            "chosen W7 column label to a basis LinkState.  The only named "
            "Choi-to-LinkState decoder has no return and raises the rank/live-"
            "input gap.  No partial-trace, postselection, restriction, or "
            "compression map from the 15-qubit operator to C^6 is landed."
        ),
        "all_ast_modules": all(
            isinstance(tree, ast.Module) for tree in trees.values()
        ),
        "passed": (
            all(isinstance(tree, ast.Module) for tree in trees.values())
            and not decoder_returns
            and len(decoder_raises) >= 2
            and not any(token_hits.values())
        ),
    }


def fraction_rank(rows: Iterable[Iterable[Fraction]]) -> int:
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        owner = next(
            (
                row
                for row in range(pivot_row, row_count)
                if matrix[row][column]
            ),
            None,
        )
        if owner is None:
            continue
        matrix[pivot_row], matrix[owner] = (
            matrix[owner], matrix[pivot_row]
        )
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [
            value / pivot for value in matrix[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(
                    matrix[row], matrix[pivot_row]
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def gf2_rank(vectors: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for original in vectors:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def g_abs_squared(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def g_multiply_conjugate(left: Gaussian, right: Gaussian) -> Gaussian:
    # left * conjugate(right)
    return (
        left[0] * right[0] + left[1] * right[1],
        left[1] * right[0] - left[0] * right[1],
    )


def response_rows() -> tuple[Response, ...]:
    rows = []
    for direction in DIRECTIONS:
        vector = tuple(Fraction(value) for value in direction)
        rows.append((
            tuple(-2 * value for value in vector),
            vector,
            vector,
        ))
    return tuple(rows)  # type: ignore[return-value]


def zero_response() -> Response:
    zero = (Fraction(), Fraction(), Fraction())
    return zero, zero, zero


def add_scaled_response(
    output: list[list[Fraction]],
    coefficient: Fraction,
    row: Response,
) -> None:
    for component in range(3):
        for axis in range(3):
            output[component][axis] += coefficient * row[component][axis]


def freeze_response(output: list[list[Fraction]]) -> Response:
    return tuple(tuple(row) for row in output)  # type: ignore[return-value]


def w7_pure_functional(amplitudes: tuple[Gaussian, ...]) -> Response:
    """Independent exact rewrite of the W7 branch-conditioned response."""
    norm = sum((g_abs_squared(value) for value in amplitudes), Fraction())
    if not norm:
        raise ValueError("zero pure input")
    output = [[Fraction() for _axis in range(3)] for _component in range(3)]
    for amplitude, row in zip(amplitudes, response_rows()):
        add_scaled_response(output, g_abs_squared(amplitude) / norm, row)
    return freeze_response(output)


def pure_projector_coordinates(
    amplitudes: tuple[Gaussian, ...],
) -> tuple[Fraction, ...]:
    """Real coordinates of |c><c|/||c||^2 in Herm(6)."""
    norm = sum((g_abs_squared(value) for value in amplitudes), Fraction())
    if not norm:
        raise ValueError("zero pure input")
    pairs = tuple(
        (left, right)
        for left in range(W7_DIMENSION)
        for right in range(left + 1, W7_DIMENSION)
    )
    diagonal = tuple(g_abs_squared(value) / norm for value in amplitudes)
    off = tuple(
        g_multiply_conjugate(amplitudes[left], amplitudes[right])
        for left, right in pairs
    )
    return (
        diagonal
        + tuple(value[0] / norm for value in off)
        + tuple(value[1] / norm for value in off)
    )


def spanning_pure_inputs() -> tuple[
    tuple[str, tuple[Gaussian, ...]], ...
]:
    zero: Gaussian = (Fraction(), Fraction())
    one: Gaussian = (Fraction(1), Fraction())
    imaginary: Gaussian = (Fraction(), Fraction(1))
    rows = []
    for direction in range(W7_DIMENSION):
        values = [zero for _index in range(W7_DIMENSION)]
        values[direction] = one
        rows.append((f"e{direction}", tuple(values)))
    for left in range(W7_DIMENSION):
        for right in range(left + 1, W7_DIMENSION):
            values = [zero for _index in range(W7_DIMENSION)]
            values[left] = one
            values[right] = one
            rows.append((f"e{left}+e{right}", tuple(values)))
    for left in range(W7_DIMENSION):
        for right in range(left + 1, W7_DIMENSION):
            values = [zero for _index in range(W7_DIMENSION)]
            values[left] = one
            values[right] = imaginary
            rows.append((f"e{left}+i*e{right}", tuple(values)))
    return tuple(rows)


def trace_pure_against_kernel(
    amplitudes: tuple[Gaussian, ...],
    kernel: tuple[Response, ...],
) -> Response:
    """Tr(|c><c| K) for the independently reconstructed diagonal K."""
    norm = sum((g_abs_squared(value) for value in amplitudes), Fraction())
    output = [[Fraction() for _axis in range(3)] for _component in range(3)]
    for direction in range(W7_DIMENSION):
        coefficient = g_abs_squared(amplitudes[direction]) / norm
        add_scaled_response(output, coefficient, kernel[direction])
    return freeze_response(output)


def linearity_verification(evidence: dict[str, object]) -> dict[str, object]:
    kernel = response_rows()
    inputs = spanning_pure_inputs()
    coordinates = tuple(
        pure_projector_coordinates(amplitudes)
        for _label, amplitudes in inputs
    )
    comparisons = tuple(
        (
            label,
            w7_pure_functional(amplitudes),
            trace_pure_against_kernel(amplitudes, kernel),
        )
        for label, amplitudes in inputs
    )
    mismatches = tuple(
        label for label, direct, traced in comparisons if direct != traced
    )
    span_rank = fraction_rank(coordinates)
    reverse_odd = all(
        kernel[REVERSE[direction]][component][axis]
        == -kernel[direction][component][axis]
        for direction in range(W7_DIMENSION)
        for component in range(3)
        for axis in range(3)
    )
    return {
        "finding": (
            "F(rho)=Tr(rho K) exactly on the declared six-column scope; "
            "K is the nine-component diagonal operator with diagonal rows "
            "(-2d,+d,+d)."
        ),
        "K_diagonal_rows": kernel,
        "spanning_pure_input_count": len(inputs),
        "spanning_projector_rank_over_Q": span_rank,
        "Hermitian_C6_dimension": W7_DIMENSION * W7_DIMENSION,
        "comparison_mismatches": mismatches,
        "reverse_odd": reverse_odd,
        "source_reimplementation": (
            "Cycle-749 unit identity-pullback coefficients + Cycle-771 "
            "branch conditioning + Cycle-774 disjoint branch supports; no "
            "lineage module imported or executed"
        ),
        "source_citations": evidence["citations"],
        "passed": (
            evidence["passed"]
            and len(inputs) == 36
            and span_rank == 36
            and not mismatches
            and reverse_odd
        ),
    }


def manual_tableau() -> tuple[tuple[int, int], ...]:
    """Independent one-cell Pauli reconstruction: (X bits, Z bits)."""
    rows = []
    for direction in range(6):
        rows.append((0, (1 << direction) | (1 << (9 + direction))))
    for direction in range(5):
        rows.append((
            (
                (1 << direction)
                | (1 << (direction + 1))
                | (1 << (9 + direction))
                | (1 << (9 + direction + 1))
            ),
            0,
        ))
    return tuple(rows)


def symplectic(left: tuple[int, int], right: tuple[int, int]) -> int:
    return (
        (left[0] & right[1]).bit_count()
        + (left[1] & right[0]).bit_count()
    ) & 1


def generated_subgroup(generators: tuple[int, ...]) -> tuple[int, ...]:
    values = []
    for selector in range(1 << len(generators)):
        value = 0
        for index, generator in enumerate(generators):
            if (selector >> index) & 1:
                value ^= generator
        values.append(value)
    return tuple(sorted(values))


def density_digest(entries: dict[tuple[int, int], Fraction]) -> str:
    digest = sha256()
    for (row, column), value in sorted(entries.items()):
        digest.update(
            (
                f"{row}:{column}:{value.numerator}/{value.denominator}\n"
            ).encode("ascii")
        )
    return digest.hexdigest()


def reconstruct_density() -> dict[str, object]:
    tableau = manual_tableau()
    binary_rows = tuple(
        x | (z << QUBITS) for x, z in tableau
    )
    z_rows = tuple(z for x, z in tableau if not x)
    x_rows = tuple(x for x, z in tableau if not z)
    allowed = tuple(
        basis
        for basis in range(HILBERT_DIMENSION)
        if all((basis & z).bit_count() % 2 == 0 for z in z_rows)
    )
    flips = generated_subgroup(x_rows)
    entry = Fraction(1, len(allowed))
    entries = {
        (basis ^ flip, basis): entry
        for basis in allowed
        for flip in flips
    }
    trace = sum(
        (
            value
            for (row, column), value in entries.items()
            if row == column
        ),
        Fraction(),
    )
    purity = sum(
        (value * value for value in entries.values()), Fraction()
    )
    unseen = set(allowed)
    orbit_sizes = []
    while unseen:
        seed = min(unseen)
        orbit = {seed ^ flip for flip in flips}
        unseen -= orbit
        orbit_sizes.append(len(orbit))
    off_diagonal = sum(row != column for row, column in entries)
    commuting_failures = sum(
        symplectic(tableau[left], tableau[right])
        for left in range(len(tableau))
        for right in range(left)
    )
    hermitian_failures = sum(
        entries.get((column, row)) != value
        for (row, column), value in entries.items()
    )
    return {
        "tableau_rows": len(tableau),
        "tableau_rank_GF2": gf2_rank(binary_rows),
        "commuting_failures": commuting_failures,
        "allowed_basis_count": len(allowed),
        "flip_subgroup_size": len(flips),
        "matrix_nonzero_entries": len(entries),
        "matrix_diagonal_entries": len(entries) - off_diagonal,
        "matrix_off_diagonal_entries": off_diagonal,
        "matrix_entry_value": entry,
        "matrix_sha256": density_digest(entries),
        "trace": trace,
        "rank": len(orbit_sizes),
        "orbit_sizes": tuple(orbit_sizes),
        "nonzero_eigenvalue": len(flips) * entry,
        "purity": purity,
        "hermitian_failures": hermitian_failures,
        "entries": entries,
        "passed": (
            len(tableau) == 11
            and gf2_rank(binary_rows) == 11
            and commuting_failures == 0
            and len(allowed) == 512
            and len(flips) == 32
            and len(entries) == 16_384
            and len(entries) - off_diagonal == 512
            and off_diagonal == 15_872
            and entry == Fraction(1, 512)
            and trace == 1
            and len(orbit_sizes) == 16
            and set(orbit_sizes) == {32}
            and len(flips) * entry == Fraction(1, 16)
            and purity == Fraction(1, 16)
            and hermitian_failures == 0
        ),
    }


def choi_column_index(direction: int) -> int:
    return (1 << direction) | (1 << (9 + direction))


def response_from_diagonal(weights: tuple[Fraction, ...]) -> Response:
    if len(weights) != W7_DIMENSION:
        raise ValueError("W7 diagonal has the wrong dimension")
    output = [[Fraction() for _axis in range(3)] for _component in range(3)]
    for weight, row in zip(weights, response_rows()):
        add_scaled_response(output, weight, row)
    return freeze_response(output)


def subtract_response(left: Response, right: Response) -> Response:
    return tuple(
        tuple(
            left[component][axis] - right[component][axis]
            for axis in range(3)
        )
        for component in range(3)
    )  # type: ignore[return-value]


def embedded_compression(
    entries: dict[tuple[int, int], Fraction],
) -> tuple[tuple[Fraction, ...], ...]:
    columns = tuple(choi_column_index(direction) for direction in range(6))
    return tuple(
        tuple(entries.get((row, column), Fraction()) for column in columns)
        for row in columns
    )


def compression_coordinates(
    compression: tuple[tuple[Fraction, ...], ...],
) -> tuple[Fraction, ...]:
    pairs = tuple(
        (left, right)
        for left in range(W7_DIMENSION)
        for right in range(left + 1, W7_DIMENSION)
    )
    return (
        tuple(compression[index][index] for index in range(W7_DIMENSION))
        + tuple(compression[left][right] for left, right in pairs)
        + tuple(Fraction() for _pair in pairs)
    )


def span_gap_verification(
    density: dict[str, object],
) -> dict[str, object]:
    entries = density["entries"]
    assert isinstance(entries, dict)
    pure_rows = tuple(
        pure_projector_coordinates(amplitudes)
        for _label, amplitudes in spanning_pure_inputs()
    )
    pure_rank = fraction_rank(pure_rows)
    compression = embedded_compression(entries)
    outside_coordinate = entries.get((0, 0), Fraction())
    augmented_rows = tuple(row + (Fraction(),) for row in pure_rows) + (
        compression_coordinates(compression) + (outside_coordinate,),
    )
    augmented_rank = fraction_rank(augmented_rows)
    compression_trace = sum(
        (compression[index][index] for index in range(6)), Fraction()
    )
    in_span = augmented_rank == pure_rank
    return {
        "finding": (
            "The rank-16 720 density is not in the embedded six-column "
            "pure-density span."
        ),
        "ambient_Hilbert_dimension": HILBERT_DIMENSION,
        "ambient_Hermitian_operator_dimension":
            HILBERT_DIMENSION * HILBERT_DIMENSION,
        "W7_column_subspace_dimension": W7_DIMENSION,
        "W7_Hermitian_operator_dimension": W7_DIMENSION * W7_DIMENSION,
        "spanning_pure_projector_count": len(pure_rows),
        "exact_pure_projector_span_rank": pure_rank,
        "exact_rank_after_adjoining_rho_720": augmented_rank,
        "rho_720_in_span": in_span,
        "rho_720_operator_rank": density["rank"],
        "rank_obstruction": (
            "Every operator supported on the W7 image has rank <=6, whereas "
            "rho_720 has exact rank 16."
        ),
        "independent_outside_coordinate_witness": {
            "basis_matrix_coordinate": "(0,0)",
            "rho_value": outside_coordinate,
            "all_W7_span_values": 0,
        },
        "embedded_W7_compression_trace": compression_trace,
        "dimension_figures": (
            f"H={HILBERT_DIMENSION}; Herm(H)={HILBERT_DIMENSION ** 2}; "
            f"W7=6; Herm(W7)=36; span_rank={pure_rank}; "
            f"augmented_rank={augmented_rank}; rank(rho_720)={density['rank']}"
        ),
        "passed": (
            density["passed"]
            and pure_rank == 36
            and augmented_rank == 37
            and not in_span
            and density["rank"] == 16
            and outside_coordinate == Fraction(1, 512)
            and compression_trace == Fraction(3, 256)
        ),
    }


def lift_spread_recount(density: dict[str, object]) -> dict[str, object]:
    entries = density["entries"]
    assert isinstance(entries, dict)
    embedded = {
        choi_column_index(direction) for direction in range(W7_DIMENSION)
    }
    outside_left = 0
    outside_right = 0b11 | (0b11 << 9)
    rho_uv = entries.get((outside_left, outside_right), Fraction())
    rho_vu = entries.get((outside_right, outside_left), Fraction())
    difference = rho_uv + rho_vu
    return {
        "finding": (
            "rho_720 has 15,872 off-diagonal entries, each 1/512; two "
            "Hermitian lifts agreeing on the full W7 span differ by exactly "
            "1/256 on rho_720."
        ),
        "matrix_nonzero_entries": density["matrix_nonzero_entries"],
        "matrix_diagonal_entries": density["matrix_diagonal_entries"],
        "matrix_off_diagonal_entries": density[
            "matrix_off_diagonal_entries"
        ],
        "entry_value": density["matrix_entry_value"],
        "lift_pair": {
            "K0": "arbitrary fixed W7 diagonal K, zero off its image",
            "K1": "K0+|u><v|+|v><u|",
            "u": outside_left,
            "v": outside_right,
            "u_and_v_outside_W7_image":
                outside_left not in embedded and outside_right not in embedded,
            "agreement_on_every_W7_density": True,
            "rho_uv": rho_uv,
            "rho_vu": rho_vu,
            "Tr_rho_times_K1_minus_K0": difference,
        },
        "passed": (
            density["passed"]
            and density["matrix_off_diagonal_entries"] == 15_872
            and density["matrix_entry_value"] == Fraction(1, 512)
            and outside_left not in embedded
            and outside_right not in embedded
            and rho_uv == rho_vu == Fraction(1, 512)
            and difference == Fraction(1, 256)
        ),
    }


def partial_trace_to_output(
    entries: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    """Trace the input-matter and companion tensor factors exactly."""
    reduced: dict[tuple[int, int], Fraction] = {}
    for (row, column), value in entries.items():
        if (row >> 6) != (column >> 6):
            continue
        coordinate = (row & OUTPUT_MASK, column & OUTPUT_MASK)
        reduced[coordinate] = reduced.get(coordinate, Fraction()) + value
    return reduced


def normalized_diagonal(
    matrix: dict[tuple[int, int], Fraction],
    indices: tuple[int, ...],
) -> tuple[tuple[Fraction, ...], Fraction]:
    diagonal = tuple(
        matrix.get((index, index), Fraction()) for index in indices
    )
    trace = sum(diagonal, Fraction())
    if not trace:
        raise ValueError("zero postselection probability")
    return tuple(value / trace for value in diagonal), trace


def add_tau_retraction(
    base_diagonal: tuple[Fraction, ...],
    complement_weight: Fraction,
    tau_direction: int,
) -> tuple[Fraction, ...]:
    return tuple(
        value + (complement_weight if index == tau_direction else Fraction())
        for index, value in enumerate(base_diagonal)
    )


def uniform_coherent_density_coordinates() -> tuple[Fraction, ...]:
    """Coordinates of |s><s|, s=(1,...,1)/sqrt(6), without radicals."""
    pairs = W7_DIMENSION * (W7_DIMENSION - 1) // 2
    return (
        (Fraction(1, 6),) * W7_DIMENSION
        + (Fraction(1, 6),) * pairs
        + (Fraction(),) * pairs
    )


def canonicity_attack(
    density: dict[str, object],
    evidence: dict[str, object],
) -> dict[str, object]:
    entries = density["entries"]
    assert isinstance(entries, dict)
    compression = embedded_compression(entries)
    direct_base = tuple(compression[index][index] for index in range(6))
    direct_trace = sum(direct_base, Fraction())
    direct_postselected = tuple(value / direct_trace for value in direct_base)
    direct_postselected_response = response_from_diagonal(direct_postselected)

    reduced = partial_trace_to_output(entries)
    reduced_trace = sum(
        (
            value
            for (row, column), value in reduced.items()
            if row == column
        ),
        Fraction(),
    )
    reduced_is_maximally_mixed = (
        len(reduced) == 64
        and all(
            reduced.get((index, index)) == Fraction(1, 64)
            for index in range(64)
        )
        and all(row == column for row, column in reduced)
    )
    exact_one_indices = tuple(1 << direction for direction in range(6))
    sector_postselected, sector_trace = normalized_diagonal(
        reduced, exact_one_indices
    )
    sector_postselected_response = response_from_diagonal(
        sector_postselected
    )

    # Two explicit full-space -> C^6 CPTP retractions.  Their Kraus
    # completeness is P + sum_{q outside P}|q><q| = I.  Each is identity on
    # the complete embedded W7 operator algebra, but the fallback state differs.
    direct_complement = Fraction(1) - direct_trace
    direct_r0 = add_tau_retraction(direct_base, direct_complement, 0)
    direct_r1 = add_tau_retraction(direct_base, direct_complement, 1)
    direct_response_0 = response_from_diagonal(direct_r0)
    direct_response_1 = response_from_diagonal(direct_r1)
    direct_response_difference = subtract_response(
        direct_response_0, direct_response_1
    )

    # The same nonuniqueness survives after the genuine canonical partial
    # trace.  Exact-one compression is completed to a channel by routing the
    # 58-dimensional complement to an arbitrary W7 state.
    sector_base = tuple(
        reduced.get((index, index), Fraction())
        for index in exact_one_indices
    )
    sector_complement = Fraction(1) - sector_trace
    sector_r0 = add_tau_retraction(sector_base, sector_complement, 0)
    sector_r1 = add_tau_retraction(sector_base, sector_complement, 1)
    sector_response_difference = subtract_response(
        response_from_diagonal(sector_r0),
        response_from_diagonal(sector_r1),
    )

    # Even full permutation covariance does not make the reduction map unique:
    # tau=I/6 and tau=|s><s| are distinct invariant fallback densities.
    uniform_mixed = (
        (Fraction(1, 6),) * 6
        + (Fraction(),) * 15
        + (Fraction(),) * 15
    )
    uniform_coherent = uniform_coherent_density_coordinates()
    invariant_fallbacks_distinct = uniform_mixed != uniform_coherent

    candidates = (
        {
            "candidate": "partial trace over companion+Choi-input",
            "well_defined_on_rho_720": True,
            "CPTP": True,
            "unique_given_this_tensor_factor_split": True,
            "lands_on_C6": False,
            "result": "I_64/64 on the six-qubit output register",
            "failure_of_canonicity": (
                "A partial trace lands on dimension 64, not the W7 dimension "
                "6; C^6 is not a qubit tensor factor."
            ),
        },
        {
            "candidate": "direct restriction to the six embedded W7 columns",
            "well_defined_on_rho_720": True,
            "CPTP": False,
            "CP_trace_nonincreasing": True,
            "success_probability": direct_trace,
            "normalized_result": "I_6/6",
            "response": direct_postselected_response,
            "failure_of_canonicity": (
                "Compression is not trace preserving.  Dividing by its trace "
                "is nonlinear and is undefined on states with zero W7 weight."
            ),
        },
        {
            "candidate": "partial trace then exact-one output restriction",
            "well_defined_on_rho_720": True,
            "CPTP": False,
            "CP_trace_nonincreasing": True,
            "success_probability": sector_trace,
            "normalized_result": "I_6/6",
            "response": sector_postselected_response,
            "failure_of_canonicity": (
                "The exact-one projection is trace decreasing; normalized "
                "postselection is nonlinear and selects an occupation sector."
            ),
        },
        {
            "candidate": "CPTP retractions fixing every landed W7 state",
            "well_defined_on_rho_720": True,
            "CPTP": True,
            "unique": False,
            "Kraus_completeness": (
                "A=V^dagger P plus B_q=|tau><q| for each q in P^perp; "
                "A^dagger A+sum_q B_q^dagger B_q=P+Q=I"
            ),
            "direct_full_space_complement_weight": direct_complement,
            "two_response_difference": direct_response_difference,
            "after_partial_trace_complement_weight": sector_complement,
            "two_response_difference_after_partial_trace":
                sector_response_difference,
            "failure_of_canonicity": (
                "tau is free.  tau=|e0><e0| and tau=|e1><e1| are both CPTP "
                "and both act identically on every declared W7 density."
            ),
        },
        {
            "candidate": "permutation/cubic-covariant CPTP completion",
            "unique": False,
            "two_distinct_invariant_fallbacks":
                ("I_6/6", "|s><s| with s proportional to (1,1,1,1,1,1)"),
            "fallback_coordinate_vectors_distinct":
                invariant_fallbacks_distinct,
            "failure_of_canonicity": (
                "Symmetry still leaves distinct invariant fallback density "
                "operators, so it does not select a unique reduction map."
            ),
        },
        {
            "candidate": "Choi live-input contraction / decoder",
            "present_in_landed_lineage": False,
            "failure_of_canonicity": (
                "Cycle-803's decoder candidate has no return: it requires a "
                "live-input amplitude ray, exact-one projection, companion "
                "gauge/branch selection, or equivalent new supply."
            ),
        },
    )
    unique_landed_reduction_exists = False
    return {
        "finding": (
            "No unique landed-principled reduction exists.  The genuine "
            "partial trace misses C^6; both sector restrictions require "
            "postselection; CPTP completions fixing the entire W7 scope form "
            "an explicit nonunique family."
        ),
        "candidates_examined": candidates,
        "partial_trace_output": {
            "shape": (64, 64),
            "trace": reduced_trace,
            "nonzero_entries": len(reduced),
            "equals_I64_over_64": reduced_is_maximally_mixed,
        },
        "illustrative_zero_bridges": {
            "direct_W7_postselection_response": direct_postselected_response,
            "partial_trace_then_exact_one_response":
                sector_postselected_response,
            "matches_kernel_prediction_zero": (
                direct_postselected_response
                == sector_postselected_response
                == zero_response()
            ),
            "status": (
                "well-defined on rho_720 but nonlinear/non-CPTP; agreement "
                "with zero cannot select either bridge"
            ),
        },
        "landed_lineage_search": evidence,
        "unique_landed_principled_reduction_exists":
            unique_landed_reduction_exists,
        "reopen": False,
        "verdict": "TIGHTENED_EXTENSION_NOT_CANONICAL",
        "passed": (
            density["passed"]
            and evidence["passed"]
            and reduced_trace == 1
            and reduced_is_maximally_mixed
            and direct_trace == Fraction(3, 256)
            and sector_trace == Fraction(3, 32)
            and direct_postselected == (Fraction(1, 6),) * 6
            and sector_postselected == (Fraction(1, 6),) * 6
            and direct_postselected_response == zero_response()
            and sector_postselected_response == zero_response()
            and direct_complement == Fraction(253, 256)
            and sector_complement == Fraction(29, 32)
            and any(
                value != 0
                for vector in direct_response_difference
                for value in vector
            )
            and any(
                value != 0
                for vector in sector_response_difference
                for value in vector
            )
            and invariant_fallbacks_distinct
            and not unique_landed_reduction_exists
        ),
    }


def public_density(density: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in density.items() if key != "entries"
    }


def run_core(
    raw: dict[str, bytes],
    texts: dict[str, str],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    evidence = source_evidence(raw, texts, trees)
    density = reconstruct_density()
    return {
        "linearity": linearity_verification(evidence),
        "density": public_density(density),
        "span_gap": span_gap_verification(density),
        "lift_spread": lift_spread_recount(density),
        "canonicity": canonicity_attack(density, evidence),
    }


def source_controls(
    raw_before: dict[str, bytes],
    raw_after: dict[str, bytes],
    *,
    deterministic: bool,
    science_passed: bool,
    runtime: float,
    stdout_upper_bound: int,
) -> dict[str, object]:
    shas_before = {
        path: sha256_bytes(data) for path, data in raw_before.items()
    }
    shas_after = {
        path: sha256_bytes(data) for path, data in raw_after.items()
    }
    firewall = own_import_firewall()
    paths_exist = {
        path: (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
    }
    return {
        "finding": (
            "Seven literal worktree-relative inputs are SHA-pinned and "
            "unchanged; the Cycle-812/803 primaries remained BLOCKLISTED "
            "text/AST-only; the exact recomputation is deterministic and "
            "within runtime/stdout bounds."
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_tuple_verified":
            literal_input_paths() == AUDIT_INPUT_PATHS,
        "paths_exist": paths_exist,
        "sha256": shas_after,
        "sha_stable_during_run": shas_before == shas_after,
        "sha_matches_expected": shas_after == EXPECTED_SHA256,
        "BLOCKLISTED_MODULES": BLOCKLISTED_MODULES,
        "blocklist_firewall": firewall,
        "current_worktree_HEAD": git_head(ROOT),
        "lineage_copy_HEAD": git_head(ROOT.parent / "born-harness-worktree"),
        "deterministic": deterministic,
        "runtime_sec_before_render": runtime,
        "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
        "stdout_upper_bound_bytes": stdout_upper_bound,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "passed": (
            len(AUDIT_INPUT_PATHS) == 7
            and literal_input_paths() == AUDIT_INPUT_PATHS
            and all(paths_exist.values())
            and shas_before == shas_after == EXPECTED_SHA256
            and firewall["text_ast_only"]
            and deterministic
            and science_passed
            and runtime < AUDIT_TIMEOUT_SEC
            and stdout_upper_bound < STDOUT_LIMIT_BYTES
        ),
    }


def render_certificate_line(
    name: str, finding: dict[str, object]
) -> str:
    prefix = "PASS" if finding["passed"] else "FAIL"
    return (
        f"{prefix} {name} :: "
        + json.dumps(
            finding,
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )


def main() -> int:
    raw_before, texts_before, trees_before = read_source_packet()
    first = run_core(raw_before, texts_before, trees_before)
    raw_second, texts_second, trees_second = read_source_packet()
    second = run_core(raw_second, texts_second, trees_second)
    deterministic = first == second
    science_names = ("linearity", "span_gap", "lift_spread", "canonicity")
    science_passed = all(first[name]["passed"] for name in science_names)

    preliminary_lines = (
        render_certificate_line("LINEARITY VERIFICATION", first["linearity"]),
        render_certificate_line("SPAN-GAP VERIFICATION", first["span_gap"]),
        render_certificate_line("LIFT-SPREAD RECOUNT", first["lift_spread"]),
        render_certificate_line("THE CANONICITY ATTACK", first["canonicity"]),
    )
    # A conservative allowance covers the controls line and terminal summary.
    stdout_upper_bound = (
        sum(len((line + "\n").encode("utf-8")) for line in preliminary_lines)
        + 20_000
    )
    runtime = time.monotonic() - STARTED
    controls = source_controls(
        raw_before,
        raw_second,
        deterministic=deterministic,
        science_passed=science_passed,
        runtime=runtime,
        stdout_upper_bound=stdout_upper_bound,
    )
    lines = preliminary_lines + (
        render_certificate_line("CONTROLS", controls),
        (
            "FINAL VERDICT :: "
            + (
                "TIGHTENED_EXTENSION_NOT_CANONICAL"
                if first["canonicity"]["passed"]
                else "CHECK_FAILED"
            )
        ),
        (
            "CANONICITY FINDING :: "
            + str(first["canonicity"]["finding"])
        ),
        f"RUNTIME_SECONDS {time.monotonic() - STARTED:.6f}",
    )
    rendered = "\n".join(lines) + "\n"
    actual_stdout_bytes = len(rendered.encode("utf-8"))
    bounds_passed = (
        actual_stdout_bytes < STDOUT_LIMIT_BYTES
        and actual_stdout_bytes <= stdout_upper_bound
        and (time.monotonic() - STARTED) < AUDIT_TIMEOUT_SEC
    )
    print(rendered, end="")
    return 0 if science_passed and controls["passed"] and bounds_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
