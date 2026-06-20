#!/usr/bin/env python3
"""Poisson/CHSH to teleportation-resource audit.

Citeable content: the BOUNDED FINITE EXTRACTION CORE. This script asks a narrow
question on the two small audited surfaces (`1D N=8`, `2D 4x4`):

    Does the existing Poisson-driven CHSH ground state already contain a
    deterministic, high-fidelity encoded Bell pair usable as the resource for
    ordinary quantum state teleportation, under the retained-axis finite
    operator-algebra last-taste-bit identification?

The core checks (helper source, retained-axis finite operator algebra, last-taste
carrier algebra, teleportation-convention sanity, null control, and the bounded
extraction diagnostics on the two surfaces) carry per-check PASS:/FAIL: tags and a
final TOTAL/SUMMARY PASS=N FAIL=0.

The native preparation/readout/apparatus bridge (a physical deterministic
teleportation apparatus) is open and NOT part of the citeable core.
Its consistency report is segregated and does not contribute to the core summary.

It does not claim matter teleportation, charge transfer, mass transfer, or FTL
transport. It only audits the two-species state produced by the existing
`frontier_bell_inequality.py` machinery.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.linalg import eigh


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_bell_inequality as bell_lane  # noqa: E402
from frontier_bell_inequality import (  # noqa: E402
    build_H1,
    build_H2_tensor,
    build_pair_hop_X,
    build_poisson,
    build_sublattice_Z,
    chsh_horodecki,
    lattice_1d,
    lattice_2d,
    lattice_3d,
)


I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)

OUTCOME_ORDER = ((0, 0), (1, 0), (0, 1), (1, 1))
OUTCOME_LABELS = {
    (0, 0): "Phi+",
    (1, 0): "Phi-",
    (0, 1): "Psi+",
    (1, 1): "Psi-",
}
SOURCE_REQUIRED_SYMBOLS = (
    "build_H1",
    "build_H2_tensor",
    "build_pair_hop_X",
    "build_poisson",
    "build_sublattice_Z",
    "build_cell_taste_operator",
    "taste_identity_check",
    "chsh_horodecki",
    "lattice_1d",
    "lattice_2d",
    "lattice_3d",
)
RALA_CLAIM_ID = "teleportation_retained_axis_operator_algebra_closure_note"
RESOURCE_NOTE = ROOT / "docs" / "TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"
RALA_NOTE = ROOT / "docs" / "TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md"
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}
PREP_READOUT_NOTE = ROOT / "docs" / "TELEPORTATION_PREPARATION_READOUT_PROBE_NOTE.md"
OPERATOR_END_TO_END_NOTE = ROOT / "docs" / "TELEPORTATION_OPERATOR_CONSISTENT_END_TO_END_NOTE.md"
MICROSCOPIC_CLOSURE_NOTE = ROOT / "docs" / "TELEPORTATION_MICROSCOPIC_CLOSURE_NOTE.md"
APPARATUS_DYNAMICS_NOTE = ROOT / "docs" / "TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
RALA_REQUIRED_SNIPPETS = (
    "RALA(a) = { O_logical",
    "T2 (axis Pauli operators are in RALA)",
    "T3 (axis Bell projectors are in pair-RALA)",
    "T5 (fixed pair-hop X membership)",
    "T8 (RALA teleportation closure)",
)


@dataclasses.dataclass(frozen=True)
class AuditCase:
    label: str
    dim: int
    side: int
    mass: float
    G: float


@dataclasses.dataclass(frozen=True)
class SiteFactorization:
    logical: np.ndarray
    env: np.ndarray
    env_labels: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]


DEFAULT_CASES = (
    AuditCase("1d_null", dim=1, side=8, mass=0.0, G=0.0),
    AuditCase("1d_poisson_chsh", dim=1, side=8, mass=0.0, G=1000.0),
    AuditCase("2d_poisson_chsh", dim=2, side=4, mass=0.0, G=1000.0),
)


def lattice_for_case(case: AuditCase):
    if case.dim == 1:
        return lattice_1d(case.side)
    if case.dim == 2:
        return lattice_2d(case.side)
    if case.dim == 3:
        return lattice_3d(case.side)
    raise ValueError(f"unsupported dimension: {case.dim}")


def helper_source_certificate() -> dict[str, object]:
    helper_path = Path(bell_lane.__file__).resolve()
    helper_text = helper_path.read_text(encoding="utf-8")
    missing = [
        symbol
        for symbol in SOURCE_REQUIRED_SYMBOLS
        if not hasattr(bell_lane, symbol) or f"def {symbol}" not in helper_text
    ]
    if missing:
        raise RuntimeError(f"Poisson/CHSH helper source is incomplete: {missing}")
    return {
        "path": helper_path,
        "sha256": hashlib.sha256(helper_text.encode("utf-8")).hexdigest(),
        "line_count": len(helper_text.splitlines()),
        "symbol_count": len(SOURCE_REQUIRED_SYMBOLS),
    }


def ledger_status(claim_id: str) -> str | None:
    if not LEDGER_PATH.exists():
        return None
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = ledger.get("rows", ledger)
    if isinstance(rows, dict):
        iterable = rows.values()
    else:
        iterable = rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row.get("effective_status")
    return None


def retained_axis_source_certificate() -> dict[str, object]:
    if not RALA_NOTE.exists():
        raise RuntimeError("RALA retained-axis source note is missing")
    text = RALA_NOTE.read_text(encoding="utf-8")
    missing = [snippet for snippet in RALA_REQUIRED_SNIPPETS if snippet not in text]
    if missing:
        raise RuntimeError(f"RALA source note is missing expected theorem snippets: {missing}")
    status = ledger_status(RALA_CLAIM_ID)
    if status not in RETAINED_GRADES:
        raise RuntimeError(
            "RALA source note must remain retained-grade for this bounded support route; "
            f"ledger status={status!r}"
        )
    return {
        "path": RALA_NOTE,
        "status": status,
        "snippet_count": len(RALA_REQUIRED_SNIPPETS),
    }


def source_status_firewall_certificate() -> dict[str, object]:
    note_text = RESOURCE_NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    prep_text = PREP_READOUT_NOTE.read_text(encoding="utf-8")
    op_text = OPERATOR_END_TO_END_NOTE.read_text(encoding="utf-8")
    micro_text = MICROSCOPIC_CLOSURE_NOTE.read_text(encoding="utf-8")
    apparatus_text = APPARATUS_DYNAMICS_NOTE.read_text(encoding="utf-8")
    required_note_snippets = (
        "2026-06-12 Native Preparation/Readout Hard Residual",
        "The live blocker is still a native preparation/readout and apparatus theorem",
        "No retained-grade proposal or status promotion is made here",
        "row remains an open gate for a physical deterministic resource",
        "2026-06-15 Native Apparatus Candidate Bridge",
        "TELEPORTATION_MICROSCOPIC_CLOSURE_NOTE.md",
        "TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md",
        "concrete bridge path, not a retained teleportation theorem and not an audit verdict",
    )
    missing = [snippet for snippet in required_note_snippets if snippet not in note_flat]
    if missing:
        raise RuntimeError(f"source firewall snippets missing from resource note: {missing}")
    if "preparation/readout remains open" not in prep_text.lower():
        raise RuntimeError("preparation/readout probe no longer states the hard residual")
    if "physical apparatus derivation" not in op_text.lower():
        raise RuntimeError("operator-consistent end-to-end note no longer firewalls prep/readout")
    micro_lower = micro_text.lower()
    microscopic_snippets = (
        "native retained-axis `cl(3)/z^3` stabilizers close",
        "stabilizer-controlled transducer hamiltonian terms commute",
        "thermodynamic bath bound drives record overlap to zero",
        "native taste-apparatus ledger theorem covers controlled generators",
        "resource preparation and retained readout/correction scaling remain bounded",
    )
    missing_micro = [
        snippet for snippet in microscopic_snippets if snippet not in micro_lower
    ]
    if missing_micro:
        raise RuntimeError(
            f"microscopic closure candidate no longer states expected gates: {missing_micro}"
        )
    apparatus_lower = apparatus_text.lower()
    apparatus_snippets = (
        "retarded field front derives eikonal carrier",
        "bell transducer is finite-strength unitary, not projection",
        "finite spin bath decoheres records irreversibly when traced",
        "apparatus energy and ledgers are branch independent",
        "microscopic `cl(3)/z^3` apparatus hamiltonian",
    )
    missing_apparatus = [
        snippet for snippet in apparatus_snippets if snippet not in apparatus_lower
    ]
    if missing_apparatus:
        raise RuntimeError(
            f"apparatus dynamics candidate no longer states expected gates: {missing_apparatus}"
        )
    return {
        "path": RESOURCE_NOTE,
        "prep_probe": PREP_READOUT_NOTE,
        "operator_end_to_end": OPERATOR_END_TO_END_NOTE,
        "microscopic_closure": MICROSCOPIC_CLOSURE_NOTE,
        "apparatus_dynamics": APPARATUS_DYNAMICS_NOTE,
        "snippet_count": len(required_note_snippets)
        + len(microscopic_snippets)
        + len(apparatus_snippets),
    }


def logical_carrier_certificate(case: AuditCase) -> dict[str, object]:
    n, _adj, parity, _coords = lattice_for_case(case)
    factors = factor_sites(case.dim, case.side)
    if len(factors.env_labels) != n // 2:
        raise RuntimeError(f"{case.label}: expected {n // 2} logical environments")

    env_logical_counts: dict[int, set[int]] = {}
    for site, env_index in enumerate(factors.env):
        env_logical_counts.setdefault(int(env_index), set()).add(int(factors.logical[site]))
    bad_envs = [
        env_index
        for env_index, logical_values in env_logical_counts.items()
        if logical_values != {0, 1}
    ]
    if bad_envs:
        raise RuntimeError(f"{case.label}: environments without both logical bits: {bad_envs}")

    X = build_pair_hop_X(n)
    Z_full = build_sublattice_Z(n, parity)
    z_matches, x_matches, _xi5, _xi_last = bell_lane.taste_identity_check(
        n, case.side, case.dim, Z_full, X
    )
    if not (z_matches and x_matches):
        raise RuntimeError(f"{case.label}: helper KS taste identity check failed")

    x_preserves_env_and_flips_logical = True
    for site in range(n):
        targets = np.flatnonzero(np.abs(X[:, site]) > 1e-12)
        if len(targets) != 1:
            x_preserves_env_and_flips_logical = False
            break
        target = int(targets[0])
        same_env = factors.env[target] == factors.env[site]
        flipped = factors.logical[target] == 1 - factors.logical[site]
        if not (same_env and flipped):
            x_preserves_env_and_flips_logical = False
            break
    if not x_preserves_env_and_flips_logical:
        raise RuntimeError(f"{case.label}: pair-hop X is not logical-last-bit X")

    Z_last = np.diag([1.0 if bit == 0 else -1.0 for bit in factors.logical]).astype(complex)
    I_n = np.eye(n, dtype=complex)
    last_pauli_ok = (
        np.allclose(Z_last @ Z_last, I_n, atol=1e-12)
        and np.allclose(X @ X, I_n, atol=1e-12)
        and np.allclose(Z_last @ X + X @ Z_last, np.zeros_like(X), atol=1e-12)
    )
    if not last_pauli_ok:
        raise RuntimeError(f"{case.label}: last-taste logical Pauli check failed")

    return {
        "case": case.label,
        "n_sites": n,
        "n_env": len(factors.env_labels),
        "logical_axis": case.dim - 1,
        "helper_z_xi5": z_matches,
        "helper_x_xi_last": x_matches,
        "x_is_last_logical_x": x_preserves_env_and_flips_logical,
        "z_last_pauli": last_pauli_ok,
        "sublattice_z_equals_z_last": bool(np.allclose(Z_full, Z_last, atol=1e-12)),
    }


def ground_state_resource(case: AuditCase) -> dict[str, object]:
    n, adj, parity, _coords = lattice_for_case(case)
    H1 = build_H1(n, adj, parity, mass=case.mass)
    V = build_poisson(n, adj)
    H2 = build_H2_tensor(H1, V, case.G, n)
    evals, evecs = eigh(H2)
    psi = evecs[:, 0]

    Z = build_sublattice_Z(n, parity)
    X = build_pair_hop_X(n)
    full_chsh, _T = chsh_horodecki(psi, Z, X, Z, X, n)
    return {
        "n": n,
        "adj": adj,
        "parity": parity,
        "ground_energy": float(evals[0]),
        "psi": psi,
        "full_chsh": float(full_chsh),
    }


def coords_from_index(index: int, dim: int, side: int) -> tuple[int, ...]:
    coords: list[int] = []
    remaining = index
    for power in range(dim - 1, -1, -1):
        stride = side**power
        coord = remaining // stride
        coords.append(coord)
        remaining %= stride
    return tuple(coords)


def factor_sites(dim: int, side: int, logical_axis: int | None = None) -> SiteFactorization:
    if side % 2 != 0:
        raise ValueError("KS taste factorization requires an even side length")
    if logical_axis is None:
        logical_axis = dim - 1
    if logical_axis < 0 or logical_axis >= dim:
        raise ValueError("logical_axis is outside the spatial dimension")

    n = side**dim
    logical = np.zeros(n, dtype=int)
    env_raw: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

    for site in range(n):
        coords = coords_from_index(site, dim, side)
        cell = tuple(coord // 2 for coord in coords)
        eta = tuple(coord % 2 for coord in coords)
        spectator = tuple(bit for axis, bit in enumerate(eta) if axis != logical_axis)
        logical[site] = eta[logical_axis]
        env_raw.append((cell, spectator))

    env_labels = tuple(dict.fromkeys(env_raw))
    env_index = {label: index for index, label in enumerate(env_labels)}
    env = np.array([env_index[label] for label in env_raw], dtype=int)
    return SiteFactorization(logical=logical, env=env, env_labels=env_labels)


def amplitudes_by_logical_env(
    psi: np.ndarray, n_sites: int, factors: SiteFactorization
) -> np.ndarray:
    n_env = len(factors.env_labels)
    amp = np.zeros((2, n_env, 2, n_env), dtype=complex)
    for site_a in range(n_sites):
        logical_a = factors.logical[site_a]
        env_a = factors.env[site_a]
        for site_b in range(n_sites):
            logical_b = factors.logical[site_b]
            env_b = factors.env[site_b]
            amp[logical_a, env_a, logical_b, env_b] = psi[site_a * n_sites + site_b]
    return amp


def reduced_logical_resource(amp: np.ndarray) -> np.ndarray:
    rho = np.einsum("aebf,cedf->abcd", amp, amp.conj(), optimize=True)
    rho = rho.reshape(4, 4)
    trace = np.trace(rho)
    if abs(trace) <= 1e-15:
        raise ValueError("logical resource has zero trace")
    return rho / trace


def bell_state(z_bit: int, x_bit: int) -> np.ndarray:
    sign = -1.0 if z_bit else 1.0
    state = np.zeros(4, dtype=complex)
    if x_bit == 0:
        state[0] = 1.0 / math.sqrt(2.0)
        state[3] = sign / math.sqrt(2.0)
    else:
        state[1] = 1.0 / math.sqrt(2.0)
        state[2] = sign / math.sqrt(2.0)
    return state


def bell_projector(z_bit: int, x_bit: int) -> np.ndarray:
    state = bell_state(z_bit, x_bit)
    return np.outer(state, state.conj())


def bell_overlap_spectrum(rho: np.ndarray) -> tuple[tuple[float, str], ...]:
    overlaps: list[tuple[float, str]] = []
    for z_bit, x_bit in OUTCOME_ORDER:
        state = bell_state(z_bit, x_bit)
        overlap = float(np.real(state.conj() @ rho @ state))
        overlaps.append((overlap, OUTCOME_LABELS[(z_bit, x_bit)]))
    return tuple(overlaps)


def best_bell_overlap(rho: np.ndarray, tolerance: float = 1e-12) -> tuple[float, str]:
    overlaps = bell_overlap_spectrum(rho)
    best = max(overlap for overlap, _label in overlaps)
    for overlap, label in overlaps:
        if abs(overlap - best) <= tolerance:
            return overlap, label
    raise AssertionError("unreachable: Bell-overlap spectrum is empty")


def bell_overlap_ties(rho: np.ndarray, tolerance: float = 1e-12) -> tuple[str, ...]:
    overlaps = bell_overlap_spectrum(rho)
    best = max(overlap for overlap, _label in overlaps)
    return tuple(label for overlap, label in overlaps if abs(overlap - best) <= tolerance)


def two_qubit_chsh(rho: np.ndarray) -> float:
    paulis = (X2, Y2, Z2)
    T = np.zeros((3, 3), dtype=float)
    for i, op_a in enumerate(paulis):
        for j, op_b in enumerate(paulis):
            T[i, j] = float(np.real(np.trace(rho @ np.kron(op_a, op_b))))
    eigvals = sorted(np.linalg.eigvalsh(T.T @ T), reverse=True)
    return float(2.0 * math.sqrt(max(eigvals[0] + eigvals[1], 0.0)))


def negativity(rho: np.ndarray) -> float:
    partial_transpose_b = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    eigvals = np.linalg.eigvalsh(partial_transpose_b)
    return float(sum(abs(value) for value in eigvals if value < 0.0))


def normalize(state: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(state)
    if norm <= 1e-15:
        raise ValueError("cannot normalize a zero vector")
    return state / norm


def random_qubit(rng: np.random.Generator) -> np.ndarray:
    return normalize(rng.standard_normal(2) + 1j * rng.standard_normal(2))


def correction_operator(z_bit: int, x_bit: int) -> np.ndarray:
    z_op = Z2 if z_bit else I2
    x_op = X2 if x_bit else I2
    return z_op @ x_op


def standard_teleportation_stats(
    resource_rho: np.ndarray, trials: int, seed: int
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    fidelities: list[float] = []
    trace_errors: list[float] = []

    for _ in range(trials):
        input_state = random_qubit(rng)
        input_rho = np.outer(input_state, input_state.conj())
        total = np.kron(input_rho, resource_rho).reshape(2, 2, 2, 2, 2, 2)
        output = np.zeros((2, 2), dtype=complex)

        for z_bit, x_bit in OUTCOME_ORDER:
            beta = bell_state(z_bit, x_bit).reshape(2, 2)
            branch = np.einsum("ar,arbcsd,cs->bd", beta.conj(), total, beta)
            correction = correction_operator(z_bit, x_bit)
            output += correction @ branch @ correction.conj().T

        trace_errors.append(abs(float(np.real(np.trace(output))) - 1.0))
        fidelity = float(np.real(input_state.conj() @ output @ input_state))
        fidelities.append(fidelity)

    max_trace_error = float(np.max(trace_errors))
    if max_trace_error <= 1e-12:
        max_trace_error = 0.0
    return {
        "mean": float(np.mean(fidelities)),
        "min": float(np.min(fidelities)),
        "max": float(np.max(fidelities)),
        "max_trace_error": max_trace_error,
    }


def verify_teleportation_convention(seed: int) -> dict[str, float]:
    stats = standard_teleportation_stats(bell_projector(0, 0), trials=16, seed=seed)
    if abs(1.0 - stats["min"]) > 1e-12 or stats["max_trace_error"] > 1e-12:
        raise RuntimeError("standard Bell teleportation convention sanity check failed")
    return stats


def postselected_branch_scan(
    amp: np.ndarray,
    env_labels: Iterable[tuple[tuple[int, ...], tuple[int, ...]]],
    probability_floor: float,
) -> dict[str, object]:
    labels = tuple(env_labels)
    best: dict[str, object] = {
        "bell_fidelity": 0.0,
        "bell_label": "none",
        "probability": 0.0,
        "env_a": None,
        "env_b": None,
        "logical_chsh": 0.0,
        "negativity": 0.0,
    }

    for env_a, label_a in enumerate(labels):
        for env_b, label_b in enumerate(labels):
            branch = amp[:, env_a, :, env_b]
            probability = float(np.real(np.vdot(branch, branch)))
            if probability < probability_floor:
                continue
            branch_state = (branch / math.sqrt(probability)).reshape(4)
            rho = np.outer(branch_state, branch_state.conj())
            fidelity, bell_label = best_bell_overlap(rho)
            if fidelity > float(best["bell_fidelity"]):
                best = {
                    "bell_fidelity": fidelity,
                    "bell_label": bell_label,
                    "probability": probability,
                    "env_a": label_a,
                    "env_b": label_b,
                    "logical_chsh": two_qubit_chsh(rho),
                    "negativity": negativity(rho),
                }
    return best


def audit_case(
    case: AuditCase,
    trials: int,
    seed: int,
    high_fidelity_threshold: float,
    probability_floor: float,
) -> dict[str, object]:
    resource = ground_state_resource(case)
    n_sites = int(resource["n"])
    psi = resource["psi"]
    factors = factor_sites(case.dim, case.side)
    amp = amplitudes_by_logical_env(psi, n_sites, factors)
    rho = reduced_logical_resource(amp)

    bell_fidelity, bell_label = best_bell_overlap(rho)
    teleportation = standard_teleportation_stats(rho, trials=trials, seed=seed)
    postselected = postselected_branch_scan(
        amp,
        factors.env_labels,
        probability_floor=probability_floor,
    )
    logical_bell_ties = bell_overlap_ties(rho)

    purity = float(np.real(np.trace(rho @ rho)))
    logical_chsh = two_qubit_chsh(rho)
    neg = negativity(rho)
    extracted = bool(bell_fidelity >= high_fidelity_threshold)
    return {
        "case": case,
        "n_sites": n_sites,
        "n_env": len(factors.env_labels),
        "ground_energy": resource["ground_energy"],
        "full_chsh": resource["full_chsh"],
        "logical_bell_fidelity": bell_fidelity,
        "logical_bell_label": bell_label,
        "logical_bell_ties": logical_bell_ties,
        "logical_chsh": logical_chsh,
        "purity": purity,
        "negativity": neg,
        "teleportation": teleportation,
        "postselected": postselected,
        "deterministic_high_fidelity_resource": extracted,
    }


def print_result(result: dict[str, object], high_fidelity_threshold: float) -> None:
    case = result["case"]
    assert isinstance(case, AuditCase)
    tel = result["teleportation"]
    post = result["postselected"]
    assert isinstance(tel, dict)
    assert isinstance(post, dict)

    print(f"Case: {case.label}")
    print(
        "  lattice/params: "
        f"dim={case.dim} side={case.side} N={result['n_sites']} "
        f"envs/logical_qubit={result['n_env']} mass={case.mass:g} G={case.G:g}"
    )
    print(f"  ground energy: {result['ground_energy']:.12g}")
    print(f"  full-state CHSH |S| from existing lane: {result['full_chsh']:.6f}")
    print(
        "  traced logical taste-qubit resource: "
        f"best Bell overlap={result['logical_bell_fidelity']:.6f} "
        f"({result['logical_bell_label']}), "
        f"CHSH={result['logical_chsh']:.6f}, "
        f"purity={result['purity']:.6f}, "
        f"negativity={result['negativity']:.6f}"
    )
    ties = result["logical_bell_ties"]
    if isinstance(ties, tuple) and len(ties) > 1:
        print(
            "  traced Bell max-label tie: "
            f"{', '.join(ties)} (deterministic report uses {result['logical_bell_label']})"
        )
    print(
        "  standard teleportation with traced resource: "
        f"mean fidelity={tel['mean']:.6f}, min={tel['min']:.6f}, "
        f"max={tel['max']:.6f}, max trace error={tel['max_trace_error']:.3e}"
    )
    print(
        "  best fixed-env postselected branch: "
        f"Bell overlap={post['bell_fidelity']:.6f} ({post['bell_label']}), "
        f"probability={post['probability']:.6e}, "
        f"CHSH={post['logical_chsh']:.6f}, negativity={post['negativity']:.6f}"
    )
    print(f"    env A={post['env_a']} env B={post['env_b']}")
    status = "YES" if result["deterministic_high_fidelity_resource"] else "NO"
    print(
        "  deterministic high-fidelity Bell resource "
        f"(threshold {high_fidelity_threshold:.3f}): {status}"
    )
    print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=128, help="random teleportation inputs")
    parser.add_argument("--seed", type=int, default=20260425, help="random seed")
    parser.add_argument(
        "--high-fidelity-threshold",
        type=float,
        default=0.90,
        help="Bell-overlap threshold for calling the traced resource high fidelity",
    )
    parser.add_argument(
        "--probability-floor",
        type=float,
        default=1e-12,
        help="ignore postselected branches below this probability",
    )
    parser.add_argument(
        "--case",
        choices=[case.label for case in DEFAULT_CASES],
        action="append",
        help="case label to run; omit to run the default audit set",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.trials <= 0:
        raise ValueError("--trials must be positive")
    if not (0.0 < args.high_fidelity_threshold <= 1.0):
        raise ValueError("--high-fidelity-threshold must be in (0, 1]")
    if args.probability_floor < 0.0:
        raise ValueError("--probability-floor must be nonnegative")

    requested = set(args.case or [])
    cases = [case for case in DEFAULT_CASES if not requested or case.label in requested]

    # 2026-06-20 source-side repair: per-check PASS:/FAIL: discipline for
    # the BOUNDED FINITE EXTRACTION CORE (the citeable core), with a final
    # TOTAL/SUMMARY. The native preparation/readout/apparatus bridge is NOT part
    # of the citeable core; its consistency report is segregated below and
    # does NOT contribute to the core PASS/FAIL summary.
    core_pass = 0
    core_fail = 0

    def core_check(name: str, ok: bool, detail: str = "") -> None:
        nonlocal core_pass, core_fail
        tag = "PASS" if ok else "FAIL"
        if ok:
            core_pass += 1
        else:
            core_fail += 1
        suffix = f" {detail}" if detail else ""
        print(f"{tag}: {name}{suffix}")

    print("POISSON/CHSH TELEPORTATION RESOURCE AUDIT")
    print("Status: bounded finite extraction core (citeable); open gate for the native")
    print("        preparation/readout/apparatus bridge (open, not supplied here)")
    print("Extraction: trace cells/spectator tastes, keep the last KS taste bit per species")
    print()
    print("=== BOUNDED FINITE EXTRACTION CORE (citeable core) ===")

    helper = helper_source_certificate()
    helper_path = Path(helper["path"])
    try:
        helper_label = helper_path.relative_to(SCRIPT_DIR.parent)
    except ValueError:
        helper_label = helper_path
    core_check(
        "poisson_chsh_helper_source",
        True,
        f"{helper_label} sha256={helper['sha256']} "
        f"lines={helper['line_count']} required_symbols={helper['symbol_count']}",
    )

    rala = retained_axis_source_certificate()
    rala_path = Path(rala["path"])
    try:
        rala_label = rala_path.relative_to(SCRIPT_DIR.parent)
    except ValueError:
        rala_label = rala_path
    core_check(
        "retained_axis_finite_operator_algebra",
        True,
        f"{rala_label} ledger={rala['status']} "
        f"required_theorem_snippets={rala['snippet_count']}",
    )

    for certificate in (logical_carrier_certificate(case) for case in cases):
        z_scope = (
            "sublattice Z is last-bit Z"
            if certificate["sublattice_z_equals_z_last"]
            else "sublattice Z is xi5; last-bit Z is separate"
        )
        core_check(
            f"last_taste_carrier[{certificate['case']}]",
            bool(certificate["x_is_last_logical_x"] and certificate["z_last_pauli"]),
            f"envs={certificate['n_env']} logical_axis={certificate['logical_axis']} "
            f"X=xi_last/logical-flip; Z_last Pauli; {z_scope}",
        )

    sanity = verify_teleportation_convention(args.seed - 1)
    core_check(
        "teleportation_convention_sanity",
        abs(1.0 - sanity["min"]) <= 1e-12 and sanity["max_trace_error"] <= 1e-12,
        f"ideal Phi+ mean fidelity={sanity['mean']:.16f} min={sanity['min']:.16f} "
        f"max trace error={sanity['max_trace_error']:.3e}",
    )
    print()

    results = [
        audit_case(
            case,
            trials=args.trials,
            seed=args.seed + index,
            high_fidelity_threshold=args.high_fidelity_threshold,
            probability_floor=args.probability_floor,
        )
        for index, case in enumerate(cases)
    ]

    for result in results:
        print_result(result, high_fidelity_threshold=args.high_fidelity_threshold)

    # Bounded finite-extraction core acceptance: the null G=0 control must NOT
    # yield a high-fidelity logical resource, and every Poisson/CHSH case must.
    for result in results:
        case = result["case"]
        assert isinstance(case, AuditCase)
        extracted = bool(result["deterministic_high_fidelity_resource"])
        if case.G == 0.0:
            core_check(
                f"null_control_no_resource[{case.label}]",
                not extracted,
                f"best Bell overlap={result['logical_bell_fidelity']:.6f} "
                f"negativity={result['negativity']:.6f}",
            )
        else:
            core_check(
                f"poisson_extraction_high_fidelity[{case.label}]",
                extracted,
                f"best Bell overlap={result['logical_bell_fidelity']:.6f} "
                f"({result['logical_bell_label']}) "
                f"tel mean={result['teleportation']['mean']:.6f}",
            )

    print()
    print(f"TOTAL: PASS={core_pass} FAIL={core_fail}")
    print(f"SUMMARY PASS={core_pass} FAIL={core_fail}")
    print()

    # === SEGREGATED: native preparation/readout/apparatus bridge ===
    # This block is NOT part of the citeable bounded extraction core. The check
    # below only confirms that the note keeps the native preparation/readout and
    # apparatus bridge open and not supplied here; it asserts no apparatus,
    # preparation, or readout theorem and does NOT contribute to the TOTAL/SUMMARY
    # above.
    print(
        "=== OPEN BRIDGE (native preparation/readout/apparatus; "
        "NOT part of citeable core) ==="
    )
    firewall = source_status_firewall_certificate()
    print(
        "INFO: open_bridge_firewall "
        f"{Path(firewall['path']).relative_to(ROOT)} "
        "note keeps native preparation/readout/apparatus bridge explicitly open "
        f"(not supplied here); required_snippets={firewall['snippet_count']}"
    )
    print()

    poisson_results = [
        result
        for result in results
        if isinstance(result["case"], AuditCase) and result["case"].G != 0.0
    ]
    moved = any(result["deterministic_high_fidelity_resource"] for result in poisson_results)
    print("Conclusion:")
    if moved:
        print(
            "  A traced deterministic high-fidelity Bell resource was found on at least "
            "one Poisson case. This is the bounded finite extraction core only."
        )
    else:
        print(
            "  Limitation remains open: the audited Poisson/CHSH ground states do not yet "
            "provide a deterministic high-fidelity encoded Bell pair."
        )
    print(
        "  CHSH violation in the full C^N x C^N state is not by itself a teleportation "
        "resource derivation."
    )
    print("  Postselected branches, when present, are diagnostics only in this artifact.")
    print(
        "  The native preparation/readout/apparatus bridge is open and is NOT part "
        "of the citeable bounded extraction core."
    )
    return 0 if core_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
