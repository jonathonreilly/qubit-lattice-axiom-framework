#!/usr/bin/env python3
"""Cycle597: state-family grade-to-transition synthesis tournament."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import inspect
import json
from math import floor
from pathlib import Path
import re
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_ti_innovation_bath_offgrid_history_tournament_cycle595_2026_07_22 as c595
import physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22 as c580

c592 = c595.c592
c587 = c595.c587
c577 = c595.c577
c552 = c595.c552
Gate = c587.Gate
Word = tuple[int, ...]

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_STATE_FAMILY_GRADE_TRANSITION_SYNTHESIS_TOURNAMENT_CYCLE597_NOTE_2026-07-22.md"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_PATHS = {
    "Cycle595 runner": ROOT / "scripts/physical_ti_innovation_bath_offgrid_history_tournament_cycle595_2026_07_22.py",
    "Cycle595 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TI_INNOVATION_BATH_OFFGRID_HISTORY_TOURNAMENT_CYCLE595_NOTE_2026-07-22.md",
    "Cycle592 runner": ROOT / "scripts/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_2026_07_22.py",
    "Cycle592 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md",
    "Cycle580 runner": ROOT / "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py",
    "Cycle580 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md",
    "Cycle577 runner": ROOT / "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py",
    "Cycle577 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md",
}
FROZEN = {
    "Cycle595 runner": "cdfcddb00974205faa8bc60c617ff0dd42bf9f8947b0a55a4b172157b2d28de2",
    "Cycle595 note": "b1b1fc0960f69abcf9050b7eee2f3387188d45ea7704ca2db87381cd5fd3b730",
    "Cycle592 runner": "ab565af6aa59e66cea7b1ce625c08f8a88235ae9f7415e5e7d89d63af34ce9ce",
    "Cycle592 note": "dccf62d6126287b20cbf96ff410534adfa1746d9cf3aba94fbfb2893855be212",
    "Cycle580 runner": "c46917d4a932cd3ad9a78e0547625055f5adf9d5cf7393700d7e6715dd515cd3",
    "Cycle580 note": "e8ca5acdaec0c7ec5f0ba9772d7736352bcf132e961483d93f19c679439df276",
    "Cycle577 runner": "93bf1fa2859289b13037bfe7882cce86732e9377ed8b60e56c3bd55ebc0ce74f",
    "Cycle577 note": "23ef5601b73c121d5e82c9031ec0ff4acffdc5471c43aa4dec63a78085aa7c0f",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


# This complete rule object is frozen before train or held input declarations.
# In particular, the 2-bit parameter grid, 6-bit transition address, and rotor
# constants are selected without any held parameter, precision, or corpus size.
SYNTHESIS_LAW = {
    "family": "three-M2 product states Z(p_L) tensor X(p_M) tensor Z(p_R), 0<=p_j<=1",
    "route_A": "Cycle577 Z-X-Z projector query using the Cycle580 encoded H/CNOT extraction block; four supplied copies",
    "route_B": {
        "parameter_fraction_bits": 2,
        "parameter_encoding": "four-bit unary threshold, nearest-grid half-up",
        "transition_bits": 6,
        "transition_addresses": 64,
        "rule": "all 4x4x4 microaddresses classified by the three unary parameter comparisons",
        "answer_rows": 0,
    },
    "route_C": {
        "rotor": "r_(n+1)=r_n+25 mod 64",
        "genesis": 9,
        "selection": "derived grade mask at r_n, never a host sampler",
        "worst_case_domain": "all 5^3 unary parameter words and all prefixes 1..64",
    },
    "occurrence_adapter": "fixed member = history mod 4; unchanged Cycle552 conditional occurrence",
}
SYNTHESIS_LAW_SHA256 = sha256(json.dumps(SYNTHESIS_LAW, sort_keys=True).encode()).hexdigest()
EXPECTED_SYNTHESIS_LAW_SHA256 = "9a2a6121730ad67c6049a42150a056687cc33fc6771897425fccb3d9e5b877b6"


@dataclass(frozen=True)
class Spec:
    name: str
    parameters: tuple[Fraction, Fraction, Fraction]
    corpus_size: int
    split: str


# Declared strictly after SYNTHESIS_LAW and its hash.
TRAIN_SPECS = (
    Spec("train_uniform", (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)), 128, "train"),
    Spec("train_basis_corner", (Fraction(1), Fraction(1), Fraction(1)), 96, "train"),
    Spec("train_asymmetric", (Fraction(3, 4), Fraction(1, 4), Fraction(1, 2)), 160, "train"),
)
HELD_SPECS = (
    Spec("held_offgrid_7over11_4over9_5over13", (Fraction(7, 11), Fraction(4, 9), Fraction(5, 13)), 137, "held"),
    Spec("held_offgrid_11over17_13over19_17over23", (Fraction(11, 17), Fraction(13, 19), Fraction(17, 23)), 211, "held"),
)
SPECS = TRAIN_SPECS + HELD_SPECS
HELD_DECLARATION = {
    "points": tuple(tuple(str(value) for value in spec.parameters) for spec in HELD_SPECS),
    "physical_parameter_fraction_bits": 2,
    "transition_bits": 6,
    "sizes": tuple(spec.corpus_size for spec in HELD_SPECS),
}
HELD_SHA256 = sha256(json.dumps(HELD_DECLARATION, sort_keys=True).encode()).hexdigest()


def product_state(parameters: tuple[Fraction, Fraction, Fraction]) -> np.ndarray:
    if len(parameters) != 3 or any(value < 0 or value > 1 for value in parameters):
        raise ValueError("parameters leave the declared product-state cube")
    p_left, p_middle, p_right = (float(value) for value in parameters)
    minus = (c577.ZERO - c577.ONE) / np.sqrt(2.0)
    left = np.sqrt(p_left) * c577.ZERO + np.sqrt(1.0 - p_left) * c577.ONE
    middle = np.sqrt(p_middle) * c577.PLUS + np.sqrt(1.0 - p_middle) * minus
    right = np.sqrt(p_right) * c577.ZERO + np.sqrt(1.0 - p_right) * c577.ONE
    return c577.kron_all(left.reshape(-1, 1), middle.reshape(-1, 1), right.reshape(-1, 1)).reshape(-1)


def exact_product_grade(parameters: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, ...]:
    p_left, p_middle, p_right = parameters
    output = []
    for middle_sign, left_value, right_value in c577.HISTORIES:
        middle = p_middle if middle_sign == 1 else 1 - p_middle
        left = p_left if left_value == 0 else 1 - p_left
        right = p_right if right_value == 0 else 1 - p_right
        output.append(middle * left * right)
    return tuple(output)


def independent_grade(state: np.ndarray) -> np.ndarray:
    return c592.independent_grade_vector(state)


# Route A: exact coherent projector query and copied history-label register.
A_QUERY_NAMES = {
    "logical_H_open_decode", "logical_H_open_H", "logical_H_open_encode",
    "extract_X_middle", "extract_Z_left", "extract_Z_right",
    "logical_H_close_decode", "logical_H_close_H", "logical_H_close_encode",
}
A_QUERY = tuple(gate for gate in c580.ELEMENTARY_GATES if gate.name in A_QUERY_NAMES)
A_COPY = tuple(gate for gate in c580.ELEMENTARY_GATES if gate.role == "dephasing-copy")


def a_initial(state: np.ndarray) -> np.ndarray:
    encoded = c577.W3 @ state
    return np.kron(
        np.kron(np.kron(encoded, c577.ket(0, 64)), c577.ket(0, 8)),
        c577.ket(0, 8),
    ).reshape(-1, 1)


def register_distribution(state: np.ndarray, register: str) -> np.ndarray:
    tensor = state.reshape(64, 64, 8, 8)
    if register == "pointer":
        return np.sum(np.abs(tensor) ** 2, axis=(0, 1, 3)).reshape(8)
    if register == "copy":
        return np.sum(np.abs(tensor) ** 2, axis=(0, 1, 2)).reshape(8)
    raise ValueError("unknown Route-A register")


def route_a_controls() -> dict[str, object]:
    # Reconstruct the complete accepted Cycle580 instrument and its inverse as
    # a shore check.  The state-query below uses only its exact pointer block;
    # using the full reset/contact instrument would overwrite the queried state.
    shore_initial = c580.initial_columns()
    shore_compiled = c580.apply_sequence(shore_initial, c580.ELEMENTARY_GATES)
    shore_target = c580.cycle577_target_columns()
    full_instrument_residual = float(np.linalg.norm(shore_compiled - shore_target))
    full_inverse_residual = float(np.linalg.norm(c580.inverse_sequence(shore_compiled, c580.ELEMENTARY_GATES) - shore_initial))
    del shore_initial, shore_compiled, shore_target

    rows = []
    maximum_query_residual = maximum_inverse_residual = maximum_copy_residual = 0.0
    maximum_expected_grade_residual = maximum_sector_mass_residual = 0.0
    maximum_boundary_leakage = 0.0
    maximum_active_query_deletion = maximum_active_copy_deletion = 0.0
    query_copies = 4
    for spec in SPECS:
        state = product_state(spec.parameters)
        exact = np.asarray(tuple(float(value) for value in exact_product_grade(spec.parameters)))
        projector_grade = independent_grade(state)
        maximum_expected_grade_residual = max(maximum_expected_grade_residual, float(np.linalg.norm(projector_grade - exact)))
        initial = a_initial(state)
        queried = c580.apply_sequence(initial, A_QUERY)
        copied = c580.apply_sequence(queried, A_COPY)
        pointer = register_distribution(queried, "pointer")
        grade_copy = register_distribution(copied, "copy")
        maximum_query_residual = max(maximum_query_residual, float(np.linalg.norm(pointer - exact)))
        maximum_copy_residual = max(maximum_copy_residual, float(np.linalg.norm(grade_copy - exact)))
        recovered_query = c580.inverse_sequence(queried, A_QUERY)
        recovered_full = c580.inverse_sequence(copied, A_QUERY + A_COPY)
        maximum_inverse_residual = max(maximum_inverse_residual, float(np.linalg.norm(recovered_query - initial)), float(np.linalg.norm(recovered_full - initial)))
        maximum_boundary_leakage = max(
            maximum_boundary_leakage,
            c580.code_leakage(queried, c580.SYSTEM_PAIRS),
            c580.code_leakage(copied, c580.SYSTEM_PAIRS),
        )

        deleted_query = c580.apply_sequence(initial, tuple(g for g in A_QUERY + A_COPY if g.name != "extract_X_middle"))
        deleted_copy = c580.apply_sequence(initial, tuple(g for g in A_QUERY + A_COPY if g.name != "copy_middle_dephase"))
        maximum_active_query_deletion = max(maximum_active_query_deletion, float(np.linalg.norm(register_distribution(deleted_query, "copy") - exact, ord=1)))
        maximum_active_copy_deletion = max(maximum_active_copy_deletion, float(np.linalg.norm(register_distribution(deleted_copy, "copy") - exact, ord=1)))

        # Four independent supplied copies yield a coherent tuple register.
        # Its sector weights form a multinomial ledger; no sector is selected.
        expected_counts = np.zeros(8)
        sector_mass = 0.0
        retained = 0
        for labels in product(range(8), repeat=query_copies):
            mass = float(np.prod(tuple(exact[label] for label in labels)))
            sector_mass += mass
            if mass > TOL:
                retained += 1
            for label in labels:
                expected_counts[label] += mass / query_copies
        maximum_sector_mass_residual = max(maximum_sector_mass_residual, abs(sector_mass - 1.0), float(np.linalg.norm(expected_counts - exact)))
        rows.append({
            "name": spec.name, "split": spec.split,
            "exact_grade": tuple(float(x) for x in exact),
            "nonzero_single_query_sectors": int(np.sum(exact > TOL)),
            "retained_four_query_tuple_sectors": retained,
            "maximum_single_component_empirical_variance": float(max(exact * (1.0 - exact) / query_copies)),
            "numeric_grade_word_or_objective_sector_derived": False,
        })

    frames = c577.c41.proper_cubic_rotations()
    edge_failures = 0
    two_site = tuple(gate for gate in A_QUERY + A_COPY if len(gate.qubits) == 2)
    for frame in frames:
        for gate in two_site:
            left_name, right_name = (c580.QUBIT_NAMES[index] for index in gate.qubits)
            left = frame @ np.asarray(c580.LAYOUT[left_name], dtype=int)
            right = frame @ np.asarray(c580.LAYOUT[right_name], dtype=int)
            edge_failures += int(sum(abs(int(a - b)) for a, b in zip(left, right)) != 1)

    result = {
        "route": "A coherent Cycle577-projector/Cycle580-pointer query",
        "complete_Cycle580_instrument_residual": full_instrument_residual,
        "complete_Cycle580_inverse_residual": full_inverse_residual,
        "query_elementary_gates": len(A_QUERY), "copy_CNOTs": len(A_COPY),
        "physical_M2_per_query_copy": 18,
        "supplied_identically_prepared_query_copies": query_copies,
        "physical_M2_per_four_query_batch": 18 * query_copies,
        "maximum_projector_formula_residual": maximum_expected_grade_residual,
        "maximum_query_distribution_residual": maximum_query_residual,
        "maximum_copied_label_distribution_residual": maximum_copy_residual,
        "maximum_exact_inverse_residual": maximum_inverse_residual,
        "maximum_boundary_dual_rail_leakage": maximum_boundary_leakage,
        "four_query_sector_ledger_residual": maximum_sector_mass_residual,
        "active_query_gate_deletion_fixture_L1": maximum_active_query_deletion,
        "active_copy_gate_deletion_fixture_L1": maximum_active_copy_deletion,
        "all_retained_sectors": True,
        "coherent_grade_register_is_objective_probability": False,
        "state_copy_preparation_or_no_cloning_derived": False,
        "proper_cubic_frames": len(frames),
        "all24_query_copy_edge_tests": len(frames) * len(two_site),
        "all24_query_copy_edge_failures": edge_failures,
        "rows": rows,
        "pass": max(full_instrument_residual, full_inverse_residual, maximum_expected_grade_residual,
                    maximum_query_residual, maximum_copy_residual, maximum_inverse_residual,
                    maximum_boundary_leakage, maximum_sector_mass_residual) < TOL
        and maximum_active_query_deletion > TOL and maximum_active_copy_deletion > TOL
        and edge_failures == 0 and len(frames) == 24,
    }
    check("Route A exactly queries and copies the Cycle577 grade distribution while retaining every coherent sector and supplied-copy import", result["pass"], result)
    return result


# Route B: one reversible product-family circuit, with no program selector and
# no per-state answer rows.  Each continuous parameter is rounded to a four-cell
# unary threshold; all 4^3 addresses then synthesize an exact denominator-64
# history mask by three literal comparisons.
B_PARAM_CELLS = 4
B_ADDRESS_COUNT = B_PARAM_CELLS**3
_b = [0]
B_PARAMETERS = tuple(take(_b, B_PARAM_CELLS) for _ in range(3))
B_WORK = take(_b, 1)[0]
B_MASK = tuple(take(_b, B_ADDRESS_COUNT) for _ in range(8))
B_WIDTH = _b[0]


def address_triple(address: int) -> tuple[int, int, int]:
    if address not in range(B_ADDRESS_COUNT):
        raise ValueError("microaddress leaves 4x4x4 domain")
    return address // 16, (address // 4) % 4, address % 4


def round_parameter(value: Fraction) -> int:
    if value < 0 or value > 1:
        raise ValueError("parameter leaves unit interval")
    return min(B_PARAM_CELLS, floor(value * B_PARAM_CELLS + Fraction(1, 2)))


def quantized_parameters(parameters: tuple[Fraction, Fraction, Fraction]) -> tuple[tuple[int, int, int], tuple[Fraction, Fraction, Fraction]]:
    if len(parameters) != 3:
        raise ValueError("parameter word must have exactly three entries")
    counts = tuple(round_parameter(value) for value in parameters)
    return counts, tuple(Fraction(value, B_PARAM_CELLS) for value in counts)


def build_b_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for address in range(B_ADDRESS_COUNT):
        left_index, middle_index, right_index = address_triple(address)
        for history, (middle_sign, left_value, right_value) in enumerate(c577.HISTORIES):
            literal_sites = (B_PARAMETERS[0][left_index], B_PARAMETERS[1][middle_index], B_PARAMETERS[2][right_index])
            invert = (left_value == 1, middle_sign == -1, right_value == 1)
            for slot, (site, needed) in enumerate(zip(literal_sites, invert)):
                if needed:
                    gates.append(Gate("X", (site,), f"B:mask:{history}:{address}:invert:{slot}:pre"))
            gates.append(Gate("TOFFOLI", (literal_sites[0], literal_sites[1], B_WORK), f"B:mask:{history}:{address}:and12"))
            gates.append(Gate("TOFFOLI", (B_WORK, literal_sites[2], B_MASK[history][address]), f"B:mask:{history}:{address}:write"))
            gates.append(Gate("TOFFOLI", (literal_sites[0], literal_sites[1], B_WORK), f"B:mask:{history}:{address}:unand12"))
            for slot, (site, needed) in reversed(tuple(enumerate(zip(literal_sites, invert)))):
                if needed:
                    gates.append(Gate("X", (site,), f"B:mask:{history}:{address}:invert:{slot}:post"))
    return tuple(gates)


B_SCHEDULE = build_b_schedule()


def prepare_b(parameters: tuple[Fraction, Fraction, Fraction]) -> Word:
    counts, _quantized = quantized_parameters(parameters)
    bits = [0] * B_WIDTH
    for sites, count in zip(B_PARAMETERS, counts):
        for index, site in enumerate(sites):
            bits[site] = int(index < count)
    return tuple(bits)


def validate_unary(bits: Word) -> None:
    if len(bits) != B_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Route-B word leaves binary domain")
    for sites in B_PARAMETERS:
        word = tuple(bits[site] for site in sites)
        if word != tuple(sorted(word, reverse=True)):
            raise ValueError("Route-B parameter is not unary monotone")
    if bits[B_WORK] != 0 or any(bits[site] for row in B_MASK for site in row):
        raise ValueError("Route-B work/mask target is not blank")


def history_for_address(counts: tuple[int, int, int], address: int) -> int:
    left_index, middle_index, right_index = address_triple(address)
    return 4 * int(middle_index >= counts[1]) + 2 * int(left_index >= counts[0]) + int(right_index >= counts[2])


def expected_mask(counts: tuple[int, int, int]) -> Word:
    return tuple(int(history_for_address(counts, address) == history) for history in range(8) for address in range(B_ADDRESS_COUNT))


def mask_from_b_output(bits: Word) -> Word:
    return tuple(bits[site] for row in B_MASK for site in row)


def mask_counts(mask: Word) -> tuple[int, ...]:
    if len(mask) != 8 * B_ADDRESS_COUNT:
        raise ValueError("grade mask has wrong width")
    return tuple(sum(mask[history * B_ADDRESS_COUNT:(history + 1) * B_ADDRESS_COUNT]) for history in range(8))


def route_b_controls() -> dict[str, object]:
    line = c587.static_line_compiler_controls(B_SCHEDULE, B_WIDTH)
    exhaustive_failures = inverse_failures = code_failures = 0
    for counts in product(range(5), repeat=3):
        parameters = tuple(Fraction(value, 4) for value in counts)
        source = prepare_b(parameters)
        validate_unary(source)
        output = c587.apply_schedule(source, B_SCHEDULE)
        exhaustive_failures += mask_from_b_output(output) != expected_mask(counts)
        exhaustive_failures += output[B_WORK] != 0
        inverse_failures += c587.apply_schedule(output, B_SCHEDULE, reverse=True) != source
        code_failures += int(any(bit not in (0, 1) for bit in output))

    rows = []
    maximum_exact_grade_residual = maximum_product_synthesis_residual = 0.0
    maximum_bound_violation = 0.0
    for spec in SPECS:
        source = prepare_b(spec.parameters)
        output = c587.apply_schedule(source, B_SCHEDULE)
        counts, quantized = quantized_parameters(spec.parameters)
        synthesized_counts = mask_counts(mask_from_b_output(output))
        synthesized = np.asarray(synthesized_counts, dtype=float) / B_ADDRESS_COUNT
        exact = np.asarray(tuple(float(value) for value in exact_product_grade(spec.parameters)))
        quantized_exact = np.asarray(tuple(float(value) for value in exact_product_grade(quantized)))
        exact_from_projector = independent_grade(product_state(spec.parameters))
        maximum_exact_grade_residual = max(maximum_exact_grade_residual, float(np.linalg.norm(exact_from_projector - exact)))
        maximum_product_synthesis_residual = max(maximum_product_synthesis_residual, float(np.linalg.norm(synthesized - quantized_exact)))
        actual_l1 = float(np.linalg.norm(synthesized - exact, ord=1))
        parameter_l1_bound = float(2 * sum(abs(value - rounded) for value, rounded in zip(spec.parameters, quantized)))
        maximum_bound_violation = max(maximum_bound_violation, actual_l1 - parameter_l1_bound)
        rows.append({
            "name": spec.name, "split": spec.split,
            "parameters": tuple(str(value) for value in spec.parameters),
            "quantized_parameters": tuple(str(value) for value in quantized),
            "denominator64_counts": synthesized_counts,
            "target_to_synthesized_L1": actual_l1,
            "product_parameter_L1_bound": parameter_l1_bound,
        })

    # Active parameter-bit deletion changes the derived grade word; deleting
    # the whole parameter word is lawfully refused.  Neither control reads a
    # state-specific answer row.
    deletion_spec = HELD_SPECS[0]
    ideal_source = prepare_b(deletion_spec.parameters)
    ideal_output = c587.apply_schedule(ideal_source, B_SCHEDULE)
    deleted_source = list(ideal_source)
    active_site = next(site for sites in B_PARAMETERS for site in reversed(sites) if deleted_source[site])
    deleted_source[active_site] = 0
    deleted_output = c587.apply_schedule(tuple(deleted_source), B_SCHEDULE)
    parameter_bit_deletion_l1 = float(np.linalg.norm(
        np.asarray(mask_counts(mask_from_b_output(ideal_output))) / B_ADDRESS_COUNT
        - np.asarray(mask_counts(mask_from_b_output(deleted_output))) / B_ADDRESS_COUNT,
        ord=1,
    ))
    absent_refused = 0
    try:
        prepare_b(())  # type: ignore[arg-type]
    except ValueError:
        absent_refused = 1

    relevant_source = inspect.getsource(build_b_schedule) + inspect.getsource(prepare_b) + inspect.getsource(expected_mask)
    answer_table_reads = relevant_source.count("HISTORY_TABLE") + relevant_source.count("MEMBER_TABLE")
    result = {
        "route": "B reversible unary fixed-point product-family synthesizer",
        "parameter_fraction_bits": 2, "transition_bits": 6,
        "physical_M2": B_WIDTH,
        "logical_gate_count": len(B_SCHEDULE),
        "exhaustive_parameter_words": 125,
        "exhaustive_mask_failures": exhaustive_failures,
        "inverse_failures": inverse_failures,
        "binary_code_failures": code_failures,
        "maximum_projector_formula_residual": maximum_exact_grade_residual,
        "maximum_exact_quantized_product_synthesis_residual": maximum_product_synthesis_residual,
        "maximum_approximation_bound_violation": maximum_bound_violation,
        "parameter_bit_deletion_L1": parameter_bit_deletion_l1,
        "absent_parameter_word_refusals": absent_refused,
        "Cycle592_answer_table_reads": answer_table_reads,
        "program_selector_M2": 0,
        "state_specific_answer_rows": 0,
        "static_nearest_neighbor_compiler": line,
        "rows": rows,
        "pass": exhaustive_failures == inverse_failures == code_failures == 0
        and max(maximum_exact_grade_residual, maximum_product_synthesis_residual) < TOL
        and maximum_bound_violation < TOL and parameter_bit_deletion_l1 > TOL
        and absent_refused == 1 and answer_table_reads == 0 and line["pass"],
    }
    check("Route B uses one reversible fixed-point product rule over all 125 parameter words with no program selector or answer ROM", result["pass"], result)
    return result


# Route C: a deterministic +25 one-carrier rotor reads the derived Route-B
# grade mask.  A fresh blank archive packet is consumed per occurrence; no
# history word or random draw is supplied by the host.
ROTOR_INCREMENT = 25
ROTOR_GENESIS = 9
_c = [0]
C_A = take(_c, 64)
C_BUFFER = take(_c, 64)
C_MASK = tuple(take(_c, 64) for _ in range(8))
C_SELECT = tuple(take(_c, 64) for _ in range(8))
C_HISTORY = take(_c, 8)
C_ARCHIVE = take(_c, 8)
C_WIDTH = _c[0]


def build_c_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for history, address in product(range(8), range(64)):
        gates.append(Gate("TOFFOLI", (C_MASK[history][address], C_A[address], C_SELECT[history][address]), f"C:select:{history}:{address}"))
    for history, address in product(range(8), range(64)):
        gates.append(Gate("CNOT", (C_SELECT[history][address], C_HISTORY[history]), f"C:history:{history}:{address}:write"))
    for history in range(8):
        gates.append(Gate("CNOT", (C_HISTORY[history], C_ARCHIVE[history]), f"C:archive:{history}"))
    for history, address in reversed(tuple(product(range(8), range(64)))):
        gates.append(Gate("CNOT", (C_SELECT[history][address], C_HISTORY[history]), f"C:history:{history}:{address}:clear"))
    for history, address in reversed(tuple(product(range(8), range(64)))):
        gates.append(Gate("TOFFOLI", (C_MASK[history][address], C_A[address], C_SELECT[history][address]), f"C:unselect:{history}:{address}"))
    for address in range(64):
        gates.append(Gate("SWAP", (C_A[address], C_BUFFER[address]), f"C:onsite:{address}"))
    for address in range(64):
        gates.append(Gate("SWAP", (C_BUFFER[address], C_A[(address + ROTOR_INCREMENT) % 64]), f"C:cross:{address}"))
    return tuple(gates)


C_SCHEDULE = build_c_schedule()


def validate_grade_mask(mask: Word) -> None:
    if len(mask) != 512 or any(type(bit) is not int or bit not in (0, 1) for bit in mask):
        raise ValueError("Route-C grade mask leaves binary 8x64 domain")
    if any(sum(mask[history * 64 + address] for history in range(8)) != 1 for address in range(64)):
        raise ValueError("Route-C grade mask is not one history per address")


def prepare_c(mask: Word, address: int) -> Word:
    validate_grade_mask(mask)
    if address not in range(64):
        raise ValueError("Route-C carrier leaves 64-address ring")
    bits = [0] * C_WIDTH
    bits[C_A[address]] = 1
    for history in range(8):
        for microaddress in range(64):
            bits[C_MASK[history][microaddress]] = mask[history * 64 + microaddress]
    return tuple(bits)


def mask_history(mask: Word, address: int) -> int:
    validate_grade_mask(mask)
    return next(history for history in range(8) if mask[history * 64 + address])


def expected_c(mask: Word, address: int) -> Word:
    output = list(prepare_c(mask, (address + ROTOR_INCREMENT) % 64))
    output[C_ARCHIVE[mask_history(mask, address)]] = 1
    return tuple(output)


def grade_mask_for_parameters(parameters: tuple[Fraction, Fraction, Fraction]) -> Word:
    output = c587.apply_schedule(prepare_b(parameters), B_SCHEDULE)
    return mask_from_b_output(output)


def discrepancy_certificate(order: tuple[int, ...]) -> Fraction:
    maximum = Fraction(0)
    for parameter_counts in product(range(5), repeat=3):
        target = [0] * 8
        for address in range(64):
            target[history_for_address(parameter_counts, address)] += 1
        prefix = [0] * 8
        for length, address in enumerate(order, start=1):
            prefix[history_for_address(parameter_counts, address)] += 1
            maximum = max(maximum, *(abs(Fraction(prefix[h]) - Fraction(length * target[h], 64)) for h in range(8)))
    return maximum


def route_c_controls() -> dict[str, object]:
    line = c587.static_line_compiler_controls(C_SCHEDULE, C_WIDTH)
    rotor_order = tuple((ROTOR_GENESIS + ROTOR_INCREMENT * index) % 64 for index in range(64))
    natural_order = tuple(range(64))
    rotor_discrepancy = discrepancy_certificate(rotor_order)
    natural_discrepancy = discrepancy_certificate(natural_order)
    eg_failures = inverse_failures = interface_failures = mask_ledger_failures = 0
    rows = []
    maximum_budget_violation = 0.0
    for spec in SPECS:
        mask = grade_mask_for_parameters(spec.parameters)
        validate_grade_mask(mask)
        grade_counts = mask_counts(mask)
        counts, quantized = quantized_parameters(spec.parameters)
        mask_ledger_failures += grade_counts != tuple(int(64 * value) for value in exact_product_grade(quantized))
        for address in range(64):
            source = prepare_c(mask, address)
            output = c587.apply_schedule(source, C_SCHEDULE)
            eg_failures += output != expected_c(mask, address)
            inverse_failures += c587.apply_schedule(output, C_SCHEDULE, reverse=True) != source

        histories = tuple(mask_history(mask, (ROTOR_GENESIS + ROTOR_INCREMENT * index) % 64) for index in range(spec.corpus_size))
        empirical = np.asarray(tuple(histories.count(history) / spec.corpus_size for history in range(8)))
        quantized_grade = np.asarray(grade_counts, dtype=float) / 64.0
        target_grade = np.asarray(tuple(float(value) for value in exact_product_grade(spec.parameters)))
        rotor_l1 = float(np.linalg.norm(empirical - quantized_grade, ord=1))
        approximation_l1 = float(np.linalg.norm(quantized_grade - target_grade, ord=1))
        total_l1 = float(np.linalg.norm(empirical - target_grade, ord=1))
        parameter_bound = float(2 * sum(abs(value - rounded) for value, rounded in zip(spec.parameters, quantized)))
        rotor_bound = float(8 * rotor_discrepancy / spec.corpus_size)
        total_bound = parameter_bound + rotor_bound
        maximum_budget_violation = max(maximum_budget_violation, total_l1 - total_bound, rotor_l1 - rotor_bound, approximation_l1 - parameter_bound)
        for history in set(histories):
            member = history % 4
            base = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=history)
            fields, _law = c552.snapshot_view(c552.physical_step(base), 0)
            interface_failures += int(fields[:3] != (1, 1, 1))
        rows.append({
            "name": spec.name, "split": spec.split, "corpus_size": spec.corpus_size,
            "denominator64_grade": tuple(float(x) for x in quantized_grade),
            "finite_rotor_frequency": tuple(float(x) for x in empirical),
            "rotor_to_grade_L1": rotor_l1,
            "grade_approximation_L1": approximation_l1,
            "frequency_to_target_L1": total_l1,
            "parameter_approximation_bound": parameter_bound,
            "rotor_discrepancy_bound": rotor_bound,
            "combined_L1_bound": total_bound,
        })

    deletion_mask = grade_mask_for_parameters(HELD_SPECS[0].parameters)
    deletion_address = ROTOR_GENESIS
    deletion_history = mask_history(deletion_mask, deletion_address)
    source = prepare_c(deletion_mask, deletion_address)
    ideal = c587.apply_schedule(source, C_SCHEDULE)
    deleted_select = c587.apply_schedule(source, C_SCHEDULE, delete_label=f"C:select:{deletion_history}:{deletion_address}")
    deleted_cross = c587.apply_schedule(source, C_SCHEDULE, delete_label=f"C:cross:{deletion_address}")
    select_deletion_residual = float(np.linalg.norm(np.asarray(deleted_select) - np.asarray(ideal)))
    rotor_deletion_residual = float(np.linalg.norm(np.asarray(deleted_cross) - np.asarray(ideal)))
    deleted_grade_refused = absent_grade_refused = 0
    broken = list(deletion_mask)
    broken[deletion_history * 64 + deletion_address] = 0
    try:
        prepare_c(tuple(broken), deletion_address)
    except ValueError:
        deleted_grade_refused = 1
    try:
        prepare_c((), deletion_address)
    except ValueError:
        absent_grade_refused = 1

    source_text = inspect.getsource(build_c_schedule) + inspect.getsource(prepare_c) + inspect.getsource(expected_c) + inspect.getsource(mask_history)
    host_sampler_tokens = sum(source_text.count(token) for token in ("random", "choice(", "HISTORY_TABLE", "MEMBER_TABLE"))
    result = {
        "route": "C deterministic +25 low-discrepancy physical rotor",
        "physical_M2_per_occurrence_fixture": C_WIDTH,
        "rotor_increment": ROTOR_INCREMENT, "rotor_genesis": ROTOR_GENESIS,
        "rotor_period": len(set(rotor_order)),
        "exhaustive_grade_words": 125, "exhaustive_prefixes_per_word": 64,
        "rotor_maximum_per_history_count_discrepancy": str(rotor_discrepancy),
        "natural_order_comparator_discrepancy": str(natural_discrepancy),
        "EG_failures": eg_failures, "inverse_failures": inverse_failures,
        "grade_mask_ledger_failures": mask_ledger_failures,
        "unchanged_Cycle552_interface_failures": interface_failures,
        "maximum_error_budget_violation": maximum_budget_violation,
        "active_select_deletion_residual": select_deletion_residual,
        "active_rotor_edge_deletion_residual": rotor_deletion_residual,
        "deleted_grade_word_refusals": deleted_grade_refused,
        "absent_grade_word_refusals": absent_grade_refused,
        "host_sampler_or_answer_table_tokens": host_sampler_tokens,
        "carrier_and_grade_mask_catalytically_retained": True,
        "fresh_blank_archive_M2_per_occurrence": 8,
        "archive_packet_renewal_derived": False,
        "rotor_frequency_promoted_to_Born": False,
        "static_nearest_neighbor_compiler": line,
        "rows": rows,
        "pass": rotor_discrepancy == Fraction(67, 32) and natural_discrepancy == Fraction(16)
        and len(set(rotor_order)) == 64 and rotor_discrepancy < natural_discrepancy
        and not any((eg_failures, inverse_failures, mask_ledger_failures, interface_failures))
        and maximum_budget_violation < TOL and min(select_deletion_residual, rotor_deletion_residual) > TOL
        and deleted_grade_refused == absent_grade_refused == 1 and host_sampler_tokens == 0 and line["pass"],
    }
    check("Route C deterministically consumes the derived grade mask with an exhaustive discrepancy certificate and explicit approximation/resource budget", result["pass"], result)
    return result


def covariance_domain_controls() -> dict[str, object]:
    frames = c577.c41.proper_cubic_rotations()
    frame_failures = group_failures = frame_tests = 0
    for frame in frames:
        for member in range(4):
            source = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=member)
            framed, axis = c552.frame_word(source, 0, frame)
            expected, expected_axis = c552.frame_word(c552.physical_step(source), 0, frame)
            frame_failures += int(c552.physical_step(framed) != expected or axis != expected_axis)
            frame_tests += 1
    for left, right in product(frames, repeat=2):
        source = c552.prepare(0, 0, 0, 0, edge=1, plus=1, minus=0, K_position=0)
        for axis in range(3):
            _, axis1 = c552.frame_word(source, axis, right)
            _, axis2 = c552.frame_word(source, axis1, left)
            _, axisp = c552.frame_word(source, axis, left @ right)
            group_failures += axis2 != axisp
    malformed = (
        lambda: product_state((Fraction(-1), Fraction(1, 2), Fraction(1, 2))),
        lambda: prepare_b(()),
        lambda: prepare_b((Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))),
        lambda: address_triple(64),
        lambda: prepare_c((0,) * 512, 0),
        lambda: prepare_c(grade_mask_for_parameters(TRAIN_SPECS[0].parameters), 64),
    )
    refused = 0
    for action in malformed:
        try:
            action()
        except ValueError:
            refused += 1
    result = {
        "proper_cubic_frames": len(frames),
        "all24_member_tests": frame_tests, "all24_member_failures": frame_failures,
        "all576_axis_tests": len(frames) ** 2 * 3, "all576_axis_failures": group_failures,
        "malformed_domain_refusals": refused, "malformed_domain_total": len(malformed),
        "pass": len(frames) == 24 and frame_failures == group_failures == 0 and refused == len(malformed),
    }
    check("all24/all576 conditional-occurrence covariance and malformed-domain controls remain exact", result["pass"], result)
    return result


def dependency_discipline_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    body = " ".join(note.lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "state-family", "off-grid", "nearest-neighbor", "all 24", "all 576",
        "coherent grade register is not objective probability", "rotor frequency is not born",
        "schedule is not time", "spent resource is not energy", "packet is not record",
        "supplied / derived / open", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "n1 status: fail", "no axiom pressure", "cycle-597-local",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    declared = re.search(r"Runner SHA-256:\s*([0-9a-f]{64})", note)

    routes = (
        {"family": "coherent projector-query tuple register", "object": "Cycle577 projectors and Cycle580 extraction unitary", "mechanism": "four-copy coherent query sector weights", "status": "ATTEMPTED", "terminal": "derive a reusable numeric grade without supplied identical copies or sector selection"},
        {"family": "reversible fixed-point product synthesizer", "object": "unary parameter registers and 4x4x4 microaddress mask", "mechanism": "reversible literal products", "status": "ATTEMPTED", "terminal": "derive the parameter-register/state calibration and expand family/precision"},
        {"family": "deterministic lattice rotor", "object": "one-carrier 64-cycle and derived grade mask", "mechanism": "exhaustively bounded +25 discrepancy", "status": "ATTEMPTED", "terminal": "derive Born calibration, actuality, and archive renewal"},
        {"family": "full quantum amplitude estimation", "object": "phase/kickback grade register", "mechanism": "controlled projector reflections", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "compile controlled reflections, phase arithmetic, copy supply, and error bound locally"},
        {"family": "renewable stochastic reservoir", "object": "stationary local bath transition kernel", "mechanism": "mixing invariant measure", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "derive kernel, invariant law, resource renewal, and actuality owner"},
        {"family": "adaptive physical tomography", "object": "renewable calibration corpus and estimator", "mechanism": "confidence-controlled state-family learning", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "derive independent trials, estimator dynamics, stopping rule, and Record semantics"},
    )
    qualifying = tuple(route for route in routes if route["status"] == "ATTEMPTED")
    walls = (
        "state-to-parameter calibration", "state-family and precision coverage", "objective actuality",
        "Record permanence", "frequency-to-Born calibration", "resource renewal",
    )
    pairs = tuple({
        "pair": (walls[left], walls[right]),
        "left_closes_right": False, "right_closes_left": False, "independent": True,
        "reason": "the two conditions have distinct typed witnesses and neither construction supplies the other",
    } for left, right in combinations(range(len(walls)), 2))
    hidden = (
        "four identically prepared input copies", "two-bit unary parameter/state calibration",
        "blank pointer/copy/work/mask/archive M2", "finite 64-address chart and rotor genesis",
        "Cycle552 conditional member/history interface", "finite corpus sizes and held preparations",
    )
    residuals = (
        {"witness": "Cycle595 finite answer ROM/off-grid refusal", "current_residual": "replace state-specific rows on declared product family", "match": True, "disposition": "closed only at two-bit parameter precision"},
        {"witness": "Cycle580 local unitary/inverse compiler", "current_residual": "physical projector-query locality and inverse", "match": True, "disposition": "exact shore, no probability semantics"},
        {"witness": "Cycle577 projector instrument", "current_residual": "Z-X-Z grade formula", "match": True, "disposition": "exact projector identity"},
        {"witness": "Cycle592 occurrence/frequency bridge", "current_residual": "conditional occurrence and finite frequency propagation", "match": True, "disposition": "frequency retained without Born promotion"},
    )
    partial = (
        "retain Route A as a coherent projector-query diagnostic",
        "retain Route B/C as a finite-precision product-family compiler",
        "increase unary precision and prove scalable local arithmetic bounds",
        "derive parameter-register/state calibration without answer rows",
        "derive renewable archive formation and separate actuality/Record law",
    )
    steelman = {
        "mechanism": "a locally compiled controlled-reflection amplitude-estimation network could transform the exact Cycle577 query into a reusable b-bit grade register, while a scalable reversible comparator and renewable record medium remove the supplied parameter word and archive debit",
        "terminal": "construct controlled reflections, copy/source ledger, phase-error theorem, scalable NN arithmetic, actuality owner, and blinded renewable Records",
        "status": "open and therefore defeats any broad no-go",
    }
    echo = (
        "Cycle577 turned projector identities into an exact local instrument without actuality",
        "Cycle580 retired the host-gate compiler import but not query-copy or Born semantics",
        "Cycle592 exposed the finite answer-ROM and frequency-calibration imports",
        "Cycle595 retired the balanced innovation word with an orbit-index carrier but retained the state-family wall",
        "Cycle597 retires per-state rows only for one fixed-precision product family",
    )
    discipline = {
        "N1_routes": routes, "N1_qualifying": len(qualifying), "N1_required": 5, "N1_status": "FAIL",
        "N2_collapsed_walls": walls, "N2_pairwise": pairs,
        "N3_explicit_supplies": hidden, "N3_hidden_phrase_scan": "all load-bearing construction choices promoted to supplied inventory",
        "N4_residual_matches": residuals,
        "N5_rhetoric": (
            "coherent grade register statement is scoped to the tested four-copy block, not lattice-wide",
            "rotor-frequency statement is scoped to finite declared corpora, not every asymptotic process",
            "schedule/time, resource/energy, and packet/Record are typed non-promotions at the constructed block",
        ),
        "N6_partial_closure_paths": partial, "N6_new_axiom_required": False,
        "N7_steelman": steelman, "N8_cross_cycle_echo": echo,
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction": "NOT_ESTABLISHED", "axiom_pressure": "NONE",
    }
    result = {
        "expected": FROZEN, "observed": observed,
        "synthesis_law_sha256": SYNTHESIS_LAW_SHA256,
        "expected_synthesis_law_sha256": EXPECTED_SYNTHESIS_LAW_SHA256,
        "held_declaration_sha256": HELD_SHA256,
        "note_missing": missing,
        "declared_runner_sha256": declared.group(1) if declared else None,
        "runner_sha256": file_sha(Path(__file__)),
        "discipline": discipline,
        "inventory": {
            "supplied": hidden,
            "derived": (
                "exact coherent projector-query distribution and inverse",
                "one row-free reversible denominator-64 product-family grade mask",
                "deterministic physical rotor with exhaustive finite discrepancy certificate",
                "explicit approximation plus rotor-frequency error budgets through conditional occurrence",
            ),
            "open": (
                "objective actuality and framework Record", "Born/probability calibration",
                "state-to-parameter ownership and family/precision scaling", "copy/archive renewal",
                "time, energy, source, stress, gravity, noise, and infinite-volume integration",
            ),
        },
        "pass": observed == FROZEN and SYNTHESIS_LAW_SHA256 == EXPECTED_SYNTHESIS_LAW_SHA256
        and not missing and declared is not None and declared.group(1) == file_sha(Path(__file__))
        and len(qualifying) == 3 and len(pairs) == 15 and len(residuals) == 4 and len(partial) == len(echo) == 5,
    }
    check("exact shores, rule-before-held freeze, inventory, and full N1-N8 prevent state-family and Born overclaim", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_result: str = "one reversible row-free denominator-64 product-family grade synthesizer feeding a deterministic local rotor and unchanged conditional occurrence"
    objective_actuality: None = None
    framework_Record: None = None
    derived_Born_probability: None = None
    physical_time: None = None
    energy_or_source: None = None
    axiom_pressure: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle597 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        route_a = route_a_controls()
        route_b = route_b_controls()
        route_c = route_c_controls()
        covariance = covariance_domain_controls()
        dependency = dependency_discipline_controls()
        resources = {
            "elapsed_seconds": time.perf_counter() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_bytes": RSS_CAP_BYTES,
        }
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["maximum_RSS_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "route_A": route_a, "route_B": route_b, "route_C": route_c,
            "covariance_domain": covariance, "dependency_discipline_inventory": dependency,
            "resources": resources, "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; coherent grade register is not objective probability; rotor frequency is not Born; schedule is not time; spent resource is not energy; packet is not Record")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
