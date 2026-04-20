#!/usr/bin/env python3
"""Scan lattice spacing at fixed physical box for one-body observables."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, write_json  # noqa: E402
from scripts.atomic_one_body_runtime import benchmark_one_body_candidate  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimension", type=int, default=3)
    parser.add_argument("--reference-coupling", type=float, default=1.595)
    parser.add_argument("--nuclear-charge", type=float, default=2.0)
    parser.add_argument(
        "--lattice-spacings",
        type=float,
        nargs="*",
        default=(1.0, 0.8, 2.0 / 3.0, 4.0 / 7.0),
    )
    parser.add_argument("--softening-multiplier", type=float, default=0.75)
    parser.add_argument(
        "--nuclear-profile",
        choices=("hard_floor", "plummer", "shifted", "erf_softcore", "exp_softcore"),
        default="hard_floor",
    )
    parser.add_argument("--nuclear-quadrature-order", type=int, default=1)
    parser.add_argument("--nuclear-counterterm-strength", type=float, default=0.0)
    parser.add_argument("--nuclear-counterterm-radius", type=float)
    parser.add_argument(
        "--kinetic-stencil",
        choices=("three_point", "five_point"),
        default="three_point",
    )
    parser.add_argument("--max-orbitals", type=int, default=16)
    parser.add_argument("--n-eig", type=int, default=40)
    parser.add_argument("--reference-spacing", type=float, default=1.0)
    parser.add_argument("--reference-sizes", type=int, nargs="*")
    parser.add_argument("--min-size", type=int, default=8)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_spacing_scan.json",
    )
    args = parser.parse_args()

    reference_sizes = (
        tuple(int(value) for value in args.reference_sizes)
        if args.reference_sizes
        else None
    )
    spacings = [float(value) for value in args.lattice_spacings]
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    for index, spacing in enumerate(spacings, start=1):
        scan_started = time.perf_counter()
        benchmark = benchmark_one_body_candidate(
            dimension=int(args.dimension),
            reference_coupling=float(args.reference_coupling),
            nuclear_charge=float(args.nuclear_charge),
            lattice_spacing=float(spacing),
            softening_multiplier=float(args.softening_multiplier),
            nuclear_profile=str(args.nuclear_profile),
            nuclear_quadrature_order=int(args.nuclear_quadrature_order),
            nuclear_counterterm_strength=float(args.nuclear_counterterm_strength),
            nuclear_counterterm_radius=args.nuclear_counterterm_radius,
            kinetic_stencil=str(args.kinetic_stencil),
            max_orbitals=int(args.max_orbitals),
            n_eig=int(args.n_eig),
            fixed_physical_box=True,
            reference_spacing=float(args.reference_spacing),
            reference_sizes=reference_sizes,
            min_size=int(args.min_size),
        )
        benchmark["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
        rows.append(benchmark)
        scores = benchmark["metrics"]["scores"]
        print(
            f"[{index}/{len(spacings)}] "
            f"a={spacing:.6f} sizes={benchmark['parameters']['active_sizes']} "
            f"H={benchmark['metrics']['relative_errors']['hydrogen_ground']:.4%} "
            f"He+={benchmark['metrics']['relative_errors']['helium_ion_ground']:.4%} "
            f"rms={scores['one_body_rms_relative_error']:.6f}",
            flush=True,
        )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "scan_configuration": {
            "dimension": int(args.dimension),
            "reference_coupling": float(args.reference_coupling),
            "nuclear_charge": float(args.nuclear_charge),
            "lattice_spacings": spacings,
            "softening_multiplier": float(args.softening_multiplier),
            "nuclear_profile": str(args.nuclear_profile),
            "nuclear_quadrature_order": int(args.nuclear_quadrature_order),
            "nuclear_counterterm_strength": float(args.nuclear_counterterm_strength),
            "nuclear_counterterm_radius": (
                float(args.nuclear_counterterm_radius)
                if args.nuclear_counterterm_radius is not None
                else None
            ),
            "kinetic_stencil": str(args.kinetic_stencil),
            "max_orbitals": int(args.max_orbitals),
            "n_eig": int(args.n_eig),
            "reference_spacing": float(args.reference_spacing),
            "reference_sizes": (
                [int(size) for size in reference_sizes]
                if reference_sizes is not None
                else None
            ),
            "min_size": int(args.min_size),
        },
        "rows": rows,
        "best_by_one_body_rms": min(
            rows,
            key=lambda row: (
                float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic One-Body Spacing Scan")
    print("============================")
    print(
        f"- Best spacing candidate: a="
        f"{output_payload['best_by_one_body_rms']['parameters']['lattice_spacing']:.6f} "
        f"with RMS={output_payload['best_by_one_body_rms']['metrics']['scores']['one_body_rms_relative_error']:.6f}."
    )
    print(f"- Wrote spacing scan to {args.write_json}.")


if __name__ == "__main__":
    main()
