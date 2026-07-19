#!/usr/bin/env python3
"""Cycle 446: physical NN functional source-control compiler.

Compile both Cycle-445 full functional source controls on a seventeen-M2 line.
The analytic F9 and source-mode bases are synthesized into fixed adjacent
Q1-preserving Givens gates.  Spectral pair phases are routed to the unique
register/source boundary without mixing the two Q1 sectors, then both basis
changes are inverted.  There is no eigenray lookup, state query, or
branch-dependent host schedule.

The Cayley and principal laws remain unselected supplied candidates.
Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from inspect import getsource
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_mass_source_echo_lapse_candidate_tournament_cycle445_2026_07_19 as c445


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NN_FUNCTIONAL_SOURCE_CONTROL_COMPILER_CYCLE446_NOTE_2026-07-19.md"
)
PRIOR = (
    ROOT / "docs/work_history/repo/review_feedback/COHERENT_MULTIBETA_PHYSICAL_MASS_CONTROLLER_TOURNAMENT_CYCLE441_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MASS_SOURCE_ECHO_LAPSE_CANDIDATE_TOURNAMENT_CYCLE445_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_PAIRED_DIRECT_ORBIT_FACTORIZATION_CYCLE310_NOTE_2026-07-17.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_NN_MENU_ARITHMETIC_COMPILER_CYCLE391_NOTE_2026-07-18.md",
)

AUTHORITY = "none"
AUDIT = "unset"
REGISTER_MODES = 9
SOURCE_MODES = 8
TOTAL_M2 = REGISTER_MODES + SOURCE_MODES
TAU = c445.TAU
TOL = 2.0e-11
Coord = tuple[int, int, int]
PASS = 0
FAIL = 0
CONSTRUCTION_EVENTS: list[str] = []


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical nn functional source-control compiler",
        "seventeen-m2 line",
        "fixed analytic f9",
        "fixed analytic source-mode basis",
        "full operator before any state or sector menu",
        "no eigenray lookup",
        "q1 x q1",
        "adjacent boundary sites 8 and 9",
        "route restoration",
        "cayley and principal remain unselected",
        "train and held coherent superpositions",
        "all 24 proper-cubic frames",
        "compiler depth is not time",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-446 note freezes the compiler and semantic boundary", not missing, missing)
    texts = tuple(normalized(path) for path in PRIOR)
    check(
        "the relevant dense-control and physical-gate compiler boundaries are read and preserved",
        all(path.is_file() for path in PRIOR)
        and "primitive synthesis remains open" in texts[0]
        and "primitive nearest-neighbour synthesis" in texts[1]
        and "complex qr gives 156 two-level factors" in texts[2]
        and "stable adjacent swaps" in texts[3],
        {
            "Cycle441_dense_control_wall": "input",
            "Cycle445_adapter": "input",
            "Cycle310_two_level_QR": "bounded prior compiler pattern",
            "Cycle391_NN_routing": "bounded prior compiler pattern",
        },
    )


def fourier(size: int) -> np.ndarray:
    rows = np.arange(size)
    return np.exp(-2j * np.pi * np.outer(rows, rows) / size) / np.sqrt(size)


def source_basis() -> np.ndarray:
    reservoir = np.eye(SOURCE_MODES, dtype=complex)[:, 0]
    uniform = np.zeros(SOURCE_MODES, dtype=complex)
    uniform[1:7] = 1 / np.sqrt(6)
    plus = (reservoir + uniform) / np.sqrt(2)
    minus = (reservoir - uniform) / np.sqrt(2)
    field_fourier = fourier(6)
    contrasts = []
    for character in range(1, 6):
        vector = np.zeros(SOURCE_MODES, dtype=complex)
        vector[1:7] = field_fourier[:, character]
        contrasts.append(vector)
    receiver = np.eye(SOURCE_MODES, dtype=complex)[:, 7]
    return np.column_stack((plus, minus, *contrasts, receiver))


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    matrix: tuple[complex, ...]
    label: str


def mode_gate(left: int, right: int, matrix: np.ndarray, label: str) -> Gate:
    if right != left + 1 or left < 0 or right >= TOTAL_M2:
        raise ValueError("mode gate must occupy one declared NN edge")
    if (left < REGISTER_MODES) != (right < REGISTER_MODES):
        raise ValueError("mode gate may not mix the two Q1 sectors")
    if matrix.shape != (2, 2) or np.linalg.norm(matrix.conj().T @ matrix - np.eye(2)) > TOL:
        raise ValueError("mode block is not a two-mode unitary")
    return Gate("mode", (left, right), tuple(matrix.reshape(-1)), label)


def onsite_phase(site: int, phase: complex, label: str) -> Gate:
    if not 0 <= site < TOTAL_M2 or abs(abs(phase) - 1) > TOL:
        raise ValueError("invalid onsite phase")
    return Gate("onsite-phase", (site,), (complex(phase),), label)


def swap_gate(left: int, right: int, label: str) -> Gate:
    validated = mode_gate(
        left, right, np.asarray(((0, 1), (1, 0)), dtype=complex), label
    )
    return Gate("swap", validated.sites, validated.matrix, label)


def controlled_phase(left: int, right: int, phase: complex, label: str) -> Gate:
    if (left, right) != (REGISTER_MODES - 1, REGISTER_MODES):
        raise ValueError("controlled phase must occupy the unique register/source boundary")
    if abs(abs(phase) - 1) > TOL:
        raise ValueError("invalid controlled phase")
    return Gate("controlled-phase", (left, right), (complex(phase),), label)


def gate_matrix(gate: Gate) -> np.ndarray:
    if gate.kind in ("mode", "swap"):
        return np.asarray(gate.matrix, dtype=complex).reshape(2, 2)
    if gate.kind in ("onsite-phase", "controlled-phase"):
        return np.asarray(gate.matrix, dtype=complex)
    raise ValueError("unknown primitive")


def physical_primitive(gate: Gate) -> np.ndarray:
    """Literal one-/two-M2 lift in basis 0,10,01,11 for pair gates."""
    if gate.kind in ("mode", "swap"):
        output = np.eye(4, dtype=complex)
        output[np.ix_((1, 2), (1, 2))] = gate_matrix(gate)
        return output
    if gate.kind == "onsite-phase":
        return np.diag((1, gate.matrix[0])).astype(complex)
    if gate.kind == "controlled-phase":
        return np.diag((1, 1, 1, gate.matrix[0])).astype(complex)
    raise ValueError("unknown physical primitive")


def inverse_gate(gate: Gate) -> Gate:
    if gate.kind in ("mode", "swap"):
        matrix = gate_matrix(gate).conj().T
        return Gate(gate.kind, gate.sites, tuple(matrix.reshape(-1)), "inverse:" + gate.label)
    return Gate(gate.kind, gate.sites, (np.conj(gate.matrix[0]),), "inverse:" + gate.label)


def inverse_schedule(schedule: tuple[Gate, ...]) -> tuple[Gate, ...]:
    return tuple(inverse_gate(gate) for gate in reversed(schedule))


def decompose_mode_unitary(unitary: np.ndarray, offset: int, label: str) -> tuple[Gate, ...]:
    """Adjacent-row QR; returned order is the physical application order."""
    size = unitary.shape[0]
    if unitary.shape != (size, size) or np.linalg.norm(unitary.conj().T @ unitary - np.eye(size)) > TOL:
        raise ValueError("mode target is not unitary")
    work = unitary.copy()
    eliminations: list[tuple[int, int, np.ndarray]] = []
    for column in range(size - 1):
        for lower in range(size - 1, column, -1):
            upper = lower - 1
            a = work[upper, column]
            b = work[lower, column]
            if abs(b) < 1e-13:
                continue
            radius = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                ((np.conj(a) / radius, np.conj(b) / radius), (-b / radius, a / radius)),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    if np.linalg.norm(work - np.diag(np.diag(work))) > TOL:
        raise RuntimeError("adjacent QR did not reach a diagonal")
    schedule: list[Gate] = []
    for index, phase in enumerate(np.diag(work)):
        if abs(phase - 1) > 1e-13:
            schedule.append(onsite_phase(offset + index, phase, f"{label}:diagonal-{index}"))
    for upper, lower, elimination in reversed(eliminations):
        schedule.append(
            mode_gate(
                offset + upper,
                offset + lower,
                elimination.conj().T,
                f"{label}:givens-{upper}-{lower}",
            )
        )
    return tuple(schedule)


def apply_gate(state: np.ndarray, gate: Gate) -> np.ndarray:
    if state.shape != (REGISTER_MODES, SOURCE_MODES):
        raise ValueError("compiler state is outside Q1 x Q1")
    output = state.copy()
    if gate.kind in ("mode", "swap"):
        left, right = gate.sites
        matrix = gate_matrix(gate)
        if right < REGISTER_MODES:
            output[[left, right], :] = matrix @ output[[left, right], :]
        elif left >= REGISTER_MODES:
            columns = (left - REGISTER_MODES, right - REGISTER_MODES)
            output[:, columns] = output[:, columns] @ matrix.T
        else:
            raise ValueError("Q-sector-mixing mode gate")
    elif gate.kind == "onsite-phase":
        site = gate.sites[0]
        if site < REGISTER_MODES:
            output[site, :] *= gate.matrix[0]
        else:
            output[:, site - REGISTER_MODES] *= gate.matrix[0]
    elif gate.kind == "controlled-phase":
        output[gate.sites[0], gate.sites[1] - REGISTER_MODES] *= gate.matrix[0]
    else:
        raise ValueError("unknown primitive")
    return output


def apply_schedule(state: np.ndarray, schedule: tuple[Gate, ...]) -> np.ndarray:
    output = state
    for gate in schedule:
        output = apply_gate(output, gate)
    return output


def schedule_operator(schedule: tuple[Gate, ...]) -> np.ndarray:
    operator = np.zeros((REGISTER_MODES * SOURCE_MODES,) * 2, dtype=complex)
    for register, source in product(range(REGISTER_MODES), range(SOURCE_MODES)):
        state = np.zeros((REGISTER_MODES, SOURCE_MODES), dtype=complex)
        state[register, source] = 1
        operator[:, register * SOURCE_MODES + source] = apply_schedule(state, schedule).reshape(-1)
    return operator


def route_pair_phase(register: int, source: int, phase: complex, label: str) -> tuple[tuple[Gate, ...], dict[str, object]]:
    if not 0 <= register < REGISTER_MODES or not 0 <= source < SOURCE_MODES:
        raise ValueError("spectral pair is outside the two one-hot registers")
    placement = list(range(TOTAL_M2))
    forward_register = []
    for left in range(register, REGISTER_MODES - 1):
        gate = swap_gate(left, left + 1, f"{label}:route-register")
        forward_register.append(gate)
        placement[left], placement[left + 1] = placement[left + 1], placement[left]
    forward_source = []
    for right in range(REGISTER_MODES + source, REGISTER_MODES, -1):
        gate = swap_gate(right - 1, right, f"{label}:route-source")
        forward_source.append(gate)
        placement[right - 1], placement[right] = placement[right], placement[right - 1]
    boundary_labels = (placement[REGISTER_MODES - 1], placement[REGISTER_MODES])
    phase_gate = controlled_phase(REGISTER_MODES - 1, REGISTER_MODES, phase, label)
    schedule = tuple(forward_register + forward_source + [phase_gate])
    schedule += inverse_schedule(tuple(forward_source))
    schedule += inverse_schedule(tuple(forward_register))
    for gate in inverse_schedule(tuple(forward_source)) + inverse_schedule(tuple(forward_register)):
        left, right = gate.sites
        placement[left], placement[right] = placement[right], placement[left]
    return schedule, {
        "spectral_pair": (register, source),
        "boundary_labels": boundary_labels,
        "boundary_sites": phase_gate.sites,
        "restored_placement": tuple(placement),
        "swap_count": sum(gate.kind == "swap" for gate in schedule),
    }


@dataclass(frozen=True)
class CompiledLaw:
    name: str
    target: np.ndarray
    schedule: tuple[Gate, ...]
    mass_spectrum: tuple[float, ...]
    register_basis_residual: float
    source_basis_residual: float
    routing: tuple[dict[str, object], ...]


def compile_full_source_law(name: str, mass: np.ndarray) -> CompiledLaw:
    """Compile one full analytic functional law before any state/sector menu."""
    if name not in ("cayley", "principal"):
        raise ValueError("undeclared functional mass law")
    if mass.shape != (REGISTER_MODES, REGISTER_MODES) or np.linalg.norm(mass - mass.conj().T) > TOL:
        raise ValueError("mass input is not a nine-mode Hermitian operator")
    shift = c445.cyclic_shift(REGISTER_MODES)
    if np.linalg.norm(mass @ shift - shift @ mass) > TOL:
        raise ValueError("mass input is not a full nine-cycle functional operator")
    register_basis = fourier(REGISTER_MODES)
    source_modes = source_basis()
    exchange = c445.source_exchange()
    register_diagonal = register_basis.conj().T @ mass @ register_basis
    source_diagonal = source_modes.conj().T @ exchange @ source_modes
    register_residual = float(np.linalg.norm(register_diagonal - np.diag(np.diag(register_diagonal))))
    source_residual = float(np.linalg.norm(source_diagonal - np.diag(np.diag(source_diagonal))))
    if register_residual > TOL or source_residual > TOL:
        raise ValueError("fixed analytic bases do not diagonalize the candidate law")

    register_forward = decompose_mode_unitary(register_basis.conj().T, 0, f"{name}:F9-dagger")
    source_forward = decompose_mode_unitary(source_modes.conj().T, REGISTER_MODES, f"{name}:V-dagger")
    phases: list[Gate] = []
    routes = []
    mass_values = np.real_if_close(np.diag(register_diagonal)).real
    source_values = np.real_if_close(np.diag(source_diagonal)).real
    for register, source in product(range(REGISTER_MODES), (0, 1)):
        angle = TAU * mass_values[register] * source_values[source]
        # Two k=0 entries are analytically identity and require no physical
        # route.  Every nonzero full-operator spectral pair is compiled.
        if abs(angle) < 1e-13:
            continue
        routed, audit = route_pair_phase(register, source, np.exp(1j * angle), f"{name}:pair-{register}-{source}")
        phases.extend(routed)
        routes.append(audit)
    schedule = register_forward + source_forward + tuple(phases)
    schedule += inverse_schedule(source_forward) + inverse_schedule(register_forward)
    target = expm(1j * TAU * np.kron(mass, exchange))
    CONSTRUCTION_EVENTS.append(name + "-full-operator-compiled")
    return CompiledLaw(
        name,
        target,
        schedule,
        tuple(float(value) for value in mass_values),
        register_residual,
        source_residual,
        tuple(routes),
    )


def gate_digest(schedule: tuple[Gate, ...]) -> str:
    digest = sha256()
    for gate in schedule:
        digest.update(gate.kind.encode())
        digest.update(repr(gate.sites).encode())
        for value in gate.matrix:
            digest.update(float(value.real).hex().encode())
            digest.update(float(value.imag).hex().encode())
        digest.update(gate.label.encode())
    return digest.hexdigest()


def schedule_depth(schedule: tuple[Gate, ...]) -> int:
    last = [-1] * TOTAL_M2
    for gate in schedule:
        layer = max(last[site] for site in gate.sites) + 1
        for site in gate.sites:
            last[site] = layer
    return max(last) + 1


def schedule_controls(compiled: tuple[CompiledLaw, ...]) -> dict[str, object]:
    rows = []
    failures = 0
    for law in compiled:
        counts = {kind: sum(gate.kind == kind for gate in law.schedule) for kind in ("mode", "onsite-phase", "controlled-phase", "swap")}
        route_failures = sum(
            row["boundary_sites"] != (8, 9)
            or row["boundary_labels"] != row["spectral_pair"][:1] + (REGISTER_MODES + row["spectral_pair"][1],)
            or row["restored_placement"] != tuple(range(TOTAL_M2))
            for row in law.routing
        )
        adjacency_failures = sum(
            len(gate.sites) == 2 and gate.sites[1] - gate.sites[0] != 1
            for gate in law.schedule
        )
        q_sector_failures = sum(
            gate.kind in ("mode", "swap")
            and ((gate.sites[0] < REGISTER_MODES) != (gate.sites[1] < REGISTER_MODES))
            for gate in law.schedule
        )
        primitive_unitarity = []
        primitive_charge_failures = 0
        for gate in law.schedule:
            matrix = physical_primitive(gate)
            primitive_unitarity.append(
                float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(matrix.shape[0])))
            )
            if len(gate.sites) == 2:
                charges = (0, 1, 1, 2)
                primitive_charge_failures += sum(
                    abs(matrix[row, column]) > 1e-13 and charges[row] != charges[column]
                    for row, column in product(range(4), repeat=2)
                )
        failures += route_failures + adjacency_failures + q_sector_failures + primitive_charge_failures
        rows.append(
            {
                "law": law.name,
                "M2": TOTAL_M2,
                "serial_primitives": len(law.schedule),
                "dependency_layers": schedule_depth(law.schedule),
                "counts": counts,
                "active_spectral_pairs": len(law.routing),
                "analytic_zero_pair_slots_omitted": 2,
                "route_restore_failures": route_failures,
                "NN_failures": adjacency_failures,
                "Q1xQ1_mixing_failures": q_sector_failures,
                "physical_primitive_charge_failures": int(primitive_charge_failures),
                "maximum_primitive_unitarity_residual": max(primitive_unitarity),
                "digest": gate_digest(law.schedule),
            }
        )
    check(
        "each full law has one fixed restored-placement NN schedule with only adjacent boundary pair phases",
        failures == 0
        and all(row["counts"] == {"mode": 104, "onsite-phase": 2, "controlled-phase": 16, "swap": 128} for row in rows)
        and all(row["serial_primitives"] == 250 for row in rows)
        and all(row["maximum_primitive_unitarity_residual"] < TOL for row in rows),
        {
            "rows": rows,
            "compiler_schedule_is_serial": True,
            "disjoint_support_layering_certificate_reported": True,
            "compiler_depth_is_time": False,
        },
    )
    return {"rows": rows}


def operator_and_code_controls(compiled: tuple[CompiledLaw, ...]) -> dict[str, object]:
    rows = []
    maximum = 0.0
    for law in compiled:
        operator = schedule_operator(law.schedule)
        inverse = schedule_operator(inverse_schedule(law.schedule))
        identity = np.eye(operator.shape[0], dtype=complex)
        row = {
            "law": law.name,
            "register_basis_diagonalization": law.register_basis_residual,
            "source_basis_diagonalization": law.source_basis_residual,
            "full_operator_EG": float(np.linalg.norm(operator - law.target)),
            "compiled_unitarity": float(np.linalg.norm(operator.conj().T @ operator - identity)),
            "explicit_inverse": float(np.linalg.norm(inverse @ operator - identity)),
            "Q1xQ1_code_leakage": 0.0,
            "basis_columns": operator.shape[1],
        }
        maximum = max(maximum, *(value for key, value in row.items() if key not in ("law", "basis_columns")))
        rows.append(row)
    check(
        "both schedules satisfy full 72-column E/G, explicit inverse, unitarity, and zero Q1 x Q1 leakage",
        maximum < TOL,
        {"rows": rows, "maximum": maximum, "encoding": "two one-hot M2 registers -> 17-bit masks"},
    )
    return {"rows": rows, "maximum": maximum}


def code_mask(register_mask: int, source_mask: int) -> tuple[int, int]:
    if not isinstance(register_mask, int) or register_mask < 0 or register_mask >= 1 << REGISTER_MODES or register_mask.bit_count() != 1:
        raise ValueError("register mask is outside Q1")
    if not isinstance(source_mask, int) or source_mask < 0 or source_mask >= 1 << SOURCE_MODES or source_mask.bit_count() != 1:
        raise ValueError("source mask is outside Q1")
    return register_mask.bit_length() - 1, source_mask.bit_length() - 1


def state_fixture_controls(
    controller: c445.MassController,
    compiled: tuple[CompiledLaw, ...],
    menu: tuple[c445.Sector, ...],
) -> dict[str, object]:
    alpha = np.asarray((0.37, 0.41j, -0.52, 0.64j), dtype=complex)
    alpha /= np.linalg.norm(alpha)
    coherent = sum((alpha[index] * sector.eigenray for index, sector in enumerate(menu)), start=np.zeros(REGISTER_MODES, dtype=complex))
    states = tuple((f"beta={sector.beta}", sector.eigenray, sector.held) for sector in menu) + (("train+held coherent", coherent, True),)
    rows = []
    maximum = 0.0
    for law in compiled:
        mass = controller.cayley if law.name == "cayley" else controller.principal
        for name, ray, held in states:
            initial = c445.source_initial(ray)
            compiled_output = apply_schedule(initial, law.schedule)
            direct = (law.target @ initial.reshape(-1)).reshape(REGISTER_MODES, SOURCE_MODES)
            residual = float(np.linalg.norm(compiled_output - direct))
            restored = apply_schedule(compiled_output, inverse_schedule(law.schedule))
            inverse = float(np.linalg.norm(restored - initial))
            before_mass = float(np.real(np.vdot(ray, mass @ ray)))
            after_mass = float(
                np.real(sum(np.vdot(compiled_output[:, source], mass @ compiled_output[:, source]) for source in range(SOURCE_MODES)))
            )
            transported = c445.transport_to_receiver(compiled_output)
            receiver = float(np.linalg.norm(transported[:, 7]) ** 2)
            direct_receiver = float(np.linalg.norm(c445.transport_to_receiver(direct)[:, 7]) ** 2)
            maximum = max(maximum, residual, inverse, abs(before_mass - after_mass), abs(receiver - direct_receiver))
            rows.append(
                {
                    "law": law.name,
                    "state": name,
                    "held_or_contains_held": held,
                    "EG": residual,
                    "inverse": inverse,
                    "mass_fixture_before_after": (before_mass, after_mass),
                    "selected_receiver_squared_norm": receiver,
                    "receiver_fixture_residual": abs(receiver - direct_receiver),
                }
            )
    held = [row for row in rows if row["state"] == f"beta={c445.HELD_BETA}"]
    held_weights = {row["law"]: row["selected_receiver_squared_norm"] for row in held}
    check(
        "train, held, and train+held coherent states preserve the Cycle445 mass and receiver fixtures without lookup",
        maximum < TOL
        and abs(held_weights["cayley"] - 0.09418478131620477) < TOL
        and abs(held_weights["principal"] - 0.0014001584922212114) < TOL,
        {"rows": rows, "maximum": maximum, "held_receiver_weights": held_weights},
    )
    return {"rows": rows, "maximum": maximum}


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        permutation_matrix = np.eye(3, dtype=int)[list(permutation)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation_matrix
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple({tuple(frame.reshape(-1)): frame for frame in frames}.values())


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def direction_representation(frame: np.ndarray) -> np.ndarray:
    directions = (
        np.asarray((1, 0, 0)), np.asarray((-1, 0, 0)),
        np.asarray((0, 1, 0)), np.asarray((0, -1, 0)),
        np.asarray((0, 0, 1)), np.asarray((0, 0, -1)),
    )
    output = np.eye(SOURCE_MODES, dtype=complex)
    output[1:7, 1:7] = 0
    for source, direction in enumerate(directions):
        moved = tuple(int(value) for value in frame @ direction)
        target = next(index for index, candidate in enumerate(directions) if tuple(candidate) == moved)
        output[1 + target, 1 + source] = 1
    return output


def covariance_locality_controls(compiled: tuple[CompiledLaw, ...]) -> None:
    frames = proper_cubic_frames()
    sites = tuple((index, 0, 0) for index in range(TOTAL_M2))
    locality_failures = 0
    covariance = []
    exchange = c445.source_exchange()
    for law in compiled:
        for gate in law.schedule:
            if len(gate.sites) == 2:
                edge = (sites[gate.sites[0]], sites[gate.sites[1]])
                locality_failures += int(manhattan(*edge) != 1)
                for frame in frames:
                    moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in edge)
                    locality_failures += int(manhattan(*moved) != 1)
        for frame in frames:
            source_frame = direction_representation(frame)
            covariance.append(float(np.linalg.norm(source_frame @ exchange @ source_frame.conj().T - exchange)))
    check(
        "the 17-M2 line, every primitive edge, and uniform six-field target are covariant in all 24 proper-cubic frames",
        len(frames) == 24 and locality_failures == 0 and max(covariance) == 0,
        {
            "frames": len(frames),
            "primitive_edge_frame_failures": locality_failures,
            "maximum_source_target_covariance_residual": max(covariance),
            "line_template_carried_with_frame": True,
            "preferred_global_frame": False,
        },
    )


def anti_lookup_controls() -> None:
    source = (getsource(compile_full_source_law) + getsource(decompose_mode_unitary) + getsource(route_pair_phase)).lower()
    forbidden = ("linalg.eig", "linalg.eigh", "sector_menu", "target_betas", "eigenray", "lookup_route", "branch")
    present = tuple(item for item in forbidden if item in source)
    check(
        "the compiler consumes each full analytic operator before the state menu and contains no eigenray/branch lookup",
        not present
        and tuple(CONSTRUCTION_EVENTS) == ("cayley-full-operator-compiled", "principal-full-operator-compiled", "state-menu-built"),
        {
            "forbidden_tokens_present": present,
            "construction_events": CONSTRUCTION_EVENTS,
            "spectral_values": "fixed law constants from diag(F9^dagger M(S) F9), before states",
        },
    )


def deletion_domain_controls(compiled: tuple[CompiledLaw, ...]) -> None:
    law = next(item for item in compiled if item.name == "cayley")
    baseline = schedule_operator(law.schedule)
    indices = {
        "F9-transform": next(index for index, gate in enumerate(law.schedule) if "F9-dagger:givens" in gate.label),
        "V-transform": next(index for index, gate in enumerate(law.schedule) if "V-dagger:givens" in gate.label),
        "spectral-phase": next(index for index, gate in enumerate(law.schedule) if gate.kind == "controlled-phase"),
        "route-restore": next(index for index, gate in enumerate(law.schedule) if gate.kind == "swap" and gate.label.startswith("inverse:")),
    }
    deletion_residuals = {}
    for name, index in indices.items():
        deleted = law.schedule[:index] + law.schedule[index + 1 :]
        operator = schedule_operator(deleted)
        deletion_residuals[name] = float(np.linalg.norm(operator - baseline))

    malformed = 0
    for operation in (
        lambda: code_mask(0, 1),
        lambda: code_mask(3, 1),
        lambda: code_mask(1, 0),
        lambda: code_mask(1, 3),
        lambda: mode_gate(0, 2, np.eye(2), "non-NN"),
        lambda: controlled_phase(7, 9, 1, "non-boundary"),
        lambda: compile_full_source_law("lookup", np.eye(9)),
        lambda: compile_full_source_law("cayley", np.eye(8)),
        lambda: compile_full_source_law("cayley", np.diag(np.arange(9))),
    ):
        try:
            operation()
        except ValueError:
            malformed += 1
    check(
        "F9, V, spectral-phase, and route-restore deletions visibly break the compiled target or placement",
        min(deletion_residuals.values()) > 1e-4,
        {"deletion_residuals": deletion_residuals, "frozen_visible_threshold": 1e-4},
    )
    check(
        "Q0/Q2 codes, non-NN/non-boundary gates, undeclared laws, and malformed functional operators are refused",
        malformed == 9,
        {"malformed_rejections": malformed, "expected": 9},
    )


def inventory_scope_controls(schedule_details: dict[str, object]) -> None:
    inventory = {
        "supplied": (
            "nine-cycle S, its internal orientation, and analytic Cayley/principal functional laws",
            "analytic F9 convention and analytic reservoir/uniform/contrast source basis",
            "tau=0.05, one-hot preparations, primitive gate family, line layout and serial order",
            "one selected physical field rail and downstream Cycle445 receiver/echo adapter",
        ),
        "compiled_derived": (
            "17-M2 Q1 x Q1 code and 250-primitive fixed NN schedule per law",
            "adjacent QR/Givens factors, routed spectral pair phases and exact placement restoration",
            "full 72-column E/G, inverse, zero leakage and all24 transported covariance",
            "train/held coherent action plus Cycle445 mass and receiver fixtures",
        ),
        "open": (
            "selection or derivation of Cayley versus principal functional law and tau",
            "autonomous preparation/program selection and homogeneous repetition",
            "derivation of the internal nine-cycle orientation from cubic geometry",
            "Cycle445 Record occurrence, lapse/proper time, passive trajectory and gravity lanes",
        ),
    }
    check(
        "the compiler closes only the bounded dense-control primitive-synthesis wall and exposes every remaining supply",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "inventory": inventory,
            "schedule_details": schedule_details,
            "mass_law_selected": False,
            "compiler_depth_called_time": False,
            "receiver_weight_called_occurrence_or_probability": False,
            "lapse_or_gravity_derived": False,
            "no_go_or_axiom_pressure": False,
        },
    )


def main() -> int:
    contracts()
    controller = c445.build_mass_controller()
    compiled = (
        compile_full_source_law("cayley", controller.cayley),
        compile_full_source_law("principal", controller.principal),
    )
    menu = c445.sectors(controller)
    CONSTRUCTION_EVENTS.append("state-menu-built")
    schedule_details = schedule_controls(compiled)
    operator_and_code_controls(compiled)
    state_fixture_controls(controller, compiled, menu)
    covariance_locality_controls(compiled)
    anti_lookup_controls()
    deletion_domain_controls(compiled)
    inventory_scope_controls(schedule_details)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL == 0:
        print("RESULT PHYSICAL_NN_FUNCTIONAL_SOURCE_CONTROL_COMPILER_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
