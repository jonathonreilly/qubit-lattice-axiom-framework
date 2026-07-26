#!/usr/bin/env python3
"""Cycle 705 Route B: geometry-local seam-gauge/tableau discriminator.

The construction appends one abstract Z2 edge-gauge qubit to every coarse matter seam of
the Cycle-703 seven-mode local-D graph.  The gauge stabilizer copies a frozen
elementary-face cell-parity word into that edge qubit.  The edge-qubit seam word is
built directly from the transported coframe, a local staggered orientation,
the two endpoint cells, and bounded gauge support.  No path interval is
queried by that constructor.

The elementary-face rule is frozen on the open L and 2x2 patches, then held
unchanged on open 3x3 and periodic L3/L4.  A phase-aware canonical tableau is
constructed analytically from the landed patch tableau, and every scheduled
coin, seam, and contact factor is decoded through the same common E.

The held failure is deliberately route-specific: it applies to the frozen
one-face edge-gauge rule and to an independently enlarged elementary
radius-one cell-parity span, not to arbitrary gauge codes or recurrent local
dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import inspect
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base
import frontier_cycle703_bksf_patch_tableau_covariance_2026_07_25 as patch
import frontier_cycle703_bksf_two_cell_tableau_intertwiner_2026_07_25 as two


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "CYCLE705_GEOMETRY_LOCAL_SEAM_GAUGE_TABLEAU_NOTE_2026-07-25.md"
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def pauli_product(rows) -> base.Pauli:
    return patch.pauli_product(rows)


def pauli_weight(row: base.Pauli) -> int:
    return patch.pauli_weight(row)


def frame_key(frame: np.ndarray) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in row) for row in frame)


class ChartPatchGraph(patch.PatchGraph):
    """Patch graph plus a transported ordered coframe and chart origin."""

    def __init__(
        self,
        cells: tuple[tuple[int, int, int], ...],
        periodic_length: int | None = None,
        chart: np.ndarray | None = None,
        origin: tuple[int, int, int] = (0, 0, 0),
    ):
        super().__init__(cells, periodic_length)
        self.chart = np.eye(3, dtype=int) if chart is None else np.asarray(chart, int)
        self.origin = tuple(int(value) for value in origin)
        if not np.array_equal(self.chart.T @ self.chart, np.eye(3, dtype=int)):
            raise ValueError("chart must be an integral orthogonal coframe")
        self.stream_index_by_edge = {
            edge: index
            for index, (edge, *_rest) in enumerate(self.stream_edges)
        }

    def local_coordinate(self, cell) -> tuple[int, int, int]:
        delta = np.asarray(cell, dtype=int) - np.asarray(self.origin, dtype=int)
        if self.periodic:
            delta %= self.periodic_length
        local = self.chart.T @ delta
        if self.periodic:
            local %= self.periodic_length
        return tuple(int(value) for value in local)

    def shifted_local(self, cell, axis: int, amount: int):
        value = np.asarray(cell, dtype=int) + amount * self.chart[:, axis]
        if self.periodic:
            value %= self.periodic_length
        return tuple(int(entry) for entry in value)


def cell_parity_pauli(graph: ChartPatchGraph, cell) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(6)
    )


def cell_logical_mask(graph: ChartPatchGraph, cells) -> int:
    mask = 0
    for cell in cells:
        index = graph.cell_index[cell]
        mask ^= ((1 << 6) - 1) << (6 * index)
    return mask


def local_seam_axis_and_start(
    graph: ChartPatchGraph,
    source_cell,
    target_cell,
    global_axis: int,
) -> tuple[int, tuple[int, int, int]]:
    local_step = graph.chart.T @ np.eye(3, dtype=int)[:, global_axis]
    local_axis = int(np.flatnonzero(local_step)[0])
    sign = int(local_step[local_axis])
    start = source_cell if sign == 1 else target_cell
    return local_axis, graph.local_coordinate(start)


def frozen_face_cells(
    graph: ChartPatchGraph,
    source_cell,
    target_cell,
    global_axis: int,
) -> tuple[tuple[int, int, int], ...]:
    """The one-face rule frozen before held inspection.

    Local-axis-0 seams are the row links.  A local-axis-1 seam on an exposed
    negative-axis-0 boundary copies the parity of the opposite edge of its
    elementary 0-1 face.  No axis-2 word was learned from the planar freeze
    fixtures, so it remains identity.  This boundary-local rule is exact on
    the frozen L/2x2 pair and makes no periodic path selection.
    """

    local_axis, _start = local_seam_axis_and_start(
        graph, source_cell, target_cell, global_axis
    )
    if local_axis != 1:
        return ()
    positive = tuple(
        graph.shifted_local(cell, 0, 1)
        for cell in (source_cell, target_cell)
    )
    negative = tuple(
        graph.shifted_local(cell, 0, -1)
        for cell in (source_cell, target_cell)
    )
    if not all(cell in graph.cell_set for cell in positive):
        return ()
    if not all(cell not in graph.cell_set for cell in negative):
        return ()
    return positive


def locally_oriented_seam(
    graph: ChartPatchGraph,
    source_cell,
    target_cell,
    source_mode: int,
    target_mode: int,
    global_axis: int,
):
    """Orient a seam from coframe/color data, never from the cell list order."""

    local_step = graph.chart.T @ np.eye(3, dtype=int)[:, global_axis]
    local_axis = int(np.flatnonzero(local_step)[0])
    sign = int(local_step[local_axis])
    if sign == 1:
        negative = (source_cell, source_mode)
        positive = (target_cell, target_mode)
    else:
        negative = (target_cell, target_mode)
        positive = (source_cell, source_mode)
    negative_coordinate = graph.local_coordinate(negative[0])
    positive_coordinate = graph.local_coordinate(positive[0])
    wraps_chart_cut = (
        graph.periodic
        and negative_coordinate[local_axis] == graph.periodic_length - 1
        and positive_coordinate[local_axis] == 0
    )
    if local_axis == 0:
        y, z = negative_coordinate[1:]
        row_index = (
            y
            if not graph.periodic or z % 2 == 0
            else graph.periodic_length - 1 - y
        )
        forward = (z + row_index) % 2 == 0
    elif local_axis == 1:
        forward = negative_coordinate[2] % 2 == 0
    else:
        forward = True
    if wraps_chart_cut:
        forward = not forward
    return (*((negative, positive) if forward else (positive, negative)), local_axis)


@dataclass
class GaugeCode:
    graph: ChartPatchGraph
    base_code: patch.CodeData
    candidate_cells: tuple[tuple[tuple[int, int, int], ...], ...]
    candidate_masks: tuple[int, ...]
    gauge_stabilizers: tuple[base.Pauli, ...]
    stabilizers: tuple[base.Pauli, ...]
    logical_z: tuple[base.Pauli, ...]
    logical_x: tuple[base.Pauli, ...]
    w_rows: tuple[base.Pauli, ...]
    v_rows: tuple[base.Pauli, ...]
    digest: str

    @property
    def base_qubits(self) -> int:
        return len(self.graph.edges)

    @property
    def gauge_qubits(self) -> int:
        return len(self.graph.stream_edges)

    @property
    def qubits(self) -> int:
        return self.base_qubits + self.gauge_qubits


def canonical_failures(code: GaugeCode) -> int:
    qubits = code.qubits
    w = [row.symplectic(qubits) for row in code.w_rows]
    v = [row.symplectic(qubits) for row in code.v_rows]
    return sum(
        two.symplectic(w[left], w[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        two.symplectic(v[left], v[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        two.symplectic(v[left], w[right], qubits) != int(left == right)
        for left in range(qubits)
        for right in range(qubits)
    )


def build_gauge_code(
    graph: ChartPatchGraph,
    validate: bool = True,
    cloned_base: patch.CodeData | None = None,
) -> GaugeCode:
    base_code = cloned_base or patch.build_code(graph, validate=validate)
    base_qubits = len(graph.edges)
    logical_count = len(base_code.logical_z)
    candidate_masks = []
    candidate_cells = []
    gauge_stabilizers = []
    for seam_index, (
        _edge,
        source_cell,
        target_cell,
        _source_mode,
        _target_mode,
        global_axis,
    ) in enumerate(graph.stream_edges):
        cells = frozen_face_cells(graph, source_cell, target_cell, global_axis)
        candidate_cells.append(cells)
        logical_mask = cell_logical_mask(graph, cells)
        candidate_masks.append(logical_mask)
        copied = pauli_product(cell_parity_pauli(graph, cell) for cell in cells)
        gauge_stabilizers.append(
            copied @ base.Pauli(z=1 << (base_qubits + seam_index))
        )

    w_rows = list(base_code.w_rows) + gauge_stabilizers
    v_rows = []
    for index, row in enumerate(base_code.v_rows):
        x = row.x
        if index < logical_count:
            for seam_index, mask in enumerate(candidate_masks):
                if (mask >> index) & 1:
                    x ^= 1 << (base_qubits + seam_index)
        v_rows.append(base.Pauli(row.phase, x, row.z))
    v_rows.extend(
        base.Pauli(x=1 << (base_qubits + seam_index))
        for seam_index in range(len(gauge_stabilizers))
    )
    stabilizers = tuple(base_code.stabilizers) + tuple(gauge_stabilizers)
    logical_z = tuple(base_code.logical_z)
    logical_x = tuple(v_rows[:logical_count])
    serialized = "\n".join(
        f"{kind}:{index}:{row.phase}:{row.x:x}:{row.z:x}"
        for kind, rows in (("W", w_rows), ("V", v_rows))
        for index, row in enumerate(rows)
    )
    code = GaugeCode(
        graph,
        base_code,
        tuple(candidate_cells),
        tuple(candidate_masks),
        tuple(gauge_stabilizers),
        stabilizers,
        logical_z,
        logical_x,
        tuple(w_rows),
        tuple(v_rows),
        sha256(serialized.encode("ascii")).hexdigest(),
    )
    if validate:
        if canonical_failures(code):
            raise ValueError("gauge tableau is not canonical")
        if base.gf2_rank(
            row.symplectic(code.qubits) for row in code.w_rows + code.v_rows
        ) != 2 * code.qubits:
            raise ValueError("gauge tableau is not full rank")
        if base.stabilizer_phase_failures(list(code.stabilizers), code.qubits):
            raise ValueError("gauge stabilizer phase relation is inconsistent")
    return code


def decoded_logical(row: base.Pauli, code: GaugeCode) -> base.Pauli:
    coordinates = two.decode_full(row, code.w_rows, code.v_rows, code.qubits)
    logical_count = len(code.logical_z)
    if coordinates.v_mask >> logical_count:
        raise ValueError("operator leaks from the gauge code")
    mask = (1 << logical_count) - 1
    return base.Pauli(
        coordinates.phase,
        coordinates.v_mask & mask,
        coordinates.w_mask & mask,
    )


def logical_right_z_residual(
    actual: tuple[base.Pauli, base.Pauli],
    target: tuple[base.Pauli, base.Pauli],
) -> int | None:
    """Return the common right-Z residual, including exact Pauli phases."""

    for order in permutations(range(2)):
        masks = []
        valid = True
        for index, target_index in enumerate(order):
            if actual[index].x != target[target_index].x:
                valid = False
                break
            masks.append(actual[index].z ^ target[target_index].z)
        if not valid or masks[0] != masks[1]:
            continue
        residual = base.Pauli(z=masks[0])
        if all(
            actual[index] == target[target_index] @ residual
            for index, target_index in enumerate(order)
        ):
            return masks[0]
    return None


def positive_stabilizer_delta(
    actual: base.Pauli, expected: base.Pauli, code: GaugeCode
) -> bool:
    coordinates = two.decode_full(
        actual @ expected, code.w_rows, code.v_rows, code.qubits
    )
    logical_count = len(code.logical_z)
    return (
        coordinates.phase == 0
        and coordinates.v_mask == 0
        and not (coordinates.w_mask & ((1 << logical_count) - 1))
    )


def edge_seam_rows(
    code: GaugeCode, seam_index: int
) -> tuple[tuple[base.Pauli, base.Pauli], dict[str, object]]:
    graph = code.graph
    (
        _edge,
        source_cell,
        target_cell,
        source_mode,
        target_mode,
        _axis,
    ) = graph.stream_edges[seam_index]
    (left_cell, left_mode), (right_cell, right_mode), local_axis = locally_oriented_seam(
        graph,
        source_cell,
        target_cell,
        source_mode,
        target_mode,
        graph.stream_edges[seam_index][5],
    )
    u = graph.vertex_index[(left_cell, left_mode)]
    v = graph.vertex_index[(right_cell, right_mode)]
    ru = graph.vertex_index[(left_cell, 6)]
    rv = graph.vertex_index[(right_cell, 6)]
    core = graph.A(ru, u) @ graph.A(v, rv)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(right_cell, mode)])
        for mode in range(6)
        if mode != right_mode
    )
    local_terms = (
        base.Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(u) @ graph.B(v) @ core,
    )
    gauge_z = base.Pauli(z=1 << (code.base_qubits + seam_index))
    # A seam changes the whole-cell parity at both endpoints.  It must
    # therefore flip every copied gauge bit whose D_f contains exactly one
    # endpoint; otherwise a later factor would leave the common-E stabilizer
    # sector.  This is the local state-compatibility update missing from the
    # naive diagonal readout.
    collateral = tuple(
        gauge_index
        for gauge_index, cells in enumerate(code.candidate_cells)
        if (source_cell in cells) ^ (target_cell in cells)
    )
    collateral_x = base.Pauli(
        x=sum(1 << (code.base_qubits + index) for index in collateral)
    )
    rows = tuple(
        row @ gauge_z @ collateral_x for row in local_terms
    )
    return rows, {
        "program_left": (left_cell, left_mode),
        "program_right": (right_cell, right_mode),
        "local_axis": local_axis,
        "collateral_gauge_flips": collateral,
    }


def seam_terms(
    code: GaugeCode, seam_index: int
) -> tuple[tuple[base.Pauli, base.Pauli], dict[str, object]]:
    """Attach target logical labels only after the edge-qubit rows are built."""

    rows, detail = edge_seam_rows(code, seam_index)
    graph = code.graph
    _edge, source_cell, target_cell, source_mode, target_mode, _axis = (
        graph.stream_edges[seam_index]
    )
    return rows, {
        **detail,
        "logical_indices": (
            6 * graph.cell_index[source_cell] + source_mode,
            6 * graph.cell_index[target_cell] + target_mode,
        ),
    }


def greedy_localize(
    row: base.Pauli, code: GaugeCode
) -> tuple[base.Pauli, int, tuple[int, ...]]:
    current = row
    mask = 0
    steps = []
    while True:
        weight = pauli_weight(current)
        choices = []
        for index, stabilizer in enumerate(code.stabilizers):
            candidate = current @ stabilizer
            candidate_weight = pauli_weight(candidate)
            if candidate_weight < weight:
                choices.append((candidate_weight, index, candidate))
        if not choices:
            break
        _, index, current = min(choices, key=lambda item: (item[0], item[1]))
        mask ^= 1 << index
        steps.append(index)
    return current, mask, tuple(steps)


def extended_support_cells(row: base.Pauli, code: GaugeCode):
    cells = patch.support_cells(
        base.Pauli(row.phase, row.x & ((1 << code.base_qubits) - 1), row.z & ((1 << code.base_qubits) - 1)),
        code.graph,
    )
    gauge_support = (row.x | row.z) >> code.base_qubits
    while gauge_support:
        bit = gauge_support & -gauge_support
        seam = bit.bit_length() - 1
        _edge, source, target, *_rest = code.graph.stream_edges[seam]
        cells.update((source, target))
        gauge_support ^= bit
    return cells


def extended_diameter(row: base.Pauli, code: GaugeCode) -> int:
    cells = extended_support_cells(row, code)

    def distance(left, right):
        values = [abs(left[axis] - right[axis]) for axis in range(3)]
        if code.graph.periodic:
            values = [
                min(value, code.graph.periodic_length - value)
                for value in values
            ]
        return sum(values)

    return max(
        (distance(left, right) for left in cells for right in cells),
        default=0,
    )


@dataclass(frozen=True)
class Factor:
    key: tuple[object, ...]
    kind: str
    rows: tuple[base.Pauli, ...]
    target: tuple[base.Pauli, ...]
    support: int


def factor_dictionary(code: GaugeCode):
    graph = code.graph
    factors = []
    preservation_failures = inverse_failures = target_decode_failures = 0
    seam_target_failures = 0
    raw_seam_max = localized_seam_max = seam_diameter = 0
    localization_reconstruction_failures = 0
    localization_steps = []

    def append(key, kind, rows, target):
        nonlocal preservation_failures, inverse_failures, target_decode_failures
        decoded = tuple(decoded_logical(row, code) for row in rows)
        target_decode_failures += patch.term_signature(decoded) != patch.term_signature(target)
        support = 0
        for row in rows:
            support |= row.x | row.z
            preservation_failures += sum(
                not row.commutes(stabilizer) for stabilizer in code.stabilizers
            )
            coordinates = two.decode_full(row, code.w_rows, code.v_rows, code.qubits)
            inverse_failures += (
                two.encode_full(coordinates, code.w_rows, code.v_rows, code.qubits)
                != row
            )
        factors.append(Factor(tuple(key), kind, tuple(rows), tuple(target), support))

    for cell_index, cell in enumerate(graph.cells):
        for left, right in combinations(range(6), 2):
            if patch.REVERSE[left] == right:
                continue
            u = graph.vertex_index[(cell, left)]
            v = graph.vertex_index[(cell, right)]
            a = graph.A(u, v)
            rows = (
                base.Pauli(phase=3) @ graph.B(u) @ a,
                base.Pauli(phase=1) @ graph.B(v) @ a,
            )
            append(
                ("coin", cell_index, left, right),
                "onsite_coin",
                rows,
                patch.logical_hop_terms(
                    6 * cell_index + left, 6 * cell_index + right
                ),
            )

    for seam_index, row in enumerate(graph.stream_edges):
        raw_rows, detail = seam_terms(code, seam_index)
        localized = []
        for raw in raw_rows:
            descended, mask, steps = greedy_localize(raw, code)
            localization_reconstruction_failures += not positive_stabilizer_delta(
                raw, descended, code
            )
            localization_steps.append((mask.bit_count(), len(steps)))
            raw_seam_max = max(raw_seam_max, pauli_weight(raw))
            localized_seam_max = max(localized_seam_max, pauli_weight(descended))
            seam_diameter = max(seam_diameter, extended_diameter(descended, code))
            localized.append(descended)
        target = patch.logical_hop_terms(*detail["logical_indices"])
        decoded = tuple(decoded_logical(term, code) for term in localized)
        seam_target_failures += logical_right_z_residual(decoded, target) != 0
        append(
            ("seam", seam_index, row[5]),
            "directed_seam",
            tuple(localized),
            target,
        )

    for cell_index, cell in enumerate(graph.cells):
        for left, right in combinations(range(6), 2):
            row = graph.B(graph.vertex_index[(cell, left)]) @ graph.B(
                graph.vertex_index[(cell, right)]
            )
            append(
                ("contact", cell_index, left, right),
                "onsite_contact",
                (row,),
                (
                    base.Pauli(
                        z=(1 << (6 * cell_index + left))
                        | (1 << (6 * cell_index + right))
                    ),
                ),
            )

    # target_decode_failures counts precisely the held seam misses.  Common-E
    # state compatibility is tested independently by stabilizer commutation,
    # exact full-tableau inversion, and localization reconstruction.
    return factors, {
        "code_preservation_failures": preservation_failures,
        "inverse_tableau_failures": inverse_failures,
        "target_schedule_factor_failures": target_decode_failures,
        "seam_target_failures": seam_target_failures,
        "localization_reconstruction_failures": localization_reconstruction_failures,
        "raw_seam_max_weight": raw_seam_max,
        "localized_seam_max_weight": localized_seam_max,
        "localized_seam_max_cell_diameter": seam_diameter,
        "maximum_localization_basis_rows": max(
            (count for count, _steps in localization_steps), default=0
        ),
    }


def schedule_controls(code: GaugeCode):
    factors, controls = factor_dictionary(code)
    layer_supports = []
    colors = []
    for factor in factors:
        for color, occupied in enumerate(layer_supports):
            if not (factor.support & occupied):
                break
        else:
            color = len(layer_supports)
            layer_supports.append(0)
        colors.append(color)
        layer_supports[color] |= factor.support
    collisions = sum(
        bool(left.support & right.support)
        for left_index, left in enumerate(factors)
        for right_index, right in enumerate(factors)
        if left_index < right_index and colors[left_index] == colors[right_index]
    )

    def digest(rows, color_rows):
        return sha256(
            "\n".join(
                f"{color}:{factor.key}:"
                + ";".join(
                    f"{row.phase}:{row.x:x}:{row.z:x}" for row in factor.rows
                )
                for factor, color in zip(rows, color_rows)
            ).encode("ascii")
        ).hexdigest()

    full_digest = digest(factors, colors)
    deletion = next(
        index for index, factor in enumerate(factors) if factor.kind == "directed_seam"
    )
    deleted_digest = digest(
        factors[:deletion] + factors[deletion + 1 :],
        colors[:deletion] + colors[deletion + 1 :],
    )
    summands = [row for factor in factors for row in factor.rows]
    return {
        "factors": len(factors),
        "factor_counts": {
            kind: sum(factor.kind == kind for factor in factors)
            for kind in ("onsite_coin", "directed_seam", "onsite_contact")
        },
        "colors": len(layer_supports),
        "collisions": collisions,
        "edge_schedule_sha256": full_digest,
        "complete_seam_factor_deletion_active": deleted_digest != full_digest,
        "individual_G_summand_max_weight": max(map(pauli_weight, summands)),
        "individual_G_summand_max_cell_diameter": max(
            extended_diameter(row, code) for row in summands
        ),
        **controls,
    }


def elementary_radius_one_cells(code: GaugeCode, seam_index: int):
    graph = code.graph
    _edge, source, target, *_rest = graph.stream_edges[seam_index]
    cells = set()
    for candidate in graph.cells:
        for endpoint in (source, target):
            differences = [
                abs(candidate[axis] - endpoint[axis]) for axis in range(3)
            ]
            if graph.periodic:
                differences = [
                    min(value, graph.periodic_length - value)
                    for value in differences
                ]
            if sum(differences) <= 1:
                cells.add(candidate)
    return cells


def held_span_controls(code: GaugeCode):
    frozen_failures = []
    radius_one_failures = []
    residual_shape_failures = 0
    for seam_index, row in enumerate(code.graph.stream_edges):
        edge_rows, detail = seam_terms(code, seam_index)
        decoded = tuple(decoded_logical(term, code) for term in edge_rows)
        target = patch.logical_hop_terms(*detail["logical_indices"])
        residual = logical_right_z_residual(decoded, target)
        residual_cells = set()
        partial_cells = []
        if residual is not None:
            for cell_index, cell in enumerate(code.graph.cells):
                block = (residual >> (6 * cell_index)) & 0x3F
                if block == 0x3F:
                    residual_cells.add(cell)
                elif block:
                    partial_cells.append((cell, block))
        residual_shape_failures += residual is None or bool(partial_cells)
        exact = residual == 0
        if not exact:
            frozen_failures.append(
                {
                    "seam": seam_index,
                    "axis": row[5],
                    "residual_is_common_right_Z": residual is not None,
                    "residual_full_cells": len(residual_cells),
                    "residual_partial_cells": len(partial_cells),
                    "residual_weight": residual.bit_count() if residual is not None else -1,
                }
            )
        radius_one = elementary_radius_one_cells(code, seam_index)
        in_elementary_cell_span = (
            residual is not None
            and not partial_cells
            and residual_cells.issubset(radius_one)
        )
        if not in_elementary_cell_span:
            radius_one_failures.append(
                {
                    "seam": seam_index,
                    "residual_is_common_right_Z": residual is not None,
                    "residual_full_cells": len(residual_cells),
                    "residual_partial_cells": len(partial_cells),
                    "outside_elementary_radius_one": len(residual_cells - radius_one),
                }
            )
    return {
        "seams": len(code.graph.stream_edges),
        "frozen_face_rule_failures": len(frozen_failures),
        "non_cell_parity_residuals": residual_shape_failures,
        "first_frozen_failure": frozen_failures[:1],
        "elementary_radius_one_arbitrary_cell_parity_span_failures": len(
            radius_one_failures
        ),
        "first_radius_one_failure": radius_one_failures[:1],
        "maximum_frozen_residual_cells": max(
            (row["residual_full_cells"] for row in frozen_failures),
            default=0,
        ),
        "maximum_radius_one_outside_cells": max(
            (row["outside_elementary_radius_one"] for row in radius_one_failures),
            default=0,
        ),
    }


def transform_graph(
    source: ChartPatchGraph,
    frame: np.ndarray | None = None,
    displacement: tuple[int, int, int] | None = None,
) -> tuple[ChartPatchGraph, dict, dict[int, int]]:
    if (frame is None) == (displacement is None):
        raise ValueError("select one transform")
    if frame is not None:
        direction_map = base.direction_map(frame)

        def mapped(cell):
            value = frame @ np.asarray(cell, dtype=int)
            if source.periodic:
                value %= source.periodic_length
            return tuple(int(entry) for entry in value)

        chart = frame @ source.chart
        origin = mapped(source.origin)
    else:
        direction_map = {mode: mode for mode in range(6)}

        def mapped(cell):
            value = np.asarray(cell, dtype=int) + np.asarray(displacement, dtype=int)
            if source.periodic:
                value %= source.periodic_length
            return tuple(int(entry) for entry in value)

        chart = source.chart
        origin = mapped(source.origin)
    cell_map = {cell: mapped(cell) for cell in source.cells}
    target = ChartPatchGraph(
        tuple(cell_map[cell] for cell in source.cells),
        source.periodic_length,
        chart,
        origin,
    )
    return target, cell_map, direction_map


def clone_translated_code(source: GaugeCode, target_graph: ChartPatchGraph):
    base_source = source.base_code
    base_clone = patch.CodeData(
        target_graph,
        base_source.loops,
        base_source.wilsons,
        base_source.ds,
        base_source.stabilizers,
        base_source.logical_z,
        base_source.logical_x,
        base_source.w_rows,
        base_source.v_rows,
        base_source.selected_windings,
        base_source.digest,
    )
    return build_gauge_code(target_graph, validate=False, cloned_base=base_clone)


def transform_extended(
    row: base.Pauli,
    source: GaugeCode,
    target: GaugeCode,
    edge_map,
    toggles,
    pairs,
    flips,
    gauge_map,
) -> base.Pauli:
    base_mask = (1 << source.base_qubits) - 1
    base_row = base.Pauli(row.phase, row.x & base_mask, row.z & base_mask)
    transformed = patch.transform_pauli(base_row, edge_map, toggles, pairs, flips)
    gauge_x = row.x >> source.base_qubits
    gauge_z = row.z >> source.base_qubits
    mapped_x = mapped_z = 0
    for source_index, target_index in enumerate(gauge_map):
        if (gauge_x >> source_index) & 1:
            mapped_x ^= 1 << (target.base_qubits + target_index)
        if (gauge_z >> source_index) & 1:
            mapped_z ^= 1 << (target.base_qubits + target_index)
    return base.Pauli(
        transformed.phase,
        transformed.x ^ mapped_x,
        transformed.z ^ mapped_z,
    )


class PositiveStabilizerReducer:
    """Exact signed membership in one independent commuting stabilizer span."""

    def __init__(self, rows: tuple[base.Pauli, ...], qubits: int):
        self.pivots: dict[int, base.Pauli] = {}
        for original in rows:
            row = original
            while row.x or row.z:
                pivot = row.symplectic(qubits).bit_length() - 1
                if pivot in self.pivots:
                    row = row @ self.pivots[pivot]
                else:
                    self.pivots[pivot] = row
                    break
            else:
                if row.phase:
                    raise ValueError("inconsistent stabilizer character")

    def contains(self, row: base.Pauli, qubits: int) -> bool:
        current = row
        while current.x or current.z:
            pivot = current.symplectic(qubits).bit_length() - 1
            if pivot not in self.pivots:
                return False
            current = current @ self.pivots[pivot]
        return current.phase == 0


def covariance_case(
    source: GaugeCode,
    target: GaugeCode,
    cell_map,
    direction_map,
):
    vertex_map = [
        target.graph.vertex_index[
            (cell_map[cell], 6 if mode == 6 else direction_map[mode])
        ]
        for cell, mode in source.graph.vertices
    ]
    edge_map, toggles, pairs, flips, generator_failures = patch.transform_data(
        source.graph, target.graph, vertex_map
    )
    gauge_map = [
        target.graph.stream_index_by_edge[edge_map[edge]]
        for edge, *_rest in source.graph.stream_edges
    ]
    transform = lambda row: transform_extended(
        row,
        source,
        target,
        edge_map,
        toggles,
        pairs,
        flips,
        gauge_map,
    )
    target_index = {
        (cell, mode): 6 * cell_index + mode
        for cell_index, cell in enumerate(target.graph.cells)
        for mode in range(6)
    }
    logical_permutation = [
        target_index[(cell_map[cell], direction_map[mode])]
        for cell in source.graph.cells
        for mode in range(6)
    ]
    reducer = PositiveStabilizerReducer(target.stabilizers, target.qubits)
    positive = lambda actual, expected=base.Pauli(): reducer.contains(
        actual @ expected, target.qubits
    )
    stabilizer_failures = sum(
        not positive(transform(row))
        for row in source.stabilizers
    )
    logical_z_failures = sum(
        not positive(transform(row), target.logical_z[logical_permutation[index]])
        for index, row in enumerate(source.logical_z)
    )
    logical_x_failures = 0
    for index, row in enumerate(source.logical_x):
        destination = logical_permutation[index]
        crossings = [
            logical_permutation[other]
            for other in range(len(logical_permutation))
            if other != index
            and (other - index) * (logical_permutation[other] - destination) < 0
        ]
        expected = target.logical_x[destination] @ pauli_product(
            target.logical_z[crossing] for crossing in crossings
        )
        logical_x_failures += not positive(transform(row), expected)
    candidate_mask_failures = 0
    for source_index, target_index_value in enumerate(gauge_map):
        source_cells = {
            cell_map[cell]
            for cell in frozen_face_cells(
                source.graph,
                source.graph.stream_edges[source_index][1],
                source.graph.stream_edges[source_index][2],
                source.graph.stream_edges[source_index][5],
            )
        }
        target_row = target.graph.stream_edges[target_index_value]
        target_cells = set(
            frozen_face_cells(
                target.graph,
                target_row[1],
                target_row[2],
                target_row[5],
            )
        )
        candidate_mask_failures += source_cells != target_cells

    seam_coset_failures = 0
    for source_index, target_index_value in enumerate(gauge_map):
        actual = tuple(transform(row) for row in seam_terms(source, source_index)[0])
        expected = seam_terms(target, target_index_value)[0]
        seam_coset_failures += not any(
            all(
                positive(actual[index], expected[target_slot])
                for index, target_slot in enumerate(order)
            )
            for order in permutations(range(2))
        )
    return {
        "BKSF_generator_failures": generator_failures,
        "stabilizer_character_failures": stabilizer_failures,
        "logical_Z_failures": logical_z_failures,
        "phase_oriented_logical_X_failures": logical_x_failures,
        "candidate_chart_failures": candidate_mask_failures,
        "seam_signed_coset_failures": seam_coset_failures,
    }


def composition_controls(code: GaugeCode):
    frames = base.proper_cubic_frames()
    lookup = {frame_key(frame): frame for frame in frames}
    failures = 0
    cases = 0
    for left in frames:
        for right in frames:
            combined = lookup[frame_key(left @ right)]
            cases += 1
            for seam_index, row in enumerate(code.graph.stream_edges):
                _edge, source, target, _sm, _tm, axis = row
                source_cells = frozen_face_cells(
                    code.graph, source, target, axis
                )
                sequential = {
                    tuple(int(value) for value in left @ (right @ np.asarray(cell)))
                    for cell in source_cells
                }
                direct = {
                    tuple(int(value) for value in combined @ np.asarray(cell))
                    for cell in source_cells
                }
                if code.graph.periodic:
                    sequential = {
                        tuple(value % code.graph.periodic_length for value in cell)
                        for cell in sequential
                    }
                    direct = {
                        tuple(value % code.graph.periodic_length for value in cell)
                        for cell in direct
                    }
                failures += sequential != direct
    return {
        "proper_cubic_frames": 24,
        "ordered_frame_products": cases,
        "candidate_cell_and_gauge_composition_failures": failures,
    }


def covariance_controls(code: GaugeCode):
    frame_rows = []
    for frame in base.proper_cubic_frames():
        target_graph, cell_map, direction_map = transform_graph(
            code.graph, frame=frame
        )
        target = build_gauge_code(target_graph, validate=False)
        frame_rows.append(
            covariance_case(code, target, cell_map, direction_map)
        )
    translations = (
        tuple(product(range(code.graph.periodic_length), repeat=3))
        if code.graph.periodic
        else ((0, 0, 0), (1, -2, 3), (-3, 1, 2), (2, 2, -1))
    )
    translation_rows = []
    for displacement in translations:
        target_graph, cell_map, direction_map = transform_graph(
            code.graph, displacement=displacement
        )
        target = clone_translated_code(code, target_graph)
        translation_rows.append(
            covariance_case(code, target, cell_map, direction_map)
        )
    keys = tuple(frame_rows[0])
    return {
        "proper_cubic_frames": len(frame_rows),
        "translations": len(translation_rows),
        "frame_failure_totals": {
            key: sum(row[key] for row in frame_rows) for key in keys
        },
        "translation_failure_totals": {
            key: sum(row[key] for row in translation_rows) for key in keys
        },
        "composition": composition_controls(code),
    }


def deletion_controls(code: GaugeCode):
    rank = base.gf2_rank(
        row.symplectic(code.qubits) for row in code.stabilizers
    )
    gauge_offset = len(code.base_code.stabilizers)
    gauge_delete_ranks = {
        base.gf2_rank(
            row.symplectic(code.qubits)
            for index, row in enumerate(code.stabilizers)
            if index != gauge_offset + deleted
        )
        for deleted in range(code.gauge_qubits)
    }
    nontrivial = next(
        (index for index, mask in enumerate(code.candidate_masks) if mask), None
    )
    face_copy_deletion_active = False
    if nontrivial is not None:
        rows, detail = seam_terms(code, nontrivial)
        without_gauge = tuple(
            row @ base.Pauli(z=1 << (code.base_qubits + nontrivial))
            for row in rows
        )
        target = patch.logical_hop_terms(*detail["logical_indices"])
        face_copy_deletion_active = (
            patch.term_signature(tuple(decoded_logical(row, code) for row in without_gauge))
            != patch.term_signature(target)
        )
    return {
        "stabilizer_rank": rank,
        "all_edge_gauge_rows_independent": gauge_delete_ranks == {rank - 1},
        "gauge_delete_ranks": sorted(gauge_delete_ranks),
        "nontrivial_face_copy_present": nontrivial is not None,
        "deleting_nontrivial_edge_gauge_factor_changes_target_action": face_copy_deletion_active,
    }


def fixture_row(name, graph):
    code = build_gauge_code(graph)
    schedule = schedule_controls(code)
    spans = held_span_controls(code)
    covariance = covariance_controls(code)
    deletions = deletion_controls(code)
    covariance_failures = sum(
        value
        for family in ("frame_failure_totals", "translation_failure_totals")
        for value in covariance[family].values()
    ) + covariance["composition"]["candidate_cell_and_gauge_composition_failures"]
    structural_failures = (
        canonical_failures(code)
        + base.stabilizer_phase_failures(list(code.stabilizers), code.qubits)
        + int(len(code.w_rows) != code.qubits)
        + int(len(code.v_rows) != code.qubits)
        + int(not deletions["all_edge_gauge_rows_independent"])
        + schedule["code_preservation_failures"]
        + schedule["inverse_tableau_failures"]
        + schedule["localization_reconstruction_failures"]
        + spans["non_cell_parity_residuals"]
        + schedule["collisions"]
        + int(not schedule["complete_seam_factor_deletion_active"])
        + covariance_failures
    )
    return code, {
        "name": name,
        "cells": len(graph.cells),
        "base_edge_qubits": code.base_qubits,
        "seam_gauge_edge_qubits": code.gauge_qubits,
        "total_edge_qubits": code.qubits,
        "base_stabilizers": len(code.base_code.stabilizers),
        "edge_gauge_stabilizers": len(code.gauge_stabilizers),
        "logical_matter_qubits": len(code.logical_z),
        "tableau_rows": 2 * code.qubits,
        "tableau_sha256": code.digest,
        "common_E_typing": (
            "H_matter tensor C^8_Wilson -> H_gauge_code"
            if graph.periodic
            else "H_matter -> H_gauge_code"
        ),
        "Wilson_action": "G_matter tensor I_8" if graph.periodic else "none",
        "schedule": schedule,
        "held_span": spans,
        "covariance": covariance,
        "deletions": deletions,
        "structural_failures": structural_failures,
        "target_schedule_failures": schedule["target_schedule_factor_failures"],
    }


def note_contract() -> None:
    text = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").split()
    )
    required = (
        "type: meta",
        "authority: none",
        "audit: unset",
        "one abstract edge-gauge qubit",
        "elementary face",
        "no supplied hamiltonian cell path",
        "common e",
        "individual pauli summand",
        "open `3 x 3`",
        "periodic `l=3`",
        "periodic `l=4`",
        "24 proper-cubic frames",
        "576 ordered frame products",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent no-go",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the Route-B claim ceiling and N1-N8 gate", not missing, missing)


def run():
    edge_source = inspect.getsource(locally_oriented_seam) + inspect.getsource(
        edge_seam_rows
    )
    forbidden_edge_queries = tuple(
        token
        for token in (
            "stream_terms",
            "intermediate_cell_parity",
            "cell_index",
            "cell_path",
            "desired_interval",
        )
        if token in edge_source
    )
    check(
        "edge-qubit seam construction contains no path, interval, or target-order query",
        not forbidden_edge_queries,
        forbidden_edge_queries,
    )
    fixtures = (
        (
            "freeze_open_L",
            ChartPatchGraph(patch.OPEN_GEOMETRIES["open_three_center_L"]),
        ),
        ("freeze_open_2x2", ChartPatchGraph(patch.OPEN_GEOMETRIES["held_2x2"])),
        ("hold_open_3x3", ChartPatchGraph(patch.OPEN_GEOMETRIES["held_3x3"])),
        (
            "hold_periodic_L3",
            ChartPatchGraph(patch.cell_path_3d(3), periodic_length=3),
        ),
        (
            "hold_periodic_L4",
            ChartPatchGraph(patch.cell_path_3d(4), periodic_length=4),
        ),
    )
    rows = {}
    for name, graph in fixtures:
        _code, rows[name] = fixture_row(name, graph)
        print(
            "FIXTURE",
            name,
            "structural",
            rows[name]["structural_failures"],
            "target",
            rows[name]["target_schedule_failures"],
            "maxW",
            rows[name]["schedule"]["individual_G_summand_max_weight"],
        )

    freeze = [rows["freeze_open_L"], rows["freeze_open_2x2"]]
    holds = [
        rows["hold_open_3x3"],
        rows["hold_periodic_L3"],
        rows["hold_periodic_L4"],
    ]
    check(
        "the frozen L/2x2 face-gauge tableaus exactly intertwine the full scheduled target G",
        all(
            row["structural_failures"] == 0
            and row["target_schedule_failures"] == 0
            and row["schedule"]["localized_seam_max_weight"] <= 17
            and row["schedule"]["localized_seam_max_cell_diameter"] <= 2
            for row in freeze
        ),
        {
            row["name"]: {
                "tableau": row["tableau_rows"],
                "factors": row["schedule"]["factor_counts"],
                "colors": row["schedule"]["colors"],
                "seam_weight": row["schedule"]["localized_seam_max_weight"],
                "seam_diameter": row["schedule"]["localized_seam_max_cell_diameter"],
                "target_failures": row["target_schedule_failures"],
            }
            for row in freeze
        },
    )
    check(
        "all five finite common-E tableaus, schedules, translations, frames, 576 products, and deletions are structurally exact",
        all(row["structural_failures"] == 0 for row in rows.values()),
        {
            name: {
                "edge_qubits": row["total_edge_qubits"],
                "tableau_rows": row["tableau_rows"],
                "translations": row["covariance"]["translations"],
                "frames": row["covariance"]["proper_cubic_frames"],
                "products": row["covariance"]["composition"]["ordered_frame_products"],
                "structural_failures": row["structural_failures"],
            }
            for name, row in rows.items()
        },
    )
    check(
        "held target seam cosets falsify the frozen one-face rule without refit",
        all(row["target_schedule_failures"] > 0 for row in holds)
        and [row["target_schedule_failures"] for row in holds] == [5, 55, 132],
        {
            row["name"]: {
                "seams": row["held_span"]["seams"],
                "frozen_failures": row["held_span"]["frozen_face_rule_failures"],
                "target_schedule_failures": row["target_schedule_failures"],
                "max_residual_cells": row["held_span"]["maximum_frozen_residual_cells"],
            }
            for row in holds
        },
    )
    check(
        "the stronger arbitrary elementary-radius-one cell-parity span also misses every held family",
        all(
            row["held_span"][
                "elementary_radius_one_arbitrary_cell_parity_span_failures"
            ]
            > 0
            for row in holds
        ),
        {
            row["name"]: row["held_span"][
                "elementary_radius_one_arbitrary_cell_parity_span_failures"
            ]
            for row in holds
        },
    )
    check(
        "the held seam cosets still have constant weight-17 representatives; the failure is logical target transfer",
        all(
            row["schedule"]["localized_seam_max_weight"] <= 17
            and row["schedule"]["localized_seam_max_cell_diameter"] <= 3
            for row in holds
        ),
        {
            row["name"]: (
                row["schedule"]["localized_seam_max_weight"],
                row["schedule"]["localized_seam_max_cell_diameter"],
            )
            for row in holds
        },
    )
    note_contract()
    summary = {
        "terminal": (
            "CYCLE705_FACE_GAUGE_COMMON_E_FREEZE_EXACT_"
            "HELD_SEAM_COSETS_5_55_132_ROUTE_OPEN"
        ),
        "authority": "none",
        "audit": "unset",
        "fixtures": rows,
        "route_specific_negative": {
            "frozen_one_face_rule_held_failures": [5, 55, 132],
            "broad_no_go": False,
            "live_routes": [
                "radius-two or cube-supported stabilizer copy",
                "multiple face channels",
                "non-diagonal Gauss constraints",
                "recurrent local gauge dynamics",
                "different state chart without a Hamiltonian path",
            ],
        },
        "tests_passed": PASS,
        "tests_failed": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", summary["terminal"] if FAIL == 0 else "UNFINISHED_CYCLE705_ROUTE_B")
    if FAIL:
        raise SystemExit(1)
    return summary


if __name__ == "__main__":
    run()
