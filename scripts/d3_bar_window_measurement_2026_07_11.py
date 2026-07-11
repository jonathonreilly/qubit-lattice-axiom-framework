#!/usr/bin/env python3
"""Execute the supervisor-frozen d=3 route-C bar-window protocol delta.

``D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md`` is the frozen protocol;
``D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md`` is its inherited parent.

Modes are ``--validate`` (default), ``--full``, and ``--report``.  The
claim-bearing mode is intentionally guarded by live ``k=4``, ``k=5``, and
``q=9,10,11`` cube gathers before any trace can start.  ``--report`` reads
only completed streams/checkpoints and never evolves or reconstructs an
observable.

SPEC-NOTE (frozen bar-window memo, inherited bar-location parent): this runner uses the trajectory's
verified ``t=0`` row for every dynamical excess, ends the dt-halving grid at
``Jt=1.10``, and samples pairs only on the frozen route-C subgrid.  The mixed
ground doublet is a stationary control and diagnostic only; it is never a
gate baseline.  These memo rules intentionally supersede the older pilot
runner conventions.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.

No formation rule.

Sets no audit status.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
from typing import Any, Callable, Iterable, Mapping, Sequence

import numpy as np
import numpy.typing as npt


_OLD_DONT_WRITE_BYTECODE = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    import d3_cubic_orbit_engine_2026_07_09 as orbit_engine
    import d3_bar_location_engine_ext_2026_07_10 as engine_ext
finally:
    sys.dont_write_bytecode = _OLD_DONT_WRITE_BYTECODE


LAMBDAS = (0.02, 0.05, 0.10, 0.20)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DELTA_KEYS = {delta: f"{delta:.2f}" for delta in DELTAS}
DT = 0.10
N_STEPS = 100
T_FINAL = 10.0
FINE_LAM = 0.10
FINE_DT = 0.05
FINE_N_STEPS = 22
FINE_T_FINAL = 1.10
HEADLINE_TIME = 1.0
PAIR_MAIN_STEPS = frozenset((*range(0, 13), 15, 20, 50, 100))
PAIR_MAIN_TIMES = tuple(step * DT for step in sorted(PAIR_MAIN_STEPS))

H_FLOOR = 0.05
EPS_EXCESS = 0.02
ETA_INDEPENDENCE = 0.02
MIN_REDUNDANCY = 2
PERSISTENCE_SAMPLES = 3
POINTER_DRIFT_LIMIT = 0.10
BAR_WINDOW_FLOOR = 0.20
DELTA_FACTOR_LIMIT = 1.5
DT_ONSET_SHIFT_TOL = 0.10
DT_THETA_RELATIVE_TOL = 0.05
NUMERIC_GATE_TOL = 1.0e-10
MACHINERY_TOL = 1.0e-9
GROUND_RESIDUAL_TOL = 1.0e-8
VALIDATION_RSS_GB = 4.0
PREFLIGHT_RSS_GB = 8.0
FULL_RSS_GB = 10.0
VALIDATION_WALL_SECONDS = 30.0 * 60.0
PREFLIGHT_WALL_SECONDS = 13.5 * 3600.0
FULL_WALL_SECONDS = 14.0 * 3600.0
FROZEN_WEIGHTED_UNITS = 2785.0
PILOT_UNIT_SECONDS = 8.28
FROZEN_RESERVE_SECONDS = 0.70 * 3600.0

STREAM_SCHEMA = "d3-bar-window-observable-v1"
CHECKPOINT_SCHEMA = "d3-bar-window-checkpoint-v1"
GROUND_SCHEMA = "d3-bar-window-ground-doublet-v1"
REPORT_SCHEMA = "d3-bar-location-report-v1"
PREFLIGHT_SCHEMA = "d3-bar-window-preflight-v1"

BOUNDARY_SENTENCES = (
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
)
BOUNDARY_TEXT = " ".join(BOUNDARY_SENTENCES)
SPEC_NOTE = (
    "SPEC-NOTE frozen-protocol=D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md; "
    "inherited-parent=D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md. "
    "SPEC-NOTE frozen-memo-wins: excess=chi(t)-chi(t=0); the ground doublet "
    "is stationary-control-plus-diagnostic-only; fine-grid=0:0.05:1.10; "
    "missing off-subgrid pair data is never independence. SPEC-NOTE validation-RSS: "
    "two-state k=2 Lanczos uses ncv=5 with the frozen tolerance/maxiter/residual gates. "
    "SPEC-NOTE zero-weight-X: the exact t=0 X-minus block has p=0; I/d is a marked "
    "diagnostic placeholder with zero weight in every scalar and gate."
)

PREPARATION_BLOCH_VECTORS: Mapping[str, tuple[float, float, float]] = {
    "center": (1.0, 0.0, 0.0),
    "face": (1.0, 0.0, 0.0),
    "edge": (0.0, 0.0, 1.0),
    "corner": (0.0, 0.0, 1.0),
}

REPO_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = REPO_ROOT / "docs" / "D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
PARENT_PROTOCOL_PATH = REPO_ROOT / "docs" / "D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
RUN_DIR = REPO_ROOT / "logs" / "runner-cache" / "d3_bar_window_checkpoints"
REPORT_CACHE_PATH = RUN_DIR / "bar_location_report.json"
PREFLIGHT_CACHE_PATH = RUN_DIR / "cube_gather_preflight.json"

PAULI_X = np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
PAULI_Y = np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
PAULI_Z = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)

PAIR_REPRESENTATIVES: Mapping[str, tuple[str, str]] = {
    "opposite-55": ("+x", "-x"),
    "opposite-44": ("+y", "-y"),
    "plus-x-orthogonal": ("+x", "+y"),
    "minus-x-orthogonal": ("-x", "+y"),
    "transverse-orthogonal": ("+y", "+z"),
}
FRAGMENT_REPRESENTATIVES: Mapping[str, str] = {
    "closed-five": "+x",
    "wedge-four": "+y",
}


class SigtermRequested(RuntimeError):
    """Internal clean stop after the latest complete state/row is saved."""


@dataclass(frozen=True)
class RunIdentity:
    protocol_hash: str
    parent_protocol_hash: str
    fragment_descriptor_checksum: str
    boundary_sentences: tuple[str, str, str]


@dataclass
class SignalCheckpointContext:
    save_now: Callable[[str], None]
    requested: bool = False
    saving: bool = False
    error: str | None = None


_SIGNAL_CONTEXT: SignalCheckpointContext | None = None
_SIGTERM_PENDING = False


def _identity() -> RunIdentity:
    frozen_bytes = PROTOCOL_PATH.read_bytes()
    try:
        frozen_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError("frozen protocol memo is not valid UTF-8") from exc
    parent_bytes = PARENT_PROTOCOL_PATH.read_bytes()
    try:
        parent_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError("inherited parent protocol memo is not valid UTF-8") from exc
    descriptors = engine_ext.verify_fragment_descriptors()
    return RunIdentity(
        protocol_hash=hashlib.sha256(frozen_bytes).hexdigest(),
        parent_protocol_hash=hashlib.sha256(parent_bytes).hexdigest(),
        fragment_descriptor_checksum=descriptors.checksum,
        boundary_sentences=BOUNDARY_SENTENCES,
    )


def _require_engine_api() -> None:
    engine_names = (
        "build_orbit_basis",
        "build_hamiltonian_tables",
        "hamiltonian_apply",
        "evolve",
        "center_bond_state",
        "rss_gb",
        "density_matrix_diagnostics",
        "dense_slab_crosscheck",
    )
    extension_names = (
        "class_product_state",
        "get_raw_to_orbit_lookup",
        "conditional_fragment_marginal",
        "fragment_pair_marginal",
        "partial_trace_density",
        "two_lowest_states",
        "dense_slab_extension_crosscheck",
        "verify_fragment_descriptors",
    )
    missing = [name for name in engine_names if not hasattr(orbit_engine, name)]
    missing += [
        f"ext.{name}" for name in extension_names if not hasattr(engine_ext, name)
    ]
    if missing:
        raise RuntimeError("commissioned engine API missing: " + ",".join(missing))


def _guard_rss(label: str, budget_gb: float) -> None:
    orbit_engine._guard_rss(f"d3 bar location {label}", budget_gb)


def _lam_token(lam: float) -> str:
    return f"{lam:.2f}".replace(".", "p")


def _trace_prefix(lam: float, *, fine: bool) -> str:
    return (
        f"dt_half_lam_{_lam_token(lam)}" if fine else f"lam_{_lam_token(lam)}"
    )


def _stream_path(lam: float, *, fine: bool) -> Path:
    return RUN_DIR / f"{_trace_prefix(lam, fine=fine)}_observables.jsonl"


def _checkpoint_path(prefix: str, step: int) -> Path:
    return RUN_DIR / f"{prefix}_step_{step:03d}.npz"


def _ground_path(lam: float) -> Path:
    return RUN_DIR / f"ground_doublet_3x3x3_lam_{_lam_token(lam)}.npz"


def _json_dumps(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _atomic_savez(path: Path, **arrays: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.stem}.{os.getpid()}.tmp.npz")
    try:
        np.savez(temporary, **arrays)
        with temporary.open("rb") as handle:
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _atomic_write_json(path: Path, payload: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        encoded = (_json_dumps(dict(payload)) + "\n").encode("utf-8")
        descriptor = os.open(
            temporary, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644
        )
        try:
            written = os.write(descriptor, encoded)
            if written != len(encoded):
                raise OSError(f"short JSON write {written}/{len(encoded)}")
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _append_jsonl(path: Path, row: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (_json_dumps(dict(row)) + "\n").encode("utf-8")
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o644)
    try:
        written = os.write(descriptor, payload)
        if written != len(payload):
            raise OSError(f"short JSONL append {written}/{len(payload)}")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _state_checksum(state: npt.NDArray[np.complex128]) -> str:
    array = np.ascontiguousarray(np.asarray(state, dtype=np.complex128))
    digest = hashlib.sha256()
    digest.update(array.dtype.str.encode("ascii"))
    digest.update(np.asarray(array.shape, dtype=np.int64).tobytes())
    digest.update(memoryview(array).cast("B"))
    return digest.hexdigest()


def _preparation_amplitudes() -> dict[str, tuple[complex, complex]]:
    return {
        name: engine_ext.qubit_amplitudes_from_bloch(vector)
        for name, vector in PREPARATION_BLOCH_VECTORS.items()
    }


def _preparation_json() -> dict[str, list[float]]:
    return {
        name: [float(component) for component in vector]
        for name, vector in PREPARATION_BLOCH_VECTORS.items()
    }


def _fmt(value: float | int | None) -> str:
    if value is None:
        return "unavailable"
    number = float(value)
    if not np.isfinite(number):
        return "unavailable"
    return f"{number:.6g}"


def _fmt_vector(values: Iterable[float | int | None]) -> str:
    return "[" + ",".join(_fmt(value) for value in values) + "]"


def _with_boundaries(line: str) -> str:
    if "\n" in line:
        raise AssertionError("stdout record is not single-line")
    return f"{line} {BOUNDARY_TEXT}"


def _binary_entropy(probabilities: Sequence[float]) -> float:
    values = tuple(float(value) for value in probabilities)
    if (
        len(values) != 2
        or any(not np.isfinite(value) or value < -1.0e-12 for value in values)
        or abs(sum(values) - 1.0) > MACHINERY_TOL
    ):
        raise AssertionError(f"invalid binary probabilities {values}")
    return float(-sum(value * math.log2(value) for value in values if value > 0.0))


def _density_entropy(matrix: npt.NDArray[np.complex128]) -> float:
    return engine_ext.density_summary(matrix).entropy_bits


def _holevo_from_states(
    probabilities: Sequence[float],
    states: Sequence[npt.NDArray[np.complex128]],
) -> float:
    p = tuple(float(value) for value in probabilities)
    average = p[0] * np.asarray(states[0]) + p[1] * np.asarray(states[1])
    value = _density_entropy(average) - sum(
        p[index] * _density_entropy(np.asarray(states[index])) for index in range(2)
    )
    entropy = _binary_entropy(p)
    if value < -MACHINERY_TOL or value > entropy + MACHINERY_TOL:
        raise AssertionError(f"Holevo value {value:.16g} outside [0,H]")
    return float(value)


def _singleton_gate(entropy: float, chi: float, excess: float, delta: float) -> bool:
    return bool(
        entropy >= H_FLOOR
        and chi + NUMERIC_GATE_TOL >= (1.0 - delta) * entropy
        and excess + NUMERIC_GATE_TOL >= EPS_EXCESS
    )


def _partial_one_site(
    states: Sequence[npt.NDArray[np.complex128]],
    n_qubits: int,
    factor: int,
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    return (
        engine_ext.partial_trace_density(states[0], n_qubits, (factor,)),
        engine_ext.partial_trace_density(states[1], n_qubits, (factor,)),
    )


def _max_matrix_disagreement(
    ensembles: Sequence[tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]]
) -> float:
    if not ensembles:
        return 0.0
    reference = ensembles[0]
    return max(
        (
            float(np.max(np.abs(candidate[outcome] - reference[outcome])))
            for candidate in ensembles[1:]
            for outcome in range(2)
        ),
        default=0.0,
    )


def _mean_ensemble(
    ensembles: Sequence[tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]]
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    if not ensembles:
        raise ValueError("cannot average an empty density ensemble")
    return (
        np.mean(np.stack([ensemble[0] for ensemble in ensembles]), axis=0),
        np.mean(np.stack([ensemble[1] for ensemble in ensembles]), axis=0),
    )


def _bloch_from_ensemble(
    probabilities: Sequence[float],
    states: Sequence[npt.NDArray[np.complex128]],
) -> dict[str, float]:
    rho = float(probabilities[0]) * states[0] + float(probabilities[1]) * states[1]
    result: dict[str, float] = {}
    for name, pauli in (("x", PAULI_X), ("y", PAULI_Y), ("z", PAULI_Z)):
        value = complex(np.trace(rho @ pauli))
        if abs(value.imag) > MACHINERY_TOL:
            raise AssertionError(f"Bloch {name} has imaginary part {value.imag:.3e}")
        result[name] = float(value.real)
    return result


def _summary_dict(summary: engine_ext.DensitySummary) -> dict[str, object]:
    return summary.as_dict()


def _summary_errors(summaries: Iterable[engine_ext.DensitySummary]) -> dict[str, float]:
    values = tuple(summaries)
    if not values:
        return {"hermiticity": 0.0, "trace": 0.0, "negativity": 0.0}
    return {
        "hermiticity": max(value.hermiticity_error for value in values),
        "trace": max(abs(value.trace_real - 1.0) + abs(value.trace_imag) for value in values),
        "negativity": max(max(0.0, -value.minimum_eigenvalue) for value in values),
    }


def _fragment_type_for_label(label: str) -> str:
    return "closed-five" if label in ("+x", "-x") else "wedge-four"


def _normalized_pair(left: str, right: str) -> tuple[str, str]:
    return tuple(
        sorted((left, right), key=engine_ext.FRAGMENT_LABEL_ORDER.index)
    )  # type: ignore[return-value]


def _pair_key(left: str, right: str) -> str:
    normalized = _normalized_pair(left, right)
    return f"{normalized[0]}|{normalized[1]}"


def _pair_class_lookup() -> dict[tuple[str, str], str]:
    result: dict[tuple[str, str], str] = {}
    for class_name, members in engine_ext.PAIR_CLASS_MEMBERS.items():
        for left, right in members:
            normalized = _normalized_pair(left, right)
            if normalized in result:
                raise AssertionError(f"duplicate physical pair mapping {normalized}")
            result[normalized] = class_name
    expected = set(itertools.combinations(engine_ext.FRAGMENT_LABEL_ORDER, 2))
    if set(result) != expected:
        raise AssertionError("pair-class lookup does not populate all 15 graph edges")
    return result


PAIR_CLASS_LOOKUP = _pair_class_lookup()


def _largest_independent_subset(
    certifies: Mapping[str, bool], pair_information: Mapping[str, float]
) -> tuple[int, tuple[str, ...]]:
    names = tuple(
        label
        for label in engine_ext.FRAGMENT_LABEL_ORDER
        if bool(certifies.get(label, False))
    )
    for size in range(len(names), 0, -1):
        for subset in itertools.combinations(names, size):
            if all(
                float(pair_information[_pair_key(left, right)])
                <= ETA_INDEPENDENCE + NUMERIC_GATE_TOL
                for left, right in itertools.combinations(subset, 2)
            ):
                return size, tuple(subset)
    return 0, ()


def _fragment_panel(
    *,
    basis: Any,
    lookup: engine_ext.RawOrbitLookup,
    states: Sequence[npt.NDArray[np.complex128]],
    weights: Sequence[float] | None,
    pointer_basis: str,
    budget_gb: float,
) -> dict[str, object]:
    """Measure two coarse classes and all redundant one-site reductions."""

    marginals: dict[str, engine_ext.ConditionalMarginal] = {}
    class_chi: dict[str, float] = {}
    summaries: list[engine_ext.DensitySummary] = []
    for class_name in engine_ext.FRAGMENT_CLASS_ORDER:
        label = FRAGMENT_REPRESENTATIVES[class_name]
        marginal = engine_ext.conditional_fragment_marginal(
            basis,
            lookup,
            states,
            engine_ext.fragment_sites(basis, label),
            pointer_basis=pointer_basis,
            weights=weights,
            budget_gb=budget_gb,
        )
        marginals[class_name] = marginal
        class_chi[class_name] = engine_ext.holevo_bits(marginal)
        summaries.extend(marginal.state_summaries)
    probabilities = marginals["closed-five"].probabilities
    probability_disagreement = max(
        abs(
            probabilities[index]
            - marginals["wedge-four"].probabilities[index]
        )
        for index in range(2)
    )

    closed = marginals["closed-five"]
    wedge = marginals["wedge-four"]
    closed_face = _partial_one_site(closed.states, 5, 0)
    wedge_face = _partial_one_site(wedge.states, 4, 0)
    closed_edges = [_partial_one_site(closed.states, 5, factor) for factor in range(1, 5)]
    wedge_edge = _partial_one_site(wedge.states, 4, 1)
    wedge_corners = [_partial_one_site(wedge.states, 4, factor) for factor in (2, 3)]
    face_sources = (closed_face, wedge_face)
    edge_sources = tuple(closed_edges) + (wedge_edge,)
    corner_sources = tuple(wedge_corners)
    face_disagreement = _max_matrix_disagreement(face_sources)
    edge_disagreement = _max_matrix_disagreement(edge_sources)
    corner_disagreement = _max_matrix_disagreement(corner_sources)
    symmetry_error = max(
        probability_disagreement,
        face_disagreement,
        edge_disagreement,
        corner_disagreement,
    )
    if max(face_disagreement, edge_disagreement) > MACHINERY_TOL:
        raise AssertionError(
            "cubic class agreement failed: "
            f"face={face_disagreement:.3e}, edge={edge_disagreement:.3e}"
        )
    face_states = _mean_ensemble(face_sources)
    edge_states = _mean_ensemble(edge_sources)
    corner_states = _mean_ensemble(corner_sources)
    site_states = {
        "face": face_states,
        "edge": edge_states,
        "corner": corner_states,
    }
    site_chi = {
        name: _holevo_from_states(probabilities, ensemble)
        for name, ensemble in site_states.items()
    }
    site_summaries: dict[str, tuple[engine_ext.DensitySummary, engine_ext.DensitySummary]] = {}
    for name, ensemble in site_states.items():
        local = (
            engine_ext.density_summary(ensemble[0], label=f"{name} conditional +"),
            engine_ext.density_summary(ensemble[1], label=f"{name} conditional -"),
        )
        site_summaries[name] = local
        summaries.extend(local)
    capacity_gain = {
        "closed-five": class_chi["closed-five"]
        - max(site_chi["face"], site_chi["edge"]),
        "wedge-four": class_chi["wedge-four"]
        - max(site_chi["face"], site_chi["edge"], site_chi["corner"]),
    }
    serialized_types: dict[str, dict[str, object]] = {}
    for class_name, marginal in marginals.items():
        roles = ("face", "edge") if class_name == "closed-five" else (
            "face",
            "edge",
            "corner",
        )
        serialized_types[class_name] = {
            "representative_fragment": FRAGMENT_REPRESENTATIVES[class_name],
            "pointer_basis": pointer_basis.upper(),
            "probabilities": list(marginal.probabilities),
            "zero_probability_outcomes": list(marginal.zero_probability_outcomes),
            "chi_bits": class_chi[class_name],
            "conditional_density": [
                _summary_dict(summary) for summary in marginal.state_summaries
            ],
            "dephased_joint_density": _summary_dict(marginal.joint_summary),
            "removed_pointer_coherence": marginal.removed_pointer_coherence,
            "one_site_reductions": {
                role: {
                    "chi_bits": site_chi[role],
                    "conditional_density": [
                        _summary_dict(summary) for summary in site_summaries[role]
                    ],
                }
                for role in roles
            },
            "capacity_gain_bits": capacity_gain[class_name],
        }
    return {
        "probabilities": probabilities,
        "entropy_bits": _binary_entropy(probabilities),
        "class_chi": class_chi,
        "site_chi": site_chi,
        "site_states": site_states,
        "serialized_types": serialized_types,
        "capacity_gain": capacity_gain,
        "symmetry": {
            "probabilities": probability_disagreement,
            "face_closed_five_vs_wedge_four": face_disagreement,
            "edge_reductions": edge_disagreement,
            "corner_reductions": corner_disagreement,
            "maximum": symmetry_error,
        },
        "density_errors": _summary_errors(summaries),
    }


def _pair_panel(
    *,
    basis: Any,
    lookup: engine_ext.RawOrbitLookup,
    states: Sequence[npt.NDArray[np.complex128]],
    weights: Sequence[float] | None,
    pointer_basis: str,
    reference_probabilities: Sequence[float],
    budget_gb: float,
) -> dict[str, object]:
    """Measure five pair types sequentially and populate all 15 edges."""

    type_values: dict[str, float] = {}
    serialized_types: dict[str, dict[str, object]] = {}
    probability_error = 0.0
    density_errors = {"hermiticity": 0.0, "trace": 0.0, "negativity": 0.0}
    for class_name in engine_ext.PAIR_CLASS_ORDER:
        left, right = PAIR_REPRESENTATIVES[class_name]
        pair = engine_ext.fragment_pair_marginal(
            basis,
            lookup,
            states,
            engine_ext.fragment_sites(basis, left),
            engine_ext.fragment_sites(basis, right),
            pointer_basis=pointer_basis,
            weights=weights,
            budget_gb=budget_gb,
        )
        probability_error = max(
            probability_error,
            max(
                abs(pair.conditional.probabilities[index] - float(reference_probabilities[index]))
                for index in range(2)
            ),
        )
        cmi = float(pair.conditional_mi_bits)
        joint_holevo = float(engine_ext.holevo_bits(pair.conditional))
        type_values[class_name] = cmi
        local_summaries = (
            *pair.conditional.state_summaries,
            *pair.fragment_a_summaries,
            *pair.fragment_b_summaries,
        )
        local_errors = _summary_errors(local_summaries)
        for name in density_errors:
            density_errors[name] = max(density_errors[name], local_errors[name])
        serialized_types[class_name] = {
            "representative_pair": [left, right],
            "joint_qubits": 1
            + len(engine_ext.FRAGMENT_COORDINATES[left])
            + len(engine_ext.FRAGMENT_COORDINATES[right]),
            "tensor_order": ["S", left, right],
            "pointer_basis": pointer_basis.upper(),
            "probabilities": list(pair.conditional.probabilities),
            "zero_probability_outcomes": list(
                pair.conditional.zero_probability_outcomes
            ),
            "conditional_mi_bits": cmi,
            "joint_holevo_bits": joint_holevo,
            "dephased_joint_density": _summary_dict(pair.conditional.joint_summary),
            "conditional_pair_density": [
                _summary_dict(summary) for summary in pair.conditional.state_summaries
            ],
            "fragment_a_density": [
                _summary_dict(summary) for summary in pair.fragment_a_summaries
            ],
            "fragment_b_density": [
                _summary_dict(summary) for summary in pair.fragment_b_summaries
            ],
        }
        del pair
        _guard_rss(f"pair panel {pointer_basis}/{class_name}", budget_gb)
    if probability_error > MACHINERY_TOL:
        raise AssertionError(
            f"pair pointer probabilities disagree by {probability_error:.3e}"
        )
    physical: dict[str, float] = {}
    mappings: dict[str, str] = {}
    for left, right in itertools.combinations(engine_ext.FRAGMENT_LABEL_ORDER, 2):
        class_name = PAIR_CLASS_LOOKUP[_normalized_pair(left, right)]
        key = _pair_key(left, right)
        physical[key] = type_values[class_name]
        mappings[key] = class_name
    return {
        "type_values": type_values,
        "serialized_types": serialized_types,
        "physical_values": physical,
        "physical_mappings": mappings,
        "probability_error": probability_error,
        "density_errors": density_errors,
    }


def _bond_observation(
    basis: Any, rho: npt.NDArray[np.complex128]
) -> dict[str, object]:
    matrix = np.asarray(rho, dtype=np.complex128)
    summary = engine_ext.density_summary(matrix, label="center bond")
    purity_complex = complex(np.trace(matrix @ matrix))
    if abs(purity_complex.imag) > MACHINERY_TOL:
        raise AssertionError("center-bond purity has an imaginary component")
    purity = float(purity_complex.real)
    if purity < -MACHINERY_TOL or purity > 1.0 + MACHINERY_TOL:
        raise AssertionError(f"center-bond purity {purity:.16g} outside [0,1]")
    observables: dict[str, float] = {}
    pauli_i = np.eye(2, dtype=np.complex128)
    for name, operator in (
        ("zz", np.kron(PAULI_Z, PAULI_Z)),
        ("x_pointer", np.kron(PAULI_X, pauli_i)),
        ("x_face", np.kron(pauli_i, PAULI_X)),
    ):
        value = complex(np.trace(matrix @ operator))
        if abs(value.imag) > MACHINERY_TOL:
            raise AssertionError(f"center-bond {name} is not real")
        observables[name] = float(value.real)
    return {
        "purity": purity,
        "one_minus_purity": 1.0 - purity,
        "density": _summary_dict(summary),
        **observables,
    }


def _mixed_center_bond(
    states: Sequence[npt.NDArray[np.complex128]],
    weights: Sequence[float],
) -> npt.NDArray[np.complex128]:
    if len(states) != len(weights):
        raise ValueError("center-bond mixture states/weights differ in length")
    matrix = np.zeros((4, 4), dtype=np.complex128)
    for state, weight in zip(states, weights, strict=True):
        matrix += float(weight) * orbit_engine.center_bond_state(state)
    return matrix


def _demolition_table(basis: Any, lam: float) -> dict[str, object]:
    """Exact centered-Frobenius commutator panel from Pauli orthogonality."""

    dimension = float(1 << int(basis.n_sites))
    h_weight = float(len(basis.bonds)) + basis.n_sites * float(lam) ** 2
    common = math.sqrt(dimension) * math.sqrt(h_weight)
    degrees = np.zeros(basis.n_sites, dtype=np.int16)
    for left, right in np.asarray(basis.bonds, dtype=np.int16):
        degrees[int(left)] += 1
        degrees[int(right)] += 1
    class_sites: dict[str, list[int]] = {
        "center": [],
        "face": [],
        "edge": [],
        "corner": [],
    }
    for site, coordinate in enumerate(basis.coordinates):
        nonzero = sum(int(component) != 0 for component in coordinate)
        class_sites[("center", "face", "edge", "corner")[nonzero]].append(site)
    classes: dict[str, dict[str, float]] = {}
    z_values: list[float] = []
    x_values: list[float] = []
    for class_name, sites in class_sites.items():
        local_degrees = {int(degrees[site]) for site in sites}
        if len(local_degrees) != 1:
            raise AssertionError(f"demolition class {class_name} mixes degrees")
        degree = local_degrees.pop()
        z_value = 2.0 * abs(float(lam)) / common
        x_value = 2.0 * math.sqrt(float(degree)) / common
        y_value = 2.0 * math.sqrt(float(degree) + float(lam) ** 2) / common
        classes[class_name] = {
            "degree": float(degree),
            "Z": z_value,
            "X": x_value,
            "Y": y_value,
        }
        z_values.append(z_value)
        x_values.append(x_value)
    return {
        "normalization": "||[H,O]||F/(||H||F*||O-Tr(O)I/d||F)",
        "classes": classes,
        "max_z": max(z_values),
        "min_x": min(x_values),
        "gate": bool(max(z_values) < min(x_values)),
    }


def _stationary_control_counts(
    *,
    fragment_chi: Mapping[str, float],
    entropy: float,
    pair_information: Mapping[str, float],
) -> list[int]:
    """Feed three identical mixed-doublet rows through the event graph gate."""

    r_ind: dict[str, int] = {}
    subsets: dict[str, list[str]] = {}
    for delta in DELTAS:
        key = DELTA_KEYS[delta]
        # Its own first row is the anchor, so every excess is algebraically
        # zero on all three repeated samples.  This is the identical
        # singleton/graph routine, not a special event override.
        certifies = {
            label: _singleton_gate(
                entropy,
                float(fragment_chi[_fragment_type_for_label(label)]),
                0.0,
                delta,
            )
            for label in engine_ext.FRAGMENT_LABEL_ORDER
        }
        redundancy, _ = _largest_independent_subset(certifies, pair_information)
        r_ind[key] = redundancy
        subsets[key] = []
    repeated_rows = [
        {
            "pair_subgrid": True,
            "r_ind": dict(r_ind),
            "certifying_subsets": dict(subsets),
            "pair_conditional_mi_bits": {
                "physical": dict(pair_information)
            },
            "step": step,
            "jt": step * DT,
        }
        for step in range(3)
    ]
    return [
        int(_first_event(repeated_rows, delta, pointer="Z") is not None)
        for delta in DELTAS
    ]


def _compact_ground_metadata(
    *,
    identity: RunIdentity,
    basis: Any,
    lookup: engine_ext.RawOrbitLookup,
    lam: float,
    doublet: engine_ext.TwoStateLanczosResult,
    cache_status: str,
    z_fragment: Mapping[str, object],
    z_pair: Mapping[str, object],
    x_fragment: Mapping[str, object],
    x_pair: Mapping[str, object],
    bond: Mapping[str, object],
) -> dict[str, object]:
    z_chi = {name: float(value) for name, value in z_fragment["class_chi"].items()}
    x_chi = {name: float(value) for name, value in x_fragment["class_chi"].items()}
    z_pair_values = {
        name: float(value) for name, value in z_pair["physical_values"].items()
    }
    x_pair_values = {
        name: float(value) for name, value in x_pair["physical_values"].items()
    }
    counts_z = _stationary_control_counts(
        fragment_chi=z_chi,
        entropy=float(z_fragment["entropy_bits"]),
        pair_information=z_pair_values,
    )
    counts_x = _stationary_control_counts(
        fragment_chi=x_chi,
        entropy=float(x_fragment["entropy_bits"]),
        pair_information=x_pair_values,
    )
    if counts_z != [0, 0, 0] or counts_x != [0, 0, 0]:
        raise AssertionError(
            f"stationary mixed doublet acquired events Z={counts_z}, X={counts_x}"
        )
    return {
        "schema": GROUND_SCHEMA,
        "protocol_hash": identity.protocol_hash,
        "parent_protocol_hash": identity.parent_protocol_hash,
        "basis_checksum": basis.checksum,
        "fragment_descriptor_checksum": identity.fragment_descriptor_checksum,
        "raw_to_orbit_checksum": lookup.checksum,
        "boundary_sentences": list(identity.boundary_sentences),
        "geometry": basis.geometry_name,
        "lam": float(lam),
        "energies": list(doublet.energies),
        "splitting": float(doublet.energies[1] - doublet.energies[0]),
        "residuals": list(doublet.residuals),
        "norm_errors": list(doublet.norm_errors),
        "overlap": doublet.overlap,
        "cache_status": cache_status,
        "fragment_z": {
            "probabilities": list(z_fragment["probabilities"]),
            "entropy_bits": float(z_fragment["entropy_bits"]),
            "chi_bits": z_chi,
            "site_chi_bits": {
                name: float(value) for name, value in z_fragment["site_chi"].items()
            },
            "density": z_fragment["serialized_types"],
        },
        "fragment_x": {
            "probabilities": list(x_fragment["probabilities"]),
            "entropy_bits": float(x_fragment["entropy_bits"]),
            "chi_bits": x_chi,
            "site_chi_bits": {
                name: float(value) for name, value in x_fragment["site_chi"].items()
            },
            "density": x_fragment["serialized_types"],
        },
        "pair_z": {
            "class_values": {
                name: float(value) for name, value in z_pair["type_values"].items()
            },
            "physical_values": z_pair_values,
            "density": z_pair["serialized_types"],
        },
        "pair_x": {
            "class_values": {
                name: float(value) for name, value in x_pair["type_values"].items()
            },
            "physical_values": x_pair_values,
            "density": x_pair["serialized_types"],
        },
        "center_bond": dict(bond),
        "stationary_event_counts": {"Z": counts_z, "X": counts_x},
        "stationary_observable_max_deviation": 0.0,
        "stationary_anchor": "mixed-doublet-own-first-row",
        "role": "stationary-control-and-reported-diagnostic-only-never-gate-baseline",
        "demolition": _demolition_table(basis, lam),
        "spec_note": SPEC_NOTE,
    }


def _load_or_build_ground_doublet(
    *,
    identity: RunIdentity,
    basis: Any,
    tables: Any,
    lookup: engine_ext.RawOrbitLookup,
    lam: float,
    budget_gb: float,
    allow_build: bool,
) -> tuple[tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]], dict[str, object]]:
    path = _ground_path(lam)
    if path.exists():
        with np.load(path, allow_pickle=False) as archive:
            schema = str(np.asarray(archive["schema"]).item())
            protocol_hash = str(np.asarray(archive["protocol_hash"]).item())
            parent_protocol_hash = str(
                np.asarray(archive["parent_protocol_hash"]).item()
            )
            basis_checksum = str(np.asarray(archive["basis_checksum"]).item())
            descriptor_checksum = str(
                np.asarray(archive["fragment_descriptor_checksum"]).item()
            )
            raw_lookup_checksum = str(
                np.asarray(archive["raw_to_orbit_checksum"]).item()
            )
            stored_lam = float(np.asarray(archive["lam"]).item())
            first = np.asarray(archive["g0"], dtype=np.complex128)
            second = np.asarray(archive["g1"], dtype=np.complex128)
            first_checksum = str(np.asarray(archive["g0_checksum"]).item())
            second_checksum = str(np.asarray(archive["g1_checksum"]).item())
            metadata = json.loads(str(np.asarray(archive["metadata_json"]).item()))
        exact = (
            schema == GROUND_SCHEMA
            and protocol_hash == identity.protocol_hash
            and parent_protocol_hash == identity.parent_protocol_hash
            and basis_checksum == basis.checksum
            and descriptor_checksum == identity.fragment_descriptor_checksum
            and raw_lookup_checksum == lookup.checksum
            and stored_lam == float(lam)
            and first.shape == (basis.n_orbits,)
            and second.shape == (basis.n_orbits,)
            and _state_checksum(first) == first_checksum
            and _state_checksum(second) == second_checksum
            and metadata.get("boundary_sentences") == list(identity.boundary_sentences)
            and metadata.get("parent_protocol_hash")
            == identity.parent_protocol_hash
            and metadata.get("role")
            == "stationary-control-and-reported-diagnostic-only-never-gate-baseline"
        )
        if not exact:
            raise RuntimeError(f"ground-doublet cache identity mismatch {path}")
        energies = tuple(float(value) for value in metadata["energies"])
        residuals: list[float] = []
        norm_errors: list[float] = []
        for state, energy in zip((first, second), energies, strict=True):
            residuals.append(
                float(
                    np.linalg.norm(
                        orbit_engine.hamiltonian_apply(basis, tables, lam, state)
                        - energy * state
                    )
                )
            )
            norm_errors.append(abs(float(np.vdot(state, state).real) - 1.0))
        overlap = float(abs(np.vdot(first, second)))
        if (
            max(residuals) > GROUND_RESIDUAL_TOL
            or max(norm_errors) > MACHINERY_TOL
            or overlap > MACHINERY_TOL
        ):
            raise RuntimeError("loaded ground doublet fails residual/orthogonality gates")
        metadata = dict(metadata)
        metadata["cache_status"] = "loaded"
        _guard_rss(f"load ground doublet lambda={lam:g}", budget_gb)
        return (first, second), metadata

    if not allow_build:
        raise FileNotFoundError(
            f"missing warm ground-doublet cache {path}; run --validate before --full"
        )
    doublet = engine_ext.two_lowest_states(
        basis, tables, lam, budget_gb=budget_gb
    )
    states = doublet.states
    weights = (0.5, 0.5)
    z_fragment = _fragment_panel(
        basis=basis,
        lookup=lookup,
        states=states,
        weights=weights,
        pointer_basis="Z",
        budget_gb=budget_gb,
    )
    z_pair = _pair_panel(
        basis=basis,
        lookup=lookup,
        states=states,
        weights=weights,
        pointer_basis="Z",
        reference_probabilities=z_fragment["probabilities"],
        budget_gb=budget_gb,
    )
    x_fragment = _fragment_panel(
        basis=basis,
        lookup=lookup,
        states=states,
        weights=weights,
        pointer_basis="X",
        budget_gb=budget_gb,
    )
    x_pair = _pair_panel(
        basis=basis,
        lookup=lookup,
        states=states,
        weights=weights,
        pointer_basis="X",
        reference_probabilities=x_fragment["probabilities"],
        budget_gb=budget_gb,
    )
    bond = _bond_observation(basis, _mixed_center_bond(states, weights))
    metadata = _compact_ground_metadata(
        identity=identity,
        basis=basis,
        lookup=lookup,
        lam=lam,
        doublet=doublet,
        cache_status="built",
        z_fragment=z_fragment,
        z_pair=z_pair,
        x_fragment=x_fragment,
        x_pair=x_pair,
        bond=bond,
    )
    first, second = states
    _atomic_savez(
        path,
        schema=np.asarray(GROUND_SCHEMA),
        protocol_hash=np.asarray(identity.protocol_hash),
        parent_protocol_hash=np.asarray(identity.parent_protocol_hash),
        basis_checksum=np.asarray(basis.checksum),
        fragment_descriptor_checksum=np.asarray(identity.fragment_descriptor_checksum),
        raw_to_orbit_checksum=np.asarray(lookup.checksum),
        boundary_sentences_json=np.asarray(_json_dumps(list(identity.boundary_sentences))),
        lam=np.asarray(lam, dtype=np.float64),
        g0=first,
        g1=second,
        g0_checksum=np.asarray(_state_checksum(first)),
        g1_checksum=np.asarray(_state_checksum(second)),
        metadata_json=np.asarray(_json_dumps(metadata)),
    )
    _guard_rss(f"build ground doublet lambda={lam:g}", budget_gb)
    return states, metadata


def _cube_preflight(
    *,
    identity: RunIdentity,
    basis: Any,
    lookup: engine_ext.RawOrbitLookup,
    initial: npt.NDArray[np.complex128],
    budget_gb: float,
) -> dict[str, object]:
    """Time all five live gathers and enforce the frozen launch projection."""

    timings: dict[str, float] = {}

    def timed(name: str, operation: Callable[[], object]) -> None:
        started = time.perf_counter()
        value = operation()
        timings[name] = time.perf_counter() - started
        del value
        _guard_rss(f"preflight {name}", budget_gb)

    timed(
        "k4",
        lambda: engine_ext.conditional_fragment_marginal(
            basis,
            lookup,
            (initial,),
            engine_ext.fragment_sites(basis, "+y"),
            pointer_basis="Z",
            budget_gb=budget_gb,
        ),
    )
    timed(
        "k5",
        lambda: engine_ext.conditional_fragment_marginal(
            basis,
            lookup,
            (initial,),
            engine_ext.fragment_sites(basis, "+x"),
            pointer_basis="Z",
            budget_gb=budget_gb,
        ),
    )
    for name, pair_class in (
        ("q9", "opposite-44"),
        ("q10", "plus-x-orthogonal"),
        ("q11", "opposite-55"),
    ):
        left, right = PAIR_REPRESENTATIVES[pair_class]
        timed(
            name,
            lambda left=left, right=right: engine_ext.fragment_pair_marginal(
                basis,
                lookup,
                (initial,),
                engine_ext.fragment_sites(basis, left),
                engine_ext.fragment_sites(basis, right),
                pointer_basis="Z",
                budget_gb=budget_gb,
            ),
        )

    calibrated_unit = max(
        PILOT_UNIT_SECONDS,
        timings["k4"] / 1.25,
        timings["k5"] / 1.25,
        timings["q9"] / 1.50,
        timings["q10"] / 1.50,
        timings["q11"] / 1.50,
    )
    projected_wall = FROZEN_WEIGHTED_UNITS * calibrated_unit + FROZEN_RESERVE_SECONDS
    projected_rss = float(orbit_engine.rss_gb())
    gate = bool(
        projected_wall <= PREFLIGHT_WALL_SECONDS
        and projected_rss <= PREFLIGHT_RSS_GB
    )
    payload: dict[str, object] = {
        "schema": PREFLIGHT_SCHEMA,
        "protocol_hash": identity.protocol_hash,
        "parent_protocol_hash": identity.parent_protocol_hash,
        "basis_checksum": basis.checksum,
        "fragment_descriptor_checksum": identity.fragment_descriptor_checksum,
        "raw_to_orbit_checksum": lookup.checksum,
        "boundary_sentences": list(identity.boundary_sentences),
        "preparation_bloch_vectors": _preparation_json(),
        "timings_seconds": timings,
        "calibrated_pilot_unit_seconds": calibrated_unit,
        "weighted_units": FROZEN_WEIGHTED_UNITS,
        "reserve_seconds": FROZEN_RESERVE_SECONDS,
        "projected_wall_seconds": projected_wall,
        "projected_rss_gb": projected_rss,
        "wall_limit_seconds": PREFLIGHT_WALL_SECONDS,
        "rss_limit_gb": PREFLIGHT_RSS_GB,
        "gate": gate,
        "spec_note": SPEC_NOTE,
    }
    _atomic_write_json(PREFLIGHT_CACHE_PATH, payload)
    return payload


def _baseline_from_row(row: Mapping[str, object]) -> dict[str, object]:
    if int(row["step"]) != 0:
        raise ValueError("trajectory baseline must come from step zero")
    fragment_types = row["fragment_types"]
    if not isinstance(fragment_types, Mapping):
        raise TypeError("step-zero row lacks fragment types")
    pointer_x = row.get("pointer_x")
    x_types = (
        pointer_x.get("fragment_types") if isinstance(pointer_x, Mapping) else None
    )
    result = {
        "pointer_z": list(row["pointer_z"]["p"]),
        "fragment_chi": {
            name: float(fragment_types[name]["chi_bits"])
            for name in engine_ext.FRAGMENT_CLASS_ORDER
        },
        "site_chi": {
            role: float(
                fragment_types[
                    "closed-five" if role in ("face", "edge") else "wedge-four"
                ]["one_site_reductions"][role]["chi_bits"]
            )
            for role in ("face", "edge", "corner")
        },
        "bond_one_minus_purity": float(row["center_bonds"][0]["one_minus_purity"]),
    }
    if isinstance(x_types, Mapping):
        result["x_fragment_chi"] = {
            name: float(x_types[name]["chi_bits"])
            for name in engine_ext.FRAGMENT_CLASS_ORDER
        }
        result["x_site_chi"] = {
            role: float(
                x_types[
                    "closed-five" if role in ("face", "edge") else "wedge-four"
                ]["one_site_reductions"][role]["chi_bits"]
            )
            for role in ("face", "edge", "corner")
        }
    return result


def _augment_fragment_serialization(
    *,
    panel: Mapping[str, object],
    t0_class_chi: Mapping[str, float],
    t0_site_chi: Mapping[str, float],
    gs_class_chi: Mapping[str, float],
    gs_site_chi: Mapping[str, float],
) -> dict[str, dict[str, object]]:
    serialized = json.loads(_json_dumps(panel["serialized_types"]))
    class_chi = panel["class_chi"]
    site_chi = panel["site_chi"]
    for class_name in engine_ext.FRAGMENT_CLASS_ORDER:
        entry = serialized[class_name]
        entry["chi_bits"] = float(class_chi[class_name])
        entry["trajectory_t0_chi_bits"] = float(t0_class_chi[class_name])
        entry["excess_bits"] = float(class_chi[class_name]) - float(
            t0_class_chi[class_name]
        )
        entry["gs_doublet_chi_bits"] = float(gs_class_chi[class_name])
        for role, reduction in entry["one_site_reductions"].items():
            reduction["trajectory_t0_chi_bits"] = float(t0_site_chi[role])
            reduction["excess_bits"] = float(site_chi[role]) - float(
                t0_site_chi[role]
            )
            reduction["gs_doublet_chi_bits"] = float(gs_site_chi[role])
    return serialized


def _serialized_pair_joint_holevo_max(pair_types: Mapping[str, object]) -> float:
    return max(
        abs(float(entry["joint_holevo_bits"]))
        for entry in pair_types.values()
    )


def _row_t0_information_error(row: Mapping[str, object]) -> float:
    fragment_types = row["fragment_types"]
    if not isinstance(fragment_types, Mapping):
        raise TypeError("t0 row fragment types malformed")
    values: list[float] = []
    for entry in fragment_types.values():
        values.append(abs(float(entry["chi_bits"])))
        values.extend(
            abs(float(reduction["chi_bits"]))
            for reduction in entry["one_site_reductions"].values()
        )
    pair_types = row.get("pair_types")
    if not isinstance(pair_types, Mapping):
        raise TypeError("t0 row must be on the frozen pair subgrid")
    values.append(_serialized_pair_joint_holevo_max(pair_types))
    pointer_x = row.get("pointer_x")
    if isinstance(pointer_x, Mapping):
        x_types = pointer_x["fragment_types"]
        for entry in x_types.values():
            values.append(abs(float(entry["chi_bits"])))
            values.extend(
                abs(float(reduction["chi_bits"]))
                for reduction in entry["one_site_reductions"].values()
            )
    return max(values, default=0.0)


def _measure_row(
    *,
    identity: RunIdentity,
    basis: Any,
    lookup: engine_ext.RawOrbitLookup,
    state: npt.NDArray[np.complex128],
    ground_metadata: Mapping[str, object],
    baseline: Mapping[str, object] | None,
    run_kind: str,
    lam: float,
    dt: float,
    step: int,
    pair_sampled: bool,
    include_x: bool,
    reference_norm: float,
    z_consecutive_previous: Mapping[str, int],
    x_consecutive_previous: Mapping[str, int],
    budget_gb: float,
) -> tuple[dict[str, object], dict[str, int], dict[str, int]]:
    """Measure and serialize one complete frozen-grid row."""

    row_started = time.perf_counter()
    z_fragment = _fragment_panel(
        basis=basis,
        lookup=lookup,
        states=(state,),
        weights=(1.0,),
        pointer_basis="Z",
        budget_gb=budget_gb,
    )
    p_z = tuple(float(value) for value in z_fragment["probabilities"])
    h_z = float(z_fragment["entropy_bits"])
    class_chi = {
        name: float(value) for name, value in z_fragment["class_chi"].items()
    }
    site_chi = {
        name: float(value) for name, value in z_fragment["site_chi"].items()
    }
    if baseline is None:
        t0_class_chi = dict(class_chi)
        t0_site_chi = dict(site_chi)
        p0_z = p_z
    else:
        t0_class_chi = {
            name: float(value) for name, value in baseline["fragment_chi"].items()
        }
        t0_site_chi = {
            name: float(value) for name, value in baseline["site_chi"].items()
        }
        p0_z = tuple(float(value) for value in baseline["pointer_z"])
    class_excess = {
        name: class_chi[name] - t0_class_chi[name]
        for name in engine_ext.FRAGMENT_CLASS_ORDER
    }
    site_excess = {
        name: site_chi[name] - t0_site_chi[name]
        for name in ("face", "edge", "corner")
    }
    tv_drift = 0.5 * sum(
        abs(p_z[index] - p0_z[index]) for index in range(2)
    )

    singleton_flags: dict[str, dict[str, bool]] = {}
    for delta in DELTAS:
        key = DELTA_KEYS[delta]
        singleton_flags[key] = {
            label: _singleton_gate(
                h_z,
                class_chi[_fragment_type_for_label(label)],
                class_excess[_fragment_type_for_label(label)],
                delta,
            )
            for label in engine_ext.FRAGMENT_LABEL_ORDER
        }

    z_pair: dict[str, object] | None = None
    r_ind: dict[str, int] | None = None
    certifying_subsets: dict[str, list[str]] | None = None
    z_consecutive = {key: int(value) for key, value in z_consecutive_previous.items()}
    if pair_sampled:
        z_pair = _pair_panel(
            basis=basis,
            lookup=lookup,
            states=(state,),
            weights=(1.0,),
            pointer_basis="Z",
            reference_probabilities=p_z,
            budget_gb=budget_gb,
        )
        r_ind = {}
        certifying_subsets = {}
        for delta in DELTAS:
            key = DELTA_KEYS[delta]
            redundancy, subset = _largest_independent_subset(
                singleton_flags[key], z_pair["physical_values"]
            )
            r_ind[key] = redundancy
            certifying_subsets[key] = list(subset)
            z_consecutive[key] = (
                z_consecutive.get(key, 0) + 1 if redundancy >= MIN_REDUNDANCY else 0
            )

    ground_z = ground_metadata["fragment_z"]
    fragment_types = _augment_fragment_serialization(
        panel=z_fragment,
        t0_class_chi=t0_class_chi,
        t0_site_chi=t0_site_chi,
        gs_class_chi=ground_z["chi_bits"],
        gs_site_chi=ground_z["site_chi_bits"],
    )
    fragments = [
        {
            "label": label,
            "coordinates": [
                list(coordinate) for coordinate in engine_ext.FRAGMENT_COORDINATES[label]
            ],
            "tensor_factor_order": [
                list(coordinate) for coordinate in engine_ext.FRAGMENT_COORDINATES[label]
            ],
            "fragment_type": _fragment_type_for_label(label),
            "singleton_certifies": {
                key: bool(singleton_flags[key][label]) for key in singleton_flags
            },
        }
        for label in engine_ext.FRAGMENT_LABEL_ORDER
    ]

    pointer_x: dict[str, object] | None = None
    x_density_errors = {"hermiticity": 0.0, "trace": 0.0, "negativity": 0.0}
    x_entropy_bound = 0.0
    x_symmetry_error = 0.0
    x_consecutive = {key: int(value) for key, value in x_consecutive_previous.items()}
    if include_x:
        x_fragment = _fragment_panel(
            basis=basis,
            lookup=lookup,
            states=(state,),
            weights=(1.0,),
            pointer_basis="X",
            budget_gb=budget_gb,
        )
        p_x = tuple(float(value) for value in x_fragment["probabilities"])
        h_x = float(x_fragment["entropy_bits"])
        x_class_chi = {
            name: float(value) for name, value in x_fragment["class_chi"].items()
        }
        x_site_chi = {
            name: float(value) for name, value in x_fragment["site_chi"].items()
        }
        if baseline is None:
            x_t0_class = dict(x_class_chi)
            x_t0_site = dict(x_site_chi)
        else:
            x_t0_class = {
                name: float(value)
                for name, value in baseline["x_fragment_chi"].items()
            }
            x_t0_site = {
                name: float(value) for name, value in baseline["x_site_chi"].items()
            }
        x_excess = {
            name: x_class_chi[name] - x_t0_class[name]
            for name in engine_ext.FRAGMENT_CLASS_ORDER
        }
        x_flags: dict[str, dict[str, bool]] = {}
        lazy_pair_required = False
        for delta in DELTAS:
            key = DELTA_KEYS[delta]
            x_flags[key] = {
                label: _singleton_gate(
                    h_x,
                    x_class_chi[_fragment_type_for_label(label)],
                    x_excess[_fragment_type_for_label(label)],
                    delta,
                )
                for label in engine_ext.FRAGMENT_LABEL_ORDER
            }
            lazy_pair_required = lazy_pair_required or sum(x_flags[key].values()) >= 2
        x_pair: dict[str, object] | None = None
        x_r_ind = {DELTA_KEYS[delta]: 0 for delta in DELTAS}
        x_subsets = {DELTA_KEYS[delta]: [] for delta in DELTAS}
        if lazy_pair_required:
            x_pair = _pair_panel(
                basis=basis,
                lookup=lookup,
                states=(state,),
                weights=(1.0,),
                pointer_basis="X",
                reference_probabilities=p_x,
                budget_gb=budget_gb,
            )
            for delta in DELTAS:
                key = DELTA_KEYS[delta]
                redundancy, subset = _largest_independent_subset(
                    x_flags[key], x_pair["physical_values"]
                )
                x_r_ind[key] = redundancy
                x_subsets[key] = list(subset)
        x_density_errors = dict(x_fragment["density_errors"])
        x_symmetry_error = float(x_fragment["symmetry"]["maximum"])
        if x_pair is not None:
            for name in x_density_errors:
                x_density_errors[name] = max(
                    x_density_errors[name], float(x_pair["density_errors"][name])
                )
        x_entropy_bound = max(
            [
                max(0.0, -value, value - h_x)
                for value in (*x_class_chi.values(), *x_site_chi.values())
            ]
            + (
                [max(0.0, -float(value)) for value in x_pair["type_values"].values()]
                if x_pair is not None
                else [0.0]
            )
        )
        for delta in DELTAS:
            key = DELTA_KEYS[delta]
            x_consecutive[key] = (
                x_consecutive.get(key, 0) + 1
                if x_r_ind[key] >= MIN_REDUNDANCY
                else 0
            )
        ground_x = ground_metadata["fragment_x"]
        x_types = _augment_fragment_serialization(
            panel=x_fragment,
            t0_class_chi=x_t0_class,
            t0_site_chi=x_t0_site,
            gs_class_chi=ground_x["chi_bits"],
            gs_site_chi=ground_x["site_chi_bits"],
        )
        pointer_x = {
            "p": list(p_x),
            "entropy_bits": h_x,
            "fragment_types": x_types,
            "singleton_certifies": x_flags,
            "pair_types": None if x_pair is None else x_pair["serialized_types"],
            "pair_conditional_mi_bits": None
            if x_pair is None
            else {
                "classes": x_pair["type_values"],
                "physical": x_pair["physical_values"],
                "mappings": x_pair["physical_mappings"],
            },
            "pair_null_reason": None
            if x_pair is not None
            else "fewer-than-two-x-singletons-pass-frozen-gates",
            "r_ind": x_r_ind,
            "certifying_subsets": x_subsets,
            "consecutive_sample_counts": dict(x_consecutive),
            "lazy_pair_rule_fired": lazy_pair_required,
            "symmetry_consistency": x_fragment["symmetry"],
        }

    bond = _bond_observation(basis, orbit_engine.center_bond_state(state))
    if baseline is None:
        bond_t0 = float(bond["one_minus_purity"])
    else:
        bond_t0 = float(baseline["bond_one_minus_purity"])
    theta = float(bond["one_minus_purity"]) - bond_t0
    center_bonds = [
        {
            "axis": label,
            **bond,
            "trajectory_t0_one_minus_purity": bond_t0,
            "theta_contribution": theta,
            "gs_doublet_one_minus_purity": float(
                ground_metadata["center_bond"]["one_minus_purity"]
            ),
        }
        for label in engine_ext.FRAGMENT_LABEL_ORDER
    ]

    bloch = {
        role: _bloch_from_ensemble(p_z, z_fragment["site_states"][role])
        for role in ("face", "edge", "corner")
    }
    q_quiet = 1.0 - (bloch["edge"]["z"] + bloch["corner"]["z"]) / 2.0
    x_face = bloch["face"]["x"]
    reached_shells = [
        shell
        for shell, role in ((1, "face"), (2, "edge"), (3, "corner"))
        if site_excess[role] + NUMERIC_GATE_TOL >= EPS_EXCESS
    ]
    xi_reg = max(reached_shells) if reached_shells else None
    sum_fragment_excess = (
        2.0 * class_excess["closed-five"]
        + 4.0 * class_excess["wedge-four"]
    )

    density_errors = dict(z_fragment["density_errors"])
    if z_pair is not None:
        for name in density_errors:
            density_errors[name] = max(
                density_errors[name], float(z_pair["density_errors"][name])
            )
    if pointer_x is not None:
        for name in density_errors:
            density_errors[name] = max(
                density_errors[name], float(x_density_errors[name])
            )
    bond_density = bond["density"]
    density_errors["hermiticity"] = max(
        density_errors["hermiticity"], float(bond_density["hermiticity_error"])
    )
    density_errors["trace"] = max(
        density_errors["trace"],
        abs(float(bond_density["trace_real"]) - 1.0)
        + abs(float(bond_density["trace_imag"])),
    )
    density_errors["negativity"] = max(
        density_errors["negativity"],
        max(0.0, -float(bond_density["minimum_eigenvalue"])),
    )
    entropy_bound = max(
        [
            max(0.0, -value, value - h_z)
            for value in (*class_chi.values(), *site_chi.values())
        ]
        + (
            [max(0.0, -float(value)) for value in z_pair["type_values"].values()]
            if z_pair is not None
            else [0.0]
        )
    )
    entropy_bound = max(entropy_bound, x_entropy_bound)
    norm = float(np.linalg.norm(state))
    relative_norm_error = abs(norm - reference_norm) / reference_norm
    if relative_norm_error > MACHINERY_TOL:
        raise RuntimeError(
            f"state norm error {relative_norm_error:.3e} exceeds 1e-9"
        )

    max_ratio = max(class_chi.values()) / h_z if h_z > 0.0 else None
    seam_leakage = None
    opposite_55 = None
    opposite_44 = None
    raw_minus_ind = None
    if z_pair is not None and r_ind is not None:
        seam_leakage = max(
            float(z_pair["type_values"][name])
            for name in (
                "plus-x-orthogonal",
                "minus-x-orthogonal",
                "transverse-orthogonal",
            )
        )
        opposite_55 = float(z_pair["type_values"]["opposite-55"])
        opposite_44 = float(z_pair["type_values"]["opposite-44"])
        headline_key = DELTA_KEYS[HEADLINE_DELTA]
        raw_count = sum(singleton_flags[headline_key].values())
        raw_minus_ind = raw_count - int(r_ind[headline_key])

    pair_types_value = None if z_pair is None else z_pair["serialized_types"]
    pair_values_value = None
    if z_pair is not None:
        pair_values_value = {
            "classes": z_pair["type_values"],
            "physical": z_pair["physical_values"],
            "mappings": z_pair["physical_mappings"],
        }
    row: dict[str, object] = {
        "schema": STREAM_SCHEMA,
        "run_kind": run_kind,
        "geometry": basis.geometry_name,
        "lam": float(lam),
        "dt": float(dt),
        "step": int(step),
        "jt": float(step * dt),
        "protocol_hash": identity.protocol_hash,
        "parent_protocol_hash": identity.parent_protocol_hash,
        "basis_checksum": basis.checksum,
        "fragment_descriptor_checksum": identity.fragment_descriptor_checksum,
        "raw_to_orbit_checksum": lookup.checksum,
        "preparation_bloch_vectors": _preparation_json(),
        "boundary_sentences": list(identity.boundary_sentences),
        "spec_note": SPEC_NOTE,
        "pointer_z": {
            "p": list(p_z),
            "entropy_bits": h_z,
            "tv_from_t0": tv_drift,
            "trajectory_t0_p": list(p0_z),
        },
        "pointer_x": pointer_x,
        "pointer_x_reason": None
        if pointer_x is not None
        else "not-on-frozen-x-demolition-grid",
        "fragment_types": fragment_types,
        "fragments": fragments,
        "pair_subgrid": True if pair_sampled else None,
        "pair_types": pair_types_value,
        "pair_conditional_mi_bits": pair_values_value,
        "pair_null_reason": None
        if pair_sampled
        else "not-on-frozen-pair-subgrid",
        "r_ind": r_ind,
        "certifying_subsets": certifying_subsets,
        "consecutive_sample_counts": dict(z_consecutive) if pair_sampled else None,
        "center_bonds": center_bonds,
        "theta": theta,
        "shell_excess_profile": {
            "face": site_excess["face"],
            "edge": site_excess["edge"],
            "corner": site_excess["corner"],
        },
        "fragment_excess_profile": dict(class_excess),
        "sum_fragment_excess_bits": sum_fragment_excess,
        "Q_quiet": q_quiet,
        "<X>_face": x_face,
        "bloch_vectors": bloch,
        "xi_reg": xi_reg,
        "contrast_profile": {
            "Q_quiet": q_quiet,
            "<X>_face": x_face,
            "face_bloch": bloch["face"],
            "edge_bloch": bloch["edge"],
            "corner_bloch": bloch["corner"],
        },
        "risk_signatures": {
            "max_fragment_chi_over_pointer_entropy": max_ratio,
            "max_fragment_excess_bits": max(class_excess.values()),
            "pointer_z_tv_from_t0": tv_drift,
            "L_seam_bits": seam_leakage,
            "C_opposite_55_bits": opposite_55,
            "C_opposite_44_bits": opposite_44,
            "R_raw_minus_R_ind_headline": raw_minus_ind,
            "capacity_gain_bits": z_fragment["capacity_gain"],
            "Q_quiet": q_quiet,
            "<X>_face": x_face,
        },
        "diagnostics": {
            "state_norm": norm,
            "relative_norm_error": relative_norm_error,
            "orbit_normalization_error": relative_norm_error,
            "entropy_bound_error": entropy_bound,
            "density_errors": density_errors,
            "symmetry_consistency": {
                **dict(z_fragment["symmetry"]),
                "z_maximum": float(z_fragment["symmetry"]["maximum"]),
                "x_maximum": x_symmetry_error,
                "maximum": max(
                    float(z_fragment["symmetry"]["maximum"]), x_symmetry_error
                ),
            },
            "symmetry_consistency_method": (
                "exact-invariant-sector-single-subset-plus-redundant-class-gates"
            ),
            "rss_peak_gb": float(orbit_engine.rss_gb()),
            "row_wall_seconds": time.perf_counter() - row_started,
        },
    }
    return row, z_consecutive, x_consecutive


def _sigterm_handler(_signum: int, _frame: object) -> None:
    global _SIGNAL_CONTEXT, _SIGTERM_PENDING
    _SIGTERM_PENDING = True
    context = _SIGNAL_CONTEXT
    if context is None:
        return
    context.requested = True
    if context.saving:
        return
    try:
        context.saving = True
        context.save_now("SIGTERM")
    except Exception as exc:  # pragma: no cover - asynchronous path
        context.error = f"{type(exc).__name__}: {exc}"
    finally:
        context.saving = False


def _rows_by_step(rows: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    ordered = sorted((dict(row) for row in rows), key=lambda row: int(row["step"]))
    steps = [int(row["step"]) for row in ordered]
    if len(steps) != len(set(steps)):
        raise RuntimeError("accumulated rows contain duplicate steps")
    return ordered


def _trace_grid(dt: float, n_steps: int) -> list[float]:
    return [float(step * dt) for step in range(n_steps + 1)]


def _save_trace_checkpoint(
    *,
    identity: RunIdentity,
    prefix: str,
    reason: str,
    basis: Any,
    lookup: engine_ext.RawOrbitLookup,
    lam: float,
    dt: float,
    n_steps: int,
    fine: bool,
    step: int,
    state: npt.NDArray[np.complex128],
    initial_checksum: str,
    reference_norm: float,
    rows: Sequence[Mapping[str, object]],
    ground_metadata: Mapping[str, object],
    run_wall_seconds: float,
) -> Path:
    ordered = _rows_by_step(rows)
    if not ordered or int(ordered[-1]["step"]) != int(step):
        raise RuntimeError("checkpoint state step does not match latest row")
    state_array = np.asarray(state, dtype=np.complex128)
    metadata = {
        "schema": CHECKPOINT_SCHEMA,
        "protocol_hash": identity.protocol_hash,
        "parent_protocol_hash": identity.parent_protocol_hash,
        "basis_checksum": basis.checksum,
        "fragment_descriptor_checksum": identity.fragment_descriptor_checksum,
        "raw_to_orbit_checksum": lookup.checksum,
        "boundary_sentences": list(identity.boundary_sentences),
        "preparation_bloch_vectors": _preparation_json(),
        "prefix": prefix,
        "reason": reason,
        "geometry": basis.geometry_name,
        "run_kind": "cube-dt-halving" if fine else "cube-full",
        "lam": float(lam),
        "dt": float(dt),
        "n_steps": int(n_steps),
        "trace_coordinates": _trace_grid(dt, n_steps),
        "step": int(step),
        "initial_checksum": initial_checksum,
        "reference_norm": float(reference_norm),
        "run_wall_seconds": float(run_wall_seconds),
        "spec_note": SPEC_NOTE,
    }
    path = _checkpoint_path(prefix, step)
    _atomic_savez(
        path,
        schema=np.asarray(CHECKPOINT_SCHEMA),
        protocol_hash=np.asarray(identity.protocol_hash),
        parent_protocol_hash=np.asarray(identity.parent_protocol_hash),
        basis_checksum=np.asarray(basis.checksum),
        fragment_descriptor_checksum=np.asarray(identity.fragment_descriptor_checksum),
        raw_to_orbit_checksum=np.asarray(lookup.checksum),
        prefix=np.asarray(prefix),
        lam=np.asarray(lam, dtype=np.float64),
        dt=np.asarray(dt, dtype=np.float64),
        n_steps=np.asarray(n_steps, dtype=np.int64),
        step=np.asarray(step, dtype=np.int64),
        psi=state_array,
        psi_checksum=np.asarray(_state_checksum(state_array)),
        initial_checksum=np.asarray(initial_checksum),
        reference_norm=np.asarray(reference_norm, dtype=np.float64),
        rows_json=np.asarray(_json_dumps(ordered)),
        ground_json=np.asarray(_json_dumps(dict(ground_metadata))),
        metadata_json=np.asarray(_json_dumps(metadata)),
    )
    return path


def _newest_checkpoint_path(prefix: str) -> Path | None:
    paths = sorted(RUN_DIR.glob(f"{prefix}_step_*.npz"))
    return paths[-1] if paths else None


def _load_trace_checkpoint(
    path: Path,
    *,
    identity: RunIdentity,
    expected_prefix: str,
    expected_lam: float,
    expected_dt: float,
    expected_n_steps: int,
    expected_basis_checksum: str | None,
    expected_lookup_checksum: str | None,
    expected_initial_checksum: str | None,
    expected_state_size: int | None,
    load_state: bool,
) -> dict[str, object]:
    with np.load(path, allow_pickle=False) as archive:
        state = np.asarray(archive["psi"], dtype=np.complex128)
        result: dict[str, object] = {
            "schema": str(np.asarray(archive["schema"]).item()),
            "protocol_hash": str(np.asarray(archive["protocol_hash"]).item()),
            "parent_protocol_hash": str(
                np.asarray(archive["parent_protocol_hash"]).item()
            ),
            "basis_checksum": str(np.asarray(archive["basis_checksum"]).item()),
            "fragment_descriptor_checksum": str(
                np.asarray(archive["fragment_descriptor_checksum"]).item()
            ),
            "raw_to_orbit_checksum": str(
                np.asarray(archive["raw_to_orbit_checksum"]).item()
            ),
            "prefix": str(np.asarray(archive["prefix"]).item()),
            "lam": float(np.asarray(archive["lam"]).item()),
            "dt": float(np.asarray(archive["dt"]).item()),
            "n_steps": int(np.asarray(archive["n_steps"]).item()),
            "step": int(np.asarray(archive["step"]).item()),
            "psi_checksum": str(np.asarray(archive["psi_checksum"]).item()),
            "initial_checksum": str(np.asarray(archive["initial_checksum"]).item()),
            "reference_norm": float(np.asarray(archive["reference_norm"]).item()),
            "rows": json.loads(str(np.asarray(archive["rows_json"]).item())),
            "ground": json.loads(str(np.asarray(archive["ground_json"]).item())),
            "metadata": json.loads(str(np.asarray(archive["metadata_json"]).item())),
            "state_shape": state.shape,
        }
        if load_state:
            result["psi"] = state
    metadata = result["metadata"]
    exact = (
        result["schema"] == CHECKPOINT_SCHEMA
        and result["protocol_hash"] == identity.protocol_hash
        and result["parent_protocol_hash"] == identity.parent_protocol_hash
        and result["fragment_descriptor_checksum"]
        == identity.fragment_descriptor_checksum
        and result["prefix"] == expected_prefix
        and float(result["lam"]) == float(expected_lam)
        and float(result["dt"]) == float(expected_dt)
        and int(result["n_steps"]) == int(expected_n_steps)
        and metadata.get("boundary_sentences") == list(identity.boundary_sentences)
        and metadata.get("parent_protocol_hash") == identity.parent_protocol_hash
        and metadata.get("preparation_bloch_vectors") == _preparation_json()
        and metadata.get("trace_coordinates") == _trace_grid(
            expected_dt, expected_n_steps
        )
        and (
            expected_basis_checksum is None
            or result["basis_checksum"] == expected_basis_checksum
        )
        and (
            expected_lookup_checksum is None
            or result["raw_to_orbit_checksum"] == expected_lookup_checksum
        )
        and (
            expected_initial_checksum is None
            or result["initial_checksum"] == expected_initial_checksum
        )
        and (
            expected_state_size is None
            or result["state_shape"] == (expected_state_size,)
        )
    )
    if not exact:
        raise RuntimeError(f"checkpoint identity mismatch {path}")
    if _state_checksum(state) != result["psi_checksum"]:
        raise RuntimeError(f"checkpoint state checksum mismatch {path}")
    ordered = _rows_by_step(result["rows"])
    if not ordered or int(ordered[-1]["step"]) != int(result["step"]):
        raise RuntimeError(f"checkpoint rows do not end at its state step {path}")
    result["rows"] = ordered
    return result


def _read_stream(
    path: Path,
    *,
    identity: RunIdentity,
    expected_lam: float,
    expected_dt: float,
    expected_kind: str,
    expected_basis_checksum: str | None,
) -> list[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(f"missing observable stream {path}")
    rows: list[dict[str, object]] = []
    seen: set[int] = set()
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.endswith("\n"):
                raise RuntimeError(f"unterminated JSONL row {path}:{line_number}")
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"invalid JSONL row {path}:{line_number}: {exc}") from exc
            exact = (
                row.get("schema") == STREAM_SCHEMA
                and row.get("protocol_hash") == identity.protocol_hash
                and row.get("parent_protocol_hash") == identity.parent_protocol_hash
                and row.get("fragment_descriptor_checksum")
                == identity.fragment_descriptor_checksum
                and row.get("boundary_sentences") == list(identity.boundary_sentences)
                and row.get("preparation_bloch_vectors") == _preparation_json()
                and float(row.get("lam", math.nan)) == float(expected_lam)
                and float(row.get("dt", math.nan)) == float(expected_dt)
                and row.get("run_kind") == expected_kind
                and (
                    expected_basis_checksum is None
                    or row.get("basis_checksum") == expected_basis_checksum
                )
            )
            if not exact:
                raise RuntimeError(f"observable stream identity mismatch {path}:{line_number}")
            step = int(row["step"])
            if step in seen:
                raise RuntimeError(f"duplicate observable step {step} in {path}")
            seen.add(step)
            rows.append(row)
    return _rows_by_step(rows)


def _progress_line(
    *,
    lam: float,
    step: int,
    n_steps: int,
    fine: bool,
    run_started: float,
    completed_units: int,
    total_units: int,
    wall_offset_seconds: float,
) -> None:
    elapsed = max(0.0, float(wall_offset_seconds) + time.monotonic() - run_started)
    fraction = min(1.0, max(1.0 / total_units, completed_units / total_units))
    remaining = elapsed * (1.0 - fraction) / fraction
    projected = datetime.fromtimestamp(
        time.time() + remaining, tz=timezone.utc
    ).isoformat(timespec="seconds")
    print(
        f"PROGRESS trace={'dt-half' if fine else 'main'} lam={lam:g} "
        f"step={step}/{n_steps} wall={elapsed:.1f}s "
        f"projected-completion={projected} rss={orbit_engine.rss_gb():.3f}GiB",
        file=sys.stderr,
        flush=True,
    )


def _previous_consecutive(
    rows: Sequence[Mapping[str, object]], *, pointer: str
) -> dict[str, int]:
    values = {DELTA_KEYS[delta]: 0 for delta in DELTAS}
    if pointer == "Z":
        sampled = [row for row in rows if row.get("pair_subgrid") is True]
        if sampled:
            panel = sampled[-1].get("consecutive_sample_counts")
            if isinstance(panel, Mapping):
                values = {key: int(panel[key]) for key in values}
    elif pointer == "X":
        sampled_x = [row.get("pointer_x") for row in rows if isinstance(row.get("pointer_x"), Mapping)]
        if sampled_x:
            panel = sampled_x[-1].get("consecutive_sample_counts")
            if isinstance(panel, Mapping):
                values = {key: int(panel[key]) for key in values}
    else:
        raise ValueError("pointer must be Z or X")
    return values


def _run_trace(
    *,
    identity: RunIdentity,
    basis: Any,
    tables: Any,
    lookup: engine_ext.RawOrbitLookup,
    lam: float,
    dt: float,
    n_steps: int,
    fine: bool,
    initial: npt.NDArray[np.complex128],
    ground_metadata: Mapping[str, object],
    run_started: float,
    progress_base_units: int,
    progress_total_units: int,
    wall_offset_seconds: float,
) -> dict[str, object]:
    """Run/resume one trace with fsynced rows and atomic step checkpoints."""

    global _SIGNAL_CONTEXT, _SIGTERM_PENDING
    prefix = _trace_prefix(lam, fine=fine)
    run_kind = "cube-dt-halving" if fine else "cube-full"
    stream_path = _stream_path(lam, fine=fine)
    initial_state = np.asarray(initial, dtype=np.complex128)
    initial_checksum = _state_checksum(initial_state)
    reference_norm = float(np.linalg.norm(initial_state))
    if abs(reference_norm - 1.0) > MACHINERY_TOL:
        raise RuntimeError("initial state is not normalized")

    newest = _newest_checkpoint_path(prefix)
    effective_wall_offset = float(wall_offset_seconds)
    if newest is None:
        if stream_path.exists() and stream_path.stat().st_size:
            raise RuntimeError(f"stream {stream_path} exists without a matching checkpoint")
        start_step = 0
        state = initial_state.copy()
        rows: list[dict[str, object]] = []
        baseline: dict[str, object] | None = None
    else:
        loaded = _load_trace_checkpoint(
            newest,
            identity=identity,
            expected_prefix=prefix,
            expected_lam=lam,
            expected_dt=dt,
            expected_n_steps=n_steps,
            expected_basis_checksum=basis.checksum,
            expected_lookup_checksum=lookup.checksum,
            expected_initial_checksum=initial_checksum,
            expected_state_size=basis.n_orbits,
            load_state=True,
        )
        start_step = int(loaded["step"])
        state = np.asarray(loaded["psi"], dtype=np.complex128)
        rows = [dict(row) for row in loaded["rows"]]
        reference_norm = float(loaded["reference_norm"])
        loaded_wall = float(loaded["metadata"].get("run_wall_seconds", 0.0))
        if not np.isfinite(loaded_wall) or loaded_wall < 0.0:
            raise RuntimeError("checkpoint has invalid cumulative wall metadata")
        effective_wall_offset = max(effective_wall_offset, loaded_wall)
        loaded_ground = dict(loaded["ground"])
        current_ground = dict(ground_metadata)
        loaded_ground.pop("cache_status", None)
        current_ground.pop("cache_status", None)
        if _json_dumps(loaded_ground) != _json_dumps(current_ground):
            raise RuntimeError("checkpoint ground/control metadata mismatch")
        if start_step > n_steps or not rows or int(rows[0]["step"]) != 0:
            raise RuntimeError("checkpoint does not retain a valid t=0 row")
        baseline = _baseline_from_row(rows[0])
        streamed = _read_stream(
            stream_path,
            identity=identity,
            expected_lam=lam,
            expected_dt=dt,
            expected_kind=run_kind,
            expected_basis_checksum=basis.checksum,
        )
        if _json_dumps(streamed) != _json_dumps(rows):
            raise RuntimeError("stream/checkpoint row identity mismatch on resume")

    row_by_step = {int(row["step"]): row for row in rows}
    z_consecutive = _previous_consecutive(rows, pointer="Z")
    x_consecutive = _previous_consecutive(rows, pointer="X")
    live: dict[str, object] = {"state": state, "step": start_step, "rows": rows}

    def save_now(reason: str) -> None:
        current_rows = list(live["rows"])
        if not current_rows:
            return
        _save_trace_checkpoint(
            identity=identity,
            prefix=prefix,
            reason=reason,
            basis=basis,
            lookup=lookup,
            lam=lam,
            dt=dt,
            n_steps=n_steps,
            fine=fine,
            step=int(live["step"]),
            state=np.asarray(live["state"], dtype=np.complex128),
            initial_checksum=initial_checksum,
            reference_norm=reference_norm,
            rows=current_rows,
            ground_metadata=ground_metadata,
            run_wall_seconds=effective_wall_offset + time.monotonic() - run_started,
        )

    context = SignalCheckpointContext(save_now=save_now, requested=_SIGTERM_PENDING)
    _SIGNAL_CONTEXT = context
    original_resume = os.environ.get("D3_ENGINE_RESUME")
    os.environ["D3_ENGINE_RESUME"] = "0"

    def callback(local_step: int, psi: npt.NDArray[np.complex128]) -> None:
        nonlocal baseline, z_consecutive, x_consecutive
        global_step = start_step + int(local_step)
        if global_step > n_steps:
            raise AssertionError("evolution callback exceeded frozen grid")
        existing = row_by_step.get(global_step)
        if existing is None:
            pair_sampled = fine or global_step in PAIR_MAIN_STEPS
            include_x = (
                not fine
                and global_step * dt <= HEADLINE_TIME + NUMERIC_GATE_TOL
            )
            row, z_consecutive, x_consecutive = _measure_row(
                identity=identity,
                basis=basis,
                lookup=lookup,
                state=psi,
                ground_metadata=ground_metadata,
                baseline=baseline,
                run_kind=run_kind,
                lam=lam,
                dt=dt,
                step=global_step,
                pair_sampled=pair_sampled,
                include_x=include_x,
                reference_norm=reference_norm,
                z_consecutive_previous=z_consecutive,
                x_consecutive_previous=x_consecutive,
                budget_gb=FULL_RSS_GB,
            )
            if global_step == 0:
                t0_error = _row_t0_information_error(row)
                if t0_error > MACHINERY_TOL:
                    raise AssertionError(
                        f"trajectory t=0 information {t0_error:.3e} exceeds 1e-9"
                    )
                baseline = _baseline_from_row(row)
            elif baseline is None:
                raise RuntimeError("trace lost its t=0 trajectory anchor")
            _append_jsonl(stream_path, row)
            rows.append(row)
            row_by_step[global_step] = row
        elif int(local_step) != 0:
            raise RuntimeError(f"new evolution collided with existing step {global_step}")

        live["state"] = np.asarray(psi, dtype=np.complex128)
        live["step"] = global_step
        live["rows"] = rows
        _progress_line(
            lam=lam,
            step=global_step,
            n_steps=n_steps,
            fine=fine,
            run_started=run_started,
            completed_units=progress_base_units + global_step + 1,
            total_units=progress_total_units,
            wall_offset_seconds=effective_wall_offset,
        )
        if global_step % 10 == 0 or global_step == n_steps:
            context.saving = True
            try:
                save_now("complete" if global_step == n_steps else "interval-10")
            finally:
                context.saving = False
        if context.requested or _SIGTERM_PENDING:
            if context.error:
                raise RuntimeError(f"SIGTERM checkpoint failed: {context.error}")
            if global_step % 10 != 0 and global_step != n_steps:
                save_now("SIGTERM-callback")
            raise SigtermRequested("SIGTERM received after latest complete row checkpoint")
        _guard_rss(f"trace {prefix} step {global_step}", FULL_RSS_GB)

    try:
        remaining = n_steps - start_step
        if remaining == 0:
            callback(0, state)
        else:
            orbit_engine.evolve(
                basis, tables, lam, state, dt, remaining, callback
            )
    finally:
        if original_resume is None:
            os.environ.pop("D3_ENGINE_RESUME", None)
        else:
            os.environ["D3_ENGINE_RESUME"] = original_resume
        _SIGNAL_CONTEXT = None

    ordered = _rows_by_step(rows)
    if [int(row["step"]) for row in ordered] != list(range(n_steps + 1)):
        raise RuntimeError(f"trace {prefix} is incomplete on its frozen grid")
    streamed = _read_stream(
        stream_path,
        identity=identity,
        expected_lam=lam,
        expected_dt=dt,
        expected_kind=run_kind,
        expected_basis_checksum=basis.checksum,
    )
    if _json_dumps(streamed) != _json_dumps(ordered):
        raise RuntimeError(f"complete stream/checkpoint row mismatch for {prefix}")
    completion_wall = effective_wall_offset + time.monotonic() - run_started
    _save_trace_checkpoint(
        identity=identity,
        prefix=prefix,
        reason="complete-verified-stream-identity",
        basis=basis,
        lookup=lookup,
        lam=lam,
        dt=dt,
        n_steps=n_steps,
        fine=fine,
        step=n_steps,
        state=np.asarray(live["state"], dtype=np.complex128),
        initial_checksum=initial_checksum,
        reference_norm=reference_norm,
        rows=ordered,
        ground_metadata=ground_metadata,
        run_wall_seconds=completion_wall,
    )
    return {
        "rows": ordered,
        "ground": dict(ground_metadata),
        "prefix": prefix,
        "completion_wall_seconds": completion_wall,
        "wall_offset_seconds": effective_wall_offset,
    }


def _first_event(
    rows: Sequence[Mapping[str, object]],
    delta: float,
    *,
    pointer: str = "Z",
) -> dict[str, object] | None:
    key = DELTA_KEYS[delta]
    if pointer == "Z":
        certification_rows = [row for row in rows if row.get("pair_subgrid") is True]

        def panel(row: Mapping[str, object]) -> tuple[int, list[str], Mapping[str, float]]:
            pair_information = row["pair_conditional_mi_bits"]["physical"]
            return (
                int(row["r_ind"][key]),
                list(row["certifying_subsets"][key]),
                pair_information,
            )

    elif pointer == "X":
        certification_rows = [
            row for row in rows if isinstance(row.get("pointer_x"), Mapping)
        ]

        def panel(row: Mapping[str, object]) -> tuple[int, list[str], Mapping[str, float]]:
            x = row["pointer_x"]
            pair_panel = x.get("pair_conditional_mi_bits")
            physical = {} if pair_panel is None else pair_panel["physical"]
            return int(x["r_ind"][key]), list(x["certifying_subsets"][key]), physical

    else:
        raise ValueError("pointer must be Z or X")

    for index, row in enumerate(certification_rows):
        redundancy, subset, pair_information = panel(row)
        if redundancy < MIN_REDUNDANCY:
            continue
        consecutive = 0
        for later in certification_rows[index:]:
            later_redundancy, _, _ = panel(later)
            if later_redundancy < MIN_REDUNDANCY:
                break
            consecutive += 1
        witness_pairs = {
            _pair_key(left, right): float(pair_information[_pair_key(left, right)])
            for left, right in itertools.combinations(subset, 2)
        }
        return {
            "step": int(row["step"]),
            "jt": float(row["jt"]),
            "theta_star": float(row["theta"]),
            "r_ind": redundancy,
            "subset": subset,
            "witness_pair_values": witness_pairs,
            "consecutive_samples": consecutive,
            "persistence": consecutive >= PERSISTENCE_SAMPLES,
            "persistence_label": (
                "PERSISTENT-FINITE-TIME"
                if consecutive >= PERSISTENCE_SAMPLES
                else "TRANSIENT-ONSET"
            ),
            "pointer_z_tv": float(row["pointer_z"]["tv_from_t0"]),
            "Q_quiet": float(row["Q_quiet"]),
            "<X>_face": float(row["<X>_face"]),
        }
    return None


def _shell_crossings(rows: Sequence[Mapping[str, object]]) -> dict[str, float | None]:
    result: dict[str, float | None] = {"face": None, "edge": None, "corner": None}
    for row in rows:
        for role in result:
            if (
                result[role] is None
                and float(row["shell_excess_profile"][role]) + NUMERIC_GATE_TOL
                >= EPS_EXCESS
            ):
                result[role] = float(row["jt"])
    return result


def _shell_order_ok(crossings: Mapping[str, float | None]) -> bool:
    values = [
        math.inf if crossings[role] is None else float(crossings[role])
        for role in ("face", "edge", "corner")
    ]
    return bool(values[0] <= values[1] <= values[2])


def _profile_summary(rows: Sequence[Mapping[str, object]]) -> dict[str, object]:
    if not rows:
        raise ValueError("cannot profile an empty trace")
    totals = np.asarray(
        [float(row["sum_fragment_excess_bits"]) for row in rows], dtype=np.float64
    )
    if not np.all(np.isfinite(totals)):
        raise RuntimeError("nonfinite fragment-excess profile")
    index = int(np.argmax(totals))
    row = rows[index]
    return {
        "step": int(row["step"]),
        "jt": float(row["jt"]),
        "sum_fragment_excess_bits": float(totals[index]),
        "shell_excess_profile": dict(row["shell_excess_profile"]),
        "xi_reg": row["xi_reg"],
        "Q_quiet": float(row["Q_quiet"]),
        "<X>_face": float(row["<X>_face"]),
    }


def _trace_summary(case: Mapping[str, object]) -> dict[str, object]:
    rows = [dict(row) for row in case["rows"]]
    ground = dict(case["ground"])
    events = {DELTA_KEYS[delta]: _first_event(rows, delta) for delta in DELTAS}
    x_events = {
        DELTA_KEYS[delta]: _first_event(rows, delta, pointer="X")
        for delta in DELTAS
    }
    crossings = _shell_crossings(rows)
    diagnostics = {
        "ground_residual": max(float(value) for value in ground["residuals"]),
        "ground_norm_error": max(float(value) for value in ground["norm_errors"]),
        "ground_overlap": float(ground["overlap"]),
        "norm_error": max(
            float(row["diagnostics"]["relative_norm_error"]) for row in rows
        ),
        "entropy_bound_error": max(
            float(row["diagnostics"]["entropy_bound_error"]) for row in rows
        ),
        "density_error": max(
            max(float(value) for value in row["diagnostics"]["density_errors"].values())
            for row in rows
        ),
        "symmetry_error": max(
            float(row["diagnostics"]["symmetry_consistency"]["maximum"])
            for row in rows
        ),
        "rss_peak_gb": max(float(row["diagnostics"]["rss_peak_gb"]) for row in rows),
    }
    return {
        "lam": float(ground["lam"]),
        "rows": rows,
        "ground": ground,
        "events": events,
        "x_events": x_events,
        "headline": events[DELTA_KEYS[HEADLINE_DELTA]],
        "shell_crossings": crossings,
        "shell_order": _shell_order_ok(crossings),
        "profile": _profile_summary(rows),
        "t0_information_error": _row_t0_information_error(rows[0]),
        "diagnostics": diagnostics,
    }


def _dt_halving_summary(
    coarse_case: Mapping[str, object], fine_case: Mapping[str, object]
) -> dict[str, object]:
    coarse_rows = [
        row
        for row in coarse_case["rows"]
        if float(row["jt"]) <= FINE_T_FINAL + NUMERIC_GATE_TOL
    ]
    fine_rows = [dict(row) for row in fine_case["rows"]]
    coarse = _first_event(coarse_rows, HEADLINE_DELTA)
    fine = _first_event(fine_rows, HEADLINE_DELTA)
    if coarse is None and fine is None:
        return {
            "gate": True,
            "status": "NO-EVENT-BOTH-PHYSICS-ABSENCE",
            "onset_shift": None,
            "theta_relative_shift": None,
        }
    if (coarse is None) != (fine is None):
        return {
            "gate": False,
            "status": "EVENT-MISMATCH",
            "onset_shift": None,
            "theta_relative_shift": None,
        }
    assert coarse is not None and fine is not None
    onset_shift = abs(float(coarse["jt"]) - float(fine["jt"]))
    coarse_theta = float(coarse["theta_star"])
    fine_theta = float(fine["theta_star"])
    theta_shift = (
        float("inf")
        if coarse_theta == 0.0 or not np.isfinite(coarse_theta + fine_theta)
        else abs(fine_theta - coarse_theta) / abs(coarse_theta)
    )
    gate = bool(
        onset_shift <= DT_ONSET_SHIFT_TOL + NUMERIC_GATE_TOL
        and theta_shift <= DT_THETA_RELATIVE_TOL + NUMERIC_GATE_TOL
    )
    return {
        "gate": gate,
        "status": "OK" if gate else "SHIFT-FAIL",
        "onset_shift": onset_shift,
        "theta_relative_shift": theta_shift,
        "coarse": coarse,
        "fine": fine,
    }


def _median_theta(
    summaries: Sequence[Mapping[str, object]], delta: float
) -> float | None:
    if not summaries:
        return None
    key = DELTA_KEYS[delta]
    values: list[float] = []
    for summary in summaries:
        event = summary["events"][key]
        if event is None:
            return None
        value = float(event["theta_star"])
        if not np.isfinite(value):
            return None
        values.append(value)
    return float(np.median(np.asarray(values, dtype=np.float64)))


def _analyze_cases(
    cases: Mapping[float, Mapping[str, object]],
    fine_case: Mapping[str, object],
    *,
    preflight: Mapping[str, object],
    elapsed_seconds: float,
) -> dict[str, object]:
    if set(cases) != set(LAMBDAS):
        raise RuntimeError("claim-bearing lambda set is incomplete")
    summaries = [_trace_summary(cases[lam]) for lam in LAMBDAS]
    by_lam = {float(summary["lam"]): summary for summary in summaries}
    fine_summary = _trace_summary(fine_case)

    check_01 = all(
        float(summary["t0_information_error"]) <= MACHINERY_TOL
        and summary["ground"]["stationary_event_counts"]["Z"] == [0, 0, 0]
        and summary["ground"]["stationary_event_counts"]["X"] == [0, 0, 0]
        and float(summary["ground"]["stationary_observable_max_deviation"])
        <= MACHINERY_TOL
        for summary in summaries
    )

    demolition_ok = all(bool(summary["ground"]["demolition"]["gate"]) for summary in summaries)
    drift_ok = all(
        summary["headline"] is None
        or float(summary["headline"]["pointer_z_tv"])
        <= POINTER_DRIFT_LIMIT + NUMERIC_GATE_TOL
        for summary in summaries
    )
    x_control_ok = all(
        event is None or float(event["jt"]) > HEADLINE_TIME + NUMERIC_GATE_TOL
        for summary in summaries
        for event in summary["x_events"].values()
    )
    check_02 = demolition_ok and drift_ok and x_control_ok

    full_certification_ledger: dict[float, dict[str, object]] = {}
    for summary in summaries:
        delta_hits: dict[str, dict[str, object]] = {}
        all_deltas_by_deadline = True
        for delta in DELTAS:
            key = DELTA_KEYS[delta]
            event = summary["events"][key]
            by_deadline = bool(
                event is not None
                and int(event["r_ind"]) >= MIN_REDUNDANCY
                and float(event["jt"]) <= HEADLINE_TIME + NUMERIC_GATE_TOL
            )
            delta_hits[key] = {
                "first_hit_jt": None if event is None else float(event["jt"]),
                "first_hit_r_ind": None if event is None else int(event["r_ind"]),
                "by_jt_1": by_deadline,
            }
            all_deltas_by_deadline = all_deltas_by_deadline and by_deadline
        headline = summary["headline"]
        headline_persistence = bool(
            headline is not None and bool(headline["persistence"])
        )
        lam = float(summary["lam"])
        full_certification_ledger[lam] = {
            "delta_first_hits": delta_hits,
            "all_deltas_by_jt_1": all_deltas_by_deadline,
            "headline_consecutive_samples": None
            if headline is None
            else int(headline["consecutive_samples"]),
            "headline_persistence": headline_persistence,
            "full_certification": bool(
                all_deltas_by_deadline and headline_persistence
            ),
        }
    w_full = tuple(
        lam
        for lam in LAMBDAS
        if bool(full_certification_ledger[lam]["full_certification"])
    )
    window_size_ok = len(w_full) >= 2
    locality_ok = all(bool(summary["shell_order"]) for summary in summaries)
    witness_ok = all(
        summary["headline"] is None
        or (
            bool(summary["headline"]["witness_pair_values"])
            and all(
                float(value) <= ETA_INDEPENDENCE + NUMERIC_GATE_TOL
                for value in summary["headline"]["witness_pair_values"].values()
            )
        )
        for summary in summaries
    )
    check_03 = window_size_ok and locality_ok and witness_ok and drift_ok

    window_summaries = [by_lam[lam] for lam in w_full]
    delta_medians = {
        DELTA_KEYS[delta]: _median_theta(window_summaries, delta)
        for delta in DELTAS
    }
    median_values = np.asarray(
        [
            math.nan if delta_medians[DELTA_KEYS[delta]] is None else delta_medians[DELTA_KEYS[delta]]
            for delta in DELTAS
        ],
        dtype=np.float64,
    )
    delta_factor = (
        float(np.max(median_values) / np.min(median_values))
        if np.all(np.isfinite(median_values)) and np.all(median_values > 0.0)
        else float("inf")
    )
    tolerance_stability_ok = bool(
        np.all(np.isfinite(median_values))
        and np.all(median_values > 0.0)
        and delta_factor < DELTA_FACTOR_LIMIT
    )
    headline_window_values = [
        float(summary["headline"]["theta_star"])
        for summary in window_summaries
    ]
    field_factor = (
        float(max(headline_window_values) / min(headline_window_values))
        if headline_window_values
        and all(np.isfinite(value) and value > 0.0 for value in headline_window_values)
        else float("inf")
    )
    field_stability_ok = bool(field_factor < DELTA_FACTOR_LIMIT)
    check_04 = tolerance_stability_ok and field_stability_ok

    bar_cases: dict[float, dict[str, object]] = {}
    headline_values: list[float] = []
    below_window = False
    for summary in window_summaries:
        event = summary["headline"]
        assert event is not None
        theta = float(event["theta_star"])
        headline_values.append(theta)
        status = "inside" if theta >= BAR_WINDOW_FLOOR else "BAR-BELOW-WINDOW"
        below_window = below_window or status == "BAR-BELOW-WINDOW"
        bar_cases[float(summary["lam"])] = {"theta_star": theta, "status": status}
    if not headline_values:
        check_05 = "unavailable"
        headline_median = None
        headline_range = (None, None)
    else:
        check_05 = "BAR-BELOW-WINDOW" if below_window else "inside"
        headline_median = float(np.median(np.asarray(headline_values)))
        headline_range = (min(headline_values), max(headline_values))

    window_indices = [index for index, lam in enumerate(LAMBDAS) if lam in w_full]
    noncontiguous_window = bool(
        window_indices
        and window_indices
        != list(range(min(window_indices), max(window_indices) + 1))
    )
    if not w_full:
        boundary: tuple[float, float] | str = "unavailable"
    else:
        max_certified = max(w_full)
        noncertified_above = [
            lam for lam in LAMBDAS if lam > max_certified and lam not in w_full
        ]
        boundary = (
            (max_certified, min(noncertified_above))
            if noncertified_above
            else "not-bracketed-above-0.20"
        )
    risk_signatures = {
        "full_certification_ledger": full_certification_ledger,
        "NONCONTIGUOUS-WINDOW": noncontiguous_window,
    }

    dt_halving = _dt_halving_summary(by_lam[FINE_LAM], fine_summary)
    diagnostic_sets = [summary["diagnostics"] for summary in summaries] + [
        fine_summary["diagnostics"]
    ]
    machinery_values = {
        "ground_residual": max(float(values["ground_residual"]) for values in diagnostic_sets),
        "ground_norm_error": max(float(values["ground_norm_error"]) for values in diagnostic_sets),
        "ground_overlap": max(float(values["ground_overlap"]) for values in diagnostic_sets),
        "norm_error": max(float(values["norm_error"]) for values in diagnostic_sets),
        "entropy_bound_error": max(float(values["entropy_bound_error"]) for values in diagnostic_sets),
        "density_error": max(float(values["density_error"]) for values in diagnostic_sets),
        "symmetry_error": max(float(values["symmetry_error"]) for values in diagnostic_sets),
        "rss_peak_gb": max(
            float(orbit_engine.rss_gb()),
            max(float(values["rss_peak_gb"]) for values in diagnostic_sets),
        ),
        "elapsed_seconds": float(elapsed_seconds),
        "dt_halving": dt_halving,
        "preflight": dict(preflight),
    }
    machinery = bool(
        bool(preflight["gate"])
        and float(machinery_values["ground_residual"]) <= GROUND_RESIDUAL_TOL
        and float(machinery_values["ground_norm_error"]) <= MACHINERY_TOL
        and float(machinery_values["ground_overlap"]) <= MACHINERY_TOL
        and float(machinery_values["norm_error"]) <= MACHINERY_TOL
        and float(machinery_values["entropy_bound_error"]) <= MACHINERY_TOL
        and float(machinery_values["density_error"]) <= MACHINERY_TOL
        and float(machinery_values["symmetry_error"]) <= MACHINERY_TOL
        and float(machinery_values["rss_peak_gb"]) < FULL_RSS_GB
        and float(elapsed_seconds) < FULL_WALL_SECONDS
        and bool(dt_halving["gate"])
    )
    if not machinery or not check_01:
        verdict, exit_code = "MACHINERY-FAIL", 2
    elif not (check_02 and check_03 and check_04):
        verdict, exit_code = "BAR-NOT-PINNED", 1
    else:
        verdict, exit_code = "BAR-DERIVED-EFFECTIVE", 0
    return {
        "summaries": summaries,
        "fine_summary": fine_summary,
        "check_01": check_01,
        "check_02": check_02,
        "check_02_parts": {
            "demolition": demolition_ok,
            "pointer_drift": drift_ok,
            "x_control": x_control_ok,
        },
        "check_03": check_03,
        "check_03_parts": {
            "window_size": window_size_ok,
            "locality": locality_ok,
            "event_witness": witness_ok,
            "event_drift": drift_ok,
        },
        "check_04": check_04,
        "check_04_parts": {
            "tolerance_stability": tolerance_stability_ok,
            "field_stability": field_stability_ok,
        },
        "check_05": check_05,
        "delta_medians": delta_medians,
        "delta_factor": delta_factor,
        "field_factor": field_factor,
        "bar_cases": bar_cases,
        "headline_median": headline_median,
        "headline_range": headline_range,
        "below_window": below_window,
        "w_full": w_full,
        "boundary": boundary,
        "noncontiguous_window": noncontiguous_window,
        "risk_signatures": risk_signatures,
        "machinery": machinery,
        "machinery_values": machinery_values,
        "verdict": verdict,
        "exit_code": exit_code,
    }


def _format_demolition(panel: Mapping[str, object]) -> str:
    return ",".join(
        f"{name}:Z={_fmt(values['Z'])}/X={_fmt(values['X'])}/Y={_fmt(values['Y'])}"
        for name, values in panel["classes"].items()
    )


def _format_boundary(boundary: tuple[float, float] | str) -> str:
    if isinstance(boundary, str):
        return f"({boundary})"
    return f"({_fmt(boundary[0])},{_fmt(boundary[1])})"


def _six_output_lines(
    result: Mapping[str, object], identity: RunIdentity
) -> list[str]:
    summaries = list(result["summaries"])
    preflight = result["machinery_values"]["preflight"]
    setup = (
        "SETUP geometry=open-3x3x3 N=27 J=1 open "
        "H=-sum_<ij>ZiZj-lambda*sum_iXi lambda=[0.02,0.05,0.10,0.20] "
        "prep=center+faces:+X,edges+corners:+Z route=C "
        "fragments=[5,5,4,4,4,4] grid=0:0.1:10 "
        f"T_C={_fmt_vector(PAIR_MAIN_TIMES)} fine=lambda0.10/0:0.05:1.10 "
        "pointer=Z_center excess-anchor=trajectory-t0 doublet=stationary-control+diagnostic-only "
        f"protocol_hash={identity.protocol_hash} descriptor={identity.fragment_descriptor_checksum} "
        f"{SPEC_NOTE}"
    )

    event_parts: list[str] = []
    for summary in summaries:
        counts = [
            int(summary["events"][DELTA_KEYS[delta]] is not None) for delta in DELTAS
        ]
        event = summary["headline"]
        if event is None:
            headline = "none"
        else:
            headline = (
                f"t={_fmt(event['jt'])}/theta*={_fmt(event['theta_star'])}/"
                f"R={event['r_ind']}/subset={event['subset']}/"
                f"run={event['consecutive_samples']}/{event['persistence_label']}"
            )
        event_parts.append(
            f"lambda={float(summary['lam']):g}:N={counts},d0.10={headline}"
        )
    events = (
        "EVENTS N-order=delta[0.05,0.10,0.20] first-certification-sampled-hit; "
        + "; ".join(event_parts)
    )

    profile_parts: list[str] = []
    demolition_parts: list[str] = []
    for summary in summaries:
        profile = summary["profile"]
        shells = profile["shell_excess_profile"]
        crossings = summary["shell_crossings"]
        profile_parts.append(
            f"lambda={float(summary['lam']):g}:t_summax={_fmt(profile['jt'])}/"
            f"DeltaChi[face,edge,corner]={_fmt_vector([shells['face'],shells['edge'],shells['corner']])}/"
            f"cross={_fmt_vector([crossings['face'],crossings['edge'],crossings['corner']])}/"
            f"sum={_fmt(profile['sum_fragment_excess_bits'])}/xi={_fmt(profile['xi_reg'])}/"
            f"Q={_fmt(profile['Q_quiet'])}/Xface={_fmt(profile['<X>_face'])}"
        )
        demolition_parts.append(
            f"lambda={float(summary['lam']):g}[{_format_demolition(summary['ground']['demolition'])}]"
        )
    timings = preflight["timings_seconds"]
    profile_line = (
        "PROFILE+DEMOLITION "
        + "; ".join(profile_parts)
        + "; centered-Frobenius="
        + ";".join(demolition_parts)
        + f"; preflight[k4,k5,q9,q10,q11]={_fmt_vector([timings[name] for name in ('k4','k5','q9','q10','q11')])}s"
        + f" projected={float(preflight['projected_wall_seconds'])/3600.0:.4g}h/"
        f"{_fmt(preflight['projected_rss_gb'])}GiB gate={preflight['gate']}"
    )

    delta_parts = ",".join(
        f"d={delta:g}:{_fmt(result['delta_medians'][DELTA_KEYS[delta]])}"
        for delta in DELTAS
    )
    bar_parts = "; ".join(
        f"lambda={lam:g}:theta*={_fmt(result['bar_cases'][lam]['theta_star'])}/"
        f"{result['bar_cases'][lam]['status']}"
        for lam in result["w_full"]
    )
    bar = (
        f"BAR delta-medians={delta_parts} factor={_fmt(result['delta_factor'])}(<1.5); "
        f"field-factor={_fmt(result['field_factor'])}(<1.5); "
        f"headline {bar_parts if bar_parts else 'unavailable'}; "
        f"median={_fmt(result['headline_median'])} "
        f"range={_fmt_vector(result['headline_range'])}; "
        f"window={_fmt_vector(result['w_full'])} "
        f"boundary={_format_boundary(result['boundary'])}"
    )

    machinery = result["machinery_values"]
    dt_panel = machinery["dt_halving"]
    checks = (
        f"CHECKS+MACHINERY CHECK-01={'ok' if result['check_01'] else 'FAIL'} "
        f"CHECK-02={'ok' if result['check_02'] else 'FAIL'}"
        f"(comm={result['check_02_parts']['demolition']},drift={result['check_02_parts']['pointer_drift']},X={result['check_02_parts']['x_control']}) "
        f"CHECK-03={'ok' if result['check_03'] else 'FAIL'}"
        f"(window-size={result['check_03_parts']['window_size']},locality={result['check_03_parts']['locality']},witness={result['check_03_parts']['event_witness']},drift={result['check_03_parts']['event_drift']}) "
        f"CHECK-04={'ok' if result['check_04'] else 'FAIL'}"
        f"(tolerance={result['check_04_parts']['tolerance_stability']},field={result['check_04_parts']['field_stability']}) "
        f"CHECK-05={result['check_05']} "
        f"MACHINERY={'ok' if result['machinery'] else 'FAIL'}"
        f"(GSres={float(machinery['ground_residual']):.2e},norm={float(machinery['norm_error']):.2e},"
        f"entropy={float(machinery['entropy_bound_error']):.2e},density={float(machinery['density_error']):.2e},"
        f"symmetry={float(machinery['symmetry_error']):.2e},dt={dt_panel['status']}/"
        f"shift={_fmt(dt_panel['onset_shift'])}/theta-rel={_fmt(dt_panel['theta_relative_shift'])},"
        f"RSS={_fmt(machinery['rss_peak_gb'])}GiB,wall={float(machinery['elapsed_seconds'])/3600.0:.4g}h)"
    )

    failed = [
        name
        for name, passed in (
            ("CHECK-01", result["check_01"]),
            ("CHECK-02", result["check_02"]),
            ("CHECK-03", result["check_03"]),
            ("CHECK-04", result["check_04"]),
            ("MACHINERY", result["machinery"]),
        )
        if not passed
    ]
    flags = ["BAR-BELOW-WINDOW"] if result["below_window"] else []
    if result["noncontiguous_window"]:
        flags.append("NONCONTIGUOUS-WINDOW")
    persistence_values = [
        summary["headline"] is not None and summary["headline"]["persistence"]
        for summary in summaries
    ]
    persistence = (
        "all"
        if all(persistence_values)
        else "partial"
        if any(persistence_values)
        else "none"
    )
    total = (
        f"TOTAL {result['verdict']} theta*={_fmt(result['headline_median'])} "
        f"window={_fmt_vector(result['w_full'])} "
        f"boundary={_format_boundary(result['boundary'])} persistence={persistence} "
        f"flags={','.join(flags) if flags else 'none'} "
        f"failed={','.join(failed) if failed else 'none'} {SPEC_NOTE}"
    )
    lines = [setup, events, profile_line, bar, checks, total]
    if len(lines) != 6:
        raise AssertionError("six-line stdout contract construction failed")
    return [_with_boundaries(line) for line in lines]


def _failure_lines(mode: str, exc: BaseException) -> list[str]:
    message = " ".join(str(exc).split())[:400]
    methods_label = " SLAB-METHODS-ONLY" if "SLAB-METHODS-ONLY" in mode else ""
    lines = [
        f"SETUP{methods_label} mode={mode} status=incomplete {SPEC_NOTE}",
        f"EVENTS{methods_label} unavailable",
        f"PROFILE+DEMOLITION{methods_label} unavailable",
        f"BAR{methods_label} unavailable",
        f"CHECKS+MACHINERY{methods_label} MACHINERY=FAIL error={type(exc).__name__}:{message}",
        f"TOTAL MACHINERY-FAIL{methods_label} theta*=unavailable window=[] boundary=(unavailable) persistence=unavailable failed=MACHINERY {SPEC_NOTE}",
    ]
    return [_with_boundaries(line) for line in lines]


def _json_safe(value: object) -> object:
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    if isinstance(value, np.floating):
        number = float(value)
        return number if np.isfinite(number) else None
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


def _result_cache_summary(result: Mapping[str, object]) -> dict[str, object]:
    summaries = []
    for summary in result["summaries"]:
        summaries.append(
            {
                "lam": summary["lam"],
                "events": summary["events"],
                "x_events": summary["x_events"],
                "headline": summary["headline"],
                "shell_crossings": summary["shell_crossings"],
                "shell_order": summary["shell_order"],
                "profile": summary["profile"],
                "t0_information_error": summary["t0_information_error"],
                "diagnostics": summary["diagnostics"],
                "ground": {
                    key: summary["ground"][key]
                    for key in (
                        "lam",
                        "energies",
                        "splitting",
                        "residuals",
                        "norm_errors",
                        "overlap",
                        "stationary_event_counts",
                        "role",
                    )
                },
            }
        )
    keys = (
        "check_01",
        "check_02",
        "check_02_parts",
        "check_03",
        "check_03_parts",
        "check_04",
        "check_04_parts",
        "check_05",
        "delta_medians",
        "delta_factor",
        "field_factor",
        "bar_cases",
        "headline_median",
        "headline_range",
        "below_window",
        "w_full",
        "boundary",
        "noncontiguous_window",
        "risk_signatures",
        "machinery",
        "machinery_values",
        "verdict",
        "exit_code",
    )
    payload = {key: result[key] for key in keys}
    payload["summaries"] = summaries
    return _json_safe(payload)  # type: ignore[return-value]


def _write_report_cache(
    *,
    identity: RunIdentity,
    basis_checksum: str,
    lookup_checksum: str,
    result: Mapping[str, object],
    lines: Sequence[str],
) -> None:
    payload: dict[str, object] = {
        "schema": REPORT_SCHEMA,
        "protocol_hash": identity.protocol_hash,
        "parent_protocol_hash": identity.parent_protocol_hash,
        "basis_checksum": basis_checksum,
        "fragment_descriptor_checksum": identity.fragment_descriptor_checksum,
        "raw_to_orbit_checksum": lookup_checksum,
        "boundary_sentences": list(identity.boundary_sentences),
        "preparation_bloch_vectors": _preparation_json(),
        "stdout_lines": list(lines),
        "result": _result_cache_summary(result),
        "spec_note": SPEC_NOTE,
    }
    if REPORT_CACHE_PATH.exists():
        with REPORT_CACHE_PATH.open("r", encoding="utf-8") as handle:
            existing = json.load(handle)
        identity_ok = (
            existing.get("schema") == REPORT_SCHEMA
            and existing.get("protocol_hash") == identity.protocol_hash
            and existing.get("parent_protocol_hash") == identity.parent_protocol_hash
            and existing.get("basis_checksum") == basis_checksum
            and existing.get("fragment_descriptor_checksum")
            == identity.fragment_descriptor_checksum
            and existing.get("raw_to_orbit_checksum") == lookup_checksum
            and existing.get("boundary_sentences") == list(identity.boundary_sentences)
        )
        if not identity_ok:
            raise RuntimeError("existing report cache identity mismatch")
    _atomic_write_json(REPORT_CACHE_PATH, payload)


def _load_preflight(
    *,
    identity: RunIdentity,
    basis_checksum: str,
    lookup_checksum: str,
) -> dict[str, object]:
    if not PREFLIGHT_CACHE_PATH.exists():
        raise FileNotFoundError("missing frozen cube gather preflight artifact")
    with PREFLIGHT_CACHE_PATH.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    exact = (
        payload.get("schema") == PREFLIGHT_SCHEMA
        and payload.get("protocol_hash") == identity.protocol_hash
        and payload.get("parent_protocol_hash") == identity.parent_protocol_hash
        and payload.get("basis_checksum") == basis_checksum
        and payload.get("fragment_descriptor_checksum")
        == identity.fragment_descriptor_checksum
        and payload.get("raw_to_orbit_checksum") == lookup_checksum
        and payload.get("boundary_sentences") == list(identity.boundary_sentences)
        and payload.get("preparation_bloch_vectors") == _preparation_json()
        and float(payload.get("weighted_units", math.nan)) == FROZEN_WEIGHTED_UNITS
    )
    if not exact:
        raise RuntimeError("preflight artifact identity mismatch")
    return payload


def _load_report_case(
    *,
    identity: RunIdentity,
    lam: float,
    dt: float,
    n_steps: int,
    fine: bool,
) -> tuple[dict[str, object], str, str]:
    prefix = _trace_prefix(lam, fine=fine)
    run_kind = "cube-dt-halving" if fine else "cube-full"
    rows = _read_stream(
        _stream_path(lam, fine=fine),
        identity=identity,
        expected_lam=lam,
        expected_dt=dt,
        expected_kind=run_kind,
        expected_basis_checksum=None,
    )
    if [int(row["step"]) for row in rows] != list(range(n_steps + 1)):
        raise RuntimeError(f"observable stream {prefix} is incomplete")
    basis_checksum = str(rows[0]["basis_checksum"])
    lookup_checksum = str(rows[0]["raw_to_orbit_checksum"])
    if any(
        row["basis_checksum"] != basis_checksum
        or row["raw_to_orbit_checksum"] != lookup_checksum
        for row in rows
    ):
        raise RuntimeError(f"observable stream {prefix} changes basis/lookup identity")
    checkpoint_path = _newest_checkpoint_path(prefix)
    if checkpoint_path is None:
        raise FileNotFoundError(f"missing checkpoint for {prefix}")
    checkpoint = _load_trace_checkpoint(
        checkpoint_path,
        identity=identity,
        expected_prefix=prefix,
        expected_lam=lam,
        expected_dt=dt,
        expected_n_steps=n_steps,
        expected_basis_checksum=basis_checksum,
        expected_lookup_checksum=lookup_checksum,
        expected_initial_checksum=None,
        expected_state_size=None,
        load_state=False,
    )
    if int(checkpoint["step"]) != n_steps:
        raise RuntimeError(f"newest checkpoint for {prefix} is not complete")
    if _json_dumps(checkpoint["rows"]) != _json_dumps(rows):
        raise RuntimeError(f"checkpoint/stream normalized JSON mismatch for {prefix}")
    ground = dict(checkpoint["ground"])
    if (
        ground.get("protocol_hash") != identity.protocol_hash
        or ground.get("parent_protocol_hash") != identity.parent_protocol_hash
        or ground.get("basis_checksum") != basis_checksum
        or ground.get("fragment_descriptor_checksum")
        != identity.fragment_descriptor_checksum
        or ground.get("boundary_sentences") != list(identity.boundary_sentences)
    ):
        raise RuntimeError(f"checkpoint ground metadata identity mismatch for {prefix}")
    completion_wall = float(checkpoint["metadata"].get("run_wall_seconds", math.nan))
    if not np.isfinite(completion_wall) or completion_wall < 0.0:
        raise RuntimeError(f"checkpoint {prefix} lacks valid cumulative wall metadata")
    return {
        "rows": rows,
        "ground": ground,
        "completion_wall_seconds": completion_wall,
    }, basis_checksum, lookup_checksum


def run_full() -> int:
    _require_engine_api()
    identity = _identity()
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    run_started = time.monotonic()
    basis = orbit_engine.build_orbit_basis()
    tables = orbit_engine.build_hamiltonian_tables(basis)
    if (
        basis.geometry_name != "open-3x3x3"
        or basis.n_orbits != orbit_engine.EXPECTED_CUBE_ORBITS
    ):
        raise AssertionError("claim-bearing basis is not the verified open 3x3x3 cube")
    if basis.cache_status != "loaded" or tables.cache_status != "loaded":
        raise RuntimeError(
            "--full requires warm validated basis/Hamiltonian tables; cache reconstruction belongs to --validate"
        )
    tables = engine_ext.center_bond_runtime_tables(basis, tables)
    descriptors = engine_ext.verify_fragment_descriptors()
    if descriptors.checksum != identity.fragment_descriptor_checksum:
        raise AssertionError("fragment descriptor checksum changed during setup")
    lookup = engine_ext.get_raw_to_orbit_lookup(basis, budget_gb=FULL_RSS_GB)
    initial = engine_ext.class_product_state(basis, **_preparation_amplitudes())
    preflight = _cube_preflight(
        identity=identity,
        basis=basis,
        lookup=lookup,
        initial=initial,
        budget_gb=FULL_RSS_GB,
    )
    if not bool(preflight["gate"]):
        raise RuntimeError(
            "launch preflight gate failed: "
            f"projected wall={float(preflight['projected_wall_seconds'])/3600.0:.4g}h "
            f"(limit 13.5h), RSS={float(preflight['projected_rss_gb']):.3f}GiB "
            "(limit 8GiB); frozen grids and pair classes were not changed"
        )

    ground_metadata: dict[float, dict[str, object]] = {}
    for lam in LAMBDAS:
        states, metadata = _load_or_build_ground_doublet(
            identity=identity,
            basis=basis,
            tables=tables,
            lookup=lookup,
            lam=lam,
            budget_gb=FULL_RSS_GB,
            allow_build=False,
        )
        ground_metadata[lam] = metadata
        del states

    total_units = len(LAMBDAS) * (N_STEPS + 1) + FINE_N_STEPS + 1
    cases: dict[float, dict[str, object]] = {}
    wall_offset = 0.0
    for index, lam in enumerate(LAMBDAS):
        cases[lam] = _run_trace(
            identity=identity,
            basis=basis,
            tables=tables,
            lookup=lookup,
            lam=lam,
            dt=DT,
            n_steps=N_STEPS,
            fine=False,
            initial=initial,
            ground_metadata=ground_metadata[lam],
            run_started=run_started,
            progress_base_units=index * (N_STEPS + 1),
            progress_total_units=total_units,
            wall_offset_seconds=wall_offset,
        )
        wall_offset = max(wall_offset, float(cases[lam]["wall_offset_seconds"]))
        if _SIGTERM_PENDING:
            raise SigtermRequested("SIGTERM received between lambda traces")
    fine_case = _run_trace(
        identity=identity,
        basis=basis,
        tables=tables,
        lookup=lookup,
        lam=FINE_LAM,
        dt=FINE_DT,
        n_steps=FINE_N_STEPS,
        fine=True,
        initial=initial,
        ground_metadata=ground_metadata[FINE_LAM],
        run_started=run_started,
        progress_base_units=len(LAMBDAS) * (N_STEPS + 1),
        progress_total_units=total_units,
        wall_offset_seconds=wall_offset,
    )
    elapsed = float(fine_case["completion_wall_seconds"])
    result = _analyze_cases(
        cases, fine_case, preflight=preflight, elapsed_seconds=elapsed
    )
    lines = _six_output_lines(result, identity)
    _write_report_cache(
        identity=identity,
        basis_checksum=basis.checksum,
        lookup_checksum=lookup.checksum,
        result=result,
        lines=lines,
    )
    for line in lines:
        print(line)
    return int(result["exit_code"])


def run_report() -> int:
    _require_engine_api()
    identity = _identity()
    prior_report: dict[str, object] | None = None
    if REPORT_CACHE_PATH.exists():
        with REPORT_CACHE_PATH.open("r", encoding="utf-8") as handle:
            prior_report = json.load(handle)
        if (
            prior_report.get("schema") != REPORT_SCHEMA
            or prior_report.get("protocol_hash") != identity.protocol_hash
            or prior_report.get("parent_protocol_hash")
            != identity.parent_protocol_hash
            or prior_report.get("fragment_descriptor_checksum")
            != identity.fragment_descriptor_checksum
            or prior_report.get("boundary_sentences") != list(identity.boundary_sentences)
        ):
            raise RuntimeError("report cache protocol/descriptor identity mismatch")

    cases: dict[float, dict[str, object]] = {}
    basis_checksum: str | None = None
    lookup_checksum: str | None = None
    for lam in LAMBDAS:
        case, local_basis, local_lookup = _load_report_case(
            identity=identity, lam=lam, dt=DT, n_steps=N_STEPS, fine=False
        )
        cases[lam] = case
        if basis_checksum is None:
            basis_checksum, lookup_checksum = local_basis, local_lookup
        elif basis_checksum != local_basis or lookup_checksum != local_lookup:
            raise RuntimeError("completed main traces use different basis/lookup identities")
    fine_case, fine_basis, fine_lookup = _load_report_case(
        identity=identity,
        lam=FINE_LAM,
        dt=FINE_DT,
        n_steps=FINE_N_STEPS,
        fine=True,
    )
    if basis_checksum != fine_basis or lookup_checksum != fine_lookup:
        raise RuntimeError("dt-halving trace identity differs from main traces")
    assert basis_checksum is not None and lookup_checksum is not None
    if prior_report is not None and (
        prior_report.get("basis_checksum") != basis_checksum
        or prior_report.get("raw_to_orbit_checksum") != lookup_checksum
    ):
        raise RuntimeError("report cache basis/lookup identity mismatch")
    preflight = _load_preflight(
        identity=identity,
        basis_checksum=basis_checksum,
        lookup_checksum=lookup_checksum,
    )
    elapsed = float(fine_case["completion_wall_seconds"])
    result = _analyze_cases(
        cases, fine_case, preflight=preflight, elapsed_seconds=elapsed
    )
    lines = _six_output_lines(result, identity)
    if prior_report is not None and prior_report.get("stdout_lines") != lines:
        raise RuntimeError("regenerated report is not byte-equivalent to report cache")
    _write_report_cache(
        identity=identity,
        basis_checksum=basis_checksum,
        lookup_checksum=lookup_checksum,
        result=result,
        lines=lines,
    )
    for line in lines:
        print(line)
    return int(result["exit_code"])


def _validation_lines(
    *,
    identity: RunIdentity,
    existing_dense: Mapping[str, object],
    extension_dense: Mapping[str, object],
    preflight: Mapping[str, object],
    ground_metadata: Sequence[Mapping[str, object]],
    t0_information_error: float,
    elapsed_seconds: float,
    machinery_ok: bool,
) -> list[str]:
    timings = preflight["timings_seconds"]
    setup = (
        "SETUP SLAB-METHODS-ONLY geometry=open-3x3x2 physics-claim=none "
        f"extension-maxdev={float(extension_dense['maximum_deviation']):.2e} "
        f"existing-maxdev={max(existing_dense['maximum_deviations'].values()):.2e} "
        f"protocol_hash={identity.protocol_hash} descriptor={identity.fragment_descriptor_checksum} {SPEC_NOTE}"
    )
    events = (
        "EVENTS SLAB-METHODS-ONLY no-physics-claim; cube-t0-product-error="
        f"{t0_information_error:.2e}; stationary-doublet-event-counts="
        + ";".join(
            f"lambda={float(metadata['lam']):g}:Z={metadata['stationary_event_counts']['Z']}/X={metadata['stationary_event_counts']['X']}"
            for metadata in ground_metadata
        )
    )
    profile = (
        "PROFILE+DEMOLITION SLAB-METHODS-ONLY cube-centered-Frobenius="
        + ";".join(
            f"lambda={float(metadata['lam']):g}[{_format_demolition(metadata['demolition'])}]/gate={metadata['demolition']['gate']}"
            for metadata in ground_metadata
        )
        + f"; preflight-gather-seconds[k4,k5,q9,q10,q11]={_fmt_vector([timings[name] for name in ('k4','k5','q9','q10','q11')])}"
    )
    bar = (
        "BAR SLAB-METHODS-ONLY unavailable no-physics-claim; "
        f"launch-projection={float(preflight['projected_wall_seconds'])/3600.0:.4g}h/"
        f"{float(preflight['projected_rss_gb']):.3f}GiB gate={preflight['gate']}"
    )
    checks = (
        "CHECKS+MACHINERY SLAB-METHODS-ONLY "
        f"class-product+k4+k5+q9+q10+q11+X+partial-trace+doublet-mix="
        f"{'ok' if float(extension_dense['maximum_deviation']) <= MACHINERY_TOL else 'FAIL'} "
        f"cube-CHECK-01={'ok' if t0_information_error <= MACHINERY_TOL else 'FAIL'} "
        f"preflight={'ok' if preflight['gate'] else 'FAIL'} "
        f"RSS={orbit_engine.rss_gb():.3f}GiB(<4) wall={elapsed_seconds:.1f}s(<1800)"
    )
    total = (
        f"TOTAL {'VALIDATION-PASS' if machinery_ok else 'MACHINERY-FAIL'} "
        f"SLAB-METHODS-ONLY no-physics-claim window=[] boundary=(unavailable) {SPEC_NOTE}"
    )
    return [_with_boundaries(line) for line in (setup, events, profile, bar, checks, total)]


def run_validate() -> int:
    _require_engine_api()
    identity = _identity()
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    extension_dense = engine_ext.dense_slab_extension_crosscheck()
    existing_dense = orbit_engine.dense_slab_crosscheck()
    engine_ext.clear_raw_to_orbit_lookup()

    basis = orbit_engine.build_orbit_basis()
    tables = orbit_engine.build_hamiltonian_tables(basis)
    if basis.geometry_name != "open-3x3x3":
        raise AssertionError("cube validation did not receive open 3x3x3 basis")
    tables = engine_ext.center_bond_runtime_tables(basis, tables)
    lookup = engine_ext.get_raw_to_orbit_lookup(
        basis, budget_gb=VALIDATION_RSS_GB
    )
    initial = engine_ext.class_product_state(basis, **_preparation_amplitudes())
    preflight = _cube_preflight(
        identity=identity,
        basis=basis,
        lookup=lookup,
        initial=initial,
        budget_gb=VALIDATION_RSS_GB,
    )
    metadata_by_lam: dict[float, dict[str, object]] = {}
    for lam in LAMBDAS:
        states, metadata = _load_or_build_ground_doublet(
            identity=identity,
            basis=basis,
            tables=tables,
            lookup=lookup,
            lam=lam,
            budget_gb=VALIDATION_RSS_GB,
            allow_build=True,
        )
        metadata_by_lam[lam] = metadata
        del states

    t0_row, _, _ = _measure_row(
        identity=identity,
        basis=basis,
        lookup=lookup,
        state=initial,
        ground_metadata=metadata_by_lam[FINE_LAM],
        baseline=None,
        run_kind="SLAB-METHODS-ONLY-CUBE-CHECK-01",
        lam=FINE_LAM,
        dt=DT,
        step=0,
        pair_sampled=True,
        include_x=True,
        reference_norm=float(np.linalg.norm(initial)),
        z_consecutive_previous={DELTA_KEYS[delta]: 0 for delta in DELTAS},
        x_consecutive_previous={DELTA_KEYS[delta]: 0 for delta in DELTAS},
        budget_gb=VALIDATION_RSS_GB,
    )
    t0_error = _row_t0_information_error(t0_row)
    elapsed = time.monotonic() - started
    ground_ok = all(
        max(float(value) for value in metadata["residuals"])
        <= GROUND_RESIDUAL_TOL
        and max(float(value) for value in metadata["norm_errors"])
        <= MACHINERY_TOL
        and float(metadata["overlap"]) <= MACHINERY_TOL
        and metadata["stationary_event_counts"]["Z"] == [0, 0, 0]
        and metadata["stationary_event_counts"]["X"] == [0, 0, 0]
        and bool(metadata["demolition"]["gate"])
        for metadata in metadata_by_lam.values()
    )
    machinery_ok = bool(
        float(extension_dense["maximum_deviation"]) <= MACHINERY_TOL
        and max(existing_dense["maximum_deviations"].values()) <= MACHINERY_TOL
        and t0_error <= MACHINERY_TOL
        and ground_ok
        and bool(preflight["gate"])
        and float(orbit_engine.rss_gb()) < VALIDATION_RSS_GB
        and elapsed < VALIDATION_WALL_SECONDS
    )
    lines = _validation_lines(
        identity=identity,
        existing_dense=existing_dense,
        extension_dense=extension_dense,
        preflight=preflight,
        ground_metadata=[metadata_by_lam[lam] for lam in LAMBDAS],
        t0_information_error=t0_error,
        elapsed_seconds=elapsed,
        machinery_ok=machinery_ok,
    )
    for line in lines:
        print(line)
    return 0 if machinery_ok else 2


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate, run, or report the frozen d=3 bar-location protocol."
    )
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--validate", action="store_true", help="methods validation (default)")
    modes.add_argument("--full", action="store_true", help="claim-bearing overnight cube run")
    modes.add_argument("--report", action="store_true", help="regenerate six lines from artifacts")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    if args.full:
        previous_handler = signal.signal(signal.SIGTERM, _sigterm_handler)
        try:
            return run_full()
        except SigtermRequested as exc:
            print(f"RUN-CHECKPOINTED {exc}", file=sys.stderr, flush=True)
            return 128 + signal.SIGTERM
        except Exception as exc:  # noqa: BLE001 - preserve six-line stdout.
            for line in _failure_lines("full", exc):
                print(line)
            return 2
        finally:
            signal.signal(signal.SIGTERM, previous_handler)
    if args.report:
        try:
            return run_report()
        except Exception as exc:  # noqa: BLE001 - preserve six-line stdout.
            for line in _failure_lines("report", exc):
                print(line)
            return 2
    try:
        return run_validate()
    except Exception as exc:  # noqa: BLE001 - validation also keeps six lines.
        for line in _failure_lines("validate-SLAB-METHODS-ONLY", exc):
            print(line)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
