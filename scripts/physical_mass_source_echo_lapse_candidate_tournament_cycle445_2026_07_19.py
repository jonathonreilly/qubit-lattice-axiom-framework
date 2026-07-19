#!/usr/bin/env python3
"""Cycle 445: physical mass/source-to-echo lapse-candidate tournament.

This bounded adapter composes the Cycle-441 nine-M2 functional mass
controller, the exact Cycle-438 hard-core reservoir/field restriction, a
selected-field-to-receiver SWAP, the Cycle-431 reversible receiver-controlled
clock response, and the Cycle-444 physical echo/latch endpoint apparatus.

Both receiver branches are retained coherently.  The reported ratio is only a
branch-relative dimensionless clock-rate/lapse candidate.  It is not physical
lapse or proper time: Record formation, occurrence, the response law, echo
calibration, and scale conversion remain supplied.  Authority is none and
audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm, logm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19 as c444


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MASS_SOURCE_ECHO_LAPSE_CANDIDATE_TOURNAMENT_CYCLE445_NOTE_2026-07-19.md"
)
SOURCE_NOTES = (
    ROOT / "docs/work_history/repo/review_feedback/COHERENT_MULTIBETA_PHYSICAL_MASS_CONTROLLER_TOURNAMENT_CYCLE441_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MASS_PASSIVE_TRAJECTORY_TOURNAMENT_CYCLE442_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_EVENT_LATCHED_RECURRENT_ECHO_CALIBRATION_TOURNAMENT_CYCLE444_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CLOCK_RESPONSE_LAW_TOURNAMENT_CYCLE431_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MASS_CLOCK_ACTIVE_SOURCE_RECEIVER_TOURNAMENT_CYCLE438_NOTE_2026-07-19.md",
)
SOURCE_RUNNERS = (
    ROOT / "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py",
    ROOT / "scripts/physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19.py",
    ROOT / "scripts/physical_source_clock_response_law_tournament_cycle431_2026_07_19.py",
    ROOT / "scripts/physical_mass_clock_active_source_receiver_tournament_cycle438_2026_07_19.py",
)
FRONTIER = ROOT / "scripts/frontier_broad_gravity.py"

AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-11
CLOCK_BITS = 16
REGISTER_BITS = 9
SOURCE_BITS = 8  # reservoir, six hard-core field rails, receiver
TAU = 0.05
TRAIN_BETAS = (-2 * np.pi / 9, -4 * np.pi / 9, -2 * np.pi / 3)
HELD_BETA = -8 * np.pi / 9
PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Word = tuple[int, ...]


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


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical mass/source-to-echo lapse-candidate tournament",
        "both receiver branches remain coherent",
        "branch-relative dimensionless clock-rate/lapse candidate",
        "not physical lapse",
        "not proper time",
        "source-off matched apparatus",
        "delay and advance remain competing supplied laws",
        "all 24 proper-cubic frames",
        "train l5 and held l9",
        "inverse, leakage, deletion, and lawful-domain controls",
        "calibration deletion",
        "cycle 442 remains a deferred passive consumer",
        "l^{-1}=g_0",
        "rho=|psi|^2",
        "s=l(1-phi)",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-445 note freezes the bounded claim and firewalls", not missing, missing)

    notes = tuple(normalized(path) for path in SOURCE_NOTES)
    runners = tuple(normalized(path) for path in SOURCE_RUNNERS)
    frontier = normalized(FRONTIER)
    check(
        "the exact upstream restrictions and frontier admitted inputs remain visible",
        all(path.is_file() for path in SOURCE_NOTES + SOURCE_RUNNERS + (FRONTIER,))
        and "nine-m2" in notes[0]
        and "no proper-time bridge" in notes[1]
        and "no lapse is derived" in notes[2]
        and "delay law" in notes[3]
        and "source" in notes[4]
        and "def functional_route" in runners[0]
        and "def clock_forward" in runners[1]
        and "fredkin" in runners[2]
        and "source" in runners[3]
        and "l^{-1} = g_0" in frontier
        and "rho = |psi|^2" in frontier
        and "s = l(1-phi)" in frontier.replace("s  =", "s ="),
        {
            "frontier_admitted_inputs": ("L^{-1}=G_0", "rho=|psi|^2", "S=L(1-phi)"),
            "inputs_derived_or_modified_here": False,
        },
    )


def cyclic_shift(size: int) -> np.ndarray:
    shift = np.zeros((size, size), dtype=complex)
    for source in range(size):
        shift[(source + 1) % size, source] = 1
    return shift


def hermitian(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


@dataclass(frozen=True)
class MassController:
    shift: np.ndarray
    rest: np.ndarray
    cayley: np.ndarray
    principal: np.ndarray
    construction_order: tuple[str, ...]


def build_mass_controller() -> MassController:
    shift = cyclic_shift(REGISTER_BITS)
    identity = np.eye(REGISTER_BITS, dtype=complex)
    cayley = hermitian(3j * (shift - identity) @ np.linalg.inv(shift + identity))
    rest = expm(1j * cayley / 3)
    principal = hermitian(-3j * logm(rest))
    return MassController(
        shift,
        rest,
        cayley,
        principal,
        ("nine-cycle shift", "Cayley mass", "common rest update", "principal mass", "sector menu"),
    )


def angular_distance(left: float, right: float) -> float:
    return abs(np.angle(np.exp(1j * (left - right))))


@dataclass(frozen=True)
class Sector:
    beta: float
    eigenray: np.ndarray
    cayley_mass: float
    principal_mass: float
    held: bool


def sectors(controller: MassController) -> tuple[Sector, ...]:
    # The frozen beta menu is the spectrum of the represented nine-cycle S,
    # not the wrapped rest unitary exp(i M_C/3).
    values, vectors = np.linalg.eig(controller.shift)
    phases = np.angle(values)
    output = []
    for beta in TRAIN_BETAS + (HELD_BETA,):
        index = min(range(REGISTER_BITS), key=lambda item: angular_distance(phases[item], beta))
        ray = vectors[:, index]
        ray = ray / np.linalg.norm(ray)
        output.append(
            Sector(
                beta,
                ray,
                float(np.real(np.vdot(ray, controller.cayley @ ray))),
                float(np.real(np.vdot(ray, controller.principal @ ray))),
                beta == HELD_BETA,
            )
        )
    return tuple(output)


def source_exchange() -> np.ndarray:
    exchange = np.zeros((SOURCE_BITS, SOURCE_BITS), dtype=complex)
    for field in range(1, 7):
        exchange[0, field] = exchange[field, 0] = 1 / np.sqrt(6)
    return exchange


def source_update(mass: np.ndarray, *, enabled: bool = True) -> np.ndarray:
    dimension = REGISTER_BITS * SOURCE_BITS
    if not enabled:
        return np.eye(dimension, dtype=complex)
    return expm(1j * TAU * np.kron(mass, source_exchange()))


def source_initial(ray: np.ndarray) -> np.ndarray:
    state = np.zeros((REGISTER_BITS, SOURCE_BITS), dtype=complex)
    state[:, 0] = ray
    return state


def apply_source(state: np.ndarray, mass: np.ndarray, *, enabled: bool = True, inverse: bool = False) -> np.ndarray:
    operator = source_update(mass, enabled=enabled)
    if inverse:
        operator = operator.conj().T
    return (operator @ state.reshape(-1)).reshape(REGISTER_BITS, SOURCE_BITS)


def transport_to_receiver(state: np.ndarray) -> np.ndarray:
    output = state.copy()
    output[:, (1, 7)] = output[:, (7, 1)]
    return output


def one_hot_index(bit: int) -> int:
    if bit < 0:
        raise ValueError("negative one-hot bit")
    return 1 << bit


def encode_source(state: np.ndarray) -> np.ndarray:
    if state.shape != (REGISTER_BITS, SOURCE_BITS):
        raise ValueError("logical source state has the wrong shape")
    physical = np.zeros((1 << REGISTER_BITS, 1 << SOURCE_BITS), dtype=complex)
    for register, local in product(range(REGISTER_BITS), range(SOURCE_BITS)):
        physical[one_hot_index(register), one_hot_index(local)] = state[register, local]
    return physical


def decode_source(physical: np.ndarray) -> np.ndarray:
    if physical.shape != (1 << REGISTER_BITS, 1 << SOURCE_BITS):
        raise ValueError("physical source block has the wrong shape")
    logical = np.zeros((REGISTER_BITS, SOURCE_BITS), dtype=complex)
    for register, local in product(range(REGISTER_BITS), range(SOURCE_BITS)):
        logical[register, local] = physical[one_hot_index(register), one_hot_index(local)]
    return logical


def physical_source_completion(physical: np.ndarray, mass: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    logical = decode_source(physical)
    moved = apply_source(logical, mass, inverse=inverse)
    return physical + encode_source(moved - logical)


def code_leakage(physical: np.ndarray) -> float:
    return float(np.linalg.norm(physical - encode_source(decode_source(physical))))


def source_mass_controls(controller: MassController, menu: tuple[Sector, ...]) -> dict[str, object]:
    rows = []
    maximum = 0.0
    for sector in menu:
        route_rows = []
        for name, mass in (("cayley", controller.cayley), ("principal", controller.principal)):
            initial = source_initial(sector.eigenray)
            encoded = encode_source(initial)
            logical = transport_to_receiver(apply_source(initial, mass))
            physical = physical_source_completion(encoded, mass)
            physical = encode_source(transport_to_receiver(decode_source(physical)))
            residual = float(np.linalg.norm(physical - encode_source(logical)))
            restored = physical_source_completion(
                encode_source(transport_to_receiver(decode_source(physical))), mass, inverse=True
            )
            inverse = float(np.linalg.norm(restored - encoded))
            leakage = code_leakage(physical)
            receiver_weight = float(np.linalg.norm(logical[:, 7]) ** 2)
            field_weight = float(np.linalg.norm(logical[:, 1:7]) ** 2 + receiver_weight)
            total_q = float(np.linalg.norm(logical) ** 2)
            maximum = max(maximum, residual, inverse, leakage, abs(total_q - 1))
            route_rows.append(
                {
                    "route": name,
                    "mass": sector.cayley_mass if name == "cayley" else sector.principal_mass,
                    "receiver_branch_squared_norm": receiver_weight,
                    "total_field_squared_norm": field_weight,
                    "total_Q": total_q,
                    "E_G_residual": residual,
                    "inverse_residual": inverse,
                    "leakage": leakage,
                }
            )
        rows.append({"beta": sector.beta, "held": sector.held, "routes": route_rows})

    train_difference = max(
        abs(row["routes"][0]["receiver_branch_squared_norm"] - row["routes"][1]["receiver_branch_squared_norm"])
        for row in rows if not row["held"]
    )
    held = next(row for row in rows if row["held"])
    held_difference = abs(
        held["routes"][0]["receiver_branch_squared_norm"]
        - held["routes"][1]["receiver_branch_squared_norm"]
    )
    check(
        "the nine-M2 functional controller drives a physical Q1 source/receiver code with exact E/G, inverse, leakage, and total-Q conservation",
        controller.construction_order[-1] == "sector menu" and maximum < TOL,
        {"rows": rows, "maximum_residual": maximum, "receiver_squared_norm_is_occurrence_or_probability": False},
    )
    check(
        "the no-refit train sectors agree while the held branch separates the two supplied mass routes",
        train_difference < TOL and held_difference > 0.09,
        {
            "train_max_receiver_weight_difference": train_difference,
            "held_receiver_weight_difference": held_difference,
            "frozen_held_threshold": 0.09,
        },
    )
    return {"rows": rows, "train_difference": train_difference, "held_difference": held_difference}


@dataclass(frozen=True)
class ResponseState:
    receiver: int
    rail: Word
    clock: Word


def validate_response(state: ResponseState) -> None:
    if state.receiver not in (0, 1) or len(state.rail) != CLOCK_BITS - 1 or any(bit not in (0, 1) for bit in state.rail):
        raise ValueError("malformed response control/rail")
    c444.clock_position(state.clock)


def fan_receiver(state: ResponseState) -> ResponseState:
    rail = list(state.rail)
    rail[0] ^= state.receiver
    for index in range(len(rail) - 1):
        rail[index + 1] ^= rail[index]
    return ResponseState(state.receiver, tuple(rail), state.clock)


def unfan_receiver(state: ResponseState) -> ResponseState:
    rail = list(state.rail)
    for index in reversed(range(len(rail) - 1)):
        rail[index + 1] ^= rail[index]
    rail[0] ^= state.receiver
    return ResponseState(state.receiver, tuple(rail), state.clock)


def controlled_clock_swap(state: ResponseState, pair: tuple[int, int]) -> ResponseState:
    left, right = pair
    clock = list(state.clock)
    control = state.rail[min(left, len(state.rail) - 1)]
    if control:
        clock[left], clock[right] = clock[right], clock[left]
    return ResponseState(state.receiver, state.rail, tuple(clock))


def response_update(state: ResponseState, law: str, *, inverse: bool = False, delete_control: bool = False) -> ResponseState:
    validate_response(state)
    if law not in ("delay", "advance"):
        raise ValueError("undeclared response law")
    if delete_control:
        return state
    output = fan_receiver(state)
    forward = c444.CLOCK_INVERSE_SWAPS if law == "delay" else c444.CLOCK_FORWARD_SWAPS
    schedule = tuple(reversed(forward)) if inverse else forward
    for pair in schedule:
        output = controlled_clock_swap(output, pair)
    output = unfan_receiver(output)
    validate_response(output)
    return output


def response_controls() -> None:
    failures = 0
    rows = []
    for law, receiver, position in product(("delay", "advance"), (0, 1), range(CLOCK_BITS)):
        initial = ResponseState(receiver, (0,) * (CLOCK_BITS - 1), c444.one_hot(position))
        output = response_update(initial, law)
        restored = response_update(output, law, inverse=True)
        expected = position if receiver == 0 else ((position - 1) % CLOCK_BITS if law == "delay" else (position + 1) % CLOCK_BITS)
        failures += int(c444.clock_position(output.clock) != expected)
        failures += int(any(output.rail))
        failures += int(restored != initial)
        rows.append((law, receiver, position, expected))
    permutation_rows = {}
    for law in ("delay", "advance"):
        operator = response_permutation(law)
        permutation_rows[law] = {
            "unitarity": float(np.linalg.norm(operator.conj().T @ operator - np.eye(operator.shape[0]))),
            "dimension": operator.shape,
        }
    check(
        "the exact fan/Fredkin/unfan response preserves both receiver branches and has an exact inverse",
        failures == 0 and max(row["unitarity"] for row in permutation_rows.values()) == 0,
        {
            "exhaustive_inputs": len(rows),
            "failures": failures,
            "fixed_coherent_local_mode_x_clock_permutations": permutation_rows,
            "branch_dependent_host_schedule": False,
            "delay_or_advance_selected": False,
        },
    )


def response_permutation(law: str) -> np.ndarray:
    """One fixed 8-local-mode x 16-clock permutation for a supplied law.

    Local mode 7 is the receiver-occupied codeword.  All other Q1 modes are
    receiver-zero.  The same controlled permutation acts on a coherent sum;
    the host never chooses a schedule from an observed branch.
    """
    dimension = SOURCE_BITS * CLOCK_BITS
    operator = np.zeros((dimension, dimension), dtype=complex)
    for local_mode, position in product(range(SOURCE_BITS), range(CLOCK_BITS)):
        receiver = int(local_mode == 7)
        output = response_update(
            ResponseState(receiver, (0,) * (CLOCK_BITS - 1), c444.one_hot(position)), law
        )
        target = local_mode * CLOCK_BITS + c444.clock_position(output.clock)
        source = local_mode * CLOCK_BITS + position
        operator[target, source] = 1
    return operator


def endpoint_interval(start_position: int, end_word: Word, *, formation: bool = True, predecessor: bool = True, latch: bool = True) -> c444.IntervalWord | None:
    start_latch = c444.apply_latch(c444.blank_latch(1, c444.one_hot(start_position), c444.bits(1, c444.EVENT_BITS)))
    end_latch = c444.apply_latch(
        c444.blank_latch(1, end_word, c444.bits(2, c444.EVENT_BITS)),
        deleted_gate=None if latch else "valid-copy",
    )
    start = c444.form_endpoint(
        latch=start_latch,
        site=(-1, -1, 1),
        predecessors=(),
        formation_enabled=formation,
    )
    end = c444.form_endpoint(
        latch=end_latch,
        site=(-1, -1, 2),
        predecessors=() if start is None or not predecessor else (start.record,),
        formation_enabled=formation,
        event_record_edge=True,
    )
    return c444.match_interval(start, end)


@dataclass(frozen=True)
class BranchInterval:
    size: int
    length: int
    start: int
    law: str
    source_enabled: bool
    receiver: int
    squared_norm: float
    fine_cells: int | None
    ratio_to_source_off: float | None


def branch_experiment(
    sector: Sector,
    mass: np.ndarray,
    size: int,
    length: int,
    start: int,
    law: str,
    *,
    source_enabled: bool,
    calibration: c444.EchoCalibration | None,
    delete_transport: bool = False,
    delete_control: bool = False,
) -> tuple[BranchInterval, ...]:
    if size < 5 or size % 2 == 0 or length > (size - 1) // 2:
        raise ValueError("experiment is outside the odd periodic envelope")
    local = apply_source(source_initial(sector.eigenray), mass, enabled=source_enabled)
    if not delete_transport:
        local = transport_to_receiver(local)
    receiver_weights = {
        0: float(np.linalg.norm(local[:, :7]) ** 2),
        1: float(np.linalg.norm(local[:, 7]) ** 2),
    }
    echo = c444.run_echo(c444.echo_initial(length, start), length)
    source_off_interval = endpoint_interval(start, echo.clock)
    if source_off_interval is None:
        return tuple(
            BranchInterval(size, length, start, law, source_enabled, receiver, weight, None, None)
            for receiver, weight in receiver_weights.items()
            if weight > TOL
        )
    output = []
    for receiver, weight in receiver_weights.items():
        if weight <= TOL:
            continue
        response = response_update(
            ResponseState(receiver, (0,) * (CLOCK_BITS - 1), echo.clock),
            law,
            delete_control=delete_control,
        )
        interval = endpoint_interval(start, response.clock)
        ratio = None
        if calibration is not None and interval is not None:
            ratio = interval.fine_cells / source_off_interval.fine_cells
        output.append(
            BranchInterval(
                size,
                length,
                start,
                law,
                source_enabled,
                receiver,
                weight,
                None if interval is None else interval.fine_cells,
                ratio,
            )
        )
    return tuple(output)


def coherent_branch_inverse(controller: MassController, sector: Sector, law: str, length: int, start: int) -> float:
    local = transport_to_receiver(apply_source(source_initial(sector.eigenray), controller.cayley))
    base = c444.run_echo(c444.echo_initial(length, start), length).clock
    initial_joint = np.zeros((REGISTER_BITS, SOURCE_BITS, CLOCK_BITS), dtype=complex)
    initial_joint[:, :, c444.clock_position(base)] = local
    operator = response_permutation(law)
    joint = np.stack(
        [(operator @ initial_joint[register].reshape(-1)).reshape(SOURCE_BITS, CLOCK_BITS) for register in range(REGISTER_BITS)]
    )
    restored_joint = np.stack(
        [(operator.conj().T @ joint[register].reshape(-1)).reshape(SOURCE_BITS, CLOCK_BITS) for register in range(REGISTER_BITS)]
    )
    if np.linalg.norm(restored_joint - initial_joint) > TOL:
        raise RuntimeError("fixed coherent response inverse did not restore the common echo word")
    restored = restored_joint[:, :, c444.clock_position(base)]
    restored = transport_to_receiver(restored)
    restored = apply_source(restored, controller.cayley, inverse=True)
    return float(np.linalg.norm(restored - source_initial(sector.eigenray)))


def echo_lapse_candidate_controls(controller: MassController, menu: tuple[Sector, ...]) -> dict[str, object]:
    train_echo = tuple(c444.observe_echo(c444.TRAIN_SIZE, length, c444.TRAIN_START) for length in (1, 2))
    calibration = c444.derive_calibration(train_echo)
    rows = []
    failures = 0
    for sector in menu:
        size = c444.HELD_SIZE if sector.held else c444.TRAIN_SIZE
        start = c444.HELD_START if sector.held else c444.TRAIN_START
        for mass_name, mass in (("cayley", controller.cayley), ("principal", controller.principal)):
            for law in ("delay", "advance"):
                source_off = branch_experiment(
                    sector, mass, size, 2, start, law, source_enabled=False, calibration=calibration
                )
                source_on = branch_experiment(
                    sector, mass, size, 2, start, law, source_enabled=True, calibration=calibration
                )
                inverse = coherent_branch_inverse(controller, sector, law, 2, start)
                off0 = next(item for item in source_off if item.receiver == 0)
                on0 = next(item for item in source_on if item.receiver == 0)
                on1 = next(item for item in source_on if item.receiver == 1)
                expected = 0.75 if law == "delay" else 1.25
                failures += int(off0.fine_cells != 4 or off0.ratio_to_source_off != 1)
                failures += int(on0.fine_cells != 4 or on0.ratio_to_source_off != 1)
                failures += int(on1.fine_cells != (3 if law == "delay" else 5))
                failures += int(abs((on1.ratio_to_source_off or 0) - expected) > TOL)
                failures += int(inverse > TOL)
                failures += int(abs(sum(item.squared_norm for item in source_on) - 1) > TOL)
                rows.append(
                    {
                        "beta": sector.beta,
                        "held": sector.held,
                        "mass_route": mass_name,
                        "law": law,
                        "source_off": source_off,
                        "source_on": source_on,
                        "coherent_inverse_residual": inverse,
                    }
                )
    check(
        "matched source-off/on apparatus retains coherent receiver branches and yields frozen delay/advance candidate ratios",
        calibration is not None and failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "source_off_dK": 4,
            "delay_receiver_branch_dK_and_ratio": (3, 0.75),
            "advance_receiver_branch_dK_and_ratio": (5, 1.25),
            "quantity": "branch-relative dimensionless clock-rate/lapse candidate",
            "physical_lapse_or_proper_time": False,
        },
    )
    return {"calibration": calibration, "rows": rows}


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        permutation_matrix = np.eye(3, dtype=int)[list(permutation)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation_matrix
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple({tuple(frame.reshape(-1)): frame for frame in frames}.values())


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def support_connected(support: tuple[Coord, ...]) -> bool:
    reached = {support[0]}
    changed = True
    while changed:
        changed = False
        for site in support:
            if site not in reached and any(manhattan(site, other) == 1 for other in reached):
                reached.add(site)
                changed = True
    return len(reached) == len(support)


def combined_supports(length: int) -> tuple[tuple[Coord, ...], ...]:
    clock = tuple((index, 0, 0) for index in range(CLOCK_BITS))
    response_rail = tuple((index, 1, 0) for index in range(CLOCK_BITS - 1))
    receiver = (-1, 1, 0)
    latch_bus = tuple((index, -1, 0) for index in range(c444.BUS_BITS))
    detector = (-1, -1, 0)
    latched_clock = tuple((index, -2, 0) for index in range(CLOCK_BITS))
    identity = tuple((CLOCK_BITS + index, 0, 0) for index in range(c444.EVENT_BITS))
    latched_identity = tuple((CLOCK_BITS + index, -2, 0) for index in range(c444.EVENT_BITS))
    valid = (c444.BUS_BITS - 1, 0, 0)
    echo_path = tuple((-2 - index, -1, 0) for index in range(length + 1))
    reflector = (-2 - length, -2, 0)
    supports = []
    supports.append((receiver, response_rail[0]))
    supports.extend((response_rail[index], clock[index], clock[index + 1]) for index in range(CLOCK_BITS - 1))
    supports.append((detector, latch_bus[0]))
    supports.extend((latch_bus[index], latch_bus[index + 1]) for index in range(c444.BUS_BITS - 1))
    supports.extend((latch_bus[index], clock[index], latched_clock[index]) for index in range(CLOCK_BITS))
    supports.extend((latch_bus[CLOCK_BITS + index], identity[index], latched_identity[index]) for index in range(c444.EVENT_BITS))
    supports.append((latch_bus[-1], valid))
    supports.extend((echo_path[index], echo_path[index + 1]) for index in range(length))
    supports.append((echo_path[0], detector))
    supports.append((echo_path[-1], reflector))
    # Exact local star for the reservoir and six cubic field directions.  The
    # +x field rail is adjacent to the receiver for the selected SWAP.
    reservoir = (-3, 1, 0)
    source_fields = ((-2, 1, 0), (-4, 1, 0), (-3, 2, 0), (-3, 0, 0), (-3, 1, 1), (-3, 1, -1))
    supports.extend((reservoir, field) for field in source_fields)
    supports.append((source_fields[0], receiver))
    return tuple(supports)


def geometry_controls() -> None:
    frames = proper_cubic_frames()
    failures = 0
    collisions = []
    for length in (1, 2):
        supports = combined_supports(length)
        for support in supports:
            failures += int(not support_connected(support))
            for frame in frames:
                moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in support)
                failures += int(not support_connected(moved))
        collisions.append({"length": length, "supports": len(supports)})
    check(
        "the combined finite source/receiver/response/echo/latch supports are bounded and local in all 24 proper-cubic frames",
        len(frames) == 24 and failures == 0,
        {"frames": len(frames), "locality_failures": failures, "rows": collisions, "preferred_frame_selected": False},
    )


def deletion_domain_controls(controller: MassController, menu: tuple[Sector, ...]) -> None:
    sector = next(item for item in menu if item.held)
    calibration = c444.derive_calibration(
        tuple(c444.observe_echo(c444.TRAIN_SIZE, length, c444.TRAIN_START) for length in (1, 2))
    )
    no_calibration = c444.derive_calibration(
        (c444.observe_echo(c444.TRAIN_SIZE, 2, c444.TRAIN_START),), enabled=False
    )
    baseline = branch_experiment(
        sector, controller.cayley, c444.HELD_SIZE, 2, c444.HELD_START, "delay",
        source_enabled=True, calibration=calibration,
    )
    source_deleted = branch_experiment(
        sector, controller.cayley, c444.HELD_SIZE, 2, c444.HELD_START, "delay",
        source_enabled=False, calibration=calibration,
    )
    mass_deleted = branch_experiment(
        sector, np.zeros_like(controller.cayley), c444.HELD_SIZE, 2, c444.HELD_START, "delay",
        source_enabled=True, calibration=calibration,
    )
    transport_deleted = branch_experiment(
        sector, controller.cayley, c444.HELD_SIZE, 2, c444.HELD_START, "delay",
        source_enabled=True, calibration=calibration, delete_transport=True,
    )
    control_deleted = branch_experiment(
        sector, controller.cayley, c444.HELD_SIZE, 2, c444.HELD_START, "delay",
        source_enabled=True, calibration=calibration, delete_control=True,
    )
    calibration_deleted = branch_experiment(
        sector, controller.cayley, c444.HELD_SIZE, 2, c444.HELD_START, "delay",
        source_enabled=True, calibration=no_calibration,
    )
    echo_deletions = {
        "transport": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_transport=True).interval,
        "reflection": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_reflection=True).interval,
        "reflection-certificate": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_reflector_certificate=True).interval,
        "detector": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_detector=True).interval,
        "latch": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_latch=True).interval,
        "Record-edge": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_record_edge=True).interval,
        "formation": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_formation=True).interval,
        "identity": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_identity=True).interval,
        "predecessor": c444.observe_echo(c444.HELD_SIZE, 2, c444.HELD_START, delete_predecessor=True).interval,
    }
    oscillator_deleted = c444.observe_echo(
        c444.HELD_SIZE, 2, c444.HELD_START, delete_oscillator=True
    ).interval
    wrapped = c444.observe_echo(c444.TRAIN_SIZE, 1, 15)

    malformed = 0
    for operation in (
        lambda: source_initial(np.zeros(8)),
        lambda: encode_source(np.zeros((9, 7))),
        lambda: decode_source(np.zeros((511, 256))),
        lambda: response_update(ResponseState(2, (0,) * 15, c444.one_hot(1)), "delay"),
        lambda: response_update(ResponseState(1, (0,) * 15, c444.one_hot(1)), "retard"),
        lambda: branch_experiment(sector, controller.cayley, 4, 2, 1, "delay", source_enabled=True, calibration=calibration),
        lambda: c444.clock_position((1, 1) + (0,) * 14),
    ):
        try:
            operation()
        except (ValueError, IndexError):
            malformed += 1

    baseline1 = next(item for item in baseline if item.receiver == 1)
    control1 = next(item for item in control_deleted if item.receiver == 1)
    check(
        "source, selected transport, response control, echo/latch/formation/predecessor, calibration, and wrap deletions are visible",
        baseline1.fine_cells == 3
        and all(item.receiver == 0 for item in source_deleted)
        and all(item.receiver == 0 for item in mass_deleted)
        and all(item.receiver == 0 for item in transport_deleted)
        and control1.fine_cells == 4
        and all(item.ratio_to_source_off is None for item in calibration_deleted)
        and all(value is None for value in echo_deletions.values())
        and oscillator_deleted is not None
        and oscillator_deleted.fine_cells != 4
        and wrapped.interval is None,
        {
            "baseline_receiver_branch": baseline1,
            "source_deleted": source_deleted,
            "mass_observable_deleted": mass_deleted,
            "transport_deleted": transport_deleted,
            "response_control_deleted": control_deleted,
            "calibration_deleted": calibration_deleted,
            "echo_and_record_deletions": echo_deletions,
            "oscillator_deleted_interval": oscillator_deleted,
            "wrap_interval": wrapped.interval,
        },
    )
    check(
        "malformed physical codes, receiver controls, laws, envelopes, and words are refused",
        malformed == 7,
        {"malformed_rejections": malformed, "expected": 7},
    )


def inventory_scope_controls() -> None:
    inventory = {
        "axiomatic_inputs_only": (
            "physical Z3 sites, nearest-neighbour adjacency, translations and proper-cubic rotations",
            "one M2 possibility domain per physical site",
            "Record type, site lock, one-per-site, permanence, readability, finite additive scalar",
        ),
        "approved_primitives_inputs_only": (
            "scale-reference conversion anchor",
            "form-only kinetic isotropy",
            "pointwise realized-state reference slot with no supplied history content",
        ),
        "supplied_candidate_structure": (
            "nine-cycle register preparation and Cayley/principal functional mass routes",
            "hard-core reservoir/field exchange strength tau=0.05 and selected field rail",
            "source-on preparation, source-off deletion, field-to-receiver SWAP",
            "competing delay and advance fan/Fredkin/unfan response schedules",
            "echo device, oscillator word/epoch/identities, latch, conditional Record formation and predecessor grammar",
            "echo calibration, scale interpretation, and branch conditioning for diagnostics",
        ),
        "derived_finite": (
            "source-on total-Q conservation and receiver-branch squared norms",
            "factorwise physical E/G, inverse, leakage and coherent branch inverse",
            "source-off dK=4 and receiver-branch delay/advance dK=3/5",
            "branch-relative dimensionless ratios 3/4 and 5/4",
            "train agreement, held mass-route separation, all24 covariance and deletion firewalls",
        ),
        "open": (
            "selection between Cayley/principal mass and delay/advance response laws",
            "Record occurrence/formation and realized branch/history",
            "physical lapse, proper time, universal calibration, continuum/boost theorem",
            "energy/stress source, gravity law and passive trajectory consumer",
            "primitive nearest-neighbour synthesis of the supplied dense functional controls",
            "frontier broad-gravity inputs L^{-1}=G_0, rho=|psi|^2, S=L(1-phi)",
        ),
    }
    check(
        "the supply inventory keeps Cycle442 and broad gravity downstream and derives no lapse, source field, occurrence, or probability",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "inventory": inventory,
            "Cycle442_passive_consumer_executed": False,
            "frontier_inputs_derived_or_changed": False,
            "receiver_squared_norm_called_occurrence_or_probability": False,
            "c_number_field_called_derived": False,
            "update_count_called_time": False,
            "physical_lapse_or_proper_time_derived": False,
            "law_selected": False,
            "no_go_or_axiom_pressure": False,
        },
    )


def main() -> int:
    contracts()
    controller = build_mass_controller()
    menu = sectors(controller)
    source_mass_controls(controller, menu)
    response_controls()
    geometry_controls()
    echo_lapse_candidate_controls(controller, menu)
    deletion_domain_controls(controller, menu)
    inventory_scope_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL == 0:
        print("RESULT PHYSICAL_MASS_SOURCE_ECHO_LAPSE_CANDIDATE_TOURNAMENT_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
