#!/usr/bin/env python3
"""Cycle 438: physical mass-clock-to-active-source/receiver tournament.

Use one Cycle-437 physical M64 rest-sector coordinate in two supplied ways:
it drives the Cycle-437 Ramsey/clock latch and sets the angle of the
Cycle-426/429 recoil-field-distinct-receiver law.  Principal-phase and
Cayley-unwrapped candidates agree on three unaliased training sectors and
make different held alias-sector clock and receiver predictions.

The coordinate-to-clock scale, coordinate-to-source scale, preparation,
factor order, and bounded projector controls remain supplied.  Angle,
eigenphase, occupation, circuit layer, and update count are not energy,
stress, rate, time, force, gravity, occurrence, probability, or a Record.
Neither active-source law is selected.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_matter_inertia_clock_composition_bridge_cycle437_2026_07_19 as c437
import physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19 as c429


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MASS_CLOCK_ACTIVE_SOURCE_RECEIVER_TOURNAMENT_CYCLE438_NOTE_2026-07-19.md"
)
SOURCES = {
    "cycle204": ROOT / "docs/work_history/repo/review_feedback/REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md",
    "cycle221": ROOT / "docs/work_history/repo/review_feedback/OPERATOR_MASS_EQUIVALENCE_CYCLE221_NOTE_2026-07-17.md",
    "cycle426": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CYCLE426_NOTE_2026-07-19.md",
    "cycle429": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TEST_MATTER_RECOIL_RECEIVER_MULTIEDGE_PREDICTION_CYCLE429_NOTE_2026-07-19.md",
    "cycle434": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CARRIED_SOURCE_MOTION_RECOIL_BRIDGE_CYCLE434_NOTE_2026-07-19.md",
    "cycle437": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_INERTIA_CLOCK_COMPOSITION_BRIDGE_CYCLE437_NOTE_2026-07-19.md",
}

AUTHORITY = "none"
AUDIT = "unset"
SOURCE_SCALE = 0.05
CLOCK_SCALE = c437.CLOCK_SCALE
NETWORK_TRAIN_LENGTH = 5
NETWORK_HELD_LENGTH = 6
DEPTH = 3
TOL = 1.2e-9
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class TournamentFixture:
    name: str
    coordinate_fixture: c437.Fixture
    network_length: int


FIXTURES = tuple(
    TournamentFixture(item.name, item, NETWORK_HELD_LENGTH if item.held else NETWORK_TRAIN_LENGTH)
    for item in c437.FIXTURES
)


@dataclass
class TournamentLaw:
    fixture: TournamentFixture
    law: c437.Law
    coordinate: c437.MatterLaw
    theta: float


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
        "positive physical law tournament",
        "one declared bounded physical code",
        "same physical m64 rest-sector coordinate",
        "principal-phase law",
        "cayley-unwrapped law",
        "three unaliased training sectors",
        "held alias sector",
        "no refit",
        "chi = m/8",
        "theta_source = 0.05 m",
        "factorwise/tensor composition",
        "kronecker array is not materialized",
        "exact e/g and inverse",
        "source depletion and field gain",
        "distinct physical receiver",
        "complete clock-word predictions",
        "periodic-angle alias audit",
        "all 24 proper-cubic frames",
        "source-angle, receiver, transport, calibration, oscillator, and latch deletions",
        "leakage and lawful-domain controls",
        "45-m2 clock control",
        "69-m2 coordinate-source control",
        "no primitive sparse synthesis",
        "cycle-204 common-lapse and passive-trajectory flags remain false",
        "cycle-420 named prediction flags remain false",
        "angle, eigenphase, occupation, circuit layer, and update count are not energy, stress, rate, time, force, or gravity",
        "neither active-source law is selected",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-438 note freezes the joint tournament and semantic boundary", not missing, missing)

    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the cited science stack distinguishes conditional mass, physical recoil/receiver, carried preparation, and clock calibration",
        all(path.is_file() for path in SOURCES.values())
        and "acceleration / gravitational_gradient = m_passive / m_inertial" in source["cycle204"]
        and "principal-phase alias" in source["cycle221"]
        and "fixed hard-core recoil generator" in source["cycle426"]
        and "distinct physical m64 cell" in source["cycle429"]
        and "literal carried-source reservoir track" in source["cycle434"]
        and "physical matter/inertia-to-clock composition bridge" in source["cycle437"],
        {
            "coordinate_near_side": "Cycle437 physical M64 rest sector",
            "response_near_side": "Cycle426/429 recoil field and distinct receiver",
            "selected_active_source_law": False,
        },
    )


def build_tournament_laws() -> tuple[TournamentLaw, ...]:
    codes = {
        c437.TRAIN_LENGTH: c437.build_matter_code(c437.TRAIN_LENGTH),
        c437.HELD_LENGTH: c437.build_matter_code(c437.HELD_LENGTH),
    }
    coordinate = {
        item.name: c437.build_matter_law(item, codes[item.length])
        for item in c437.FIXTURES
    }
    return tuple(
        TournamentLaw(
            fixture,
            law,
            coordinate[fixture.name],
            SOURCE_SCALE * c437.calibration_coordinate(coordinate[fixture.name], law),
        )
        for fixture in FIXTURES
        for law in c437.LAWS
    )


@lru_cache(maxsize=None)
def local_vertex(theta: float) -> np.ndarray:
    return c429.c322.local_source_blocks(theta)[1]


@lru_cache(maxsize=None)
def embedded_source(theta: float, cell: int) -> sparse.csc_matrix:
    if cell not in c429.CELLS or not np.isfinite(theta):
        raise ValueError("dynamic recoil source needs a finite angle and A/B/C cell")
    vertex = local_vertex(theta)
    rows = []
    columns = []
    data = []
    for matter_source, label in enumerate(c429.LABELS):
        specs = list(c429.c319.label_specs(label))
        local_source = c429.c396.LOCAL_SPEC_INDEX[specs[cell]]
        for q_source in range(7):
            vertex_column = 7 * local_source + q_source
            targets = np.flatnonzero(abs(vertex[:, vertex_column]) > 2e-14)
            for local_joint_target in targets:
                local_target, q_target = divmod(int(local_joint_target), 7)
                target_specs = list(specs)
                target_specs[cell] = c429.c322.LOCAL_LABELS[local_target]
                target_label = tuple(item for spec in target_specs for item in spec)
                matter_target = c429.LABEL_INDEX[target_label]
                rows.append(7 * matter_target + q_target)
                columns.append(7 * matter_source + q_source)
                data.append(vertex[local_joint_target, vertex_column])
    dimension = 7 * c429.MATTER_DIM
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()


def apply_source_angle(
    state: c429.LogicalState,
    cell: int,
    theta: float,
    *,
    inverse: bool = False,
    enabled: bool = True,
) -> c429.LogicalState:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    active = (c429.reservoir_site(cell),) + tuple(c429.field_site(cell, d) for d in range(6))
    zero = np.zeros(c429.MATTER_DIM, dtype=complex)
    joint = np.column_stack([state.get(key, zero) for key in active]).reshape(-1)
    operator = embedded_source(theta, cell)
    transformed = ((operator.getH() if inverse else operator) @ joint).reshape((c429.MATTER_DIM, 7))
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, local]
    return c429.prune(output)


def apply_sources_angle(
    state: c429.LogicalState,
    theta: float,
    *,
    inverse: bool = False,
    enabled: tuple[bool, bool, bool] = (True, True, True),
) -> c429.LogicalState:
    order = tuple(reversed(c429.role_cells("A_to_C"))) if inverse else c429.role_cells("A_to_C")
    output = state
    for cell in order:
        output = apply_source_angle(
            output, cell, theta, inverse=inverse, enabled=enabled[cell]
        )
    return output


def logical_step(
    state: c429.LogicalState,
    theta: float,
    factors,
    *,
    source_enabled: tuple[bool, bool, bool] = (True, True, True),
    enabled_edges: tuple[bool, bool] = (True, True),
    contact_enabled: bool = True,
) -> c429.LogicalState:
    coin, first, second, contact = factors
    output = c429.apply_matter(state, coin)
    output = c429.apply_field_coin(output)
    output = apply_sources_angle(output, theta, enabled=source_enabled)
    output = c429.apply_matter(output, first)
    output = c429.apply_matter(output, second)
    output = c429.apply_transport(output, "A_to_C", enabled_edges=enabled_edges)
    return c429.apply_matter(output, contact) if contact_enabled else output


def logical_inverse(
    state: c429.LogicalState, theta: float, factors
) -> c429.LogicalState:
    coin, first, second, contact = factors
    output = c429.apply_matter(state, contact.getH())
    output = c429.apply_transport(output, "A_to_C", inverse=True)
    output = c429.apply_matter(output, second.getH())
    output = c429.apply_matter(output, first.getH())
    output = apply_sources_angle(output, theta, inverse=True)
    output = c429.apply_field_coin(output, inverse=True)
    return c429.apply_matter(output, coin.getH())


def evolve(
    state: c429.LogicalState, theta: float, factors, depth: int = DEPTH, **kwargs
) -> c429.LogicalState:
    output = state
    for _ in range(depth):
        output = logical_step(output, theta, factors, **kwargs)
    return output


def apply_physical_source_angle(
    state: c429.PhysicalState,
    encoding,
    cell: int,
    theta: float,
    *,
    inverse: bool = False,
) -> c429.PhysicalState:
    active = (c429.reservoir_site(cell),) + tuple(c429.field_site(cell, d) for d in range(6))
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    decoded = {key: encoding.getH() @ state.get(key, zero_physical) for key in active}
    transformed = apply_source_angle(decoded, cell, theta, inverse=inverse)
    output = {key: value.copy() for key, value in state.items() if key not in active}
    zero_logical = np.zeros(c429.MATTER_DIM, dtype=complex)
    for key in active:
        before_physical = state.get(key, zero_physical)
        before_logical = decoded[key]
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return c429.prune(output)


def physical_step(state, encoding, theta: float, factors):
    coin, first, second, contact = factors
    output = c429.apply_physical_matter(state, encoding, coin)
    output = c429.apply_field_coin(output)
    for cell in c429.role_cells("A_to_C"):
        output = apply_physical_source_angle(output, encoding, cell, theta)
    output = c429.apply_physical_matter(output, encoding, first)
    output = c429.apply_physical_matter(output, encoding, second)
    output = c429.apply_transport(output, "A_to_C")
    return c429.apply_physical_matter(output, encoding, contact)


def physical_inverse(state, encoding, theta: float, factors):
    coin, first, second, contact = factors
    output = c429.apply_physical_matter(state, encoding, contact.getH())
    output = c429.apply_transport(output, "A_to_C", inverse=True)
    output = c429.apply_physical_matter(output, encoding, second.getH())
    output = c429.apply_physical_matter(output, encoding, first.getH())
    for cell in reversed(c429.role_cells("A_to_C")):
        output = apply_physical_source_angle(output, encoding, cell, theta, inverse=True)
    output = c429.apply_field_coin(output, inverse=True)
    return c429.apply_physical_matter(output, encoding, coin.getH())


def physical_evolve(state, encoding, theta: float, factors, depth: int = DEPTH):
    output = state
    for _ in range(depth):
        output = physical_step(output, encoding, theta, factors)
    return output


def physical_unevolve(state, encoding, theta: float, factors, depth: int = DEPTH):
    output = state
    for _ in range(depth):
        output = physical_inverse(output, encoding, theta, factors)
    return output


def state_inner(left: dict, right: dict) -> complex:
    return sum(np.vdot(left[key], right[key]) for key in left.keys() & right.keys())


def product_residual(
    left_first: dict,
    left_second: dict,
    right_first: dict,
    right_second: dict,
) -> float:
    # Evaluate a stable factorwise upper bound for the residual of the implicit
    # tensor products.  Forming the norm from two nearly equal unit norms and
    # their overlap loses several digits through cancellation; the triangle
    # decomposition (a-c) x b + c x (b-d) does not.
    first_residual = c437.physical_residual(left_first, right_first)
    second_residual = c429.state_residual(left_second, right_second)
    return float(
        first_residual * np.sqrt(c429.state_norm(left_second))
        + np.sqrt(c437.physical_norm(right_first)) * second_residual
    )


def source_trace(theta: float, factors) -> dict[str, object]:
    initial = c429.initial_state("A_to_C")
    coin, _first, _second, _contact = factors
    before = c429.apply_matter(initial, coin)
    before = c429.apply_field_coin(before)
    after = apply_source_angle(before, c429.source_cell("A_to_C"), theta)
    cell = c429.source_cell("A_to_C")
    reservoir_loss = c429.reservoir_weight(before, cell) - c429.reservoir_weight(after, cell)
    before_field = c429.cell_q(before, cell) - c429.reservoir_weight(before, cell)
    after_field = c429.cell_q(after, cell) - c429.reservoir_weight(after, cell)
    matter_change = c429.matter_direction(after, cell) - c429.matter_direction(before, cell)
    twice_field_change = 2 * (c429.field_direction(after, cell) - c429.field_direction(before, cell))
    return {
        "source_reservoir_depletion": reservoir_loss,
        "source_field_gain": after_field - before_field,
        "source_resource_residual": reservoir_loss - (after_field - before_field),
        "source_matter_direction_change": matter_change,
        "source_twice_field_direction_change": twice_field_change,
        "source_direction_ledger_residual": matter_change + twice_field_change,
    }


def receiver_trace(second: c429.LogicalState, theta: float, factors) -> dict[str, object]:
    coin, _first, _second, _contact = factors
    order = c429.role_cells("A_to_C")
    output = c429.apply_matter(second, coin)
    output = c429.apply_field_coin(output)
    for cell in order[:-1]:
        output = apply_source_angle(output, cell, theta)
    before = output
    receiver = order[-1]
    after = apply_source_angle(before, receiver, theta)
    matter_change = c429.matter_direction(after, receiver) - c429.matter_direction(before, receiver)
    twice_field_change = 2 * (
        c429.field_direction(after, receiver) - c429.field_direction(before, receiver)
    )
    return {
        "receiver_gain_at_vertex": c429.reservoir_weight(after, receiver) - c429.reservoir_weight(before, receiver),
        "receiver_matter_direction_change": matter_change,
        "receiver_twice_field_direction_change": twice_field_change,
        "receiver_direction_ledger_residual": matter_change + twice_field_change,
    }


def response_controls(laws: tuple[TournamentLaw, ...], factors) -> dict[tuple[str, str], dict]:
    print("\nSAME COORDINATE -> CLOCK LATCH AND RECOIL/FIELD/RECEIVER")
    rows = {}
    failures = 0
    for item in laws:
        initial = c429.initial_state("A_to_C")
        first = logical_step(initial, item.theta, factors)
        second = logical_step(first, item.theta, factors)
        third = logical_step(second, item.theta, factors)
        source = source_trace(item.theta, factors)
        receiver = receiver_trace(second, item.theta, factors)
        clock_initial = {c437.blank_key(c437.INITIAL_CLOCK_POSITION): 1 + 0j}
        clock_output = c437.logical_forward(
            clock_initial, item.coordinate, item.law, 1
        )
        clock_weights = c437.clock_weights_logical(clock_output)
        row = {
            "fixture": item.fixture.name,
            "held": item.fixture.coordinate_fixture.held,
            "law": item.law.name,
            "coordinate": c437.calibration_coordinate(item.coordinate, item.law),
            "chi": c437.calibration_angle(item.coordinate, item.law, 1),
            "theta_source": item.theta,
            **source,
            **receiver,
            "receiver_response_after_three_applications": c429.reservoir_weight(
                third, c429.receiver_cell("A_to_C")
            ),
            "clock_bright_word": c437.BRIGHT_POSITION,
            "clock_dark_word": c437.DARK_POSITION,
            "clock_bright_weight": clock_weights[c437.BRIGHT_POSITION],
            "clock_dark_weight": clock_weights[c437.DARK_POSITION],
            "network_norm": c429.state_norm(third),
        }
        rows[(item.fixture.name, item.law.name)] = row
        failures += int(abs(row["source_resource_residual"]) > 3e-14)
        failures += int(np.linalg.norm(row["source_direction_ledger_residual"]) > 3e-14)
        failures += int(np.linalg.norm(row["receiver_direction_ledger_residual"]) > 3e-14)
        failures += int(abs(row["network_norm"] - 1) > 3e-11)

    train_clock = []
    train_receiver = []
    for fixture in FIXTURES[:-1]:
        principal = rows[(fixture.name, c437.PRINCIPAL.name)]
        cayley = rows[(fixture.name, c437.CAYLEY.name)]
        train_clock.append(abs(principal["clock_dark_weight"] - cayley["clock_dark_weight"]))
        train_receiver.append(
            abs(principal["receiver_response_after_three_applications"] - cayley["receiver_response_after_three_applications"])
        )
    held_principal = rows[(FIXTURES[-1].name, c437.PRINCIPAL.name)]
    held_cayley = rows[(FIXTURES[-1].name, c437.CAYLEY.name)]
    held_clock = abs(held_principal["clock_dark_weight"] - held_cayley["clock_dark_weight"])
    held_receiver = abs(
        held_principal["receiver_response_after_three_applications"]
        - held_cayley["receiver_response_after_three_applications"]
    )
    check(
        "the same rest coordinate gives identical unaliased train laws and distinct held clock plus physical receiver predictions with resource/recoil ledgers",
        failures == 0
        and max(train_clock + train_receiver) < 5e-14
        and held_clock > 0.7
        and held_receiver > 1e-6
        and min(row["source_reservoir_depletion"] for row in rows.values()) > 0
        and min(row["receiver_response_after_three_applications"] for row in rows.values()) > 0,
        {
            "rows": tuple(rows.values()),
            "maximum_train_clock_receiver_law_difference": max(train_clock + train_receiver),
            "held_clock_dark_weight_difference": held_clock,
            "held_receiver_response_difference": held_receiver,
            "angle_eigenphase_occupation_called_energy_stress_rate_time_force_gravity": False,
        },
    )
    return rows


def joint_eg_inverse_controls(laws: tuple[TournamentLaw, ...], factors) -> None:
    print("\nFACTORWISE/TENSOR E/G AND INVERSE")
    rows = []
    encoded_cache = {}
    for item in laws:
        key = (item.fixture.network_length, item.fixture.coordinate_fixture.held)
        if key not in encoded_cache:
            encodings, _reducer, support, gram = c429.c396.build_shell(item.fixture.network_length)
            encoding = encodings[c429.c319.ORDER_INDEX[(0, 1, 2)]]
            network_initial = c429.initial_state("A_to_C")
            encoded_cache[key] = (encoding, support, gram, network_initial, c429.encode_state(network_initial, encoding))
        encoding, support, gram, network_initial, network_physical = encoded_cache[key]

        network_logical_output = evolve(network_initial, item.theta, factors)
        network_physical_output = physical_evolve(network_physical, encoding, item.theta, factors)
        network_expected = c429.encode_state(network_logical_output, encoding)
        network_restored = physical_unevolve(network_physical_output, encoding, item.theta, factors)
        network_logical_restored = network_logical_output
        for _ in range(DEPTH):
            network_logical_restored = logical_inverse(network_logical_restored, item.theta, factors)

        maximum_clock_forward = maximum_clock_inverse = maximum_joint_forward = maximum_joint_inverse = 0.0
        maximum_norm = maximum_clock_leakage = 0.0
        for position in range(c437.c428.CLOCK_BITS):
            clock_key = c437.blank_key(position)
            clock_logical = {clock_key: 1 + 0j}
            clock_physical = c437.encode_state(clock_logical, item.coordinate)
            clock_logical_output = c437.logical_forward(
                clock_logical, item.coordinate, item.law, 1
            )
            clock_physical_output = c437.physical_forward(
                clock_physical, item.coordinate, item.law, 1
            )
            clock_expected = c437.encode_state(clock_logical_output, item.coordinate)
            clock_restored = c437.physical_inverse(
                clock_physical_output, item.coordinate, item.law, 1
            )
            maximum_clock_forward = max(
                maximum_clock_forward,
                c437.physical_residual(clock_physical_output, clock_expected),
            )
            maximum_clock_inverse = max(
                maximum_clock_inverse,
                c437.physical_residual(clock_restored, clock_physical),
            )
            maximum_joint_forward = max(
                maximum_joint_forward,
                product_residual(
                    clock_physical_output,
                    network_physical_output,
                    clock_expected,
                    network_expected,
                ),
            )
            maximum_joint_inverse = max(
                maximum_joint_inverse,
                product_residual(
                    clock_restored,
                    network_restored,
                    clock_physical,
                    network_physical,
                ),
            )
            maximum_norm = max(
                maximum_norm,
                abs(
                    c437.physical_norm(clock_physical_output)
                    * c429.state_norm(network_physical_output)
                    - 1
                ),
            )
            maximum_clock_leakage = max(
                maximum_clock_leakage,
                c437.leakage(clock_physical_output, item.coordinate.code.rest_physical),
            )
        decoded_network = {
            site: encoding.getH() @ value for site, value in network_physical_output.items()
        }
        reconstructed_network = c429.encode_state(decoded_network, encoding)
        rows.append(
            {
                "fixture": item.fixture.name,
                "law": item.law.name,
                "network_length": item.fixture.network_length,
                "network_matter_encoding_shape": encoding.shape,
                "matter_support": support,
                "Gram_raw_maximum": max(gram),
                "clock_forward_EG_residual": maximum_clock_forward,
                "network_forward_EG_residual": c429.state_residual(network_physical_output, network_expected),
                "joint_tensor_forward_EG_residual": maximum_joint_forward,
                "clock_physical_inverse_residual": maximum_clock_inverse,
                "network_physical_inverse_residual": c429.state_residual(network_restored, network_physical),
                "network_logical_inverse_residual": c429.state_residual(network_logical_restored, network_initial),
                "joint_tensor_inverse_residual": maximum_joint_inverse,
                "joint_norm_drift": maximum_norm,
                "clock_controller_leakage": maximum_clock_leakage,
                "network_code_leakage": c429.state_residual(network_physical_output, reconstructed_network),
            }
        )
    maximum = max(
        max(
            value
            for key, value in row.items()
            if key.endswith("residual") or key.endswith("drift") or key.endswith("leakage") or key == "Gram_raw_maximum"
        )
        for row in rows
    )
    check(
        "the controller-clock and recoil-network factors compose into an exact tensor E/G and adjoint inverse on the declared code",
        maximum < TOL,
        {
            "declared_code": "Cycle437 M64 rest controller x Cycle429 988xQ1 receiver network x complete one-hot clock/blank latch",
            "factorwise_tensor_identity": "(E_c G_c) tensor (E_r G_r) = (G_pc E_c) tensor (G_pr E_r)",
            "Kronecker_array_materialized": False,
            "maximum_EG_inverse_Gram_norm_leakage_residual": maximum,
            "rows": rows,
        },
    )


def angle_alias_deletion_domain_controls(
    laws: tuple[TournamentLaw, ...], factors, responses: dict[tuple[str, str], dict]
) -> None:
    print("\nPERIODIC-ANGLE ALIAS / LAW-SWAP / DELETIONS / DOMAIN")
    held_p = next(item for item in laws if item.fixture.name == FIXTURES[-1].name and item.law == c437.PRINCIPAL)
    held_c = next(item for item in laws if item.fixture.name == FIXTURES[-1].name and item.law == c437.CAYLEY)
    wrapped_p = float(np.angle(np.exp(1j * held_p.theta)))
    wrapped_c = float(np.angle(np.exp(1j * held_c.theta)))
    periodic_residual = float(np.linalg.norm(local_vertex(held_c.theta + 2 * np.pi) - local_vertex(held_c.theta)))
    held_vertex_residual = float(np.linalg.norm(local_vertex(held_p.theta) - local_vertex(held_c.theta)))

    initial = c429.initial_state("A_to_C")
    angle_deleted = evolve(initial, 0.0, factors)
    receiver_disabled = evolve(
        initial, held_c.theta, factors, source_enabled=(True, True, False)
    )
    first_edge_deleted = evolve(initial, held_c.theta, factors, enabled_edges=(False, True))
    second_edge_deleted = evolve(initial, held_c.theta, factors, enabled_edges=(True, False))
    contact_deleted = evolve(initial, held_c.theta, factors, contact_enabled=False)
    blank = {key: np.zeros_like(value) for key, value in initial.items()}
    blank_output = evolve(blank, held_c.theta, factors)
    receiver = c429.receiver_cell("A_to_C")
    baseline = responses[(FIXTURES[-1].name, c437.CAYLEY.name)]["receiver_response_after_three_applications"]

    clock_initial = {c437.blank_key(c437.INITIAL_CLOCK_POSITION): 1 + 0j}
    clock_deleted_calibration = c437.logical_forward(
        clock_initial, held_c.coordinate, held_c.law, 1, delete_calibration=True
    )
    clock_deleted_oscillator = c437.logical_forward(
        clock_initial, held_c.coordinate, held_c.law, 1, delete_oscillator=True
    )
    clock_deleted_latch = c437.logical_forward(
        clock_initial, held_c.coordinate, held_c.law, 1, delete_latch=True
    )
    calibration_weights = c437.clock_weights_logical(clock_deleted_calibration)
    oscillator_weights = c437.clock_weights_logical(clock_deleted_oscillator)
    latch_valid = sum(abs(value) ** 2 for key, value in clock_deleted_latch.items() if key.valid)

    swapped_p_theta = SOURCE_SCALE * c437.calibration_coordinate(held_p.coordinate, c437.CAYLEY)
    swapped_c_theta = SOURCE_SCALE * c437.calibration_coordinate(held_c.coordinate, c437.PRINCIPAL)
    swapped_p_receiver = c429.reservoir_weight(evolve(initial, swapped_p_theta, factors), receiver)
    swapped_c_receiver = c429.reservoir_weight(evolve(initial, swapped_c_theta, factors), receiver)
    law_swap_residual = max(
        abs(swapped_p_receiver - responses[(FIXTURES[-1].name, c437.CAYLEY.name)]["receiver_response_after_three_applications"]),
        abs(swapped_c_receiver - responses[(FIXTURES[-1].name, c437.PRINCIPAL.name)]["receiver_response_after_three_applications"]),
    )

    rest = held_c.coordinate.code.rest_physical
    deleted_rest = rest.copy()
    deleted_rest[int(np.argmax(abs(deleted_rest)))] = 0
    deleted_projector_gram = abs(float(np.vdot(deleted_rest, deleted_rest).real) - 1)
    deleted_projector_constraint = float(
        np.linalg.norm(held_c.coordinate.code.constraint @ deleted_rest - deleted_rest)
    )

    rejections = 0
    for operation in (
        lambda: embedded_source(float("nan"), 0),
        lambda: embedded_source(0.1, 3),
        lambda: c437.calibration_coordinate(held_c.coordinate, c437.Law("lookup")),
        lambda: c437.calibration_angle(held_c.coordinate, held_c.law, 3),
        lambda: c429.field_site(0, 6),
        lambda: c429.validate_state({c429.FIELD_DIM: np.zeros(c429.MATTER_DIM)}),
        lambda: c437.blank_key(16),
    ):
        try:
            operation()
        except ValueError:
            rejections += 1

    check(
        "held angles remain distinct modulo 2pi, the source parameter does not secretly wrap at 2pi, law swaps exchange predictions, and deletions are visible",
        abs(wrapped_c - wrapped_p) > 0.8
        and periodic_residual > 1
        and held_vertex_residual > 1
        and c429.reservoir_weight(angle_deleted, receiver) == 0
        and c429.reservoir_weight(receiver_disabled, receiver) == 0
        and c429.reservoir_weight(first_edge_deleted, receiver) == 0
        and c429.reservoir_weight(second_edge_deleted, receiver) == 0
        and abs(c429.reservoir_weight(contact_deleted, receiver) - baseline) > 1e-8
        and c429.state_norm(blank_output) == 0
        and calibration_weights[c437.DARK_POSITION] == 0
        and oscillator_weights[c437.INITIAL_CLOCK_POSITION] > 0.2
        and latch_valid == 0
        and law_swap_residual < 5e-14
        and deleted_projector_gram > 1e-3
        and deleted_projector_constraint > 1e-3
        and rejections == 7,
        {
            "held_principal_theta": held_p.theta,
            "held_cayley_theta": held_c.theta,
            "held_principal_theta_mod_2pi": wrapped_p,
            "held_cayley_theta_mod_2pi": wrapped_c,
            "theta_plus_2pi_vertex_residual": periodic_residual,
            "held_law_vertex_residual": held_vertex_residual,
            "source_angle_deleted_receiver": c429.reservoir_weight(angle_deleted, receiver),
            "receiver_vertex_deleted": c429.reservoir_weight(receiver_disabled, receiver),
            "first_transport_deleted": c429.reservoir_weight(first_edge_deleted, receiver),
            "second_transport_deleted": c429.reservoir_weight(second_edge_deleted, receiver),
            "contact_deleted": c429.reservoir_weight(contact_deleted, receiver),
            "blank_preparation_output_norm": c429.state_norm(blank_output),
            "clock_calibration_deleted_dark_weight": calibration_weights[c437.DARK_POSITION],
            "oscillator_deleted_initial_word_weight": oscillator_weights[c437.INITIAL_CLOCK_POSITION],
            "latch_deleted_valid_weight": latch_valid,
            "law_swap_receiver_residual": law_swap_residual,
            "deleted_projector_Gram": deleted_projector_gram,
            "deleted_projector_constraint": deleted_projector_constraint,
            "lawful_domain_rejections": rejections,
        },
    )


def covariance_support_mass_contact_controls(laws: tuple[TournamentLaw, ...], factors) -> None:
    print("\nALL-24 COVARIANCE / SUPPORT / MASS / CONTACT")
    frames = c429.c210.proper_cubic_frames()
    generator_residuals = []
    path_failures = 0
    for frame in frames:
        representation = c429.c426.recoil_frame(1, frame)
        generator = c429.c426.recoil_generator(1)
        generator_residuals.append(
            float(sparse.linalg.norm(representation @ generator @ representation.getH() - generator))
        )
        path = tuple(
            tuple(int(value) for value in frame @ np.asarray((offset, 0, 0)))
            for offset in range(3)
        )
        path_failures += sum(
            sum(abs(a - b) for a, b in zip(left, right)) != 1
            for left, right in zip(path, path[1:])
        )

    coordinate_projector_residuals = []
    coordinate_rest_residuals = []
    for length in (c437.TRAIN_LENGTH, c437.HELD_LENGTH):
        coordinate = next(item.coordinate for item in laws if item.coordinate.code.length == length)
        code = coordinate.code
        reducer = c437.c311.c305.StabilizerReducer(code.encoder.code)
        old_rest = code.flagged @ code.rest_seam
        for frame in frames:
            old_rep, failures = c437.c311.flagged_frame_representation(
                code.encoder, code.basis, {}, frame, reducer
            )
            path_failures += failures
            moved = old_rep @ old_rest
            coordinate_rest_residuals.append(float(np.linalg.norm(moved - old_rest)))
            coordinate_projector_residuals.append(
                float(np.linalg.norm(np.outer(moved, moved.conj()) - np.outer(old_rest, old_rest.conj())))
            )

    update_rows, _coin, _first, _second, contact, _forward, _reverse = c429.c319.update_controls(
        c429.LABELS, "path"
    )
    mass_residual = abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
    check(
        "both projector controls and the physical source/receiver path are bounded and covariant in all 24 frames while mass and contact remain separate factors",
        len(frames) == 24
        and max(generator_residuals + coordinate_rest_residuals + coordinate_projector_residuals) < TOL
        and path_failures == 0
        and mass_residual < 3e-13
        and update_rows["contact_nontrivial_columns"] == 645,
        {
            "proper_cubic_frames": len(frames),
            "maximum_recoil_generator_covariance": max(generator_residuals),
            "maximum_coordinate_rest_covariance": max(coordinate_rest_residuals),
            "maximum_coordinate_projector_covariance": max(coordinate_projector_residuals),
            "source_receiver_path_frame_failures": path_failures,
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_rest_mass": update_rows["three_cell_rest_mass"],
            "mass_residual": mass_residual,
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
            "train_controller_clock_plus_receiver_patch_M2": 106 + 142,
            "held_controller_clock_plus_receiver_patch_M2": 106 + 146,
            "clock_projector_control_support_M2": 45,
            "coordinate_source_control_support_M2": 44 + 25,
            "local_recoil_vertex_support_M2": 25,
            "clock_latch_primitive_support_M2": 3,
            "primitive_sparse_synthesis_of_45_and_69_M2_controls": "supplied/open",
            "minimum_content_claim": False,
        },
    )


def boundaries_and_inventory() -> None:
    print("\nTYPED PREDICTION BOUNDARIES / INVENTORY")
    cycle204 = {
        "bounded_active_source_candidates": True,
        "active_source_law_selected": False,
        "common_lapse": False,
        "passive_trajectory": False,
        "end_to_end_a_over_g": False,
    }
    cycle420 = {
        "physical_source_EG": False,
        "physical_test_matter_readout": False,
        "host_profile_join": False,
        "host_packet_or_centroid_join": False,
        "named_prediction_closed": False,
    }
    inventory = {
        "supplied": (
            "principal/Cayley coordinate formulas and beta-sector populations",
            "chi=M/8 and theta_source=0.05M including signs, zeros, and invocation",
            "45-M2 clock projector and 69-M2 coordinate-source projector controls without primitive sparse synthesis",
            "prepared reservoir, blank field, Cycle429 matter column, factor order, path, and readouts",
            "clock initial word, Ramsey arms, latch trigger, event identity, and blank sidecar",
        ),
        "derived": (
            "one common-coordinate clock plus recoil/receiver tensor compiler",
            "three unaliased train agreements and held alias disagreement in both readouts",
            "source depletion/field gain and source/receiver direction ledgers",
            "factorwise and tensor E/G/inverse, covariance, support, deletions, leakage, and domain controls",
        ),
        "open": (
            "selection/derivation of either coordinate law and both scales",
            "coherent cross-sector population and primitive projector-control synthesis",
            "autonomous source preparation, recurrence, physical energy/stress/source calibration",
            "common lapse, passive response, Cycle420 host joins, metric/proper time, Record formation, Born law, and empirical selection",
        ),
        "negative_claim": False,
        "axiom_pressure": False,
    }
    check(
        "the bounded candidate active-source tournament leaves every Cycle204 far-side and Cycle420 named prediction flag false",
        cycle204["bounded_active_source_candidates"]
        and not any(value for key, value in cycle204.items() if key != "bounded_active_source_candidates")
        and not any(cycle420.values())
        and AUTHORITY == "none"
        and AUDIT == "unset",
        {
            "Cycle204": cycle204,
            "Cycle420": cycle420,
            "inventory": inventory,
            "angle_eigenphase_occupation_layer_update_count_called_energy_stress_rate_time_force_gravity": False,
            "selected_active_source_law": False,
            "Record_formed": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> int:
    contracts()
    laws = build_tournament_laws()
    update_rows, coin, first, second, contact, _forward, _reverse = c429.c319.update_controls(
        c429.LABELS, "path"
    )
    factors = (coin, first, second, contact)
    responses = response_controls(laws, factors)
    joint_eg_inverse_controls(laws, factors)
    angle_alias_deletion_domain_controls(laws, factors, responses)
    covariance_support_mass_contact_controls(laws, factors)
    boundaries_and_inventory()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
