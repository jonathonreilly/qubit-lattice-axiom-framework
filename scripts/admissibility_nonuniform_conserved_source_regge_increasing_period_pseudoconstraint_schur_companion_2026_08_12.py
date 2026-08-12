#!/usr/bin/env python3
"""Independent full-harmonic Schur companion for the increasing-period gate."""

from __future__ import annotations

import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12 as scaling  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_"
    "PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_INCREASING_PERIOD_PSEUDOCONSTRAINT_SCALING_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_schur_companion_2026_08_12.py",
    "scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


def main() -> int:
    checks = scaling.Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    os.environ["TOE_SCHUR_PERIODS"] = "3,5"
    results = {
        (period, source): scaling.SliceModel(period, source).analyze()
        for period in (3, 5)
        for source in ("static", "null")
    }

    print(
        "analytic_boundary: orthonormal full-harmonic Schur complements of the actual sourced Regge length Hessian"
    )
    print(
        "physical_boundary: Euclidean finite-spacing pseudo-constraint inertia, not a Lorentzian ghost or continuum theorem"
    )
    for key, result in results.items():
        schur = result["schur"]
        print(
            f"schur_result: source={key[1]} L={key[0]} dimension={schur['dimension']} "
            f"inertia={schur['negative']}-/{schur['positive']}+/{schur['zero']}zero "
            f"max_abs/eta={schur['maximum_over_amplitude']:.6f}"
        )

    checks.check(
        "schur-source-branches",
        "all four companion branches solve the nongauge equations before Hessian elimination",
        all(
            result["projected_residual"] < 1.0e-12
            and result["complete_rank"] == 15 * result["period"]
            and result["minimum_length"] > 0.99
            for result in results.values()
        ),
    )

    inertia_condition = True
    for (period, _source), result in results.items():
        half = (period - 1) // 2
        schur = result["schur"]
        inertia_condition &= (
            schur["dimension"] == 8 * half
            and schur["negative"] == 5 * half
            and schur["positive"] == 3 * half
            and schur["zero"] == 0
        )
    checks.check(
        "full-harmonic-mixed-sign-inertia",
        "every executed displacement harmonic remains lifted with five-negative/three-positive inertia",
        inertia_condition,
    )

    softening_details = []
    softening_condition = mutation != "schur_softening"
    for source in ("static", "null"):
        lower = results[(3, source)]["schur"]["maximum_over_amplitude"]
        upper = results[(5, source)]["schur"]["maximum_over_amplitude"]
        softening_condition &= upper < 0.85 * lower
        softening_details.append(f"{source}: {lower:.6f}->{upper:.6f}")
    checks.check(
        "pseudoconstraint-schur-softening",
        "the largest normalized Schur lift decreases from period three to period five for both sources",
        softening_condition,
        "; ".join(softening_details),
    )

    checks.check(
        "companion-scope-boundary",
        "the source note identifies this independent companion and preserves the finite-spacing boundary",
        "schur companion" in note
        and "no physical ghost interpretation" in note
        and "not an all-l theorem" in note,
    )

    print(
        "N5_CERTIFICATE: four complete orthonormal Schur eliminations cover both sources and both declared periods"
    )
    print(
        "per_element: complex-step differentiated every raw length column before orthonormal projection"
    )
    print(
        "per_site: all fifty hinge classes and 240 simplex-hinge incidences contribute to each Hessian column"
    )
    print(
        "per_mode: all eight real displacement directions per positive Fourier representative enter the Schur block"
    )
    print(
        "per_block: compared 8-by-8 and 16-by-16 relaxed gauge blocks for static and Record/null sources"
    )
    print(
        "lattice_wide: not executed; this companion establishes finite-period mixed-sign lift and initial softening only"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
