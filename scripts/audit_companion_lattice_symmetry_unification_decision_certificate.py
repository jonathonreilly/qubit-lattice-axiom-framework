#!/usr/bin/env python3
"""Compact certificate for a stipulated finite lattice-symmetry proxy census.

The primary decision runner prints a useful exploratory report, but its stdout
can be clipped when embedded in an audit packet.  This companion recomputes the
same finite surface and emits a compact, complete certificate for the
load-bearing rows. It also checks the sign and selection-predicate counts with
a second predicate implementation instead of trusting the primary runner's
summary. The certificate makes no framework-derived physical interpretation.
"""

from __future__ import annotations

import hashlib
import inspect
import math
import sys
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/lattice_symmetry_unification_decision.py",
    "scripts/lattice_mirror_hybrid.py",
)

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts import lattice_symmetry_unification_decision as decision  # noqa: E402
from scripts import lattice_mirror_hybrid as helper  # noqa: E402


PASS = 0
FAIL = 0

CONTRACT_MAX_DY = (3, 4, 5, 6)
CONTRACT_GEOMETRIES = {
    "narrow_center": (4,),
    "wide_center": (3, 4, 5),
    "wide_outer": (4, 5, 6),
}
CONTRACT_OFFSETS = (-1, 0, 1)
CONTRACT_B_VALUES = (2, 3, 4, 5, 6, 7, 8, 10, 13, 16, 19)
CONTRACT_N_LAYERS = 40
CONTRACT_HALF_WIDTH = 20
CONTRACT_FIELD_STRENGTH = 0.1
CONTRACT_FIELD_SOFTENER = 0.1
CONTRACT_BETA = 0.8
CONTRACT_K = 5.0
CONTRACT_LAM = 10.0
CONTRACT_N_YBINS = 8
CONTRACT_CANONICAL_GEOMETRY = "wide_center"
CONTRACT_CANONICAL_OFFSET = 1
CONTRACT_THRESHOLDS = (1.0e-12, 1.0e-9, 0.10, 0.03, 0.80)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"CHECK|{tag}|{label}{suffix}")


def sha256(rel_path: str) -> str:
    return hashlib.sha256((ROOT / rel_path).read_bytes()).hexdigest()


def displayed_residual(value: float) -> float:
    """Serialize cancellation-scale residuals by their certified tolerance."""
    if math.isfinite(value) and abs(value) <= CONTRACT_THRESHOLDS[0]:
        return 0.0
    return value


def contract_mismatches() -> list[str]:
    """Compare the imported computation surface with the declared contract."""
    actual = {
        "max_dy": tuple(decision.MAX_DY_VALUES),
        "geometries": {key: tuple(value) for key, value in decision.GEOMETRIES.items()},
        "offsets": tuple(decision.TRADEOFF_OFFSETS),
        "b_values": tuple(decision.B_VALUES),
        "n_layers": decision.N_LAYERS,
        "half_width": decision.HALF_WIDTH,
        "field_strength_default": inspect.signature(decision.field_for_mass)
        .parameters["strength"]
        .default,
        "beta": helper.BETA,
        "k": helper.K,
        "lam": helper.LAM,
        "n_ybins": helper.N_YBINS,
        "canonical_geometry": decision.CANONICAL_GEOMETRY,
        "canonical_offset": decision.CANONICAL_OFFSET,
        "thresholds": (
            decision.RETAIN_BORN_MAX,
            decision.RETAIN_K0_MAX,
            decision.RETAIN_MI_MIN,
            decision.RETAIN_DECOH_MIN,
            decision.RETAIN_DISTANCE_R2_MIN,
        ),
    }
    expected = {
        "max_dy": CONTRACT_MAX_DY,
        "geometries": CONTRACT_GEOMETRIES,
        "offsets": CONTRACT_OFFSETS,
        "b_values": CONTRACT_B_VALUES,
        "n_layers": CONTRACT_N_LAYERS,
        "half_width": CONTRACT_HALF_WIDTH,
        "field_strength_default": CONTRACT_FIELD_STRENGTH,
        "beta": CONTRACT_BETA,
        "k": CONTRACT_K,
        "lam": CONTRACT_LAM,
        "n_ybins": CONTRACT_N_YBINS,
        "canonical_geometry": CONTRACT_CANONICAL_GEOMETRY,
        "canonical_offset": CONTRACT_CANONICAL_OFFSET,
        "thresholds": CONTRACT_THRESHOLDS,
    }
    return [key for key in expected if actual[key] != expected[key]]


def setup_matches_contract(setup: decision.Setup, max_dy: int) -> bool:
    expected_positions = [
        (float(layer), float(y))
        for layer in range(CONTRACT_N_LAYERS)
        for y in range(-CONTRACT_HALF_WIDTH, CONTRACT_HALF_WIDTH + 1)
    ]
    if setup.positions != expected_positions:
        return False
    if setup.barrier_layer != CONTRACT_N_LAYERS // 3:
        return False
    if setup.gravity_layer != 2 * CONTRACT_N_LAYERS // 3:
        return False
    if setup.source != [setup.node_map[(0, 0)]]:
        return False
    expected_detector = [
        setup.node_map[(CONTRACT_N_LAYERS - 1, y)]
        for y in range(-CONTRACT_HALF_WIDTH, CONTRACT_HALF_WIDTH + 1)
    ]
    if setup.detector != expected_detector:
        return False
    expected_barrier = [
        setup.node_map[(setup.barrier_layer, y)]
        for y in range(-CONTRACT_HALF_WIDTH, CONTRACT_HALF_WIDTH + 1)
    ]
    if setup.barrier_nodes != expected_barrier:
        return False
    expected_adj: dict[int, list[int]] = {}
    for layer in range(CONTRACT_N_LAYERS - 1):
        for y in range(-CONTRACT_HALF_WIDTH, CONTRACT_HALF_WIDTH + 1):
            source = setup.node_map[(layer, y)]
            expected_adj[source] = [
                setup.node_map[(layer + 1, target_y)]
                for target_y in range(
                    max(-CONTRACT_HALF_WIDTH, y - max_dy),
                    min(CONTRACT_HALF_WIDTH, y + max_dy) + 1,
                )
            ]
    if setup.adj != expected_adj:
        return False
    for mass_y in CONTRACT_B_VALUES:
        actual_field = decision.field_for_mass(
            setup.positions,
            setup.node_map,
            setup.gravity_layer,
            mass_y,
            strength=CONTRACT_FIELD_STRENGTH,
        )
        mass_x, mass_y_float = setup.positions[
            setup.node_map[(setup.gravity_layer, mass_y)]
        ]
        expected_field = [
            CONTRACT_FIELD_STRENGTH
            / (math.hypot(x - mass_x, y - mass_y_float) + CONTRACT_FIELD_SOFTENER)
            for x, y in setup.positions
        ]
        if actual_field != expected_field:
            return False
    return True


def independent_retained(
    metrics: dict[str, float],
    distance_fit: decision.DistanceFit | None,
) -> bool:
    """Second implementation of the documented row-retention conjunction."""
    finite = all(
        math.isfinite(metrics[key])
        for key in ("born", "gravity_k0", "mi", "decoh", "gravity")
    )
    return bool(
        finite
        and metrics["born"] <= CONTRACT_THRESHOLDS[0]
        and abs(metrics["gravity_k0"]) <= CONTRACT_THRESHOLDS[1]
        and metrics["mi"] >= CONTRACT_THRESHOLDS[2]
        and metrics["decoh"] >= CONTRACT_THRESHOLDS[3]
        and metrics["gravity"] > 0.0
        and distance_fit is not None
        and distance_fit.alpha < 0.0
        and distance_fit.r2 >= CONTRACT_THRESHOLDS[4]
    )


def main() -> int:
    print("LATTICE_SYMMETRY_FINITE_PROXY_CENSUS_CERTIFICATE_V2")
    print(
        "SHA256_PIN|companion|"
        f"{sha256('scripts/audit_companion_lattice_symmetry_unification_decision_certificate.py')}"
    )
    print(
        "SHA256_PIN|primary|"
        f"{sha256('scripts/lattice_symmetry_unification_decision.py')}"
    )
    print(
        "SHA256_PIN|helper|"
        f"{sha256('scripts/lattice_mirror_hybrid.py')}"
    )
    print(
        "SCOPE|model=stipulated_directed_2d_layer_dag|"
        "max_dy=3,4,5,6|"
        "geometries=narrow_center,wide_center,wide_outer|"
        "offsets=-1,0,+1|strength=0.1"
    )
    mismatches = contract_mismatches()
    check(
        "imported finite/model constants equal the declared contract",
        not mismatches,
        "mismatches=" + ",".join(mismatches) if mismatches else "",
    )
    if mismatches:
        print(f"SUMMARY|PASS={PASS}|FAIL={FAIL}")
        return 1

    setups = {max_dy: decision.build_setup(max_dy) for max_dy in CONTRACT_MAX_DY}
    setup_failures = [
        str(max_dy)
        for max_dy, setup in setups.items()
        if not setup_matches_contract(setup, max_dy)
    ]
    check(
        "directed lattice, boundaries, source, detector, and field equal the declared contract",
        not setup_failures,
        "max_dy=" + ",".join(setup_failures) if setup_failures else "",
    )
    if setup_failures:
        print(f"SUMMARY|PASS={PASS}|FAIL={FAIL}")
        return 1
    no_barrier_fits: dict[int, decision.DistanceFit | None] = {}
    barrier_curves: dict[int, list[tuple[int, float]]] = {}
    canonical: dict[int, dict[str, float]] = {}

    for max_dy, setup in setups.items():
        canonical[max_dy] = decision.barrier_metrics(
            setup,
            decision.GEOMETRIES[decision.CANONICAL_GEOMETRY],
            decision.CANONICAL_OFFSET,
        )
        barrier = decision.aperture_for_rows(
            setup,
            decision.GEOMETRIES[decision.CANONICAL_GEOMETRY],
        )["blocked"]
        barrier_curves[max_dy] = decision.distance_curve(setup, barrier)
        no_barrier_fits[max_dy] = decision.fit_tail(
            decision.distance_curve(setup, set())
        )

    print("SECTION|CANONICAL_SWEEP_CERTIFICATE|rows=4")
    for max_dy in CONTRACT_MAX_DY:
        metrics = canonical[max_dy]
        retained = decision.retained(metrics, no_barrier_fits[max_dy])
        print(
            "C|{md}|mass={mass:.0f}|mi={mi:.6f}|dtv={dtv:.6f}|decoh={decoh:.6f}|"
            "gravity={gravity:+.12e}|k0={k0:+.3e}|born={born:.3e}|retained={retained}".format(
                md=max_dy,
                mass=metrics["mass_y"],
                mi=metrics["mi"],
                dtv=metrics["dtv"],
                decoh=metrics["decoh"],
                gravity=metrics["gravity"],
                k0=metrics["gravity_k0"],
                born=displayed_residual(metrics["born"]),
                retained=int(retained),
            )
        )

    print("SECTION|BARRIER_DISTANCE_CURVE_CERTIFICATE|curves=4|points=44")
    for max_dy in CONTRACT_MAX_DY:
        curve = barrier_curves[max_dy]
        points = ",".join(f"{b}:{delta:+.8f}" for b, delta in curve)
        print(f"B|{max_dy}|{points}")

    print("SECTION|NO_BARRIER_DISTANCE_FIT_CERTIFICATE|fits=4")
    for max_dy in CONTRACT_MAX_DY:
        fit = no_barrier_fits[max_dy]
        if fit is None:
            print(f"N|{max_dy}|none")
        else:
            print(
                f"N|{max_dy}|peak={fit.peak_b}|alpha={fit.alpha:+.8f}|r2={fit.r2:.8f}"
            )

    expected_keys = {
        (max_dy, geometry, offset)
        for max_dy in CONTRACT_MAX_DY
        for geometry in CONTRACT_GEOMETRIES
        for offset in CONTRACT_OFFSETS
    }
    rows: dict[
        tuple[int, str, int],
        tuple[dict[str, float], bool, bool],
    ] = {}
    geometry_codes = {
        "narrow_center": "nc",
        "wide_center": "wc",
        "wide_outer": "wo",
    }

    print(
        "SECTION|TRADEOFF_36_ROW_CERTIFICATE|rows=36|"
        "flags=three_slit,mi_purity,k0,distance,positive_shift,primary_predicate,second_predicate"
    )
    print("ALIASES|nc=narrow_center|wc=wide_center|wo=wide_outer")
    for max_dy in CONTRACT_MAX_DY:
        setup = setups[max_dy]
        fit = no_barrier_fits[max_dy]
        for geometry, upper_rows_tuple in CONTRACT_GEOMETRIES.items():
            upper_rows = list(upper_rows_tuple)
            for offset in CONTRACT_OFFSETS:
                metrics = decision.barrier_metrics(setup, upper_rows, offset)
                primary_retained = decision.retained(metrics, fit)
                second_retained = independent_retained(metrics, fit)
                key = (max_dy, geometry, offset)
                rows[key] = (metrics, primary_retained, second_retained)
                born_pass = metrics["born"] <= CONTRACT_THRESHOLDS[0]
                coexistence_pass = (
                    metrics["mi"] >= CONTRACT_THRESHOLDS[2]
                    and metrics["decoh"] >= CONTRACT_THRESHOLDS[3]
                )
                k0_pass = abs(metrics["gravity_k0"]) <= CONTRACT_THRESHOLDS[1]
                distance_pass = bool(
                    fit is not None
                    and fit.alpha < 0.0
                    and fit.r2 >= CONTRACT_THRESHOLDS[4]
                )
                flags = "".join(
                    str(int(value))
                    for value in (
                        born_pass,
                        coexistence_pass,
                        k0_pass,
                        distance_pass,
                        metrics["gravity"] > 0.0,
                        primary_retained,
                        second_retained,
                    )
                )
                print(
                    "T|{md}|{geometry}|{offset:+d}|{born:.2e}|{mi:.4f}|"
                    "{decoh:.4f}|{gravity:+.8f}|{flags}".format(
                        md=max_dy,
                        geometry=geometry_codes[geometry],
                        offset=offset,
                        born=displayed_residual(metrics["born"]),
                        mi=metrics["mi"],
                        decoh=metrics["decoh"],
                        gravity=metrics["gravity"],
                        flags=flags,
                    )
                )

    print("SECTION|INDEPENDENT_SIGN_AND_COUNT_CHECK")
    raw_gravities = [metrics["gravity"] for metrics, _, _ in rows.values()]
    primary_positive_count = sum(gravity > 0.0 for gravity in raw_gravities)
    second_nonpositive_count = sum(
        math.isfinite(gravity) and gravity <= 0.0 for gravity in raw_gravities
    )
    primary_retained_count = sum(primary for _, primary, _ in rows.values())
    second_retained_count = sum(second for _, _, second in rows.values())
    born_clean_count = sum(
        metrics["born"] <= CONTRACT_THRESHOLDS[0] for metrics, _, _ in rows.values()
    )
    coexistence_count = sum(
        metrics["mi"] >= CONTRACT_THRESHOLDS[2]
        and metrics["decoh"] >= CONTRACT_THRESHOLDS[3]
        for metrics, _, _ in rows.values()
    )
    barrier_positive_count = sum(
        delta > 0.0
        for curve in barrier_curves.values()
        for _, delta in curve
    )

    check(
        "exact Cartesian key coverage",
        set(rows) == expected_keys,
        f"observed={len(rows)} expected={len(expected_keys)}",
    )
    check(
        "all 36 centroid-shift values are finite",
        all(math.isfinite(value) for value in raw_gravities),
    )
    check(
        "primary positive-centroid-shift count is 0/36",
        primary_positive_count == 0,
        f"count={primary_positive_count}/36",
    )
    check(
        "independent nonpositive-centroid-shift count is 36/36",
        second_nonpositive_count == 36,
        f"count={second_nonpositive_count}/36",
    )
    check(
        "strict negative margin exists",
        max(raw_gravities) < 0.0,
        f"max={max(raw_gravities):+.12e}",
    )
    check(
        "primary and independent retention predicates agree",
        all(primary == second for _, primary, second in rows.values()),
    )
    check(
        "primary selection-predicate count is 0/36",
        primary_retained_count == 0,
        f"count={primary_retained_count}/36",
    )
    check(
        "independent selection-predicate count is 0/36",
        second_retained_count == 0,
        f"count={second_retained_count}/36",
    )
    check(
        "three-slit residual count within tolerance is 36/36",
        born_clean_count == 36,
        f"count={born_clean_count}/36",
    )
    check(
        "MI plus purity-deficit proxy count is 36/36",
        coexistence_count == 36,
        f"count={coexistence_count}/36",
    )
    check(
        "all 44 barrier-distance centroid-shift points are nonpositive",
        barrier_positive_count == 0,
        f"positive={barrier_positive_count}/44",
    )

    canonical_consistent = all(
        math.isclose(
            canonical[max_dy]["gravity"],
            rows[
                (max_dy, decision.CANONICAL_GEOMETRY, decision.CANONICAL_OFFSET)
            ][0]["gravity"],
            rel_tol=0.0,
            abs_tol=0.0,
        )
        for max_dy in CONTRACT_MAX_DY
    )
    check("canonical rows equal their tradeoff-map rows", canonical_consistent)

    if FAIL:
        print(f"SUMMARY|PASS={PASS}|FAIL={FAIL}")
        return 1

    decision_tag = (
        "FINITE_CENSUS_NONPOSITIVE"
        if primary_retained_count == 0
        and primary_positive_count == 0
        and coexistence_count > 0
        else "NOT_CERTIFIED"
    )
    print("SECTION|FINAL_DECISION_CERTIFICATE")
    print(f"COUNT|three_slit_residual_within_tolerance|{born_clean_count}/36")
    print(f"COUNT|mi_plus_purity_deficit_proxy|{coexistence_count}/36")
    print(f"COUNT|positive_centroid_shift|{primary_positive_count}/36")
    print(f"COUNT|selected_predicate|{primary_retained_count}/36")
    print(f"DECISION|{decision_tag}|scope=stipulated_finite_proxy_census_only")
    check(
        "finite proxy census is nonpositive",
        decision_tag == "FINITE_CENSUS_NONPOSITIVE",
    )
    print(f"SUMMARY|PASS={PASS}|FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
