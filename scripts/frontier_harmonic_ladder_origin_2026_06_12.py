#!/usr/bin/env python3
"""Class-A finite-dimensional check for the harmonic origin of capture deficit.

Source note:
    docs/HARMONIC_LADDER_ORIGIN_OF_CAPTURE_DEFICIT_BOUNDED_THEOREM_NOTE_2026-06-12.md

Scope: exact L=3 realized-state data.  The audit lane grades.

Run:
    python3 scripts/frontier_harmonic_ladder_origin_2026_06_12.py
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


@dataclass(frozen=True)
class StateSpec:
    label: str
    k_occ: int
    seed: int


@dataclass(frozen=True)
class CoupledTone:
    gap: float
    weight: float


@dataclass(frozen=True)
class RawToneAnalysis:
    landed_active_count: int
    activity_active_count: int
    on_ladder_count: int
    off_ladder_count: int
    off_ladder_weight_fraction: float
    nearest_ladder_tail_fraction: float
    nearest_ladder_k2_weight: float
    reconstruction_error: float


@dataclass(frozen=True)
class HarmonicAnalysis:
    active_count: int
    max_abs_k: int
    w_by_abs_k: dict[int, float]
    tail_beyond_fundamental: float
    w1: float
    w2: float
    w2_over_w1: float
    max_gap_residual: float


@dataclass(frozen=True)
class StateAnalysis:
    spec: StateSpec
    capture4: float
    hankel_tail_fraction: float
    no_floor_gaps: tuple[float, ...]
    raw: RawToneAnalysis
    harmonic: HarmonicAnalysis


L = 3
NC = 3
DIM = L * NC
TAU = 0.35
T_STEPS = 256
CAPTURE_WINDOW = 64
BASE_GAP = 3.0
BASE_ANGLE_STEP = BASE_GAP * TAU
SAMPLED_GAP_RESOLUTION = 2.0 * math.pi / (T_STEPS * TAU)
RAW_ACTIVITY_FLOOR_REL = 1.0e-10
HARMONIC_SAMPLES = 4096
HARMONIC_ACTIVITY_FLOOR_REL = 1.0e-10
FULL_TONE_ZERO_TOL = 1.0e-13

CAPTURE_TOL = 1.0e-10
TAIL_TOL = 1.0e-12
RECONSTRUCTION_TOL = 1.0e-12
WEIGHT_TOL = 1.0e-10
RATIO_TOL = 1.0e-10
EXACT_GAP_TOL = 1.0e-9
FUNDAMENTAL_OFFGRID_MIN = 0.15
K2_NONZERO_FLOOR = 1.0e-12

STATES = (
    StateSpec("K=3", 3, 391),
    StateSpec("K=4", 4, 99),
    StateSpec("K=5(seed=99)", 5, 99),
    StateSpec("K=6", 6, 466),
)

FROZEN_NO_FLOOR_GAP_SETS = (
    (3, (-3.0, 0.0, 3.0)),
    (4, (-3.0, 0.0, 3.0)),
    (5, (-3.0, 0.0, 3.0)),
    (6, (-3.0, 0.0, 3.0)),
)
FROZEN_CAPTURE4_W64 = (
    (3, 0.8981300885645052),
    (4, 0.7776195573427411),
    (5, 0.8991555454934871),
    (6, 0.9949365168913127),
)
FROZEN_HANKEL_TAIL_FRACTION_W64 = (
    (3, 0.10186991143549493),
    (4, 0.2223804426572589),
    (5, 0.10084445450651301),
    (6, 0.005063483108687255),
)
FROZEN_FULL_ACTIVE_TONE_COUNTS = (
    (3, 255),
    (4, 255),
    (5, 255),
    (6, 255),
)
FROZEN_RAW_ACTIVITY_ACTIVE_COUNTS = (
    (3, 255),
    (4, 255),
    (5, 255),
    (6, 255),
)
FROZEN_RAW_ON_LADDER_COUNTS = (
    (3, 5),
    (4, 5),
    (5, 5),
    (6, 5),
)
FROZEN_RAW_OFF_LADDER_COUNTS = (
    (3, 250),
    (4, 250),
    (5, 250),
    (6, 250),
)
FROZEN_RAW_OFF_LADDER_WEIGHT_FRACTION = (
    (3, 0.49179434937426936),
    (4, 0.5592211594624541),
    (5, 0.36239647634281924),
    (6, 0.1520278736829762),
)
FROZEN_RAW_NEAREST_LADDER_TAIL_FRACTION = (
    (3, 0.8968355316156804),
    (4, 0.44582105738955263),
    (5, 0.3806720017693567),
    (6, 0.03914301886190944),
)
FROZEN_RAW_K2_WEIGHT = (
    (3, 0.6937632309878934),
    (4, 0.1417959172103973),
    (5, 0.2803261279233252),
    (6, 0.034301272386951624),
)
FROZEN_HARMONIC_ACTIVE_COUNTS = (
    (3, 1034),
    (4, 4081),
    (5, 978),
    (6, 50),
)
FROZEN_HARMONIC_MAX_ABS_K = (
    (3, 589),
    (4, 2048),
    (5, 548),
    (6, 27),
)
FROZEN_HARMONIC_TAIL_BEYOND_FUNDAMENTAL = (
    (3, 0.9195170362374587),
    (4, 0.855947795669448),
    (5, 0.4613240821293625),
    (6, 0.041463947067063106),
)
FROZEN_HARMONIC_W1 = (
    (3, 0.08048295383438742),
    (4, 0.1440522037836752),
    (5, 0.5386759094844884),
    (6, 0.9585360527752671),
)
FROZEN_HARMONIC_W2 = (
    (3, 0.5530957186939333),
    (4, 0.039738951671227936),
    (5, 0.23590287142564084),
    (6, 0.031142737013937785),
)
FROZEN_HARMONIC_W2_OVER_W1 = (
    (3, 6.872209484657554),
    (4, 0.27586493387428046),
    (5, 0.43793098460890767),
    (6, 0.03248989636203004),
)
FROZEN_HARMONIC_MINUS_HANKEL_TAIL = (
    (3, 0.8176471248019638),
    (4, 0.6335673530121891),
    (5, 0.36047962762284946),
    (6, 0.03640046395837585),
)
FROZEN_LANDED_DEFICIT_ORDER_ASCENDING = (6, 5, 3, 4)
FROZEN_HARMONIC_COEFF_TAIL_ORDER_ASCENDING = (6, 5, 4, 3)


def lattice_hamiltonian(n_sites: int) -> np.ndarray:
    h = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    for x in range(n_sites):
        y = (x + 1) % n_sites
        for c in range(NC):
            h[NC * x + c, NC * y + c] = -1.0
            h[NC * y + c, NC * x + c] = -1.0
    return h


def polar_u(m: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(m.conj().T @ m)
    if float(np.min(w)) <= 1.0e-14:
        raise FloatingPointError(f"polar block singular: min eig={float(np.min(w)):.3e}")
    return m @ v @ np.diag(w**-0.5) @ v.conj().T


def state_modes(dim: int, k_occ: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(dim, k_occ)) + 1j * rng.normal(size=(dim, k_occ))
    q, r = np.linalg.qr(z)
    phases = np.exp(-1j * np.angle(np.diag(r)))
    q = q @ np.diag(phases)
    return q[:, :k_occ]


def det_polar_site01(
    theta: float,
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> complex:
    spectral_time = theta / BASE_GAP
    u = evecs @ np.diag(np.exp(-1j * spectral_time * evals)) @ evecs.conj().T
    rho_t = u @ rho0 @ u.conj().T
    block_01 = rho_t[0:NC, NC : 2 * NC]
    return complex(np.linalg.det(polar_u(block_01)))


def phase_increment_sequence(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    q = state_modes(DIM, spec.k_occ, spec.seed)
    rho0 = q @ q.conj().T
    phases = []
    for t in range(T_STEPS + 1):
        theta = BASE_ANGLE_STEP * t
        phases.append(float(np.angle(det_polar_site01(theta, rho0, evals, evecs))))
    raw = np.diff(np.unwrap(np.array(phases)))
    centered = raw - float(np.mean(raw))
    return rho0, centered


def trajectory_hankel(x: np.ndarray, window: int) -> np.ndarray:
    if len(x) < window:
        raise ValueError("sequence shorter than Hankel window")
    return np.column_stack([x[i : i + window] for i in range(len(x) - window + 1)])


def hankel_svals(x: np.ndarray, window: int) -> np.ndarray:
    return np.linalg.svd(trajectory_hankel(x, window), compute_uv=False)


def sv_capture(svals: np.ndarray, order: int) -> float:
    total = float(np.sum(svals * svals))
    kept = float(np.sum(svals[:order] * svals[:order]))
    return kept / total


def tail_fraction_from_svals(svals: np.ndarray, order: int) -> float:
    weights = svals * svals
    return float(np.sum(weights[order:]) / np.sum(weights))


def site01_projector(n_sites: int) -> np.ndarray:
    p = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    p[0:NC, 0:NC] = np.eye(NC)
    p[NC : 2 * NC, NC : 2 * NC] = np.eye(NC)
    return p


def coupled_tone_weights(
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
    floor: float,
) -> tuple[CoupledTone, ...]:
    occ = evecs.conj().T @ rho0 @ evecs
    p01 = evecs.conj().T @ site01_projector(L) @ evecs
    weights: dict[float, float] = {}
    for a in range(len(evals)):
        for b in range(len(evals)):
            weight = abs(occ[a, b]) * abs(p01[b, a])
            if weight > floor:
                gap = round(float(evals[a] - evals[b]), 12)
                weights[gap] = weights.get(gap, 0.0) + float(weight)
    return tuple(CoupledTone(gap=gap, weight=weights[gap]) for gap in sorted(weights))


def full_sampled_tone_spectrum(x: np.ndarray) -> np.ndarray:
    return np.fft.fft(x) / len(x)


def raw_tone_analysis(coeffs: np.ndarray, x: np.ndarray) -> RawToneAnalysis:
    weights = np.abs(coeffs) ** 2
    total = float(np.sum(weights))
    activity_floor = RAW_ACTIVITY_FLOOR_REL * total
    active = np.flatnonzero(weights > activity_floor)
    gaps = np.fft.fftfreq(len(coeffs), d=1.0) * (2.0 * math.pi / TAU)
    grouped: dict[int, float] = {}
    on_ladder_count = 0
    off_ladder_count = 0
    off_ladder_weight = 0.0
    for idx in active:
        gap = float(gaps[idx])
        nearest_k = int(round(gap / BASE_GAP))
        nearest_gap = BASE_GAP * nearest_k
        distance = abs(gap - nearest_gap)
        grouped[nearest_k] = grouped.get(nearest_k, 0.0) + float(weights[idx] / total)
        if distance <= 0.5 * SAMPLED_GAP_RESOLUTION + EXACT_GAP_TOL:
            on_ladder_count += 1
        else:
            off_ladder_count += 1
            off_ladder_weight += float(weights[idx] / total)

    reconstructed = np.fft.ifft(coeffs * len(coeffs)).real
    nearest_tail = sum(weight for k, weight in grouped.items() if abs(k) > 1)
    nearest_k2 = grouped.get(2, 0.0) + grouped.get(-2, 0.0)
    return RawToneAnalysis(
        landed_active_count=int(np.sum(np.abs(coeffs) > FULL_TONE_ZERO_TOL)),
        activity_active_count=int(len(active)),
        on_ladder_count=on_ladder_count,
        off_ladder_count=off_ladder_count,
        off_ladder_weight_fraction=off_ladder_weight,
        nearest_ladder_tail_fraction=float(nearest_tail),
        nearest_ladder_k2_weight=float(nearest_k2),
        reconstruction_error=float(np.max(np.abs(x - reconstructed))),
    )


def base_angle_increment_values(
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> np.ndarray:
    theta = 2.0 * math.pi * np.arange(HARMONIC_SAMPLES) / HARMONIC_SAMPLES
    values = np.empty(HARMONIC_SAMPLES, dtype=float)
    for i, theta_i in enumerate(theta):
        z0 = det_polar_site01(float(theta_i), rho0, evals, evecs)
        z1 = det_polar_site01(float(theta_i + BASE_ANGLE_STEP), rho0, evals, evecs)
        values[i] = float(np.angle(z1 / z0))
    return values - float(np.mean(values))


def harmonic_ladder_analysis(values: np.ndarray) -> HarmonicAnalysis:
    coeffs = np.fft.fft(values) / len(values)
    weights = np.abs(coeffs) ** 2
    total = float(np.sum(weights))
    activity_floor = HARMONIC_ACTIVITY_FLOOR_REL * total
    active = np.flatnonzero(weights > activity_floor)
    raw_k = np.fft.fftfreq(len(values)) * len(values)
    signed_k = np.rint(raw_k).astype(int)
    w_by_abs_k: dict[int, float] = {}
    max_gap_residual = 0.0
    for idx in active:
        k = int(signed_k[idx])
        gap = BASE_GAP * float(raw_k[idx])
        nearest_gap = BASE_GAP * int(round(gap / BASE_GAP))
        max_gap_residual = max(max_gap_residual, abs(gap - nearest_gap))
        abs_k = abs(k)
        w_by_abs_k[abs_k] = w_by_abs_k.get(abs_k, 0.0) + float(weights[idx] / total)
    w1 = w_by_abs_k.get(1, 0.0)
    w2 = w_by_abs_k.get(2, 0.0)
    tail = sum(weight for k, weight in w_by_abs_k.items() if k > 1)
    return HarmonicAnalysis(
        active_count=int(len(active)),
        max_abs_k=int(max(abs(int(signed_k[idx])) for idx in active)),
        w_by_abs_k=w_by_abs_k,
        tail_beyond_fundamental=float(tail),
        w1=float(w1),
        w2=float(w2),
        w2_over_w1=float(w2 / w1),
        max_gap_residual=max_gap_residual,
    )


def analyze_state(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> StateAnalysis:
    rho0, increments = phase_increment_sequence(spec, evals, evecs)
    svals = hankel_svals(increments, CAPTURE_WINDOW)
    coeffs = full_sampled_tone_spectrum(increments)
    no_floor_gaps = tuple(tone.gap for tone in coupled_tone_weights(rho0, evals, evecs, 0.0))
    harmonic_values = base_angle_increment_values(rho0, evals, evecs)
    return StateAnalysis(
        spec=spec,
        capture4=sv_capture(svals, 4),
        hankel_tail_fraction=tail_fraction_from_svals(svals, 4),
        no_floor_gaps=no_floor_gaps,
        raw=raw_tone_analysis(coeffs, increments),
        harmonic=harmonic_ladder_analysis(harmonic_values),
    )


def table_close(
    observed: tuple[tuple[int, float], ...],
    frozen: tuple[tuple[int, float], ...],
    tol: float,
) -> bool:
    if len(observed) != len(frozen):
        return False
    return all(
        observed_k == frozen_k and abs(observed_value - frozen_value) <= tol
        for (observed_k, observed_value), (frozen_k, frozen_value) in zip(observed, frozen)
    )


def value_table(records: tuple[StateAnalysis, ...], attr_path: tuple[str, ...]) -> tuple[tuple[int, float], ...]:
    rows: list[tuple[int, float]] = []
    for record in records:
        item = record
        for attr in attr_path:
            item = getattr(item, attr)
        rows.append((record.spec.k_occ, float(item)))
    return tuple(rows)


def count_table(records: tuple[StateAnalysis, ...], attr_path: tuple[str, ...]) -> tuple[tuple[int, int], ...]:
    rows: list[tuple[int, int]] = []
    for record in records:
        item = record
        for attr in attr_path:
            item = getattr(item, attr)
        rows.append((record.spec.k_occ, int(item)))
    return tuple(rows)


def table_detail(rows: tuple[tuple[int, float], ...]) -> str:
    return ", ".join(f"K{k}:{value:.12g}" for k, value in rows)


def count_detail(rows: tuple[tuple[int, int], ...]) -> str:
    return ", ".join(f"K{k}:{value:d}" for k, value in rows)


def order_by_float(rows: tuple[tuple[int, float], ...]) -> tuple[int, ...]:
    return tuple(k for k, _ in sorted(rows, key=lambda item: item[1]))


def gap_set_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, tuple[float, ...]], ...]:
    return tuple(
        (record.spec.k_occ, tuple(round(gap, 9) for gap in record.no_floor_gaps))
        for record in records
    )


def print_harmonic_weight_rows(records: tuple[StateAnalysis, ...]) -> None:
    print("  paired coefficient weights w_|k|; omitted mass is below activity floor")
    header = "state active max|k|      w1        w2        w3        w4        w5    tail|k|>1  HankelTail"
    print("  " + header)
    for record in records:
        w = record.harmonic.w_by_abs_k
        print(
            f"  K={record.spec.k_occ:<1d} {record.harmonic.active_count:6d}"
            f" {record.harmonic.max_abs_k:6d}"
            f" {w.get(1, 0.0):9.6f}"
            f" {w.get(2, 0.0):9.6f}"
            f" {w.get(3, 0.0):9.6f}"
            f" {w.get(4, 0.0):9.6f}"
            f" {w.get(5, 0.0):9.6f}"
            f" {record.harmonic.tail_beyond_fundamental:12.6f}"
            f" {record.hankel_tail_fraction:11.6f}"
        )


def main() -> int:
    print("=" * 78)
    print("Harmonic-ladder origin of the L=3 capture deficit")
    print("=" * 78)
    print(f"constants: L={L}, NC={NC}, tau={TAU}, T={T_STEPS}, window={CAPTURE_WINDOW}")
    print(
        f"raw FFT activity floor={RAW_ACTIVITY_FLOOR_REL:.1e} of coefficient energy; "
        f"sampled gap resolution={SAMPLED_GAP_RESOLUTION:.12g}"
    )
    print(
        f"base-angle harmonic samples={HARMONIC_SAMPLES}, "
        f"harmonic activity floor={HARMONIC_ACTIVITY_FLOOR_REL:.1e}"
    )
    print()

    h = lattice_hamiltonian(L)
    evals, evecs = np.linalg.eigh(h)
    records = tuple(analyze_state(spec, evals, evecs) for spec in STATES)

    print("H1 anchors from tracked capture-deficit note")
    print("-" * 78)
    observed_gap_sets = gap_set_table(records)
    check(
        "ANCHOR: no-floor coupled eigenpair gap set is frozen as (-3,0,+3) per state",
        observed_gap_sets == FROZEN_NO_FLOOR_GAP_SETS,
        ", ".join(f"K{k}:{gaps}" for k, gaps in observed_gap_sets),
    )

    observed_capture = value_table(records, ("capture4",))
    check(
        "ANCHOR: landed capture@order4/window64 table is reproduced",
        table_close(observed_capture, FROZEN_CAPTURE4_W64, CAPTURE_TOL),
        table_detail(observed_capture),
    )

    observed_tail = value_table(records, ("hankel_tail_fraction",))
    check(
        "ANCHOR: landed Hankel tail fractions are reproduced",
        table_close(observed_tail, FROZEN_HANKEL_TAIL_FRACTION_W64, TAIL_TOL),
        table_detail(observed_tail),
    )

    observed_full_active = count_table(records, ("raw", "landed_active_count"))
    check(
        "anti-fabrication: landed raw FFT active counts are the frozen 255-per-state table",
        observed_full_active == FROZEN_FULL_ACTIVE_TONE_COUNTS,
        count_detail(observed_full_active),
    )

    observed_recon = value_table(records, ("raw", "reconstruction_error"))
    check(
        "ANCHOR: full raw tone sum reconstructs the centered trajectory below 1e-12",
        max(value for _, value in observed_recon) <= RECONSTRUCTION_TOL,
        table_detail(observed_recon),
    )

    print()
    print("H2 sampled spectrum vs integer ladder")
    print("-" * 78)
    observed_raw_activity = count_table(records, ("raw", "activity_active_count"))
    observed_raw_on = count_table(records, ("raw", "on_ladder_count"))
    observed_raw_off = count_table(records, ("raw", "off_ladder_count"))
    observed_raw_off_mass = value_table(records, ("raw", "off_ladder_weight_fraction"))
    check(
        "H2 raw FFT: active counts above the fixed 1e-10 energy floor are frozen",
        observed_raw_activity == FROZEN_RAW_ACTIVITY_ACTIVE_COUNTS,
        count_detail(observed_raw_activity),
    )
    check(
        "H2 measured alternative: raw FFT has only the frozen near-ladder bin count",
        observed_raw_on == FROZEN_RAW_ON_LADDER_COUNTS,
        count_detail(observed_raw_on),
    )
    check(
        "H2 measured alternative: raw FFT has the frozen off-ladder leakage count",
        observed_raw_off == FROZEN_RAW_OFF_LADDER_COUNTS,
        count_detail(observed_raw_off),
    )
    check(
        "H2 measured alternative: raw FFT off-ladder leakage mass is frozen",
        table_close(observed_raw_off_mass, FROZEN_RAW_OFF_LADDER_WEIGHT_FRACTION, WEIGHT_TOL),
        table_detail(observed_raw_off_mass),
    )

    observed_harmonic_active = count_table(records, ("harmonic", "active_count"))
    observed_harmonic_max_k = count_table(records, ("harmonic", "max_abs_k"))
    observed_gap_residual = value_table(records, ("harmonic", "max_gap_residual"))
    check(
        "H2 base-angle construction consistency: the ladder-grid readout carries "
        "integer-k gaps to machine precision (a consistency check of the grid, not "
        "a physical finding)",
        max(value for _, value in observed_gap_residual) <= EXACT_GAP_TOL,
        table_detail(observed_gap_residual),
    )
    # The physical content the base-angle readout cannot show: in the RAW
    # time-sampled FFT the fundamental gap g=3 sits at FFT-bin index
    # g*TAU*T_STEPS/(2 pi), which is genuinely off-grid (non-integer) -> the
    # off-ladder leakage above is forced, not a measurement choice.
    fundamental_bin = BASE_GAP * TAU * T_STEPS / (2.0 * math.pi)
    fundamental_offgrid = abs(fundamental_bin - round(fundamental_bin))
    check(
        "H2 raw-FFT fundamental g=3 is off the FFT grid by the frozen margin "
        "(forces the leakage; not a tautology of the ladder construction)",
        fundamental_offgrid >= FUNDAMENTAL_OFFGRID_MIN,
        f"bin={fundamental_bin:.6f}, |offgrid|={fundamental_offgrid:.6f}, "
        f"min={FUNDAMENTAL_OFFGRID_MIN:.2f}",
    )
    check(
        "H2 physical base-angle active harmonic counts are frozen",
        observed_harmonic_active == FROZEN_HARMONIC_ACTIVE_COUNTS,
        count_detail(observed_harmonic_active),
    )
    check(
        "H2 physical base-angle maximum active ladder depth is frozen",
        observed_harmonic_max_k == FROZEN_HARMONIC_MAX_ABS_K,
        count_detail(observed_harmonic_max_k),
    )

    print()
    print("H3 ladder weights and depth")
    print("-" * 78)
    print_harmonic_weight_rows(records)
    observed_harmonic_tail = value_table(records, ("harmonic", "tail_beyond_fundamental"))
    observed_raw_nearest_tail = value_table(records, ("raw", "nearest_ladder_tail_fraction"))
    check(
        "H3 coefficient ladder tail beyond |k|=1 is the frozen measured table",
        table_close(observed_harmonic_tail, FROZEN_HARMONIC_TAIL_BEYOND_FUNDAMENTAL, WEIGHT_TOL),
        table_detail(observed_harmonic_tail),
    )
    check(
        "H3 raw nearest-ladder grouped tail beyond |k|=1 is the frozen measured table",
        table_close(observed_raw_nearest_tail, FROZEN_RAW_NEAREST_LADDER_TAIL_FRACTION, WEIGHT_TOL),
        table_detail(observed_raw_nearest_tail),
    )
    check(
        "H3 measured alternative: coefficient-tail order is frozen as K6,K5,K4,K3",
        order_by_float(observed_harmonic_tail) == FROZEN_HARMONIC_COEFF_TAIL_ORDER_ASCENDING,
        f"order={order_by_float(observed_harmonic_tail)}",
    )
    check(
        "H3 landed depth order remains the Hankel-tail order K6,K5,K3,K4",
        order_by_float(observed_tail) == FROZEN_LANDED_DEFICIT_ORDER_ASCENDING,
        f"order={order_by_float(observed_tail)}",
    )
    observed_tail_delta = tuple(
        (k, harmonic_tail - hankel_tail)
        for (k, harmonic_tail), (_, hankel_tail) in zip(observed_harmonic_tail, observed_tail)
    )
    check(
        "H3 measured alternative: coefficient ladder tail is not the landed Hankel tail",
        table_close(observed_tail_delta, FROZEN_HARMONIC_MINUS_HANKEL_TAIL, WEIGHT_TOL),
        table_detail(observed_tail_delta),
    )

    print()
    print("H4 nonlinearity tie: second harmonic")
    print("-" * 78)
    observed_w1 = value_table(records, ("harmonic", "w1"))
    observed_w2 = value_table(records, ("harmonic", "w2"))
    observed_ratio = value_table(records, ("harmonic", "w2_over_w1"))
    observed_raw_k2 = value_table(records, ("raw", "nearest_ladder_k2_weight"))
    for (k, w2), (_, ratio) in zip(observed_w2, observed_ratio):
        print(f"  K={k}: physical w2={w2:.12g}, w2/w1={ratio:.12g}")
    check(
        "H4 anti-fabrication: physical k=2 ladder weight is nonzero in every state",
        min(value for _, value in observed_w2) >= K2_NONZERO_FLOOR,
        table_detail(observed_w2),
    )
    check(
        "H4 physical fundamental weights w1 are frozen",
        table_close(observed_w1, FROZEN_HARMONIC_W1, WEIGHT_TOL),
        table_detail(observed_w1),
    )
    check(
        "H4 physical k=2 weights are frozen",
        table_close(observed_w2, FROZEN_HARMONIC_W2, WEIGHT_TOL),
        table_detail(observed_w2),
    )
    check(
        "H4 physical k=2/fundamental ratios are frozen",
        table_close(observed_ratio, FROZEN_HARMONIC_W2_OVER_W1, RATIO_TOL),
        table_detail(observed_ratio),
    )
    check(
        "H4 raw nearest-ladder k=2 grouped weights are frozen",
        table_close(observed_raw_k2, FROZEN_RAW_K2_WEIGHT, WEIGHT_TOL),
        table_detail(observed_raw_k2),
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: exact finite L=3 realized states only.")
    print("FINDING: the base-angle determinant-phase readout has an integer harmonic")
    print("  ladder and nonzero k=2 in every state.  The raw 256-step FFT used for the")
    print("  landed active-count anchor is not itself an exact ladder display; because")
    print("  3*tau is off the FFT grid, it shows frozen off-ladder leakage.  The landed")
    print("  capture depth is the Hankel-SVD tail order, not the simple coefficient")
    print("  tail beyond the fundamental.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
