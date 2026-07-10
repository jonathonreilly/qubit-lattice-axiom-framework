#!/usr/bin/env python3
"""Run the frozen d=3 registration-onset pilot.

The protocol is implemented from
``docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md``.  Numerical
evolution and local-state reconstruction are delegated to
``d3_cubic_orbit_engine_2026_07_09.py``.  Verdict conventions mirror (and
cite, but never import)
``scripts/registration_redundancy_onset_2026_07_09.py``: same-H ground-state
excess, ``eps_exc=0.02 bit``, ``H_floor=0.05 bit``, the declared delta sweep,
first-sampled hits, and the separation of physics absence from machinery
failure.

Full-run JSONL schema
---------------------
One compact JSON object is appended and fsynced for every sampled state.  The
three claim-bearing files are
``logs/runner-cache/d3_pilot_checkpoints/lam_<lambda>_observables.jsonl``;
the declared dt-halving subsample has the same schema in
``dt_half_lam_0p10_observables.jsonl``.  Every row contains:

``schema``
    Literal ``d3-registration-onset-observable-v1``.
``run_kind, geometry, lam, dt, step, jt``
    Trace identity and the exact sampled grid coordinate.
``pointer_z``
    ``p=[p(+),p(-)]``, binary entropy in bits, and total-variation drift from
    the preparation.  ``pointer_x`` is the same information for the
    demolition declaration through ``Jt<=1`` and is null later.
``fragments``
    All 26 exterior cube labels, each with coordinate, orbit/site class,
    Manhattan shell, ``chi_z_bits``, and the algebraic (unclipped)
    ``delta_chi_z_bits=chi-chi_GS``.  Symmetry-class representatives are
    contracted once by the engine and copied to their explicitly retained
    physical labels; the six axial labels remain separate graph vertices.
``axial_x``
    X-pointer axial Holevo/excess values used only by CHECK-02.
``pair_conditional_mi_bits``
    Opposite-axis and orthogonal-axis ``I(F_a:F_b|pointer)`` in bits.  Z
    values are always present.  X values are evaluated lazily exactly when
    an X singleton can pass a declared gate; null therefore means that
    singleton certification already failed and ``R_ind(X)=0``.
``r_ind, certifying_subsets, singleton_certifies``
    Largest pairwise-independent axial subset and its deterministic witness,
    plus pre-independence singleton gates, for each declared delta.
``center_bonds, theta``
    Six explicit centre-axis entries.  Each records purity,
    ``1-purity``, its same-lambda GS excess, and an exact local-Hamiltonian
    energy allocation.  ``theta`` is the unnormalised six-bond mean of the
    GS-subtracted ``1-purity`` values, without clipping.
``shell_delta_chi_bits, sum_delta_chi_bits, bond_profile``
    The streamed locality/profile inputs.  The bond activity is the frozen
    ``1-purity`` quantity used by the theta map; local field energy is shared
    over incident bonds so the allocation sums to the declared Hamiltonian.
``diagnostics``
    Relative norm error, entropy-bound violation, orbit-normalisation error,
    symmetry consistency (exact inside the invariant orbit sector), and any
    roundoff cleanup recorded by the entropy calculation.

Checkpoints are atomic, uncompressed ``npz`` files named
``<trace>_step_<NNN>.npz``.  They contain the state, its SHA-256 checksum,
the accumulated observable rows, the same-lambda ground/control metadata,
the initial-state checksum and reference norm, and exact trace coordinates.
They are written at step zero, every ten steps, completion, and from the
SIGTERM handler using the latest completed state.  Resume accepts only an
exact schema/basis/lambda/grid/checksum match.  No cache mismatch is silently
repaired.  ``--report`` reads the JSONL streams and final checkpoints and
does no state evolution or observable reconstruction.

The slab uses the engine's three exposed fragment classes as a labelled
six-axis methods surrogate so every event/observable/check path is exercised;
every validation output line is explicitly ``SLAB-METHODS-ONLY`` and carries
no physics claim.

This runner fixes a comparator, not a basis-neutral law: the Ising ``ZZ``
term and declared pointer privilege Z.  It supplies no formation rule, no
gravity claim, and no audit status.
"""

from __future__ import annotations

import argparse
import contextlib
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import io
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


# Import exactly the commissioned machinery module without creating an extra
# bytecode artifact in the repository.  The d=1 convention runner is cited in
# the docstring above and deliberately is not imported.
_OLD_DONT_WRITE_BYTECODE = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    import d3_cubic_orbit_engine_2026_07_09 as orbit_engine
finally:
    sys.dont_write_bytecode = _OLD_DONT_WRITE_BYTECODE


LAMBDAS = (0.05, 0.10, 0.20)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DT = 0.10
T_FINAL = 10.0
N_STEPS = 100
FINE_LAM = 0.10
FINE_DT = 0.05
FINE_T_FINAL = 2.0
FINE_N_STEPS = 40
HEADLINE_TIME = 1.0
EPS_EXCESS = 0.02
H_FLOOR = 0.05
ETA_INDEPENDENCE = 0.02
MIN_REDUNDANCY = 2
PERSISTENCE_SAMPLES = 3
SPARSE_WINDOW_FLOOR = 0.2
DELTA_FACTOR_LIMIT = 1.5
NUMERIC_GATE_TOL = 1.0e-10
GROUND_RESIDUAL_TOL = 1.0e-8
NORM_ERROR_TOL = 1.0e-9
ENTROPY_BOUND_TOL = 1.0e-9
SYMMETRY_TOL = 1.0e-9
DT_ONSET_SHIFT_TOL = 0.10
DT_THETA_RELATIVE_TOL = 0.05
VALIDATE_RSS_GB = 4.0
FULL_RSS_GB = 10.0
VALIDATE_WALL_SECONDS = 15.0 * 60.0

STREAM_SCHEMA = "d3-registration-onset-observable-v1"
CHECKPOINT_SCHEMA = "d3-registration-onset-checkpoint-v1"
GROUND_SCHEMA = "d3-registration-onset-ground-v1"
REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = REPO_ROOT / "logs" / "runner-cache" / "d3_pilot_checkpoints"

DELTA_KEYS = {delta: f"{delta:.2f}" for delta in DELTAS}
AXIAL_LABELS = (
    ("+x", (1, 0, 0)),
    ("-x", (-1, 0, 0)),
    ("+y", (0, 1, 0)),
    ("-y", (0, -1, 0)),
    ("+z", (0, 0, 1)),
    ("-z", (0, 0, -1)),
)
CLASS_ORDER = ("axial", "edge", "corner")
CLASS_SHELL = {"axial": 1, "edge": 2, "corner": 3}

PAULI_I = np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.complex128)
PAULI_X = np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
PAULI_Z = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)


class SigtermRequested(RuntimeError):
    """Internal clean-stop signal after the latest completed state is saved."""


@dataclass
class SignalCheckpointContext:
    save_now: Callable[[str], None]
    requested: bool = False
    saving: bool = False
    error: str | None = None


_SIGNAL_CONTEXT: SignalCheckpointContext | None = None
_SIGTERM_PENDING = False


def _require_engine_api() -> None:
    required = (
        "build_orbit_basis",
        "build_hamiltonian_tables",
        "hamiltonian_apply",
        "ground_state",
        "evolve",
        "pointer_populations",
        "conditional_fragment_state",
        "conditional_pair_state",
        "center_bond_state",
        "site_class_table",
        "rss_gb",
        "density_matrix_diagnostics",
        "dense_slab_crosscheck",
        "_guard_rss",
        "_slab_geometry",
        "_build_basis_for_geometry",
        "_reduced_product_state",
        "_observable_spec",
        "_geometry_for_basis",
        "_permutation_luts",
        "_permute_bits",
        "_dense_partial_trace",
    )
    missing = [name for name in required if not hasattr(orbit_engine, name)]
    if missing:
        raise RuntimeError("commissioned engine API missing: " + ",".join(missing))


def _guard_rss(label: str, budget_gb: float) -> None:
    """Invoke the engine's conservative peak-RSS guard."""

    orbit_engine._guard_rss(f"d3 pilot {label}", budget_gb)


def _lam_token(lam: float) -> str:
    return f"{lam:.2f}".replace(".", "p")


def _trace_prefix(lam: float, *, fine: bool = False) -> str:
    stem = f"lam_{_lam_token(lam)}"
    return f"dt_half_{stem}" if fine else stem


def _stream_path(lam: float, *, fine: bool = False) -> Path:
    return RUN_DIR / f"{_trace_prefix(lam, fine=fine)}_observables.jsonl"


def _checkpoint_path(prefix: str, step: int) -> Path:
    return RUN_DIR / f"{prefix}_step_{step:03d}.npz"


def _ground_path(geometry: str, lam: float) -> Path:
    safe_geometry = geometry.replace("open-", "").replace("x", "x")
    return RUN_DIR / f"ground_{safe_geometry}_lam_{_lam_token(lam)}.npz"


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


def _append_jsonl(path: Path, row: Mapping[str, object]) -> None:
    """Append one complete row with one O_APPEND write and an fsync."""

    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (_json_dumps(dict(row)) + "\n").encode("utf-8")
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o644)
    try:
        written = os.write(descriptor, payload)
        if written != len(payload):
            raise OSError(f"short JSONL append {written}/{len(payload)} bytes")
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


def _fmt(value: float | int | None) -> str:
    if value is None:
        return "unavailable"
    number = float(value)
    if not np.isfinite(number):
        return "unavailable"
    return f"{number:.6g}"


def _fmt_vector(values: Iterable[float | int | None]) -> str:
    return "[" + ",".join(_fmt(value) for value in values) + "]"


def _clean_probability(value: float, label: str) -> tuple[float, float]:
    """Clean only <=1e-12 probability roundoff and report its magnitude."""

    number = float(value)
    if number < -1.0e-12 or number > 1.0 + 1.0e-12 or not np.isfinite(number):
        raise AssertionError(f"invalid probability {label}={number!r}")
    cleaned = min(1.0, max(0.0, number))
    return cleaned, abs(cleaned - number)


def _entropy_bits(
    matrix: npt.NDArray[np.complex128], diagnostics: dict[str, float]
) -> float:
    hermitian = 0.5 * (np.asarray(matrix) + np.asarray(matrix).conj().T)
    eigenvalues = np.linalg.eigvalsh(hermitian)
    minimum = float(np.min(eigenvalues))
    trace_error = abs(float(np.sum(eigenvalues)) - 1.0)
    if minimum < -1.0e-9 or trace_error > 1.0e-9:
        raise AssertionError(
            f"entropy input invalid: minimum={minimum:.3e}, trace={trace_error:.3e}"
        )
    cleanup = float(np.sum(np.abs(eigenvalues[eigenvalues < 0.0])))
    diagnostics["entropy_roundoff_cleanup"] = max(
        diagnostics.get("entropy_roundoff_cleanup", 0.0), cleanup, trace_error
    )
    positive = eigenvalues[eigenvalues > 0.0]
    return float(-np.sum(positive * np.log2(positive)))


def _binary_entropy(
    probabilities: Sequence[float], diagnostics: dict[str, float]
) -> tuple[tuple[float, float], float]:
    if len(probabilities) != 2:
        raise ValueError("binary pointer must have two probabilities")
    cleaned: list[float] = []
    cleanup = 0.0
    for index, value in enumerate(probabilities):
        local, error = _clean_probability(float(value), f"p[{index}]")
        cleaned.append(local)
        cleanup = max(cleanup, error)
    normalization_error = abs(sum(cleaned) - 1.0)
    if normalization_error > 1.0e-9:
        raise AssertionError(f"pointer normalization error {normalization_error:.3e}")
    diagnostics["entropy_roundoff_cleanup"] = max(
        diagnostics.get("entropy_roundoff_cleanup", 0.0),
        cleanup,
        normalization_error,
    )
    entropy = -sum(p * math.log2(p) for p in cleaned if p > 0.0)
    return (cleaned[0], cleaned[1]), float(entropy)


def _holevo_bits(
    probabilities: Sequence[float],
    states: Sequence[npt.NDArray[np.complex128]],
    diagnostics: dict[str, float],
) -> float:
    if len(states) != 2:
        raise ValueError("pointer ensemble must contain two states")
    p, _ = _binary_entropy(probabilities, diagnostics)
    average = p[0] * np.asarray(states[0]) + p[1] * np.asarray(states[1])
    return float(
        _entropy_bits(average, diagnostics)
        - p[0] * _entropy_bits(np.asarray(states[0]), diagnostics)
        - p[1] * _entropy_bits(np.asarray(states[1]), diagnostics)
    )


def _partial_traces_two_qubit(
    matrix: npt.NDArray[np.complex128],
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    tensor = np.asarray(matrix, dtype=np.complex128).reshape(2, 2, 2, 2)
    return (
        np.trace(tensor, axis1=1, axis2=3),
        np.trace(tensor, axis1=0, axis2=2),
    )


def _conditional_pair_information_bits(
    probabilities: Sequence[float],
    states: Sequence[npt.NDArray[np.complex128]],
    diagnostics: dict[str, float],
) -> float:
    p, _ = _binary_entropy(probabilities, diagnostics)
    value = 0.0
    for weight, matrix in zip(p, states, strict=True):
        first, second = _partial_traces_two_qubit(np.asarray(matrix))
        value += weight * (
            _entropy_bits(first, diagnostics)
            + _entropy_bits(second, diagnostics)
            - _entropy_bits(np.asarray(matrix), diagnostics)
        )
    return float(value)


def _entropy_bound_violation(chi: float, pointer_entropy: float) -> float:
    return max(0.0, -float(chi), float(chi) - float(pointer_entropy))


def _coordinate_key(coordinate: Sequence[int]) -> str:
    return ",".join(str(int(value)) for value in coordinate)


def _class_coordinates() -> dict[str, tuple[tuple[int, int, int], ...]]:
    classes = orbit_engine.site_class_table()
    expected = {"center": 1, "axial": 6, "edge": 12, "corner": 8}
    counts = {name: len(values) for name, values in classes.items()}
    if counts != expected:
        raise AssertionError(f"site classes {counts}, expected {expected}")
    return {
        name: tuple(tuple(map(int, value)) for value in values)
        for name, values in classes.items()
    }


def _axis_pair_class(first: str, second: str) -> str:
    if first == second:
        raise ValueError("an axis label cannot be paired with itself")
    return "opposite-axis" if first[1] == second[1] else "orthogonal-axis"


def _largest_independent_subset(
    certifies: Mapping[str, bool], pair_information: Mapping[str, float]
) -> tuple[int, tuple[str, ...]]:
    """Return the deterministic maximum clique of the frozen six-axis graph."""

    names = tuple(name for name, _ in AXIAL_LABELS if certifies.get(name, False))
    for size in range(len(names), 0, -1):
        for subset in itertools.combinations(names, size):
            if all(
                float(pair_information[_axis_pair_class(left, right)])
                <= ETA_INDEPENDENCE + NUMERIC_GATE_TOL
                for left, right in itertools.combinations(subset, 2)
            ):
                return size, tuple(subset)
    return 0, ()


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
    except Exception as exc:  # pragma: no cover - asynchronous failure path
        context.error = f"{type(exc).__name__}: {exc}"
    finally:
        context.saving = False


def _pointer_orbit_sites(basis: Any) -> tuple[int, ...]:
    spec = orbit_engine._observable_spec(basis)
    sites = sorted(
        {int(permutation[int(spec.pointer)]) for permutation in basis.site_permutations}
    )
    if not sites:
        raise AssertionError("pointer rotation orbit is empty")
    return tuple(sites)


def _hadamard_pointer_orbit(
    basis: Any, tables: Any, psi: npt.NDArray[np.complex128], budget_gb: float
) -> npt.NDArray[np.complex128]:
    """Map an X declaration to Z using the engine's exact orbit flip tables.

    The centre is a fixed point on the cube, so this local unitary remains in
    the invariant sector and all public conditional-state APIs remain valid.
    The slab pointer has a two-site orbit and therefore uses the engine's
    independent dense validation partial-trace path below instead.
    """

    state = np.asarray(psi, dtype=np.complex128).copy()
    representatives = basis.representatives
    for site in _pointer_orbit_sites(basis):
        z_phase = 1.0 - 2.0 * (
            (representatives >> np.uint32(site)) & np.uint32(1)
        ).astype(np.float64)
        x_state = (
            tables.flip_amplitudes[site]
            * state[tables.flip_targets[site]]
        )
        state = np.asarray((z_phase * state + x_state) / math.sqrt(2.0), dtype=np.complex128)
        _guard_rss(f"Hadamard pointer-orbit site {site}", budget_gb)
    input_norm = float(np.linalg.norm(psi))
    output_norm = float(np.linalg.norm(state))
    relative_error = abs(output_norm - input_norm) / max(input_norm, 1.0e-300)
    if relative_error > NORM_ERROR_TOL:
        raise AssertionError(
            f"pointer-basis rotation norm error {relative_error:.3e} exceeds 1e-9"
        )
    return state


def _expand_validation_slab(
    basis: Any,
    psi: npt.NDArray[np.complex128],
    budget_gb: float,
) -> npt.NDArray[np.complex128]:
    """Expand only the 18-qubit methods slab via engine permutation helpers."""

    if basis.geometry_name != "open-3x3x2" or basis.n_sites != 18:
        raise RuntimeError("raw expansion is restricted to SLAB-METHODS-ONLY")
    geometry = orbit_engine._geometry_for_basis(basis)
    luts = orbit_engine._permutation_luts(geometry)
    raw = np.zeros(1 << basis.n_sites, dtype=np.complex128)
    assigned = np.zeros(raw.size, dtype=bool)
    amplitudes = np.asarray(psi, dtype=np.complex128) / np.sqrt(
        basis.orbit_sizes.astype(np.float64)
    )
    for rotation_lut in luts:
        images = orbit_engine._permute_bits(basis.representatives, rotation_lut)
        raw[images] = amplitudes
        assigned[images] = True
    if not np.all(assigned):
        raise AssertionError("slab invariant expansion left raw configurations unassigned")
    norm_error = abs(float(np.linalg.norm(raw)) - float(np.linalg.norm(psi)))
    if norm_error > NORM_ERROR_TOL:
        raise AssertionError(f"slab raw expansion norm error {norm_error:.3e}")
    _guard_rss("slab X-pointer raw expansion", budget_gb)
    return raw


def _x_conditioned_state(
    joint: npt.NDArray[np.complex128],
    outcome: int,
) -> tuple[float, npt.NDArray[np.complex128]]:
    """Project the leading qubit of a joint density matrix onto X=+/-1."""

    if outcome not in (1, -1):
        raise ValueError("X outcome must be +1 or -1")
    matrix = np.asarray(joint, dtype=np.complex128)
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] % 2:
        raise ValueError("joint pointer density matrix has invalid shape")
    rest = matrix.shape[0] // 2
    tensor = matrix.reshape(2, rest, 2, rest)
    vector = np.asarray([1.0, float(outcome)], dtype=np.complex128) / math.sqrt(2.0)
    conditioned = np.einsum(
        "a,aibj,b->ij", vector.conj(), tensor, vector, optimize=True
    )
    probability = float(np.trace(conditioned).real)
    if probability <= 1.0e-15 or abs(float(np.trace(conditioned).imag)) > 1.0e-9:
        raise AssertionError("invalid X conditioning probability on slab")
    return probability, np.asarray(conditioned / probability, dtype=np.complex128)


def _slab_x_observables(
    basis: Any,
    psi: npt.NDArray[np.complex128],
    diagnostics: dict[str, float],
    budget_gb: float,
) -> dict[str, object]:
    """Exact X-pointer panel from the engine's dense slab validation path."""

    raw = _expand_validation_slab(basis, psi, budget_gb)
    spec = orbit_engine._observable_spec(basis)
    _, bond = orbit_engine._dense_partial_trace(
        raw, basis.n_sites, spec.center_bond
    )
    fragment_conditioned = [_x_conditioned_state(bond, sign) for sign in (1, -1)]
    probabilities = [item[0] for item in fragment_conditioned]
    p_x, h_x = _binary_entropy(probabilities, diagnostics)
    chi_x = _holevo_bits(
        p_x, [item[1] for item in fragment_conditioned], diagnostics
    )
    pairs: dict[str, float] = {}
    for class_name, pair in spec.pairs.items():
        _, triple = orbit_engine._dense_partial_trace(
            raw,
            basis.n_sites,
            (int(spec.pointer), int(pair[0]), int(pair[1])),
        )
        pair_conditioned = [_x_conditioned_state(triple, sign) for sign in (1, -1)]
        local_probabilities = [item[0] for item in pair_conditioned]
        if max(
            abs(local - reference)
            for local, reference in zip(local_probabilities, p_x, strict=True)
        ) > ENTROPY_BOUND_TOL:
            raise AssertionError("slab X pointer marginal depends on pair class")
        pairs[class_name] = _conditional_pair_information_bits(
            p_x, [item[1] for item in pair_conditioned], diagnostics
        )
    del raw
    return {
        "p": list(p_x),
        "entropy_bits": h_x,
        "chi_axial_bits": chi_x,
        "pair_conditional_mi_bits": pairs,
    }


def _bond_endpoints(basis: Any) -> tuple[int, int]:
    spec = orbit_engine._observable_spec(basis)
    return tuple(map(int, spec.center_bond))


def _bond_degrees(basis: Any, pair: tuple[int, int]) -> tuple[int, int]:
    degrees = np.zeros(basis.n_sites, dtype=np.int16)
    for left, right in np.asarray(basis.bonds, dtype=np.int16):
        degrees[int(left)] += 1
        degrees[int(right)] += 1
    first, second = pair
    if degrees[first] <= 0 or degrees[second] <= 0:
        raise AssertionError("centre bond endpoint has zero graph degree")
    return int(degrees[first]), int(degrees[second])


def _bond_observables(
    basis: Any,
    rho: npt.NDArray[np.complex128],
    lam: float,
    diagnostics: dict[str, float],
) -> dict[str, float]:
    pair = _bond_endpoints(basis)
    degree_s, degree_f = _bond_degrees(basis, pair)
    zz = float(np.trace(np.asarray(rho) @ np.kron(PAULI_Z, PAULI_Z)).real)
    x_s = float(np.trace(np.asarray(rho) @ np.kron(PAULI_X, PAULI_I)).real)
    x_f = float(np.trace(np.asarray(rho) @ np.kron(PAULI_I, PAULI_X)).real)
    purity_complex = np.trace(np.asarray(rho) @ np.asarray(rho))
    if abs(float(purity_complex.imag)) > 1.0e-9:
        raise AssertionError("centre-bond purity has an imaginary component")
    purity = float(purity_complex.real)
    if purity < -1.0e-9 or purity > 1.0 + 1.0e-9:
        raise AssertionError(f"centre-bond purity {purity:.16g} outside [0,1]")
    cleanup = max(0.0, -purity, purity - 1.0)
    diagnostics["entropy_roundoff_cleanup"] = max(
        diagnostics.get("entropy_roundoff_cleanup", 0.0), cleanup
    )
    energy = -zz - float(lam) * (x_s / degree_s + x_f / degree_f)
    return {
        # Do not clip: the memo freezes an algebraic GS subtraction.  The
        # raw tolerance violation is recorded above and hard-fails at 1e-9.
        "purity": purity,
        "one_minus_purity": 1.0 - purity,
        "allocated_energy": float(energy),
        "zz": zz,
        "x_pointer": x_s,
        "x_fragment": x_f,
        "pointer_degree": float(degree_s),
        "fragment_degree": float(degree_f),
    }


def _measure_pointer_and_fragments(
    psi: npt.NDArray[np.complex128],
    diagnostics: dict[str, float],
    fragment_classes: Sequence[str],
) -> tuple[tuple[float, float], float, dict[str, float]]:
    probabilities, entropy = _binary_entropy(
        orbit_engine.pointer_populations(psi), diagnostics
    )
    chis: dict[str, float] = {}
    for class_name in fragment_classes:
        states = orbit_engine.conditional_fragment_state(psi, class_name)
        chis[class_name] = _holevo_bits(probabilities, states, diagnostics)
    return probabilities, entropy, chis


def _measure_pairs(
    psi: npt.NDArray[np.complex128],
    probabilities: Sequence[float],
    diagnostics: dict[str, float],
) -> dict[str, float]:
    result: dict[str, float] = {}
    for pair_class in ("opposite-axis", "orthogonal-axis"):
        states = orbit_engine.conditional_pair_state(psi, pair_class)
        result[pair_class] = _conditional_pair_information_bits(
            probabilities, states, diagnostics
        )
    return result


def _raw_observables(
    *,
    basis: Any,
    tables: Any,
    psi: npt.NDArray[np.complex128],
    lam: float,
    budget_gb: float,
    include_x: bool,
    x_baseline_chi: float | None,
    force_x_pairs: bool = False,
) -> dict[str, object]:
    """Contract the memo's local observable set from one reduced state."""

    diagnostics: dict[str, float] = {
        "entropy_roundoff_cleanup": 0.0,
        "entropy_bound_violation": 0.0,
        "symmetry_consistency": 0.0,
    }
    p_z, h_z, chi_z = _measure_pointer_and_fragments(
        psi, diagnostics, CLASS_ORDER
    )
    pair_z = _measure_pairs(psi, p_z, diagnostics)
    bond_rho = orbit_engine.center_bond_state(psi)
    bond = _bond_observables(basis, bond_rho, lam, diagnostics)

    for chi in chi_z.values():
        diagnostics["entropy_bound_violation"] = max(
            diagnostics["entropy_bound_violation"],
            _entropy_bound_violation(chi, h_z),
        )
    for value in pair_z.values():
        diagnostics["entropy_bound_violation"] = max(
            diagnostics["entropy_bound_violation"], max(0.0, -float(value))
        )

    x_result: dict[str, object] | None = None
    if include_x:
        if basis.geometry_name == "open-3x3x2":
            x_result = _slab_x_observables(
                basis, psi, diagnostics, budget_gb
            )
            p_x = tuple(float(value) for value in x_result["p"])
            h_x = float(x_result["entropy_bits"])
            chi_x = float(x_result["chi_axial_bits"])
            pair_x = {
                name: float(value)
                for name, value in dict(x_result["pair_conditional_mi_bits"]).items()
            }
        else:
            rotated = _hadamard_pointer_orbit(basis, tables, psi, budget_gb)
            p_x, h_x, chi_x_map = _measure_pointer_and_fragments(
                rotated, diagnostics, ("axial",)
            )
            chi_x = float(chi_x_map["axial"])
            pair_x = None
        diagnostics["entropy_bound_violation"] = max(
            diagnostics["entropy_bound_violation"],
            _entropy_bound_violation(chi_x, h_x),
        )
        singleton_can_pass = force_x_pairs
        if x_baseline_chi is not None:
            excess_x = chi_x - float(x_baseline_chi)
            singleton_can_pass = singleton_can_pass or any(
                h_x >= H_FLOOR
                and chi_x + NUMERIC_GATE_TOL >= (1.0 - delta) * h_x
                and excess_x + NUMERIC_GATE_TOL >= EPS_EXCESS
                for delta in DELTAS
            )
        if basis.geometry_name != "open-3x3x2":
            pair_x = (
                _measure_pairs(rotated, p_x, diagnostics)
                if singleton_can_pass
                else None
            )
        if pair_x is not None:
            for value in pair_x.values():
                diagnostics["entropy_bound_violation"] = max(
                    diagnostics["entropy_bound_violation"],
                    max(0.0, -float(value)),
                )
        x_result = {
            "p": list(p_x),
            "entropy_bits": h_x,
            "chi_axial_bits": chi_x,
            "pair_conditional_mi_bits": pair_x,
        }
        if basis.geometry_name != "open-3x3x2":
            del rotated

    _guard_rss("observable contraction", budget_gb)
    return {
        "p_z": list(p_z),
        "h_z_bits": h_z,
        "chi_z_bits": chi_z,
        "pair_z_bits": pair_z,
        "bond": bond,
        "x": x_result,
        "diagnostics": diagnostics,
    }


def _baseline_from_ground_raw(raw: Mapping[str, object]) -> dict[str, object]:
    x = raw.get("x")
    if not isinstance(x, Mapping):
        raise TypeError("ground raw observables lack X-pointer control")
    pair_x = x.get("pair_conditional_mi_bits")
    if not isinstance(pair_x, Mapping):
        raise TypeError("ground raw observables lack X conditional pairs")
    return {
        "p_z": list(raw["p_z"]),
        "h_z_bits": float(raw["h_z_bits"]),
        "chi_z_bits": {
            name: float(value)
            for name, value in dict(raw["chi_z_bits"]).items()
        },
        "pair_z_bits": {
            name: float(value)
            for name, value in dict(raw["pair_z_bits"]).items()
        },
        "bond": {name: float(value) for name, value in dict(raw["bond"]).items()},
        "x": {
            "p": list(x["p"]),
            "entropy_bits": float(x["entropy_bits"]),
            "chi_axial_bits": float(x["chi_axial_bits"]),
            "pair_conditional_mi_bits": {
                name: float(value) for name, value in dict(pair_x).items()
            },
        },
    }


def _singleton_gate(
    entropy: float, chi: float, excess: float, delta: float
) -> bool:
    return bool(
        entropy >= H_FLOOR
        and chi + NUMERIC_GATE_TOL >= (1.0 - delta) * entropy
        and excess + NUMERIC_GATE_TOL >= EPS_EXCESS
    )


def _assemble_row(
    *,
    raw: Mapping[str, object],
    baseline: Mapping[str, object],
    p0_z: Sequence[float],
    run_kind: str,
    geometry: str,
    lam: float,
    dt: float,
    step: int,
    norm_error: float,
) -> dict[str, object]:
    classes = _class_coordinates()
    chi_z = {name: float(value) for name, value in dict(raw["chi_z_bits"]).items()}
    gs_chi_z = {
        name: float(value) for name, value in dict(baseline["chi_z_bits"]).items()
    }
    delta_chi = {name: chi_z[name] - gs_chi_z[name] for name in CLASS_ORDER}
    h_z = float(raw["h_z_bits"])
    p_z = tuple(float(value) for value in raw["p_z"])
    tv_drift = 0.5 * sum(
        abs(value - float(reference)) for value, reference in zip(p_z, p0_z, strict=True)
    )

    fragments: list[dict[str, object]] = []
    for class_name in CLASS_ORDER:
        for coordinate in classes[class_name]:
            fragments.append(
                {
                    "coordinate": list(coordinate),
                    "label": _coordinate_key(coordinate),
                    "site_class": class_name,
                    "manhattan_distance": CLASS_SHELL[class_name],
                    "chi_z_bits": chi_z[class_name],
                    "delta_chi_z_bits": delta_chi[class_name],
                }
            )
    if len(fragments) != 26:
        raise AssertionError(f"stream row has {len(fragments)} exterior fragments")

    pair_z = {
        name: float(value) for name, value in dict(raw["pair_z_bits"]).items()
    }
    r_z: dict[str, int] = {}
    subset_z: dict[str, list[str]] = {}
    singleton_z: dict[str, dict[str, bool]] = {}
    for delta in DELTAS:
        key = DELTA_KEYS[delta]
        class_flags = {
            class_name: _singleton_gate(
                h_z, chi_z[class_name], delta_chi[class_name], delta
            )
            for class_name in CLASS_ORDER
        }
        axis_flags = {name: class_flags["axial"] for name, _ in AXIAL_LABELS}
        redundancy, subset = _largest_independent_subset(axis_flags, pair_z)
        r_z[key] = redundancy
        subset_z[key] = list(subset)
        singleton_z[key] = class_flags

    x_raw = raw.get("x")
    x_pointer: dict[str, object] | None = None
    axial_x: dict[str, float] | None = None
    pair_x: dict[str, float | None] = {
        "opposite-axis": None,
        "orthogonal-axis": None,
    }
    r_x = {DELTA_KEYS[delta]: 0 for delta in DELTAS}
    subset_x = {DELTA_KEYS[delta]: [] for delta in DELTAS}
    singleton_x = {DELTA_KEYS[delta]: False for delta in DELTAS}
    if isinstance(x_raw, Mapping):
        x_probabilities = [float(value) for value in x_raw["p"]]
        x_entropy = float(x_raw["entropy_bits"])
        x_chi = float(x_raw["chi_axial_bits"])
        gs_x = baseline.get("x")
        if not isinstance(gs_x, Mapping):
            raise TypeError("ground baseline lacks X pointer data")
        x_excess = x_chi - float(gs_x["chi_axial_bits"])
        x_pointer = {
            "p": x_probabilities,
            "entropy_bits": x_entropy,
        }
        axial_x = {
            "chi_bits": x_chi,
            "delta_chi_bits": x_excess,
        }
        supplied_pairs = x_raw.get("pair_conditional_mi_bits")
        if isinstance(supplied_pairs, Mapping):
            pair_x = {name: float(value) for name, value in supplied_pairs.items()}
        for delta in DELTAS:
            key = DELTA_KEYS[delta]
            passes = _singleton_gate(x_entropy, x_chi, x_excess, delta)
            singleton_x[key] = passes
            if passes:
                if any(value is None for value in pair_x.values()):
                    raise AssertionError("X singleton passed but X pair panel was not measured")
                usable_pairs = {name: float(value) for name, value in pair_x.items()}
                axis_flags = {name: True for name, _ in AXIAL_LABELS}
                redundancy, subset = _largest_independent_subset(
                    axis_flags, usable_pairs
                )
                r_x[key] = redundancy
                subset_x[key] = list(subset)

    bond = {name: float(value) for name, value in dict(raw["bond"]).items()}
    gs_bond = {
        name: float(value) for name, value in dict(baseline["bond"]).items()
    }
    theta = bond["one_minus_purity"] - gs_bond["one_minus_purity"]
    center_bonds: list[dict[str, object]] = []
    for axis_name, _ in AXIAL_LABELS:
        center_bonds.append(
            {
                "axis": axis_name,
                "purity": bond["purity"],
                "one_minus_purity": bond["one_minus_purity"],
                "theta_contribution": theta,
                "allocated_energy": bond["allocated_energy"],
                "delta_allocated_energy": (
                    bond["allocated_energy"] - gs_bond["allocated_energy"]
                ),
            }
        )

    shell_delta = {
        str(CLASS_SHELL[name]): delta_chi[name] for name in CLASS_ORDER
    }
    total_delta = sum(
        len(classes[name]) * delta_chi[name] for name in CLASS_ORDER
    )
    bond_profile = [
        {
            "axis": axis_name,
            "delta_allocated_energy": (
                bond["allocated_energy"] - gs_bond["allocated_energy"]
            ),
            "activity_1_minus_purity": bond["one_minus_purity"],
            "delta_activity": theta,
        }
        for axis_name, _ in AXIAL_LABELS
    ]

    diagnostics = {
        name: float(value)
        for name, value in dict(raw["diagnostics"]).items()
    }
    diagnostics.update(
        {
            "relative_norm_error": float(norm_error),
            "orbit_normalization_error": float(norm_error),
            "symmetry_consistency": 0.0,
            "symmetry_consistency_method": "exact-in-invariant-orbit-sector",
        }
    )
    return {
        "schema": STREAM_SCHEMA,
        "run_kind": run_kind,
        "geometry": geometry,
        "fragment_geometry": (
            "physical-open-cube"
            if geometry == "open-3x3x3"
            else "cube-label-surrogate-SLAB-METHODS-ONLY"
        ),
        "lam": float(lam),
        "dt": float(dt),
        "step": int(step),
        "jt": float(step * dt),
        "pointer_z": {
            "p": list(p_z),
            "entropy_bits": h_z,
            "tv_from_t0": float(tv_drift),
        },
        "pointer_x": x_pointer,
        "fragments": fragments,
        "axial_x": axial_x,
        "pair_conditional_mi_bits": {"Z": pair_z, "X": pair_x},
        "r_ind": {"Z": r_z, "X": r_x},
        "certifying_subsets": {"Z": subset_z, "X": subset_x},
        "singleton_certifies": {
            "Z": singleton_z,
            "X_axial": singleton_x,
        },
        "center_bonds": center_bonds,
        "theta": float(theta),
        "shell_delta_chi_bits": shell_delta,
        "sum_delta_chi_bits": float(total_delta),
        "bond_profile": bond_profile,
        "diagnostics": diagnostics,
    }


def _stationary_control_counts(
    raw: Mapping[str, object], baseline: Mapping[str, object], lam: float
) -> list[int]:
    """Feed a 101-sample stationary GS trace through the identical row gate."""

    p0 = [float(value) for value in raw["p_z"]]
    template = _assemble_row(
        raw=raw,
        baseline=baseline,
        p0_z=p0,
        run_kind="ground-stationary-control",
        geometry="ground-control",
        lam=lam,
        dt=DT,
        step=0,
        norm_error=0.0,
    )
    counts: list[int] = []
    for delta in DELTAS:
        key = DELTA_KEYS[delta]
        # The same exact baseline-subtracted row is repeated on all samples.
        has_event = any(
            int(template["r_ind"]["Z"][key]) >= MIN_REDUNDANCY
            for _ in range(N_STEPS + 1)
        )
        counts.append(int(has_event))
    return counts


def _rows_by_step(rows: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    ordered = sorted((dict(row) for row in rows), key=lambda row: int(row["step"]))
    steps = [int(row["step"]) for row in ordered]
    if len(steps) != len(set(steps)):
        raise RuntimeError("accumulated checkpoint rows contain duplicate steps")
    return ordered


def _first_event(
    rows: Sequence[Mapping[str, object]], delta: float, pointer: str = "Z"
) -> dict[str, object] | None:
    key = DELTA_KEYS[delta]
    for index, row in enumerate(rows):
        if int(row["r_ind"][pointer][key]) < MIN_REDUNDANCY:
            continue
        consecutive = 0
        for later in rows[index:]:
            if int(later["r_ind"][pointer][key]) < MIN_REDUNDANCY:
                break
            consecutive += 1
        return {
            "step": int(row["step"]),
            "jt": float(row["jt"]),
            "theta_star": float(row["theta"]),
            "r_ind": int(row["r_ind"][pointer][key]),
            "subset": list(row["certifying_subsets"][pointer][key]),
            "consecutive_samples": consecutive,
            "persistence": consecutive >= PERSISTENCE_SAMPLES,
            "label": (
                "PERSISTENT-FINITE-TIME"
                if consecutive >= PERSISTENCE_SAMPLES
                else "TRANSIENT-ONSET"
            ),
            "tv_drift": float(row["pointer_z"]["tv_from_t0"]),
        }
    return None


def _profile_summary(rows: Sequence[Mapping[str, object]]) -> dict[str, object]:
    if not rows:
        raise ValueError("cannot profile an empty trace")
    sums = np.asarray([float(row["sum_delta_chi_bits"]) for row in rows])
    if not np.all(np.isfinite(sums)):
        raise RuntimeError("nonfinite sum_F Delta chi profile")
    index = int(np.argmax(sums))  # numpy returns the first sampled maximizer.
    row = rows[index]
    shells = {
        int(shell): float(value)
        for shell, value in row["shell_delta_chi_bits"].items()
    }
    reached = [
        shell
        for shell, value in shells.items()
        if value + NUMERIC_GATE_TOL >= EPS_EXCESS
    ]
    return {
        "step": int(row["step"]),
        "jt": float(row["jt"]),
        "sum_delta_chi_bits": float(sums[index]),
        "shell_delta_chi_bits": shells,
        "xi_reg": max(reached) if reached else None,
        "bond_profile": list(row["bond_profile"]),
    }


def _locality_before_axial(
    rows: Sequence[Mapping[str, object]], event: Mapping[str, object] | None
) -> tuple[bool, list[str]]:
    if event is None:
        stop_step = math.inf
    else:
        stop_step = int(event["step"])
    offenders: list[str] = []
    key = DELTA_KEYS[HEADLINE_DELTA]
    for row in rows:
        if int(row["step"]) >= stop_step:
            break
        flags = row["singleton_certifies"]["Z"][key]
        for class_name in ("edge", "corner"):
            if bool(flags[class_name]):
                offenders.append(f"d{CLASS_SHELL[class_name]}@{float(row['jt']):g}")
    return not offenders, offenders


def _load_or_compute_ground(
    basis: Any,
    tables: Any,
    lam: float,
    budget_gb: float,
) -> tuple[float, npt.NDArray[np.complex128], float, str]:
    """Load an exact-metadata GS cache or call the public engine solver."""

    path = _ground_path(str(basis.geometry_name), lam)
    state: npt.NDArray[np.complex128]
    energy: float
    cache_status: str
    if path.exists():
        with np.load(path, allow_pickle=False) as archive:
            schema = str(np.asarray(archive["schema"]).item())
            stored_basis = str(np.asarray(archive["basis_checksum"]).item())
            stored_lam = float(np.asarray(archive["lam"]).item())
            energy = float(np.asarray(archive["energy"]).item())
            state = np.asarray(archive["psi"], dtype=np.complex128)
            stored_checksum = str(np.asarray(archive["psi_checksum"]).item())
        if schema != GROUND_SCHEMA:
            raise RuntimeError(f"ground cache schema {schema!r} is not {GROUND_SCHEMA!r}")
        if stored_basis != basis.checksum or stored_lam != float(lam):
            raise RuntimeError("ground cache does not match basis/lambda")
        if state.shape != (basis.n_orbits,):
            raise RuntimeError("ground cache state has the wrong shape")
        computed_checksum = _state_checksum(state)
        if computed_checksum != stored_checksum:
            raise RuntimeError("ground cache state checksum mismatch")
        cache_status = "loaded"
    else:
        with contextlib.redirect_stdout(io.StringIO()):
            energy, state = orbit_engine.ground_state(basis, tables, lam)
        state = np.asarray(state, dtype=np.complex128)
        checksum = _state_checksum(state)
        _atomic_savez(
            path,
            schema=np.asarray(GROUND_SCHEMA),
            basis_checksum=np.asarray(basis.checksum),
            geometry=np.asarray(basis.geometry_name),
            lam=np.asarray(lam, dtype=np.float64),
            energy=np.asarray(energy, dtype=np.float64),
            psi=state,
            psi_checksum=np.asarray(checksum),
        )
        cache_status = "built"

    residual_vector = orbit_engine.hamiltonian_apply(
        basis, tables, lam, state
    ) - energy * state
    residual = float(np.linalg.norm(residual_vector))
    if not np.isfinite(residual) or residual > GROUND_RESIDUAL_TOL:
        raise RuntimeError(
            f"ground residual {residual:.3e} exceeds {GROUND_RESIDUAL_TOL:.1e}"
        )
    norm_error = abs(float(np.linalg.norm(state)) - 1.0)
    if norm_error > NORM_ERROR_TOL:
        raise RuntimeError(f"ground norm error {norm_error:.3e} exceeds 1e-9")
    _guard_rss(f"ground state lambda={lam:g}", budget_gb)
    return energy, state, residual, cache_status


def _ground_metadata(
    *,
    basis: Any,
    tables: Any,
    lam: float,
    energy: float,
    ground: npt.NDArray[np.complex128],
    residual: float,
    cache_status: str,
    budget_gb: float,
) -> dict[str, object]:
    raw = _raw_observables(
        basis=basis,
        tables=tables,
        psi=ground,
        lam=lam,
        budget_gb=budget_gb,
        include_x=True,
        x_baseline_chi=None,
        force_x_pairs=True,
    )
    baseline = _baseline_from_ground_raw(raw)
    controls = _stationary_control_counts(raw, baseline, lam)
    if controls != [0, 0, 0]:
        raise AssertionError(
            f"same-lambda stationary GS acquired events {controls} at lambda={lam:g}"
        )
    return {
        "lam": float(lam),
        "energy": float(energy),
        "residual": float(residual),
        "cache_status": cache_status,
        "baseline": baseline,
        "stationary_event_counts": controls,
    }


def _demolition_table(basis: Any, lam: float) -> dict[str, object]:
    """Exact centred-Frobenius Pauli-string table without a 2^N matrix."""

    dimension = float(1 << int(basis.n_sites))
    h_pauli_weight = float(len(basis.bonds)) + basis.n_sites * float(lam) ** 2
    common = math.sqrt(dimension) * math.sqrt(h_pauli_weight)
    degrees = np.zeros(basis.n_sites, dtype=np.int16)
    for left, right in np.asarray(basis.bonds, dtype=np.int16):
        degrees[int(left)] += 1
        degrees[int(right)] += 1

    if basis.geometry_name == "open-3x3x3":
        demolition_names = ("center", "face", "edge", "corner")
        class_sites: dict[str, list[int]] = {name: [] for name in demolition_names}
        for index, coordinate in enumerate(basis.coordinates):
            nonzero = sum(int(value) != 0 for value in coordinate)
            class_sites[demolition_names[nonzero]].append(index)
    else:
        # Validation is methods-only.  Group actual slab sites by graph degree
        # so the same formula and max-Z/min-X gate are still exercised.
        class_sites = {
            f"degree-{degree}": list(np.flatnonzero(degrees == degree))
            for degree in sorted(set(map(int, degrees)))
        }

    classes: dict[str, dict[str, float]] = {}
    all_z: list[float] = []
    all_x: list[float] = []
    for class_name, sites in class_sites.items():
        local_degrees = [int(degrees[site]) for site in sites]
        if len(set(local_degrees)) != 1:
            raise AssertionError(f"site class {class_name} mixes graph degrees")
        degree = local_degrees[0]
        z_value = 2.0 * abs(float(lam)) / common
        x_value = 2.0 * math.sqrt(float(degree)) / common
        y_value = 2.0 * math.sqrt(float(degree) + float(lam) ** 2) / common
        classes[class_name] = {
            "degree": float(degree),
            "Z": z_value,
            "X": x_value,
            "Y": y_value,
        }
        all_z.append(z_value)
        all_x.append(x_value)
    gate = max(all_z) < min(all_x)
    return {
        "normalization": "||[H,O]||F/(||H||F*||O-Tr(O)I/d||F)",
        "classes": classes,
        "max_z": max(all_z),
        "min_x": min(all_x),
        "gate": bool(gate),
    }


def _save_trace_checkpoint(
    *,
    prefix: str,
    reason: str,
    basis: Any,
    lam: float,
    dt: float,
    n_steps: int,
    step: int,
    psi: npt.NDArray[np.complex128],
    initial_checksum: str,
    reference_norm: float,
    rows: Sequence[Mapping[str, object]],
    ground_metadata: Mapping[str, object],
) -> Path:
    ordered_rows = _rows_by_step(rows)
    if not ordered_rows or int(ordered_rows[-1]["step"]) != int(step):
        raise RuntimeError("checkpoint state step does not match accumulated rows")
    state = np.asarray(psi, dtype=np.complex128)
    path = _checkpoint_path(prefix, step)
    _atomic_savez(
        path,
        schema=np.asarray(CHECKPOINT_SCHEMA),
        prefix=np.asarray(prefix),
        reason=np.asarray(reason),
        basis_checksum=np.asarray(basis.checksum),
        geometry=np.asarray(basis.geometry_name),
        lam=np.asarray(lam, dtype=np.float64),
        dt=np.asarray(dt, dtype=np.float64),
        n_steps=np.asarray(n_steps, dtype=np.int64),
        step=np.asarray(step, dtype=np.int64),
        psi=state,
        psi_checksum=np.asarray(_state_checksum(state)),
        initial_checksum=np.asarray(initial_checksum),
        reference_norm=np.asarray(reference_norm, dtype=np.float64),
        rows_json=np.asarray(_json_dumps(ordered_rows)),
        ground_json=np.asarray(_json_dumps(dict(ground_metadata))),
    )
    return path


def _newest_checkpoint_path(prefix: str) -> Path | None:
    paths = sorted(RUN_DIR.glob(f"{prefix}_step_*.npz"))
    return paths[-1] if paths else None


def _load_trace_checkpoint(
    path: Path,
    *,
    expected_prefix: str | None = None,
    basis: Any | None = None,
    lam: float | None = None,
    dt: float | None = None,
    n_steps: int | None = None,
    initial_checksum: str | None = None,
    load_state: bool,
) -> dict[str, object]:
    with np.load(path, allow_pickle=False) as archive:
        metadata: dict[str, object] = {
            "schema": str(np.asarray(archive["schema"]).item()),
            "prefix": str(np.asarray(archive["prefix"]).item()),
            "reason": str(np.asarray(archive["reason"]).item()),
            "basis_checksum": str(np.asarray(archive["basis_checksum"]).item()),
            "geometry": str(np.asarray(archive["geometry"]).item()),
            "lam": float(np.asarray(archive["lam"]).item()),
            "dt": float(np.asarray(archive["dt"]).item()),
            "n_steps": int(np.asarray(archive["n_steps"]).item()),
            "step": int(np.asarray(archive["step"]).item()),
            "psi_checksum": str(np.asarray(archive["psi_checksum"]).item()),
            "initial_checksum": str(np.asarray(archive["initial_checksum"]).item()),
            "reference_norm": float(np.asarray(archive["reference_norm"]).item()),
            "rows": json.loads(str(np.asarray(archive["rows_json"]).item())),
            "ground": json.loads(str(np.asarray(archive["ground_json"]).item())),
            "state_shape": tuple(archive["psi"].shape),
        }
        if load_state:
            metadata["psi"] = np.asarray(archive["psi"], dtype=np.complex128)

    if metadata["schema"] != CHECKPOINT_SCHEMA:
        raise RuntimeError(f"checkpoint {path} has unknown schema")
    exact_checks = (
        (expected_prefix is None or metadata["prefix"] == expected_prefix),
        (basis is None or metadata["basis_checksum"] == basis.checksum),
        (basis is None or metadata["state_shape"] == (basis.n_orbits,)),
        (lam is None or float(metadata["lam"]) == float(lam)),
        (dt is None or float(metadata["dt"]) == float(dt)),
        (n_steps is None or int(metadata["n_steps"]) == int(n_steps)),
        (
            initial_checksum is None
            or metadata["initial_checksum"] == initial_checksum
        ),
    )
    if not all(exact_checks):
        raise RuntimeError(f"checkpoint {path} does not exactly match requested trace")
    rows = _rows_by_step(metadata["rows"])
    if not rows or int(rows[-1]["step"]) != int(metadata["step"]):
        raise RuntimeError(f"checkpoint {path} rows do not end at saved step")
    metadata["rows"] = rows
    if load_state:
        state = np.asarray(metadata["psi"], dtype=np.complex128)
        if _state_checksum(state) != metadata["psi_checksum"]:
            raise RuntimeError(f"checkpoint {path} state checksum mismatch")
    return metadata


def _read_stream(
    path: Path,
    *,
    expected_lam: float,
    expected_dt: float,
    expected_kind: str,
) -> list[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(f"missing observable stream {path}")
    by_step: dict[int, dict[str, object]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.endswith("\n"):
                raise RuntimeError(f"unterminated JSONL row {path}:{line_number}")
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"invalid JSONL row {path}:{line_number}: {exc}") from exc
            if (
                row.get("schema") != STREAM_SCHEMA
                or float(row.get("lam", math.nan)) != float(expected_lam)
                or float(row.get("dt", math.nan)) != float(expected_dt)
                or row.get("run_kind") != expected_kind
            ):
                raise RuntimeError(f"observable stream identity mismatch {path}:{line_number}")
            step = int(row["step"])
            previous = by_step.get(step)
            if previous is not None and _json_dumps(previous) != _json_dumps(row):
                raise RuntimeError(f"non-identical duplicate step {step} in {path}")
            by_step[step] = row
    return [by_step[step] for step in sorted(by_step)]


def _progress_line(
    *,
    lam: float,
    step: int,
    n_steps: int,
    fine: bool,
    run_started: float,
    completed_units: int,
    total_units: int,
) -> None:
    elapsed = max(0.0, time.monotonic() - run_started)
    fraction = min(1.0, max(1.0 / total_units, completed_units / total_units))
    remaining = elapsed * (1.0 - fraction) / fraction
    projected = datetime.fromtimestamp(
        time.time() + remaining, tz=timezone.utc
    ).isoformat(timespec="seconds")
    label = "dt-half" if fine else "main"
    print(
        f"PROGRESS trace={label} lam={lam:g} step={step}/{n_steps} "
        f"wall={elapsed:.1f}s projected-completion={projected} "
        f"rss={orbit_engine.rss_gb():.3f}GiB",
        file=sys.stderr,
        flush=True,
    )


def _prepare_ground_and_baseline(
    basis: Any,
    tables: Any,
    lam: float,
    budget_gb: float,
) -> tuple[npt.NDArray[np.complex128], dict[str, object]]:
    energy, ground, residual, cache_status = _load_or_compute_ground(
        basis, tables, lam, budget_gb
    )
    metadata = _ground_metadata(
        basis=basis,
        tables=tables,
        lam=lam,
        energy=energy,
        ground=ground,
        residual=residual,
        cache_status=cache_status,
        budget_gb=budget_gb,
    )
    metadata["demolition"] = _demolition_table(basis, lam)
    return ground, metadata


def _run_persistent_trace(
    *,
    basis: Any,
    tables: Any,
    lam: float,
    dt: float,
    n_steps: int,
    fine: bool,
    initial: npt.NDArray[np.complex128],
    ground_metadata: dict[str, object],
    run_started: float,
    progress_base_units: int,
    progress_total_units: int,
) -> dict[str, object]:
    """Run or resume one trace, streaming rows and checkpointing every 10."""

    global _SIGNAL_CONTEXT, _SIGTERM_PENDING
    prefix = _trace_prefix(lam, fine=fine)
    run_kind = "cube-dt-halving-subsample" if fine else "cube-full"
    stream_path = _stream_path(lam, fine=fine)
    initial_state = np.asarray(initial, dtype=np.complex128)
    initial_checksum = _state_checksum(initial_state)
    reference_norm = float(np.linalg.norm(initial_state))
    if abs(reference_norm - 1.0) > NORM_ERROR_TOL:
        raise RuntimeError(f"initial state norm {reference_norm:.16g} is invalid")

    newest = _newest_checkpoint_path(prefix)
    if newest is None:
        if stream_path.exists() and stream_path.stat().st_size:
            raise RuntimeError(
                f"stream {stream_path} exists without a resumable checkpoint"
            )
        start_step = 0
        state = initial_state.copy()
        rows: list[dict[str, object]] = []
        p0_z: list[float] | None = None
    else:
        loaded = _load_trace_checkpoint(
            newest,
            expected_prefix=prefix,
            basis=basis,
            lam=lam,
            dt=dt,
            n_steps=n_steps,
            initial_checksum=initial_checksum,
            load_state=True,
        )
        start_step = int(loaded["step"])
        state = np.asarray(loaded["psi"], dtype=np.complex128)
        rows = [dict(row) for row in loaded["rows"]]
        loaded_ground = dict(loaded["ground"])
        comparable_loaded = dict(loaded_ground)
        comparable_current = dict(ground_metadata)
        comparable_loaded.pop("cache_status", None)
        comparable_current.pop("cache_status", None)
        if _json_dumps(comparable_loaded) != _json_dumps(comparable_current):
            raise RuntimeError("checkpoint ground/control metadata mismatch")
        reference_norm = float(loaded["reference_norm"])
        if start_step > n_steps:
            raise RuntimeError("checkpoint step exceeds requested trace")
        if not rows or int(rows[0]["step"]) != 0:
            raise RuntimeError("checkpoint does not retain the t=0 observable row")
        p0_z = [float(value) for value in rows[0]["pointer_z"]["p"]]
        streamed = _read_stream(
            stream_path,
            expected_lam=lam,
            expected_dt=dt,
            expected_kind=run_kind,
        )
        streamed_by_step = {int(row["step"]): row for row in streamed}
        for saved_row in rows:
            saved_step = int(saved_row["step"])
            if saved_step not in streamed_by_step:
                raise RuntimeError(
                    f"checkpoint step {saved_step} is absent from {stream_path}"
                )
            if _json_dumps(saved_row) != _json_dumps(streamed_by_step[saved_step]):
                raise RuntimeError(
                    f"checkpoint/stream mismatch at step {saved_step}"
                )

    baseline = ground_metadata.get("baseline")
    if not isinstance(baseline, Mapping):
        raise TypeError("ground metadata lacks baseline")
    row_by_step = {int(row["step"]): row for row in rows}
    live: dict[str, object] = {
        "state": state,
        "step": start_step,
        "rows": rows,
    }

    def save_now(reason: str) -> None:
        current_state = np.asarray(live["state"], dtype=np.complex128)
        current_step = int(live["step"])
        current_rows = list(live["rows"])
        # Before the t=0 observer finishes there is no internally consistent
        # state+row unit to save.  The requested flag makes that callback save
        # immediately after completing its row.
        if not current_rows:
            return
        _save_trace_checkpoint(
            prefix=prefix,
            reason=reason,
            basis=basis,
            lam=lam,
            dt=dt,
            n_steps=n_steps,
            step=current_step,
            psi=current_state,
            initial_checksum=initial_checksum,
            reference_norm=reference_norm,
            rows=current_rows,
            ground_metadata=ground_metadata,
        )

    context = SignalCheckpointContext(
        save_now=save_now,
        requested=_SIGTERM_PENDING,
    )
    _SIGNAL_CONTEXT = context
    original_resume = os.environ.get("D3_ENGINE_RESUME")
    os.environ["D3_ENGINE_RESUME"] = "0"

    def callback(local_step: int, psi: npt.NDArray[np.complex128]) -> None:
        nonlocal p0_z
        global_step = start_step + int(local_step)
        if global_step > n_steps:
            raise AssertionError("evolution callback exceeded requested grid")

        existing = row_by_step.get(global_step)
        if existing is None:
            state_norm = float(np.linalg.norm(psi))
            norm_error = abs(state_norm - reference_norm) / reference_norm
            jt = global_step * dt
            raw = _raw_observables(
                basis=basis,
                tables=tables,
                psi=psi,
                lam=lam,
                budget_gb=FULL_RSS_GB,
                include_x=jt <= HEADLINE_TIME + NUMERIC_GATE_TOL,
                x_baseline_chi=float(baseline["x"]["chi_axial_bits"]),
            )
            if global_step == 0:
                t0_chi_error = max(
                    abs(float(value)) for value in dict(raw["chi_z_bits"]).values()
                )
                if t0_chi_error > ENTROPY_BOUND_TOL:
                    raise AssertionError(
                        f"cube preparation t=0 intersite chi {t0_chi_error:.3e} exceeds 1e-9"
                    )
            if p0_z is None:
                if global_step != 0:
                    raise RuntimeError("resume lacks t=0 pointer reference")
                p0_z = [float(value) for value in raw["p_z"]]
            row = _assemble_row(
                raw=raw,
                baseline=baseline,
                p0_z=p0_z,
                run_kind=run_kind,
                geometry=basis.geometry_name,
                lam=lam,
                dt=dt,
                step=global_step,
                norm_error=norm_error,
            )
            _append_jsonl(stream_path, row)
            rows.append(row)
            row_by_step[global_step] = row
            live["rows"] = rows
        elif int(local_step) != 0:
            raise RuntimeError(f"unexpected existing row at newly evolved step {global_step}")

        # Publish a signal-safe consistent unit only after the observable row
        # is durably appended (or verified as the resumed initial row).
        live["state"] = np.asarray(psi, dtype=np.complex128)
        live["step"] = global_step
        live["rows"] = rows

        completed = progress_base_units + global_step + 1
        _progress_line(
            lam=lam,
            step=global_step,
            n_steps=n_steps,
            fine=fine,
            run_started=run_started,
            completed_units=completed,
            total_units=progress_total_units,
        )
        if global_step % 10 == 0 or global_step == n_steps:
            context.saving = True
            try:
                save_now("interval-10" if global_step < n_steps else "complete")
            finally:
                context.saving = False
        if context.requested or _SIGTERM_PENDING:
            if context.error:
                raise RuntimeError(f"SIGTERM checkpoint failed: {context.error}")
            if global_step % 10 != 0 and global_step != n_steps:
                save_now("SIGTERM-callback")
            raise SigtermRequested("SIGTERM received after checkpoint")
        _guard_rss(f"trace {prefix} step {global_step}", FULL_RSS_GB)

    try:
        remaining = n_steps - start_step
        if remaining == 0:
            callback(0, state)
        else:
            orbit_engine.evolve(
                basis,
                tables,
                lam,
                state,
                dt,
                remaining,
                callback,
            )
    finally:
        if original_resume is None:
            os.environ.pop("D3_ENGINE_RESUME", None)
        else:
            os.environ["D3_ENGINE_RESUME"] = original_resume
        _SIGNAL_CONTEXT = None

    ordered = _rows_by_step(rows)
    expected_steps = list(range(n_steps + 1))
    if [int(row["step"]) for row in ordered] != expected_steps:
        raise RuntimeError(f"trace {prefix} is not complete on its declared grid")
    streamed = _read_stream(
        stream_path,
        expected_lam=lam,
        expected_dt=dt,
        expected_kind=run_kind,
    )
    if _json_dumps(streamed) != _json_dumps(ordered):
        raise RuntimeError(f"completed checkpoint/stream mismatch for {prefix}")
    return {"rows": ordered, "ground": ground_metadata, "prefix": prefix}


def _run_in_memory_trace(
    *,
    basis: Any,
    tables: Any,
    lam: float,
    initial: npt.NDArray[np.complex128],
    ground_metadata: dict[str, object],
    budget_gb: float,
) -> dict[str, object]:
    """Validation trace: identical observer/event path, without claim streams."""

    baseline = ground_metadata.get("baseline")
    if not isinstance(baseline, Mapping):
        raise TypeError("validation ground metadata lacks baseline")
    reference_norm = float(np.linalg.norm(initial))
    rows: list[dict[str, object]] = []
    p0_z: list[float] | None = None
    original_resume = os.environ.get("D3_ENGINE_RESUME")
    os.environ["D3_ENGINE_RESUME"] = "0"

    def callback(step: int, psi: npt.NDArray[np.complex128]) -> None:
        nonlocal p0_z
        norm_error = abs(float(np.linalg.norm(psi)) - reference_norm) / reference_norm
        raw = _raw_observables(
            basis=basis,
            tables=tables,
            psi=psi,
            lam=lam,
            budget_gb=budget_gb,
            include_x=step * DT <= HEADLINE_TIME + NUMERIC_GATE_TOL,
            x_baseline_chi=float(baseline["x"]["chi_axial_bits"]),
        )
        if p0_z is None:
            p0_z = [float(value) for value in raw["p_z"]]
        rows.append(
            _assemble_row(
                raw=raw,
                baseline=baseline,
                p0_z=p0_z,
                run_kind="SLAB-METHODS-ONLY",
                geometry=basis.geometry_name,
                lam=lam,
                dt=DT,
                step=step,
                norm_error=norm_error,
            )
        )
        _guard_rss(f"slab protocol lambda={lam:g} step={step}", budget_gb)

    try:
        orbit_engine.evolve(
            basis,
            tables,
            lam,
            initial,
            DT,
            N_STEPS,
            callback,
        )
    finally:
        if original_resume is None:
            os.environ.pop("D3_ENGINE_RESUME", None)
        else:
            os.environ["D3_ENGINE_RESUME"] = original_resume
    return {"rows": _rows_by_step(rows), "ground": ground_metadata}


def _trace_case_summary(case: Mapping[str, object]) -> dict[str, object]:
    rows = [dict(row) for row in case["rows"]]
    ground = dict(case["ground"])
    lam = float(ground["lam"])
    events = {DELTA_KEYS[delta]: _first_event(rows, delta) for delta in DELTAS}
    x_events = {
        DELTA_KEYS[delta]: _first_event(rows, delta, pointer="X")
        for delta in DELTAS
    }
    headline = events[DELTA_KEYS[HEADLINE_DELTA]]
    locality_ok, locality_offenders = _locality_before_axial(rows, headline)
    profile = _profile_summary(rows)
    t0_chi_error = max(
        abs(float(fragment["chi_z_bits"])) for fragment in rows[0]["fragments"]
    )
    diagnostics = {
        "ground_residual": float(ground["residual"]),
        "norm_error": max(
            float(row["diagnostics"]["relative_norm_error"]) for row in rows
        ),
        "entropy_bound_violation": max(
            float(row["diagnostics"]["entropy_bound_violation"]) for row in rows
        ),
        "symmetry_consistency": max(
            float(row["diagnostics"]["symmetry_consistency"]) for row in rows
        ),
        "entropy_roundoff_cleanup": max(
            float(row["diagnostics"]["entropy_roundoff_cleanup"]) for row in rows
        ),
    }
    return {
        "lam": lam,
        "rows": rows,
        "ground": ground,
        "events": events,
        "x_events": x_events,
        "headline": headline,
        "locality_ok": locality_ok,
        "locality_offenders": locality_offenders,
        "profile": profile,
        "t0_chi_error": t0_chi_error,
        "diagnostics": diagnostics,
    }


def _dt_halving_summary(
    coarse_case: Mapping[str, object], fine_case: Mapping[str, object] | None
) -> dict[str, object]:
    if fine_case is None:
        return {
            "gate": True,
            "status": "DECLARED-SUBSAMPLE-NOT-RUN-IN-VALIDATE",
            "onset_shift": None,
            "theta_relative_shift": None,
        }
    coarse_rows = [
        row for row in coarse_case["rows"] if float(row["jt"]) <= FINE_T_FINAL + 1.0e-12
    ]
    fine_rows = [dict(row) for row in fine_case["rows"]]
    coarse_event = _first_event(coarse_rows, DELTAS[0])
    fine_event = _first_event(fine_rows, DELTAS[0])
    if coarse_event is None and fine_event is None:
        return {
            "gate": True,
            "status": "NO-EVENT-BOTH-PHYSICS-ABSENCE",
            "onset_shift": None,
            "theta_relative_shift": None,
        }
    if (coarse_event is None) != (fine_event is None):
        return {
            "gate": False,
            "status": "EVENT-MISMATCH",
            "onset_shift": None,
            "theta_relative_shift": None,
        }
    assert coarse_event is not None and fine_event is not None
    onset_shift = abs(float(coarse_event["jt"]) - float(fine_event["jt"]))
    coarse_theta = float(coarse_event["theta_star"])
    fine_theta = float(fine_event["theta_star"])
    if not np.isfinite(coarse_theta) or not np.isfinite(fine_theta) or coarse_theta == 0.0:
        theta_shift = float("inf")
    else:
        theta_shift = abs(fine_theta - coarse_theta) / abs(coarse_theta)
    gate = bool(
        onset_shift <= DT_ONSET_SHIFT_TOL + NUMERIC_GATE_TOL
        and theta_shift <= DT_THETA_RELATIVE_TOL + NUMERIC_GATE_TOL
    )
    return {
        "gate": gate,
        "status": "OK" if gate else "SHIFT-FAIL",
        "onset_shift": onset_shift,
        "theta_relative_shift": theta_shift,
        "coarse": coarse_event,
        "fine": fine_event,
    }


def _median_theta(
    summaries: Sequence[Mapping[str, object]], delta: float
) -> float | None:
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
    fine_case: Mapping[str, object] | None,
) -> dict[str, object]:
    if set(cases) != set(LAMBDAS):
        raise RuntimeError(f"case lambda set {sorted(cases)} is incomplete")
    summaries = [_trace_case_summary(cases[lam]) for lam in LAMBDAS]
    by_lam = {float(summary["lam"]): summary for summary in summaries}

    check_01 = all(
        list(summary["ground"]["stationary_event_counts"]) == [0, 0, 0]
        and float(summary["t0_chi_error"]) <= ENTROPY_BOUND_TOL
        for summary in summaries
    )

    demolition_ok = all(bool(summary["ground"]["demolition"]["gate"]) for summary in summaries)
    drift_ok = all(
        summary["headline"] is None
        or float(summary["headline"]["tv_drift"]) <= 0.10 + NUMERIC_GATE_TOL
        for summary in summaries
    )
    x_control_ok = all(
        event is None or float(event["jt"]) > HEADLINE_TIME + NUMERIC_GATE_TOL
        for summary in summaries
        for event in summary["x_events"].values()
    )
    check_02 = demolition_ok and drift_ok and x_control_ok

    event_deadline_ok = all(
        summary["headline"] is not None
        and int(summary["headline"]["r_ind"]) >= MIN_REDUNDANCY
        and float(summary["headline"]["jt"]) <= HEADLINE_TIME + NUMERIC_GATE_TOL
        for summary in summaries
    )
    locality_ok = all(bool(summary["locality_ok"]) for summary in summaries)
    persistence_ok = all(
        summary["headline"] is not None and bool(summary["headline"]["persistence"])
        for summary in summaries
    )
    check_03 = event_deadline_ok and locality_ok and persistence_ok

    delta_medians = {
        DELTA_KEYS[delta]: _median_theta(summaries, delta) for delta in DELTAS
    }
    median_values = np.asarray(
        [
            math.nan if delta_medians[DELTA_KEYS[delta]] is None else delta_medians[DELTA_KEYS[delta]]
            for delta in DELTAS
        ],
        dtype=np.float64,
    )
    if np.all(np.isfinite(median_values)) and np.all(median_values > 0.0):
        delta_factor = float(np.max(median_values) / np.min(median_values))
    else:
        delta_factor = float("inf")
    check_04 = bool(
        np.all(np.isfinite(median_values))
        and np.all(median_values > 0.0)
        and delta_factor < DELTA_FACTOR_LIMIT
    )

    bar_cases: dict[float, dict[str, object]] = {}
    below_window = False
    unavailable = False
    headline_theta_values: list[float] = []
    for summary in summaries:
        event = summary["headline"]
        if event is None:
            status = "unavailable"
            theta = None
            unavailable = True
        else:
            theta = float(event["theta_star"])
            headline_theta_values.append(theta)
            status = "inside" if theta >= SPARSE_WINDOW_FLOOR else "BAR-BELOW-WINDOW"
            below_window = below_window or status == "BAR-BELOW-WINDOW"
        bar_cases[float(summary["lam"])] = {"theta_star": theta, "status": status}
    if unavailable:
        check_05 = "unavailable"
    elif below_window:
        check_05 = "BAR-BELOW-WINDOW"
    else:
        check_05 = "inside"
    headline_median = (
        float(np.median(np.asarray(headline_theta_values)))
        if len(headline_theta_values) == len(LAMBDAS)
        else None
    )
    headline_range = (
        (min(headline_theta_values), max(headline_theta_values))
        if len(headline_theta_values) == len(LAMBDAS)
        else (None, None)
    )

    fine_summary = None if fine_case is None else _trace_case_summary(fine_case)
    dt_halving = _dt_halving_summary(by_lam[FINE_LAM], fine_summary)
    maximum_ground_residual = max(
        float(summary["diagnostics"]["ground_residual"]) for summary in summaries
    )
    maximum_norm_error = max(
        float(summary["diagnostics"]["norm_error"]) for summary in summaries
    )
    maximum_entropy_violation = max(
        float(summary["diagnostics"]["entropy_bound_violation"])
        for summary in summaries
    )
    maximum_symmetry_error = max(
        float(summary["diagnostics"]["symmetry_consistency"])
        for summary in summaries
    )
    if fine_summary is not None:
        maximum_norm_error = max(
            maximum_norm_error, float(fine_summary["diagnostics"]["norm_error"])
        )
        maximum_entropy_violation = max(
            maximum_entropy_violation,
            float(fine_summary["diagnostics"]["entropy_bound_violation"]),
        )
        maximum_symmetry_error = max(
            maximum_symmetry_error,
            float(fine_summary["diagnostics"]["symmetry_consistency"]),
        )
    machinery = bool(
        maximum_ground_residual <= GROUND_RESIDUAL_TOL
        and maximum_norm_error <= NORM_ERROR_TOL
        and maximum_entropy_violation <= ENTROPY_BOUND_TOL
        and maximum_symmetry_error <= SYMMETRY_TOL
        and bool(dt_halving["gate"])
    )

    # CHECK-01 is an exact self-subtraction/control invariant.  Its failure is
    # machinery, whereas CHECK-02/03/04 failures are declared physics absence.
    if not machinery or not check_01:
        verdict, exit_code = "MACHINERY-FAIL", 2
    elif not (check_02 and check_03 and check_04):
        verdict, exit_code = "BAR-NOT-PINNED", 1
    else:
        verdict, exit_code = "BAR-DERIVED-EFFECTIVE", 0

    return {
        "summaries": summaries,
        "by_lam": by_lam,
        "check_01": check_01,
        "check_02": check_02,
        "check_02_parts": {
            "demolition": demolition_ok,
            "pointer_drift": drift_ok,
            "x_control": x_control_ok,
        },
        "check_03": check_03,
        "check_03_parts": {
            "deadline": event_deadline_ok,
            "locality": locality_ok,
            "persistence": persistence_ok,
        },
        "check_04": check_04,
        "check_05": check_05,
        "delta_medians": delta_medians,
        "delta_factor": delta_factor,
        "bar_cases": bar_cases,
        "headline_median": headline_median,
        "headline_range": headline_range,
        "below_window": below_window,
        "machinery": machinery,
        "machinery_values": {
            "ground_residual": maximum_ground_residual,
            "norm_error": maximum_norm_error,
            "entropy_bound_violation": maximum_entropy_violation,
            "symmetry_consistency": maximum_symmetry_error,
            "dt_halving": dt_halving,
        },
        "verdict": verdict,
        "exit_code": exit_code,
    }


def _format_demolition(panel: Mapping[str, object]) -> str:
    classes = panel["classes"]
    entries = []
    for class_name, values in classes.items():
        entries.append(
            f"{class_name}:Z={_fmt(values['Z'])}/X={_fmt(values['X'])}/Y={_fmt(values['Y'])}"
        )
    return ",".join(entries)


def _six_output_lines(result: Mapping[str, object]) -> list[str]:
    summaries = list(result["summaries"])
    setup = (
        "SETUP geometry=open-3x3x3 N=27 J=1 open; "
        "H=-sum_<ij>ZiZj-lambda*sum_iXi lambda=[0.05,0.10,0.20]; "
        "prep=uniform-product Bloch=(1,1,1)/sqrt(3); grid=Jt=0:0.1:10 "
        "headline=Jt<=1; pointer=Z_center; fragments=six-axial-single-qubits; "
        "cert=H>=0.05 AND chi>=(1-delta)H AND chi-chi_GS>=0.02 AND "
        "I(Fa:Fb|Z)<=0.02; delta=[0.05,0.10,0.20] headline=0.10 R_ind>=2"
    )

    event_parts: list[str] = []
    for summary in summaries:
        counts = [int(summary["events"][DELTA_KEYS[delta]] is not None) for delta in DELTAS]
        event = summary["headline"]
        if event is None:
            headline = "none"
        else:
            headline = (
                f"t={_fmt(event['jt'])}/theta*={_fmt(event['theta_star'])}/"
                f"R={event['r_ind']}/run={event['consecutive_samples']}/"
                f"{event['label']}"
            )
        event_parts.append(
            f"lambda={float(summary['lam']):g}:N={counts},d0.10={headline}"
        )
    events_line = (
        "EVENTS N-order=delta[0.05,0.10,0.20],first-sampled-hit; "
        + "; ".join(event_parts)
    )

    profile_parts: list[str] = []
    demolition_parts: list[str] = []
    for summary in summaries:
        profile = summary["profile"]
        shells = profile["shell_delta_chi_bits"]
        profile_parts.append(
            f"lambda={float(summary['lam']):g}:t_summax={_fmt(profile['jt'])},"
            f"DeltaChi[d1,d2,d3]={_fmt_vector([shells[1], shells[2], shells[3]])},"
            f"sum={_fmt(profile['sum_delta_chi_bits'])},xi_reg={_fmt(profile['xi_reg'])}"
        )
        panel = summary["ground"]["demolition"]
        demolition_parts.append(
            f"lambda={float(summary['lam']):g}[{_format_demolition(panel)}]"
        )
    profile_line = (
        "PROFILE+DEMOLITION DeltaChi=chi-chi_GS first-argmax(sum_all26); "
        + "; ".join(profile_parts)
        + "; C_F=centered-Frobenius "
        + "; ".join(demolition_parts)
        + f"; max-Z<min-X={result['check_02_parts']['demolition']}"
    )

    bar_case_parts = []
    for lam in LAMBDAS:
        bar = result["bar_cases"][lam]
        bar_case_parts.append(
            f"lambda={lam:g}:theta*={_fmt(bar['theta_star'])}/{bar['status']}"
        )
    delta_parts = [
        f"d={delta:g}:{_fmt(result['delta_medians'][DELTA_KEYS[delta]])}"
        for delta in DELTAS
    ]
    bar_line = (
        "BAR delta-medians=" + ",".join(delta_parts)
        + f" factor={_fmt(result['delta_factor'])}(<1.5); headline "
        + "; ".join(bar_case_parts)
        + f"; median={_fmt(result['headline_median'])}"
        + f" range={_fmt_vector(result['headline_range'])}"
    )

    machinery = result["machinery_values"]
    dt_panel = machinery["dt_halving"]
    control_parts = [
        f"lambda={float(summary['lam']):g}:{summary['ground']['stationary_event_counts']}"
        for summary in summaries
    ]
    x_parts = []
    for summary in summaries:
        x_hits = [
            event
            for event in summary["x_events"].values()
            if event is not None and float(event["jt"]) <= HEADLINE_TIME + NUMERIC_GATE_TOL
        ]
        x_parts.append(f"lambda={float(summary['lam']):g}:{len(x_hits)}")
    checks_line = (
        f"CHECKS+MACHINERY CHECK-01={'ok' if result['check_01'] else 'FAIL'}"
        f"(GS-events={control_parts},t0-chi<=1e-9); "
        f"CHECK-02={'ok' if result['check_02'] else 'FAIL'}"
        f"(comm={result['check_02_parts']['demolition']},"
        f"Z-TV<=0.10={result['check_02_parts']['pointer_drift']},"
        f"X-onsets-by1={x_parts}); "
        f"CHECK-03={'ok' if result['check_03'] else 'FAIL'}"
        f"(deadline={result['check_03_parts']['deadline']},"
        f"locality={result['check_03_parts']['locality']},"
        f"persistence={result['check_03_parts']['persistence']}); "
        f"CHECK-04={'ok' if result['check_04'] else 'FAIL'}"
        f"(factor={_fmt(result['delta_factor'])}); CHECK-05={result['check_05']}; "
        f"MACHINERY={'ok' if result['machinery'] else 'FAIL'}"
        f"(GSres={float(machinery['ground_residual']):.2e},"
        f"norm={float(machinery['norm_error']):.2e},"
        f"entropy-bound={float(machinery['entropy_bound_violation']):.2e},"
        f"symmetry={float(machinery['symmetry_consistency']):.2e},"
        f"dt-half={dt_panel['status']}/dt-shift={_fmt(dt_panel['onset_shift'])}/"
        f"theta-rel-shift={_fmt(dt_panel['theta_relative_shift'])})"
    )

    if result["check_05"] == "inside":
        window = "inside"
    elif result["check_05"] == "BAR-BELOW-WINDOW":
        window = "below"
    else:
        window = "unavailable"
    xi_parts = [
        f"lambda={float(summary['lam']):g}:{_fmt(summary['profile']['xi_reg'])}"
        for summary in summaries
    ]
    persistence_values = [
        summary["headline"] is not None and bool(summary["headline"]["persistence"])
        for summary in summaries
    ]
    persistence = "all" if all(persistence_values) else (
        "partial" if any(persistence_values) else "none"
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
    total = (
        f"TOTAL {result['verdict']} theta*={_fmt(result['headline_median'])} "
        f"window={window} xi_reg=[{','.join(xi_parts)}] persistence={persistence} "
        f"flags={','.join(flags) if flags else 'none'} "
        f"failed={','.join(failed) if failed else 'none'} "
        "SPEC-NOTE=not-basis-neutral:ZZ-and-declared-Z-pointer-privilege-Z;"
        "comparator-inputs:H=-sumZZ-lambda-sumX,prep=uniform-(1,1,1)/sqrt3,"
        "pointer=Z_center,tolerances=H0.05/content-delta[0.05,0.10,0.20]/"
        "excess0.02/conditional-independence0.02/TV0.10,"
        "theta-map=mean-six-center-bonds-GS-subtracted-(1-purity)-unnormalized-unclipped;"
        "finite-volume:open-3^3-face-registers-no-radial-buffer,persistence-flag-finite-time-only;"
        "no-formation-rule;no-audit-status"
    )
    lines = [setup, events_line, profile_line, bar_line, checks_line, total]
    if len(lines) != 6 or any("\n" in line for line in lines):
        raise AssertionError("six-line stdout contract construction failed")
    return lines


def _failure_lines(mode: str, exc: BaseException) -> list[str]:
    message = " ".join(str(exc).split())[:300]
    spec_note = (
        "not-basis-neutral:ZZ-and-declared-Z-pointer-privilege-Z;"
        "comparator-inputs:H/preparation/pointer/tolerances/theta-map-as-frozen;"
        "finite-volume:face-registers-no-radial-buffer,persistence-finite-time-only;"
        "no-formation-rule;no-audit-status"
    )
    return [
        f"SETUP mode={mode} status=incomplete",
        "EVENTS unavailable",
        "PROFILE+DEMOLITION unavailable",
        "BAR unavailable",
        f"CHECKS+MACHINERY MACHINERY=FAIL error={type(exc).__name__}:{message}",
        f"TOTAL MACHINERY-FAIL theta*=unavailable window=unavailable xi_reg=unavailable persistence=unavailable flags=none failed=MACHINERY SPEC-NOTE={spec_note}",
    ]


def _checkpoint_ground_if_present(
    *,
    prefix: str,
    basis: Any,
    lam: float,
    dt: float,
    n_steps: int,
    initial_checksum: str,
) -> dict[str, object] | None:
    path = _newest_checkpoint_path(prefix)
    if path is None:
        return None
    loaded = _load_trace_checkpoint(
        path,
        expected_prefix=prefix,
        basis=basis,
        lam=lam,
        dt=dt,
        n_steps=n_steps,
        initial_checksum=initial_checksum,
        load_state=False,
    )
    return dict(loaded["ground"])


def run_full() -> int:
    _require_engine_api()
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    run_started = time.monotonic()
    basis = orbit_engine.build_orbit_basis()
    tables = orbit_engine.build_hamiltonian_tables(basis)
    if basis.geometry_name != "open-3x3x3" or basis.n_orbits != orbit_engine.EXPECTED_CUBE_ORBITS:
        raise AssertionError("claim-bearing basis is not the verified open 3^3 cube")
    initial = orbit_engine._reduced_product_state(basis)
    initial_checksum = _state_checksum(initial)
    _guard_rss("full setup", FULL_RSS_GB)

    total_units = len(LAMBDAS) * (N_STEPS + 1) + (FINE_N_STEPS + 1)
    cases: dict[float, dict[str, object]] = {}
    for lam_index, lam in enumerate(LAMBDAS):
        prefix = _trace_prefix(lam)
        metadata = _checkpoint_ground_if_present(
            prefix=prefix,
            basis=basis,
            lam=lam,
            dt=DT,
            n_steps=N_STEPS,
            initial_checksum=initial_checksum,
        )
        if metadata is None:
            _ground, metadata = _prepare_ground_and_baseline(
                basis, tables, lam, FULL_RSS_GB
            )
            del _ground
        cases[lam] = _run_persistent_trace(
            basis=basis,
            tables=tables,
            lam=lam,
            dt=DT,
            n_steps=N_STEPS,
            fine=False,
            initial=initial,
            ground_metadata=metadata,
            run_started=run_started,
            progress_base_units=lam_index * (N_STEPS + 1),
            progress_total_units=total_units,
        )
        if _SIGTERM_PENDING:
            raise SigtermRequested("SIGTERM received between lambda traces")

    fine_prefix = _trace_prefix(FINE_LAM, fine=True)
    fine_metadata = _checkpoint_ground_if_present(
        prefix=fine_prefix,
        basis=basis,
        lam=FINE_LAM,
        dt=FINE_DT,
        n_steps=FINE_N_STEPS,
        initial_checksum=initial_checksum,
    )
    if fine_metadata is None:
        fine_metadata = dict(cases[FINE_LAM]["ground"])
    fine_case = _run_persistent_trace(
        basis=basis,
        tables=tables,
        lam=FINE_LAM,
        dt=FINE_DT,
        n_steps=FINE_N_STEPS,
        fine=True,
        initial=initial,
        ground_metadata=fine_metadata,
        run_started=run_started,
        progress_base_units=len(LAMBDAS) * (N_STEPS + 1),
        progress_total_units=total_units,
    )
    result = _analyze_cases(cases, fine_case)
    for line in _six_output_lines(result):
        print(line)
    return int(result["exit_code"])


def _load_report_case(
    *, lam: float, dt: float, n_steps: int, fine: bool
) -> dict[str, object]:
    prefix = _trace_prefix(lam, fine=fine)
    kind = "cube-dt-halving-subsample" if fine else "cube-full"
    rows = _read_stream(
        _stream_path(lam, fine=fine),
        expected_lam=lam,
        expected_dt=dt,
        expected_kind=kind,
    )
    expected = list(range(n_steps + 1))
    if [int(row["step"]) for row in rows] != expected:
        raise RuntimeError(f"observable stream {prefix} is incomplete")
    checkpoint_path = _newest_checkpoint_path(prefix)
    if checkpoint_path is None:
        raise FileNotFoundError(f"missing checkpoint for {prefix}")
    checkpoint = _load_trace_checkpoint(
        checkpoint_path,
        expected_prefix=prefix,
        lam=lam,
        dt=dt,
        n_steps=n_steps,
        load_state=False,
    )
    if int(checkpoint["step"]) != n_steps:
        raise RuntimeError(f"newest checkpoint for {prefix} is not complete")
    checkpoint_rows = list(checkpoint["rows"])
    if _json_dumps(checkpoint_rows) != _json_dumps(rows):
        raise RuntimeError(f"stream/checkpoint observable mismatch for {prefix}")
    return {"rows": rows, "ground": dict(checkpoint["ground"])}


def run_report() -> int:
    _require_engine_api()
    cases = {
        lam: _load_report_case(lam=lam, dt=DT, n_steps=N_STEPS, fine=False)
        for lam in LAMBDAS
    }
    fine_case = _load_report_case(
        lam=FINE_LAM,
        dt=FINE_DT,
        n_steps=FINE_N_STEPS,
        fine=True,
    )
    result = _analyze_cases(cases, fine_case)
    for line in _six_output_lines(result):
        print(line)
    return int(result["exit_code"])


def _slab_event_text(result: Mapping[str, object]) -> str:
    parts = []
    for summary in result["summaries"]:
        event = summary["headline"]
        parts.append(
            f"lambda={float(summary['lam']):g}:"
            + (
                "none"
                if event is None
                else f"t={_fmt(event['jt'])}/theta*={_fmt(event['theta_star'])}/R={event['r_ind']}/{event['label']}"
            )
        )
    return "; ".join(parts)


def run_validate() -> int:
    _require_engine_api()
    started = time.monotonic()
    dense = orbit_engine.dense_slab_crosscheck()
    geometry = orbit_engine._slab_geometry()
    slab_basis = orbit_engine._build_basis_for_geometry(geometry)
    slab_tables = orbit_engine.build_hamiltonian_tables(slab_basis)
    slab_initial = orbit_engine._reduced_product_state(slab_basis)
    slab_cases: dict[float, dict[str, object]] = {}
    for lam in LAMBDAS:
        ground, metadata = _prepare_ground_and_baseline(
            slab_basis, slab_tables, lam, VALIDATE_RSS_GB
        )
        del ground
        slab_cases[lam] = _run_in_memory_trace(
            basis=slab_basis,
            tables=slab_tables,
            lam=lam,
            initial=slab_initial,
            ground_metadata=metadata,
            budget_gb=VALIDATE_RSS_GB,
        )
    slab_result = _analyze_cases(slab_cases, None)

    # Claim-bearing cube controls exercise the exact cube basis, tables and
    # all three same-lambda GS calculations, but never launch long evolution.
    cube_basis = orbit_engine.build_orbit_basis()
    cube_tables = orbit_engine.build_hamiltonian_tables(cube_basis)
    cube_controls: list[dict[str, object]] = []
    maximum_cube_residual = 0.0
    for lam in LAMBDAS:
        ground, metadata = _prepare_ground_and_baseline(
            cube_basis, cube_tables, lam, VALIDATE_RSS_GB
        )
        maximum_cube_residual = max(
            maximum_cube_residual, float(metadata["residual"])
        )
        cube_controls.append(metadata)
        del ground

    cube_initial = orbit_engine._reduced_product_state(cube_basis)
    cube_t0_raw = _raw_observables(
        basis=cube_basis,
        tables=cube_tables,
        psi=cube_initial,
        lam=HEADLINE_DELTA,
        budget_gb=VALIDATE_RSS_GB,
        include_x=False,
        x_baseline_chi=None,
    )
    cube_t0_chi = max(
        abs(float(value)) for value in dict(cube_t0_raw["chi_z_bits"]).values()
    )
    if cube_t0_chi > ENTROPY_BOUND_TOL:
        raise AssertionError(
            f"cube product preparation t=0 chi {cube_t0_chi:.3e} exceeds 1e-9"
        )
    cube_control_ok = all(
        metadata["stationary_event_counts"] == [0, 0, 0]
        and bool(metadata["demolition"]["gate"])
        for metadata in cube_controls
    )
    elapsed = time.monotonic() - started
    _guard_rss("complete validation", VALIDATE_RSS_GB)
    methods_machinery = bool(
        slab_result["machinery"]
        and cube_control_ok
        and maximum_cube_residual <= GROUND_RESIDUAL_TOL
        and cube_t0_chi <= ENTROPY_BOUND_TOL
        and float(dense["rss_peak_gb"]) <= VALIDATE_RSS_GB
        and elapsed < VALIDATE_WALL_SECONDS
    )

    control_text = "; ".join(
        f"lambda={float(metadata['lam']):g}:events={metadata['stationary_event_counts']}/"
        f"GSres={float(metadata['residual']):.2e}/"
        f"C_F[{_format_demolition(metadata['demolition'])}]"
        for metadata in cube_controls
    )
    profile_text = "; ".join(
        f"lambda={float(summary['lam']):g}:xi={_fmt(summary['profile']['xi_reg'])}/"
        f"shells={_fmt_vector([summary['profile']['shell_delta_chi_bits'][shell] for shell in (1,2,3)])}"
        for summary in slab_result["summaries"]
    )
    lines = [
        "SLAB-METHODS-ONLY SETUP geometry=open-3x3x2 physics-claim=none; full protocol grid/lambdas/deltas/gates observer-path exercised with cube-label fragment surrogate",
        "SLAB-METHODS-ONLY EVENTS " + _slab_event_text(slab_result),
        "SLAB-METHODS-ONLY PROFILE " + profile_text,
        f"SLAB-METHODS-ONLY CHECK-EXERCISE check01={slab_result['check_01']} check02={slab_result['check_02']} check03={slab_result['check_03']} check04={slab_result['check_04']} check05={slab_result['check_05']} (no physics verdict)",
        f"SLAB-METHODS-ONLY CUBE-CONTROLS {control_text}; t0-intersite-chi={cube_t0_chi:.2e}; demolition=max-Z<min-X",
        f"SLAB-METHODS-ONLY MACHINERY slab-orbits={dense['slab_orbits']} max-observable-dev={max(dense['maximum_deviations'].values()):.2e} dense/reduced-norm={max(dense['dense_norm_drift'],dense['reduced_norm_drift']):.2e} cube-GSres={maximum_cube_residual:.2e} RSS={orbit_engine.rss_gb():.3f}GiB elapsed={elapsed:.1f}s limit=<900s",
        f"SLAB-METHODS-ONLY TOTAL {'VALIDATION-PASS' if methods_machinery else 'MACHINERY-FAIL'} no-physics-claim no-formation-rule no-audit-status",
    ]
    if any("SLAB-METHODS-ONLY" not in line or "\n" in line for line in lines):
        raise AssertionError("validation output labeling contract failed")
    for line in lines:
        print(line)
    return 0 if methods_machinery else 2


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run, validate, or report the frozen d=3 registration pilot."
    )
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--validate", action="store_true", help="methods validation (default)")
    modes.add_argument("--full", action="store_true", help="overnight claim-bearing cube sweep")
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
        except Exception as exc:  # noqa: BLE001 - preserve stdout contract.
            for line in _failure_lines("full", exc):
                print(line)
            return 2
        finally:
            signal.signal(signal.SIGTERM, previous_handler)
    if args.report:
        try:
            return run_report()
        except Exception as exc:  # noqa: BLE001 - preserve stdout contract.
            for line in _failure_lines("report", exc):
                print(line)
            return 2
    try:
        return run_validate()
    except Exception as exc:  # noqa: BLE001 - validation has its own label.
        message = " ".join(str(exc).split())[:400]
        print(
            f"SLAB-METHODS-ONLY FAILURE {type(exc).__name__}:{message}"
        )
        print(
            "SLAB-METHODS-ONLY TOTAL MACHINERY-FAIL no-physics-claim "
            "no-formation-rule no-audit-status"
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
