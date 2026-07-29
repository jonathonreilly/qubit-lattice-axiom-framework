#!/usr/bin/env python3
"""Compact audit certificate for the finite lattice-symmetry decision sweep.

The primary decision runner prints a useful exploratory report, but its stdout
can be clipped when embedded in an audit packet.  This companion recomputes the
same finite surface and emits a compact, complete certificate for the
load-bearing rows.  It also checks the sign and retention counts with a second
predicate implementation instead of trusting the primary runner's summary.
"""

from __future__ import annotations

import hashlib
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


PASS = 0
FAIL = 0


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
        and metrics["born"] <= 1.0e-12
        and abs(metrics["gravity_k0"]) <= 1.0e-9
        and metrics["mi"] >= 0.10
        and metrics["decoh"] >= 0.03
        and metrics["gravity"] > 0.0
        and distance_fit is not None
        and distance_fit.alpha < 0.0
        and distance_fit.r2 >= 0.80
    )


def main() -> int:
    print("LATTICE_SYMMETRY_UNIFICATION_SLICED_CERTIFICATE_V1")
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
        "SCOPE|max_dy=3,4,5,6|"
        "geometries=narrow_center,wide_center,wide_outer|"
        "offsets=-1,0,+1|strength=0.1"
    )

    check(
        "primary thresholds match independent predicate",
        (
            decision.RETAIN_BORN_MAX == 1.0e-12
            and decision.RETAIN_K0_MAX == 1.0e-9
            and decision.RETAIN_MI_MIN == 0.10
            and decision.RETAIN_DECOH_MIN == 0.03
            and decision.RETAIN_DISTANCE_R2_MIN == 0.80
        ),
    )

    setups = {max_dy: decision.build_setup(max_dy) for max_dy in decision.MAX_DY_VALUES}
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
    for max_dy in decision.MAX_DY_VALUES:
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
                born=metrics["born"],
                retained=int(retained),
            )
        )

    print("SECTION|BARRIER_DISTANCE_CURVE_CERTIFICATE|curves=4|points=44")
    for max_dy in decision.MAX_DY_VALUES:
        curve = barrier_curves[max_dy]
        points = ",".join(f"{b}:{delta:+.8f}" for b, delta in curve)
        print(f"B|{max_dy}|{points}")

    print("SECTION|NO_BARRIER_DISTANCE_FIT_CERTIFICATE|fits=4")
    for max_dy in decision.MAX_DY_VALUES:
        fit = no_barrier_fits[max_dy]
        if fit is None:
            print(f"N|{max_dy}|none")
        else:
            print(
                f"N|{max_dy}|peak={fit.peak_b}|alpha={fit.alpha:+.8f}|r2={fit.r2:.8f}"
            )

    expected_keys = {
        (max_dy, geometry, offset)
        for max_dy in decision.MAX_DY_VALUES
        for geometry in decision.GEOMETRIES
        for offset in decision.TRADEOFF_OFFSETS
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
        "flags=born,coexist,k0,distance,positive,primary_retained,second_retained"
    )
    print("ALIASES|nc=narrow_center|wc=wide_center|wo=wide_outer")
    for max_dy in decision.MAX_DY_VALUES:
        setup = setups[max_dy]
        fit = no_barrier_fits[max_dy]
        for geometry, upper_rows in decision.GEOMETRIES.items():
            for offset in decision.TRADEOFF_OFFSETS:
                metrics = decision.barrier_metrics(setup, upper_rows, offset)
                primary_retained = decision.retained(metrics, fit)
                second_retained = independent_retained(metrics, fit)
                key = (max_dy, geometry, offset)
                rows[key] = (metrics, primary_retained, second_retained)
                born_pass = metrics["born"] <= 1.0e-12
                coexistence_pass = metrics["mi"] >= 0.10 and metrics["decoh"] >= 0.03
                k0_pass = abs(metrics["gravity_k0"]) <= 1.0e-9
                distance_pass = bool(
                    fit is not None and fit.alpha < 0.0 and fit.r2 >= 0.80
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
                        born=metrics["born"],
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
        metrics["born"] <= 1.0e-12 for metrics, _, _ in rows.values()
    )
    coexistence_count = sum(
        metrics["mi"] >= 0.10 and metrics["decoh"] >= 0.03
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
        "all 36 gravity values are finite",
        all(math.isfinite(value) for value in raw_gravities),
    )
    check(
        "primary positive-gravity count is 0/36",
        primary_positive_count == 0,
        f"count={primary_positive_count}/36",
    )
    check(
        "independent nonpositive-gravity count is 36/36",
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
        "primary retained count is 0/36",
        primary_retained_count == 0,
        f"count={primary_retained_count}/36",
    )
    check(
        "independent retained count is 0/36",
        second_retained_count == 0,
        f"count={second_retained_count}/36",
    )
    check(
        "Born-clean count is 36/36",
        born_clean_count == 36,
        f"count={born_clean_count}/36",
    )
    check(
        "MI plus decoherence count is 36/36",
        coexistence_count == 36,
        f"count={coexistence_count}/36",
    )
    check(
        "all 44 barrier-distance points are nonpositive",
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
        for max_dy in decision.MAX_DY_VALUES
    )
    check("canonical rows equal their tradeoff-map rows", canonical_consistent)

    decision_tag = (
        "NEGATIVE"
        if primary_retained_count == 0
        and primary_positive_count == 0
        and coexistence_count > 0
        else "NOT_CERTIFIED"
    )
    print("SECTION|FINAL_DECISION_CERTIFICATE")
    print(f"COUNT|born_clean|{born_clean_count}/36")
    print(f"COUNT|mi_plus_decoherence|{coexistence_count}/36")
    print(f"COUNT|positive_gravity|{primary_positive_count}/36")
    print(f"COUNT|retained_one_family|{primary_retained_count}/36")
    print(f"DECISION|{decision_tag}|scope=finite_standard_strength_slice_only")
    check("finite decision is NEGATIVE", decision_tag == "NEGATIVE")
    print(f"SUMMARY|PASS={PASS}|FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
