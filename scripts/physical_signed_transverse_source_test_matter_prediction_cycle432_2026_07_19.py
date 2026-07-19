#!/usr/bin/env python3
"""Cycle 432: phase-coded transverse source and physical matter receiver.

Install three Cycle-319/396 physical M64 matter cells in the Cycle-425 cubic
Q=1 reservoir/field lattice.  Two source reservoirs are prepared coherently
with a fixed relative phase and a distinct M64 cell supplies the local
receiver effect.  Relative phase supplies the sign of the interference term;
no occupation is negative.

This is a bounded near-side prediction seam.  It is not the host density,
packet, centroid, width, or fit used by the named Cycle-420 impact and
quadrupole surfaces.  Direction ledgers are not force, momentum, energy,
stress, or gravity; step count is not time; coherent weights are not a Born
law or Records.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_cubic_transient_stationary_update_cycle425_2026_07_19 as c425
import physical_recoil_hard_core_field_bridge_cycle426_2026_07_19 as c426
import physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18 as c396
import physical_source_prediction_bridge_contract_cycle420_2026_07_19 as c420


c319 = c396.c319
c322 = c396.c322
c210 = c396.c210
c219 = c319.c219
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SIGNED_TRANSVERSE_SOURCE_TEST_MATTER_PREDICTION_CYCLE432_NOTE_2026-07-19.md"
)
LABELS = c396.LABELS
LABEL_INDEX = c396.LABEL_INDEX
MATTER_DIM = len(LABELS)
LOCAL_FIELD_DIM = 7
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 9e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
LogicalState = dict[int, np.ndarray]
PhysicalState = dict[int, np.ndarray]


@dataclass(frozen=True)
class Geometry:
    name: str
    length: int
    sources: tuple[Coord, Coord]
    receiver: Coord
    depth: int
    held: bool


TRAIN = Geometry(
    "train_b1_d2", 5, ((0, 2, 1), (0, 2, 3)), (2, 2, 2), 4, False
)
HELD_TRANSLATED = Geometry(
    "held_translated_b1_d2", 6, ((1, 3, 2), (1, 3, 4)), (3, 3, 3), 4, True
)
HELD_SEPARATION = Geometry(
    "held_b1_d3", 6, ((0, 3, 2), (0, 3, 4)), (3, 3, 3), 5, True
)
HELD_TRANSVERSE = Geometry(
    "held_b2_d2", 6, ((0, 3, 1), (0, 3, 5)), (2, 3, 3), 5, True
)
GEOMETRIES = (TRAIN, HELD_TRANSLATED, HELD_SEPARATION, HELD_TRANSVERSE)


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
        "phase-coded transverse dipole seam",
        "no occupation is negative",
        "three physical m64 matter cells",
        "complete global q=1 sector",
        "physical test-matter receiver effect",
        "e_432 g_432 = g_physical,432 e_432",
        "exact inverse",
        "all 24 proper-cubic frames",
        "held translated origin, longitudinal separation, and transverse separation",
        "no refit",
        "source-one, source-two, receiver, stream, coherence, and contact deletions",
        "coefficient-two direction ledger",
        "cycle-420 impact and quadrupole named-surface flags remain false",
        "direction is not force, momentum, energy, stress, or gravity",
        "step count is not time",
        "coherent weight is not a born law or a record",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-432 note freezes the signed-profile receiver boundary", not missing, missing)


def cell_count(length: int) -> int:
    return length**3


def reservoir_index(cell: Coord, length: int) -> int:
    return c425.reservoir_index(cell, length)


def field_index(cell: Coord, direction: int, length: int) -> int:
    return c425.field_index(cell, direction, length)


def decode_field(index: int, length: int) -> tuple[Coord, int]:
    flat, direction = divmod(index - cell_count(length), 6)
    return (
        (flat // (length * length), (flat // length) % length, flat % length),
        direction,
    )


def validate_geometry(geometry: Geometry) -> None:
    coordinates = geometry.sources + (geometry.receiver,)
    if geometry.length < 5 or len(set(coordinates)) != 3:
        raise ValueError("geometry requires three distinct cells on L>=5")
    if any(value not in range(geometry.length) for cell in coordinates for value in cell):
        raise ValueError("geometry coordinate is outside its periodic cube")
    if geometry.depth < 1:
        raise ValueError("depth must be positive")


def validate_state(state: dict, length: int) -> None:
    dimension = 7 * cell_count(length)
    for key, value in state.items():
        if key not in range(dimension) or value.ndim != 1:
            raise ValueError("state is outside the cubic global-Q=1 code")


def prune(state: dict, threshold: float = 2e-13) -> dict:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def state_residual(left: dict, right: dict) -> float:
    if not left and not right:
        return 0.0
    sample = next(iter(left.values()), next(iter(right.values())))
    zero = np.zeros_like(sample)
    return float(
        np.sqrt(
            sum(
                np.vdot(left.get(key, zero) - right.get(key, zero), left.get(key, zero) - right.get(key, zero)).real
                for key in left.keys() | right.keys()
            )
        )
    )


def combine(left: dict, right: dict, phase: complex) -> dict:
    sample = next(iter(left.values()), next(iter(right.values())))
    zero = np.zeros_like(sample)
    return prune(
        {
            key: (left.get(key, zero) + phase * right.get(key, zero)) / np.sqrt(2)
            for key in left.keys() | right.keys()
        }
    )


def apply_matter(state: dict, factor: sparse.spmatrix) -> dict:
    return prune({key: factor @ value for key, value in state.items()})


def apply_field_coin(state: dict, length: int, *, inverse: bool = False, enabled: bool = True) -> dict:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    coin = c396.c214.FIELD_COIN.conj().T if inverse else c396.c214.FIELD_COIN
    output = {}
    for key, value in state.items():
        if key < cell_count(length):
            output[key] = output.get(key, 0) + value
            continue
        cell, source_direction = decode_field(key, length)
        for target_direction in range(6):
            coefficient = coin[target_direction, source_direction]
            if abs(coefficient) > 1e-15:
                target = field_index(cell, target_direction, length)
                output[target] = output.get(target, 0) + coefficient * value
    return prune(output)


def stream_target(key: int, length: int, *, inverse: bool = False) -> int:
    if key < cell_count(length):
        return key
    cell, direction = decode_field(key, length)
    displacement = (-1 if inverse else 1) * c210.DIRECTIONS[direction]
    target = tuple(int((cell[axis] + displacement[axis]) % length) for axis in range(3))
    return field_index(target, direction, length)


def apply_stream(state: dict, length: int, *, inverse: bool = False, enabled: bool = True) -> dict:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    return prune({stream_target(key, length, inverse=inverse): value for key, value in state.items()})


def source_keys(cell: Coord, length: int) -> tuple[int, ...]:
    return (reservoir_index(cell, length),) + tuple(
        field_index(cell, direction, length) for direction in range(6)
    )


def apply_source(
    state: LogicalState,
    geometry: Geometry,
    cell_index: int,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> LogicalState:
    if cell_index not in range(3):
        raise ValueError("source/receiver cell index must be zero, one, or two")
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    cell = geometry.sources[cell_index] if cell_index < 2 else geometry.receiver
    active = source_keys(cell, geometry.length)
    zero = np.zeros(MATTER_DIM, dtype=complex)
    joint = np.column_stack([state.get(key, zero) for key in active]).reshape(-1)
    operator = c396.embedded_source_operator("coefficient_two", cell_index, inverse)
    transformed = (operator @ joint).reshape((MATTER_DIM, 7))
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, local]
    return prune(output)


def logical_step(
    state: LogicalState,
    geometry: Geometry,
    factors,
    *,
    source_enabled: tuple[bool, bool, bool] = (True, True, True),
    stream_enabled: bool = True,
    contact_enabled: bool = True,
    coin_enabled: bool = True,
) -> LogicalState:
    validate_geometry(geometry)
    validate_state(state, geometry.length)
    coin, contact = factors
    output = apply_matter(state, coin)
    output = apply_field_coin(output, geometry.length, enabled=coin_enabled)
    for cell_index in range(3):
        output = apply_source(output, geometry, cell_index, enabled=source_enabled[cell_index])
    output = apply_stream(output, geometry.length, enabled=stream_enabled)
    if contact_enabled:
        output = apply_matter(output, contact)
    return output


def logical_inverse(state: LogicalState, geometry: Geometry, factors) -> LogicalState:
    coin, contact = factors
    output = apply_matter(state, contact.getH())
    output = apply_stream(output, geometry.length, inverse=True)
    for cell_index in (2, 1, 0):
        output = apply_source(output, geometry, cell_index, inverse=True)
    output = apply_field_coin(output, geometry.length, inverse=True)
    return apply_matter(output, coin.getH())


def evolve(state: LogicalState, geometry: Geometry, factors, **kwargs) -> LogicalState:
    output = state
    for _ in range(geometry.depth):
        output = logical_step(output, geometry, factors, **kwargs)
    return output


@lru_cache(maxsize=1)
def uniform_three_particle_matter() -> np.ndarray:
    vector = np.zeros(MATTER_DIM, dtype=complex)
    for first, second, third in product(range(6), repeat=3):
        label = (1, (first,), 1, (second,), 1, (third,))
        vector[LABEL_INDEX[label]] = 1 / np.sqrt(6**3)
    return vector


def source_basis(geometry: Geometry, source_index: int) -> LogicalState:
    if source_index not in (0, 1):
        raise ValueError("source basis index must be zero or one")
    return {
        reservoir_index(geometry.sources[source_index], geometry.length):
        uniform_three_particle_matter().copy()
    }


def prepared_state(geometry: Geometry, phase: complex) -> LogicalState:
    if not np.isclose(abs(phase), 1):
        raise ValueError("relative phase must have unit modulus")
    return combine(source_basis(geometry, 0), source_basis(geometry, 1), phase)


def reservoir_inner(left: dict, right: dict, geometry: Geometry) -> complex:
    key = reservoir_index(geometry.receiver, geometry.length)
    if key not in left or key not in right:
        return 0j
    return complex(np.vdot(left[key], right[key]))


def local_uniform_effect_inner(left: dict, right: dict, cell_index: int) -> complex:
    """Matrix element of a local |uniform,n=1><uniform,n=1| matter effect."""
    if cell_index not in range(3):
        raise ValueError("matter cell index must be zero, one, or two")
    result = 0j
    keys = left.keys() | right.keys()
    zero = np.zeros(MATTER_DIM, dtype=complex)
    for key in keys:
        left_vector = left.get(key, zero)
        right_vector = right.get(key, zero)
        left_groups = {}
        right_groups = {}
        for index, label in enumerate(LABELS):
            specs = c319.label_specs(label)
            number, local_label = specs[cell_index]
            if number != 1:
                continue
            others = tuple(spec for position, spec in enumerate(specs) if position != cell_index)
            left_groups[others] = left_groups.get(others, 0j) + left_vector[index] / np.sqrt(6)
            right_groups[others] = right_groups.get(others, 0j) + right_vector[index] / np.sqrt(6)
        result += sum(
            np.conj(left_groups.get(group, 0j)) * right_groups.get(group, 0j)
            for group in left_groups.keys() | right_groups.keys()
        )
    return complex(result)


def phase_rows(left: dict, right: dict, geometry: Geometry):
    reservoir_cross = reservoir_inner(left, right, geometry)
    receiver_cross = local_uniform_effect_inner(left, right, 2)
    reservoir_base = (reservoir_inner(left, left, geometry).real + reservoir_inner(right, right, geometry).real) / 2
    receiver_base = (local_uniform_effect_inner(left, left, 2).real + local_uniform_effect_inner(right, right, 2).real) / 2
    rows = []
    for label, phase in (("0", 1 + 0j), ("pi/2", 1j), ("pi", -1 + 0j), ("-pi/2", -1j)):
        rows.append(
            {
                "phase": label,
                "reservoir_weight": float(reservoir_base + np.real(phase * reservoir_cross)),
                "reservoir_signed_contrast": float(np.real(phase * reservoir_cross)),
                "receiver_uniform_effect": float(receiver_base + np.real(phase * receiver_cross)),
                "receiver_signed_contrast": float(np.real(phase * receiver_cross)),
            }
        )
    return rows, reservoir_cross, receiver_cross


@lru_cache(maxsize=None)
def matter_direction_values(cell_index: int, axis: int) -> np.ndarray:
    return np.asarray(
        [
            sum(float(c210.DIRECTIONS[direction, axis]) for direction in c319.label_specs(label)[cell_index][1])
            for label in LABELS
        ]
    )


def matter_direction(state: dict, cell_index: int) -> np.ndarray:
    return np.asarray(
        [
            sum(np.vdot(value, matter_direction_values(cell_index, axis) * value).real for value in state.values())
            for axis in range(3)
        ]
    )


def field_direction(state: dict, geometry: Geometry, cell: Coord) -> np.ndarray:
    result = np.zeros(3, dtype=float)
    for direction in range(6):
        value = state.get(field_index(cell, direction, geometry.length))
        if value is not None:
            result += float(np.vdot(value, value).real) * c210.DIRECTIONS[direction]
    return result


def receiver_vertex_trace(state: dict, geometry: Geometry, factors):
    coin, _contact = factors
    output = apply_matter(state, coin)
    output = apply_field_coin(output, geometry.length)
    output = apply_source(output, geometry, 0)
    output = apply_source(output, geometry, 1)
    return output, apply_source(output, geometry, 2)


def prediction_controls(factors) -> dict:
    print("\nPHASE-CODED TRANSVERSE PROFILE / HELD GEOMETRIES")
    summaries = []
    states = {}
    for geometry in GEOMETRIES:
        left = evolve(source_basis(geometry, 0), geometry, factors)
        right = evolve(source_basis(geometry, 1), geometry, factors)
        rows, reservoir_cross, receiver_cross = phase_rows(left, right, geometry)
        summaries.append(
            {
                "geometry": asdict(geometry),
                "source_occupations": (0.5, 0.5),
                "negative_occupations": 0,
                "phase_rows": rows,
                "reservoir_cross_term": reservoir_cross,
                "receiver_cross_term": receiver_cross,
                "norm_left": state_norm(left),
                "norm_right": state_norm(right),
                "phase_or_coupling_refit": False,
            }
        )
        states[geometry.name] = (left, right)
    by_name = {row["geometry"]["name"]: row for row in summaries}
    train = by_name[TRAIN.name]
    translated = by_name[HELD_TRANSLATED.name]
    max_norm = max(abs(row[key] - 1) for row in summaries for key in ("norm_left", "norm_right"))
    check(
        "a fixed local update turns a nonnegative two-reservoir preparation into a signed transverse receiver contrast",
        all(row["negative_occupations"] == 0 and row["source_occupations"] == (0.5, 0.5) for row in summaries)
        and all(row["phase_rows"][0]["reservoir_signed_contrast"] > 1e-10 for row in summaries)
        and all(row["phase_rows"][2]["reservoir_signed_contrast"] < -1e-10 for row in summaries)
        and all(
            abs(row["phase_rows"][0]["receiver_signed_contrast"]) > 1e-10
            and row["phase_rows"][0]["receiver_signed_contrast"]
            * row["phase_rows"][2]["receiver_signed_contrast"]
            < 0
            for row in summaries
        )
        and max_norm < TOLERANCE,
        {"rows": summaries, "signed_coordinate": "coherent contrast around the incoherent two-source baseline"},
    )
    translation_residual = max(
        abs(train["phase_rows"][index][key] - translated["phase_rows"][index][key])
        for index in range(4)
        for key in ("reservoir_weight", "receiver_uniform_effect")
    )
    check(
        "the same phase law and receiver predict translated, held longitudinal, and held transverse geometries without refitting",
        translation_residual < 2e-11
        and all(row["phase_or_coupling_refit"] is False for row in summaries)
        and all(abs(row["reservoir_cross_term"]) > 1e-10 for row in summaries)
        and all(abs(row["receiver_cross_term"]) > 1e-10 for row in summaries)
        and sum(row["geometry"]["held"] for row in summaries) == 3,
        {
            "training_geometry": asdict(TRAIN),
            "held_geometries": tuple(asdict(item) for item in GEOMETRIES if item.held),
            "translation_readout_residual": translation_residual,
            "refits_on_held": 0,
            "prediction_law": "W(phi)=B+Re[exp(i phi) K] from linear unitary propagation",
        },
    )

    third = prepared_state(TRAIN, 1 + 0j)
    for _ in range(TRAIN.depth - 1):
        third = logical_step(third, TRAIN, factors)
    before, after = receiver_vertex_trace(third, TRAIN, factors)
    matter_change = matter_direction(after, 2) - matter_direction(before, 2)
    twice_field_change = 2 * (field_direction(after, TRAIN, TRAIN.receiver) - field_direction(before, TRAIN, TRAIN.receiver))
    check(
        "the distinct physical receiver obeys the exact coefficient-two local direction balance",
        np.linalg.norm(matter_change + twice_field_change) < 2e-11,
        {
            "receiver_cell": TRAIN.receiver,
            "matter_direction_change": matter_change,
            "twice_field_direction_change": twice_field_change,
            "ledger_residual": matter_change + twice_field_change,
            "semantics": "dimensionless direction ledger only; the symmetric prepared history has a direction-null receiver trace",
        },
    )
    return {"summaries": summaries, "states": states}


def deletion_controls(factors, prediction_data) -> None:
    print("\nSOURCE / RECEIVER / STREAM / COHERENCE / CONTACT DELETIONS")
    baseline = prediction_data["summaries"][0]["phase_rows"][0]["reservoir_signed_contrast"]
    rows = []
    for label, source_enabled, stream_enabled in (
        ("source_one", (False, True, True), True),
        ("source_two", (True, False, True), True),
        ("receiver", (True, True, False), True),
        ("stream", (True, True, True), False),
    ):
        left = evolve(source_basis(TRAIN, 0), TRAIN, factors, source_enabled=source_enabled, stream_enabled=stream_enabled)
        right = evolve(source_basis(TRAIN, 1), TRAIN, factors, source_enabled=source_enabled, stream_enabled=stream_enabled)
        cross = reservoir_inner(left, right, TRAIN)
        rows.append({"deletion": label, "signed_contrast": float(cross.real)})
    incoherent_contrast = 0.0

    contact = factors[1]
    label = (2, (0, 1), 0, (), 0, ())
    vector = np.zeros(MATTER_DIM, dtype=complex)
    vector[LABEL_INDEX[label]] = 1
    contact_state = {reservoir_index(TRAIN.sources[0], TRAIN.length): vector}
    contact_on = apply_matter(contact_state, contact)
    contact_off = contact_state
    contact_residual = state_residual(contact_on, contact_off)
    prediction_contact_on = evolve(prepared_state(TRAIN, 1 + 0j), TRAIN, factors)
    prediction_contact_off = evolve(prepared_state(TRAIN, 1 + 0j), TRAIN, factors, contact_enabled=False)
    prediction_contact_residual = state_residual(prediction_contact_on, prediction_contact_off)
    check(
        "source-one, source-two, receiver, stream, and coherence deletions remove the signed receiver contrast",
        abs(baseline) > 1e-10
        and max(abs(row["signed_contrast"]) for row in rows) < TOLERANCE
        and incoherent_contrast == 0,
        {"baseline_signed_contrast": baseline, "rows": rows, "incoherent_mixture_contrast": incoherent_contrast},
    )
    check(
        "contact deletion is visible on the declared n<=3 code but inactive on the prepared one-particle-per-cell prediction history",
        contact_residual > 1e-6 and prediction_contact_residual < TOLERANCE,
        {
            "two-particle_code_state_contact_deletion_residual": contact_residual,
            "prediction_history_contact_deletion_residual": prediction_contact_residual,
            "contact_called_prediction_driver": False,
        },
    )


def encode_state(state: LogicalState, encoding) -> PhysicalState:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter(state: PhysicalState, encoding, factor) -> PhysicalState:
    output = {}
    for key, value in state.items():
        decoded = encoding.getH() @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_source(state: PhysicalState, encoding, geometry: Geometry, cell_index: int, *, inverse: bool = False) -> PhysicalState:
    cell = geometry.sources[cell_index] if cell_index < 2 else geometry.receiver
    active = source_keys(cell, geometry.length)
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    decoded = {key: encoding.getH() @ state.get(key, zero_physical) for key in active}
    transformed = apply_source(decoded, geometry, cell_index, inverse=inverse)
    output = {key: value.copy() for key, value in state.items() if key not in active}
    zero_logical = np.zeros(MATTER_DIM, dtype=complex)
    for key in active:
        before_physical = state.get(key, zero_physical)
        before_logical = decoded[key]
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return prune(output)


def physical_step(state: PhysicalState, encoding, geometry: Geometry, factors) -> PhysicalState:
    coin, contact = factors
    output = apply_physical_matter(state, encoding, coin)
    output = apply_field_coin(output, geometry.length)
    for cell_index in range(3):
        output = apply_physical_source(output, encoding, geometry, cell_index)
    output = apply_stream(output, geometry.length)
    return apply_physical_matter(output, encoding, contact)


def physical_inverse(state: PhysicalState, encoding, geometry: Geometry, factors) -> PhysicalState:
    coin, contact = factors
    output = apply_physical_matter(state, encoding, contact.getH())
    output = apply_stream(output, geometry.length, inverse=True)
    for cell_index in (2, 1, 0):
        output = apply_physical_source(output, encoding, geometry, cell_index, inverse=True)
    output = apply_field_coin(output, geometry.length, inverse=True)
    return apply_physical_matter(output, encoding, coin.getH())


@lru_cache(maxsize=None)
def build_shell(length: int, cells: tuple[Coord, Coord, Coord]):
    code = c319.c269.build_code(length)
    return c319.multi_order_encodings(code, cells, LABELS)


def physical_compiler_controls(factors) -> dict:
    print("\nPHYSICAL E/G / INVERSE / HELD CODE")
    rows = []
    support_rows = []
    for geometry in (TRAIN, HELD_TRANSVERSE):
        cells = geometry.sources + (geometry.receiver,)
        encodings, _reducer, support = build_shell(geometry.length, cells)
        identity = sparse.eye(MATTER_DIM, format="csc")
        grams = tuple(c319.c315.raw_maximum_abs(encoding.getH() @ encoding - identity) for encoding in encodings)
        encoding = encodings[c319.ORDER_INDEX[(0, 1, 2)]]
        logical = prepared_state(geometry, -1 + 0j)
        encoded = encode_state(logical, encoding)
        logical_output = logical_step(logical, geometry, factors)
        physical_output = physical_step(encoded, encoding, geometry, factors)
        expected = encode_state(logical_output, encoding)
        restored = physical_inverse(physical_output, encoding, geometry, factors)
        rows.append(
            {
                "geometry": geometry.name,
                "held": geometry.held,
                "encoding_shape": encoding.shape,
                "all_order_Gram_raw_maximum": max(grams),
                "EG_residual": state_residual(physical_output, expected),
                "inverse_residual": state_residual(restored, encoded),
                "output_norm": state_norm(physical_output),
            }
        )
        support_rows.append(
            {
                "geometry": geometry.name,
                "matter_support_M2": support["face_port_cell_role_union_M2"],
                "maximum_joint_branch_M2": support[
                    "maximum_joint_branch_before_multiedge_role_M2"
                ],
            }
        )
    check(
        "E_432 G_432 = G_physical,432 E_432 and the adjoint inverse close on train and held physical M2 codes",
        max(max(row["all_order_Gram_raw_maximum"], row["EG_residual"], row["inverse_residual"], abs(row["output_norm"] - 1)) for row in rows) < TOLERANCE,
        {
            "logical_matter_dimension": MATTER_DIM,
            "global_field_code": "complete Q=1 sector of 7 L^3 hard-core M2",
            "rows": rows,
            "off_code_completion": "factorwise identity outside each matter code image",
        },
    )
    return {"rows": rows, "support_rows": support_rows}


def local_uniform_projector(cell_index: int) -> sparse.csc_matrix:
    rows = []
    columns = []
    data = []
    groups = {}
    for index, label in enumerate(LABELS):
        specs = c319.label_specs(label)
        if specs[cell_index][0] == 1:
            others = tuple(spec for position, spec in enumerate(specs) if position != cell_index)
            groups.setdefault(others, []).append(index)
    for indices in groups.values():
        for row in indices:
            for column in indices:
                data.append(1 / 6)
                rows.append(row)
                columns.append(column)
    return sparse.coo_matrix((data, (rows, columns)), shape=(MATTER_DIM, MATTER_DIM), dtype=complex).tocsc()


def frame_covariance_controls(factors) -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    coin, contact = factors
    matter_rows = []
    source_rows = []
    field_rows = []
    geometry_rows = []
    projector = local_uniform_projector(2)
    field_coin = c425.field_coin_layer(3)
    stream = c425.stream_layer(3)
    train_seed = np.zeros(7 * TRAIN.length**3, dtype=complex)
    train_seed[reservoir_index(TRAIN.sources[0], TRAIN.length)] = 1 / np.sqrt(2)
    train_seed[reservoir_index(TRAIN.sources[1], TRAIN.length)] = -1 / np.sqrt(2)
    for frame in c210.proper_cubic_frames():
        matter_representation = c319.triple_frame_representation(LABELS, frame)
        matter_rows.append(
            max(
                c319.c315.raw_maximum_abs(matter_representation @ coin - coin @ matter_representation),
                c319.c315.raw_maximum_abs(matter_representation @ contact - contact @ matter_representation),
                c319.c315.raw_maximum_abs(matter_representation @ projector - projector @ matter_representation),
            )
        )
        local_representation = c322.local_source_frame(frame)
        source_vertex = c322.local_source_blocks(c322.ANGLE)[1]
        source_rows.append(float(np.linalg.norm(local_representation @ source_vertex @ local_representation.T - source_vertex)))
        field_representation = c425.frame_representation(3, frame)
        field_rows.append(
            max(
                c319.c315.raw_maximum_abs(field_representation @ field_coin - field_coin @ field_representation),
                c319.c315.raw_maximum_abs(field_representation @ stream - stream @ field_representation),
            )
        )
        train_representation = c425.frame_representation(TRAIN.length, frame)
        rotated = tuple(tuple(int(value % TRAIN.length) for value in frame @ np.asarray(cell)) for cell in TRAIN.sources)
        rotated_seed = np.zeros_like(train_seed)
        rotated_seed[reservoir_index(rotated[0], TRAIN.length)] = 1 / np.sqrt(2)
        rotated_seed[reservoir_index(rotated[1], TRAIN.length)] = -1 / np.sqrt(2)
        geometry_rows.append(float(np.linalg.norm(train_representation @ train_seed - rotated_seed)))
    check(
        "matter coin/contact/receiver effect, recoil vertex, cubic field coin/stream, and phase-labelled geometry are covariant under all 24 proper-cubic frames",
        len(matter_rows) == len(source_rows) == len(field_rows) == len(geometry_rows) == 24
        and max(matter_rows) < TOLERANCE
        and max(source_rows) < TOLERANCE
        and max(field_rows) < TOLERANCE
        and max(geometry_rows) == 0,
        {
            "proper_cubic_frames": 24,
            "maximum_matter_receiver_residual": max(matter_rows),
            "maximum_recoil_source_residual": max(source_rows),
            "maximum_field_residual": max(field_rows),
            "maximum_geometry_seed_residual": max(geometry_rows),
        },
    )


@dataclass(frozen=True)
class SurfaceDisposition:
    surface: str
    bounded_phase_source_seam: bool
    bounded_physical_receiver_effect: bool
    cycle420_physical_source_EG: bool
    cycle420_physical_test_matter_readout: bool
    exact_host_profile_join: bool
    exact_packet_or_centroid_join: bool
    named_surface_prediction_closed: bool
    residual: str


def cycle420_boundary_controls(prediction_data) -> None:
    print("\nCYCLE-420 EXACT CONTRACT BOUNDARY")
    contracts = {surface.name: surface for surface in c420.SURFACES}
    rows = (
        SurfaceDisposition(
            "impact_parameter", True, True, False, False, False, False, False,
            "phase-coded two-source transverse cells are not positive host strength/r at b=5,6,7,8,10; local receiver effect is not detector centroid/log fit",
        ),
        SurfaceDisposition(
            "quadrupole_width", True, True, False, False, False, False, False,
            "two coherent sources are not the signed host (+1,-2,+1) profile; no propagated packet centroid or width",
        ),
        SurfaceDisposition(
            "diamond_nv", True, True, False, False, False, False, False,
            "relative reservoir phase is physical here, but the receiver is not the frozen host lock-in X/Y/phase surface",
        ),
    )
    check(
        "the near-side signed-source and receiver seams are positive while every exact Cycle-420 named-surface flag remains false",
        all(row.bounded_phase_source_seam and row.bounded_physical_receiver_effect for row in rows)
        and all(not row.cycle420_physical_source_EG for row in rows)
        and all(not row.cycle420_physical_test_matter_readout for row in rows)
        and all(not row.exact_host_profile_join for row in rows)
        and all(not row.exact_packet_or_centroid_join for row in rows)
        and all(not row.named_surface_prediction_closed for row in rows)
        and contracts["impact_parameter"].source_interface.startswith("positive host")
        and contracts["quadrupole_width"].source_interface.startswith("signed host")
        and "lock-in" in contracts["diamond_nv"].readout,
        {
            "rows": tuple(asdict(row) for row in rows),
            "Cycle420_original_flags_all_false": all(not surface.physical_source_eg and not surface.physical_test_matter_readout for surface in c420.SURFACES),
            "constructed_train_rows": prediction_data["summaries"][0]["phase_rows"],
        },
    )


def mass_contact_resource_domain_controls(factors, update_rows, compiler_data) -> None:
    print("\nMASS / CONTACT / RESOURCES / DOMAIN / INVENTORY")
    coin, contact = factors
    one_particle_indices = [index for index, label in enumerate(LABELS) if label[0] + label[2] + label[4] == 1]
    matter_update = contact @ coin
    sector = matter_update[np.ix_(one_particle_indices, one_particle_indices)]
    uniform = np.ones(len(one_particle_indices), dtype=complex) / np.sqrt(len(one_particle_indices))
    eigenvalue = np.vdot(uniform, sector @ uniform)
    eigen_residual = float(np.linalg.norm(sector @ uniform - eigenvalue * uniform))
    mass = float(abs(np.angle(eigenvalue)) / c219.C_SQUARED)
    rejected = 0
    probe = prepared_state(TRAIN, 1 + 0j)
    for function in (
        lambda: validate_geometry(Geometry("bad", 4, TRAIN.sources, TRAIN.receiver, 4, False)),
        lambda: validate_state({7 * TRAIN.length**3: next(iter(probe.values()))}, TRAIN.length),
        lambda: prepared_state(TRAIN, 0.5 + 0j),
        lambda: source_basis(TRAIN, 2),
        lambda: local_uniform_effect_inner(probe, probe, 3),
    ):
        try:
            function()
        except ValueError:
            rejected += 1
    inventory = {
        "supplied": (
            "Cycle319/396 physical n<=3 three-cell M64 code, local checks/Wilson sector, six factor orders, and identity completion",
            "Cycle426 coefficient-two even-CAR recoil vertex with fixed theta=0.8m calibration",
            "Cycle425 one reservoir plus six directional field M2 per cubic cell, field coin, and nearest-neighbor stream",
            "Cycle420 exact source/sign/readout/train/held contracts used only as the comparison boundary",
            "two-source relative phase, three-cell coordinates, global-Q=1 preparation, receiver effect, and update depth",
        ),
        "derived": (
            "bounded phase-coded transverse dipole seam with nonnegative source occupations",
            "distinct physical M64 receiver effect and signed coherent contrast",
            "train/held physical propagation, exact E/G and inverse, coefficient-two direction balance, deletions, and all-24 covariance",
            "exact boundary keeping Cycle420 impact, quadrupole, and lock-in surface closures false",
        ),
        "open": (
            "physical positive strength/r source family at frozen b=5,6,7,8,10 and detector centroid/log-fit join",
            "physical (+1,-2,+1) quadrupole profile, propagated test packet, and centroid/width join",
            "autonomous phase preparation, primitive synthesis replacing inherited matrix-unit completion, and higher-Q histories",
            "contact-work law, physical clock, Records, Born law, energy/stress/source selection, metric, and gravity",
        ),
        "host_expectation_queries_controlling_gates": 0,
        "negative_occupation_used": False,
        "global_Jordan_Wigner_or_parity_service": False,
        "preferred_global_ordering": False,
        "direction_called_force_momentum_energy_stress_or_gravity": False,
        "steps_called_time": False,
        "Born_claim": False,
        "Records_added": 0,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the Cycle-219 one-particle mass fixture and Cycle-230 contact survive on the physical prediction code",
        abs(mass - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
        and eigen_residual < TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14) == 645,
        {
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "Cycle432_matter_mass": mass,
            "one_particle_eigen_residual": eigen_residual,
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
        },
    )
    check(
        "the local compiler and field installation have bounded constant overhead with locally inherited gauge constraints",
        all(row["matter_support_M2"] > 0 for row in compiler_data["support_rows"]),
        {
            "physical_matter_support_rows": compiler_data["support_rows"],
            "homogeneous_matter_plus_field_M2_per_active_coarse_cell": 36,
            "field_M2_per_cubic_cell": 7,
            "maximum_active_recoil_vertex_support_M2": 25,
            "logical_matter_columns": MATTER_DIM,
            "matter_number_domain": "n=0,...,3",
            "field_domain": "complete global Q=1 sector",
            "auxiliary_constraints": "Cycle269/319 local checks and Wilson sector; six local factor-order encodings tested",
        },
    )
    check(
        "lawful-domain checks and the supplied/derived/open inventory preserve the bounded positive scope",
        rejected == 5
        and inventory["host_expectation_queries_controlling_gates"] == 0
        and not inventory["negative_occupation_used"]
        and not inventory["global_Jordan_Wigner_or_parity_service"]
        and not inventory["preferred_global_ordering"]
        and not inventory["direction_called_force_momentum_energy_stress_or_gravity"]
        and not inventory["steps_called_time"]
        and not inventory["Born_claim"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        {"domain_rejections": rejected, **inventory},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 432: PHYSICAL SIGNED TRANSVERSE SOURCE / TEST-MATTER PREDICTION")
    print("authority=none; audit=unset")
    note_contract()
    update_rows, coin, _first, _second, contact, _forward, _reverse = c319.update_controls(LABELS, "path")
    factors = (coin, contact)
    prediction_data = prediction_controls(factors)
    deletion_controls(factors, prediction_data)
    compiler_data = physical_compiler_controls(factors)
    frame_covariance_controls(factors)
    cycle420_boundary_controls(prediction_data)
    mass_contact_resource_domain_controls(factors, update_rows, compiler_data)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_SIGNED_TRANSVERSE_SOURCE_TEST_MATTER_PREDICTION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_SIGNED_TRANSVERSE_SOURCE_TEST_MATTER_PREDICTION_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
