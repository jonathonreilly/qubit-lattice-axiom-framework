#!/usr/bin/env python3
"""Finite-box signed pullback primitives for the Cycle-727 runner."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json

import frontier_cycle727_finite_fixtures_2026_07_28 as C
import frontier_cycle727_finite_fixtures_2026_07_28 as M
import frontier_cycle727_finite_factorization_2026_07_28 as O
import frontier_cycle727_finite_pauli_tableau_2026_07_28 as A


Pauli = C.Pauli
Coord = tuple[int, int, int]
FAMILIES = ("free", "seam", "reverse", "contact", "coin")
PRIMARY_REGRESSION_SHAPES = ((2, 2, 2), (3, 2, 2), (3, 3, 2))
HELD_SHAPE = (5, 3, 2)
REGRESSION_SHAPES = PRIMARY_REGRESSION_SHAPES + (HELD_SHAPE,)
PARITY_SECTORS = ((False, "even", +1), (True, "odd", -1))
FROZEN_SECTOR_EXPONENT_PAIRS = {
    (2, 2, 2): (48, 47),
    (3, 2, 2): (72, 71),
    (3, 3, 2): (108, 107),
    (5, 3, 2): (180, 179),
}
FROZEN_DICTIONARY_DIGESTS = {
    (2, 2, 2): "dadb2087ae6604e877d8c406c056fb0d88ed31fceb772daf4093e685fed1797e",
    (3, 2, 2): "c55deffa417b236dc8d98cc55848b4a934d65b4b669f4d43fe44a0aa9e5dfb5f",
    (3, 3, 2): "8214b0b177946978e3093caff08deec409eab384ea1a096d50da0fa5d90ecd89",
    (5, 3, 2): "d3d60bdd877d6f8b1d4fe35be6c7ea9fcbf2ee9a203564fe0fd0654f46e7ccf2",
}
FROZEN_SUPPLY_COUNT_DIGESTS = {
    (2, 2, 2): "7fb346b59906eed6730a96f0b6530ddc3d45fbe5fddf9f37f2717cfd42f9356f",
    (3, 2, 2): "a153fbd0d2edd4e821d6fe50c292b6871532acb74e807016b6587f30b756adc9",
    (3, 3, 2): "ab93f2109967f7fd4b997a1b216caf0872b3fcc30a521d3eca217992724e0f7a",
    (5, 3, 2): "b9d9f50e3900e77e695dd78a699bc73c237a0de3810b9b940089a507009917b6",
}


def pauli_key(row: Pauli) -> str:
    return f"{row.phase}:{row.x:x}:{row.z:x}"


def signed_digest(rows) -> str:
    return sha256("|".join(pauli_key(row) for row in rows).encode()).hexdigest()


def json_digest(value) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def gf2_rank(rows) -> int:
    return A.gf2_rank(rows)


def gf2_in_span(target: int, rows) -> bool:
    rows = tuple(rows)
    return gf2_rank(rows + (target,)) == gf2_rank(rows)


def product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


@dataclass(frozen=True)
class CommonGenerator:
    family: str
    label: str
    target: Pauli
    reference_physical: Pauli
    companion_physical: Pauli


def common_dictionary(
    reference: C.CellEdgeGauge,
    companion: M.CompanionFixture,
) -> tuple[tuple[CommonGenerator, ...], dict[str, object]]:
    """Freeze the unique common even-CAR generators in a stable order.

    The two endpoint-Z rows repeated inside every four-row landed seam tuple
    are represented once by their stable ``free`` labels.  The remaining two
    oriented seam Majorana bilinears are named ``seam`` and ``reverse``.
    The two signed onsite-even Majorana rows for every unordered mode pair are
    named ``contact`` and ``coin`` dictionary basis rows.  These are algebraic
    generator roles, not a claim that a non-Clifford contact/coin gate is
    recompiled here.
    """
    if reference.cells != companion.cells or reference.edges != companion.edges:
        raise ValueError("reference and companion incidence dictionaries differ")

    generators: list[CommonGenerator] = []
    for cell, coordinate in enumerate(reference.cells):
        for local_mode in range(6):
            mode = 6 * cell + local_mode
            row = Pauli(z=1 << mode)
            generators.append(CommonGenerator(
                "free",
                f"free:c{coordinate}:m{local_mode}:q{mode}",
                row,
                row,
                row,
            ))

    for edge, (
        left, right, owner, axis, left_mode, right_mode
    ) in enumerate(reference.edges):
        reference_terms = reference.physical_terms(edge)
        reference_targets = reference.expected_terms(edge)
        companion_terms = companion.physical_terms(edge)
        companion_targets = companion.target_terms(edge)
        if reference_targets != companion_targets:
            raise ValueError(("target seam dictionary mismatch", edge))
        endpoint = (
            f"e{edge}:owner{owner}:a{axis}:"
            f"{left}/{left_mode}->{right}/{right_mode}"
        )
        generators.extend((
            CommonGenerator(
                "seam",
                f"seam:{endpoint}",
                reference_targets[2],
                reference_terms[2],
                companion_terms[2],
            ),
            CommonGenerator(
                "reverse",
                f"reverse:{endpoint}",
                reference_targets[3],
                reference_terms[3],
                companion_terms[3],
            ),
        ))

    for cell, coordinate in enumerate(reference.cells):
        for left_local, right_local in combinations(range(6), 2):
            left = 6 * cell + left_local
            right = 6 * cell + right_local
            endpoints = (1 << left) | (1 << right)
            between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
            contact = Pauli(
                phase=2, x=endpoints, z=between | endpoints
            )
            coin = Pauli(x=endpoints, z=between)
            suffix = f"c{coordinate}:m{left_local}-{right_local}"
            generators.extend((
                CommonGenerator(
                    "contact", f"contact:{suffix}",
                    contact, contact, contact,
                ),
                CommonGenerator(
                    "coin", f"coin:{suffix}",
                    coin, coin, coin,
                ),
            ))

    by_family = {
        family: tuple(row for row in generators if row.family == family)
        for family in FAMILIES
    }
    ordered = tuple(row for family in FAMILIES for row in by_family[family])
    modes = tuple({
        "cell": cell,
        "cell_coordinate": reference.cells[cell],
        "local_mode": local,
        "global_mode": 6 * cell + local,
    } for cell in range(len(reference.cells)) for local in range(6))
    edges = tuple({
        "edge": edge,
        "left_cell": row[0],
        "right_cell": row[1],
        "owner": row[2],
        "axis": row[3],
        "left_mode": row[4],
        "right_mode": row[5],
    } for edge, row in enumerate(reference.edges))
    generator_lists = {
        family: tuple({
            "label": row.label,
            "signed_target": pauli_key(row.target),
        } for row in by_family[family])
        for family in FAMILIES
    }
    payload = {
        "shape": reference.shape,
        "cells": reference.cells,
        "modes": modes,
        "oriented_edges": edges,
        "endpoint_convention": (
            "positive-axis edge owner is the lower coordinate; "
            "left endpoint mode=6*left+2*axis+1 and "
            "right endpoint mode=6*right+2*axis"
        ),
        "generator_order": FAMILIES,
        "signed_generator_lists": generator_lists,
        "duplicate_policy": (
            "the two endpoint-Z members repeated in each landed four-row "
            "seam tuple are represented once by their free-mode labels"
        ),
        "total_parity_convention": (
            "P_total=product of Z on all 6N matter modes; even is s=+1 "
            "(odd=False), odd is s=-1 (odd=True)"
        ),
    }
    payload["family_order_digests"] = {
        family: json_digest(generator_lists[family]) for family in FAMILIES
    }
    payload["frozen_dictionary_digest"] = json_digest(payload)
    return ordered, payload


def reference_orientation(
    fixture,
    generators: tuple[CommonGenerator, ...],
) -> dict[str, object]:
    """Reconstruct C's signed diagonal common-E orientation explicitly."""
    modes = fixture.matter_qubits
    variables = modes * (modes + 1) // 2
    equations: list[tuple[int, int]] = []
    decoded_rows = []
    leakage_failures = 0
    for generator in generators:
        decoded, leakage, stabilizer = fixture.decoded(
            generator.reference_physical
        )
        decoded_rows.append((generator, decoded, leakage, stabilizer))
        leakage_failures += bool(leakage)
        if decoded.x != generator.target.x:
            return {
                "coordinate_system_inconsistent": True,
                "images": (),
                "decoded_rows": tuple(decoded_rows),
                "X_coordinate_failures": 1,
                "logical_leakage_failures": leakage_failures,
            }
        difference = decoded.z ^ generator.target.z
        for output in range(modes):
            mask = 0
            bits = decoded.x
            while bits:
                bit = bits & -bits
                source = bit.bit_length() - 1
                mask ^= 1 << C.symmetric_index(source, output, modes)
                bits ^= bit
            equations.append((mask, (difference >> output) & 1))
    solution, coefficient_rank, contradictions = C.gf2_solve(equations)
    matrix_rows = [0] * modes
    active_pairs = []
    for left in range(modes):
        for right in range(left, modes):
            if (solution >> C.symmetric_index(left, right, modes)) & 1:
                matrix_rows[left] ^= 1 << right
                if left != right:
                    matrix_rows[right] ^= 1 << left
                active_pairs.append((left, right))
    base_images = tuple(
        Pauli(
            phase=(matrix_rows[mode] >> mode) & 1,
            x=1 << mode,
            z=matrix_rows[mode],
        )
        for mode in range(modes)
    ) + tuple(Pauli(z=1 << mode) for mode in range(modes))
    phase_equations = []
    phase_parity_failures = 0
    for generator, decoded, _leakage, _stabilizer in decoded_rows:
        transformed = A.apply_images(base_images, decoded, modes)
        coordinate_match = (
            transformed.x == generator.target.x
            and transformed.z == generator.target.z
        )
        if not coordinate_match:
            raise AssertionError("reference coordinate solve did not replay")
        delta = (generator.target.phase - transformed.phase) % 4
        phase_parity_failures += delta & 1
        phase_equations.append((decoded.x, delta // 2))
    phase_solution, phase_rank, phase_contradictions = C.gf2_solve(
        phase_equations
    )
    images = tuple(
        Pauli(
            phase=(
                ((matrix_rows[mode] >> mode) & 1)
                + 2 * ((phase_solution >> mode) & 1)
            ),
            x=1 << mode,
            z=matrix_rows[mode],
        )
        for mode in range(modes)
    ) + tuple(Pauli(z=1 << mode) for mode in range(modes))
    replay_failures = sum(
        (
            transformed.phase != generator.target.phase
            or transformed.x != generator.target.x
            or transformed.z != generator.target.z
        )
        for generator, decoded, _leakage, _stabilizer in decoded_rows
        for transformed in (
            A.apply_images(images, decoded, modes),
        )
    )
    return {
        "coordinate_system_inconsistent": False,
        "symmetric_variables": variables,
        "equations": len(equations),
        "coefficient_rank": coefficient_rank,
        "augmented_contradictions": contradictions,
        "phase_rank": phase_rank,
        "phase_parity_failures": phase_parity_failures,
        "phase_contradictions": phase_contradictions,
        "logical_leakage_failures": leakage_failures,
        "replay_failures": replay_failures,
        "active_diagonal_terms": len(active_pairs),
        "images": images,
        "decoded_rows": tuple(decoded_rows),
    }


def cell_diameter(cells: tuple[Coord, ...]) -> int:
    return max((
        sum(abs(a - b) for a, b in zip(left, right))
        for left in cells for right in cells
    ), default=0)


def reference_support_cells(
    fixture: C.CellEdgeGauge,
    row: Pauli,
) -> tuple[Coord, ...]:
    support = row.x | row.z
    cells = set()
    for qubit in range(fixture.qubits):
        if not ((support >> qubit) & 1):
            continue
        if qubit < fixture.matter_qubits:
            cells.add(fixture.cells[qubit // 6])
        else:
            edge = qubit - fixture.matter_qubits
            left, right = fixture.edges[edge][:2]
            cells.add(fixture.cells[left])
            cells.add(fixture.cells[right])
    return tuple(sorted(cells))


def companion_support_cells(
    fixture: M.CompanionFixture,
    row: Pauli,
) -> tuple[Coord, ...]:
    support = row.x | row.z
    return tuple(sorted({
        fixture.cells[M.qubit_cell(fixture, qubit)]
        for qubit in range(fixture.qubits)
        if (support >> qubit) & 1
    }))


def target_support_cells(
    fixture: M.CompanionFixture,
    row: Pauli,
) -> tuple[Coord, ...]:
    support = row.x | row.z
    return tuple(sorted({
        fixture.cells[mode // 6]
        for mode in range(fixture.matter_qubits)
        if (support >> mode) & 1
    }))


def locality_row(
    reference: C.CellEdgeGauge,
    companion: M.CompanionFixture,
    generator: CommonGenerator,
) -> dict[str, object]:
    reference_cells = reference_support_cells(
        reference, generator.reference_physical
    )
    companion_cells = companion_support_cells(
        companion, generator.companion_physical
    )
    target_cells = target_support_cells(companion, generator.target)
    return {
        "semantic_cell_diameter": (
            1 if generator.family in ("seam", "reverse") else 0
        ),
        "reference_weight": (
            generator.reference_physical.x
            | generator.reference_physical.z
        ).bit_count(),
        "reference_cell_diameter": cell_diameter(reference_cells),
        "companion_weight": (
            generator.companion_physical.x
            | generator.companion_physical.z
        ).bit_count(),
        "companion_cell_diameter": cell_diameter(companion_cells),
        "target_weight": (generator.target.x | generator.target.z).bit_count(),
        "target_cell_diameter": cell_diameter(target_cells),
    }


def family_locality_census(rows: tuple[dict[str, object], ...]) -> dict[str, int]:
    keys = (
        "semantic_cell_diameter",
        "reference_weight",
        "reference_cell_diameter",
        "companion_weight",
        "companion_cell_diameter",
        "target_weight",
        "target_cell_diameter",
    )
    return {
        f"maximum_{key}": max((int(row[key]) for row in rows), default=0)
        for key in keys
    }


def fixed_sector_target(
    factor: O.Factorization,
    row: Pauli,
    odd: bool,
) -> Pauli:
    """Canonical signed representative of a target row modulo P_total=s."""
    coordinates = A.decode(
        row,
        factor.target_w,
        factor.target_v,
        factor.fixture.matter_qubits,
    )
    base = product(
        factor.target_v[index]
        for index in range(factor.logical)
        if (coordinates.v_mask >> index) & 1
    ) @ product(
        factor.target_w[index]
        for index in range(factor.logical)
        if (coordinates.w_mask >> index) & 1
    )
    parity_coordinate = (
        coordinates.w_mask >> factor.logical
    ) & 1
    return Pauli(
        (
            base.phase + coordinates.phase
            + 2 * int(odd) * parity_coordinate
        ) % 4,
        base.x,
        base.z,
    )


def companion_signed_pullback(
    factor: O.Factorization,
    row: Pauli,
    odd: bool,
) -> tuple[Pauli, object]:
    """Signed companion pullback, retaining the input row's actual phase."""
    coordinates = A.decode(
        row,
        factor.physical_w,
        factor.physical_v,
        factor.fixture.qubits,
    )
    base = product(
        factor.target_v[index]
        for index in range(factor.logical)
        if (coordinates.v_mask >> index) & 1
    ) @ product(
        factor.target_w[index]
        for index in range(factor.logical)
        if (coordinates.w_mask >> index) & 1
    )
    physical_parity_coordinate = (
        coordinates.w_mask
        >> (factor.logical + factor.gauge + factor.center - 1)
    ) & 1
    pullback = Pauli(
        (
            base.phase + coordinates.phase
            + 2 * int(odd) * physical_parity_coordinate
        ) % 4,
        base.x,
        base.z,
    )
    return pullback, coordinates
