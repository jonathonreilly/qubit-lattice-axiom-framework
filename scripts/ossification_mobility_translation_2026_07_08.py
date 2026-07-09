#!/usr/bin/env python3
"""Block02 deposition-constant ossification/mobility translation comparator.

Purpose
-------
Block02 of the deposition-constant campaign: translate kappa into the two
phenomenological handles -- the moving-body trail (wake transient) and the
collapsed-body ossification (black-hole mobility) -- in one comparator, and
print the joint sparse window.  This is a declared comparator: it supplies no
derivation and sets no audit status.

Companion note:
OSSIFICATION_MOBILITY_TRANSLATION_BOUNDED_NOTE_2026-07-08.md.

The dynamics are imported from
``scripts/collapse_merger_toy_engine_2026_07_08.py``.  The meaning of kappa as
a deposition-per-activity comparator coupling is cited from
``scripts/deposition_per_activity_kappa_2026_07_08.py``; that runner's measured
values and implementation are not imported.

Declared measurement conventions
--------------------------------
The initial parcel counts are a seeded, rounded sample from a sigma-6 Gaussian
profile; Leg A repeats the measurement over five spawned seeds and gates on
seed means.  Leg A adds ``+0.15`` to every parcel's engine ``p_R`` and sets
``p_L = 1 - p_R``; out-of-range probabilities fail rather than being clipped.
The nominal wind speed is therefore 0.30 site/step and the 200-site comparison
horizon is 667 integer steps.  Trail density is the record fill on the integer
corridor the centroid has actually swept forward, capped at 200 sites (a
zero-length sweep retains its initial lattice site).  Mobility is capped
maximum forward centroid progress, ``min(200, max_t(x_t - x_0)) / 200``.

Deposition uses the engine's Poisson rate-to-probability conversion
``1 - exp(-kappa * n * (A/A0) * dt)``, so offers are valid at any occupancy;
nothing is clipped or substepped here.

Two transport modes exist in this d = 1 comparator and are declared as such.
A single record is a total barrier on a line, so coherent transport survives
only while the body's own core has deposited nothing (the mobile-sparse
mode).  At large kappa apparent centroid motion continues as a
deposit-displace ratchet (formation relocates parcels to the nearest open
site), which paints trail fill near one and is not coherent mobility; it is
flagged, and the joint-window statement is made on the coherent mode only.
The d = 1 wall is the dimensional extreme: in d >= 2 open-site bypass would
widen the mobile window.

The density centroid is the continuously unwrapped circular first moment on
the engine ring.  In Leg B, a candidate step is anchored exactly when each of
the 500 centroids beginning at that step lies within +/-2 sites of the
candidate step's centroid.  The reported anchoring time is the first such
candidate, or ``inf``.  These wind and anchoring choices are supplied
phenomenological devices, not consequences of the engine.
"""

from __future__ import annotations

import math
import sys
import time
from dataclasses import dataclass

import numpy as np

import collapse_merger_toy_engine_2026_07_08 as engine


SEED = 20260708
L = 400
BETA = 0.6
KAPPAS = (1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2)
N_PARCELS = 120
BLOB_SIGMA = 6.0
BLOB_CENTER = L // 4
DRIFT_BIAS = 0.15
TRAVERSE_DISTANCE = 200
NOMINAL_DRIFT = 2.0 * DRIFT_BIAS
MOVING_STEPS = int(round(TRAVERSE_DISTANCE / NOMINAL_DRIFT))
N_MOVING_SEEDS = 5
STATIONARY_STEPS = 4000
ANCHOR_RADIUS = 2.0
ANCHOR_STEPS = 500
ORDER_GATE = 4
TRAIL_GATE = 0.3
MOBILITY_GATE = 0.8
EXTREME_KAPPA = 1.0e-3
EXTREME_MOBILITY_GATE = 0.5
OSSIFICATION_GATE = 0.5
RATCHET_HUSK = 300
NUMERIC_TOL = 1.0e-12


@dataclass(frozen=True)
class MovingResult:
    kappa: float
    trail_density: float
    mobility: float
    directed_distance: float
    swept_sites: int
    husk_sites: int


@dataclass(frozen=True)
class MovingAggregate:
    kappa: float
    trail_density: float
    mobility: float
    directed_distance: float
    max_husk: int
    ratchet: bool


@dataclass(frozen=True)
class StationaryResult:
    kappa: float
    ossification: float
    anchor_time: int | None
    husk_sites: int


class CentroidTracker:
    """Continuously unwrap the circular density centroid of one state."""

    def __init__(self, parcels: np.ndarray):
        self._phases = np.exp(2.0j * np.pi * np.arange(L, dtype=np.float64) / L)
        self.wrapped = self._wrapped_centroid(parcels)
        self.unwrapped = self.wrapped

    def _wrapped_centroid(self, parcels: np.ndarray) -> float:
        count = int(parcels.sum())
        if count <= 0:
            raise RuntimeError("density centroid requires at least one parcel")
        moment = complex(np.dot(parcels, self._phases)) / count
        if abs(moment) <= NUMERIC_TOL:
            raise RuntimeError("circular density centroid is undefined")
        angle = math.atan2(moment.imag, moment.real) % (2.0 * math.pi)
        return angle * L / (2.0 * math.pi)

    def update(self, parcels: np.ndarray) -> float:
        wrapped = self._wrapped_centroid(parcels)
        delta = (wrapped - self.wrapped + 0.5 * L) % L - 0.5 * L
        self.unwrapped += delta
        self.wrapped = wrapped
        return self.unwrapped


def validate_engine_contract() -> None:
    required = (
        "EngineState",
        "engine_step",
        "hop_probabilities",
        "validate_state",
    )
    missing = [name for name in required if not hasattr(engine, name)]
    if missing:
        raise RuntimeError("missing engine API: " + ",".join(missing))
    if engine.L != L or engine.BETA != BETA:
        raise RuntimeError(
            f"engine constants disagree: L={engine.L},beta={engine.BETA}"
        )
    if MOVING_STEPS != 667:
        raise AssertionError("the declared integer moving horizon changed")


def moving_seeds() -> tuple[int, ...]:
    children = np.random.SeedSequence(SEED).spawn(N_MOVING_SEEDS)
    return tuple(
        int(child.generate_state(1, dtype=np.uint64)[0]) for child in children
    )


def initialized_blob(seed: int) -> tuple[engine.EngineState, np.random.Generator]:
    """Return a seeded Gaussian blob and the post-initialization RNG state."""

    rng = np.random.default_rng(seed)
    draws = np.rint(rng.normal(BLOB_CENTER, BLOB_SIGMA, N_PARCELS)).astype(
        np.int64
    )
    parcels = np.zeros(L, dtype=np.int64)
    np.add.at(parcels, draws % L, 1)
    state = engine.EngineState(
        records=np.zeros(L, dtype=np.bool_),
        parcels=parcels,
    )
    engine.validate_state(state, N_PARCELS)
    return state, rng


def driven_hop(state: engine.EngineState, rng: np.random.Generator) -> None:
    """Apply the engine's blocked simultaneous hop with the declared wind."""

    _, engine_p_right = engine.hop_probabilities(state.records, beta=BETA)
    p_right = engine_p_right + DRIFT_BIAS
    if np.any((p_right < 0.0) | (p_right > 1.0)):
        raise RuntimeError("declared drift produces an out-of-range p_R")

    right = rng.binomial(state.parcels, p_right).astype(np.int64, copy=False)
    left = state.parcels - right
    right_blocked = np.roll(state.records, -1)
    left_blocked = np.roll(state.records, 1)
    stay = np.where(right_blocked, right, 0) + np.where(left_blocked, left, 0)
    accepted_right = np.where(right_blocked, 0, right)
    accepted_left = np.where(left_blocked, 0, left)
    state.parcels = (
        stay + np.roll(accepted_right, 1) + np.roll(accepted_left, -1)
    ).astype(np.int64, copy=False)


def driven_step(
    state: engine.EngineState,
    rng: np.random.Generator,
    kappa: float,
) -> None:
    """Wind hop followed by the imported engine deposition/displacement step."""

    driven_hop(state, rng)
    engine.engine_step(
        state,
        rng,
        kappa=kappa,
        beta=BETA,
        hops_enabled=False,
        expected_parcels=N_PARCELS,
    )


def swept_corridor(initial_centroid: float, maximum_centroid: float) -> np.ndarray:
    swept_distance = min(
        float(TRAVERSE_DISTANCE), max(0.0, maximum_centroid - initial_centroid)
    )
    swept_sites = max(1, int(math.floor(swept_distance + NUMERIC_TOL)))
    first_site = int(math.floor(initial_centroid)) % L
    return (first_site + np.arange(swept_sites, dtype=np.int64)) % L


def run_moving(kappa: float, seed: int) -> MovingResult:
    state, rng = initialized_blob(seed)
    tracker = CentroidTracker(state.parcels)
    initial_centroid = tracker.unwrapped
    maximum_centroid = initial_centroid

    for _ in range(MOVING_STEPS):
        driven_step(state, rng, kappa)
        maximum_centroid = max(maximum_centroid, tracker.update(state.parcels))

    corridor = swept_corridor(initial_centroid, maximum_centroid)
    forward = max(0.0, maximum_centroid - initial_centroid)
    return MovingResult(
        kappa=kappa,
        trail_density=float(state.records[corridor].mean()),
        mobility=min(float(TRAVERSE_DISTANCE), forward) / TRAVERSE_DISTANCE,
        directed_distance=tracker.unwrapped - initial_centroid,
        swept_sites=int(corridor.size),
        husk_sites=int(state.records.sum()),
    )


def aggregate_moving(kappa: float) -> MovingAggregate:
    results = [run_moving(kappa, seed) for seed in moving_seeds()]
    return MovingAggregate(
        kappa=kappa,
        trail_density=float(np.mean([r.trail_density for r in results])),
        mobility=float(np.mean([r.mobility for r in results])),
        directed_distance=float(np.mean([r.directed_distance for r in results])),
        max_husk=max(r.husk_sites for r in results),
        ratchet=any(r.husk_sites > RATCHET_HUSK for r in results),
    )


def first_anchor_time(centroids: np.ndarray) -> int | None:
    """First post-initial step starting a 500-step +/-2 confinement run."""

    last_start = centroids.size - ANCHOR_STEPS
    for step in range(1, last_start + 1):
        window = centroids[step : step + ANCHOR_STEPS]
        if np.all(np.abs(window - window[0]) <= ANCHOR_RADIUS + NUMERIC_TOL):
            return step
    return None


def run_stationary(kappa: float) -> StationaryResult:
    state, rng = initialized_blob(SEED)
    tracker = CentroidTracker(state.parcels)
    centroids = np.empty(STATIONARY_STEPS + 1, dtype=np.float64)
    centroids[0] = tracker.unwrapped

    for step in range(1, STATIONARY_STEPS + 1):
        engine.engine_step(
            state,
            rng,
            kappa=kappa,
            beta=BETA,
            expected_parcels=N_PARCELS,
        )
        centroids[step] = tracker.update(state.parcels)

    husk_sites = int(state.records.sum())
    return StationaryResult(
        kappa=kappa,
        ossification=husk_sites / (husk_sites + N_PARCELS),
        anchor_time=first_anchor_time(centroids),
        husk_sites=husk_sites,
    )


def monotone_subsequence_length(values: np.ndarray, increasing: bool) -> int:
    """Longest ordered subsequence, allowing ties, in the kappa sweep order."""

    lengths = np.ones(values.size, dtype=np.int64)
    for right in range(values.size):
        for left in range(right):
            ordered = (
                values[left] <= values[right] + NUMERIC_TOL
                if increasing
                else values[left] + NUMERIC_TOL >= values[right]
            )
            if ordered:
                lengths[right] = max(lengths[right], lengths[left] + 1)
    return int(lengths.max(initial=0))


def fmt_kappa(value: float) -> str:
    return f"{value:g}"


def fmt_anchor(value: int | None) -> str:
    return "inf" if value is None else str(value)


def fmt_window(kappas: list[float]) -> str:
    if not kappas:
        return "none"
    return "{" + ",".join(fmt_kappa(value) for value in kappas) + "}"


def fmt_moving(result: MovingAggregate) -> str:
    ratchet = ",RATCHET" if result.ratchet else ""
    return (
        f"k={fmt_kappa(result.kappa)} d_trail={result.trail_density:.4f} "
        f"m={result.mobility:.4f} dx={result.directed_distance:.1f} "
        f"husk<={result.max_husk}{ratchet}"
    )


def fmt_stationary(result: StationaryResult) -> str:
    return (
        f"k={fmt_kappa(result.kappa)} o={result.ossification:.4f} "
        f"husk={result.husk_sites} t_anchor={fmt_anchor(result.anchor_time)}"
    )


def run() -> tuple[tuple[str, ...], str]:
    started = time.monotonic()
    validate_engine_contract()
    moving = [aggregate_moving(kappa) for kappa in KAPPAS]
    stationary = [run_stationary(kappa) for kappa in KAPPAS]

    trail = np.asarray([result.trail_density for result in moving])
    mobility = np.asarray([result.mobility for result in moving])
    ossification = np.asarray([result.ossification for result in stationary])

    trail_order = monotone_subsequence_length(trail, increasing=True)
    ossification_order = monotone_subsequence_length(ossification, increasing=True)
    monotonic_ok = bool(
        trail_order >= ORDER_GATE and ossification_order >= ORDER_GATE
    )

    window = [
        result.kappa
        for result in moving
        if result.trail_density <= TRAIL_GATE + NUMERIC_TOL
        and result.mobility + NUMERIC_TOL >= MOBILITY_GATE
    ]
    window_ok = bool(window)

    extreme_index = KAPPAS.index(EXTREME_KAPPA)
    extreme_mobility = float(mobility[extreme_index])
    extreme_ok = bool(extreme_mobility <= EXTREME_MOBILITY_GATE + NUMERIC_TOL)

    mobile_kappas = [
        result.kappa
        for result in moving
        if result.mobility + NUMERIC_TOL >= MOBILITY_GATE
    ]
    ossified_kappas = [
        result.kappa
        for result in stationary
        if result.ossification + NUMERIC_TOL >= OSSIFICATION_GATE
    ]
    kappa_mobile = max(mobile_kappas) if mobile_kappas else None
    kappa_ossified = min(ossified_kappas) if ossified_kappas else None
    separation_ok = bool(
        kappa_mobile is not None
        and kappa_ossified is not None
        and kappa_mobile < kappa_ossified
    )

    finite_ok = bool(
        np.all(np.isfinite(trail))
        and np.all(np.isfinite(mobility))
        and np.all(np.isfinite(ossification))
        and np.all((trail >= 0.0) & (trail <= 1.0))
        and np.all((mobility >= 0.0) & (mobility <= 1.0))
        and np.all((ossification >= 0.0) & (ossification <= 1.0))
    )
    elapsed = time.monotonic() - started
    runtime_ok = elapsed < 900.0

    machinery_ok = finite_ok and runtime_ok
    gates_ok = monotonic_ok and window_ok and extreme_ok and separation_ok
    if not machinery_ok:
        verdict = "MACHINERY-FAIL"
    elif gates_ok:
        verdict = "WINDOW-MAPPED"
    else:
        verdict = "WINDOW-NOT-EXHIBITED"

    setup_line = (
        "SETUP seed=20260708 L=400 beta=0.6 Np=120 sigma=6 "
        "kappa=[1e-6,1e-5,1e-4,1e-3,1e-2] wind=+0.15pR "
        f"legA=200sites/{MOVING_STEPS}steps x{N_MOVING_SEEDS}seeds legB_T=4000 "
        "dt=1 poisson-offers"
    )
    leg_a_line = "LEG-A(seed-means) " + "; ".join(map(fmt_moving, moving))
    leg_b_line = "LEG-B " + "; ".join(map(fmt_stationary, stationary))
    joint_line = "JOINT " + "; ".join(
        f"k={fmt_kappa(a.kappa)}(d_trail={a.trail_density:.4f},"
        f"m={a.mobility:.4f},o={b.ossification:.4f})"
        for a, b in zip(moving, stationary)
    )
    gates_line = (
        f"GATES monotonic(d,o)={monotonic_ok} order=({trail_order}/5,"
        f"{ossification_order}/5) window_nonempty={window_ok} "
        f"extreme_m@{fmt_kappa(EXTREME_KAPPA)}={extreme_mobility:.4f}"
        f"<=0.5:{extreme_ok} separation kappa_mob="
        f"{fmt_kappa(kappa_mobile) if kappa_mobile is not None else 'none'}<"
        f"kappa_oss="
        f"{fmt_kappa(kappa_ossified) if kappa_ossified is not None else 'none'}"
        f":{separation_ok} finite={finite_ok} elapsed={elapsed:.3f}s"
    )
    total_line = (
        f"TOTAL: {verdict} flags(kappa_window={fmt_window(window)},"
        f"monotonic={monotonic_ok},extreme_contrast={extreme_ok},"
        f"mobility_forces_sparsity={separation_ok},runtime_lt_900={runtime_ok}); "
        "SPEC-NOTE: drift-wind is supplied pR+=0.15,pL=1-pR; deposition offers "
        "are the engine's Poisson conversion, no clipping or substepping; a "
        "single record is a total d=1 barrier, so the pinning scale is the "
        "dimensional extreme and high-kappa centroid motion is a "
        "deposit-displace ratchet (flagged), not coherent mobility; anchoring "
        "means the first 500-step run within +/-2 of its first centroid; "
        "declared comparator, no derivation, no audit status."
    )
    lines = (setup_line, leg_a_line, leg_b_line, joint_line, gates_line, total_line)
    if len(lines) > 6:
        raise AssertionError("stdout contract exceeded six lines")
    return lines, verdict


def main() -> int:
    try:
        lines, verdict = run()
        for line in lines:
            print(line)
        if verdict == "WINDOW-MAPPED":
            return 0
        return 2 if verdict == "MACHINERY-FAIL" else 1
    except Exception as exc:  # noqa: BLE001 - fail closed within stdout budget.
        message = " ".join(str(exc).split())[:220]
        print(
            f"TOTAL: MACHINERY-FAIL {type(exc).__name__}:{message}; "
            "SPEC-NOTE: drift-wind=pR+0.15,pL=1-pR; poisson-offers, no clipping, "
            "no substepping; anchoring=first-500-step-run-within-"
            "+/-2-of-first-centroid; declared "
            "comparator, no derivation, no audit status."
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())
