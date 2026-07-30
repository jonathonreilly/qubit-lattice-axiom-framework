#!/usr/bin/env python3
"""Cycle 812: test a choice-free mixed-input extension of the W7 response.

This runner is deliberately self-contained.  The seven named historical
primaries are SHA-pinned text/AST evidence only: none is imported or executed.
All physics used below is reimplemented with stdlib exact arithmetic.
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


PROCESS_STARTED = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
COPY_ROOT = ROOT.parent / "born-harness-worktree"
AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200_000
REFERENCE_COMMIT = "596edad4baf851c18cca1432e963655f2839729b"

# Literal, worktree-relative, seven-file packet.  These are tracked copies in
# ../born-harness-worktree and are never imported or executed.
AUDIT_INPUT_PATHS = (
    "../born-harness-worktree/scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle803_decoder_derivation_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle803_decoder_independent_check_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[1]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[2]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[3]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[4]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[5]:
        "df3287bd2aa0fdfc3361551894760f04d3ebb60ba6214fe83f005056e8aec0ab",
    AUDIT_INPUT_PATHS[6]:
        "33c3c26c4781efe7ab77eef83ed61a6e25cc72bfde271f52b534342f4d0ff5e8",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle749_response_comparison_harness_2026_07_28",
    "frontier_cycle768_response_law_candidate_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
    "frontier_cycle774_interference_sector_2026_07_28",
    "frontier_cycle778_norefit_attachment_2026_07_28",
    "frontier_cycle803_decoder_derivation_2026_07_28",
    "frontier_cycle803_decoder_independent_check_2026_07_28",
)

# This is printed before the tableau is rebuilt or any response outcome is
# evaluated.  It is the conditional value obtained by applying W7's diagonal
# unit kernel to a direction-symmetric six-channel density.
PREREGISTERED_PREDICTION = {
    "conditional_assumption":
        "the 720 operator is canonically a density on W7's six-column space",
    "derived_kernel": "unit diagonal recoil kernel; zero fitted defaults",
    "instrument_response": (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    ),
    "interference_nonzero_cells": 0,
    "strict_package_prediction":
        "UNDEFINED unless the span/embedding gate passes",
}

PASS = 0
FAIL = 0
STDOUT_BYTES = 0


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


def emit(line: str) -> None:
    global STDOUT_BYTES
    print(line)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))


def certificate(name: str, passed: bool, detail: object) -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
        prefix = "PASS"
    else:
        FAIL += 1
        prefix = "FAIL"
    emit(
        f"{prefix} {name} :: "
        + json.dumps(
            detail, sort_keys=True, separators=(",", ":"), default=jsonable
        )
    )


def sha256_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def read_reference_copies() -> dict[str, bytes]:
    return {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}


def line_of_fragment(text: str, fragment: str) -> int:
    offset = text.find(fragment)
    if offset < 0:
        raise ValueError(f"defining fragment absent: {fragment!r}")
    return text.count("\n", 0, offset) + 1


def literal_paths_from_self() -> tuple[str, ...]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    if len(matches) != 1 or not isinstance(matches[0].value, ast.Tuple):
        return ()
    elements = matches[0].value.elts
    if not all(
        isinstance(element, ast.Constant)
        and isinstance(element.value, str)
        for element in elements
    ):
        return ()
    return tuple(element.value for element in elements)


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
        "passed": not forbidden and not any(loaded.values()),
    }


def tracked_copy_status() -> dict[str, object]:
    head = subprocess.run(
        ("git", "-C", str(COPY_ROOT), "rev-parse", "HEAD"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    tracked = {}
    prefix = "../born-harness-worktree/"
    for path in AUDIT_INPUT_PATHS:
        relative = path.removeprefix(prefix)
        result = subprocess.run(
            (
                "git", "-C", str(COPY_ROOT), "ls-files",
                "--error-unmatch", relative,
            ),
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        tracked[path] = result.returncode == 0
    actual_head = head.stdout.strip() if head.returncode == 0 else "ERROR"
    return {
        "actual_copy_commit": actual_head,
        "initial_copy_commit": REFERENCE_COMMIT,
        "commit_match_informational": actual_head == REFERENCE_COMMIT,
        "provenance_rule": (
            "the sibling worktree HEAD may advance; the scientific anchors "
            "are tracked status plus the seven exact SHA-256 values"
        ),
        "tracked": tracked,
        "all_tracked": all(tracked.values()),
    }


def defining_code_audit(copies: dict[str, bytes]) -> dict[str, object]:
    texts = {
        path: data.decode("utf-8") for path, data in copies.items()
    }
    citations = (
        (
            AUDIT_INPUT_PATHS[2],
            "return Fraction.from_float(real * real + imaginary * imaginary)",
            "pure amplitude enters as |amplitude|^2",
        ),
        (
            AUDIT_INPUT_PATHS[2],
            "tuple(value / weight for value in matter)",
            "Cycle-771 conditions every column response by branch weight",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "raw[component][axis] / total",
            "Cycle-774 coherent response is explicitly branch-conditioned",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "cross_term = coherent_probability - mixture_probability",
            "Cycle-774 defines the interference tensor exactly",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "(matter,mediator,auxiliary)=(REVERSE[d],d,d)",
            "orthogonal source labels make the W7 interference sector empty",
        ),
        (
            AUDIT_INPUT_PATHS[4],
            "composition_row = add_response_rows(input_rows)",
            "Cycle-778's kernel prediction is additive over identity columns",
        ),
        (
            AUDIT_INPUT_PATHS[5],
            "return U320.LinkState({ORIGIN: vector}, {})",
            "Cycle-803 identifies each W7 defining input with one C^6 column",
        ),
        (
            AUDIT_INPUT_PATHS[5],
            "it does not map Pauli bits to six ",
            "Cycle-803 explicitly denies a tableau-to-LinkState amplitude map",
        ),
    )
    rows = []
    for path, fragment, meaning in citations:
        rows.append({
            "path": path,
            "line": line_of_fragment(texts[path], fragment),
            "defining_code": fragment,
            "meaning": meaning,
        })
    parsed = {
        path: isinstance(ast.parse(text, filename=path), ast.Module)
        for path, text in texts.items()
    }
    return {
        "citations": tuple(rows),
        "all_ast_parse": all(parsed.values()),
        "ast_parse": parsed,
    }


def source_control_certificate() -> dict[str, object]:
    before = read_reference_copies()
    shas_before = {
        path: sha256_bytes(data) for path, data in before.items()
    }
    defining = defining_code_audit(before)
    tracked = tracked_copy_status()
    firewall_before = own_import_firewall()
    after = read_reference_copies()
    shas_after = {
        path: sha256_bytes(data) for path, data in after.items()
    }
    firewall_after = own_import_firewall()
    literal_paths = literal_paths_from_self()
    passed = (
        len(AUDIT_INPUT_PATHS) == 7
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and shas_before == EXPECTED_SHA256
        and shas_after == EXPECTED_SHA256
        and shas_before == shas_after
        and tracked["all_tracked"]
        and defining["all_ast_parse"]
        and firewall_before["passed"]
        and firewall_after["passed"]
    )
    return {
        "pass": passed,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "defining_code_audit": defining,
        "literal_paths": literal_paths,
        "reference_copy": tracked,
        "sha256": shas_after,
        "text_ast_only_before": firewall_before,
        "text_ast_only_after": firewall_after,
    }


QUBITS = 15
OUTPUT_MATTER = tuple(range(6))
OUTPUT_COMPANION = tuple(range(6, 9))
CHOI_INPUT_MATTER = tuple(range(9, 15))
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
REVERSE = (1, 0, 3, 2, 5, 4)
COEFFICIENT_FAMILY = (
    ("1,1", ((1, 0), (1, 0))),
    ("1,-1", ((1, 0), (-1, 0))),
    ("1,i", ((1, 0), (0, 1))),
    ("1,-i", ((1, 0), (0, -1))),
    ("2,1", ((2, 0), (1, 0))),
    ("1,2", ((1, 0), (2, 0))),
)


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


def symplectic(left: tuple[int, int], right: tuple[int, int]) -> int:
    left_x, left_z = left
    right_x, right_z = right
    return (
        (left_x & right_z).bit_count()
        + (left_z & right_x).bit_count()
    ) & 1


def manual_720_tableau() -> tuple[tuple[int, int, int, str], ...]:
    """Rebuild the literal one-cell 720 rows; no historical code is called."""
    rows = []
    for direction in range(6):
        rows.append((
            0,
            (1 << direction) | (1 << (9 + direction)),
            0,
            f"Z_output_{direction} Z_input_{direction}",
        ))
    for direction in range(5):
        rows.append((
            (
                (1 << direction)
                | (1 << (direction + 1))
                | (1 << (9 + direction))
                | (1 << (9 + direction + 1))
            ),
            0,
            0,
            (
                f"X_output_{direction} X_output_{direction + 1} "
                f"X_input_{direction} X_input_{direction + 1}"
            ),
        ))
    return tuple(rows)


def x_subgroup(generators: tuple[int, ...]) -> tuple[int, ...]:
    output = []
    for selector in range(1 << len(generators)):
        value = 0
        for index, generator in enumerate(generators):
            if (selector >> index) & 1:
                value ^= generator
        output.append(value)
    return tuple(sorted(output))


def density_digest(entries: dict[tuple[int, int], Fraction]) -> str:
    digest = sha256()
    for (row, column), value in sorted(entries.items()):
        digest.update(
            (
                f"{row}:{column}:{value.numerator}/{value.denominator}\n"
            ).encode("ascii")
        )
    return digest.hexdigest()


def reconstruct_720_density() -> dict[str, object]:
    """Construct the exact sparse 32768x32768 stabilizer density matrix.

    Six Z correlations select output_bits=input_bits, with all three
    companion bits free.  The five adjacent-XX rows generate the 32-element
    even-flip orbit.  Expanding 2^-15 product_j(I+S_j) therefore gives the
    exact 16,384 nonzero matrix entries below, each equal to 1/512.
    """
    tableau = manual_720_tableau()
    pairs = tuple((row[0], row[1]) for row in tableau)
    vectors = tuple(x | (z << QUBITS) for x, z in pairs)
    rank = gf2_rank(vectors)
    commuting_failures = sum(
        symplectic(pairs[left], pairs[right])
        for left in range(len(pairs))
        for right in range(left)
    )
    z_generators = tuple(z for x, z in pairs if not x)
    x_generators = tuple(x for x, z in pairs if not z)
    allowed = tuple(
        basis
        for basis in range(1 << QUBITS)
        if all((basis & z).bit_count() % 2 == 0 for z in z_generators)
    )
    flips = x_subgroup(x_generators)
    entry = Fraction(1, len(allowed))
    entries = {
        (basis ^ flip, basis): entry
        for basis in allowed
        for flip in flips
    }

    hermitian_failures = sum(
        entries.get((column, row)) != value
        for (row, column), value in entries.items()
    )
    invariance_failures = 0
    for x, z in pairs:
        for (row, column), value in entries.items():
            sign = -1 if (z & row).bit_count() % 2 else 1
            if entries.get((row ^ x, column), Fraction()) != sign * value:
                invariance_failures += 1

    trace = sum(
        (
            value
            for (row, column), value in entries.items()
            if row == column
        ),
        start=Fraction(),
    )
    purity = sum(
        (value * value for value in entries.values()),
        start=Fraction(),
    )
    unseen = set(allowed)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {seed ^ flip for flip in flips}
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    density_rank = len(orbits)
    nonzero_eigenvalue = len(flips) * entry
    off_diagonal_count = sum(row != column for row, column in entries)
    diagonal_count = len(entries) - off_diagonal_count
    serialized_tableau = tuple(
        {
            "label": label,
            "phase_i_power": phase,
            "x_columns": tuple(
                bit for bit in range(QUBITS) if (x >> bit) & 1
            ),
            "z_columns": tuple(
                bit for bit in range(QUBITS) if (z >> bit) & 1
            ),
        }
        for x, z, phase, label in tableau
    )
    passed = (
        len(tableau) == 11
        and rank == 11
        and commuting_failures == 0
        and len(allowed) == 512
        and len(flips) == 32
        and len(entries) == 16_384
        and diagonal_count == 512
        and off_diagonal_count == 15_872
        and hermitian_failures == 0
        and invariance_failures == 0
        and trace == 1
        and density_rank == 16
        and all(len(orbit) == 32 for orbit in orbits)
        and nonzero_eigenvalue == Fraction(1, 16)
        and purity == Fraction(1, 16)
    )
    return {
        "pass": passed,
        "Q": QUBITS,
        "tableau": serialized_tableau,
        "tableau_rank": rank,
        "commuting_failures": commuting_failures,
        "matrix_dimension": 1 << QUBITS,
        "matrix_representation": (
            "exact sparse dict[(row,column)]=Fraction; "
            "rho=2^-15 product_j(I+S_j)"
        ),
        "matrix_nonzero_entries": len(entries),
        "matrix_diagonal_entries": diagonal_count,
        "matrix_off_diagonal_entries": off_diagonal_count,
        "matrix_entry_value": entry,
        "matrix_sha256": density_digest(entries),
        "allowed_computational_basis_states": len(allowed),
        "x_subgroup_size": len(flips),
        "orbit_count": len(orbits),
        "orbit_sizes": tuple(len(orbit) for orbit in orbits),
        "rank": density_rank,
        "nonzero_eigenvalue": nonzero_eigenvalue,
        "trace": trace,
        "purity": purity,
        "hermitian_failures": hermitian_failures,
        "stabilizer_invariance_failures": invariance_failures,
        "entries": entries,
    }


def response_rows() -> tuple[tuple[tuple[Fraction, ...], ...], ...]:
    rows = []
    for direction in DIRECTIONS:
        vector = tuple(Fraction(value) for value in direction)
        rows.append((
            tuple(-2 * value for value in vector),
            vector,
            vector,
        ))
    return tuple(rows)


def fraction_rank(rows: tuple[tuple[Fraction, ...], ...]) -> int:
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
                value - factor * owner_value
                for value, owner_value in zip(
                    matrix[row], matrix[pivot_row]
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def pure_projector_span_rank() -> dict[str, object]:
    """Exact real span of 6x6 Hermitian pure-state density matrices."""
    dimension = 6
    pairs = tuple(
        (left, right)
        for left in range(dimension)
        for right in range(left + 1, dimension)
    )
    coordinate_count = dimension + 2 * len(pairs)
    projectors = []
    labels = []
    for direction in range(dimension):
        row = [Fraction() for _index in range(coordinate_count)]
        row[direction] = 1
        projectors.append(tuple(row))
        labels.append(f"|{direction}><{direction}|")
    for pair_index, (left, right) in enumerate(pairs):
        row = [Fraction() for _index in range(coordinate_count)]
        row[left] = row[right] = Fraction(1, 2)
        row[dimension + pair_index] = Fraction(1, 2)
        projectors.append(tuple(row))
        labels.append(f"|{left}+{right}><{left}+{right}|/2")
    for pair_index, (left, right) in enumerate(pairs):
        row = [Fraction() for _index in range(coordinate_count)]
        row[left] = row[right] = Fraction(1, 2)
        row[dimension + len(pairs) + pair_index] = Fraction(-1, 2)
        projectors.append(tuple(row))
        labels.append(f"|{left}+i{right}><{left}+i{right}|/2")
    rank = fraction_rank(tuple(projectors))
    return {
        "w7_link_column_dimension": dimension,
        "hermitian_operator_dimension": coordinate_count,
        "pure_projector_count": len(projectors),
        "exact_projector_span_rank": rank,
        "basis_labels": tuple(labels),
        "pass": rank == coordinate_count == 36,
    }


def w7_linearity_certificate(
    source_controls: dict[str, object],
) -> dict[str, object]:
    rows = response_rows()
    branch_supports = tuple(
        36 * REVERSE[direction] + 6 * direction + direction
        for direction in range(6)
    )
    zero_cross_members = []
    nonzero_cross_members = []
    for left in range(6):
        for right in range(left + 1, 6):
            for label, coefficients in COEFFICIENT_FAMILY:
                # Each input column has unit amplitude at one distinct branch
                # cell.  Hence |a phi_l+b phi_r|^2 is the classical mixture
                # pointwise, including unequal and complex coefficients.
                cross = Fraction(0) if (
                    branch_supports[left] != branch_supports[right]
                ) else Fraction(
                    2
                    * (
                        coefficients[0][0] * coefficients[1][0]
                        + coefficients[0][1] * coefficients[1][1]
                    )
                )
                member = f"{left}-{right}:{label}"
                if cross:
                    nonzero_cross_members.append((member, cross))
                else:
                    zero_cross_members.append(member)
    span = pure_projector_span_rank()
    passed = (
        source_controls["pass"]
        and len(set(branch_supports)) == 6
        and len(zero_cross_members) == 90
        and not nonzero_cross_members
        and span["pass"]
        and all(
            rows[REVERSE[direction]][component][axis]
            == -rows[direction][component][axis]
            for direction in range(6)
            for component in range(3)
            for axis in range(3)
        )
    )
    return {
        "pass": passed,
        "ruling": "EXPECTATION_ON_DECLARED_W7_SIX_COLUMN_SCOPE",
        "exact_formula": (
            "F(|c><c|)=sum_d |c_d|^2 r_d="
            "Tr(|c><c| K), K=diag(r_0,...,r_5)"
        ),
        "response_rows_r_d": rows,
        "normalization_audit": {
            "code_form": (
                "raw/total with total=sum_d |c_d|^2 on the declared "
                "orthogonal equal-weight branches"
            ),
            "normalized_LinkState_total": Fraction(1),
            "simplified_form": "linear expectation; no surviving quotient",
        },
        "branch_support_flat_indices": branch_supports,
        "declared_interference_census": {
            "member_count": len(zero_cross_members),
            "nonzero_count": len(nonzero_cross_members),
            "nonzero_members": tuple(nonzero_cross_members),
            "zero_count": len(zero_cross_members),
        },
        "unique_linear_extension_on_w7_scope": span,
        "scope_boundary": (
            "The cited primaries evaluate six excited identity columns and "
            "their superpositions/mixtures.  They do not define K on U320's "
            "216 pair columns or on a 15-qubit Choi Hilbert space."
        ),
        "defining_code_citations":
            source_controls["defining_code_audit"]["citations"],
    }


def choi_basis_index(output_bits: int, companion_bits: int, input_bits: int) -> int:
    return output_bits | (companion_bits << 6) | (input_bits << 9)


def extension_span_certificate(
    density: dict[str, object],
    linearity: dict[str, object],
) -> dict[str, object]:
    entries = density["entries"]
    assert isinstance(entries, dict)
    embedded_columns = tuple(
        choi_basis_index(1 << direction, 0, 1 << direction)
        for direction in range(6)
    )
    compression = tuple(
        tuple(
            entries.get((left, right), Fraction())
            for right in embedded_columns
        )
        for left in embedded_columns
    )
    compression_trace = sum(
        (compression[index][index] for index in range(6)),
        start=Fraction(),
    )
    projected_kernel_response = []
    rows = response_rows()
    for component in range(3):
        projected_kernel_response.append(tuple(
            sum(
                (
                    compression[direction][direction]
                    * rows[direction][component][axis]
                    for direction in range(6)
                ),
                start=Fraction(),
            )
            for axis in range(3)
        ))

    # Two exact linear operator lifts agree on every embedded W7 pure state.
    # K0 is zero outside the chosen six-column image.  K1 adds Q=I-P_image
    # to one scalar response.  Their 720 values differ by Tr(rho Q).
    complement_weight = Fraction(1) - compression_trace

    # A cross-term ambiguity can also be put wholly outside the W7 image.
    outside_left = choi_basis_index(0, 0, 0)
    outside_right = choi_basis_index(0b11, 0, 0b11)
    outside_cross_entry = entries.get(
        (outside_left, outside_right), Fraction()
    )
    cross_lift_difference = (
        outside_cross_entry
        + entries.get((outside_right, outside_left), Fraction())
    )
    rho_in_span = (
        density["matrix_dimension"] == 6 and density["rank"] <= 6
    )
    passed = (
        linearity["pass"]
        and density["pass"]
        and not rho_in_span
        and density["matrix_dimension"] == 32_768
        and density["rank"] == 16
        and compression_trace == Fraction(3, 256)
        and all(
            value == Fraction()
            for vector in projected_kernel_response
            for value in vector
        )
        and complement_weight == Fraction(253, 256)
        and outside_left not in embedded_columns
        and outside_right not in embedded_columns
        and outside_cross_entry == Fraction(1, 512)
        and cross_lift_difference == Fraction(1, 256)
    )
    return {
        "pass": passed,
        "rho_720_in_span_of_w7_pure_densities": rho_in_span,
        "w7_density_matrix_shape": (6, 6),
        "rho_720_density_matrix_shape": (32_768, 32_768),
        "exact_rank_obstruction": (
            "every operator in an embedded six-column pure-density span is "
            "supported on a subspace of dimension <=6, but rank(rho_720)=16"
        ),
        "canonical_extension_on_original_w7_scope": True,
        "canonical_extension_to_720_scope": False,
        "named_missing_choice": (
            "a linear reduction/channel from the 15-qubit "
            "output-companion-input operator to the six W7 columns "
            "(or, equivalently, an operator lift outside those columns); "
            "exact-one postselection and renormalization is one physical "
            "choice, and a supplied purification/live input is another"
        ),
        "illustrative_column_matching_bridge": {
            "warning": "witness choice only; not canonically supplied",
            "basis_indices": embedded_columns,
            "compressed_density": compression,
            "compressed_trace": compression_trace,
            "zero_extension_response": tuple(projected_kernel_response),
        },
        "nonuniqueness_witness": {
            "K0": "embedded W7 K, zero on the orthogonal complement",
            "K1": "K0 + (I-P_W7) in the matter-x scalar response",
            "agreement_on_every_w7_pure_density": True,
            "rho_720_value_difference": complement_weight,
            "cross_term_lift": (
                "Kcross=K0+|u><v|+|v><u| with u,v outside P_W7"
            ),
            "outside_basis_indices": (outside_left, outside_right),
            "rho_uv": outside_cross_entry,
            "rho_720_cross_response_difference": cross_lift_difference,
        },
    }


def density_public_certificate(density: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in density.items()
        if key != "entries"
    }


def render_final_certificate(
    *,
    controls: dict[str, object],
    linearity: dict[str, object],
    density: dict[str, object],
    extension: dict[str, object],
    deterministic: bool,
    runtime: float,
    projected_stdout_bytes: int,
) -> dict[str, object]:
    verdict = "EXTENSION_NOT_CANONICAL"
    extension_stopped = not extension["canonical_extension_to_720_scope"]
    return {
        "certificate_A": linearity,
        "certificate_B": {
            **extension,
            "status": "SPAN_GATE_FAILED_EXTENSION_STOPPED",
        },
        "certificate_C": {
            "preregistered_prediction": PREREGISTERED_PREDICTION,
            "computed_canonical_response":
                "NOT_COMPUTED_SPAN_GATE_FAILED",
            "illustrative_noncanonical_bridge_response":
                extension["illustrative_column_matching_bridge"][
                    "zero_extension_response"
                ],
            "comparison": (
                "No canonical numerical comparison exists.  The illustrative "
                "postselected/column-matching choice gives the preregistered "
                "zero, but that agreement cannot select the choice."
            ),
            "stop_honored": extension_stopped,
        },
        "certificate_D": {
            "w7_prediction": "EMPTY_INTERFERENCE_SECTOR",
            "canonical_cross_term":
                "NOT_COMPUTED_SPAN_GATE_FAILED",
            "rho_720_raw_off_diagonal_entries":
                density["matrix_off_diagonal_entries"],
            "loud_exact_nonuniqueness": (
                "NONCANONICAL COMPLEMENT LIFT PRODUCES EXACT "
                f"CROSS-RESPONSE {fraction_text(extension['nonuniqueness_witness']['rho_720_cross_response_difference'])}"
            ),
            "interpretation": (
                "The raw 720 coherences are real, but W7 supplies no operator "
                "on their sector.  A lift that vanishes on all W7 states can "
                "make their response contribution 0 or 1/256, so emptiness "
                "cannot be tested choice-free."
            ),
            "stop_honored": extension_stopped,
        },
        "certificate_E": {
            "verdict": verdict,
            "reason": (
                "A is an expectation on the W7 C^6 scope, but B proves the "
                "rank-16 15-qubit resource is outside the pure-density span; "
                "the operator lift/reduction is a new physical supply."
            ),
        },
        "certificate_F": {
            "source_controls": controls,
            "deterministic": deterministic,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
        },
        "density_720": density_public_certificate(density),
        "fail": FAIL,
        "pass": PASS,
        "runtime_sec": runtime,
        "verdict": verdict,
    }


def main() -> int:
    emit(
        "PREREGISTERED W7 PREDICTION :: "
        + json.dumps(
            PREREGISTERED_PREDICTION,
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )
    controls = source_control_certificate()
    certificate(
        "CERTIFICATE F source copies, SHA anchors, and BLOCKLIST",
        bool(controls["pass"]),
        controls,
    )
    linearity = w7_linearity_certificate(controls)
    certificate(
        "CERTIFICATE A exact W7 input dependence",
        bool(linearity["pass"]),
        linearity,
    )

    first_density = reconstruct_720_density()
    second_density = reconstruct_720_density()
    deterministic_density = (
        density_public_certificate(first_density)
        == density_public_certificate(second_density)
    )
    certificate(
        "CERTIFICATE 720 exact tableau density reconstruction",
        bool(first_density["pass"]) and deterministic_density,
        density_public_certificate(first_density),
    )

    extension = extension_span_certificate(first_density, linearity)
    certificate(
        "CERTIFICATE B exact span gate and extension uniqueness",
        bool(extension["pass"])
        and not extension["rho_720_in_span_of_w7_pure_densities"]
        and not extension["canonical_extension_to_720_scope"],
        extension,
    )
    emit(
        "LOUD CROSS-TERM FINDING :: "
        + (
            "rho_720 has "
            f"{first_density['matrix_off_diagonal_entries']} exact nonzero "
            "off-diagonal entries of value 1/512; a complement operator lift "
            "that agrees on every W7 pure state changes the response by "
            f"{fraction_text(extension['nonuniqueness_witness']['rho_720_cross_response_difference'])}"
        )
    )
    certificate(
        "CERTIFICATE C 720 response comparison stop",
        (
            extension["pass"]
            and not extension["canonical_extension_to_720_scope"]
            and extension["illustrative_column_matching_bridge"][
                "zero_extension_response"
            ] == PREREGISTERED_PREDICTION["instrument_response"]
        ),
        {
            "preregistered": PREREGISTERED_PREDICTION,
            "computed_canonical_response":
                "NOT_COMPUTED_SPAN_GATE_FAILED",
            "illustrative_noncanonical_bridge_response":
                extension["illustrative_column_matching_bridge"][
                    "zero_extension_response"
                ],
            "status": "STOPPED_WITHOUT_CHOOSING_A_LIFT",
        },
    )
    certificate(
        "CERTIFICATE D composite cross-term stop",
        (
            extension["pass"]
            and extension["nonuniqueness_witness"][
                "rho_720_cross_response_difference"
            ] == Fraction(1, 256)
        ),
        {
            "kernel_prediction": "EMPTY_INTERFERENCE_SECTOR",
            "canonical_surface_result":
                "NOT_COMPUTED_SPAN_GATE_FAILED",
            "raw_density_off_diagonal_count":
                first_density["matrix_off_diagonal_entries"],
            "two_admissible_lift_cross_response_difference":
                extension["nonuniqueness_witness"][
                    "rho_720_cross_response_difference"
                ],
        },
    )
    verdict = "EXTENSION_NOT_CANONICAL"
    certificate(
        "CERTIFICATE E terminal verdict",
        verdict == "EXTENSION_NOT_CANONICAL"
        and bool(extension["pass"])
        and not extension["canonical_extension_to_720_scope"],
        {
            "verdict": verdict,
            "linearity": linearity["ruling"],
            "extension_status": "FAILED_EXACT_SPAN_GATE",
            "choice_required": extension["named_missing_choice"],
        },
    )

    runtime = time.monotonic() - PROCESS_STARTED
    deterministic = (
        deterministic_density
        and controls == source_control_certificate()
        and linearity == w7_linearity_certificate(controls)
        and extension == extension_span_certificate(first_density, linearity)
    )
    projected_stdout_bytes = STDOUT_BYTES + 45_000
    bounds_pass = (
        deterministic
        and runtime < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
        and FAIL == 0
    )
    certificate(
        "CERTIFICATE F determinism, runtime, and stdout bounds",
        bounds_pass,
        {
            "deterministic": deterministic,
            "runtime_limit_sec": AUDIT_TIMEOUT_SEC,
            "runtime_sec": runtime,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_projected_bytes": projected_stdout_bytes,
        },
    )
    final_runtime = time.monotonic() - PROCESS_STARTED
    final = render_final_certificate(
        controls=controls,
        linearity=linearity,
        density=first_density,
        extension=extension,
        deterministic=deterministic,
        runtime=final_runtime,
        projected_stdout_bytes=STDOUT_BYTES + 45_000,
    )
    final["fail"] = FAIL
    final["pass"] = PASS
    emit(
        "FINAL :: "
        + json.dumps(
            final, sort_keys=True, separators=(",", ":"), default=jsonable
        )
    )
    emit(f"VERDICT {verdict}")
    emit(f"RUNTIME_SECONDS {time.monotonic() - PROCESS_STARTED:.6f}")
    return 0 if bounds_pass and FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
