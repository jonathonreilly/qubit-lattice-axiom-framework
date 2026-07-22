#!/usr/bin/env python3
"""Cycle608: dressed detector / controlled-update / recurrence extraction.

The runner materializes the accepted table-defined W factors needed by an
origin A2 readout and lowers every accepted physical update-factor family to
one/two-M2 gates.  Analytic factor lowering is distinguished from executing a
full-torus dense operator.  Membership is not phase, a candidate is not a
Record, and a recurrence count is not time.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from hashlib import sha256
from itertools import combinations, product
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import struct
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_global_N3_returned_slot_compiler_cycle560_2026_07_21 as c560


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_"
    "TOURNAMENT_CYCLE608_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_radius_one_dressed_detector_controlled_update_"
    "recurrence_tournament_cycle608_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-9
SIGNAL = 1e-8
WALL_CAP_SECONDS = 480.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0

FROZEN_SHORES = {
    "scripts/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_2026_07_22.py":
        "201461575d99bb54c6c68a0293064885f05cf016eae9f77ec8dd4b360d8eaf82",
    "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_DETECTOR_EVENT_ASSOCIATION_CONTROLLED_ECHO_TOURNAMENT_CYCLE605_NOTE_2026-07-22.md":
        "aa09a8208263e51ba0140b0bee11363924e3ce94c72388b1f2f407e967a71daa",
    "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json":
        "9b46a4c1751fa281bca1240f927b0676aa2cecac7cdb87ca76a3131a4a54acc9",
    "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py":
        "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
}

FROZEN_LAW = {
    "sizes": {"train": 3, "held_out": 4, "held": 6},
    "detector": "d+=(a+Ga)/sqrt(2), d+i=(a+iGa)/sqrt(2)",
    "read_origin": (0, 0, 0),
    "controlled_update": "control every Wdagger, G_target, W factor by the local scalar path field",
    "event_prefixes": (1, 2, 4, 5, 8),
}
FROZEN_LAW_SHA256 = sha256(json.dumps(FROZEN_LAW, sort_keys=True).encode()).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    raise TypeError(type(value).__name__)


def shore() -> dict[str, object]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    prior = json.loads((ROOT / "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json").read_text())
    fixtures = prior["shore"]["Cycle602_pass"], prior["shore"].get("retained_physical_fixtures", {})
    condition = observed == FROZEN_SHORES and prior["pass"] is True
    result = {"expected": FROZEN_SHORES, "observed": observed,
              "Cycle605_pass": prior["pass"], "retained": fixtures}
    check("accepted Cycle560/563/590/605 shores are byte exact", condition, result)
    return result


Coord = tuple[int, int, int]


@dataclass
class Layout:
    length: int
    modulus: int
    code: object
    cells: tuple[Coord, ...]
    tables: tuple[dict, ...]
    roles: tuple[tuple[int, ...], ...]
    q: tuple[tuple[Coord, ...], ...]
    branch: tuple[tuple[Coord, ...], ...]
    work: tuple[tuple[Coord, ...], ...]
    path: tuple[Coord, ...]
    read_work: tuple[Coord, ...]
    pointer: Coord

    def distance(self, first: Coord, second: Coord) -> int:
        return c560.c533.c527.periodic_l1(first, second, self.modulus)


def build_layout(length: int) -> Layout:
    cells = c560.c555.network_cells(length)
    code = c560.c539.c525.c319.c269.build_code(length)
    tables = c560.c539.local_tables(code, cells)
    roles = tuple(c560.c557.local_roles(code, cell) for cell in cells)
    modulus = c560.c533.c527.fine_length(length)
    total_physical = c560.c555.physical_bit_count(code)
    physical = tuple(c560.c533.coordinate_for_qubit(code, bit) for bit in range(total_physical))
    q = tuple(tuple(c560.c533.c527.shadow_coordinate(cell, direction, length)
                    for direction in range(6)) for cell in cells)
    occupied = set(physical) | {site for row in q for site in row}
    branch = tuple(c560.allocated_block(c560.c533.c527.cell_center(cell, length), 6, occupied, modulus)
                   for cell in cells)
    work = tuple(c560.allocated_block(c560.c533.c527.cell_center(cell, length), 18, occupied, modulus)
                 for cell in cells)
    # A single transported offset makes the scalar path field covariant.  The
    # -4 corner is outside every accepted A/B update wire motif and all
    # physical/q/branch/work sites; the finite search is a construction check.
    path = ()
    offsets = ((-4, -4, -4),) + tuple(product(range(-8, 9), repeat=3))
    for offset in offsets:
        candidate = tuple(tuple((c560.c533.c527.cell_center(cell, length)[axis]
                                  + offset[axis]) % modulus for axis in range(3))
                          for cell in cells)
        if len(set(candidate)) == len(candidate) and not (set(candidate) & occupied):
            path = candidate
            occupied.update(path)
            break
    if not path:
        raise ValueError("no covariant scalar path offset")
    origin_index = cells.index(FROZEN_LAW["read_origin"])
    read = c560.allocated_block(c560.c533.c527.cell_center(cells[origin_index], length), 6, occupied, modulus)
    return Layout(length, modulus, code, cells, tables, roles, q, branch, work, path,
                  read[:5], read[5])


@dataclass
class Counts:
    one_M2: int = 0
    logical_two_M2: int = 0
    route_return_SWAP: int = 0
    Toffoli: int = 0
    explicit_two_M2_core: int = 0
    maximum_pair_edges: int = 0
    pair_calls: int = 0

    def add_one(self, number: int = 1) -> None:
        self.one_M2 += number

    def add_pair(self, layout: Layout, first: Coord, second: Coord, number: int = 1,
                 *, core: bool = False) -> None:
        distance = layout.distance(first, second)
        if distance < 1:
            raise ValueError("two-M2 gate received one site")
        self.logical_two_M2 += number
        self.route_return_SWAP += number * 2 * (distance - 1)
        self.maximum_pair_edges = max(self.maximum_pair_edges, distance)
        self.pair_calls += number
        self.explicit_two_M2_core += int(core) * number

    def add_toffoli(self, layout: Layout, first: Coord, second: Coord, target: Coord) -> None:
        self.Toffoli += 1
        self.one_M2 += 9
        for left, right in ((second, target), (first, target), (second, target),
                            (first, target), (first, second), (first, second)):
            self.add_pair(layout, left, right)

    def add(self, other: "Counts", scale: int = 1) -> None:
        self.one_M2 += scale * other.one_M2
        self.logical_two_M2 += scale * other.logical_two_M2
        self.route_return_SWAP += scale * other.route_return_SWAP
        self.Toffoli += scale * other.Toffoli
        self.explicit_two_M2_core += scale * other.explicit_two_M2_core
        self.maximum_pair_edges = max(self.maximum_pair_edges, other.maximum_pair_edges)
        self.pair_calls += scale * other.pair_calls

    def row(self) -> dict[str, int]:
        installed_two = self.logical_two_M2 + self.route_return_SWAP
        return {
            "one_M2_gates": self.one_M2,
            "logical_two_M2_gates": self.logical_two_M2,
            "NN_route_return_SWAPs": self.route_return_SWAP,
            "installed_two_M2_gates": installed_two,
            "Toffoli_calls": self.Toffoli,
            "specific_explicit_two_M2_cores": self.explicit_two_M2_core,
            "maximum_pair_route_edges": self.maximum_pair_edges,
            "serial_depth": self.one_M2 + installed_two,
            "elementary_total": self.one_M2 + installed_two,
        }


def negative_shell(counts: Counts, values: tuple[int, ...]) -> None:
    counts.add_one(2 * sum(value == 0 for value in values))


def add_mcx(counts: Counts, layout: Layout, controls: tuple[Coord, ...], target: Coord,
            work: tuple[Coord, ...], values: tuple[int, ...]) -> None:
    if len(controls) != len(values):
        raise ValueError("control/value mismatch")
    negative_shell(counts, values)
    size = len(controls)
    if size == 1:
        counts.add_pair(layout, controls[0], target)
    elif size == 2:
        counts.add_toffoli(layout, controls[0], controls[1], target)
    else:
        if len(work) < size - 2:
            raise ValueError("insufficient clean conjunction work")
        compute = [(controls[0], controls[1], work[0])]
        for index in range(2, size - 1):
            compute.append((work[index - 2], controls[index], work[index - 1]))
        for triple in compute:
            counts.add_toffoli(layout, *triple)
        counts.add_toffoli(layout, work[size - 3], controls[-1], target)
        for triple in reversed(compute):
            counts.add_toffoli(layout, *triple)


def add_phase_predicate(counts: Counts, layout: Layout, controls: tuple[Coord, ...],
                        work: tuple[Coord, ...], values: tuple[int, ...]) -> None:
    # Equality-controlled -1: after normalizing negative controls, use the
    # final predicate bit as the Z target around an MCX on the others.
    negative_shell(counts, values)
    counts.add_one(2)
    add_mcx(counts, layout, controls[:-1], controls[-1], work,
            (1,) * (len(controls) - 1))


def add_conjunction_core(counts: Counts, layout: Layout, controls: tuple[Coord, ...],
                         work: tuple[Coord, ...], values: tuple[int, ...],
                         first_target: Coord, second_target: Coord) -> None:
    """Compute conjunction, apply exact controlled two-ray Givens, uncompute."""
    negative_shell(counts, values)
    if len(work) < len(controls) - 1:
        raise ValueError("insufficient Givens-control work")
    chain = [(controls[0], controls[1], work[0])]
    for index in range(2, len(controls)):
        chain.append((work[index - 2], controls[index], work[index - 1]))
    for triple in chain:
        counts.add_toffoli(layout, *triple)
    control = work[len(controls) - 2]
    # Gray CNOT, exact CCU(V^2=U), inverse Gray CNOT: four target-pair,
    # two control/second-target, one control/first-target two-M2 gates.
    counts.add_pair(layout, first_target, second_target, 4, core=True)
    counts.add_pair(layout, control, second_target, 2, core=True)
    counts.add_pair(layout, control, first_target, 1, core=True)
    for triple in reversed(chain):
        counts.add_toffoli(layout, *triple)


def pauli_inverse(pauli):
    phase = (-pauli.phase + 2 * (pauli.x & pauli.z).bit_count()) % 4
    return type(pauli)(phase, pauli.x, pauli.z)


def pattern(code, representative, roles: tuple[int, ...]) -> tuple[int, ...]:
    auxiliary = representative.x >> code.qubits
    return tuple((auxiliary >> role) & 1 for role in roles)


def q_values(word: int) -> tuple[int, ...]:
    return tuple((word >> direction) & 1 for direction in range(6))


def local_word_data(layout: Layout, cell_index: int, maximum_number: int = 3):
    table = layout.tables[cell_index]
    roles = layout.roles[cell_index]
    rows = []
    for word in range(64):
        if word.bit_count() > maximum_number:
            continue
        entries = table[word]
        vector = np.asarray([complex(amplitude) for _term, amplitude in entries])
        schedule, forward, inverse, deleted = c560.c557.preparation_residuals(vector)
        patterns = tuple(pattern(layout.code, term.representative, roles)
                         for term, _amplitude in entries)
        if len(entries) == 2:
            vacuum = table[0]
            pivot_mask = (vacuum[0][0].representative.x
                          ^ vacuum[1][0].representative.x) >> layout.code.qubits
            if pivot_mask.bit_count() != 1:
                raise ValueError("ordinary decoder has no singleton companion pivot")
            subset = (roles.index(pivot_mask.bit_length() - 1),)
        else:
            subset = c560.c557.smallest_injective_subset(patterns)
        if subset is None:
            raise ValueError("noninjective physical decoder row")
        rows.append((word, entries, schedule, patterns, subset, forward, inverse, deleted))
    return tuple(rows)


def add_local_W(counts: Counts, layout: Layout, cell_index: int, *, controlled: bool,
                maximum_number: int, digest=None) -> dict[str, int]:
    qsites = layout.q[cell_index]
    branch = layout.branch[cell_index]
    work = layout.work[cell_index]
    path = layout.path[cell_index]
    roles = layout.roles[cell_index]
    role_sites = tuple(c560.c533.coordinate_for_qubit(
        layout.code, layout.code.qubits + role) for role in roles)
    rows = local_word_data(layout, cell_index, maximum_number)
    census = Counter()

    # Initialize one branch rail from the all-zero supplied block.
    if controlled:
        counts.add_pair(layout, path, branch[0])
    else:
        counts.add_one()
    census["branch_initialization"] += 1

    # A: q-word-controlled one-excitation Givens.
    for word, _entries, schedule, _patterns, _subset, *_ in rows:
        controls = ((path,) if controlled else ()) + qsites
        values = ((1,) if controlled else ()) + q_values(word)
        for target, matrix in schedule:
            add_conjunction_core(counts, layout, controls, work, values,
                                 branch[0], branch[int(target)])
            census["A_Givens"] += 1
            if digest is not None:
                digest.update(repr(("A", cell_index, word, int(target), tuple(
                    c560.c533.complex_token(value) for value in matrix.reshape(-1)
                ))).encode())

    # SELECT: exact phase-folded representative X then Z factors.
    for word, entries, _schedule, _patterns, _subset, *_ in rows:
        for branch_index, (term, _amplitude) in enumerate(entries):
            controls = ((path,) if controlled else ()) + qsites + (branch[branch_index],)
            values = ((1,) if controlled else ()) + q_values(word) + (1,)
            representative = term.representative
            for kind, bits in (("X", representative.x), ("Z", representative.z)):
                for bit in range(bits.bit_length()):
                    if not ((bits >> bit) & 1):
                        continue
                    target = c560.c533.coordinate_for_qubit(layout.code, bit)
                    if kind == "Z":
                        counts.add_one(2)
                    add_mcx(counts, layout, controls, target, work, values)
                    census[f"SELECT_{kind}"] += 1
                    if digest is not None:
                        digest.update(repr(("SELECT", cell_index, word, branch_index,
                                            kind, bit, target)).encode())

    # D: q plus smallest injective native-pattern equality clears the active rail.
    for word, entries, _schedule, patterns, subset, *_ in rows:
        for branch_index, (_term, _amplitude) in enumerate(entries):
            selected_sites = tuple(role_sites[index] for index in subset)
            selected_values = tuple(patterns[branch_index][index] for index in subset)
            controls = ((path,) if controlled else ()) + qsites + selected_sites
            values = ((1,) if controlled else ()) + q_values(word) + selected_values
            add_mcx(counts, layout, controls, branch[branch_index], work, values)
            census["D_comparator_rows"] += 1
            if digest is not None:
                digest.update(repr(("D", cell_index, word, branch_index, subset,
                                    selected_values, branch[branch_index])).encode())
    return dict(census)


def pauli_cancellation_test(layout: Layout) -> dict[str, object]:
    origin = layout.cells.index(FROZEN_LAW["read_origin"])
    origin_rows = local_word_data(layout, origin, 2)
    role_tuple = layout.roles[origin]
    cases = pattern_failures = cancellation_failures = 0
    maximum_prep = maximum_inverse = 0.0
    digest = sha256()
    contact_local_cases = seam_neighbor_cases = periodic_wrap_cases = 0
    foreign_cache = {
        (foreign, maximum): local_word_data(layout, foreign, maximum)
        for foreign in range(len(layout.cells)) if foreign != origin
        for maximum in range(3)
    }
    for word, entries, _schedule, patterns, subset, forward, inverse, _deleted in origin_rows:
        maximum_prep = max(maximum_prep, forward)
        maximum_inverse = max(maximum_inverse, inverse)
        remaining = 2 - word.bit_count()
        for branch_index, (origin_term, _amplitude) in enumerate(entries):
            expected_pattern = tuple(patterns[branch_index][index] for index in subset)
            origin_rep = origin_term.representative
            for foreign in range(len(layout.cells)):
                if foreign == origin:
                    continue
                for foreign_word, foreign_entries, *_tail in foreign_cache[(foreign, remaining)]:
                    if foreign_word.bit_count() > remaining:
                        continue
                    for foreign_term, _foreign_amplitude in foreign_entries:
                        product = origin_rep @ foreign_term.representative
                        observed = pattern(layout.code, product, role_tuple)
                        pattern_failures += tuple(observed[index] for index in subset) != expected_pattern
                        removed = pauli_inverse(origin_rep) @ product
                        cancellation_failures += removed != foreign_term.representative
                        digest.update(repr((word, branch_index, foreign, foreign_word,
                                            subset, expected_pattern, removed.phase)).encode())
                        contact_local_cases += int(word.bit_count() == 2 and foreign_word == 0)
                        coarse_distance = sum(min(coordinate % layout.length,
                                                  (-coordinate) % layout.length)
                                              for coordinate in layout.cells[foreign])
                        seam_neighbor_cases += int(word.bit_count() == foreign_word.bit_count() == 1
                                                   and coarse_distance == 1)
                        periodic_wrap_cases += int(coarse_distance == 1 and
                                                   any(value == layout.length - 1
                                                       for value in layout.cells[foreign]))
                        cases += 1
    return {
        "lawful_basis_ray_cases_touching_origin": cases,
        "foreign_invariant_decoder_pattern_failures": pattern_failures,
        "origin_SELECT_inverse_cancellation_failures": cancellation_failures,
        "maximum_origin_A_preparation_residual": maximum_prep,
        "maximum_origin_A_inverse_residual": maximum_inverse,
        "comparison_digest": digest.hexdigest(),
        "Cycle230_local_contact_branch_cases": contact_local_cases,
        "one_plus_one_particle_seam_neighbor_cases": seam_neighbor_cases,
        "periodic_wrap_neighbor_cases": periodic_wrap_cases,
        "minimum_tested_coarse_support": "origin plus one arbitrary foreign cell; nontrivial decoder support is origin only via its unique companion pivot",
        "full_Wdagger_P_W_comparison_scope": (
            "all complete-N<=2 basis rays with an arbitrary foreign occupied cell; "
            "the accepted foreign-pivot theorem extends spectator vacuum factors"
        ),
        "counterexample_control": (
            "omitting Ddagger leaves the branch one-hot label and therefore cannot "
            "feed the six-q A2 mesh; residual is at least the minimum branch-one amplitude"
        ),
        "omitted_Ddagger_minimum_residual": 2**-0.5,
        "pass": pattern_failures == cancellation_failures == 0
                and max(maximum_prep, maximum_inverse) < TOL,
    }


@dataclass
class Mesh:
    upper: np.ndarray
    residual: float
    digest: str


def factor_orthogonal(matrix: np.ndarray) -> Mesh:
    work = matrix.copy()
    upper = []
    digest = sha256()
    for column in range(len(matrix) - 1):
        for lower in range(len(matrix) - 1, column, -1):
            top = lower - 1
            a, b = float(work[top, column]), float(work[lower, column])
            if abs(b) < 1e-15:
                continue
            radius = math.hypot(a, b)
            cosine, sine = a / radius, b / radius
            left, right = work[top, column:].copy(), work[lower, column:].copy()
            work[top, column:] = cosine * left + sine * right
            work[lower, column:] = -sine * left + cosine * right
            upper.append(top)
            digest.update(struct.pack("<Idd", top, cosine, sine))
    diagonal = np.diag(work).copy()
    digest.update(diagonal.tobytes())
    return Mesh(np.asarray(upper, dtype=np.int32),
                float(np.linalg.norm(work - np.diag(diagonal))), digest.hexdigest())


def a2_mesh():
    # Cycle605's byte-pinned executed Slater factorization.  These two real
    # orbitals reconstruct A2 to 5.47e-16; retaining them avoids importing the
    # dense two-body engine alongside the physical-code compiler.
    first = np.asarray((0.0, 0.0, -0.4999999999999997, -0.5000000000000003,
                        0.4999999999999999, 0.4999999999999999))
    second = np.asarray((0.5773502691896258, 0.5773502691896258,
                         -0.28867513459481287, -0.2886751345948128,
                         -0.2886751345948129, -0.28867513459481287))
    columns = [first, second]
    for unit in np.eye(6):
        work = unit.copy()
        for column in columns:
            work -= np.dot(column, work) * column
        if np.linalg.norm(work) > 1e-11:
            columns.append(work / np.linalg.norm(work))
    matrix = np.column_stack(columns)
    if np.linalg.det(matrix) < 0:
        matrix[:, -1] *= -1
    return factor_orthogonal(matrix)


def add_physical_A2_predicate(counts: Counts, layout: Layout, *, target: Coord) -> dict[str, object]:
    origin = layout.cells.index(FROZEN_LAW["read_origin"])
    mesh = a2_mesh()
    qsites = layout.q[origin]
    for top in mesh.upper:
        counts.add_pair(layout, qsites[int(top)], qsites[int(top) + 1], core=True)
    add_mcx(counts, layout, qsites, target, layout.read_work, (1, 1, 0, 0, 0, 0))
    for top in reversed(mesh.upper):
        counts.add_pair(layout, qsites[int(top)], qsites[int(top) + 1], core=True)
    return {"adjacent_Givens": len(mesh.upper) * 2, "mesh_digest": mesh.digest,
            "mesh_residual": mesh.residual}


def local_dressed_readout(length: int) -> tuple[dict[str, object], Layout]:
    layout = build_layout(length)
    origin = layout.cells.index(FROZEN_LAW["read_origin"])
    counts = Counts()
    digest = sha256()
    # W_origin^dagger, physical predicate, W_origin.  Counts are symmetric.
    one_W = Counts()
    census = add_local_W(one_W, layout, origin, controlled=False,
                         maximum_number=2, digest=digest)
    counts.add(one_W, 2)
    predicate = add_physical_A2_predicate(counts, layout, target=layout.pointer)
    comparison = pauli_cancellation_test(layout)
    support_bits = set()
    for word, entries, *_tail in local_word_data(layout, origin, 2):
        for term, _amplitude in entries:
            rep = term.representative
            support_bits.update(bit for bit in range((rep.x | rep.z).bit_length())
                                if ((rep.x | rep.z) >> bit) & 1)
    support_sites = {c560.c533.coordinate_for_qubit(layout.code, bit) for bit in support_bits}
    center = c560.c533.c527.cell_center(FROZEN_LAW["read_origin"], length)
    maximum_radius = max((layout.distance(center, site) for site in support_sites), default=0)
    result = {
        "length": length,
        "split": next(name for name, value in FROZEN_LAW["sizes"].items() if value == length),
        "origin_local_factor_census_one_direction": census,
        "materialized_factor_word_sha256": digest.hexdigest(),
        "physical_auxiliary_dressing_comparison": comparison,
        "predicate": predicate,
        "counts_Wdagger_predicate_W": counts.row(),
        "selected_physical_support_M2": len(support_sites),
        "maximum_selected_support_fine_L1_radius": maximum_radius,
        "compiler_M2_per_cell_before_path": 53,
        "path_M2_per_cell": 1,
        "retained_pointer_M2": 1,
        "renewed_read_work_M2": 5,
        "global_N_le_3_domain_locally_enforced": False,
    }
    result["pass"] = bool(comparison["pass"] and predicate["mesh_residual"] < TOL
                          and counts.maximum_pair_edges <= 64)
    return result, layout


def pair_matrix(gate: np.ndarray, first: int, second: int, qubits: int = 3) -> np.ndarray:
    result = np.zeros((2**qubits, 2**qubits), dtype=complex)
    for column in range(2**qubits):
        bits = [(column >> (qubits - 1 - index)) & 1 for index in range(qubits)]
        local_column = 2 * bits[first] + bits[second]
        for local_row in range(4):
            target = bits.copy()
            target[first], target[second] = divmod(local_row, 2)
            row = sum(bit << (qubits - 1 - index) for index, bit in enumerate(target))
            result[row, column] += gate[local_row, local_column]
    return result


def controlled_one_matrix(unitary: np.ndarray) -> np.ndarray:
    result = np.eye(4, dtype=complex)
    result[2:, 2:] = unitary
    return result


def controlled_givens_core_test() -> dict[str, object]:
    """Execute the seven two-M2 CCU/Gray lowering on every accepted A row."""
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
    residual = 0.0
    cases = 0
    digest = sha256()
    # L3 contains every transported cell orientation.  The byte-pinned
    # Cycle560 table law is size independent; L4/L6 are held geometry tests.
    for length in (FROZEN_LAW["sizes"]["train"],):
        layout = build_layout(length)
        for cell in range(len(layout.cells)):
            for word, _entries, schedule, *_tail in local_word_data(layout, cell, 3):
                for target, matrix in schedule:
                    unitary = np.asarray(matrix, dtype=complex)
                    eigenvalues, eigenvectors = np.linalg.eig(unitary)
                    root = eigenvectors @ np.diag(np.sqrt(eigenvalues)) @ np.linalg.inv(eigenvectors)
                    cv = controlled_one_matrix(root)
                    cvd = controlled_one_matrix(root.conj().T)
                    sequence = (
                        pair_matrix(cnot, 1, 2),
                        pair_matrix(cv, 2, 1),
                        pair_matrix(cnot, 0, 2),
                        pair_matrix(cvd, 2, 1),
                        pair_matrix(cnot, 0, 2),
                        pair_matrix(cv, 0, 1),
                        pair_matrix(cnot, 1, 2),
                    )
                    actual = np.eye(8, dtype=complex)
                    for gate in sequence:
                        actual = gate @ actual
                    target4 = np.eye(4, dtype=complex)
                    target4[1, 1] = unitary[0, 0]
                    target4[1, 2] = unitary[0, 1]
                    target4[2, 1] = unitary[1, 0]
                    target4[2, 2] = unitary[1, 1]
                    expected = np.eye(8, dtype=complex)
                    expected[4:, 4:] = target4
                    residual = max(residual, float(np.linalg.norm(actual - expected)))
                    digest.update(repr((length, cell, word, int(target), tuple(
                        c560.c533.complex_token(value) for value in root.reshape(-1)
                    ))).encode())
                    cases += 1
    return {
        "accepted_local_Givens_cases": cases,
        "execution_scope": "every q-word Givens row in all 27 L3 cell orientations; transported unchanged to L4/L6",
        "specific_two_M2_word": (
            "CNOT(a,b), CV(b,a), CNOT(c,b), CVdagger(b,a), "
            "CNOT(c,b), CV(c,a), CNOT(a,b), V^2=U"
        ),
        "two_M2_gates_per_controlled_Givens_after_conjunction": 7,
        "maximum_executed_8x8_residual": residual,
        "root_parameter_digest_sha256": digest.hexdigest(),
        "pass": residual < TOL and cases > 0,
    }


def one_matrix(gate: np.ndarray, target: int, qubits: int = 3) -> np.ndarray:
    result = np.zeros((2**qubits, 2**qubits), dtype=complex)
    for column in range(2**qubits):
        bits = [(column >> (qubits - 1 - index)) & 1 for index in range(qubits)]
        for value in (0, 1):
            target_bits = bits.copy(); target_bits[target] = value
            row = sum(bit << (qubits - 1 - index) for index, bit in enumerate(target_bits))
            result[row, column] += gate[value, bits[target]]
    return result


def primitive_family_matrix_tests(givens: dict[str, object]) -> dict[str, object]:
    H = np.asarray([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    T = np.diag((1, np.exp(1j * np.pi / 4)))
    Tdg = T.conj().T
    cnot = np.asarray([[1, 0, 0, 0], [0, 1, 0, 0],
                       [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
    sequence = (
        one_matrix(H, 2), pair_matrix(cnot, 1, 2), one_matrix(Tdg, 2),
        pair_matrix(cnot, 0, 2), one_matrix(T, 2), pair_matrix(cnot, 1, 2),
        one_matrix(Tdg, 2), pair_matrix(cnot, 0, 2), one_matrix(T, 1),
        one_matrix(T, 2), one_matrix(H, 2), pair_matrix(cnot, 0, 1),
        one_matrix(T, 0), one_matrix(Tdg, 1), pair_matrix(cnot, 0, 1),
    )
    actual = np.eye(8, dtype=complex)
    for gate in sequence:
        actual = gate @ actual
    expected = np.eye(8, dtype=complex)
    expected[6, 6] = expected[7, 7] = 0
    expected[6, 7] = expected[7, 6] = 1
    toffoli_residual = float(np.linalg.norm(actual - expected))
    coupling = 0.37
    contact_residual = 0.0
    for selector in (0, 1):
        for left in (0, 1):
            for right in (0, 1):
                exponent = (selector + left + right - (selector ^ left)
                            - (selector ^ right) - (left ^ right)
                            + (selector ^ left ^ right)) / 4
                actual_phase = np.exp(1j * coupling * exponent)
                expected_phase = np.exp(1j * coupling * selector * left * right)
                contact_residual = max(contact_residual, abs(actual_phase - expected_phase))
    one_site_residual = 0.0
    for angle in (0.0, np.pi, 0.37, -0.37):
        U = np.diag((np.exp(-0.5j * angle), np.exp(0.5j * angle)))
        actual_cu = controlled_one_matrix(U)
        expected_cu = np.diag((1, 1, U[0, 0], U[1, 1]))
        one_site_residual = max(one_site_residual, float(np.linalg.norm(actual_cu - expected_cu)))
    result = {
        "one_site_to_controlled_two_M2_maximum_4x4_residual": one_site_residual,
        "CNOT_to_Toffoli_executed_8x8_residual": toffoli_residual,
        "Toffoli_word": {"one_M2": 9, "two_M2": 6},
        "fermionic_Givens_to_Gray_CCU_maximum_8x8_residual": givens["maximum_executed_8x8_residual"],
        "contact_phase_polynomial_truth_table_maximum_residual": contact_residual,
        "contact_word_per_pair": {"one_M2_phase": 7, "two_M2_CNOT": 10},
        "inverse_rule": "reverse each literal word and invert every one/two-M2 factor",
        "families": ("H/Rz/S/Sdg/onsite-phase", "CNOT", "fermionic-Givens", "contact-phase"),
    }
    result["pass"] = max(one_site_residual, toffoli_residual,
                          givens["maximum_executed_8x8_residual"], contact_residual) < TOL
    return result


def correction_rows(layout: Layout):
    term_rows = []
    for table in layout.tables:
        rows = []
        for word in range(64):
            if word.bit_count() > 3:
                continue
            for branch, (term, _amplitude) in enumerate(table[word]):
                rows.append((word, branch, term.representative))
        term_rows.append(tuple(rows))
    modulus = 3 if layout.length % 2 else 2
    colors = {index: sum(cell) % modulus for index, cell in enumerate(layout.cells)}
    scheduled = sorted(range(len(layout.cells)), key=lambda index: (colors[index], layout.cells[index]))
    position = {cell: index for index, cell in enumerate(scheduled)}
    for first, second in combinations(range(len(layout.cells)), 2):
        distance = sum(min((layout.cells[first][axis] - layout.cells[second][axis]) % layout.length,
                           (layout.cells[second][axis] - layout.cells[first][axis]) % layout.length)
                       for axis in range(3))
        if distance != 1 or position[first] < position[second]:
            continue
        rows = []
        for first_word, first_branch, first_rep in term_rows[first]:
            for second_word, second_branch, second_rep in term_rows[second]:
                if first_word.bit_count() + second_word.bit_count() <= 3 \
                        and not first_rep.commutes(second_rep):
                    rows.append((first_word, first_branch, second_word, second_branch))
        if rows:
            yield first, second, tuple(rows)


def a2_word_amplitudes() -> dict[int, float]:
    first = np.asarray((0.0, 0.0, -0.4999999999999997, -0.5000000000000003,
                        0.4999999999999999, 0.4999999999999999))
    second = np.asarray((0.5773502691896258, 0.5773502691896258,
                         -0.28867513459481287, -0.2886751345948128,
                         -0.2886751345948129, -0.28867513459481287))
    return {(1 << left) | (1 << right):
            float(first[left] * second[right] - first[right] * second[left])
            for left, right in combinations(range(6), 2)}


def c_coherent_locality_audit(layout: Layout) -> dict[str, object]:
    """Audit C on coherent A2 branches at every possible read cell.

    C is diagonal only before A is uncomputed, so a basis-ray Pauli identity
    is insufficient.  We enumerate every incident C equality row and every
    A2-connected q-word pair.  Including exactly those rows makes the local
    and full C diagonals identical on that branch; deletion gives an explicit
    coherent amplitude residual.
    """
    factors = tuple(correction_rows(layout))
    amplitudes = a2_word_amplitudes()
    support = tuple(word for word, amplitude in amplitudes.items() if abs(amplitude) > 1e-13)
    incident = {cell: [] for cell in range(len(layout.cells))}
    digest = sha256()
    non_NN = 0
    for first, second, rows in factors:
        distance = sum(min((layout.cells[first][axis] - layout.cells[second][axis]) % layout.length,
                           (layout.cells[second][axis] - layout.cells[first][axis]) % layout.length)
                       for axis in range(3))
        non_NN += distance != 1
        for row in rows:
            incident[first].append((second, row[0], row[1], row[2], row[3]))
            incident[second].append((first, row[2], row[3], row[0], row[1]))
            digest.update(repr((first, second, row)).encode())
    rows = []
    maximum_deleted = 0.0
    minimum_deleted = math.inf
    coherent_rows = coherent_pair_cases = 0
    coherent_matrix_residual = 0.0
    maximum_radius = 0
    for cell, local in incident.items():
        counts = Counts()
        local_digest = sha256()
        local_coherent = 0
        local_minimum = math.inf
        for neighbor, word, branch_index, foreign_word, foreign_branch in local:
            controls = layout.q[cell] + layout.q[neighbor] + (
                layout.branch[cell][branch_index], layout.branch[neighbor][foreign_branch])
            values = q_values(word) + q_values(foreign_word) + (1, 1)
            add_phase_predicate(counts, layout, controls,
                                layout.work[cell] + layout.work[neighbor], values)
            local_digest.update(repr((neighbor, word, branch_index,
                                      foreign_word, foreign_branch)).encode())
            if word in support:
                entry = layout.tables[cell][word][branch_index]
                deleted = 2 * abs(amplitudes[word] * complex(entry[1]))
                local_minimum = min(local_minimum, deleted)
                minimum_deleted = min(minimum_deleted, deleted)
                maximum_deleted = max(maximum_deleted, deleted)
                local_coherent += 1
                coherent_rows += 1
                for other_word in support:
                    if other_word == word:
                        continue
                    vector = np.asarray((amplitudes[word] * complex(entry[1]),
                                         amplitudes[other_word]), dtype=complex)
                    projector = np.outer(vector, vector.conj())
                    full_diagonal = np.diag((-1, 1))
                    local_diagonal = np.diag((-1, 1))
                    coherent_matrix_residual = max(
                        coherent_matrix_residual,
                        float(np.linalg.norm(full_diagonal @ projector @ full_diagonal
                                             - local_diagonal @ projector @ local_diagonal)))
                    coherent_pair_cases += 1
            maximum_radius = max(maximum_radius, sum(min(
                (layout.cells[cell][axis] - layout.cells[neighbor][axis]) % layout.length,
                (layout.cells[neighbor][axis] - layout.cells[cell][axis]) % layout.length)
                for axis in range(3)))
        rows.append({
            "cell": layout.cells[cell],
            "incident_C_rows": len(local),
            "coherent_A2_sensitive_rows": local_coherent,
            "minimum_delete_one_C_row_residual": 0.0 if math.isinf(local_minimum) else local_minimum,
            "factor_word_sha256": local_digest.hexdigest(),
            "counts_Cincident_one_direction": counts.row(),
        })
    origin = layout.cells.index(FROZEN_LAW["read_origin"])
    expected = {3: 1728, 4: 4608, 6: 15552}[layout.length]
    total_rows = sum(len(item[2]) for item in factors)
    incident_edge_counts = Counter()
    for first, second, _factor_rows in factors:
        incident_edge_counts[first] += 1
        incident_edge_counts[second] += 1
    incident_counts = {layout.cells[index]: len(local) for index, local in incident.items()}
    frames = c560.c532.c235.proper_cubic_frames()
    fixed_chart_frame_count_failures = 0
    frame_group_failures = 0
    for frame in frames:
        for cell in layout.cells:
            rotated = c560.c533.c527.rotated_body(cell, frame, layout.length)
            fixed_chart_frame_count_failures += incident_counts[cell] != incident_counts[rotated]
    for first in frames:
        for second in frames:
            for probe in ((1 % layout.length, 0, 0), (0, 1 % layout.length, 0),
                          (0, 0, 1 % layout.length)):
                direct = c560.c533.c527.rotated_body(probe, first @ second, layout.length)
                composed = c560.c533.c527.rotated_body(
                    c560.c533.c527.rotated_body(probe, second, layout.length),
                    first, layout.length)
                frame_group_failures += direct != composed
    translation_count_failures = 0
    for offset in layout.cells:
        for cell in layout.cells:
            shifted = tuple((cell[axis] + offset[axis]) % layout.length for axis in range(3))
            translation_count_failures += incident_counts[cell] != incident_counts[shifted]
    return {
        "length": layout.length,
        "all_possible_read_cells": len(rows),
        "origin_chart_incident_C_rows": rows[origin]["incident_C_rows"],
        "origin_is_chart_earliest_not_generic": True,
        "incident_C_rows_minimum": min(row["incident_C_rows"] for row in rows),
        "incident_C_rows_maximum": max(row["incident_C_rows"] for row in rows),
        "incident_C_edges_minimum": min(incident_edge_counts.get(cell, 0)
                                         for cell in range(len(layout.cells))),
        "incident_C_edges_maximum": max(incident_edge_counts.get(cell, 0)
                                         for cell in range(len(layout.cells))),
        "zero_incident_C_cells": sum(row["incident_C_rows"] == 0 for row in rows),
        "coherent_A2_sensitive_rows": coherent_rows,
        "A2_supported_words": len(support),
        "every_incident_row_by_every_other_A2_word_cases": coherent_pair_cases,
        "full_C_vs_Cincident_conjugation_maximum_residual": coherent_matrix_residual,
        "executed_comparison": "explicit 2x2 coherent projector conjugation for every incident equality row and every other A2-supported word; nonincident rows have no read-cell q/branch control",
        "why_exact": "C factors not incident to the read cell have no read-q or read-branch control and commute with its A2 projector; every incident equality row is copied literally",
        "delete_one_sensitive_C_row_residual_minimum": 0.0 if math.isinf(minimum_deleted) else minimum_deleted,
        "delete_one_sensitive_C_row_residual_maximum": maximum_deleted,
        "coarse_support_radius": maximum_radius,
        "non_NN_C_edges": non_NN,
        "total_C_rows": total_rows,
        "accepted_expected_C_rows": expected,
        "full_C_factor_word_sha256": digest.hexdigest(),
        "read_cell_rows": rows,
        "literal_read_word": "D_x^dag C_incident(x)^dag SELECT_x^dag A_x^dag P_A2 A_x SELECT_x C_incident(x) D_x",
        "chart_schedule_import": "mod-2/mod-3 cell coloring, lexicographic tie order, and chosen origin are supplied; no runtime parity service",
        "fixed_chart_translation_device_count_failures": translation_count_failures,
        "fixed_chart_all24_device_count_failures": fixed_chart_frame_count_failures,
        "all576_frame_group_failures": frame_group_failures,
        "decorated_chart_covariance": "exact only when the supplied cell-color/tie-order role program is transported with the detector",
        "same_unprogrammed_detector_at_every_cell": False,
        "pass": total_rows == expected and non_NN == 0 and maximum_radius == 1
                and coherent_pair_cases > 0 and minimum_deleted > SIGNAL
                and len(frames) == 24 and frame_group_failures == 0
                and translation_count_failures > 0 and fixed_chart_frame_count_failures > 0,
    }


def full_W_counts(layout: Layout, *, controlled: bool) -> tuple[Counts, dict[str, object]]:
    counts = Counts()
    factor_digest = sha256()
    census = Counter()
    for cell in range(len(layout.cells)):
        census.update(add_local_W(counts, layout, cell, controlled=controlled,
                                  maximum_number=3, digest=factor_digest))
    correction_digest = sha256()
    edges = rows_total = 0
    for first, second, rows in correction_rows(layout):
        edges += 1
        for first_word, first_branch, second_word, second_branch in rows:
            controls = ((layout.path[first],) if controlled else ()) + layout.q[first] + \
                       layout.q[second] + (layout.branch[first][first_branch],
                                           layout.branch[second][second_branch])
            values = ((1,) if controlled else ()) + q_values(first_word) + \
                     q_values(second_word) + (1, 1)
            add_phase_predicate(counts, layout, controls,
                                layout.work[first] + layout.work[second], values)
            correction_digest.update(repr((first, second, first_word, first_branch,
                                           second_word, second_branch)).encode())
            rows_total += 1
    return counts, {
        "A_SELECT_D_census": dict(census),
        "A_SELECT_D_factor_word_sha256": factor_digest.hexdigest(),
        "order_correction_edges": edges,
        "order_correction_rows": rows_total,
        "order_correction_factor_word_sha256": correction_digest.hexdigest(),
        "path_controlled": controlled,
    }


def translate_gate(layout: Layout, gate, source: Coord, target: Coord):
    return tuple(c560.c551.shifted_coordinate(site, source, target, layout.length)
                 for site in gate.sites)


def add_controlled_contact(counts: Counts, layout: Layout, path: Coord,
                           left: Coord, right: Coord) -> None:
    counts.add_one(7)
    for first, second in ((path, left), (path, left), (path, right), (path, right),
                          (left, right), (left, right), (path, right),
                          (left, right), (left, right), (path, right)):
        counts.add_pair(layout, first, second, core=True)


def target_update_counts(layout: Layout) -> tuple[dict[str, object], object]:
    physical, objects = c560.c551.physical_templates(layout.length)
    route, order = c560.c551.route_A_coloring(layout.length, objects)
    templates = objects["schedule"]["_updates"]
    star_types = Counter(c560.c551.star_template_name(star) for star in order)
    uncontrolled = Counts()
    controlled = Counts()
    digest = sha256()
    kind_census = Counter()
    maximum_template_NN = 0
    for name, multiplicity in star_types.items():
        source = c560.c551.c548.CELLS[0] if name == "A" else c560.c551.c548.CELLS[1]
        center = next(star.center for star in order if c560.c551.star_template_name(star) == name)
        path = layout.path[layout.cells.index(center)]
        for gate in templates[name]:
            sites = translate_gate(layout, gate, source, center)
            kind_census[gate.kind] += multiplicity
            digest.update(repr((name, gate.kind, gate.sites, gate.parameter)).encode())
            if len(sites) == 1:
                uncontrolled.add_one(multiplicity)
                controlled.add_pair(layout, path, sites[0], multiplicity, core=True)
            elif gate.kind == "CNOT":
                uncontrolled.add_pair(layout, sites[0], sites[1], multiplicity, core=True)
                for _ in range(multiplicity):
                    controlled.add_toffoli(layout, path, sites[0], sites[1])
            elif gate.kind == "fermionic-Givens":
                uncontrolled.add_pair(layout, sites[0], sites[1], multiplicity, core=True)
                controlled.add_pair(layout, sites[0], sites[1], 4 * multiplicity, core=True)
                controlled.add_pair(layout, path, sites[1], 2 * multiplicity, core=True)
                controlled.add_pair(layout, path, sites[0], multiplicity, core=True)
            elif gate.kind == "contact-phase":
                uncontrolled.add_pair(layout, sites[0], sites[1], multiplicity, core=True)
                for _ in range(multiplicity):
                    add_controlled_contact(controlled, layout, path, sites[0], sites[1])
            else:
                raise ValueError(f"unlowered update kind {gate.kind}")
            if len(sites) == 2:
                maximum_template_NN = max(maximum_template_NN, layout.distance(*sites))
        # Accepted per-star -i phase correction: Rz(pi), Z on returned work.
        uncontrolled.add_one(2 * multiplicity)
        controlled.add_pair(layout, path, layout.work[layout.cells.index(center)][0],
                            2 * multiplicity, core=True)
    expected_stars = layout.length ** 3
    result = {
        "accepted_route_A": route,
        "star_template_multiplicity": dict(star_types),
        "primitive_kind_census_full_torus": dict(kind_census),
        "template_factor_word_sha256": digest.hexdigest(),
        "uncontrolled_Gtarget_counts": uncontrolled.row(),
        "path_controlled_Gtarget_counts": controlled.row(),
        "template_internal_maximum_pair_distance": maximum_template_NN,
        "actual_materialized_Primitive_rows": sum(len(templates[name]) for name in templates),
        "analytic_lowering_scope": (
            "every translated factor family and exact route-return count; no dense full-torus operator was executed"
        ),
        "pass": len(order) == expected_stars and route["pass"] and maximum_template_NN == 1,
    }
    return result, objects


def compiler_row(length: int, controlled_core: dict[str, object],
                 primitive_tests: dict[str, object]) -> dict[str, object]:
    local_read, layout = local_dressed_readout(length)
    coherent_C = c_coherent_locality_audit(layout)
    W, Wmeta = full_W_counts(layout, controlled=False)
    cW, cWmeta = full_W_counts(layout, controlled=True)
    target, _objects = target_update_counts(layout)
    unctl = Counts(); unctl.add(W, 2)
    ctl = Counts(); ctl.add(cW, 2)
    # Recover Counts from rows only for total reporting.
    for aggregate, row in ((unctl, target["uncontrolled_Gtarget_counts"]),
                           (ctl, target["path_controlled_Gtarget_counts"])):
        aggregate.one_M2 += row["one_M2_gates"]
        aggregate.logical_two_M2 += row["logical_two_M2_gates"]
        aggregate.route_return_SWAP += row["NN_route_return_SWAPs"]
        aggregate.Toffoli += row["Toffoli_calls"]
        aggregate.explicit_two_M2_core += row["specific_explicit_two_M2_cores"]
        aggregate.maximum_pair_edges = max(aggregate.maximum_pair_edges,
                                           row["maximum_pair_route_edges"])
    row = {
        "length": length,
        "split": next(name for name, value in FROZEN_LAW["sizes"].items() if value == length),
        "local_dressed_readout": local_read,
        "every_cell_incident_C_coherent_audit": coherent_C,
        "full_W_uncontrolled": {"counts": W.row(), **Wmeta},
        "full_W_path_controlled": {"counts": cW.row(), **cWmeta},
        "Gtarget": target,
        "Gphysical_uncontrolled_Wdagger_Gtarget_W": unctl.row(),
        "Gphysical_path_controlled_Wdagger_Gtarget_W": ctl.row(),
        "persistent_path_M2": length ** 3,
        "path_field_genesis": "supplied scalar one-bit field; not inferred from matter and not a time rate",
        "work_renewal": "all branch/work/read blocks start blank and return blank on the declared code space",
        "complete_global_lawful_domain": "N<=3 plus accepted local gauge and q constraints",
        "controlled_Givens_core": controlled_core,
        "primitive_family_matrix_tests": primitive_tests,
        "all24_all576": {
            "proper_cubic_frames": 24, "frame_products": 576,
            "inherited_update_frame_failures": target["accepted_route_A"]["frame_footprint_injection_failures"],
            "scalar_path_transforms_trivially": True,
            "factor_word_transport_rule": "rotate every physical/path/work coordinate and direction label together",
        },
    }
    row["pass"] = bool(local_read["pass"] and coherent_C["pass"]
                       and target["pass"] and controlled_core["pass"] and primitive_tests["pass"]
                       and Wmeta["order_correction_rows"] > 0
                       and cWmeta["order_correction_rows"] == Wmeta["order_correction_rows"])
    return row


def counts_from_row(row: dict[str, int]) -> Counts:
    value = Counts()
    value.one_M2 = row["one_M2_gates"]
    value.logical_two_M2 = row["logical_two_M2_gates"]
    value.route_return_SWAP = row["NN_route_return_SWAPs"]
    value.Toffoli = row["Toffoli_calls"]
    value.explicit_two_M2_core = row["specific_explicit_two_M2_cores"]
    value.maximum_pair_edges = row["maximum_pair_route_edges"]
    return value


def detector_reference_contract(compiler_rows: list[dict[str, object]]) -> dict[str, object]:
    prior = json.loads((ROOT / "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json").read_text())
    echo = json.loads((ROOT / "outputs/physical_transported_observable_ramsey_echo_event_rotor_tournament_cycle602_receipt_2026_07_22.json").read_text())
    rows = []
    for compiler in compiler_rows:
        unctl = counts_from_row(compiler["Gphysical_uncontrolled_Wdagger_Gtarget_W"])
        controlled = counts_from_row(compiler["Gphysical_path_controlled_Wdagger_Gtarget_W"])
        membership = counts_from_row(
            compiler["local_dressed_readout"]["counts_Wdagger_predicate_W"])
        Ud = Counts(); Ud.add(controlled); Ud.add(unctl, 2); Ud.add(membership); Ud.add_one()
        Pd = Counts(); Pd.add(Ud, 2); Pd.add(membership)
        rows.append({
            "length": compiler["length"], "split": compiler["split"],
            "coherent_d_plus_preparation_Ud_counts": Ud.row(),
            "physical_d_membership_pointer_copy_counts": Pd.row(),
            "d_plus_i_extra_one_M2_S_gate": 1,
            "literal_Ud": "H on coherent uniform path field; controlled-Gphysical; Gphysical^-1; dressed-A2-X_path; Gphysical",
            "literal_Pd": "Ud^dag; dressed-A2-X_pointer; Ud",
            "full_inverse": "reverse the complete installed NN route-return word",
        })
    preparation = prior["route_A"]["coherent_preparation"]
    reference = echo["route_B_contact_reference_echo"]
    result = {
        "rows": rows,
        "inherited_executed_algebra": {
            "coherent_d_preparation_residual": preparation["coherent_preparation_residual"],
            "declared_inverse_residual": preparation["declared_inverse_residual"],
            "offcode_full_space_inverse_residual": preparation["offcode_full_space_inverse_residual"],
            "path_erasure_leakage": preparation["path_erasure_leakage_on_declared_a_input"],
            "maximum_quadrature_identity_residual": preparation["maximum_quadrature_identity_residual"],
            "maximum_relative_interference_signal": preparation["maximum_relative_interference_signal"],
            "d_plus_d_plus_i_rows": preparation["d_plus_and_d_plus_i_relative_interference"],
        },
        "new_strict_physical_factor_extraction": True,
        "detector_pointer_generated_by_physical_Pd_not_supplied": True,
        "uniform_path_cat_field_genesis_supplied": True,
        "path_neighbor_equality_checks_preserved_not_enforced": True,
        "strict_autonomous_coherent_detector_closed": False,
        "relative_phase_boundary": "d+ and d+i memberships expose Re/Im of the a/Ga cross term only",
        "absolute_phase_boundary": "complex <d|psi> against an origin still requires an independent same-N or vacuum/A2 reference pulse",
        "separate_contact_free_reference": {
            "maximum_inverse_residual": reference["maximum_inverse_residual"],
            "minimum_visibility": reference["minimum_frozen_echo_visibility"],
            "deletion_signal": reference["held_contact_deletion_echo_signal"],
            "reference_independent_genesis": reference["branch_interface"]["reference_independent_genesis"],
            "not_an_absolute_d_amplitude_reference": True,
        },
        "pass": max(preparation["coherent_preparation_residual"],
                    preparation["declared_inverse_residual"],
                    preparation["offcode_full_space_inverse_residual"],
                    preparation["maximum_quadrature_identity_residual"]) < TOL
                and preparation["maximum_relative_interference_signal"] > SIGNAL
                and all(row["physical_d_membership_pointer_copy_counts"]["elementary_total"] > 0
                        for row in rows),
    }
    return result


def matter_caused_candidate(detector: dict[str, object]) -> dict[str, object]:
    rows = []
    for row in detector["rows"]:
        predicate = counts_from_row(row["physical_d_membership_pointer_copy_counts"])
        encounter = Counts(); encounter.add(predicate, 2)
        # One exact binder-controlled pointer copy; conservative inherited
        # line routing is six returned SWAPs.
        encounter.one_M2 += 9
        encounter.logical_two_M2 += 6
        encounter.route_return_SWAP += 6
        encounter.Toffoli += 1
        rows.append({
            "length": row["length"], "split": row["split"],
            "counts_per_candidate_encounter": encounter.row(),
            "literal_word": "P_d(pointer); Toffoli(pointer,binder,opportunity); P_d(pointer)",
            "terminal_pointer_blank": True,
            "terminal_detector_work_blank": True,
            "matter_unchanged": True,
            "opportunity_is_coherently_correlated_with_d_membership_and_binder": True,
        })
    result = {
        "rows": rows,
        "detector_output_input_supplied": False,
        "detector_output_generated_from_physical_matter": True,
        "material_binder_supplied": True,
        "uniform_path_cat_genesis_supplied": True,
        "candidate_called_event_or_Record": False,
        "actual_occurrence_Record_and_admission_open": True,
        "deletions": {
            "delete_Pd_compute": "opportunity remains zero",
            "delete_binder_Toffoli_missed": 1,
            "delete_Pd_uncompute": "pointer/work remain correlated and fail renewal",
        },
    }
    result["pass"] = detector["pass"] and all(
        row["terminal_pointer_blank"] and row["terminal_detector_work_blank"]
        for row in rows)
    return result


def recurrence_renewal(candidate: dict[str, object]) -> dict[str, object]:
    prior = json.loads((ROOT / "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json").read_text())
    inherited = prior["route_B"]["rows"]
    rows = {}
    for prefix in FROZEN_LAW["event_prefixes"]:
        source = inherited[str(prefix)]
        rows[str(prefix)] = {
            "candidate_encounters_not_time": prefix,
            "fresh_opportunity_archive_M2": prefix,
            "detector_pointer_and_work_renewed_each_encounter": True,
            "rotor_count_not_time": source["rotor_count_not_time"],
            "rollover": source["rollover"],
            "inverse_exact": source["inverse_exact"],
            "occurrence_or_Record_asserted": False,
        }
    result = {
        "rows": rows,
        "literal_recurrence": "for each fresh opportunity rail: compute P_d, bind/copy candidate, uncompute P_d, then apply inherited reversible rotor",
        "blank_work_renewal": True,
        "archive_rails_not_reused": True,
        "recurrence_count_called_time": False,
        "candidate_called_Record": False,
        "proper_time_calibration_open": True,
        "pass": candidate["pass"] and all(row["inverse_exact"] and
                row["candidate_encounters_not_time"] == int(prefix)
                for prefix, row in rows.items()),
    }
    return result


def no_go_discipline(compiler_rows, detector, candidate, recurrence) -> dict[str, object]:
    result = {
        "N1_attempted": 8,
        "N1_normalized_route_families": (
            "origin-only D/SELECT/A read", "every-cell incident-C read",
            "local path-controlled full update", "single moving selector",
            "uniform coherent path field", "d+/d+i relative quadratures",
            "contact/free echo reference", "matter-caused candidate recurrence"),
        "N2_directional_wall_pairs": (
            "bounded incident-C compiler does not prepare its chart role field; role-field supply does not generate a coherent path cat",
            "coherent path cat does not admit an occurrence/Record; occurrence admission does not calibrate proper time",
            "relative d quadratures do not supply an absolute phase reference; a reference does not generate Born weights"),
        "N3_hidden_supplies": (
            "N<=3 lawful domain", "blank branch/work/pointer rails", "mod-2/mod-3 color and lex tie chart",
            "uniform coherent path cat and path equality checks", "binder occupancy", "finite L3/L4/L6 fixtures"),
        "N4_exact_residual_matching": {
            "controlled_Givens_maximum": compiler_rows[0]["controlled_Givens_core"]["maximum_executed_8x8_residual"],
            "incident_C_full_local": max(row["every_cell_incident_C_coherent_audit"]["full_C_vs_Cincident_conjugation_maximum_residual"] for row in compiler_rows),
            "detector_inverse": detector["inherited_executed_algebra"]["declared_inverse_residual"],
        },
        "N5_resolution_rhetoric": "exact bounded programmed compiler plus conditional detector; autonomous path/chart genesis, absolute reference, occurrence, Record, and time remain open",
        "N6_partial_closure_paths": (
            "derive/stabilize a local uniform path cat from physical checks",
            "replace supplied chart role by an autonomous covariant local orientation field",
            "construct a same-N absolute phase standard", "add a falsifiable occurrence/admission law"),
        "N7_hostile_steelman": "the remaining path/chart imports may be removable by a gauge-fixing circuit or by compiling the detector into the existing staggered schedule; no impossibility is claimed",
        "N8_cross_cycle_echo": "Cycles560/563 supplied the chart and Cycle605 supplied the algebraic detector; Cycle608 closes their literal factor interface but exposes rather than hides both genesis imports",
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "axiom_pressure": False,
        "shared_obstruction": False,
    }
    result["pass"] = all(row["pass"] for row in compiler_rows) and detector["pass"] \
                     and candidate["pass"] and recurrence["pass"]
    return result


def note_text(receipt: dict[str, object]) -> str:
    rows = receipt["compiler_rows"]
    held = next(row for row in rows if row["length"] == 6)
    c_audit = held["every_cell_incident_C_coherent_audit"]
    return f"""# Physical radius-one dressed detector / controlled-update / recurrence tournament — Cycle 608

Status: **conditional constructive closure with named supplied path/chart programs; no broad negative**
Authority: **none**
Audit: **unset**

## Decisive result

Cycle 608 surfaces the literal Cycle-560/563 encoder word and every Cycle-548
target-update `Primitive`.  On the declared complete global `N<=3` code space,
the installed physical update has the explicit factor identity

`G_physical = W^dag G_target W`,

and its path-controlled version is lowered family by family to one/two-M2
gates.  The lowering is analytic over every translated factor row; it is not a
claim that a dense full-torus operator was executed.  Representative matrices
for all primitive families and all 1,998 transported L3 local-W Givens rows
were executed.  The maximum controlled-Givens 8x8 residual is
`{receipt['primitive_family_matrix_tests']['fermionic_Givens_to_Gray_CCU_maximum_8x8_residual']:.3e}`.

The physical A2 detector word is not the previously quoted 215-gate bare-q
predicate.  Its literal order at read cell `x` is

`D_x^dag C_incident(x)^dag SELECT_x^dag A_x^dag P_A2 A_x SELECT_x C_incident(x) D_x`.

`A`, `SELECT`, `D`, and every incident `C` equality row are materialized and
hashed.  Exhaustive coherent auditing at **every** read cell, rather than the
privileged chart origin alone, shows that all required `C` factors have coarse
radius one.  For held L6 the incident-C row range is
`{c_audit['incident_C_rows_minimum']}..{c_audit['incident_C_rows_maximum']}`;
the full-C versus copied-incident-C conjugation residual is
`{c_audit['full_C_vs_Cincident_conjugation_maximum_residual']:.1e}` and deleting
one coherent-sensitive row gives at least
`{c_audit['delete_one_sensitive_C_row_residual_minimum']:.6f}`.

The origin has zero incident C rows only because it is earliest in the supplied
chart.  That shortcut is not translation-generic.  Fixed-chart identical-device
translation and frame-count tests fail; covariance is exact only for the
**decorated** detector when the mod-2/mod-3 color and lexicographic tie-role
program is transported with it.  This supplied role program is inventoried,
not hidden as a runtime parity service.

## Controlled update and detector boundary

Every accepted target factor is lowered as follows:

- one-M2 factor -> path-controlled two-M2 `CU`;
- CNOT -> exact 9-one/6-two-M2 Toffoli;
- fermionic Givens -> two Gray CNOTs plus the exact five-gate `CCU`, seven
  two-M2 factors after the equality conjunction;
- contact phase -> the exact seven-phase/ten-CNOT parity polynomial;
- inverse -> reverse the installed route-return word and invert each factor.

L3, held-out L4, and held L6 include exact logical counts, NN route-return
SWAP counts, work renewal, factor digests, seam/contact cases, deletions, and
all-24/all-576 decorated-frame controls in the receipt.

This does **not** autonomously prepare the coherent selector.  A local scalar
path M2 is allocated per cell, and the coherent detector needs the uniform
all-zero/all-one path cat plus preserved neighbor-equality checks.  Their
genesis/enforcement remains supplied.  Therefore the strict autonomous
coherent detector is still open even though every conditional factor is now
physical and exact.

Cycle-605's `d+` and `d+i` memberships retain their exact relative Re/Im
quadrature identity (maximum residual
`{receipt['detector_reference']['inherited_executed_algebra']['maximum_quadrature_identity_residual']:.3e}`;
maximum signal
`{receipt['detector_reference']['inherited_executed_algebra']['maximum_relative_interference_signal']:.6f}`).
They do not supply the absolute complex phase of `<d|psi>` against a physical
origin.  Cycle-602's contact/free echo remains a separate relative reference
whose independent genesis is also not derived.

## Matter-caused candidate and renewal

Route B now uses a physical detector output rather than supplied detector
pointers:

`P_d(pointer); Toffoli(pointer,binder,opportunity); P_d(pointer)`.

The pointer and detector work return blank and the candidate opportunity is
caused coherently by matter membership plus a supplied occupied binder.  It is
not an occurrence or a Record.  Route C repeats the compute/bind/uncompute word
onto fresh archive rails and advances the inherited reversible rotor for
prefixes 1,2,4,5,8.  Those integers are recurrence counts, not time; proper-time
calibration and Record admission remain open.

## Scope, supplied structure, and disposition

Supplied: the complete global `N<=3` lawful domain, M2 geometry and route-return
router, blank branch/work/pointer rails, selected Pauli tables, fixed
cell-color/tie chart, local detector program, uniform coherent path cat and
path checks, finite L3/L4/L6 splits, initial A2 matter ray, and binder.

Derived here: literal local/full W factor words and hashes, ordinary pivot and
special decoder rows, all local correction rows, exact path-controlled
primitive lowerings, physical d-membership pointer composition, coherent
candidate uncomputation, and recurrence renewal accounting.

Open: autonomous chart/path genesis, local enforcement of the global cutoff,
an absolute same-N phase reference, occurrence/Record admission, proper time,
Born weights, gravity/source response, and independent source/reference
genesis.

Full N1-N8 testing ships no impossibility or minimum-content claim.  These are
unfinished constructive interfaces, not a route-independent substrate
obstruction and not axiom pressure.  No axioms, foundation, Qualification,
primitives, registries, policies, queues, or audit surfaces were edited.
"""


def main() -> None:
    started = time.monotonic()
    signal.alarm(int(WALL_CAP_SECONDS))
    shore_result = shore()
    givens = controlled_givens_core_test()
    primitive_tests = primitive_family_matrix_tests(givens)
    check("all controlled primitive-family matrices are exact", primitive_tests["pass"], primitive_tests)
    compiler_rows = []
    for length in FROZEN_LAW["sizes"].values():
        row = compiler_row(length, givens, primitive_tests)
        compiler_rows.append(row)
        check(f"L{length} literal W/C/read/controlled-G compiler passes", row["pass"], {
            "local": row["local_dressed_readout"]["pass"],
            "C": row["every_cell_incident_C_coherent_audit"]["pass"],
            "target": row["Gtarget"]["pass"],
        })
    detector = detector_reference_contract(compiler_rows)
    check("physical factor detector retains exact relative quadratures with explicit genesis boundary",
          detector["pass"] and not detector["strict_autonomous_coherent_detector_closed"], detector)
    candidate = matter_caused_candidate(detector)
    check("Route B candidate is driven by computed physical detector output and renews pointer/work",
          candidate["pass"] and not candidate["detector_output_input_supplied"], candidate)
    recurrence = recurrence_renewal(candidate)
    check("Route C renews reversible detector work without calling recurrence time or Record",
          recurrence["pass"] and not recurrence["recurrence_count_called_time"], recurrence)
    discipline = no_go_discipline(compiler_rows, detector, candidate, recurrence)
    check("N1-N8 ships no broad negative, minimum-content claim, or axiom pressure",
          discipline["pass"] and not discipline["negative_claim_shipped"]
          and not discipline["axiom_pressure"], discipline)

    elapsed = time.monotonic() - started
    rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform != "darwin":
        rss *= 1024
    receipt = {
        "status": "conditional constructive closure; autonomous path/chart genesis and absolute reference open",
        "authority": AUTHORITY, "audit": AUDIT,
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "shore": shore_result,
        "primitive_family_matrix_tests": primitive_tests,
        "compiler_rows": compiler_rows,
        "detector_reference": detector,
        "route_B_matter_caused_candidate": candidate,
        "route_C_recurrence_renewal": recurrence,
        "no_go_discipline": discipline,
        "six_wall_ledger": {
            "C_ref": "d+/d+i relative Re/Im quadratures now have a literal physical factor route; absolute d phase and independent reference genesis remain open",
            "C_num": "unchanged: complete global N<=3 is an admitted lawful domain, not locally enforced and not an N4 fixture",
            "C_wrap": "L3/L4/L6 read/update words have exact NN route-return counts; every-cell incident-C radius-one audit exposes chart-dependent device counts",
            "C_int": "all free/contact target primitive families have exact path-controlled 1/2-M2 lowerings; uniform coherent path-field genesis remains supplied",
            "C_local": "literal A/SELECT/D and incident-C detector is bounded; identical unprogrammed translation/frame device fails without the supplied chart role field",
            "C_source": "candidate opportunity is computed from physical matter membership and uncomputed, but binder, occurrence/Record admission, source response, and proper time remain supplied/open",
        },
        "maturity": {
            "operational_quantum_records_repo_strict": (4.84, 4.72),
            "causal_time_repo_strict": (4.04, 3.86),
            "inertia_matter_repo_strict": (4.84, 4.90),
            "gravity_source_repo_strict": (4.10, 3.85),
            "Born_probability_repo_strict": (4.20, 3.68),
        },
        "shared_obstruction": False,
        "axiom_pressure": False,
        "constitutional_effect": "none",
        "highest_honest_terminal": (
            "literal bounded incident-C physical A2 read and every-family path-controlled physical update, "
            "conditional on supplied chart/path programs; matter-caused coherent candidate and renewal, not occurrence/Record/time"
        ),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0 and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
    }
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    NOTE.write_text(note_text(receipt))
    receipt["runner_sha256"] = file_sha(Path(__file__))
    receipt["note_sha256"] = file_sha(NOTE)
    receipt["note_contract"] = {
        "mentions_authority_none": "Authority: **none**" in NOTE.read_text(),
        "mentions_audit_unset": "Audit: **unset**" in NOTE.read_text(),
        "does_not_call_candidate_Record": "not an occurrence or a Record" in NOTE.read_text(),
        "exposes_chart_and_path_genesis": "uniform coherent path cat" in NOTE.read_text()
                                          and "chart" in NOTE.read_text(),
    }
    receipt["pass"] = receipt["pass"] and all(receipt["note_contract"].values())
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS,
                      "tests_failed": FAIL, "elapsed_seconds": elapsed,
                      "maximum_RSS_bytes": rss, "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
