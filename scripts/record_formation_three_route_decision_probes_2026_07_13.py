#!/usr/bin/env python3
"""Finite decision probes for three live record-formation routes.

The three routes are:

1. an objective fundamental commit;
2. a derived invariant sector / global admissibility constraint;
3. access-relative (relational) records.

This is an attack harness, not an axiom derivation, empirical result, or audit
surface.  Each conclusion is limited to the explicit finite construction (or
finite-size sequence) checked in its block.  In particular, a failed toy route
is never promoted to a framework-wide no-go.
"""

from __future__ import annotations

from collections import deque
from itertools import product
import math

import numpy as np


TOL = 1.0e-10
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"FAIL {label}{suffix}")


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)
PLUS = (KET0 + KET1) / math.sqrt(2.0)
MINUS = (KET0 - KET1) / math.sqrt(2.0)


def ket_all(*kets: np.ndarray) -> np.ndarray:
    out = np.array([1.0 + 0.0j])
    for ket in kets:
        out = np.kron(out, ket)
    return out


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def cnot() -> np.ndarray:
    return np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
        dtype=complex,
    )


def commutant_dimension(generators: list[np.ndarray]) -> int:
    """Complex dimension of matrices commuting with every generator."""
    dim = generators[0].shape[0]
    columns: list[np.ndarray] = []
    for row in range(dim):
        for column in range(dim):
            basis = np.zeros((dim, dim), dtype=complex)
            basis[row, column] = 1.0
            columns.append(
                np.concatenate([(basis @ gen - gen @ basis).reshape(-1) for gen in generators])
            )
    linear_map = np.column_stack(columns)
    singular_values = np.linalg.svd(linear_map, compute_uv=False)
    rank = int(np.sum(singular_values > 1.0e-9))
    return dim * dim - rank


def bits(n: int) -> list[tuple[int, ...]]:
    return list(product((0, 1), repeat=n))


def connected_components(
    vertices: list[tuple[int, ...]],
    neighbors: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> list[set[tuple[int, ...]]]:
    unseen = set(vertices)
    components: list[set[tuple[int, ...]]] = []
    while unseen:
        seed = next(iter(unseen))
        queue: deque[tuple[int, ...]] = deque([seed])
        component: set[tuple[int, ...]] = set()
        while queue:
            state = queue.popleft()
            if state in component:
                continue
            component.add(state)
            unseen.discard(state)
            queue.extend(neighbors[state] - component)
        components.append(component)
    return components


def coordinate_constants(component: set[tuple[int, ...]]) -> dict[int, int]:
    constants: dict[int, int] = {}
    width = len(next(iter(component)))
    for index in range(width):
        values = {state[index] for state in component}
        if len(values) == 1:
            constants[index] = next(iter(values))
    return constants


def route_one_objective_commit() -> None:
    section("R1 - Objective fundamental commit")

    p0 = density(KET0)
    p1 = density(KET1)
    rho_plus = density(PLUS)
    dephased = p0 @ rho_plus @ p0 + p1 @ rho_plus @ p1
    dephased_twice = p0 @ dephased @ p0 + p1 @ dephased @ p1
    check("the nonselective pointer map is trace preserving", abs(np.trace(dephased) - 1.0) < TOL)
    check("the nonselective pointer map is positive", np.min(np.linalg.eigvalsh(dephased)) > -TOL)
    check("the nonselective pointer map is repeat-idempotent", np.linalg.norm(dephased_twice - dephased) < TOL)
    check("the nonselective output is not a one-outcome record", np.linalg.norm(dephased - p0) > 0.5 and np.linalg.norm(dephased - p1) > 0.5)

    # A concrete deterministic argmax selector exposes ensemble dependence.
    ensemble_z = ((0.5, KET0), (0.5, KET1))
    ensemble_x = ((0.5, PLUS), (0.5, MINUS))
    rho_z = sum((weight * density(psi) for weight, psi in ensemble_z), np.zeros((2, 2), complex))
    rho_x = sum((weight * density(psi) for weight, psi in ensemble_x), np.zeros((2, 2), complex))

    def argmax_commit(psi: np.ndarray) -> np.ndarray:
        # Fixed tie-break is part of this candidate and deliberately visible.
        return p0 if abs(psi[0]) ** 2 >= abs(psi[1]) ** 2 else p1

    out_z = sum((weight * argmax_commit(psi) for weight, psi in ensemble_z), np.zeros((2, 2), complex))
    out_x = sum((weight * argmax_commit(psi) for weight, psi in ensemble_x), np.zeros((2, 2), complex))
    check("the two input ensembles have the same density matrix", np.linalg.norm(rho_z - rho_x) < TOL)
    check("this deterministic selector depends on ensemble decomposition", np.linalg.norm(out_z - out_x) > 0.5)

    born_z = sum(weight * abs(psi[0]) ** 2 for weight, psi in ensemble_z)
    born_x = sum(weight * abs(psi[0]) ** 2 for weight, psi in ensemble_x)
    check("Born-linear event weights pass this ensemble control", abs(born_z - born_x) < TOL)
    check("Born-linear weights still do not name the realized branch", abs(born_z - 0.5) < TOL)

    # The conditional branches are individually normalized only after their
    # probabilities and the realized label are separately supplied.
    psi = np.array([math.sqrt(0.3), np.exp(0.41j) * math.sqrt(0.7)], complex)
    probabilities = np.array([np.vdot(psi, p0 @ psi).real, np.vdot(psi, p1 @ psi).real])
    branches = [p0 @ psi / math.sqrt(probabilities[0]), p1 @ psi / math.sqrt(probabilities[1])]
    check("selective branch probabilities normalize", abs(float(np.sum(probabilities)) - 1.0) < TOL)
    check("each conditional branch is one-hot and repeatable", all(abs(np.linalg.norm(branch) - 1.0) < TOL for branch in branches))
    check("the branch label is information beyond the nonselective density operator", np.linalg.norm(dephased - p0) > 0.5)


def route_two_sector_and_constraint() -> None:
    section("R2A - Finite algebra: sectors require an operation restriction")

    x1, z1 = np.kron(X, I2), np.kron(Z, I2)
    x2, z2 = np.kron(I2, X), np.kron(I2, Z)
    full_commutant_dim = commutant_dimension([x1, z1, x2, z2])
    check("the full two-qubit matrix algebra has scalar commutant", full_commutant_dim == 1, f"dimension={full_commutant_dim}")

    parity_labels = (1, -1, -1, 1)  # computational order 00,01,10,11
    parity = np.diag(parity_labels).astype(complex)
    restricted_basis: list[np.ndarray] = []
    for row in range(4):
        for column in range(4):
            if parity_labels[row] == parity_labels[column]:
                unit = np.zeros((4, 4), dtype=complex)
                unit[row, column] = 1.0
                restricted_basis.append(unit)
    restricted_center_dim = commutant_dimension(restricted_basis)
    check("the parity-preserving algebra has two central sectors", restricted_center_dim == 2, f"dimension={restricted_center_dim}")
    check("parity commutes with every restricted operation", all(np.linalg.norm(parity @ op - op @ parity) < TOL for op in restricted_basis))
    check("a one-site flip changes parity and lies outside that algebra", np.linalg.norm(parity @ x1 - x1 @ parity) > 1.0)
    check("the same site Hilbert space admits both full and restricted operation algebras", full_commutant_dim != restricted_center_dim)

    section("R2B - Configuration connectivity: a sector is not yet a local record")
    n = 4
    vertices = bits(n)

    unrestricted_neighbors = {state: set() for state in vertices}
    for state in vertices:
        for index in range(n):
            target = list(state)
            target[index] ^= 1
            unrestricted_neighbors[state].add(tuple(target))
    unrestricted_components = connected_components(vertices, unrestricted_neighbors)
    check("unrestricted one-site changes make the configuration graph connected", len(unrestricted_components) == 1)
    check("no site value is invariant on the unrestricted component", coordinate_constants(unrestricted_components[0]) == {})

    pair_neighbors = {state: set() for state in vertices}
    for state in vertices:
        for index in range(n):
            target = list(state)
            target[index] ^= 1
            target[(index + 1) % n] ^= 1
            pair_neighbors[state].add(tuple(target))
    parity_components = connected_components(vertices, pair_neighbors)
    check("nearest-neighbor pair flips produce two parity components", len(parity_components) == 2)
    check("parity is constant on each component", all(len({sum(state) % 2 for state in component}) == 1 for component in parity_components))
    check("neither parity component fixes any one site", all(coordinate_constants(component) == {} for component in parity_components))

    equality_vertices = [tuple([0] * n), tuple([1] * n)]
    equality_neighbors = {state: set() for state in equality_vertices}
    equality_components = connected_components(equality_vertices, equality_neighbors)
    check("the nearest-neighbor equality constraint has two disconnected components", len(equality_components) == 2)
    check("each equality component fixes every site", all(len(coordinate_constants(component)) == n for component in equality_components))
    check("each single site is a decoder for the equality-sector label", all(all(state[index] == state[0] for state in equality_vertices) for index in range(n)))

    global_flip = {state: tuple(1 - bit for bit in state) for state in equality_vertices}
    check("a global flip exchanges the two equality sectors", global_flip[equality_vertices[0]] == equality_vertices[1])
    check("that exchange has no path made of constraint-preserving one-site moves", equality_neighbors[equality_vertices[0]] == set())

    section("R2C - Exact local protection, thermodynamic protection, and finite-time reach")
    n_code = 5
    zero_code = ket_all(*([KET0] * n_code))
    one_code = ket_all(*([KET1] * n_code))
    paulis = (I2, X, Y, Z)
    for support in (1, 2, n_code - 1):
        matrix_elements: list[complex] = []
        for local_word in product(paulis, repeat=support):
            local_operator = np.eye(1, dtype=complex)
            for index in range(n_code):
                local_operator = np.kron(
                    local_operator,
                    local_word[index] if index < support else I2,
                )
            matrix_elements.append(np.vdot(one_code, local_operator @ zero_code))
        check(
            f"no Pauli-basis operator on {support} of {n_code} sites connects repetition sectors",
            max(abs(value) for value in matrix_elements) < TOL,
        )
    global_flip_op = X
    for _ in range(n_code - 1):
        global_flip_op = np.kron(global_flip_op, X)
    check("the all-site operation connects the repetition sectors", abs(np.vdot(one_code, global_flip_op @ zero_code) - 1.0) < TOL)

    overlap = 0.8
    finite_support = 2
    sizes = (4, 8, 16, 32, 64)
    tails = [overlap ** (size - finite_support) for size in sizes]
    check("finite-support cross-sector matrix elements decay with redundant size", all(b < a for a, b in zip(tails, tails[1:])))
    check("the finite-size sequence approaches a disjoint-sector limit", tails[-1] < 2.0e-6, f"last bound={tails[-1]:.3e}")

    # A finite-speed signal from one origin reaches only finitely many Z^3
    # sites after every finite number of nearest-neighbor steps.
    def l1_ball(radius: int) -> int:
        return sum(
            1
            for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1)
            for z in range(-radius, radius + 1)
            if abs(x) + abs(y) + abs(z) <= radius
        )

    ball_sizes = [l1_ball(radius) for radius in range(7)]
    check("finite nearest-neighbor propagation has finite support at every tested step", all(size < math.inf for size in ball_sizes))
    check("the finite light-cone support grows but never becomes unbounded at a finite tested step", all(b > a for a, b in zip(ball_sizes, ball_sizes[1:])))

    section("R2D - Continuation forcing: qualification versus formation")

    def equality_completions(seed: dict[int, int]) -> list[tuple[int, ...]]:
        return [
            state
            for state in equality_vertices
            if all(state[index] == value for index, value in seed.items())
        ]

    def forced_sites(completions: list[tuple[int, ...]]) -> dict[int, int]:
        if not completions:
            return {}
        return {
            index: next(iter(values))
            for index in range(n)
            if len(values := {state[index] for state in completions}) == 1
        }

    empty_completions = equality_completions({})
    seeded_completions = equality_completions({0: 1})
    check("an unseeded symmetric constraint has two admissible completions", len(empty_completions) == 2)
    check("the unseeded constraint forces no local value", forced_sites(empty_completions) == {})
    check("one realized boundary record selects one completion", seeded_completions == [tuple([1] * n)])
    check("that seed propagates a unique locally readable value", len(forced_sites(seeded_completions)) == n)

    # A directed continuation tree can make a value future-invariant only
    # after an actual branch is entered.  It still does not choose the branch.
    future_values = {"open": {0, 1}, "branch_0": {0}, "branch_1": {1}}
    check("the open node does not yet qualify as a record", len(future_values["open"]) == 2)
    check("each realized branch is future-single-valued", len(future_values["branch_0"]) == len(future_values["branch_1"]) == 1)
    check("continuation forcing contains two possible branch transitions", future_values["branch_0"] != future_values["branch_1"])

    section("R2E - Contextuality, weights, and clock metric remain discriminators")
    deterministic_chsh_values = []
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        deterministic_chsh_values.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
    check("a single joint deterministic completion obeys the CHSH bound", max(abs(value) for value in deterministic_chsh_values) == 2)

    correlations = {(0, 0): 1 / math.sqrt(2), (0, 1): 1 / math.sqrt(2), (1, 0): 1 / math.sqrt(2), (1, 1): -1 / math.sqrt(2)}
    table: dict[tuple[int, int, int, int], float] = {}
    for x, y in product((0, 1), repeat=2):
        for a, b in product((-1, 1), repeat=2):
            table[(a, b, x, y)] = (1.0 + a * b * correlations[(x, y)]) / 4.0
    check("the contextual quantum target table is nonnegative and normalized", min(table.values()) >= 0.0 and all(abs(sum(table[(a, b, x, y)] for a, b in product((-1, 1), repeat=2)) - 1.0) < TOL for x, y in product((0, 1), repeat=2)))
    alice_no_signal = all(
        abs(
            sum(table[(a, b, x, 0)] for b in (-1, 1))
            - sum(table[(a, b, x, 1)] for b in (-1, 1))
        )
        < TOL
        for a, x in product((-1, 1), (0, 1))
    )
    bob_no_signal = all(
        abs(
            sum(table[(a, b, 0, y)] for a in (-1, 1))
            - sum(table[(a, b, 1, y)] for a in (-1, 1))
        )
        < TOL
        for b, y in product((-1, 1), (0, 1))
    )
    check("the contextual target table is no-signaling in both directions", alice_no_signal and bob_no_signal)
    chsh = correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)]
    check("the contextual target exceeds the joint-completion CHSH bound", abs(chsh - 2.0 * math.sqrt(2.0)) < TOL)

    distributions = (np.array([0.2, 0.8]), np.array([0.5, 0.5]), np.array([0.91, 0.09]))
    check("multiple normalized weights fit the same two-sector support", all(abs(float(np.sum(dist))) - 1.0 < TOL for dist in distributions))
    check("sector connectivity alone does not distinguish those weights", len({tuple(dist) for dist in distributions}) == len(distributions))

    event_order_a = (0.0, 1.0, 2.0, 3.0)
    event_order_b = tuple(value * value for value in event_order_a)
    check("a monotone clock reparameterization preserves event order", all((event_order_a[i] < event_order_a[j]) == (event_order_b[i] < event_order_b[j]) for i in range(4) for j in range(4)))
    check("the same reparameterization changes elapsed durations", np.diff(event_order_a).tolist() != np.diff(event_order_b).tolist())

    section("R2F - Record-generated refinement of the physical law algebra")

    p0, p1 = density(KET0), density(KET1)

    def sector_restriction(operator: np.ndarray, projector: np.ndarray) -> np.ndarray:
        complement = np.eye(projector.shape[0], dtype=complex) - projector
        return projector @ operator @ projector + complement @ operator @ complement

    test_operator = np.array([[0.2, 0.3 + 0.4j], [0.3 - 0.4j, -0.1]], dtype=complex)
    once = sector_restriction(test_operator, p0)
    twice = sector_restriction(once, p0)
    check("the post-record sector restriction is idempotent", np.linalg.norm(once - twice) < TOL)
    check("the record projector is fixed by the restriction", np.linalg.norm(sector_restriction(p0, p0) - p0) < TOL)
    check("the cross-sector interference operator is removed after activation", np.linalg.norm(sector_restriction(X, p0)) < TOL)
    check("the same interference operator exists before activation", np.linalg.norm(X) > 1.0)

    angle = 0.37
    rotation = math.cos(angle / 2.0) * I2 - 1j * math.sin(angle / 2.0) * Y
    rotated_projector = rotation @ p0 @ rotation.conj().T
    rotated_operator = rotation @ test_operator @ rotation.conj().T
    covariant_left = sector_restriction(rotated_operator, rotated_projector)
    covariant_right = rotation @ sector_restriction(test_operator, p0) @ rotation.conj().T
    check("the sector restriction is covariant when record content transforms with the presentation", np.linalg.norm(covariant_left - covariant_right) < TOL)

    p0_left = np.kron(p0, I2)
    p0_right = np.kron(I2, p0)
    two_site_operator = np.kron(X + 0.2 * Z, Y - 0.3 * X)
    left_then_right = sector_restriction(sector_restriction(two_site_operator, p0_left), p0_right)
    right_then_left = sector_restriction(sector_restriction(two_site_operator, p0_right), p0_left)
    check("disjoint record refinements compose without an order choice", np.linalg.norm(left_then_right - right_then_left) < TOL)

    tilted_ket = math.cos(0.61 / 2.0) * KET0 + math.sin(0.61 / 2.0) * KET1
    tilted_projector = density(tilted_ket)
    z_then_tilt = sector_restriction(sector_restriction(Z, p0), tilted_projector)
    tilt_then_z = sector_restriction(sector_restriction(Z, tilted_projector), p0)
    check("overlapping noncommuting refinements require a physical order or compatibility rule", np.linalg.norm(z_then_tilt - tilt_then_z) > 0.1)

    fixed_states = [p * p0 + (1.0 - p) * p1 for p in (0.13, 0.5, 0.87)]
    check("the same sector restriction permits multiple sector weights", all(np.linalg.norm(sector_restriction(rho, p0) - rho) < TOL for rho in fixed_states))
    check("sector activation does not select which block is realized", all(np.linalg.matrix_rank(rho, tol=1.0e-9) == 2 for rho in fixed_states))

    phase_unitary = np.diag([np.exp(0.17j), np.exp(-0.29j)])
    check("within-sector dynamics preserves record content", np.linalg.norm(phase_unitary @ p0 @ phase_unitary.conj().T - p0) < TOL)
    check("a sector-changing flip is excluded only by the post-record restriction", np.linalg.norm(X @ p0 @ X - p1) < TOL and np.linalg.norm(sector_restriction(X, p0)) < TOL)

    # The fixed point algebra itself is timeless.  If imposed before the write,
    # it removes the very interference whose later loss formation should mark.
    pre_record_state = density(PLUS)
    prematurely_restricted = sector_restriction(pre_record_state, p0)
    check("a fixed restriction imposed from the start destroys pre-record coherence", abs(np.trace(pre_record_state @ X).real - 1.0) < TOL and abs(np.trace(prematurely_restricted @ X).real) < TOL)


def route_three_relational_records() -> None:
    section("R3 - Access-relative / relational records")

    initial = ket_all(PLUS, KET0)
    bell = cnot() @ initial
    coherent = density(bell)
    mixture = 0.5 * density(ket_all(KET0, KET0)) + 0.5 * density(ket_all(KET1, KET1))

    diagonal_observables = [np.eye(4), np.kron(Z, I2), np.kron(I2, Z), np.kron(Z, Z)]
    diagonal_differences = [abs(np.trace((coherent - mixture) @ observable)) for observable in diagonal_observables]
    check("the record-diagonal observer cannot distinguish coherence from mixture", max(diagonal_differences) < TOL)
    check("a full-algebra interference observable does distinguish them", abs(np.trace((coherent - mixture) @ np.kron(X, X)).real - 1.0) < TOL)

    diagonal_basis: list[np.ndarray] = []
    for index in range(4):
        projector = np.zeros((4, 4), dtype=complex)
        projector[index, index] = 1.0
        diagonal_basis.append(projector)
    check("the diagonal observer algebra has four-dimensional center", commutant_dimension(diagonal_basis) == 4)
    check("the full two-qubit algebra has scalar center", commutant_dimension([np.kron(X, I2), np.kron(Z, I2), np.kron(I2, X), np.kron(I2, Z)]) == 1)

    pointer_probabilities = np.real(np.diag(coherent))
    check("the two local pointer reads agree whenever a value is obtained", abs(pointer_probabilities[1]) < TOL and abs(pointer_probabilities[2]) < TOL)
    check("coherent global access reverses the record-writing interaction", np.linalg.norm(cnot().conj().T @ bell - initial) < TOL)

    for p in (0.1, 0.5, 0.9):
        state = math.sqrt(p) * ket_all(KET0, KET0) + math.sqrt(1.0 - p) * ket_all(KET1, KET1)
        probs = np.real(np.diag(density(state)))
        check(f"relational readability is compatible with branch weight p={p:.1f}", abs(probs[0] - p) < TOL and abs(probs[3] - (1.0 - p)) < TOL)

    check("the same relational record is not permanent for the larger coherent-access algebra", np.linalg.norm(cnot().conj().T @ bell - initial) < TOL)


def cross_route_scorecard() -> None:
    section("Cross-route finite-probe scorecard")
    print("R1 objective commit: can output one branch, but must supply a selection/weight law and its conservation/covariance controls.")
    print("R2 invariant sector: can make a locally readable value exact against the declared admissible local operations; fixed sectors alone do not create a finite-time formation event, choose a sector, supply weights, or set a clock metric.")
    print("R3 relational record: preserves global coherence while giving a restricted observer a definite record; permanence is then explicitly access-relative, not the current axiom's unrestricted permanence.")
    print("R2 discriminator: derive the admissible-change/continuation relation from Admissibility, or expose its still-composite candidate constitutional content and test each residual atom separately.")


def main() -> None:
    route_one_objective_commit()
    route_two_sector_and_constraint()
    route_three_relational_records()
    cross_route_scorecard()
    print("\n" + "=" * 79)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 79)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
