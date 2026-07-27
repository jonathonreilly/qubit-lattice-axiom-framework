#!/usr/bin/env python3
"""Cycle716: same-code six-port admission candidates.

This bounded runner asks a narrow constructive question on the Cycle713/714 physical-M2 lineage:

* can all six seam-opportunity bits incident on one M64 cell be produced in one
  shared physical code block;
* can fixed local reversible circuits expose more than one candidate admission
  relation without a run-time table, host winner, or copied branch-ray state;
* and which of those outputs is already type-correct for the landed finite
  proper-cubic admission-table discriminator?

The two candidate laws are compile-time gate words, not Nature's
Admissibility.  ``unique_quorum`` accepts weight one.  ``odd_shells`` accepts
weights one, three, and five.  Both retain the whole archive, admitted
alternative mask, rejected mask, empty flag, and collision flag coherently.
Only the unique-quorum output fits the landed lane-zero grammar without adding
a winner selector.  The odd-shell refusal is a representation/type result, not
an impossibility claim.

No audit, axiom, Record, actuality, Born, source, gravity, energy, or physical
time claim is made here.  The circuit ordinal is a fixed controller schedule.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 300
NOTE_PATH = "docs/SAME_CODE_SIX_PORT_ADMISSION_CYCLE716_BOUNDED_CONSTRUCTION_NOTE_2026-07-26.md"
AUDIT_INPUT_PATHS = (
    "docs/SAME_CODE_SIX_PORT_ADMISSION_CYCLE716_BOUNDED_CONSTRUCTION_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/finite_proper_cubic_admission_table_discriminator_2026_07_23.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle716_same_code_six_port_admission_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import finite_proper_cubic_admission_table_discriminator_2026_07_23 as DISC
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714


TOL = 3e-10
DIRECTIONS = DISC.DIRECTIONS
OPPOSITE = (1, 0, 3, 2, 5, 4)
STAR_CENTER = (1, 1, 1)
STAR_NEIGHBORS = tuple(
    tuple(STAR_CENTER[axis] + direction[axis] for axis in range(3))
    for direction in DIRECTIONS
)
BOX_CELLS = C712.C709.G.box_cells((3, 3, 3))
SELECTED_CELLS = (STAR_CENTER,) + STAR_NEIGHBORS


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]


def cn(control: int, target: int, kind: str = "CNOT") -> Gate:
    return Gate(kind, (control, target))


def tof(a: int, b: int, target: int, kind: str = "TOF") -> Gate:
    return Gate(kind, (a, b, target))


def xx(target: int, kind: str = "X") -> Gate:
    return Gate(kind, (target,))


# Candidate-register layout.  INPUT aliases the six retained seam pointers.
INPUT = tuple(range(6))
ARCHIVE = tuple(range(6, 12))
ELIGIBLE = tuple(range(12, 18))
LOSERS = tuple(range(18, 24))
ACCEPT, COLLISION, EMPTY, READY, SPENT, EDGE = range(24, 30)
MEMBER, RECEIPT = 30, 31
SNAPSHOT = (32, 33, 34)
SEEN = tuple(range(35, 41))
PAIR = tuple(range(41, 46))
COLLISION_CHAIN = tuple(range(46, 51))
CANDIDATE_QUBITS = 51
OUTPUT_QUBITS = tuple(range(6, 35))
WORK_QUBITS = SEEN + PAIR + COLLISION_CHAIN


def or_into(left: int, right: int, target: int, prefix: str) -> tuple[Gate, ...]:
    """Compute target ^= left OR right for clean target."""
    return (
        cn(left, target, prefix + "_left"),
        cn(right, target, prefix + "_right"),
        tof(left, right, target, prefix + "_and"),
    )


def feature_word() -> tuple[Gate, ...]:
    """Reversibly compute nonempty and collision features into work chains."""
    word: list[Gate] = [cn(INPUT[0], SEEN[0], "seen_seed")]
    for index in range(1, 6):
        previous_seen = SEEN[index - 1]
        pair = PAIR[index - 1]
        collision = COLLISION_CHAIN[index - 1]
        word.append(tof(previous_seen, INPUT[index], pair, "collision_pair"))
        if index == 1:
            word.append(cn(pair, collision, "collision_seed"))
        else:
            word.extend(or_into(
                COLLISION_CHAIN[index - 2], pair, collision, "collision_OR"
            ))
        word.extend(or_into(previous_seen, INPUT[index], SEEN[index], "seen_OR"))
    return tuple(word)


def inverse_semantic_word(word: tuple[Gate, ...]) -> tuple[Gate, ...]:
    # X, CNOT, and Toffoli are all self-inverse.
    return tuple(reversed(word))


def candidate_word(law: str) -> tuple[Gate, ...]:
    """Compile one fixed law; ``law`` is construction-time, never a run-time rail."""
    if law not in ("unique_quorum", "odd_shells"):
        raise ValueError(law)
    feature = feature_word()
    word: list[Gate] = []
    for source, archive, loser in zip(INPUT, ARCHIVE, LOSERS):
        word.append(cn(source, archive, "archive_copy"))
        word.append(cn(source, loser, "rejected_copy"))
    word.extend(feature)
    word.append(cn(COLLISION_CHAIN[-1], COLLISION, "collision_output"))
    word.append(xx(EMPTY, "empty_not"))
    word.append(cn(SEEN[-1], EMPTY, "empty_from_seen"))
    if law == "unique_quorum":
        word.append(xx(COLLISION_CHAIN[-1], "unique_negative_control_open"))
        word.append(tof(
            SEEN[-1], COLLISION_CHAIN[-1], ACCEPT, "unique_accept"
        ))
        word.append(xx(COLLISION_CHAIN[-1], "unique_negative_control_close"))
    else:
        for source in INPUT:
            word.append(cn(source, ACCEPT, "odd_parity_accept"))
    for source, eligible, loser in zip(INPUT, ELIGIBLE, LOSERS):
        word.append(tof(ACCEPT, source, eligible, "eligible_copy"))
        word.append(tof(ACCEPT, source, loser, "admitted_remove_from_losers"))
    word.append(xx(READY, "ready_not"))
    word.append(cn(ACCEPT, READY, "ready_from_accept"))
    for target, kind in (
        (SPENT, "spent_copy"),
        (EDGE, "edge_copy"),
        (MEMBER, "member_copy"),
        (RECEIPT, "receipt_copy"),
        (SNAPSHOT[0], "snapshot_precommit_copy"),
        (SNAPSHOT[1], "snapshot_occurrence_copy"),
        (SNAPSHOT[2], "snapshot_atom_copy"),
    ):
        word.append(cn(ACCEPT, target, kind))
    word.extend(inverse_semantic_word(feature))
    return tuple(word)


def apply_gate(bits: tuple[int, ...], gate: Gate) -> tuple[int, ...]:
    output = list(bits)
    if len(gate.wires) == 1:
        output[gate.wires[0]] ^= 1
    elif len(gate.wires) == 2:
        control, target = gate.wires
        output[target] ^= output[control]
    elif len(gate.wires) == 3:
        left, right, target = gate.wires
        output[target] ^= output[left] & output[right]
    else:
        raise ValueError(gate)
    return tuple(output)


def apply_word(bits: tuple[int, ...], word: tuple[Gate, ...]) -> tuple[int, ...]:
    output = bits
    for gate in word:
        output = apply_gate(output, gate)
    return output


def initial_candidate(word: tuple[int, ...], dirty: int | None = None) -> tuple[int, ...]:
    bits = [0] * CANDIDATE_QUBITS
    for wire, value in zip(INPUT, word):
        bits[wire] = value
    if dirty is not None:
        bits[dirty] = 1
    return tuple(bits)


def candidate_expected(word: tuple[int, ...], law: str) -> dict[str, object]:
    weight = sum(word)
    accept = int(weight == 1) if law == "unique_quorum" else weight % 2
    eligible = tuple(bit & accept for bit in word)
    return {
        "accept": accept,
        "archive": word,
        "eligible": eligible,
        "losers": tuple(bit ^ admitted for bit, admitted in zip(word, eligible)),
        "collision": int(weight >= 2),
        "empty": int(weight == 0),
        "ready": 1 - accept,
        "spent": accept,
        "edge": accept,
        "member": accept,
        "receipt": accept,
        "snapshot": (accept, accept, accept),
    }


def read_candidate(bits: tuple[int, ...]) -> dict[str, object]:
    return {
        "accept": bits[ACCEPT],
        "archive": tuple(bits[q] for q in ARCHIVE),
        "eligible": tuple(bits[q] for q in ELIGIBLE),
        "losers": tuple(bits[q] for q in LOSERS),
        "collision": bits[COLLISION],
        "empty": bits[EMPTY],
        "ready": bits[READY],
        "spent": bits[SPENT],
        "edge": bits[EDGE],
        "member": bits[MEMBER],
        "receipt": bits[RECEIPT],
        "snapshot": tuple(bits[q] for q in SNAPSHOT),
    }


def candidate_to_port(fields: dict[str, object]) -> DISC.PortTuple:
    accept = int(fields["accept"])
    return DISC.PortTuple(
        archive=tuple(fields["archive"]),
        losers=tuple(fields["losers"]),
        ready=int(fields["ready"]),
        spent=int(fields["spent"]),
        edge=int(fields["edge"]),
        member=(int(fields["member"]), 0, 0, 0, 0),
        receipt=(int(fields["receipt"]), 0, 0, 0, 0),
        snapshot=tuple(fields["snapshot"]) + (0,) * 9,
    )


def candidate_certificate() -> dict[str, object]:
    frames = DISC.proper_cubic_frames()
    report: dict[str, object] = {}
    outputs: dict[str, dict[tuple[int, ...], dict[str, object]]] = {}
    for law in ("unique_quorum", "odd_shells"):
        gate_word = candidate_word(law)
        inverse = inverse_semantic_word(gate_word)
        fields_by_word = {}
        equation_failures = inverse_failures = work_failures = 0
        for word in DISC.WORDS:
            before = initial_candidate(word)
            after = apply_word(before, gate_word)
            fields = read_candidate(after)
            fields_by_word[word] = fields
            equation_failures += fields != candidate_expected(word, law)
            inverse_failures += apply_word(after, inverse) != before
            work_failures += any(after[q] for q in WORK_QUBITS)
        outputs[law] = fields_by_word

        # Coherent comparison: a sparse state with support on all 64 clean rows.
        amplitudes = {
            sum(bit << wire for wire, bit in zip(INPUT, word)):
            complex(math.cos(index + 0.25), math.sin(2 * index + 0.5))
            for index, word in enumerate(DISC.WORDS)
        }
        norm = math.sqrt(sum(abs(value) ** 2 for value in amplitudes.values()))
        amplitudes = {basis: value / norm for basis, value in amplitudes.items()}
        observed: dict[int, complex] = {}
        expected_state: dict[int, complex] = {}
        for source, amplitude in amplitudes.items():
            before = tuple((source >> q) & 1 for q in range(CANDIDATE_QUBITS))
            after = apply_word(before, gate_word)
            target = sum(bit << q for q, bit in enumerate(after))
            observed[target] = observed.get(target, 0.0j) + amplitude
            word = tuple(before[q] for q in INPUT)
            expected_bits = list(before)
            expected = candidate_expected(word, law)
            for key, wires in (
                ("archive", ARCHIVE), ("eligible", ELIGIBLE),
                ("losers", LOSERS), ("snapshot", SNAPSHOT),
            ):
                for wire, value in zip(wires, expected[key]):
                    expected_bits[wire] = value
            for key, wire in (
                ("accept", ACCEPT), ("collision", COLLISION), ("empty", EMPTY),
                ("ready", READY), ("spent", SPENT), ("edge", EDGE),
                ("member", MEMBER), ("receipt", RECEIPT),
            ):
                expected_bits[wire] = int(expected[key])
            expected_target = sum(bit << q for q, bit in enumerate(expected_bits))
            expected_state[expected_target] = expected_state.get(expected_target, 0.0j) + amplitude
        keys = set(observed) | set(expected_state)
        coherent_residual = math.sqrt(sum(
            abs(observed.get(key, 0.0j) - expected_state.get(key, 0.0j)) ** 2
            for key in keys
        ))

        # Proper-cubic covariance of the directional outputs and scalar features.
        frame_failures = 0
        for word in DISC.WORDS:
            base = fields_by_word[word]
            for frame in frames:
                rotated_word = DISC.rotate_six(word, frame)
                rotated = fields_by_word[rotated_word]
                frame_failures += rotated["archive"] != DISC.rotate_six(base["archive"], frame)
                frame_failures += rotated["eligible"] != DISC.rotate_six(base["eligible"], frame)
                frame_failures += rotated["losers"] != DISC.rotate_six(base["losers"], frame)
                for scalar in (
                    "accept", "collision", "empty", "ready", "spent", "edge",
                    "member", "receipt", "snapshot",
                ):
                    frame_failures += rotated[scalar] != base[scalar]

        # Active deletions and dirty-domain rows.
        selectors = {
            "law_gate": lambda gate: gate.kind in ("unique_accept", "odd_parity_accept"),
            "archive_copy": lambda gate: gate.kind == "archive_copy",
            "collision_pair": lambda gate: gate.kind == "collision_pair",
            "eligible_copy": lambda gate: gate.kind == "eligible_copy",
            "ready_from_accept": lambda gate: gate.kind == "ready_from_accept",
        }
        deletion_differences = {}
        for label, selector in selectors.items():
            index = next(i for i, gate in enumerate(gate_word) if selector(gate))
            damaged = gate_word[:index] + gate_word[index + 1:]
            deletion_differences[label] = sum(
                read_candidate(apply_word(initial_candidate(word), damaged))
                != fields_by_word[word]
                for word in DISC.WORDS
            )
        dirty_rows = (SEEN[0], PAIR[0], ARCHIVE[0], ACCEPT)
        dirty_rejected = 0
        dirty_differences = {}
        clean_reference = apply_word(initial_candidate((1, 0, 0, 0, 0, 0)), gate_word)
        for dirty in dirty_rows:
            dirty_after = apply_word(
                initial_candidate((1, 0, 0, 0, 0, 0), dirty), gate_word
            )
            # These rows are outside the declared clean-output/clean-work code.
            rejected = any(initial_candidate((1, 0, 0, 0, 0, 0), dirty)[q]
                           for q in OUTPUT_QUBITS + WORK_QUBITS)
            dirty_rejected += int(rejected)
            dirty_differences[str(dirty)] = sum(
                left != right for left, right in zip(dirty_after, clean_reference)
            )

        report[law] = {
            "semantic_gates": len(gate_word),
            "gate_census": dict(Counter(g.kind for g in gate_word)),
            "all_64_equation_failures": equation_failures,
            "all_64_inverse_failures": inverse_failures,
            "all_64_work_cleanup_failures": work_failures,
            "coherent_all_64_residual": coherent_residual,
            "proper_cubic_frame_rows": 64 * 24,
            "proper_cubic_output_failures": frame_failures,
            "deletion_difference_counts": deletion_differences,
            "dirty_rows": len(dirty_rows),
            "dirty_rows_rejected": dirty_rejected,
            "dirty_output_difference_counts": dirty_differences,
        }

    unique_stream = [candidate_to_port(outputs["unique_quorum"][word]) for word in DISC.WORDS]
    odd_stream = [candidate_to_port(outputs["odd_shells"][word]) for word in DISC.WORDS]
    unique_verdict = DISC.discriminate(unique_stream, DISC.RULES, frames)
    odd_verdict = DISC.discriminate(odd_stream, DISC.RULES, frames)
    odd_malformed = sum(not DISC.port_well_formed(port)[0] for port in odd_stream)
    report["discriminator_bridge"] = {
        "unique_quorum_verdict": unique_verdict,
        "unique_quorum_well_formed_ports": sum(
            DISC.port_well_formed(port)[0] for port in unique_stream
        ),
        "odd_shells_verdict": odd_verdict,
        "odd_shells_malformed_ports": odd_malformed,
        "odd_shells_malformed_weights": sorted({
            sum(port.archive) for port in odd_stream
            if not DISC.port_well_formed(port)[0]
        }),
        "interpretation": (
            "unique quorum needs no winner convention because every admitted word has one bit; "
            "odd-shell admitted weights 3 and 5 retain all alternatives and therefore fail the "
            "landed grammar's exactly-one-cleared-loser clause"
        ),
    }
    return report


def cell_mode(cell: tuple[int, int, int], direction: int) -> int:
    return 6 * BOX_CELLS.index(cell) + direction


def star_endpoints() -> tuple[tuple[int, int], ...]:
    return tuple(
        (cell_mode(STAR_CENTER, OPPOSITE[direction]),
         cell_mode(STAR_NEIGHBORS[direction], direction))
        for direction in range(6)
    )


def adjacent_fswap_transposition(left: int, right: int) -> tuple[C712.AGate, ...]:
    lo, hi = sorted((left, right))
    adjacent = tuple((wire, wire + 1) for wire in range(lo, hi))
    pairs = adjacent + tuple(reversed(adjacent[:-1]))
    # The walk swaps logical modes lo and hi.  It is symmetric in the endpoint
    # labels; endpoint order matters only for the retained directional tag.
    return tuple(C712.AGate("star_seam_FSWAP", pair, C712.FSWAP) for pair in pairs)


def star_seam_instrument_word(aux_base: int) -> tuple[C712.AGate, ...]:
    output: list[C712.AGate] = []
    for direction, (left, right) in enumerate(star_endpoints()):
        du, dv, pointer = (aux_base + 3 * direction + offset for offset in range(3))
        before, after, clean = C713.endpoint_register_word(left, right, du, dv, pointer)
        output.extend(before)
        output.extend(adjacent_fswap_transposition(left, right))
        output.extend(after)
        output.extend(clean)
    return tuple(output)


def contact_word() -> tuple[C712.AGate, ...]:
    phase = np.diag((1, 1, 1, np.exp(1j * C712.F128.CONTACT))).astype(complex)
    output = []
    for cell in SELECTED_CELLS:
        offset = 6 * BOX_CELLS.index(cell)
        for left in range(6):
            for right in range(left + 1, 6):
                output.append(C712.AGate(
                    "star_onsite_contact", (offset + left, offset + right), phase
                ))
    return tuple(output)


def local_coin_reverse_word() -> tuple[C712.AGate, ...]:
    coin, _mass, _phase = C712.F128.common_coin()
    schedule, residual = C712.S25.compile_adjacent_qr(coin)
    if residual >= TOL:
        raise AssertionError(("coin QR", residual))
    output: list[C712.AGate] = []
    for cell in SELECTED_CELLS:
        offset = 6 * BOX_CELLS.index(cell)
        output.extend(
            C712.AGate("star_" + kind, tuple(offset + q for q in wires), matrix)
            for kind, wires, matrix in schedule
        )
        for left, right in ((0, 1), (2, 3), (4, 5)):
            output.append(C712.AGate(
                "star_reverse_FSWAP", (offset + left, offset + right), C712.FSWAP
            ))
    return tuple(output)


def apply_sparse_basis(source: int, word: tuple[C712.AGate, ...]) -> dict[int, complex]:
    return C713.apply_sparse_word({source: 1.0 + 0.0j}, word)


def fermionic_permutation_amplitude(source: int, permutation: tuple[int, ...]) -> tuple[int, int]:
    occupied = [mode for mode in range(len(permutation)) if (source >> mode) & 1]
    targets = [permutation[mode] for mode in occupied]
    inversions = sum(targets[i] > targets[j] for i in range(len(targets))
                     for j in range(i + 1, len(targets)))
    target = 0
    for mode in targets:
        target |= 1 << mode
    return target, -1 if inversions % 2 else 1


def seam_permutation(modes: int) -> tuple[int, ...]:
    permutation = list(range(modes))
    for left, right in star_endpoints():
        permutation[left], permutation[right] = permutation[right], permutation[left]
    return tuple(permutation)


def contact_phase(target: int) -> complex:
    exponent = 0
    for cell in SELECTED_CELLS:
        offset = 6 * BOX_CELLS.index(cell)
        number = ((target >> offset) & 0x3F).bit_count()
        exponent += number * (number - 1) // 2
    return np.exp(1j * C712.F128.CONTACT * exponent)


def seam_instrument_certificate() -> dict[str, object]:
    matter_modes = 6 * len(BOX_CELLS)
    aux_base = matter_modes
    word = star_seam_instrument_word(aux_base) + contact_word()
    permutation = seam_permutation(matter_modes)
    endpoints = star_endpoints()
    rng = np.random.default_rng(713_6)
    cases: list[tuple[str, int]] = []
    # Complete directional truth domain: right endpoint zero, left carries word.
    for index, opportunity in enumerate(DISC.WORDS):
        source = 0
        for bit, (left, _right) in zip(opportunity, endpoints):
            source |= bit << left
        cases.append((f"word:{index}", source))
    cases.append((
        "contact:0",
        # These two neighbor endpoints land in center modes 0 and 1 after the
        # first two seam transpositions, activating the first center contact.
        (1 << endpoints[0][1]) | (1 << endpoints[1][1]),
    ))
    # Hostile backgrounds populate arbitrary selected and exterior matter modes.
    for index in range(384):
        source = 0
        density = (index % 9) + 1
        for mode in range(matter_modes):
            if int(rng.integers(0, density + 2)) == 0:
                source |= 1 << mode
        cases.append((f"held:{index}", source))

    support_failures = target_failures = pointer_failures = scratch_failures = 0
    phase_residual = norm_residual = 0.0
    opportunity_census = Counter()
    expected_rows = {}
    for label, source in cases:
        observed = apply_sparse_basis(source, word)
        support_failures += len(observed) != 1
        if len(observed) != 1:
            continue
        target_full, amplitude = next(iter(observed.items()))
        expected_target, sign = fermionic_permutation_amplitude(source, permutation)
        expected_amp = sign * contact_phase(expected_target)
        target_matter = target_full & ((1 << matter_modes) - 1)
        target_failures += target_matter != expected_target
        phase_residual = max(phase_residual, abs(amplitude - expected_amp))
        norm_residual = max(norm_residual, abs(abs(amplitude) - 1.0))
        opportunity = tuple(
            ((source >> left) & 1) ^ ((source >> right) & 1)
            for left, right in endpoints
        )
        observed_pointer = tuple(
            (target_full >> (aux_base + 3 * direction + 2)) & 1
            for direction in range(6)
        )
        pointer_failures += observed_pointer != opportunity
        scratch_failures += any(
            (target_full >> (aux_base + 3 * direction + offset)) & 1
            for direction in range(6) for offset in (0, 1)
        )
        opportunity_census[opportunity] += 1
        expected_rows[label] = (expected_target, expected_amp, opportunity)

    deletion_results = {}
    deletion_selectors = {
        "first_prewrite": lambda gate: gate.kind == "endpoint_pre_left",
        "first_seam_FSWAP": lambda gate: gate.kind == "star_seam_FSWAP",
        "first_OR_Toffoli_factor": lambda gate: gate.kind == "endpoint_OR_Toffoli_H",
        "first_contact": lambda gate: gate.kind == "star_onsite_contact",
    }
    for deletion, selector in deletion_selectors.items():
        index = next(i for i, gate in enumerate(word) if selector(gate))
        damaged = word[:index] + word[index + 1:]
        differences = 0
        maximum = 0.0
        for label, source in cases[:64] + cases[64:96]:
            observed = apply_sparse_basis(source, damaged)
            expected_target, expected_amp, opportunity = expected_rows[label]
            expected_full = expected_target
            for direction, bit in enumerate(opportunity):
                expected_full |= bit << (aux_base + 3 * direction + 2)
            delta = {
                key: observed.get(key, 0.0j)
                - (expected_amp if key == expected_full else 0.0j)
                for key in set(observed) | {expected_full}
            }
            residual = math.sqrt(sum(abs(value) ** 2 for value in delta.values()))
            maximum = max(maximum, residual)
            differences += residual > TOL
        deletion_results[deletion] = {
            "tested_rows": 96,
            "difference_rows": differences,
            "maximum_residual": maximum,
        }

    clean_source = 1 << endpoints[0][0]
    clean_output = apply_sparse_basis(clean_source, word)
    dirty_rows_rejected = 0
    dirty_difference_residuals = {}
    for dirty_offset in (0, 1, 2, 3, 5):
        source = clean_source | (1 << (aux_base + dirty_offset))
        dirty_rows_rejected += int(any(
            (source >> (aux_base + offset)) & 1 for offset in range(18)
        ))
        dirty_output = apply_sparse_basis(source, word)
        keys = set(clean_output) | set(dirty_output)
        dirty_difference_residuals[str(dirty_offset)] = math.sqrt(sum(
            abs(dirty_output.get(key, 0.0j) - clean_output.get(key, 0.0j)) ** 2
            for key in keys
        ))

    return {
        "box_cells": len(BOX_CELLS),
        "selected_star_cells": len(SELECTED_CELLS),
        "matter_modes": matter_modes,
        "shared_center_endpoint_modes": tuple(left for left, _ in endpoints),
        "neighbor_endpoint_modes": tuple(right for _, right in endpoints),
        "unique_shared_center_endpoint_modes": len({left for left, _ in endpoints}),
        "unique_all_endpoint_modes": len({q for pair in endpoints for q in pair}),
        "instrument_gate_census": dict(Counter(g.kind for g in word)),
        "tested_basis_rows": len(cases),
        "complete_direction_words_seen": len({word for word in opportunity_census}),
        "support_failures": support_failures,
        "matter_target_failures": target_failures,
        "pointer_truth_failures": pointer_failures,
        "scratch_cleanup_failures": scratch_failures,
        "maximum_phase_residual": phase_residual,
        "maximum_norm_residual": norm_residual,
        "deletion_controls": deletion_results,
        "dirty_ancilla_rows": 5,
        "dirty_ancilla_rows_rejected": dirty_rows_rejected,
        "dirty_ancilla_output_difference_residuals": dirty_difference_residuals,
    }


def one_particle_certificate() -> dict[str, object]:
    modes = 6 * len(BOX_CELLS)
    compiled = np.eye(modes, dtype=complex)
    for gate in local_coin_reverse_word():
        local = np.eye(modes, dtype=complex)
        wires = gate.wires
        if len(wires) == 1:
            # A one-qubit number-preserving Fock gate contributes its occupied phase.
            local[wires[0], wires[0]] = gate.matrix[1, 1]
        else:
            one = gate.matrix[np.ix_((1, 2), (1, 2))]
            local[np.ix_(wires, wires)] = one
        compiled = local @ compiled
    # Seam instrument CNOTs touch auxiliaries and do not alter matter.  The seam
    # FSWAP walks have the following one-particle permutation.
    seam_matrix = C712.F128.permutation_matrix(seam_permutation(modes), modes)
    compiled = seam_matrix @ compiled

    coin, mass, _rest = C712.F128.common_coin()
    expected = np.eye(modes, dtype=complex)
    for cell in SELECTED_CELLS:
        offset = 6 * BOX_CELLS.index(cell)
        expected[offset:offset + 6, offset:offset + 6] = coin
    reverse_map = list(range(modes))
    for cell in SELECTED_CELLS:
        offset = 6 * BOX_CELLS.index(cell)
        for left, right in ((0, 1), (2, 3), (4, 5)):
            reverse_map[offset + left], reverse_map[offset + right] = (
                reverse_map[offset + right], reverse_map[offset + left]
            )
    expected = seam_matrix @ C712.F128.permutation_matrix(tuple(reverse_map), modes) @ expected
    uniform = np.ones(6, dtype=complex) / math.sqrt(6)
    eigenvalue = np.vdot(uniform, coin @ uniform)
    compiled_mass = float(np.angle(eigenvalue)) / (1 / 3)
    pair_semantics = C712.cycle230_semantic_certificate(C712.decoded_word(2)[0])
    return {
        "one_particle_dimension": modes,
        "star_free_one_particle_residual": float(np.linalg.norm(compiled - expected)),
        "one_particle_mass": compiled_mass,
        "Cycle230_mass": mass,
        "mass_residual": abs(compiled_mass - mass),
        "Cycle230_pair_semantic_reconciliation": pair_semantics,
    }


def expand_candidate_to_abstract(
    law: str, pointer_wires: tuple[int, ...], extra_base: int
) -> tuple[C712.AGate, ...]:
    mapping = {wire: pointer_wires[wire] for wire in INPUT}
    next_extra = extra_base
    for wire in range(6, CANDIDATE_QUBITS):
        mapping[wire] = next_extra
        next_extra += 1
    output: list[C712.AGate] = []
    for gate in candidate_word(law):
        wires = tuple(mapping[q] for q in gate.wires)
        if len(wires) == 1:
            # X = H S S H, all in the inherited one-M2 Clifford alphabet.
            target = wires[0]
            output.extend((
                C712.AGate("candidate_X_H", (target,), C712.c707.c655.H),
                C712.AGate("candidate_X_S", (target,), C712.c707.S_GATE),
                C712.AGate("candidate_X_S", (target,), C712.c707.S_GATE),
                C712.AGate("candidate_X_H", (target,), C712.c707.c655.H),
            ))
        elif len(wires) == 2:
            output.append(C712.AGate(
                "candidate_" + gate.kind, wires, C712.c707.c655.CNOT
            ))
        else:
            output.extend(C713.toffoli_word(*wires))
    return tuple(output)


def allocate_near(
    occupied: set[tuple[int, int, int]], anchors: tuple[tuple[int, int, int], ...], count: int
) -> tuple[tuple[int, int, int], ...]:
    center = tuple(round(sum(site[axis] for site in anchors) / len(anchors)) for axis in range(3))
    candidates = []
    for radius in range(0, 32):
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                for dz in range(-radius, radius + 1):
                    if max(abs(dx), abs(dy), abs(dz)) != radius:
                        continue
                    site = (center[0] + dx, center[1] + dy, center[2] + dz)
                    if site in occupied:
                        continue
                    distances = tuple(sum(abs(site[a] - anchor[a]) for a in range(3))
                                      for anchor in anchors)
                    candidates.append((max(distances), sum(distances), site))
        if len(candidates) >= count * 4:
            break
    selected = tuple(row[2] for row in sorted(candidates)[:count])
    if len(selected) != count or len(set(selected)) != count:
        raise AssertionError((count, len(selected), len(set(selected))))
    occupied.update(selected)
    return selected


def abstract_instruction_signature(gate: C712.AGate) -> tuple[object, ...]:
    return gate.kind, gate.wires, C712.c707.c655.matrix_digest(gate.matrix)


def primitive_expansion_certificate() -> dict[str, float]:
    x_compiled = (
        C712.c707.c655.H @ C712.c707.S_GATE @ C712.c707.S_GATE
        @ C712.c707.c655.H
    )
    x_expected = np.asarray(((0, 1), (1, 0)), dtype=complex)
    toffoli = C713.word_matrix(C713.toffoli_word(0, 1, 2), 3)
    return {
        "X_HSSH_residual": float(np.linalg.norm(x_compiled - x_expected)),
        "Toffoli_HTCNOT_residual": float(np.linalg.norm(toffoli - C713.exact_toffoli())),
    }


_PHYSICAL_COMMON: dict[str, object] | None = None


def physical_common() -> dict[str, object]:
    """Build the one shared code/placement/decoder once per runner process."""
    global _PHYSICAL_COMMON
    if _PHYSICAL_COMMON is not None:
        return _PHYSICAL_COMMON
    eq, graph, site_map, gauges, occupied_tuple, collisions = C712.P709.placement_bundle(BOX_CELLS)
    carriers = C712.carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    occupied = set(occupied_tuple)
    seam_sites = []
    for left, right in star_endpoints():
        seam_sites.extend(allocate_near(occupied, (wire_sites[left], wire_sites[right]), 3))
    seam_sites = tuple(seam_sites)
    candidate_extra_sites = allocate_near(
        occupied, tuple(wire_sites[cell_mode(STAR_CENTER, d)] for d in range(6)),
        CANDIDATE_QUBITS - 6,
    )
    target_decode = C712.synthesize_decode(eq.target_w, eq.target_v)
    _PHYSICAL_COMMON = {
        "eq": eq,
        "carriers": carriers,
        "wire_sites": wire_sites,
        "repeated": repeated,
        "occupied_tuple": occupied_tuple,
        "collisions": collisions,
        "seam_sites": seam_sites,
        "candidate_extra_sites": candidate_extra_sites,
        "target_decode": target_decode,
    }
    return _PHYSICAL_COMMON


def physical_certificate(law: str) -> dict[str, object]:
    common = physical_common()
    eq = common["eq"]
    carriers = common["carriers"]
    wire_sites = common["wire_sites"]
    repeated = common["repeated"]
    occupied_tuple = common["occupied_tuple"]
    collisions = common["collisions"]
    seam_sites = common["seam_sites"]
    candidate_extra_sites = common["candidate_extra_sites"]
    endpoints = star_endpoints()
    pointer_sites = tuple(seam_sites[3 * direction + 2] for direction in range(6))
    extended_sites = wire_sites + seam_sites + candidate_extra_sites
    aux_base = eq.qubits
    pointer_wires = tuple(aux_base + 3 * direction + 2 for direction in range(6))
    candidate_extra_base = aux_base + len(seam_sites)

    target_decode = common["target_decode"]
    target_encode = C712.inverse_word(target_decode)
    logical_word = (
        local_coin_reverse_word()
        + star_seam_instrument_word(aux_base)
        + contact_word()
        + expand_candidate_to_abstract(law, pointer_wires, candidate_extra_base)
    )
    repetition_decode = tuple(
        C712.c707.Instruction(
            "star_repetition_decode_CNOT", carriers[index], C712.c707.c655.CNOT
        ) for index in repeated
    )
    repetition_encode = tuple(
        C712.c707.Instruction(
            "star_repetition_encode_CNOT", carriers[index], C712.c707.c655.CNOT
        ) for index in reversed(repeated)
    )
    physical_word = (
        repetition_decode
        + C712.abstract_to_physical(target_decode, extended_sites, "star_target_decode_")
        + C712.abstract_to_physical(logical_word, extended_sites, "star_decoded_")
        + C712.abstract_to_physical(target_encode, extended_sites, "star_target_encode_")
        + repetition_encode
    )
    routed, route = C712.c707.route_word(physical_word)
    assigned = set(occupied_tuple) | set(seam_sites) | set(candidate_extra_sites)
    touched = set(route["touched_coordinates"])

    # Translation and active-frame audits use the actual routed physical word.
    translations = ((0, 0, 0), (37, -19, 11), (-23, 31, -7))
    unit_steps = DIRECTIONS
    translation_failures = 0
    # Since route_word has already checked every two-site routed gate is NN,
    # translation covariance reduces exactly to the six possible unit steps.
    for shift in translations:
        for step in unit_steps:
            left = shift
            right = tuple(shift[axis] + step[axis] for axis in range(3))
            translation_failures += sum(abs(left[a] - right[a]) for a in range(3)) != 1

    frames = C712.C709.F.base.proper_cubic_frames()
    physical_frame_failures = 0
    frame_images = []
    for frame in frames:
        def rotate(site):
            return tuple(int(sum(frame[row, col] * site[col] for col in range(3)))
                         for row in range(3))
        image = tuple(rotate(site) for site in sorted(assigned))
        frame_images.append(image)
        physical_frame_failures += len(set(image)) != len(assigned)
        # Signed permutations preserve each of the six possible NN steps.  In
        # conjunction with route_word's all-gate NN scan this covers every
        # routed two-site instruction without a 24 x 1.3M redundant replay.
        for step in unit_steps:
            rotated_step = rotate(step)
            physical_frame_failures += sum(abs(value) for value in rotated_step) != 1
    composition_failures = 0
    assigned_sorted = tuple(sorted(assigned))
    for left in frames:
        for right in frames:
            product_frame = left @ right
            for site in assigned_sorted:
                composed = tuple(int(sum(left[row, middle] * sum(
                    right[middle, col] * site[col] for col in range(3)
                ) for middle in range(3))) for row in range(3))
                direct = tuple(int(sum(product_frame[row, col] * site[col]
                                       for col in range(3))) for row in range(3))
                composition_failures += composed != direct

    # The 27-cell code is shared: all six central ports are distinct wires of
    # one equivalence, not six copies of the central branch state.
    central_carriers = tuple(wire_sites[left] for left, _right in endpoints)
    return {
        "law": law,
        "box_shape": (3, 3, 3),
        "code_cells": len(BOX_CELLS),
        "selected_update_cells": len(SELECTED_CELLS),
        "code_qubits": eq.qubits,
        "code_stabilizer_rank": C712.rank(eq.target_w[6 * len(BOX_CELLS):], eq.qubits),
        "literal_code_M2": len(occupied_tuple),
        "shared_center_carriers": central_carriers,
        "shared_center_carrier_count": len(set(central_carriers)),
        "endpoint_register_M2": len(seam_sites),
        "retained_pointer_M2": len(pointer_sites),
        "candidate_extra_M2": len(candidate_extra_sites),
        "total_assigned_M2": len(assigned),
        "placement_collisions": collisions + len(assigned)
        - len(occupied_tuple) - len(seam_sites) - len(candidate_extra_sites),
        "abstract_logical_gates": len(logical_word),
        "abstract_gate_census": dict(Counter(g.kind for g in logical_word)),
        "physical_primitives": len(physical_word),
        "routed_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "routed_word_sha256": route["word_sha256"],
        "touched_M2": len(touched),
        "blank_route_work_M2": len(touched - assigned),
        "proper_cubic_frames": len(frames),
        "proper_cubic_products": len(frames) ** 2,
        "physical_frame_failures": physical_frame_failures,
        "frame_composition_coordinate_failures": composition_failures,
        "translations": translations,
        "translation_metric_failures": translation_failures,
        "decoded_stabilizer_failures": C712.tableau_failures(
            C712.apply_word_rows(eq.target_w[6 * len(BOX_CELLS):], target_decode),
            [C712.c707.Pauli(z=1 << i) for i in range(6 * len(BOX_CELLS), eq.qubits)],
        ),
        "logical_word_sha256": sha256(json.dumps(
            [abstract_instruction_signature(gate) for gate in logical_word],
            sort_keys=True,
        ).encode()).hexdigest(),
        "primitive_expansion": primitive_expansion_certificate(),
        "runtime_truth_table_ROM_bits": 0,
        "runtime_law_selector_bits": 0,
    }


def group_certificate() -> dict[str, object]:
    frames = DISC.proper_cubic_frames()
    permutations = []
    for frame in frames:
        permutations.append(tuple(
            DIRECTIONS.index(DISC.matvec(frame, direction)) for direction in DIRECTIONS
        ))
    failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            matrix = tuple(tuple(sum(left[i][k] * right[k][j] for k in range(3))
                                 for j in range(3)) for i in range(3))
            target = frames.index(matrix)
            composed = tuple(permutations[left_index][permutations[right_index][q]]
                             for q in range(6))
            failures += composed != permutations[target]
    return {
        "proper_cubic_frames": len(frames),
        "ordered_products": len(frames) ** 2,
        "direction_composition_failures": failures,
        "distinct_direction_permutations": len(set(permutations)),
    }


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, (set, frozenset)):
        return sorted(value)
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(type(value).__name__)


def main() -> int:
    provenance = C714.provenance_certificate(AUDIT_INPUT_PATHS, __file__)
    candidate = candidate_certificate()
    seam = seam_instrument_certificate()
    free = one_particle_certificate()
    group = group_certificate()
    physical = {
        law: physical_certificate(law)
        for law in ("unique_quorum", "odd_shells")
    }
    checks = {
        "source_closure": provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["missing_dynamic_scripts"]
        and not provenance["untracked_inputs"],
        "candidate_unique": candidate["unique_quorum"]["all_64_equation_failures"] == 0
        and candidate["unique_quorum"]["all_64_inverse_failures"] == 0
        and candidate["unique_quorum"]["all_64_work_cleanup_failures"] == 0
        and candidate["unique_quorum"]["coherent_all_64_residual"] < TOL,
        "candidate_odd": candidate["odd_shells"]["all_64_equation_failures"] == 0
        and candidate["odd_shells"]["all_64_inverse_failures"] == 0
        and candidate["odd_shells"]["all_64_work_cleanup_failures"] == 0
        and candidate["odd_shells"]["coherent_all_64_residual"] < TOL,
        "candidate_covariance": candidate["unique_quorum"]["proper_cubic_output_failures"] == 0
        and candidate["odd_shells"]["proper_cubic_output_failures"] == 0
        and group["direction_composition_failures"] == 0,
        "candidate_deletions": all(
            value > 0 for law in ("unique_quorum", "odd_shells")
            for value in candidate[law]["deletion_difference_counts"].values()
        ),
        "discriminator_unique":
            candidate["discriminator_bridge"]["unique_quorum_verdict"].get("law")
            == "unique_quorum"
            and candidate["discriminator_bridge"]["unique_quorum_well_formed_ports"] == 64,
        "discriminator_odd_firewall":
            candidate["discriminator_bridge"]["odd_shells_verdict"].get("kind")
            == "refuse_malformed"
            and candidate["discriminator_bridge"]["odd_shells_malformed_ports"] > 0,
        "six_seam_instrument": seam["complete_direction_words_seen"] == 64
        and seam["support_failures"] == seam["matter_target_failures"] == 0
        and seam["pointer_truth_failures"] == seam["scratch_cleanup_failures"] == 0
        and seam["maximum_phase_residual"] < TOL,
        "dirty_domains": seam["dirty_ancilla_rows_rejected"] == seam["dirty_ancilla_rows"]
        and all(value > TOL for value in
                seam["dirty_ancilla_output_difference_residuals"].values())
        and all(candidate[law]["dirty_rows_rejected"] == candidate[law]["dirty_rows"]
                for law in ("unique_quorum", "odd_shells")),
        "shared_center": seam["unique_shared_center_endpoint_modes"] == 6
        and seam["unique_all_endpoint_modes"] == 12,
        "seam_deletions": all(
            row["difference_rows"] > 0 and row["maximum_residual"] > TOL
            for row in seam["deletion_controls"].values()
        ),
        "free_contact_mass": free["star_free_one_particle_residual"] < TOL
        and free["mass_residual"] < TOL
        and free["Cycle230_pair_semantic_reconciliation"]["coin_matrix_residual"] < TOL
        and free["Cycle230_pair_semantic_reconciliation"]["onsite_64_state_contact_residual"] < TOL,
        "physical_words": all(
            row["placement_collisions"] == 0
            and row["non_NN_failures"] == 0
            and row["operand_order_failures"] == 0
            and row["route_return_failures"] == 0
            and row["decoded_stabilizer_failures"] == 0
            and row["primitive_expansion"]["X_HSSH_residual"] < TOL
            and row["primitive_expansion"]["Toffoli_HTCNOT_residual"] < TOL
            for row in physical.values()
        ),
        "physical_covariance_translation": all(
            row["physical_frame_failures"] == 0
            and row["frame_composition_coordinate_failures"] == 0
            and row["translation_metric_failures"] == 0
            for row in physical.values()
        ),
    }
    report = {
        "authority": "none",
        "audit": "unset",
        "cycle": 716,
        "status": "bounded constructive comparison",
        "declared_inputs": AUDIT_INPUT_PATHS,
        "provenance": provenance,
        "candidate_laws": candidate,
        "six_seam_instrument": seam,
        "free_contact_mass": free,
        "proper_cubic_group": group,
        "physical_M2": physical,
        "checks": checks,
        "pass": all(checks.values()),
        "supplied": [
            "Cycle713/712 physical code, gate alphabet, common coin/contact fixtures",
            "one clean 3x3x3 prepared PatchGraph+four-rail code block",
            "clean seam and candidate ancillas",
            "compile-time choice of unique-quorum or odd-shell candidate word",
            "fixed reversible gate order and route workspace",
            "the landed five-table family and lane-zero grammar for comparison only",
        ],
        "derived": [
            "six directional seam-opportunity pointers in one shared central-cell code",
            "complete unique-quorum and odd-shell Boolean relations by fixed local gates",
            "coherent archive/eligible/rejected/collision/empty outputs",
            "unique-quorum lane-zero discriminator stream without a winner convention",
            "proper-cubic scalar/directional covariance and translation compatibility",
        ],
        "open": [
            "Nature's fixed Admissibility and objective actuality",
            "an autonomous law selector or genesis/enforcement theorem",
            "a covariant winner-bearing grammar for multi-opportunity admitted words",
            "recurrent tiling of overlapping 3x3x3 blocks and autonomous clean-ancilla supply",
            "Record permanence, Born/history selection, source/gravity, and physical time",
        ],
        "firewall": (
            "The constructed circuits expose two extensional candidate tables.  They do not "
            "choose Nature's law.  The odd-shell grammar mismatch is route-specific and creates "
            "no no-go or axiom-pressure claim."
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True, default=json_default))
    print("CYCLE716_SAME_CODE_SIX_PORT_ADMISSION_PASS" if report["pass"]
          else "CYCLE716_SAME_CODE_SIX_PORT_ADMISSION_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
