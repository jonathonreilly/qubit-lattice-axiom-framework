#!/usr/bin/env python3
"""Minimum viable discriminators for candidate record-formation architectures.

This is a source-side toy harness, not an axiom derivation or audit surface.
Every result is scoped to the explicit finite model in the corresponding
block.  The purpose is to find which words a future formation statement may
or may not safely carry before constitutional drafting begins.
"""

from __future__ import annotations

import itertools
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


def embed(op: np.ndarray, nqubits: int, target: int) -> np.ndarray:
    ops = [I2] * nqubits
    ops[target] = op
    return kron_all(*ops)


def cnot(nqubits: int, control: int, target: int) -> np.ndarray:
    dim = 2**nqubits
    out = np.zeros((dim, dim), dtype=complex)
    for column in range(dim):
        bits = [(column >> (nqubits - 1 - q)) & 1 for q in range(nqubits)]
        mapped = list(bits)
        mapped[target] ^= bits[control]
        row = 0
        for bit in mapped:
            row = (row << 1) | bit
        out[row, column] = 1.0
    return out


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


def purity(rho: np.ndarray) -> float:
    return float(np.trace(rho @ rho).real)


def visibility(rho_qubit: np.ndarray) -> float:
    return float(2.0 * abs(rho_qubit[0, 1]))


def dephase_qubit(rho: np.ndarray, nqubits: int, target: int, basis_op: np.ndarray = Z) -> np.ndarray:
    p_plus = (I2 + basis_op) / 2.0
    p_minus = (I2 - basis_op) / 2.0
    projectors = [embed(p_plus, nqubits, target), embed(p_minus, nqubits, target)]
    return sum(projector @ rho @ projector for projector in projectors)


def expectation(psi: np.ndarray, op: np.ndarray) -> float:
    return float(np.vdot(psi, op @ psi).real)


def probe_unitary_clock_and_commit() -> None:
    section("P1 - A unitary clock tag is correlation, not irreversible commit")
    psi0 = ket_all(PLUS, KET0, KET0)  # source, reader, clock register
    u_read = cnot(3, 0, 1)
    u_clock_carries_outcome = cnot(3, 1, 2)
    u_total = u_clock_carries_outcome @ u_read
    psi_tagged = u_total @ psi0

    source_after = partial_trace(density(psi_tagged), (0,), (2, 2, 2))
    check("source is locally dephased while the tagged global state remains pure",
          abs(purity(source_after) - 0.5) < TOL and abs(purity(density(psi_tagged)) - 1.0) < TOL)
    restored = u_total.conj().T @ psi_tagged
    check("the full unitary read-plus-clock tag reverses exactly",
          np.linalg.norm(restored - psi0) < TOL)

    u_unconditional_tick = embed(X, 3, 2)
    psi_tick = u_unconditional_tick @ u_read @ psi0
    z_source = embed(Z, 3, 0)
    z_clock = embed(Z, 3, 2)
    cov_tick = expectation(psi_tick, z_source @ z_clock) - expectation(psi_tick, z_source) * expectation(psi_tick, z_clock)
    check("an outcome-blind clock tick carries no outcome correlation", abs(cov_tick) < TOL)

    cov_cond = expectation(psi_tagged, z_source @ z_clock) - expectation(psi_tagged, z_source) * expectation(psi_tagged, z_clock)
    check("an outcome-conditioned clock register is another outcome witness", abs(cov_cond - 1.0) < TOL)

    rho_tagged = density(psi_tagged)
    rho_committed = dephase_qubit(rho_tagged, 3, 0)
    rho_after_inverse = u_total.conj().T @ rho_committed @ u_total
    source_after_inverse = partial_trace(rho_after_inverse, (0,), (2, 2, 2))
    check("adding a nonunitary/superselected commit changes the reversal result",
          abs(purity(source_after_inverse) - 0.5) < TOL and visibility(source_after_inverse) < TOL)


def probe_one_two_witness_reversal() -> None:
    section("P2 - One/two witnesses distinguish local robustness, not global permanence")
    psi0 = ket_all(PLUS, KET0, KET0)
    u_r1 = cnot(3, 0, 1)
    u_r2 = cnot(3, 0, 2)
    u_two = u_r2 @ u_r1
    psi_two = u_two @ psi0

    psi_undo_one = u_r1 @ psi_two
    source_undo_one = partial_trace(density(psi_undo_one), (0,), (2, 2, 2))
    check("undoing one witness leaves the source decohered through the other",
          abs(purity(source_undo_one) - 0.5) < TOL and visibility(source_undo_one) < TOL)

    psi_undo_both = u_two.conj().T @ psi_two
    check("coherent access to both witnesses globally restores the source",
          np.linalg.norm(psi_undo_both - psi0) < TOL)

    psi_one = u_r1 @ psi0
    check("a single controlled copy is adjoint-revocable",
          np.linalg.norm(u_r1.conj().T @ psi_one - psi0) < TOL)

    rho_r1 = partial_trace(density(psi_two), (1,), (2, 2, 2))
    rho_r2 = partial_trace(density(psi_two), (2,), (2, 2, 2))
    check("the two disjoint witnesses have matching local outcome statistics",
          np.linalg.norm(rho_r1 - rho_r2) < TOL)


def probe_bell_and_order() -> None:
    section("P3 - Bell, no-signaling, and spacelike commit-order controls")
    phi_plus = (ket_all(KET0, KET0) + ket_all(KET1, KET1)) / math.sqrt(2.0)
    a0, a1 = Z, X
    b0 = (Z + X) / math.sqrt(2.0)
    b1 = (Z - X) / math.sqrt(2.0)
    chsh = (
        np.kron(a0, b0)
        + np.kron(a0, b1)
        + np.kron(a1, b0)
        - np.kron(a1, b1)
    )
    value = expectation(phi_plus, chsh)
    check("quantum two-site carrier reaches the Tsirelson value", abs(value - 2.0 * math.sqrt(2.0)) < TOL,
          f"S={value:.12f}")

    deterministic_values = []
    for aa0, aa1, bb0, bb1 in itertools.product((-1, 1), repeat=4):
        deterministic_values.append(aa0 * bb0 + aa0 * bb1 + aa1 * bb0 - aa1 * bb1)
    check("preassigned local binary outcomes remain at the classical CHSH bound",
          max(abs(v) for v in deterministic_values) == 2)

    rho = density(phi_plus)
    alice_before = partial_trace(rho, (0,), (2, 2))
    bob0_unread = dephase_qubit(rho, 2, 1, b0)
    bob1_unread = dephase_qubit(rho, 2, 1, b1)
    alice_after_b0 = partial_trace(bob0_unread, (0,), (2, 2))
    alice_after_b1 = partial_trace(bob1_unread, (0,), (2, 2))
    check("remote unread commits do not change Alice's local state",
          np.linalg.norm(alice_before - alice_after_b0) < TOL
          and np.linalg.norm(alice_before - alice_after_b1) < TOL)

    a_then_b = dephase_qubit(dephase_qubit(rho, 2, 0, a0), 2, 1, b0)
    b_then_a = dephase_qubit(dephase_qubit(rho, 2, 1, b0), 2, 0, a0)
    check("commuting local nonselective instruments are order-independent",
          np.linalg.norm(a_then_b - b_then_a) < TOL)


def probe_clock_metric() -> None:
    section("P4 - Clock readings supply order only after a monotone ledger map")
    word = (0, 1, 1, 0)
    clocks = {
        "uniform": (0.0, 1.0, 2.0, 3.0, 4.0),
        "slow": (0.0, 2.0, 4.0, 6.0, 8.0),
        "accelerating": (0.0, 1.0, 3.0, 6.0, 10.0),
    }
    rates = {name: len(word) / (times[-1] - times[0]) for name, times in clocks.items()}
    check("one record word admits inequivalent physical rates", len(set(rates.values())) == 3, str(rates))

    oscillator_period = 4
    event_indices = (1, 5)
    phases = tuple(index % oscillator_period for index in event_indices)
    check("a periodic reference phase aliases distinct events", phases[0] == phases[1], f"phases={phases}")
    check("a monotone ledger index removes the phase alias", event_indices[0] < event_indices[1])


def probe_capacity_and_reuse() -> None:
    section("P5 - Permanent first-registration capacity and site reuse")
    nsites = 8
    occupied: set[int] = set()
    new_events = []
    for tick in range(nsites + 3):
        site = tick % nsites
        before = len(occupied)
        occupied.add(site)
        new_events.append(len(occupied) - before)
    check("committing every visit saturates a fixed N-site region after N first registrations",
          new_events[:nsites] == [1] * nsites and new_events[nsites:] == [0, 0, 0], str(new_events))

    walker_positions = [tick % 4 for tick in range(12)]
    committed_positions = set(walker_positions)
    check("recurrent reversible motion revisits sites after the permanent ledger is full",
          len(walker_positions) > len(committed_positions) and len(committed_positions) == 4)

    growing_capacity = [tick + 1 for tick in range(12)]
    commits = list(range(1, 13))
    check("one-commit-per-tick continuation works if fresh capacity grows by assumption",
          all(commit <= capacity for commit, capacity in zip(commits, growing_capacity)))

    sink_bits = 9
    exported_per_reset = 3
    check("a finite sink supports only finitely many arbitrary clean reuse cycles",
          sink_bits // exported_per_reset == 3)


def probe_probability_and_preparation() -> None:
    section("P6 - Formation form, frame form, and prepared-state identity are separate")
    write = np.zeros((4, 2), dtype=complex)
    write[0, 0] = 1.0
    write[3, 1] = 1.0
    check("the controlled-copy write is an isometry", np.linalg.norm(write.conj().T @ write - I2) < TOL)

    branch_weights = []
    for p0 in (0.2, 0.8):
        psi = np.array([math.sqrt(p0), math.sqrt(1.0 - p0)], dtype=complex)
        out = write @ psi
        branch_weights.append((abs(out[0]) ** 2, abs(out[3]) ** 2))
    check("the same write form permits different input outcome weights",
          np.linalg.norm(np.array(branch_weights[0]) - np.array(branch_weights[1])) > 0.5,
          str(branch_weights))

    directions = []
    for vector in (
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1),
    ):
        n = np.array(vector, dtype=float)
        n /= np.linalg.norm(n)
        directions.extend((n, -n))
    rogue = np.array([(1.0 + n[2] ** 3) / 2.0 for n in directions])
    antipodal_ok = all(abs(rogue[2 * i] + rogue[2 * i + 1] - 1.0) < TOL for i in range(len(directions) // 2))
    design = np.array(directions) / 2.0
    target = rogue - 0.5
    _, _, _, _ = np.linalg.lstsq(design, target, rcond=None)
    fitted = design @ np.linalg.lstsq(design, target, rcond=None)[0] + 0.5
    residual = float(np.max(np.abs(fitted - rogue)))
    check("a one-qubit non-Born frame assignment normalizes every antipodal menu", antipodal_ok)
    check("that assignment is not representable by one density-matrix Bloch vector", residual > 0.05,
          f"max residual={residual:.6f}")

    prep_state = density(KET0)
    alternative_frame_state = I2 / 2.0
    p_prep = float(np.trace(prep_state @ density(KET0)).real)
    p_alt = float(np.trace(alternative_frame_state @ density(KET0)).real)
    check("density-form alone does not identify the frame state with the preparation",
          abs(p_prep - 1.0) < TOL and abs(p_alt - 0.5) < TOL)


def probe_basis_covariance() -> None:
    section("P7 - A universal commit criterion cannot silently name a gauge frame")
    rho = density(KET0)

    def z_dephase(state: np.ndarray) -> np.ndarray:
        p0 = density(KET0)
        p1 = density(KET1)
        return p0 @ state @ p0 + p1 @ state @ p1

    left = z_dephase(H @ rho @ H.conj().T)
    right = H @ z_dephase(rho) @ H.conj().T
    violation = float(np.linalg.norm(left - right))
    check("fixed-basis dephasing fails covariance under a basis rotation", violation > 0.5,
          f"norm={violation:.6f}")
    check("trace-only record content is invariant under the same rotation",
          abs(np.trace(rho) - np.trace(H @ rho @ H.conj().T)) < TOL)


def stationary_distribution(kernel: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eig(kernel.T)
    index = int(np.argmin(np.abs(values - 1.0)))
    vector = vectors[:, index].real
    vector /= np.sum(vector)
    if np.any(vector < 0):
        vector *= -1.0
    return vector / np.sum(vector)


def probe_thermodynamic_kernel() -> None:
    section("P8 - Record append semantics does not select equilibrium or temperature")
    uniform_kernel = np.array([[0.9, 0.1], [0.1, 0.9]], dtype=float)
    biased_kernel = np.array([[0.9, 0.1], [0.3, 0.7]], dtype=float)
    pi_uniform = stationary_distribution(uniform_kernel)
    pi_biased = stationary_distribution(biased_kernel)
    check("two valid one-record-per-step kernels have different stationary states",
          np.linalg.norm(pi_uniform - pi_biased) > 0.3,
          f"uniform={pi_uniform}, biased={pi_biased}")

    beta = math.log(3.0)
    gibbs = np.array([1.0, math.exp(-beta)])
    gibbs /= np.sum(gibbs)
    detailed_balance = abs(pi_biased[0] * biased_kernel[0, 1] - pi_biased[1] * biased_kernel[1, 0]) < TOL
    check("the biased kernel is Gibbs only after a detailed-balance rate ratio is supplied",
          detailed_balance and np.linalg.norm(pi_biased - gibbs) < TOL,
          f"beta={beta:.6f}, pi={pi_biased}")


def probe_resource_gravity() -> None:
    section("P9 - Storage and throughput are distinct; archive sourcing leaves trails")
    a0 = 2.0
    response_factors = {
        "linear": 1.0,
        "square_root": 0.5,
        "saturating": 1.0 / (1.0 + a0),
    }
    check("monotone formation-rate laws give different local lapse responses",
          len({round(value, 12) for value in response_factors.values()}) == 3,
          str(response_factors))

    size = 21
    positions = (4, 8, 12, 16)
    length = 2.5

    def field_at(source: int) -> np.ndarray:
        x = np.arange(size)
        return np.exp(-np.abs(x - source) / length)

    active = field_at(positions[-1])
    archive = sum((field_at(position) for position in positions), np.zeros(size))
    old_site = positions[0]
    trail = float(archive[old_site] - active[old_site])
    check("an undifferentiated permanent archive produces a field at an abandoned source site",
          trail > 1.0, f"trail={trail:.6f}")

    load = 0.4
    universal_rate_a = 1.0 / (1.0 + load)
    universal_rate_b = 1.0 / (1.0 + load)
    nonuniversal_rate_b = 1.0 / math.sqrt(1.0 + load)
    check("universal time dilation requires every clock species to consume the same rate law",
          abs(universal_rate_a - universal_rate_b) < TOL
          and abs(universal_rate_a - nonuniversal_rate_b) > 0.05)


def probe_matter_statistics_and_chirality() -> None:
    section("P10 - Record occupancy does not select matter statistics or chirality")
    direct_amplitude = 1.0
    exchange_amplitude_boson = 1.0
    exchange_amplitude_fermion = -1.0
    boson_intensity = abs(direct_amplitude + exchange_amplitude_boson) ** 2
    fermion_intensity = abs(direct_amplitude + exchange_amplitude_fermion) ** 2
    check("identical endpoint occupancy permits different exchange interference",
          boson_intensity == 4.0 and fermion_intensity == 0.0)

    frame = np.eye(3)
    proper_rotation = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=float)
    mirror = np.diag([-1.0, 1.0, 1.0])
    original_sign = np.linalg.det(frame)
    proper_sign = np.linalg.det(proper_rotation @ frame)
    mirror_sign = np.linalg.det(mirror @ frame)
    check("an ordered source-reader-clock frame is orientation-sensitive",
          original_sign > 0 and proper_sign > 0 and mirror_sign < 0)
    check("the two mirror orientations remain distinct candidate branches",
          abs(proper_sign + mirror_sign) < TOL)


def probe_collapse_energy_and_wigner() -> None:
    section("P11 - Fundamental commit and branch-relative record controls")
    rho_plus = density(PLUS)
    energy_before = float(np.trace(rho_plus @ X).real)
    rho_after_z_commit = dephase_qubit(rho_plus, 1, 0, Z)
    energy_after = float(np.trace(rho_after_z_commit @ X).real)
    check("a Z-commit channel need not conserve a noncommuting X-Hamiltonian energy",
          abs(energy_before - 1.0) < TOL and abs(energy_after) < TOL)
    rho_z_eigen = density(KET0)
    check("the same commit conserves a commuting Z pointer eigenstate",
          np.linalg.norm(dephase_qubit(rho_z_eigen, 1, 0, Z) - rho_z_eigen) < TOL)

    psi0 = ket_all(PLUS, KET0)  # system and Wigner's friend memory
    u_friend = cnot(2, 0, 1)
    psi_friend = u_friend @ psi0
    friend_local = partial_trace(density(psi_friend), (1,), (2, 2))
    check("the friend has a locally classical record after the unitary write",
          np.linalg.norm(friend_local - I2 / 2.0) < TOL)
    psi_wigner_reversal = u_friend.conj().T @ psi_friend
    check("an external coherent reversal erases that unitary friend record globally",
          np.linalg.norm(psi_wigner_reversal - psi0) < TOL)


def probe_update_order_and_foliation() -> None:
    section("P12 - Local causal order does not itself choose a global update foliation")
    left = cnot(4, 0, 1)
    right = cnot(4, 2, 3)
    check("disjoint local updates commute", np.linalg.norm(left @ right - right @ left) < TOL)

    first = cnot(3, 0, 1)
    second = cnot(3, 1, 2)
    commutator_norm = float(np.linalg.norm(first @ second - second @ first))
    check("overlapping local updates require an ordering rule", commutator_norm > 1.0,
          f"commutator norm={commutator_norm:.6f}")


def probe_action_cost_interface() -> None:
    section("P13 - Multiplicative history weights permit additive costs but do not select one")
    w1, w2 = 0.8, 0.3
    composed_weight = w1 * w2
    composed_cost = -math.log(composed_weight)
    additive_cost = -math.log(w1) - math.log(w2)
    check("independent supplied history weights give additive negative-log cost",
          abs(composed_cost - additive_cost) < TOL)

    alternatives = ((0.8, 0.3), (0.7, 0.4), (0.9, 0.2))
    costs = tuple(-math.log(a * b) for a, b in alternatives)
    check("composition algebra alone leaves multiple action-cost assignments",
          len({round(cost, 12) for cost in costs}) == len(costs), str(costs))


def probe_composite_context_and_prep_frame() -> None:
    section("P14 - Composite context consistency and PREP-FRAME discriminator")
    amplitudes = np.array(
        [math.sqrt(0.2), math.sqrt(0.3), math.sqrt(0.1), math.sqrt(0.4)],
        dtype=complex,
    )
    standard = np.eye(4, dtype=complex)
    rotated = np.eye(4, dtype=complex)
    rotated[:, 1] = (standard[:, 1] + standard[:, 2]) / math.sqrt(2.0)
    rotated[:, 2] = (standard[:, 1] - standard[:, 2]) / math.sqrt(2.0)

    def probabilities(basis: np.ndarray) -> np.ndarray:
        return np.abs(basis.conj().T @ amplitudes) ** 2

    p_standard = probabilities(standard)
    p_rotated = probabilities(rotated)
    check("Born-linear weight of a shared projector is context-independent",
          abs(p_standard[0] - p_rotated[0]) < TOL)

    q = 2.0
    power_standard = p_standard**q / np.sum(p_standard**q)
    power_rotated = p_rotated**q / np.sum(p_rotated**q)
    check("a normalized power-law alternative is context-dependent on M_4",
          abs(power_standard[0] - power_rotated[0]) > 0.01,
          f"shared weights={power_standard[0]:.6f},{power_rotated[0]:.6f}")

    psi_projector = density(amplitudes)
    maximally_mixed_frame = np.eye(4, dtype=complex) / 4.0
    prepared_certainty = float(np.trace(psi_projector @ psi_projector).real)
    mismatched_certainty = float(np.trace(maximally_mixed_frame @ psi_projector).real)
    check("a valid frame state can fail prepared-state eigenstate certainty",
          abs(prepared_certainty - 1.0) < TOL and abs(mismatched_certainty - 0.25) < TOL)

    phase_zero = np.array([1.0, 1.0, 0.0, 0.0], dtype=complex) / math.sqrt(2.0)
    phase_quarter = np.array([1.0, 1.0j, 0.0, 0.0], dtype=complex) / math.sqrt(2.0)
    pointer_zero = np.abs(phase_zero) ** 2
    pointer_quarter = np.abs(phase_quarter) ** 2
    plus_projector = density(phase_zero)
    plus_zero = float(np.trace(density(phase_zero) @ plus_projector).real)
    plus_quarter = float(np.trace(density(phase_quarter) @ plus_projector).real)
    check("two states can have identical agreement-basis data but different phase-sensitive reads",
          np.linalg.norm(pointer_zero - pointer_quarter) < TOL
          and abs(plus_zero - plus_quarter) > 0.4,
          f"phase-sensitive weights={plus_zero:.6f},{plus_quarter:.6f}")


def probe_reversible_local_clock_construction() -> None:
    section("P15 - A local reference can timestamp a commit without already being a record")
    dim = 4
    clock_phase = np.zeros(dim, dtype=complex)
    clock_phase[2] = 1.0
    blank_stamp = np.zeros(dim, dtype=complex)
    blank_stamp[0] = 1.0
    copy_phase = np.zeros((dim * dim, dim * dim), dtype=complex)
    for clock in range(dim):
        for stamp in range(dim):
            source = clock * dim + stamp
            target = clock * dim + ((stamp + clock) % dim)
            copy_phase[target, source] = 1.0
    check("phase-copy map is unitary", np.linalg.norm(copy_phase.conj().T @ copy_phase - np.eye(dim * dim)) < TOL)

    initial = np.kron(clock_phase, blank_stamp)
    timestamped = copy_phase @ initial
    stamp_state = partial_trace(density(timestamped), (1,), (dim, dim))
    expected_stamp = density(clock_phase)
    check("a definite reversible reference phase is copied into a blank timestamp register",
          np.linalg.norm(stamp_state - expected_stamp) < TOL)
    check("the timestamp correlation remains globally reversible",
          np.linalg.norm(copy_phase.conj().T @ timestamped - initial) < TOL)

    clock_superposition = np.zeros(dim, dtype=complex)
    clock_superposition[0] = 1.0 / math.sqrt(2.0)
    clock_superposition[1] = 1.0 / math.sqrt(2.0)
    entangled_stamp = copy_phase @ np.kron(clock_superposition, blank_stamp)
    local_clock = partial_trace(density(entangled_stamp), (0,), (dim, dim))
    check("copying an unresolved reference phase entangles clock and timestamp",
          abs(purity(local_clock) - 0.5) < TOL)


def probe_semantic_state_machine() -> None:
    section("P16 - Minimal semantic consistency filter for formation vocabularies")
    routes = {
        "first_unitary_write_strict": {"global_reversible": True, "permanence": "strict"},
        "two_witness_strict": {"global_reversible": True, "permanence": "strict"},
        "two_witness_local": {"global_reversible": True, "permanence": "local"},
        "unitary_clock_strict": {"global_reversible": True, "permanence": "strict"},
        "fundamental_append_strict": {"global_reversible": False, "permanence": "strict"},
        "relational_record_local": {"global_reversible": True, "permanence": "local"},
        "sink_export_local": {"global_reversible": True, "permanence": "local"},
    }

    def semantically_consistent(route: dict[str, object]) -> bool:
        return not (route["permanence"] == "strict" and route["global_reversible"] is True)

    verdicts = {name: semantically_consistent(route) for name, route in routes.items()}
    check("strict permanence conflicts with calling a globally reversible stage a record",
          not verdicts["first_unitary_write_strict"]
          and not verdicts["two_witness_strict"]
          and not verdicts["unitary_clock_strict"])
    check("strict fundamental append and local/relational readings survive the syntax filter",
          verdicts["fundamental_append_strict"]
          and verdicts["two_witness_local"]
          and verdicts["relational_record_local"]
          and verdicts["sink_export_local"])
    check("the syntax filter leaves multiple physical routes and therefore selects no axiom wording",
          sum(verdicts.values()) == 4, str(verdicts))


def main() -> int:
    print("BARE-METAL RECORD FORMATION - MINIMUM VIABLE PROBE HARNESS")
    print("Finite toy discriminators only; no axiom, primitive, or audit status is changed.")
    probe_unitary_clock_and_commit()
    probe_one_two_witness_reversal()
    probe_bell_and_order()
    probe_clock_metric()
    probe_capacity_and_reuse()
    probe_probability_and_preparation()
    probe_basis_covariance()
    probe_thermodynamic_kernel()
    probe_resource_gravity()
    probe_matter_statistics_and_chirality()
    probe_collapse_energy_and_wigner()
    probe_update_order_and_foliation()
    probe_action_cost_interface()
    probe_composite_context_and_prep_frame()
    probe_reversible_local_clock_construction()
    probe_semantic_state_machine()
    section("SCORECARD")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("INTERPRETATION: use the accompanying probe map; passing a toy check is not a framework derivation.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
