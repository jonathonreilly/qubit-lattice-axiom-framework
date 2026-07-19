#!/usr/bin/env python3
"""Cycle 431: physical source-to-clock-response law tournament.

On the Cycle-425 cubic Q1 hard-core field and Cycle-428 sixteen-M2 one-hot
oscillator, compare two fixed reversible hypotheses.  After one common
three-sweep clock baseline, a selected local field-occupation M2 coherently
controls either an inverse sweep (delay law) or a forward sweep (advance law).
The two laws share every input and are not selected.

Occupation controls bounded Fredkin circuits directly; no expectation or host
branch controls a gate.  Field occupation is not energy, source, stress, or a
Born weight.  A latched word is a reversible event candidate, not a Record.
Clock-word displacement is dimensionless and is not metric time, a rate,
proper time, lapse, or Lorentz structure.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_cubic_transient_stationary_update_cycle425_2026_07_19 as c425
import physical_detector_record_clock_map_candidate_cycle428_2026_07_19 as c428


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_CLOCK_RESPONSE_LAW_TOURNAMENT_CYCLE431_NOTE_2026-07-19.md"
)
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
FIREWALL = ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md"
CYCLE416_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_STRICT_RESPONSE_SOURCE_CLOCK_METRIC_RECEIVER_CYCLE416_NOTE_2026-07-18.md"
)
CYCLE420_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_PREDICTION_BRIDGE_CONTRACT_CYCLE420_NOTE_2026-07-19.md"
)
CYCLE425_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "COMMON_CUBIC_TRANSIENT_STATIONARY_UPDATE_CYCLE425_NOTE_2026-07-19.md"
)
CYCLE426_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CYCLE426_NOTE_2026-07-19.md"
)
CYCLE428_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DETECTOR_RECORD_CLOCK_MAP_CANDIDATE_CYCLE428_NOTE_2026-07-19.md"
)

AUTHORITY = "none"
AUDIT = "unset"
CLOCK_BITS = c428.CLOCK_BITS
CONTROL_RAIL_BITS = CLOCK_BITS - 1
BASE_SWEEPS = 3
TRAIN_LENGTH = 5
HELD_LENGTH = 9
TOL = 8.0e-11
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
        "one declared physical common code",
        "delay law",
        "advance law",
        "neither law is selected",
        "occupation-controlled fredkin",
        "no expectation or host branch controls a gate",
        "exact inverse",
        "field-q and clock-hamming ledgers",
        "blank control rail cleanup",
        "all 24 proper-cubic frames",
        "transient source seed",
        "stationary dressed input",
        "periodic l=5 training and held l=9",
        "held distance and response strength",
        "source, coupling, and clock deletions",
        "alias, wrap, and lawful-domain controls",
        "cycle-428 event/record latch boundary",
        "dimensionless clock-word displacement",
        "cycle-416 and cycle-420 matching coordinates",
        "metric, lapse, proper-time, and lorentz flags remain false",
        "coupling, initial phase, response sign and strength, unit, calibration, formation law, occurrence, and empirical selection remain supplied or open",
        "field occupation is not energy, source, stress, or a born weight",
        "update count and eigenphase are not time or a rate",
        "positive competing-law result",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-431 note freezes the competing-law and semantic contract", not missing, missing)

    axioms = normalized(AXIOMS)
    firewall = normalized(FIREWALL)
    c416 = normalized(CYCLE416_NOTE)
    c420 = normalized(CYCLE420_NOTE)
    c425 = normalized(CYCLE425_NOTE)
    c426 = normalized(CYCLE426_NOTE)
    c428 = normalized(CYCLE428_NOTE)
    check(
        "the source stack admits only the physical positive-occupation and dimensionless clock-word coordinates used here",
        "records form" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "requires clock map" in firewall
        and "no metric is reconstructed" in c416
        and "positive occupation information" in c420
        and "signed phase-bearing amplitude/history" in c420
        and "update count is not time" in c425
        and "no host expectation controls a gate" in c426
        and "number is not called energy/source/work" in c426
        and "clock transition is a physical recurrent degree of freedom" in c428
        and "candidate formation is unselected" in c428,
        {
            "matched_source_coordinate": "positive physical hard-core occupation",
            "matched_clock_coordinate": "complete recurrent one-hot word",
            "metric_receiver_promoted": False,
            "signed_profile_or_phase_imported": False,
        },
    )


@dataclass(frozen=True)
class Law:
    name: str
    response_sign: int


DELAY = Law("occupation-conditioned-delay", -1)
ADVANCE = Law("occupation-conditioned-advance", 1)
LAWS = (DELAY, ADVANCE)


@dataclass(frozen=True)
class RailState:
    occupation: int
    rail: Word
    clock: Word


@dataclass(frozen=True)
class Primitive:
    name: str
    support: tuple[Coord, ...]


FIELD_SITE = (-1, 1, 0)
RAIL_SITES = tuple((index, 1, 0) for index in range(CONTROL_RAIL_BITS))
CLOCK_SITES = tuple((index, 0, 0) for index in range(CLOCK_BITS))


def validate_rail_state(state: RailState) -> None:
    if state.occupation not in (0, 1):
        raise ValueError("local field occupation must be one M2 basis value")
    if len(state.rail) != CONTROL_RAIL_BITS or any(bit not in (0, 1) for bit in state.rail):
        raise ValueError("control rail is outside its M2 basis domain")
    c428.clock_position(state.clock)


def fan_schedule() -> tuple[Primitive, ...]:
    output = [Primitive("fan-field", (FIELD_SITE, RAIL_SITES[0]))]
    output.extend(
        Primitive(f"fan-{index}", (RAIL_SITES[index], RAIL_SITES[index + 1]))
        for index in range(CONTROL_RAIL_BITS - 1)
    )
    return tuple(output)


FAN = fan_schedule()


def fredkin_schedule(response_sign: int) -> tuple[Primitive, ...]:
    if response_sign not in (-1, 1):
        raise ValueError("response sign must be delay=-1 or advance=+1")
    pairs = c428.CLOCK_FORWARD_SWAPS if response_sign == 1 else c428.CLOCK_INVERSE_SWAPS
    return tuple(
        Primitive(
            f"fredkin-{response_sign:+d}-{left}",
            (RAIL_SITES[left], CLOCK_SITES[left], CLOCK_SITES[right]),
        )
        for left, right in pairs
    )


def apply_fan(state: RailState, primitive: Primitive) -> RailState:
    rail = list(state.rail)
    if primitive.name == "fan-field":
        rail[0] ^= state.occupation
    elif primitive.name.startswith("fan-"):
        index = int(primitive.name.split("-")[1])
        rail[index + 1] ^= rail[index]
    else:
        raise ValueError("not a fan primitive")
    return replace(state, rail=tuple(rail))


def apply_fredkin(state: RailState, primitive: Primitive) -> RailState:
    left = int(primitive.name.rsplit("-", 1)[1])
    clock = list(state.clock)
    if state.rail[left]:
        clock[left], clock[left + 1] = clock[left + 1], clock[left]
    return replace(state, clock=tuple(clock))


def controlled_response(
    state: RailState,
    law: Law,
    strength: int,
    *,
    inverse: bool = False,
    delete_coupling: bool = False,
) -> RailState:
    validate_rail_state(state)
    if law not in LAWS:
        raise ValueError("unknown source-to-clock response law")
    if strength not in (1, 2):
        raise ValueError("declared response strength must be one or two sweeps")
    current = state
    for primitive in FAN:
        current = apply_fan(current, primitive)
    if not delete_coupling:
        sign = -law.response_sign if inverse else law.response_sign
        schedule = fredkin_schedule(sign)
        for _ in range(strength):
            for primitive in schedule:
                current = apply_fredkin(current, primitive)
    for primitive in reversed(FAN):
        current = apply_fan(current, primitive)
    validate_rail_state(current)
    return current


def baseline(word: Word, *, inverse: bool = False, deleted_swap: int | None = None) -> Word:
    output = word
    operation = c428.clock_inverse if inverse else c428.clock_forward
    for _ in range(BASE_SWEEPS):
        output = operation(output, deleted_swap=deleted_swap)
    return output


def basis_response(
    occupation: int,
    word: Word,
    law: Law,
    strength: int,
    *,
    inverse: bool = False,
    delete_coupling: bool = False,
    delete_clock: bool = False,
) -> Word:
    if delete_clock:
        return word
    state = RailState(occupation, (0,) * CONTROL_RAIL_BITS, word)
    if inverse:
        state = controlled_response(
            state, law, strength, inverse=True, delete_coupling=delete_coupling
        )
        return baseline(state.clock, inverse=True)
    advanced = baseline(word)
    state = replace(state, clock=advanced)
    return controlled_response(
        state, law, strength, delete_coupling=delete_coupling
    ).clock


def physical_circuit_controls() -> None:
    print("\nBOUNDED OCCUPATION-CONTROLLED CLOCK CIRCUITS")
    inverse_failures = hamming_failures = cleanup_failures = 0
    predictions = {}
    for law, strength, occupation, position in product(
        LAWS, (1, 2), (0, 1), range(CLOCK_BITS)
    ):
        initial = c428.one_hot(position)
        output = basis_response(occupation, initial, law, strength)
        restored = basis_response(occupation, output, law, strength, inverse=True)
        inverse_failures += int(restored != initial)
        hamming_failures += int(sum(output) != 1)
        rail_output = controlled_response(
            RailState(occupation, (0,) * CONTROL_RAIL_BITS, baseline(initial)),
            law,
            strength,
        )
        cleanup_failures += int(any(rail_output.rail))
        predictions[(law.name, strength, occupation, position)] = c428.clock_position(output)

    primitives = (
        FAN
        + tuple(reversed(FAN))
        + fredkin_schedule(-1)
        + fredkin_schedule(1)
        + tuple(
            Primitive(f"baseline-{left}", (CLOCK_SITES[left], CLOCK_SITES[right]))
            for left, right in c428.CLOCK_FORWARD_SWAPS
        )
    )
    support_failures = 0
    for primitive in primitives:
        distances = tuple(
            c428.c255.manhattan(left, right)
            for left in primitive.support
            for right in primitive.support
        )
        support_failures += int(max(distances) > 2 or len(primitive.support) not in (2, 3))
        # Every diameter-two Fredkin support is a connected three-site NN path.
        support_failures += int(
            len(primitive.support) == 3
            and sum(
                c428.c255.manhattan(primitive.support[index], primitive.support[index + 1]) == 1
                for index in range(2)
            ) != 2
        )

    sites = (FIELD_SITE,) + RAIL_SITES + CLOCK_SITES
    frame_failures = 0
    for frame in c428.c255.proper_frames():
        moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in sites)
        frame_failures += int(len(moved) != len(set(moved)))
        for primitive in primitives:
            moved_support = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in primitive.support
            )
            frame_failures += int(
                max(
                    c428.c255.manhattan(left, right)
                    for left in moved_support
                    for right in moved_support
                ) > 2
            )

    check(
        "both competing laws are exact reversible bounded circuits with clean work rails and all-frame support",
        inverse_failures == hamming_failures == cleanup_failures == 0
        and support_failures == frame_failures == 0
        and predictions[(DELAY.name, 1, 0, 2)] == 5
        and predictions[(ADVANCE.name, 1, 0, 2)] == 5
        and predictions[(DELAY.name, 1, 1, 2)] == 4
        and predictions[(ADVANCE.name, 1, 1, 2)] == 6,
        {
            "common_clock_baseline_sweeps": BASE_SWEEPS,
            "control_rail_blank_M2": CONTROL_RAIL_BITS,
            "lawful_basis_cases": len(predictions),
            "delay_event_prediction_strength1": 4,
            "free_prediction": 5,
            "advance_event_prediction_strength1": 6,
            "maximum_strength2_Fredkins": 2 * (CLOCK_BITS - 1),
            "maximum_primitive_support_M2": 3,
            "maximum_primitive_support_diameter": 2,
            "proper_cubic_frames": len(c428.c255.proper_frames()),
            "maximum_blank_rail_cleanup_residual": cleanup_failures,
            "maximum_24_frame_support_covariance_residual": frame_failures,
        },
    )


def common_code_eg_controls() -> None:
    """Check E G_logical = G_physical E on the complete control/clock code."""
    print("\nCOMMON-CODE FORWARD E/G AND INVERSE")
    length = 3
    dimension = 7 * length**3
    displacement = tuple(int(value) for value in c425.c210.DIRECTIONS[0])
    control = target_index(length, 1, displacement)
    spectator = c425.reservoir_index(c425.SOURCE_CELL, length)
    forward_residuals = []
    inverse_residuals = []
    field_q_residuals = []
    clock_hamming_residuals = []
    for law, strength, occupation, position in product(
        LAWS, (1, 2), (0, 1), range(CLOCK_BITS)
    ):
        field_index = control if occupation else spectator
        encoded = np.zeros((dimension, CLOCK_BITS), dtype=complex)
        encoded[field_index, position] = 1
        physical = response_gate(encoded, control, law, strength)
        logical_word = basis_response(
            occupation, c428.one_hot(position), law, strength
        )
        expected = np.zeros_like(encoded)
        expected[field_index, c428.clock_position(logical_word)] = 1
        restored = response_gate(
            physical, control, law, strength, inverse=True
        )
        forward_residuals.append(float(np.linalg.norm(physical - expected)))
        inverse_residuals.append(float(np.linalg.norm(restored - encoded)))
        field_q_residuals.append(abs(float(np.vdot(physical, physical).real) - 1))
        clock_hamming_residuals.append(
            abs(
                sum(
                    float(np.linalg.norm(physical[:, clock_position]) ** 2)
                    for clock_position in range(CLOCK_BITS)
                )
                - 1
            )
        )
    check(
        "the logical control/clock permutation and physical common-code response exactly intertwine in both laws",
        max(forward_residuals) == 0
        and max(inverse_residuals) == 0
        and max(field_q_residuals) == 0
        and max(clock_hamming_residuals) == 0,
        {
            "declared_common_code": "Cycle425 cubic Q1 field x Cycle428 one-hot clock",
            "control_sector_representatives": (spectator, control),
            "logical_columns_checked": len(forward_residuals),
            "maximum_forward_EG_residual": max(forward_residuals),
            "maximum_basis_inverse_residual": max(inverse_residuals),
            "maximum_field_Q_ledger_residual": max(field_q_residuals),
            "maximum_clock_Hamming_ledger_residual": max(clock_hamming_residuals),
        },
    )


def shift_clock(joint: np.ndarray, amount: int) -> np.ndarray:
    return np.roll(joint, amount, axis=1)


def response_gate(
    joint: np.ndarray,
    control_index: int,
    law: Law,
    strength: int,
    *,
    inverse: bool = False,
    delete_coupling: bool = False,
    delete_clock: bool = False,
) -> np.ndarray:
    if joint.ndim != 2 or joint.shape[1] != CLOCK_BITS:
        raise ValueError("joint field/clock state has the wrong common-code shape")
    if not 0 <= control_index < joint.shape[0]:
        raise ValueError("local occupation control is outside the field basis")
    if law not in LAWS or strength not in (1, 2):
        raise ValueError("response law or strength is outside the declared domain")
    if delete_clock:
        return joint.copy()
    output = joint.copy()
    if inverse:
        if not delete_coupling:
            output[control_index] = np.roll(
                output[control_index], -law.response_sign * strength
            )
        return shift_clock(output, -BASE_SWEEPS)
    output = shift_clock(output, BASE_SWEEPS)
    if not delete_coupling:
        output[control_index] = np.roll(
            output[control_index], law.response_sign * strength
        )
    return output


def apply_field(operator, joint: np.ndarray) -> np.ndarray:
    return np.asarray(operator @ joint)


def initial_joint(field: np.ndarray, position: int) -> np.ndarray:
    output = np.zeros((len(field), CLOCK_BITS), dtype=complex)
    output[:, position] = field
    return output


def direction_for(displacement: tuple[int, int, int]) -> int:
    matches = tuple(
        index
        for index, candidate in enumerate(c425.c210.DIRECTIONS)
        if np.array_equal(candidate, np.asarray(displacement))
    )
    if len(matches) != 1:
        raise ValueError("displacement is not one proper-cubic field direction")
    return matches[0]


def target_index(length: int, distance: int, displacement: tuple[int, int, int]) -> int:
    if distance not in (1, 2):
        raise ValueError("declared response distance is one or two edges")
    direction = direction_for(displacement)
    cell = tuple(int((distance * value) % length) for value in displacement)
    return c425.field_index(cell, direction, length)


def transient_field(
    length: int,
    distance: int,
    displacement: tuple[int, int, int],
    *,
    delete_source: bool = False,
) -> tuple[np.ndarray, object]:
    if length not in (TRAIN_LENGTH, HELD_LENGTH):
        raise ValueError("transient tournament uses periodic L=5 or held L=9")
    operator = c425.cubic_update(length, 1, delete_vertex=delete_source)
    field = c425.source_seed(length)[:, 0]
    for _ in range(distance):
        field = operator @ field
    return np.asarray(field), operator


@dataclass(frozen=True)
class Prediction:
    law: str
    length: int
    distance: int
    strength: int
    initial_position: int
    free_position: int
    event_position: int
    event_sector_weight: float
    dimensionless_fine_interval: int | None
    dimensionless_pair_interval: int | None
    dimensionless_quartet_interval: int | None
    wrapped: bool


def prediction(
    joint: np.ndarray,
    control: int,
    law: Law,
    length: int,
    distance: int,
    strength: int,
    initial_position: int,
) -> Prediction:
    weights = np.abs(joint[control]) ** 2
    occupied = float(np.sum(weights))
    event_position = int(np.argmax(weights)) if occupied > 1e-18 else -1
    raw_free = initial_position + BASE_SWEEPS
    raw_event = raw_free + law.response_sign * strength
    wrapped = not (0 <= raw_event < CLOCK_BITS)
    if occupied <= 1e-18 or wrapped or raw_event <= initial_position:
        fine = pair = quartet = None
    else:
        fine = raw_event - initial_position
        pair = (
            c428.partition_word(c428.one_hot(raw_event), 2).index(1)
            - c428.partition_word(c428.one_hot(initial_position), 2).index(1)
        )
        quartet = (
            c428.partition_word(c428.one_hot(raw_event), 4).index(1)
            - c428.partition_word(c428.one_hot(initial_position), 4).index(1)
        )
    return Prediction(
        law.name,
        length,
        distance,
        strength,
        initial_position,
        raw_free % CLOCK_BITS,
        event_position,
        occupied,
        fine,
        pair,
        quartet,
        wrapped,
    )


def run_transient_case(
    length: int,
    distance: int,
    strength: int,
    initial_position: int = 2,
    *,
    delete_source: bool = False,
    delete_coupling: bool = False,
    delete_clock: bool = False,
) -> tuple[dict[str, Prediction], dict[str, np.ndarray], dict[str, float]]:
    displacement = tuple(int(value) for value in c425.c210.DIRECTIONS[0])
    field, operator = transient_field(
        length, distance, displacement, delete_source=delete_source
    )
    control = target_index(length, distance, displacement)
    original = initial_joint(c425.source_seed(length)[:, 0], initial_position)
    before_response = initial_joint(field, initial_position)
    outputs = {}
    predictions = {}
    inverse_residuals = {}
    for law in LAWS:
        output = response_gate(
            before_response,
            control,
            law,
            strength,
            delete_coupling=delete_coupling,
            delete_clock=delete_clock,
        )
        outputs[law.name] = output
        predictions[law.name] = prediction(
            output, control, law, length, distance, strength, initial_position
        )
        restored = response_gate(
            output,
            control,
            law,
            strength,
            inverse=True,
            delete_coupling=delete_coupling,
            delete_clock=delete_clock,
        )
        for _ in range(distance):
            restored = apply_field(operator.getH(), restored)
        inverse_residuals[law.name] = float(np.linalg.norm(restored - original))
    return predictions, outputs, inverse_residuals


def transient_tournament_controls() -> dict[str, Prediction]:
    print("\nTRANSIENT COMMON-INPUT COMPETING-LAW TOURNAMENT")
    cases = (
        (TRAIN_LENGTH, 1, 1, "train"),
        (HELD_LENGTH, 1, 1, "held-size"),
        (HELD_LENGTH, 2, 1, "held-distance"),
        (HELD_LENGTH, 1, 2, "held-strength"),
        (HELD_LENGTH, 2, 2, "held-joint"),
    )
    rows = []
    failures = 0
    all_inverse_residuals = []
    field_q_ledger_residuals = []
    clock_hamming_ledger_residuals = []
    train_predictions: dict[str, Prediction] = {}
    for length, distance, strength, label in cases:
        predictions, outputs, inverses = run_transient_case(length, distance, strength)
        control_weight = predictions[DELAY.name].event_sector_weight
        expected = float(np.sin(c425.ANGLE) ** 2 / 6 ** (2 * distance - 1))
        # For distance two the common field coin gives one additional 1/3
        # amplitude, hence 1/9 in weight relative to the one-edge coordinate.
        if distance == 2:
            expected = float(np.sin(c425.ANGLE) ** 2 / 54)
        difference = float(np.linalg.norm(outputs[DELAY.name] - outputs[ADVANCE.name]))
        norm_rows = {
            law.name: float(np.vdot(outputs[law.name], outputs[law.name]).real)
            for law in LAWS
        }
        clock_hamming = {
            law.name: sum(
                float(np.linalg.norm(outputs[law.name][:, position]) ** 2)
                for position in range(CLOCK_BITS)
            )
            for law in LAWS
        }
        failures += int(abs(control_weight - expected) > 8e-14)
        failures += int(predictions[ADVANCE.name].event_sector_weight != control_weight)
        failures += int(predictions[DELAY.name].event_position == predictions[ADVANCE.name].event_position)
        failures += int(abs(difference - np.sqrt(2 * control_weight)) > 8e-14)
        failures += sum(int(value > 8e-13) for value in inverses.values())
        failures += sum(int(abs(value - 1) > 8e-13) for value in norm_rows.values())
        failures += sum(int(abs(value - 1) > 8e-13) for value in clock_hamming.values())
        all_inverse_residuals.extend(inverses.values())
        field_q_ledger_residuals.extend(abs(value - 1) for value in norm_rows.values())
        clock_hamming_ledger_residuals.extend(
            abs(value - 1) for value in clock_hamming.values()
        )
        rows.append(
            {
                "case": label,
                "predictions": tuple(asdict(predictions[law.name]) for law in LAWS),
                "law_state_residual": difference,
                "expected_sqrt_2w": float(np.sqrt(2 * control_weight)),
                "inverse_residuals": inverses,
                "field_Q_ledgers": norm_rows,
                "clock_Hamming_ledgers": clock_hamming,
            }
        )
        if label == "train":
            train_predictions = predictions

    deleted_source, source_outputs, _ = run_transient_case(
        HELD_LENGTH, 1, 1, delete_source=True
    )
    deleted_coupling, coupling_outputs, _ = run_transient_case(
        HELD_LENGTH, 1, 1, delete_coupling=True
    )
    deleted_clock, clock_outputs, _ = run_transient_case(
        HELD_LENGTH, 1, 1, delete_clock=True
    )
    deletion_rows = {
        "source": float(
            np.linalg.norm(source_outputs[DELAY.name] - source_outputs[ADVANCE.name])
        ),
        "coupling": float(
            np.linalg.norm(coupling_outputs[DELAY.name] - coupling_outputs[ADVANCE.name])
        ),
        "clock": float(
            np.linalg.norm(clock_outputs[DELAY.name] - clock_outputs[ADVANCE.name])
        ),
    }
    failures += int(deleted_source[DELAY.name].event_sector_weight != 0)
    failures += sum(int(value != 0) for value in deletion_rows.values())

    displacement = tuple(int(value) for value in c425.c210.DIRECTIONS[0])
    field1, _ = transient_field(TRAIN_LENGTH, 1, displacement)
    field2, _ = transient_field(TRAIN_LENGTH, 2, displacement)
    base_one = abs(field1[target_index(TRAIN_LENGTH, 1, displacement)]) ** 2
    base_two = abs(field2[target_index(TRAIN_LENGTH, 2, displacement)]) ** 2
    frame_residuals = []
    for frame in c428.c255.proper_frames():
        moved = tuple(int(value) for value in frame @ np.asarray(displacement))
        frame_residuals.extend(
            (
                abs(abs(field1[target_index(TRAIN_LENGTH, 1, moved)]) ** 2 - base_one),
                abs(abs(field2[target_index(TRAIN_LENGTH, 2, moved)]) ** 2 - base_two),
            )
        )
    check(
        "the delay and advance laws make distinct exact transient clock-word predictions on train and held inputs",
        failures == 0 and max(frame_residuals) < 8e-14,
        {
            "same_source_field_clock_input_per_case": True,
            "neither_law_selected": True,
            "rows": rows,
            "deletion_law_state_residuals": deletion_rows,
            "proper_cubic_frames": len(c428.c255.proper_frames()),
            "maximum_frame_occupation_residual": max(frame_residuals),
            "maximum_common_update_inverse_residual": max(all_inverse_residuals),
            "maximum_field_Q_ledger_residual": max(field_q_ledger_residuals),
            "maximum_clock_Hamming_ledger_residual": max(clock_hamming_ledger_residuals),
            "gate_controlled_by_expectation": False,
        },
    )
    return train_predictions


def stationary_profile_controls() -> None:
    print("\nSTATIONARY DRESSED COMMON-INPUT CONTROL")
    displacement = tuple(int(value) for value in c425.c210.DIRECTIONS[0])
    rows = []
    failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        update, eigenvalue, shore_state = c425.shore.dressed_eigenstate(length)
        state = np.asarray(c425.shore_embedding(length) @ shore_state)
        evolved = np.asarray(c425.cubic_update(length, 1) @ state)
        control = target_index(length, 1, displacement)
        occupation = float(abs(state[control]) ** 2)
        evolved_occupation = float(abs(evolved[control]) ** 2)
        before = initial_joint(evolved, 7)
        outputs = {
            law.name: response_gate(before, control, law, 1)
            for law in LAWS
        }
        predictions = {
            law.name: prediction(outputs[law.name], control, law, length, 1, 1, 7)
            for law in LAWS
        }
        inverse = {
            law.name: float(
                np.linalg.norm(
                    response_gate(outputs[law.name], control, law, 1, inverse=True)
                    - before
                )
            )
            for law in LAWS
        }
        difference = float(np.linalg.norm(outputs[DELAY.name] - outputs[ADVANCE.name]))
        failures += int(abs(occupation - evolved_occupation) > 4e-12)
        failures += int(predictions[DELAY.name].event_position != 9)
        failures += int(predictions[ADVANCE.name].event_position != 11)
        failures += int(abs(difference - np.sqrt(2 * occupation)) > 4e-12)
        failures += sum(int(value != 0) for value in inverse.values())
        rows.append(
            {
                "L": length,
                "held": length == HELD_LENGTH,
                "local_stationary_field_occupation": occupation,
                "post_update_local_occupation": evolved_occupation,
                "stationary_component_residual": abs(occupation - evolved_occupation),
                "delay_latched_word_position": predictions[DELAY.name].event_position,
                "advance_latched_word_position": predictions[ADVANCE.name].event_position,
                "law_state_residual": difference,
                "response_inverse_residuals": inverse,
                "eigenstate_preparation_supplied": True,
                "eigenphase_called_time_or_rate": False,
                "eigenvalue_modulus": float(abs(eigenvalue)),
                "returned_update_shape": update.shape,
            }
        )
    check(
        "the same two laws remain distinct on supplied stationary dressed inputs at training and held size",
        failures == 0,
        {"rows": rows, "neither_stationary_law_selected": True},
    )


def event_record_boundary_controls(train: dict[str, Prediction]) -> None:
    print("\nCYCLE-428 EVENT LATCH / CONDITIONAL RECORD BOUNDARY")
    fixture = c428.c364.c342.c338.build_fixture(3)
    payload = c428.c364.words(fixture, 1)[0]
    answers = {}
    latches = {}
    inverse_failures = 0
    for law in LAWS:
        event_position = train[law.name].event_position
        initial = c428.blank_latch(1, c428.one_hot(event_position), c428.bits(1, c428.EVENT_BITS))
        latch = c428.apply_latch(initial)
        inverse_failures += int(c428.invert_latch(latch) != initial)
        latches[law.name] = latch
        answers[law.name] = c428.c364.apply_candidate_law(
            fixture,
            c428.c364.FormationState(),
            c428.c364.proposal((0, 0, 0), payload, close=latch.valid),
        )
    false_latch = c428.apply_latch(
        c428.blank_latch(0, c428.one_hot(5), c428.bits(1, c428.EVENT_BITS))
    )
    false_answer = c428.c364.apply_candidate_law(
        fixture,
        c428.c364.FormationState(),
        c428.c364.proposal((0, 0, 0), payload, close=false_latch.valid),
    )
    delay_word = latches[DELAY.name].latched_clock
    advance_word = latches[ADVANCE.name].latched_clock
    check(
        "the common event sector latches different complete words before two unselected conditional Record attempts",
        inverse_failures == 0
        and c428.decoded_latch(latches[DELAY.name]) == (4, 1)
        and c428.decoded_latch(latches[ADVANCE.name]) == (6, 1)
        and delay_word != advance_word
        and answers[DELAY.name].status == answers[ADVANCE.name].status == "formed"
        and false_answer.formed is None
        and false_answer.state == c428.c364.FormationState(),
        {
            "delay_latched_clock_word": delay_word,
            "advance_latched_clock_word": advance_word,
            "shared_event_identity": 1,
            "shared_Record_payload": True,
            "conditional_statuses": tuple(answers[law.name].status for law in LAWS),
            "candidate_formation_law_selected": False,
            "reversible_latch_is_Record": False,
            "event_sector_occurrence_asserted": False,
            "false_event_status": false_answer.status,
        },
    )


def alias_wrap_domain_controls() -> None:
    print("\nALIAS, WRAP, DELETION, AND LAWFUL-DOMAIN CONTROLS")
    alias_a = basis_response(1, c428.one_hot(1), ADVANCE, 1)
    alias_b = basis_response(1, c428.one_hot(3), ADVANCE, 1)
    wrap_input = initial_joint(np.asarray((1.0 + 0j,)), 13)
    wrap_output = response_gate(wrap_input, 0, ADVANCE, 2)
    wrapped = prediction(wrap_output, 0, ADVANCE, 1, 1, 2, 13)
    deleted_swap = c428.clock_position(
        baseline(c428.one_hot(6), deleted_swap=7)
    )
    rejections = 0
    for probe in (
        lambda: controlled_response(
            RailState(1, (0,) * CONTROL_RAIL_BITS, c428.one_hot(0)),
            Law("bad", 0),
            1,
        ),
        lambda: controlled_response(
            RailState(1, (0,) * CONTROL_RAIL_BITS, c428.one_hot(0)), DELAY, 3
        ),
        lambda: response_gate(np.zeros((2, 15)), 0, DELAY, 1),
        lambda: target_index(5, 3, tuple(int(value) for value in c425.c210.DIRECTIONS[0])),
        lambda: validate_rail_state(
            RailState(1, (1,) + (0,) * (CONTROL_RAIL_BITS - 1), (0,) * CLOCK_BITS)
        ),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    check(
        "the complete word exposes parity aliases, wrap, clock deletion, and malformed domains without false intervals",
        (c428.clock_position(alias_a) & 1) == (c428.clock_position(alias_b) & 1)
        and alias_a != alias_b
        and wrapped.wrapped
        and wrapped.dimensionless_fine_interval is None
        and wrapped.event_position == 2
        and deleted_swap != 9
        and rejections == 5,
        {
            "offset_two_input_positions": (1, 3),
            "output_complete_words_equal": alias_a == alias_b,
            "wrapped_advance_strength2": asdict(wrapped),
            "baseline_deleted_swap_position": deleted_swap,
            "lawful_domain_rejections": rejections,
        },
    )


def receiver_typing_and_inventory_controls(train: dict[str, Prediction]) -> None:
    print("\nCYCLE-416/420 MATCHING COORDINATES AND CLAIM BOUNDARY")
    cycle416_angle = c425.c422.c418.c416.source_angle()[0]
    total_field_coordinate = float(np.sin(c425.ANGLE) ** 2)
    local_field_coordinate = total_field_coordinate / 6
    typing = {
        "Cycle416_matching_coordinate": "one physical scalar occupation transferred at the common angle",
        "Cycle420_matching_coordinate": "positive hard-core field occupation",
        "Cycle420_signed_density_coordinate_used": False,
        "Cycle420_signed_phase_history_used": False,
        "physical_recurrent_clock_candidate": True,
        "actual_Record_selected": False,
        "metric_reconstructed": False,
        "lapse_derived": False,
        "proper_time_derived": False,
        "Lorentz_structure_derived": False,
    }
    inventory = {
        "supplied": (
            "Cycle425/Cycle426 positive hard-core field meaning and prepared source seed",
            "local field site, oscillator coupling, three-sweep baseline, and invocation",
            "initial clock phase, response sign and integer strength",
            "clock-word interpretation, unit, calibration, and nonwrap epoch",
            "stationary eigenstate preparation",
            "event identity, blank sidecar, Record payload binding, and Cycle364 formation applicability",
            "empirical law selection and occurrence",
        ),
        "derived": (
            "two exact inverse occupation-controlled clock permutations",
            "field-Q, clock-Hamming, and blank-rail ledgers",
            "distinct transient and stationary complete-word predictions",
            "dimensionless fine/pair/quartet word displacements on the lawful domain",
            "held size, distance, strength, deletion, alias, wrap, and frame controls",
        ),
        "selected": (),
        "negative_claim": False,
        "axiom_pressure": False,
    }
    check(
        "only matching Cycle-416/420 scalar-occupation coordinates are compared and every metric/selection flag stays false",
        abs(cycle416_angle - c425.ANGLE) < 2e-16
        and abs(total_field_coordinate - 0.12589921612871371) < 2e-15
        and abs(local_field_coordinate - train[DELAY.name].event_sector_weight) < 8e-14
        and train[DELAY.name].dimensionless_fine_interval == 2
        and train[ADVANCE.name].dimensionless_fine_interval == 4
        and not any(
            typing[key]
            for key in (
                "actual_Record_selected",
                "metric_reconstructed",
                "lapse_derived",
                "proper_time_derived",
                "Lorentz_structure_derived",
            )
        )
        and not inventory["selected"]
        and not inventory["negative_claim"]
        and not inventory["axiom_pressure"],
        {
            "Cycle416_angle": cycle416_angle,
            "Cycle425_angle": c425.ANGLE,
            "Cycle420_total_positive_field_coordinate": total_field_coordinate,
            "one_edge_local_positive_occupation": local_field_coordinate,
            "delay_dimensionless_interval": train[DELAY.name].dimensionless_fine_interval,
            "advance_dimensionless_interval": train[ADVANCE.name].dimensionless_fine_interval,
            "typing": typing,
            "inventory": inventory,
            "field_occupation_called_energy_source_or_stress": False,
            "update_count_or_eigenphase_called_time_or_rate": False,
            "Born_or_occurrence_claim": False,
        },
    )


def main() -> int:
    contracts()
    physical_circuit_controls()
    common_code_eg_controls()
    train = transient_tournament_controls()
    stationary_profile_controls()
    event_record_boundary_controls(train)
    alias_wrap_domain_controls()
    receiver_typing_and_inventory_controls(train)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
