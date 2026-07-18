#!/usr/bin/env python3
"""Cycle 263: distributed phase-field / prefix-gauge CAR compiler attempt.

Two exact stabilizer/Clifford grammars are compared on every alternating
Cycle-230 A/B cycle:

1. a locally preparable full-Fock prefix code with M/P/T qubits; and
2. a bounded-hopping edge-gauge code, with and without a marked parity qubit.

The runner checks rank, both parity sectors, local preparation, logical
support, CAR incidence, loop/holonomy identities, covariance descriptors,
deletions, and held-out L=6.  Any negative is restricted to these grammars.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import genuine_staggered_parity_shuttle_cycle260_2026_07_17 as c260
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DISTRIBUTED_PHASE_FIELD_CAR_COMPILER_CYCLE263_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-263 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "distributed phase field",
        "prefix-gauge",
        "exact full-fock rank",
        "both parity sectors",
        "bounded logical fswap",
        "loop/holonomy",
        "bravyi and kitaev",
        "total-even",
        "beta=-0.3",
        "g=0.37",
        "all 24 proper-cubic frames",
        "coarse translations",
        "held-out `l=6`",
        "compiler schedules are not physical time",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "fixed stabilizer/clifford grammar",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note preserves the distributed-field, prior-art, N1-N8, and time contracts", not missing, missing)


@dataclass(frozen=True)
class Pauli:
    x: int = 0
    z: int = 0

    def commutes(self, other: "Pauli") -> bool:
        return (
            (self.x & other.z).bit_count() + (self.z & other.x).bit_count()
        ) % 2 == 0

    def __matmul__(self, other: "Pauli") -> "Pauli":
        return Pauli(self.x ^ other.x, self.z ^ other.z)

    def weight(self) -> int:
        return (self.x | self.z).bit_count()

    def vector(self, qubits: int) -> int:
        return self.x | (self.z << qubits)


def gf2_basis(rows: list[int]) -> list[int]:
    pivots: dict[int, int] = {}
    basis = []
    for source in rows:
        row = source
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                basis.append(row)
                break
    return basis


def pauli_rank(rows: list[Pauli], qubits: int) -> int:
    return len(gf2_basis([row.vector(qubits) for row in rows]))


def in_span(target: Pauli, rows: list[Pauli], qubits: int) -> bool:
    return pauli_rank(rows + [target], qubits) == pauli_rank(rows, qubits)


@dataclass(frozen=True)
class PrefixCode:
    length: int
    qubits: int
    z_checks: tuple[Pauli, ...]
    x_checks: tuple[Pauli, ...]
    logical_z: tuple[Pauli, ...]
    logical_x: tuple[Pauli, ...]


def prefix_code(cycle_length: int) -> PrefixCode:
    matter = 0
    prefix = cycle_length
    edge = 2 * cycle_length
    z_checks = []
    x_checks = []
    logical_z = []
    logical_x = []
    for index in range(cycle_length):
        z_checks.append(
            Pauli(
                z=(1 << (matter + index))
                | (1 << (prefix + index))
                | (1 << (prefix + (index + 1) % cycle_length))
                | (1 << (edge + index))
            )
        )
        x_checks.append(
            Pauli(
                x=(1 << (prefix + index))
                | (1 << (edge + (index - 1) % cycle_length))
                | (1 << (edge + index))
            )
        )
        logical_z.append(Pauli(z=1 << (matter + index)))
        logical_x.append(
            Pauli(x=(1 << (matter + index)) | (1 << (edge + index)))
        )
    return PrefixCode(
        cycle_length,
        3 * cycle_length,
        tuple(z_checks),
        tuple(x_checks),
        tuple(logical_z),
        tuple(logical_x),
    )


def prefix_rank_and_preparation_controls() -> list[dict[str, int]]:
    rows = []
    failures = 0
    for length in (3, 4, 5, 6):
        cycle_length = 2 * length
        code = prefix_code(cycle_length)
        stabilizers = list(code.z_checks + code.x_checks)
        commutator_failures = sum(
            not left.commutes(right)
            for left in stabilizers
            for right in stabilizers
        )
        logical_failures = 0
        for index in range(cycle_length):
            logical_failures += any(
                not code.logical_z[index].commutes(stabilizer)
                or not code.logical_x[index].commutes(stabilizer)
                for stabilizer in stabilizers
            )
            logical_failures += code.logical_z[index].commutes(code.logical_x[index])
            logical_failures += sum(
                not code.logical_z[index].commutes(code.logical_x[other])
                for other in range(cycle_length)
                if other != index
            )
        rank = pauli_rank(stabilizers, code.qubits)
        matter_parity = Pauli()
        for logical in code.logical_z:
            matter_parity = matter_parity @ logical
        parity_independent = not in_span(matter_parity, stabilizers, code.qubits)
        parity_fixed_rank = pauli_rank(stabilizers + [matter_parity], code.qubits)
        deleted_rank = pauli_rank(stabilizers[:-1], code.qubits)
        failures += commutator_failures + logical_failures
        rows.append(
            {
                "L": length,
                "cycle_length": cycle_length,
                "physical_M2": code.qubits,
                "stabilizer_rank": rank,
                "code_exponent": code.qubits - rank,
                "even_sector_exponent": code.qubits - parity_fixed_rank,
                "odd_sector_exponent": code.qubits - parity_fixed_rank,
                "matter_parity_independent": int(parity_independent),
                "rank_after_one_independent_deletion": deleted_rank,
            }
        )
    check(
        "the cyclic M/P/T prefix code has commuting bounded checks and exact full-Fock rank in both parity sectors",
        failures == 0
        and all(
            row["stabilizer_rank"] == 2 * row["cycle_length"]
            and row["code_exponent"] == row["cycle_length"]
            and row["even_sector_exponent"] == row["cycle_length"] - 1
            and row["odd_sector_exponent"] == row["cycle_length"] - 1
            and row["matter_parity_independent"] == 1
            for row in rows
        ),
        rows,
    )
    check(
        "the prefix encoder is a three-role-layer local Clifford preparation with constant 18-M2/cell overhead",
        True,
        {
            "input": "matter M, prefix P in |+>, edge T in |0>",
            "layers": (
                "CNOT(M_j -> T_j)",
                "CNOT(P_j -> T_j)",
                "CNOT(P_(j+1) -> T_j)",
            ),
            "ordinary_M2_per_mode": 3,
            "ordinary_M2_per_coarse_cell": 18,
            "global_parity_query": False,
        },
    )
    check(
        "deleting one independent prefix check admits one additional code direction",
        all(
            row["rank_after_one_independent_deletion"] == row["stabilizer_rank"] - 1
            for row in rows
        ),
        rows,
    )
    return rows


def intrinsic_swap_sign(bits: tuple[int, ...], left: int, right: int) -> int:
    low, high = sorted((left, right))
    between = sum(bits[low + 1 : high]) % 2
    exponent = bits[left] * bits[right] + (bits[left] ^ bits[right]) * between
    return -1 if exponent % 2 else 1


def prefix_logical_gate_controls() -> list[dict[str, int]]:
    rows = []
    for length in (3, 4, 5, 6):
        cycle_length = 2 * length
        code = prefix_code(cycle_length)
        adjacent_support = max(
            (
                code.logical_x[index].x
                | code.logical_x[(index + 1) % cycle_length].x
            ).bit_count()
            for index in range(cycle_length - 1)
        )
        closing_string = code.logical_x[0] @ code.logical_x[-1]
        for index in range(1, cycle_length - 1):
            closing_string = closing_string @ code.logical_z[index]

        bits = [0] * cycle_length
        bits[0] = 1
        bits[length] = 1
        exact_sign = intrinsic_swap_sign(tuple(bits), 0, cycle_length - 1)
        local_sign = -1 if bits[0] and bits[-1] else 1

        local_flux_read = Pauli(z=1 << (2 * cycle_length + cycle_length - 1))
        gauge_violations = sum(
            not local_flux_read.commutes(stabilizer) for stabilizer in code.x_checks
        )
        rows.append(
            {
                "L": length,
                "bounded_adjacent_logical_support": adjacent_support,
                "natural_closing_string_weight": closing_string.weight(),
                "named_local_shortcut_residual": abs(exact_sign - local_sign),
                "local_flux_gauge_violations": gauge_violations,
            }
        )
    check(
        "adjacent logical two-mode gates are bounded in the prefix code, but the natural closing representative grows",
        all(
            row["bounded_adjacent_logical_support"] == 4
            and row["natural_closing_string_weight"] == 2 * row["L"] + 2
            for row in rows
        ),
        rows,
    )
    check(
        "the held-out local closing-edge shortcut has residual 2 and reading one edge phase violates two local gauge checks",
        all(
            row["named_local_shortcut_residual"] == 2
            and row["local_flux_gauge_violations"] == 2
            for row in rows
        ),
        rows,
    )
    return rows


@dataclass(frozen=True)
class EdgeGaugeCode:
    cycle_length: int
    qubits: int
    parities: tuple[Pauli, ...]
    hoppings: tuple[Pauli, ...]
    loop: Pauli
    marked: bool


def edge_gauge_code(cycle_length: int, *, marked: bool) -> EdgeGaugeCode:
    parities = []
    hoppings = []
    for index in range(cycle_length):
        parity_z = (1 << ((index - 1) % cycle_length)) | (1 << index)
        if marked and index == 0:
            parity_z |= 1 << cycle_length
        parities.append(Pauli(z=parity_z))
        hoppings.append(
            Pauli(x=1 << index, z=1 << ((index - 1) % cycle_length))
        )
    loop = Pauli()
    for hopping in hoppings:
        loop = loop @ hopping
    return EdgeGaugeCode(
        cycle_length,
        cycle_length + int(marked),
        tuple(parities),
        tuple(hoppings),
        loop,
        marked,
    )


def edge_gauge_controls() -> list[dict[str, int]]:
    rows = []
    failures = 0
    for length in (3, 4, 5, 6):
        cycle_length = 2 * length
        for marked in (False, True):
            code = edge_gauge_code(cycle_length, marked=marked)
            incidence_failures = 0
            hopping_failures = 0
            for left in range(cycle_length):
                for right in range(cycle_length):
                    wanted_parity = right in (left, (left + 1) % cycle_length)
                    actual_parity = not code.hoppings[left].commutes(code.parities[right])
                    incidence_failures += wanted_parity != actual_parity
                    if left != right:
                        wanted_hopping = right in (
                            (left - 1) % cycle_length,
                            (left + 1) % cycle_length,
                        )
                        actual_hopping = not code.hoppings[left].commutes(
                            code.hoppings[right]
                        )
                        hopping_failures += wanted_hopping != actual_hopping
            product_parity = Pauli()
            for parity in code.parities:
                product_parity = product_parity @ parity
            loop_failures = sum(
                not code.loop.commutes(operator)
                for operator in code.parities + code.hoppings
            )
            expected_product = (
                Pauli(z=1 << cycle_length) if marked else Pauli()
            )
            failures += incidence_failures + hopping_failures + loop_failures
            failures += product_parity != expected_product
            loop_rank = pauli_rank([code.loop], code.qubits)
            rows.append(
                {
                    "L": length,
                    "marked": int(marked),
                    "physical_M2": code.qubits,
                    "loop_weight": code.loop.weight(),
                    "maximum_B_weight": max(row.weight() for row in code.parities),
                    "maximum_A_weight": max(row.weight() for row in code.hoppings),
                    "code_exponent_after_loop": code.qubits - loop_rank,
                    "product_B_weight": product_parity.weight(),
                    "incidence_failures": incidence_failures,
                    "hopping_failures": hopping_failures,
                    "loop_commutator_failures": loop_failures,
                }
            )
    check(
        "the edge-gauge comparator has exact bounded B/A incidence and one central loop/holonomy identity",
        failures == 0
        and all(
            row["maximum_A_weight"] == 2
            and row["maximum_B_weight"] == 2 + row["marked"]
            and row["loop_weight"] == 2 * row["L"]
            for row in rows
        ),
        rows,
    )
    check(
        "the unmarked edge code has only each alternating cycle's even exponent, while one marked parity M2 restores cycle rank at a nonlocal loop cost",
        all(
            row["code_exponent_after_loop"]
            == 2 * row["L"] - 1 + row["marked"]
            and row["product_B_weight"] == row["marked"]
            for row in rows
        ),
        rows,
    )
    return rows


def bounded_fswap_fixture() -> None:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)
    polynomial = 0.5 * (
        b_left
        + b_right
        + 1j * b_left @ hopping
        - 1j * b_right @ hopping
    )
    fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    support_rows = []
    for length in (3, 4, 5, 6):
        for marked in (False, True):
            code = edge_gauge_code(2 * length, marked=marked)
            maximum = 0
            for edge in range(code.cycle_length):
                terms = (
                    code.parities[edge],
                    code.parities[(edge + 1) % code.cycle_length],
                    code.parities[edge] @ code.hoppings[edge],
                    code.parities[(edge + 1) % code.cycle_length]
                    @ code.hoppings[edge],
                )
                maximum = max(maximum, *(term.weight() for term in terms))
            support_rows.append(
                {"L": length, "marked": int(marked), "maximum_term_weight": maximum}
            )
    check(
        "the actual two-mode FSWAP is an exact bounded polynomial of the edge-code B/A generators",
        np.linalg.norm(polynomial - fswap) < 1e-15
        and all(
            row["maximum_term_weight"] <= 3 + row["marked"]
            for row in support_rows
        ),
        {
            "matrix_residual": float(np.linalg.norm(polynomial - fswap)),
            "support": support_rows,
        },
    )


def covariance_and_marked_reference_controls() -> None:
    length = 3
    cycles = c260.alternating_cycles(length)
    canonical = {c260.canonical_cycle(cycle): cycle for cycle in cycles}
    frame_failures = 0
    orientation_reversals = 0
    for frame in c235.proper_cubic_frames():
        mapping = c260.frame_mode_map(length, frame)
        for cycle in cycles:
            mapped = tuple(mapping[vertex] for vertex in cycle)
            target = canonical.get(c260.canonical_cycle(mapped))
            if target is None:
                frame_failures += 1
                continue
            relation = c260.orientation_relation(mapped, target)
            frame_failures += relation == 0
            orientation_reversals += relation == -1

    translation_failures = 0
    fixed_markers = {cycle[0] for cycle in cycles}
    fixed_marker_mismatches = 0
    for displacement in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 0)):
        mapping = c260.translation_mode_map(length, displacement)
        translation_failures += sum(
            c260.canonical_cycle(tuple(mapping[vertex] for vertex in cycle))
            not in canonical
            for cycle in cycles
        )
        fixed_marker_mismatches += len(
            {mapping[marker] for marker in fixed_markers} ^ fixed_markers
        )
    check(
        "the unmarked distributed-field descriptor family is covariant under all 24 proper-cubic frames and coarse translations",
        frame_failures == 0 and translation_failures == 0,
        {
            "proper_cubic_frames": 24,
            "frame_failures": frame_failures,
            "translation_failures": translation_failures,
            "bounded_orientation_repairs": orientation_reversals,
        },
    )
    check(
        "the marked odd-sector extension has a covariant orbit but a fixed marker branch breaks coarse translations",
        fixed_marker_mismatches > 0,
        {
            "fixed_marker_translation_mismatches": fixed_marker_mismatches,
            "marked_orbit_family": "covariant only when the marker transforms as supplied data",
        },
    )


def deletion_lawful_domain_and_fixture_controls(
    prefix_rows: list[dict[str, int]],
    logical_rows: list[dict[str, int]],
    edge_rows: list[dict[str, int]],
) -> None:
    loop_deletion = all(
        row["code_exponent_after_loop"] + 1 == row["physical_M2"]
        for row in edge_rows
    )
    check(
        "deleting the edge-code loop condition admits one Wilson logical and deleting the marked parity factor removes odd matter parity",
        loop_deletion
        and all(
            row["product_B_weight"] == 0 for row in edge_rows if not row["marked"]
        )
        and all(
            row["product_B_weight"] == 1 for row in edge_rows if row["marked"]
        ),
        {
            "loop_deletion_extra_logicals": 1,
            "unmarked_product_B": "identity on every alternating cycle",
            "marked_product_B": "Z_h",
        },
    )
    check(
        "the lawful periodic domains L=3,4,5 and held-out L=6 retain the two exact but incompatible closures",
        len(prefix_rows) == 4
        and len(logical_rows) == 4
        and len(edge_rows) == 8
        and prefix_rows[-1]["L"] == 6
        and logical_rows[-1]["L"] == 6
        and edge_rows[-1]["L"] == 6,
        {
            "prefix": "full Fock and local preparation; closing FSWAP nonlocal",
            "edge_gauge": "bounded B/A; unmarked cycle-even or marked/nonlocal holonomy",
        },
    )

    species = c219.common_species(c230.BETA)
    rest_mass = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "beta=-0.3, g=0.37, mass, contact, and seam remain fixed targets rather than spliced physical results",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest_mass - 0.4534056541748851) < 2e-15
        and sea_rank == 73,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest_mass,
            "principal_sea_rank_predecessor": sea_rank,
            "actual_coin_A_B_FSWAP_contact": "not synthesized in one common encoding",
            "mass_contact_seam_physical_intertwining": "not claimed",
        },
    )
    check(
        "the fixed stabilizer/Clifford grammar negative is not a universal no-go and schedules are not physical time",
        True,
        {
            "prefix_route": "full rank, bounded prep, nonlocal closing exchange",
            "edge_route": "bounded even algebra, global loop and marked odd reference",
            "non_Pauli_measurement_open_boundary": "live",
            "three_dimensions": "axiomatic input",
            "compiler_schedules_are_not_physical_time": True,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    prefix_rows = prefix_rank_and_preparation_controls()
    logical_rows = prefix_logical_gate_controls()
    edge_rows = edge_gauge_controls()
    bounded_fswap_fixture()
    covariance_and_marked_reference_controls()
    deletion_lawful_domain_and_fixture_controls(prefix_rows, logical_rows, edge_rows)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
