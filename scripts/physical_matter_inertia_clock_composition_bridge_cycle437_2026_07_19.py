#!/usr/bin/env python3
"""Cycle 437: bounded physical matter/inertia-to-clock composition bridge.

Compose the Cycle-311 physical M64 one-particle rest ray and Cycle-219 free
coin with the Cycle-428 physical sixteen-M2 one-hot oscillator and reversible
latch.  Two supplied, unselected calibrations convert the same rest-sector
phase data into a bounded Ramsey response: a principal-phase coordinate and
the Cycle-220/221 Cayley-unwrapped coordinate.  They agree on three unaliased
training sectors and make different held alias-sector clock-word predictions.

The oscillator sweep and the mass-to-clock calibration are separate physical
factors.  Eigenphase, generator, circuit layer, and update count are not time,
rate, duration, or energy.  A reversible latch is not a Record.  No common
lapse, source law, passive trajectory, proper time, or inertia-law selection
is claimed.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_detector_record_clock_map_candidate_cycle428_2026_07_19 as c428
import operator_mass_equivalence_cycle221_2026_07_17 as c221


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MATTER_INERTIA_CLOCK_COMPOSITION_BRIDGE_CYCLE437_NOTE_2026-07-19.md"
)
SOURCES = {
    "cycle204": ROOT / "docs/work_history/repo/review_feedback/REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md",
    "cycle219": ROOT / "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md",
    "cycle221": ROOT / "docs/work_history/repo/review_feedback/OPERATOR_MASS_EQUIVALENCE_CYCLE221_NOTE_2026-07-17.md",
    "cycle319": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_THREE_CELL_MULTIEDGE_CYCLE319_NOTE_2026-07-18.md",
    "cycle396": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_MIDDLE_THREE_CELL_SOURCE_COMPILER_CYCLE396_NOTE_2026-07-18.md",
    "cycle426": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CYCLE426_NOTE_2026-07-19.md",
    "cycle428": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_DETECTOR_RECORD_CLOCK_MAP_CANDIDATE_CYCLE428_NOTE_2026-07-19.md",
    "cycle431": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CLOCK_RESPONSE_LAW_TOURNAMENT_CYCLE431_NOTE_2026-07-19.md",
}

AUTHORITY = "none"
AUDIT = "unset"
TRAIN_LENGTH = 4
HELD_LENGTH = 6
CLOCK_SCALE = 8.0
INITIAL_CLOCK_POSITION = 2
BRIGHT_POSITION = 3
DARK_POSITION = 4
EVENT_IDENTITY = 7
TOL = 8.0e-11
PASS = 0
FAIL = 0

LogicalState = dict[c428.LatchState, complex]
PhysicalState = dict[c428.LatchState, np.ndarray]


@dataclass(frozen=True)
class Law:
    name: str


PRINCIPAL = Law("principal-phase")
CAYLEY = Law("cayley-unwrapped")
LAWS = (PRINCIPAL, CAYLEY)


@dataclass(frozen=True)
class Fixture:
    name: str
    beta: float
    length: int
    held: bool


TRAIN_BETAS = (-2 * np.pi / 9, -4 * np.pi / 9, -2 * np.pi / 3)
HELD_BETA = -8 * np.pi / 9
FIXTURES = tuple(
    Fixture(f"train-sector-{index + 1}", beta, TRAIN_LENGTH, False)
    for index, beta in enumerate(TRAIN_BETAS)
) + (Fixture("held-alias-sector-4", HELD_BETA, HELD_LENGTH, True),)
MASS_FIXTURE_BETA = -0.3


@dataclass
class MatterCode:
    length: int
    encoder: object
    basis: tuple
    flagged: np.ndarray
    exchange: np.ndarray
    constrained: np.ndarray
    constraint: np.ndarray
    rest_seam: np.ndarray
    rest_physical: np.ndarray
    matter_union_m2: int
    maximum_branch_support_m2: int


@dataclass
class MatterLaw:
    fixture: Fixture
    species: object
    code: MatterCode
    logical_coin: np.ndarray
    physical_coin: np.ndarray
    old_coin: np.ndarray
    rest_eigenvalue: complex
    principal_mass: float
    cayley_mass: float


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
        "positive bounded physical composition",
        "cycle-311 physical m64 one-particle rest ray",
        "cycle-428 sixteen-m2 one-hot oscillator",
        "locally enforced role-gauge constraint",
        "principal-phase calibration",
        "cayley-unwrapped calibration",
        "three unaliased training sectors",
        "held alias sector",
        "same physical code and no refit",
        "one- and two-application predictions",
        "exact e/g and inverse",
        "all 24 proper-cubic frames",
        "bounded support",
        "matter, calibration, oscillator, ramsey, and latch deletions",
        "leakage and lawful-domain controls",
        "oscillator sweep is distinct from the supplied chi calibration",
        "a/g = m_passive / m_inertial",
        "common-lapse, source, and trajectory flags remain false",
        "eigenphase, generator, circuit layer, and update count are not time, rate, duration, or energy",
        "reversible latch is not a record",
        "no proper time or inertia-law selection",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-437 note freezes the physical join and interpretation boundary", not missing, missing)

    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the cited science stack exposes the exact mass/clock target without importing an audit verdict",
        all(path.is_file() for path in SOURCES.values())
        and "acceleration / gravitational_gradient = m_passive / m_inertial" in source["cycle204"]
        and "one-parameter family is not one generated spectrum" in source["cycle219"]
        and "principal-phase alias" in source["cycle221"]
        and "supplied additive composition" in source["cycle221"]
        and "uniform one-particle state retains mass" in source["cycle319"]
        and "cycle-219 mass fixture" in source["cycle396"]
        and "one-particle mass fixture remains" in source["cycle426"]
        and "sixteen-m2 one-hot oscillator" in source["cycle428"]
        and "eigenphase is not time or a rate" in source["cycle431"],
        {
            "target_surface": "Cycle204 conditional a/g=M_passive/M_inertial",
            "physical_near_side": "Cycle311 M64 rest ray -> Cycle428 oscillator/latch",
            "selected_clock_or_inertia_law": False,
        },
    )


def build_matter_code(length: int) -> MatterCode:
    if length not in (TRAIN_LENGTH, HELD_LENGTH):
        raise ValueError("Cycle437 declares only L4 training and held L6")
    code = c311.c269.build_code(length)
    encoder = c311.common_encoder(code)
    basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    constrained = c311.constrained_encoding(flagged, exchange)
    constraint = c311.role_constraint(exchange)
    rest_fock = np.zeros(c311.FOCK_DIMENSION, dtype=complex)
    for direction in range(6):
        rest_fock[c311.FOCK_INDEX[(1, (direction,))]] = 1 / np.sqrt(6)
    rest_seam = c311.fock_input_embedding() @ rest_fock
    rest_physical = constrained @ rest_seam
    union = 0
    maximum = 0
    for branch in basis:
        for role in (0, 1):
            representative = c311.branch_representative(code, encoder.body, branch, role)
            support = representative.x | representative.z
            union |= support
            maximum = max(maximum, support.bit_count())
    return MatterCode(
        length,
        encoder,
        basis,
        flagged,
        exchange,
        constrained,
        constraint,
        rest_seam,
        rest_physical,
        union.bit_count(),
        maximum,
    )


def build_matter_law(item: Fixture, code: MatterCode) -> MatterLaw:
    if item.length != code.length or item not in FIXTURES:
        raise ValueError("fixture is outside the frozen train/held family")
    species = c311.c219.common_species(item.beta)
    logical_coin = c311.logical_coin(species.coin)
    physical_coin, old_coin = c311.physical_coin(
        code.flagged, logical_coin, code.exchange
    )
    eigenvalue = complex(np.vdot(code.rest_seam, logical_coin @ code.rest_seam))
    principal_mass = 3 * float(np.angle(eigenvalue))
    cayley_mass = float(species.analytic_mass)
    return MatterLaw(
        item,
        species,
        code,
        logical_coin,
        physical_coin,
        old_coin,
        eigenvalue,
        principal_mass,
        cayley_mass,
    )


def calibration_coordinate(matter: MatterLaw, law: Law) -> float:
    if law == PRINCIPAL:
        return matter.principal_mass
    if law == CAYLEY:
        return matter.cayley_mass
    raise ValueError("unknown mass-to-clock calibration law")


def calibration_angle(matter: MatterLaw, law: Law, applications: int) -> float:
    if applications not in (1, 2):
        raise ValueError("declared calibration applications are one or two")
    return applications * calibration_coordinate(matter, law) / CLOCK_SCALE


def blank_key(position: int, event_identity: int = EVENT_IDENTITY) -> c428.LatchState:
    if not 0 < event_identity < 1 << c428.EVENT_BITS:
        raise ValueError("Cycle437 requires one nonzero four-M2 calibration identity")
    return c428.blank_latch(
        1, c428.one_hot(position), c428.bits(event_identity, c428.EVENT_BITS)
    )


def validate_blank_input(key: c428.LatchState) -> None:
    c428.clock_position(key.clock)
    if (
        key.detector != 1
        or any(key.bus)
        or any(key.latched_clock)
        or any(key.latched_identity)
        or key.valid != 0
        or c428.integer(key.event_identity) != EVENT_IDENTITY
    ):
        raise ValueError("input must use the frozen blank Cycle437 latch preparation")


def add_logical(output: LogicalState, key: c428.LatchState, value: complex) -> None:
    output[key] = output.get(key, 0j) + value


def add_physical(output: PhysicalState, key: c428.LatchState, value: np.ndarray) -> None:
    if key in output:
        output[key] = output[key] + value
    else:
        output[key] = value.copy()


def logical_norm(state: LogicalState) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def physical_norm(state: PhysicalState) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def logical_residual(left: LogicalState, right: LogicalState) -> float:
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def physical_residual(left: PhysicalState, right: PhysicalState) -> float:
    keys = set(left) | set(right)
    zero = np.zeros(0, dtype=complex)
    total = 0.0
    for key in keys:
        if key in left:
            lvalue = left[key]
            rvalue = right.get(key, np.zeros_like(lvalue))
        else:
            rvalue = right[key]
            lvalue = np.zeros_like(rvalue)
        if len(lvalue) == 0 or len(rvalue) == 0:
            raise RuntimeError(zero)
        total += float(np.linalg.norm(lvalue - rvalue) ** 2)
    return float(np.sqrt(total))


def encode_state(state: LogicalState, matter: MatterLaw) -> PhysicalState:
    return {
        key: value * matter.code.rest_physical
        for key, value in state.items()
    }


def apply_clock_sweep_logical(state: LogicalState, *, inverse: bool = False) -> LogicalState:
    operation = c428.clock_inverse if inverse else c428.clock_forward
    output: LogicalState = {}
    for key, value in state.items():
        moved = replace(key, clock=operation(key.clock))
        add_logical(output, moved, value)
    return output


def apply_clock_sweep_physical(state: PhysicalState, *, inverse: bool = False) -> PhysicalState:
    operation = c428.clock_inverse if inverse else c428.clock_forward
    output: PhysicalState = {}
    for key, value in state.items():
        moved = replace(key, clock=operation(key.clock))
        add_physical(output, moved, value)
    return output


def beam_targets(position: int) -> tuple[tuple[int, complex], ...]:
    if position == BRIGHT_POSITION:
        return (
            (BRIGHT_POSITION, 1 / np.sqrt(2)),
            (DARK_POSITION, 1 / np.sqrt(2)),
        )
    if position == DARK_POSITION:
        return (
            (BRIGHT_POSITION, 1 / np.sqrt(2)),
            (DARK_POSITION, -1 / np.sqrt(2)),
        )
    return ((position, 1 + 0j),)


def apply_beam_logical(state: LogicalState) -> LogicalState:
    output: LogicalState = {}
    for key, value in state.items():
        position = c428.clock_position(key.clock)
        for target, coefficient in beam_targets(position):
            add_logical(
                output,
                replace(key, clock=c428.one_hot(target)),
                coefficient * value,
            )
    return output


def apply_beam_physical(state: PhysicalState) -> PhysicalState:
    output: PhysicalState = {}
    for key, value in state.items():
        position = c428.clock_position(key.clock)
        for target, coefficient in beam_targets(position):
            add_physical(
                output,
                replace(key, clock=c428.one_hot(target)),
                coefficient * value,
            )
    return output


def apply_calibration_logical(
    state: LogicalState,
    matter: MatterLaw,
    law: Law,
    applications: int,
    *,
    inverse: bool = False,
    deleted: bool = False,
) -> LogicalState:
    phase = 1 + 0j if deleted else np.exp(
        (-1j if inverse else 1j) * calibration_angle(matter, law, applications)
    )
    output: LogicalState = {}
    for key, value in state.items():
        multiplier = phase if c428.clock_position(key.clock) == DARK_POSITION else 1
        add_logical(output, key, multiplier * value)
    return output


def apply_calibration_physical(
    state: PhysicalState,
    matter: MatterLaw,
    law: Law,
    applications: int,
    *,
    inverse: bool = False,
    deleted: bool = False,
) -> PhysicalState:
    phase = 1 + 0j if deleted else np.exp(
        (-1j if inverse else 1j) * calibration_angle(matter, law, applications)
    )
    rest = matter.code.rest_physical
    output: PhysicalState = {}
    for key, value in state.items():
        if c428.clock_position(key.clock) == DARK_POSITION:
            moved = value + (phase - 1) * rest * np.vdot(rest, value)
        else:
            moved = value
        add_physical(output, key, moved)
    return output


def apply_matter_logical(
    state: LogicalState, matter: MatterLaw, *, inverse: bool = False, deleted: bool = False
) -> LogicalState:
    phase = 1 + 0j if deleted else (
        np.conjugate(matter.rest_eigenvalue) if inverse else matter.rest_eigenvalue
    )
    return {key: phase * value for key, value in state.items()}


def apply_matter_physical(
    state: PhysicalState, matter: MatterLaw, *, inverse: bool = False, deleted: bool = False
) -> PhysicalState:
    if deleted:
        return {key: value.copy() for key, value in state.items()}
    operator = matter.physical_coin.conj().T if inverse else matter.physical_coin
    return {key: operator @ value for key, value in state.items()}


def apply_latch_logical(
    state: LogicalState, *, inverse: bool = False, deleted_gate: str | None = None
) -> LogicalState:
    operation = c428.invert_latch if inverse else c428.apply_latch
    output: LogicalState = {}
    for key, value in state.items():
        add_logical(output, operation(key, deleted_gate=deleted_gate), value)
    return output


def apply_latch_physical(
    state: PhysicalState, *, inverse: bool = False, deleted_gate: str | None = None
) -> PhysicalState:
    operation = c428.invert_latch if inverse else c428.apply_latch
    output: PhysicalState = {}
    for key, value in state.items():
        add_physical(output, operation(key, deleted_gate=deleted_gate), value)
    return output


def logical_forward(
    state: LogicalState,
    matter: MatterLaw,
    law: Law,
    applications: int,
    *,
    delete_matter: bool = False,
    delete_calibration: bool = False,
    delete_oscillator: bool = False,
    delete_first_ramsey: bool = False,
    delete_second_ramsey: bool = False,
    delete_latch: bool = False,
    deleted_latch_gate: str | None = None,
) -> LogicalState:
    output = apply_matter_logical(state, matter, deleted=delete_matter)
    if not delete_oscillator:
        output = apply_clock_sweep_logical(output)
    if not delete_first_ramsey:
        output = apply_beam_logical(output)
    output = apply_calibration_logical(
        output, matter, law, applications, deleted=delete_calibration
    )
    if not delete_second_ramsey:
        output = apply_beam_logical(output)
    if not delete_latch:
        output = apply_latch_logical(output, deleted_gate=deleted_latch_gate)
    return output


def physical_forward(
    state: PhysicalState,
    matter: MatterLaw,
    law: Law,
    applications: int,
    *,
    delete_matter: bool = False,
    delete_calibration: bool = False,
    delete_oscillator: bool = False,
    delete_first_ramsey: bool = False,
    delete_second_ramsey: bool = False,
    delete_latch: bool = False,
    deleted_latch_gate: str | None = None,
) -> PhysicalState:
    output = apply_matter_physical(state, matter, deleted=delete_matter)
    if not delete_oscillator:
        output = apply_clock_sweep_physical(output)
    if not delete_first_ramsey:
        output = apply_beam_physical(output)
    output = apply_calibration_physical(
        output, matter, law, applications, deleted=delete_calibration
    )
    if not delete_second_ramsey:
        output = apply_beam_physical(output)
    if not delete_latch:
        output = apply_latch_physical(output, deleted_gate=deleted_latch_gate)
    return output


def logical_inverse(
    state: LogicalState, matter: MatterLaw, law: Law, applications: int
) -> LogicalState:
    output = apply_latch_logical(state, inverse=True)
    output = apply_beam_logical(output)
    output = apply_calibration_logical(
        output, matter, law, applications, inverse=True
    )
    output = apply_beam_logical(output)
    output = apply_clock_sweep_logical(output, inverse=True)
    return apply_matter_logical(output, matter, inverse=True)


def physical_inverse(
    state: PhysicalState, matter: MatterLaw, law: Law, applications: int
) -> PhysicalState:
    output = apply_latch_physical(state, inverse=True)
    output = apply_beam_physical(output)
    output = apply_calibration_physical(
        output, matter, law, applications, inverse=True
    )
    output = apply_beam_physical(output)
    output = apply_clock_sweep_physical(output, inverse=True)
    return apply_matter_physical(output, matter, inverse=True)


def clock_weights_logical(state: LogicalState) -> dict[int, float]:
    weights = {position: 0.0 for position in range(c428.CLOCK_BITS)}
    for key, value in state.items():
        weights[c428.clock_position(key.clock)] += abs(value) ** 2
    return weights


def clock_weights_physical(state: PhysicalState) -> dict[int, float]:
    weights = {position: 0.0 for position in range(c428.CLOCK_BITS)}
    for key, value in state.items():
        weights[c428.clock_position(key.clock)] += float(np.vdot(value, value).real)
    return weights


def latch_failures(state: PhysicalState) -> tuple[int, int]:
    decode = 0
    dirty_bus = 0
    for key in state:
        decode += c428.decoded_latch(key) is None
        dirty_bus += any(key.bus)
    return decode, dirty_bus


def leakage(state: PhysicalState, rest: np.ndarray) -> float:
    total = 0.0
    for value in state.values():
        outside = value - rest * np.vdot(rest, value)
        total += float(np.linalg.norm(outside) ** 2)
    return float(np.sqrt(total))


def mass_fixture_and_code_controls(codes: dict[int, MatterCode]) -> None:
    print("\nPHYSICAL M64 REST FIXTURE / LOCAL ROLE GAUGE")
    rows = []
    for length, code in codes.items():
        item = Fixture("canonical-mass-control", MASS_FIXTURE_BETA, length, length == HELD_LENGTH)
        species = c311.c219.common_species(item.beta)
        logical_coin = c311.logical_coin(species.coin)
        physical_coin, _old = c311.physical_coin(code.flagged, logical_coin, code.exchange)
        eigenvalue = complex(np.vdot(code.rest_seam, logical_coin @ code.rest_seam))
        physical_res = float(
            np.linalg.norm(
                physical_coin @ code.rest_physical
                - code.constrained @ (logical_coin @ code.rest_seam)
            )
        )
        rows.append(
            {
                "L": length,
                "held": length == HELD_LENGTH,
                "physical_rest_Gram": abs(float(np.vdot(code.rest_physical, code.rest_physical).real) - 1),
                "physical_coin_EG_residual": physical_res,
                "principal_rest_mass": 3 * float(np.angle(eigenvalue)),
                "Cycle219_analytic_mass": float(species.analytic_mass),
                "rest_eigen_residual": float(
                    np.linalg.norm(logical_coin @ code.rest_seam - eigenvalue * code.rest_seam)
                ),
                "role_constraint_residual": float(
                    np.linalg.norm(code.constraint @ code.rest_physical - code.rest_physical)
                ),
                "matter_union_M2": code.matter_union_m2,
                "maximum_branch_support_M2": code.maximum_branch_support_m2,
            }
        )
    maximum = max(
        max(
            row["physical_rest_Gram"],
            row["physical_coin_EG_residual"],
            row["rest_eigen_residual"],
            row["role_constraint_residual"],
            abs(row["principal_rest_mass"] - row["Cycle219_analytic_mass"]),
        )
        for row in rows
    )
    check(
        "the physical M64 rest ray preserves the canonical Cycle-219 one-particle/free mass and local role gauge on train and held sizes",
        maximum < TOL and all(row["matter_union_M2"] == 44 for row in rows),
        {"rows": rows, "maximum_mass_code_residual": maximum},
    )


def eg_inverse_prediction_controls(matter_laws: tuple[MatterLaw, ...]) -> dict[str, object]:
    print("\nCOMMON-CODE E/G, INVERSE, AND ONE/TWO-APPLICATION PREDICTIONS")
    residual_rows = []
    predictions = []
    for matter in matter_laws:
        for law in LAWS:
            for applications in (1, 2):
                maximum_forward = maximum_logical_inverse = maximum_physical_inverse = 0.0
                maximum_norm = maximum_leakage = 0.0
                maximum_clock_hamming = maximum_decode = maximum_bus = 0
                for position in range(c428.CLOCK_BITS):
                    key = blank_key(position)
                    validate_blank_input(key)
                    logical = {key: 1 + 0j}
                    physical = encode_state(logical, matter)
                    logical_output = logical_forward(logical, matter, law, applications)
                    physical_output = physical_forward(physical, matter, law, applications)
                    expected = encode_state(logical_output, matter)
                    restored_logical = logical_inverse(logical_output, matter, law, applications)
                    restored_physical = physical_inverse(physical_output, matter, law, applications)
                    maximum_forward = max(maximum_forward, physical_residual(physical_output, expected))
                    maximum_logical_inverse = max(
                        maximum_logical_inverse, logical_residual(restored_logical, logical)
                    )
                    maximum_physical_inverse = max(
                        maximum_physical_inverse, physical_residual(restored_physical, physical)
                    )
                    maximum_norm = max(
                        maximum_norm,
                        abs(logical_norm(logical_output) - 1),
                        abs(physical_norm(physical_output) - 1),
                    )
                    maximum_leakage = max(
                        maximum_leakage,
                        leakage(physical_output, matter.code.rest_physical),
                    )
                    decoded, dirty = latch_failures(physical_output)
                    maximum_clock_hamming = max(
                        maximum_clock_hamming,
                        sum(int(sum(key.clock) != 1) for key in physical_output),
                    )
                    maximum_decode = max(maximum_decode, decoded)
                    maximum_bus = max(maximum_bus, dirty)
                residual_rows.append(
                    {
                        "fixture": matter.fixture.name,
                        "law": law.name,
                        "applications": applications,
                        "logical_columns": c428.CLOCK_BITS,
                        "forward_EG_residual": maximum_forward,
                        "logical_inverse_residual": maximum_logical_inverse,
                        "physical_inverse_residual": maximum_physical_inverse,
                        "norm_drift": maximum_norm,
                        "matter_code_leakage": maximum_leakage,
                        "clock_Hamming_failures": maximum_clock_hamming,
                        "latch_decode_failures": maximum_decode,
                        "blank_bus_failures": maximum_bus,
                    }
                )

                initial = {blank_key(INITIAL_CLOCK_POSITION): 1 + 0j}
                output = logical_forward(initial, matter, law, applications)
                weights = clock_weights_logical(output)
                chi = calibration_angle(matter, law, applications)
                predictions.append(
                    {
                        "fixture": matter.fixture.name,
                        "held": matter.fixture.held,
                        "beta": matter.fixture.beta,
                        "law": law.name,
                        "applications": applications,
                        "coordinate": calibration_coordinate(matter, law),
                        "chi": chi,
                        "bright_word": BRIGHT_POSITION,
                        "dark_word": DARK_POSITION,
                        "bright_weight": weights[BRIGHT_POSITION],
                        "dark_weight": weights[DARK_POSITION],
                        "analytic_dark_weight": float(np.sin(chi / 2) ** 2),
                    }
                )

    maximum = max(
        max(
            row["forward_EG_residual"],
            row["logical_inverse_residual"],
            row["physical_inverse_residual"],
            row["norm_drift"],
            row["matter_code_leakage"],
        )
        for row in residual_rows
    )
    training_pairs = {}
    held_pairs = {}
    for row in predictions:
        key = (row["fixture"], row["applications"])
        target = held_pairs if row["held"] else training_pairs
        target.setdefault(key, {})[row["law"]] = row
    training_difference = max(
        abs(pair[PRINCIPAL.name]["dark_weight"] - pair[CAYLEY.name]["dark_weight"])
        for pair in training_pairs.values()
    )
    held_difference = {
        applications: abs(
            held_pairs[("held-alias-sector-4", applications)][PRINCIPAL.name]["dark_weight"]
            - held_pairs[("held-alias-sector-4", applications)][CAYLEY.name]["dark_weight"]
        )
        for applications in (1, 2)
    }
    check(
        "both unselected calibrations exactly intertwine and invert on all clock words while agreeing on unaliased train sectors and separating the held alias",
        maximum < TOL
        and all(
            row["clock_Hamming_failures"]
            == row["latch_decode_failures"]
            == row["blank_bus_failures"]
            == 0
            for row in residual_rows
        )
        and training_difference < 2e-14
        and min(held_difference.values()) > 0.6
        and all(abs(row["dark_weight"] - row["analytic_dark_weight"]) < 3e-14 for row in predictions),
        {
            "declared_code": "Cycle311 physical M64 n=1 rest ray x complete Cycle428 Q_clock=1 x blank latch",
            "maximum_EG_inverse_norm_leakage_residual": maximum,
            "residual_rows": residual_rows,
            "prediction_rows": predictions,
            "maximum_training_law_difference": training_difference,
            "held_one_two_application_dark_weight_differences": held_difference,
        },
    )
    return {
        "predictions": predictions,
        "maximum_residual": maximum,
        "held_difference": held_difference,
    }


def covariance_and_support_controls(
    codes: dict[int, MatterCode], matter_laws: tuple[MatterLaw, ...]
) -> None:
    print("\nBOUNDED SUPPORT / ALL-24 PROPER-CUBIC COVARIANCE")
    frames = c311.c235.proper_cubic_frames()
    rest_covariance = []
    projector_covariance = []
    coin_covariance = []
    branch_failures = 0
    by_length = {length: [] for length in codes}
    for matter in matter_laws:
        by_length[matter.fixture.length].append(matter)
    for length, code in codes.items():
        reducer = c311.c305.StabilizerReducer(code.encoder.code)
        old_rest = code.flagged @ code.rest_seam
        for frame in frames:
            old_rep, failures = c311.flagged_frame_representation(
                code.encoder, code.basis, {}, frame, reducer
            )
            branch_failures += failures
            moved_rest = old_rep @ old_rest
            rest_covariance.append(float(np.linalg.norm(moved_rest - old_rest)))
            projector_covariance.append(
                float(
                    np.linalg.norm(
                        np.outer(moved_rest, moved_rest.conj())
                        - np.outer(old_rest, old_rest.conj())
                    )
                )
            )
            for matter in by_length[length]:
                coin_covariance.append(
                    float(np.linalg.norm(old_rep @ matter.old_coin @ old_rep.conj().T - matter.old_coin))
                )

    oscillator_primitives = tuple(
        c428.Primitive(f"oscillator-{left}", (c428.CLOCK_SITES[left], c428.CLOCK_SITES[right]))
        for left, right in c428.CLOCK_FORWARD_SWAPS
    )
    ramsey = c428.Primitive(
        "ramsey-beamsplitter",
        (c428.CLOCK_SITES[BRIGHT_POSITION], c428.CLOCK_SITES[DARK_POSITION]),
    )
    matter_interface = (DARK_POSITION, 1, 1)
    calibration_interface = c428.Primitive(
        "matter-clock-calibration-interface",
        (c428.CLOCK_SITES[DARK_POSITION], matter_interface),
    )
    primitives = oscillator_primitives + (ramsey, calibration_interface) + c428.LATCH_SCHEDULE
    layout_failures = 0
    for frame in c428.c255.proper_frames():
        for primitive in primitives:
            moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in primitive.support)
            distances = tuple(
                c428.c255.manhattan(left, right)
                for left in moved
                for right in moved
            )
            layout_failures += int(len(moved) != len(set(moved)))
            layout_failures += int(max(distances) > 2)
            if len(moved) == 3:
                layout_failures += int(
                    sum(c428.c255.manhattan(moved[index], moved[index + 1]) == 1 for index in range(2)) != 2
                )

    maximum_matter_union = max(code.matter_union_m2 for code in codes.values())
    maximum_compiled_control = maximum_matter_union + 1
    combined_installation = maximum_matter_union + c428.TOTAL_AUXILIARY_M2
    check(
        "the M64 rest projector, free coin, Ramsey pair, oscillator sweep, calibration interface, and latch form one bounded all-frame family",
        len(frames) == 24
        and branch_failures == layout_failures == 0
        and max(rest_covariance + projector_covariance + coin_covariance) < TOL
        and maximum_matter_union == 44
        and maximum_compiled_control == 45
        and combined_installation == 106,
        {
            "proper_cubic_frames": len(frames),
            "maximum_rest_ray_covariance": max(rest_covariance),
            "maximum_rest_projector_covariance": max(projector_covariance),
            "maximum_free_coin_covariance": max(coin_covariance),
            "frame_branch_failures": branch_failures,
            "clock_latch_layout_failures": layout_failures,
            "physical_M64_patch_union_M2": maximum_matter_union,
            "Cycle428_clock_latch_auxiliary_M2": c428.TOTAL_AUXILIARY_M2,
            "combined_bounded_installation_M2": combined_installation,
            "maximum_compiled_mass_clock_control_support_M2": maximum_compiled_control,
            "oscillator_and_Ramsey_primitive_support_M2": 2,
            "latch_primitive_support_M2": 3,
            "clock_latch_box": "22 x 3 x 1",
            "matter_clock_interface": (c428.CLOCK_SITES[DARK_POSITION], matter_interface),
            "primitive_sparse_synthesis_of_45_M2_projector_control": "supplied",
        },
    )


def deletion_leakage_domain_controls(matter_laws: tuple[MatterLaw, ...]) -> None:
    print("\nDELETIONS / LEAKAGE / LAWFUL DOMAIN")
    matter = next(item for item in matter_laws if item.fixture.name == "held-alias-sector-4")
    logical = {blank_key(INITIAL_CLOCK_POSITION): 1 + 0j}
    baseline = logical_forward(logical, matter, CAYLEY, 1)
    baseline_weights = clock_weights_logical(baseline)
    deleted = {
        "matter": logical_forward(logical, matter, CAYLEY, 1, delete_matter=True),
        "calibration": logical_forward(logical, matter, CAYLEY, 1, delete_calibration=True),
        "oscillator": logical_forward(logical, matter, CAYLEY, 1, delete_oscillator=True),
        "first_Ramsey": logical_forward(logical, matter, CAYLEY, 1, delete_first_ramsey=True),
        "second_Ramsey": logical_forward(logical, matter, CAYLEY, 1, delete_second_ramsey=True),
        "latch": logical_forward(logical, matter, CAYLEY, 1, delete_latch=True),
        "dark_word_copy": logical_forward(
            logical, matter, CAYLEY, 1, deleted_latch_gate=f"clock-copy-{DARK_POSITION}"
        ),
    }
    calibration_weights = clock_weights_logical(deleted["calibration"])
    oscillator_weights = clock_weights_logical(deleted["oscillator"])
    first_weights = clock_weights_logical(deleted["first_Ramsey"])
    second_weights = clock_weights_logical(deleted["second_Ramsey"])
    latch_valid_weight = sum(
        abs(value) ** 2 for key, value in deleted["latch"].items() if key.valid
    )
    dark_copy_invalid_weight = sum(
        abs(value) ** 2
        for key, value in deleted["dark_word_copy"].items()
        if c428.decoded_latch(key) is None
    )
    matter_residual = logical_residual(deleted["matter"], baseline)

    rest = matter.code.rest_physical
    deleted_rest = rest.copy()
    deletion_index = int(np.argmax(abs(deleted_rest)))
    deleted_amplitude = deleted_rest[deletion_index]
    deleted_rest[deletion_index] = 0
    deleted_gram = abs(float(np.vdot(deleted_rest, deleted_rest).real) - 1)
    deleted_constraint = float(
        np.linalg.norm(matter.code.constraint @ deleted_rest - deleted_rest)
    )

    rejections = 0
    for operation in (
        lambda: build_matter_code(3),
        lambda: calibration_coordinate(matter, Law("host-lookup")),
        lambda: calibration_angle(matter, CAYLEY, 3),
        lambda: blank_key(16),
        lambda: blank_key(2, 0),
        lambda: validate_blank_input(replace(blank_key(2), valid=1)),
    ):
        try:
            operation()
        except ValueError:
            rejections += 1

    check(
        "matter, calibration, oscillator, Ramsey, latch, encoding, gauge, and lawful-domain controls are independently visible",
        matter_residual > 0.1
        and calibration_weights[DARK_POSITION] < 2e-14
        and oscillator_weights[INITIAL_CLOCK_POSITION] > 0.2
        and abs(first_weights[DARK_POSITION] - 0.5) < 2e-14
        and abs(second_weights[DARK_POSITION] - 0.5) < 2e-14
        and latch_valid_weight == 0
        and dark_copy_invalid_weight > 0.7
        and abs(deleted_amplitude) > 0
        and deleted_gram > 1e-3
        and deleted_constraint > 1e-3
        and rejections == 6,
        {
            "baseline_dark_word_weight": baseline_weights[DARK_POSITION],
            "matter_free_factor_deletion_state_residual": matter_residual,
            "calibration_deleted_dark_word_weight": calibration_weights[DARK_POSITION],
            "oscillator_deleted_initial_word_weight": oscillator_weights[INITIAL_CLOCK_POSITION],
            "first_Ramsey_deleted_dark_word_weight": first_weights[DARK_POSITION],
            "second_Ramsey_deleted_dark_word_weight": second_weights[DARK_POSITION],
            "latch_deleted_valid_weight": latch_valid_weight,
            "dark_word_copy_deleted_invalid_weight": dark_copy_invalid_weight,
            "deleted_encoding_amplitude": deleted_amplitude,
            "deleted_encoding_Gram_residual": deleted_gram,
            "deleted_encoding_constraint_residual": deleted_constraint,
            "lawful_domain_rejections": rejections,
        },
    )


def cycle204_comparator_and_inventory(matter_laws: tuple[MatterLaw, ...]) -> None:
    print("\nCYCLE-204 TARGET COMPARATOR / SUPPLIED-DERIVED-OPEN INVENTORY")
    rows = []
    for matter in matter_laws:
        rows.append(
            {
                "fixture": matter.fixture.name,
                "held": matter.fixture.held,
                "assumed_candidate_M_inertial": matter.cayley_mass,
                "principal_candidate_M_passive": matter.principal_mass,
                "cayley_candidate_M_passive": matter.cayley_mass,
                "principal_conditional_a_over_g": matter.principal_mass / matter.cayley_mass,
                "cayley_conditional_a_over_g": 1.0,
                "common_lapse_applied": False,
                "passive_trajectory_evolved": False,
                "inertia_independently_measured_on_this_sector": False,
            }
        )
    training = [row for row in rows if not row["held"]]
    held = next(row for row in rows if row["held"])
    flags = {
        "Cycle204_physical_clock_calibration_candidates": True,
        "Cycle204_common_lapse": False,
        "Cycle204_active_source_map": False,
        "Cycle204_passive_force_or_trajectory": False,
        "Cycle204_end_to_end_a_over_g_prediction": False,
        "proper_time": False,
        "inertia_law_selected": False,
    }
    inventory = {
        "supplied": (
            "three unaliased beta populations and one held alias beta population",
            "principal versus Cayley coordinate formulas and CLOCK_SCALE=8",
            "one/two calibration applications, Ramsey arms, oscillator initial word, and factor order",
            "M64 reference/role preparation, matrix-unit completion, latch trigger, event identity, and blank sidecar",
            "the conditional Cycle204 identification M_passive=clock calibration coordinate",
        ),
        "derived": (
            "physical rest-ray/free-coin and role-gauge preservation",
            "exact physical E/G and inverse on complete one-hot clock code",
            "agreement on three unaliased sectors and held alias separation",
            "one/two-application complete latched-word weights",
            "bounded support, all-frame covariance, deletions, leakage, and lawful-domain rejection",
        ),
        "open": (
            "selection of principal or Cayley calibration and derivation of CLOCK_SCALE",
            "physical multiparticle/additive or deformed composition law",
            "common lapse, active source, passive force/trajectory, and end-to-end Cycle204 response",
            "clock unit, metric/proper time, autonomous recurrence, Record formation, occurrence, and empirical selection",
        ),
        "negative_claim": False,
        "axiom_pressure": False,
    }
    check(
        "the exact Cycle-204 a/g comparator is exposed while all common-lapse, source, trajectory, proper-time, and selection flags remain false",
        max(abs(row["principal_conditional_a_over_g"] - 1) for row in training) < 3e-14
        and held["principal_conditional_a_over_g"] < -0.1
        and held["cayley_conditional_a_over_g"] == 1
        and not any(value for key, value in flags.items() if key != "Cycle204_physical_clock_calibration_candidates")
        and flags["Cycle204_physical_clock_calibration_candidates"]
        and AUTHORITY == "none"
        and AUDIT == "unset",
        {
            "Cycle204_surface": "a/g = M_passive / M_inertial, conditional on common lapse",
            "rows": rows,
            "flags": flags,
            "inventory": inventory,
            "oscillator_sweep_is_chi_calibration": False,
            "eigenphase_or_generator_called_time_rate_duration_energy": False,
            "pointer_copy_called_Record": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> int:
    contracts()
    codes = {
        TRAIN_LENGTH: build_matter_code(TRAIN_LENGTH),
        HELD_LENGTH: build_matter_code(HELD_LENGTH),
    }
    matter_laws = tuple(build_matter_law(item, codes[item.length]) for item in FIXTURES)
    mass_fixture_and_code_controls(codes)
    eg_inverse_prediction_controls(matter_laws)
    covariance_and_support_controls(codes, matter_laws)
    deletion_leakage_domain_controls(matter_laws)
    cycle204_comparator_and_inventory(matter_laws)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
