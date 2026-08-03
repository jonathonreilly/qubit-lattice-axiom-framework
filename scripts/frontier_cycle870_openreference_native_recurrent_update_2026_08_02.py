#!/usr/bin/env python3
"""Native OpenReferenceGraph physical-M2 update composition probe.

This bounded component never compares the update with a global Jordan--Wigner
character.  Its source algebra is the landed Cycle703 OpenReferenceGraph
itself.  It composes the Cycle703 graph constraints, the Cycle870/707 carrier
placement, an exact Cycle219 onsite coin synthesis, onsite reverse FSWAPs,
every reference-dressed seam FSWAP, and the Cycle230 contact phase.  Every
Pauli rotation is compiled and serially routed by returned nearest-neighbour
Manhattan macros.

The result is deliberately update-only.  The initial +1 stabilizer character,
clean controller registers, autonomous boundary/coframe choice, and recurrent
preparation/genesis are not inferred from update closure.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ROUTE_SCRIPTS = ROOT / "scripts"
ROOT_PLACEMENT_SOURCE = ROUTE_SCRIPTS / (
    "frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py"
)
sys.path.insert(0, str(ROUTE_SCRIPTS))

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
)
EXPECTED_DEPENDENCY_SHA256 = {
    "frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py": "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
    "ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py": "717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9",
    "common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py": "833ac9ee1d7f83185fdd66d89e2f3208e514c0b3b2cff660e7227dc28f506245",
    "frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py": "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
    "frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py": "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
}

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25 as prep
import frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26 as c706
import frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26 as c707
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


def load_root_placement():
    spec = importlib.util.spec_from_file_location(
        "cycle870_root_openreference_placement", ROOT_PLACEMENT_SOURCE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load root placement probe")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


root_place = load_root_placement()

Coord = tuple[int, int, int]
Pauli = base.Pauli
REVERSE = tuple(int(value) for value in base.REVERSE)
MODE_PATH = (0, 2, 1, 4, 3, 5)
PRIMARY_CENTERS = ((0, 0, 0), (1, 0, 0))
HELD_SHAPE = (3, 2, 2)
TOL = 2.0e-9


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * item for item in row)


def matvec(frame: np.ndarray, row: Coord) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(row, dtype=int))


def box_cells(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(product(*(range(length) for length in shape)))


def star_cells(center: Coord) -> tuple[Coord, ...]:
    rows = {center}
    for axis in range(3):
        for sign in (-1, 1):
            delta = tuple(sign if index == axis else 0 for index in range(3))
            rows.add(add(center, delta))
    return tuple(sorted(rows))


def two_star_union() -> tuple[Coord, ...]:
    return tuple(sorted(set(star_cells(PRIMARY_CENTERS[0])) | set(star_cells(PRIMARY_CENTERS[1]))))


def pauli_product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = result @ row
    return result


def pauli_weight(row: Pauli) -> int:
    return (row.x | row.z).bit_count()


def is_hermitian(row: Pauli) -> bool:
    return (row.phase - (row.x & row.z).bit_count()) % 2 == 0


def local_d(graph: prep.OpenReferenceGraph, cell: Coord) -> Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def local_stabilizers(graph: prep.OpenReferenceGraph) -> tuple[Pauli, ...]:
    loops = tuple(
        graph.loop_pauli(vertices)
        for _mask, vertices, _kind, _key in prep.open_local_cycles(graph)
    )
    return loops + tuple(local_d(graph, cell) for cell in graph.cells[:-1])


def edge_address(graph: prep.OpenReferenceGraph, edge: int):
    u, v, kind, _owner = graph.edges[edge]
    return kind, frozenset((graph.vertices[u], graph.vertices[v]))


def address_placement(graph, site_map):
    return {
        edge_address(graph, edge): tuple(sites)
        for edge, sites in site_map.items()
    }


def carrier_placement(graph: prep.OpenReferenceGraph):
    """Consume the exact Cycle870 root placement rule."""
    return root_place.carrier_placement(graph)


@dataclass(frozen=True)
class PhysicalContext:
    graph: prep.OpenReferenceGraph
    site_map: dict[int, tuple[Coord, ...]]
    sites: tuple[Coord, ...]
    index: dict[Coord, int]


def physical_context(graph: prep.OpenReferenceGraph) -> PhysicalContext:
    site_map = carrier_placement(graph)
    sites = tuple(sorted(root_place.occupied(site_map)))
    return PhysicalContext(graph, site_map, sites, {site: index for index, site in enumerate(sites)})


def physical_lift(row: Pauli, context: PhysicalContext) -> Pauli:
    x = z = 0
    for edge, carriers in context.site_map.items():
        if (row.x >> edge) & 1:
            for carrier in carriers:
                x ^= 1 << context.index[carrier]
        if (row.z >> edge) & 1:
            z ^= 1 << context.index[carriers[0]]
    return Pauli(row.phase, x, z)


def repetition_rows(context: PhysicalContext) -> tuple[Pauli, ...]:
    rows = []
    for edge, (_u, _v, kind, _owner) in enumerate(context.graph.edges):
        if kind != "matter_stream":
            continue
        left, right = context.site_map[edge]
        rows.append(Pauli(z=(1 << context.index[left]) | (1 << context.index[right])))
    return tuple(rows)


def physical_stabilizers(context: PhysicalContext) -> tuple[Pauli, ...]:
    return tuple(physical_lift(row, context) for row in local_stabilizers(context.graph)) + repetition_rows(context)


def support_diameter(row: Pauli, sites: tuple[Coord, ...]) -> int:
    points = [sites[index] for index in range(len(sites)) if ((row.x | row.z) >> index) & 1]
    return max(
        (
            sum(abs(a - b) for a, b in zip(left, right))
            for left in points
            for right in points
        ),
        default=0,
    )


def direct_hop_rows(graph, cell: Coord, left: int, right: int) -> tuple[Pauli, Pauli]:
    u = graph.vertex_index[(cell, left)]
    v = graph.vertex_index[(cell, right)]
    a = graph.A(u, v)
    return (
        Pauli(phase=3) @ graph.B(u) @ a,
        Pauli(phase=1) @ graph.B(v) @ a,
    )


def seam_hop_rows(
    graph,
    left_cell: Coord,
    left_mode: int,
    right_cell: Coord,
    right_mode: int,
) -> tuple[Pauli, Pauli]:
    u = graph.vertex_index[(left_cell, left_mode)]
    v = graph.vertex_index[(right_cell, right_mode)]
    ru = graph.vertex_index[(left_cell, 6)]
    rv = graph.vertex_index[(right_cell, 6)]
    core = graph.A(u, v) @ graph.A(ru, rv)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(right_cell, mode)])
        for mode in range(6)
        if mode != right_mode
    )
    return (
        Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(u) @ graph.B(v) @ core,
    )


def semantic_row(graph, meta: tuple[object, ...]) -> Pauli:
    kind = meta[0]
    if kind == "B":
        _, cell, mode = meta
        return graph.B(graph.vertex_index[(cell, mode)])
    if kind == "BB":
        _, cell, left, right = meta
        return semantic_row(graph, ("B", cell, left)) @ semantic_row(graph, ("B", cell, right))
    if kind in ("direct_h1", "direct_h2"):
        _, cell, left, right = meta
        return direct_hop_rows(graph, cell, left, right)[kind.endswith("2")]
    if kind in ("seam_h1", "seam_h2"):
        _, left_cell, left_mode, right_cell, right_mode = meta
        return seam_hop_rows(
            graph, left_cell, left_mode, right_cell, right_mode
        )[kind.endswith("2")]
    raise ValueError(("unknown semantic row", meta))


Poly = dict[Pauli, complex]


def poly_clean(poly: Poly, tolerance: float = 2.0e-12) -> Poly:
    # Fold i^phase into the coefficient so equal X^x Z^z words written with
    # phases 0 and 2 cancel in the same dictionary slot.
    output: Poly = {}
    for row, coefficient in poly.items():
        canonical = Pauli(0, row.x, row.z)
        output[canonical] = output.get(canonical, 0.0j) + (1j ** row.phase) * coefficient
    return {
        row: coefficient
        for row, coefficient in output.items()
        if abs(coefficient) > tolerance
    }


def poly_add(*polys: Poly) -> Poly:
    output: Poly = {}
    for poly in polys:
        for row, coefficient in poly.items():
            output[row] = output.get(row, 0.0j) + coefficient
    return poly_clean(output)


def poly_scale(poly: Poly, scalar: complex) -> Poly:
    return poly_clean({row: scalar * coefficient for row, coefficient in poly.items()})


def poly_mul(left: Poly, right: Poly) -> Poly:
    output: Poly = {}
    for lrow, lcoefficient in left.items():
        for rrow, rcoefficient in right.items():
            row = lrow @ rrow
            output[row] = output.get(row, 0.0j) + lcoefficient * rcoefficient
    return poly_clean(output)


def poly_residual(left: Poly, right: Poly) -> float:
    keys = set(left) | set(right)
    return float(math.sqrt(sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in keys)))


def aligned_poly_residual(observed: Poly, expected: Poly) -> tuple[float, complex]:
    keys = set(observed) | set(expected)
    overlap = sum(np.conj(expected.get(key, 0.0j)) * observed.get(key, 0.0j) for key in keys)
    phase = overlap / abs(overlap) if abs(overlap) else 1.0 + 0.0j
    return poly_residual(observed, poly_scale(expected, phase)), complex(phase)


def fswap_polynomial(rows: tuple[Pauli, Pauli, Pauli, Pauli]) -> Poly:
    return poly_add(*(poly_scale({row: 1.0 + 0.0j}, 0.5) for row in rows))


def rotation_polynomial(row: Pauli, angle: float) -> Poly:
    return {
        Pauli(): complex(math.cos(angle / 2)),
        row: complex(-1j * math.sin(angle / 2)),
    }


def fswap_factorization(rows: tuple[Pauli, Pauli, Pauli, Pauli], deleted: int | None = None) -> Poly:
    output: Poly = {Pauli(): 1.0 + 0.0j}
    for index, row in enumerate(rows):
        if index == deleted:
            continue
        output = poly_mul(rotation_polynomial(row, math.pi / 2), output)
    return output


def fswap_certificate(rows: tuple[Pauli, Pauli, Pauli, Pauli]) -> dict[str, object]:
    target = fswap_polynomial(rows)
    identity = {Pauli(): 1.0 + 0.0j}
    involution = poly_residual(poly_mul(target, target), identity)
    factorization, phase = aligned_poly_residual(fswap_factorization(rows), target)
    term_deletions = []
    for deleted in range(4):
        reduced = fswap_polynomial(tuple(row for index, row in enumerate(rows) if index != deleted))
        term_deletions.append(poly_residual(poly_mul(reduced, reduced), identity))
    rotation_deletions = [
        aligned_poly_residual(fswap_factorization(rows, deleted), target)[0]
        for deleted in range(4)
    ]
    return {
        "hermitian_term_failures": sum(not is_hermitian(row) for row in rows),
        "full_space_involution_residual": involution,
        "four_rotation_residual_up_to_global_phase": factorization,
        "four_rotation_global_phase": [phase.real, phase.imag],
        "term_deletion_involution_residuals": term_deletions,
        "rotation_deletion_residuals": rotation_deletions,
    }


def direct_fswap_poly(graph, cell: Coord, left: int, right: int) -> Poly:
    rows = (
        semantic_row(graph, ("B", cell, left)),
        semantic_row(graph, ("B", cell, right)),
        *direct_hop_rows(graph, cell, left, right),
    )
    return fswap_polynomial(rows)


def gaussian_pair_algebra_certificate(graph, cell: Coord, pairs) -> dict[str, object]:
    identity = {Pauli(): 1.0 + 0.0j}
    square_failures = anticommutator_failures = projector_failures = 0
    hop_commutator_failures = hermitian_failures = 0
    maximum_residual = 0.0
    for left, right in sorted(set(tuple(pair) for pair in pairs)):
        bu = semantic_row(graph, ("B", cell, left))
        bv = semantic_row(graph, ("B", cell, right))
        h1, h2 = direct_hop_rows(graph, cell, left, right)
        hermitian_failures += sum(not is_hermitian(row) for row in (bu, bv, h1, h2))
        hop_commutator_failures += not h1.commutes(h2)
        odd = poly_add(
            poly_scale(identity, 0.5),
            poly_scale({bu @ bv: 1.0 + 0.0j}, -0.5),
        )
        xaxis = poly_add(
            poly_scale({h1: 1.0 + 0.0j}, 0.5),
            poly_scale({h2: 1.0 + 0.0j}, 0.5),
        )
        zaxis = poly_add(
            poly_scale({bv: 1.0 + 0.0j}, 0.5),
            poly_scale({bu: 1.0 + 0.0j}, -0.5),
        )
        x_square = poly_residual(poly_mul(xaxis, xaxis), odd)
        z_square = poly_residual(poly_mul(zaxis, zaxis), odd)
        anticommutator = poly_residual(
            poly_add(poly_mul(xaxis, zaxis), poly_mul(zaxis, xaxis)), {}
        )
        x_projected = poly_residual(poly_mul(odd, xaxis), xaxis)
        z_projected = poly_residual(poly_mul(odd, zaxis), zaxis)
        residuals = (x_square, z_square, anticommutator, x_projected, z_projected)
        maximum_residual = max(maximum_residual, *residuals)
        square_failures += x_square > TOL or z_square > TOL
        anticommutator_failures += anticommutator > TOL
        projector_failures += x_projected > TOL or z_projected > TOL
    return {
        "allowed_mode_pairs": len(set(tuple(pair) for pair in pairs)),
        "Hermiticity_failures": hermitian_failures,
        "commuting_hop_summand_failures": hop_commutator_failures,
        "odd_sector_axis_square_failures": square_failures,
        "XZ_anticommutator_failures": anticommutator_failures,
        "odd_projector_action_failures": projector_failures,
        "maximum_native_su2_residual": maximum_residual,
        "meaning": "intrinsic B/A algebra certifies the QR/Euler coin lift without a global-JW chart",
    }


def reverse_braid_certificate(graph, cell: Coord) -> dict[str, object]:
    identity = {Pauli(): 1.0 + 0.0j}
    involution_residuals = []
    occupation_conjugation_residuals = []
    deletion_residuals = []
    for left, right in ((0, 1), (2, 3), (4, 5)):
        helper = reverse_helper(left, right)
        factors = (
            direct_fswap_poly(graph, cell, left, helper),
            direct_fswap_poly(graph, cell, right, helper),
            direct_fswap_poly(graph, cell, left, helper),
        )
        word = identity
        for factor in factors:
            word = poly_mul(factor, word)
        involution_residuals.append(poly_residual(poly_mul(word, word), identity))
        for source, target in ((left, right), (right, left), (helper, helper)):
            observed = poly_mul(
                word,
                poly_mul(
                    {semantic_row(graph, ("B", cell, source)): 1.0 + 0.0j},
                    word,
                ),
            )
            expected = {semantic_row(graph, ("B", cell, target)): 1.0 + 0.0j}
            occupation_conjugation_residuals.append(poly_residual(observed, expected))
        for deleted in range(3):
            reduced = identity
            for index, factor in enumerate(factors):
                if index != deleted:
                    reduced = poly_mul(factor, reduced)
            deletion_residuals.append(poly_residual(reduced, word))
    return {
        "reverse_pairs": 3,
        "maximum_full_space_braid_involution_residual": max(involution_residuals),
        "maximum_occupation_conjugation_residual": max(occupation_conjugation_residuals),
        "minimum_helper_FSWAP_deletion_residual": min(deletion_residuals),
    }


@dataclass(frozen=True)
class OneParticleGate:
    kind: str
    modes: tuple[int, ...]
    matrix: np.ndarray


def embed_one_particle(matrix: np.ndarray, modes: tuple[int, ...]) -> np.ndarray:
    output = np.eye(6, dtype=complex)
    output[np.ix_(modes, modes)] = matrix
    return output


def qr_coin_schedule(coin: np.ndarray) -> tuple[tuple[OneParticleGate, ...], dict[str, float]]:
    order = MODE_PATH
    work = np.asarray(coin, dtype=complex)[np.ix_(order, order)].copy()
    eliminations = []
    for column in range(5):
        for lower in range(5, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) < 1.0e-13:
                continue
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                (
                    (np.conj(a) / radius, np.conj(b) / radius),
                    (-b / radius, a / radius),
                ),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    gates = []
    for position, value in enumerate(np.diag(work)):
        phase = value / abs(value)
        gates.append(
            OneParticleGate(
                "phase", (order[position],), np.asarray(((phase,),), dtype=complex)
            )
        )
    for upper, lower, elimination in reversed(eliminations):
        gates.append(
            OneParticleGate(
                "u2",
                (order[upper], order[lower]),
                elimination.conj().T,
            )
        )
    reconstructed = np.eye(6, dtype=complex)
    for gate in gates:
        if gate.kind == "phase":
            matrix = np.eye(6, dtype=complex)
            matrix[gate.modes[0], gate.modes[0]] = gate.matrix[0, 0]
        else:
            matrix = embed_one_particle(gate.matrix, gate.modes)
        reconstructed = matrix @ reconstructed
    return tuple(gates), {
        "QR_off_diagonal_residual": float(np.linalg.norm(work - np.diag(np.diag(work)))),
        "reconstruction_residual": float(np.linalg.norm(reconstructed - coin)),
        "eliminations": len(eliminations),
    }


def rz(angle: float) -> np.ndarray:
    return np.diag((np.exp(-0.5j * angle), np.exp(0.5j * angle))).astype(complex)


def rx(angle: float) -> np.ndarray:
    c, s = math.cos(angle / 2), math.sin(angle / 2)
    return np.asarray(((c, -1j * s), (-1j * s, c)), dtype=complex)


def euler_zxz_candidate(unitary: np.ndarray, delta: float):
    special = np.exp(-1j * delta) * unitary
    cabs, sabs = abs(special[0, 0]), abs(special[1, 0])
    beta = 2 * math.atan2(sabs, cabs)
    if sabs < 1.0e-12:
        alpha = -2 * float(np.angle(special[0, 0]))
        gamma = 0.0
    elif cabs < 1.0e-12:
        alpha = 2 * (float(np.angle(special[1, 0])) + math.pi / 2)
        gamma = 0.0
    else:
        p = float(np.angle(special[0, 0]))
        q = float(np.angle(special[1, 0]))
        alpha = -p + q + math.pi / 2
        gamma = -p - q - math.pi / 2
    reconstructed = np.exp(1j * delta) * rz(alpha) @ rx(beta) @ rz(gamma)
    return (delta, alpha, beta, gamma), float(np.linalg.norm(reconstructed - unitary))


def euler_zxz(unitary: np.ndarray):
    delta = 0.5 * float(np.angle(np.linalg.det(unitary)))
    candidates = [euler_zxz_candidate(unitary, delta + offset) for offset in (0.0, math.pi)]
    return min(candidates, key=lambda row: row[1])


@dataclass(frozen=True)
class Rotation:
    serial: int
    kind: str
    factor: tuple[object, ...]
    meta: tuple[object, ...]
    row: Pauli
    angle: float


class RotationBuilder:
    def __init__(self, graph):
        self.graph = graph
        self.rows: list[Rotation] = []

    def add(self, kind: str, factor, meta, angle: float):
        if abs(angle) < 1.0e-13:
            return
        row = semantic_row(self.graph, tuple(meta))
        self.rows.append(
            Rotation(len(self.rows), kind, tuple(factor), tuple(meta), row, float(angle))
        )


def add_z_rotation(builder: RotationBuilder, kind: str, factor, cell, left, right, angle):
    builder.add(kind, factor, ("B", cell, right), angle / 2)
    builder.add(kind, factor, ("B", cell, left), -angle / 2)


def add_rx_rotation(builder: RotationBuilder, kind: str, factor, cell, left, right, angle):
    builder.add(kind, factor, ("direct_h1", cell, left, right), angle / 2)
    builder.add(kind, factor, ("direct_h2", cell, left, right), angle / 2)


def add_u2(builder: RotationBuilder, cell: Coord, factor, modes, unitary, euler_residuals):
    (delta, alpha, beta, gamma), residual = euler_zxz(unitary)
    euler_residuals.append(residual)
    left, right = modes
    builder.add("onsite_coin_mass", factor, ("B", cell, left), delta)
    builder.add("onsite_coin_mass", factor, ("B", cell, right), delta)
    add_z_rotation(builder, "onsite_coin_mass", factor, cell, left, right, gamma)
    add_rx_rotation(builder, "onsite_coin_mass", factor, cell, left, right, beta)
    add_z_rotation(builder, "onsite_coin_mass", factor, cell, left, right, alpha)


def add_direct_fswap(builder: RotationBuilder, kind: str, factor, cell, left, right):
    builder.add(kind, factor, ("B", cell, left), math.pi / 2)
    builder.add(kind, factor, ("B", cell, right), math.pi / 2)
    builder.add(kind, factor, ("direct_h1", cell, left, right), math.pi / 2)
    builder.add(kind, factor, ("direct_h2", cell, left, right), math.pi / 2)


def add_seam_fswap(builder: RotationBuilder, factor, left_cell, left_mode, right_cell, right_mode):
    builder.add("directed_seam_fswap", factor, ("B", left_cell, left_mode), math.pi / 2)
    builder.add("directed_seam_fswap", factor, ("B", right_cell, right_mode), math.pi / 2)
    builder.add(
        "directed_seam_fswap",
        factor,
        ("seam_h1", left_cell, left_mode, right_cell, right_mode),
        math.pi / 2,
    )
    builder.add(
        "directed_seam_fswap",
        factor,
        ("seam_h2", left_cell, left_mode, right_cell, right_mode),
        math.pi / 2,
    )


def reverse_helper(left: int, right: int) -> int:
    return next(
        mode
        for mode in range(6)
        if mode not in (left, right)
        and REVERSE[left] != mode
        and REVERSE[right] != mode
    )


def graph_seams(graph):
    rows = []
    for (cell, axis, copy), _edge in graph.cross_edge.items():
        if copy != 0:
            continue
        target = list(cell)
        target[axis] += 1
        rows.append((cell, axis, tuple(target), 2 * axis + 1, 2 * axis))
    return tuple(sorted(rows, key=lambda row: (row[1], row[0][row[1]] & 1, row[0])))


def build_update(graph, coin_gates):
    builder = RotationBuilder(graph)
    euler_residuals = []
    # Convention: U_rotations = exp(i * compiled_relative_phase) G_native.
    # The exact target word therefore carries the formal zero-site scalar
    # exp(-i * compiled_relative_phase).  This scalar has no routed M2 cost.
    compiled_relative_phase = 0.0
    phase_breakdown = Counter()
    for cell in graph.cells:
        for gate_index, gate in enumerate(coin_gates):
            factor = ("coin", cell, gate_index, gate.modes)
            if gate.kind == "phase":
                phase = float(np.angle(gate.matrix[0, 0]))
                builder.add("onsite_coin_mass", factor, ("B", cell, gate.modes[0]), phase)
                contribution = -phase / 2
                compiled_relative_phase += contribution
                phase_breakdown["coin"] += contribution
            else:
                decomposition, _residual = euler_zxz(gate.matrix)
                contribution = -decomposition[0]
                compiled_relative_phase += contribution
                phase_breakdown["coin"] += contribution
                add_u2(
                    builder,
                    cell,
                    factor,
                    gate.modes,
                    gate.matrix,
                    euler_residuals,
                )

    reverse_direct_factors = 0
    for cell in graph.cells:
        for left, right in ((0, 1), (2, 3), (4, 5)):
            helper = reverse_helper(left, right)
            for step, pair in enumerate(((left, helper), (right, helper), (left, helper))):
                add_direct_fswap(
                    builder,
                    "onsite_reverse_fswap",
                    ("reverse", cell, left, right, step, pair),
                    cell,
                    pair[0],
                    pair[1],
                )
                # Four commuting pi/2 rotations equal -i times one FSWAP.
                contribution = -math.pi / 2
                compiled_relative_phase += contribution
                phase_breakdown["reverse_FSWAP"] += contribution
                reverse_direct_factors += 1

    seams = graph_seams(graph)
    for seam_index, (cell, axis, target, left_mode, right_mode) in enumerate(seams):
        add_seam_fswap(
            builder,
            ("seam", seam_index, cell, axis, target),
            cell,
            left_mode,
            target,
            right_mode,
        )
        contribution = -math.pi / 2
        compiled_relative_phase += contribution
        phase_breakdown["seam_FSWAP"] += contribution

    coupling = float(c230.COUPLING)
    for cell in graph.cells:
        for left, right in combinations(range(6), 2):
            factor = ("contact", cell, left, right)
            builder.add("onsite_contact", factor, ("B", cell, left), coupling / 2)
            builder.add("onsite_contact", factor, ("B", cell, right), coupling / 2)
            builder.add("onsite_contact", factor, ("BB", cell, left, right), -coupling / 2)
            contribution = -coupling / 4
            compiled_relative_phase += contribution
            phase_breakdown["contact"] += contribution

    # The breakdown is the analytic ledger.  Reconstruct the total from its
    # named components so the reported scalar and the audit checksum share one
    # numerically stable summation convention.
    compiled_relative_phase = math.fsum(phase_breakdown.values())

    return tuple(builder.rows), {
        "coin_euler_max_residual": max(euler_residuals, default=0.0),
        "coin_one_particle_gates_per_cell": len(coin_gates),
        "logical_reverse_FSWAPs": 3 * len(graph.cells),
        "direct_reverse_helper_FSWAPs": reverse_direct_factors,
        "seam_FSWAPs": len(seams),
        "contact_pairs": 15 * len(graph.cells),
        "phase_convention": (
            "U_rotations = exp(i*compiled_relative_to_target_global_phase_angle) "
            "G_native_exact"
        ),
        "compiled_relative_to_target_global_phase_angle": compiled_relative_phase,
        "compiled_relative_phase_breakdown": dict(sorted(phase_breakdown.items())),
        "phase_breakdown_sum_residual": abs(
            compiled_relative_phase - math.fsum(phase_breakdown.values())
        ),
        "exact_target_global_phase_correction_angle": -compiled_relative_phase,
        "global_phase_correction_routed_gate_count": 0,
    }


def contact_semantics() -> dict[str, object]:
    coupling = float(c230.COUPLING)
    ratios = []
    observed = []
    expected = []
    for bits in product((0, 1), repeat=6):
        phase = 1.0 + 0.0j
        for left, right in combinations(range(6), 2):
            bi = -1 if bits[left] else 1
            bj = -1 if bits[right] else 1
            phase *= np.exp(-0.25j * coupling * bi)
            phase *= np.exp(-0.25j * coupling * bj)
            phase *= np.exp(0.25j * coupling * bi * bj)
        target = np.exp(1j * coupling * sum(bits) * (sum(bits) - 1) / 2)
        observed.append(phase)
        expected.append(target)
        if abs(target):
            ratios.append(phase / target)
    anchor = ratios[0] / abs(ratios[0])
    return {
        "occupation_words": 64,
        "maximum_residual_up_to_global_phase": max(
            abs(left - anchor * right) for left, right in zip(observed, expected)
        ),
        "global_phase": [anchor.real, anchor.imag],
        "contact_pairs": 15,
    }


def one_particle_semantics(coin, coin_gates) -> dict[str, object]:
    frames = base.proper_cubic_frames()
    covariance = []
    for frame in frames:
        mapping = base.direction_map(frame)
        permutation = np.zeros((6, 6), dtype=complex)
        for source, target in mapping.items():
            permutation[target, source] = 1
        covariance.append(float(np.linalg.norm(permutation @ coin @ permutation.conj().T - coin)))

    reverse = np.eye(6, dtype=complex)
    for left, right in ((0, 1), (2, 3), (4, 5)):
        helper = reverse_helper(left, right)
        for pair in ((left, helper), (right, helper), (left, helper)):
            swap = np.eye(6, dtype=complex)
            swap[pair[0], pair[0]] = swap[pair[1], pair[1]] = 0
            swap[pair[0], pair[1]] = swap[pair[1], pair[0]] = 1
            reverse = swap @ reverse
    species = c219.common_species(float(c230.BETA))
    scalar_phase = np.vdot(base.c210.UNIFORM, coin @ base.c210.UNIFORM)
    return {
        "coin_unitarity_residual": float(np.linalg.norm(coin.conj().T @ coin - np.eye(6))),
        "proper_cubic_frames": len(frames),
        "maximum_coin_covariance_residual": max(covariance),
        "reverse_helper_permutation_residual": float(np.linalg.norm(reverse - base.c210.REVERSE)),
        "beta": float(c230.BETA),
        "analytic_mass": float(species.analytic_mass),
        "rest_mass": float(c219.rest_mass(species)),
        "scalar_rest_phase": float(np.angle(scalar_phase)),
        "one_particle_schedule_gates": len(coin_gates),
    }


def constraint_certificate(graph, context, rotations) -> dict[str, object]:
    abstract = local_stabilizers(graph)
    physical = physical_stabilizers(context)
    abstract_qubits = len(graph.edges)
    physical_qubits = len(context.sites)
    abstract_rank = base.gf2_rank(row.symplectic(abstract_qubits) for row in abstract)
    physical_rank = base.gf2_rank(row.symplectic(physical_qubits) for row in physical)
    lifted_rows = [physical_lift(rotation.row, context) for rotation in rotations]
    lift_homomorphism_failures = 0
    for edge in range(abstract_qubits):
        xrow = Pauli(x=1 << edge)
        zrow = Pauli(z=1 << edge)
        lift_homomorphism_failures += (
            physical_lift(xrow @ zrow, context)
            != physical_lift(xrow, context) @ physical_lift(zrow, context)
        )
        lift_homomorphism_failures += (
            physical_lift(zrow @ xrow, context)
            != physical_lift(zrow, context) @ physical_lift(xrow, context)
        )
    return {
        "abstract_edge_qubits": abstract_qubits,
        "physical_carrier_M2": physical_qubits,
        "abstract_constraint_rows": len(abstract),
        "abstract_constraint_rank": abstract_rank,
        "expected_abstract_rank": abstract_qubits - 6 * len(graph.cells),
        "repetition_constraints": len(repetition_rows(context)),
        "physical_constraint_rows": len(physical),
        "physical_constraint_rank": physical_rank,
        "expected_physical_rank": physical_qubits - 6 * len(graph.cells),
        "abstract_phase_dependency_failures": base.stabilizer_phase_failures(list(abstract), abstract_qubits),
        "physical_phase_dependency_failures": base.stabilizer_phase_failures(list(physical), physical_qubits),
        "abstract_constraint_commutator_failures": sum(
            not left.commutes(right)
            for index, left in enumerate(abstract)
            for right in abstract[index + 1 :]
        ),
        "physical_constraint_commutator_failures": sum(
            not left.commutes(right)
            for index, left in enumerate(physical)
            for right in physical[index + 1 :]
        ),
        "abstract_update_preservation_failures": sum(
            not rotation.row.commutes(stabilizer)
            for rotation in rotations
            for stabilizer in abstract
        ),
        "physical_update_preservation_failures": sum(
            not row.commutes(stabilizer)
            for row in lifted_rows
            for stabilizer in physical
        ),
        "signed_repetition_lift_homomorphism_failures": lift_homomorphism_failures,
        "update_hermiticity_failures": sum(not is_hermitian(row) for row in lifted_rows),
        "maximum_abstract_rotation_weight": max(map(pauli_weight, (rotation.row for rotation in rotations))),
        "maximum_physical_rotation_weight": max(map(pauli_weight, lifted_rows)),
        "maximum_physical_rotation_diameter": max(
            support_diameter(row, context.sites) for row in lifted_rows
        ),
        "all_D_product_identity": pauli_product(local_d(graph, cell) for cell in graph.cells) == Pauli(),
    }


def route_update(context: PhysicalContext, rotations) -> dict[str, object]:
    primitive_counts: Counter[str] = Counter()
    routed_counts: Counter[str] = Counter()
    primitive_digest = sha256()
    routed_digest = sha256()
    routed_gates = maximum_distance = non_nn = operand_failures = return_failures = 0
    deletion_detected = 0
    touched = set()
    occupied = set(context.sites)
    traversed_occupied_spectators = set()
    endpoint_pairs = 0
    for rotation in rotations:
        physical = physical_lift(rotation.row, context)
        word = c707.compile_pauli_rotation(physical, context.sites, rotation.angle)
        for instruction in word:
            primitive_counts[instruction.kind] += 1
            matrix_hash = c707.c655.matrix_digest(instruction.matrix)
            primitive_digest.update(
                f"{instruction.kind}:{instruction.sites}:{matrix_hash}".encode()
            )
            if len(instruction.sites) == 1:
                routed_gates += 1
                routed_counts[instruction.kind] += 1
                routed_digest.update(
                    f"{instruction.kind}:{instruction.sites}:{matrix_hash}".encode()
                )
                touched.update(instruction.sites)
                continue
            endpoint_pairs += 1
            left, right = instruction.sites
            path = tuple(c707.c655.manhattan_path(left, right))
            distance = len(path) - 1
            maximum_distance = max(maximum_distance, distance)
            non_nn += sum(c707.c655.l1(a, b) != 1 for a, b in zip(path, path[1:]))
            labels = list(path)
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            operand_failures += labels[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            return_failures += labels != list(path)
            if len(path) > 2:
                deleted = list(path)
                for index in range(1, len(path) - 2):
                    deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
                for index in reversed(range(len(path) - 2)):
                    deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
                deletion_detected += deleted != list(path)
            for index in range(len(path) - 2):
                sites = (path[index], path[index + 1])
                routed_counts["route_swap"] += 1
                routed_digest.update(f"route_swap:{sites}:SWAP".encode())
            gate_sites = (path[-2], path[-1])
            routed_counts[instruction.kind] += 1
            routed_digest.update(f"{instruction.kind}:{gate_sites}:{matrix_hash}".encode())
            for index in reversed(range(len(path) - 2)):
                sites = (path[index], path[index + 1])
                routed_counts["route_swap"] += 1
                routed_digest.update(f"route_swap:{sites}:SWAP".encode())
            routed_gates += 2 * distance - 1
            touched.update(path)
            traversed_occupied_spectators.update((set(path) & occupied) - {left, right})
    # Every routed two-site edge is a unit coordinate edge by construction;
    # explicitly recheck its proper-cubic orbit.
    unit_steps = tuple(
        tuple(sign if index == axis else 0 for index in range(3))
        for axis in range(3)
        for sign in (-1, 1)
    )
    rotated_step_failures = sum(
        sum(abs(value) for value in matvec(frame, step)) != 1
        for frame in base.proper_cubic_frames()
        for step in unit_steps
    )
    return {
        "rotations": len(rotations),
        "primitive_gate_count": sum(primitive_counts.values()),
        "primitive_kind_census": dict(sorted(primitive_counts.items())),
        "primitive_word_sha256": primitive_digest.hexdigest(),
        "two_site_primitive_count": endpoint_pairs,
        "routed_gate_count": routed_gates,
        "routed_kind_census": dict(sorted(routed_counts.items())),
        "routed_word_sha256": routed_digest.hexdigest(),
        "maximum_route_distance": maximum_distance,
        "non_NN_failures": non_nn,
        "operand_order_failures": operand_failures,
        "route_return_failures": return_failures,
        "first_swap_deletion_detected_macros": deletion_detected,
        "touched_lattice_sites": len(touched),
        "occupied_spectator_sites_traversed_and_returned": len(traversed_occupied_spectators),
        "proper_cubic_rotated_unit_step_failures": rotated_step_failures,
        "schedule": "supplied serial factor/primitive order; no parallel-depth claim",
        "persistent_route_work_M2": 0,
    }


def map_meta(meta, cell_map, direction_map):
    kind = meta[0]
    if kind == "B":
        _, cell, mode = meta
        return kind, cell_map[cell], direction_map[mode]
    if kind == "BB":
        _, cell, left, right = meta
        return kind, cell_map[cell], direction_map[left], direction_map[right]
    if kind in ("direct_h1", "direct_h2"):
        _, cell, left, right = meta
        return kind, cell_map[cell], direction_map[left], direction_map[right]
    if kind in ("seam_h1", "seam_h2"):
        _, left_cell, left_mode, right_cell, right_mode = meta
        return (
            kind,
            cell_map[left_cell],
            direction_map[left_mode],
            cell_map[right_cell],
            direction_map[right_mode],
        )
    raise ValueError(meta)


def covariance_certificate(graph, context, rotations, do_products: bool) -> dict[str, object]:
    frames = base.proper_cubic_frames()
    frame_operator_failures = frame_angle_failures = graph_generator_failures = 0
    placement_failures = 0
    base_addresses = address_placement(graph, context.site_map)
    transforms = {}
    targets = {}
    for frame_index, frame in enumerate(frames):
        cells = tuple(matvec(frame, cell) for cell in graph.cells)
        target = prep.OpenReferenceGraph(cells)
        targets[frame_index] = target
        transform = c706.graph_transform_data(graph, target, frame)
        transforms[frame_index] = transform
        cell_map, direction, edge_map, toggles, pairs, flips, failures = transform
        graph_generator_failures += failures
        for rotation in rotations:
            observed = c706.transform_graph_pauli(
                rotation.row, edge_map, toggles, pairs, flips
            )
            expected = semantic_row(target, map_meta(rotation.meta, cell_map, direction))
            frame_operator_failures += observed != expected
            frame_angle_failures += not math.isfinite(rotation.angle)
        target_map = address_placement(target, carrier_placement(target))
        for address, sites in base_addresses.items():
            ulabel = tuple(address[1])
            mapped_vertices = frozenset(
                (
                    cell_map[cell],
                    6 if mode == 6 else direction[mode],
                )
                for cell, mode in ulabel
            )
            mapped_address = (address[0], mapped_vertices)
            placement_failures += set(target_map[mapped_address]) != {
                matvec(frame, site) for site in sites
            }

    meta_product_failures = signed_generator_product_failures = 0
    coordinate_product_failures = 0
    if do_products:
        frame_lookup = {
            tuple(int(value) for value in frame.flat): index
            for index, frame in enumerate(frames)
        }
        generators = tuple(
            [Pauli(x=1 << edge) for edge in range(len(graph.edges))]
            + [Pauli(z=1 << edge) for edge in range(len(graph.edges))]
        )
        for left_index, left in enumerate(frames):
            for right_index, right in enumerate(frames):
                product_frame = left @ right
                product_index = frame_lookup[tuple(int(value) for value in product_frame.flat)]
                first = transforms[right_index]
                middle = targets[right_index]
                final_cells = tuple(matvec(left, cell) for cell in middle.cells)
                final = prep.OpenReferenceGraph(final_cells)
                second = c706.graph_transform_data(middle, final, left)
                direct = transforms[product_index]
                graph_generator_failures += second[-1]
                for generator in generators:
                    midway = c706.transform_graph_pauli(
                        generator, first[2], first[3], first[4], first[5]
                    )
                    sequential = c706.transform_graph_pauli(
                        midway, second[2], second[3], second[4], second[5]
                    )
                    direct_row = c706.transform_graph_pauli(
                        generator, direct[2], direct[3], direct[4], direct[5]
                    )
                    signed_generator_product_failures += sequential != direct_row
                right_cell, right_direction = first[0], first[1]
                left_cell, left_direction = second[0], second[1]
                direct_cell, direct_direction = direct[0], direct[1]
                for rotation in rotations:
                    sequential_meta = map_meta(
                        map_meta(rotation.meta, right_cell, right_direction),
                        left_cell,
                        left_direction,
                    )
                    direct_meta = map_meta(rotation.meta, direct_cell, direct_direction)
                    meta_product_failures += sequential_meta != direct_meta
                for site in context.sites:
                    coordinate_product_failures += matvec(left, matvec(right, site)) != matvec(product_frame, site)
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2 if do_products else 0,
        "graph_generator_transport_failures": graph_generator_failures,
        "all_update_rotation_transport_failures": frame_operator_failures,
        "rotation_parameter_transport_failures": frame_angle_failures,
        "carrier_set_transport_failures": placement_failures,
        "update_metadata_product_failures": meta_product_failures,
        "signed_AB_generator_product_failures": signed_generator_product_failures,
        "physical_coordinate_product_failures": coordinate_product_failures,
        "coframe": "supplied and transported; lab-fixed textual rebuild is not claimed",
    }


def translation_certificate(graph, context, rotations) -> dict[str, object]:
    failures = placement_failures = 0
    cases = ((0, 0, 0), (1, -2, 3), (-3, 1, 2), (2, 2, -1))
    for shift in cases:
        target = prep.OpenReferenceGraph(tuple(add(cell, shift) for cell in graph.cells))
        cell_map = {cell: add(cell, shift) for cell in graph.cells}
        direction = {mode: mode for mode in range(7)}
        vertex_map = [
            target.vertex_index[(cell_map[cell], mode)] for cell, mode in graph.vertices
        ]
        edge_map = [
            target.edge_between(vertex_map[u], vertex_map[v])
            for u, v, _kind, _owner in graph.edges
        ]
        for rotation in rotations:
            observed = base.permute_pauli(rotation.row, edge_map)
            expected = semantic_row(target, map_meta(rotation.meta, cell_map, direction))
            failures += observed != expected
        source_map = address_placement(graph, context.site_map)
        target_map = address_placement(target, carrier_placement(target))
        for address, sites in source_map.items():
            mapped_address = (
                address[0],
                frozenset((cell_map[cell], mode) for cell, mode in address[1]),
            )
            expected_sites = tuple(add(site, scale(16, shift)) for site in sites)
            placement_failures += target_map[mapped_address] != expected_sites
    return {
        "coarse_translation_cases": len(cases),
        "native_update_translation_failures": failures,
        "carrier_translation_failures": placement_failures,
        "arbitrary_physical_origin_translation": "add the supplied integer origin to every routed coordinate",
    }


def shared_star_certificate(union_graph, union_context, union_rotations) -> dict[str, object]:
    stars = []
    for center in PRIMARY_CENTERS:
        graph = prep.OpenReferenceGraph(star_cells(center))
        context = physical_context(graph)
        stars.append((graph, context))
    union_map = address_placement(union_graph, union_context.site_map)
    left_map = address_placement(stars[0][0], stars[0][1].site_map)
    right_map = address_placement(stars[1][0], stars[1][1].site_map)
    shared = set(left_map) & set(right_map)
    all_sub = list(left_map.items()) + list(right_map.items())
    rotation_by_factor = {}
    for rotation in union_rotations:
        rotation_by_factor.setdefault(rotation.factor, []).append(rotation)
    central_seam_factors = [
        factor
        for factor in rotation_by_factor
        if factor and factor[0] == "seam"
        and set((factor[2], factor[4])) == set(PRIMARY_CENTERS)
    ]
    return {
        "maximal_stars": 2,
        "cells_per_star": [len(star[0].cells) for star in stars],
        "star_union_cells": len(union_graph.cells),
        "star_cell_intersection": len(set(stars[0][0].cells) & set(stars[1][0].cells)),
        "shared_edge_addresses": len(shared),
        "shared_address_coordinate_failures": sum(left_map[key] != right_map[key] for key in shared),
        "subview_to_union_coordinate_failures": sum(union_map[key] != value for key, value in all_sub),
        "union_carrier_M2": len(union_context.sites),
        "two_subview_carriers_subset_global": (
            set(stars[0][1].sites) | set(stars[1][1].sites)
        ) <= set(union_context.sites),
        "induced_global_only_carriers": len(
            set(union_context.sites)
            - (set(stars[0][1].sites) | set(stars[1][1].sites))
        ),
        "central_shared_seam_factor_count": len(central_seam_factors),
        "central_shared_seam_rotation_count": sum(
            len(rotation_by_factor[factor]) for factor in central_seam_factors
        ),
        "common_global_constraint_bank": len(physical_stabilizers(union_context)),
        "view_rule": "both stars are views of one global graph/register bank; cropped boundary A/B rebuilds are not substituted",
    }


def seam_controls(graph, context) -> dict[str, object]:
    certificates = []
    physical_certificates = []
    bare_D_counts = []
    for cell, axis, target, left_mode, right_mode in graph_seams(graph):
        u = graph.vertex_index[(cell, left_mode)]
        v = graph.vertex_index[(target, right_mode)]
        rows = (
            graph.B(u),
            graph.B(v),
            *seam_hop_rows(graph, cell, left_mode, target, right_mode),
        )
        certificates.append(fswap_certificate(rows))
        physical_certificates.append(
            fswap_certificate(tuple(physical_lift(row, context) for row in rows))
        )
        bare = graph.A(u, v)
        bare_D_counts.append(
            sum(not bare.commutes(local_d(graph, endpoint)) for endpoint in graph.cells)
        )
    direct_certificates = []
    reference_cell = graph.cells[0]
    for left, right in ((0, 2), (1, 2), (2, 4)):
        rows = (
            semantic_row(graph, ("B", reference_cell, left)),
            semantic_row(graph, ("B", reference_cell, right)),
            *direct_hop_rows(graph, reference_cell, left, right),
        )
        direct_certificates.append(fswap_certificate(rows))
    return {
        "seams": len(certificates),
        "maximum_full_space_involution_residual": max(
            row["full_space_involution_residual"] for row in certificates
        ),
        "maximum_four_rotation_residual": max(
            row["four_rotation_residual_up_to_global_phase"] for row in certificates
        ),
        "hermitian_term_failures": sum(row["hermitian_term_failures"] for row in certificates),
        "minimum_term_deletion_involution_residual": min(
            value
            for row in certificates
            for value in row["term_deletion_involution_residuals"]
        ),
        "minimum_rotation_deletion_residual": min(
            value
            for row in certificates
            for value in row["rotation_deletion_residuals"]
        ),
        "physical_lift_maximum_full_space_involution_residual": max(
            row["full_space_involution_residual"] for row in physical_certificates
        ),
        "physical_lift_maximum_four_rotation_residual": max(
            row["four_rotation_residual_up_to_global_phase"]
            for row in physical_certificates
        ),
        "bare_matter_edge_D_anticommutator_census": dict(Counter(bare_D_counts)),
        "direct_onsite_FSWAP_max_involution_residual": max(
            row["full_space_involution_residual"] for row in direct_certificates
        ),
        "direct_onsite_FSWAP_max_factorization_residual": max(
            row["four_rotation_residual_up_to_global_phase"] for row in direct_certificates
        ),
    }


def factor_digest(rotations) -> str:
    payload = "\n".join(
        f"{rotation.serial}:{rotation.kind}:{rotation.factor}:{rotation.meta}:"
        f"{rotation.row.phase}:{rotation.row.x:x}:{rotation.row.z:x}:{rotation.angle:.17g}"
        for rotation in rotations
    )
    return sha256(payload.encode()).hexdigest()


def fixture(name: str, cells: tuple[Coord, ...], coin_gates, do_products: bool):
    graph = prep.OpenReferenceGraph(cells)
    context = physical_context(graph)
    rotations, inventory = build_update(graph, coin_gates)
    constraints = constraint_certificate(graph, context, rotations)
    route = route_update(context, rotations)
    result = {
        "name": name,
        "cells": len(graph.cells),
        "coarse_edges": len(graph.cross_edge) // 2,
        "placement_collisions": sum(len(sites) for sites in context.site_map.values()) - len(context.sites),
        "abstract_edge_formula": 18 * len(graph.cells) + 2 * (len(graph.cross_edge) // 2),
        "physical_carrier_formula": 18 * len(graph.cells) + 3 * (len(graph.cross_edge) // 2),
        "update_rotation_count": len(rotations),
        "update_kind_census": dict(Counter(rotation.kind for rotation in rotations)),
        "factor_sha256": factor_digest(rotations),
        "inventory": inventory,
        "constraints": constraints,
        "native_coin_algebra": gaussian_pair_algebra_certificate(
            graph,
            graph.cells[0],
            tuple(gate.modes for gate in coin_gates if gate.kind == "u2"),
        ),
        "native_reverse_braid": reverse_braid_certificate(graph, graph.cells[0]),
        "seams": seam_controls(graph, context),
        "route": route,
        "translations": translation_certificate(graph, context, rotations),
        "covariance": covariance_certificate(graph, context, rotations, do_products),
    }
    return result, graph, context, rotations


def root_placement_boundary_audit() -> dict[str, object]:
    noncube = prep.OpenReferenceGraph(box_cells(HELD_SHAPE))
    site_map = carrier_placement(noncube)
    noncube_controller = root_place.controller_interactions(
        HELD_SHAPE, noncube, site_map
    )
    return {
        "source": str(ROOT_PLACEMENT_SOURCE.relative_to(ROOT)),
        "source_sha256": file_sha256(ROOT_PLACEMENT_SOURCE),
        "site_rule_consumption": "direct import by the pinned source path",
        "noncubic_held_shape": HELD_SHAPE,
        "noncubic_controller_interactions": len(noncube_controller),
        "guard_confirmed": len(noncube_controller) == 0,
        "interpretation": (
            "the root artifact closes carrier placement and declared cubic structural routes; "
            "it does not supply a noncubic preparation controller, and this update probe does not consume one"
        ),
    }


def collect_failures(report) -> list[str]:
    failures = []
    if report["coin"]["QR_off_diagonal_residual"] > TOL:
        failures.append("coin QR")
    if report["coin"]["reconstruction_residual"] > TOL:
        failures.append("coin reconstruction")
    if report["coin"]["maximum_coin_covariance_residual"] > TOL:
        failures.append("coin covariance")
    if report["coin"]["reverse_helper_permutation_residual"] > TOL:
        failures.append("reverse")
    if report["contact"]["maximum_residual_up_to_global_phase"] > TOL:
        failures.append("contact")
    for fixture_row in report["fixtures"]:
        prefix = fixture_row["name"]
        if fixture_row["inventory"]["phase_breakdown_sum_residual"] > TOL:
            failures.append(f"{prefix}:global phase ledger")
        constraints = fixture_row["constraints"]
        coin_algebra = fixture_row["native_coin_algebra"]
        reverse_braid = fixture_row["native_reverse_braid"]
        seams = fixture_row["seams"]
        route = fixture_row["route"]
        covariance = fixture_row["covariance"]
        translations = fixture_row["translations"]
        exact_zero_fields = {
            "placement_collisions": fixture_row["placement_collisions"],
            "abstract_rank": constraints["abstract_constraint_rank"] - constraints["expected_abstract_rank"],
            "physical_rank": constraints["physical_constraint_rank"] - constraints["expected_physical_rank"],
            "abstract_phase": constraints["abstract_phase_dependency_failures"],
            "physical_phase": constraints["physical_phase_dependency_failures"],
            "abstract_comm": constraints["abstract_constraint_commutator_failures"],
            "physical_comm": constraints["physical_constraint_commutator_failures"],
            "abstract_update": constraints["abstract_update_preservation_failures"],
            "physical_update": constraints["physical_update_preservation_failures"],
            "lift_homomorphism": constraints["signed_repetition_lift_homomorphism_failures"],
            "hermitian": constraints["update_hermiticity_failures"],
            "coin_algebra_hermitian": coin_algebra["Hermiticity_failures"],
            "coin_algebra_commuting": coin_algebra["commuting_hop_summand_failures"],
            "coin_algebra_squares": coin_algebra["odd_sector_axis_square_failures"],
            "coin_algebra_XZ": coin_algebra["XZ_anticommutator_failures"],
            "coin_algebra_projector": coin_algebra["odd_projector_action_failures"],
            "seam_hermitian": seams["hermitian_term_failures"],
            "route_nn": route["non_NN_failures"],
            "route_operand": route["operand_order_failures"],
            "route_return": route["route_return_failures"],
            "rotated_steps": route["proper_cubic_rotated_unit_step_failures"],
            "translation_update": translations["native_update_translation_failures"],
            "translation_place": translations["carrier_translation_failures"],
            "cov_graph": covariance["graph_generator_transport_failures"],
            "cov_update": covariance["all_update_rotation_transport_failures"],
            "cov_angles": covariance["rotation_parameter_transport_failures"],
            "cov_place": covariance["carrier_set_transport_failures"],
            "cov_meta_products": covariance["update_metadata_product_failures"],
            "cov_signed_products": covariance["signed_AB_generator_product_failures"],
            "cov_coordinate_products": covariance["physical_coordinate_product_failures"],
        }
        for key, value in exact_zero_fields.items():
            if value != 0:
                failures.append(f"{prefix}:{key}={value}")
        if seams["maximum_full_space_involution_residual"] > TOL:
            failures.append(f"{prefix}:seam involution")
        if seams["maximum_four_rotation_residual"] > TOL:
            failures.append(f"{prefix}:seam factorization")
        if seams["physical_lift_maximum_full_space_involution_residual"] > TOL:
            failures.append(f"{prefix}:physical seam involution")
        if seams["physical_lift_maximum_four_rotation_residual"] > TOL:
            failures.append(f"{prefix}:physical seam factorization")
        if coin_algebra["maximum_native_su2_residual"] > TOL:
            failures.append(f"{prefix}:native coin algebra")
        if reverse_braid["maximum_full_space_braid_involution_residual"] > TOL:
            failures.append(f"{prefix}:reverse braid involution")
        if reverse_braid["maximum_occupation_conjugation_residual"] > TOL:
            failures.append(f"{prefix}:reverse braid conjugation")
        if reverse_braid["minimum_helper_FSWAP_deletion_residual"] < 1.0e-3:
            failures.append(f"{prefix}:inactive reverse helper deletion")
        if seams["minimum_term_deletion_involution_residual"] < 1.0e-3:
            failures.append(f"{prefix}:inactive seam term deletion")
        if seams["minimum_rotation_deletion_residual"] < 1.0e-3:
            failures.append(f"{prefix}:inactive seam rotation deletion")
        if seams["bare_matter_edge_D_anticommutator_census"] != {2: fixture_row["coarse_edges"]}:
            failures.append(f"{prefix}:reference deletion")
        if not constraints["all_D_product_identity"]:
            failures.append(f"{prefix}:global D dependency identity")
        if fixture_row["abstract_edge_formula"] != constraints["abstract_edge_qubits"]:
            failures.append(f"{prefix}:abstract formula")
        if fixture_row["physical_carrier_formula"] != constraints["physical_carrier_M2"]:
            failures.append(f"{prefix}:physical formula")
    shared = report["shared_stars"]
    for key in (
        "shared_address_coordinate_failures",
        "subview_to_union_coordinate_failures",
    ):
        if shared[key] != 0:
            failures.append(f"shared:{key}")
    if not shared["two_subview_carriers_subset_global"]:
        failures.append("shared:carrier subset")
    if shared["central_shared_seam_factor_count"] != 1:
        failures.append("shared:central seam")
    return failures


def main() -> int:
    dependency_hashes = {
        name: file_sha256(ROUTE_SCRIPTS / name)
        for name in EXPECTED_DEPENDENCY_SHA256
    }
    dependency_pin_failures = {
        name: {"expected": expected, "observed": dependency_hashes[name]}
        for name, expected in EXPECTED_DEPENDENCY_SHA256.items()
        if dependency_hashes[name] != expected
    }
    species = c219.common_species(float(c230.BETA))
    coin = np.asarray(species.coin, dtype=complex)
    coin_gates, qr = qr_coin_schedule(coin)
    coin_report = dict(qr)
    coin_report.update(one_particle_semantics(coin, coin_gates))
    primary, primary_graph, primary_context, primary_rotations = fixture(
        "two_overlapping_maximal_stars",
        two_star_union(),
        coin_gates,
        False,
    )
    held, _held_graph, _held_context, _held_rotations = fixture(
        "held_3x2x2_open_box",
        box_cells(HELD_SHAPE),
        coin_gates,
        True,
    )
    report = {
        "status": "pending",
        "claim_scope": (
            "native OpenReferenceGraph finite update closure and literal returned NN routing; "
            "no global-JW target character and no autonomous preparation/genesis claim"
        ),
        "coin": coin_report,
        "contact": contact_semantics(),
        "fixtures": [primary, held],
        "shared_stars": shared_star_certificate(
            primary_graph, primary_context, primary_rotations
        ),
        "root_placement_boundary_audit": root_placement_boundary_audit(),
        "dependency_sha256": dependency_hashes,
        "dependency_pin_failures": dependency_pin_failures,
        "source_pins": {
            "this_source_sha256": file_sha256(Path(__file__)),
            "Cycle703_OpenReferenceGraph_sha256": file_sha256(
                ROUTE_SCRIPTS / "frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py"
            ),
            "Cycle706_covariance_sha256": file_sha256(
                ROUTE_SCRIPTS / "frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py"
            ),
            "Cycle707_placement_routing_sha256": file_sha256(
                ROUTE_SCRIPTS / "frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py"
            ),
            "Cycle219_coin_sha256": file_sha256(
                ROUTE_SCRIPTS / "common_matter_field_coin_family_cycle219_2026_07_16.py"
            ),
            "Cycle230_contact_sha256": file_sha256(
                ROUTE_SCRIPTS / "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
            ),
        },
        "boundary": {
            "supplied": [
                "finite connected open cell set and its boundary",
                "integer origin, proper-cubic coframe, BKSF incident-edge order gauge, and serial layer order",
                "Cycle219 beta=-0.3 coin and Cycle230 g=0.37 contact",
                "the +1 OpenReference loop/local-D character when an encoded state is required",
            ],
            "derived": [
                "18N+3E collision-free physical carrier placement with the reference bond at each seam midpoint",
                "one common physical stabilizer/repetition bank of rank q-6N for every update factor",
                "exact onsite coin/mass, onsite reverse FSWAP, every dressed seam FSWAP, and onsite contact word",
                "full-space seam Hermiticity/involution and exact four-rotation synthesis with active deletions",
                "returned nearest-neighbour serial routing, translations, 24 frames, and 576 products",
            ],
            "open": [
                "autonomous genesis or preparation of the supplied +1 stabilizer character",
                "a noncubic or arbitrary-cell physical echo/controller composition",
                "intrinsic coframe/boundary/layer-order selection, periodic Wilson sectors, and fault repair",
                "collision-free constant-depth parallel routing or a recurrent all-volume controller",
            ],
            "not_claimed": [
                "no OpenReference-to-PatchGraph conversion is used as update semantics",
                "no global Jordan--Wigner target characters are used",
                "no broad obstruction, minimum resource theorem, autonomous preparation, or periodic result",
            ],
        },
    }
    failures = [f"dependency pin:{name}" for name in dependency_pin_failures]
    failures.extend(collect_failures(report))
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    payload = json.dumps(report, sort_keys=True, indent=2, default=str)
    report["content_sha256_before_hash_field"] = sha256(payload.encode()).hexdigest()
    output = ROOT / "outputs" / "cycle870_openreference_native_recurrent_update_receipt_2026_08_02.json"
    output.write_text(json.dumps(report, sort_keys=True, indent=2, default=str) + "\n")
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("RECEIPT", output)
    print(
        "OPENREFERENCE_NATIVE_UPDATE_PASS"
        if not failures
        else "OPENREFERENCE_NATIVE_UPDATE_FAIL"
    )
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
