#!/usr/bin/env python3
"""Cycle 420: adversarial source-to-prediction bridge contract.

Freeze and execute the shortest currently visible join from the Cycle-416/417
coherent source interface through the conserved seven-M2 reservoir/field block
to the Cycle-213/216 dynamic/static scalar receivers and older prediction-bearing
gravity/source probes.

The runner distinguishes signed coherent amplitude, signed scalar density, and
positive occupation/density interfaces.  Legacy scalar adapters are diagnostic
comparators only: they query a post-update occupation and therefore are not a
physical E/G source compiler.  Detector centroids and widths are host-array
readouts, not physical-M2 test-matter instruments or Records.

This is a constructive contract and interface audit.  It makes no no-go,
minimum-content, shared-obstruction, axiom-pressure, energy, gravity, clock,
Born, occurrence, or Record claim.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import causal_impact_parameter_probe as impact
import causal_propagating_field as causal
import cycle416_seven_m2_common_code_seed_cycle418_2026_07_19 as c418
import diamond_ideal_lockin_detector_theorem as nv
import local_conjugate_reservoir_source_field_ledger_repair_2026_07_17 as reservoir
import moving_source_cross_family_probe as moving
import multipole_tidal_response_probe as multipole
import physical_coherent_receiver_source_injection_cycle417_2026_07_18 as c417
import physical_strict_response_source_clock_metric_receiver_cycle416_2026_07_18 as c416


c213 = c416.c213
c216 = c416.c216
c211 = c416.route_a.c211

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_PREDICTION_BRIDGE_CONTRACT_CYCLE420_NOTE_2026-07-19.md"
)
TOL = 8.0e-10
TRAIN_LENGTH = 5
HELD_LENGTH = 6
ROUTE_STRENGTHS = {
    "unit_weight": 7.501679264744504e-7,
    "coefficient_two": 3.7828627925537926e-6,
}
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SurfaceContract:
    name: str
    source_interface: str
    sign_origin: str
    readout: str
    training_domain: str
    held_domain: str
    physical_source_eg: bool = False
    physical_test_matter_readout: bool = False


SURFACES = (
    SurfaceContract(
        "causal_ratio",
        "positive host scalar density strength/r",
        "positive source; causal schedule changes support",
        "host detector centroid from normalized complex-array weights",
        "strengths 7.501679264744504e-7 and legacy 1e-5/5e-5",
        "strength 3.7828627925537926e-6 and legacy 1e-4",
    ),
    SurfaceContract(
        "moving_source_odd_response",
        "positive host scalar density sampled on a moving trajectory",
        "velocity reversal, not source-amplitude sign",
        "host detector centroid relative to the v=0 static control",
        "v=+-0.5 on portable family 1",
        "v=+-1 on portable families 1 and 2",
    ),
    SurfaceContract(
        "quadrupole_width",
        "signed host scalar density coefficients (+1,-2,+1)",
        "explicit signed source-profile coefficients",
        "host test-packet centroid and width from normalized complex-array weights",
        "a=1 at the unit-route strength",
        "held strength at a=1, held separation at unit strength, and their joint perturbation",
    ),
    SurfaceContract(
        "impact_parameter",
        "positive host scalar density strength/r",
        "positive source; detector/source geometry fixes toward sign",
        "host detector centroid and a log-log fit",
        "realized b=(5,6,7), fit once",
        "realized b=(8,10), no refit",
    ),
    SurfaceContract(
        "diamond_nv",
        "signed phase-bearing real signal amplitude/history",
        "drive/reference phase supplies quadrature sign",
        "ideal host lock-in X,Y,phi and spatial phase slope",
        "analytic lock-in channels and one small-delay point",
        "pi flip, drive/static nulls, frequency/delay and widefield phase ramp",
    ),
)


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
        check("the Cycle-420 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "positive scalar density",
        "signed scalar density",
        "signed phase-bearing amplitude",
        "velocity reversal",
        "static-limit identity",
        "no refit",
        "physical test-matter readout",
        "not physical energy",
        "not a physical clock",
        "not a born law",
        "not records",
        "no no-go or axiom-pressure claim",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note freezes source types, held controls, and semantic boundaries", not missing, missing)


def source_type_contract_controls() -> None:
    print("\nPREDECLARED SOURCE / READOUT TYPES")
    rows = tuple(asdict(surface) for surface in SURFACES)
    source_types = {surface.source_interface for surface in SURFACES}
    check(
        "five prediction surfaces freeze density/amplitude type, sign origin, train/held split, and readout before replay",
        len(SURFACES) == 5
        and len(source_types) >= 3
        and all(not surface.physical_source_eg for surface in SURFACES)
        and all(not surface.physical_test_matter_readout for surface in SURFACES)
        and causal.FIELD_STRENGTHS == (1e-5, 5e-5, 1e-4)
        and moving.VELOCITIES == (0.0, 0.5, 1.0, -0.5, -1.0)
        and multipole.build_quadrupole(1.0) == [(-1.0, 1.0), (0.0, -2.0), (1.0, 1.0)]
        and impact.B_VALUES == (5, 6, 7, 8, 10),
        rows,
    )


def scalar_field_embedding() -> np.ndarray:
    """Import the exact signed Cycle-418 source/scalar seed."""

    return c418.seed().copy()


def hard_core_lift_controls() -> None:
    print("\nCYCLE-416 -> CONSERVED HARD-CORE FIELD")
    angle, _charge = c416.source_angle()
    physical = reservoir.reservoir_field_operators()
    embedding = scalar_field_embedding()
    rows = []
    for response in (0, 1):
        physical_gate = c418.physical_gate(response, angle)
        coarse_gate = c418.logical_gate(response, angle)
        rows.append(
            {
                "response": response,
                "EG_residual": float(np.linalg.norm(physical_gate @ embedding - embedding @ coarse_gate)),
                "number_commutator": float(
                    np.linalg.norm(physical_gate @ physical["Q"] - physical["Q"] @ physical_gate)
                ),
                "inverse_residual": float(
                    np.linalg.norm(physical_gate.conj().T @ physical_gate - np.eye(128))
                ),
            }
        )
    emitted = reservoir.exchange_gate(angle, physical["exchange"]) @ embedding[:, 0]
    emitted_weight = float(np.vdot(emitted, physical["F"] @ emitted).real)
    check(
        "the Cycle-420 bridge replays Cycle 418's exact Cycle-416-to-seven-M2 source/scalar seed",
        np.linalg.norm(embedding.conj().T @ embedding - np.eye(2)) < 3e-15
        and max(row["EG_residual"] for row in rows) < 3e-15
        and max(row["number_commutator"] for row in rows) < 3e-14
        and max(row["inverse_residual"] for row in rows) < 3e-14
        and abs(emitted_weight - math.sin(angle) ** 2) < 3e-14,
        {
            "angle": angle,
            "rows": rows,
            "emitted_field_occupation": emitted_weight,
            "field_M2": 6,
            "reservoir_M2": 1,
        },
    )


def held_coherent_port_controls() -> dict[str, float]:
    print("\nCYCLE-417 HELD COHERENT PORTS")
    angle, _charge = c416.source_angle()
    transfer = float(math.sin(angle) ** 2)
    _source_rows, factors = c416.c399.source_factors()
    packet_layout, packet_initial = c416.c399.packet_fixture()
    rows = []
    failures = 0
    held_strengths: dict[str, float] = {}
    for route in c416.c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c417.c403.pre_admission_response(
                    origin, route, length, factors, packet_layout, packet_initial
                )
                balanced = c416.balance_step(c416.encode(source), origin, angle)
                injected = c417.source_injection(c417.lift(balanced))
                expected = c417.c403.target_sector_weight(source, origin) * transfer
                mediator = c417.weight(injected, lambda key: key.mediator == 1)
                retarded = c417.weight(injected, lambda key: key.retarded_source == 1)
                static = c417.weight(injected, lambda key: key.static_source == 1)
                failures += int(max(abs(value - expected) for value in (mediator, retarded, static)) > TOL)
                rows.append(
                    {
                        "route": route,
                        "L": length,
                        "held": length == HELD_LENGTH,
                        "origin": "A" if origin == 0 else "C",
                        "weight": mediator,
                    }
                )
                if length == HELD_LENGTH and origin == 0:
                    held_strengths[route] = mediator
    check(
        "Cycle-417 preserves every L5/blind-L6 route/origin weight in both coherent receiver ports",
        failures == 0
        and all(abs(held_strengths[key] - value) < TOL for key, value in ROUTE_STRENGTHS.items()),
        {"rows": rows, "failures": failures, "host_expectation_queries_in_port_update": 0},
    )
    return held_strengths


def cycle417_fanout_resource_boundary() -> None:
    print("\nCYCLE-417 FANOUT RESOURCE BOUNDARY")
    packet_layout, packet_initial = c416.c399.packet_fixture()
    bridge = next(iter(c416.c399.initial_bridge_state(0, packet_layout, packet_initial)))
    balance = {
        c416.BalanceKey(bridge, 0, 1): np.asarray((1.0 + 0.0j,)),
    }
    before = c417.lift(balance)
    after = c417.source_injection(before)
    before_numbers = tuple(
        key.mediator + key.retarded_source + key.static_source for key in before
    )
    after_numbers = tuple(
        key.mediator + key.retarded_source + key.static_source for key in after
    )
    restored = c417.source_injection(after, inverse=True)
    check(
        "Cycle 417's mediator-one fanout is reversible label copying but not global resource transfer",
        before_numbers == (1,)
        and after_numbers == (3,)
        and c417.residual(restored, before) == 0,
        {
            "mediator_plus_ports_before": before_numbers,
            "mediator_plus_ports_after": after_numbers,
            "inverse_residual": c417.residual(restored, before),
            "physical_resource_ledger_closed": False,
        },
    )


def common_dynamic_static_controls(strengths: dict[str, float]) -> None:
    print("\nCOMMON DYNAMIC / STATIC SCALAR REFERENCE")
    rows = []
    failures = 0
    fields: dict[tuple[int, str], np.ndarray] = {}
    dynamic: dict[tuple[int, str], np.ndarray] = {}
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        for route, strength in strengths.items():
            rho = strength * c211.point_source(length)
            zero = np.zeros_like(rho)
            following = c213.wave_step(zero, zero, rho)
            coin_field = c216.solve_coin_field(rho)
            static_residual = float(
                np.linalg.norm(c216.apply_stiffness(coin_field) - rho[..., None] * c416.route_a.c210.UNIFORM)
            )
            scalar_residual = float(
                np.linalg.norm(c216.scalar_field(coin_field).real - 3 * c211.solve_field(rho))
            )
            dynamic_residual = float(np.linalg.norm(following - c213.DT**2 * rho))
            failures += int(max(dynamic_residual, static_residual, scalar_residual) > 3e-11)
            fields[(length, route)] = coin_field
            dynamic[(length, route)] = following
            rows.append(
                {
                    "L": length,
                    "held": length == HELD_LENGTH,
                    "route": route,
                    "strength": strength,
                    "dynamic_residual": dynamic_residual,
                    "static_residual": static_residual,
                    "static_scalar_residual": scalar_residual,
                }
            )

    ratio = strengths["coefficient_two"] / strengths["unit_weight"]
    linearity = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        linearity.extend(
            (
                float(
                    np.linalg.norm(
                        dynamic[(length, "coefficient_two")]
                        - ratio * dynamic[(length, "unit_weight")]
                    )
                ),
                float(
                    np.linalg.norm(
                        fields[(length, "coefficient_two")]
                        - ratio * fields[(length, "unit_weight")]
                    )
                ),
            )
        )

    static_limit = []
    for momentum in (
        np.asarray((0.41, -0.23, 0.17)),
        np.asarray((0.72, 0.31, -0.19)),
        np.asarray((-1.13, 0.44, 0.29)),
    ):
        walk = c216.walk(momentum)
        static_limit.append(
            float(np.linalg.norm(c216.stiffness(momentum) - (2 * np.eye(6) - walk - walk.conj().T)))
        )

    deleted = c216.solve_coin_field(np.zeros((HELD_LENGTH,) * 3))
    check(
        "one scalar source coordinate gives exact linear Cycle-213 dynamic and Cycle-216 static equations at L5/held-L6",
        failures == 0
        and max(linearity) < 3e-14
        and max(static_limit) == 0
        and np.max(np.abs(deleted)) == 0,
        {
            "rows": rows,
            "source_strength_ratio": ratio,
            "maximum_linearity_residual": max(linearity),
            "static_limit_identity_residual": max(static_limit),
            "deletion_residual": float(np.max(np.abs(deleted))),
            "source_adapter": "post-update occupation diagnostic; not physical E/G injection",
        },
    )


def causal_ratio_controls(strengths: dict[str, float]) -> None:
    print("\nCAUSAL RATIO / SOURCE-STRENGTH CONTROL")
    rows = []
    cases = (
        ("unit_weight", strengths["unit_weight"]),
        ("coefficient_two", strengths["coefficient_two"]),
        ("legacy_1e-5", 1e-5),
        ("legacy_5e-5", 5e-5),
        ("legacy_1e-4", 1e-4),
    )
    for label, strength in cases:
        summary, zero_delta, zero_field = causal._measure_strength(strength)
        rows.append((label, summary, zero_delta, zero_field))
    by_label = {label: summary for label, summary, _zero_delta, _zero_field in rows}
    source_ratio = strengths["coefficient_two"] / strengths["unit_weight"]
    response_ratio = (
        by_label["coefficient_two"].inst_mean / by_label["unit_weight"].inst_mean
    )
    forward_spread = float(np.ptp([row[1].forward_ratio for row in rows]))
    dynamic_c1_spread = float(np.ptp([row[1].dynamic_ratios[1.0] for row in rows]))
    dynamic_c05_spread = float(np.ptp([row[1].dynamic_ratios[0.5] for row in rows]))
    check(
        "the causal-ratio proxy keeps deletion, strength scaling, and frozen ratio ordering on actual and legacy strengths",
        max(max(row[2], row[3]) for row in rows) == 0
        and abs(response_ratio / source_ratio - 1) < 5e-4
        and forward_spread < 0.005
        and dynamic_c1_spread < 0.005
        and dynamic_c05_spread < 0.005
        and by_label["unit_weight"].dynamic_ratios[1.0]
        > by_label["unit_weight"].dynamic_ratios[0.5],
        {
            "rows": [
                {
                    "route": route,
                    "strength": summary.strength,
                    "instantaneous_centroid": summary.inst_mean,
                    "forward_ratio": summary.forward_ratio,
                    "dynamic_c1_ratio": summary.dynamic_ratios[1.0],
                    "dynamic_c0.5_ratio": summary.dynamic_ratios[0.5],
                }
                for route, summary, _zero_delta, _zero_field in rows
            ],
            "source_ratio": source_ratio,
            "response_ratio": response_ratio,
            "forward_ratio_spread": forward_spread,
            "dynamic_c1_ratio_spread": dynamic_c1_spread,
            "dynamic_c0.5_ratio_spread": dynamic_c05_spread,
            "physical_source_EG": False,
        },
    )


def moving_odd_controls(strengths: dict[str, float]) -> None:
    print("\nMOVING-SOURCE VELOCITY REVERSAL")
    rows = []
    failures = 0
    for family_index, (label, drift, restore) in enumerate(moving.FAMILIES):
        values = {
            velocity: moving._summarize(drift, restore, velocity, strengths["unit_weight"])
            for velocity in (-1.0, -0.5, 0.0, 0.5, 1.0)
        }
        odd_train = (values[0.5].delta_static_mean - values[-0.5].delta_static_mean) / 2
        even_train = (values[0.5].delta_static_mean + values[-0.5].delta_static_mean) / 2
        odd_held = (values[1.0].delta_static_mean - values[-1.0].delta_static_mean) / 2
        even_held = (values[1.0].delta_static_mean + values[-1.0].delta_static_mean) / 2
        no_refit_linear_residual = odd_held - 2 * odd_train
        failures += int(values[0.5].delta_static_mean <= 0 or values[-0.5].delta_static_mean >= 0)
        failures += int(values[1.0].delta_static_mean <= 0 or values[-1.0].delta_static_mean >= 0)
        failures += int(abs(values[0.0].delta_static_mean) > 2e-15)
        rows.append(
            {
                "family": label,
                "held_family": family_index == 1,
                "odd_v0.5": odd_train,
                "even_v0.5": even_train,
                "odd_v1": odd_held,
                "even_v1": even_held,
                "no_refit_linear_v_residual": no_refit_linear_residual,
            }
        )
    check(
        "velocity reversal flips the centroid response on train and held magnitudes/families without refitting",
        failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "sign_origin": "trajectory velocity; source strength remains positive",
            "linear_in_velocity_law_claimed": False,
            "physical_carried_source_compiler": False,
        },
    )


def quadrupole_width_controls(strengths: dict[str, float]) -> None:
    print("\nSIGNED QUADRUPOLE / WIDTH RESPONSE")
    lat = multipole.Lattice3D(multipole.PHYS_L, multipole.PHYS_W, multipole.H)
    det = multipole.detector(lat)
    initial = multipole.point_packet(lat)
    free = multipole.propagate_charge(lat, initial, np.zeros(lat.n), 0)
    free_centroid, free_width = multipole.moments(free, det, lat.pos)
    same_site = multipole.field_from_sources(lat, [(0.0, 1.0), (0.0, -1.0)])
    same = multipole.response_delta(
        lat, initial, det, same_site, 1, free_centroid, free_width
    )
    neutral_field = multipole.field_from_sources(lat, multipole.build_quadrupole(1.0))
    neutral = multipole.response_delta(
        lat, initial, det, neutral_field, 0, free_centroid, free_width
    )
    rows = []
    for separation in (1.0, 2.0):
        for route in ("unit_weight", "coefficient_two"):
            base = multipole.field_from_sources(lat, multipole.build_quadrupole(separation))
            field = base * strengths[route] / multipole.SOURCE_STRENGTH
            centroid, width = multipole.response_delta(
                lat, initial, det, field, 1, free_centroid, free_width
            )
            rows.append(
                {
                    "separation": separation,
                    "held_separation": separation == 2.0,
                    "route": route,
                    "held_strength": route == "coefficient_two",
                    "centroid": centroid,
                    "width": width,
                }
            )
    by_key = {(row["separation"], row["route"]): row for row in rows}
    check(
        "signed deletion is exact and the frozen quadrupole 2x2 separates held strength from held separation",
        max(abs(value) for value in (*same, *neutral)) == 0
        and max(abs(row["centroid"]) for row in rows) < 3e-14
        and min(row["width"] for row in rows) > 0
        and by_key[(1.0, "coefficient_two")]["width"]
        > by_key[(1.0, "unit_weight")]["width"]
        and by_key[(2.0, "coefficient_two")]["width"]
        > by_key[(2.0, "unit_weight")]["width"]
        and by_key[(2.0, "unit_weight")]["width"]
        > by_key[(1.0, "unit_weight")]["width"]
        and by_key[(2.0, "coefficient_two")]["width"]
        > by_key[(1.0, "coefficient_two")]["width"],
        {
            "same_site_deletion": same,
            "neutral_test_matter": neutral,
            "rows": rows,
            "source_interface": "signed scalar density, not a positive occupation alone",
            "physical_test_matter_readout": False,
        },
    )


def training_power_law(
    field_values: dict[int, list[float]],
    anchors: dict[int, impact.AnchorDiagnostic],
) -> tuple[float, float, list[float]]:
    training = impact.B_VALUES[:3]
    held = impact.B_VALUES[3:]
    xs = np.log([anchors[b].realized_mean for b in training])
    ys = np.log([abs(impact._mean(field_values[b])) for b in training])
    alpha, log_coefficient = np.polyfit(xs, ys, 1)
    residuals = [
        float(
            math.log(abs(impact._mean(field_values[b])))
            - (log_coefficient + alpha * math.log(anchors[b].realized_mean))
        )
        for b in held
    ]
    return float(alpha), float(log_coefficient), residuals


def impact_no_refit_controls() -> None:
    print("\nIMPACT-PARAMETER NO-REFIT HOLDOUT")
    summaries, zero_delta, zero_field, values, anchors = impact._measure_family(impact.FAMILY)
    rows = []
    for key in ("instantaneous", "forward-only", "dynamic(c=1)", "dynamic(c=0.5)"):
        alpha, log_coefficient, held = training_power_law(values[key], anchors)
        rows.append(
            {
                "field": key,
                "training_alpha_b5_b7": alpha,
                "training_log_coefficient": log_coefficient,
                "held_log_residuals_b8_b10": held,
                "maximum_held_log_residual": max(abs(value) for value in held),
                "all_row_alpha": summaries[key].alpha,
                "all_row_R2": summaries[key].r2,
            }
        )
    by_name = {row["field"]: row for row in rows}
    check(
        "the frozen b5/b6/b7 fit predicts static held b8/b10 without refit and exposes the dynamic held deviations",
        zero_delta == zero_field == 0
        and by_name["instantaneous"]["maximum_held_log_residual"] < 0.03
        and by_name["forward-only"]["maximum_held_log_residual"] < 0.01
        and by_name["dynamic(c=1)"]["maximum_held_log_residual"] > 0.20
        and by_name["dynamic(c=0.5)"]["maximum_held_log_residual"] > 0.40,
        {
            "training_b": impact.B_VALUES[:3],
            "held_b": impact.B_VALUES[3:],
            "rows": rows,
            "refits_on_held": 0,
            "dynamic_deviation_is_route_specific": True,
            "physical_source_EG": False,
        },
    )


def nv_phase_controls(strengths: dict[str, float]) -> None:
    print("\nDIAMOND / NV IDEAL PHASE RECEIVER")
    theorem_ok, theorem_rows = nv.run_checks()
    frequency = 1_000.0
    delay = 1e-7
    density_rows = {
        route: nv.lockin_result(strength, frequency, delay)
        for route, strength in strengths.items()
    }
    amplitude_rows = {
        route: nv.lockin_result(math.sqrt(strength), frequency, delay)
        for route, strength in strengths.items()
    }
    phases = [row.phase_rad for row in (*density_rows.values(), *amplitude_rows.values())]
    check(
        "the ideal NV receiver preserves phase/sign controls but does not select occupation versus coherent-amplitude normalization",
        theorem_ok
        and max(phases) - min(phases) < 3e-14
        and density_rows["coefficient_two"].y_numeric > density_rows["unit_weight"].y_numeric > 0
        and amplitude_rows["coefficient_two"].y_numeric
        > amplitude_rows["unit_weight"].y_numeric
        > 0,
        {
            "theorem_checks": theorem_rows,
            "density_adapter": {key: asdict(value) for key, value in density_rows.items()},
            "amplitude_adapter": {key: asdict(value) for key, value in amplitude_rows.items()},
            "normalization_selected_by_ideal_phase_map": False,
            "signed_phase_history_from_Cycle417_compiled": False,
            "NV_coupling_or_signal_budget_derived": False,
        },
    )


def exact_failure_and_spillover_inventory() -> None:
    print("\nEXACT LIVE INTERFACE COORDINATES")
    inventory = {
        "closed": (
            "Cycle416-to-seven-M2 source/scalar-field E/G and inverse",
            "reservoir-plus-field occupation conservation",
            "Cycle417 coherent retarded/static port fanout without expectation feedback",
            "diagnostic scalar Cycle213/216 linear response at actual held strengths",
            "legacy deletion, velocity-reversal, signed-profile, no-refit, and ideal-phase controls",
        ),
        "live_coordinates": {
            "port_consumption_and_cleanup": "not constructed",
            "global_Cycle417_fanout_resource_transfer": "not constructed; mediator plus ports maps 1 to 3",
            "port_or_mediator_to_signed_profile": "not constructed",
            "hard_core_field_to_Cycle213_216_physical_EG": "not constructed",
            "static_K_inverse_as_local_reversible_update": "not constructed",
            "physical_M2_test_matter_force_or_detector": "not constructed",
            "source_motion_recoil_and_carried_profile": "not constructed",
            "NV_transfer_coefficient_and_signal_budget": "not constructed",
        },
        "spillover": {
            "time": "legacy layer, velocity, frequency, and delay parameters lack an admitted Record clock/rate",
            "Born": "normalized squared-array weights are readouts without occurrence or frequency law",
            "matter": "test packets/force responses are not a common physical-M2 matter/recoil compiler",
            "Records": "Cycle417 ports and legacy detector values have no Record typing, append, or protection law",
        },
        "negative_claim": False,
        "axiom_pressure": False,
    }
    check(
        "the bridge inventory keeps unfinished physical interfaces and TOE-lane spillover explicit",
        len(inventory["live_coordinates"]) == 8
        and set(inventory["spillover"]) == {"time", "Born", "matter", "Records"}
        and not inventory["negative_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 420: PHYSICAL SOURCE / PREDICTION BRIDGE CONTRACT")
    note_contract()
    source_type_contract_controls()
    hard_core_lift_controls()
    strengths = held_coherent_port_controls()
    cycle417_fanout_resource_boundary()
    common_dynamic_static_controls(strengths)
    causal_ratio_controls(strengths)
    moving_odd_controls(strengths)
    quadrupole_width_controls(strengths)
    impact_no_refit_controls()
    nv_phase_controls(strengths)
    exact_failure_and_spillover_inventory()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_SOURCE_PREDICTION_BRIDGE_CONTRACT_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_SOURCE_PREDICTION_BRIDGE_CONTRACT_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
