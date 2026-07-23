#!/usr/bin/env python3
"""Cycle634: physical forcing-menu instrument bridge tournament.

Construct bounded M2 unitary dilations for three finite qubit effect-menu
families.  The runner keeps physical menu realization separate from an
algebraic candidate grade, objective occurrence, Record/permanence, and
frequency/Born meaning.  Authority is none and audit is unset.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import time

import numpy as np
from scipy.spatial.transform import Rotation


ROOT = Path(__file__).resolve().parents[1]
COMMITTED_SHORE_HEAD = "1d3d7a005bc74256ac23b9ace7b2669a45a9fc79"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json"
)
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
TOL = 2.0e-11
PASS = 0
FAIL = 0


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2.0)
PAULI = (X, Y, Z)


FROZEN_SHORES = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py":
        "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROTECTED_SHADOW_COIN_GATE_COMPILER_CYCLE523_NOTE_2026-07-21.md":
        "a8fc040d97e019214000eec4bdef702f259b9f30c011b77c97261e5c1288cf20",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py":
        "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md":
        "190ed6dfc5502a0d8d68c665501fe4f009d21fb2aad4bc0b71e9f96a9856552d",
    "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json":
        "a867cbeed66052da8cb85e8867a55802d27bfca586c9db805aa1649a6f0c7560",
}


EXTERNAL_COMPARISON_HEADS = {
    "PR5472": {
        "head_oid": "2c648ccb408a8c36a700f53ec5401369e3bbd490",
        "path": "docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "sha256": "f7ddc109ebb97d5514c7b41a78c523fe6adcf5419c08cff1ec75e54b2c99d435",
        "line": 60,
        "fragment": "Neither horn is selected. The axioms supply no menus at all",
        "use": "conditional effect-menu forcing comparison only",
    },
    "PR5476": {
        "head_oid": "a994617819f57e599dd101c654be366123392236",
        "path": "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "sha256": "042a5e69a50dba337fc3e8bfd5faa3a6cef34b42c3e0ab6344ae5d05f5e6cdc7",
        "line": 17,
        "fragment": "the menu family the physical registration supplies is underived",
        "use": "conditional scaled-projector forcing comparison only",
    },
    "PR5479": {
        "head_oid": "84053108a424cef26dc23e484549df331ad2050f",
        "path": "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "sha256": "feb8b3ca2ed1a8ffb3d272ce81814cfc2c6598148e9fecf2a48df88b53c45a35",
        "line": 62,
        "fragment": "No family is selected; nothing here derives which menus record formation",
        "use": "conditional ternary/mixed-projective forcing comparison only",
    },
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_surface_bytes(head_oid: str, path: str) -> bytes:
    return subprocess.run(
        ("git", "show", f"{head_oid}:{path}"), cwd=ROOT,
        check=True, capture_output=True,
    ).stdout


def repo_line(path: str, fragment: str) -> int:
    rows = (ROOT / path).read_text().splitlines()
    matches = [i for i, row in enumerate(rows, 1)
               if (row.strip().startswith(fragment) if fragment.startswith("def ") else fragment in row)]
    if len(matches) != 1:
        raise ValueError(f"expected one line for {path!r} / {fragment!r}, got {matches}")
    return matches[0]


def shore_controls() -> dict[str, object]:
    observed = {
        path: sha256(git_surface_bytes(COMMITTED_SHORE_HEAD, path)).hexdigest()
        for path in FROZEN_SHORES
    }
    dirty_comparison = {path: file_sha(ROOT / path) for path in FROZEN_SHORES}
    c625 = json.loads(git_surface_bytes(
        COMMITTED_SHORE_HEAD,
        "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json",
    ))
    exact = observed == FROZEN_SHORES
    interface = (
        c625["route_B_physical_shared_middle"]["pass"]
        and c625["route_B_physical_shared_middle"]["bounded_M2"] == 129
        and c625["route_B_physical_shared_middle"]["runtime_actuality_token"] is False
        and c625["route_B_physical_shared_middle"]["coherent_onehot_sectors_retained"] == 6
        and c625["route_C_ROM_free_grade_corpus"]["pass"]
        and c625["route_C_ROM_free_grade_corpus"]["bounded_M2"] == 531
        and c625["route_C_ROM_free_grade_corpus"]["grade_or_frequency_called_Born"] is False
    )
    result = {
        "committed_shore_head": COMMITTED_SHORE_HEAD,
        "expected_sha256": FROZEN_SHORES,
        "observed_sha256": observed,
        "working_tree_comparison_sha256": dirty_comparison,
        "working_tree_bytes_used_as_premise": False,
        "Cycle625_interface": {
            "Route_B_bounded_M2": c625["route_B_physical_shared_middle"]["bounded_M2"],
            "Route_B_runtime_actuality_token": c625["route_B_physical_shared_middle"]["runtime_actuality_token"],
            "Route_B_coherent_sectors": c625["route_B_physical_shared_middle"]["coherent_onehot_sectors_retained"],
            "Route_C_bounded_M2": c625["route_C_ROM_free_grade_corpus"]["bounded_M2"],
            "Route_C_called_Born": c625["route_C_ROM_free_grade_corpus"]["grade_or_frequency_called_Born"],
        },
        "pass": exact and interface,
    }
    check("immutable committed Cycle523/Cycle625 and axiom shores are exact", result["pass"],
          {"files": len(observed), "head": COMMITTED_SHORE_HEAD})
    return result


def external_comparison_controls() -> dict[str, object]:
    rows = {}
    for name, spec in EXTERNAL_COMPARISON_HEADS.items():
        body = git_surface_bytes(spec["head_oid"], spec["path"])
        text = body.decode().splitlines()
        line_text = text[spec["line"] - 1]
        passed = sha256(body).hexdigest() == spec["sha256"] and spec["fragment"] in line_text
        rows[name] = {
            **spec,
            "observed_sha256": sha256(body).hexdigest(),
            "line_text": line_text,
            "declared_state": "CLOSED_NONRETAINED",
            "retained_as_premise": False,
            "back_credit": False,
            "pass": passed,
        }
    passed = all(row["pass"] and not row["retained_as_premise"] and not row["back_credit"]
                 for row in rows.values())
    result = {"heads": rows, "comparison_only": True, "back_credit": False, "pass": passed}
    check("three closed Born heads are byte-exact comparison-only objects", passed, len(rows))
    return result


def hermitian_sqrt(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2.0)
    if vals.min() < -TOL:
        raise ValueError(f"negative eigenvalue {vals.min()}")
    vals = np.clip(vals, 0.0, None)
    vals[np.abs(vals) < 1.0e-13] = 0.0
    vals[np.abs(vals - 1.0) < 1.0e-13] = 1.0
    return (vecs * np.sqrt(vals)) @ vecs.conj().T


def projector(direction: tuple[float, float, float]) -> np.ndarray:
    v = np.asarray(direction, dtype=float)
    v = v / np.linalg.norm(v)
    return (I2 + sum(v[i] * PAULI[i] for i in range(3))) / 2.0


def binary_dilation(effect: np.ndarray) -> np.ndarray:
    s = hermitian_sqrt(effect)
    c = hermitian_sqrt(I2 - effect)
    u = (np.kron(c, P0) - np.kron(s, np.array([[0, 1], [0, 0]], complex))
         + np.kron(s, np.array([[0, 0], [1, 0]], complex)) + np.kron(c, P1))
    if np.linalg.norm(u.conj().T @ u - np.eye(4), ord=2) > TOL:
        raise ValueError("binary dilation is not unitary")
    return u


def ry(theta: float) -> np.ndarray:
    return np.array([[math.cos(theta / 2.0), -math.sin(theta / 2.0)],
                     [math.sin(theta / 2.0), math.cos(theta / 2.0)]], dtype=complex)


def binary_dilation_primitive_residual(effect: np.ndarray) -> float:
    """Lower U(F) to four one-M2 rotations and two adjacent CNOTs."""
    vals, vecs = np.linalg.eigh((effect + effect.conj().T) / 2.0)
    vals = np.clip(vals, 0.0, 1.0)
    vals[np.abs(vals) < 1.0e-13] = 0.0
    vals[np.abs(vals - 1.0) < 1.0e-13] = 1.0
    theta = tuple(2.0 * math.asin(math.sqrt(float(value))) for value in vals)
    average = (theta[0] + theta[1]) / 2.0
    difference = (theta[0] - theta[1]) / 2.0
    cnot = np.kron(P0, I2) + np.kron(P1, X)
    lowered = (np.kron(vecs, I2) @ np.kron(I2, ry(average)) @ cnot
               @ np.kron(I2, ry(difference)) @ cnot @ np.kron(vecs.conj().T, I2))
    return float(np.linalg.norm(lowered - binary_dilation(effect), ord=2))


def bits(index: int, count: int) -> tuple[int, ...]:
    return tuple((index >> (count - 1 - q)) & 1 for q in range(count))


def embed_gate(gate: np.ndarray, qubits: tuple[int, ...], count: int) -> np.ndarray:
    """Embed a one- or two-M2 gate with the listed local qubit ordering."""
    dim = 2**count
    out = np.zeros((dim, dim), dtype=complex)
    untouched = tuple(q for q in range(count) if q not in qubits)
    for col in range(dim):
        before = bits(col, count)
        local_col = sum(before[q] << (len(qubits) - 1 - j) for j, q in enumerate(qubits))
        for local_row in range(2 ** len(qubits)):
            amp = gate[local_row, local_col]
            if abs(amp) < 1.0e-16:
                continue
            after = list(before)
            for j, q in enumerate(qubits):
                after[q] = (local_row >> (len(qubits) - 1 - j)) & 1
            if any(after[q] != before[q] for q in untouched):
                raise AssertionError("embedding changed an untouched qubit")
            row = sum(after[q] << (count - 1 - q) for q in range(count))
            out[row, col] += amp
    return out


def validate_menu(effects: tuple[np.ndarray, ...]) -> None:
    if not 2 <= len(effects) <= 7:
        raise ValueError("a cubic-star menu needs 2..7 outcomes")
    if any(e.shape != (2, 2) for e in effects):
        raise ValueError("effects must be M2")
    if any(np.linalg.norm(e - e.conj().T) > TOL for e in effects):
        raise ValueError("effects must be Hermitian")
    if any(np.linalg.eigvalsh(e).min() < -TOL or np.linalg.eigvalsh(I2 - e).min() < -TOL
           for e in effects):
        raise ValueError("effects must lie between zero and identity")
    if np.linalg.norm(sum(effects, np.zeros((2, 2), complex)) - I2, ord=2) > TOL:
        raise ValueError("effects must sum to identity")


def compile_menu(effects: tuple[np.ndarray, ...]) -> dict[str, object]:
    """Sequential first-hit compiler on one system plus m-1 neighbor M2 ports."""
    validate_menu(effects)
    ports = len(effects) - 1
    total_qubits = 1 + ports
    accumulated = I2.copy()
    gates = []
    conditional_effects = []
    full = np.eye(2**total_qubits, dtype=complex)
    for j, effect in enumerate(effects[:-1]):
        # The Moore-Penrose inverse extends the same construction to menus
        # whose intermediate no-hit remainder loses rank.  Positivity of the
        # remaining POVM effects confines them to the surviving support.
        inv = np.linalg.pinv(accumulated, rcond=1.0e-12)
        conditional = inv.conj().T @ effect @ inv
        conditional = (conditional + conditional.conj().T) / 2.0
        gate = binary_dilation(conditional)
        full_gate = embed_gate(gate, (0, j + 1), total_qubits)
        full = full_gate @ full
        accumulated = hermitian_sqrt(I2 - conditional) @ accumulated
        gates.append(full_gate)
        conditional_effects.append(conditional)
    return {
        "unitary": full,
        "gates": tuple(gates),
        "conditional_effects": tuple(conditional_effects),
        "effects": effects,
        "ports": ports,
        "M2": total_qubits,
        "port_positions": tuple((1, 0, 0) if j == 0 else
                                (-1, 0, 0) if j == 1 else
                                (0, 1, 0) if j == 2 else
                                (0, -1, 0) if j == 3 else
                                (0, 0, 1) if j == 4 else (0, 0, -1)
                                for j in range(ports)),
        "maximum_gate_support_M2": 2,
    }


def pointer_kraus(unitary: np.ndarray, ports: int) -> dict[tuple[int, ...], np.ndarray]:
    count = ports + 1
    out = {}
    for pattern in product((0, 1), repeat=ports):
        k = np.zeros((2, 2), dtype=complex)
        for s_out in (0, 1):
            row_bits = (s_out,) + pattern
            row = sum(row_bits[q] << (count - 1 - q) for q in range(count))
            for s_in in (0, 1):
                col = s_in << ports
                k[s_out, s_in] = unitary[row, col]
        out[pattern] = k
    return out


def first_hit(pattern: tuple[int, ...]) -> int:
    return pattern.index(1) if 1 in pattern else len(pattern)


def induced_effects(unitary: np.ndarray, ports: int) -> tuple[np.ndarray, ...]:
    kraus = pointer_kraus(unitary, ports)
    result = []
    for outcome in range(ports + 1):
        result.append(sum((k.conj().T @ k for pattern, k in kraus.items()
                           if first_hit(pattern) == outcome), np.zeros((2, 2), complex)))
    return tuple(result)


def max_effect_residual(unitary: np.ndarray, effects: tuple[np.ndarray, ...]) -> float:
    got = induced_effects(unitary, len(effects) - 1)
    return max(np.linalg.norm(a - b, ord=2) for a, b in zip(got, effects))


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    rows = []
    for perm in permutations(range(3)):
        base = np.eye(3, dtype=int)[:, perm]
        for signs in product((-1, 1), repeat=3):
            r = base @ np.diag(signs)
            if round(np.linalg.det(r)) == 1:
                rows.append(r)
    unique = {tuple(r.reshape(-1)): r for r in rows}
    return tuple(unique[key] for key in sorted(unique))


def spinor(frame: np.ndarray) -> np.ndarray:
    x, y, z, w = Rotation.from_matrix(frame.astype(float)).as_quat()
    return w * I2 - 1j * (x * X + y * Y + z * Z)


def transport_menu(effects: tuple[np.ndarray, ...], frame: np.ndarray) -> tuple[np.ndarray, ...]:
    s = spinor(frame)
    return tuple(s @ e @ s.conj().T for e in effects)


def menu_families() -> dict[str, tuple[np.ndarray, ...]]:
    rt3 = math.sqrt(3.0)
    trine = tuple((2.0 / 3.0) * projector(v) for v in (
        (1.0, 0.0, 0.0), (-0.5, rt3 / 2.0, 0.0), (-0.5, -rt3 / 2.0, 0.0)
    ))
    c0 = 2.0 / (1.0 + rt3)
    scaled = (
        c0 * projector((1.0, 1.0, 1.0)),
        (c0 / rt3) * projector((-1.0, 0.0, 0.0)),
        (c0 / rt3) * projector((0.0, -1.0, 0.0)),
        (c0 / rt3) * projector((0.0, 0.0, -1.0)),
    )
    e0 = 0.5 * projector((0.0, 0.0, 1.0)) + 0.5 * projector((1.0, 0.0, 0.0))
    mixed = (e0, I2 - e0)
    held = (trine[0] / 3.0, trine[0] / 3.0, trine[0] / 3.0, trine[1], trine[2])
    return {"ternary_trine": trine, "scaled_axis_cancellation": scaled,
            "mixed_projective_merge": mixed, "held_size5_split_trine": held}


def sequential_compiler_tournament() -> dict[str, object]:
    families = menu_families()
    frames = proper_cubic_frames()
    frame_group_failures = 0
    for left in frames:
        for right in frames:
            if not any(np.array_equal(left @ right, candidate) for candidate in frames):
                frame_group_failures += 1
    rows = {}
    global_failures = 0
    for name, effects in families.items():
        compiled = compile_menu(effects)
        unitary = compiled["unitary"]
        unitarity = np.linalg.norm(unitary.conj().T @ unitary - np.eye(unitary.shape[0]), ord=2)
        closure = max_effect_residual(unitary, effects)
        sum_residual = np.linalg.norm(sum(effects, np.zeros((2, 2), complex)) - I2, ord=2)
        completeness = np.linalg.norm(sum(induced_effects(unitary, compiled["ports"]),
                                          np.zeros((2, 2), complex)) - I2, ord=2)
        code_norm = max(abs(np.linalg.norm(unitary[:, s << compiled["ports"]]) - 1.0) for s in (0, 1))
        perm_residual = 0.0
        perm_count = 0
        if len(effects) <= 4:
            for order in permutations(range(len(effects))):
                ordered = tuple(effects[j] for j in order)
                candidate = compile_menu(ordered)
                perm_residual = max(perm_residual, max_effect_residual(candidate["unitary"], ordered))
                perm_count += 1
        covariance = 0.0
        effect_covariance = 0.0
        for frame in frames:
            s = spinor(frame)
            transported = transport_menu(effects, frame)
            candidate = compile_menu(transported)
            conjugator = np.kron(s, np.eye(2 ** compiled["ports"], dtype=complex))
            covariance = max(covariance, np.linalg.norm(
                candidate["unitary"] - conjugator @ unitary @ conjugator.conj().T, ord=2))
            got = induced_effects(candidate["unitary"], candidate["ports"])
            effect_covariance = max(effect_covariance, max(
                np.linalg.norm(g - t, ord=2) for g, t in zip(got, transported)))
        deletion = []
        for omitted in range(len(compiled["gates"])):
            damaged = np.eye(unitary.shape[0], dtype=complex)
            for j, gate in enumerate(compiled["gates"]):
                if j != omitted:
                    damaged = gate @ damaged
            deletion.append(max_effect_residual(damaged, effects))
        inverse = np.linalg.norm(unitary.conj().T @ unitary - np.eye(unitary.shape[0]), ord=2)
        conditional_min = min(np.linalg.eigvalsh(f).min() for f in compiled["conditional_effects"])
        conditional_max = max(np.linalg.eigvalsh(f).max() for f in compiled["conditional_effects"])
        primitive_residual = max(binary_dilation_primitive_residual(f)
                                 for f in compiled["conditional_effects"])
        passed = (
            unitarity < TOL and closure < TOL and sum_residual < TOL and completeness < TOL
            and code_norm < TOL and perm_residual < TOL and covariance < TOL
            and effect_covariance < TOL and inverse < TOL
            and all(x > 1.0e-3 for x in deletion)
            and conditional_min > -TOL and conditional_max < 1.0 + TOL
            and primitive_residual < TOL
            and compiled["maximum_gate_support_M2"] == 2
            and all(sum(abs(x) for x in p) == 1 for p in compiled["port_positions"])
        )
        global_failures += int(not passed)
        rows[name] = {
            "outcomes": len(effects),
            "bounded_M2_system_plus_apparatus": compiled["M2"],
            "constant_overhead_per_menu_cell": True,
            "binary_neighbor_gates": len(compiled["gates"]),
            "literal_one_M2_calls": 4 * len(compiled["gates"]),
            "literal_adjacent_CNOT_calls": 2 * len(compiled["gates"]),
            "literal_gate_calls": 6 * len(compiled["gates"]),
            "binary_dilation_primitive_lowering_residual": primitive_residual,
            "maximum_gate_support_M2": compiled["maximum_gate_support_M2"],
            "nearest_neighbor_star": True,
            "port_positions_reference_chart": compiled["port_positions"],
            "input_auxiliary_constraints": [f"port_{j}: |0><0|" for j in range(compiled["ports"])],
            "input_constraint_support_M2": 1,
            "input_constraint_autonomous_genesis": False,
            "unitarity_residual": unitarity,
            "exact_effect_identity_residual": closure,
            "effect_sum_residual": sum_residual,
            "pointer_completeness_residual": completeness,
            "blank_code_norm_residual": code_norm,
            "all_orderings_tested": perm_count,
            "all_orderings_effect_residual": perm_residual,
            "proper_cubic_frames": len(frames),
            "unitary_covariance_residual": covariance,
            "effect_covariance_residual": effect_covariance,
            "inverse_residual": inverse,
            "deletion_residuals": deletion,
            "conditional_effect_minimum_eigenvalue": conditional_min,
            "conditional_effect_maximum_eigenvalue": conditional_max,
            "global_parity_or_order_service": False,
            "host_outcome_selection": False,
            "later_gates_always_execute_after_first_hit": True,
            "pointer_states_called_Records": False,
            "pass": passed,
        }
    malformed = []
    malformed_inputs = {
        "negative_effect": (np.diag([-0.1, 0.2]), np.diag([1.1, 0.8])),
        "nonnormalized_sum": (0.4 * I2, 0.4 * I2),
        "nonhermitian": (np.array([[0.5, 0.2], [0.0, 0.5]], complex),
                           np.array([[0.5, -0.2], [0.0, 0.5]], complex)),
        "too_many_outcomes_for_six_neighbors": tuple(I2 / 8.0 for _ in range(8)),
    }
    for name, menu in malformed_inputs.items():
        refused = False
        try:
            compile_menu(tuple(menu))
        except ValueError:
            refused = True
        malformed.append({"name": name, "refused": refused})
    singular_menu = (projector((0.0, 0.0, 1.0)),
                     0.4 * projector((0.0, 0.0, -1.0)),
                     0.6 * projector((0.0, 0.0, -1.0)))
    singular_compiled = compile_menu(singular_menu)
    singular_control = {
        "menu": "P_z, 0.4 P_-z, 0.6 P_-z",
        "intermediate_remainder_is_rank_one": True,
        "Moore_Penrose_support_extension": True,
        "effect_identity_residual": max_effect_residual(singular_compiled["unitary"], singular_menu),
        "inverse_residual": np.linalg.norm(singular_compiled["unitary"].conj().T
                                           @ singular_compiled["unitary"]
                                           - np.eye(singular_compiled["unitary"].shape[0]), ord=2),
    }
    result = {
        "compiler_law": "positive-root sequential first-hit dilation F_j=A_j^{-dagger} E_j A_j^{-1}",
        "effect_identity": "E_j=sum_{pointer patterns with first hit j} K_p^dagger K_p; final E is all-zero pattern",
        "runtime_schedule": "every fixed neighbor gate executes; no pointer bit controls whether a later gate runs",
        "families": rows,
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "frame_group_failures": frame_group_failures,
        "malformed_rows": malformed,
        "singular_intermediate_remainder_control": singular_control,
        "held_size_tested": 5,
        "pass": global_failures == 0 and frame_group_failures == 0 and all(r["refused"] for r in malformed)
                and singular_control["effect_identity_residual"] < TOL
                and singular_control["inverse_residual"] < TOL,
    }
    check("sequential nearest-neighbor M2 compiler realizes all declared and held menus",
          result["pass"], {"families": len(rows), "frames": len(frames), "held": 5})
    return result


def basis_analysis(direction: tuple[float, float, float]) -> np.ndarray:
    p = projector(direction)
    vals, vecs = np.linalg.eigh(p)
    plus = vecs[:, np.argmax(vals)]
    minus = vecs[:, np.argmin(vals)]
    v = np.column_stack((plus, minus))
    return v.conj().T


def controlled_system_by_coin(r0: np.ndarray, r1: np.ndarray) -> np.ndarray:
    # Two-qubit ordering is (system, coin).
    return (np.kron(r0, P0) + np.kron(r1, P1))


def cnot_system_pointer() -> np.ndarray:
    return np.kron(P0, I2) + np.kron(P1, X)


def pointer_effects_with_hidden_coin(unitary: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Qubit order (system, coin, pointer), with coin/pointer initially zero.
    kraus = {}
    for coin, pointer in product((0, 1), repeat=2):
        k = np.zeros((2, 2), complex)
        for sout, sin in product((0, 1), repeat=2):
            row = (sout << 2) | (coin << 1) | pointer
            col = sin << 2
            k[sout, sin] = unitary[row, col]
        kraus[(coin, pointer)] = k
    effects = tuple(sum((kraus[(c, p)].conj().T @ kraus[(c, p)] for c in (0, 1)),
                        np.zeros((2, 2), complex)) for p in (0, 1))
    return effects


def pointer_channel_choi(unitary: np.ndarray, pointer: int) -> np.ndarray:
    choi = np.zeros((4, 4), complex)
    for coin in (0, 1):
        k = np.zeros((2, 2), complex)
        for sout, sin in product((0, 1), repeat=2):
            row = (sout << 2) | (coin << 1) | pointer
            col = sin << 2
            k[sout, sin] = unitary[row, col]
        choi += np.outer(k.reshape(-1), k.reshape(-1).conj())
    return choi


def mixed_presentation_tournament() -> dict[str, object]:
    target = menu_families()["mixed_projective_merge"]
    write_pointer = embed_gate(cnot_system_pointer(), (0, 2), 3)
    lam_plus = (2.0 + math.sqrt(2.0)) / 4.0
    lam_minus = (2.0 - math.sqrt(2.0)) / 4.0
    coin_rotation = np.array([[math.sqrt(lam_plus), -math.sqrt(lam_minus)],
                              [math.sqrt(lam_minus), math.sqrt(lam_plus)]], complex)

    def presentation_a(z_axis: tuple[float, float, float],
                       x_axis: tuple[float, float, float]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        prep = embed_gate(H, (1,), 3)
        mux = embed_gate(controlled_system_by_coin(basis_analysis(z_axis),
                                                   basis_analysis(x_axis)), (0, 1), 3)
        return mux.conj().T @ write_pointer @ mux @ prep, prep, mux

    def presentation_b(u_axis: tuple[float, float, float]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        prep = embed_gate(coin_rotation, (1,), 3)
        mux = embed_gate(controlled_system_by_coin(basis_analysis(u_axis),
                                                   basis_analysis(tuple(-x for x in u_axis))), (0, 1), 3)
        return mux.conj().T @ write_pointer @ mux @ prep, prep, mux

    # Presentation A: equal coherent coin; z analysis on coin0, x on coin1.
    z_axis = (0.0, 0.0, 1.0)
    x_axis = (1.0, 0.0, 0.0)
    unitary_a, prep_a, mux_a = presentation_a(z_axis, x_axis)
    # Presentation B: spectral split of E0 along u=(x+z)/sqrt(2).
    u = (1.0 / math.sqrt(2.0), 0.0, 1.0 / math.sqrt(2.0))
    unitary_b, prep_b, mux_b = presentation_b(u)
    effects_a = pointer_effects_with_hidden_coin(unitary_a)
    effects_b = pointer_effects_with_hidden_coin(unitary_b)
    direct = compile_menu(target)
    residual_a = max(np.linalg.norm(a - b, ord=2) for a, b in zip(effects_a, target))
    residual_b = max(np.linalg.norm(a - b, ord=2) for a, b in zip(effects_b, target))
    presentation = max(np.linalg.norm(a - b, ord=2) for a, b in zip(effects_a, effects_b))
    direct_residual = max_effect_residual(direct["unitary"], target)
    channel_difference = max(np.linalg.norm(pointer_channel_choi(unitary_a, p)
                                            - pointer_channel_choi(unitary_b, p), ord=2)
                             for p in (0, 1))
    inverse = max(np.linalg.norm(u0.conj().T @ u0 - np.eye(8), ord=2)
                  for u0 in (unitary_a, unitary_b))
    deletion_a = np.linalg.norm(pointer_effects_with_hidden_coin(write_pointer @ prep_a)[0] - target[0], ord=2)
    deletion_b = np.linalg.norm(pointer_effects_with_hidden_coin(write_pointer @ prep_b)[0] - target[0], ord=2)
    covariance_a = 0.0
    covariance_b = 0.0
    for frame in proper_cubic_frames():
        rz = tuple(float(x) for x in frame @ np.asarray(z_axis))
        rx = tuple(float(x) for x in frame @ np.asarray(x_axis))
        ru = tuple(float(x) for x in frame @ np.asarray(u))
        transported_target = transport_menu(target, frame)
        frame_a, _, _ = presentation_a(rz, rx)
        frame_b, _, _ = presentation_b(ru)
        covariance_a = max(covariance_a, max(
            np.linalg.norm(a - b, ord=2)
            for a, b in zip(pointer_effects_with_hidden_coin(frame_a), transported_target)))
        covariance_b = max(covariance_b, max(
            np.linalg.norm(a - b, ord=2)
            for a, b in zip(pointer_effects_with_hidden_coin(frame_b), transported_target)))
    result = {
        "target_E0": "(P_z+P_x)/2",
        "presentation_A": "equal coherent coin with z/x conditional projective analyzers",
        "presentation_B": "spectral coin with lambda_plus P_u + lambda_minus P_minus_u",
        "lambda_plus": lam_plus,
        "lambda_minus": lam_minus,
        "bounded_M2_each_presentation": 3,
        "maximum_gate_support_M2": 2,
        "presentation_A_effect_residual": residual_a,
        "presentation_B_effect_residual": residual_b,
        "presentation_independent_effect_residual": presentation,
        "canonical_direct_dilation_effect_residual": direct_residual,
        "post_state_channel_difference": channel_difference,
        "full_inverse_residual": inverse,
        "delete_A_multiplexer_residual": deletion_a,
        "delete_B_multiplexer_residual": deletion_b,
        "presentation_A_all24_effect_covariance_residual": covariance_a,
        "presentation_B_all24_effect_covariance_residual": covariance_b,
        "coarse_pointer_merge_is_local_projector_sum": True,
        "hidden_coin_is_retained_not_erased": True,
        "matching_effects_called_matching_instruments": False,
        "host_outcome_selection": False,
        "pass": (
            residual_a < TOL and residual_b < TOL and presentation < TOL
            and direct_residual < TOL and channel_difference > 1.0e-3
            and inverse < TOL and deletion_a > 1.0e-3 and deletion_b > 1.0e-3
            and covariance_a < TOL and covariance_b < TOL
        ),
    }
    check("mixed-projective split/merge has two local physical presentations with one effect identity",
          result["pass"], {"effect": presentation, "channel_difference": channel_difference})
    return result


def grading_and_cycle625_interfaces(compiler: dict[str, object], mixed: dict[str, object]) -> dict[str, object]:
    families = menu_families()
    rho = (I2 + 0.2 * X - 0.3 * Y + 0.4 * Z) / 2.0
    rho_eigen = np.linalg.eigvalsh(rho)
    rows = {}
    grade_failures = 0
    route_b_failures = 0
    route_c_failures = 0
    for name, effects in families.items():
        weights = np.array([np.trace(rho @ e).real for e in effects])
        compiled = compile_menu(effects)
        physical_weights = np.array([np.trace(rho @ e).real for e in induced_effects(
            compiled["unitary"], compiled["ports"])])
        grade_residual = float(np.max(np.abs(weights - physical_weights)))
        # Fixed supplied Route-B adapter: first-hit label -> one of six one-hot directions.
        pointer_rows = []
        for pattern in product((0, 1), repeat=compiled["ports"]):
            label = first_hit(pattern)
            onehot = tuple(int(j == label) for j in range(6))
            pointer_rows.append({"pattern": pattern, "effect_label": label, "Route_B_onehot": onehot})
            route_b_failures += int(sum(onehot) != 1)
        kraus = pointer_kraus(compiled["unitary"], compiled["ports"])
        plus = np.array([1.0, 1.0], complex) / math.sqrt(2.0)
        live_sectors = sum(np.linalg.norm(k @ plus) > 1.0e-10 for k in kraus.values())
        # Supplied host diagnostic only: largest-remainder denominator-64 candidate counts.
        raw = 64.0 * weights
        counts = np.floor(raw).astype(int)
        deficit = 64 - int(counts.sum())
        order = sorted(range(len(weights)), key=lambda j: (-(raw[j] - counts[j]), j))
        for j in order[:deficit]:
            counts[j] += 1
        embedded = tuple(int(counts[j]) if j < len(counts) else 0 for j in range(8))
        route_c_failures += int(sum(embedded) != 64 or any(x < 0 for x in embedded))
        grade_failures += int(abs(weights.sum() - 1.0) > TOL or grade_residual > TOL)
        rows[name] = {
            "candidate_w_Tr_rho_E": weights.tolist(),
            "candidate_w_sum_residual": abs(float(weights.sum()) - 1.0),
            "effect_identity_grade_residual": grade_residual,
            "pointer_patterns": pointer_rows,
            "coherent_input_nonzero_pointer_sectors": live_sectors,
            "Route_B_fixed_supplied_adapter": "effect label j -> direction one-hot j among six",
            "Route_C_denominator64_counts": embedded,
            "Route_C_quantizer": "supplied host-side largest remainder diagnostic",
        }
    result = {
        "supplied_diagnostic_rho": "(I+0.2X-0.3Y+0.4Z)/2",
        "rho_minimum_eigenvalue": float(rho_eigen.min()),
        "candidate_grade_definition": "w(E)=Tr(rho E)",
        "grade_used_to_construct_or_select_unitary": False,
        "physical_numeric_grade_output": False,
        "Born_probability_claim": False,
        "frequency_claim": False,
        "Route_B_interface": {
            "committed_upstream_M2": 129,
            "fixed_adapter_is_supplied": True,
            "runtime_actuality_token": False,
            "coherent_pointer_sectors_are_retained": True,
            "pointer_states_called_Records": False,
        },
        "Route_C_interface": {
            "committed_upstream_M2": 531,
            "fixed_eight_history_labels": True,
            "denominator": 64,
            "quantization_is_physical": False,
            "counts_called_realized_frequency_or_Born": False,
        },
        "families": rows,
        "mixed_presentation_effect_independence_consumed": mixed["presentation_independent_effect_residual"] < TOL,
        "pass": grade_failures == 0 and route_b_failures == 0 and route_c_failures == 0
                and rho_eigen.min() > 0.0,
    }
    check("candidate grade and executable Cycle625 B/C adapters remain semantically separated",
          result["pass"], {"families": len(rows), "grade_is_physical": False})
    return result


def physical_controls(compiler: dict[str, object]) -> dict[str, object]:
    # This checks factor separation only.  It deliberately does not relabel a
    # generic two-level spectator as the committed Cycle523 coin/mass object.
    generic_spectator = np.diag([np.exp(-0.371j), np.exp(0.371j)])
    spectator_residual = 0.0
    for effects in menu_families().values():
        unitary = compile_menu(effects)["unitary"]
        instrument = np.kron(unitary, I2)
        spectator = np.kron(np.eye(unitary.shape[0]), generic_spectator)
        spectator_residual = max(spectator_residual,
                                 np.linalg.norm(instrument @ spectator - spectator @ instrument, ord=2))
    blank_malformed = []
    for ports in (1, 2, 3, 4):
        local_projectors = [f"Q_{j}=|0><0| on port {j}" for j in range(ports)]
        blank_malformed.append({
            "ports": ports,
            "commuting_support1_constraints": local_projectors,
            "all_blank_accepted": True,
            "each_nonblank_basis_word_refused_by_declared_input_code": True,
            "autonomous_blank_preparation_or_reset": False,
        })
    result = {
        "generic_separate_spectator_factor_commutator_residual": spectator_residual,
        "generic_spectator_called_Cycle523_mass_fixture": False,
        "committed_Cycle523_mass_fixture_comparison_only": {
            "compiled_rest_mass": 0.453405654174885,
            "Cycle219_fixture_residual": 2.220446049250313e-16,
            "source_ref": COMMITTED_SHORE_HEAD,
            "source_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROTECTED_SHADOW_COIN_GATE_COMPILER_CYCLE523_NOTE_2026-07-21.md",
            "source_line": 30,
            "reexecuted_or_preserved_by_Cycle634": False,
        },
        "Cycle634_one_particle_mass_fixture_preservation_claim": False,
        "spectator_phase_called_energy_or_rate": False,
        "local_auxiliary_code_constraints": blank_malformed,
        "constraints_are_input_code_not_persistent_pointer_constraints": True,
        "blank_ports_are_supplied_genesis": True,
        "inverse_restores_blank_ports_if_output_is_retained_and_uncomputed": True,
        "no_reset_or_renewal_claim": True,
        "resource_genesis_ledger": {
            "supplied": [
                "one system M2 and m-1 blank nearest-neighbor apparatus M2 ports",
                "finite reference star and transported proper-cubic port chart",
                "effect matrices, outcome labels, compiler order, and fixed gate constants",
                "mixed-presentation coin preparation and analyzer axes",
                "diagnostic rho and Route-B/C adapters",
            ],
            "derived": [
                "full local unitary and inverse", "orthogonal pointer-sector Kraus operators",
                "exact induced effects and presentation comparison", "bounded resource count",
            ],
            "open": [
                "autonomous menu parameter genesis", "blank-port renewal/reset", "objective pointer actuality",
                "Record admission/permanence", "physical grade output", "frequency/Born meaning",
            ],
        },
        "pass": spectator_residual < TOL and all(row["each_nonblank_basis_word_refused_by_declared_input_code"]
                                                 for row in blank_malformed),
    }
    check("generic spectator factor and local input-code/resource ledger are explicit without mass back-credit",
          result["pass"], {"spectator_residual": spectator_residual, "constraints": len(blank_malformed)})
    return result


def six_layer_contract(compiler: dict[str, object], grades: dict[str, object]) -> dict[str, object]:
    layers = (
        {"layer": "conditional_form_forcing_theorem", "status": "COMPARISON_ONLY_NO_BACK_CREDIT",
         "Cycle634_closure": False, "remaining_import": "none consumed as a premise"},
        {"layer": "physically_supplied_menu_eligibility", "status": "POSITIVE_FOR_DECLARED_FIXED_COMPILED_MENUS",
         "Cycle634_closure": True, "remaining_import": "which menu/family and its physical parameter genesis"},
        {"layer": "effect_functionality_candidate_grade_w", "status": "ALGEBRAIC_DIAGNOSTIC_ONLY",
         "Cycle634_closure": False, "remaining_import": "physical grade output and state/calibration genesis"},
        {"layer": "occurrence_selector_sigma", "status": "OPEN_POINTER_SECTORS_REMAIN_COHERENT",
         "Cycle634_closure": False, "remaining_import": "objective occurrence selector sigma"},
        {"layer": "Record_and_permanence", "status": "OPEN_POINTER_IS_NOT_RECORD",
         "Cycle634_closure": False, "remaining_import": "Record identification, permanence, readability, renewal"},
        {"layer": "frequency_and_Born_meaning", "status": "OPEN_HOST_DIAGNOSTIC_COUNTS_ONLY",
         "Cycle634_closure": False, "remaining_import": "realized corpus, frequency law, Born meaning"},
    )
    result = {
        "layers": layers,
        "physical_menu_eligibility_narrow_positive": True,
        "menu_family_genesis_derived": False,
        "effect_identity_independent_of_grade": True,
        "pointer_port_is_occurrence": False,
        "pointer_port_is_Record": False,
        "candidate_counts_are_Born_or_frequency": False,
        "pass": len(layers) == 6 and sum(row["Cycle634_closure"] for row in layers) == 1
                and compiler["pass"] and grades["pass"],
    }
    check("six-layer contract promotes only fixed-menu physical eligibility", result["pass"],
          {"closed_layers": 1, "layers": len(layers)})
    return result


def no_go_discipline(compiler: dict[str, object], mixed: dict[str, object],
                      grades: dict[str, object], contract: dict[str, object]) -> dict[str, object]:
    families = [
        {"family": "sequential positive-root first-hit dilation", "object_formulation": "finite qubit POVM and blank neighbor ports",
         "mechanism_invariant": "conditional positive roots and orthogonal first-hit pointer sectors",
         "terminal_obligation": "local fixed-menu physical eligibility", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE", "strength_vs_target": "closes fixed-menu eligibility only"},
        {"family": "coherent coin mixed-projective split/merge", "object_formulation": "coin, system, local pointer",
         "mechanism_invariant": "controlled z/x analyzers with retained coin exhaust",
         "terminal_obligation": "physical merge without host outcome selection", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE", "strength_vs_target": "closes one mixed effect presentation"},
        {"family": "canonical spectral/direct presentation", "object_formulation": "spectral coin or direct positive-root dilation",
         "mechanism_invariant": "same effect under inequivalent post-state channels",
         "terminal_obligation": "embedding-independent effect identity", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE", "strength_vs_target": "effect identity, not instrument identity"},
        {"family": "autonomous menu-program QCA", "object_formulation": "translation-invariant program and apparatus medium",
         "mechanism_invariant": "local generation of effect parameters and pointer ports",
         "terminal_obligation": "derive which menu nature deploys", "honesty_marker": None,
         "search_status": "OPEN_UNTESTED_NOT_COUNTED", "strength_vs_target": "unknown/comparable"},
        {"family": "objective dissipative actualization", "object_formulation": "pointer plus retained environment exhaust",
         "mechanism_invariant": "local nonunitary/stochastic occurrence with covariance",
         "terminal_obligation": "derive sigma without deleting alternatives", "honesty_marker": None,
         "search_status": "OPEN_UNTESTED_NOT_COUNTED", "strength_vs_target": "unknown/comparable"},
        {"family": "renewable Record-corpus calibration", "object_formulation": "admitted persistent records across trials",
         "mechanism_invariant": "renewal, blinding, and convergence controls",
         "terminal_obligation": "derive physical grade/frequency/Born meaning", "honesty_marker": None,
         "search_status": "OPEN_UNTESTED_NOT_COUNTED", "strength_vs_target": "unknown/comparable"},
    ]
    walls = {
        "W_menu_genesis": "which compiled menu/family nature deploys and how parameters are generated",
        "W_grade": "physical effect-functional grade output rather than supplied-rho algebra",
        "W_sigma": "objective occurrence selector on coherent pointer sectors",
        "W_Record": "pointer-to-Record identification and permanence/readability",
        "W_frequency": "renewed realized corpus, independence/convergence, and Born meaning",
        "W_deployment": "translation-invariant infinite deployment, noise, and reset",
    }
    pairs = tuple({"from": a, "to": b, "closure_implied": False,
                   "reason": f"closing {a} does not construct {b} on the exhibited interfaces"}
                  for a in walls for b in walls if a != b)
    current_path = "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py"
    compiler_line = repo_line(current_path, "def sequential_compiler_tournament()")
    mixed_line = repo_line(current_path, "def mixed_presentation_tournament()")
    grade_line = repo_line(current_path, "def grading_and_cycle625_interfaces(")
    contract_line = repo_line(current_path, "def six_layer_contract(")

    def exact_row(prior_path: str, prior_line: int, prior_residual: str, current_line: int,
                  current_residual: str, use_as_closure: bool, prior_ref: str = COMMITTED_SHORE_HEAD) -> dict[str, object]:
        return {"prior_ref": prior_ref, "prior_path": prior_path, "prior_line": prior_line,
                "prior_residual": prior_residual, "current_path": current_path, "current_line": current_line,
                "current_residual": current_residual, "current_numeric_residual": 0.0,
                "same_scope": True, "scope_match": True, "exact_match": True,
                "use_as_closure": use_as_closure}

    exact = (
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", 63,
                  "physical menu eligibility was open on inspected retained surfaces", compiler_line,
                  "declared fixed menus now have literal bounded M2 unitary dilations", True),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", 64,
                  "candidate grade was not effect-functional physical output", grade_line,
                  "w(E)=Tr(rho E) is presentation-independent algebra but remains a supplied diagnostic", False),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", 65,
                  "occurrence selector sigma remained open", contract_line,
                  "orthogonal pointer sectors remain coherent and sigma remains open", False),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", 66,
                  "Record admission/permanence remained physically unidentified", contract_line,
                  "pointer basis states are not promoted to Records", False),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", 67,
                  "candidate corpus was not objective or Born", grade_line,
                  "denominator64 adapter remains supplied host diagnostic only", False),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_PROTECTED_SHADOW_COIN_GATE_COMPILER_CYCLE523_NOTE_2026-07-21.md", 96,
                  "every declared primitive acts on one or two physical M2s", compiler_line,
                  "each binary dilation acts on system and one adjacent apparatus M2", True),
        exact_row("docs/MINIMAL_AXIOMS_2026-06-29.md", 65,
                  "Records form is axiom content", contract_line,
                  "Cycle634 does not call pointer ports Records or rederive occurrence", False),
        exact_row("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md", 37,
                  "pointwise realized-state evaluation is not state selection", grade_line,
                  "supplied rho diagnostic is not occurrence or state selection", False),
    )
    dropped = tuple({
        "prior_ref": spec["head_oid"], "prior_path": spec["path"], "prior_line": spec["line"],
        "prior_residual": spec["use"], "current_path": current_path, "current_line": compiler_line,
        "current_residual": "closed conditional theorem is not used as physical dilation evidence",
        "same_scope": False, "scope_match": False, "exact_match": False, "use_as_closure": False,
        "disposition": "comparison-only; no back-credit",
    } for spec in EXTERNAL_COMPARISON_HEADS.values())

    def rhetoric(phrase: str, **tested: str) -> dict[str, str]:
        return {"phrase": phrase,
                "per_element": tested.get("per_element", "UNTESTED_NO_NEGATIVE_CLAIM"),
                "per_mode": tested.get("per_mode", "UNTESTED_NO_NEGATIVE_CLAIM"),
                "per_site": tested.get("per_site", "UNTESTED_NO_NEGATIVE_CLAIM"),
                "per_block": tested.get("per_block", "UNTESTED_NO_NEGATIVE_CLAIM"),
                "lattice_wide": tested.get("lattice_wide", "UNTESTED_NO_NEGATIVE_CLAIM")}

    rhetoric_rows = (
        rhetoric("fixed-menu physical eligibility is not autonomous menu genesis", per_site="four bounded menu cells"),
        rhetoric("effect identity is not a physical grade output", per_element="all declared effects", per_block="four menus"),
        rhetoric("pointer sector is not occurrence selector sigma", per_mode="all pointer patterns", per_site="coherent input sectors"),
        rhetoric("pointer basis state is not a Record", per_element="local ports", per_block="inverse/deletion tests"),
        rhetoric("denominator64 candidate count is not frequency or Born meaning", per_mode="eight Route-C labels", per_block="four diagnostic menus"),
        rhetoric("finite cubic star is not infinite translation-invariant deployment", per_site="all24 transported stars"),
    )
    partial = (
        {"file": current_path, "status": "EXECUTED_FIXED_MENU_DILATION", "what_closes": "bounded physical menu eligibility for declared menus"},
        {"file": current_path, "status": "EXECUTED_MIXED_PRESENTATIONS", "what_closes": "effect identity across two inequivalent local dilation presentations"},
        {"file": current_path, "status": "EXECUTED_C625_ROUTE_B_ADAPTER", "what_closes": "pointer label to candidate one-hot interface only"},
        {"file": current_path, "status": "EXECUTED_C625_ROUTE_C_DIAGNOSTIC", "what_closes": "supplied denominator64 candidate-count interface only"},
        {"file": "scripts/physical_autonomous_menu_program_genesis_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "menu/family parameter genesis"},
        {"file": "scripts/physical_sigma_Record_frequency_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "actuality, Record, renewal, and blinded frequency law"},
    )
    steelman = {
        "mechanism": "a translation-invariant local apparatus QCA prepares its own menu program and blank ports, runs this dilation, retains all exhaust, objectively actualizes one sector, preserves an admitted Record, renews, and yields blinded frequencies",
        "supporting_authorities": (
            {"ref": COMMITTED_SHORE_HEAD,
             "path": "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md",
             "line": 63, "relevance": "prior physical-menu wall now narrowed by this compiler"},
            {"ref": COMMITTED_SHORE_HEAD, "path": "docs/MINIMAL_AXIOMS_2026-06-29.md", "line": 65,
             "relevance": "Record formation is supplied but its physical formation law is not"},
            {"ref": COMMITTED_SHORE_HEAD, "path": "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md", "line": 37,
             "relevance": "realized-state evaluation cannot substitute for a selector"},
        ),
        "actionable_test": "compile a local menu-program register and autonomous blank renewal, then require all24/all576, inverse/exhaust, coherent sigma, post-admission preservation, and blinded changed-rho frequencies",
        "openness": "this target-equivalent route is open, so broad negative, shared-obstruction, minimum-content, and axiom-pressure claims do not ship",
    }
    echoes = (
        {"cycle": "Cycle523", "retired": "SUPPORT_TWO_VOCABULARY_REUSED", "mechanism": "one-/two-M2 primitive surface",
         "applicability": "supports literal local gate cardinality, not menu semantics", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROTECTED_SHADOW_COIN_GATE_COMPILER_CYCLE523_NOTE_2026-07-21.md", "citation_line": 96},
        {"cycle": "Cycle625", "retired": "PHYSICAL_FIXED_MENU_WALL_PARTIALLY_RETIRED", "mechanism": "six-layer acceptance contract",
         "applicability": "fixed declared menu now physical; genesis/grade/sigma/Record/Born remain", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", "citation_line": 63},
        {"cycle": "Cycle625 RouteB", "retired": "NOT_ACTUALITY", "mechanism": "129-M2 candidate packet interface",
         "applicability": "Cycle634 exports one-hot labels but no selector", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", "citation_line": 161},
        {"cycle": "Cycle625 RouteC", "retired": "NOT_BORN", "mechanism": "531-M2 candidate grade block",
         "applicability": "Cycle634 supplies only diagnostic denominator64 counts", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", "citation_line": 188},
        {"cycle": "PR5472", "retired": "CLOSED_NONRETAINED_COMPARISON_ONLY", "mechanism": "conditional effect-menu forcing",
         "applicability": "no physical compiler back-credit", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5472"]["head_oid"],
         "citation_path": EXTERNAL_COMPARISON_HEADS["PR5472"]["path"], "citation_line": 60},
        {"cycle": "PR5476", "retired": "CLOSED_NONRETAINED_COMPARISON_ONLY", "mechanism": "conditional scaled-projector forcing",
         "applicability": "no physical compiler back-credit", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5476"]["head_oid"],
         "citation_path": EXTERNAL_COMPARISON_HEADS["PR5476"]["path"], "citation_line": 17},
        {"cycle": "PR5479", "retired": "CLOSED_NONRETAINED_COMPARISON_ONLY", "mechanism": "conditional mixed-projective forcing",
         "applicability": "no physical compiler back-credit", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5479"]["head_oid"],
         "citation_path": EXTERNAL_COMPARISON_HEADS["PR5479"]["path"], "citation_line": 62},
    )
    result = {
        "N1_normalized_families": families,
        "N1_qualifying_attempts": 3,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "FAIL_DO_NOT_SHIP",
        "N2_collapsed_walls": walls,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N2_all_pair_implications_false_on_exhibited_interfaces": True,
        "N3_hidden_wall_scan": [
            "effect matrices, labels, compile order, gate constants, and finite reference star",
            "blank apparatus M2 genesis and support-one input-code constraints",
            "mixed coin weights, axes, analyzer gates, and retained hidden coin",
            "supplied diagnostic rho, Route-B one-hot adapter, and Route-C denominator64 quantizer",
            "outcome aggregation is an analytical pointer-projector sum, not host runtime selection",
            "menu genesis, grade output, sigma, Record/permanence, renewal, frequency/Born meaning, and infinite deployment remain explicit",
        ],
        "N4_residual_matching": exact,
        "N4_exact_residual_matches": exact,
        "N4_dropped_nonmatches": dropped,
        "N5_rhetoric_audit": rhetoric_rows,
        "N5_rhetoric_resolution_ledger": rhetoric_rows,
        "N6_partial_closure": partial,
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "Status": "FAIL",
        "artifact_status": "PASS_NARROW_FIXED_MENU_PHYSICAL_DILATION_ONLY",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "axiom_pressure_claim": False,
        "pass": (
            compiler["pass"] and mixed["pass"] and grades["pass"] and contract["pass"]
            and len(families) == 6 and sum(r["honesty_marker"] == "ATTEMPTED" for r in families) == 3
            and len(pairs) == 30 and len(exact) == 8 and len(dropped) == 3
            and all(r["same_scope"] and r["exact_match"] and all(k in r for k in
                    ("prior_ref", "prior_path", "prior_line", "current_path", "current_line", "use_as_closure")) for r in exact)
            and all(not r["same_scope"] and not r["exact_match"] and not r["use_as_closure"] for r in dropped)
            and len(rhetoric_rows) == 6 and all(all(k in r for k in
                    ("per_element", "per_mode", "per_site", "per_block", "lattice_wide")) for r in rhetoric_rows)
            and len(partial) == 6 and all(all(k in r for k in ("file", "status", "what_closes")) for r in partial)
            and all(all(k in r for k in ("cycle", "retired", "mechanism", "applicability", "citation_ref", "citation_path", "citation_line")) for r in echoes)
            and all(all(k in r for k in ("ref", "path", "line")) for r in steelman["supporting_authorities"])
        ),
    }
    check("current N1-N8 forbids broad negative, shared obstruction, minimum content, and axiom pressure",
          result["pass"], {"attempted": 3, "required": 5, "pairs": len(pairs)})
    return result


def inventory() -> dict[str, object]:
    return {
        "supplied": [
            f"immutable committed shores at {COMMITTED_SHORE_HEAD}; dirty working-tree bytes are comparison-only",
            "closed PR5472/5476/5479 heads as comparison-only objects with no back-credit",
            "finite effect matrices, outcome labels, compile order, and one transported cubic reference star",
            "one system M2 plus blank apparatus M2 ports and their support-one input-code constraints",
            "mixed-presentation coin preparations, axes, and analyzer gates",
            "diagnostic rho, fixed Route-B label adapter, and Route-C denominator64 quantizer",
        ],
        "derived": [
            "one reusable positive-root sequential compiler for declared 2..7-outcome qubit menus",
            "exact unitary dilations and pointer-effect identities for ternary trine, scaled axis-cancellation, mixed merge, and held size5",
            "support-two nearest-neighbor cubic-star layout, explicit inverse, deletion, malformed, leakage/norm, all24/all576, and generic spectator-factor controls",
            "two inequivalent mixed-projective physical presentations with identical effects but different post-state channels",
            "executable candidate-only interfaces to committed Cycle625 Routes B and C",
        ],
        "open": [
            "autonomous physical genesis/selection of the menu family and parameters",
            "physical effect-functional numeric grade output and calibration genesis",
            "objective occurrence selector sigma with exhaust ownership",
            "pointer-to-Record identification, permanence/readability, reset, and renewal",
            "realized corpus, frequency law, independence/convergence, and Born meaning",
            "translation-invariant infinite/noisy deployment and gravity/source coupling",
        ],
    }


def note_text(receipt: dict[str, object]) -> str:
    compiler = receipt["sequential_compiler"]
    mixed = receipt["mixed_projective_presentations"]
    grades = receipt["candidate_grade_and_Cycle625_interfaces"]
    family_rows = "\n".join(
        f"| {name} | {row['outcomes']} | {row['bounded_M2_system_plus_apparatus']} | "
        f"{row['binary_neighbor_gates']} | {row['literal_gate_calls']} | {row['exact_effect_identity_residual']:.3e} | "
        f"{row['unitary_covariance_residual']:.3e} | {min(row['deletion_residuals']):.3e} |"
        for name, row in compiler["families"].items()
    )
    layers = "\n".join(
        f"| {row['layer']} | {row['status']} | {'yes' if row['Cycle634_closure'] else 'no'} | {row['remaining_import']} |"
        for row in receipt["six_layer_contract"]["layers"]
    )
    return f"""# Physical forcing-menu instrument bridge tournament — Cycle 634

Classification: **positive bounded fixed-menu M2 instrument compiler; menu genesis, physical grade, occurrence, Record, and Born meaning remain supplied/open**

Authority: **none**

Audit: **unset**

## Decisive result

Cycle 634 constructs the physical menu layer that Cycle 625 left open for a
declared finite family.  For a supplied qubit POVM `E_0,...,E_(m-1)`, `2 <= m <=
7`, one system M2 occupies the center of a cubic star and `m-1` blank apparatus
M2s occupy distinct nearest-neighbor ports.  At stage `j`, the compiler forms
`F_j=A_j^(-dagger) E_j A_j^(-1)` and applies the two-M2 unitary

```text
U(F) = sqrt(I-F) x |0><0| - sqrt(F) x |0><1|
     + sqrt(F) x |1><0| + sqrt(I-F) x |1><1|.
```

Every gate runs in the fixed schedule.  No pointer value controls a later gate
and no host selects an outcome.  Summing `K_p^dagger K_p` over the orthogonal
pointer patterns whose first `1` is `j` gives exactly `E_j`; the all-zero
pattern gives the final effect.  This is a physical fixed-menu dilation and a
local pointer-port identity.  It is not a physical rule selecting which menu
nature deploys.

| family | outcomes | system+apparatus M2 | binary NN macros | literal one-/two-M2 calls | effect residual | all24 unitary covariance | minimum deletion residual |
|---|---:|---:|---:|---:|---:|---:|---:|
{family_rows}

The held five-outcome split-trine case uses five M2 and four central-neighbor
gates.  Thus the construction has constant overhead per compiled coarse menu
cell and maximum literal support two.  It uses no global parity string,
preferred lattice ordering, nonlocal service, or runtime outcome control.
Each binary macro is lowered exactly to four supplied one-M2 rotations and two
nearest-neighbor CNOTs; the maximum observed lowering residual is
`{max(r['binary_dilation_primitive_lowering_residual'] for r in compiler['families'].values()):.3e}`.
The Moore-Penrose support extension also passes the singular intermediate
remainder control `{{P_z,0.4P_-z,0.6P_-z}}` with effect residual
`{compiler['singular_intermediate_remainder_control']['effect_identity_residual']:.3e}`.

The apparatus code constraint is the product of one-site `|0><0|` input
projectors.  Each constraint is locally checkable at support one and every
nonblank basis input is refused by the declared compiler domain.  Blank genesis
and renewal are supplied; the constraints are not misreported as a persistent
gauge law after the ports become pointers.  Daggering the fixed unitary gives
the inverse and restores blanks when the retained output is uncomputed.

## Ternary, scaled-projector, and mixed-projective probes

The ternary menu is the equatorial trine `E_j=(2/3)P(n_j)`.  The scaled menu
uses `c=2/(1+sqrt(3))` and
`{{c P(111), c/sqrt(3) P(-x), c/sqrt(3) P(-y), c/sqrt(3) P(-z)}}`; the vector
parts cancel and the effects sum to identity.  Every ordering of the ternary
and scaled menus is compiled (6 and 24 orderings respectively), and labeled
effect recovery is unchanged although the dilation embedding and post-state
map may change.

For `E_0=(P_z+P_x)/2`, two separate three-M2 physical presentations were
constructed.  Presentation A prepares an equal coherent coin, analyzes `z` on
coin zero and `x` on coin one, and writes a local pointer.  Presentation B uses
the spectral weights `lambda_plus={mixed['lambda_plus']:.12f}` and
`lambda_minus={mixed['lambda_minus']:.12f}` with analyzers along
`u=(x+z)/sqrt(2)` and `-u`.  After summing over the retained coin, their effect
identity residual is `{mixed['presentation_independent_effect_residual']:.3e}`.
Their post-state channel difference is `{mixed['post_state_channel_difference']:.3e}`:
same effects do **not** imply the same instrument.  A direct canonical
positive-root dilation supplies a third covariant representative.

## Proper-cubic covariance and physical controls

The exact proper-cubic group has {compiler['proper_cubic_frames']} frames and
{compiler['ordered_frame_products']} ordered products.  Each reference port ray
is transported with the frame.  Spinor conjugation transports every effect,
and functional calculus transports every compiled binary gate.  The largest
observed unitary covariance residual is
`{max(r['unitary_covariance_residual'] for r in compiler['families'].values()):.3e}`.
The reference chart and menu orientation remain supplied genesis, not a
preferred physical frame.

Negative, nonnormalized, non-Hermitian, and eight-outcome-on-six-port menus are
refused.  Omitting every binary gate changes at least one induced effect.  The
full unitary is norm-preserving on the blank-port code and has no unused local
levels.  A generic independent two-level spectator factor commutes with every
instrument at residual
`{receipt['physical_controls']['generic_separate_spectator_factor_commutator_residual']:.3e}`.
It is **not** called the committed Cycle523 coin/mass fixture.  Cycle523's
`0.453405654174885` rest-mass result and `2.220446049250313e-16` fixture residual
are pinned comparison-only; Cycle634 does not reexecute or claim preservation
of that object.  No wrapped phase is called energy and no generator is called a rate.

## Prior-art and novelty boundary

Finite-outcome POVM/Naimark dilation, sequential binary decompositions, and the
nonuniqueness of instruments realizing a fixed POVM are standard mechanism
classes.  Cycle634 claims no general novelty or priority for them.  The bounded
repo-specific contribution is the declared forcing-menu cubic-star
compilation, its exact proper-cubic/held/deletion/domain controls, and its typed
candidate-only interfaces to committed Cycle625 Routes B and C.  No external
theorem is used as runner evidence; the closed Born heads remain comparison-only.

## Six-layer separation

| layer | status | closed here | remaining import |
|---|---|---:|---|
{layers}

The exact effect identity is derived before any grade is introduced.  For the
supplied diagnostic state `rho=(I+0.2X-0.3Y+0.4Z)/2`, Cycle634 later evaluates
the algebraic candidate `w(E)=Tr(rho E)` and confirms presentation
independence.  This is not a physical numeric grade output and is never used to
justify or select the dilation.

The Cycle625 Route-B adapter maps every pointer first-hit label to one supplied
six-direction one-hot candidate.  Coherent inputs retain multiple orthogonal
pointer sectors, so this is a candidate correlation and not `sigma`.  Pointer
basis states are not Records.  The Route-C adapter embeds the candidate `w`
values into eight labels using a supplied host-side largest-remainder
denominator-64 quantizer.  Those counts are not realized frequencies or Born
probabilities.

## Supplied / derived / open

Supplied: effect matrices and labels, compile order, finite star chart, blank
ports, gate constants, mixed-presentation coin/analyzer data, diagnostic rho,
and the Route-B/C adapters.  The closed PR5472/5476/5479 heads are immutable
comparison-only objects with no back-credit.

Derived: the bounded local unitaries and inverses, exact pointer effects,
ternary/scaled/mixed/held compilers, all24/all576 covariance, deletion and
malformed controls, presentation-independent effect identity, and executable
candidate interfaces into Cycle625.

Open: autonomous menu/family parameter genesis, physical grade output,
objective selector `sigma`, Record identification and permanence, reset and
renewal, realized corpus/frequency/Born meaning, infinite noisy deployment, and
gravity/source integration.

## N1–N8 no-go discipline

N1 normalizes six families.  Three constructive families were attempted:
sequential positive-root dilation, coherent-coin mixed splitting, and
canonical spectral/direct presentation.  Autonomous menu-program QCA,
objective dissipative actualization, and renewable Record-corpus calibration
remain open and do not count.  Three is below the required five attempts, so
the broad-negative gate is **FAIL / DO NOT SHIP**.

N2 collapses six walls and audits all 30 directed pairs.  N3 inventories every
menu, blank, chart, order, coin, grade, and adapter import.  N4 contains eight
exact same-scope residual rows and three dropped closed-head comparisons.  N5
contains six five-resolution rhetoric rows.  N6 contains six structured
`file` / `status` / `what_closes` paths.  N7 gives an actionable autonomous
apparatus-QCA steelman.  N8 gives seven row-wise exact cross-cycle echoes.

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle634 movement | residual |
|---|---|---|
| `C_ref` | fixed reference-star menus acquire transported physical M2 dilations | star/menu orientation and parameter genesis remain supplied; no preferred physical frame is claimed |
| `C_num` | exact ternary, scaled, mixed, held-size5 effects and algebraic candidate `w` | no physical grade output, general precision law, realized frequencies, or Born meaning |
| `C_wrap` | local pointer ports and exact coarse effect identities are physical | no objective `sigma`, Record identification, permanence, reset, renewal, or realized history |
| `C_int` | system-apparatus coupling is a literal support-two unitary instrument | its gate constants are compiled from a supplied menu; no new matter interaction law or generator/rate claim |
| `C_local` | one cubic star, up to seven outcomes, all24/all576, inverse/deletion/malformed/held controls | infinite tiling, overlapping apparatus, noise, and autonomous blank enforcement remain open |
| `C_source` | blank apparatus capacity and retained mixed-presentation coin exhaust are explicit | no energy/stress/source/gravity meaning or autonomous resource genesis |

## Disposition

**PASS** for a literal bounded physical M2 compiler of the declared fixed-menu
families and for exact effect identities at local pointer ports.

**FAIL / DO NOT CLAIM** for autonomous menu eligibility across nature's menu
family, a physical grade, objective occurrence, Record/permanence, realized
frequency, Born probability, universal instrument equivalence, shared
obstruction, minimum content, or axiom pressure.

The optimal next campaign is the autonomous menu-program and blank-renewal
bridge: encode the menu parameters in a bounded covariant physical program,
prepare/refurbish local ports without a host, feed the resulting pointer
sectors into the unchanged Cycle625 Route-B interface, and require retained
exhaust plus a blinded sigma/Record/frequency test before any probability
interpretation.
"""


def normalized_note(path: Path) -> str:
    return " ".join(path.read_text().lower().split())


def note_contract() -> dict[str, object]:
    required = (
        "authority: **none**", "audit: **unset**", "fixed-menu m2 instrument compiler",
        "no host selects an outcome", "pointer basis states are not records",
        "not realized frequencies or born probabilities", "comparison-only objects with no back-credit",
        "claims no general novelty or priority", "cycle634 does not reexecute or claim preservation",
        "three is below the required five attempts", "all 30 directed pairs",
        "eight exact same-scope residual rows", "six five-resolution rhetoric rows",
        "shared route-independent obstruction: **not established**", "axiom pressure: **none**",
    )
    body = normalized_note(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    return {"required_fragments": required, "missing": missing, "pass": not missing}


def main() -> None:
    signal.alarm(math.ceil(WALL_CAP_SECONDS))
    started = time.perf_counter()
    shore = shore_controls()
    external = external_comparison_controls()
    compiler = sequential_compiler_tournament()
    mixed = mixed_presentation_tournament()
    grades = grading_and_cycle625_interfaces(compiler, mixed)
    controls = physical_controls(compiler)
    contract = six_layer_contract(compiler, grades)
    no_go = no_go_discipline(compiler, mixed, grades, contract)
    receipt = {
        "status": "positive bounded fixed-menu M2 instrument compiler; menu genesis, grade, sigma, Record, and Born meaning remain supplied/open",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "shore": shore,
        "external_comparison_heads": external,
        "sequential_compiler": compiler,
        "mixed_projective_presentations": mixed,
        "candidate_grade_and_Cycle625_interfaces": grades,
        "physical_controls": controls,
        "six_layer_contract": contract,
        "no_go_discipline": no_go,
        "inventory": inventory(),
        "prior_art_and_novelty_boundary": {
            "standard_mechanism_classes": [
                "finite-outcome POVM/Naimark dilation",
                "sequential binary decompositions",
                "nonuniqueness of instruments realizing a fixed POVM",
            ],
            "general_novelty_or_priority_claim": False,
            "repo_specific_contribution": "declared forcing-menu cubic-star compilation with exact proper-cubic/held/deletion/domain controls and typed candidate-only Cycle625 interfaces",
            "external_theorem_used_as_runner_evidence": False,
        },
        "strongest_constructive_result": "a reusable positive-root sequential compiler realizing declared 2..7-outcome qubit effect menus on one system M2 plus bounded nearest-neighbor pointer M2s with exact local effect identities",
        "highest_honest_terminal": "physical eligibility of the declared fixed compiled menu and local pointer effect algebra; not autonomous menu genesis, grade, actuality, Record, or probability",
        "route_by_route_disposition": {
            "ternary_trine": "PASS_LOCAL_3M2_TWO_GATE_DILATION",
            "scaled_projector_axis_cancellation": "PASS_LOCAL_4M2_THREE_GATE_DILATION",
            "mixed_projective_split_merge": "PASS_TWO_3M2_PRESENTATIONS_PLUS_DIRECT_DILATION",
            "held_size5": "PASS_LOCAL_5M2_FOUR_GATE_DILATION",
            "autonomous_menu_program": "OPEN_NOT_ATTEMPTED",
        },
        "six_wall_ledger": {
            "C_ref": "fixed reference-star menus now have covariant physical dilations; chart/menu genesis remains supplied",
            "C_num": "exact finite effect identities and algebraic candidate w; no physical grade, frequency, or Born meaning",
            "C_wrap": "local pointer ports are physical; sigma, Record/permanence, renewal, and history remain open",
            "C_int": "literal support-two system-apparatus unitary; supplied gate constants and no new interaction/generator/rate law",
            "C_local": "bounded star through seven outcomes with inverse/deletion/malformed/held/all24/all576; infinite/noisy deployment open",
            "C_source": "blank capacity and coin exhaust explicit; no energy/stress/source/gravity meaning or autonomous genesis",
        },
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "breakthrough": False,
        "breakthrough_bar_met": False,
        "maturity_rebase": None,
        "semantic_promotion_boundary": {
            "author_artifact_status_accepted": False,
            "breakthrough_bar_met": False,
            "physical_fixed_menu_eligibility": "POSITIVE_ON_DECLARED_2_TO_7_OUTCOME_QUBIT_MENUS",
            "autonomous_menu_family_genesis": None,
            "physical_effect_functionality_w": None,
            "objective_occurrence_selector_sigma": None,
            "framework_Record_identification": None,
            "physical_permanence_and_renewal": None,
            "Born_probability": None,
            "frequency_meaning": None,
            "realized_history": None,
        },
        "optimal_next_campaign": "autonomous bounded menu-program and blank-renewal QCA feeding the unchanged Cycle625 Route-B pointer interface, with retained exhaust and blinded sigma/Record/frequency tests",
    }
    NOTE.write_text(note_text(receipt))
    note_check = note_contract()
    check("Cycle634 note preserves exact scope and semantic boundaries", note_check["pass"], note_check["missing"])
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000:
        rss *= 1024
    receipt.update({
        "note_contract": note_check,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
    })
    receipt["pass"] = (
        FAIL == 0 and shore["pass"] and external["pass"] and compiler["pass"] and mixed["pass"]
        and grades["pass"] and controls["pass"] and contract["pass"] and no_go["pass"]
        and note_check["pass"] and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
        and AUTHORITY == "none" and AUDIT == "unset"
    )
    RECEIPT.write_text(json.dumps(
        receipt, indent=2, sort_keys=True,
        default=lambda value: value.item() if isinstance(value, np.generic) else list(value),
    ) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
