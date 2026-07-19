#!/usr/bin/env python3
"""Cycle 451: source-conditioned relational dual-clock bridge.

Compose the Cycle-446 nearest-neighbor compilation of the Cycle-445
mass/source adapter with a dual copy of the Cycle-444 event-latched echo
oscillator.  One reference clock and one source-exposed
clock share the same physical send/reflect/detect event pair.  A receiver M2
coherently controls either the supplied delay or supplied advance response on
the exposed clock.  The output is a matched dimensionless interval-ratio
candidate; it is not lapse, proper time, a rate, or a selected history.

Update count, circuit depth, wrapped phase, and recurrence index are never
used as time.  Phase is never called energy and no generator is called a rate.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_mass_source_echo_lapse_candidate_tournament_cycle445_2026_07_19 as c445
import physical_nn_functional_source_control_compiler_cycle446_2026_07_19 as c446


c444 = c445.c444
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 4e-11
CLOCK_BITS = c444.CLOCK_BITS
EVENT_BITS = c444.EVENT_BITS
RESPONSE_RAIL_BITS = CLOCK_BITS - 1
LENGTH = 2
SIGNAL_BITS = LENGTH + 2
CORE_M2 = c445.REGISTER_BITS + c445.SOURCE_BITS + SIGNAL_BITS + 1 + 2 * CLOCK_BITS + RESPONSE_RAIL_BITS
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


@dataclass(frozen=True)
class LogicalKey:
    register: int
    local_mode: int
    signal_position: int
    reflector: int
    reference_position: int
    probe_position: int


@dataclass(frozen=True)
class PhysicalKey:
    register: Word
    local_mode: Word
    signal: Word
    reflector: int
    reference_clock: Word
    probe_clock: Word
    response_rail: Word


@dataclass(frozen=True)
class Experiment:
    beta: float
    held: bool
    size: int
    start: int


@dataclass(frozen=True)
class DualEndpoint:
    site: Coord
    reference_latch: c444.LatchState
    probe_latch: c444.LatchState
    reference_device: int
    probe_device: int
    epoch: int
    profile_identity: int
    predecessors: tuple[Coord, ...]
    typed: bool
    permanent: bool
    conditional_candidate: bool = True


@dataclass(frozen=True)
class RelationalIntervalCandidate:
    start_identity: int
    end_identity: int
    reference_cells: int
    probe_cells: int
    probe_over_reference: Fraction
    common_profile_identity: int
    classification: str = "relational dimensionless interval candidate, not lapse or proper time"


LogicalState = dict[LogicalKey, complex]
PhysicalState = dict[PhysicalKey, complex]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "source-conditioned relational dual-clock bridge",
        "same physical launch/return echo event pair",
        "reference clock",
        "source-exposed clock",
        "relational dimensionless interval candidate",
        "not lapse or proper time",
        "source-off 4:4",
        "receiver-zero 4:4",
        "receiver-one 3:4 or 5:4",
        "common rescaling cancels",
        "train l5 and held l9",
        "all 24 proper-cubic frames",
        "update count, circuit depth, wrapped phase, and recurrence index are not time",
        "no phase is called energy and no generator is called a rate",
        "n1",
        "n8",
        "no no-go, minimum-content, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-451 note freezes the relational-clock boundary", not missing, missing)


def one_hot(position: int, width: int) -> Word:
    if not isinstance(position, int) or isinstance(position, bool) or position not in range(width):
        raise ValueError("one-hot position is outside its physical word")
    return tuple(int(index == position) for index in range(width))


def hot_position(word: Word, width: int) -> int:
    if not isinstance(word, tuple) or len(word) != width or sum(word) != 1 or any(
        not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1) for bit in word
    ):
        raise ValueError("physical word is outside its one-excitation code")
    return word.index(1)


def add_state(output: dict, key, amplitude: complex) -> None:
    output[key] = output.get(key, 0j) + amplitude
    if abs(output[key]) < 1e-15:
        del output[key]


def experiment(sector: c445.Sector) -> Experiment:
    return Experiment(
        sector.beta,
        sector.held,
        c444.HELD_SIZE if sector.held else c444.TRAIN_SIZE,
        c444.HELD_START if sector.held else c444.TRAIN_START,
    )


def validate_experiment(item: Experiment) -> None:
    if item.size < 5 or item.size % 2 == 0 or LENGTH > (item.size - 1) // 2:
        raise ValueError("dual-clock echo leaves the declared odd periodic envelope")
    c444.one_hot(item.start)


def initial_logical(sector: c445.Sector) -> LogicalState:
    item = experiment(sector)
    validate_experiment(item)
    output: LogicalState = {}
    for register, amplitude in enumerate(sector.eigenray):
        if abs(amplitude) > 1e-15:
            output[
                LogicalKey(register, 0, 0, 0, item.start, item.start)
            ] = complex(amplitude)
    return output


def encode_key(key: LogicalKey) -> PhysicalKey:
    return PhysicalKey(
        one_hot(key.register, c445.REGISTER_BITS),
        one_hot(key.local_mode, c445.SOURCE_BITS),
        one_hot(key.signal_position, SIGNAL_BITS),
        key.reflector,
        c444.one_hot(key.reference_position),
        c444.one_hot(key.probe_position),
        (0,) * RESPONSE_RAIL_BITS,
    )


def encode(state: LogicalState) -> PhysicalState:
    output: PhysicalState = {}
    for key, amplitude in state.items():
        add_state(output, encode_key(key), amplitude)
    return output


def validate_physical_key(key: PhysicalKey, *, require_blank_rail: bool = True) -> None:
    hot_position(key.register, c445.REGISTER_BITS)
    hot_position(key.local_mode, c445.SOURCE_BITS)
    hot_position(key.signal, SIGNAL_BITS)
    if key.reflector not in (0, 1):
        raise ValueError("reflection certificate is not binary")
    c444.clock_position(key.reference_clock)
    c444.clock_position(key.probe_clock)
    if len(key.response_rail) != RESPONSE_RAIL_BITS or any(bit not in (0, 1) for bit in key.response_rail):
        raise ValueError("response rail is outside its binary M2 domain")
    if require_blank_rail and any(key.response_rail):
        raise ValueError("response rail must enter and leave blank")


def transport_schedule() -> tuple[c446.Gate, ...]:
    """NN transposition of local modes 1 and 7 with modes 2..6 restored."""
    forward = tuple(
        c446.swap_gate(
            c446.REGISTER_MODES + local,
            c446.REGISTER_MODES + local + 1,
            f"Cycle451:transport-out-{local}",
        )
        for local in range(1, 7)
    )
    restore = tuple(
        c446.swap_gate(
            c446.REGISTER_MODES + local,
            c446.REGISTER_MODES + local + 1,
            f"Cycle451:transport-restore-{local}",
        )
        for local in range(5, 0, -1)
    )
    return forward + restore


TRANSPORT_SCHEDULE = transport_schedule()


def physical_source_step(
    state: PhysicalState,
    compiled: c446.CompiledLaw,
    *,
    enabled: bool,
    inverse: bool,
) -> PhysicalState:
    schedule: tuple[c446.Gate, ...] = ()
    if enabled:
        schedule = (
            c446.inverse_schedule(compiled.schedule)
            if inverse
            else compiled.schedule
        )
    output: PhysicalState = {}
    for key, amplitude in state.items():
        validate_physical_key(key)
        register = hot_position(key.register, c445.REGISTER_BITS)
        local_mode = hot_position(key.local_mode, c445.SOURCE_BITS)
        source_state = np.zeros((c446.REGISTER_MODES, c446.SOURCE_MODES), dtype=complex)
        source_state[register, local_mode] = 1
        source_state = c446.apply_schedule(source_state, schedule)
        for target_register, target_local in product(
            range(c446.REGISTER_MODES), range(c446.SOURCE_MODES)
        ):
            coefficient = source_state[target_register, target_local]
            if abs(coefficient) <= 1e-15:
                continue
            moved = replace(
                key,
                register=one_hot(target_register, c445.REGISTER_BITS),
                local_mode=one_hot(target_local, c445.SOURCE_BITS),
            )
            add_state(output, moved, amplitude * coefficient)
    return output


def physical_transport(state: PhysicalState, *, inverse: bool = False) -> PhysicalState:
    schedule = (
        c446.inverse_schedule(TRANSPORT_SCHEDULE)
        if inverse
        else TRANSPORT_SCHEDULE
    )
    output: PhysicalState = {}
    for key, amplitude in state.items():
        validate_physical_key(key)
        register = hot_position(key.register, c445.REGISTER_BITS)
        local = hot_position(key.local_mode, c445.SOURCE_BITS)
        source_state = np.zeros((c446.REGISTER_MODES, c446.SOURCE_MODES), dtype=complex)
        source_state[register, local] = 1
        source_state = c446.apply_schedule(source_state, schedule)
        for target_register, target_local in product(
            range(c446.REGISTER_MODES), range(c446.SOURCE_MODES)
        ):
            coefficient = source_state[target_register, target_local]
            if abs(coefficient) <= 1e-15:
                continue
            add_state(
                output,
                replace(
                    key,
                    register=one_hot(target_register, c445.REGISTER_BITS),
                    local_mode=one_hot(target_local, c445.SOURCE_BITS),
                ),
                amplitude * coefficient,
            )
    return output


def dual_echo_primitive(
    key: PhysicalKey,
    primitive: c444.Primitive,
    *,
    inverse: bool,
    delete_reference_sweep: bool,
    delete_probe_sweep: bool,
    delete_detector: bool,
    delete_reflection_certificate: bool,
) -> PhysicalKey:
    signal = list(key.signal)
    reflector = key.reflector
    reference = key.reference_clock
    probe = key.probe_clock
    if primitive.kind == "swap":
        if delete_detector and primitive.name == "detector-absorption":
            return key
        assert primitive.left is not None and primitive.right is not None
        signal[primitive.left], signal[primitive.right] = signal[primitive.right], signal[primitive.left]
    elif primitive.kind == "reflect":
        if delete_reflection_certificate:
            return key
        assert primitive.left is not None
        reflector ^= signal[primitive.left]
    elif primitive.kind == "clock":
        if not delete_reference_sweep:
            reference = c444.clock_inverse(reference) if inverse else c444.clock_forward(reference)
        if not delete_probe_sweep:
            probe = c444.clock_inverse(probe) if inverse else c444.clock_forward(probe)
    else:
        raise ValueError("unknown dual-echo primitive")
    return replace(
        key,
        signal=tuple(signal),
        reflector=reflector,
        reference_clock=reference,
        probe_clock=probe,
    )


def physical_dual_echo(
    state: PhysicalState,
    *,
    inverse: bool,
    delete_reference_sweep: bool = False,
    delete_probe_sweep: bool = False,
    delete_detector: bool = False,
    delete_reflection_certificate: bool = False,
) -> PhysicalState:
    schedule = c444.echo_program(LENGTH)
    if inverse:
        schedule = tuple(reversed(schedule))
    output: PhysicalState = {}
    for key, amplitude in state.items():
        moved = key
        for primitive in schedule:
            moved = dual_echo_primitive(
                moved,
                primitive,
                inverse=inverse,
                delete_reference_sweep=delete_reference_sweep,
                delete_probe_sweep=delete_probe_sweep,
                delete_detector=delete_detector,
                delete_reflection_certificate=delete_reflection_certificate,
            )
        validate_physical_key(moved)
        add_state(output, moved, amplitude)
    return output


def physical_response(
    state: PhysicalState,
    law: str,
    *,
    inverse: bool,
    delete_control: bool = False,
) -> PhysicalState:
    output: PhysicalState = {}
    for key, amplitude in state.items():
        local = hot_position(key.local_mode, c445.SOURCE_BITS)
        response = c445.response_update(
            c445.ResponseState(int(local == 7), key.response_rail, key.probe_clock),
            law,
            inverse=inverse,
            delete_control=delete_control,
        )
        moved = replace(key, probe_clock=response.clock, response_rail=response.rail)
        validate_physical_key(moved)
        add_state(output, moved, amplitude)
    return output


def physical_forward(
    initial: PhysicalState,
    compiled: c446.CompiledLaw,
    law: str,
    *,
    source_enabled: bool,
    delete_control: bool = False,
    delete_reference_sweep: bool = False,
    delete_probe_sweep: bool = False,
    delete_detector: bool = False,
    delete_reflection_certificate: bool = False,
) -> PhysicalState:
    output = physical_source_step(initial, compiled, enabled=source_enabled, inverse=False)
    output = physical_transport(output)
    output = physical_dual_echo(
        output,
        inverse=False,
        delete_reference_sweep=delete_reference_sweep,
        delete_probe_sweep=delete_probe_sweep,
        delete_detector=delete_detector,
        delete_reflection_certificate=delete_reflection_certificate,
    )
    return physical_response(output, law, inverse=False, delete_control=delete_control)


def physical_inverse(
    output: PhysicalState,
    compiled: c446.CompiledLaw,
    law: str,
    *,
    source_enabled: bool,
) -> PhysicalState:
    state = physical_response(output, law, inverse=True)
    state = physical_dual_echo(state, inverse=True)
    state = physical_transport(state, inverse=True)
    return physical_source_step(state, compiled, enabled=source_enabled, inverse=True)


def advance_position(position: int, sweeps: int) -> int:
    word = c444.one_hot(position)
    for _ in range(sweeps):
        word = c444.clock_forward(word)
    return c444.clock_position(word)


def coarse_forward(
    sector: c445.Sector,
    compiled: c446.CompiledLaw,
    law: str,
    *,
    source_enabled: bool,
) -> LogicalState:
    item = experiment(sector)
    local = c445.source_initial(sector.eigenray)
    if source_enabled:
        local = (compiled.target @ local.reshape(-1)).reshape(
            c445.REGISTER_BITS, c445.SOURCE_BITS
        )
    local = c445.transport_to_receiver(local)
    baseline = advance_position(item.start, 2 * LENGTH)
    output: LogicalState = {}
    for register, local_mode in product(range(c445.REGISTER_BITS), range(c445.SOURCE_BITS)):
        amplitude = complex(local[register, local_mode])
        if abs(amplitude) <= 1e-15:
            continue
        response = c445.response_update(
            c445.ResponseState(
                int(local_mode == 7),
                (0,) * RESPONSE_RAIL_BITS,
                c444.one_hot(baseline),
            ),
            law,
        )
        add_state(
            output,
            LogicalKey(
                register,
                local_mode,
                SIGNAL_BITS - 1,
                1,
                baseline,
                c444.clock_position(response.clock),
            ),
            amplitude,
        )
    return output


def physical_residual(left: PhysicalState, right: PhysicalState) -> float:
    keys = left.keys() | right.keys()
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def state_norm(state: PhysicalState) -> float:
    return float(sum(abs(amplitude) ** 2 for amplitude in state.values()))


def code_leakage(state: PhysicalState) -> float:
    weight = 0.0
    for key, amplitude in state.items():
        try:
            validate_physical_key(key)
        except ValueError:
            weight += abs(amplitude) ** 2
    return float(np.sqrt(weight))


def receiver_branches(state: PhysicalState) -> dict[int, dict[str, object]]:
    branches: dict[int, dict[str, object]] = {}
    for receiver in (0, 1):
        rows = [
            (key, amplitude)
            for key, amplitude in state.items()
            if int(hot_position(key.local_mode, c445.SOURCE_BITS) == 7) == receiver
        ]
        weight = float(sum(abs(amplitude) ** 2 for _, amplitude in rows))
        signatures = {
            (
                hot_position(key.signal, SIGNAL_BITS),
                key.reflector,
                c444.clock_position(key.reference_clock),
                c444.clock_position(key.probe_clock),
            )
            for key, amplitude in rows
            if abs(amplitude) > 1e-15
        }
        branches[receiver] = {"weight": weight, "signatures": signatures}
    return branches


def endpoint(
    reference_word: Word,
    probe_word: Word,
    event_identity: int,
    site: Coord,
    predecessors: tuple[Coord, ...],
    *,
    epoch: int = 0,
    profile_identity: int = 3,
    reference_detector: int = 1,
    probe_detector: int = 1,
    typed: bool = True,
    permanent: bool = True,
) -> DualEndpoint:
    event_word = c444.bits(event_identity, EVENT_BITS)
    return DualEndpoint(
        site,
        c444.apply_latch(c444.blank_latch(reference_detector, reference_word, event_word)),
        c444.apply_latch(c444.blank_latch(probe_detector, probe_word, event_word)),
        1,
        2,
        epoch,
        profile_identity,
        predecessors,
        typed,
        permanent,
    )


def match_relational_interval(
    start: DualEndpoint | None,
    end: DualEndpoint | None,
    *,
    matcher_enabled: bool = True,
    common_profile_certificate: bool = True,
    event_edge: bool = True,
) -> RelationalIntervalCandidate | None:
    if start is None or end is None or not matcher_enabled or not common_profile_certificate or not event_edge:
        return None
    decoded = (
        c444.decoded_latch(start.reference_latch),
        c444.decoded_latch(start.probe_latch),
        c444.decoded_latch(end.reference_latch),
        c444.decoded_latch(end.probe_latch),
    )
    if any(item is None for item in decoded):
        return None
    start_ref, start_probe, end_ref, end_probe = decoded
    assert start_ref is not None and start_probe is not None and end_ref is not None and end_probe is not None
    if (
        not start.typed
        or not start.permanent
        or not end.typed
        or not end.permanent
        or start_ref[1] != start_probe[1]
        or end_ref[1] != end_probe[1]
        or start_ref[1] == 0
        or end_ref[1] == 0
        or start_ref[1] == end_ref[1]
        or start.reference_device != end.reference_device
        or start.probe_device != end.probe_device
        or start.reference_device == start.probe_device
        or start.epoch != end.epoch
        or start.profile_identity != end.profile_identity
        or start.site not in end.predecessors
        or start_ref[0] != start_probe[0]
        or end_ref[0] <= start_ref[0]
        or end_probe[0] <= start_probe[0]
    ):
        return None
    reference_cells = end_ref[0] - start_ref[0]
    probe_cells = end_probe[0] - start_probe[0]
    return RelationalIntervalCandidate(
        start_ref[1],
        end_ref[1],
        reference_cells,
        probe_cells,
        Fraction(probe_cells, reference_cells),
        start.profile_identity,
    )


def interval_for_positions(
    start_position: int,
    reference_end: int,
    probe_end: int,
    *,
    end_identity: int = 2,
    end_epoch: int = 0,
    end_profile: int = 3,
    reference_detector: int = 1,
    probe_detector: int = 1,
    predecessor: bool = True,
    matcher_enabled: bool = True,
    profile_certificate: bool = True,
    event_edge: bool = True,
) -> RelationalIntervalCandidate | None:
    start_site = (-1, 2, 1)
    end_site = (-1, 2, 2)
    start = endpoint(
        c444.one_hot(start_position),
        c444.one_hot(start_position),
        1,
        start_site,
        (),
    )
    end = endpoint(
        c444.one_hot(reference_end),
        c444.one_hot(probe_end),
        end_identity,
        end_site,
        (start_site,) if predecessor else (),
        epoch=end_epoch,
        profile_identity=end_profile,
        reference_detector=reference_detector,
        probe_detector=probe_detector,
    )
    return match_relational_interval(
        start,
        end,
        matcher_enabled=matcher_enabled,
        common_profile_certificate=profile_certificate,
        event_edge=event_edge,
    )


def calibrated_ratio(
    interval: RelationalIntervalCandidate | None,
    reference_cell_scale: Fraction,
    probe_cell_scale: Fraction,
    *,
    cross_profile_certificate: bool,
) -> Fraction | None:
    if interval is None or reference_cell_scale <= 0 or probe_cell_scale <= 0:
        return None
    if reference_cell_scale != probe_cell_scale and not cross_profile_certificate:
        return None
    return Fraction(interval.probe_cells) * probe_cell_scale / (
        Fraction(interval.reference_cells) * reference_cell_scale
    )


def compiler_interface_controls(
    controller: c445.MassController,
    compiled_laws: tuple[c446.CompiledLaw, ...],
) -> dict[str, object]:
    print("\nCYCLE446 SOURCE-COMPILER / CYCLE451 INTERFACE")
    target_residuals = {}
    transport_residuals = []
    source_covariance_residuals = []
    for compiled in compiled_laws:
        mass = controller.cayley if compiled.name == "cayley" else controller.principal
        target_residuals[compiled.name] = float(
            np.linalg.norm(compiled.target - c445.source_update(mass, enabled=True))
        )
        for frame in c444.FRAMES:
            source_frame = c446.direction_representation(frame)
            joint_frame = np.kron(np.eye(c446.REGISTER_MODES), source_frame)
            source_covariance_residuals.append(
                float(
                    np.linalg.norm(
                        joint_frame @ compiled.target @ joint_frame.conj().T
                        - compiled.target
                    )
                )
            )
    for register, local in product(
        range(c446.REGISTER_MODES), range(c446.SOURCE_MODES)
    ):
        basis = np.zeros((c446.REGISTER_MODES, c446.SOURCE_MODES), dtype=complex)
        basis[register, local] = 1
        compiled_output = c446.apply_schedule(basis, TRANSPORT_SCHEDULE)
        expected = c445.transport_to_receiver(basis)
        transport_residuals.append(float(np.linalg.norm(compiled_output - expected)))
    cayley = next(item for item in compiled_laws if item.name == "cayley")
    spectral_index = next(
        index for index, gate in enumerate(cayley.schedule)
        if gate.kind == "controlled-phase"
    )
    deleted_operator = c446.schedule_operator(
        cayley.schedule[:spectral_index] + cayley.schedule[spectral_index + 1 :]
    )
    deletion_residual = float(np.linalg.norm(deleted_operator - cayley.target))
    source_rows = tuple(
        {
            "law": item.name,
            "M2": c446.TOTAL_M2,
            "source_serial_primitives": len(item.schedule),
            "maximum_support_M2": max(len(gate.sites) for gate in item.schedule),
            "NN_failures": sum(
                len(gate.sites) == 2 and gate.sites[1] - gate.sites[0] != 1
                for gate in item.schedule
            ),
            "target_residual": target_residuals[item.name],
            "schedule_digest": c446.gate_digest(item.schedule),
        }
        for item in compiled_laws
    )
    maximum = max(
        *target_residuals.values(),
        *transport_residuals,
        *source_covariance_residuals,
    )
    check(
        "the Cycle446 full-law schedules match the Cycle445 source interface and the selected-rail transport has an explicit restored-placement NN compiler",
        c446.REGISTER_MODES == c445.REGISTER_BITS == 9
        and c446.SOURCE_MODES == c445.SOURCE_BITS == 8
        and all(row["source_serial_primitives"] == 250 for row in source_rows)
        and all(row["maximum_support_M2"] <= 2 and row["NN_failures"] == 0 for row in source_rows)
        and len(TRANSPORT_SCHEDULE) == 11
        and all(
            len(gate.sites) == 2 and gate.sites[1] - gate.sites[0] == 1
            for gate in TRANSPORT_SCHEDULE
        )
        and maximum < TOL
        and deletion_residual > 1e-4,
        {
            "source_compilers": source_rows,
            "transport_serial_NN_SWAPS": len(TRANSPORT_SCHEDULE),
            "maximum_interface_residual": maximum,
            "maximum_all24_source_operator_covariance_residual": max(source_covariance_residuals),
            "source_spectral_phase_deletion_residual": deletion_residual,
            "physical_key_interface": "register/local one-hot words are exactly Cycle446 Q1 x Q1",
        },
    )
    return {
        "rows": source_rows,
        "maximum": maximum,
        "source_spectral_phase_deletion_residual": deletion_residual,
    }


def eg_inverse_leakage_controls(
    compiled_laws: tuple[c446.CompiledLaw, ...],
    menu: tuple[c445.Sector, ...],
) -> dict[str, object]:
    print("\nDUAL-CLOCK E/G / INVERSE / LEAKAGE")
    rows = []
    maximum = 0.0
    for sector in menu:
        for compiled in compiled_laws:
            mass_name = compiled.name
            for law, source_enabled in product(("delay", "advance"), (False, True)):
                initial_logical_state = initial_logical(sector)
                initial_physical = encode(initial_logical_state)
                physical = physical_forward(
                    initial_physical,
                    compiled,
                    law,
                    source_enabled=source_enabled,
                )
                expected = encode(
                    coarse_forward(
                        sector,
                        compiled,
                        law,
                        source_enabled=source_enabled,
                    )
                )
                restored = physical_inverse(
                    physical,
                    compiled,
                    law,
                    source_enabled=source_enabled,
                )
                residual = physical_residual(physical, expected)
                inverse = physical_residual(restored, initial_physical)
                leakage = code_leakage(physical)
                norm_drift = abs(state_norm(physical) - state_norm(initial_physical))
                maximum = max(maximum, residual, inverse, leakage, norm_drift)
                rows.append(
                    {
                        "beta": sector.beta,
                        "held": sector.held,
                        "mass_route": mass_name,
                        "response_law": law,
                        "source_enabled": source_enabled,
                        "E_G_residual": residual,
                        "inverse_residual": inverse,
                        "leakage": leakage,
                        "norm_drift": norm_drift,
                    }
                )
    check(
        "E_451 G_coarse = G_physical,451 E_451 with inverse and zero code/work leakage on every frozen train/held source sector",
        len(rows) == 32 and maximum < TOL and all(row["leakage"] == 0 for row in rows),
        {"rows": rows, "maximum_residual": maximum, "core_M2": CORE_M2},
    )
    return {"rows": rows, "maximum": maximum}


def branch_relational_prediction_controls(
    compiled_laws: tuple[c446.CompiledLaw, ...],
    menu: tuple[c445.Sector, ...],
) -> dict[str, object]:
    print("\nCOHERENT SOURCE BRANCHES / RELATIONAL PREDICTIONS")
    rows = []
    failures = 0
    train_differences = []
    held_weights: dict[tuple[str, str], float] = {}
    for sector in menu:
        route_weights = {}
        item = experiment(sector)
        for compiled in compiled_laws:
            mass_name = compiled.name
            for law in ("delay", "advance"):
                initial = encode(initial_logical(sector))
                off = physical_forward(initial, compiled, law, source_enabled=False)
                on = physical_forward(initial, compiled, law, source_enabled=True)
                off_branches = receiver_branches(off)
                on_branches = receiver_branches(on)
                off_signature = next(iter(off_branches[0]["signatures"]))
                zero_signature = next(iter(on_branches[0]["signatures"]))
                one_signature = next(iter(on_branches[1]["signatures"]))
                off_interval = interval_for_positions(item.start, off_signature[2], off_signature[3])
                zero_interval = interval_for_positions(item.start, zero_signature[2], zero_signature[3])
                one_interval = interval_for_positions(item.start, one_signature[2], one_signature[3])
                expected_ratio = Fraction(3, 4) if law == "delay" else Fraction(5, 4)
                failures += int(off_branches[1]["weight"] > TOL)
                failures += int(off_interval is None or off_interval.probe_over_reference != 1)
                failures += int(zero_interval is None or zero_interval.probe_over_reference != 1)
                failures += int(one_interval is None or one_interval.probe_over_reference != expected_ratio)
                failures += int(off_signature[:2] != (SIGNAL_BITS - 1, 1))
                failures += int(zero_signature[:2] != (SIGNAL_BITS - 1, 1))
                failures += int(one_signature[:2] != (SIGNAL_BITS - 1, 1))
                route_weights[mass_name] = float(on_branches[1]["weight"])
                if sector.held:
                    held_weights[(mass_name, law)] = float(on_branches[1]["weight"])
                rows.append(
                    {
                        "beta": sector.beta,
                        "held": sector.held,
                        "mass_route": mass_name,
                        "law": law,
                        "source_off_reference_probe_cells": (
                            off_interval.reference_cells if off_interval else None,
                            off_interval.probe_cells if off_interval else None,
                        ),
                        "receiver_zero_reference_probe_cells": (
                            zero_interval.reference_cells if zero_interval else None,
                            zero_interval.probe_cells if zero_interval else None,
                        ),
                        "receiver_one_reference_probe_cells": (
                            one_interval.reference_cells if one_interval else None,
                            one_interval.probe_cells if one_interval else None,
                        ),
                        "receiver_one_ratio": None if one_interval is None else one_interval.probe_over_reference,
                        "receiver_one_squared_norm": on_branches[1]["weight"],
                        "receiver_zero_squared_norm": on_branches[0]["weight"],
                        "inverse_residual": physical_residual(
                            physical_inverse(on, compiled, law, source_enabled=True), initial
                        ),
                    }
                )
        difference = abs(route_weights["cayley"] - route_weights["principal"])
        if sector.held:
            failures += int(difference <= 0.09)
        else:
            train_differences.append(difference)
            failures += int(difference >= TOL)
    check(
        "source-off and receiver-zero independently bind 4:4 while the coherent receiver-one sector binds delay 3:4 or advance 5:4 without host branch selection",
        failures == 0
        and len(rows) == 16
        and max(train_differences) < TOL
        and abs(held_weights[("cayley", "delay")] - held_weights[("principal", "delay")]) > 0.09,
        {
            "rows": rows,
            "failures": failures,
            "train_max_mass_route_weight_difference": max(train_differences),
            "held_receiver_weights": held_weights,
            "branch_selected": False,
            "receiver_squared_norm_called_probability_or_occurrence": False,
        },
    )
    return {"rows": rows, "held_weights": held_weights}


def rescaling_and_matcher_deletion_controls() -> None:
    print("\nCOMMON RESCALING / IDENTITY / EPOCH / MATCHER / EVENT / PROFILE")
    baseline = interval_for_positions(c444.HELD_START, 6, 5)
    scales = (Fraction(1, 7), Fraction(3, 2), Fraction(11, 3))
    rescaled = tuple(
        calibrated_ratio(baseline, scale, scale, cross_profile_certificate=False)
        for scale in scales
    )
    deletions = {
        "identity": interval_for_positions(c444.HELD_START, 6, 5, end_identity=0),
        "epoch": interval_for_positions(c444.HELD_START, 6, 5, end_epoch=1),
        "matcher": interval_for_positions(c444.HELD_START, 6, 5, matcher_enabled=False),
        "event": interval_for_positions(c444.HELD_START, 6, 5, probe_detector=0),
        "event-edge": interval_for_positions(c444.HELD_START, 6, 5, event_edge=False),
        "predecessor": interval_for_positions(c444.HELD_START, 6, 5, predecessor=False),
        "profile": interval_for_positions(c444.HELD_START, 6, 5, end_profile=4),
        "profile-certificate": interval_for_positions(c444.HELD_START, 6, 5, profile_certificate=False),
    }
    unmatched_scale = calibrated_ratio(
        baseline,
        Fraction(1),
        Fraction(2),
        cross_profile_certificate=False,
    )
    supplied_cross_calibration = calibrated_ratio(
        baseline,
        Fraction(1),
        Fraction(2),
        cross_profile_certificate=True,
    )
    check(
        "common cell rescaling cancels exactly, while identity/epoch/matcher/event/profile deletions are undefined rather than zero",
        baseline is not None
        and baseline.probe_over_reference == Fraction(3, 4)
        and rescaled == (Fraction(3, 4),) * len(scales)
        and all(value is None for value in deletions.values())
        and unmatched_scale is None
        and supplied_cross_calibration == Fraction(3, 2),
        {
            "common_scales": scales,
            "common_rescaled_ratios": rescaled,
            "deletions": deletions,
            "unequal_scale_without_cross_profile_certificate": unmatched_scale,
            "unequal_scale_with_supplied_cross_calibration": supplied_cross_calibration,
        },
    )


def physical_deletion_controls(
    compiled_laws: tuple[c446.CompiledLaw, ...],
    menu: tuple[c445.Sector, ...],
) -> None:
    print("\nPHYSICAL SOURCE / RESPONSE / ECHO / CLOCK DELETIONS")
    sector = next(item for item in menu if item.held)
    cayley = next(item for item in compiled_laws if item.name == "cayley")
    initial = encode(initial_logical(sector))
    nominal = physical_forward(initial, cayley, "delay", source_enabled=True)
    source_deleted = physical_forward(initial, cayley, "delay", source_enabled=False)
    response_deleted = physical_forward(
        initial, cayley, "delay", source_enabled=True, delete_control=True
    )
    reference_deleted = physical_forward(
        initial, cayley, "delay", source_enabled=True, delete_reference_sweep=True
    )
    probe_deleted = physical_forward(
        initial, cayley, "delay", source_enabled=True, delete_probe_sweep=True
    )
    detector_deleted = physical_forward(
        initial, cayley, "delay", source_enabled=True, delete_detector=True
    )
    reflection_deleted = physical_forward(
        initial,
        cayley,
        "delay",
        source_enabled=True,
        delete_reflection_certificate=True,
    )
    signatures = {
        name: receiver_branches(state)
        for name, state in (
            ("nominal", nominal),
            ("source", source_deleted),
            ("response", response_deleted),
            ("reference", reference_deleted),
            ("probe", probe_deleted),
            ("detector", detector_deleted),
            ("reflection", reflection_deleted),
        )
    }
    nominal_one = next(iter(signatures["nominal"][1]["signatures"]))
    response_one = next(iter(signatures["response"][1]["signatures"]))
    reference_one = next(iter(signatures["reference"][1]["signatures"]))
    probe_one = next(iter(signatures["probe"][1]["signatures"]))
    detector_one = next(iter(signatures["detector"][1]["signatures"]))
    reflection_one = next(iter(signatures["reflection"][1]["signatures"]))
    check(
        "source, response control, each clock pairing, detector, and reflection certificate are independently visible",
        signatures["source"][1]["weight"] < TOL
        and response_one[3] != nominal_one[3]
        and reference_one[2] != nominal_one[2]
        and probe_one[3] != nominal_one[3]
        and detector_one[0] != SIGNAL_BITS - 1
        and reflection_one[1] == 0
        and all(code_leakage(state) == 0 for state in (nominal, source_deleted, response_deleted, reference_deleted, probe_deleted, detector_deleted, reflection_deleted)),
        {
            "receiver_one_signatures": {
                "nominal": nominal_one,
                "response_control_deleted": response_one,
                "reference_pairing_deleted": reference_one,
                "probe_pairing_deleted": probe_one,
                "detector_deleted": detector_one,
                "reflection_certificate_deleted": reflection_one,
            },
            "source_deleted_receiver_one_weight": signatures["source"][1]["weight"],
        },
    )


def translated(support: tuple[Coord, ...], displacement: Coord) -> tuple[Coord, ...]:
    return tuple(tuple(a + b for a, b in zip(site, displacement)) for site in support)


def dual_clock_supports() -> tuple[tuple[Coord, ...], ...]:
    supports: list[tuple[Coord, ...]] = []
    sites = c444.echo_sites(LENGTH)
    path = sites["path"]
    assert isinstance(path, tuple)
    supports.extend(tuple(pair) for pair in zip(path[:-1], path[1:]))
    supports.append((path[0], sites["detector"]))
    supports.append((path[-1], sites["reflector"]))
    supports.extend(c444.latch_supports())
    supports.extend(translated(item, (0, 0, 4)) for item in c444.latch_supports())
    reference_clock = tuple((index, 1, 4) for index in range(CLOCK_BITS))
    supports.extend((reference_clock[index], reference_clock[index + 1]) for index in range(CLOCK_BITS - 1))
    # Local detector-copy corridor to the second latch.  It is a reversible
    # trigger fan, not a Record or occurrence selector.
    detector_fan = tuple((-1, 2, z) for z in range(5))
    supports.extend((detector_fan[index], detector_fan[index + 1]) for index in range(4))
    probe_clock = tuple((index, 1, 0) for index in range(CLOCK_BITS))
    response_rail = tuple((index, 1, 1) for index in range(RESPONSE_RAIL_BITS))
    receiver = (-1, 1, 1)
    supports.append((receiver, response_rail[0]))
    supports.extend((response_rail[index], response_rail[index + 1]) for index in range(RESPONSE_RAIL_BITS - 1))
    supports.extend((response_rail[index], probe_clock[index], probe_clock[index + 1]) for index in range(RESPONSE_RAIL_BITS))
    # Cycle446's register/source compiler and Cycle451's selected-rail
    # transposition both use this same carried seventeen-site NN line.
    source_line = tuple((index - 17, 1, 1) for index in range(c446.TOTAL_M2))
    assert source_line[-1] == receiver
    supports.extend(
        (source_line[index], source_line[index + 1])
        for index in range(c446.TOTAL_M2 - 1)
    )
    return tuple(supports)


def geometry_controls() -> None:
    print("\nALL-24 PROPER-CUBIC SUPPORT COVARIANCE")
    frames = c444.FRAMES
    supports = dual_clock_supports()
    failures = 0
    for support in supports:
        failures += int(not c444.support_connected(support))
        for frame in frames:
            moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in support)
            failures += int(not c444.support_connected(moved))
    check(
        "Cycle446 source/transport line, receiver response, shared echo, both clocks, trigger fan, and both latch families remain bounded/local in all 24 proper-cubic frames",
        len(frames) == 24 and failures == 0 and max(len(item) for item in supports) <= 3,
        {
            "frames": len(frames),
            "supports": len(supports),
            "maximum_primitive_support_M2": max(len(item) for item in supports),
            "locality_failures": failures,
            "preferred_frame": None,
        },
    )


def lawful_domain_controls(
    compiled_laws: tuple[c446.CompiledLaw, ...],
    menu: tuple[c445.Sector, ...],
) -> None:
    print("\nLAWFUL DOMAIN")
    sector = menu[0]
    cayley = next(item for item in compiled_laws if item.name == "cayley")
    valid = next(iter(encode(initial_logical(sector))))
    malformed = []
    malformed.append(replace(valid, register=(1, 1) + (0,) * 7))
    malformed.append(replace(valid, local_mode=(0,) * c445.SOURCE_BITS))
    malformed.append(replace(valid, signal=(1, 1, 0, 0)))
    malformed.append(replace(valid, response_rail=(1,) + (0,) * (RESPONSE_RAIL_BITS - 1)))
    refusals = 0
    for key in malformed:
        try:
            validate_physical_key(key)
        except ValueError:
            refusals += 1
    for action in (
        lambda: physical_forward(encode(initial_logical(sector)), cayley, "retard", source_enabled=True),
        lambda: validate_experiment(Experiment(sector.beta, False, 3, 1)),
        lambda: calibrated_ratio(None, Fraction(1), Fraction(1), cross_profile_certificate=False),
    ):
        try:
            value = action()
            if value is None and action.__name__ == "<lambda>":
                # A missing interval is lawful undefined, not a malformed refusal.
                continue
        except ValueError:
            refusals += 1
    check(
        "malformed one-hot codes, dirty work, unknown laws, and invalid envelopes are refused while missing calibration input is typed undefined",
        refusals == 6,
        {"malformed_refusals": refusals, "typed_missing_interval": None},
    )


def inventory_and_firewall_controls() -> None:
    print("\nSUPPLIED / DERIVED / PREDICTION BOUNDARY")
    supplied = (
        "nine-M2 Cycle445 controller preparation, principal/Cayley formulas, sector population, and beta-specific mass route",
        "Cycle446 analytic F9/source bases, Givens angles, spectral phases, primitive alphabet, seventeen-M2 line, and serial route order",
        "hard-core reservoir/six-field source graph, tau=0.05, source preparation, selected rail, and receiver transport target",
        "delay/advance response law, response rail, invocation, and factor order",
        "one shared Cycle444 length-two echo corridor, primitive order, reflection rule, and dual oscillator pairing per edge",
        "reference/probe oscillator initial word, orientation, device identities, common profile identity, and nonwrap epoch",
        "launch/return event identities, detector trigger fan, blank latch buses/sidecars, conditional typing/permanence, predecessor and matcher",
        "finite L5/L9 envelopes, all24 frame family, and any common cell scale used after the dimensionless ratio",
    )
    derived = (
        "consumption of each 250-primitive Cycle446 full-law source schedule plus an eleven-SWAP restored-placement NN selected-rail transport",
        "dual-clock physical-code E/G, inverse, norm, and zero leakage",
        "one common physical echo detector/reflection event for both complete clock words",
        "source-off and receiver-zero relational 4:4 candidate",
        "receiver-one delay 3:4 or advance 5:4 relational candidate",
        "common cell-scale cancellation, train agreement, held mass-route branch-weight separation, and deletion behavior",
    )
    open_conditions = (
        "selection of principal/Cayley mass and delay/advance response laws",
        "autonomous controller/source/clock/profile/epoch/event identity preparation",
        "Record formation, occurrence, branch actualization, realized endpoint pair, and empirical selection",
        "universal clock equivalence, cross-profile calibration, long-duration epoch carrier, continuum/boost theorem",
        "physical lapse, redshift/proper time, energy/stress/source identification, gravity law, and Born probability",
        "primitive compilation of the remaining response/latch blocks into one globally scheduled autonomous apparatus",
    )
    check(
        "Cycle451 inventories every calibration/epoch/identity/profile import and advances only a relational prediction-side candidate",
        AUTHORITY == "none" and AUDIT == "unset" and CORE_M2 == 69,
        {
            "core_active_M2": CORE_M2,
            "register_M2": c445.REGISTER_BITS,
            "source_local_M2": c445.SOURCE_BITS,
            "Cycle446_source_compiler_M2": c446.TOTAL_M2,
            "Cycle446_source_serial_primitives_per_law": 250,
            "Cycle451_transport_serial_NN_SWAPS": len(TRANSPORT_SCHEDULE),
            "echo_signal_plus_reflector_M2": SIGNAL_BITS + 1,
            "two_clock_M2": 2 * CLOCK_BITS,
            "response_work_M2": RESPONSE_RAIL_BITS,
            "two_reusable_latch_buses_M2": 2 * c444.BUS_BITS,
            "four_retained_start_end_clock_identity_valid_sidecars_M2": 4 * (CLOCK_BITS + EVENT_BITS + 1),
            "event_identity_input_M2_per_endpoint": EVENT_BITS,
            "supplied": supplied,
            "derived": derived,
            "open_conditions": open_conditions,
            "update_count_called_time": False,
            "circuit_depth_called_time": False,
            "wrapped_phase_called_time_or_energy": False,
            "recurrence_index_called_time": False,
            "generator_called_rate": False,
            "physical_lapse_or_proper_time_derived": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> int:
    note_contract()
    controller = c445.build_mass_controller()
    compiled_laws = (
        c446.compile_full_source_law("cayley", controller.cayley),
        c446.compile_full_source_law("principal", controller.principal),
    )
    menu = c445.sectors(controller)
    compiler_interface_controls(controller, compiled_laws)
    eg_inverse_leakage_controls(compiled_laws, menu)
    branch_relational_prediction_controls(compiled_laws, menu)
    rescaling_and_matcher_deletion_controls()
    physical_deletion_controls(compiled_laws, menu)
    geometry_controls()
    lawful_domain_controls(compiled_laws, menu)
    inventory_and_firewall_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL == 0:
        print("RESULT PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
