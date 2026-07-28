#!/usr/bin/env python3
"""Cycle-727 bounded reference-to-companion cross-code equivalence.

This runner relates, without merging, the landed ``CellEdgeGauge`` and
``EulerMarkerGauge`` reference surfaces to the fixed-sector companion surface.
It freezes one common signed even-CAR generator dictionary, computes exact
signed pullbacks generator by generator in both supplied parity sectors, and
keeps rank, phase, gauge, center/parity supply, and locality as separate
certificates.

The two inequivalences required by the scope authority are positive findings:
two separately supplied fixed-parity companion channels are not a full-sector
isometry, and the Euler marker census has no count-preserving map to companion
ports/gauge pairs/center signs/coframe bits.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations
import json
import time

import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M


Pauli = C.Pauli
Coord = tuple[int, int, int]
FAMILIES = ("free", "seam", "reverse", "contact", "coin")
PRIMARY_REGRESSION_SHAPES = ((2, 2, 2), (3, 2, 2), (3, 3, 2))
HELD_SHAPE = (5, 3, 2)
REGRESSION_SHAPES = PRIMARY_REGRESSION_SHAPES + (HELD_SHAPE,)
PARITY_SECTORS = ((False, "even", +1), (True, "odd", -1))
FROZEN_MARKER_CENSUSES = {
    (2, 2, 2): (8, 12, 6, 1),
    (3, 2, 2): (12, 20, 11, 2),
    (3, 3, 2): (18, 33, 20, 4),
    (5, 3, 2): (30, 59, 38, 8),
}
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
FAILURES = 0


def check(label: str, condition: bool, detail=None) -> None:
    """Emit the required PASS/FAIL line without hiding failed subcriteria."""
    global FAILURES
    passed = bool(condition)
    FAILURES += not passed
    print("PASS" if passed else "FAIL", label, "::", detail)


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
    return C.R.F.base.gf2_rank(rows)


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
        transformed = C.R.C709.apply_images(base_images, decoded, modes)
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
            C.R.C709.apply_images(images, decoded, modes),
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
    coordinates = O.T.decode(
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
    coordinates = O.T.decode(
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


def analyze_shape(shape: tuple[int, int, int]) -> dict[str, object]:
    """Compute every signed pullback and all five orthogonal audits."""
    reference = C.CellEdgeGauge.build(shape)
    euler = C.EulerMarkerGauge.build(shape)
    companion = M.CompanionFixture.build(shape)
    generators, dictionary = common_dictionary(reference, companion)
    cell_orientation = reference_orientation(reference, generators)
    euler_orientation = reference_orientation(euler, generators)
    factor = O.build_factorization(companion)
    mask_gauge = (1 << factor.gauge) - 1
    mask_center = (1 << factor.center) - 1
    generator_certificates = []
    pullbacks: dict[tuple[str, str, str], list[Pauli]] = {}
    sector_targets: dict[tuple[str, str], list[Pauli]] = {}
    full_reference_pullbacks: dict[tuple[str, str], list[Pauli]] = {}
    localities: dict[str, list[dict[str, object]]] = {
        family: [] for family in FAMILIES
    }

    for index, (
        generator,
        cell_decoded,
        euler_decoded,
    ) in enumerate(zip(
        generators,
        cell_orientation["decoded_rows"],
        euler_orientation["decoded_rows"],
    )):
        _cell_generator, cell_logical, cell_leakage, cell_supply = cell_decoded
        _euler_generator, euler_logical, euler_leakage, euler_supply = (
            euler_decoded
        )
        cell_pullback = C.R.C709.apply_images(
            cell_orientation["images"], cell_logical, reference.matter_qubits
        )
        euler_pullback = C.R.C709.apply_images(
            euler_orientation["images"], euler_logical, euler.matter_qubits
        )
        full_reference_pullbacks.setdefault(
            (generator.family, "CellEdgeGauge"), []
        ).append(cell_pullback)
        full_reference_pullbacks.setdefault(
            (generator.family, "EulerMarkerGauge"), []
        ).append(euler_pullback)
        _companion_even, companion_coordinates = companion_signed_pullback(
            factor, generator.companion_physical, False
        )
        companion_gauge_v = (
            companion_coordinates.v_mask >> factor.logical
        ) & mask_gauge
        companion_gauge_w = (
            companion_coordinates.w_mask >> factor.logical
        ) & mask_gauge
        center_mask = (
            companion_coordinates.w_mask
            >> (factor.logical + factor.gauge)
        ) & mask_center
        local_center_mask = center_mask & ((1 << (factor.center - 1)) - 1)
        parity_coordinate = (
            center_mask >> (factor.center - 1)
        ) & 1
        locality = locality_row(reference, companion, generator)
        localities[generator.family].append(locality)
        sectors = {}
        for odd, sector, sector_sign in PARITY_SECTORS:
            target_sector = fixed_sector_target(
                factor, generator.target, odd
            )
            cell_sector_pullback = fixed_sector_target(
                factor, cell_pullback, odd
            )
            euler_sector_pullback = fixed_sector_target(
                factor, euler_pullback, odd
            )
            companion_pullback, _coordinates = companion_signed_pullback(
                factor, generator.companion_physical, odd
            )
            for surface, row in (
                ("CellEdgeGauge", cell_sector_pullback),
                ("EulerMarkerGauge", euler_sector_pullback),
                ("CompanionFixture", companion_pullback),
            ):
                pullbacks.setdefault(
                    (generator.family, surface, sector), []
                ).append(row)
            sector_targets.setdefault(
                (generator.family, sector), []
            ).append(target_sector)
            signed_rows = {
                "target_fixed_sector": pauli_key(target_sector),
                "CellEdgeGauge_full": pauli_key(cell_pullback),
                "CellEdgeGauge_fixed_sector": pauli_key(
                    cell_sector_pullback
                ),
                "EulerMarkerGauge_full": pauli_key(euler_pullback),
                "EulerMarkerGauge_fixed_sector": pauli_key(
                    euler_sector_pullback
                ),
                "CompanionFixture_fixed_sector": pauli_key(
                    companion_pullback
                ),
            }
            sectors[sector] = {
                "sector_sign": sector_sign,
                "signed_rows_digest": json_digest(signed_rows),
                "rank_bits": {
                    "target": int(bool(
                        target_sector.x | target_sector.z
                    )),
                    "CellEdgeGauge": int(bool(
                        cell_sector_pullback.x | cell_sector_pullback.z
                    )),
                    "EulerMarkerGauge": int(bool(
                        euler_sector_pullback.x | euler_sector_pullback.z
                    )),
                    "CompanionFixture": int(bool(
                        companion_pullback.x | companion_pullback.z
                    )),
                },
                "phase_agreement": {
                    "CellEdgeGauge": (
                        cell_sector_pullback.phase == target_sector.phase
                    ),
                    "EulerMarkerGauge": (
                        euler_sector_pullback.phase == target_sector.phase
                    ),
                    "CompanionFixture": (
                        companion_pullback.phase == target_sector.phase
                    ),
                },
                "coordinate_agreement": {
                    "CellEdgeGauge": (
                        cell_sector_pullback.x == target_sector.x
                        and cell_sector_pullback.z == target_sector.z
                    ),
                    "EulerMarkerGauge": (
                        euler_sector_pullback.x == target_sector.x
                        and euler_sector_pullback.z == target_sector.z
                    ),
                    "CompanionFixture": (
                        companion_pullback.x == target_sector.x
                        and companion_pullback.z == target_sector.z
                    ),
                },
                "gauge_leakage": {
                    "CellEdgeGauge_nonmatter_v_mask": cell_leakage,
                    "EulerMarkerGauge_nonmatter_v_mask": euler_leakage,
                    "CompanionFixture_gauge_v_mask": companion_gauge_v,
                    "CompanionFixture_gauge_w_mask": companion_gauge_w,
                },
                "center_parity_supply": {
                    "CellEdgeGauge_constraint_w_mask": cell_supply,
                    "CellEdgeGauge_parity": "retained_not_supplied",
                    "EulerMarkerGauge_constraint_w_mask": euler_supply,
                    "EulerMarkerGauge_parity": (
                        "both_sectors_in_one_root_free_register"
                    ),
                    "CompanionFixture_local_center_mask": local_center_mask,
                    "CompanionFixture_parity_coordinate": parity_coordinate,
                    "CompanionFixture_parity": (
                        f"externally_supplied_s={sector_sign:+d}"
                    ),
                },
            }
        generator_certificates.append({
            "index": index,
            "family": generator.family,
            "label": generator.label,
            "signed_target": pauli_key(generator.target),
            "locality": locality,
            "sectors": sectors,
        })

    family_tables = {}
    for family in FAMILIES:
        selected = tuple(
            row for row in generators if row.family == family
        )
        targets = tuple(row.target for row in selected)
        full_target_rank = gf2_rank(
            row.symplectic(companion.matter_qubits) for row in targets
        )
        full_reference_ranks = {
            surface: gf2_rank(
                row.symplectic(companion.matter_qubits)
                for row in full_reference_pullbacks[(family, surface)]
            )
            for surface in ("CellEdgeGauge", "EulerMarkerGauge")
        }
        sector_tables = {}
        for _odd, sector, _sector_sign in PARITY_SECTORS:
            target_rank = gf2_rank(
                row.symplectic(companion.matter_qubits)
                for row in sector_targets[(family, sector)]
            )
            ranks = {
                surface: gf2_rank(
                    row.symplectic(companion.matter_qubits)
                    for row in pullbacks[(family, surface, sector)]
                )
                for surface in (
                    "CellEdgeGauge", "EulerMarkerGauge", "CompanionFixture"
                )
            }
            family_records = tuple(
                row for row in generator_certificates
                if row["family"] == family
            )
            phase_failures = {
                surface: sum(
                    not row["sectors"][sector]["phase_agreement"][surface]
                    for row in family_records
                )
                for surface in (
                    "CellEdgeGauge", "EulerMarkerGauge", "CompanionFixture"
                )
            }
            coordinate_failures = {
                surface: sum(
                    not row["sectors"][sector]["coordinate_agreement"][surface]
                    for row in family_records
                )
                for surface in (
                    "CellEdgeGauge", "EulerMarkerGauge", "CompanionFixture"
                )
            }
            leakage_totals = {
                key: sum(
                    int(row["sectors"][sector]["gauge_leakage"][key]).bit_count()
                    for row in family_records
                )
                for key in (
                    "CellEdgeGauge_nonmatter_v_mask",
                    "EulerMarkerGauge_nonmatter_v_mask",
                    "CompanionFixture_gauge_v_mask",
                    "CompanionFixture_gauge_w_mask",
                )
            }
            center_counts = {
                "CellEdgeGauge_constraint_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "CellEdgeGauge_constraint_w_mask"
                    ])
                    for row in family_records
                ),
                "EulerMarkerGauge_constraint_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "EulerMarkerGauge_constraint_w_mask"
                    ])
                    for row in family_records
                ),
                "CompanionFixture_local_center_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "CompanionFixture_local_center_mask"
                    ])
                    for row in family_records
                ),
                "CompanionFixture_parity_supplied_rows": sum(
                    bool(row["sectors"][sector]["center_parity_supply"][
                        "CompanionFixture_parity_coordinate"
                    ])
                    for row in family_records
                ),
            }
            sector_tables[sector] = {
                "target_rank": target_rank,
                "pullback_ranks": ranks,
                "rank_agreement": all(
                    rank == target_rank for rank in ranks.values()
                ),
                "phase_failures": phase_failures,
                "coordinate_failures": coordinate_failures,
                "gauge_leakage_bit_totals": leakage_totals,
                "center_parity_supply_counts": center_counts,
                "center_parity_classification": {
                    "CellEdgeGauge": (
                        "constraint rows are +1 supplies; total matter parity "
                        "is retained because the root Gauss row is omitted"
                    ),
                    "EulerMarkerGauge": (
                        "marker/equality/Gauss rows are +1 supplies; both "
                        "matter-parity sectors remain in one register"
                    ),
                    "CompanionFixture": (
                        "local center signs are fixed and total parity is the "
                        f"external sector label s={+1 if sector == 'even' else -1:+d}"
                    ),
                },
            }
        family_tables[family] = {
            "generator_count": len(selected),
            "ordered_label_digest": json_digest(
                tuple(row.label for row in selected)
            ),
            "signed_target_digest": signed_digest(targets),
            "full_sector_target_rank": full_target_rank,
            "full_sector_reference_pullback_ranks": full_reference_ranks,
            "sectors": sector_tables,
            "locality_census": family_locality_census(
                tuple(localities[family])
            ),
        }

    rank_exact = all(
        table["sectors"][sector]["rank_agreement"]
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    phase_exact = all(
        not any(table["sectors"][sector]["phase_failures"].values())
        and not any(table["sectors"][sector]["coordinate_failures"].values())
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    zero_gauge_leakage = all(
        not any(
            table["sectors"][sector][
                "gauge_leakage_bit_totals"
            ].values()
        )
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    locality_certified = all(
        table["locality_census"]["maximum_semantic_cell_diameter"] <= (
            0 if family in ("free", "contact", "coin") else 1
        )
        and table["locality_census"]["maximum_companion_cell_diameter"] <= (
            0 if family in ("free", "contact", "coin") else 1
        )
        and table["locality_census"]["maximum_reference_cell_diameter"] <= (
            0 if family in ("free", "contact", "coin") else 3
        )
        for family, table in family_tables.items()
    )
    supply_classified = all(
        table["sectors"][sector]["center_parity_classification"]
        for table in family_tables.values()
        for _odd, sector, _sign in PARITY_SECTORS
    )
    exact = (
        rank_exact
        and phase_exact
        and zero_gauge_leakage
        and locality_certified
        and supply_classified
        and not cell_orientation["coordinate_system_inconsistent"]
        and not euler_orientation["coordinate_system_inconsistent"]
        and cell_orientation["augmented_contradictions"] == 0
        and euler_orientation["augmented_contradictions"] == 0
        and cell_orientation["phase_contradictions"] == 0
        and euler_orientation["phase_contradictions"] == 0
        and cell_orientation["replay_failures"] == 0
        and euler_orientation["replay_failures"] == 0
        and factor.phase_contradictions == 0
    )
    public = {
        "shape": shape,
        "cells": len(reference.cells),
        "oriented_edges": len(reference.edges),
        "dictionary": dictionary,
        "dictionary_match": {
            "identical_cells": reference.cells == companion.cells,
            "identical_oriented_edges": reference.edges == companion.edges,
            "identical_matter_mode_count": (
                reference.matter_qubits == companion.matter_qubits
            ),
        },
        "reference_orientations": {
            "CellEdgeGauge": {
                key: value for key, value in cell_orientation.items()
                if key not in ("images", "decoded_rows")
            },
            "EulerMarkerGauge": {
                key: value for key, value in euler_orientation.items()
                if key not in ("images", "decoded_rows")
            },
        },
        "companion_factorization": {
            "logical_qubits": factor.logical,
            "gauge_pairs": factor.gauge,
            "center_signs_including_parity": factor.center,
            "local_center_rank": factor.local_center_rank,
            "phase_rank": factor.phase_rank,
            "phase_contradictions": factor.phase_contradictions,
        },
        "separate_certificates": {
            "rank_agreement": rank_exact,
            "phase_agreement": phase_exact,
            "zero_gauge_leakage": zero_gauge_leakage,
            "center_parity_supply_classified": supply_classified,
            "locality_census_certified": locality_certified,
        },
        "family_tables": family_tables,
        "per_generator_certificate_count": len(generator_certificates),
        "per_generator_certificates": tuple({
            "index": row["index"],
            "family": row["family"],
            "label": row["label"],
            "certificate_digest": json_digest(row),
        } for row in generator_certificates),
        "per_generator_certificate_digest": json_digest(
            generator_certificates
        ),
        "per_family_generator_certificate_digests": {
            family: json_digest(tuple(
                row for row in generator_certificates
                if row["family"] == family
            ))
            for family in FAMILIES
        },
        "cross_code_pullbacks_exact": exact,
    }
    return {
        "public": public,
        "factor": factor,
        "euler": euler,
        "generators": generators,
    }


def c_anchor_rerun() -> dict[str, object]:
    """Rerun C's unchanged public certificate entry points and main criteria."""
    fixtures = tuple(
        C.CellEdgeGauge.build(shape) for shape in PRIMARY_REGRESSION_SHAPES
    )
    constraints = tuple(
        C.constraint_and_update_certificate(row) for row in fixtures
    )
    root_common_e = tuple(C.diagonal_common_e(row) for row in fixtures)
    euler_fixtures = tuple(
        C.EulerMarkerGauge.build(shape) for shape in PRIMARY_REGRESSION_SHAPES
    )
    euler_constraints = tuple(
        C.euler_marker_certificate(row) for row in euler_fixtures
    )
    common_e = tuple(C.diagonal_common_e(row) for row in euler_fixtures)
    covariance = C.schedule_covariance_certificate()
    mass_contact = C.R.C703.mass_and_contact_certificate()
    criteria = (
        (
            "C.local_plaquette_capacity",
            all(
                row["local_plaquette_rank"] == row["cycle_space_rank"]
                and row[
                    "fundamental_path_loops_outside_local_plaquette_span"
                ] == 0
                and row["full_tableau_rank"]
                == row["matter_qubits"] + row["edge_gauge_qubits"]
                and row["code_exponent"] == row["matter_qubits"]
                and row["maximum_local_plaquette_weight"] <= 9
                for row in constraints
            ),
        ),
        (
            "C.edge_gauge_seam_schedule",
            all(
                row["term_stabilizer_commutator_failures"] == 0
                and row["same_phase_support_collisions"] == 0
                and row["shared_edge_register_use_minimum"] == 1
                and row["shared_edge_register_use_maximum"] == 1
                and row["delete_gauge_A_Gauss_syndrome_minimum"] > 0
                and row["delete_one_independent_loop_rank_maximum"]
                == row["independent_loop_rank"] - 1
                for row in constraints
            ),
        ),
        (
            "C.Euler_marker_full_sector",
            all(
                row["Euler_characteristic"] == 1
                and row["marker_count_parity"] == 1
                and row["marker_equality_rank"]
                == row["Euler_marker_qubits"] - 1
                and row["independent_marker_equality_rank"]
                == row["Euler_marker_qubits"] - 1
                and row["omitted_root_Gauss_rows"] == 0
                and row["full_tableau_rank"] == row["physical_qubits"]
                and row["code_exponent"] == row["matter_qubits"]
                and row["term_stabilizer_commutator_failures"] == 0
                and row["delete_gauge_A_Gauss_syndrome_minimum"] == 2
                and row["delete_one_marker_equality_rank_maximum"]
                == row["independent_marker_equality_rank"] - 1
                and not row["runtime_global_parity_query_used"]
                for row in euler_constraints
            ),
        ),
        (
            "C.signed_common_E",
            all(
                not row["coordinate_system_inconsistent"]
                and row["augmented_contradictions"] == 0
                and row["phase_contradictions"] == 0
                and row["phase_equation_replay_failures"] == 0
                and row["logical_leakage_failures"] == 0
                and row["stabilizer_commutator_failures"] == 0
                and row["transformed_logical_term_failures"] == 0
                and not any(row["transformed_family_failures"].values())
                for row in common_e
            ),
        ),
        (
            "C.nonlocal_E_and_supplied_marker_sector",
            all(
                row["restricted_coordinate_systems"][
                    "cell_radius_2"
                ]["contradictions"] > 0
                and row["maximum_cross_cell_CZ_distance"] > 2
                for row in common_e
            )
            and all(
                row["global_marker_sector_preparation_supplied"]
                for row in euler_constraints
            ),
        ),
        (
            "C.schedule_covariance",
            covariance["proper_cubic_frames"] == 24
            and covariance["frame_colour_bijection_failures"] == 0
            and covariance["ordered_frame_products"] == 576
            and covariance["frame_colour_product_failures"] == 0
            and covariance["translation_colour_failures"] == 0,
        ),
        (
            "C.mass_contact",
            mass_contact["one_particle_coin_eigen_residual"] < C.R.TOL
            and mass_contact["one_particle_mass_residual"] < C.R.TOL
            and mass_contact[
                "contact_vacuum_and_one_particle_residual"
            ] < C.R.TOL
            and mass_contact[
                "contact_double_occupation_phase_residual"
            ] < C.R.TOL,
        ),
    )
    return {
        "criteria": tuple({
            "name": name, "pass": bool(passed)
        } for name, passed in criteria),
        "criteria_count": len(criteria),
        "passed_count": sum(bool(passed) for _name, passed in criteria),
        "fixture_count": len(fixtures),
        "root_common_E_rerun_count": len(root_common_e),
        "Euler_common_E_rerun_count": len(common_e),
        "proper_cubic_frames": covariance["proper_cubic_frames"],
        "ordered_frame_products": covariance["ordered_frame_products"],
        "certificate_digest": json_digest({
            "constraints": constraints,
            "root_common_E": tuple(
                {key: value for key, value in row.items()
                 if key != "active_pairs"}
                for row in root_common_e
            ),
            "Euler": euler_constraints,
            "common_E": tuple(
                {key: value for key, value in row.items()
                 if key != "active_pairs"}
                for row in common_e
            ),
            "covariance": covariance,
            "mass_contact": mass_contact,
        }),
        "all_pass": all(passed for _name, passed in criteria),
    }


def o_anchor_rerun() -> dict[str, object]:
    """Rerun O's public three-axis and four-completion Choi entry points."""
    certificates = tuple(O.comparison_certificate(axis) for axis in range(3))
    held = O.held_edge_certificate()
    criteria = (
        (
            "O.rank_23_shared_domain",
            all(
                len({
                    row["domain_digest"] for row in certificate["patches"]
                }) == 1
                and all(
                    row["domain_rank"] == 23
                    for row in certificate["patches"]
                )
                and all(
                    row["domain_basis_mismatches"] == 0
                    for row in certificate["comparisons"]
                )
                for certificate in certificates
            ),
        ),
        (
            "O.bounded_canonical_patch_encoders",
            all(
                row["canonical_encoder_maximum_diameter"] <= 3
                for certificate in certificates
                for row in certificate["patches"]
            ),
        ),
        (
            "O.two_star_union_both_parities",
            all(
                row["binary_Choi_map_mismatches"] == 0
                and row["even_signed_Choi_map_mismatches"] == 0
                and row["odd_signed_Choi_map_mismatches"] == 0
                for certificate in certificates
                for row in certificate["comparisons"]
            ),
        ),
        (
            "O.held_completion_independence",
            all(
                row["domain_basis_mismatches"] == 0
                and row["even_signed_Choi_map_mismatches"] == 0
                and row["odd_signed_Choi_map_mismatches"] == 0
                for row in held["comparisons"]
            ),
        ),
        (
            "O.active_parity_rail_deletion",
            any(
                row["scalarize_patch_parity_deletion_mismatches"] > 0
                for certificate in certificates
                for row in certificate["comparisons"]
            ),
        ),
    )
    phase_contradictions = sum(
        row["phase_contradictions"]
        for certificate in certificates
        for row in certificate["patches"]
    ) + sum(
        row["phase_contradictions"] for row in held["fixtures"]
    )
    axes = tuple(certificate["axis"] for certificate in certificates)
    star_patch_count = sum(
        row["label"] in ("star_A", "star_B")
        for certificate in certificates for row in certificate["patches"]
    )
    union_patch_count = sum(
        row["label"] == "union"
        for certificate in certificates for row in certificate["patches"]
    )
    return {
        "criteria": tuple({
            "name": name, "pass": bool(passed)
        } for name, passed in criteria),
        "criteria_count": len(criteria),
        "passed_count": sum(bool(passed) for _name, passed in criteria),
        "axes": axes,
        "seven_cell_star_reruns": star_patch_count,
        "twelve_cell_union_reruns": union_patch_count,
        "overlap_physical_qubits": tuple(
            certificate["overlap_physical_qubits"]
            for certificate in certificates
        ),
        "rank_23_patch_domains": sum(
            row["domain_rank"] == 23
            for certificate in certificates
            for row in certificate["patches"]
        ),
        "held_completion_shapes": tuple(
            row["shape"] for row in held["fixtures"]
        ),
        "held_completion_count": len(held["fixtures"]),
        "phase_contradictions": phase_contradictions,
        "certificate_digest": json_digest({
            "axes": certificates,
            "held": held,
        }),
        "all_pass": (
            all(passed for _name, passed in criteria)
            and phase_contradictions == 0
        ),
    }


def full_sector_obstruction(
    bundles: tuple[dict[str, object], ...],
) -> dict[str, object]:
    rows = []
    for bundle in bundles:
        public = bundle["public"]
        factor = bundle["factor"]
        euler = bundle["euler"]
        matter_exponent = euler.matter_qubits
        sector_exponent = factor.logical
        full_dimension = 1 << matter_exponent
        sector_dimension = 1 << sector_exponent
        full_operator_dimension = full_dimension * full_dimension
        supplied_diagonal_operator_dimension = (
            2 * sector_dimension * sector_dimension
        )
        missing_off_diagonal_operator_dimension = (
            full_operator_dimension - supplied_diagonal_operator_dimension
        )
        rows.append({
            "shape": public["shape"],
            "matter_modes": matter_exponent,
            "EulerMarkerGauge_physical_qubits": euler.qubits,
            "EulerMarkerGauge_stabilizer_rank": (
                euler.qubits - matter_exponent
            ),
            "EulerMarkerGauge_full_sector_exponent": matter_exponent,
            "EulerMarkerGauge_full_sector_dimension": full_dimension,
            "CompanionFixture_fixed_sector_logical_exponent": (
                sector_exponent
            ),
            "CompanionFixture_each_fixed_sector_dimension": sector_dimension,
            "two_sector_dimension_sum": 2 * sector_dimension,
            "dimension_sum_matches_only_after_external_direct_sum": (
                2 * sector_dimension == full_dimension
            ),
            "single_sector_dimension_deficit_factor": (
                full_dimension // sector_dimension
            ),
            "full_operator_space_dimension": full_operator_dimension,
            "two_separately_supplied_diagonal_block_dimension": (
                supplied_diagonal_operator_dimension
            ),
            "missing_off_diagonal_sector_block_dimension": (
                missing_off_diagonal_operator_dimension
            ),
            "missing_off_diagonal_sector_blocks": 2,
            "structure_obstruction": (
                "E_+ and E_- are separately called channels indexed by an "
                "externally supplied classical sector.  They specify the two "
                "diagonal blocks but no common linear direct-sum channel and "
                "no action on Hom(H_+,H_-) or Hom(H_-,H_+)."
            ),
            "single_run_isometry_dimension_match": (
                sector_dimension == full_dimension
            ),
        })
    certified = all(
        row["CompanionFixture_fixed_sector_logical_exponent"]
        == row["EulerMarkerGauge_full_sector_exponent"] - 1
        and row["dimension_sum_matches_only_after_external_direct_sum"]
        and row["single_sector_dimension_deficit_factor"] == 2
        and row["missing_off_diagonal_sector_block_dimension"] > 0
        and not row["single_run_isometry_dimension_match"]
        for row in rows
    )
    return {
        "finding": (
            "running s=+1 and s=-1 separately does not define an isometry "
            "from the one-register EulerMarkerGauge full-sector code"
        ),
        "rows": tuple(rows),
        "obstruction_certified": certified,
        "full_sector_isometry_exists": False,
        "sector_summed_companion_channel_constructed": False,
    }


def marker_map_census(
    bundles: tuple[dict[str, object], ...],
) -> dict[str, object]:
    rows = []
    for bundle in bundles:
        public = bundle["public"]
        factor = bundle["factor"]
        euler = bundle["euler"]
        marker_counts = {
            kind: sum(row[0] == kind for row in euler.marker_objects)
            for kind in ("vertex", "edge", "face", "cube")
        }
        companion_counts = {
            "directed_ports": 6 * len(euler.cells),
            "gauge_pairs": factor.gauge,
            "center_signs": factor.center,
            "coframe_bits": 3 * len(euler.cells),
        }
        left = tuple(marker_counts.values())
        right = tuple(companion_counts.values())
        count_preserving_class_permutations = sum(
            all(left[index] == right[target] for index, target in enumerate(order))
            for order in permutations(range(4))
        )
        rows.append({
            "shape": public["shape"],
            "Euler_marker_classes": marker_counts,
            "Euler_marker_total": len(euler.marker_objects),
            "companion_structural_classes": companion_counts,
            "companion_qubits_for_six_directed_ports": (
                3 * len(euler.cells)
            ),
            "local_center_signs_excluding_total_parity": factor.center - 1,
            "total_parity_signs": 1,
            "count_preserving_class_permutations": (
                count_preserving_class_permutations
            ),
        })
    certified = all(
        row["count_preserving_class_permutations"] == 0 for row in rows
    )
    return {
        "scope": (
            "box-level object-count census only; this is not a "
            "route-independence theorem and supplies no semantic marker map"
        ),
        "rows": tuple(rows),
        "no_count_preserving_correspondence_certified": certified,
        "marker_to_coframe_correspondence_exists": False,
    }


def sign_corruption_control(bundle: dict[str, object]) -> dict[str, object]:
    certificate = bundle["public"]["per_generator_certificates"][0]
    target = bundle["generators"][0].target
    corrupted = Pauli((target.phase + 2) % 4, target.x, target.z)
    coordinate_agreement = (
        corrupted.x == target.x and corrupted.z == target.z
    )
    phase_agreement = corrupted.phase == target.phase
    return {
        "generator": certificate["label"],
        "original": pauli_key(target),
        "corrupted": pauli_key(corrupted),
        "coordinate_agreement_after_corruption": coordinate_agreement,
        "phase_agreement_after_corruption": phase_agreement,
        "pullback_certificate_pass_after_corruption": (
            coordinate_agreement and phase_agreement
        ),
        "detected": (
            coordinate_agreement
            and not phase_agreement
            and corrupted != target
        ),
    }


def dictionary_permutation_control(
    bundle: dict[str, object],
) -> dict[str, object]:
    public = bundle["public"]
    generators = list(bundle["generators"])
    if len(generators) < 2 or generators[0].family != generators[1].family:
        raise AssertionError("control requires two leading free generators")
    generators[0], generators[1] = generators[1], generators[0]
    original_payload = public["dictionary"]
    permuted_lists = {
        family: tuple({
            "label": row.label,
            "signed_target": pauli_key(row.target),
        } for row in generators if row.family == family)
        for family in FAMILIES
    }
    permuted_payload = {
        key: value for key, value in original_payload.items()
        if key not in ("signed_generator_lists", "family_order_digests",
                       "frozen_dictionary_digest")
    }
    permuted_payload["signed_generator_lists"] = permuted_lists
    permuted_payload["family_order_digests"] = {
        family: json_digest(permuted_lists[family]) for family in FAMILIES
    }
    permuted_digest = json_digest(permuted_payload)
    original_digest = original_payload["frozen_dictionary_digest"]
    changed_family_tables = tuple(
        family for family in FAMILIES
        if original_payload["family_order_digests"][family]
        != permuted_payload["family_order_digests"][family]
    )
    return {
        "permutation": "swap dictionary entries 0 and 1",
        "original_dictionary_digest": original_digest,
        "permuted_dictionary_digest": permuted_digest,
        "dictionary_digest_changed": original_digest != permuted_digest,
        "family_tables_detecting_permutation": changed_family_tables,
        "per_family_table_detected": "free" in changed_family_tables,
        "detected": (
            original_digest != permuted_digest
            and "free" in changed_family_tables
        ),
    }


def missing_anchor_control(
    c_anchors: dict[str, object],
    o_anchors: dict[str, object],
) -> dict[str, object]:
    registry = {
        row["name"]: row["pass"]
        for row in c_anchors["criteria"] + o_anchors["criteria"]
    }
    expected = tuple(registry)
    deleted_name = "O.held_completion_independence"
    corrupted = {
        key: value for key, value in registry.items()
        if key != deleted_name
    }
    missing = tuple(name for name in expected if name not in corrupted)
    passes_after_deletion = (
        not missing and all(corrupted.get(name, False) for name in expected)
    )
    return {
        "deleted_anchor": deleted_name,
        "named_missing_anchors": missing,
        "anchor_registry_pass_after_deletion": passes_after_deletion,
        "detected": missing == (deleted_name,) and not passes_after_deletion,
    }


def bounded_cross_report(public: dict[str, object]) -> dict[str, object]:
    """Project full pullback tables to bounded report-only summaries."""
    dictionary = public["dictionary"]
    family_tables = public["family_tables"]
    family_digests = public["per_family_generator_certificate_digests"]
    bounded = {
        key: value for key, value in public.items()
        if key not in (
            "dictionary",
            "family_tables",
            "per_generator_certificates",
            "per_family_generator_certificate_digests",
        )
    }
    bounded["dictionary"] = {
        key: value for key, value in dictionary.items()
        if key not in (
            "cells",
            "modes",
            "oriented_edges",
            "signed_generator_lists",
        )
    }
    bounded["family_tables"] = {
        family: {
            **family_tables[family],
            "full_table_canonical_json_sha256": family_digests[family],
        }
        for family in FAMILIES
    }
    return bounded


def main() -> None:
    started = time.monotonic()
    print(
        "FINDING no one-reference-M2-per-cell fixture exists in C; "
        "C defines CellEdgeGauge and EulerMarkerGauge"
    )

    bundles = tuple(analyze_shape(shape) for shape in REGRESSION_SHAPES)
    cross_reports = tuple(bundle["public"] for bundle in bundles)
    dictionary_ok = all(
        all(row["dictionary_match"].values()) for row in cross_reports
    )
    runtime_dictionary_digests = {
        row["shape"]: row["dictionary"]["frozen_dictionary_digest"]
        for row in cross_reports
    }
    check(
        "common cell/mode/edge/endpoint/parity dictionary is frozen on every regression box",
        dictionary_ok
        and runtime_dictionary_digests == FROZEN_DICTIONARY_DIGESTS,
        {
            "runtime": runtime_dictionary_digests,
            "frozen": FROZEN_DICTIONARY_DIGESTS,
        },
    )
    for family in FAMILIES:
        check(
            f"{family} pullbacks have separate exact rank certificates in both parity sectors",
            all(
                row["family_tables"][family]["sectors"][sector][
                    "rank_agreement"
                ]
                for row in cross_reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
            tuple(
                row["family_tables"][family]["sectors"] for row in cross_reports
            ),
        )
        check(
            f"{family} pullbacks have separate exact signed-phase certificates in both parity sectors",
            all(
                not any(
                    row["family_tables"][family]["sectors"][sector][
                        "phase_failures"
                    ].values()
                )
                and not any(
                    row["family_tables"][family]["sectors"][sector][
                        "coordinate_failures"
                    ].values()
                )
                for row in cross_reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
            tuple(
                row["family_tables"][family]["sectors"][sector][
                    "phase_failures"
                ]
                for row in cross_reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
        )
        check(
            f"{family} pullbacks have zero gauge leakage independently of center/parity supplies",
            all(
                not any(
                    row["family_tables"][family]["sectors"][sector][
                        "gauge_leakage_bit_totals"
                    ].values()
                )
                for row in cross_reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
            tuple(
                row["family_tables"][family]["sectors"][sector][
                    "center_parity_supply_counts"
                ]
                for row in cross_reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
        )
        check(
            f"{family} center/parity supply is classified separately",
            all(
                row["family_tables"][family]["sectors"][sector][
                    "center_parity_classification"
                ]
                for row in cross_reports
                for _odd, sector, _sign in PARITY_SECTORS
            ),
            "CellEdgeGauge retained; EulerMarkerGauge simultaneous; companion fixed s",
        )
        check(
            f"{family} locality census is bounded and reported separately",
            all(
                row["separate_certificates"]["locality_census_certified"]
                for row in cross_reports
            ),
            tuple(
                row["family_tables"][family]["locality_census"]
                for row in cross_reports
            ),
        )
    cross_exact = all(
        row["cross_code_pullbacks_exact"] for row in cross_reports
    )
    check(
        "every frozen generator has an exact signed cross-code pullback in both parity sectors",
        cross_exact,
        tuple(row["per_generator_certificate_count"] for row in cross_reports),
    )

    c_anchors = c_anchor_rerun()
    check(
        "C unchanged public certificates satisfy all seven main criteria",
        c_anchors["all_pass"],
        {
            "passed": c_anchors["passed_count"],
            "total": c_anchors["criteria_count"],
        },
    )
    o_anchors = o_anchor_rerun()
    check(
        "O unchanged public Choi anchors close three axes, two stars, union, both parities, parity deletion, and four completions",
        o_anchors["all_pass"],
        {
            "passed": o_anchors["passed_count"],
            "total": o_anchors["criteria_count"],
            "stars": o_anchors["seven_cell_star_reruns"],
            "unions": o_anchors["twelve_cell_union_reruns"],
            "held": o_anchors["held_completion_count"],
        },
    )

    full_sector = full_sector_obstruction(bundles)
    runtime_sector_exponent_pairs = {
        row["shape"]: (
            row["EulerMarkerGauge_full_sector_exponent"],
            row["CompanionFixture_fixed_sector_logical_exponent"],
        )
        for row in full_sector["rows"]
    }
    check(
        "frozen full-sector dimension/structure obstruction is exhibited",
        full_sector["obstruction_certified"]
        and runtime_sector_exponent_pairs == FROZEN_SECTOR_EXPONENT_PAIRS
        and not full_sector["full_sector_isometry_exists"]
        and not full_sector["sector_summed_companion_channel_constructed"],
        {
            "runtime": runtime_sector_exponent_pairs,
            "frozen": FROZEN_SECTOR_EXPONENT_PAIRS,
        },
    )
    marker_census = marker_map_census(bundles)
    runtime_marker_censuses = {
        row["shape"]: tuple(
            row["Euler_marker_classes"][kind]
            for kind in ("vertex", "edge", "face", "cube")
        )
        for row in marker_census["rows"]
    }
    check(
        "Euler markers and companion port/gauge/center/coframe structures have no count-preserving class correspondence",
        marker_census["no_count_preserving_correspondence_certified"]
        and runtime_marker_censuses == FROZEN_MARKER_CENSUSES
        and not marker_census["marker_to_coframe_correspondence_exists"],
        {
            "runtime": runtime_marker_censuses,
            "frozen": FROZEN_MARKER_CENSUSES,
        },
    )

    sign_control = sign_corruption_control(bundles[0])
    order_control = dictionary_permutation_control(bundles[0])
    missing_control = missing_anchor_control(c_anchors, o_anchors)
    check(
        "control: corrupting one generator sign breaks the signed pullback certificate",
        sign_control["detected"],
        sign_control,
    )
    check(
        "control: dictionary permutation changes the digest and a per-family table",
        order_control["detected"],
        order_control,
    )
    check(
        "control: deleting one named anchor produces a named missing-anchor failure",
        missing_control["detected"],
        missing_control,
    )

    runtime = time.monotonic() - started
    held_policy = {
        "shape": HELD_SHAPE,
        "cross_dictionary_and_pullbacks_run": (
            HELD_SHAPE in tuple(row["shape"] for row in cross_reports)
        ),
        "reason": (
            "the initial three-box clean run left ample room under the "
            "900-second budget, so the full held per-generator relation and "
            "O's held-completion anchor are both rerun"
        ),
        "O_held_completion_anchor_run": (
            HELD_SHAPE in o_anchors["held_completion_shapes"]
        ),
    }
    extract_5_4 = (
        "Full-sector mismatch: C's Euler code retains both matter-parity "
        "sectors in one root-free register, whereas the companion channel "
        "visible here fixes parity=s and center signs.",
        "Marker-to-center/coframe map: no isometry maps Euler "
        "vertex/edge/face/cube marker equalities and Gauss rows to companion "
        "ports, gauge pairs, center signs, and coframe bits.",
        "Autonomous genesis/enforcement: parity, center, mixed gauge, coframe, "
        "root, clean ancillas, and epoch remain supplied/open.",
        "Bounded physical E: C's solved common E has growing-distance logical "
        "CZ structure, while O's canonical factorization is algebraic and not "
        "itself a bounded preparation circuit.",
        "Literal TP input leg: the even-CAR Bell rows are CAR-local, but their "
        "physical-M2 input-coupling circuit and joint collision-free epoch "
        "are absent at the extracted Cycle-720 scope.",
        "Global channel tensor: O closes pairwise two-star overlap, not a "
        "tiled global PEPO/Stinespring tensor, triple overlaps, or closed-loop "
        "consistency.",
        "Periodic topology, autonomous repair, fault tolerance, renewal, and "
        "boundary-free recurrence remain outside the switch package.",
    )
    all_pass = FAILURES == 0
    bounded_cross_reports = tuple(
        bounded_cross_report(row) for row in cross_reports
    )
    report = {
        "status": (
            "cycle727-reference-to-companion-fixed-sector-equivalence-with-frozen-gaps"
            if all_pass else
            "cycle727-cross-code-equivalence-check-failures"
        ),
        "pass": all_pass,
        "one_reference_m2_fixture_exists_in_C": False,
        "reference_fixture_names": (
            "CellEdgeGauge", "EulerMarkerGauge"
        ),
        "cross_code_pullbacks_exact": cross_exact,
        "full_sector_isometry_exists": False,
        "marker_to_coframe_correspondence_exists": False,
        "sector_summed_companion_channel_constructed": False,
        "regression_shapes": REGRESSION_SHAPES,
        "held_shape_policy": held_policy,
        "cross_code_certificates": bounded_cross_reports,
        "anchor_reruns": {
            "C": c_anchors,
            "O": o_anchors,
            "total_named_criteria": (
                c_anchors["criteria_count"] + o_anchors["criteria_count"]
            ),
            "total_passed_criteria": (
                c_anchors["passed_count"] + o_anchors["passed_count"]
            ),
        },
        "frozen_mismatch_findings": {
            "full_sector": full_sector,
            "marker_map": marker_census,
        },
        "controls": {
            "sign_corruption": sign_control,
            "dictionary_permutation": order_control,
            "missing_anchor": missing_control,
        },
        "claim_boundary": {
            "relates_but_does_not_merge": True,
            "constructs_sector_summed_companion_channel": False,
            "maps_Euler_markers_to_coframes": False,
            "touches_genesis_or_enforcement": False,
            "extract_section_5_4_recorded_items": extract_5_4,
            "later_campaign_boundary": (
                "The literal TP input leg and collision-free epoch are "
                "companion-native in landed Cycles 721-722 and are not "
                "re-certified here; this runner certifies only the "
                "reference-side relation to the landed Cycle-720 companion "
                "algebra/Choi anchors."
            ),
            "not_claimed": (
                "a merged encoding",
                "a sector-summed/direct-sum companion channel",
                "a marker-to-center/coframe isometry",
                "autonomous genesis or enforcement",
                "bounded physical preparation of C's common E",
                "a global tiled PEPO/Stinespring tensor",
            ),
        },
        "runtime_seconds": runtime,
    }
    report["report_sha256"] = json_digest(report)
    print("FINAL_JSON")
    print(json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ))
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
