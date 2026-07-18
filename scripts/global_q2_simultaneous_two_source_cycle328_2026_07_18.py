#!/usr/bin/env python3
"""Cycle 328 checkpoint: global-Q2 simultaneous sources on the Cycle-322 seam.

The state is sparse in source-sector occupation labels and dense only in the
4,096-state complete two-cell matter seam.  Bosonic mediators and two
independently labelled mediator species are tested as distinct supplied
statistics.  The finite occupation observables are not physical energy,
stress, gravity, metric response, force, or time.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import factorial, sqrt
from pathlib import Path
import re
import sys

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as c322


LEFT = c322.LEFT
RIGHT = c322.RIGHT
ENDPOINTS = c322.ENDPOINTS
LABELS = c322.LABELS
LOCAL_MASKS = c322.LOCAL_MASKS
LOCAL_INDEX = c322.LOCAL_INDEX
JOINT_INDEX = c322.JOINT_INDEX
ANGLE = c322.ANGLE
REVERSE = c322.REVERSE
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 3e-10
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CYCLE328_NOTE_2026-07-18.md"
)

N1_ROUTES = (
    "bosonic global-Q2 mediator",
    "independently labelled global-Q2 mediators",
    "hardcore global-Q2 mediator",
    "fermionic antisymmetric mediator",
    "unit-weight auxiliary global-Q2",
    "paired-mediator unit-weight Q2",
    "multi-edge simultaneous source network",
    "calibrated physical source observable",
)
WALLS = ("W_stats", "W_unit", "W_multiedge", "W_prepare", "W_energy")
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)

PASS = 0
FAIL = 0

QOccupation = tuple[int, int]
State = dict[QOccupation, np.ndarray]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(file_path: Path) -> str:
    text = file_path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-328 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_q2 g_q2 = g_physical,q2 e_q2",
        "global q=2",
        "both reservoirs occupied simultaneously",
        "sparse reachable restriction",
        "bosonic mediator statistics",
        "independently labelled mediator statistics",
        "nonfactorizing occupation response",
        "statistics-sensitive",
        "product of separate q1 responses",
        "actual contact is retained and firewalled but not identified by this response",
        "all 24 proper-cubic frames",
        "endpoint reversal",
        "all l=3 translations",
        "held l=6",
        "mass firewall",
        "contact firewall",
        "not force",
        "not energy",
        "not stress",
        "not gravity",
        "not metric",
        "not time",
        "supplied structure",
        "fail / do not ship",
        "no axiom pressure",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the simultaneous-Q2 theorem and interpretation", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    allowed = {"ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED"}
    markers = {}
    illegal = []
    for route in N1_ROUTES:
        pattern = re.compile(
            rf"^\|\s*{re.escape(route)}\s*\|\s*\*\*([^*]+)\*\*\s*\|",
            re.MULTILINE,
        )
        match = pattern.search(note)
        marker = match.group(1).strip() if match else "MISSING"
        markers[route] = marker
        if marker not in allowed:
            illegal.append((route, marker))
    check(
        "N1 gives exact honesty markers to eight distinct Q2 routes",
        not illegal and len(markers) == 8,
        {"markers": markers, "illegal": illegal},
    )

    lower = note.lower()
    missing_pairs = []
    for left, right in combinations(WALLS, 2):
        row = f"| `{left.lower()}`, `{right.lower()}` | no | no | yes |"
        if row not in lower:
            missing_pairs.append((left, right))
    check(
        "N2 gives both closure directions for all ten pairs in the collapsed wall set",
        not missing_pairs,
        {"directed_pairs": 10, "missing": missing_pairs},
    )

    trigger_rows = []
    for release_path in (Path(__file__).resolve(), NOTE):
        source = release_path.read_text(encoding="utf-8").lower()
        hits = tuple("".join(parts) for parts in TRIGGER_PARTS if "".join(parts) in source)
        trigger_rows.append(
            {"path": str(release_path.relative_to(ROOT)), "hits": hits}
        )
    check(
        "N3 literal methodology-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    witnesses = (
        (
            "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
            43,
            "global-q2",
        ),
        (
            "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
            112,
            "complete cycle-315",
        ),
        (
            "docs/work_history/repo/review_feedback/FULL_FOCK_UNIT_WEIGHT_MEDIATOR_PAIRED_TWO_SOURCE_CYCLE325_NOTE_2026-07-18.md",
            311,
            "global q2",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
            26,
            "two-cell fock space",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
            172,
            "coin-fswap-contact",
        ),
    )
    failures = []
    for relative_path, line_number, fragment in witnesses:
        lines = (ROOT / relative_path).read_text(encoding="utf-8").lower().splitlines()
        if line_number > len(lines) or fragment not in lines[line_number - 1]:
            failures.append((relative_path, line_number, fragment))
    check("N4 exact file-line witnesses remain literal", not failures, failures)

    required_sections = (
        "### N5 — rhetoric audit",
        "### N6 — partial-closure paths",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Gate status: **FAIL / DO NOT SHIP**",
    )
    check(
        "N5-N8 and the broad-negative failure gate remain explicit",
        all(section in note for section in required_sections),
        tuple(section for section in required_sections if section not in note),
    )


def cell_flat(cell: tuple[int, int, int], length: int) -> int:
    return (cell[0] * length + cell[1]) * length + cell[2]


def flat_cell(index: int, length: int) -> tuple[int, int, int]:
    x, remainder = divmod(index, length * length)
    y, z = divmod(remainder, length)
    return x, y, z


def field_mode(length: int, cell: tuple[int, int, int], direction: int) -> int:
    return 2 + 6 * cell_flat(cell, length) + direction


def decode_field_mode(mode: int, length: int):
    if mode < 2:
        return None
    cell_index, direction = divmod(mode - 2, 6)
    return flat_cell(cell_index, length), direction


def state_norm(state: State) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: State, right: State) -> float:
    if not left and not right:
        return 0.0
    sample = next(iter(left.values()), next(iter(right.values())))
    zero = np.zeros_like(sample)
    return float(
        np.sqrt(
            sum(
                np.vdot(
                    left.get(key, zero) - right.get(key, zero),
                    left.get(key, zero) - right.get(key, zero),
                ).real
                for key in left.keys() | right.keys()
            )
        )
    )


def prune(state: State, threshold: float = 2e-13) -> State:
    return {
        key: value for key, value in state.items() if np.linalg.norm(value) > threshold
    }


def normalize_state(state: State) -> State:
    norm = np.sqrt(state_norm(state))
    return {key: value / norm for key, value in state.items()}


def add_vector(output: State, key: QOccupation, value: np.ndarray) -> None:
    if np.linalg.norm(value) <= 2e-13:
        return
    output[key] = output.get(key, 0) + value


def matter_matrix(vector: np.ndarray, endpoint: int) -> np.ndarray:
    matrix = np.zeros((64, 64), dtype=complex)
    for local_index in range(64):
        for other_index in range(64):
            joint_index = (
                JOINT_INDEX[(local_index, other_index)]
                if endpoint == 0
                else JOINT_INDEX[(other_index, local_index)]
            )
            matrix[local_index, other_index] = vector[joint_index]
    return matrix


def matter_vector(matrix: np.ndarray, endpoint: int) -> np.ndarray:
    vector = np.zeros(4096, dtype=complex)
    for local_index in range(64):
        for other_index in range(64):
            joint_index = (
                JOINT_INDEX[(local_index, other_index)]
                if endpoint == 0
                else JOINT_INDEX[(other_index, local_index)]
            )
            vector[joint_index] = matrix[local_index, other_index]
    return vector


@lru_cache(maxsize=None)
def boson_local_configurations(charge: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        configuration
        for configuration in combinations_with_replacement(range(7), charge)
        if configuration.count(0) <= 1
    )


@lru_cache(maxsize=None)
def boson_source_generator(charge: int) -> sparse.csc_matrix:
    configurations = boson_local_configurations(charge)
    lookup = {configuration: index for index, configuration in enumerate(configurations)}
    dimension = 64 * len(configurations)
    rows = []
    columns = []
    data = []
    for q_index, configuration in enumerate(configurations):
        if 0 not in configuration:
            continue
        for source_index, mask in enumerate(LOCAL_MASKS):
            for direction in range(6):
                hopped = c322.fermion_hop(mask, direction, REVERSE[direction])
                if hopped is None:
                    continue
                target_mask, matter_sign = hopped
                field_label = 1 + direction
                field_occupation = configuration.count(field_label)
                target_configuration = list(configuration)
                target_configuration.remove(0)
                target_configuration.append(field_label)
                target_configuration.sort()
                target_q = lookup[tuple(target_configuration)]
                target_index = LOCAL_INDEX[target_mask]
                source_row = 64 * q_index + source_index
                target_row = 64 * target_q + target_index
                amplitude = matter_sign * sqrt(field_occupation + 1)
                rows.extend((target_row, source_row))
                columns.extend((source_row, target_row))
                data.extend((amplitude, amplitude))
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()


def boson_source_frame(charge: int, frame: np.ndarray) -> sparse.csc_matrix:
    configurations = boson_local_configurations(charge)
    lookup = {configuration: index for index, configuration in enumerate(configurations)}
    q_rows = []
    q_columns = []
    for source, configuration in enumerate(configurations):
        mapped = tuple(
            sorted(
                0
                if label == 0
                else 1 + c315.c311.direction_map(frame, label - 1)
                for label in configuration
            )
        )
        q_rows.append(lookup[mapped])
        q_columns.append(source)
    q_representation = sparse.coo_matrix(
        (np.ones(len(configurations)), (q_rows, q_columns)),
        shape=(len(configurations), len(configurations)),
        dtype=complex,
    ).tocsc()
    matter_representation = sparse.csc_matrix(c322.local_fock_frame(frame))
    return sparse.kron(q_representation, matter_representation, format="csc")


def active_global_modes(
    length: int, endpoint: int, endpoint_cells=ENDPOINTS
) -> tuple[int, ...]:
    cell = endpoint_cells[endpoint]
    return (endpoint,) + tuple(field_mode(length, cell, direction) for direction in range(6))


def apply_boson_source(
    state: State,
    length: int,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
) -> State:
    active = active_global_modes(length, endpoint, endpoint_cells)
    active_lookup = {mode: index for index, mode in enumerate(active)}
    grouped: dict[tuple[int, ...], np.ndarray] = {}
    for occupation, vector in state.items():
        local = tuple(sorted(active_lookup[mode] for mode in occupation if mode in active_lookup))
        environment = tuple(sorted(mode for mode in occupation if mode not in active_lookup))
        configurations = boson_local_configurations(len(local))
        q_lookup = {configuration: index for index, configuration in enumerate(configurations)}
        block = grouped.setdefault(
            environment,
            np.zeros((64 * len(configurations), 64), dtype=complex),
        )
        q_index = q_lookup[local]
        block[64 * q_index : 64 * (q_index + 1), :] += matter_matrix(
            vector, endpoint
        )

    output: State = {}
    for environment, block in grouped.items():
        charge = 2 - len(environment)
        configurations = boson_local_configurations(charge)
        transformed = expm_multiply(
            1j * angle * boson_source_generator(charge), block
        )
        for q_index, local in enumerate(configurations):
            local_matrix = transformed[64 * q_index : 64 * (q_index + 1), :]
            if np.linalg.norm(local_matrix) <= 2e-13:
                continue
            global_local = tuple(active[index] for index in local)
            occupation = tuple(sorted(environment + global_local))
            add_vector(output, occupation, matter_vector(local_matrix, endpoint))
    return prune(output)


def apply_independent_source(
    state: State,
    length: int,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
) -> State:
    active = active_global_modes(length, endpoint, endpoint_cells)
    active_lookup = {mode: index for index, mode in enumerate(active)}
    _exchange, vertex, _charge, _number, _momenta = c322.local_source_blocks(angle)
    grouped: dict[int, np.ndarray] = {}
    output: State = {}
    for occupation, vector in state.items():
        species_mode = occupation[endpoint]
        other_mode = occupation[1 - endpoint]
        if species_mode not in active_lookup:
            add_vector(output, occupation, vector.copy())
            continue
        block = grouped.setdefault(
            other_mode, np.zeros((448, 64), dtype=complex)
        )
        q_index = active_lookup[species_mode]
        block[7 * np.arange(64) + q_index, :] += matter_matrix(vector, endpoint)
    for other_mode, block in grouped.items():
        transformed = vertex @ block
        for q_index, species_mode in enumerate(active):
            local_matrix = transformed[7 * np.arange(64) + q_index, :]
            if np.linalg.norm(local_matrix) <= 2e-13:
                continue
            occupation = (
                (species_mode, other_mode)
                if endpoint == 0
                else (other_mode, species_mode)
            )
            add_vector(output, occupation, matter_vector(local_matrix, endpoint))
    return prune(output)


def one_body_outcomes(
    mode: int, length: int, operation: str, *, inverse: bool = False
) -> tuple[tuple[int, complex], ...]:
    decoded = decode_field_mode(mode, length)
    if decoded is None:
        return ((mode, 1.0 + 0.0j),)
    cell, direction = decoded
    if operation == "coin":
        coin = c214.FIELD_COIN.conj().T if inverse else c214.FIELD_COIN
        return tuple(
            (field_mode(length, cell, target), coin[target, direction])
            for target in range(6)
        )
    if operation != "stream":
        raise ValueError("unknown one-body operation")
    sign = -1 if inverse else 1
    target_cell = tuple(
        (cell[axis] + sign * int(c210.DIRECTIONS[direction, axis])) % length
        for axis in range(3)
    )
    return ((field_mode(length, target_cell, direction), 1.0 + 0.0j),)


def occupation_factor(occupation: QOccupation) -> int:
    return factorial(occupation.count(occupation[0])) if occupation[0] == occupation[1] else 1


def apply_boson_one_body(
    state: State, length: int, operation: str, *, inverse: bool = False
) -> State:
    output: State = {}
    for occupation, vector in state.items():
        input_factor = sqrt(occupation_factor(occupation))
        for first_mode, first_amplitude in one_body_outcomes(
            occupation[0], length, operation, inverse=inverse
        ):
            for second_mode, second_amplitude in one_body_outcomes(
                occupation[1], length, operation, inverse=inverse
            ):
                target = tuple(sorted((first_mode, second_mode)))
                target_factor = sqrt(occupation_factor(target))
                coefficient = (
                    first_amplitude
                    * second_amplitude
                    * target_factor
                    / input_factor
                )
                add_vector(output, target, coefficient * vector)
    return prune(output)


def apply_independent_one_body(
    state: State, length: int, operation: str, *, inverse: bool = False
) -> State:
    output: State = {}
    for occupation, vector in state.items():
        for first_mode, first_amplitude in one_body_outcomes(
            occupation[0], length, operation, inverse=inverse
        ):
            for second_mode, second_amplitude in one_body_outcomes(
                occupation[1], length, operation, inverse=inverse
            ):
                add_vector(
                    output,
                    (first_mode, second_mode),
                    first_amplitude * second_amplitude * vector,
                )
    return prune(output)


def apply_matter_factor(state: State, factor: sparse.spmatrix) -> State:
    return prune({occupation: factor @ value for occupation, value in state.items()})


def apply_source(
    state: State,
    length: int,
    endpoint: int,
    statistics: str,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
) -> State:
    if statistics == "bosonic":
        return apply_boson_source(
            state, length, endpoint, endpoint_cells, angle=angle
        )
    if statistics == "independent":
        return apply_independent_source(
            state, length, endpoint, endpoint_cells, angle=angle
        )
    raise ValueError("unsupported mediator statistics")


def apply_one_body(
    state: State,
    length: int,
    operation: str,
    statistics: str,
    *,
    inverse: bool = False,
) -> State:
    if statistics == "bosonic":
        return apply_boson_one_body(
            state, length, operation, inverse=inverse
        )
    return apply_independent_one_body(
        state, length, operation, inverse=inverse
    )


def logical_step(
    state: State,
    length: int,
    factors,
    statistics: str,
    endpoint_cells=ENDPOINTS,
    *,
    enabled=(True, True),
    contact_enabled: bool = True,
) -> State:
    coin, fswap, contact = factors
    output = apply_matter_factor(state, coin)
    output = apply_one_body(output, length, "coin", statistics)
    for endpoint in range(2):
        if enabled[endpoint]:
            output = apply_source(
                output, length, endpoint, statistics, endpoint_cells
            )
    output = apply_matter_factor(output, fswap)
    output = apply_one_body(output, length, "stream", statistics)
    return apply_matter_factor(
        output, contact if contact_enabled else sparse.eye(4096, format="csc")
    )


def logical_inverse(
    state: State, length: int, factors, statistics: str
) -> State:
    coin, fswap, contact = factors
    output = apply_matter_factor(state, contact.conj().T)
    output = apply_one_body(output, length, "stream", statistics, inverse=True)
    output = apply_matter_factor(output, fswap.conj().T)
    for endpoint in (1, 0):
        output = apply_source(
            output, length, endpoint, statistics, angle=-ANGLE
        )
    output = apply_one_body(output, length, "coin", statistics, inverse=True)
    return apply_matter_factor(output, coin.conj().T)


def initial_state(length: int) -> State:
    del length
    return {(0, 1): c322.symmetric_one_one_state()}


def q2_observables(state: State, statistics: str) -> dict[str, float]:
    norm = state_norm(state)
    mean_a = 0.0
    mean_b = 0.0
    joint = 0.0
    both_fields = 0.0
    unlawful = 0.0
    for occupation, vector in state.items():
        weight = float(np.vdot(vector, vector).real)
        if statistics == "bosonic":
            n_a = occupation.count(0)
            n_b = occupation.count(1)
            field_count = sum(mode >= 2 for mode in occupation)
            lawful = len(occupation) == 2 and n_a <= 1 and n_b <= 1
        else:
            n_a = int(occupation[0] == 0)
            n_b = int(occupation[1] == 1)
            field_count = int(occupation[0] >= 2) + int(occupation[1] >= 2)
            lawful = (
                len(occupation) == 2
                and occupation[0] != 1
                and occupation[1] != 0
            )
        mean_a += n_a * weight
        mean_b += n_b * weight
        joint += n_a * n_b * weight
        both_fields += int(field_count == 2) * weight
        unlawful += int(not lawful) * weight
    return {
        "norm": norm,
        "R_A": mean_a,
        "R_B": mean_b,
        "R_A_R_B": joint,
        "connected_reservoir_covariance": joint - mean_a * mean_b,
        "both_fields": both_fields,
        "lawful_Q2_leakage": unlawful,
        "reachable_occupation_labels": len(state),
    }


def run_response(
    length: int,
    factors,
    statistics: str,
    *,
    enabled=(True, True),
    contact_enabled=True,
    depths: int = 2,
) -> tuple[State, dict[str, float], float]:
    state = initial_state(length)
    maximum_norm_drift = 0.0
    for _ in range(depths):
        state = logical_step(
            state,
            length,
            factors,
            statistics,
            enabled=enabled,
            contact_enabled=contact_enabled,
        )
        maximum_norm_drift = max(maximum_norm_drift, abs(state_norm(state) - 1))
    return state, q2_observables(state, statistics), maximum_norm_drift


def source_operator_controls() -> None:
    print("\nGLOBAL-Q2 LOCAL SOURCE LEDGERS")
    rows = []
    for charge in (1, 2):
        configurations = boson_local_configurations(charge)
        generator = boson_source_generator(charge)
        number_values = []
        q_values = []
        momentum_values = [[], [], []]
        for configuration in configurations:
            field_vectors = sum(
                (
                    c210.DIRECTIONS[label - 1]
                    for label in configuration
                    if label > 0
                ),
                start=np.zeros(3, dtype=int),
            )
            for mask in LOCAL_MASKS:
                matter_vector_sum = sum(
                    (
                        c210.DIRECTIONS[direction]
                        for direction in range(6)
                        if (mask >> direction) & 1
                    ),
                    start=np.zeros(3, dtype=int),
                )
                number_values.append(mask.bit_count())
                q_values.append(charge)
                for axis in range(3):
                    momentum_values[axis].append(
                        float(matter_vector_sum[axis] + 2 * field_vectors[axis])
                    )
        number = sparse.diags(number_values, format="csc", dtype=float)
        charge_operator = sparse.diags(q_values, format="csc", dtype=float)
        momenta = tuple(
            sparse.diags(values, format="csc", dtype=float)
            for values in momentum_values
        )
        frame_residuals = []
        frame_raw_maxima = []
        for frame in c210.proper_cubic_frames():
            representation = boson_source_frame(charge, frame)
            residual = representation @ generator - generator @ representation
            frame_residuals.append(c315.largest_singular(residual))
            frame_raw_maxima.append(c315.raw_maximum_abs(residual))
        rows.append(
            {
                "local_Q": charge,
                "dimension": generator.shape[0],
                "generator_hermiticity": c315.largest_singular(
                    generator - generator.conj().T
                ),
                "Q_commutator": c315.largest_singular(
                    generator @ charge_operator - charge_operator @ generator
                ),
                "matter_number_commutator": c315.largest_singular(
                    generator @ number - number @ generator
                ),
                "P_commutators": tuple(
                    c315.largest_singular(generator @ momentum - momentum @ generator)
                    for momentum in momenta
                ),
                "maximum_raw_P_commutator": max(
                    c315.raw_maximum_abs(
                        generator @ momentum - momentum @ generator
                    )
                    for momentum in momenta
                ),
                "maximum_source_frame_residual": max(frame_residuals),
                "maximum_source_frame_raw": max(frame_raw_maxima),
            }
        )
    check(
        "the bosonic Q2 source generators preserve exact Q, matter number, and coefficient-two vector ledgers",
        max(
            max(
                row["generator_hermiticity"],
                row["Q_commutator"],
                row["matter_number_commutator"],
                max(row["P_commutators"]),
                row["maximum_raw_P_commutator"],
                row["maximum_source_frame_residual"],
                row["maximum_source_frame_raw"],
            )
            for row in rows
        )
        == 0,
        rows,
    )


def response_controls(factors) -> dict[str, list[dict[str, object]]]:
    print("\nSIMULTANEOUS Q2 RESPONSE / STATISTICS COMPARISON")
    all_rows: dict[str, list[dict[str, object]]] = {}
    q1_matrix, _ = c322.response_matrix(3, factors)
    q1_product = float(q1_matrix[0, 0] * q1_matrix[1, 1])
    for statistics in ("bosonic", "independent"):
        rows = []
        for length in SIZES:
            _state, observables, drift = run_response(
                length, factors, statistics
            )
            rows.append(
                {
                    "L": length,
                    "held_out": length == HELD_SIZE,
                    **observables,
                    "maximum_norm_drift": drift,
                    "separate_Q1_survival_product": q1_product,
                    "joint_minus_Q1_product": observables["R_A_R_B"]
                    - q1_product,
                }
            )
        all_rows[statistics] = rows
        check(
            f"the {statistics} simultaneous sector is normalized and nonfactorizing through held L=6",
            max(row["maximum_norm_drift"] for row in rows) < TOLERANCE
            and max(row["lawful_Q2_leakage"] for row in rows) == 0
            and min(abs(row["joint_minus_Q1_product"]) for row in rows) > 1e-7
            and min(abs(row["connected_reservoir_covariance"]) for row in rows)
            > 1e-7,
            rows,
        )

    statistics_difference = max(
        abs(
            boson["R_A_R_B"] - independent["R_A_R_B"]
        )
        for boson, independent in zip(all_rows["bosonic"], all_rows["independent"])
    )
    check(
        "bosonic and independently labelled mediator statistics are operationally distinguished",
        statistics_difference > 1e-8,
        {
            "maximum_joint_survival_difference": statistics_difference,
            "bosonic": all_rows["bosonic"],
            "independent": all_rows["independent"],
        },
    )

    deletion_rows = []
    for statistics in ("bosonic", "independent"):
        _deleted_state, deleted, deleted_drift = run_response(
            3, factors, statistics, enabled=(True, False)
        )
        _no_contact_state, no_contact, no_contact_drift = run_response(
            3, factors, statistics, contact_enabled=False
        )
        deletion_rows.append(
            {
                "statistics": statistics,
                "deleted_source_B_reservoir": deleted["R_B"],
                "deleted_source_drift": deleted_drift,
                "contact_response_difference": abs(
                    no_contact["R_A_R_B"]
                    - all_rows[statistics][0]["R_A_R_B"]
                ),
                "no_contact_drift": no_contact_drift,
            }
        )
    check(
        "source deletion keeps R_B occupied and contact deletion is measured without norm leakage",
        min(row["deleted_source_B_reservoir"] for row in deletion_rows)
        > 1 - TOLERANCE
        and max(
            max(row["deleted_source_drift"], row["no_contact_drift"])
            for row in deletion_rows
        )
        < TOLERANCE,
        deletion_rows,
    )
    return all_rows


def random_q2_state(length: int, statistics: str, seed: int) -> State:
    rng = np.random.default_rng(seed)
    a0 = field_mode(length, LEFT, 0)
    b2 = field_mode(length, RIGHT, 2)
    if statistics == "bosonic":
        keys = ((0, 1), tuple(sorted((0, b2))), tuple(sorted((a0, b2))), (a0, a0))
    else:
        keys = ((0, 1), (0, b2), (a0, 1), (a0, b2), (a0, a0))
    return normalize_state(
        {
            key: rng.normal(size=4096) + 1j * rng.normal(size=4096)
            for key in keys
        }
    )


def encode_physical(state: State, encoding) -> State:
    return {key: encoding @ vector for key, vector in state.items()}


def apply_physical_matter(state: State, encoding, factor) -> State:
    output: State = {}
    for key, value in state.items():
        decoded = encoding.conj().T @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_source(
    state: State,
    encoding,
    length: int,
    endpoint: int,
    statistics: str,
    *,
    angle: float = ANGLE,
) -> State:
    decoded = {key: encoding.conj().T @ value for key, value in state.items()}
    transformed = apply_source(
        decoded, length, endpoint, statistics, angle=angle
    )
    output: State = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(4096, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return prune(output)


def physical_step(state: State, encoding, length: int, factors, statistics: str) -> State:
    coin, fswap, contact = factors
    output = apply_physical_matter(state, encoding, coin)
    output = apply_one_body(output, length, "coin", statistics)
    output = apply_physical_source(output, encoding, length, 0, statistics)
    output = apply_physical_source(output, encoding, length, 1, statistics)
    output = apply_physical_matter(output, encoding, fswap)
    output = apply_one_body(output, length, "stream", statistics)
    return apply_physical_matter(output, encoding, contact)


def physical_inverse(state: State, encoding, length: int, factors, statistics: str) -> State:
    coin, fswap, contact = factors
    output = apply_physical_matter(state, encoding, contact.conj().T)
    output = apply_one_body(output, length, "stream", statistics, inverse=True)
    output = apply_physical_matter(output, encoding, fswap.conj().T)
    output = apply_physical_source(
        output, encoding, length, 1, statistics, angle=-ANGLE
    )
    output = apply_physical_source(
        output, encoding, length, 0, statistics, angle=-ANGLE
    )
    output = apply_one_body(output, length, "coin", statistics, inverse=True)
    return apply_physical_matter(output, encoding, coin.conj().T)


def physical_controls(factors) -> None:
    print("\nSPARSE-Q2 / COMPLETE-MATTER PHYSICAL EG")
    forward = c322.build_encoding(3, False)
    reverse = c322.build_encoding(3, True)
    maximum_rows = max(forward.shape[0], reverse.shape[0])
    if forward.shape[0] < maximum_rows:
        forward.resize((maximum_rows, forward.shape[1]))
    if reverse.shape[0] < maximum_rows:
        reverse.resize((maximum_rows, reverse.shape[1]))
    rows = []
    for statistics in ("bosonic", "independent"):
        logical = random_q2_state(3, statistics, 3280 + len(rows))
        expected_logical = logical_step(logical, 3, factors, statistics)
        for orientation, encoding in (("AB", forward), ("BA", reverse)):
            encoded = encode_physical(logical, encoding)
            actual = physical_step(encoded, encoding, 3, factors, statistics)
            expected = encode_physical(expected_logical, encoding)
            recovered = physical_inverse(actual, encoding, 3, factors, statistics)
            rows.append(
                {
                    "statistics": statistics,
                    "orientation": orientation,
                    "EG_residual": state_residual(actual, expected),
                    "inverse_residual": state_residual(recovered, encoded),
                    "encoded_norm": state_norm(encoded),
                    "output_norm": state_norm(actual),
                    "reachable_input_labels": len(logical),
                    "reachable_output_labels": len(actual),
                }
            )
    check(
        "both statistics obey AB/BA physical EG and inverse EG on the complete matter seam",
        max(
            max(
                row["EG_residual"],
                row["inverse_residual"],
                abs(row["encoded_norm"] - 1),
                abs(row["output_norm"] - 1),
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )


def covariance_translation_support_controls(factors) -> None:
    print("\nFRAMES / TRANSLATIONS / HELD SUPPORT")
    coin, fswap, contact = factors
    inherited = c315.covariance_translation_controls(
        LABELS, coin, contact, contact @ fswap @ coin
    )
    field_coin_residuals = []
    stream_tests = 0
    stream_failures = 0
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        field_coin_residuals.append(
            float(
                np.linalg.norm(
                    representation @ c214.FIELD_COIN @ representation.T
                    - c214.FIELD_COIN
                )
            )
        )
        for cell in product(range(3), repeat=3):
            for direction in range(6):
                mapped_cell_vector = frame @ np.asarray(cell, dtype=int)
                mapped_cell = tuple(int(value) % 3 for value in mapped_cell_vector)
                mapped_direction = c315.c311.direction_map(frame, direction)
                streamed = tuple(
                    (cell[axis] + int(c210.DIRECTIONS[direction, axis])) % 3
                    for axis in range(3)
                )
                mapped_streamed_vector = frame @ np.asarray(streamed, dtype=int)
                mapped_streamed = tuple(
                    int(value) % 3 for value in mapped_streamed_vector
                )
                stream_after_map = tuple(
                    (
                        mapped_cell[axis]
                        + int(c210.DIRECTIONS[mapped_direction, axis])
                    )
                    % 3
                    for axis in range(3)
                )
                stream_tests += 1
                if mapped_streamed != stream_after_map:
                    stream_failures += 1
    check(
        "both Q2 statistics inherit all 24 frames including twelve endpoint reversals",
        inherited["proper_cubic_frames"] == 24
        and inherited["endpoint_reversing_frames"] == 12
        and inherited["endpoint_preserving_frames"] == 12
        and inherited["maximum_update_covariance_residual"] < TOLERANCE
        and max(field_coin_residuals) < TOLERANCE
        and stream_failures == 0,
        {
            "inherited_seam": inherited,
            "field_coin_maximum": max(field_coin_residuals),
            "one_body_stream_tests": stream_tests,
            "one_body_stream_failures": stream_failures,
        },
    )

    translation_rows = []
    for statistics in ("bosonic", "independent"):
        reference_state, reference, _drift = run_response(3, factors, statistics)
        del reference_state
        maximum = 0.0
        for displacement in product(range(3), repeat=3):
            moved_cells = tuple(
                tuple((cell[axis] + displacement[axis]) % 3 for axis in range(3))
                for cell in ENDPOINTS
            )
            state = initial_state(3)
            drift = 0.0
            for _ in range(2):
                state = logical_step(
                    state, 3, factors, statistics, endpoint_cells=moved_cells
                )
                drift = max(drift, abs(state_norm(state) - 1))
            observed = q2_observables(state, statistics)
            maximum = max(
                maximum,
                drift,
                abs(observed["R_A_R_B"] - reference["R_A_R_B"]),
                abs(observed["R_A"] - reference["R_A"]),
                abs(observed["R_B"] - reference["R_B"]),
            )
        translation_rows.append(
            {
                "statistics": statistics,
                "translations": 27,
                "maximum_response_or_norm_residual": maximum,
            }
        )
    check(
        "the simultaneous source family has translation-invariant responses for all L=3 translations",
        max(row["maximum_response_or_norm_residual"] for row in translation_rows)
        < TOLERANCE,
        translation_rows,
    )

    support_rows = []
    for length in SIZES:
        boson_state, _boson_observables, _ = run_response(
            length, factors, "bosonic"
        )
        independent_state, _independent_observables, _ = run_response(
            length, factors, "independent"
        )
        ambient_modes = 2 + 6 * length**3
        support_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "bosonic_ambient_Q2_dimension": ambient_modes * (ambient_modes + 1) // 2 - 2,
                "independent_ambient_Q2_dimension": (1 + 6 * length**3) ** 2,
                "bosonic_reachable_labels": len(boson_state),
                "independent_reachable_labels": len(independent_state),
                "matter_dimension_per_label": 4096,
                "candidate_M2_per_cell": 42,
                "candidate_two_cell_patch_M2": 109,
                "Q2_factor_boundary": "two boson rails or two labelled species are supplied orthogonal factors, not primitive-synthesized here",
            }
        )
    check(
        "the sparse reachable restriction remains closed through held L=6 with explicit ambient dimensions",
        all(row["bosonic_reachable_labels"] < 5000 for row in support_rows)
        and all(row["independent_reachable_labels"] < 5000 for row in support_rows),
        support_rows,
    )


def contact_mass_inventory_controls(factors, response_rows) -> None:
    print("\nCONTACT / MASS / INVENTORY")
    _coin, _fswap, contact = factors
    logical_rows = c315.logical_update_controls(LABELS)[4]
    contact_deleted = c315.largest_singular(
        contact - sparse.eye(4096, format="csc")
    )
    check(
        "the actual contact and one-particle mass fixture remain firewalled",
        logical_rows["contact_nontrivial_columns"] == 4047
        and contact_deleted > 1.9
        and abs(logical_rows["two_cell_rest_mass"] - logical_rows["Cycle219_mass_fixture"])
        < TOLERANCE,
        {
            "contact_nontrivial_columns": logical_rows["contact_nontrivial_columns"],
            "contact_deletion_opnorm": contact_deleted,
            "mass_fixture": logical_rows["Cycle219_mass_fixture"],
            "two_cell_mass": logical_rows["two_cell_rest_mass"],
            "mass_residual": logical_rows["two_cell_uniform_one_particle_residual"],
        },
    )
    inventory = {
        "matter": "Cycle-315 complete M64 tensor M64 seam and actual contact",
        "Q2 preparation": "one occupied reservoir at A and one at B",
        "bosonic choice": "one symmetric mediator species, field double occupancy allowed",
        "independent choice": "A/B labelled mediator species, coincident modes allowed",
        "source": "coefficient-two second-quantized matter/reservoir/field exchange",
        "protocol": "matter/field coins, A/B sources, FSWAP, stream, contact, two depths",
        "restriction": "sparse reachable Q2 occupation labels tensor dense 4096 matter",
        "response": "reservoir means, joint survival, covariance, both-field probability",
        "comparison": "product of separate Cycle-322 Q1 diagonal survivals",
        "derived": response_rows,
        "open": "hardcore mediator, unit-weight Q2, tag/species selection, calibration, multi-edge",
        "interpretation": "occupation response only; not energy/stress/gravity/metric/force/time",
        "authority": "none",
        "audit": "unset",
    }
    check(
        "the statistics choices, sparse restriction, preparation, observables, and open structure are explicit",
        len(inventory) == 14,
        inventory,
    )


def main() -> int:
    print("CYCLE 328: GLOBAL-Q2 SIMULTANEOUS TWO-SOURCE COMPILER")
    print("authority=none; audit=unset")
    note_contract()
    coin, fswap, contact, _update, _details = c315.logical_update_controls(LABELS)
    factors = (coin, fswap, contact)
    source_operator_controls()
    response_rows = response_controls(factors)
    physical_controls(factors)
    covariance_translation_support_controls(factors)
    contact_mass_inventory_controls(factors, response_rows)
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_OPEN")
        return 1
    print("RESULT GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
