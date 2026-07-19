#!/usr/bin/env python3
"""Cycle 427: physical absorption instrument and finite effect-registry bridge.

Restrict the actual Cycle-424 absorption update to its invariant Q<=1 sector,
embed a source/no-source logical qubit with blank detector M2, and extract the
click/no-click Kraus maps and effects directly from the physical matrix.  A
second fresh detector gives an actual sequential two-use instrument.

A separate bounded scalar apparatus code uses one spectator logical M2 and a
supplied covariant bright/dark preparation.  Its click effect is exactly the
installed Cycle-398 class 13, 0.39 I, so the existing B0/B1 candidate tables
give distinct grades.  Fine detector state, coarse effect, candidate grade,
and candidate Record remain distinct.  No branch norm is called occurrence,
probability, or Born weight.  Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_absorption_event_record_time_bridge_cycle424_2026_07_19 as c424
import physical_exact_registry_extension_bridge_cycle402_2026_07_18 as c402
import physical_local_reversible_oriented_bloch_interface_cycle412_2026_07_18 as c412


c423 = c424.c423
c421 = c423.c421
c408 = c412.c408
c385 = c408.c385
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ABSORPTION_INSTRUMENT_EFFECT_REGISTRY_BRIDGE_"
    "CYCLE427_NOTE_2026-07-19.md"
)
ANGLE = c423.ANGLE
TRAIN_ANGLES = (ANGLE, 0.219)
HELD_ANGLE = 0.517
SCALAR_CLASS = 13
SCALAR_WEIGHT = 0.39
TOL = 4.0e-10
AUTHORITY = "none"
AUDIT = "unset"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "actual cycle-424 unitary",
        "source/no-source logical code",
        "click/no-click kraus maps",
        "positivity, completeness, and stinespring",
        "two fresh detector m2",
        "one fixed sequential schedule",
        "complement and coarse-graining",
        "all 24 proper-cubic frames",
        "installed cycle-398 class 13",
        "0.39 i",
        "b0 assigns 0/96",
        "b1 assigns 7/96",
        "trace-labelled comparator assigns 0.39",
        "reference-frame candidate classes are not registry admissions",
        "deliberately supplied and inverse-designed",
        "typed precommit candidate adapter",
        "fine detector state is not a coarse effect",
        "reversible detector state is not a record",
        "branch norm is not occurrence, probability, or a born weight",
        "candidate grade is not selected",
        "no sampler, frequency law, or realized history",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-427 note freezes the instrument, registry, and semantic contract", not missing, missing)


def local_q(pair: tuple[int, int]) -> int:
    return c423.local_q(pair[0]) + c423.local_q(pair[1])


BASE_BASIS = tuple(pair for pair in c423.BASIS if local_q(pair) <= 1)
BASE_INDEX = {state: index for index, state in enumerate(BASE_BASIS)}
ONE_BASIS = tuple(
    (left, right, detector)
    for left, right in BASE_BASIS
    for detector in (0, 1)
    if local_q((left, right)) + detector <= 1
)
ONE_INDEX = {state: index for index, state in enumerate(ONE_BASIS)}
TWO_BASIS = tuple(
    (left, right, first, second)
    for left, right in BASE_BASIS
    for first in (0, 1)
    for second in (0, 1)
    if local_q((left, right)) + first + second <= 1
)
TWO_INDEX = {state: index for index, state in enumerate(TWO_BASIS)}


def validate_angle(angle: float) -> None:
    if not isinstance(angle, (int, float, np.floating)):
        raise TypeError("the coupling angle must be a real scalar")
    if not np.isfinite(angle) or not 0 <= float(angle) <= np.pi:
        raise ValueError("the coupling angle leaves the declared [0,pi] domain")


@lru_cache(maxsize=None)
def base_update(
    angle: float = ANGLE,
    direction: int = c424.EDGE_DIRECTION,
    delete_vertex: bool = False,
    delete_transport: bool = False,
    delete_coin: bool = False,
) -> np.ndarray:
    validate_angle(angle)
    if direction not in range(6):
        raise ValueError("edge direction must be in range(6)")
    coin = np.eye(c423.BLOCK_DIM, dtype=complex) if delete_coin else c423.local_coin()
    vertex = np.eye(c423.BLOCK_DIM, dtype=complex) if delete_vertex else c421.vertex(float(angle))
    local = vertex @ coin
    onsite = np.zeros((len(BASE_BASIS), len(BASE_BASIS)), dtype=complex)
    for source_index, (source_left, source_right) in enumerate(BASE_BASIS):
        for target_index, (target_left, target_right) in enumerate(BASE_BASIS):
            onsite[target_index, source_index] = (
                local[target_left, source_left] * local[target_right, source_right]
            )
    if delete_transport:
        return onsite
    stream = np.zeros_like(onsite)
    for source_index, state in enumerate(BASE_BASIS):
        stream[BASE_INDEX[c423.swap_field_bits(*state, direction)], source_index] = 1
    return stream @ onsite


def swap_detector_state(
    state: tuple[int, ...], detector_offset: int, direction: int
) -> tuple[int, ...]:
    left, right, *detectors = state
    reservoir, field = divmod(right, 64)
    rail_direction = c423.REVERSE[direction]
    rail = (field >> rail_direction) & 1
    detector = detectors[detector_offset]
    if rail != detector:
        field ^= 1 << rail_direction
        detectors[detector_offset] ^= 1
    return (left, reservoir * 64 + field, *detectors)


@lru_cache(maxsize=None)
def one_update(
    angle: float = ANGLE,
    direction: int = c424.EDGE_DIRECTION,
    delete_detector: bool = False,
    delete_vertex: bool = False,
    delete_transport: bool = False,
    delete_coin: bool = False,
) -> np.ndarray:
    base = base_update(angle, direction, delete_vertex, delete_transport, delete_coin)
    output = np.zeros((len(ONE_BASIS), len(ONE_BASIS)), dtype=complex)
    for source_index, (left, right, detector) in enumerate(ONE_BASIS):
        base_source = BASE_INDEX[(left, right)]
        for base_target in np.flatnonzero(np.abs(base[:, base_source]) > 1e-15):
            target_left, target_right = BASE_BASIS[int(base_target)]
            target = (target_left, target_right, detector)
            if not delete_detector:
                target = swap_detector_state(target, 0, direction)
            output[ONE_INDEX[target], source_index] = base[int(base_target), base_source]
    return output


@lru_cache(maxsize=None)
def two_use_layer(
    angle: float,
    detector_use: int,
    direction: int = c424.EDGE_DIRECTION,
    delete_detector: bool = False,
    delete_vertex: bool = False,
    delete_transport: bool = False,
    delete_coin: bool = False,
) -> np.ndarray:
    if detector_use not in (0, 1):
        raise ValueError("the sequential detector use must be zero or one")
    base = base_update(angle, direction, delete_vertex, delete_transport, delete_coin)
    output = np.zeros((len(TWO_BASIS), len(TWO_BASIS)), dtype=complex)
    for source_index, (left, right, first, second) in enumerate(TWO_BASIS):
        base_source = BASE_INDEX[(left, right)]
        for base_target in np.flatnonzero(np.abs(base[:, base_source]) > 1e-15):
            target_left, target_right = BASE_BASIS[int(base_target)]
            target = (target_left, target_right, first, second)
            if not delete_detector:
                target = swap_detector_state(target, detector_use, direction)
            output[TWO_INDEX[target], source_index] = base[int(base_target), base_source]
    return output


def logical_embedding(basis: tuple[tuple[int, ...], ...], index: dict, encoder=None) -> np.ndarray:
    detectors = (0,) * (len(basis[0]) - 2)
    output = np.zeros((len(basis), 2), dtype=complex)
    output[index[(0, 0, *detectors)], 0] = 1
    output[index[(64, 0, *detectors)], 1] = 1
    if encoder is not None:
        candidate = np.asarray(encoder, dtype=complex)
        if candidate.shape != (2, 2) or np.linalg.norm(candidate.conj().T @ candidate - np.eye(2)) > TOL:
            raise ValueError("the logical input encoder must be a two-dimensional isometry")
        output = output @ candidate
    return output


def validate_detector_blank(state: np.ndarray, basis: tuple[tuple[int, ...], ...]) -> None:
    candidate = np.asarray(state, dtype=complex)
    if candidate.shape != (len(basis),) or not np.all(np.isfinite(candidate)):
        raise ValueError("an instrument input must be one finite vector on its declared code")
    dirty_weight = sum(
        abs(candidate[index]) ** 2
        for index, physical in enumerate(basis)
        if any(physical[2:])
    )
    if dirty_weight > 2e-14:
        raise ValueError("every fresh detector M2 must enter blank")


def branch_extractor(
    basis: tuple[tuple[int, ...], ...], outcome: tuple[int, ...]
) -> np.ndarray:
    if len(outcome) != len(basis[0]) - 2 or any(bit not in (0, 1) for bit in outcome):
        raise ValueError("the detector outcome has the wrong width or a non-bit value")
    output = np.zeros((len(BASE_BASIS), len(basis)), dtype=complex)
    for source_index, state in enumerate(basis):
        if state[2:] == outcome:
            output[BASE_INDEX[state[:2]], source_index] = 1
    return output


def kraus_effects(update: np.ndarray, embedding: np.ndarray, outcomes: tuple[tuple[int, ...], ...], basis):
    stinespring = update @ embedding
    extractors = tuple(branch_extractor(basis, outcome) for outcome in outcomes)
    kraus = tuple(extractor @ stinespring for extractor in extractors)
    effects = tuple(operator.conj().T @ operator for operator in kraus)
    reconstruction = sum(
        extractor.conj().T @ operator for extractor, operator in zip(extractors, kraus)
    )
    return stinespring, extractors, kraus, effects, reconstruction


def native_one_use_controls() -> dict[str, object]:
    print("\nNATIVE SOURCE/NO-SOURCE ONE-USE INSTRUMENT")
    embedding = logical_embedding(ONE_BASIS, ONE_INDEX)
    outcomes = ((0,), (1,))
    rows = []
    failures = 0
    cached = {}
    for angle, held in tuple((value, False) for value in TRAIN_ANGLES) + ((HELD_ANGLE, True),):
        update = one_update(angle)
        stinespring, extractors, kraus, effects, reconstruction = kraus_effects(
            update, embedding, outcomes, ONE_BASIS
        )
        expected_click = np.diag((0.0, np.sin(angle) ** 2 / 6)).astype(complex)
        completeness = sum(effects) - np.eye(2)
        positivity = min(float(np.min(np.linalg.eigvalsh(effect))) for effect in effects)
        row = {
            "angle": angle,
            "held": held,
            "click_effect_residual": float(np.linalg.norm(effects[1] - expected_click)),
            "complement_residual": float(np.linalg.norm(effects[0] - (np.eye(2) - effects[1]))),
            "completeness_residual": float(np.linalg.norm(completeness)),
            "minimum_effect_eigenvalue": positivity,
            "Stinespring_isometry_residual": float(np.linalg.norm(stinespring.conj().T @ stinespring - np.eye(2))),
            "Stinespring_reconstruction_residual": float(np.linalg.norm(reconstruction - stinespring)),
        }
        failures += int(max(row[key] for key in (
            "click_effect_residual", "complement_residual", "completeness_residual",
            "Stinespring_isometry_residual", "Stinespring_reconstruction_residual",
        )) > 2e-12)
        failures += int(positivity < -2e-12)
        rows.append(row)
        cached[angle] = (update, stinespring, kraus, effects)

    update, stinespring, kraus, effects = cached[ANGLE]
    cycle424_indices = tuple(c424.INDEX[state] for state in ONE_BASIS)
    actual = c424.physical_update()[np.ix_(cycle424_indices, cycle424_indices)]
    direct_residual = float(np.linalg.norm(update - actual))

    held_input = np.asarray((np.sqrt(2 / 5), np.exp(1j * np.pi / 7) * np.sqrt(3 / 5)))
    held_rows = tuple(
        (
            outcome[0],
            float(np.linalg.norm(operator @ held_input) ** 2),
            float(np.vdot(held_input, effect @ held_input).real),
        )
        for outcome, operator, effect in zip(outcomes, kraus, effects)
    )

    detector_deleted = kraus_effects(
        one_update(ANGLE, delete_detector=True), embedding, outcomes, ONE_BASIS
    )[3][1]
    vertex_deleted = kraus_effects(
        one_update(ANGLE, delete_vertex=True), embedding, outcomes, ONE_BASIS
    )[3][1]
    transport_deleted = kraus_effects(
        one_update(ANGLE, delete_transport=True), embedding, outcomes, ONE_BASIS
    )[3][1]
    omitted_click_completeness = float(np.linalg.norm(effects[0] - np.eye(2)))
    coin_probe = np.zeros(len(ONE_BASIS), dtype=complex)
    coin_probe[ONE_INDEX[(1 << c424.EDGE_DIRECTION, 0, 0)]] = 1
    coin_deletion = float(np.linalg.norm(one_update(ANGLE) @ coin_probe - one_update(ANGLE, delete_coin=True) @ coin_probe))
    check(
        "the actual Cycle-424 unitary induces positive complete click/no-click Kraus effects on frozen train and held couplings",
        failures == 0
        and direct_residual < 2e-12
        and max(abs(left - right) for _, left, right in held_rows) < 2e-14
        and np.linalg.norm(detector_deleted) == 0
        and np.linalg.norm(vertex_deleted) == 0
        and np.linalg.norm(transport_deleted) == 0
        and omitted_click_completeness > 0.01
        and coin_deletion > 0.1,
        {
            "logical_code": "|0>=vacuum, |1>=left source reservoir; detector blank",
            "train_angles": TRAIN_ANGLES,
            "held_angle": HELD_ANGLE,
            "rows": rows,
            "direct_restriction_to_actual_Cycle424_residual": direct_residual,
            "held_input_branch_norm_vs_effect_value": held_rows,
            "detector_deleted_click_effect_norm": float(np.linalg.norm(detector_deleted)),
            "coupling_deleted_click_effect_norm": float(np.linalg.norm(vertex_deleted)),
            "transport_deleted_click_effect_norm": float(np.linalg.norm(transport_deleted)),
            "click_outcome_deleted_completeness_defect": omitted_click_completeness,
            "coin_deleted_lawful_directional_state_residual": coin_deletion,
            "branch_norm_called_probability_or_occurrence": False,
            "failures": failures,
        },
    )
    return {
        "embedding": embedding,
        "update": update,
        "stinespring": stinespring,
        "kraus": kraus,
        "effects": effects,
        "held_input": held_input,
    }


def two_use_instrument_controls(one: dict[str, object]) -> dict[str, object]:
    print("\nONE FIXED TWO-USE / TWO-FRESH-DETECTOR SCHEDULE")
    embedding = logical_embedding(TWO_BASIS, TWO_INDEX)
    first = two_use_layer(ANGLE, 0)
    second = two_use_layer(ANGLE, 1)
    update = second @ first
    outcomes = ((0, 0), (0, 1), (1, 0), (1, 1))
    stinespring, extractors, kraus, effects, reconstruction = kraus_effects(
        update, embedding, outcomes, TWO_BASIS
    )
    effect_by_outcome = dict(zip(outcomes, effects))
    completeness = float(np.linalg.norm(sum(effects) - np.eye(2)))
    positivity = min(float(np.min(np.linalg.eigvalsh(effect))) for effect in effects)
    first_marginal = (
        effect_by_outcome[(0, 0)] + effect_by_outcome[(0, 1)],
        effect_by_outcome[(1, 0)] + effect_by_outcome[(1, 1)],
    )
    second_marginal = (
        effect_by_outcome[(0, 0)] + effect_by_outcome[(1, 0)],
        effect_by_outcome[(0, 1)] + effect_by_outcome[(1, 1)],
    )
    any_click = effect_by_outcome[(0, 1)] + effect_by_outcome[(1, 0)] + effect_by_outcome[(1, 1)]
    no_click = effect_by_outcome[(0, 0)]
    held_input = one["held_input"]
    held_rows = tuple(
        (
            outcome,
            float(np.linalg.norm(operator @ held_input) ** 2),
            float(np.vdot(held_input, effect @ held_input).real),
        )
        for outcome, operator, effect in zip(outcomes, kraus, effects)
    )

    def branch_effects(candidate: np.ndarray) -> dict[tuple[int, int], np.ndarray]:
        return dict(zip(outcomes, kraus_effects(candidate, embedding, outcomes, TWO_BASIS)[3]))

    delete_first = branch_effects(second @ two_use_layer(ANGLE, 0, delete_detector=True))
    delete_second = branch_effects(two_use_layer(ANGLE, 1, delete_detector=True) @ first)
    delete_vertex = branch_effects(
        two_use_layer(ANGLE, 1, delete_vertex=True)
        @ two_use_layer(ANGLE, 0, delete_vertex=True)
    )
    delete_transport = branch_effects(
        two_use_layer(ANGLE, 1, delete_transport=True)
        @ two_use_layer(ANGLE, 0, delete_transport=True)
    )
    deleted_first_residual = float(sum(np.linalg.norm(delete_first[key] - effect_by_outcome[key]) for key in outcomes))
    deleted_second_residual = float(sum(np.linalg.norm(delete_second[key] - effect_by_outcome[key]) for key in outcomes))
    vertex_any = sum(delete_vertex[key] for key in outcomes if key != (0, 0))
    transport_any = sum(delete_transport[key] for key in outcomes if key != (0, 0))
    one_vs_two = float(np.linalg.norm(any_click - one["effects"][1]))
    inverse = float(np.linalg.norm(update.conj().T @ update - np.eye(len(TWO_BASIS))))

    menus = {
        "ordered-fine": tuple(effects),
        "first-detector-marginal": first_marginal,
        "second-detector-marginal": second_marginal,
        "unordered-pair": (
            effect_by_outcome[(0, 0)],
            effect_by_outcome[(0, 1)] + effect_by_outcome[(1, 0)],
            effect_by_outcome[(1, 1)],
        ),
        "same-versus-different": (
            effect_by_outcome[(0, 0)] + effect_by_outcome[(1, 1)],
            effect_by_outcome[(0, 1)] + effect_by_outcome[(1, 0)],
        ),
        "any-click-complement": (no_click, any_click),
    }
    menu_residuals = {name: float(np.linalg.norm(sum(menu) - np.eye(2))) for name, menu in menus.items()}
    check(
        "two fresh detector M2 give an exact sequential instrument, complements, and exhaustive coarse-grainings on one fixed schedule",
        inverse < 3e-12
        and completeness < 3e-12
        and positivity > -3e-12
        and np.linalg.norm(stinespring.conj().T @ stinespring - np.eye(2)) < 3e-12
        and np.linalg.norm(reconstruction - stinespring) < 3e-12
        and max(np.linalg.norm(first_marginal[i] - one["effects"][i]) for i in range(2)) < 3e-12
        and np.linalg.norm(effect_by_outcome[(1, 1)]) < 3e-12
        and max(menu_residuals.values()) < 3e-12
        and max(abs(left - right) for _, left, right in held_rows) < 3e-14
        and deleted_first_residual > 0.01
        and deleted_second_residual > 0.01
        and np.linalg.norm(vertex_any) == 0
        and np.linalg.norm(transport_any) == 0
        and one_vs_two > 0.01,
        {
            "physical_schedule": "G424_on_D1 then the same G424 word on fresh D2",
            "two_use_unitarity_residual": inverse,
            "completeness_residual": completeness,
            "minimum_effect_eigenvalue": positivity,
            "Stinespring_isometry_residual": float(np.linalg.norm(stinespring.conj().T @ stinespring - np.eye(2))),
            "Stinespring_reconstruction_residual": float(np.linalg.norm(reconstruction - stinespring)),
            "ordered_source_diagonal_weights": {str(key): float(effect[1, 1].real) for key, effect in effect_by_outcome.items()},
            "first_marginal_to_one_use_residuals": tuple(float(np.linalg.norm(first_marginal[i] - one["effects"][i])) for i in range(2)),
            "held_input_branch_norm_vs_effect_value": held_rows,
            "menu_completeness_residuals": menu_residuals,
            "first_detector_deletion_effect_residual": deleted_first_residual,
            "second_detector_deletion_effect_residual": deleted_second_residual,
            "coupling_deleted_any_click_norm": float(np.linalg.norm(vertex_any)),
            "transport_deleted_any_click_norm": float(np.linalg.norm(transport_any)),
            "two_use_vs_one_use_any_click_residual": one_vs_two,
            "branch_norm_called_probability_or_occurrence": False,
        },
    )
    return {
        "update": update,
        "embedding": embedding,
        "kraus": kraus,
        "effects": effects,
        "effect_by_outcome": effect_by_outcome,
        "menus": menus,
        "any_click": any_click,
    }


def frame_representation(basis: tuple[tuple[int, ...], ...], index: dict, frame: np.ndarray) -> np.ndarray:
    directions = c423.c210.direction_permutation(frame)
    output = np.zeros((len(basis), len(basis)), dtype=complex)
    for source_index, state in enumerate(basis):
        left, right, *detectors = state
        left_r, left_f = divmod(left, 64)
        right_r, right_f = divmod(right, 64)
        target = (
            left_r * 64 + c423.permute_field(left_f, directions),
            right_r * 64 + c423.permute_field(right_f, directions),
            *detectors,
        )
        output[index[target], source_index] = 1
    return output


def covariance_controls(one: dict[str, object], two: dict[str, object]) -> None:
    one_rows = []
    two_rows = []
    effect_rows = []
    base_one_effects = one["effects"]
    base_two_effects = two["effects"]
    for frame in c423.c210.proper_cubic_frames():
        directions = c423.c210.direction_permutation(frame)
        target_direction = int(np.argmax(directions[:, c424.EDGE_DIRECTION]))
        representation_one = frame_representation(ONE_BASIS, ONE_INDEX, frame)
        representation_two = frame_representation(TWO_BASIS, TWO_INDEX, frame)
        moved_one = one_update(ANGLE, target_direction)
        moved_two = (
            two_use_layer(ANGLE, 1, target_direction)
            @ two_use_layer(ANGLE, 0, target_direction)
        )
        one_rows.append(float(np.linalg.norm(representation_one @ one["update"] @ representation_one.conj().T - moved_one)))
        two_rows.append(float(np.linalg.norm(representation_two @ two["update"] @ representation_two.conj().T - moved_two)))
        moved_one_effects = kraus_effects(
            moved_one,
            logical_embedding(ONE_BASIS, ONE_INDEX),
            ((0,), (1,)),
            ONE_BASIS,
        )[3]
        moved_two_effects = kraus_effects(
            moved_two,
            logical_embedding(TWO_BASIS, TWO_INDEX),
            ((0, 0), (0, 1), (1, 0), (1, 1)),
            TWO_BASIS,
        )[3]
        effect_rows.append(max(
            max(np.linalg.norm(left - right) for left, right in zip(base_one_effects, moved_one_effects)),
            max(np.linalg.norm(left - right) for left, right in zip(base_two_effects, moved_two_effects)),
        ))
    check(
        "the one- and two-use physical instruments and logical effects are covariant under all 24 proper-cubic frames",
        len(one_rows) == len(two_rows) == len(effect_rows) == 24
        and max(one_rows) < 4e-12
        and max(two_rows) < 5e-12
        and max(effect_rows) < 4e-12,
        {
            "frames": len(one_rows),
            "maximum_one_use_update_covariance_residual": max(one_rows),
            "maximum_two_use_update_covariance_residual": max(two_rows),
            "maximum_logical_effect_frame_residual": max(effect_rows),
            "source_no_source_code_frame_action": "scalar/trivial",
        },
    )


def scalar_registry_bridge_controls(surfaces: c402.Surfaces) -> dict[str, object]:
    print("\nSCALAR INSTALLED-EFFECT DISCRIMINATOR")
    update = one_update(ANGLE)
    click_final = np.zeros(len(ONE_BASIS), dtype=complex)
    click_final[ONE_INDEX[(0, 0, 1)]] = 1
    dark_final = np.zeros(len(ONE_BASIS), dtype=complex)
    dark_final[ONE_INDEX[(0, 0, 0)]] = 1
    bright_input = update.conj().T @ click_final
    dark_input = update.conj().T @ dark_final
    apparatus = np.sqrt(SCALAR_WEIGHT) * bright_input + np.sqrt(1 - SCALAR_WEIGHT) * dark_input
    detector_input_weight = sum(abs(apparatus[index]) ** 2 for index, state in enumerate(ONE_BASIS) if state[2])

    logical_embedding_scalar = np.kron(np.eye(2), apparatus.reshape(-1, 1))
    joint_update = np.kron(np.eye(2), update)
    stinespring = joint_update @ logical_embedding_scalar
    physical_extractors = tuple(branch_extractor(ONE_BASIS, (detector,)) for detector in (0, 1))
    extractors = tuple(np.kron(np.eye(2), extractor) for extractor in physical_extractors)
    kraus = tuple(extractor @ stinespring for extractor in extractors)
    effects = tuple(operator.conj().T @ operator for operator in kraus)
    reconstruction = sum(extractor.conj().T @ operator for extractor, operator in zip(extractors, kraus))

    installed_effect = surfaces.installed.effects[SCALAR_CLASS]
    installed_click_residual = float(np.linalg.norm(effects[1] - installed_effect))
    scalar_identifier = c408.oriented_id(effects[1])
    complement_identifier = c408.oriented_id(effects[0])
    installed_ids_55 = tuple(c408.oriented_id(effect) for effect in surfaces.installed.effects)

    for identifier in (scalar_identifier, complement_identifier):
        c412.validate_identifier(identifier)
    states, identifiers, labels = c412.encode_cases((scalar_identifier, complement_identifier))
    decoded = c412.decode_identifiers(c412.apply_fixed_circuit(states))
    expected = identifiers.copy()
    for frame_label, frame in enumerate(c408.frames()):
        selected = labels == frame_label
        expected[selected] = np.asarray([
            c408.act_oriented(tuple(map(int, identifier)), frame)
            for identifier in identifiers[selected]
        ])
    codec_failures = int(np.sum(np.any(decoded != expected, axis=1)))

    covariant_preparation = []
    for frame in c423.c210.proper_cubic_frames():
        directions = c423.c210.direction_permutation(frame)
        target_direction = int(np.argmax(directions[:, c424.EDGE_DIRECTION]))
        representation = frame_representation(ONE_BASIS, ONE_INDEX, frame)
        moved_update = one_update(ANGLE, target_direction)
        moved_bright = moved_update.conj().T @ click_final
        moved_apparatus = np.sqrt(SCALAR_WEIGHT) * moved_bright + np.sqrt(1 - SCALAR_WEIGHT) * dark_input
        covariant_preparation.append(float(np.linalg.norm(representation @ apparatus - moved_apparatus)))

    detector_deleted = one_update(ANGLE, delete_detector=True) @ apparatus
    click_extractor = physical_extractors[1]
    detector_deleted_weight = float(np.linalg.norm(click_extractor @ detector_deleted) ** 2)
    bright_deleted_weight = float(np.linalg.norm(click_extractor @ update @ dark_input) ** 2)
    b0_numerator = 2 * c402.B_VERTEX_48[SCALAR_CLASS]
    b1_numerator = c402.B_INTERIOR_96[SCALAR_CLASS]
    trace_label = float(np.trace(effects[1]).real / 2)
    check(
        "a bounded covariant scalar apparatus code maps the physical click effect exactly to installed class 13 and exposes distinct B0/B1 candidate grades",
        abs(np.linalg.norm(apparatus) - 1) < 3e-13
        and detector_input_weight < 3e-13
        and np.linalg.norm(stinespring.conj().T @ stinespring - np.eye(2)) < 3e-12
        and np.linalg.norm(reconstruction - stinespring) < 3e-12
        and np.linalg.norm(effects[1] - SCALAR_WEIGHT * np.eye(2)) < 3e-12
        and np.linalg.norm(effects[0] - (1 - SCALAR_WEIGHT) * np.eye(2)) < 3e-12
        and installed_click_residual < 3e-12
        and scalar_identifier == installed_ids_55[SCALAR_CLASS]
        and complement_identifier not in installed_ids_55
        and b0_numerator == 0
        and b1_numerator == 7
        and abs(trace_label - SCALAR_WEIGHT) < 3e-13
        and codec_failures == 0
        and max(covariant_preparation) < 4e-12
        and detector_deleted_weight == 0
        and bright_deleted_weight == 0,
        {
            "logical_code": "one spectator M2 tensor one supplied bright/dark Cycle424 apparatus state",
            "apparatus_click_weight": SCALAR_WEIGHT,
            "detector_input_weight": detector_input_weight,
            "click_effect": "0.39 I",
            "installed_Cycle398_class": SCALAR_CLASS,
            "installed_effect_residual": installed_click_residual,
            "RouteB_identifier": scalar_identifier,
            "complement_identifier": complement_identifier,
            "complement_already_in_55_class_registry": complement_identifier in installed_ids_55,
            "B0_candidate_grade": f"{b0_numerator}/96",
            "B1_candidate_grade": f"{b1_numerator}/96",
            "trace_labelled_comparator": trace_label,
            "Cycle412_cases": len(states),
            "Cycle412_frame_action_failures": codec_failures,
            "maximum_covariant_preparation_residual": max(covariant_preparation),
            "detector_deleted_click_weight": detector_deleted_weight,
            "bright_component_deleted_click_weight": bright_deleted_weight,
            "branch_norm_identified_with_candidate_grade": False,
            "candidate_grade_selected": False,
        },
    )
    return {
        "effects": effects,
        "identifiers": (complement_identifier, scalar_identifier),
        "b0_numerator": b0_numerator,
        "b1_numerator": b1_numerator,
    }


def new_projection_rank(rows: tuple[tuple[c408.OrientedId, ...], ...], old_ids: set[c408.OrientedId]) -> tuple[int, tuple[c408.OrientedId, ...]]:
    new_ids = tuple(sorted({identifier for row in rows for identifier in row if identifier not in old_ids}))
    columns = {identifier: index for index, identifier in enumerate(new_ids)}
    matrix = np.zeros((len(rows), len(new_ids)), dtype=int)
    for row_index, row in enumerate(rows):
        for identifier, count in Counter(row).items():
            if identifier in columns:
                matrix[row_index, columns[identifier]] = count
    rank = 0 if not new_ids else int(sp.Matrix(matrix.tolist()).rank())
    return rank, new_ids


def registry_and_numerical_law_controls(
    surfaces: c402.Surfaces,
    registry_surface: c408.CodecSurface,
    one: dict[str, object],
    two: dict[str, object],
    scalar: dict[str, object],
) -> None:
    print("\nREFERENCE-FRAME CLASS / INCIDENCE LEDGER")
    installed_ids = {
        c408.oriented_id(effect) for effect in registry_surface.installed_system.effects
    }
    native_menus = {
        "one-use": tuple(one["effects"]),
        **two["menus"],
    }
    native_rows = tuple(
        tuple(c408.oriented_id(effect) for effect in menu)
        for menu in native_menus.values()
    )
    scalar_row = (scalar["identifiers"][0], scalar["identifiers"][1])
    native_gain, native_new = new_projection_rank(native_rows, installed_ids)
    all_gain, all_new = new_projection_rank(native_rows + (scalar_row,), installed_ids)
    scalar_gain, scalar_new = new_projection_rank((scalar_row,), installed_ids)

    candidate_effects = tuple(effect for menu in native_menus.values() for effect in menu) + tuple(scalar["effects"])
    candidate_ids = tuple(c408.oriented_id(effect) for effect in candidate_effects)
    trace_labels = {
        str(identifier): float(np.trace(effect).real / 2)
        for identifier, effect in zip(candidate_ids, candidate_effects)
    }
    source_click, source_no = one["effects"][1], one["effects"][0]
    nearest_55 = {
        "native_click": min(float(np.linalg.norm(source_click - effect)) for effect in surfaces.installed.effects),
        "native_no_click": min(float(np.linalg.norm(source_no - effect)) for effect in surfaces.installed.effects),
    }
    nearest_full = {
        "native_click": min(float(np.linalg.norm(source_click - effect)) for effect in registry_surface.installed_system.effects),
        "native_no_click": min(float(np.linalg.norm(source_no - effect)) for effect in registry_surface.installed_system.effects),
    }
    b0_extension = (scalar["b0_numerator"], 96 - scalar["b0_numerator"])
    b1_extension = (scalar["b1_numerator"], 96 - scalar["b1_numerator"])
    menu_residual = max(float(np.linalg.norm(sum(menu) - np.eye(2))) for menu in native_menus.values())
    check(
        "the native effects remain candidate-only while the scalar click reuses one installed class and gives an exact one-row B0/B1 extension discriminator",
        len(installed_ids) == 3347
        and registry_surface.installed_system.incidence.shape[0] == 2063
        and scalar_gain == 1
        and len(scalar_new) == 1
        and scalar["identifiers"][1] in installed_ids
        and scalar["identifiers"][0] not in installed_ids
        and c408.oriented_id(source_click) not in installed_ids
        and c408.oriented_id(source_no) not in installed_ids
        and nearest_55["native_click"] > 0.09
        and nearest_full["native_click"] > 0.002
        and b0_extension == (0, 96)
        and b1_extension == (7, 89)
        and sum(b0_extension) == sum(b1_extension) == 96
        and menu_residual < 4e-12,
        {
            "current_Cycle408_surface": {"menus": 2063, "classes": 3347, "exact_rank": 1158},
            "scalar_candidate_append": {
                "new_classes": len(scalar_new),
                "exact_rank_gain": scalar_gain,
                "candidate_shape_rank": ((2064, 3347 + len(scalar_new)), 1158 + scalar_gain),
                "B0_click_complement_numerators": b0_extension,
                "B1_click_complement_numerators": b1_extension,
            },
            "native_reference_frame_candidate_append": {
                "new_classes": len(native_new),
                "exact_new_column_projection_rank": native_gain,
                "candidate_shape_rank": ((2063 + len(native_rows), 3347 + len(native_new)), 1158 + native_gain),
            },
            "combined_candidate_append": {
                "new_classes": len(all_new),
                "exact_new_column_projection_rank": all_gain,
                "candidate_shape_rank": ((2064 + len(native_rows), 3347 + len(all_new)), 1158 + all_gain),
            },
            "native_nearest_direct_matrix_residuals_to_55": nearest_55,
            "native_nearest_direct_matrix_residuals_to_Cycle408": nearest_full,
            "trace_labelled_candidate_values": trace_labels,
            "reference_frame_candidate_classes_are_registry_admissions": False,
            "new_table_written_or_admitted": False,
            "effect_functionality_for_scalar_class": "supplied current finite-registry premise",
            "B0_or_B1_selected": False,
        },
    )


def candidate_record_typing_controls() -> None:
    fixture = c424.c364.c342.c338.build_fixture(c424.TRAIN_LENGTH)
    payload = c424.c364.words(fixture, 1)[0]
    events = tuple(
        c424.DetectorEventCandidate(
            event_id=f"Cycle427_declared_detector_label_{detected}",
            detector_site=c424.DETECTOR_COORD,
            detected=detected,
            payload=payload,
            source_case="Cycle427_declared_instrument_outcome",
        )
        for detected in (0, 1)
    )
    for event in events:
        c424.validate_event(event)
    check(
        "declared coarse labels reach the typed precommit candidate adapter without selecting an event or forming a Record",
        all(event.reversible_precommit and not event.is_Record for event in events)
        and tuple(event.detected for event in events) == (0, 1)
        and all(len(event.payload) == c424.c364.RECORD_BITS for event in events),
        {
            "declared_labels": tuple(event.detected for event in events),
            "supplied_event_identifiers": tuple(event.event_id for event in events),
            "supplied_detector_site": c424.DETECTOR_COORD,
            "supplied_payload_M2": c424.c364.RECORD_BITS,
            "fine_physical_state_dimension": len(BASE_BASIS),
            "coarse_effect_dimension": 2,
            "candidate_Record_types": tuple(event.is_Record for event in events),
            "event_selected": False,
            "Cycle364_or_Cycle366_formation_law_invoked": False,
            "actual_history_appended": False,
        },
    )


def domain_and_support_controls() -> None:
    valid_one = np.zeros(len(ONE_BASIS), dtype=complex)
    valid_one[ONE_INDEX[(0, 0, 0)]] = 1
    validate_detector_blank(valid_one, ONE_BASIS)
    dirty_one = np.zeros(len(ONE_BASIS), dtype=complex)
    dirty_one[ONE_INDEX[(0, 0, 1)]] = 1
    dirty_two = np.zeros(len(TWO_BASIS), dtype=complex)
    dirty_two[TWO_INDEX[(0, 0, 1, 0)]] = 1
    invalid = (
        lambda: validate_angle(float("nan")),
        lambda: validate_angle(-0.1),
        lambda: validate_angle(np.pi + 0.1),
        lambda: base_update(ANGLE, 6),
        lambda: two_use_layer(ANGLE, 2),
        lambda: branch_extractor(ONE_BASIS, (2,)),
        lambda: branch_extractor(TWO_BASIS, (0,)),
        lambda: logical_embedding(ONE_BASIS, ONE_INDEX, np.ones((2, 2))),
        lambda: validate_detector_blank(dirty_one, ONE_BASIS),
        lambda: validate_detector_blank(dirty_two, TWO_BASIS),
        lambda: validate_detector_blank(np.zeros(len(ONE_BASIS) - 1), ONE_BASIS),
    )
    rejected = 0
    for call in invalid:
        try:
            call()
        except (TypeError, ValueError, OverflowError, IndexError):
            rejected += 1
    support = {
        "Cycle423_transport_M2": 14,
        "native_one_use_patch_M2": 15,
        "native_two_use_patch_M2": 16,
        "fresh_detector_ancilla_M2_per_use": 1,
        "scalar_code_logical_spectator_M2": 1,
        "scalar_one_use_patch_M2": 16,
        "maximum_vertex_gate_support_M2": 7,
        "maximum_coin_gate_support_M2": 6,
        "stream_and_detector_SWAP_support_M2": 2,
        "optional_Cycle412_interface_M2": 182,
        "optional_colocated_scalar_instrument_plus_codec_M2": 198,
        "Cycle412_clean_frame_flag_work_M2": 9,
    }
    check(
        "lawful domains reject and the physical/ancilla support ledger is explicit and bounded",
        rejected == len(invalid)
        and len(BASE_BASIS) == 15
        and len(ONE_BASIS) == 16
        and len(TWO_BASIS) == 17
        and support["native_one_use_patch_M2"] == 15
        and support["native_two_use_patch_M2"] == 16
        and support["optional_colocated_scalar_instrument_plus_codec_M2"] == 198,
        {
            "Q_le_1_dimensions": {"Cycle423": len(BASE_BASIS), "one_detector": len(ONE_BASIS), "two_detectors": len(TWO_BASIS)},
            "lawful_domain_rejections": rejected,
            "support": support,
            "state_preparation_import": "class-targeted bright/dark amplitude and inverse-Cycle424 preparation are deliberately supplied",
            "minimum_resource_claim": False,
        },
    )


def semantic_inventory() -> None:
    inventory = {
        "derived": (
            "native source/no-source click/no-click Kraus maps and effects from actual Cycle424",
            "positive complete one-use and sequential two-use Stinespring instruments",
            "five exhaustive two-use coarse presentations from actual ordered branches",
            "covariant scalar 0.39I click effect equal to installed Cycle398 class13",
            "conditional B0/B1/trace-labelled numerical discriminator",
            "candidate-only class/rank increments without registry admission",
        ),
        "supplied": (
            "logical input code, detector blanks, update direction, and coupling angles",
            "fresh detector M2 and the ordered two-use invocation",
            "scalar spectator, class-targeted 0.39 bright/dark amplitude, and deliberately inverse-designed input preparation",
            "Cycle398/408 effect functionality, class order, codec resolution, and B0/B1 tables",
            "trace-labelled numerical comparator and every diagnostic input/readout tolerance",
        ),
        "not_constructed": (
            "outcome sampler or actual branch selection",
            "probability or Born interpretation of branch norms or grades",
            "frequency law, realized history, or framework Record formation",
            "autonomous apparatus/input/coupling/use renewal",
            "registry or grade-table admission outside the existing class13 match",
        ),
        "fine_detector_state_is_coarse_effect": False,
        "reversible_detector_state_is_Record": False,
        "branch_norm_is_occurrence_probability_or_Born": False,
        "candidate_grade_selected": False,
        "actual_Record_created": False,
        "sampler_frequency_or_realized_history": False,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the measurement-menu bridge preserves the fine-state/effect/grade/Record firewall and inventories every supplied interface",
        not inventory["fine_detector_state_is_coarse_effect"]
        and not inventory["reversible_detector_state_is_Record"]
        and not inventory["branch_norm_is_occurrence_probability_or_Born"]
        and not inventory["candidate_grade_selected"]
        and not inventory["actual_Record_created"]
        and not inventory["sampler_frequency_or_realized_history"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"]
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 427: PHYSICAL ABSORPTION INSTRUMENT / EFFECT REGISTRY BRIDGE")
    note_contract()
    one = native_one_use_controls()
    two = two_use_instrument_controls(one)
    covariance_controls(one, two)
    surfaces = c402.build_surfaces()
    scalar = scalar_registry_bridge_controls(surfaces)
    registry_surface = c408.build_surface(surfaces.fixtures)
    registry_and_numerical_law_controls(surfaces, registry_surface, one, two, scalar)
    candidate_record_typing_controls()
    domain_and_support_controls()
    semantic_inventory()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_ABSORPTION_INSTRUMENT_EFFECT_REGISTRY_BRIDGE_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_ABSORPTION_INSTRUMENT_EFFECT_REGISTRY_BRIDGE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
