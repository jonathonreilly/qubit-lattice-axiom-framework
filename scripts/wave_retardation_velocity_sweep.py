#!/usr/bin/env python3
"""Controlled finite-carrier checks for the moving-source schedule sweep.

This runner does not infer a continuum law or a laboratory prediction.  It
recomputes two explicitly controlled finite sweeps and matched counterchecks:

* fixed final detector layer, so the post-motion buffer varies with schedule rate;
* fixed post-motion buffer, so the detector layer varies with schedule rate;
* equal-rate shifted-trajectory and fixed-trajectory, varied-buffer pairs.

The source moves from integer cell 6 to integer cell 0.  Its onset, rounding
rule, elapsed motion intervals, endpoint, stationary clamp and measurement
layers are all explicit.  Rates are in source cells per layer and are not
normalized to a physical propagation constant.  The printed log-log slopes
are shape diagnostics only; they are never reported as scaling exponents.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
AUDIT_TIMEOUT_SEC = 1800

import argparse
import hashlib
import json
import math
import os
import random
from dataclasses import dataclass, replace
from pathlib import Path
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import wave_retarded_gravity as wrg


HELPER_PATH = Path(wrg.__file__).resolve()


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


@dataclass(frozen=True)
class Carrier:
    n_layers: int = 78
    onset: int = 10
    start_cell: int = 6
    end_cell: int = 0
    fixed_buffer: int = 7
    final_layer: int = 77
    seed: int = 0
    drift: float = 0.20
    restore: float = 0.70
    strength: float = wrg.S
    beam_k: float = wrg.K
    poisson_omega: float = 1.8
    poisson_tolerance: float = 1e-11
    poisson_max_iterations: int = 20000


CARRIER = Carrier()
DURATIONS = (60, 30, 20, 15, 12, 10, 8)
BUFFER_SCAN = (4, 7, 12, 20, 47)
INDEPENDENT_DURATIONS = (60, 20, 8)
SIGNAL_FLOOR = 1e-10


@dataclass(frozen=True)
class ControlledTrajectory:
    onset: int
    start_cell: int
    end_cell: int
    motion_intervals: int

    @property
    def endpoint_layer(self):
        return self.onset + self.motion_intervals

    @property
    def speed(self):
        return abs(self.end_cell - self.start_cell) / self.motion_intervals

    def position(self, layer):
        """Rounded linear motion followed by a stationary endpoint clamp."""
        if layer <= self.onset:
            return self.start_cell
        if layer >= self.endpoint_layer:
            return self.end_cell
        elapsed = layer - self.onset
        displacement = (self.end_cell - self.start_cell) * elapsed
        return self.start_cell + int(round(displacement / self.motion_intervals))

    def metadata(self, measurement_layer):
        return {
            "n_layers": CARRIER.n_layers,
            "onset": self.onset,
            "start_cell": self.start_cell,
            "end_cell": self.end_cell,
            "motion_intervals": self.motion_intervals,
            "speed": self.speed,
            "endpoint_layer": self.endpoint_layer,
            "measurement_layer": measurement_layer,
            "post_active_buffer": measurement_layer - self.endpoint_layer,
            "sampled_positions": [
                self.position(layer)
                for layer in range(self.onset, self.endpoint_layer + 1)
            ],
        }


@dataclass(frozen=True)
class Measurement:
    d_moving: float
    d_instantaneous: float
    difference: float
    relative_gap: float | None
    sign_relation: str


def make_trajectory(duration, *, start_cell=None, end_cell=None, onset=None):
    return ControlledTrajectory(
        CARRIER.onset if onset is None else onset,
        CARRIER.start_cell if start_cell is None else start_cell,
        CARRIER.end_cell if end_cell is None else end_cell,
        duration,
    )


def validate_trajectory(trajectory, measurement_layer, *, n_layers=None):
    if n_layers is None:
        n_layers = CARRIER.n_layers
    if trajectory.motion_intervals <= 0:
        raise AssertionError("motion interval count must be positive")
    if not 2 <= trajectory.onset < trajectory.endpoint_layer:
        raise AssertionError("onset/endpoint layers are invalid")
    if not trajectory.endpoint_layer <= measurement_layer < n_layers:
        raise AssertionError("endpoint, detector, and lattice ordering is invalid")
    if trajectory.position(trajectory.onset) != trajectory.start_cell:
        raise AssertionError("source does not start at the advertised cell")
    if trajectory.position(trajectory.endpoint_layer) != trajectory.end_cell:
        raise AssertionError("source does not reach the advertised endpoint")
    if any(
        trajectory.position(t) != trajectory.end_cell
        for t in range(trajectory.endpoint_layer, n_layers)
    ):
        raise AssertionError("source continues moving during the propagation buffer")
    grid_half_width = int(wrg.PW / wrg.H)
    positions = [trajectory.position(t) for t in range(n_layers)]
    if min(positions) <= -grid_half_width or max(positions) >= grid_half_width:
        raise AssertionError("source reaches the Dirichlet boundary")


def assert_same_fixed_controls(reference, candidate, *, allow_measurement_change=False):
    fixed = (
        "n_layers",
        "onset",
        "start_cell",
        "end_cell",
        "seed",
        "drift",
        "restore",
        "strength",
        "beam_k",
        "poisson_omega",
        "poisson_tolerance",
        "poisson_max_iterations",
    )
    if not allow_measurement_change:
        fixed += ("final_layer",)
    changed = [name for name in fixed if getattr(reference, name) != getattr(candidate, name)]
    if changed:
        raise AssertionError("controls changed: " + ", ".join(changed))


def robust_gap(d_moving, d_instantaneous):
    denominator = max(abs(d_moving), abs(d_instantaneous))
    if denominator <= SIGNAL_FLOOR:
        return None
    return abs(d_moving - d_instantaneous) / denominator


def sign_relation(left, right):
    left_zero = abs(left) <= SIGNAL_FLOOR
    right_zero = abs(right) <= SIGNAL_FLOOR
    if left_zero or right_zero:
        return "near-zero"
    return "same" if left * right > 0.0 else "opposite"


def measure(d_moving, d_instantaneous):
    return Measurement(
        d_moving,
        d_instantaneous,
        d_moving - d_instantaneous,
        robust_gap(d_moving, d_instantaneous),
        sign_relation(d_moving, d_instantaneous),
    )


def diagnostic_slope(xs, ys):
    points = [(x, y) for x, y in zip(xs, ys) if x > 0 and y is not None and y > 0]
    if len(points) < 2:
        return None
    lx = [math.log(x) for x, _ in points]
    ly = [math.log(y) for _, y in points]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    sxx = sum((x - mx) ** 2 for x in lx)
    if sxx == 0.0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(lx, ly)) / sxx


def monotonicity(values):
    clean = [value for value in values if value is not None]
    if len(clean) != len(values) or len(clean) < 2:
        return "not-clean"
    increasing = all(b > a for a, b in zip(clean, clean[1:]))
    decreasing = all(b < a for a, b in zip(clean, clean[1:]))
    return "increasing" if increasing else "decreasing" if decreasing else "non-monotone"


def build_context():
    pos, adj, nmap = wrg.grow(
        CARRIER.seed,
        CARRIER.drift,
        CARRIER.restore,
        n_layers=CARRIER.n_layers,
    )
    free = wrg._prop_beam(
        pos, adj, nmap, None, CARRIER.beam_k, n_layers=CARRIER.n_layers
    )
    return pos, adj, nmap, free


def evaluate_trajectory(context, trajectory, measurement_layers):
    pos, adj, nmap, free = context
    for layer in measurement_layers:
        validate_trajectory(trajectory, layer)
    moving_field = wrg._make_field(
        CARRIER.strength,
        trajectory.position,
        src_layer_start=trajectory.onset,
        n_layers=CARRIER.n_layers,
    )
    instantaneous_field = wrg._make_instantaneous(
        CARRIER.strength,
        trajectory.position,
        src_layer_start=trajectory.onset,
        n_layers=CARRIER.n_layers,
        omega=CARRIER.poisson_omega,
        tol=CARRIER.poisson_tolerance,
        max_iter=CARRIER.poisson_max_iterations,
    )
    moving = wrg._prop_beam(
        pos, adj, nmap, moving_field, CARRIER.beam_k, n_layers=CARRIER.n_layers
    )
    instantaneous = wrg._prop_beam(
        pos,
        adj,
        nmap,
        instantaneous_field,
        CARRIER.beam_k,
        n_layers=CARRIER.n_layers,
    )
    measured = {}
    for layer in sorted(set(measurement_layers)):
        z_free = wrg._cz_at_layer(free, pos, nmap, layer)
        d_moving = wrg._cz_at_layer(moving, pos, nmap, layer) - z_free
        d_instantaneous = (
            wrg._cz_at_layer(instantaneous, pos, nmap, layer) - z_free
        )
        measured[layer] = measure(d_moving, d_instantaneous)
    return measured


def measurement_record(duration, trajectory, layer, value):
    return {
        "duration": duration,
        "speed": trajectory.speed,
        "endpoint_layer": trajectory.endpoint_layer,
        "measurement_layer": layer,
        "buffer": layer - trajectory.endpoint_layer,
        "start_cell": trajectory.start_cell,
        "end_cell": trajectory.end_cell,
        "d_moving": value.d_moving,
        "d_instantaneous": value.d_instantaneous,
        "difference": value.difference,
        "relative_gap": value.relative_gap,
        "sign_relation": value.sign_relation,
    }


def normal_evidence(*, verbose=True):
    context = build_context()
    fixed_final = []
    fixed_buffer = []
    buffer_scan = []

    for duration in DURATIONS:
        trajectory = make_trajectory(duration)
        buffer_layer = trajectory.endpoint_layer + CARRIER.fixed_buffer
        layers = {CARRIER.final_layer, buffer_layer}
        if duration == 20:
            layers.update(trajectory.endpoint_layer + value for value in BUFFER_SCAN)
        values = evaluate_trajectory(context, trajectory, layers)
        fixed_final.append(
            measurement_record(
                duration, trajectory, CARRIER.final_layer, values[CARRIER.final_layer]
            )
        )
        fixed_buffer.append(
            measurement_record(duration, trajectory, buffer_layer, values[buffer_layer])
        )
        if duration == 20:
            for buffer in BUFFER_SCAN:
                layer = trajectory.endpoint_layer + buffer
                buffer_scan.append(
                    measurement_record(duration, trajectory, layer, values[layer])
                )

    base = make_trajectory(20)
    shifted = make_trajectory(20, start_cell=8, end_cell=2)
    pair_layer = base.endpoint_layer + CARRIER.fixed_buffer
    shifted_values = evaluate_trajectory(
        context, shifted, (pair_layer, CARRIER.final_layer)
    )
    base_at_pair = next(row for row in fixed_buffer if row["duration"] == 20)
    shifted_at_pair = measurement_record(
        20, shifted, pair_layer, shifted_values[pair_layer]
    )
    geometry_pair = [base_at_pair, shifted_at_pair]

    evidence = {
        "carrier": {
            "n_layers": CARRIER.n_layers,
            "onset": CARRIER.onset,
            "start_cell": CARRIER.start_cell,
            "end_cell": CARRIER.end_cell,
            "fixed_buffer": CARRIER.fixed_buffer,
            "final_layer": CARRIER.final_layer,
            "seed": CARRIER.seed,
            "drift": CARRIER.drift,
            "restore": CARRIER.restore,
            "H": wrg.H,
            "PW": wrg.PW,
            "beta": wrg.BETA,
            "max_d_phys": wrg.MAX_D_PHYS,
            "long_wavelength_rate_cells_per_layer": wrg.H,
            "helper_sha256": sha256_file(HELPER_PATH),
            "strength": CARRIER.strength,
            "beam_k": CARRIER.beam_k,
            "poisson_omega": CARRIER.poisson_omega,
            "poisson_tolerance": CARRIER.poisson_tolerance,
            "poisson_max_iterations": CARRIER.poisson_max_iterations,
            "rounding": "Python round (ties-to-even), then int",
            "boundary_cells": [-int(wrg.PW / wrg.H), int(wrg.PW / wrg.H)],
        },
        "fixed_final": fixed_final,
        "fixed_buffer": fixed_buffer,
        "buffer_scan": buffer_scan,
        "geometry_pair": geometry_pair,
        "schedules": [
            make_trajectory(duration).metadata(CARRIER.final_layer)
            for duration in DURATIONS
        ],
    }
    evidence["fingerprint"] = evidence_fingerprint(evidence)
    if verbose:
        print_normal(evidence)
    return evidence, context


def canonical_measurement(row):
    return {
        key: (format(value, ".12g") if isinstance(value, float) else value)
        for key, value in row.items()
    }


def evidence_fingerprint(evidence):
    payload = {
        "carrier": evidence["carrier"],
        "fixed_final": [canonical_measurement(row) for row in evidence["fixed_final"]],
        "fixed_buffer": [canonical_measurement(row) for row in evidence["fixed_buffer"]],
        "buffer_scan": [canonical_measurement(row) for row in evidence["buffer_scan"]],
        "geometry_pair": [canonical_measurement(row) for row in evidence["geometry_pair"]],
        "schedules": evidence["schedules"],
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def format_gap(value):
    return "undefined" if value is None else f"{value:.2%}"


def print_rows(title, rows):
    print("\n" + title)
    print("  dur  cell/layer  end  meas  buf       dM         dI        M-I       rel  sign")
    for row in rows:
        print(
            f"  {row['duration']:>3d}      {row['speed']:.3f}  {row['endpoint_layer']:>4d}"
            f"  {row['measurement_layer']:>4d}  {row['buffer']:>3d}"
            f"  {row['d_moving']:+.6f}  {row['d_instantaneous']:+.6f}"
            f"  {row['difference']:+.6f}  {format_gap(row['relative_gap']):>8s}"
            f"  {row['sign_relation']}"
        )


def print_normal(evidence):
    c = evidence["carrier"]
    print("=" * 96)
    print("CONTROLLED FINITE WAVE-RETARDATION CARRIER")
    print("=" * 96)
    print(
        f"NL={c['n_layers']} onset={c['onset']} start={c['start_cell']} "
        f"endpoint={c['end_cell']} detector_final={c['final_layer']}"
    )
    print(
        f"H={c['H']} PW={c['PW']} max_d_phys={c['max_d_phys']} "
        f"beta={c['beta']} seed={c['seed']} drift={c['drift']} "
        f"restore={c['restore']} S={c['strength']} K={c['beam_k']}"
    )
    print(
        "SOR omega={poisson_omega} tolerance={poisson_tolerance:.1e} "
        "max_iterations={poisson_max_iterations}".format(**c)
    )
    print("Schedule: D elapsed intervals; endpoint at onset+D; stationary clamp thereafter")
    print(
        "Wave dispersion: sin^2(omega/2)=H^2[sin^2(ky/2)+sin^2(kz/2)]; "
        f"long-wave rate={c['long_wavelength_rate_cells_per_layer']:.3f} cell/layer"
    )
    print(f"helper_sha256={c['helper_sha256']}")
    print("Identity: D=|end-start|/schedule_rate and measurement=onset+D+buffer")
    print(
        "Therefore fixed endpoints plus varying schedule rate force D to vary; "
        "final time or buffer must vary."
    )
    print_rows("A. FIXED FINAL LAYER (buffer varies)", evidence["fixed_final"])
    print_rows("B. FIXED SEVEN-LAYER BUFFER (measurement layer varies)", evidence["fixed_buffer"])
    print_rows("C. D=20 FIXED TRAJECTORY, BUFFER SCAN", evidence["buffer_scan"])
    print_rows(
        "D. SAME 0.300 CELL/LAYER AND D=20, SHIFTED GEOMETRY",
        evidence["geometry_pair"],
    )

    for name in ("fixed_final", "fixed_buffer"):
        rows = evidence[name]
        slopes = {
            "absolute difference": diagnostic_slope(
                [row["speed"] for row in rows],
                [abs(row["difference"]) for row in rows],
            ),
            "relative gap": diagnostic_slope(
                [row["speed"] for row in rows],
                [row["relative_gap"] for row in rows],
            ),
        }
        gap_shape = monotonicity([row["relative_gap"] for row in rows])
        diff_shape = monotonicity([abs(row["difference"]) for row in rows])
        signs = [math.copysign(1.0, row["difference"]) for row in rows]
        sign_changes = sum(left != right for left, right in zip(signs, signs[1:]))
        print(f"\n{name} diagnostics: |M-I|={diff_shape}; relative gap={gap_shape}")
        print(f"  signed M-I reversals across adjacent rows={sign_changes}")
        for label, slope in slopes.items():
            rendered = "undefined" if slope is None else f"{slope:+.3f}"
            print(f"  log-log {label} slope={rendered} (diagnostic only, not an exponent)")
    print(f"\ncontrolled-result fingerprint: {evidence['fingerprint']}")
    print("normal evidence objects: 21")


def independent_position(layer, onset, start_cell, end_cell, duration):
    """Separately implemented schedule used only by the independent mode."""
    elapsed = min(max(layer - onset, 0), duration)
    if elapsed == duration:
        return end_cell
    return start_cell + int(round((end_cell - start_cell) * elapsed / duration))


def independent_carrier():
    """Rebuild the seeded carrier as layer arrays without the helper graph."""
    import numpy as np

    half = 16
    width = 2 * half + 1
    y = np.zeros((CARRIER.n_layers, width, width), dtype=float)
    z = np.zeros_like(y)
    coordinates = np.arange(-half, half + 1, dtype=float) * 0.5
    y[1] = coordinates[:, None]
    z[1] = coordinates[None, :]
    rng = random.Random(CARRIER.seed)
    for layer in range(2, CARRIER.n_layers):
        for ai, iy in enumerate(range(-half, half + 1)):
            for aj, iz in enumerate(range(-half, half + 1)):
                next_y = y[layer - 1, ai, aj] + rng.gauss(
                    0.0, CARRIER.drift * 0.5
                )
                next_z = z[layer - 1, ai, aj] + rng.gauss(
                    0.0, CARRIER.drift * 0.5
                )
                y[layer, ai, aj] = (
                    (1.0 - CARRIER.restore) * next_y
                    + CARRIER.restore * iy * 0.5
                )
                z[layer, ai, aj] = (
                    (1.0 - CARRIER.restore) * next_z
                    + CARRIER.restore * iz * 0.5
                )
    return y, z


def independent_wave_history(strength, position):
    """Array-stencil leapfrog route with no helper calls."""
    import numpy as np

    half = 16
    width = 2 * half + 1
    history = np.zeros((CARRIER.n_layers, width, width), dtype=float)
    previous = np.zeros((width, width), dtype=float)
    current = np.zeros_like(previous)
    for layer in range(2, CARRIER.n_layers):
        laplacian = np.zeros_like(current)
        laplacian[1:-1, 1:-1] = (
            current[:-2, 1:-1]
            + current[2:, 1:-1]
            + current[1:-1, :-2]
            + current[1:-1, 2:]
            - 4.0 * current[1:-1, 1:-1]
        )
        source = np.zeros_like(current)
        if layer >= CARRIER.onset:
            source[half, half + position(layer)] = strength
        following = 2.0 * current - previous + 0.25 * (laplacian + source)
        history[layer] = following
        previous, current = current, following
    return history


def independent_poisson_solver():
    """Sparse-direct Dirichlet solve, algebraically distinct from primary SOR."""
    import numpy as np
    from scipy.sparse import diags, eye, kron
    from scipy.sparse.linalg import factorized

    interior = 31
    one_d = diags(
        [
            -np.ones(interior - 1),
            2.0 * np.ones(interior),
            -np.ones(interior - 1),
        ],
        [-1, 0, 1],
        format="csc",
    )
    operator = (
        kron(eye(interior, format="csc"), one_d)
        + kron(one_d, eye(interior, format="csc"))
    ).tocsc()
    solve = factorized(operator)

    def field(strength, source_cell):
        rhs = np.zeros(interior * interior, dtype=float)
        rhs[(16 - 1) * interior + (16 + source_cell - 1)] = strength
        result = np.zeros((33, 33), dtype=float)
        interior_result = solve(rhs).reshape(interior, interior)
        residual = operator @ interior_result.ravel() - rhs
        if float(np.max(np.abs(residual))) > 1e-12:
            raise AssertionError("independent sparse Poisson residual is too large")
        result[1:-1, 1:-1] = interior_result
        return result

    return field


def independent_instantaneous_history(strength, position, solve_poisson):
    import numpy as np

    history = np.zeros((CARRIER.n_layers, 33, 33), dtype=float)
    cache = {}
    for layer in range(CARRIER.onset, CARRIER.n_layers):
        source_cell = position(layer)
        if source_cell not in cache:
            cache[source_cell] = solve_poisson(strength, source_cell)
        history[layer] = cache[source_cell]
    return history


def independent_centroids(histories, y, z, detector_layer):
    """Propagate layer arrays and compute centroids without helper calls."""
    import numpy as np

    fields = np.stack(histories)
    channel_count = len(histories)
    amplitude = np.zeros((channel_count, 33, 33), dtype=complex)
    amplitude[:, 16, 16] = 1.0
    for layer in range(detector_layer):
        following = np.zeros_like(amplitude)
        for offset_y in range(-6, 7):
            sy0 = max(0, -offset_y)
            sy1 = min(33, 33 - offset_y)
            dy0 = sy0 + offset_y
            dy1 = sy1 + offset_y
            for offset_z in range(-6, 7):
                sz0 = max(0, -offset_z)
                sz1 = min(33, 33 - offset_z)
                dz0 = sz0 + offset_z
                dz1 = sz1 + offset_z
                source_amplitude = amplitude[:, sy0:sy1, sz0:sz1]
                delta_y = (
                    y[layer + 1, dy0:dy1, dz0:dz1]
                    - y[layer, sy0:sy1, sz0:sz1]
                )
                delta_z = (
                    z[layer + 1, dy0:dy1, dz0:dz1]
                    - z[layer, sy0:sy1, sz0:sz1]
                )
                length = np.sqrt(0.25 + delta_y * delta_y + delta_z * delta_z)
                angle = np.arctan2(
                    np.sqrt(delta_y * delta_y + delta_z * delta_z), 0.5
                )
                weight = np.exp(-0.8 * angle * angle) * 0.25 / (length * length)
                local_field = 0.5 * (
                    fields[:, layer, sy0:sy1, sz0:sz1]
                    + fields[:, layer + 1, dy0:dy1, dz0:dz1]
                )
                phase = np.exp(
                    1j * 5.0 * length[None] * (1.0 - local_field)
                )
                following[:, dy0:dy1, dz0:dz1] += (
                    np.where(
                        np.abs(source_amplitude) > 1e-30,
                        source_amplitude,
                        0.0,
                    )
                    * phase
                    * weight[None]
                )
        amplitude = following
    intensity = np.abs(amplitude) ** 2
    totals = intensity.sum(axis=(1, 2))
    if np.any(totals <= 0.0):
        raise AssertionError("independent route reached zero detector intensity")
    return (intensity * z[detector_layer]).sum(axis=(1, 2)) / totals


def independent_evidence(context=None, expected=None, *, verbose=True):
    import numpy as np

    del context
    y, z = independent_carrier()
    solve_poisson = independent_poisson_solver()
    rows = []
    for duration in INDEPENDENT_DURATIONS:
        position = lambda layer, d=duration: independent_position(
            layer, CARRIER.onset, CARRIER.start_cell, CARRIER.end_cell, d
        )
        endpoint = CARRIER.onset + duration
        layer = endpoint + CARRIER.fixed_buffer
        if any(position(t) != CARRIER.end_cell for t in range(endpoint, CARRIER.n_layers)):
            raise AssertionError("independent route failed its endpoint clamp")
        moving_field = independent_wave_history(CARRIER.strength, position)
        instantaneous_field = independent_instantaneous_history(
            CARRIER.strength, position, solve_poisson
        )
        centroids = independent_centroids(
            (np.zeros_like(moving_field), moving_field, instantaneous_field),
            y,
            z,
            layer,
        )
        value = measure(
            float(centroids[1] - centroids[0]),
            float(centroids[2] - centroids[0]),
        )
        row = {
            "duration": duration,
            "speed": abs(CARRIER.end_cell - CARRIER.start_cell) / duration,
            "endpoint_layer": endpoint,
            "measurement_layer": layer,
            "buffer": CARRIER.fixed_buffer,
            "start_cell": CARRIER.start_cell,
            "end_cell": CARRIER.end_cell,
            "d_moving": value.d_moving,
            "d_instantaneous": value.d_instantaneous,
            "difference": value.difference,
            "relative_gap": value.relative_gap,
            "sign_relation": value.sign_relation,
        }
        rows.append(row)

    if expected is not None:
        expected_by_duration = {row["duration"]: row for row in expected["fixed_buffer"]}
        for row in rows:
            target = expected_by_duration[row["duration"]]
            for key in ("d_moving", "d_instantaneous"):
                if not math.isclose(row[key], target[key], rel_tol=0.0, abs_tol=3e-8):
                    raise AssertionError(
                        f"independent {key} mismatch at duration {row['duration']}"
                    )
    if verbose:
        print_rows(
            "INDEPENDENT ROUTE: ARRAY CARRIER/BEAM/READOUT + SPARSE-DIRECT POISSON",
            rows,
        )
        print("independent evidence objects: 3")
    return rows


def expect_failure(label, action):
    try:
        action()
    except AssertionError as exc:
        return f"{label}: caught {exc}"
    raise AssertionError(f"hostile mutation escaped: {label}")


def note_path():
    return Path(__file__).resolve().parents[1] / "docs" / "WAVE_RETARDATION_LAB_PREDICTION_NOTE.md"


def cache_path():
    return (
        Path(__file__).resolve().parents[1]
        / "logs"
        / "runner-cache"
        / "wave_retardation_velocity_sweep.txt"
    )


def verify_cache_or_active_refresh(fingerprint):
    runner = Path(__file__).resolve()
    current_sha = hashlib.sha256(runner.read_bytes()).hexdigest()
    cache = cache_path()
    if cache.exists():
        text = cache.read_text(encoding="utf-8")
        required = (
            f"runner_sha256: {current_sha}",
            "exit_code: 0",
            "status: ok",
            f"helper_sha256={sha256_file(HELPER_PATH)}",
            f"controlled-result fingerprint: {fingerprint}",
        )
        if all(fragment in text for fragment in required):
            return "exact-SHA cache/status/stdout matched"

    in_progress = cache.parent / ".in-progress" / f"{runner.stem}.txt"
    if in_progress.exists():
        live = in_progress.read_text(encoding="utf-8", errors="replace")
        expected_header = f"# in-progress live log for scripts/{runner.name}"
        if expected_header in live:
            return "cache refresh in progress; post-refresh hostile replay required"
    raise AssertionError("runner cache is absent, stale, nonzero, or missing live fingerprint")


def expected_note_table_fragments(normal):
    fragments = []
    for schedule in normal["schedules"]:
        runs = []
        for position in schedule["sampled_positions"]:
            if runs and runs[-1][0] == position:
                runs[-1][1] += 1
            else:
                runs.append([position, 1])
        encoded = ",".join(f"{position}×{count}" for position, count in runs)
        fixed_buffer_detector = (
            schedule["endpoint_layer"] + CARRIER.fixed_buffer
        )
        fragments.append(
            f"| {schedule['motion_intervals']} | {schedule['speed']:.3f} | "
            f"{schedule['endpoint_layer']} | `{encoded}` | "
            f"{schedule['post_active_buffer']} | {fixed_buffer_detector} |"
        )
    for row in normal["fixed_final"]:
        fragments.append(
            f"| {row['duration']} | {row['speed']:.3f} | {row['endpoint_layer']} | "
            f"{row['buffer']} | {row['d_moving']:+.6f} | "
            f"{row['d_instantaneous']:+.6f} | {row['difference']:+.6f} | "
            f"{format_gap(row['relative_gap'])} |"
        )
    for row in normal["fixed_buffer"]:
        fragments.append(
            f"| {row['duration']} | {row['speed']:.3f} | {row['endpoint_layer']} | "
            f"{row['measurement_layer']} | {row['d_moving']:+.6f} | "
            f"{row['d_instantaneous']:+.6f} | {row['difference']:+.6f} | "
            f"{format_gap(row['relative_gap'])} |"
        )
    for row in normal["buffer_scan"]:
        fragments.append(
            f"| {row['buffer']} | {row['measurement_layer']} | "
            f"{row['d_moving']:+.6f} | {row['d_instantaneous']:+.6f} | "
            f"{row['difference']:+.6f} | {format_gap(row['relative_gap'])} |"
        )
    for row in normal["geometry_pair"]:
        fragments.append(
            f"| cell {row['start_cell']} to cell {row['end_cell']} | "
            f"{row['d_moving']:+.6f} | {row['d_instantaneous']:+.6f} | "
            f"{row['difference']:+.6f} | {format_gap(row['relative_gap'])} |"
        )
    fixed_final = normal["fixed_final"]
    fixed_buffer = normal["fixed_buffer"]
    fragments.extend(
        (
            f"slopes are respectively `{diagnostic_slope([row['speed'] for row in fixed_final], [abs(row['difference']) for row in fixed_final]):.3f}` "
            f"and `{diagnostic_slope([row['speed'] for row in fixed_final], [row['relative_gap'] for row in fixed_final]):.3f}`.",
            f"slopes are `{diagnostic_slope([row['speed'] for row in fixed_buffer], [abs(row['difference']) for row in fixed_buffer]):.3f}` "
            f"and `{diagnostic_slope([row['speed'] for row in fixed_buffer], [row['relative_gap'] for row in fixed_buffer]):.3f}`.",
        )
    )
    return fragments


def hostile_evidence(normal=None, context=None, *, verbose=True):
    if normal is None:
        normal, context = normal_evidence(verbose=False)
    checks = []
    base = make_trajectory(20)
    detector = base.endpoint_layer + CARRIER.fixed_buffer

    class Unclamped:
        onset = base.onset
        start_cell = base.start_cell
        end_cell = base.end_cell
        motion_intervals = base.motion_intervals
        endpoint_layer = base.endpoint_layer

        @staticmethod
        def position(layer):
            return base.start_cell + int(
                round(
                    (base.end_cell - base.start_cell)
                    * (layer - base.onset)
                    / base.motion_intervals
                )
            )

    checks.append(
        expect_failure(
            "unclamped buffer motion",
            lambda: validate_trajectory(Unclamped(), detector),
        )
    )
    checks.append(
        expect_failure(
            "moving onset",
            lambda: assert_same_fixed_controls(CARRIER, replace(CARRIER, onset=11)),
        )
    )
    checks.append(
        expect_failure(
            "changing lattice size",
            lambda: assert_same_fixed_controls(CARRIER, replace(CARRIER, n_layers=79)),
        )
    )
    checks.append(
        expect_failure(
            "changing fixed measurement layer",
            lambda: assert_same_fixed_controls(CARRIER, replace(CARRIER, final_layer=76)),
        )
    )

    note = note_path().read_text(encoding="utf-8")
    marker = "**Controlled-result fingerprint:** `"
    if marker not in note:
        raise AssertionError("note has no controlled-result fingerprint")
    recorded = note.split(marker, 1)[1].split("`", 1)[0]
    if recorded != normal["fingerprint"]:
        raise AssertionError("note tables are stale relative to live controlled results")
    missing_rows = [
        fragment for fragment in expected_note_table_fragments(normal) if fragment not in note
    ]
    if missing_rows:
        raise AssertionError(
            f"note is missing {len(missing_rows)} live formatted table row(s)"
        )
    stale_fragments = (
        "50." + "11%",
        "7." + "10%",
        "-3." + "101",
        "-2." + "791",
        "151." + "45%",
    )
    if any(fragment in note for fragment in stale_fragments):
        raise AssertionError("a superseded stdout value remains in the repaired note")
    cache_evidence = verify_cache_or_active_refresh(normal["fingerprint"])
    checks.append(
        "live note rows/fingerprint and cache guard: matched; " + cache_evidence
    )

    if robust_gap(0.0, 0.0) is not None:
        raise AssertionError("zero/zero denominator was assigned a finite relative gap")
    if sign_relation(1.0, -1.0) != "opposite":
        raise AssertionError("opposite-sign diagnostic failed")
    if not math.isclose(robust_gap(1.0, -1.0), 2.0):
        raise AssertionError("opposite-sign robust denominator diagnostic failed")
    checks.append("denominator/sign pathology guard: undefined zero and 200% opposite-sign gap")

    forbidden = (
        "PURE" + " velocity scaling",
        "v" + "/c",
        "LAB" + " EXTRAPOLATION",
        "inferred scaling" + " exponent",
        "translates to a measurable" + " phase shift",
    )
    source = Path(__file__).read_text(encoding="utf-8")
    surfaces = note + "\n" + source
    if any(phrase in surfaces for phrase in forbidden):
        raise AssertionError("false power-law or lab-observable rhetoric reappeared")
    checks.append("power-law/lab-rhetoric guard: clear")

    base_row, shifted_row = normal["geometry_pair"]
    geometry_change = abs(shifted_row["difference"] - base_row["difference"])
    if geometry_change <= 5e-4:
        raise AssertionError("load-bearing equal-rate geometry countercheck was neutralized")
    checks.append(
        "equal-rate geometry mutation remains load-bearing: "
        f"delta(M-I)={geometry_change:.6f}"
    )

    if len(checks) != 8:
        raise AssertionError("hostile evidence count changed")
    if verbose:
        print("\nHOSTILE MUTATION/GUARD EVIDENCE")
        for index, check in enumerate(checks, 1):
            print(f"  H{index}: {check}")
        print("hostile evidence objects: 8")
    return checks


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "all"),
        default="all",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    normal = None
    context = None
    if args.mode in ("normal", "all"):
        normal, context = normal_evidence()
    if args.mode == "independent":
        independent_evidence()
    elif args.mode == "hostile":
        hostile_evidence()
    elif args.mode == "all":
        independent_evidence(context, normal)
        hostile_evidence(normal, context)
        print("\nbounded conclusion: these named finite controls do not identify a schedule-rate-only")
        print("monotone power law or laboratory card; no continuum/universal claim is made.")


if __name__ == "__main__":
    main()
