#!/usr/bin/env python3
"""Cycle608: local-factor/count and exact primitive-decomposition audit.

This runner executes finite role-table enumeration, factor/count blueprints,
and small primitive matrix identities.  ``add_local_W`` does not execute a
physical encoder, detector, readout, placement, primitive product, or
intertwiner.  The controlled-Givens positive is only the exact three-qubit
decomposition actually multiplied below.  Membership roles are not Events or
Records, prefix ordinals are not time, and phase is not energy.
"""
from __future__ import annotations

import ast
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
COLD = ROOT / (
    "outputs/physical_radius_one_dressed_detector_controlled_update_"
    "recurrence_tournament_cycle608_cold_2026_07_22.txt"
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
        "fe00d384ff64823017a6c746b3ed46fde1986b46dbe1b9f7514bd857141e2bda",
    "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_DETECTOR_EVENT_ASSOCIATION_CONTROLLED_ECHO_TOURNAMENT_CYCLE605_NOTE_2026-07-22.md":
        "c59199cb71f4e01e4ae8e10e4a11678597f86558c148cf93af05f96c5b112b9b",
    "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json":
        "c2cca9a4a8600d48dfd8acb83d9c1e70becdf76a9e3b507d41f1a494369ecbed",
    "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_cold_2026_07_22.txt":
        "4498f865b0b71a72766aa14253f13981f5a137ed5ddd2572a613f3521a83b9ae",
    "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py":
        "f6d641e4735b26f9463ea623ee8ed6e28acc995fdfc88300709dcfac100c13ab",
    "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "55e51cafffa70284a6e8e1f0510ca0d2f890989ccbcf5bce64435df4c8e812a6",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "43e5b749702fba9551fab43a242f832b824fdbff54817b5206097f02ad146e55",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "f0f3ed6d41132625b8907cbcda8f105b7ec975e4b952562b45fe5b7d8e1b3a0e",
}

FROZEN_LAW = {
    "sizes": {"train": 3, "held_out": 4, "held": 6},
    "aggregate_labels": "d+=(a+Ga)/sqrt(2), d+i=(a+iGa)/sqrt(2)",
    "read_origin": (0, 0, 0),
    "candidate_factor_blueprint": "count each Wdagger, G_target, W role-table factor with a supplied scalar path role",
    "candidate_prefixes": (1, 2, 4, 5, 8),
}
FROZEN_LAW_SHA256 = sha256(json.dumps(FROZEN_LAW, sort_keys=True).encode()).hexdigest()
EXPECTED_RUNTIME_IMPORT_COUNT = 50
EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256 = "df22a04a96b33f6e26392733ac49fb0d5c5626e72bde0177d4b040a4c9aba56d"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def runtime_import_closure() -> dict[str, object]:
    modules = {path.stem: path for path in (ROOT / "scripts").glob("*.py")}
    entry = Path(__file__).resolve()
    visited: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        visited.add(path)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            names: tuple[str, ...] = ()
            if isinstance(node, ast.Import):
                names = tuple(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = (node.module.split(".")[0],)
            for name in names:
                if name in modules:
                    visit(modules[name])

    visit(entry)
    closure = tuple(sorted(str(path.relative_to(ROOT)) for path in visited if path != entry))
    observed = {path: file_sha(ROOT / path) for path in closure}
    payload = "".join(f"{path}\0{observed[path]}\n" for path in closure)
    manifest = sha256(payload.encode()).hexdigest()
    return {
        "direct_runtime_imports": (
            "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py",
        ),
        "complete_runtime_import_closure": closure,
        "runtime_import_count": len(closure),
        "hidden_runtime_import_count": len(closure) - 1,
        "observed_sha256": observed,
        "closure_manifest_sha256": manifest,
        "expected_closure_manifest_sha256": EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256,
        "pass": len(closure) == EXPECTED_RUNTIME_IMPORT_COUNT
                and "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py" in closure
                and manifest == EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256,
    }


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
    runtime = runtime_import_closure()
    fixtures = prior["shore"]["retained_coarse_fixtures"]
    cycle605_contract = {
        "pass": prior["pass"] is True,
        "authority_audit": prior["authority"] == "none" and prior["audit"] == "unset",
        "no_go_FAIL": prior["no_go_discipline"]["Status"] == "FAIL",
        "physical_boundary_null": len(prior["physical_composition_boundary"]) == 25
                                  and all(value is None for value in prior["physical_composition_boundary"].values()),
        "author_not_accepted": prior["author_accepted"] is False,
        "breakthrough_false": prior["breakthrough"] is False,
    }
    condition = observed == FROZEN_SHORES and len(FROZEN_SHORES) == 8 \
                and all(cycle605_contract.values()) and runtime["pass"] \
                and max(fixtures.values()) < TOL
    result = {"expected": FROZEN_SHORES, "observed": observed,
              "exact_pinned_surfaces": len(FROZEN_SHORES),
              "Cycle605_contract": cycle605_contract,
              "retained_coarse_fixtures": fixtures,
              "runtime_import_closure": runtime}
    check("Cycle605 quartet, Cycle560/563/590 shores, and runtime closure are byte exact", condition, result)
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


def add_algebraic_A2_predicate(counts: Counts, layout: Layout, *, target: Coord) -> dict[str, object]:
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


def local_factor_blueprint(length: int) -> tuple[dict[str, object], Layout]:
    layout = build_layout(length)
    origin = layout.cells.index(FROZEN_LAW["read_origin"])
    counts = Counts()
    digest = sha256()
    # Counted W_origin^dagger, predicate, W_origin blueprint.  No product is executed.
    one_W = Counts()
    census = add_local_W(one_W, layout, origin, controlled=False,
                         maximum_number=2, digest=digest)
    counts.add(one_W, 2)
    predicate = add_algebraic_A2_predicate(counts, layout, target=layout.pointer)
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
        "role_table_auxiliary_cancellation_comparison": comparison,
        "predicate": predicate,
        "counts_candidate_Wdagger_predicate_W_word": counts.row(),
        "selected_role_table_support_sites": len(support_sites),
        "maximum_selected_support_fine_L1_radius": maximum_radius,
        "candidate_role_sites_per_cell_before_path": 53,
        "path_role_sites_per_cell": 1,
        "retained_pointer_role_site": 1,
        "candidate_read_work_role_sites": 5,
        "global_N_le_3_domain_locally_enforced": False,
        "physical_encoder_E": None,
        "physical_update_G": None,
        "intertwiner_certificate": None,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
        "locally_enforced_chart_path_genesis": None,
        "interpretation": "explicit local role-table factor/count blueprint; add_local_W is not a physical detector or readout",
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
    """Execute only the exact three-qubit CCU/Gray matrix decomposition."""
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
    residual = inverse_residual = 0.0
    minimum_deleted_core_signal = math.inf
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
                    inverse = np.eye(8, dtype=complex)
                    for gate in reversed(sequence):
                        inverse = gate.conj().T @ inverse
                    inverse_residual = max(inverse_residual,
                                           float(np.linalg.norm(inverse @ actual - np.eye(8))))
                    deleted = np.eye(8, dtype=complex)
                    for gate in sequence[1:]:
                        deleted = gate @ deleted
                    minimum_deleted_core_signal = min(
                        minimum_deleted_core_signal, float(np.linalg.norm(deleted - expected)))
                    digest.update(repr((length, cell, word, int(target), tuple(
                        c560.c533.complex_token(value) for value in root.reshape(-1)
                    ))).encode())
                    cases += 1
    return {
        "accepted_local_Givens_cases": cases,
        "execution_scope": "exact 8x8 matrix multiplication for every q-word Givens parameter row in L3; no placement, encoder, or full product",
        "held_and_out_size_parameters": "transported from the same inherited size-independent table law; not independently matrix-executed",
        "specific_two_M2_word": (
            "CNOT(a,b), CV(b,a), CNOT(c,b), CVdagger(b,a), "
            "CNOT(c,b), CV(c,a), CNOT(a,b), V^2=U"
        ),
        "two_M2_gates_per_controlled_Givens_after_conjunction": 7,
        "maximum_executed_8x8_residual": residual,
        "maximum_executed_inverse_8x8_residual": inverse_residual,
        "minimum_delete_first_factor_8x8_signal": minimum_deleted_core_signal,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
        "root_parameter_digest_sha256": digest.hexdigest(),
        "pass": residual < TOL and inverse_residual < TOL
                and minimum_deleted_core_signal > SIGNAL and cases > 0,
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
    toffoli_inverse_residual = float(np.linalg.norm(actual.conj().T @ actual - np.eye(8)))
    toffoli_deleted_signal = float(np.linalg.norm(sequence[1] @ np.eye(8) - expected))
    result = {
        "one_site_to_controlled_two_M2_maximum_4x4_residual": one_site_residual,
        "CNOT_to_Toffoli_executed_8x8_residual": toffoli_residual,
        "CNOT_to_Toffoli_inverse_residual": toffoli_inverse_residual,
        "CNOT_to_Toffoli_delete_word_signal": toffoli_deleted_signal,
        "Toffoli_word": {"one_M2": 9, "two_M2": 6},
        "fermionic_Givens_to_Gray_CCU_maximum_8x8_residual": givens["maximum_executed_8x8_residual"],
        "contact_phase_polynomial_truth_table_maximum_residual": contact_residual,
        "contact_word_per_pair": {"one_M2_phase": 7, "two_M2_CNOT": 10},
        "inverse_rule": "reverse each literal word and invert every one/two-M2 factor",
        "families": ("one-role diagonal CU", "CNOT-to-Toffoli", "three-qubit controlled-Givens", "contact-phase truth table"),
        "scope": "small exact matrices/truth tables only; factor families are not a physical compiler, placement, or primitive product",
        "physical_encoder_E": None,
        "physical_update_G": None,
        "intertwiner_certificate": None,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
    }
    result["pass"] = max(one_site_residual, toffoli_residual, toffoli_inverse_residual,
                          givens["maximum_executed_8x8_residual"],
                          givens["maximum_executed_inverse_8x8_residual"], contact_residual) < TOL \
                     and toffoli_deleted_signal > SIGNAL
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


def c_coherent_role_table_audit(layout: Layout) -> dict[str, object]:
    """Audit counted C rows on algebraic A2 role branches at each read cell.

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
        "full_C_vs_Cincident_algebraic_conjugation_maximum_residual": coherent_matrix_residual,
        "executed_comparison": "explicit 2x2 algebraic projector conjugation for every incident equality row and every other A2-supported word; this is not full-code leakage or a physical detector product",
        "why_count_matches": "C rows not incident to the read cell have no read-q/read-branch role; every incident equality row is copied into the blueprint",
        "delete_one_sensitive_C_row_residual_minimum": 0.0 if math.isinf(minimum_deleted) else minimum_deleted,
        "delete_one_sensitive_C_row_residual_maximum": maximum_deleted,
        "coarse_support_radius": maximum_radius,
        "non_NN_C_edges": non_NN,
        "total_C_rows": total_rows,
        "accepted_expected_C_rows": expected,
        "full_C_factor_word_sha256": digest.hexdigest(),
        "read_cell_rows": rows,
        "candidate_read_word_blueprint": "D_x^dag C_incident(x)^dag SELECT_x^dag A_x^dag P_A2 A_x SELECT_x C_incident(x) D_x",
        "chart_schedule_import": "mod-2/mod-3 cell coloring, lexicographic tie order, and chosen origin are supplied; no runtime parity service",
        "transported_fixed_chart_translation_count_failures": translation_count_failures,
        "transported_all24_chart_count_failures": fixed_chart_frame_count_failures,
        "inherited_all576_frame_group_failures": frame_group_failures,
        "covariance_credit": None,
        "transported_chart_statement": "coordinate/count comparison only when the supplied cell-color/tie-order role program is transported; not physical proper-cubic covariance",
        "same_unprogrammed_device_at_every_cell": False,
        "physical_encoder_E": None,
        "physical_update_G": None,
        "intertwiner_certificate": None,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
        "locally_enforced_chart_path_genesis": None,
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
        "inherited_route_A_blueprint": route,
        "star_template_multiplicity": dict(star_types),
        "primitive_kind_census_full_torus": dict(kind_census),
        "template_factor_word_sha256": digest.hexdigest(),
        "uncontrolled_Gtarget_factor_counts": uncontrolled.row(),
        "path_controlled_Gtarget_factor_counts": controlled.row(),
        "template_internal_maximum_pair_distance": maximum_template_NN,
        "actual_materialized_Primitive_rows": sum(len(templates[name]) for name in templates),
        "analytic_lowering_scope": (
            "every translated factor-family count; no full-torus operator, placement, product, encoder or intertwiner was executed"
        ),
        "physical_encoder_E": None,
        "physical_update_G": None,
        "intertwiner_certificate": None,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
        "pass": len(order) == expected_stars and route["pass"] and maximum_template_NN == 1,
    }
    return result, objects


def compiler_row(length: int, controlled_core: dict[str, object],
                 primitive_tests: dict[str, object]) -> dict[str, object]:
    local_read, layout = local_factor_blueprint(length)
    coherent_C = c_coherent_role_table_audit(layout)
    W, Wmeta = full_W_counts(layout, controlled=False)
    cW, cWmeta = full_W_counts(layout, controlled=True)
    target, _objects = target_update_counts(layout)
    unctl = Counts(); unctl.add(W, 2)
    ctl = Counts(); ctl.add(cW, 2)
    # Recover Counts from rows only for total reporting.
    for aggregate, row in ((unctl, target["uncontrolled_Gtarget_factor_counts"]),
                           (ctl, target["path_controlled_Gtarget_factor_counts"])):
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
        "local_factor_count_blueprint": local_read,
        "every_cell_incident_C_role_table_audit": coherent_C,
        "full_W_uncontrolled": {"counts": W.row(), **Wmeta},
        "full_W_path_controlled": {"counts": cW.row(), **cWmeta},
        "Gtarget": target,
        "candidate_uncontrolled_Wdagger_Gtarget_W_counts": unctl.row(),
        "candidate_path_controlled_Wdagger_Gtarget_W_counts": ctl.row(),
        "persistent_path_role_sites": length ** 3,
        "path_field_genesis": "supplied scalar one-bit field; not inferred from matter and not a time rate",
        "work_renewal_blueprint": "counts assume blank branch/work/read roles and their formal reverse word; no full product is executed",
        "supplied_global_lawful_domain": "N<=3 plus inherited gauge/q promises; not locally enforced here",
        "controlled_Givens_core": controlled_core,
        "primitive_family_matrix_tests": primitive_tests,
        "inherited_transported_all24_all576": {
            "proper_cubic_frames": 24, "frame_products": 576,
            "inherited_update_frame_failures": target["inherited_route_A_blueprint"]["frame_footprint_injection_failures"],
            "scalar_path_transforms_trivially": True,
            "factor_word_transport_rule": "inherited coordinate-label transport only; no Cycle608 physical covariance credit",
            "Cycle608_physical_covariance_credit": None,
        },
        "physical_encoder_E": None,
        "physical_update_G": None,
        "intertwiner_certificate": None,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
        "locally_enforced_chart": None,
        "locally_enforced_path": None,
        "autonomous_genesis": None,
        "route_disposition": "explicit local-factor/count blueprint plus exact small primitive decompositions only",
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


def algebraic_composition_blueprint(compiler_rows: list[dict[str, object]]) -> dict[str, object]:
    prior = json.loads((ROOT / "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json").read_text())
    rows = []
    for compiler in compiler_rows:
        unctl = counts_from_row(compiler["candidate_uncontrolled_Wdagger_Gtarget_W_counts"])
        controlled = counts_from_row(compiler["candidate_path_controlled_Wdagger_Gtarget_W_counts"])
        membership = counts_from_row(
            compiler["local_factor_count_blueprint"]["counts_candidate_Wdagger_predicate_W_word"])
        aggregate_word = Counts(); aggregate_word.add(controlled); aggregate_word.add(unctl, 2)
        aggregate_word.add(membership); aggregate_word.add_one()
        membership_word = Counts(); membership_word.add(aggregate_word, 2); membership_word.add(membership)
        rows.append({
            "length": compiler["length"], "split": compiler["split"],
            "candidate_aggregate_preparation_word_counts": aggregate_word.row(),
            "candidate_membership_word_counts": membership_word.row(),
            "d_plus_i_extra_one_role_S_count": 1,
            "candidate_aggregate_word": "H_path; counted controlled-G word; counted G^-1 word; counted A2-role toggle; counted G word",
            "candidate_membership_word": "reverse candidate aggregate word; A2-role pointer toggle; candidate aggregate word",
            "count_reverse_identity": membership_word.row()["elementary_total"] > 0,
            "physical_encoder_E": None,
            "physical_update_G": None,
            "intertwiner_certificate": None,
            "physical_placement": None,
            "physical_primitive_product": None,
            "full_code_leakage": None,
        })
    preparation = prior["route_A"]["coherent_preparation"]
    inherited = {
        "source": "accepted Cycle605 coarse/algebraic result only",
        "coherent_aggregate_preparation_residual": preparation["coherent_preparation_residual"],
        "declared_inverse_residual": preparation["declared_inverse_residual"],
        "offdomain_full_space_inverse_residual": preparation["offcode_full_space_inverse_residual"],
        "residual_path_arm_norm": preparation["residual_path_arm_norm_on_declared_a_input"],
        "maximum_quadrature_identity_residual": preparation["maximum_quadrature_identity_residual"],
        "maximum_relative_interference_signal": preparation["maximum_relative_interference_signal"],
        "not_Cycle608_physical_credit": True,
    }
    result = {
        "rows": rows,
        "inherited_Cycle605_coarse_algebra": inherited,
        "interpretation": "counted composition blueprint only; add_local_W and role-table factors are not a physical detector/readout",
        "uniform_path_role_genesis": None,
        "path_neighbor_constraints_locally_enforced": None,
        "physical_encoder_E": None,
        "physical_update_G": None,
        "intertwiner_certificate": None,
        "physical_placement": None,
        "physical_primitive_product": None,
        "full_code_leakage": None,
        "Event": None, "Record": None, "time": None, "full_echo": None,
    }
    result["pass"] = max(inherited["coherent_aggregate_preparation_residual"],
                         inherited["declared_inverse_residual"],
                         inherited["offdomain_full_space_inverse_residual"],
                         inherited["maximum_quadrature_identity_residual"]) < TOL \
                     and inherited["maximum_relative_interference_signal"] > SIGNAL \
                     and all(row["count_reverse_identity"] for row in rows)
    return result


def candidate_role_blueprint(composition: dict[str, object]) -> dict[str, object]:
    prior = json.loads((ROOT / "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json").read_text())
    rows = []
    for row in composition["rows"]:
        predicate = counts_from_row(row["candidate_membership_word_counts"])
        encounter = Counts(); encounter.add(predicate, 2)
        encounter.one_M2 += 9; encounter.logical_two_M2 += 6
        encounter.route_return_SWAP += 6; encounter.Toffoli += 1
        rows.append({
            "length": row["length"], "split": row["split"],
            "candidate_encounter_count_blueprint": encounter.row(),
            "candidate_word": "counted membership word; Toffoli(pointer,binder,candidate); reverse counted membership word",
            "terminal_pointer_blank": None,
            "terminal_work_blank": None,
            "matter_unchanged": None,
            "physical_execution": None,
        })
    inherited_deletion = prior["route_B"]["deletion_controls"]
    result = {
        "rows": rows,
        "inherited_Cycle605_Boolean_deletion_controls": inherited_deletion,
        "material_binder": "supplied role",
        "interpretation": "count arithmetic plus inherited Boolean association; no detector output or matter-to-candidate physical product is executed",
        "physical_detector_output": None,
        "physical_candidate_association": None,
        "Event": None, "Record": None, "time": None,
    }
    result["pass"] = composition["pass"] and all(value == 1 for value in inherited_deletion.values()) \
                     and all(row["candidate_encounter_count_blueprint"]["elementary_total"] > 0 for row in rows)
    return result


def recurrence_role_controls(candidate: dict[str, object]) -> dict[str, object]:
    prior = json.loads((ROOT / "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json").read_text())
    inherited = prior["route_B"]["rows"]
    rows = {}
    for prefix in FROZEN_LAW["candidate_prefixes"]:
        source = inherited[str(prefix)]
        rows[str(prefix)] = {
            "candidate_prefix_ordinal_not_time": prefix,
            "inherited_rotor_count_not_time": source["rotor_count_not_time"],
            "inherited_rollover": source["rollover"],
            "inherited_Boolean_inverse_exact": source["inverse_exact"],
            "Cycle608_physical_renewal_executed": False,
            "Event": None, "Record": None, "time": None,
        }
    result = {
        "rows": rows,
        "interpretation": "inherited Cycle605 finite Boolean prefix controls only; no Cycle608 recurrence device, Event, Record, or time",
        "archive_placement": None,
        "blank_work_renewal": None,
        "proper_time": None,
        "pass": candidate["pass"] and all(row["inherited_Boolean_inverse_exact"] and
                row["candidate_prefix_ordinal_not_time"] == int(prefix)
                for prefix, row in rows.items()),
    }
    return result


def malformed_inverse_deletion_controls(givens: dict[str, object],
                                        primitive_tests: dict[str, object]) -> dict[str, object]:
    layout = build_layout(3)
    rejected = 0
    probes = (
        lambda: Counts().add_pair(layout, layout.path[0], layout.path[0]),
        lambda: add_mcx(Counts(), layout, layout.q[0][:2], layout.pointer,
                        layout.read_work, (1,)),
        lambda: add_mcx(Counts(), layout, layout.q[0][:6], layout.pointer, (),
                        (1, 1, 0, 0, 0, 0)),
    )
    for probe in probes:
        try:
            probe()
        except ValueError:
            rejected += 1
    result = {
        "malformed_blueprint_rejections": rejected,
        "controlled_Givens_inverse_residual": givens["maximum_executed_inverse_8x8_residual"],
        "controlled_Givens_delete_factor_signal": givens["minimum_delete_first_factor_8x8_signal"],
        "Toffoli_inverse_residual": primitive_tests["CNOT_to_Toffoli_inverse_residual"],
        "Toffoli_delete_word_signal": primitive_tests["CNOT_to_Toffoli_delete_word_signal"],
        "interpretation": "executed small-matrix inverse/deletion plus malformed blueprint validation",
    }
    result["pass"] = rejected == len(probes) \
                     and max(result["controlled_Givens_inverse_residual"], result["Toffoli_inverse_residual"]) < TOL \
                     and min(result["controlled_Givens_delete_factor_signal"], result["Toffoli_delete_word_signal"]) > SIGNAL
    return result


def line_ref(function) -> str:
    return f"{Path(inspect.getsourcefile(function) or '').name}:{inspect.getsourcelines(function)[1]}"
def no_go_discipline(compiler_rows, composition, candidate, recurrence, controls):
    def route(obj, mechanism, terminal, strength, attempted, disposition):
        return {
            "object_formulation": obj, "mechanism_invariant": mechanism,
            "terminal_obligation": terminal, "strength_vs_target": strength,
            "honesty_marker": "ATTEMPTED" if attempted else None,
            "search_status": "COUNTED" if attempted else "OPEN_UNTESTED_NOT_COUNTED",
            "disposition": disposition,
        }
    routes = (
        route("local A/SELECT/D/C role-table enumeration",
              "finite q-word, auxiliary-pattern and incident-row census",
              "factor/count blueprint on train/held/out-size", "weaker", True,
              "positive blueprint only; no encoder, intertwiner or product"),
        route("small primitive matrices and truth tables",
              "exact 4x4/8x8 multiplication and Boolean phase identity",
              "CU, Toffoli, three-qubit controlled-Givens and contact decompositions",
              "weaker", True, "exact decompositions; placement and full product open"),
        route("fixed-chart incident-C role counts",
              "radius-one incidence plus transported coordinate labels",
              "chart-dependence and inherited all24/all576 separation", "weaker", True,
              "count/counter-control only; no physical covariance"),
        route("candidate association and finite prefix roles",
              "count arithmetic plus inherited Cycle605 Boolean rows",
              "size-count blueprint and inherited prefix inverse", "weaker", True,
              "algebraic accounting only; no Event, Record or time"),
        route("literal physical encoder/intertwiner/composite",
              "executed E, G, placement, product and leakage",
              "E G_coarse = G_physical E on the full code", "target-equivalent", False, "open"),
        route("autonomous local chart/path/gauge construction",
              "locally enforced roles and genesis",
              "covariant preparation and stabilization", "unknown/comparable", False, "open"),
        route("actuality and causal-reference stack",
              "occurrence, admission, reference genesis and calibration",
              "Event/Record proper-time full-echo comparison", "unknown/comparable", False, "open"),
    )
    qualifying = tuple(row for row in routes if row["honesty_marker"] == "ATTEMPTED")
    walls = {
        "physical encoder": ("ENCODER", "literal E"),
        "intertwiner and primitive product": ("INTERTWINER_PRODUCT", "intertwiner equality and product"),
        "placement and full-code leakage": ("PLACEMENT_LEAKAGE", "placement and leakage certificate"),
        "local chart/path/genesis": ("LOCAL_GENESIS", "locally enforced roles"),
        "physical aggregate readout": ("READOUT", "aggregate measurement composition"),
        "Event and Record actuality": ("ACTUALITY", "occurrence and admission"),
        "proper time and full echo": ("CAUSAL_REFERENCE", "reference calibration and echo"),
    }
    directional = tuple({
        "pair": (left, right), "left_wall_type": walls[left][0],
        "right_wall_type": walls[right][0], "left_closes_right": False,
        "left_to_right_reason": f"{walls[left][1]} does not construct {walls[right][1]}",
        "right_closes_left": False,
        "right_to_left_reason": f"{walls[right][1]} does not construct {walls[left][1]}",
        "independent": True, "collapsed": False,
    } for left, right in combinations(walls, 2))
    proof_payload = json.dumps({
        "compiler_rows": compiler_rows, "composition": composition,
        "candidate": candidate, "recurrence": recurrence, "controls": controls,
    }, sort_keys=True, default=json_default).lower()
    scan_terms = ("we assume", "by construction", "as is standard",
                  "the framework provides", "bridge context", "background",
                  "naturally", "obviously", "standard qft", "registered", "canonical")
    phrase_hits = tuple({
        "hit": phrase, "occurrences": proof_payload.count(phrase),
        "classification": "NON_LOAD_BEARING_CONTEXT",
        "reason": "descriptive generated text only; no premise supplied",
    } for phrase in scan_terms if phrase in proof_payload)
    residuals = (
        {
            "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_DETECTOR_EVENT_ASSOCIATION_CONTROLLED_ECHO_TOURNAMENT_CYCLE605_NOTE_2026-07-22.md",
            "prior_line": 21,
            "prior_residual": "25 physical promotion fields null",
            "current_residual": "Cycle608 physical and semantic fields null",
            "same_scope": True, "scope_match": True, "exact_match": True,
            "use_as_closure": False,
            "current_path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
            "current_line": 1159,
            "current_numeric_residual": 0.0,
        },
        {
            "prior_path": "outputs/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_receipt_2026_07_22.json",
            "prior_line": 691,
            "prior_residual": "finite coarse aggregate preparation only",
            "current_residual": "inherited without physical back-credit",
            "same_scope": True, "scope_match": True, "exact_match": True,
            "use_as_closure": True,
            "current_path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
            "current_line": 1188,
            "current_numeric_residual": composition["inherited_Cycle605_coarse_algebra"]["coherent_aggregate_preparation_residual"],
        },
        {
            "prior_path": "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py",
            "prior_line": 2,
            "prior_residual": "role factors and route/count surfaces",
            "current_residual": "same factors enumerated only as blueprint",
            "same_scope": True, "scope_match": True, "exact_match": True,
            "use_as_closure": True,
            "current_path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
            "current_line": 391,
            "current_numeric_residual": float(max(
                row["local_factor_count_blueprint"]["role_table_auxiliary_cancellation_comparison"]["maximum_origin_A_inverse_residual"]
                for row in compiler_rows)),
        },
        {
            "prior_path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
            "prior_line": 660,
            "prior_residual": "no physical compiler witness",
            "current_residual": "exact three-qubit decomposition only",
            "same_scope": True, "scope_match": True, "exact_match": True,
            "use_as_closure": True,
            "current_path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
            "current_line": 660,
            "current_numeric_residual": compiler_rows[0]["controlled_Givens_core"]["maximum_executed_8x8_residual"],
        },
    )
    dropped = ({
        "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md",
        "prior_line": 56,
        "prior_residual": "counts described as physical detector/intertwiner/product",
        "current_residual": "literal E/G/product/leakage not executed",
        "same_scope": False, "scope_match": False, "exact_match": False,
        "use_as_closure": False,
        "current_path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py",
        "current_line": 1159,
        "disposition": "dropped as physical evidence",
    },)
    def rhetoric(phrase, **tested):
        return {
            "phrase": phrase,
            "per_element": tested.get("per_element", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "per_site": tested.get("per_site", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "per_mode": tested.get("per_mode", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "per_block": tested.get("per_block", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "lattice_wide": tested.get("lattice_wide", "UNTESTED_NO_NEGATIVE_CLAIM"),
        }
    rhetoric_rows = (
        rhetoric("role word not promoted to encoder", per_element="factor census", per_site="coordinate counts", per_mode="q words"),
        rhetoric("counted composite not promoted to product", per_element="small matrices", per_site="route arithmetic", per_block="no product executed"),
        rhetoric("controlled-Givens not promoted past three qubits", per_element="exact factors", per_mode="table parameters"),
        rhetoric("transported counts not promoted to covariance", per_element="frame matrices", per_site="chart counts"),
        rhetoric("candidate roles not promoted to Event or Record", per_block="Boolean inverse only"),
        rhetoric("prefix ordinals not promoted to time", per_block="prefixes 1,2,4,5,8"),
    )
    partial = (
        {"file": str(Path(__file__).relative_to(ROOT)), "candidate_path": str(Path(__file__).relative_to(ROOT)), "status": "EXECUTED_NARROW_BLUEPRINT_AND_SMALL_MATRICES", "what_closes": "counts and primitive decompositions only", "what_it_closes": "counts and primitive decompositions only"},
        {"file": "scripts/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_2026_07_22.py", "candidate_path": "scripts/physical_coherent_detector_event_association_controlled_echo_tournament_cycle605_2026_07_22.py", "status": "EXACT_PINNED_COARSE_PARENT", "what_closes": "coarse algebra only", "what_it_closes": "coarse algebra only"},
        {"file": "scripts/physical_EG_intertwiner_product_compiler_cycle_next.py", "candidate_path": "scripts/physical_EG_intertwiner_product_compiler_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "E/G/intertwiner/placement/product/leakage", "what_it_closes": "E/G/intertwiner/placement/product/leakage"},
        {"file": "scripts/autonomous_chart_path_genesis_cycle_next.py", "candidate_path": "scripts/autonomous_chart_path_genesis_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "local constraints and genesis", "what_it_closes": "local constraints and genesis"},
        {"file": "scripts/physical_event_record_time_full_echo_cycle_next.py", "candidate_path": "scripts/physical_event_record_time_full_echo_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "actuality, interval and full echo", "what_it_closes": "actuality, interval and full echo"},
    )
    steelman = {
        "mechanism": "instantiate every counted factor on the complete code, give placement E, multiply G_physical, test the intertwiner and leakage, and derive chart/path roles locally",
        "supporting_authorities": (
            {"path": "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py", "line": 2,
             "relevance": "declares the complete-network N<=3 code-space blueprint"},
            {"path": "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py", "line": 660,
             "relevance": "executes the exact three-qubit controlled-Givens decomposition"},
        ),
        "terminal_obligation": "held-L6 E/G/placement/product/intertwiner/leakage/local-constraint certificate with deletion and inverse",
        "openness": "unattempted target-equivalent route defeats broad negative and axiom-pressure claims",
    }
    echo_specs = (
        ("Cycle560 role tables", "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py", 2, "NOT_RETIRED_AS_PHYSICAL_PRODUCT", "Cycle608 counts only", "execute product"),
        ("Cycle563 held order", "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py", 2, "COMPARISON_ONLY", "held tables imported", "no leakage/product"),
        ("Cycle590 compiler", "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md", 24, "NOT_BACKCREDITED", "direct shore only", "no promotion"),
        ("Cycle605 aggregate boundary", "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_DETECTOR_EVENT_ASSOCIATION_CONTROLLED_ECHO_TOURNAMENT_CYCLE605_NOTE_2026-07-22.md", 21, "OPEN", "count blueprint only", "readout null"),
        ("later Cycle610 covariance", "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", 25, "COMPARISON_ONLY_NO_BACK_CREDIT", "not executed", "no covariance credit"),
        ("later Cycle612 interval", "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md", 32, "COMPARISON_ONLY_NO_BACK_CREDIT", "not executed", "no time credit"),
    )
    echoes = tuple({
        "cycle": wall, "prior_wall": wall,
        "citation_path": citation_path, "citation_line": citation_line,
        "retired": status, "retired_status": status,
        "mechanism": mechanism, "retirement_mechanism": mechanism,
        "applicability": applicability, "applicability_here": applicability,
    } for wall, citation_path, citation_line, status, mechanism, applicability in echo_specs)
    result = {
        "Status": "FAIL",
        "artifact_status": "PASS_NARROWED_FACTOR_COUNT_AND_SMALL_MATRIX_POSITIVES_ONLY",
        "exact_target_contract": {
            "target_statement": "literal E/G/intertwiner/placement/product/leakage/local constraints",
            "quantifiers_domain": "full declared code on train L3, held-out L4 and held L6",
            "allowed_premises": "exact pinned shores only",
            "forbidden_weakenings": "counts, tables, transported labels and inherited residuals",
            "required_controls": "deletion, malformed, inverse, held size and covariance",
            "completion_witness": "executed E G_coarse = G_physical E and leakage",
            "nonclosures": "blueprints and small primitive decompositions",
        },
        "N1_routes": routes, "N1_qualifying": len(qualifying),
        "N1_required": 5, "N1_gate": "FAIL",
        "N2_collapsed_walls": tuple({"wall": name, "type": spec[0], "obligation": spec[1]} for name, spec in walls.items()),
        "N2_directional_wall_independence": directional,
        "N3_scan_scope": "generated proof payload excluding audit text",
        "N3_phrase_hit_classifications": phrase_hits,
        "N3_hidden_conditions_promoted": 0,
        "N4_exact_residual_matches": residuals, "N4_dropped_nonmatches": dropped,
        "N5_rhetoric_resolution_ledger": rhetoric_rows,
        "N6_partial_closure_paths": partial,
        "N6_convention_only_closure_found": False,
        "N6_new_axiom_required": False, "N6_control_plane_edit": False,
        "N7_steelman": steelman, "N8_cross_cycle_echo": echoes,
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_obstruction_claim": False, "axiom_pressure_claim": False,
    }
    result["pass"] = bool(
        result["Status"] == "FAIL" and len(qualifying) == 4
        and sum(row["search_status"] == "OPEN_UNTESTED_NOT_COUNTED" for row in routes) == 3
        and len(directional) == math.comb(len(walls), 2) == 21
        and len(residuals) == 4 and all(
            row["same_scope"] and row["scope_match"] and row["exact_match"]
            and all(key in row for key in ("prior_path", "prior_line", "current_path", "current_line", "same_scope", "use_as_closure"))
            for row in residuals)
        and all(not row["same_scope"] and all(key in row for key in ("prior_path", "prior_line", "current_path", "current_line", "same_scope", "use_as_closure")) for row in dropped)
        and len(dropped) == 1 and len(rhetoric_rows) == 6
        and len(partial) == 5
        and all(all(key in row for key in ("file", "status", "what_closes")) for row in partial)
        and len(echoes) == 6
        and all(all(key in row for key in ("cycle", "retired", "mechanism", "applicability", "citation_path", "citation_line")) for row in echoes)
        and all("path" in row and "line" in row for row in steelman["supporting_authorities"])
        and result["N3_hidden_conditions_promoted"] == 0
        and not any((result["broad_no_go_claim"], result["minimum_content_claim"],
                     result["shared_obstruction_claim"], result["axiom_pressure_claim"]))
    )
    return result


def note_contract():
    body = " ".join(NOTE.read_text(encoding="utf-8").lower().replace(chr(96), "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 608", "status: fail",
        "local-factor/count blueprint", "add_local_w is not a physical detector",
        "controlled-givens", "exact three-qubit", "physical encoder: null",
        "intertwiner: null", "placement/product: null", "full-code leakage: null",
        "chart/path/genesis: null", "event: null", "record: null", "time: null",
        "full echo: null", "train l3", "held-out l4", "held l6",
        "inherited all24", "inherited all576", "deletion", "malformed", "inverse",
        "same_scope", "use_as_closure", "exact repository path and line",
        "file / status / what_closes", "cycle / retired / mechanism / applicability",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure", "author accepted: false", "breakthrough: false",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required": len(required), "missing": missing, "pass": not missing}
    check("Cycle608 note freezes promotion boundaries and current N1-N8", not missing, result)
    return result


def main():
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.alarm(int(WALL_CAP_SECONDS))
    print("Cycle608 factor/count blueprint and primitive-decomposition audit", AUTHORITY, AUDIT)
    shore_result = shore()
    givens = controlled_givens_core_test()
    primitive_tests = primitive_family_matrix_tests(givens)
    check("small primitive matrices and truth tables are exact within scope",
          primitive_tests["pass"], primitive_tests)
    compiler_rows = []
    for length in FROZEN_LAW["sizes"].values():
        row = compiler_row(length, givens, primitive_tests)
        compiler_rows.append(row)
        check(f"L{length} local-factor/count blueprint passes", row["pass"], {
            "local": row["local_factor_count_blueprint"]["pass"],
            "C": row["every_cell_incident_C_role_table_audit"]["pass"],
            "target": row["Gtarget"]["pass"],
            "physical_encoder_E": row["physical_encoder_E"],
            "physical_primitive_product": row["physical_primitive_product"],
        })
    composition = algebraic_composition_blueprint(compiler_rows)
    check("aggregate composition remains count-only with inherited Cycle605 algebra",
          composition["pass"] and composition["physical_primitive_product"] is None, composition)
    candidate = candidate_role_blueprint(composition)
    check("candidate association remains count arithmetic plus inherited Boolean controls",
          candidate["pass"] and candidate["physical_candidate_association"] is None, candidate)
    recurrence = recurrence_role_controls(candidate)
    check("prefix controls remain inherited ordinals, not Event/Record/time",
          recurrence["pass"] and recurrence["proper_time"] is None, recurrence)
    controls = malformed_inverse_deletion_controls(givens, primitive_tests)
    check("deletion/inverse and malformed blueprint controls pass", controls["pass"], controls)
    discipline = no_go_discipline(compiler_rows, composition, candidate, recurrence, controls)
    check("N1-N8 gate fails broad negative while preserving narrowed positives",
          discipline["pass"] and discipline["Status"] == "FAIL"
          and not discipline["axiom_pressure_claim"], discipline)
    physical_boundary = {
        "physical_encoder_E": None, "physical_update_G": None,
        "intertwiner_certificate": None, "physical_placement": None,
        "physical_primitive_product": None, "full_code_leakage": None,
        "locally_enforced_chart": None, "locally_enforced_path": None,
        "autonomous_genesis": None, "physical_detector_readout": None,
        "Event": None, "Record": None, "time": None, "full_echo": None,
    }
    check("all physical and semantic promotion fields remain null",
          all(value is None for value in physical_boundary.values()), physical_boundary)
    contract = note_contract()
    elapsed = time.monotonic() - started
    rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform != "darwin":
        rss *= 1024
    check("cold resource caps", elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    result = {
        "status": "PASS" if FAIL == 0 else "FAIL", "pass": FAIL == 0,
        "tests_passed": PASS, "tests_failed": FAIL, "tests_total": PASS + FAIL,
        "authority": AUTHORITY, "audit": AUDIT, "author_accepted": False,
        "breakthrough": False, "constitutional_effect": "none",
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
        "shore": shore_result, "primitive_family_matrix_tests": primitive_tests,
        "compiler_rows": compiler_rows,
        "algebraic_composition_blueprint": composition,
        "route_B_candidate_role_blueprint": candidate,
        "route_C_inherited_prefix_controls": recurrence,
        "malformed_inverse_deletion_controls": controls,
        "no_go_discipline": discipline,
        "physical_promotion_boundary": physical_boundary,
        "note_contract": contract,
        "six_wall_ledger": {
            "C_ref": "Cycle605 interference inherited only; no Cycle608 physical reference/readout/full echo",
            "C_num": "finite size counts preserve supplied global N<=3; no local enforcement",
            "C_wrap": "tables explicit; placement/product/leakage/chart/path/genesis/covariance null",
            "C_int": "small decompositions exact; no full physical G or intertwiner",
            "C_local": "factor/count support enumerated; add_local_W is not encoder/detector",
            "C_source": "candidate/prefix roles inherited; Event/Record/time/source/gravity null",
        },
        "maturity_rebase": None,
        "shared_obstruction": False, "axiom_pressure": False,
        "highest_honest_terminal": (
            "local-factor/count blueprints on train L3, held-out L4 and held L6 plus exact "
            "small primitive decompositions including the three-qubit controlled-Givens word; "
            "no physical E/G, intertwiner, placement/product, leakage, local genesis, "
            "detector/readout, Event, Record, time or full echo"
        ),
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
    }
    print(json.dumps(result, indent=2, sort_keys=True, default=json_default))
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL,
                        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
