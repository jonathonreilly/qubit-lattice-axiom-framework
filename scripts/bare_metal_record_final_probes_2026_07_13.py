#!/usr/bin/env python3
"""Final finite probes for bare-metal record formation.

This runner is a discriminator, not an axiom derivation, empirical result, or
audit surface.  Every conclusion is limited to the finite construction printed
by the corresponding block.  Its purpose is to force the remaining formation
language choices to expose their physical inputs.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 1.0e-10
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


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
H = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2.0)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)
PLUS = (KET0 + KET1) / math.sqrt(2.0)


def kron_all(*ops: np.ndarray) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for op in ops:
        out = np.kron(out, op)
    return out


def ket_all(*kets: np.ndarray) -> np.ndarray:
    out = np.array([1.0 + 0.0j])
    for ket in kets:
        out = np.kron(out, ket)
    return out


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def purity(rho: np.ndarray) -> float:
    return float(np.trace(rho @ rho).real)


def partial_trace(rho: np.ndarray, keep: tuple[int, ...], dims: tuple[int, ...]) -> np.ndarray:
    keep_set = set(keep)
    working_dims = list(dims)
    tensor = rho.reshape(tuple(working_dims + working_dims))
    n = len(working_dims)
    for axis in sorted((q for q in range(n) if q not in keep_set), reverse=True):
        tensor = np.trace(tensor, axis1=axis, axis2=axis + n)
        working_dims.pop(axis)
        n -= 1
    dim_keep = int(np.prod(working_dims, dtype=int))
    return tensor.reshape((dim_keep, dim_keep))


def cnot(nqubits: int, control: int, target: int) -> np.ndarray:
    dim = 2**nqubits
    out = np.zeros((dim, dim), dtype=complex)
    for column in range(dim):
        bits = [(column >> (nqubits - 1 - q)) & 1 for q in range(nqubits)]
        bits[target] ^= bits[control]
        row = 0
        for bit in bits:
            row = (row << 1) | bit
        out[row, column] = 1.0
    return out


def dephase_indices(rho: np.ndarray, dims: tuple[int, ...], targets: tuple[int, ...]) -> np.ndarray:
    """Dephase in the computational basis of selected tensor factors."""
    labels = [np.unravel_index(index, dims) for index in range(rho.shape[0])]
    out = rho.copy()
    for row, row_label in enumerate(labels):
        for column, column_label in enumerate(labels):
            if any(row_label[target] != column_label[target] for target in targets):
                out[row, column] = 0.0
    return out


def entropy(rho: np.ndarray) -> float:
    values = np.linalg.eigvalsh((rho + rho.conj().T) / 2.0).real
    values = values[values > 1.0e-14]
    return float(-np.sum(values * np.log(values)))


def relative_entropy_classical(p: np.ndarray, q: np.ndarray) -> float:
    mask = p > 1.0e-15
    return float(np.sum(p[mask] * np.log(p[mask] / q[mask])))


def probe_permanence_scope() -> None:
    section("F1 - Permanence depends on the allowed-operation scope")
    initial = ket_all(PLUS, KET0, KET0)  # source, witness 1, witness 2
    write_1 = cnot(3, 0, 1)
    write_2 = cnot(3, 0, 2)
    write = write_2 @ write_1
    ghz = write @ initial

    witness_2_before = partial_trace(density(ghz), (2,), (2, 2, 2))
    check(
        "the untouched witness carries a nontrivial outcome register",
        np.linalg.norm(witness_2_before - I2 / 2.0) < TOL,
    )

    # A unitary on source+witness-1 can restore local source coherence by moving
    # the which-branch information into witness-1.  It cannot erase witness-2.
    plus0 = ket_all(PLUS, KET0)
    minus = (KET0 - KET1) / math.sqrt(2.0)
    minus0 = ket_all(minus, KET0)
    minus1 = ket_all(minus, KET1)
    plus1 = ket_all(PLUS, KET1)
    local_repack = np.column_stack((plus0, minus0, minus1, plus1))
    check("the local repacking map is unitary", np.linalg.norm(local_repack.conj().T @ local_repack - np.eye(4)) < TOL)
    repacked = np.kron(local_repack, I2) @ ghz
    source_after = partial_trace(density(repacked), (0,), (2, 2, 2))
    witness_2_after = partial_trace(density(repacked), (2,), (2, 2, 2))
    check("source coherence can be restored locally by moving branch information", np.linalg.norm(source_after - density(PLUS)) < TOL)
    check("that local restoration does not revoke the untouched witness", np.linalg.norm(witness_2_after - witness_2_before) < TOL)

    initial_witness_2 = partial_trace(density(initial), (2,), (2, 2, 2))
    check(
        "no unitary disjoint from witness 2 can restore the complete initial state",
        np.linalg.norm(witness_2_before - initial_witness_2) > 0.5,
        "the untouched reduced state is invariant under operations on the other tensor factor",
    )
    check("coherent access to the complete write support reverses it", np.linalg.norm(write.conj().T @ ghz - initial) < TOL)

    # Exporting the branch label merely moves the reversal boundary unless the
    # environment is removed from the allowed physical algebra.
    initial_4 = ket_all(PLUS, KET0, KET0, KET0)
    write_4 = cnot(4, 0, 3) @ cnot(4, 0, 2) @ cnot(4, 0, 1)
    exported = write_4 @ initial_4
    visible = partial_trace(density(exported), (0, 1, 2), (2, 2, 2, 2))
    check("tracing an exported ledger produces a mixed visible state", purity(visible) < 0.51)
    check("including that ledger restores global reversibility", np.linalg.norm(write_4.conj().T @ exported - initial_4) < TOL)

    record_charge = np.kron(np.eye(4), Z)
    forbidden_flip = np.kron(np.eye(4), X)
    allowed_phase = np.kron(np.eye(4), Z)
    check("a record flip is excluded only after a record-charge algebra is imposed", np.linalg.norm(forbidden_flip @ record_charge - record_charge @ forbidden_flip) > 1.0)
    check("an operation in that restricted algebra preserves record sectors", np.linalg.norm(allowed_phase @ record_charge - record_charge @ allowed_phase) < TOL)


def pure_state_from_bloch_xz(x: float, z: float) -> np.ndarray:
    theta = math.acos(z)
    sign = 1.0 if x >= 0 else -1.0
    return np.array([math.cos(theta / 2.0), sign * math.sin(theta / 2.0)], dtype=complex)


def candidate_binary_probability(p_born: float, rule: str) -> float:
    if rule == "born":
        return p_born
    if rule == "power2":
        return p_born**2 / (p_born**2 + (1.0 - p_born) ** 2)
    if rule == "max":
        if abs(p_born - 0.5) < TOL:
            return 0.5
        return 1.0 if p_born > 0.5 else 0.0
    if rule == "uniform":
        return 0.5
    raise ValueError(rule)


def probe_selective_commit_sweep() -> None:
    section("F2 - Selective commit laws: ensemble, signaling, energy, and covariance")
    z = 0.4
    ensemble_a = (((1.0 + z) / 2.0, KET0), ((1.0 - z) / 2.0, KET1))
    x = math.sqrt(1.0 - z**2)
    ensemble_b = ((0.5, pure_state_from_bloch_xz(x, z)), (0.5, pure_state_from_bloch_xz(-x, z)))

    rho_a = sum((weight * density(psi) for weight, psi in ensemble_a), np.zeros((2, 2), dtype=complex))
    rho_b = sum((weight * density(psi) for weight, psi in ensemble_b), np.zeros((2, 2), dtype=complex))
    check("two operational ensembles represent the same local density matrix", np.linalg.norm(rho_a - rho_b) < TOL)

    n = np.array([1.0, 0.0, 1.0]) / math.sqrt(2.0)
    projector = (I2 + n[0] * X + n[1] * Y + n[2] * Z) / 2.0

    def ensemble_probability(ensemble: tuple[tuple[float, np.ndarray], ...], rule: str) -> float:
        total = 0.0
        for weight, psi in ensemble:
            p = float(np.vdot(psi, projector @ psi).real)
            total += weight * candidate_binary_probability(p, rule)
        return total

    differences: dict[str, float] = {}
    for rule in ("born", "power2", "max", "uniform"):
        differences[rule] = abs(ensemble_probability(ensemble_a, rule) - ensemble_probability(ensemble_b, rule))
    check("Born-linear weights are ensemble-independent in this steering control", differences["born"] < TOL)
    check("the normalized power-2 rule is ensemble-dependent", differences["power2"] > 0.02, f"difference={differences['power2']:.6f}")
    check("the deterministic-max rule is ensemble-dependent", differences["max"] > 0.05, f"difference={differences['max']:.6f}")
    check("a uniform rule avoids this signal but fails eigenstate certainty", differences["uniform"] < TOL and candidate_binary_probability(1.0, "uniform") == 0.5)
    check("Born, power-2, and max candidates all satisfy this binary eigenstate-certainty check", all(abs(candidate_binary_probability(1.0, rule) - 1.0) < TOL for rule in ("born", "power2", "max")))

    # A nonselective Lueders channel is linear/CPTP, but it is a mixture, not a
    # rule selecting which branch becomes the single realized record.
    p0, p1 = density(KET0), density(KET1)
    rho_plus = density(PLUS)
    lueders = p0 @ rho_plus @ p0 + p1 @ rho_plus @ p1
    check("the nonselective Lueders channel preserves trace and positivity", abs(np.trace(lueders) - 1.0) < TOL and np.min(np.linalg.eigvalsh(lueders)) > -TOL)
    check("the same channel changes a noncommuting X-energy expectation", abs(np.trace(rho_plus @ X).real - 1.0) < TOL and abs(np.trace(lueders @ X).real) < TOL)
    check("a commuting pointer eigenstate is unchanged", np.linalg.norm(p0 @ p0 @ p0 + p1 @ p0 @ p1 - p0) < TOL)

    phase_state = np.array([math.sqrt(0.3), 1j * math.sqrt(0.7)], dtype=complex)
    phase_projector = density(np.array([1.0, np.exp(0.37j)], dtype=complex) / math.sqrt(2.0))
    p = float(np.trace(density(phase_state) @ phase_projector).real)
    p_conjugate = float(np.trace(density(phase_state.conj()) @ phase_projector.conj()).real)
    check("simultaneous conjugation leaves the candidate event weight invariant", abs(p - p_conjugate) < TOL)

    fixed_left = p0 @ (H @ rho_plus @ H) @ p0 + p1 @ (H @ rho_plus @ H) @ p1
    covariant_right = H @ lueders @ H
    check("a fixed pointer channel is not covariant under arbitrary pointer rotation", np.linalg.norm(fixed_left - covariant_right) > 0.5)


def probe_two_register_tomography() -> None:
    section("F3 - Two-register tomography and PREP-FRAME falsifier")
    phase = 0.63
    prepared = np.array([math.sqrt(0.35), 0.0, 0.0, np.exp(1j * phase) * math.sqrt(0.65)], dtype=complex)
    rho = density(prepared)
    paulis = (I2, X, Y, Z)
    expectations = np.zeros((4, 4), dtype=float)
    reconstructed = np.zeros((4, 4), dtype=complex)
    for a, op_a in enumerate(paulis):
        for b, op_b in enumerate(paulis):
            op = np.kron(op_a, op_b)
            expectations[a, b] = float(np.trace(rho @ op).real)
            reconstructed += expectations[a, b] * op / 4.0
    check("the full two-register Pauli table reconstructs the prepared state", np.linalg.norm(reconstructed - rho) < TOL)

    pointer_dephased = dephase_indices(rho, (2, 2), (0, 1))
    pointer_probs = np.real(np.diag(rho))
    dephased_probs = np.real(np.diag(pointer_dephased))
    check("pointer agreement data cannot see the prepared relative phase", np.linalg.norm(pointer_probs - dephased_probs) < TOL)
    phase_distance = float(np.linalg.norm(reconstructed - pointer_dephased))
    check(
        "phase-sensitive tomography rejects the pointer-dephased frame",
        phase_distance > 0.6,
        f"Frobenius distance={phase_distance:.6f}",
    )

    rng = np.random.default_rng(20260713)
    trials = 200_000
    sampled_expectations = np.zeros((4, 4), dtype=float)
    sampled_expectations[0, 0] = 1.0
    for a, op_a in enumerate(paulis):
        for b, op_b in enumerate(paulis):
            if a == 0 and b == 0:
                continue
            exact = expectations[a, b]
            plus = rng.binomial(trials, (1.0 + exact) / 2.0)
            sampled_expectations[a, b] = (2.0 * plus - trials) / trials
    sampled_rho = np.zeros((4, 4), dtype=complex)
    for a, op_a in enumerate(paulis):
        for b, op_b in enumerate(paulis):
            sampled_rho += sampled_expectations[a, b] * np.kron(op_a, op_b) / 4.0
    true_error = float(np.linalg.norm(sampled_rho - rho))
    dephased_error = float(np.linalg.norm(sampled_rho - pointer_dephased))
    check("independently counted synthetic trials recover the prepared frame", true_error < 0.01, f"Frobenius error={true_error:.6f}")
    check("the same counts strongly reject the agreement-only frame", dephased_error > 50.0 * true_error, f"error ratio={dephased_error / true_error:.1f}")

    nulls = 1731
    plus = 120_000
    minus = trials - plus - nulls
    conditional_mean = (plus - minus) / (plus + minus)
    all_trial_mean = (plus - minus) / trials
    check("explicit null trials close the frequency denominator", plus + minus + nulls == trials)
    check("conditioning away nulls changes the reported frequency", abs(conditional_mean - all_trial_mean) > 0.001)

    standard = np.eye(4, dtype=complex)
    rotated = np.eye(4, dtype=complex)
    rotated[:, 1] = (standard[:, 1] + standard[:, 2]) / math.sqrt(2.0)
    rotated[:, 2] = (standard[:, 1] - standard[:, 2]) / math.sqrt(2.0)
    amplitudes = np.array([math.sqrt(0.2), math.sqrt(0.3), math.sqrt(0.1), math.sqrt(0.4)], dtype=complex)
    p_standard = np.abs(standard.conj().T @ amplitudes) ** 2
    p_rotated = np.abs(rotated.conj().T @ amplitudes) ** 2
    power_standard = p_standard**2 / np.sum(p_standard**2)
    power_rotated = p_rotated**2 / np.sum(p_rotated**2)
    check("Born-linear weight of a shared projector survives a context change", abs(p_standard[0] - p_rotated[0]) < TOL)
    check("normalized power weights fail the same shared-projector test", abs(power_standard[0] - power_rotated[0]) > 0.01)


def reversible_joint_read_clock_unitary() -> np.ndarray:
    dims = (2, 2, 4, 4)  # source, reader, clock phase, timestamp
    dim = int(np.prod(dims))
    unitary = np.zeros((dim, dim), dtype=complex)
    for column in range(dim):
        source, reader, clock, stamp = np.unravel_index(column, dims)
        mapped = (source, reader ^ source, clock, (stamp + clock) % 4)
        row = np.ravel_multi_index(mapped, dims)
        unitary[row, column] = 1.0
    return unitary


def probe_joint_clock_commit() -> None:
    section("F4 - A clock can timestamp a joint commit; it does not supply the commit")
    unitary = reversible_joint_read_clock_unitary()
    check("the joint read-and-timestamp map is unitary", np.linalg.norm(unitary.conj().T @ unitary - np.eye(64)) < TOL)
    clock_2 = np.array([0, 0, 1, 0], dtype=complex)
    blank_4 = np.array([1, 0, 0, 0], dtype=complex)
    initial = ket_all(PLUS, KET0, clock_2, blank_4)
    tagged = unitary @ initial
    check("the complete outcome-and-time tag reverses exactly", np.linalg.norm(unitary.conj().T @ tagged - initial) < TOL)

    tagged_rho = density(tagged)
    joint_diag = np.zeros((2, 4), dtype=float)
    for reader in range(2):
        for stamp in range(4):
            projector = np.zeros((64, 64), dtype=complex)
            for source in range(2):
                for clock in range(4):
                    index = np.ravel_multi_index((source, reader, clock, stamp), (2, 2, 4, 4))
                    projector[index, index] = 1.0
            joint_diag[reader, stamp] = float(np.trace(projector @ tagged_rho).real)
    check("the timestamp is the same for both possible outcomes", abs(joint_diag[0, 2] - 0.5) < TOL and abs(joint_diag[1, 2] - 0.5) < TOL and abs(np.sum(joint_diag[:, [0, 1, 3]])) < TOL)

    committed = dephase_indices(tagged_rho, (2, 2, 4, 4), (1, 3))
    after_inverse = unitary.conj().T @ committed @ unitary
    restored_source = partial_trace(after_inverse, (0,), (2, 2, 4, 4))
    check("a separately supplied joint commit blocks coherent source restoration", purity(restored_source) < 0.51)

    events = np.arange(8, dtype=float)
    clock_a = events
    clock_b = 3.0 * events + 2.0
    slope, intercept = np.polyfit(clock_a, clock_b, 1)
    check("repeated coincidence records determine a relative clock calibration", abs(slope - 3.0) < TOL and abs(intercept - 2.0) < TOL)

    warped_a = clock_a**3
    check("a monotone reparameterization preserves event order while changing intervals", np.all(np.diff(warped_a) > 0) and not np.allclose(np.diff(warped_a), np.diff(clock_a)))
    phases = (1 % 4, 5 % 4)
    check("a periodic phase alone aliases distinct event times", phases[0] == phases[1])


def controlled_phase(nqubits: int, left: int, right: int, angle: float) -> np.ndarray:
    dim = 2**nqubits
    diagonal = np.ones(dim, dtype=complex)
    for index in range(dim):
        bits = [(index >> (nqubits - 1 - q)) & 1 for q in range(nqubits)]
        if bits[left] and bits[right]:
            diagonal[index] = np.exp(1j * angle)
    return np.diag(diagonal)


def probe_asynchronous_causal_schedule() -> None:
    section("F5 - Local causal schedules: spacelike consistency and overlap laws")
    disjoint_left = cnot(4, 0, 1)
    disjoint_right = cnot(4, 2, 3)
    check("spacelike disjoint writes commute", np.linalg.norm(disjoint_left @ disjoint_right - disjoint_right @ disjoint_left) < TOL)

    overlap_1 = cnot(3, 0, 1)
    overlap_2 = cnot(3, 1, 2)
    check("overlapping controlled copies do not define a schedule-free rule", np.linalg.norm(overlap_1 @ overlap_2 - overlap_2 @ overlap_1) > 1.0)

    phase_1 = controlled_phase(3, 0, 1, 0.37)
    phase_2 = controlled_phase(3, 1, 2, -0.21)
    check("a nontrivial overlapping diagonal rule can be schedule-independent", np.linalg.norm(phase_1 @ phase_2 - phase_2 @ phase_1) < TOL)

    bell_pairs = ket_all(PLUS, KET0, PLUS, KET0)
    rho = density(bell_pairs)
    left_commit = dephase_indices(rho, (2, 2, 2, 2), (1,))
    left_then_right = dephase_indices(left_commit, (2, 2, 2, 2), (3,))
    right_commit = dephase_indices(rho, (2, 2, 2, 2), (3,))
    right_then_left = dephase_indices(right_commit, (2, 2, 2, 2), (1,))
    check("disjoint local commits are order-independent on a causal diamond", np.linalg.norm(left_then_right - right_then_left) < TOL)

    forward = overlap_2 @ overlap_1
    inverse = overlap_1.conj().T @ overlap_2.conj().T
    check("unitary causal order reverses by reversing the local order", np.linalg.norm(inverse @ forward - np.eye(8)) < TOL)
    committed = dephase_indices(density(forward @ ket_all(PLUS, KET0, KET0)), (2, 2, 2), (2,))
    rewound = inverse @ committed @ inverse.conj().T
    check("inserting a commit is the time-asymmetric ingredient in this circuit", purity(rewound) < 0.76)


def probe_capacity_topologies() -> None:
    section("F6 - Permanent-record capacity under site, edge, frontier, and sparse models")
    nsites = 12
    site_capacity = nsites
    ring_edge_capacity = nsites
    visits = 4 * nsites
    check("one permanent site record per event saturates after N events", min(visits, site_capacity) == nsites and visits > site_capacity)
    check("moving the record to finite ring edges changes identity but not finite capacity", visits > ring_edge_capacity)

    frontier_positions = list(range(visits))
    check("the already-infinite lattice permits a fresh nonrecurrent frontier without lattice growth", len(frontier_positions) == len(set(frontier_positions)))

    recurrent_positions = [tick % nsites for tick in range(visits)]
    fresh_recurrent_sites = len(set(recurrent_positions))
    exported_bits_needed = visits - fresh_recurrent_sites
    check("a recurrent observed process needs exported fresh memory after local sites fill", exported_bits_needed == 3 * nsites)

    pattern = np.zeros(nsites, dtype=int)
    pattern[[1, 2, 5]] = 1
    evolved = pattern.copy()
    for _ in range(5 * nsites):
        evolved = np.roll(evolved, 1)
    check("a reversible working pattern can propagate through reused sites without appending records", np.array_equal(evolved, pattern))

    detector_period = 6
    sparse_events = [tick for tick in range(visits) if tick % detector_period == 0]
    check("sparse commits reduce but do not remove unbounded archive growth", 0 < len(sparse_events) < visits and len(sparse_events) == math.ceil(visits / detector_period))

    modular_phases = [tick % 4 for tick in range(20)]
    check("a reusable periodic clock state is finite but is not a permanent event ledger", len(set(modular_phases)) == 4 and len(modular_phases) > 4)


def periodic_poisson(source: np.ndarray) -> np.ndarray:
    size = len(source)
    laplacian = np.zeros((size, size), dtype=float)
    for index in range(size):
        laplacian[index, index] = 2.0
        laplacian[index, (index - 1) % size] = -1.0
        laplacian[index, (index + 1) % size] = -1.0
    centered = source - np.mean(source)
    potential = np.linalg.pinv(laplacian) @ centered
    return potential - np.mean(potential)


def probe_resource_lapse() -> None:
    section("F7 - Storage, throughput, moving sources, and universal clock response")
    size = 31
    path = (4, 10, 16, 22)
    active_source = np.zeros(size)
    active_source[path[-1]] = 1.0
    archive_source = np.zeros(size)
    for position in path:
        archive_source[position] += 1.0
    active_potential = periodic_poisson(active_source)
    archive_potential = periodic_poisson(archive_source)
    check("the moving active load conserves total source strength", abs(np.sum(active_source) - 1.0) < TOL)
    check("an append-only archive grows source strength unless separately charged", abs(np.sum(archive_source) - len(path)) < TOL)
    trail_contrast = abs(archive_potential[path[0]] - active_potential[path[0]])
    check("archive sourcing leaves a distinct field at an abandoned position", trail_contrast > 0.1, f"contrast={trail_contrast:.6f}")

    loads = np.array([0.0, 0.2, 0.5, 0.8])
    laws = {
        "linear": 1.0 - loads,
        "exponential": np.exp(-loads),
        "reciprocal": 1.0 / (1.0 + loads),
    }
    check("multiple normalized monotone throughput laws survive the same resource story", all(abs(values[0] - 1.0) < TOL and np.all(np.diff(values) < 0) for values in laws.values()) and not np.allclose(laws["linear"], laws["exponential"]))

    phi = 0.3
    lapse_linear = 1.0 - phi
    lapse_exponential = math.exp(-phi)
    check("the source field does not select a unique potential-to-clock map", abs(lapse_linear - lapse_exponential) > 0.03)

    common_clock_a = math.exp(-phi)
    common_clock_b = math.exp(-phi)
    species_clock_b = 1.0 / (1.0 + phi)
    check("universal redshift requires the same response law for distinct clock species", abs(common_clock_a - common_clock_b) < TOL and abs(common_clock_a - species_clock_b) > 0.02)

    initial_free_capacity = 10
    archive_events = 4
    free_capacity = initial_free_capacity - archive_events
    check("a conserved storage ledger makes each permanent append consume finite free capacity", free_capacity + archive_events == initial_free_capacity and free_capacity < initial_free_capacity)


def quantum_walk_operator(size: int) -> np.ndarray:
    coin = np.kron(np.eye(size), H)
    shift = np.zeros((2 * size, 2 * size), dtype=complex)
    for position in range(size):
        shift[2 * ((position - 1) % size), 2 * position] = 1.0
        shift[2 * ((position + 1) % size) + 1, 2 * position + 1] = 1.0
    return shift @ coin


def dephase_position(rho: np.ndarray, size: int) -> np.ndarray:
    out = rho.copy()
    for p in range(size):
        for q in range(size):
            if p != q:
                out[2 * p : 2 * p + 2, 2 * q : 2 * q + 2] = 0.0
    return out


def position_variance(rho: np.ndarray, size: int, origin: int) -> float:
    probabilities = np.array([np.trace(rho[2 * p : 2 * p + 2, 2 * p : 2 * p + 2]).real for p in range(size)])
    coordinates = np.arange(size, dtype=float) - origin
    mean = float(np.sum(coordinates * probabilities))
    return float(np.sum((coordinates - mean) ** 2 * probabilities))


def metropolis_kernel(energies: np.ndarray, beta: float, proposal: float = 0.15) -> np.ndarray:
    size = len(energies)
    kernel = np.zeros((size, size), dtype=float)
    for i in range(size):
        for j in range(size):
            if i != j:
                kernel[i, j] = proposal * min(1.0, math.exp(-beta * (energies[j] - energies[i])))
        kernel[i, i] = 1.0 - np.sum(kernel[i])
    return kernel


def stationary_distribution(kernel: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eig(kernel.T)
    index = int(np.argmin(np.abs(values - 1.0)))
    vector = vectors[:, index].real
    if np.sum(vector) < 0:
        vector *= -1.0
    return vector / np.sum(vector)


def probe_coherent_matter_and_thermal() -> None:
    section("F8 - Coherent propagation and thermalization survive only with separate laws")
    size = 81
    origin = size // 2
    steps = 20
    walk = quantum_walk_operator(size)
    initial = np.zeros(2 * size, dtype=complex)
    initial[2 * origin] = 1.0 / math.sqrt(2.0)
    initial[2 * origin + 1] = 1j / math.sqrt(2.0)

    coherent = initial.copy()
    for _ in range(steps):
        coherent = walk @ coherent
    coherent_rho = density(coherent)
    decohered = density(initial)
    for _ in range(steps):
        decohered = dephase_position(walk @ decohered @ walk.conj().T, size)
    coherent_variance = position_variance(coherent_rho, size, origin)
    decohered_variance = position_variance(decohered, size, origin)
    check("every-step position commits change coherent matter propagation", coherent_variance > 2.0 * decohered_variance, f"variances={coherent_variance:.3f},{decohered_variance:.3f}")

    sparse_final_commit = dephase_position(coherent_rho, size)
    check("a final sparse read preserves the pre-read position statistics", abs(position_variance(sparse_final_commit, size, origin) - coherent_variance) < TOL)
    rewound = np.linalg.matrix_power(walk.conj().T, steps) @ coherent
    check("the uncommitted coherent walk reverses exactly", np.linalg.norm(rewound - initial) < 1.0e-9)

    energies = np.array([0.0, 1.0, 2.0])
    beta = 0.8
    kernel = metropolis_kernel(energies, beta)
    gibbs = np.exp(-beta * energies)
    gibbs /= np.sum(gibbs)
    stationary = stationary_distribution(kernel)
    check("local detailed balance produces the supplied-beta Gibbs state", np.linalg.norm(stationary - gibbs) < TOL)

    distribution = np.array([0.02, 0.03, 0.95])
    divergences = []
    for _ in range(30):
        divergences.append(relative_entropy_classical(distribution, gibbs))
        distribution = distribution @ kernel
    check("relative entropy to Gibbs decreases under the detailed-balance kernel", all(divergences[i + 1] <= divergences[i] + TOL for i in range(len(divergences) - 1)))

    second_beta = 0.2
    second_kernel = metropolis_kernel(energies, second_beta)
    check("the same record-transition grammar admits a different temperature", np.linalg.norm(stationary_distribution(second_kernel) - stationary) > 0.2)

    deterministic_word_entropy = 0.0
    fair_word_entropy = 20.0 * math.log(2.0)
    check("equal record counts can carry unequal ensemble entropy", deterministic_word_entropy != fair_word_entropy)


def main() -> int:
    print("BARE-METAL RECORD FORMATION - FINAL MINIMUM VIABLE PROBES")
    print("Finite discriminators only; no axiom, primitive, registry, or audit status is changed.")
    probe_permanence_scope()
    probe_selective_commit_sweep()
    probe_two_register_tomography()
    probe_joint_clock_commit()
    probe_asynchronous_causal_schedule()
    probe_capacity_topologies()
    probe_resource_lapse()
    probe_coherent_matter_and_thermal()
    section("SCORECARD")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("INTERPRETATION: passing a toy check narrows language; it does not derive a physical formation law.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
