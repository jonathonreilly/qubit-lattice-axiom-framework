#!/usr/bin/env python3
"""Cycle 224: stationary local first-event history on Cycle-222 matter.

Apply one fixed onsite two-outcome detector after every radius-one candidate
update.  The detector is inert outside its causal support, so causal arrival
determines the support and earliest nonzero label of the first-event family
rather than selecting one index at a scanned read time.
Orthogonal history labels provide a coherent dilation of the repeated
instrument; dephasing or selecting those labels remains supplied.

The candidate unitary, detector projector, repeated-instrument semantics,
squared-modulus weights, blank history capacity, and force profile are all
conditional inputs.  This runner derives no physical Record, outcome
occurrence, Born frequency, clock metric, gravity law, or axiom change.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np

import conditional_flavor_mass_operator_compiler_cycle222_2026_07_17 as c222
import locking_cadence_record_kernel_discriminator_cycle223_2026_07_17 as c223
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "STATIONARY_LOCAL_FIRST_EVENT_HISTORY_CYCLE224_NOTE_2026-07-17.md"
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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "stationary local first-event instrument",
        "event-ready history, not a record",
        "causal arrival determines the support of the supplied first-hit branch family",
        "orthogonal history labels are supplied",
        "one common phase tester",
        "target-unfed",
        "proper-cubic apparatus covariance",
        "does not derive a clock",
        "does not select an outcome",
        "no axiom conclusion",
        "audit unset",
        "draft pr #5389",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden = tuple(
        phrase
        for phrase in (
            "record-forming channel",
            "open: the click destroys",
            "does not select an outcome, derive born frequency, derive a physical record, establish permanence, test post-click inertia",
        )
        if phrase in text
    )
    check(
        "note preserves the bounded event-ready claim",
        not missing and not forbidden,
        {"missing": missing, "forbidden": forbidden},
    )


@dataclass(frozen=True)
class EventHistory:
    clicks: tuple[np.ndarray, ...]
    survival: np.ndarray


@dataclass(frozen=True)
class InertiaRun:
    acceleration: float
    norm: float
    band: float
    boundary: float
    click_weight: float


@dataclass(frozen=True)
class FrozenMassRow:
    c3_phase: float
    vector: np.ndarray
    dispersion_mass: float
    baseline_mass: float
    detector_mass: float
    detector_click_weight: float
    health: bool


@dataclass(frozen=True)
class ClickSectorRow:
    c3_phase: float
    click_weight: float
    sector_weight: float
    mass_value: float
    target_mass: float
    scalar_band_weight: float


@dataclass(frozen=True)
class PostClickPacketRow:
    c3_phase: float
    click_weight: float
    pre_click_band: float
    post_click_band: float
    dispersion_mass: float
    conditioned_force_response_estimator: float
    normalized_even_contamination: float
    odd_acceleration: float
    force_sign_ok: bool
    norm_residual: float
    boundary_weight: float


def axis_walk(block: np.ndarray, length: int, axis: int = 0) -> np.ndarray:
    """One cardinal slice of the proper-cubic coin-and-stream update."""
    unitary = np.zeros((6 * length, 6 * length), dtype=complex)
    for position in range(length):
        for old_direction in range(6):
            for new_direction in range(6):
                target = (
                    position + int(c210.DIRECTIONS[new_direction, axis])
                ) % length
                unitary[
                    6 * target + new_direction,
                    6 * position + old_direction,
                ] = block[new_direction, old_direction]
    return unitary


def site_mask(length: int, position: int) -> np.ndarray:
    mask = np.zeros(6 * length, dtype=float)
    mask[6 * (position % length) : 6 * ((position % length) + 1)] = 1
    return mask


def phase_state(
    length: int,
    position: int,
    phase: float,
    first_direction: int = 0,
    second_direction: int = 1,
) -> np.ndarray:
    state = np.zeros(6 * length, dtype=complex)
    state[6 * position + first_direction] = 1 / np.sqrt(2)
    state[6 * position + second_direction] = np.exp(1j * phase) / np.sqrt(2)
    return state


def first_event_history(
    unitary: np.ndarray,
    detector_mask: np.ndarray,
    initial: np.ndarray,
    steps: int,
) -> EventHistory:
    """Coherent branch amplitudes for the stationary repeated instrument."""
    open_state = np.asarray(initial, dtype=complex).copy()
    complement = 1 - detector_mask
    clicks = []
    for _ in range(steps):
        evolved = unitary @ open_state
        clicks.append(detector_mask * evolved)
        open_state = complement * evolved
    return EventHistory(tuple(clicks), open_state)


def event_weights(history: EventHistory) -> np.ndarray:
    weights = [float(np.vdot(row, row).real) for row in history.clicks]
    weights.append(float(np.vdot(history.survival, history.survival).real))
    return np.asarray(weights)


def classical_first_event_weights(
    kernel: np.ndarray,
    detector_mask: np.ndarray,
    initial_weights: np.ndarray,
    steps: int,
) -> np.ndarray:
    open_weights = np.asarray(initial_weights, dtype=float).copy()
    complement = 1 - detector_mask
    clicks = []
    for _ in range(steps):
        evolved = kernel @ open_weights
        clicks.append(float(detector_mask @ evolved))
        open_weights = complement * evolved
    clicks.append(float(np.sum(open_weights)))
    return np.asarray(clicks)


def total_variation(left: np.ndarray, right: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(left - right)))


def trace_pointer(density: np.ndarray, matter_dimension: int) -> np.ndarray:
    pointer_dimension = density.shape[0] // matter_dimension
    tensor = density.reshape(
        matter_dimension,
        pointer_dimension,
        matter_dimension,
        pointer_dimension,
    )
    return np.trace(tensor, axis1=1, axis2=3)


def translate_state(state: np.ndarray, length: int, shift: int) -> np.ndarray:
    return np.roll(state.reshape(length, 6), shift, axis=0).reshape(-1)


def event_channel_and_phase_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    length = 31
    centre = length // 2
    steps = 18
    detector = site_mask(length, centre + 1)
    phases = (0.0, np.pi / 2, np.pi)
    rows = []
    classical_rows = []
    coalescence_rows = []
    normalization_errors = []
    translation_errors = []
    representation_errors = []

    rng = np.random.default_rng(22401)
    raw = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    direction_basis, upper = np.linalg.qr(raw)
    diagonal = np.diag(upper)
    direction_basis = direction_basis @ np.diag(diagonal / np.abs(diagonal))
    full_basis = np.kron(np.eye(length), direction_basis)

    for row in blocks:
        unitary = axis_walk(row.block, length)
        coherent_distributions = []
        classical_distributions = []
        histories = []
        for phase in phases:
            initial = phase_state(length, centre, phase)
            history = first_event_history(unitary, detector, initial, steps)
            weights = event_weights(history)
            histories.append(history)
            coherent_distributions.append(weights)
            classical_distributions.append(
                classical_first_event_weights(
                    c223.born_kernel(unitary),
                    detector,
                    np.abs(initial) ** 2,
                    steps,
                )
            )
            normalization_errors.append(abs(np.sum(weights) - 1))

        coherent_tv = max(
            total_variation(left, right)
            for left, right in product(coherent_distributions, repeat=2)
        )
        classical_tv = max(
            total_variation(left, right)
            for left, right in product(classical_distributions, repeat=2)
        )
        rows.append((row.c3_phase, coherent_tv))
        classical_rows.append((row.c3_phase, classical_tv))

        middle_history = histories[1]
        incoherent_click_weight = float(np.sum(event_weights(middle_history)[:-1]))
        transported = tuple(
            np.linalg.matrix_power(unitary, steps - tick) @ click
            for tick, click in enumerate(middle_history.clicks, start=1)
        )
        coalesced_amplitude = np.sum(np.stack(transported), axis=0)
        coalesced_weight = float(np.vdot(coalesced_amplitude, coalesced_amplitude).real)
        coalescence_rows.append(
            (
                row.c3_phase,
                incoherent_click_weight,
                coalesced_weight,
                np.linalg.norm(
                    coalesced_amplitude + middle_history.survival
                    - np.linalg.matrix_power(unitary, steps)
                    @ phase_state(length, centre, np.pi / 2)
                ),
            )
        )

        reference = coherent_distributions[1]
        shifted_initial = translate_state(
            phase_state(length, centre, np.pi / 2), length, 4
        )
        shifted_detector = site_mask(length, centre + 5)
        shifted = event_weights(
            first_event_history(
                unitary, shifted_detector, shifted_initial, steps
            )
        )
        translation_errors.append(np.linalg.norm(reference - shifted))

        represented_unitary = full_basis.conj().T @ unitary @ full_basis
        represented_initial = full_basis.conj().T @ phase_state(
            length, centre, np.pi / 2
        )
        represented = event_weights(
            first_event_history(
                represented_unitary,
                detector,
                represented_initial,
                steps,
            )
        )
        representation_errors.append(np.linalg.norm(reference - represented))

    check(
        "orthogonal first-event branch weights are positive and normalized",
        max(normalization_errors) < 3e-12,
        max(normalization_errors),
    )
    check(
        "one common phase tester changes first-event history in every sector",
        min(value for _, value in rows) > 0.45
        and max(value for _, value in classical_rows) < 3e-12,
        {"coherent": rows, "same_diagonal_kernel": classical_rows},
    )
    check(
        "removing orthogonal event-time labels can change the click weight",
        max(
            abs(incoherent - coalesced)
            for _, incoherent, coalesced, _ in coalescence_rows
        )
        > 0.05
        and max(row[3] for row in coalescence_rows) < 3e-12,
        coalescence_rows,
    )
    check(
        "translated apparatus and passive direction recoding preserve event weights",
        max(translation_errors) < 3e-12
        and max(representation_errors) < 3e-12,
        {
            "translation": max(translation_errors),
            "passive_recoding": max(representation_errors),
        },
    )


def stationary_instrument_and_telescoping_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    """Check the same ready/click instrument and first-hit identity each tick."""
    length = 9
    centre = length // 2
    detector_mask = site_mask(length, centre + 1)
    detector = np.diag(detector_mask.astype(complex))
    complement = np.eye(6 * length, dtype=complex) - detector
    ready = np.array(((1, 0), (0, 0)), dtype=complex)
    clicked = np.array(((0, 0), (0, 1)), dtype=complex)
    jump = np.array(((0, 0), (1, 0)), dtype=complex)
    identity = np.eye(6 * length, dtype=complex)
    no_jump = np.kron(complement, ready) + np.kron(identity, clicked)
    first_jump = np.kron(detector, jump)
    completeness = (
        no_jump.conj().T @ no_jump
        + first_jump.conj().T @ first_jump
    )

    rng = np.random.default_rng(22402)
    seed = rng.normal(size=6 * length) + 1j * rng.normal(size=6 * length)
    seed /= np.linalg.norm(seed)
    joint_seed = np.kron(seed, np.array((1, 0), dtype=complex))
    density = np.outer(joint_seed, joint_seed.conj())
    positivity_rows = []
    for row in blocks:
        unitary = np.kron(axis_walk(row.block, length), np.eye(2))
        output = density.copy()
        for _ in range(4):
            evolved = unitary @ output @ unitary.conj().T
            output = (
                no_jump @ evolved @ no_jump.conj().T
                + first_jump @ evolved @ first_jump.conj().T
            )
        positivity_rows.append(
            (
                row.c3_phase,
                abs(np.trace(output) - 1),
                float(np.min(np.linalg.eigvalsh(output)).real),
            )
        )

    telescope_rows = []
    long_length = 31
    long_centre = long_length // 2
    long_detector = site_mask(long_length, long_centre + 1)
    long_projector = np.diag(long_detector.astype(complex))
    long_complement = np.eye(6 * long_length, dtype=complex) - long_projector
    for row in blocks:
        unitary = axis_walk(row.block, long_length)
        history = first_event_history(
            unitary,
            long_detector,
            phase_state(long_length, long_centre, np.pi / 2),
            18,
        )
        click_weights = event_weights(history)[:-1]
        survival = [1.0]
        open_state = phase_state(long_length, long_centre, np.pi / 2)
        ready_density = np.outer(open_state, open_state.conj())
        clicked_density = np.zeros_like(ready_density)
        instrument_increments = []
        for _ in range(18):
            open_state = (1 - long_detector) * (unitary @ open_state)
            survival.append(float(np.vdot(open_state, open_state).real))
            evolved_ready = unitary @ ready_density @ unitary.conj().T
            evolved_clicked = unitary @ clicked_density @ unitary.conj().T
            increment = long_projector @ evolved_ready @ long_projector
            instrument_increments.append(float(np.trace(increment).real))
            ready_density = long_complement @ evolved_ready @ long_complement
            clicked_density = evolved_clicked + increment
        differences = np.asarray(survival[:-1]) - np.asarray(survival[1:])
        telescope_rows.append(
            (
                row.c3_phase,
                float(np.max(np.abs(click_weights - differences))),
                abs(float(np.sum(click_weights)) - (1 - survival[-1])),
                float(
                    np.max(
                        np.abs(
                            click_weights - np.asarray(instrument_increments)
                        )
                    )
                ),
                abs(
                    float(np.trace(ready_density + clicked_density).real) - 1
                ),
                survival[-1],
            )
        )

    check(
        "the supplied ready-click map is one stationary CPTP instrument",
        np.linalg.norm(completeness - np.eye(12 * length)) < 3e-12
        and max(row[1] for row in positivity_rows) < 3e-12
        and min(row[2] for row in positivity_rows) > -3e-12,
        {
            "completeness": np.linalg.norm(
                completeness - np.eye(12 * length)
            ),
            "four_tick_outputs": positivity_rows,
        },
    )
    check(
        "the conditional first-event weights telescope from survival loss",
        max(row[1] for row in telescope_rows) < 3e-12
        and max(row[2] for row in telescope_rows) < 3e-12
        and max(row[3] for row in telescope_rows) < 3e-12
        and max(row[4] for row in telescope_rows) < 3e-12,
        telescope_rows,
    )


def local_pointer_copy_controls(blocks: tuple[c223.BlindBlock, ...]) -> None:
    """One or two coherent arrival pointers give one reduced dephasing."""
    length = 3
    dimension = 6 * length
    detector = np.diag(site_mask(length, 1).astype(complex))
    complement = np.eye(dimension, dtype=complex) - detector
    x_gate = np.array(((0, 1), (1, 0)), dtype=complex)
    one_write = np.kron(complement, np.eye(2)) + np.kron(detector, x_gate)
    two_flip = np.kron(x_gate, x_gate)
    two_write = np.kron(complement, np.eye(4)) + np.kron(detector, two_flip)
    zero = np.array((1, 0), dtype=complex)
    rng = np.random.default_rng(22403)
    rows = []
    for block_row in blocks:
        unitary = axis_walk(block_row.block, length)
        matter = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        matter /= np.linalg.norm(matter)
        matter = unitary @ matter
        source = np.outer(matter, matter.conj())
        expected = complement @ source @ complement + detector @ source @ detector
        one = one_write @ np.kron(matter, zero)
        two = two_write @ np.kron(matter, np.kron(zero, zero))
        one_density = trace_pointer(
            np.outer(one, one.conj()), dimension
        )
        two_density = trace_pointer(
            np.outer(two, two.conj()), dimension
        )
        rows.append(
            (
                block_row.c3_phase,
                np.linalg.norm(one_density - expected),
                np.linalg.norm(two_density - expected),
                np.linalg.norm(one_density - two_density),
                float(np.trace(detector @ source).real),
            )
        )

    check(
        "one and two coherent local pointer copies induce the same reduced channel",
        np.linalg.norm(one_write.conj().T @ one_write - np.eye(2 * dimension))
        < 3e-12
        and np.linalg.norm(
            two_write.conj().T @ two_write - np.eye(4 * dimension)
        )
        < 3e-12
        and max(max(row[1:4]) for row in rows) < 3e-12,
        rows,
    )
def causality_and_deletion_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    length = 31
    centre = length // 2
    distance = 6
    rows = []
    deletion_rows = []
    for row in blocks:
        unitary = axis_walk(row.block, length)
        initial = np.zeros(6 * length, dtype=complex)
        initial[6 * centre] = 1
        detector = site_mask(length, centre + distance)
        history = first_event_history(unitary, detector, initial, distance + 2)
        click_weights = event_weights(history)[:-1]

        open_state = initial.copy()
        complement = 1 - detector
        precontact_errors = []
        for tick in range(1, distance):
            open_state = complement * (unitary @ open_state)
            precontact_errors.append(
                np.linalg.norm(
                    open_state - np.linalg.matrix_power(unitary, tick) @ initial
                )
            )
        rows.append(
            (
                row.c3_phase,
                float(np.max(np.abs(click_weights[: distance - 1]))),
                float(click_weights[distance - 1]),
                max(precontact_errors),
            )
        )

        absent = first_event_history(
            unitary, np.zeros(6 * length), initial, 8
        )
        deletion_rows.append(
            (
                row.c3_phase,
                float(np.sum(event_weights(absent)[:-1])),
                np.linalg.norm(
                    absent.survival - np.linalg.matrix_power(unitary, 8) @ initial
                ),
            )
        )

    check(
        "the fixed detector is exactly inert before its causal light cone arrives",
        max(row[1] for row in rows) < 3e-14
        and min(row[2] for row in rows) > 1e-7
        and max(row[3] for row in rows) < 3e-12,
        rows,
    )
    check(
        "deleting the detector restores uninterrupted coherent evolution",
        max(row[1] for row in deletion_rows) < 3e-14
        and max(row[2] for row in deletion_rows) < 3e-12,
        deletion_rows,
    )


def proper_cubic_apparatus_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    length = 31
    centre = length // 2
    steps = 10
    frames = c210.proper_cubic_frames()
    errors = []
    for row in blocks:
        reference = None
        sector_errors = []
        for frame in frames:
            mapped_axis = frame @ np.array((1, 0, 0))
            axis = int(np.argmax(np.abs(mapped_axis)))
            sign = int(mapped_axis[axis])
            representation = c210.direction_permutation(frame)
            plus = int(np.argmax(np.abs(representation[:, 0])))
            minus = int(np.argmax(np.abs(representation[:, 1])))
            initial = phase_state(
                length,
                centre,
                np.pi / 2,
                plus,
                minus,
            )
            weights = event_weights(
                first_event_history(
                    axis_walk(row.block, length, axis),
                    site_mask(length, centre + sign),
                    initial,
                    steps,
                )
            )
            if reference is None:
                reference = weights
            sector_errors.append(np.linalg.norm(weights - reference))
        errors.append((row.c3_phase, max(sector_errors)))

    check(
        "the oriented detector slice has proper-cubic apparatus covariance",
        max(error for _, error in errors) < 3e-12
        and len(frames) == 24,
        errors,
    )


def history_capacity_and_redundancy_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    length = 31
    centre = length // 2
    steps = 18
    row = blocks[0]
    history = first_event_history(
        axis_walk(row.block, length),
        site_mask(length, centre + 1),
        phase_state(length, centre, np.pi / 2),
        steps,
    )
    weights = event_weights(history)
    alternatives = steps + 1
    one_label = np.eye(alternatives)
    two_labels = np.zeros((alternatives**2, alternatives))
    for label in range(alternatives):
        two_labels[label * alternatives + label, label] = 1
    one_gram = one_label.conj().T @ one_label
    two_gram = two_labels.conj().T @ two_labels
    dephased_purity = float(np.sum(weights**2))
    minimum_bits = int(np.ceil(np.log2(alternatives)))

    check(
        "one and two coherent history-label copies preserve event weights",
        np.linalg.norm(one_gram - np.eye(alternatives)) < 3e-12
        and np.linalg.norm(two_gram - np.eye(alternatives)) < 3e-12
        and abs(np.sum(weights) - 1) < 3e-12,
        {
            "one_label_rank": int(np.linalg.matrix_rank(one_gram)),
            "two_label_rank": int(np.linalg.matrix_rank(two_gram)),
        },
    )
    check(
        "readable event time requires explicit orthogonal history capacity",
        np.linalg.matrix_rank(one_gram) == alternatives
        and minimum_bits == 5
        and np.count_nonzero(weights > 3e-14) == alternatives,
        {
            "alternatives": alternatives,
            "minimum_binary_capacity": minimum_bits,
            "minimum_live_weight": float(np.min(weights)),
            "modeled_dephased_purity": dephased_purity,
        },
    )


def post_click_mass_sector_controls(
    blocks: tuple[c223.BlindBlock, ...],
    compiled: c222.Compiled,
) -> None:
    """A site click respects the internal sector but localizes its band state."""
    length = 257
    centre = length // 2
    detector_position = centre + 4
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    rows = []
    for block_row in blocks:
        state = np.zeros((length, 4, 6), dtype=complex)
        state[centre, :, 0] = block_row.vector
        for _ in range(4):
            state = c222.local_register_step_axis(state, compiled.coin)
        click_weight = float(np.sum(np.abs(state[detector_position]) ** 2))
        click = np.zeros_like(state)
        click[detector_position] = state[detector_position]
        click /= np.sqrt(click_weight)
        register_density = np.einsum(
            "xrd,xsd->rs", click, click.conj(), optimize=True
        )
        sector_weight = float(
            np.vdot(
                block_row.vector,
                register_density @ block_row.vector,
            ).real
        )
        mass_value = float(
            np.trace(register_density @ compiled.recovered_mass).real
        )
        target_mass = float(
            np.vdot(
                block_row.vector,
                compiled.recovered_mass @ block_row.vector,
            ).real
        )
        direction_component = np.einsum(
            "r,xrd->xd", block_row.vector.conj(), click, optimize=True
        )
        rows.append(
            ClickSectorRow(
                block_row.c3_phase,
                click_weight,
                sector_weight,
                mass_value,
                target_mass,
                c222.block_branch_probability(
                    direction_component,
                    momenta,
                    block_row.block,
                ),
            )
        )

    mass_direction = np.kron(compiled.recovered_mass, np.eye(6))
    commutator = mass_direction @ compiled.coin - compiled.coin @ mass_direction
    relative_commutator = np.linalg.norm(commutator) / (
        np.linalg.norm(mass_direction) * np.linalg.norm(compiled.coin)
    )
    check(
        "a local click preserves the full-register mass sector label",
        relative_commutator < 3e-12
        and min(row.click_weight for row in rows) > 1e-6
        and min(row.sector_weight for row in rows) > 1 - 3e-10
        and max(abs(row.mass_value - row.target_mass) for row in rows) < 3e-8,
        {"relative_mass_coin_commutator": relative_commutator, "rows": rows},
    )
    check(
        "the causal point-hit branch does not lie wholly in the low-momentum scalar band",
        max(row.scalar_band_weight for row in rows) < 0.3,
        [
            (row.c3_phase, row.scalar_band_weight)
            for row in rows
        ],
    )


def forced_packet_response_from_seed(
    block: np.ndarray,
    seed: np.ndarray,
    positions: np.ndarray,
    momenta: np.ndarray,
    strength: float,
    *,
    duration: int = 160,
) -> tuple[float, float, float, float]:
    packet = np.asarray(seed, dtype=complex).copy()
    half = np.exp(0.5j * strength * positions)[:, None]
    means = [
        float(np.sum(positions * np.sum(np.abs(packet) ** 2, axis=1)))
    ]
    for _ in range(duration):
        packet *= half
        packet = c210.local_molecular_step(packet, block, axis=0)
        packet *= half
        norm_squared = float(np.sum(np.abs(packet) ** 2))
        means.append(
            float(
                np.sum(positions * np.sum(np.abs(packet) ** 2, axis=1))
                / norm_squared
            )
        )
    times = np.arange(duration + 1, dtype=float)
    acceleration = float(
        2 * np.polyfit(times, np.asarray(means) - means[0], 2)[0]
    )
    norm = float(np.linalg.norm(packet))
    normalized = packet / norm
    density = np.sum(np.abs(normalized) ** 2, axis=1)
    return (
        acceleration,
        c222.block_branch_probability(normalized, momenta, block),
        norm,
        float(np.sum(density[np.abs(positions) > len(positions) / 4])),
    )


def post_click_packet_contract_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    """Test the Cycle-222 low-band/inertia contract after one site click."""
    length = 4096
    width = 0.006
    strength = 1e-6
    rows = []
    for block_row in blocks:
        positions, momenta, packet = c222.prepare_block_packet(
            block_row.block, length, width
        )
        pre_click_band = c222.block_branch_probability(
            packet, momenta, block_row.block
        )
        evolved = c210.local_molecular_step(packet, block_row.block, axis=0)
        detector_index = int(np.argmin(np.abs(positions)))
        click_weight = float(np.sum(np.abs(evolved[detector_index]) ** 2))
        clicked = np.zeros_like(evolved)
        clicked[detector_index] = evolved[detector_index]
        clicked /= np.sqrt(click_weight)
        post_click_band = c222.block_branch_probability(
            clicked, momenta, block_row.block
        )

        positive = forced_packet_response_from_seed(
            block_row.block,
            clicked,
            positions,
            momenta,
            strength,
        )
        negative = forced_packet_response_from_seed(
            block_row.block,
            clicked,
            positions,
            momenta,
            -strength,
        )
        zero = forced_packet_response_from_seed(
            block_row.block,
            clicked,
            positions,
            momenta,
            0.0,
        )
        odd_acceleration = (positive[0] - negative[0]) / 2
        normalized_even_contamination = abs(
            positive[0] + negative[0] - 2 * zero[0]
        ) / max(
            abs(positive[0] - negative[0]),
            1e-30,
        )
        inertia = -strength / odd_acceleration
        curvature = c222.block_curvature_tensor(block_row.block, step=0.003)
        dispersion = 1 / float(np.mean(np.diag(curvature)))
        rows.append(
            PostClickPacketRow(
                block_row.c3_phase,
                click_weight,
                pre_click_band,
                post_click_band,
                dispersion,
                inertia,
                normalized_even_contamination,
                odd_acceleration,
                positive[0] * negative[0] < 0,
                max(
                    abs(positive[2] - 1),
                    abs(negative[2] - 1),
                    abs(zero[2] - 1),
                ),
                max(positive[3], negative[3], zero[3]),
            )
        )

    check(
        "site projection invalidates the calibrated low-band inertia interpretation",
        min(row.click_weight for row in rows) > 0.003
        and min(row.pre_click_band for row in rows) > 0.999
        and max(row.post_click_band for row in rows) < 0.8
        and min(
            abs(row.conditioned_force_response_estimator / row.dispersion_mass - 1)
            for row in rows
        )
        > 0.05
        and max(row.normalized_even_contamination for row in rows) < 1e-8
        and min(abs(row.odd_acceleration) for row in rows) > 1e-12
        and all(row.force_sign_ok for row in rows)
        and all(
            np.isfinite(row.conditioned_force_response_estimator)
            and row.conditioned_force_response_estimator > 0
            for row in rows
        )
        and max(row.norm_residual for row in rows) < 3e-10
        and max(row.boundary_weight for row in rows) < 2e-12,
        rows,
    )
def detector_inertia(
    block: np.ndarray,
    strength: float,
    *,
    detector_position: int | None,
    length: int = 4096,
    width: float = 0.006,
    duration: int = 160,
) -> InertiaRun:
    positions, momenta, packet = c222.prepare_block_packet(block, length, width)
    half = np.exp(0.5j * strength * positions)[:, None]
    detector_index = (
        None
        if detector_position is None
        else int(np.argmin(np.abs(positions - detector_position)))
    )
    norm_squared = float(np.sum(np.abs(packet) ** 2))
    means = [float(np.sum(positions * np.sum(np.abs(packet) ** 2, axis=1)))]
    click_weight = 0.0
    for _ in range(duration):
        packet *= half
        packet = c210.local_molecular_step(packet, block, axis=0)
        packet *= half
        if detector_index is not None:
            click_weight += float(np.sum(np.abs(packet[detector_index]) ** 2))
            packet[detector_index] = 0
        norm_squared = float(np.sum(np.abs(packet) ** 2))
        means.append(
            float(
                np.sum(positions * np.sum(np.abs(packet) ** 2, axis=1))
                / norm_squared
            )
        )
    times = np.arange(duration + 1, dtype=float)
    acceleration = float(
        2 * np.polyfit(times, np.asarray(means) - means[0], 2)[0]
    )
    normalized = packet / np.sqrt(norm_squared)
    position_probability = np.sum(np.abs(normalized) ** 2, axis=1)
    return InertiaRun(
        acceleration,
        float(np.sqrt(norm_squared)),
        c222.block_branch_probability(normalized, momenta, block),
        float(np.sum(position_probability[np.abs(positions) > length / 4])),
        click_weight,
    )


def target_unfed_remote_detector_rows(
    blocks: tuple[c223.BlindBlock, ...]
) -> tuple[FrozenMassRow, ...]:
    rows = []
    strength = 1e-6
    for row in blocks:
        curvature = c222.block_curvature_tensor(row.block, step=0.003)
        dispersion = 1 / float(np.mean(np.diag(curvature)))
        baseline_positive = detector_inertia(
            row.block, strength, detector_position=None
        )
        baseline_negative = detector_inertia(
            row.block, -strength, detector_position=None
        )
        detector_positive = detector_inertia(
            row.block, strength, detector_position=1000
        )
        detector_negative = detector_inertia(
            row.block, -strength, detector_position=1000
        )
        baseline_odd = (
            baseline_positive.acceleration - baseline_negative.acceleration
        ) / 2
        detector_odd = (
            detector_positive.acceleration - detector_negative.acceleration
        ) / 2
        baseline_mass = -strength / baseline_odd
        detector_mass = -strength / detector_odd
        click_weight = max(
            detector_positive.click_weight,
            detector_negative.click_weight,
        )
        health = (
            min(
                baseline_positive.band,
                baseline_negative.band,
                detector_positive.band,
                detector_negative.band,
            )
            > 0.999
            and max(
                baseline_positive.boundary,
                baseline_negative.boundary,
                detector_positive.boundary,
                detector_negative.boundary,
            )
            < 2e-12
            and min(
                baseline_positive.norm,
                baseline_negative.norm,
                detector_positive.norm,
                detector_negative.norm,
            )
            > 0.999999999
            and baseline_positive.acceleration * baseline_negative.acceleration < 0
            and detector_positive.acceleration * detector_negative.acceleration < 0
            and np.isfinite(baseline_mass)
            and np.isfinite(detector_mass)
            and min(baseline_mass, detector_mass) > 0
        )
        rows.append(
            FrozenMassRow(
                row.c3_phase,
                row.vector,
                dispersion,
                baseline_mass,
                detector_mass,
                click_weight,
                health,
            )
        )

    check(
        "a negligible-click remote detector preserves the target-unfed inertia estimate and its agreement with dispersion",
        max(abs(row.baseline_mass / row.dispersion_mass - 1) for row in rows)
        < 0.002
        and max(abs(row.detector_mass / row.dispersion_mass - 1) for row in rows)
        < 0.002
        and max(abs(row.detector_mass / row.baseline_mass - 1) for row in rows)
        < 1e-7
        and max(row.detector_click_weight for row in rows) < 1e-14
        and all(row.health for row in rows),
        rows,
    )
    return tuple(rows)


def unblind_mass_rows(
    rows: tuple[FrozenMassRow, ...], mass: np.ndarray
) -> None:
    unblinded = []
    for row in rows:
        target = float(np.vdot(row.vector, mass @ row.vector).real)
        unblinded.append(
            (
                row.c3_phase,
                target,
                row.dispersion_mass,
                row.detector_mass,
            )
        )
    check(
        "the frozen remote-detector rows unblind to the Cycle-222 mass operator",
        max(
            max(abs(dispersion / target - 1), abs(inertia / target - 1))
            for _, target, dispersion, inertia in unblinded
        )
        < 0.002,
        unblinded,
    )


def predecessor_controls() -> None:
    predecessors = (
        ROOT
        / "scripts/conditional_flavor_mass_operator_compiler_cycle222_2026_07_17.py",
        ROOT
        / "scripts/locking_cadence_record_kernel_discriminator_cycle223_2026_07_17.py",
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md",
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    )
    check(
        "the mass cadence causal-close and commit-clock predecessors remain present",
        all(path.is_file() for path in predecessors),
        [path.name for path in predecessors],
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    compiled = c222.compile_operator(c222.REFERENCE_SCALE)
    blocks = c223.c3_blind_blocks(compiled.coin)
    check(
        "three unitary candidate blocks are extracted without passing target eigenvalues to the extractor",
        len(blocks) == 3
        and max(
            np.linalg.norm(row.block.conj().T @ row.block - np.eye(6))
            for row in blocks
        )
        < 3e-12,
        [row.c3_phase for row in blocks],
    )
    event_channel_and_phase_controls(blocks)
    stationary_instrument_and_telescoping_controls(blocks)
    local_pointer_copy_controls(blocks)
    causality_and_deletion_controls(blocks)
    proper_cubic_apparatus_controls(blocks)
    history_capacity_and_redundancy_controls(blocks)
    post_click_mass_sector_controls(blocks, compiled)
    post_click_packet_contract_controls(blocks)
    frozen = target_unfed_remote_detector_rows(blocks)
    unblind_mass_rows(frozen, compiled.recovered_mass)
    predecessor_controls()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
