#!/usr/bin/env python3
"""Solve the reduced orbital-basis two-electron helium-like companion."""

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
from scripts.atomic_two_body_runtime import solve_two_electron_atomic_model  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dimension",
        type=int,
        default=3,
        help="spatial dimension; the retained atomic lane currently uses d=3",
    )
    parser.add_argument(
        "--nuclear-charge",
        type=float,
        default=2.0,
        help="effective nuclear charge in units of the reference one-body coupling",
    )
    parser.add_argument(
        "--reference-coupling",
        type=float,
        help="override the retained d=3 reference coupling",
    )
    parser.add_argument(
        "--nuclear-coupling",
        type=float,
        help="explicit one-body nuclear coupling; overrides --nuclear-charge scaling",
    )
    parser.add_argument(
        "--electron-repulsion-coupling",
        type=float,
        help="explicit e-e repulsion coupling; defaults to the retained reference coupling",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing used to scale the Laplacian and Coulomb radius",
    )
    parser.add_argument(
        "--nuclear-softening-radius",
        type=float,
        help="softening radius for the nuclear Coulomb potential; defaults to lattice spacing",
    )
    parser.add_argument(
        "--repulsion-softening-radius",
        type=float,
        help="softening radius for the e-e Coulomb kernel; defaults to lattice spacing",
    )
    parser.add_argument(
        "--repulsion-profile",
        choices=("hard_floor", "plummer", "erf_softcore", "exp_softcore"),
        default="hard_floor",
        help="short-distance e-e repulsion profile used in the two-body kernel",
    )
    parser.add_argument(
        "--repulsion-quadrature-order",
        type=int,
        default=1,
        help="subcell quadrature order used to average the e-e kernel over each cell pair",
    )
    parser.add_argument(
        "--nuclear-profile",
        choices=("hard_floor", "plummer", "shifted", "erf_softcore", "exp_softcore"),
        default="hard_floor",
        help="short-distance nuclear core profile used in the one-body sector",
    )
    parser.add_argument(
        "--nuclear-quadrature-order",
        type=int,
        default=1,
        help="subcell quadrature order used to average the nuclear core over each lattice cell",
    )
    parser.add_argument(
        "--nuclear-counterterm-strength",
        type=float,
        default=0.0,
        help="dimensionless repulsive Gaussian UV counterterm strength",
    )
    parser.add_argument(
        "--nuclear-counterterm-radius",
        type=float,
        help="Gaussian UV counterterm radius; defaults to the nuclear softening radius",
    )
    parser.add_argument(
        "--kinetic-stencil",
        choices=("three_point", "five_point"),
        default="three_point",
        help="discrete kinetic stencil used in the one-body sector",
    )
    parser.add_argument(
        "--max-orbitals",
        type=int,
        default=16,
        help="maximum number of negative one-body orbitals kept in the reduced basis",
    )
    parser.add_argument(
        "--max-virtual-orbitals",
        type=int,
        default=0,
        help="number of low-lying positive-energy orbitals added as virtual correlation channels",
    )
    parser.add_argument(
        "--n-eig",
        type=int,
        default=40,
        help="number of one-body eigenpairs to request before truncation",
    )
    parser.add_argument(
        "--basis-sweep",
        type=int,
        nargs="*",
        default=(4, 6, 8, 10, 12, 14, 16),
        help="reduced-basis sweep sizes used for a small convergence table",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_solver.json",
        help="machine-readable helium solver output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    solution = solve_two_electron_atomic_model(
        dimension=args.dimension,
        nuclear_charge=args.nuclear_charge,
        reference_coupling=args.reference_coupling,
        nuclear_coupling=args.nuclear_coupling,
        electron_repulsion_coupling=args.electron_repulsion_coupling,
        lattice_spacing=args.lattice_spacing,
        nuclear_softening_radius=args.nuclear_softening_radius,
        repulsion_softening_radius=args.repulsion_softening_radius,
        nuclear_profile=args.nuclear_profile,
        nuclear_quadrature_order=args.nuclear_quadrature_order,
        repulsion_profile=args.repulsion_profile,
        repulsion_quadrature_order=args.repulsion_quadrature_order,
        nuclear_counterterm_strength=args.nuclear_counterterm_strength,
        nuclear_counterterm_radius=args.nuclear_counterterm_radius,
        kinetic_stencil=args.kinetic_stencil,
        max_orbitals=args.max_orbitals,
        max_virtual_orbitals=args.max_virtual_orbitals,
        n_eig=args.n_eig,
        basis_sweep=tuple(args.basis_sweep),
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "solution": solution,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    singlet = solution["two_electron"]["singlet"]
    triplet = solution["two_electron"]["triplet"]
    print()
    print("Atomic Helium Solver")
    print("====================")
    print(
        f"- He+ one-body ground energy: "
        f"{solution['helium_ion_reference']['ground_energy']:.6f}."
    )
    print(
        f"- Two-electron singlet ground energy: "
        f"{singlet['ground_energy']:.6f}."
    )
    if triplet["ground_energy"] is not None:
        print(
            f"- Two-electron triplet ground energy: "
            f"{triplet['ground_energy']:.6f}."
        )
    print(
        f"- Ionization energy on the current reduced basis: "
        f"{solution['two_electron']['ionization_energy']:.6f}."
    )
    print(f"- Wrote solver output to {args.write_json}.")


if __name__ == "__main__":
    main()
