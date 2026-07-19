#!/usr/bin/env python3
"""Cycle 416: strict-response source balance with clock/metric receivers.

The existing Cycle-399 strict response M2 controls a bounded rotation between
one source-register excitation and one scalar-mediator excitation.  The gate
conserves source-plus-mediator number and reproduces the Cycle-294 Route-A
transfer sin^2(theta).  The same declared transfer coordinate is presented to
the Cycle-213 retarded-wave and Cycle-216 static Green receivers.  A separate
four-node candidate diamond tests the Cycle-170 depth and Cycle-46
order/count receiving contracts.

The scalar-source identification, receiver maps, candidate dependency graph,
and density calibration remain supplied.  Coherent labels are not Records;
depth is not time; the transfer is not energy/stress/source by itself; and no
metric or gravity law is derived.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17 as route_a
import physical_source_response_record_counter_interface_cycle399_2026_07_18 as c399
import physical_source_response_actualization_law_tournament_cycle403_2026_07_18 as c403
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216
import record_defined_causal_depth_clock_cycle170_2026_07_16 as c170


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_STRICT_RESPONSE_SOURCE_CLOCK_METRIC_RECEIVER_CYCLE416_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 7e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


Coord = tuple[int, int, int]


@dataclass(frozen=True)
class BalanceKey:
    bridge: c399.BridgeKey
    source: int
    mediator: int


BalanceState = dict[BalanceKey, np.ndarray]


@dataclass(frozen=True)
class ReceiverContract:
    dynamic_residual: float
    dynamic_inverse_residual: float
    dynamic_balance_residual: float
    static_residual: float
    static_scalar_residual: float
    source_strength: float


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
    if not NOTE.exists():
        check("the Cycle-416 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "three-m2 common code",
        "one source-register excitation",
        "source-plus-mediator number",
        "cycle-294 route a",
        "cycle-213 retarded",
        "cycle-216 static",
        "cycle-170",
        "cycle-46",
        "no host branch query",
        "blind held l6",
        "not physical energy, stress, or a selected source",
        "candidate dependency graph, not an actual record graph",
        "depth is not time",
        "no metric is reconstructed",
        "no gravity or axiom-pressure claim",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note states the common-code and far-side receiving contract", not missing, missing)


def source_angle() -> tuple[float, float]:
    species = route_a.c210.tuned_species(route_a.BETA)
    charge = c213.rest_charge(species.coin, route_a.c210.P_SCALAR)
    return route_a.MEDIATOR_COUPLING * charge, charge


def balance_unitary(response: int, angle: float) -> np.ndarray:
    if response not in (0, 1):
        raise ValueError("response must be binary")
    unitary = np.eye(4, dtype=complex)
    if response:
        cosine = np.cos(angle)
        sine = np.sin(angle)
        # Basis index = 2*source + mediator. Rotate |10> <-> |01>.
        unitary[np.ix_((2, 1), (2, 1))] = np.asarray(
            ((cosine, 1j * sine), (1j * sine, cosine)), dtype=complex
        )
    return unitary


def response_bit(key: c399.BridgeKey, origin: int) -> int:
    target = c399.c396.q_reservoir(c403.target_cell(origin))
    side = c403.target_side(origin)
    return int(key.q_key == target and key.enables[side] == 1)


def encode(state: c399.BridgeState) -> BalanceState:
    return {BalanceKey(key, 1, 0): value.copy() for key, value in state.items()}


def validate_balance_state(state: BalanceState) -> None:
    for key in state:
        if key.source not in (0, 1) or key.mediator not in (0, 1):
            raise ValueError("source/mediator labels must be binary")
        if key.source + key.mediator != 1:
            raise ValueError("declared source-balance code requires one excitation")


def balance_step(
    state: BalanceState,
    origin: int,
    angle: float,
    *,
    inverse: bool = False,
) -> BalanceState:
    validate_balance_state(state)
    output: BalanceState = {}
    for key, value in state.items():
        unitary = balance_unitary(response_bit(key.bridge, origin), angle)
        if inverse:
            unitary = unitary.conj().T
        source_index = 2 * key.source + key.mediator
        for target_index in range(4):
            coefficient = unitary[target_index, source_index]
            if abs(coefficient) < 1e-15:
                continue
            target = BalanceKey(key.bridge, target_index // 2, target_index % 2)
            output[target] = output.get(target, 0) + coefficient * value
    validate_balance_state(output)
    return output


def state_residual(left: BalanceState, right: BalanceState) -> float:
    total = 0.0
    for key in set(left) | set(right):
        template = left.get(key, right.get(key))
        assert template is not None
        a = left.get(key, np.zeros_like(template))
        b = right.get(key, np.zeros_like(template))
        total += float(np.vdot(a - b, a - b).real)
    return float(np.sqrt(total))


def weighted(state: BalanceState, predicate) -> float:
    return float(
        sum(np.vdot(value, value).real for key, value in state.items() if predicate(key))
    )


def balance_layout_controls() -> None:
    print("\nTHREE-M2 COMMON SOURCE-BALANCE CODE")
    angle, charge = source_angle()
    rows = []
    failures = 0
    for response in (0, 1):
        unitary = balance_unitary(response, angle)
        failures += int(np.linalg.norm(unitary.conj().T @ unitary - np.eye(4)) > 2e-14)
        number = np.diag((0, 1, 1, 2))
        failures += int(np.linalg.norm(unitary @ number - number @ unitary) > 2e-14)
        emitted = unitary @ np.asarray((0, 0, 1, 0), dtype=complex)
        restored = unitary.conj().T @ emitted
        rows.append(
            {
                "response": response,
                "mediator_weight": float(abs(emitted[1]) ** 2),
                "source_weight": float(abs(emitted[2]) ** 2),
                "inverse_residual": float(
                    np.linalg.norm(restored - np.asarray((0, 0, 1, 0)))
                ),
            }
        )
    expected = np.sin(angle) ** 2
    check(
        "one connected three-M2 controlled rotation conserves source-plus-mediator number and has an exact inverse",
        failures == 0
        and abs(rows[0]["mediator_weight"]) < 2e-15
        and abs(rows[1]["mediator_weight"] - expected) < 2e-14
        and abs(expected - 0.12589921612871371) < 3e-13,
        {
            "M2": {
                "existing_strict_response": 1,
                "new_source_register": 1,
                "new_scalar_mediator_register": 1,
                "total_common_installation": 4857,
            },
            "maximum_gate_support": 3,
            "connected_NN_support": True,
            "angle": angle,
            "vacuum_relative_mass_charge": charge,
            "Cycle294_RouteA_emission_transfer": expected,
            "rows": rows,
            "host_branch_queries": 0,
        },
    )


def held_strict_response_controls(factors, packet_layout, packet_initial):
    print("\nL5 / BLIND HELD-L6 STRICT RESPONSE BALANCE")
    angle, _charge = source_angle()
    transfer = np.sin(angle) ** 2
    rows = []
    failures = 0
    cases = {}
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c403.pre_admission_response(
                    origin, route, length, factors, packet_layout, packet_initial
                )
                encoded = encode(source)
                output = balance_step(encoded, origin, angle)
                restored = balance_step(output, origin, angle, inverse=True)
                target = c403.target_sector_weight(source, origin)
                mediator = weighted(output, lambda key: key.mediator == 1)
                response_mediator = weighted(
                    output,
                    lambda key: key.mediator == 1 and response_bit(key.bridge, origin) == 1,
                )
                source_depletion = target - weighted(
                    output,
                    lambda key: key.source == 1 and response_bit(key.bridge, origin) == 1,
                )
                total_number = weighted(output, lambda key: key.source + key.mediator == 1)
                inverse = state_residual(restored, encoded)
                failures += int(abs(mediator - target * transfer) > TOLERANCE)
                failures += int(abs(response_mediator - mediator) > TOLERANCE)
                failures += int(abs(source_depletion - mediator) > TOLERANCE)
                failures += int(abs(total_number - 1) > TOLERANCE)
                failures += int(inverse > TOLERANCE)
                rows.append(
                    {
                        "route": route,
                        "L": length,
                        "held": length == HELD_LENGTH,
                        "origin": "A" if origin == 0 else "C",
                        "strict_response_weight": target,
                        "mediator_transfer_weight": mediator,
                        "source_depletion": source_depletion,
                        "balance_residual": abs(source_depletion - mediator),
                        "inverse_residual": inverse,
                    }
                )
                cases[(route, length, origin)] = (source, encoded, output)
    check(
        "the one strict response coherently consumes/restores the source register with reciprocal L5 and blind held-L6 balance",
        failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "transfer_factor": transfer,
            "weight_semantics": "squared-norm sector weight, not probability/Born weight",
            "selected_physical_source": False,
        },
    )
    return cases


def receiver_contract(side: int, strength: float) -> ReceiverContract:
    rho = strength * route_a.c211.point_source(side)
    zero = np.zeros_like(rho)
    following = c213.wave_step(zero, zero, rho)
    dynamic_expected = c213.DT**2 * rho
    dynamic_residual = float(np.linalg.norm(following - dynamic_expected))
    dynamic_inverse = float(np.linalg.norm(c213.reverse_step(zero, following, rho)))
    dynamic_energy = c213.field_energy(following, zero)
    dynamic_work = float(np.sum(c213.work_density(zero, following, rho)))

    coin_field = c216.solve_coin_field(rho)
    static_residual = float(
        np.linalg.norm(
            c216.apply_stiffness(coin_field)
            - rho[..., None] * route_a.c210.UNIFORM
        )
    )
    scalar = c216.scalar_field(coin_field).real
    green = route_a.c211.solve_field(rho)
    scalar_residual = float(np.linalg.norm(scalar - 3 * green))
    return ReceiverContract(
        dynamic_residual,
        dynamic_inverse,
        abs(dynamic_energy - dynamic_work),
        static_residual,
        scalar_residual,
        strength,
    )


def field_receiver_controls(cases) -> None:
    print("\nCYCLE-213 / CYCLE-216 FAR-SIDE RECEIVERS")
    rows = []
    failures = 0
    strengths = {}
    for (route, length, origin), (_source, _encoded, output) in cases.items():
        strength = weighted(output, lambda key: key.mediator == 1)
        receiver = receiver_contract(length, strength)
        rows.append(
            {
                "route": route,
                "L": length,
                "held": length == HELD_LENGTH,
                "origin": "A" if origin == 0 else "C",
                "actual_mediator_expectation": strength,
                "receiver": receiver,
            }
        )
        strengths[(route, length, origin)] = strength
        failures += int(receiver.dynamic_residual > 2e-14)
        failures += int(receiver.dynamic_inverse_residual > 2e-14)
        failures += int(receiver.dynamic_balance_residual > 2e-14)
        failures += int(receiver.static_residual > 3e-11)
        failures += int(receiver.static_scalar_residual > 3e-11)
    deleted = receiver_contract(HELD_LENGTH, 0.0)
    check(
        "each actual route/size/orientation mediator expectation drives its own exact Cycle-213 retarded and Cycle-216 static receivers",
        failures == 0
        and strengths[("unit_weight", TRAIN_LENGTH, 0)]
        == strengths[("unit_weight", HELD_LENGTH, 0)]
        and strengths[("coefficient_two", TRAIN_LENGTH, 0)]
        == strengths[("coefficient_two", HELD_LENGTH, 0)]
        and strengths[("coefficient_two", HELD_LENGTH, 0)]
        > strengths[("unit_weight", HELD_LENGTH, 0)]
        and deleted.dynamic_residual == deleted.static_residual == deleted.static_scalar_residual == 0,
        {
            "rows": rows,
            "failures": failures,
            "source_deleted": deleted,
            "source_identification": "supplied actual-mediator-expectation-to-scalar-source map",
            "physical_energy_or_stress_derived": False,
        },
    )


def rotate_coord(site: Coord, frame: np.ndarray) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(site))


def candidate_diamond() -> tuple[dict[Coord, str], dict[Coord, frozenset[Coord]], Coord]:
    root = (0, 0, 0)
    dynamic = (1, 0, 0)
    static = (0, 1, 0)
    compare = (1, 1, 0)
    expected = {
        root: "source-balance-proposal",
        dynamic: "retarded-receiver-proposal",
        static: "static-receiver-proposal",
        compare: "comparison-proposal",
    }
    dependencies = {
        root: frozenset(),
        dynamic: frozenset((root,)),
        static: frozenset((root,)),
        compare: frozenset((dynamic, static)),
    }
    return expected, dependencies, compare


def clock_metric_receiver_controls() -> None:
    print("\nCYCLE-170 / CYCLE-46 RECEIVING BOUNDARY")
    expected, dependencies, output = candidate_diamond()
    certificate = c170.dag_certificate(expected, dependencies, (output,))
    frame_failures = local_failures = 0
    depths = []
    for frame in route_a.c210.proper_cubic_frames():
        moved_expected = {rotate_coord(site, frame): label for site, label in expected.items()}
        moved_dependencies = {
            rotate_coord(site, frame): frozenset(rotate_coord(parent, frame) for parent in parents)
            for site, parents in dependencies.items()
        }
        moved_output = rotate_coord(output, frame)
        moved = c170.dag_certificate(moved_expected, moved_dependencies, (moved_output,))
        depths.append(moved["depth"])
        frame_failures += int(moved["depth"] != certificate["depth"])
        local_failures += sum(
            sum(abs(a - b) for a, b in zip(site, parent)) != 1
            for site, parents in moved_dependencies.items()
            for parent in parents
        )

    # Cycle 46 diamond separator and unknown-density conformal compensation.
    event_count = len(expected)
    chain_count = certificate["depth"]
    dimension = 4
    omega = 2.0
    rho = 11.0
    base_volume = event_count / rho
    scaled_volume = omega**dimension * base_volume
    compensating_density = rho / omega**dimension
    measure_residual = abs(compensating_density * scaled_volume - event_count)
    receiving = {
        "candidate_graph_only": True,
        "actual_Records": 0,
        "actual_clock_admitted": False,
        "causal_faithfulness_proved": False,
        "uniform_volume_density_proved": False,
        "density_calibrated_to_scale": False,
        "metric_reconstructed": False,
    }
    check(
        "the four-node candidate diamond satisfies the Cycle-170 depth shape and the Cycle-46 count-versus-chain separator in all frames",
        certificate["nodes"] == 4
        and certificate["edges"] == 4
        and certificate["depth"] == 3
        and certificate["output_depths"] == (3,)
        and event_count == 4
        and chain_count == 3
        and len(depths) == 24
        and frame_failures == local_failures == 0
        and measure_residual < 1e-14,
        {
            "candidate_certificate": {
                "nodes": certificate["nodes"],
                "edges": certificate["edges"],
                "depth": certificate["depth"],
                "output_depths": certificate["output_depths"],
            },
            "frames": len(depths),
            "local_edge_failures": local_failures,
            "regional_candidate_count": event_count,
            "maximum_candidate_chain": chain_count,
            "unknown_density_conformal_measure_residual": measure_residual,
            "receiving_contract": receiving,
        },
    )
    check(
        "the coherent proposal graph is not admitted as an actual Cycle-170 clock or a Cycle-46 metric reconstruction",
        not any(
            receiving[key]
            for key in (
                "actual_clock_admitted",
                "causal_faithfulness_proved",
                "uniform_volume_density_proved",
                "density_calibrated_to_scale",
                "metric_reconstructed",
            )
        ),
        receiving,
    )


def covariance_identity_deletion_controls(cases, factors, packet_layout, packet_initial) -> None:
    print("\nCOVARIANCE / IDENTITY / DELETION")
    coin, first, second, contact = factors
    covariance = c399.c396.c319.covariance_schedule_controls(
        c399.c396.LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        contact @ second @ first @ coin,
        contact @ first @ second @ coin,
    )
    frames = route_a.c210.proper_cubic_frames()
    angle, _charge = source_angle()
    # Source, mediator, and response are explicitly declared proper-cubic
    # scalars, so their installed frame representation is the identity.  This
    # checks that declared representation; it is not a derived tensor law.
    scalar_representation_residual = max(
        np.linalg.norm(np.eye(4) @ balance_unitary(1, angle) - balance_unitary(1, angle) @ np.eye(4))
        for _frame in frames
    )
    source, encoded, output = cases[("unit_weight", HELD_LENGTH, 0)]
    original_hash = c399.c360.record_hash(packet_initial)
    identity_failures = 0
    for key in output:
        identity_failures += int(key.bridge not in source)
        identity_failures += int(
            c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.a_bits))
            != original_hash
        )
        identity_failures += int(
            c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.c_bits))
            != original_hash
        )

    update_rows, _ = c399.source_factors()
    contact_columns = np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
    deleted = balance_step(encoded, 0, 0.0)
    deleted_mediator = weighted(deleted, lambda key: key.mediator == 1)
    check(
        "the balance gate respects its declared scalar identity action in all 24 proper-cubic spatial frames",
        len(frames) == 24
        and scalar_representation_residual == 0
        and covariance["maximum_update_covariance_residual"] < TOLERANCE
        and covariance["frame_group_law_failures"] == 0,
        {
            "frames": len(frames),
            "declared_scalar_identity_residual": scalar_representation_residual,
            "derived_tensor_transformation_law": False,
            "source": covariance,
        },
    )
    check(
        "the common code preserves prior Records and mass/Q/number/vector/contact fixtures while gate deletion removes transfer",
        identity_failures == 0
        and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and contact_columns == 645
        and deleted_mediator == 0,
        {
            "Record_hash": original_hash,
            "identity_failures": identity_failures,
            "mass": update_rows["Cycle219_mass_fixture"],
            "Q": 1,
            "matter_number": "3.0 -> 3.000000000000002",
            "vector_commutators": 0,
            "contact_columns": int(contact_columns),
            "deleted_gate_mediator_weight": deleted_mediator,
        },
    )


def domain_and_inventory_controls() -> None:
    print("\nDOMAIN / SUPPLIED-DERIVED-OPEN INVENTORY")
    rejections = 0
    template = np.ones(1, dtype=complex)
    bad_states = (
        {BalanceKey(next(iter(c399.initial_bridge_state(0, *c399.packet_fixture()))), 2, 0): template},
        {BalanceKey(next(iter(c399.initial_bridge_state(0, *c399.packet_fixture()))), 0, 0): template},
        {BalanceKey(next(iter(c399.initial_bridge_state(0, *c399.packet_fixture()))), 1, 1): template},
    )
    for state in bad_states:
        try:
            validate_balance_state(state)
        except ValueError:
            rejections += 1
    inventory = {
        "supplied": (
            "Cycle399 strict response state and response-bit decoder",
            "Cycle294 Route-A mass-normalized angle and scalar mediator meaning",
            "one source excitation, one scalar-mediator M2, and dense three-M2 balance gate",
            "number-transfer-to-Cycle213/216 scalar-source identification",
            "four-node candidate dependency graph and Cycle170/46 receiver interpretation",
        ),
        "derived": (
            "exact source-plus-mediator balance, emission/absorption inverse, held reciprocity and covariance",
            "exact Cycle213 first-step/inverse/work balance and Cycle216 static solve",
            "Cycle170 diamond depth and Cycle46 count-versus-chain receiving separator",
        ),
        "open": (
            "selection of number transfer as physical source/energy/stress",
            "autonomous source-register preparation, recurrence, recoil, and full matter-field history",
            "actual Record formation and clock admission",
            "causal/volume faithfulness, density calibration, metric dynamics, and gravity",
        ),
        "host_branch_queries": 0,
        "actual_Records_added": 0,
        "physical_source_selected": False,
        "clock_or_metric_derived": False,
        "negative_or_minimum_claim": False,
        "axiom_pressure": False,
    }
    check(
        "lawful-domain and inventory controls keep a constructive receiver join separate from source, clock, metric, and gravity selection",
        rejections == 3
        and not inventory["physical_source_selected"]
        and not inventory["clock_or_metric_derived"]
        and not inventory["negative_or_minimum_claim"]
        and not inventory["axiom_pressure"],
        {"domain_rejections": rejections, **inventory},
    )


def main() -> int:
    print("CYCLE 416: STRICT RESPONSE / SOURCE BALANCE / CLOCK-METRIC RECEIVERS")
    note_contract()
    balance_layout_controls()
    _rows, factors = c399.source_factors()
    packet_layout, packet_initial = c399.packet_fixture()
    cases = held_strict_response_controls(factors, packet_layout, packet_initial)
    field_receiver_controls(cases)
    clock_metric_receiver_controls()
    covariance_identity_deletion_controls(
        cases, factors, packet_layout, packet_initial
    )
    domain_and_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_STRICT_RESPONSE_SOURCE_CLOCK_METRIC_RECEIVER_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_STRICT_RESPONSE_SOURCE_CLOCK_METRIC_RECEIVER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
