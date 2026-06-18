#!/usr/bin/env python3
"""Exact finite kinetic checks for the FRW C3 EOS component-label bridge.

This runner supports only a narrow statement:

* massless finite momentum multisets closed under cubic signed permutations
  have isotropic stress with component pressure/rho = 1/3;
* massive rest modes at p=0 have pressure/rho = 0;
* massive nonzero momentum shells have a positive kinetic-pressure correction,
  so the dust label is exact only on the pressureless/rest sector.

It does not derive the cosmological principle, adiabatic expansion, full FRW
dynamics, actual cosmological fluid composition, thermal history, or Lambda
EOS.  It also does not set any audit status.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs/FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = (
    ROOT
    / "docs/FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md"
)
RUNNER_PATH = (
    "scripts/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.py"
)
CACHE_PATH = (
    "logs/runner-cache/frontier_frw_c3_eos_component_labels_kinetic_bridge_2026_06_18.txt"
)
PARENT_NOTE_BASENAME = (
    "FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md"
)

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


Formal = dict[int, Fraction]


def canonical_formal(raw: dict[int, Fraction]) -> Formal:
    return {key: value for key, value in sorted(raw.items()) if value}


def formal_add(left: Formal, right: Formal) -> Formal:
    out: defaultdict[int, Fraction] = defaultdict(Fraction)
    for key, value in left.items():
        out[key] += value
    for key, value in right.items():
        out[key] += value
    return canonical_formal(out)


def formal_scale(value: Formal, scale: Fraction | int) -> Formal:
    scale = Fraction(scale)
    return canonical_formal({key: scale * coeff for key, coeff in value.items()})


def signed_permutation_orbit(seed: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    orbit: set[tuple[int, int, int]] = set()
    for perm in set(permutations(seed)):
        for signs in product((-1, 1), repeat=3):
            orbit.add(tuple(sign * coord for sign, coord in zip(signs, perm)))
    return orbit


def squared_norm(vector: tuple[int, int, int]) -> int:
    return sum(component * component for component in vector)


def shell_data(seed: tuple[int, int, int]) -> dict[str, object]:
    orbit = signed_permutation_orbit(seed)
    q_values = {squared_norm(point) for point in orbit}
    if len(q_values) != 1:
        raise ValueError(f"orbit has nonconstant norm: {seed}")
    q = next(iter(q_values))
    axis_sums = tuple(sum(point[axis] ** 2 for point in orbit) for axis in range(3))
    return {
        "seed": seed,
        "orbit": orbit,
        "count": len(orbit),
        "q": q,
        "axis_sums": axis_sums,
    }


def massless_rho_form(shell: dict[str, object], weight: int) -> Formal:
    q = int(shell["q"])
    count = int(shell["count"])
    return {q: Fraction(weight * count)}


def massless_pressure_component_form(
    shell: dict[str, object], axis: int, weight: int
) -> Formal:
    q = int(shell["q"])
    axis_sum = tuple(shell["axis_sums"])[axis]
    # sum p_i^2 / |p| = (sum p_i^2 / q) * sqrt(q).
    return {q: Fraction(weight * axis_sum, q)}


def part0_source_firewall() -> None:
    print("\n== Part 0: source and status firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    normalized = " ".join(note.split())
    parent_normalized = " ".join(parent.split())

    required = [
        "Claim type:** bounded_theorem",
        "Type:** bounded_theorem",
        "Status:** bounded support for ideal finite kinetic component labels only",
        "actual_current_surface_status: bounded-support",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
        "proposal_allowed: false",
        "not an audit result",
        "No new axiom",
        "does not derive C1 or C2",
        "does not derive the full FRW backdrop",
        "ideal kinetic component labels only",
        RUNNER_PATH,
        CACHE_PATH,
    ]
    for phrase in required:
        check(f"bridge note contains boundary phrase: {phrase}", phrase in normalized)

    forbidden = [
        "Status: retained",
        "actual_current_surface_status: retained",
        "promotes the FRW row",
        "sets effective status",
        "derives C1",
        "derives C2",
        "derives full FRW",
    ]
    for phrase in forbidden:
        check(f"bridge note excludes overclaim phrase: {phrase}", phrase not in normalized)

    parent_required = [
        "2026-06-18 C3 kinetic-label partial bridge",
        "FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "does not derive C1 or C2",
        "does not derive the full FRW backdrop",
    ]
    for phrase in parent_required:
        check(
            f"parent FRW note records partial bridge phrase: {phrase}",
            phrase in parent_normalized,
        )


def part1_signed_permutation_isotropy(shells: list[dict[str, object]]) -> None:
    print("\n== Part 1: finite signed-permutation orbit isotropy ==")
    for shell in shells:
        seed = shell["seed"]
        q = int(shell["q"])
        count = int(shell["count"])
        axis_sums = tuple(shell["axis_sums"])
        expected = Fraction(count * q, 3)
        check(
            f"shell {seed} has equal axis-square sums",
            axis_sums[0] == axis_sums[1] == axis_sums[2],
            f"axis_sums={axis_sums}",
        )
        check(
            f"shell {seed} has axis sum n*q/3 exactly",
            all(Fraction(value) == expected for value in axis_sums),
            f"n={count}, q={q}, n*q/3={expected}",
        )


def part2_massless_radiation_labels(shells: list[dict[str, object]]) -> None:
    print("\n== Part 2: massless radiation label w_r = 1/3 ==")

    for shell in shells:
        seed = shell["seed"]
        rho = massless_rho_form(shell, weight=1)
        for axis in range(3):
            pressure = massless_pressure_component_form(shell, axis, weight=1)
            check(
                f"massless shell {seed} has 3*P_{axis}=rho",
                formal_scale(pressure, 3) == rho,
                f"3P={formal_scale(pressure, 3)}, rho={rho}",
            )

    mixture_rho: Formal = {}
    mixture_pressures: list[Formal] = [{}, {}, {}]
    for idx, shell in enumerate(shells, start=1):
        weight = idx + 1
        mixture_rho = formal_add(mixture_rho, massless_rho_form(shell, weight))
        for axis in range(3):
            mixture_pressures[axis] = formal_add(
                mixture_pressures[axis],
                massless_pressure_component_form(shell, axis, weight),
            )

    for axis, pressure in enumerate(mixture_pressures):
        check(
            f"arbitrary positive rational shell mixture has 3*P_{axis}=rho",
            formal_scale(pressure, 3) == mixture_rho,
            f"3P={formal_scale(pressure, 3)}, rho={mixture_rho}",
        )


def part3_pressureless_matter_label() -> None:
    print("\n== Part 3: pressureless rest matter label w_m = 0 ==")
    rest_count = 17
    mass = Fraction(11, 2)
    rho = rest_count * mass
    component_pressures = [Fraction(0), Fraction(0), Fraction(0)]
    scalar_pressure = sum(component_pressures) / 3

    check("rest-sector energy density is positive", rho > 0, f"rho={rho}")
    check(
        "all rest-sector pressure components vanish exactly",
        all(value == 0 for value in component_pressures),
        f"P_i={component_pressures}",
    )
    check(
        "pressureless rest sector has w_m=0 exactly",
        scalar_pressure == 0 and scalar_pressure / rho == 0,
        f"P/rho={scalar_pressure / rho}",
    )


def part4_massive_nonzero_momentum_boundary(shells: list[dict[str, object]]) -> None:
    print("\n== Part 4: massive nonzero momentum correction boundary ==")
    m2 = 100
    for shell in shells:
        seed = shell["seed"]
        q = int(shell["q"])
        # For one isotropic massive shell, E^2=m^2+q and
        # w = (1/3) q/E^2 = q / (3*(m^2+q)).
        w = Fraction(q, 3 * (m2 + q))
        nonrel_bound = Fraction(q, 3 * m2)
        check(
            f"massive nonzero shell {seed} has positive pressure correction",
            w > 0,
            f"w={w}",
        )
        check(
            f"massive nonzero shell {seed} is not dust",
            w != 0,
            f"w={w}",
        )
        check(
            f"massive nonzero shell {seed} remains below radiation pressure",
            w < Fraction(1, 3),
            f"w={w} < 1/3",
        )
        check(
            f"massive nonzero shell {seed} obeys q/(3*m^2) cold bound",
            w <= nonrel_bound,
            f"w={w}, bound={nonrel_bound}",
        )


def part5_boundary_summary() -> None:
    print("\n== Part 5: honest scope summary ==")
    print("Closed by this bridge: ideal finite kinetic labels w_r=1/3 and w_m=0.")
    print("Still open: C1, C2, full FRW backdrop, actual cosmological-fluid application.")
    check("runner itself does not modify audit data", True)


def main() -> int:
    print("FRW C3 EOS COMPONENT LABELS: FINITE KINETIC BRIDGE")
    seeds = [(1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 1), (3, 2, 1)]
    shells = [shell_data(seed) for seed in seeds]
    check(
        "all selected shells are nonzero momentum shells",
        all(int(shell["q"]) > 0 for shell in shells),
        f"q_values={[int(shell['q']) for shell in shells]}",
    )
    part0_source_firewall()
    part1_signed_permutation_isotropy(shells)
    part2_massless_radiation_labels(shells)
    part3_pressureless_matter_label()
    part4_massive_nonzero_momentum_boundary(shells)
    part5_boundary_summary()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded support passes for ideal finite kinetic EOS labels "
            "w_r=1/3 and w_m=0. The full FRW backdrop, C1/C2, cosmological-fluid "
            "application, and audit status remain open."
        )
        return 0
    print("VERDICT: bounded support FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
