#!/usr/bin/env python3
"""Independent adversary for the companion-bank input package.

The three primary runners are read only as specification data and are never
imported.  This checker independently rebuilds the companion-bank row family,
the six-qubit exchange port, transported seam classes, private duals, and one
finite A/B/C/D liveness schedule.  It has authority none and audit unset.  It
does not promote the separate route census into a route-expanded circuit or
the staged prefix checks into a composite-channel identity.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
from copy import copy
from dataclasses import dataclass
from hashlib import sha256
import importlib
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import sys
from time import perf_counter
from typing import Iterable

import numpy as np


AUDIT_TIMEOUT_SEC = 900
PRIMARY_SPEC_PATHS = (
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_companion_bank_even_exchange_port_2026_07_28.py",
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_companion_three_route_independent_adversary_2026_07_27.py",
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_companion_bank_even_exchange_port_2026_07_28.py",
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

TOP_LEVEL_BLOCKLIST = {
    "frontier_companion_bank_bell_character_dilation_2026_07_28",
    "frontier_companion_bank_even_exchange_port_2026_07_28",
    "frontier_companion_bank_epoch_liveness_2026_07_28",
}
TOL = 4.0e-10

M = U = F = O = R = Q = T = P = V = None
Pauli = object


def load_dependencies(source_root: Path) -> None:
    """Load only lower-level Cycle-720 construction dependencies."""
    global M, U, F, O, R, Q, T, P, V, Pauli
    scripts = (source_root / "scripts").resolve()
    if not scripts.is_dir():
        raise SystemExit(f"missing scripts directory: {scripts}")
    sys.path.insert(0, str(scripts))
    names = {
        "M": "frontier_cycle720_cell_majorana_companion_geometry_2026_07_27",
        "U": "frontier_cycle720_companion_subsystem_m2_update_2026_07_27",
        "F": "frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27",
        "O": "frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27",
        "R": "frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27",
        "Q": "frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27",
        "T": "frontier_cycle708_endpoint_cube_tableau_core_2026_07_26",
        "P": "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27",
        "V": "frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27",
    }
    loaded = {key: importlib.import_module(name) for key, name in names.items()}
    M, U, F, O, R, Q, T, P, V = (
        loaded[key] for key in ("M", "U", "F", "O", "R", "Q", "T", "P", "V")
    )
    Pauli = M.Pauli
    forbidden = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    if forbidden:
        raise AssertionError(
            f"companion-bank primary imported transitively: {forbidden}"
        )


def declared_conventions(source_root: Path) -> dict[str, object]:
    """Parse only module docstrings from the three blocked runner files."""
    docstrings = {}
    digests = {}
    for relative in PRIMARY_SPEC_PATHS:
        body = (source_root / relative).read_text()
        doc = ast.get_docstring(ast.parse(body), clean=False) or ""
        name = Path(relative).stem
        docstrings[name] = doc
        digests[name] = sha256(doc.encode()).hexdigest()
    f1 = docstrings[Path(PRIMARY_SPEC_PATHS[0]).stem]
    f2 = docstrings[Path(PRIMARY_SPEC_PATHS[1]).stem]
    f3 = docstrings[Path(PRIMARY_SPEC_PATHS[2]).stem]
    return {
        "docstring_sha256": digests,
        "bell_character_declares_code_0_q": "``[0, q)``" in f1,
        "bell_character_declares_bank_q_2q": "``[q, 2q)``" in f1,
        "bell_character_declares_H_CP_H": (
            "``H(a); controlled local Pauli letters; H(a)``" in f1
        ),
        "bell_character_declares_fixed_X_and_character_Z": (
            "``X(a)`` is fixed" in f1
            and "``Z(a)`` is transported" in f1
        ),
        "even_exchange_port_declares_one_six_mode_live_bank": (
            "a six-mode live input\nbank" in f2
            or "six-mode live input bank" in f2
        ),
        "even_exchange_port_declares_colocation": "co-located" in f2,
        "epoch_liveness_declares_literal_slot_walk": "literal slot walk" in f3,
        "epoch_liveness_declares_stage_components": all(
            token in f3
            for token in (
                "tree/plaquette Choi pump",
                "retained Bell",
                "routed recurrent word",
            )
        ),
        "derived_bell_character_range_formula": "[q,2q)",
        "derived_even_exchange_port_range_formula": "[q,q+6)",
        "derivation": (
            "bell_character states its q-wide mirror range literally.  even_exchange_port declares one "
            "six-mode bank, and the code register ends at q, so its separate "
            "bank occupies the next six registers [q,q+6)."
        ),
    }


@dataclass(frozen=True)
class IntPauli:
    """Independent i^phase X^x Z^z integer Pauli representation."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def fields(self) -> tuple[int, int, int]:
        return self.phase % 4, self.x, self.z


@dataclass(frozen=True)
class CliffordGate:
    kind: str
    first: int
    second: int = -1
    target_pauli: IntPauli = IntPauli()


def ip(row) -> IntPauli:
    return IntPauli(int(row.phase) % 4, int(row.x), int(row.z))


def pauli_multiply(left: IntPauli, right: IntPauli) -> IntPauli:
    """Multiply in i^p X^x Z^z order, including the exact mod-four phase."""
    phase = (
        left.phase
        + right.phase
        + 2 * (left.z & right.x).bit_count()
    ) % 4
    return IntPauli(phase, left.x ^ right.x, left.z ^ right.z)


def pauli_product(rows: Iterable[IntPauli]) -> IntPauli:
    output = IntPauli()
    for row in rows:
        output = pauli_multiply(output, row)
    return output


def signed_single(qubit: int, letter: str) -> IntPauli:
    if letter == "X":
        return IntPauli(x=1 << qubit)
    if letter == "Z":
        return IntPauli(z=1 << qubit)
    if letter == "Y":
        return IntPauli(phase=1, x=1 << qubit, z=1 << qubit)
    if letter == "I":
        return IntPauli()
    raise ValueError(letter)


def anticommutator_bit(left: IntPauli, right: IntPauli) -> int:
    return (
        (left.x & right.z).bit_count()
        + (left.z & right.x).bit_count()
    ) & 1


def _generator_after_gate(
    gate: CliffordGate, qubit: int, x_generator: bool
) -> IntPauli:
    base = IntPauli(
        x=(1 << qubit) if x_generator else 0,
        z=0 if x_generator else (1 << qubit),
    )
    if gate.kind == "H":
        if qubit != gate.first:
            return base
        return IntPauli(
            z=1 << qubit
        ) if x_generator else IntPauli(x=1 << qubit)
    if gate.kind == "CNOT":
        control, target = gate.first, gate.second
        if x_generator and qubit == control:
            return IntPauli(x=(1 << control) | (1 << target))
        if not x_generator and qubit == target:
            return IntPauli(z=(1 << control) | (1 << target))
        return base
    if gate.kind == "CZ":
        left, right = gate.first, gate.second
        if x_generator and qubit == left:
            return IntPauli(x=1 << left, z=1 << right)
        if x_generator and qubit == right:
            return IntPauli(x=1 << right, z=1 << left)
        return base
    if gate.kind == "CP":
        control = gate.first
        if qubit == control:
            if x_generator:
                return pauli_multiply(
                    IntPauli(x=1 << control), gate.target_pauli
                )
            return base
        if anticommutator_bit(base, gate.target_pauli):
            return pauli_multiply(
                IntPauli(z=1 << control), base
            )
        return base
    raise ValueError(gate.kind)


def conjugate_gate(row: IntPauli, gate: CliffordGate) -> IntPauli:
    """Rebuild a Clifford image from independently derived generator images."""
    output = IntPauli(row.phase % 4)
    bits = row.x
    while bits:
        low = bits & -bits
        output = pauli_multiply(
            output,
            _generator_after_gate(gate, low.bit_length() - 1, True),
        )
        bits ^= low
    bits = row.z
    while bits:
        low = bits & -bits
        output = pauli_multiply(
            output,
            _generator_after_gate(gate, low.bit_length() - 1, False),
        )
        bits ^= low
    return output


def conjugate_word(
    row: IntPauli, word: Iterable[CliffordGate]
) -> IntPauli:
    output = row
    for gate in word:
        output = conjugate_gate(output, gate)
    return output


def dense_pauli(row: IntPauli, width: int) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    x_matrix = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z_matrix = np.asarray(((1, 0), (0, -1)), dtype=complex)
    output = np.asarray(((1,),), dtype=complex)
    for qubit in reversed(range(width)):
        local = identity
        if (row.x >> qubit) & 1:
            local = local @ x_matrix
        if (row.z >> qubit) & 1:
            local = local @ z_matrix
        output = np.kron(output, local)
    return (1j ** (row.phase % 4)) * output


def dense_gate(gate: CliffordGate, width: int) -> np.ndarray:
    dimension = 1 << width
    if gate.kind == "H":
        return (
            dense_pauli(IntPauli(x=1 << gate.first), width)
            + dense_pauli(IntPauli(z=1 << gate.first), width)
        ) / math.sqrt(2)
    if gate.kind == "CNOT":
        output = np.zeros((dimension, dimension), dtype=complex)
        for basis in range(dimension):
            image = basis
            if (basis >> gate.first) & 1:
                image ^= 1 << gate.second
            output[image, basis] = 1
        return output
    if gate.kind == "CZ":
        output = np.eye(dimension, dtype=complex)
        for basis in range(dimension):
            if (
                ((basis >> gate.first) & 1)
                and ((basis >> gate.second) & 1)
            ):
                output[basis, basis] = -1
        return output
    if gate.kind == "CP":
        identity = np.eye(dimension, dtype=complex)
        z_control = dense_pauli(
            IntPauli(z=1 << gate.first), width
        )
        p0 = (identity + z_control) / 2
        p1 = (identity - z_control) / 2
        return p0 + p1 @ dense_pauli(gate.target_pauli, width)
    raise ValueError(gate.kind)


def dense_integer_pauli_certificate() -> dict[str, object]:
    """All signed weight-one/two rows against every three-qubit gate instance."""
    rows = []
    for letters in product(("I", "X", "Y", "Z"), repeat=3):
        weight = sum(letter != "I" for letter in letters)
        if weight not in (1, 2):
            continue
        canonical = pauli_product(
            signed_single(qubit, letter)
            for qubit, letter in enumerate(letters)
            if letter != "I"
        )
        rows.extend(
            IntPauli(
                (canonical.phase + phase) % 4,
                canonical.x,
                canonical.z,
            )
            for phase in range(4)
        )

    gates = [
        CliffordGate("H", qubit) for qubit in range(3)
    ]
    gates.extend(
        CliffordGate("CNOT", control, target)
        for control in range(3)
        for target in range(3)
        if control != target
    )
    gates.extend(
        CliffordGate("CZ", left, right)
        for left, right in combinations(range(3), 2)
    )
    for control in range(3):
        targets = tuple(qubit for qubit in range(3) if qubit != control)
        for letters in product(("I", "X", "Y", "Z"), repeat=2):
            if letters == ("I", "I"):
                continue
            target = pauli_product(
                signed_single(qubit, letter)
                for qubit, letter in zip(targets, letters)
                if letter != "I"
            )
            gates.append(
                CliffordGate("CP", control, target_pauli=target)
            )

    mismatches = 0
    maximum_residual = 0.0
    for gate in gates:
        unitary = dense_gate(gate, 3)
        for row in rows:
            actual = dense_pauli(conjugate_gate(row, gate), 3)
            expected = (
                unitary @ dense_pauli(row, 3) @ unitary.conj().T
            )
            residual = float(np.max(np.abs(actual - expected)))
            maximum_residual = max(maximum_residual, residual)
            mismatches += residual > TOL
    return {
        "signed_weight_1_or_2_rows": len(rows),
        "H_instances": 3,
        "CNOT_instances": 6,
        "CZ_instances": 3,
        "controlled_Pauli_instances": 45,
        "gate_instances": len(gates),
        "comparisons": len(rows) * len(gates),
        "mismatches": mismatches,
        "maximum_dense_residual": maximum_residual,
    }


def fixture_222():
    return O.arbitrary_fixture(Q.shape_cells((2, 2, 2)))


def physical_cell(fixture, qubit: int) -> int:
    if qubit < fixture.matter_qubits:
        return qubit // 6
    if qubit < fixture.qubits:
        return (qubit - fixture.matter_qubits) // 3
    raise ValueError(f"physical qubit outside fixture: {qubit}")


def support_indices(row) -> tuple[int, ...]:
    mask = int(row.x) | int(row.z)
    output = []
    while mask:
        low = mask & -mask
        output.append(low.bit_length() - 1)
        mask ^= low
    return tuple(output)


def support_diameter(cells: Iterable[tuple[int, int, int]]) -> int:
    cells = tuple(cells)
    return max(
        (
            sum(abs(a - b) for a, b in zip(left, right))
            for left in cells for right in cells
        ),
        default=0,
    )


def six_swap_word(bank_base: int, matter_base: int) -> tuple[CliffordGate, ...]:
    gates = []
    for mode in range(6):
        bank, matter = bank_base + mode, matter_base + mode
        gates.extend((
            CliffordGate("CNOT", bank, matter),
            CliffordGate("CNOT", matter, bank),
            CliffordGate("CNOT", bank, matter),
        ))
    return tuple(gates)


def replace_port_matter(
    row: IntPauli, fixture, port: int, bank_base: int
) -> IntPauli:
    x, z = row.x, row.z
    for mode in range(6):
        matter = 1 << (6 * port + mode)
        bank = 1 << (bank_base + mode)
        if x & matter:
            x ^= matter | bank
        if z & matter:
            z ^= matter | bank
    return IntPauli(row.phase, x, z)


def exchange_port_certificate(
    conventions: dict[str, object],
) -> dict[str, object]:
    fixture = fixture_222()
    q = fixture.qubits
    port = fixture.cells.index(min(fixture.cells))
    bank_base = q
    word = six_swap_word(bank_base, 6 * port)
    cell_mask = sum(
        1 << (6 * port + mode) for mode in range(6)
    ) | sum(
        1 << (fixture.matter_qubits + 3 * port + axis)
        for axis in range(3)
    )
    dictionary = tuple(M.operator_rows(fixture))
    local_rows = tuple(
        ip(physical)
        for family, physical, _target in dictionary
        if family in ("onsite_B", "onsite_even")
        and (int(physical.x) | int(physical.z))
        and not ((int(physical.x) | int(physical.z)) & ~cell_mask)
    )
    forward_failures = reverse_failures = 0
    for physical in local_rows:
        bank = replace_port_matter(
            physical, fixture, port, bank_base
        )
        forward_failures += (
            conjugate_word(bank, word).fields() != physical.fields()
        )
        reverse_failures += (
            conjugate_word(physical, word).fields() != bank.fields()
        )

    affected_failures = unaffected_failures = 0
    for _family, physical_pauli, _target in dictionary:
        physical = ip(physical_pauli)
        actual = conjugate_word(physical, word)
        if (physical.x | physical.z) & sum(
            1 << (6 * port + mode) for mode in range(6)
        ):
            expected = replace_port_matter(
                physical, fixture, port, bank_base
            )
            affected_failures += actual.fields() != expected.fields()
        else:
            unaffected_failures += actual.fields() != physical.fields()

    matter_parity = sum(
        1 << (6 * port + mode) for mode in range(6)
    )
    companion_parity = sum(
        1 << (fixture.matter_qubits + 3 * port + axis)
        for axis in range(3)
    )
    bank_parity = sum(1 << (bank_base + mode) for mode in range(6))
    cell_parity = IntPauli(z=matter_parity | companion_parity)
    joint_parity = IntPauli(
        z=matter_parity | companion_parity | bank_parity
    )
    expected_cell = IntPauli(z=bank_parity | companion_parity)
    odd_detection_failures = 0
    odd_image_detection_failures = 0
    for mode in range(6):
        odd = IntPauli(x=1 << (bank_base + mode))
        odd_detection_failures += (
            anticommutator_bit(odd, joint_parity) != 1
        )
        odd_image_detection_failures += (
            anticommutator_bit(
                conjugate_word(odd, word), joint_parity
            ) != 1
        )

    touched_cells = {
        fixture.cells[port]
        for gate in word
        for qubit in (gate.first, gate.second)
        if qubit >= 0
    }
    dense = dense_integer_pauli_certificate()
    return {
        "shape": (2, 2, 2),
        "q": q,
        "bell_character_docstring_range": (q, 2 * q),
        "even_exchange_port_derived_six_qubit_range": (q, q + 6),
        "convention_evidence_pass": all((
            conventions["bell_character_declares_code_0_q"],
            conventions["bell_character_declares_bank_q_2q"],
            conventions["even_exchange_port_declares_one_six_mode_live_bank"],
            conventions["even_exchange_port_declares_colocation"],
        )),
        "six_SWAP_blocks": len(word) // 3,
        "CNOT_primitives": len(word),
        "port_dictionary_rows": len(local_rows),
        "forward_dictionary_exchange_failures": forward_failures,
        "reverse_dictionary_exchange_failures": reverse_failures,
        "all_affected_dictionary_exchange_failures": affected_failures,
        "unaffected_dictionary_invariance_failures": unaffected_failures,
        "cell_parity_image_failures": (
            conjugate_word(cell_parity, word).fields()
            != expected_cell.fields()
        ),
        "joint_parity_invariance_failures": (
            conjugate_word(joint_parity, word).fields()
            != joint_parity.fields()
        ),
        "odd_bank_detection_failures": odd_detection_failures,
        "odd_image_detection_failures": odd_image_detection_failures,
        "support_cells": len(touched_cells),
        "support_diameter": support_diameter(touched_cells),
        "dense_integer_Pauli_selftest": dense,
    }


def gf2_rank(rows: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def symplectic_int(left: IntPauli, right: IntPauli) -> int:
    return (
        (left.x & right.z).bit_count()
        + (left.z & right.x).bit_count()
    ) & 1


def canonical_pauli(x: int, z: int):
    return Pauli((x & z).bit_count() & 1, x, z)


def tag_physical_row(fixture, tag):
    if tag[0] == "onsite_Z":
        return Pauli(z=1 << (6 * tag[1] + tag[2]))
    if tag[0] == "onsite_XX":
        left = 6 * tag[1] + tag[2]
        return Pauli(x=(1 << left) | (1 << (left + 1)))
    if tag[0] == "edge":
        return fixture.physical_terms(tag[1])[2]
    raise ValueError(tag)


def rebuilt_companion_rows(fixture):
    graph, tags = P.direct_graph_basis(fixture)
    q = fixture.qubits
    mask = (1 << q) - 1
    rows = []
    restriction_failures = 0
    for graph_row, tag in zip(graph, tags):
        code = canonical_pauli(
            int(graph_row.x) & mask, int(graph_row.z) & mask
        )
        physical = tag_physical_row(fixture, tag)
        restriction_failures += (
            ip(code).fields() != ip(physical).fields()
        )
        x = int(code.x) | (int(physical.x) << q)
        z = int(code.z) | (int(physical.z) << q)
        rows.append(canonical_pauli(x, z))
    return tuple(graph), tuple(tags), tuple(rows), restriction_failures


def tag_anchor(fixture, tag) -> tuple[int, int, int]:
    if tag[0].startswith("onsite"):
        return fixture.cells[tag[1]]
    if tag[0] not in ("edge", "tree", "plaquette"):
        raise ValueError(f"unsupported scheduled tag: {tag!r}")
    left, right, owner, *_rest = fixture.edges[tag[1]]
    anchor = fixture.cells[owner] if isinstance(owner, int) else tuple(owner)
    if anchor not in (fixture.cells[left], fixture.cells[right]):
        raise AssertionError("edge anchor is not an endpoint")
    return anchor


def doubled_row_cells(fixture, row) -> frozenset[tuple[int, int, int]]:
    q = fixture.qubits
    cells = set()
    for qubit in support_indices(row):
        local = qubit if qubit < q else qubit - q
        cells.add(fixture.cells[physical_cell(fixture, local)])
    return frozenset(cells)


def dilation_certificate() -> dict[str, object]:
    fixture = fixture_222()
    graph, tags, rows, restriction_failures = rebuilt_companion_rows(
        fixture
    )
    q = fixture.qubits
    graph_width = q + fixture.matter_qubits
    compiled_width = 2 * q
    commutator_failures = sum(
        symplectic_int(ip(left), ip(right))
        for index, left in enumerate(rows)
        for right in rows[:index]
    )
    x_failures = z_failures = 0
    support_failures = 0
    maximum_cells = maximum_diameter = 0
    support_census = Counter()
    for index, (tag, row) in enumerate(zip(tags, rows)):
        ancilla = 2 * q + index
        target = ip(row)
        word = (
            CliffordGate("H", ancilla),
            CliffordGate("CP", ancilla, target_pauli=target),
            CliffordGate("H", ancilla),
        )
        x_ancilla = IntPauli(x=1 << ancilla)
        z_ancilla = IntPauli(z=1 << ancilla)
        expected_z = pauli_multiply(z_ancilla, target)
        x_failures += (
            conjugate_word(x_ancilla, word).fields()
            != x_ancilla.fields()
        )
        z_failures += (
            conjugate_word(z_ancilla, word).fields()
            != expected_z.fields()
        )
        cells = set(doubled_row_cells(fixture, row))
        cells.add(tag_anchor(fixture, tag))
        diameter = support_diameter(cells)
        support_census[(len(cells), diameter)] += 1
        maximum_cells = max(maximum_cells, len(cells))
        maximum_diameter = max(maximum_diameter, diameter)
        support_failures += len(cells) > 2 or diameter > 1
    return {
        "shape": (2, 2, 2),
        "rows": len(rows),
        "physical_restriction_tag_rebuild_failures": restriction_failures,
        "compiled_commutator_failures": commutator_failures,
        "graph_rank": gf2_rank(
            int(row.symplectic(graph_width)) for row in graph
        ),
        "compiled_rank": gf2_rank(
            int(row.symplectic(compiled_width)) for row in rows
        ),
        "dilation_X_invariance_failures": x_failures,
        "dilation_Z_character_failures": z_failures,
        "support_gate_failures": support_failures,
        "maximum_compiled_support_cells": maximum_cells,
        "maximum_compiled_support_diameter": maximum_diameter,
        "per_row_support_census": tuple(
            {
                "support_cells": cells,
                "support_diameter": diameter,
                "rows": count,
            }
            for (cells, diameter), count in sorted(
                support_census.items()
            )
        ),
    }


def solve_binary(equations: Iterable[tuple[int, int]]) -> tuple[int, int]:
    pivots: dict[int, tuple[int, int]] = {}
    contradictions = 0
    for original_mask, original_rhs in equations:
        mask, rhs = int(original_mask), int(original_rhs) & 1
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                old_mask, old_rhs = pivots[pivot]
                mask ^= old_mask
                rhs ^= old_rhs
            else:
                pivots[pivot] = (mask, rhs)
                break
        else:
            contradictions += rhs
    solution = 0
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        other = mask & ~(1 << pivot)
        value = rhs ^ ((other & solution).bit_count() & 1)
        solution |= value << pivot
    return solution, contradictions


def solve_private_dual(rows, target: int, allowed: tuple[int, ...]):
    equations = []
    for index, stabilizer in enumerate(rows):
        mask = 0
        for variable, qubit in enumerate(allowed):
            mask |= (
                (int(stabilizer.z) >> qubit) & 1
            ) << (2 * variable)
            mask |= (
                (int(stabilizer.x) >> qubit) & 1
            ) << (2 * variable + 1)
        equations.append((mask, int(index == target)))
    solution, contradictions = solve_binary(equations)
    x = sum(
        ((solution >> (2 * variable)) & 1) << qubit
        for variable, qubit in enumerate(allowed)
    )
    z = sum(
        ((solution >> (2 * variable + 1)) & 1) << qubit
        for variable, qubit in enumerate(allowed)
    )
    return canonical_pauli(x, z), contradictions


def one_cell_allowed_sets(fixture, tag) -> tuple[tuple[int, ...], ...]:
    q = fixture.qubits
    m = fixture.matter_qubits
    if tag[0] != "edge":
        cells = (tag[1],)
        include_full = True
    else:
        left, right, *_rest = fixture.edges[tag[1]]
        cells = (left, right)
        include_full = False
    output = []
    for cell in cells:
        if include_full:
            allowed = tuple(
                range(6 * cell, 6 * cell + 6)
            ) + tuple(
                range(m + 3 * cell, m + 3 * cell + 3)
            ) + tuple(
                range(q + 6 * cell, q + 6 * cell + 6)
            )
        else:
            allowed = tuple(
                range(m + 3 * cell, m + 3 * cell + 3)
            )
        output.append(allowed)
    return tuple(output)


def graph_row_cells(fixture, row) -> frozenset[tuple[int, int, int]]:
    q = fixture.qubits
    m = fixture.matter_qubits
    cells = set()
    for qubit in support_indices(row):
        if qubit < m:
            cell = qubit // 6
        elif qubit < q:
            cell = (qubit - m) // 3
        elif qubit < q + m:
            cell = (qubit - q) // 6
        else:
            raise AssertionError("private dual escaped graph width")
        cells.add(fixture.cells[cell])
    return frozenset(cells)


def atlas_correction_certificate() -> dict[str, object]:
    fixture = fixture_222()
    graph, tags = P.direct_graph_basis(fixture)
    total = fixture.qubits + fixture.matter_qubits
    atlas = {}
    no_one_cell_solution = 0
    solve_contradictions = 0
    for target, tag in enumerate(tags):
        chosen = None
        for allowed in one_cell_allowed_sets(fixture, tag):
            candidate, contradictions = solve_private_dual(
                graph, target, allowed
            )
            syndrome = tuple(
                symplectic_int(ip(candidate), ip(row))
                for row in graph
            )
            if not contradictions and syndrome == tuple(
                int(index == target) for index in range(len(graph))
            ):
                chosen = candidate
                break
            solve_contradictions += contradictions
        if chosen is None:
            no_one_cell_solution += 1
            chosen = canonical_pauli(0, 0)
        atlas[tag] = chosen

    one_hot_failures = 0
    support_failures = 0
    maximum_cells = 0
    for target, tag in enumerate(tags):
        correction = atlas[tag]
        one_hot_failures += sum(
            symplectic_int(ip(correction), ip(stabilizer))
            != int(index == target)
            for index, stabilizer in enumerate(graph)
        )
        cells = graph_row_cells(fixture, correction)
        maximum_cells = max(maximum_cells, len(cells))
        support_failures += len(cells) > 1
    return {
        "shape": (2, 2, 2),
        "graph_width": total,
        "graph_rows": len(graph),
        "graph_rank": gf2_rank(
            int(row.symplectic(total)) for row in graph
        ),
        "atlas_entries": len(atlas),
        "solve_contradictions": solve_contradictions,
        "rows_without_one_cell_solution": no_one_cell_solution,
        "one_hot_duality_failures": one_hot_failures,
        "one_cell_support_failures": support_failures,
        "maximum_private_dual_support_cells": maximum_cells,
    }


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = np.zeros((3, 3), dtype=int)
            for target_axis, source_axis in enumerate(permutation):
                frame[target_axis, source_axis] = signs[target_axis]
            if round(float(np.linalg.det(frame))) == 1:
                frames.append(frame)
    if len(frames) != 24:
        raise AssertionError("proper cubic frame census is not 24")
    return tuple(frames)


def affine_cell(cell, frame, shift) -> tuple[int, int, int]:
    return tuple(
        int(value)
        for value in (
            frame @ np.asarray(cell, dtype=int)
            + np.asarray(shift, dtype=int)
        )
    )


def apply_physical_images(row, images) -> IntPauli:
    x_images, z_images = images
    output = IntPauli(int(row.phase) % 4)
    bits = int(row.x)
    while bits:
        low = bits & -bits
        output = pauli_multiply(
            output, ip(x_images[low.bit_length() - 1])
        )
        bits ^= low
    bits = int(row.z)
    while bits:
        low = bits & -bits
        output = pauli_multiply(
            output, ip(z_images[low.bit_length() - 1])
        )
        bits ^= low
    return output


def reversed_physical_terms(fixture, edge_index: int) -> tuple:
    left, right, _owner, axis, left_mode, right_mode = (
        fixture.edges[edge_index]
    )
    reversed_record = (
        right,
        left,
        fixture.cells[right],
        axis,
        right_mode,
        left_mode,
    )
    reversed_fixture = copy(fixture)
    edges = list(fixture.edges)
    edges[edge_index] = reversed_record
    object.__setattr__(reversed_fixture, "edges", tuple(edges))
    return tuple(reversed_fixture.physical_terms(edge_index))


def transported_edge_index(
    source, source_edge: int, target, frame, shift
) -> int | None:
    left, right, *_rest = source.edges[source_edge]
    endpoints = frozenset((
        affine_cell(source.cells[left], frame, shift),
        affine_cell(source.cells[right], frame, shift),
    ))
    for edge_index, edge in enumerate(target.edges):
        if frozenset((
            target.cells[edge[0]], target.cells[edge[1]]
        )) == endpoints:
            return edge_index
    return None


def seam_class_certificate() -> dict[str, object]:
    source = fixture_222()
    frames = proper_cubic_frames()
    shifts = tuple(product((0, 1), repeat=3))
    forward_classes = reversed_classes = 0
    missing_edge_failures = 0
    zero_class_failures = double_class_failures = 0
    quadruples = 0
    first_failure = None
    for frame_index, frame in enumerate(frames):
        for shift in shifts:
            target = O.arbitrary_fixture(
                Q.affine_cells(source.cells, frame, shift)
            )
            images = Q.physical_images(source, target, frame, shift)
            for source_edge in range(len(source.edges)):
                quadruples += 1
                target_edge = transported_edge_index(
                    source, source_edge, target, frame, shift
                )
                if target_edge is None:
                    missing_edge_failures += 1
                    continue
                transported = tuple(
                    apply_physical_images(row, images)
                    for row in source.physical_terms(source_edge)
                )
                forward = tuple(
                    ip(row) for row in target.physical_terms(target_edge)
                )
                reversed_rows = tuple(
                    ip(row)
                    for row in reversed_physical_terms(
                        target, target_edge
                    )
                )
                matches = (
                    transported == forward,
                    transported == reversed_rows,
                )
                forward_classes += matches[0] and not matches[1]
                reversed_classes += matches[1] and not matches[0]
                zero_class_failures += not any(matches)
                double_class_failures += all(matches)
                if (
                    first_failure is None
                    and sum(bool(value) for value in matches) != 1
                ):
                    first_failure = {
                        "frame_index": frame_index,
                        "shift": shift,
                        "source_edge": source_edge,
                        "target_edge": target_edge,
                        "forward_match": bool(matches[0]),
                        "reversed_match": bool(matches[1]),
                    }
    return {
        "shape": (2, 2, 2),
        "proper_cubic_frames": len(frames),
        "translation_parities": len(shifts),
        "contexts": len(frames) * len(shifts),
        "transported_quadruples": quadruples,
        "forward_class_count": forward_classes,
        "reversed_class_count": reversed_classes,
        "missing_edge_failures": missing_edge_failures,
        "zero_class_failures": zero_class_failures,
        "double_class_failures": double_class_failures,
        "first_failure": first_failure,
        "transport_surface": "Q.affine_cells plus Q.physical_images",
        "reversed_surface": (
            "fixture.physical_terms after explicit endpoint/mode reordering"
        ),
    }


def greedy_layers(supports: Iterable[frozenset[int]]) -> tuple[int, ...]:
    occupied: list[set[int]] = []
    assignment = []
    for support in supports:
        for layer, used in enumerate(occupied):
            if not used.intersection(support):
                used.update(support)
                assignment.append(layer)
                break
        else:
            occupied.append(set(support))
            assignment.append(len(occupied) - 1)
    return tuple(assignment)


def merge_accesses(entries: Iterable[tuple[int, str]]) -> dict[int, str]:
    rank = {"read": 0, "write": 1}
    output: dict[int, str] = {}
    for register, mode in entries:
        if register not in output or rank[mode] > rank[output[register]]:
            output[register] = mode
    return output


def route_rails(
    fixture, route, rail_base: int
) -> tuple[int, ...]:
    lookup = {cell: index for index, cell in enumerate(fixture.cells)}
    return tuple(sorted({
        rail_base + lookup[cell]
        for transition in route
        for cell in transition
    }))


def independent_liveness_walk(
    slots: list[dict[str, object]],
    handoffs: set[tuple[str, str, int]],
) -> dict[str, object]:
    """Own literal owner walk; every ownership transfer needs a named edge."""
    owner: dict[int, str] = {}
    executed: set[str] = set()
    consumed: set[tuple[str, str, int]] = set()
    violations = []
    collision_count = 0
    touches = 0
    for slot_index, slot in enumerate(slots):
        claimed = {}
        for word in slot["words"]:
            for register in word["accesses"]:
                if register in claimed:
                    collision_count += 1
                    violations.append(
                        f"collision:slot={slot_index}:register={register}:"
                        f"{claimed[register]}:{word['id']}"
                    )
                else:
                    claimed[register] = word["id"]
        for word in slot["words"]:
            word_id = word["id"]
            for register, mode in word["accesses"].items():
                touches += 1
                previous = owner.get(register)
                if previous is None:
                    if mode == "read":
                        violations.append(
                            f"read_before_write:slot={slot_index}:"
                            f"register={register}:word={word_id}"
                        )
                elif previous != word_id:
                    edge = (previous, word_id, register)
                    if edge not in handoffs:
                        violations.append(
                            f"missing_handoff:slot={slot_index}:"
                            f"register={register}:{previous}->{word_id}"
                        )
                    elif previous not in executed:
                        violations.append(
                            f"handoff_before_producer:slot={slot_index}:"
                            f"register={register}:{previous}->{word_id}"
                        )
                    else:
                        consumed.add(edge)
                owner[register] = word_id
            executed.add(word_id)
    for producer, consumer, register in sorted(handoffs - consumed):
        violations.append(
            f"declared_handoff_unconsumed:register={register}:"
            f"{producer}->{consumer}"
        )
    return {
        "slots_walked": len(slots),
        "words_walked": sum(len(slot["words"]) for slot in slots),
        "register_touches": touches,
        "registers_seen": len(owner),
        "handoffs_declared": len(handoffs),
        "handoffs_consumed": len(consumed),
        "collision_count": collision_count,
        "ownership_or_handoff_violation_count": len(violations),
        "violations": tuple(violations[:30]),
    }


def declare_handoffs(
    slots: list[dict[str, object]],
) -> set[tuple[str, str, int]]:
    last: dict[int, str] = {}
    handoffs = set()
    for slot in slots:
        for word in slot["words"]:
            for register in word["accesses"]:
                if register in last and last[register] != word["id"]:
                    handoffs.add(
                        (last[register], word["id"], register)
                    )
                last[register] = word["id"]
    return handoffs


def row_route(fixture, row, anchor):
    support = set(P.pauli_cells(fixture, row))
    support.add(anchor)
    return P.returned_route(anchor, frozenset(support))


def epoch_liveness_certificate() -> dict[str, object]:
    fixture = fixture_222()
    root = min(fixture.cells)
    axis_order = (2, 1, 0)
    atlas = P.build_private_atlases()
    pump_rows, pump_tags, _pump_report = P.schedule_basis(
        fixture, root, axis_order
    )
    pump_corrections = tuple(
        P.schedule_correction(fixture, tag, atlas)
        for tag in pump_tags
    )
    graph, tags, coupling_rows, restriction_failures = (
        rebuilt_companion_rows(fixture)
    )
    corrections = tuple(
        P.correction_from_atlas(fixture, tag, atlas)
        for tag in tags
    )
    correction_supports = tuple(
        frozenset(support_indices(row)) for row in corrections
    )
    correction_assignment = greedy_layers(correction_supports)
    correction_order = tuple(sorted(
        range(len(corrections)),
        key=lambda index: (correction_assignment[index], index),
    ))

    placed = U.placement(fixture)
    physical_word, update_report = U.physical_word(fixture, placed)
    routed, route_report = U.c707.route_word(physical_word)
    q = fixture.qubits
    placed_sites = tuple(tuple(site) for site in placed["sites_by_qubit"])
    placed_lookup = {
        site: qubit for qubit, site in enumerate(placed_sites)
    }
    touched_sites = {
        tuple(site)
        for instruction in routed
        for site in instruction.sites
    }
    extra_sites = tuple(sorted(touched_sites - set(placed_lookup)))
    g_register = dict(placed_lookup)
    g_register.update(
        (site, 2 * q + index)
        for index, site in enumerate(extra_sites)
    )
    cursor = 2 * q + len(extra_sites)
    bell_base = cursor
    cursor += len(coupling_rows)
    pump_base = cursor
    cursor += len(pump_rows)
    rail_base = cursor
    cursor += len(fixture.cells)

    slots: list[dict[str, object]] = []
    stages = []
    routes = []

    def add_word(stage: str, word_id: str, entries) -> None:
        stages.append(stage)
        slots.append({
            "stage": stage,
            "words": [{
                "id": word_id,
                "stage": stage,
                "accesses": merge_accesses(entries),
            }],
        })

    add_word(
        "A",
        "A:clean_code_and_bank_supply",
        ((register, "write") for register in range(2 * q)),
    )

    for index, (row, tag, correction) in enumerate(
        zip(pump_rows, pump_tags, pump_corrections)
    ):
        syndrome = pump_base + index
        anchor = tag_anchor(fixture, tag)
        route = row_route(fixture, row, anchor)
        routes.append((f"A:pump_measure:{index}", anchor, route))
        add_word(
            "A",
            f"A:pump_measure:{index}",
            (
                *((register, "write") for register in support_indices(row)),
                (syndrome, "write"),
                *((register, "write") for register in route_rails(
                    fixture, route, rail_base
                )),
            ),
        )
        correction_route = row_route(fixture, correction, anchor)
        routes.append((
            f"A:pump_correction:{index}", anchor, correction_route
        ))
        add_word(
            "A",
            f"A:pump_correction:{index}",
            (
                *((register, "write") for register in support_indices(
                    correction
                )),
                (syndrome, "read"),
                *((register, "write") for register in route_rails(
                    fixture, correction_route, rail_base
                )),
            ),
        )

    for index, (tag, row) in enumerate(zip(tags, coupling_rows)):
        ancilla = bell_base + index
        anchor = tag_anchor(fixture, tag)
        cells = set(doubled_row_cells(fixture, row))
        cells.add(anchor)
        route = P.returned_route(anchor, frozenset(cells))
        routes.append((f"B:coupling:{index}", anchor, route))
        add_word(
            "B",
            f"B:coupling:{index}",
            (
                *((register, "write") for register in support_indices(row)),
                (ancilla, "write"),
                *((register, "write") for register in route_rails(
                    fixture, route, rail_base
                )),
            ),
        )

    for index in correction_order:
        correction = corrections[index]
        tag = tags[index]
        ancilla = bell_base + index
        anchor = tag_anchor(fixture, tag)
        route = row_route(fixture, correction, anchor)
        routes.append((f"C:correction:{index}", anchor, route))
        add_word(
            "C",
            f"C:correction:{index}",
            (
                *((register, "write") for register in support_indices(
                    correction
                )),
                (ancilla, "read"),
                *((register, "write") for register in route_rails(
                    fixture, route, rail_base
                )),
            ),
        )

    for index, instruction in enumerate(routed):
        add_word(
            "D",
            f"D:G:{index}",
            (
                (g_register[tuple(site)], "write")
                for site in instruction.sites
            ),
        )

    handoffs = declare_handoffs(slots)
    lawful = independent_liveness_walk(slots, handoffs)
    route_failures = Counter()
    for word_id, anchor, route in routes:
        forward, inverse = P.route_execution_failures(anchor, route)
        route_failures["forward"] += forward
        route_failures["inverse"] += inverse

    dropped_edge = next(
        edge for edge in sorted(handoffs)
        if edge[0].startswith("B:coupling:")
        and edge[1].startswith("C:correction:")
    )
    dropped_handoffs = set(handoffs)
    dropped_handoffs.remove(dropped_edge)
    dropped_walk = independent_liveness_walk(
        slots, dropped_handoffs
    )
    dropped_named = any(
        violation.startswith("missing_handoff:")
        and f"register={dropped_edge[2]}" in violation
        for violation in dropped_walk["violations"]
    )

    duplicate_index = next(
        index
        for index, slot in enumerate(slots)
        if slot["words"][0]["id"].startswith("B:coupling:")
    )
    duplicate_slots = list(slots)
    original = slots[duplicate_index]["words"][0]
    duplicate = {
        "id": f"{original['id']}:duplicate_owner",
        "stage": original["stage"],
        "accesses": dict(original["accesses"]),
    }
    duplicate_slots[duplicate_index] = {
        "stage": slots[duplicate_index]["stage"],
        "words": [original, duplicate],
    }
    duplicate_walk = independent_liveness_walk(
        duplicate_slots, handoffs
    )
    duplicate_named = any(
        violation.startswith("collision:")
        for violation in duplicate_walk["violations"]
    )

    stage_rank = {stage: index for index, stage in enumerate("ABCD")}
    stage_order_failures = sum(
        stage_rank[right] < stage_rank[left]
        for left, right in zip(stages, stages[1:])
    )
    correction_layer_sequence = tuple(
        correction_assignment[index] for index in correction_order
    )
    correction_layer_order_failures = sum(
        right < left
        for left, right in zip(
            correction_layer_sequence,
            correction_layer_sequence[1:],
        )
    )
    return {
        "shape": (2, 2, 2),
        "root": root,
        "axis_order": axis_order,
        "pump_rows": len(pump_rows),
        "pump_onsite_rows": sum(
            tag[0].startswith("onsite") for tag in pump_tags
        ),
        "pump_tree_rows": sum(tag[0] == "tree" for tag in pump_tags),
        "pump_fill_rows": sum(
            tag[0] == "plaquette" for tag in pump_tags
        ),
        "coupling_rows": len(coupling_rows),
        "coupling_physical_restriction_failures": restriction_failures,
        "coupling_graph_tag_order_failures": int(
            tuple(tags) != tuple(P.direct_graph_basis(fixture)[1])
        ),
        "correction_layers": (
            max(correction_assignment, default=-1) + 1
        ),
        "correction_layer_order_failures": (
            correction_layer_order_failures
        ),
        "stage_order_failures": stage_order_failures,
        "recurrent_placement_collisions": int(
            placed["placement_collisions"]
        ),
        "recurrent_logical_update_factors": int(
            update_report["logical_update_factors"]
        ),
        "recurrent_routed_primitives": len(routed),
        "recurrent_route_return_failures": int(
            route_report["route_return_failures"]
        ),
        "recurrent_non_NN_failures": int(
            route_report["non_NN_failures"]
        ),
        "A_B_C_route_failures": dict(route_failures),
        "namespace": {
            "code": (0, q),
            "companion_encoded_bank": (q, 2 * q),
            "G_routed_only_sites": (
                2 * q, 2 * q + len(extra_sites)
            ),
            "Bell_ancillae": (
                bell_base, bell_base + len(coupling_rows)
            ),
            "pump_syndromes": (
                pump_base, pump_base + len(pump_rows)
            ),
            "route_rails": (
                rail_base, rail_base + len(fixture.cells)
            ),
            "total_registers": cursor,
        },
        "lawful_walk": lawful,
        "dropped_handoff_control": {
            "deleted_edge": dropped_edge,
            "violation_count": dropped_walk[
                "ownership_or_handoff_violation_count"
            ],
            "named_missing_handoff_detected": dropped_named,
        },
        "duplicated_owner_control": {
            "slot": duplicate_index,
            "duplicated_word": original["id"],
            "collision_count": duplicate_walk["collision_count"],
            "named_collision_detected": duplicate_named,
        },
    }


def fixed_sector_kraus_certificate() -> dict[str, object]:
    """Derive dense Bell-branch Kraus maps without importing the EB runner."""
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    y = 1j * x @ z
    correction_candidates = (identity, x, y, z)
    phi = np.asarray((1, 0, 0, 1), dtype=complex) / math.sqrt(2)
    bell_generators = (identity, x, z, x @ z)
    bell_states = tuple(
        np.kron(identity, generator) @ phi
        for generator in bell_generators
    )
    bell_gram = np.asarray([
        [np.vdot(left, right) for right in bell_states]
        for left in bell_states
    ])
    isometry = np.kron(identity, phi.reshape(-1, 1))
    uncorrected = tuple(
        np.kron(bell.conj().reshape(1, 4), identity) @ isometry
        for bell in bell_states
    )
    corrections = []
    corrected = []
    branch_identity_residual = 0.0
    for kraus in uncorrected:
        candidates = []
        for correction in correction_candidates:
            branch = correction @ kraus
            scalar = np.trace(branch) / 2
            residual = float(np.linalg.norm(
                branch - scalar * identity
            ))
            candidates.append((residual, correction, branch, scalar))
        residual, correction, branch, scalar = min(
            candidates, key=lambda item: item[0]
        )
        corrections.append(correction)
        corrected.append(branch)
        branch_identity_residual = max(
            branch_identity_residual,
            residual,
            abs(abs(scalar) - 0.5),
        )
    uncorrected_completeness = sum(
        operator.conj().T @ operator for operator in uncorrected
    )
    corrected_completeness = sum(
        operator.conj().T @ operator for operator in corrected
    )
    bell_residual = float(np.linalg.norm(
        bell_gram - np.eye(4, dtype=complex)
    ))
    uncorrected_residual = float(np.linalg.norm(
        uncorrected_completeness - identity
    ))
    corrected_residual = float(np.linalg.norm(
        corrected_completeness - identity
    ))
    sectors = {}
    maximum = max(
        bell_residual,
        uncorrected_residual,
        corrected_residual,
        branch_identity_residual,
    )
    for name, basis in (
        ("even", (0, 3)),
        ("odd", (1, 2)),
    ):
        embedding = np.eye(4, dtype=complex)[:, basis]
        projector = embedding @ embedding.conj().T
        lifted = tuple(
            embedding @ operator @ embedding.conj().T
            for operator in corrected
        )
        leakage = max(
            float(np.linalg.norm(
                (np.eye(4) - projector) @ operator @ projector
            ))
            for operator in lifted
        )
        lifted_completeness = sum(
            operator.conj().T @ operator for operator in lifted
        )
        sector_residual = float(np.linalg.norm(
            lifted_completeness - projector
        ))
        maximum = max(maximum, sector_residual, leakage)
        sectors[name] = {
            "sector_dimension": 2,
            "Kraus_operators": len(lifted),
            "completeness_residual": sector_residual,
            "sector_leakage_residual": leakage,
        }
    return {
        "physical_modes": 2,
        "fixed_parity_sector_dimension": 2,
        "outcomes_per_sector": 4,
        "Bell_basis_orthonormality_residual": bell_residual,
        "uncorrected_Kraus_completeness_residual": (
            uncorrected_residual
        ),
        "corrected_Kraus_completeness_residual": corrected_residual,
        "corrected_branch_identity_residual": (
            branch_identity_residual
        ),
        "sectors": sectors,
        "maximum_residual": maximum,
        "construction": (
            "four Kraus maps derived by contracting an input/resource Bell "
            "basis against a dense Bell pair, corrected by the independently "
            "selected logical Pauli, then embedded in each two-mode parity "
            "sector"
        ),
    }


def fixture_certificate(
    conventions: dict[str, object],
) -> dict[str, object]:
    eb_module = (
        "frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27"
    )
    eb_present_before = eb_module in sys.modules
    mass = U.C.R.local_free_contact_mass()["mass_contact"]
    cycle230 = U.C712.cycle230_semantic_certificate(
        U.C712.decoded_word(2)[0]
    )
    mass_fields = (
        "one_particle_mass_residual",
        "contact_vacuum_and_one_particle_residual",
        "contact_double_occupation_phase_residual",
    )
    cycle230_fields = (
        "coin_matrix_residual",
        "mass_residual",
        "FSWAP_matrix_residual",
        "onsite_64_state_contact_residual",
        "internal_depth_two_stream_residual",
    )
    mass_selected = {
        name: float(mass[name]) for name in mass_fields
    }
    cycle230_selected = {
        name: float(cycle230[name]) for name in cycle230_fields
    }
    kraus = fixed_sector_kraus_certificate()
    return {
        "mass_contact_residuals": mass_selected,
        "cycle230_residuals": cycle230_selected,
        "maximum_inherited_residual": max(
            (*mass_selected.values(), *cycle230_selected.values())
        ),
        "EB_module_present_before_dense_rebuild": eb_present_before,
        "EB_module_present_after_dense_rebuild": eb_module in sys.modules,
        "two_mode_fixed_sector_Kraus": kraus,
        "docstring_fixed_sector_inventory_evidence": (
            conventions["bell_character_declares_fixed_X_and_character_Z"]
            and conventions["even_exchange_port_declares_one_six_mode_live_bank"]
        ),
    }


def all_zero(mapping: dict[str, int]) -> bool:
    return all(int(value) == 0 for value in mapping.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = perf_counter()
    source_root = args.source_root.resolve()
    conventions = declared_conventions(source_root)
    load_dependencies(source_root)

    exchange = exchange_port_certificate(conventions)
    dilation = dilation_certificate()
    atlas = atlas_correction_certificate()
    seam = seam_class_certificate()
    epoch = epoch_liveness_certificate()
    fixtures = fixture_certificate(conventions)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "exchange_port_certificate",
        exchange["convention_evidence_pass"]
        and exchange["six_SWAP_blocks"] == 6
        and exchange["CNOT_primitives"] == 18
        and exchange["port_dictionary_rows"] == 36
        and exchange["forward_dictionary_exchange_failures"] == 0
        and exchange["reverse_dictionary_exchange_failures"] == 0
        and exchange["all_affected_dictionary_exchange_failures"] == 0
        and exchange["unaffected_dictionary_invariance_failures"] == 0
        and exchange["cell_parity_image_failures"] == 0
        and exchange["joint_parity_invariance_failures"] == 0
        and exchange["odd_bank_detection_failures"] == 0
        and exchange["odd_image_detection_failures"] == 0
        and exchange["support_cells"] == 1
        and exchange["support_diameter"] == 0
        and exchange["dense_integer_Pauli_selftest"]["mismatches"] == 0,
    )
    check(
        "dilation_certificate",
        dilation["physical_restriction_tag_rebuild_failures"] == 0
        and dilation["compiled_commutator_failures"] == 0
        and dilation["graph_rank"] == dilation["compiled_rank"]
        and dilation["graph_rank"] == dilation["rows"]
        and dilation["dilation_X_invariance_failures"] == 0
        and dilation["dilation_Z_character_failures"] == 0
        and dilation["support_gate_failures"] == 0
        and dilation["maximum_compiled_support_cells"] <= 2
        and dilation["maximum_compiled_support_diameter"] <= 1,
    )
    check(
        "atlas_correction_certificate",
        atlas["graph_rank"] == atlas["graph_rows"]
        and atlas["atlas_entries"] == atlas["graph_rows"]
        and atlas["solve_contradictions"] == 0
        and atlas["rows_without_one_cell_solution"] == 0
        and atlas["one_hot_duality_failures"] == 0
        and atlas["one_cell_support_failures"] == 0
        and atlas["maximum_private_dual_support_cells"] <= 1,
    )
    check(
        "seam_class_certificate",
        seam["proper_cubic_frames"] == 24
        and seam["translation_parities"] == 8
        and seam["contexts"] == 24 * 8
        and seam["missing_edge_failures"] == 0
        and seam["zero_class_failures"] == 0
        and seam["double_class_failures"] == 0
        and seam["forward_class_count"] > 0
        and seam["reversed_class_count"] > 0
        and (
            seam["forward_class_count"] + seam["reversed_class_count"]
            == seam["transported_quadruples"]
        ),
    )
    check(
        "epoch_liveness_certificate",
        epoch["coupling_physical_restriction_failures"] == 0
        and epoch["coupling_graph_tag_order_failures"] == 0
        and epoch["correction_layer_order_failures"] == 0
        and epoch["stage_order_failures"] == 0
        and epoch["recurrent_placement_collisions"] == 0
        and epoch["recurrent_route_return_failures"] == 0
        and epoch["recurrent_non_NN_failures"] == 0
        and all_zero(epoch["A_B_C_route_failures"])
        and epoch["lawful_walk"]["collision_count"] == 0
        and (
            epoch["lawful_walk"][
                "ownership_or_handoff_violation_count"
            ]
            == 0
        )
        and epoch["dropped_handoff_control"][
            "named_missing_handoff_detected"
        ]
        and epoch["dropped_handoff_control"]["violation_count"] > 0
        and epoch["duplicated_owner_control"][
            "named_collision_detected"
        ]
        and epoch["duplicated_owner_control"]["collision_count"] > 0,
    )
    check(
        "fixture_certificate",
        fixtures["maximum_inherited_residual"] < TOL
        and not fixtures["EB_module_present_before_dense_rebuild"]
        and not fixtures["EB_module_present_after_dense_rebuild"]
        and fixtures["two_mode_fixed_sector_Kraus"][
            "maximum_residual"
        ] < 1e-12,
    )

    wording_corrections = [
        (
            "The epoch runner's description of its alternate port as the even_exchange_port "
            "leg needs a namespace qualifier: standalone even_exchange_port declares one "
            "six-qubit bank [q,q+6), whereas the epoch embeds a port-indexed "
            "six-qubit sub-block inside the q-wide bell_character bank [q,2q).  These "
            "register conventions coincide only for port index zero."
        )
    ]
    passing = all(row["pass"] for row in checks)
    report = {
        "status": "PASS" if passing else "FAIL",
        "authority": "none",
        "audit": "unset",
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
        "declared_conventions": conventions,
        "checks": checks,
        "certificates": {
            "exchange_port": exchange,
            "dilation": dilation,
            "atlas_correction": atlas,
            "seam_class": seam,
            "epoch_liveness": epoch,
            "fixture": fixtures,
        },
        "wording_corrections": wording_corrections,
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(payload + "\n")
    print(payload)
    print(
        "COMPANION_BANK_INPUT_PACKAGE_INDEPENDENT_ADVERSARY_PASS"
        if passing
        else "COMPANION_BANK_INPUT_PACKAGE_INDEPENDENT_ADVERSARY_INCOMPLETE"
    )
    if not passing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
