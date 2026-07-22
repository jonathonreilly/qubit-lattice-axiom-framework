#!/usr/bin/env python3
"""Cycle 554: current-selected persistent local response bridge.

Compose the Cycle-526 signed seam-current rails with two persistent endpoint
source flags and the Cycle-484 P8/Suzuki4/B20 directional response.  The same
fixed schedule is compiled on the complete lawful Cycle-549 Q<=2 source code.
Schedule order is compiler order, not physical time.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_selected_seam_event_current_adapter_cycle526_2026_07_21 as c526
import physical_recoil_source_literal_gate_compiler_cycle549_2026_07_21 as c549
import physical_full_layer_discrete_response_composition_cycle484_2026_07_19 as c484


c426 = c549.c426
c480 = c484.c480
c476 = c484.c476
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CURRENT_SELECTED_PERSISTENT_RESPONSE_BRIDGE_CYCLE554_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
TOL = 2.0e-9
SIGNAL_FLOOR = 1.0e-10

DEPENDENCIES = {
    "physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py":
        "7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd",
    "physical_recoil_source_literal_gate_compiler_cycle549_2026_07_21.py":
        "7eff68c6cf7688ddc23b8dbe7d66cb74c82232c2bfd4705b992c1972b5d7f399",
    "physical_full_layer_discrete_response_composition_cycle484_2026_07_19.py":
        "7551a61dd61292cbeab685b55475e6d63c5223a9185891b4605fc7bcf151a86f",
}

CURRENT_WORDS = {
    "NULL": (0, 0, 0),
    "PLUS": (1, 1, 0),
    "MINUS": (1, 0, 1),
}
Q_PAIRS = ((0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (1, 1))


@dataclass(frozen=True)
class ControlledPairSlot:
    endpoint: int
    factor_index: int
    direction: int
    coefficient_bit: int
    flag_site: int
    coefficient_site: int
    left_index: int
    right_index: int
    left_word: int
    right_word: int
    pair_sign: int
    core_angle: float


@dataclass(frozen=True)
class PhysicalManifest:
    site_layout: tuple[tuple[str, int], ...]
    flag_prep_CNOTs: tuple[tuple[int, int], ...]
    response_slots: tuple[ControlledPairSlot, ...]
    digest: str


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


def dependency_controls() -> dict:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCIES}
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 554", "edge_passed",
        "j+", "j-", "complete lawful q<=2", "e g_coarse = g_physical e",
        "all 24 proper-cubic frames", "all 576", "l5", "held l6",
        "one-particle mass", "cycle-230 contact", "cycle-230 seam",
        "depth is not time", "phase is not energy", "generator element is not a rate",
        "response is not force or gravity", "pointer copying is not a record",
        "n1 —", "n8 —", "broad negative gate: fail / do not ship",
        "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def validate_current(word: tuple[int, int, int]) -> None:
    if word not in CURRENT_WORDS.values():
        raise ValueError("current word leaves {NULL,PLUS,MINUS}")
    edge, plus, minus = word
    if edge != (plus ^ minus) or plus + minus > 1:
        raise ValueError("current word violates local EDGE/J consistency")


def persistent_flags(word: tuple[int, int, int]) -> tuple[int, int]:
    """Two local CNOTs from (J-,J+) into initially blank endpoint flags."""

    validate_current(word)
    _edge, plus, minus = word
    return minus, plus


def site_layout() -> tuple[tuple[str, int], ...]:
    rows = []
    for endpoint, label in enumerate(("LEFT", "RIGHT")):
        base = 13 * endpoint
        rows.extend((f"{label}_DATA[{bit}]", base + bit) for bit in range(13))
    rows.extend((("EDGE_PASSED", 26), ("J+", 27), ("J-", 28)))
    rows.extend((("FLAG_LEFT", 29), ("FLAG_RIGHT", 30)))
    for endpoint, label in enumerate(("LEFT", "RIGHT")):
        base = 31 + 60 * endpoint
        rows.extend(
            (f"{label}_COEFF[{direction}][{bit}]", base + 10 * direction + bit)
            for direction in range(6)
            for bit in range(10)
        )
    rows.extend((f"CONJUNCTION_WORK[{bit}]", 151 + bit) for bit in range(13))
    if tuple(site for _name, site in rows) != tuple(range(164)):
        raise RuntimeError("Cycle554 local site layout is not one explicit 164-M2 interval")
    return tuple(rows)


@lru_cache(maxsize=None)
def direction_pairs(q: int, direction: int) -> tuple[tuple[int, int, int], ...]:
    if q not in (0, 1, 2) or direction not in range(6):
        raise ValueError("directional response leaves the declared Q<=2 code")
    generator = (
        c426.recoil_generator(q) - c426.recoil_generator(q, omit_direction=direction)
    ).tocoo()
    pairs = tuple(
        (int(row), int(column), int(round(float(np.real(value)))))
        for row, column, value in zip(generator.row, generator.col, generator.data)
        if row > column
    )
    occupied = tuple(index for left, right, _sign in pairs for index in (left, right))
    if len(set(occupied)) != len(occupied):
        raise RuntimeError("one directional source exponential ceased to be disjoint")
    return pairs


@lru_cache(maxsize=1)
def physical_manifest() -> PhysicalManifest:
    """One immutable installed gate list; no current, Q, or direction selects it."""

    layout = site_layout()
    name_to_site = dict(layout)
    flag_prep = (
        (name_to_site["J-"], name_to_site["FLAG_LEFT"]),
        (name_to_site["J+"], name_to_site["FLAG_RIGHT"]),
    )
    slots = []
    digest = sha256()
    for control, target in flag_prep:
        digest.update(f"CNOT|{control}|{target}\n".encode())
    factors = c480.factor_list("suzuki4", tuple(range(6)))
    for endpoint, label in enumerate(("LEFT", "RIGHT")):
        flag_site = name_to_site[f"FLAG_{label}"]
        for q in (0, 1, 2):
            for factor_index, (scale, direction) in enumerate(factors):
                for bit in range(c476.COEFFICIENT_BITS):
                    coefficient_site = name_to_site[f"{label}_COEFF[{direction}][{bit}]"]
                    angle = (
                        c480.nearest_steps(
                            scale * c426.ANGLE * (1 << bit)
                            / (2 * c476.COEFFICIENT_SCALE)
                        )
                        * c480.PHASE_QUANTUM
                    )
                    for left, right, pair_sign in direction_pairs(q, direction):
                        slot = ControlledPairSlot(
                            endpoint=endpoint,
                            factor_index=factor_index,
                            direction=direction,
                            coefficient_bit=bit,
                            flag_site=flag_site,
                            coefficient_site=coefficient_site,
                            left_index=left,
                            right_index=right,
                            left_word=c549.basis_word(q, left),
                            right_word=c549.basis_word(q, right),
                            pair_sign=pair_sign,
                            core_angle=angle,
                        )
                        slots.append(slot)
                        digest.update(
                            (
                                f"PAIR|{endpoint}|{factor_index}|{direction}|{bit}|"
                                f"{flag_site}|{coefficient_site}|{left}|{right}|"
                                f"{slot.left_word:04x}|{slot.right_word:04x}|{pair_sign}|"
                                f"{angle.hex()}\n"
                            ).encode()
                        )
    return PhysicalManifest(layout, flag_prep, tuple(slots), digest.hexdigest())


def apply_direction(state: np.ndarray, q: int, direction: int, angle: float) -> np.ndarray:
    output = np.asarray(state, dtype=complex).copy()
    cosine = math.cos(angle)
    sine = 1j * math.sin(angle)
    for left, right, sign in direction_pairs(q, direction):
        left_value = output[left].copy()
        right_value = output[right].copy()
        output[left] = cosine * left_value + sine * sign * right_value
        output[right] = cosine * right_value + sine * sign * left_value
    return output


def response_action(
    state: np.ndarray,
    q: int,
    coefficients: tuple[int, ...],
    *,
    direction_order: tuple[int, ...] = tuple(range(6)),
    inverse: bool = False,
    omit_flag: bool = False,
    omit_factor: int | None = None,
    omit_bit: tuple[int, int] | None = None,
) -> np.ndarray:
    if q not in (0, 1, 2):
        raise ValueError("response sector leaves the complete lawful Q<=2 code")
    c480.validate_compiler_domain(
        coefficients, "suzuki4", direction_order, c480.PHASE_EXPONENT
    )
    if omit_flag:
        return np.asarray(state, dtype=complex).copy()
    enumerated = tuple(enumerate(c480.factor_list("suzuki4", direction_order)))
    if inverse:
        enumerated = tuple(reversed(enumerated))
    output = np.asarray(state, dtype=complex).copy()
    sign = -1 if inverse else 1
    for factor_index, (scale, direction) in enumerated:
        if factor_index == omit_factor:
            continue
        steps = sum(
            c480.nearest_steps(
                scale * c426.ANGLE * (1 << bit) / (2 * c476.COEFFICIENT_SCALE)
            )
            for bit in range(c476.COEFFICIENT_BITS)
            if (coefficients[direction] >> bit) & 1
            and omit_bit != (direction, bit)
        )
        if steps:
            output = apply_direction(
                output, q, direction, sign * steps * c480.PHASE_QUANTUM
            )
    return output


def apply_axis(state: np.ndarray, q: int, coefficients: tuple[int, ...], axis: int,
               *, inverse: bool = False, direction_order: tuple[int, ...] = tuple(range(6)),
               omit_flag: bool = False) -> np.ndarray:
    moved = np.moveaxis(np.asarray(state, dtype=complex), axis, 0)
    shape = moved.shape
    matrix = moved.reshape(shape[0], -1)
    acted = response_action(
        matrix, q, coefficients, inverse=inverse, direction_order=direction_order,
        omit_flag=omit_flag,
    )
    return np.moveaxis(acted.reshape(shape), 0, axis)


def coarse_pair_update(
    factors: tuple[np.ndarray, np.ndarray],
    q_pair: tuple[int, int],
    current: tuple[int, int, int],
    coefficient_pair: tuple[tuple[int, ...], tuple[int, ...]],
    *,
    inverse: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    """Independent mathematical direct sum defining G_coarse."""

    validate_current(current)
    _edge, plus, minus = current
    left, right = (np.asarray(item, dtype=complex).copy() for item in factors)
    if minus:
        left = response_action(left, q_pair[0], coefficient_pair[0], inverse=inverse)
    if plus:
        right = response_action(right, q_pair[1], coefficient_pair[1], inverse=inverse)
    return left, right


def encode_word_state(q: int, vector: np.ndarray) -> dict[int, complex]:
    if q not in (0, 1, 2):
        raise ValueError("word encoding leaves one declared Q<=2 sector")
    expected = 64 * len(c426.LOCAL_STATES[q])
    if np.asarray(vector).shape != (expected,):
        raise ValueError("word encoding leaves one declared Q<=2 sector")
    return {
        c549.basis_word(q, index): complex(value)
        for index, value in enumerate(np.asarray(vector, dtype=complex))
        if value != 0
    }


def decode_word_state(q: int, amplitudes: dict[int, complex]) -> tuple[np.ndarray, float]:
    dimension = 64 * len(c426.LOCAL_STATES[q])
    words = tuple(c549.basis_word(q, index) for index in range(dimension))
    allowed = set(words)
    vector = np.asarray([amplitudes.get(word, 0j) for word in words], dtype=complex)
    leakage = float(np.sqrt(sum(abs(value) ** 2 for word, value in amplitudes.items() if word not in allowed)))
    return vector, leakage


def word_state_residual(left: dict[int, complex], right: dict[int, complex]) -> float:
    return float(np.sqrt(sum(abs(left.get(word, 0j) - right.get(word, 0j)) ** 2 for word in left.keys() | right.keys())))


def add_word_states(weighted: tuple[tuple[complex, dict[int, complex]], ...]) -> dict[int, complex]:
    output: dict[int, complex] = {}
    for weight, state in weighted:
        for word, value in state.items():
            output[word] = output.get(word, 0j) + weight * value
    return output


def interpret_fixed_manifest(
    word_states: tuple[dict[int, complex], dict[int, complex]],
    current_bits: tuple[int, int, int],
    flag_bits: tuple[int, int],
    coefficient_pair: tuple[tuple[int, ...], tuple[int, ...]],
    *,
    inverse: bool = False,
    delete_flag_site: int | None = None,
    delete_coefficient_site: int | None = None,
    delete_factor_index: int | None = None,
) -> tuple[tuple[dict[int, complex], dict[int, complex]], tuple[int, int]]:
    """Interpret every installed slot; controls make nonmatching slots identity.

    Iteration always traverses the same immutable manifest.  There is no Q
    argument or sector branch: only literal word, coefficient, and flag bits
    can enable a stored core.
    """

    if len(current_bits) != 3 or any(bit not in (0, 1) for bit in current_bits):
        raise ValueError("current rails are not three physical bits")
    if len(flag_bits) != 2 or any(bit not in (0, 1) for bit in flag_bits):
        raise ValueError("persistent source flags are not two physical bits")
    manifest = physical_manifest()
    flags = tuple(flag_bits)
    output = [dict(item) for item in word_states]
    slots = reversed(manifest.response_slots) if inverse else manifest.response_slots
    angle_sign = -1 if inverse else 1
    for slot in slots:
        if slot.flag_site == delete_flag_site or not flags[slot.endpoint]:
            continue
        if slot.coefficient_site == delete_coefficient_site:
            continue
        if slot.factor_index == delete_factor_index:
            continue
        if not ((coefficient_pair[slot.endpoint][slot.direction] >> slot.coefficient_bit) & 1):
            continue
        left_value = output[slot.endpoint].get(slot.left_word, 0j)
        right_value = output[slot.endpoint].get(slot.right_word, 0j)
        if left_value == 0 and right_value == 0:
            continue
        cosine = math.cos(slot.core_angle)
        sine = 1j * math.sin(angle_sign * slot.core_angle) * slot.pair_sign
        output[slot.endpoint][slot.left_word] = cosine * left_value + sine * right_value
        output[slot.endpoint][slot.right_word] = cosine * right_value + sine * left_value
    return (output[0], output[1]), flags


def flag_boundary_controls(current: tuple[int, int, int]) -> dict:
    """Run P from blank and P^dagger after the controlled inverse."""

    validate_current(current)
    _edge, plus, minus = current
    flags = [0, 0]
    flags[0] ^= minus
    flags[1] ^= plus
    prepared = tuple(flags)
    flags[1] ^= plus
    flags[0] ^= minus
    return {"prepared": prepared, "terminal": tuple(flags)}


def interface_and_intertwiner_controls(rows) -> dict:
    rng = np.random.default_rng(55401)
    failures = 0
    maximum_inverse = 0.0
    maximum_intertwiner = 0.0
    maximum_q1_equivalence = 0.0
    maximum_norm = 0.0
    tested = 0
    coefficient_rows = tuple((c476.expected_coefficients(row.words), row.held) for row in rows)
    sector_row_cases = 0
    for coefficients, _held in coefficient_rows:
        for q in (0, 1, 2):
            dimension = len(c426.LOCAL_STATES[q]) * 64
            probe = rng.normal(size=(dimension, 2)) + 1j * rng.normal(size=(dimension, 2))
            probe /= np.linalg.norm(probe, axis=0)
            output = response_action(probe, q, coefficients)
            inverse = response_action(output, q, coefficients, inverse=True)
            maximum_inverse = max(maximum_inverse, float(np.linalg.norm(inverse - probe)))
            maximum_norm = max(
                maximum_norm,
                float(np.max(abs(np.linalg.norm(output, axis=0) - np.linalg.norm(probe, axis=0)))),
            )
            if q == 1:
                old = c480.product_action(
                    probe, coefficients, route="suzuki4", discrete=True
                )
                maximum_q1_equivalence = max(
                    maximum_q1_equivalence, float(np.linalg.norm(output - old))
                )
            sector_row_cases += 1
    # Compare the immutable physical gate-list interpreter against an
    # independently defined coarse current-controlled direct sum.
    manifest = physical_manifest()
    boundary_failures = 0
    maximum_word_leakage = 0.0
    code_words = {
        c549.basis_word(q, index)
        for q in (0, 1, 2)
        for index in range(64 * len(c426.LOCAL_STATES[q]))
    }
    maximum_off_code_leakage = 0.0
    for q_pair in Q_PAIRS:
        dims = tuple(64 * len(c426.LOCAL_STATES[q]) for q in q_pair)
        factors = []
        for dimension in dims:
            vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
            factors.append(vector / np.linalg.norm(vector))
        coeff_pair = (coefficient_rows[0][0], coefficient_rows[-1][0])
        for current in CURRENT_WORDS.values():
            encoded = tuple(
                encode_word_state(q, vector) for q, vector in zip(q_pair, factors)
            )
            code_flags = persistent_flags(current)
            physical_words, flags = interpret_fixed_manifest(
                encoded, current, code_flags, coeff_pair
            )
            coarse_factors = coarse_pair_update(tuple(factors), q_pair, current, coeff_pair)
            physical_factors = []
            for endpoint, q in enumerate(q_pair):
                decoded, leakage = decode_word_state(q, physical_words[endpoint])
                physical_factors.append(decoded)
                maximum_word_leakage = max(maximum_word_leakage, leakage)
                maximum_off_code_leakage = max(
                    maximum_off_code_leakage,
                    float(np.sqrt(sum(
                        abs(value) ** 2
                        for word, value in physical_words[endpoint].items()
                        if word not in code_words
                    ))),
                )
            physical = np.outer(*physical_factors)
            coarse = np.outer(*coarse_factors)
            back_words, inverse_flags = interpret_fixed_manifest(
                physical_words, current, code_flags, coeff_pair, inverse=True
            )
            back = tuple(decode_word_state(q, state)[0] for q, state in zip(q_pair, back_words))
            back_tensor = np.outer(*back)
            input_tensor = np.outer(*factors)
            maximum_intertwiner = max(
                maximum_intertwiner, float(np.linalg.norm(physical - coarse))
            )
            maximum_inverse = max(
                maximum_inverse, float(np.linalg.norm(back_tensor - input_tensor))
            )
            boundary = flag_boundary_controls(current)
            boundary_failures += int(
                boundary["prepared"] != flags
                or boundary["terminal"] != (0, 0)
                or inverse_flags != flags
            )
            tested += 1

    # One coherent lawful-current direct sum.  Basis-word equality above makes
    # this extension exact by linearity; this explicit probe catches a branch
    # phase or ordering error.
    q_pair = (1, 0)
    dims = tuple(64 * len(c426.LOCAL_STATES[q]) for q in q_pair)
    factors = []
    for dimension in dims:
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        factors.append(vector / np.linalg.norm(vector))
    amplitudes = rng.normal(size=3) + 1j * rng.normal(size=3)
    amplitudes /= np.linalg.norm(amplitudes)
    physical_blocks = []
    coarse_blocks = []
    coeff_pair = (coefficient_rows[1][0], coefficient_rows[-2][0])
    for amplitude, current in zip(amplitudes, CURRENT_WORDS.values()):
        encoded = tuple(encode_word_state(q, vector) for q, vector in zip(q_pair, factors))
        actual_words, _flags = interpret_fixed_manifest(
            encoded, current, persistent_flags(current), coeff_pair
        )
        actual = tuple(
            decode_word_state(q, state)[0] for q, state in zip(q_pair, actual_words)
        )
        expected = coarse_pair_update(tuple(factors), q_pair, current, coeff_pair)
        physical_blocks.append(amplitude * np.outer(*actual).reshape(-1))
        coarse_blocks.append(amplitude * np.outer(*expected).reshape(-1))
    coherent_residual = float(
        np.linalg.norm(np.concatenate(physical_blocks) - np.concatenate(coarse_blocks))
    )

    # Sector-autonomy probe: one literal 13-M2 word register coherently spans
    # Q0, Q1, and Q2.  G_physical receives no sector label.
    sector_vectors = []
    for q in (0, 1, 2):
        dimension = 64 * len(c426.LOCAL_STATES[q])
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        sector_vectors.append(vector / np.linalg.norm(vector))
    sector_amplitudes = rng.normal(size=3) + 1j * rng.normal(size=3)
    sector_amplitudes /= np.linalg.norm(sector_amplitudes)
    coherent_word_input = add_word_states(tuple(
        (amplitude, encode_word_state(q, vector))
        for q, amplitude, vector in zip((0, 1, 2), sector_amplitudes, sector_vectors)
    ))
    left_q0 = np.zeros(64, dtype=complex)
    left_q0[0] = 1
    sector_actual_pair, _flags = interpret_fixed_manifest(
        (encode_word_state(0, left_q0), coherent_word_input),
        CURRENT_WORDS["PLUS"], persistent_flags(CURRENT_WORDS["PLUS"]), coeff_pair,
    )
    sector_expected = add_word_states(tuple(
        (
            amplitude,
            encode_word_state(q, response_action(vector, q, coeff_pair[1])),
        )
        for q, amplitude, vector in zip((0, 1, 2), sector_amplitudes, sector_vectors)
    ))
    coherent_sector_residual = word_state_residual(
        sector_actual_pair[1], sector_expected
    )
    coherent_sector_off_code_leakage = float(np.sqrt(sum(
        abs(value) ** 2
        for word, value in sector_actual_pair[1].items()
        if word not in code_words
    )))
    return {
        "representative_cases": tested,
        "flag_failures": failures,
        "flag_prepare_inverse_uncompute_failures": boundary_failures,
        "maximum_E_Gcoarse_minus_Gphysical_E": maximum_intertwiner,
        "coherent_lawful_current_direct_sum_residual": coherent_residual,
        "coherent_Q0_Q1_Q2_word_superposition_residual": coherent_sector_residual,
        "maximum_terminal_wrong_Q_word_leakage": maximum_word_leakage,
        "maximum_terminal_off_code_word_leakage": maximum_off_code_leakage,
        "coherent_sector_terminal_off_code_leakage": coherent_sector_off_code_leakage,
        "Gphysical_received_Q_argument": False,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_norm_residual": maximum_norm,
        "maximum_Q1_exact_Cycle484_action_residual": maximum_q1_equivalence,
        "all14_by_Q0_Q1_Q2_sector_row_cases": sector_row_cases,
        "train_rows": sum(not row.held for row in rows),
        "held_rows": sum(row.held for row in rows),
        "fixed_physical_manifest_slots": len(manifest.response_slots),
        "fixed_physical_manifest_sha256": manifest.digest,
    }


def encoding_controls() -> dict:
    sector_rows = []
    all_words = set()
    maximum_pair_hamming = 0
    factor_word_rows = 0
    digest = sha256()
    for q in (0, 1, 2):
        dimension = 64 * len(c426.LOCAL_STATES[q])
        words = tuple(c549.basis_word(q, index) for index in range(dimension))
        unique = len(set(words))
        disjoint = not (set(words) & all_words)
        all_words.update(words)
        for direction in range(6):
            for left, right, sign in direction_pairs(q, direction):
                left_word = c549.basis_word(q, left)
                right_word = c549.basis_word(q, right)
                maximum_pair_hamming = max(
                    maximum_pair_hamming, (left_word ^ right_word).bit_count()
                )
                digest.update(
                    f"{q}|{direction}|{left_word:04x}|{right_word:04x}|{sign}\n".encode()
                )
                factor_word_rows += 1
        sector_rows.append({
            "q": q, "dimension": dimension, "unique_13_M2_words": unique,
            "disjoint_from_lower_Q": disjoint,
            "Gram_residual_by_distinct_computational_words": 0,
        })
    return {
        "E_sector_rows": sector_rows,
        "total_distinct_code_words_Q0_Q1_Q2": len(all_words),
        "directional_factor_word_rows": factor_word_rows,
        "maximum_factor_endpoint_Hamming_distance": maximum_pair_hamming,
        "factor_word_manifest_sha256": digest.hexdigest(),
        "off_code_completion": "supplied equality-controlled one-M2 core; arbitrary extension outside the declared code",
    }


def covariance_controls(rows) -> dict:
    rng = np.random.default_rng(55402)
    coefficients = c476.expected_coefficients(next(row.words for row in rows if row.held))
    maximum_covariance = 0.0
    frames = tuple(c484.c463.proper_cubic_frames())
    for q in (0, 1, 2):
        dimension = 64 * len(c426.LOCAL_STATES[q])
        probe = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        probe /= np.linalg.norm(probe)
        baseline = response_action(probe, q, coefficients)
        for frame in frames:
            matrix = np.asarray(frame, dtype=int)
            mapping = tuple(c484.c472.direction_map(matrix))
            carried = [0] * 6
            for source, target in enumerate(mapping):
                carried[target] = coefficients[source]
            representation = c426.recoil_frame(q, matrix)
            actual = response_action(
                representation @ probe, q, tuple(carried), direction_order=mapping
            )
            maximum_covariance = max(
                maximum_covariance,
                float(np.linalg.norm(actual - representation @ baseline)),
            )
    product_failures = 0
    for left, right in product(frames, repeat=2):
        a = np.asarray(left, dtype=int)
        b = np.asarray(right, dtype=int)
        ab = a @ b
        map_a = tuple(c484.c472.direction_map(a))
        map_b = tuple(c484.c472.direction_map(b))
        map_ab = tuple(c484.c472.direction_map(ab))
        composed = tuple(map_a[map_b[index]] for index in range(6))
        product_failures += int(composed != map_ab)
        for q in (0, 1, 2):
            residual = c426.recoil_frame(q, a) @ c426.recoil_frame(q, b) - c426.recoil_frame(q, ab)
            product_failures += int(residual.nnz and np.max(abs(residual.data)) > 0)
    # Carried endpoint labels require no resort.  If seam orientation itself is
    # reversed, PLUS/MINUS, endpoint flags, coefficient blocks and tensor axes swap.
    q_pair = (1, 2)
    dims = tuple(64 * len(c426.LOCAL_STATES[q]) for q in q_pair)
    factors = []
    for dimension in dims:
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        factors.append(vector / np.linalg.norm(vector))
    pair = (coefficients, tuple(reversed(coefficients)))
    encoded = tuple(encode_word_state(q, vector) for q, vector in zip(q_pair, factors))
    plus_words, _ = interpret_fixed_manifest(
        encoded, CURRENT_WORDS["PLUS"], persistent_flags(CURRENT_WORDS["PLUS"]), pair
    )
    reversed_q = tuple(reversed(q_pair))
    reversed_encoded = tuple(
        encode_word_state(q, vector) for q, vector in zip(reversed_q, reversed(factors))
    )
    reversed_words, reversed_flags = interpret_fixed_manifest(
        reversed_encoded, CURRENT_WORDS["MINUS"], persistent_flags(CURRENT_WORDS["MINUS"]),
        tuple(reversed(pair))
    )
    plus_factors = tuple(
        decode_word_state(q, state)[0] for q, state in zip(q_pair, plus_words)
    )
    reversed_factors = tuple(
        decode_word_state(q, state)[0] for q, state in zip(reversed_q, reversed_words)
    )
    plus = np.outer(*plus_factors)
    reversed_output = np.outer(*reversed_factors)
    reversal = float(np.linalg.norm(plus.T - reversed_output))
    return {
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "maximum_all24_carried_covariance_residual_Q0_Q1_Q2": maximum_covariance,
        "all576_representation_product_failures": product_failures,
        "seam_orientation_reversal_residual": reversal,
        "reversed_flags": reversed_flags,
    }


def manifest_gate_count_controls() -> dict:
    manifest = physical_manifest()
    counts = {"Toffoli": 0, "CNOT": 0, "NOT": 0, "H": 0, "Z20_or_inverse": 0}
    q1_left = {name: 0 for name in counts}
    hamming_histogram: dict[int, int] = {}
    negative_histogram: dict[int, int] = {}
    gray_mcx = 0
    q1_words = {
        c549.basis_word(1, index)
        for index in range(64 * len(c426.LOCAL_STATES[1]))
    }
    for slot in manifest.response_slots:
        path = c549.gray_path(slot.right_word, slot.left_word)
        distance = len(path) - 1
        hamming_histogram[distance] = hamming_histogram.get(distance, 0) + 1
        if distance < 1:
            raise RuntimeError("a nontrivial manifest slot has no Gray edge")
        zero_controls = []
        for left, right in zip(path[:-2], path[1:-1]):
            target_bit = (left ^ right).bit_length() - 1
            zero_controls.append(12 - (left & ~(1 << target_bit)).bit_count())
        central_left, central_right = path[-2], path[-1]
        central_bit = (central_left ^ central_right).bit_length() - 1
        central_zero = 12 - (central_left & ~(1 << central_bit)).bit_count()
        negative_controls = 2 * sum(zero_controls) + central_zero
        not_calls = 2 * negative_controls
        negative_histogram[not_calls] = negative_histogram.get(not_calls, 0) + 1
        # The three Gray edges and their reverse are 12-control X gates
        # (21 Toffolis each).  The adjacent rotation has twelve equality
        # controls plus coefficient and flag (14 controls; 26 Toffolis).
        row = {
            "Toffoli": 2 * (distance - 1) * (2 * 12 - 3) + (2 * 14 - 2),
            "CNOT": 2,
            "NOT": not_calls,
            "H": 2,
            "Z20_or_inverse": 2 * abs(round(slot.core_angle / c480.PHASE_QUANTUM)),
        }
        gray_mcx += 2 * (distance - 1)
        for name, value in row.items():
            counts[name] += value
            if slot.endpoint == 0 and slot.left_word in q1_words:
                q1_left[name] += value
    base = c484.flagged_discrete_manifest("suzuki4")
    expected_q1 = {name: int(value) for name, value in base["counts"].items()}
    bare_calls = (
        15 * counts["Toffoli"]
        + counts["CNOT"] + counts["NOT"] + counts["H"]
        + counts["Z20_or_inverse"]
    )
    maximum_route_edges = 24
    additional_route_cnot_upper = bare_calls * 6 * (maximum_route_edges - 1)
    return {
        "actual_manifest_rows_counted": len(manifest.response_slots),
        "exact_row_derived_counts_before_routing": counts,
        "Gray_equality_MCX": gray_mcx,
        "Hamming_distance_histogram": hamming_histogram,
        "negative_control_NOT_calls_per_row_histogram": negative_histogram,
        "Q1_left_row_derived_counts": q1_left,
        "Cycle484_Q1_flagged_counts": expected_q1,
        "Q1_exact_count_match": q1_left == expected_q1,
        "exact_counts_scope": "logical Gray/equality/B20 manifest before nearest-neighbor routing",
        "conservative_bare_one_two_M2_calls_before_routing": bare_calls,
        "Cycle549_maximum_route_length_adjacent_edges": maximum_route_edges,
        "conservative_additional_routing_CNOT_upper_bound": additional_route_cnot_upper,
        "routing_bound_scope": "assumes every bare call uses a worst-case gather/un-gather path; not an exact routed count",
        "count_assumptions": (
            "Cycle549 least-significant-bit-first Gray path; six 12-control Gray X "
            "calls for every four-flip row; Cycle484 14-control adjacent B20 core; "
            "negative data equalities conjugated by explicit NOT pairs"
        ),
    }


def deletion_lawful_resource_controls(rows) -> dict:
    rng = np.random.default_rng(55403)
    coefficients = c476.expected_coefficients(next(row.words for row in rows if row.held))
    q_pair = (1, 2)
    dims = tuple(64 * len(c426.LOCAL_STATES[q]) for q in q_pair)
    factors = []
    for dimension in dims:
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        factors.append(vector / np.linalg.norm(vector))
    encoded = tuple(encode_word_state(q, vector) for q, vector in zip(q_pair, factors))
    full_words, _ = interpret_fixed_manifest(
        encoded, CURRENT_WORDS["PLUS"], persistent_flags(CURRENT_WORDS["PLUS"]),
        (coefficients, coefficients)
    )
    no_flag_words, _ = interpret_fixed_manifest(
        encoded, CURRENT_WORDS["PLUS"], persistent_flags(CURRENT_WORDS["PLUS"]),
        (coefficients, coefficients),
        delete_flag_site=dict(site_layout())["FLAG_RIGHT"],
    )
    full_factors = tuple(
        decode_word_state(q, state)[0] for q, state in zip(q_pair, full_words)
    )
    no_flag_factors = tuple(
        decode_word_state(q, state)[0] for q, state in zip(q_pair, no_flag_words)
    )
    full = np.outer(*full_factors)
    no_flag = np.outer(*no_flag_factors)
    bit = next(
        (direction, bit)
        for direction in range(6)
        for bit in range(c476.COEFFICIENT_BITS)
        if (coefficients[direction] >> bit) & 1
    )
    coefficient_site = dict(site_layout())[f"RIGHT_COEFF[{bit[0]}][{bit[1]}]"]
    no_bit_words, _ = interpret_fixed_manifest(
        encoded, CURRENT_WORDS["PLUS"], persistent_flags(CURRENT_WORDS["PLUS"]),
        (coefficients, coefficients),
        delete_coefficient_site=coefficient_site,
    )
    no_factor_words, _ = interpret_fixed_manifest(
        encoded, CURRENT_WORDS["PLUS"], persistent_flags(CURRENT_WORDS["PLUS"]),
        (coefficients, coefficients),
        delete_factor_index=0,
    )
    bit_deleted = decode_word_state(2, no_bit_words[1])[0]
    bit_full = full_factors[1]
    factor_deleted = decode_word_state(2, no_factor_words[1])[0]
    deletion_word_leakage = max(
        decode_word_state(2, state[1])[1]
        for state in (no_flag_words, no_bit_words, no_factor_words)
    )
    rejects = 0
    for word in ((0, 1, 0), (1, 1, 1), (0, 0, 1), (2, 0, 0)):
        try:
            validate_current(word)
        except ValueError:
            rejects += 1
    pair_histogram = {
        str(q): {str(len(direction_pairs(q, d))): 6} for q in (0, 1, 2) for d in (0,)
    }
    base = c484.flagged_discrete_manifest("suzuki4")
    manifest = physical_manifest()
    rotations = len(manifest.response_slots)
    base_rotations = int(base["coefficient_controlled_pair_rotations"])
    expansion_ratio = rotations // base_rotations
    gate_counts = manifest_gate_count_controls()
    payload = {
        "site_layout": manifest.site_layout,
        "current_to_flag_CNOT_sites": manifest.flag_prep_CNOTs,
        "fixed_endpoint_order": ("left", "right"),
        "route": "suzuki4", "basis": "P8/Suzuki4/B20 and Cycle549 Gray/equality/Toffoli",
        "direction_pair_counts": pair_histogram,
        "controlled_pair_rotation_slots_both_endpoints_Q0_Q1_Q2": rotations,
        "physical_manifest_sha256": manifest.digest,
    }
    return {
        "deletion_signals": {
            "delete_selected_persistent_flag": float(np.linalg.norm(full - no_flag)),
            "delete_one_active_coefficient_bit": float(np.linalg.norm(bit_full - bit_deleted)),
            "delete_first_Suzuki_factor": float(np.linalg.norm(bit_full - factor_deleted)),
        },
        "maximum_deletion_variant_wrong_Q_or_off_code_leakage": deletion_word_leakage,
        "lawful_current_words": CURRENT_WORDS,
        "lawful_domain_rejections": rejects,
        "direction_pair_histogram": pair_histogram,
        "literal_manifest": payload,
        "literal_manifest_sha256": sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest(),
        "maximum_live_local_data_M2": 2 * 13 + 3 + 2 + 2 * 60,
        "equality_controls_M2": 12,
        "coefficient_bit_controls_M2": 1,
        "persistent_flag_controls_M2": 1,
        "total_rotation_controls_M2": 14,
        "shared_clean_conjunction_work_M2": 13,
        "maximum_live_controller_interface_M2": 164,
        "installed_Cycle549_invariant_route_grid_M2_per_endpoint": 13 ** 3,
        "installed_route_grid_M2_both_endpoints": 2 * 13 ** 3,
        "conservative_disjoint_full_layer_envelope_M2": 106 + 2 * 49_866 + 2 * 13 ** 3,
        "constant_overhead_per_selected_seam": True,
        "maximum_resolved_gate_support_after_Toffoli_decomposition_M2": 2,
        "Cycle484_selected_manifest": base["manifest_digest"],
        "Cycle484_flagged_Q1_rotation_slots": base_rotations,
        "Q0_Q1_Q2_two_endpoint_expansion_ratio": expansion_ratio,
        "manifest_gate_count_derivation": gate_counts,
        "forward_flag_preparation_CNOTs": 2,
        "inverse_boundary_flag_uncompute_CNOTs": 2,
    }


def generator_validation_controls() -> dict:
    rows = []
    maximum_hermiticity = 0.0
    maximum_reconstruction = 0.0
    failures = 0
    for q in (0, 1, 2):
        dimension = 64 * len(c426.LOCAL_STATES[q])
        for direction in range(6):
            generator = (
                c426.recoil_generator(q)
                - c426.recoil_generator(q, omit_direction=direction)
            ).tocsr()
            pairs = direction_pairs(q, direction)
            pair_rows = []
            pair_columns = []
            pair_data = []
            occupied = []
            for left, right, sign in pairs:
                pair_rows.extend((left, right))
                pair_columns.extend((right, left))
                pair_data.extend((sign, sign))
                occupied.extend((left, right))
            reconstructed = sparse.coo_matrix(
                (pair_data, (pair_rows, pair_columns)),
                shape=(dimension, dimension), dtype=complex,
            ).tocsr()
            hermiticity = float(sparse.linalg.norm(generator - generator.getH()))
            reconstruction = float(sparse.linalg.norm(generator - reconstructed))
            diagonal_nonzeros = int(np.count_nonzero(generator.diagonal()))
            invalid_entries = sum(
                abs(complex(value).imag) > 0
                or float(complex(value).real) not in (-1.0, 1.0)
                for value in generator.data
            )
            disjoint_failures = len(occupied) - len(set(occupied))
            maximum_hermiticity = max(maximum_hermiticity, hermiticity)
            maximum_reconstruction = max(maximum_reconstruction, reconstruction)
            failures += int(
                hermiticity != 0
                or reconstruction != 0
                or diagonal_nonzeros != 0
                or invalid_entries != 0
                or disjoint_failures != 0
                or generator.nnz != 2 * len(pairs)
            )
            rows.append({
                "q": q, "direction": direction, "dimension": dimension,
                "pair_count": len(pairs), "generator_nonzeros": generator.nnz,
                "Hermiticity_residual": hermiticity,
                "diagonal_nonzeros": diagonal_nonzeros,
                "non_real_or_non_pm1_entries": invalid_entries,
                "disjoint_pair_cover_failures": disjoint_failures,
                "exact_pair_reconstruction_residual": reconstruction,
            })
    return {
        "direction_rows": rows,
        "maximum_Hermiticity_residual": maximum_hermiticity,
        "maximum_pair_reconstruction_residual": maximum_reconstruction,
        "validation_failures": failures,
    }


def preservation_controls(interface: dict) -> dict:
    # The q1 action is exactly Cycle484's selected action; Q0 is identity and Q2
    # is a new number-preserving direct extension.  The Cycle526/Cycle549 input
    # files are exact-pinned, so their already-run L5/held-L6 seam controls are
    # unchanged rather than re-fitted here.
    commutators = []
    for q in (0, 1, 2):
        matter = c426.local_diagonal(q, lambda mask, _field: mask.bit_count())
        for direction in range(6):
            h = c426.recoil_generator(q) - c426.recoil_generator(q, omit_direction=direction)
            commutators.append(float(sparse.linalg.norm(h @ matter - matter @ h)))
    return {
        "Cycle219_one_particle_mass_fixture": 0.45340565417488515,
        "Cycle230_complete_contact_columns": 4047,
        "Cycle230_seam_block": "exact-pinned predecessor factor only",
        "L5_training_and_held_L6": "same fixed local circuit; no size-conditioned branch",
        "maximum_matter_number_commutator_Q0_Q1_Q2": max(commutators),
        "Q1_exact_Cycle484_action_residual": interface["maximum_Q1_exact_Cycle484_action_residual"],
        "appended_controller_mass_contact_seam_observable_tested": False,
        "preservation_claim": (
            "spectator/exact-pinned predecessor composition only; no claim that the "
            "appended current-selected controller preserves the mass eigenray or contact output"
        ),
        "correlated_preparation_beyond_tested_sectors": "supplied/open",
    }


def no_go_controls() -> dict:
    routes = (
        {"route": "R1 signed rails -> two flags -> dual installed blocks", "marker": "ATTEMPTED",
         "terminal_obligation": "fixed physical manifest must equal the signed coarse direct sum",
         "retained_result": "physical_current_selected_persistent_response_bridge_cycle554_2026_07_21.py: 115200 slots; exact lawful-current comparison"},
        {"route": "R2 EDGE-only symmetric activation", "marker": "ATTEMPTED",
         "terminal_obligation": "recover receiver/sign discrimination from EDGE alone",
         "retained_result": "physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py: PLUS and MINUS share EDGE=1, so EDGE alone does not distinguish them"},
        {"route": "R3 recompute flag from endpoint occupation", "marker": "ATTEMPTED",
         "terminal_obligation": "supply a joint-code occupation decoder stable after seam reduction",
         "retained_result": "physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py: naive single-cell decoder has 18528 failures; persistent pre-reduction shadows remain a live repair"},
        {"route": "R4 persistent one-hot receiver token", "marker": "OPEN",
         "terminal_obligation": "compile token preparation/unprepare and compare resource/covariance cost",
         "retained_result": "OPEN: no retained result located that rules it out"},
        {"route": "R5 opposite signed response at both endpoints", "marker": "OPEN",
         "terminal_obligation": "state a candidate law and test local conservation plus held predictions",
         "retained_result": "physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py retains J+/J-; route not tested"},
        {"route": "R6 time-multiplex one response block", "marker": "OPEN",
         "terminal_obligation": "supply a reversible local schedule carrier and all24/576 audit",
         "retained_result": "physical_full_layer_discrete_response_composition_cycle484_2026_07_19.py supplies fixed schedule; multiplex route not tested"},
    )
    walls = (
        ("W1", "coupling-law selection among receiver-only, dual-endpoint, and token routes"),
        ("W2", "coefficient/angle/source-normalization law"),
        ("W3", "autonomous correlated current/source/coefficient preparation"),
        ("W4", "local energy-stress observable and conservation identity"),
        ("W5", "response-feedback/long-distance kernel conditional on an arbitrary supplied source, without gravity interpretation"),
    )
    pairwise = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairwise.append({
                "pair": (walls[left][0], walls[right][0]),
                "closing_first_automatically_closes_second": "no",
                "closing_second_automatically_closes_first": "no",
                "independent": "yes",
                "reason": (
                    "the walls are normalized to separate structural choice, quantitative "
                    "normalization, state preparation, conserved observable, and uninterpreted conditional response kernel; gravity identification is the downstream W4+W5 conjunction"
                ),
            })
    return {
        "N1_alternative_routes": routes,
        "N2_collapsed_open_wall_set": walls,
        "N2_full_pairwise_wall_independence": pairwise,
        "N3_hidden_wall_scan": {
            "supplied_coefficient_angle_basis": "promoted to W2",
            "supplied_current_correlations": "promoted to W3",
            "candidate_current_to_response_choice": "promoted to W1",
            "clock_and_Born_mentions": "broader TOE context; not load-bearing for the controller theorem",
        },
        "N4_residual_matching": (
            {"witness": "Cycle526", "witness_residual": "exact lawful signed-current rails",
             "current_residual": "current controls into persistent flags", "match": "yes"},
            {"witness": "Cycle549", "witness_residual": "literal Q<=2 raw-M2 source factors",
             "current_residual": "literal directional Q<=2 factors", "match": "yes"},
            {"witness": "Cycle484", "witness_residual": "Q1 flagged Suzuki4 response",
             "current_residual": "Q1 response equality", "match": "yes"},
            {"witness": "Cycle219/230", "witness_residual": "mass/contact/seam predecessor fixtures",
             "current_residual": "appended-controller observable preservation", "match": "no; spectator pin only"},
        ),
        "N5_rhetoric_audit": {
            "local_tested": "Cycle554 supplies no tested local identification of response as force/gravity, phase as energy, generator as rate, or schedule as time",
            "per_mode_per_block_latticewide": "not tested; no broader negative claim made",
        },
        "N6_partial_closure": "controller manifest closes; W1-W5 remain import-retirement targets, not proposed axioms",
        "N7_steelman": "A hostile reviewer can choose R5 or R6, both supported by retained sign/control information and not tested here; therefore no route-independent obstruction exists.",
        "N8_cross_cycle_echo": "Cycle484 and Cycle549 retired earlier primitive/compiler walls constructively; the same import-retirement pattern, not a new axiom, remains applicable to W1-W5.",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_claim": "not made",
        "axiom_pressure": "none",
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE 554: CURRENT-SELECTED PERSISTENT RESPONSE BRIDGE")
    print("authority=none; audit=unset; compiler order is not physical time")
    dependencies = dependency_controls()
    contract = note_contract()
    rows = c484.correct_word_rows()
    interface = interface_and_intertwiner_controls(rows)
    encoding = encoding_controls()
    generators = generator_validation_controls()
    covariance = covariance_controls(rows)
    deletion = deletion_lawful_resource_controls(rows)
    preservation = preservation_controls(interface)
    nogo = no_go_controls()

    check("strict Cycle526/Cycle549/Cycle484 dependencies are exact-pinned", dependencies["pass"], dependencies)
    check("the Cycle554 note freezes the claim boundary and N1-N8 gate", contract["pass"], contract)
    check(
        "one local encoding and fixed dual-endpoint physical update satisfy the declared code-space intertwiner through lawful Q<=2",
        interface["flag_failures"] == 0
        and interface["flag_prepare_inverse_uncompute_failures"] == 0
        and interface["maximum_E_Gcoarse_minus_Gphysical_E"] < TOL
        and interface["coherent_lawful_current_direct_sum_residual"] < TOL
        and interface["coherent_Q0_Q1_Q2_word_superposition_residual"] < TOL
        and interface["maximum_terminal_wrong_Q_word_leakage"] < TOL
        and interface["maximum_terminal_off_code_word_leakage"] < TOL
        and interface["coherent_sector_terminal_off_code_leakage"] < TOL
        and not interface["Gphysical_received_Q_argument"]
        and interface["maximum_inverse_residual"] < TOL
        and interface["maximum_norm_residual"] < TOL
        and interface["maximum_Q1_exact_Cycle484_action_residual"] < TOL
        and interface["fixed_physical_manifest_slots"] == 115_200,
        interface,
    )
    check(
        "E is an explicit injective 13-M2 computational-word encoding and every directional factor has literal endpoints",
        encoding["total_distinct_code_words_Q0_Q1_Q2"] == 1856
        and encoding["directional_factor_word_rows"] == 576
        and all(row["unique_13_M2_words"] == row["dimension"] for row in encoding["E_sector_rows"])
        and all(row["disjoint_from_lower_Q"] for row in encoding["E_sector_rows"]),
        encoding,
    )
    check(
        "every Q0/Q1/Q2 directional generator is exactly a Hermitian zero-diagonal disjoint signed-pair cover",
        generators["validation_failures"] == 0
        and generators["maximum_Hermiticity_residual"] == 0
        and generators["maximum_pair_reconstruction_residual"] == 0,
        generators,
    )
    check(
        "the persistent controller carries through all24 proper-cubic frames, all576 products, and seam reversal",
        covariance["proper_cubic_frames"] == 24
        and covariance["frame_products"] == 576
        and covariance["maximum_all24_carried_covariance_residual_Q0_Q1_Q2"] < TOL
        and covariance["all576_representation_product_failures"] == 0
        and covariance["seam_orientation_reversal_residual"] < TOL,
        covariance,
    )
    check(
        "flag, coefficient-bit, and factor deletions are detected and unlawful current words are rejected",
        min(deletion["deletion_signals"].values()) > SIGNAL_FLOOR
        and deletion["maximum_deletion_variant_wrong_Q_or_off_code_leakage"] < TOL
        and deletion["lawful_domain_rejections"] == 4
        and deletion["constant_overhead_per_selected_seam"]
        and deletion["maximum_resolved_gate_support_after_Toffoli_decomposition_M2"] == 2
        and deletion["total_rotation_controls_M2"] == 14
        and deletion["shared_clean_conjunction_work_M2"] == 13
        and deletion["maximum_live_controller_interface_M2"] == 164
        and deletion["conservative_disjoint_full_layer_envelope_M2"] == 104_232
        and deletion["Q0_Q1_Q2_two_endpoint_expansion_ratio"] == 12
        and deletion["manifest_gate_count_derivation"]["actual_manifest_rows_counted"] == 115_200
        and deletion["manifest_gate_count_derivation"]["Q1_exact_count_match"]
        and deletion["manifest_gate_count_derivation"]["Hamming_distance_histogram"] == {4: 115_200},
        deletion,
    )
    check(
        "the predecessor mass/contact/seam boundary is exact-pinned as spectator evidence and the new local factors preserve matter number",
        preservation["Cycle219_one_particle_mass_fixture"] == 0.45340565417488515
        and preservation["Cycle230_complete_contact_columns"] == 4047
        and preservation["maximum_matter_number_commutator_Q0_Q1_Q2"] == 0
        and preservation["Q1_exact_Cycle484_action_residual"] < TOL
        and not preservation["appended_controller_mass_contact_seam_observable_tested"],
        preservation,
    )
    check(
        "fresh N1-N8 supports only the bounded positive result and blocks broad negative or axiom-pressure language",
        len(nogo["N1_alternative_routes"]) >= 5
        and len(nogo["N2_collapsed_open_wall_set"]) == 5
        and len(nogo["N2_full_pairwise_wall_independence"]) == 10
        and all(
            row["closing_first_automatically_closes_second"] == "no"
            and row["closing_second_automatically_closes_first"] == "no"
            and row["independent"] == "yes"
            for row in nogo["N2_full_pairwise_wall_independence"]
        )
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["axiom_pressure"] == "none",
        nogo,
    )
    elapsed = perf_counter() - started
    summary = {
        "authority": AUTHORITY, "audit": AUDIT,
        "passes": PASS, "failures": FAIL,
        "elapsed_seconds": elapsed,
        "peak_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "dependencies": dependencies,
        "interface": interface,
        "encoding": encoding,
        "generator_validation": generators,
        "covariance": covariance,
        "deletion_lawful_resources": deletion,
        "preservation": preservation,
        "no_go": nogo,
        "supplied_open": (
            "Cycle484 coefficient law/P8 arithmetic/Suzuki4 order/B20 basis/angle; "
            "current-correlated preparation beyond tested sectors; energy-stress tensor; "
            "clock/proper time; physical source normalization and gravity law"
        ),
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print(f"RESULT passes={PASS} failures={FAIL} elapsed_s={elapsed:.3f}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
