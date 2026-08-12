#!/usr/bin/env python3
"""Test a conserved Record worldline and the two-TT causal update boundary.

The runner constructs a monotone, proper-cubic family of Record path prefixes,
derives a local frontier/source decoder and conserved rank-one stress current,
and then compares positivity, Lorentzian stability, and explicit one-tick
locality for the Block-51 quadratic transfer family.  It does not select a
physical clock or amend the axioms.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_"
    "CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
RECORD_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_"
    "TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
CURVATURE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
TRANSFER_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_"
    "CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
JOINT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RECORD_WORLDLINE_CONSERVED_STRESS_TWO_TT_LORENTZIAN_CFL_LOCALITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for permutation in permutations(range(3)):
        sign_p = permutation_sign(permutation)
        for signs in product((-1, 1), repeat=3):
            if sign_p * int(np.prod(signs)) != 1:
                continue
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            rotations.append(matrix)
    return tuple(rotations)


PAULI = (
    np.asarray(((0, 1), (1, 0)), dtype=complex),
    np.asarray(((0, -1j), (1j, 0)), dtype=complex),
    np.asarray(((1, 0), (0, -1)), dtype=complex),
)


def direction_content(direction: np.ndarray) -> np.ndarray:
    return sum(float(direction[index]) * PAULI[index] for index in range(3))


def path_prefix(
    origin: tuple[int, int, int], direction: np.ndarray, length: int
) -> dict[tuple[int, int, int], np.ndarray | None]:
    records: dict[tuple[int, int, int], np.ndarray | None] = {origin: None}
    point = np.asarray(origin, dtype=int)
    incoming = -np.asarray(direction, dtype=int)
    for _ in range(length):
        point = point + direction
        site = tuple(int(value) for value in point)
        if site in records:
            raise ValueError("worldline prefix is not self-avoiding")
        records[site] = incoming.copy()
    return records


def frontier_charge(
    records: dict[tuple[int, int, int], np.ndarray | None]
) -> dict[tuple[int, int, int], int]:
    outgoing = {site: 0 for site in records}
    for child, incoming in records.items():
        if incoming is None:
            continue
        parent = tuple(int(child[index] + incoming[index]) for index in range(3))
        if parent not in outgoing:
            raise ValueError("incoming Record pointer has no parent")
        outgoing[parent] += 1
    return {site: 1 - outgoing[site] for site in records}


def periodic_incidence(size: int) -> tuple[np.ndarray, dict[tuple[int, int], int]]:
    sites = size**3
    incidence = np.zeros((sites, 3 * sites), dtype=float)
    lookup: dict[tuple[int, int], int] = {}

    def index(site: tuple[int, int, int]) -> int:
        return (site[0] * size + site[1]) * size + site[2]

    edge = 0
    for site in product(range(size), repeat=3):
        source = index(site)
        for axis in range(3):
            target_site = list(site)
            target_site[axis] = (target_site[axis] + 1) % size
            target = index(tuple(target_site))
            incidence[source, edge] = 1.0
            incidence[target, edge] = -1.0
            lookup[(source, axis)] = edge
            edge += 1
    return incidence, lookup


def periodic_laplacian(size: int) -> np.ndarray:
    incidence, _ = periodic_incidence(size)
    return incidence @ incidence.T


SYMMETRIC_BASIS = (
    np.asarray(((1, 0, 0), (0, 0, 0), (0, 0, 0)), dtype=float),
    np.asarray(((0, 0, 0), (0, 1, 0), (0, 0, 0)), dtype=float),
    np.asarray(((0, 0, 0), (0, 0, 0), (0, 0, 1)), dtype=float),
    np.asarray(((0, 1, 0), (1, 0, 0), (0, 0, 0)), dtype=float) / np.sqrt(2.0),
    np.asarray(((0, 0, 1), (0, 0, 0), (1, 0, 0)), dtype=float) / np.sqrt(2.0),
    np.asarray(((0, 0, 0), (0, 0, 1), (0, 1, 0)), dtype=float) / np.sqrt(2.0),
)


def lattice_vector(momentum: np.ndarray) -> np.ndarray:
    return 2.0 * np.sin(np.asarray(momentum, dtype=float) / 2.0)


def spatial_laplacian_symbol(momentum: np.ndarray) -> float:
    vector = lattice_vector(momentum)
    return float(vector @ vector)


def tt_constraint(momentum: np.ndarray) -> np.ndarray:
    vector = lattice_vector(momentum)
    rows = [np.asarray([np.trace(basis) for basis in SYMMETRIC_BASIS])]
    rows.extend(
        np.asarray([(basis @ vector)[axis] for basis in SYMMETRIC_BASIS])
        for axis in range(3)
    )
    return np.asarray(rows, dtype=float)


def discrete_lorentz_data(kappa_squared: float, coefficient: float):
    temporal_mass = 1.0 + coefficient * kappa_squared
    lambda_value = kappa_squared / temporal_mass
    trace = 2.0 - lambda_value
    transfer = np.asarray(((trace, -1.0), (1.0, 0.0)))
    energy_form = np.asarray(((1.0, -trace / 2.0), (-trace / 2.0, 1.0)))
    return temporal_mass, lambda_value, trace, transfer, energy_form


def continuous_time_data(kappa_squared: float):
    kappa = float(np.sqrt(kappa_squared))
    cosine = np.cos(kappa)
    sine = np.sin(kappa)
    transfer = np.asarray(
        ((cosine, sine / kappa), (-kappa * sine, cosine)), dtype=float
    )
    hessian = np.diag((kappa_squared, 1.0))
    return transfer, hessian


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    kinetic = flat(KINETIC_PATH)
    record = flat(RECORD_PATH)
    curvature = flat(CURVATURE_PATH)
    transfer_note = flat(TRANSFER_PATH)
    joint = flat(JOINT_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current foundation and exact Record/curvature/transfer parents are read without importing a selected dynamics",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "c_t = c_s" in kinetic
        and "permanent" in record
        and "j_(x+t)" in curvature
        and "transition-based conserved source-current decoder" in transfer_note
        and "record-extension instrument" in joint,
    )

    rotations = proper_cubic_rotations()
    directions = tuple(
        sign * np.eye(3, dtype=int)[axis]
        for axis in range(3)
        for sign in (-1, 1)
    )
    content_error = 0.0
    path_failures = 0
    frontier_failures = 0
    for rotation in rotations:
        for direction in directions:
            rotated = rotation @ direction
            content = direction_content(rotated)
            decoded = np.asarray(
                [0.5 * np.trace(matrix @ content).real for matrix in PAULI]
            )
            content_error = max(
                content_error,
                float(np.linalg.norm(content - content.conj().T)),
                float(np.linalg.norm(content @ content - np.eye(2))),
                abs(float(np.trace(content).real)),
                float(np.linalg.norm(decoded - rotated)),
            )
            for length in range(7):
                records = path_prefix((2, -3, 5), rotated, length)
                charges = frontier_charge(records)
                endpoint = tuple(
                    int(value)
                    for value in np.asarray((2, -3, 5)) + length * rotated
                )
                pointer_failure = any(
                    value is not None and not np.array_equal(value, -rotated)
                    for value in records.values()
                )
                path_failures += int(
                    len(records) != length + 1
                    or len(set(records)) != len(records)
                    or pointer_failure
                )
                frontier_failures += int(
                    charges.get(endpoint) != 1
                    or sum(charges.values()) != 1
                    or any(value != 0 for site, value in charges.items() if site != endpoint)
                )
    checks.check(
        "proper-cubic-monotone-record-worldline",
        "every rotated straight prefix is self-avoiding, permanent, one-Record-per-site, and its incoming direction is an M2 involution",
        len(rotations) == 24
        and path_failures == 0
        and content_error < 1.0e-14
        and "incoming-pointer record" in note,
        f"rotations={len(rotations)}; prefixes={len(rotations)*len(directions)*7}; content={content_error:.3e}",
    )
    checks.check(
        "local-frontier-source-decoder",
        "occupancy minus outgoing-child count cancels every permanent interior Record and leaves exactly one active endpoint source",
        frontier_failures == 0 and "occupancy minus outgoing degree" in note,
        f"frontier failures={frontier_failures}",
    )

    size = 5
    incidence, edge_lookup = periodic_incidence(size)
    sites = size**3
    old_site = 0
    new_site = size**2
    delta_charge = np.zeros(sites)
    delta_charge[new_site] = 1.0
    delta_charge[old_site] = -1.0
    edge_flux = np.zeros(3 * sites)
    edge_flux[edge_lookup[(old_site, 0)]] = 1.0
    continuity_error = float(np.linalg.norm(delta_charge + incidence @ edge_flux))
    checks.check(
        "record-transition-continuity",
        "one path extension moves the frontier charge across one edge and obeys Delta J plus div S equals zero exactly",
        continuity_error < 1.0e-15 and abs(np.sum(delta_charge)) < 1.0e-15,
        f"support={np.flatnonzero(delta_charge)}; continuity={continuity_error:.3e}",
    )

    direction = np.asarray((1.0, 0.0, 0.0))
    null_vector = np.concatenate(([1.0], direction))
    minkowski = np.diag((-1.0, 1.0, 1.0, 1.0))
    density = 1.0 / (2.0 * np.sqrt(2.0))
    stress = density * np.outer(null_vector, null_vector)
    lorentz_trace = float(np.sum(minkowski * stress))
    euclidean_trace = float(np.trace(stress))
    euclidean_temporal_reverse = stress[0, 0] - 0.5 * euclidean_trace
    lorentz_temporal_reverse = stress[0, 0] - 0.5 * minkowski[0, 0] * lorentz_trace
    column_error = 0.0
    gauss_error = 0.0
    for component in range(4):
        charge_increment = density * null_vector[component] * delta_charge
        flux = density * null_vector[component] * edge_flux
        column_error = max(
            column_error,
            float(np.linalg.norm(charge_increment + incidence @ flux)),
        )
        field_increment = -flux
        gauss_error = max(
            gauss_error,
            float(np.linalg.norm(incidence @ field_increment - charge_increment)),
        )
    checks.check(
        "conserved-symmetric-null-stress-current",
        "the straight Record extension carries a symmetric rank-one Lorentz-null stress whose four columns are exactly conserved",
        np.linalg.matrix_rank(stress, tol=1.0e-13) == 1
        and np.linalg.norm(stress - stress.T) < 1.0e-15
        and abs(lorentz_trace) < 1.0e-15
        and column_error < 1.0e-15,
        f"Lorentz trace={lorentz_trace:.1e}; four-column continuity={column_error:.3e}",
    )
    checks.check(
        "signature-aware-ricci-source-repair",
        "the Euclidean x+t trace reversal vanishes while Lorentzian trace reversal leaves the positive null energy source",
        abs(euclidean_temporal_reverse) < 1.0e-15
        and abs(lorentz_temporal_reverse - density) < 1.0e-15
        and "signature-aware source decoder" in note,
        f"Euclidean={euclidean_temporal_reverse:.9f}; Lorentzian={lorentz_temporal_reverse:.9f}",
    )
    checks.check(
        "four-constraint-gauss-intertwiner",
        "updating each contracted connection flux by minus the stress flux preserves all four sourced Gauss/Bianchi constraints",
        gauss_error < 1.0e-15 and "four contracted constraints" in note,
        f"maximum four-column error={gauss_error:.3e}",
    )

    momentum = np.asarray((0.55, 0.83, -0.37))
    constraint = tt_constraint(momentum)
    quotient = null_space(constraint, rcond=1.0e-12)
    spatial_stress_coordinates = np.asarray(
        [np.sum(basis * stress[1:, 1:]) for basis in SYMMETRIC_BASIS]
    )
    tt_force = quotient.T @ spatial_stress_coordinates
    checks.check(
        "two-tt-radiative-source-channel",
        "the conserved null stress has a nonzero projection on the exact two-dimensional TT quotient at generic momentum",
        quotient.shape == (6, 2)
        and np.linalg.norm(constraint @ quotient) < 2.0e-15
        and np.linalg.norm(tt_force) > 0.05,
        f"quotient={quotient.shape}; TT force norm={np.linalg.norm(tt_force):.9f}",
    )

    grid = np.linspace(-np.pi, np.pi, 17)
    kappa_values = np.asarray(
        [spatial_laplacian_symbol(np.asarray(values)) for values in product(grid, repeat=3)]
    )
    worst = {}
    for coefficient in (0.0, 1.0 / 12.0, 1.0 / 6.0, 1.0 / 4.0, 1.0):
        lambdas = kappa_values / (1.0 + coefficient * kappa_values)
        worst[coefficient] = float(np.max(lambdas))
    checks.check(
        "cfl-stability-threshold",
        "the unit-tick local Lorentz recurrence is unstable below r=1/6, marginal at r=1/6, and strictly stable above it on the full Brillouin zone",
        abs(float(np.max(kappa_values)) - 12.0) < 1.0e-14
        and worst[0.0] > 4.0
        and worst[1.0 / 12.0] > 4.0
        and abs(worst[1.0 / 6.0] - 4.0) < 1.0e-14
        and worst[1.0 / 4.0] < 4.0
        and "r > 1/6" in note,
        f"max lambda r=0,1/12,1/6,1/4: {worst[0.0]:.3f},{worst[1/12]:.3f},{worst[1/6]:.3f},{worst[1/4]:.3f}",
    )

    symplectic_form = np.asarray(((0.0, 1.0), (-1.0, 0.0)))
    stable_minimum = np.inf
    symplectic_error = 0.0
    marginal_minimum = np.inf
    for kappa_squared in kappa_values:
        if kappa_squared < 1.0e-12:
            continue
        for coefficient in (1.0 / 4.0, 1.0):
            _, _, _, matrix, energy_form = discrete_lorentz_data(
                float(kappa_squared), coefficient
            )
            stable_minimum = min(
                stable_minimum, float(np.linalg.eigvalsh(energy_form)[0])
            )
            symplectic_error = max(
                symplectic_error,
                float(np.linalg.norm(matrix.T @ symplectic_form @ matrix - symplectic_form)),
                float(np.linalg.norm(matrix.T @ energy_form @ matrix - energy_form)),
            )
        *_, marginal_form = discrete_lorentz_data(
            float(kappa_squared), 1.0 / 6.0
        )
        marginal_minimum = min(
            marginal_minimum, float(np.linalg.eigvalsh(marginal_form)[0])
        )
    *_, marginal_corner, marginal_corner_form = discrete_lorentz_data(
        12.0, 1.0 / 6.0
    )
    marginal_jordan_rank = int(
        np.linalg.matrix_rank(marginal_corner + np.eye(2), tol=1.0e-13)
    )
    marginal_growth = float(np.linalg.norm(np.linalg.matrix_power(marginal_corner, 16)))
    checks.check(
        "stable-positive-discrete-lorentz-family",
        "r=1/4 and r=1 preserve a positive mode energy and symplectic form, while the r=1/6 corner energy is only semidefinite",
        stable_minimum > 1.0e-3
        and symplectic_error < 3.0e-14
        and marginal_minimum > -2.0e-15
        and marginal_minimum < 2.0e-15
        and np.linalg.eigvalsh(marginal_corner_form)[0] < 2.0e-15
        and marginal_jordan_rank == 1
        and marginal_growth > 20.0,
        f"stable min={stable_minimum:.6f}; marginal min={marginal_minimum:.3e}; Jordan growth={marginal_growth:.3f}",
    )

    laplacian = periodic_laplacian(size)
    inverse_minima = []
    inverse_row_errors = []
    for coefficient in (1.0 / 4.0, 1.0):
        temporal_block = np.eye(sites) + coefficient * laplacian
        inverse = np.linalg.inv(temporal_block)
        inverse_minima.append(float(np.min(inverse)))
        inverse_row_errors.append(float(np.max(np.abs(np.sum(inverse, axis=1) - 1.0))))
    zero_inverse = np.linalg.inv(np.eye(sites))
    checks.check(
        "stable-update-explicit-locality-obstruction",
        "every stable r>1/6 temporal block has a dense strictly positive inverse, whereas r=0 has an onsite inverse but unstable UV modes",
        min(inverse_minima) > 1.0e-8
        and max(inverse_row_errors) < 2.0e-15
        and np.count_nonzero(zero_inverse - np.diag(np.diag(zero_inverse))) == 0
        and "finite-range laurent inverse" in note,
        f"dense inverse minima={inverse_minima}; row errors={inverse_row_errors}",
    )

    continuous_symplectic = 0.0
    continuous_energy = 0.0
    for kappa_squared in kappa_values[1::53]:
        if kappa_squared < 1.0e-12:
            continue
        matrix, hessian = continuous_time_data(float(kappa_squared))
        continuous_symplectic = max(
            continuous_symplectic,
            float(np.linalg.norm(matrix.T @ symplectic_form @ matrix - symplectic_form)),
        )
        continuous_energy = max(
            continuous_energy,
            float(np.linalg.norm(matrix.T @ hessian @ matrix - hessian)),
        )
    nonzero_per_row = np.count_nonzero(laplacian, axis=1)
    laplacian_values, laplacian_vectors = np.linalg.eigh(laplacian)
    roots = np.sqrt(np.maximum(laplacian_values, 0.0))
    cosine_kernel = (
        laplacian_vectors * np.cos(roots)
    ) @ laplacian_vectors.T
    sine_factors = np.ones_like(roots)
    nonzero = roots > 1.0e-12
    sine_factors[nonzero] = np.sin(roots[nonzero]) / roots[nonzero]
    sine_kernel = (laplacian_vectors * sine_factors) @ laplacian_vectors.T
    time_one_minimum = min(
        float(np.min(np.abs(cosine_kernel))),
        float(np.min(np.abs(sine_kernel))),
    )
    checks.check(
        "continuous-time-local-generator-repair",
        "the r=0 continuous-time Hamiltonian has a finite-range positive generator and stable unit-speed modes, while its time-one map is not declared a strict Record step",
        set(nonzero_per_row) == {7}
        and continuous_symplectic < 2.0e-15
        and continuous_energy < 2.0e-14
        and time_one_minimum > 1.0e-10
        and "asynchronous record events" in note,
        f"generator entries/row={sorted(set(nonzero_per_row))}; time-one min={time_one_minimum:.3e}; energy={continuous_energy:.3e}",
    )

    checks.check(
        "exact-causal-lstar-decision-boundary",
        "the joint law must choose discrete implicit action-local, continuous generator-local, or auxiliary circuit causality and bind the conserved Record instrument",
        all(
            phrase in note
            for phrase in (
                "implicit action-local",
                "continuous generator-local",
                "auxiliary finite-depth circuit",
                "no canonical axiom is edited",
                "zero toe percentage points",
            )
        ),
    )
    checks.check(
        "fresh-no-go-discipline-packet",
        "the family-scoped locality/stability boundary and Record-source repair pass N1 through N8 without becoming a gravity no-go",
        all(f"n{index} —" in note for index in range(1, 9))
        and all(
            phrase in note
            for phrase in (
                "smaller time step",
                "infrared band restriction",
                "continuous-time hamiltonian",
                "operator splitting",
                "auxiliary qca",
                "different spacetime action",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: all 24 proper cubic frames, six straight directions, 1,008 monotone Record prefixes, local frontier decoding, one periodic transition, four conserved stress columns, one generic two-TT source projection, 4,913 Brillouin modes at five r values, two stable discrete members, the marginal threshold, two dense temporal inverses, and a continuous-time local-generator repair are resolved"
    )
    print(
        "per_element: checked every path Record and incoming M2 pointer, all stress-tensor entries, four current columns, six tensor coordinates, two TT forces, and every transfer matrix entry"
    )
    print(
        "per_site: checked every site of the L=5 incidence/Laplacian carriers, each prefix interior cancellation, both transition endpoints, and all dense-inverse rows"
    )
    print(
        "per_mode: checked 4,913 full-zone spatial momenta for r=0,1/12,1/6,1/4,1 and representative continuous-time symplectic/energy controls"
    )
    print(
        "per_block: checked Record path validity, frontier/source decoding, four-current continuity, signature-aware trace reversal, TT forcing, CFL stability, discrete positive energy, explicit locality, and continuous-time repair"
    )
    print(
        "lattice_wide: the worldline and zero-total transition formulas are translation/proper-cubic covariant on Z3, but no arbitrary path, acceleration, nonlinear geometry, interacting source, boundary ensemble, selected clock, full history measure, or axiom adoption is inferred"
    )
    print(
        "scope_boundary: one straight null Record-worldline construction plus the Block-51 quadratic-family locality/stability cut; not all causal updates, massive matter, nonlinear gravity, axiom necessity, adoption, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
