#!/usr/bin/env python3
"""Finite constructive gate for the O/T/I/G/B TOE interfaces."""

from __future__ import annotations

from collections import deque
from pathlib import Path
import math

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "TOE_INTERFACE_CONSTRUCTIVE_GATE_NOTE_2026-07-13.md"
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
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
SM = np.array([[0, 1], [0, 0]], dtype=complex)
P0 = (I2 + Z) / 2.0
P1 = (I2 - Z) / 2.0


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def partial_trace_second(rho: np.ndarray) -> np.ndarray:
    return np.trace(rho.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def partial_transpose_second(rho: np.ndarray) -> np.ndarray:
    return rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)


def source_contract() -> None:
    section("A - Source and interface contract")
    text = NOTE.read_text(encoding="utf-8").lower()
    normalized = text.replace("*", "").replace("`", "")
    check("A note is authority-free", "authority: none" in normalized)
    check("A all five interfaces are named", all(marker in text for marker in (
        "operational quantum closure", "time and causal continuum",
        "matter and physical individuation", "resource, thermodynamics, and gravity",
        "boundary and realized history",
    )))
    check("A interface completeness is not claimed", "not interface-complete" in text)
    check("A quantitative TOE is not claimed", "standard model" in text and "derivation" in text)
    check("A live edit is refused", "not enough to call the framework finished or to perform the one final axiom\nedit" in text)
    check("A N1-N8 gate is complete", all(f"### n{index}" in text for index in range(1, 9)))


def operational_interface() -> None:
    section("O - Operational closure witness")
    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)
    plus = (zero + one) / math.sqrt(2.0)
    minus = (zero - one) / math.sqrt(2.0)

    rho_zero = density(zero)
    rho_one = density(one)
    rho_z_mix = (rho_zero + rho_one) / 2.0
    rho_x_mix = (density(plus) + density(minus)) / 2.0
    effects = (P0, P1, (I2 + X) / 2.0, (I2 - X) / 2.0, (I2 + Y) / 2.0)

    check("O a test separates distinct preparations", abs(np.trace(rho_zero @ P0) - np.trace(rho_one @ P0)) > 0.9)
    check("O equivalent mixtures have the same density representation", np.linalg.norm(rho_z_mix - rho_x_mix) < TOL)
    check("O equivalent mixtures have identical tested probabilities", all(
        abs(np.trace(rho_z_mix @ effect) - np.trace(rho_x_mix @ effect)) < TOL
        for effect in effects
    ))

    phi = (np.kron(zero, zero) + np.kron(one, one)) / math.sqrt(2.0)
    rho_bell = density(phi)
    rho_a = partial_trace_second(rho_bell)
    check("O Bell marginal is normalized", abs(np.trace(rho_a) - 1.0) < TOL)
    check("O untouched spectator preserves every tested local probability", all(
        abs(np.trace(rho_bell @ np.kron(effect, I2)) - np.trace(rho_a @ effect)) < TOL
        for effect in effects
    ))

    p_first = float(np.trace(rho_z_mix @ P0).real)
    conditioned = P0 @ rho_z_mix @ P0 / p_first
    p_repeat = float(np.trace(conditioned @ P0).real)
    check("O the supplied selective instrument is repeatable", abs(p_repeat - 1.0) < TOL)

    one_site = density((zero + 1j * one) / math.sqrt(2.0))
    check("O transpose preserves one-site positivity", np.linalg.eigvalsh(one_site.T).min() > -TOL)
    check("O transpose fails ancilla stability", np.linalg.eigvalsh(partial_transpose_second(rho_bell)).min() < -0.49)


def time_interface() -> None:
    section("T - Causal order, rate, and continuum seed")

    origin = (0, 0, 0)
    reached = {origin: 0}
    queue: deque[tuple[int, int, int]] = deque([origin])
    while queue:
        x, y, z = queue.popleft()
        distance = reached[(x, y, z)]
        if distance == 4:
            continue
        for neighbor in ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)):
            if neighbor not in reached:
                reached[neighbor] = distance + 1
                queue.append(neighbor)
    check("T nearest-neighbor arrival time equals Manhattan distance", all(time == sum(abs(value) for value in site) for site, time in reached.items()))
    check("T finite time reaches a finite causal cone", len(reached) == 129)

    # Event DAG: A causes B and C; B and C independently precede D.
    edges = {"A": {"B", "C"}, "B": {"D"}, "C": {"D"}, "D": set()}

    def reachable(source: str, target: str) -> bool:
        frontier = [source]
        seen = set()
        while frontier:
            item = frontier.pop()
            if item == target:
                return True
            if item in seen:
                continue
            seen.add(item)
            frontier.extend(edges[item])
        return False

    check("T causal event order is acyclic", not any(
        reachable(target, source)
        for source, targets in edges.items()
        for target in targets
    ))
    check("T disjoint events can remain incomparable", not reachable("B", "C") and not reachable("C", "B"))
    check("T causal ancestry orders the final event", reachable("A", "D") and reachable("B", "D") and reachable("C", "D"))

    events = ("A", "B", "C", "D")
    dilated = tuple(item for event in events for item in (None, None, None, event))
    check("T idle dilation preserves the event corpus", tuple(item for item in dilated if item is not None) == events)
    check("T idle dilation changes events per microscopic step", abs(len(events) / len(dilated) - 0.25) < TOL)

    def laplacian_symbol(k: np.ndarray) -> float:
        return float(4.0 * np.sum(np.sin(k / 2.0) ** 2))

    scales = (0.4, 0.2, 0.1, 0.05)
    errors = []
    for scale in scales:
        vector = np.array([scale, 0.7 * scale, -0.2 * scale])
        continuum = float(np.dot(vector, vector))
        errors.append(abs(laplacian_symbol(vector) - continuum) / continuum)
    check("T cubic dispersion converges to the quadratic continuum symbol", all(later < earlier for earlier, later in zip(errors, errors[1:])))
    magnitude = 0.8
    axis = np.array([magnitude, 0.0, 0.0])
    diagonal = np.array([magnitude / math.sqrt(3.0)] * 3)
    check("T finite-lattice equal-norm directions remain anisotropic", abs(laplacian_symbol(axis) - laplacian_symbol(diagonal)) > 1.0e-3)


def matter_interface() -> None:
    section("I - Stable excitation and statistics fork")

    size = 6
    hopping = np.zeros((size, size), dtype=complex)
    for index in range(size):
        hopping[index, (index + 1) % size] = -1.0
        hopping[(index + 1) % size, index] = -1.0
    check("I supplied hopping generator is Hermitian", np.linalg.norm(hopping - hopping.conj().T) < TOL)
    eigenvalues, eigenvectors = np.linalg.eigh(hopping)
    check("I one-particle modes form a complete orthonormal basis", np.linalg.norm(eigenvectors.conj().T @ eigenvectors - np.eye(size)) < TOL)
    check("I the one-particle sector has bounded stable energies", eigenvalues.min() >= -2.0 - TOL and eigenvalues.max() <= 2.0 + TOL)

    # Exact unitary time step from the supplied Hamiltonian.
    phases = np.exp(-1j * 0.37 * eigenvalues)
    unitary = eigenvectors @ np.diag(phases) @ eigenvectors.conj().T
    localized = np.zeros(size, dtype=complex)
    localized[0] = 1.0
    evolved = unitary @ localized
    check("I hopping evolution conserves one-particle norm", abs(np.vdot(evolved, evolved).real - 1.0) < TOL)

    hard_1 = np.kron(SM, I2)
    hard_2 = np.kron(I2, SM)
    car_1 = np.kron(SM, I2)
    car_2 = np.kron(Z, SM)
    check("I distinct hard-core lowering operators commute", np.linalg.norm(hard_1 @ hard_2 - hard_2 @ hard_1) < TOL)
    check("I distinct CAR lowering operators anticommute", np.linalg.norm(car_1 @ car_2 + car_2 @ car_1) < TOL)
    hard_n1, hard_n2 = hard_1.conj().T @ hard_1, hard_2.conj().T @ hard_2
    car_n1, car_n2 = car_1.conj().T @ car_1, car_2.conj().T @ car_2
    check("I hard-core and CAR presentations share local occupation projectors", np.linalg.norm(hard_n1 - car_n1) < TOL and np.linalg.norm(hard_n2 - car_n2) < TOL)
    check("I the exchange algebras nevertheless differ", np.linalg.norm(hard_1 @ hard_2 + hard_2 @ hard_1) > 1.0)

    rng = np.random.default_rng(713)
    raw = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    q, _ = np.linalg.qr(raw)
    observable = np.kron(Z, I2) + 0.3 * np.kron(X, X)
    conjugate = q @ observable @ q.conj().T
    check("I unitary presentation changes preserve spectra", np.linalg.norm(np.sort(np.linalg.eigvalsh(observable)) - np.sort(np.linalg.eigvalsh(conjugate))) < TOL)
    check("I unitary presentation changes preserve trace fingerprints", all(abs(np.trace(np.linalg.matrix_power(observable, power)) - np.trace(np.linalg.matrix_power(conjugate, power))) < TOL for power in range(1, 5)))


def gravity_resource_interface() -> None:
    section("G - Capacity, entropy, source, and lapse forks")

    total_capacity = 10
    free, active, exported = total_capacity, 0, 0
    states = [(free, active, exported)]
    for step in range(8):
        if step % 3 == 2 and active:
            active -= 1
            exported += 1
        else:
            free -= 1
            active += 1
        states.append((free, active, exported))
    check("G declared token accounting is conserved", all(sum(state) == total_capacity for state in states))
    check("G local free capacity can be renewed by export", any(after[1] < before[1] and after[2] > before[2] for before, after in zip(states, states[1:])))

    record_count = 4
    pure = np.array([1.0] + [0.0] * (2**record_count - 1))
    uniform = np.ones(2**record_count) / (2**record_count)

    def shannon(probabilities: np.ndarray) -> float:
        positive = probabilities[probabilities > 0]
        return float(-np.sum(positive * np.log2(positive)))

    check("G equal record length permits different ensemble entropy", abs(shannon(pure)) < TOL and abs(shannon(uniform) - record_count) < TOL)

    archive_history = np.arange(6, dtype=float)
    source_maps = {
        "archive": archive_history,
        "active": np.ones_like(archive_history),
        "none": np.zeros_like(archive_history),
    }
    check("G one archive accepts inequivalent active-source maps", len({tuple(values) for values in source_maps.values()}) == 3)
    clock_events = np.arange(1, 6, dtype=float)
    lapse_a = clock_events * 0.99
    lapse_b_universal = clock_events * 0.99
    lapse_b_nonuniversal = clock_events * 0.97
    check("G universal and species-dependent lapse maps fit the same events", np.allclose(lapse_a, lapse_b_universal) and not np.allclose(lapse_a, lapse_b_nonuniversal))


def boundary_interface() -> None:
    section("B - Boundary and history dependence")

    def append_history(width: int, seed: int | None, initially_full: bool = False) -> list[tuple[int | None, ...]]:
        if initially_full:
            state: list[int | None] = [0] * width
        else:
            state = [None] * width
            if seed is not None:
                state[0] = seed
        history = [tuple(state)]
        while True:
            nxt = list(state)
            for index in range(1, width):
                if state[index] is None and state[index - 1] is not None:
                    nxt[index] = state[index - 1]
            if nxt == state:
                return history
            state = nxt
            history.append(tuple(state))

    zero_history = append_history(7, 0)
    one_history = append_history(7, 1)
    saturated_history = append_history(7, None, initially_full=True)
    check("B one law accepts different seed-conditioned histories", zero_history != one_history and len(zero_history) == len(one_history))
    check("B a low-record boundary permits monotone growth", len(zero_history) == 7)
    check("B a saturated boundary permits no further append history", len(saturated_history) == 1)
    check("B the local rule does not select between its accepted boundaries", zero_history[-1] == (0,) * 7 and one_history[-1] == (1,) * 7)


def classification() -> None:
    section("Z - Interface classification")
    text = NOTE.read_text(encoding="utf-8").lower()
    normalized = " ".join(text.split())
    markers = (
        "not interface-complete",
        "finite conditional witness",
        "no coherent candidate substrate produces all five witnesses",
        "must be derived or be part of the constitution's supplied",
        "none of these results requires new record prose",
        "compute/storage-limited-universe picture",
    )
    for marker in markers:
        check(f"Z note marker: {marker}", marker in normalized)


def main() -> int:
    source_contract()
    operational_interface()
    time_interface()
    matter_interface()
    gravity_resource_interface()
    boundary_interface()
    classification()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: finite interface witnesses; no one-law TOE closure")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
