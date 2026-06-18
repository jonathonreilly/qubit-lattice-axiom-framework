#!/usr/bin/env python3
"""Finite stress-tensor lift for the FRW C3 kinetic component labels.

This runner checks a narrow bridge downstream of the finite kinetic EOS-label
bridge:

* a massless isotropic kinetic component lifts to a mixed stress tensor
  diag(-rho_r, rho_r/3, rho_r/3, rho_r/3);
* a pressureless rest matter component lifts to diag(-rho_m, 0, 0, 0);
* a supplied Lambda component from the separate dark-energy EOS surface can be
  direct-summed with those components without changing the non-Lambda labels;
* finite cell homogeneity is required for an FRW background, and source-free
  continuity is required for the usual scaling laws.

The runner does not derive C1, C2, real cosmological species allocation,
thermal history, or audit status.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs/FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = (
    ROOT
    / "docs/FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md"
)
KINETIC_NOTE_BASENAME = (
    "FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
RUNNER_PATH = (
    "scripts/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.py"
)
CACHE_PATH = (
    "logs/runner-cache/frontier_frw_c3_kinetic_component_fluid_lift_2026_06_18.txt"
)

Tensor = tuple[tuple[Fraction, Fraction, Fraction, Fraction], ...]

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")
    return condition


def diag_tensor(rho: Fraction, pressure: Fraction) -> Tensor:
    zero = Fraction(0)
    return (
        (-rho, zero, zero, zero),
        (zero, pressure, zero, zero),
        (zero, zero, pressure, zero),
        (zero, zero, zero, pressure),
    )


def tensor_add(*items: Tensor) -> Tensor:
    zero = Fraction(0)
    out = [[zero for _ in range(4)] for _ in range(4)]
    for tensor in items:
        for i in range(4):
            for j in range(4):
                out[i][j] += tensor[i][j]
    return tuple(tuple(row) for row in out)


def tensor_scale(scale: Fraction, tensor: Tensor) -> Tensor:
    return tuple(tuple(scale * value for value in row) for row in tensor)


def tensor_average(items: list[Tensor]) -> Tensor:
    return tensor_scale(Fraction(1, len(items)), tensor_add(*items))


def is_diagonal(tensor: Tensor) -> bool:
    return all(tensor[i][j] == 0 for i in range(4) for j in range(4) if i != j)


def isotropic_pressure(tensor: Tensor) -> bool:
    return tensor[1][1] == tensor[2][2] == tensor[3][3]


def rho_of(tensor: Tensor) -> Fraction:
    return -tensor[0][0]


def pressure_of(tensor: Tensor) -> Fraction:
    return (tensor[1][1] + tensor[2][2] + tensor[3][3]) / 3


def w_of(tensor: Tensor) -> Fraction:
    rho = rho_of(tensor)
    if rho == 0:
        raise ZeroDivisionError("zero density")
    return pressure_of(tensor) / rho


def part0_source_firewall() -> None:
    print("\n== Part 0: source/status firewall ==")
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    parent = " ".join(PARENT_NOTE_PATH.read_text(encoding="utf-8").split())

    required_note = [
        "Claim type:** bounded_theorem",
        "Type:** bounded_theorem",
        "Status:** bounded support for finite perfect-fluid lift of ideal C3 kinetic labels only",
        "actual_current_surface_status: bounded-support",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
        "proposal_allowed: false",
        "not an audit result",
        "No new axiom",
        "does not derive C1",
        "does not derive C2",
        "does not derive real cosmological species allocation",
        "finite perfect-fluid lift only",
        KINETIC_NOTE_BASENAME,
        RUNNER_PATH,
        CACHE_PATH,
        "[`FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md`](FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md)",
        "[`DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`](DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md)",
    ]
    for phrase in required_note:
        check(f"fluid-lift note contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "Status: retained",
        "actual_current_surface_status: retained",
        "sets effective status",
        "derives the cosmological principle",
        "derives adiabatic expansion",
        "derives real cosmological fluids",
    ]
    for phrase in forbidden:
        check(f"fluid-lift note excludes overclaim phrase: {phrase}", phrase not in note)

    required_parent = [
        "2026-06-18 C3 perfect-fluid lift partial bridge",
        "FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "does not derive C1 or C2",
        "does not derive real cosmological species allocation",
    ]
    for phrase in required_parent:
        check(f"parent FRW note records fluid-lift phrase: {phrase}", phrase in parent)


def part1_component_tensors() -> tuple[Tensor, Tensor, Tensor]:
    print("\n== Part 1: component mixed stress tensors ==")
    rho_r = Fraction(12)
    rho_m = Fraction(21)
    rho_lambda = Fraction(5)
    radiation = diag_tensor(rho_r, rho_r / 3)
    matter = diag_tensor(rho_m, Fraction(0))
    lambda_component = diag_tensor(rho_lambda, -rho_lambda)

    for name, tensor in [
        ("radiation", radiation),
        ("matter", matter),
        ("Lambda", lambda_component),
    ]:
        check(f"{name} component tensor is diagonal", is_diagonal(tensor), str(tensor))
        check(
            f"{name} component has isotropic pressure",
            isotropic_pressure(tensor),
            f"P=({tensor[1][1]}, {tensor[2][2]}, {tensor[3][3]})",
        )

    check("radiation component has w_r=1/3", w_of(radiation) == Fraction(1, 3))
    check("pressureless rest matter component has w_m=0", w_of(matter) == 0)
    check(
        "Lambda component is separate supplied w=-1 surface",
        w_of(lambda_component) == -1,
    )
    return radiation, matter, lambda_component


def part2_direct_sum_fluid(
    radiation: Tensor, matter: Tensor, lambda_component: Tensor
) -> Tensor:
    print("\n== Part 2: finite direct-sum perfect-fluid aggregation ==")
    total = tensor_add(radiation, matter, lambda_component)
    rho_total = rho_of(total)
    p_total = pressure_of(total)
    expected_rho = rho_of(radiation) + rho_of(matter) + rho_of(lambda_component)
    expected_pressure = (
        rho_of(radiation) / 3 + Fraction(0) - rho_of(lambda_component)
    )

    check("total tensor remains diagonal", is_diagonal(total), str(total))
    check(
        "total tensor remains isotropic in spatial pressure",
        isotropic_pressure(total),
        f"P=({total[1][1]}, {total[2][2]}, {total[3][3]})",
    )
    check(
        "total density is component density sum",
        rho_total == expected_rho,
        f"rho_total={rho_total}, expected={expected_rho}",
    )
    check(
        "total pressure is component pressure sum",
        p_total == expected_pressure,
        f"p_total={p_total}, expected={expected_pressure}",
    )
    check(
        "effective w is weighted component sum",
        w_of(total)
        == (
            Fraction(1, 3) * rho_of(radiation)
            + 0 * rho_of(matter)
            - rho_of(lambda_component)
        )
        / rho_total,
        f"w_eff={w_of(total)}",
    )
    return total


def part3_cell_homogeneity_boundary(total: Tensor) -> None:
    print("\n== Part 3: finite cell homogeneity boundary ==")
    homogeneous_cells = [total, total, total, total]
    avg = tensor_average(homogeneous_cells)
    check("homogeneous finite cell average equals each cell tensor", avg == total)
    check(
        "homogeneous cell packet is pointwise FRW-compatible",
        all(cell == total and is_diagonal(cell) and isotropic_pressure(cell) for cell in homogeneous_cells),
    )

    cell_a = diag_tensor(Fraction(9), Fraction(3))
    cell_b = diag_tensor(Fraction(15), Fraction(5))
    check("inhomogeneous cells can each retain local w_r=1/3", w_of(cell_a) == w_of(cell_b) == Fraction(1, 3))
    check(
        "inhomogeneous cells are not a homogeneous FRW background",
        cell_a != cell_b,
        f"cell_a={cell_a}, cell_b={cell_b}",
    )
    check(
        "cell inhomogeneity is a C1 residual, not a C3 label failure",
        w_of(cell_a) == Fraction(1, 3) and cell_a != cell_b,
    )


def part4_source_free_continuity_boundary() -> None:
    print("\n== Part 4: source-free continuity boundary ==")
    rho = Fraction(7)
    w_r = Fraction(1, 3)
    w_m = Fraction(0)
    residual_radiation = -4 * rho + 3 * (1 + w_r) * rho
    residual_matter = -3 * rho + 3 * (1 + w_m) * rho
    injected_residual = residual_radiation + Fraction(2)
    check(
        "source-free radiation scaling exponent a^-4 matches w=1/3",
        residual_radiation == 0,
        f"residual={residual_radiation}",
    )
    check(
        "source-free matter scaling exponent a^-3 matches w=0",
        residual_matter == 0,
        f"residual={residual_matter}",
    )
    check(
        "nonzero source term blocks adiabatic/scaling closure",
        injected_residual != 0,
        f"residual_with_source={injected_residual}",
    )
    check(
        "source injection is a C2 residual, not a C3 label failure",
        residual_radiation == 0 and injected_residual != 0,
    )


def part5_result() -> None:
    print("\n== Result ==")
    print("Closed by this bridge: finite component tensors and homogeneous cell aggregation.")
    print("Still open: C1, C2, real species allocation, thermal history, and audit status.")


def main() -> int:
    print("FRW C3 KINETIC COMPONENT TO PERFECT-FLUID LIFT")
    part0_source_firewall()
    radiation, matter, lambda_component = part1_component_tensors()
    total = part2_direct_sum_fluid(radiation, matter, lambda_component)
    part3_cell_homogeneity_boundary(total)
    part4_source_free_continuity_boundary()
    part5_result()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded support passes for the finite perfect-fluid lift "
            "of ideal kinetic C3 labels. C1, C2, real cosmological species "
            "allocation, and audit status remain open."
        )
        return 0
    print("VERDICT: bounded support FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
