#!/usr/bin/env python3
"""Bounded harmonic ladder weight-law check for the L=3 realized states.

Source draft:
    docs/HARMONIC_LADDER_WEIGHT_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md

Run:
    python3 scripts/frontier_harmonic_ladder_weight_law_2026_06_12.py
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
class HarmonicAnalysis:
    active_count: int
    max_abs_k: int
    w_by_abs_k: dict[int, float]
    tail_ge2: float
    tail_ge3: float
    max_gap_residual: float


@dataclass(frozen=True)
class LawAnalysis:
    harmonic: HarmonicAnalysis
    laurent_validation_error: float
    root_inside_count: int
    root_outside_count: int
    rho_star: float


@dataclass(frozen=True)
class StateAnalysis:
    spec: StateSpec
    capture4: float
    hankel_tail_fraction: float
    no_floor_gaps: tuple[float, ...]
    raw_reconstruction_error: float
    harmonic: HarmonicAnalysis
    law: LawAnalysis


L = 3
NC = 3
DIM = L * NC
TAU = 0.35
T_STEPS = 256
CAPTURE_WINDOW = 64
BASE_GAP = 3.0
BASE_ANGLE_STEP = BASE_GAP * TAU
HARMONIC_SAMPLES = 4096
HARMONIC_ACTIVITY_FLOOR_REL = 1.0e-10
FULL_TONE_ZERO_TOL = 1.0e-13
LAURENT_DEGREE = 3
LAURENT_SAMPLE_COUNT = 2 * LAURENT_DEGREE + 1
LAURENT_VALIDATE_COUNT = 23
ROOT_UNIT_MARGIN = 1.0e-8

CAPTURE_TOL = 1.0e-10
RECONSTRUCTION_TOL = 1.0e-12
WEIGHT_TOL = 1.0e-10
LAW_REL_TOL = 1.0e-10
LAURENT_VALIDATION_TOL = 1.0e-12
RHO_TOL = 1.0e-10
EXACT_GAP_TOL = 1.0e-9
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
FROZEN_HARMONIC_W1 = (
    (3, 0.08048295383438742),
    (4, 0.1440522037836752),
    (5, 0.5386759094844884),
    (6, 0.9585360527752671),
)
FROZEN_HARMONIC_W2 = (
    (3, 0.5530957186939333),
    (4, 0.03973895167122795),
    (5, 0.2359028714256409),
    (6, 0.031142737013937785),
)
FROZEN_HARMONIC_W3 = (
    (3, 0.22475620052259018),
    (4, 0.2438506157558906),
    (5, 0.07844023339874479),
    (6, 0.005115793420849276),
)
FROZEN_HARMONIC_W4 = (
    (3, 0.07855932462449593),
    (4, 0.04625192478276678),
    (5, 0.06706947058861758),
    (6, 0.002228063335537077),
)
FROZEN_TAIL_GE2 = (
    (3, 0.9195170362374585),
    (4, 0.8559477956694486),
    (5, 0.46132408212936277),
    (6, 0.04146394706706311),
)
FROZEN_TAIL_GE3 = (
    (3, 0.3664213175435252),
    (4, 0.8162088439982206),
    (5, 0.22542121070372184),
    (6, 0.010321210053125331),
)
FROZEN_ROOT_SPLIT = (
    (3, 3, 3),
    (4, 4, 2),
    (5, 3, 3),
    (6, 2, 4),
)
FROZEN_RHO_STAR = (
    (3, 0.9919549005210793),
    (4, 0.8930424659337683),
    (5, 0.9911070642613854),
    (6, 0.7619077977082198),
)
FROZEN_SINGLE_SIDEBAND_INVALID_RHO12_STATES = (3, 4, 5)
FROZEN_TAIL_GE2_ORDER_ASCENDING = (6, 5, 4, 3)
FROZEN_DEPTH_ORDER_ASCENDING = (6, 5, 3, 4)


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


def evolved_site01_block(
    theta: float,
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> np.ndarray:
    spectral_time = theta / BASE_GAP
    u = evecs @ np.diag(np.exp(-1j * spectral_time * evals)) @ evecs.conj().T
    rho_t = u @ rho0 @ u.conj().T
    return rho_t[0:NC, NC : 2 * NC]


def raw_det_site01(
    theta: float,
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> complex:
    return complex(np.linalg.det(evolved_site01_block(theta, rho0, evals, evecs)))


def det_polar_site01(
    theta: float,
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> complex:
    return complex(np.linalg.det(polar_u(evolved_site01_block(theta, rho0, evals, evecs))))


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


def raw_reconstruction_error(x: np.ndarray) -> float:
    coeffs = np.fft.fft(x) / len(x)
    reconstructed = np.fft.ifft(coeffs * len(coeffs)).real
    active_count = int(np.sum(np.abs(coeffs) > FULL_TONE_ZERO_TOL))
    if active_count == 0:
        raise FloatingPointError("raw FFT unexpectedly has no active coefficients")
    return float(np.max(np.abs(x - reconstructed)))


def site01_projector(n_sites: int) -> np.ndarray:
    p = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    p[0:NC, 0:NC] = np.eye(NC)
    p[NC : 2 * NC, NC : 2 * NC] = np.eye(NC)
    return p


def coupled_gap_set(
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> tuple[float, ...]:
    occ = evecs.conj().T @ rho0 @ evecs
    p01 = evecs.conj().T @ site01_projector(L) @ evecs
    weights: dict[float, float] = {}
    for a in range(len(evals)):
        for b in range(len(evals)):
            weight = abs(occ[a, b]) * abs(p01[b, a])
            if weight > 0.0:
                gap = round(float(evals[a] - evals[b]), 12)
                weights[gap] = weights.get(gap, 0.0) + float(weight)
    return tuple(sorted(weights))


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
    tail_ge2 = sum(weight for k, weight in w_by_abs_k.items() if k >= 2)
    tail_ge3 = sum(weight for k, weight in w_by_abs_k.items() if k >= 3)
    return HarmonicAnalysis(
        active_count=int(len(active)),
        max_abs_k=int(max(abs(int(signed_k[idx])) for idx in active)),
        w_by_abs_k=w_by_abs_k,
        tail_ge2=float(tail_ge2),
        tail_ge3=float(tail_ge3),
        max_gap_residual=max_gap_residual,
    )


def determinant_laurent_coefficients(
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> np.ndarray:
    theta = 2.0 * math.pi * np.arange(LAURENT_SAMPLE_COUNT) / LAURENT_SAMPLE_COUNT
    values = np.array([raw_det_site01(float(theta_i), rho0, evals, evecs) for theta_i in theta])
    return np.array(
        [
            np.mean(values * np.exp(-1j * n * theta))
            for n in range(-LAURENT_DEGREE, LAURENT_DEGREE + 1)
        ],
        dtype=complex,
    )


def eval_laurent(coeffs: np.ndarray, theta: np.ndarray) -> np.ndarray:
    powers = np.arange(-LAURENT_DEGREE, LAURENT_DEGREE + 1)
    return np.exp(1j * np.outer(theta, powers)) @ coeffs


def laurent_validation_error(
    coeffs: np.ndarray,
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> float:
    theta = 2.0 * math.pi * np.arange(LAURENT_VALIDATE_COUNT) / LAURENT_VALIDATE_COUNT
    observed = np.array([raw_det_site01(float(theta_i), rho0, evals, evecs) for theta_i in theta])
    predicted = eval_laurent(coeffs, theta)
    return float(np.max(np.abs(observed - predicted)))


def corrected_law_values(coeffs: np.ndarray) -> np.ndarray:
    theta = 2.0 * math.pi * np.arange(HARMONIC_SAMPLES) / HARMONIC_SAMPLES
    z0 = eval_laurent(coeffs, theta)
    z1 = eval_laurent(coeffs, theta + BASE_ANGLE_STEP)
    values = np.angle(z1 / z0)
    return values - float(np.mean(values))


def determinant_root_law(
    coeffs: np.ndarray,
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> LawAnalysis:
    roots = np.roots(coeffs[::-1])
    inside = [root for root in roots if abs(root) < 1.0 - ROOT_UNIT_MARGIN]
    outside = [root for root in roots if abs(root) > 1.0 + ROOT_UNIT_MARGIN]
    rho_candidates = [abs(root) for root in inside] + [1.0 / abs(root) for root in outside]
    if not rho_candidates:
        raise FloatingPointError("determinant root law has no subunit root datum")
    return LawAnalysis(
        harmonic=harmonic_ladder_analysis(corrected_law_values(coeffs)),
        laurent_validation_error=laurent_validation_error(coeffs, rho0, evals, evecs),
        root_inside_count=len(inside),
        root_outside_count=len(outside),
        rho_star=float(max(rho_candidates)),
    )


def analyze_state(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> StateAnalysis:
    rho0, increments = phase_increment_sequence(spec, evals, evecs)
    svals = hankel_svals(increments, CAPTURE_WINDOW)
    harmonic_values = base_angle_increment_values(rho0, evals, evecs)
    coeffs = determinant_laurent_coefficients(rho0, evals, evecs)
    return StateAnalysis(
        spec=spec,
        capture4=sv_capture(svals, 4),
        hankel_tail_fraction=tail_fraction_from_svals(svals, 4),
        no_floor_gaps=coupled_gap_set(rho0, evals, evecs),
        raw_reconstruction_error=raw_reconstruction_error(increments),
        harmonic=harmonic_ladder_analysis(harmonic_values),
        law=determinant_root_law(coeffs, rho0, evals, evecs),
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


def value_detail(rows: tuple[tuple[int, float], ...]) -> str:
    return ", ".join(f"K{k}:{value:.12g}" for k, value in rows)


def count_detail(rows: tuple[tuple[int, int, int], ...]) -> str:
    return ", ".join(f"K{k}:in={inside},out={outside}" for k, inside, outside in rows)


def order_by_float(rows: tuple[tuple[int, float], ...]) -> tuple[int, ...]:
    return tuple(k for k, _ in sorted(rows, key=lambda item: item[1]))


def gap_set_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, tuple[float, ...]], ...]:
    return tuple(
        (record.spec.k_occ, tuple(round(gap, 9) for gap in record.no_floor_gaps))
        for record in records
    )


def capture_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, float], ...]:
    return tuple((record.spec.k_occ, record.capture4) for record in records)


def reconstruction_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, float], ...]:
    return tuple((record.spec.k_occ, record.raw_reconstruction_error) for record in records)


def measured_weight_table(records: tuple[StateAnalysis, ...], k: int) -> tuple[tuple[int, float], ...]:
    return tuple((record.spec.k_occ, record.harmonic.w_by_abs_k.get(k, 0.0)) for record in records)


def law_weight_table(records: tuple[StateAnalysis, ...], k: int) -> tuple[tuple[int, float], ...]:
    return tuple((record.spec.k_occ, record.law.harmonic.w_by_abs_k.get(k, 0.0)) for record in records)


def tail_table(records: tuple[StateAnalysis, ...], source: str, threshold_k: int) -> tuple[tuple[int, float], ...]:
    rows: list[tuple[int, float]] = []
    for record in records:
        harmonic = record.harmonic if source == "measured" else record.law.harmonic
        if threshold_k == 2:
            value = harmonic.tail_ge2
        elif threshold_k == 3:
            value = harmonic.tail_ge3
        else:
            raise ValueError("unsupported tail threshold")
        rows.append((record.spec.k_occ, value))
    return tuple(rows)


def root_split_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (record.spec.k_occ, record.law.root_inside_count, record.law.root_outside_count)
        for record in records
    )


def rho_star_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, float], ...]:
    return tuple((record.spec.k_occ, record.law.rho_star) for record in records)


def single_sideband_rho12_table(records: tuple[StateAnalysis, ...]) -> tuple[tuple[int, float], ...]:
    rows: list[tuple[int, float]] = []
    for record in records:
        w1 = record.harmonic.w_by_abs_k.get(1, 0.0)
        w2 = record.harmonic.w_by_abs_k.get(2, 0.0)
        rows.append((record.spec.k_occ, 2.0 * math.sqrt(w2 / w1)))
    return tuple(rows)


def max_law_relative_deviation(records: tuple[StateAnalysis, ...], ks: tuple[int, ...]) -> float:
    max_rel = 0.0
    for record in records:
        for k in ks:
            measured = record.harmonic.w_by_abs_k.get(k, 0.0)
            predicted = record.law.harmonic.w_by_abs_k.get(k, 0.0)
            max_rel = max(max_rel, abs(predicted - measured) / measured)
    return max_rel


def print_weight_rows(records: tuple[StateAnalysis, ...]) -> None:
    print("  state      rho_*     rho_12        w1          w2          w3          w4")
    for record in records:
        rho12 = 2.0 * math.sqrt(
            record.harmonic.w_by_abs_k.get(2, 0.0) / record.harmonic.w_by_abs_k.get(1, 0.0)
        )
        w = record.harmonic.w_by_abs_k
        print(
            f"  K={record.spec.k_occ:<1d}"
            f" {record.law.rho_star:10.6f}"
            f" {rho12:10.6f}"
            f" {w.get(1, 0.0):11.9f}"
            f" {w.get(2, 0.0):11.9f}"
            f" {w.get(3, 0.0):11.9f}"
            f" {w.get(4, 0.0):11.9f}"
        )


def main() -> int:
    print("=" * 78)
    print("Harmonic ladder weight law: single-sideband refutation and corrected law")
    print("=" * 78)
    print(f"constants: L={L}, NC={NC}, tau={TAU}, T={T_STEPS}, window={CAPTURE_WINDOW}")
    print(
        f"base-angle samples={HARMONIC_SAMPLES}, delta={BASE_ANGLE_STEP:.12g}, "
        f"activity floor={HARMONIC_ACTIVITY_FLOOR_REL:.1e}"
    )
    print("corrected law: degree-3 Laurent determinant with principal-branch Arg")
    print()

    h = lattice_hamiltonian(L)
    evals, evecs = np.linalg.eigh(h)
    records = tuple(analyze_state(spec, evals, evecs) for spec in STATES)

    print("S0 anchors from the landed harmonic-ladder machinery")
    print("-" * 78)
    observed_gap_sets = gap_set_table(records)
    check(
        "ANCHOR: no-floor coupled eigenpair gap set is frozen as (-3,0,+3) per state",
        observed_gap_sets == FROZEN_NO_FLOOR_GAP_SETS,
        ", ".join(f"K{k}:{gaps}" for k, gaps in observed_gap_sets),
    )
    observed_capture = capture_table(records)
    check(
        "ANCHOR: landed capture@order4/window64 table is reproduced",
        table_close(observed_capture, FROZEN_CAPTURE4_W64, CAPTURE_TOL),
        value_detail(observed_capture),
    )
    observed_recon = reconstruction_table(records)
    check(
        "ANCHOR: full raw tone sum reconstructs the centered trajectory below 1e-12",
        max(value for _, value in observed_recon) <= RECONSTRUCTION_TOL,
        value_detail(observed_recon),
    )
    observed_w2 = measured_weight_table(records, 2)
    check(
        "anti-fabrication: measured k=2 ladder weight is nonzero in every state",
        min(value for _, value in observed_w2) >= K2_NONZERO_FLOOR,
        value_detail(observed_w2),
    )
    check(
        "ANCHOR: measured k=2 ladder weights are frozen",
        table_close(observed_w2, FROZEN_HARMONIC_W2, WEIGHT_TOL),
        value_detail(observed_w2),
    )

    print()
    print("S1 rho extraction")
    print("-" * 78)
    print("  rho_12 is the single-sideband extraction 2*sqrt(w2/w1).")
    print("  rho_* is the corrected-law dominant subunit determinant-root datum.")
    print_weight_rows(records)
    observed_validation = tuple(
        (record.spec.k_occ, record.law.laurent_validation_error) for record in records
    )
    check(
        "S1 corrected-law anti-fabrication: Laurent determinant reconstructs held-out det samples",
        max(value for _, value in observed_validation) <= LAURENT_VALIDATION_TOL,
        value_detail(observed_validation),
    )
    observed_root_split = root_split_table(records)
    check(
        "S1 determinant-root split is frozen and nontrivial",
        observed_root_split == FROZEN_ROOT_SPLIT,
        count_detail(observed_root_split),
    )
    observed_rho_star = rho_star_table(records)
    check(
        "S1 corrected rho_* table is frozen",
        table_close(observed_rho_star, FROZEN_RHO_STAR, RHO_TOL),
        value_detail(observed_rho_star),
    )
    check(
        "S1 anti-fabrication: every corrected rho_* is strictly nonzero and subunit",
        all(0.0 < value < 1.0 for _, value in observed_rho_star),
        value_detail(observed_rho_star),
    )

    print()
    print("S2 ladder-law test")
    print("-" * 78)
    observed_rho12 = single_sideband_rho12_table(records)
    invalid_rho12 = tuple(k for k, value in observed_rho12 if not (0.0 < value < 1.0))
    check(
        "S2 refutation: single-sideband rho_12 violates |B|<|A| in the frozen states",
        invalid_rho12 == FROZEN_SINGLE_SIDEBAND_INVALID_RHO12_STATES,
        value_detail(observed_rho12),
    )
    observed_w1 = measured_weight_table(records, 1)
    observed_w3 = measured_weight_table(records, 3)
    observed_w4 = measured_weight_table(records, 4)
    check(
        "S2 measured w1 table is frozen",
        table_close(observed_w1, FROZEN_HARMONIC_W1, WEIGHT_TOL),
        value_detail(observed_w1),
    )
    check(
        "S2 measured w3 table is frozen",
        table_close(observed_w3, FROZEN_HARMONIC_W3, WEIGHT_TOL),
        value_detail(observed_w3),
    )
    check(
        "S2 measured w4 table is frozen",
        table_close(observed_w4, FROZEN_HARMONIC_W4, WEIGHT_TOL),
        value_detail(observed_w4),
    )
    max_rel = max_law_relative_deviation(records, (2, 3, 4))
    check(
        "S2 corrected Laurent-Arg law predicts w2,w3,w4 below fixed relative tolerance",
        max_rel <= LAW_REL_TOL,
        f"max_rel={max_rel:.3e}, tol={LAW_REL_TOL:.1e}",
    )
    observed_gap_residual = tuple(
        (record.spec.k_occ, record.harmonic.max_gap_residual) for record in records
    )
    check(
        "S2 base-angle ladder-grid residual is machine-zero against gap 3k",
        max(value for _, value in observed_gap_residual) <= EXACT_GAP_TOL,
        value_detail(observed_gap_residual),
    )

    print()
    print("S3 tail closed-form analog")
    print("-" * 78)
    measured_tail_ge2 = tail_table(records, "measured", 2)
    law_tail_ge2 = tail_table(records, "law", 2)
    measured_tail_ge3 = tail_table(records, "measured", 3)
    law_tail_ge3 = tail_table(records, "law", 3)
    print("  full nonfundamental tail T_ge2=sum_{k>=2} w_k")
    print("   measured:", value_detail(measured_tail_ge2))
    print("   law:     ", value_detail(law_tail_ge2))
    print("  depth tail T_ge3=sum_{k>=3} w_k after separating the k=2 sideband")
    print("   measured:", value_detail(measured_tail_ge3))
    print("   law:     ", value_detail(law_tail_ge3))
    check(
        "S3 measured full nonfundamental tail T_ge2 table is frozen",
        table_close(measured_tail_ge2, FROZEN_TAIL_GE2, WEIGHT_TOL),
        value_detail(measured_tail_ge2),
    )
    check(
        "S3 corrected law reproduces the full nonfundamental tail T_ge2",
        table_close(law_tail_ge2, measured_tail_ge2, WEIGHT_TOL),
        value_detail(law_tail_ge2),
    )
    check(
        "S3 full T_ge2 order is the frozen refutation of the depth-order claim",
        order_by_float(measured_tail_ge2) == FROZEN_TAIL_GE2_ORDER_ASCENDING,
        f"order={order_by_float(measured_tail_ge2)}",
    )
    check(
        "S3 measured depth tail T_ge3 table is frozen",
        table_close(measured_tail_ge3, FROZEN_TAIL_GE3, WEIGHT_TOL),
        value_detail(measured_tail_ge3),
    )
    check(
        "S3 corrected law reproduces the depth tail T_ge3",
        table_close(law_tail_ge3, measured_tail_ge3, WEIGHT_TOL),
        value_detail(law_tail_ge3),
    )
    check(
        "S3 T_ge3 ordering reproduces the landed depth order K6,K5,K3,K4",
        order_by_float(measured_tail_ge3) == FROZEN_DEPTH_ORDER_ASCENDING,
        f"order={order_by_float(measured_tail_ge3)}",
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: exact finite L=3 realized states only.")
    print("FINDING: the single-carrier/single-sideband phase-modulation law is")
    print("  refuted by the measured rho_12 table.  The weights are reproduced by")
    print("  the finite Laurent determinant corrected law")
    print("  Arg(F(e^{i(theta+delta)})/F(e^{i theta})) with principal-branch wrap.")
    print("  The full k>=2 tail does not reproduce the depth order; after separating")
    print("  the nonzero k=2 sideband, the k>=3 tail has the landed order K6,K5,K3,K4.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
