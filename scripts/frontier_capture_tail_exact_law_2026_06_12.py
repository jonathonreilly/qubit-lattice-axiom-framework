#!/usr/bin/env python3
"""Class-A finite-dimensional verification for capture-deficit tail accounting.

Source note:
    docs/CAPTURE_DEFICIT_EXACT_TAIL_ACCOUNTING_BOUNDED_THEOREM_NOTE_2026-06-12.md

Scope: exact L=3 realized-state data.  The audit lane grades.

Run:
    python3 scripts/frontier_capture_tail_exact_law_2026_06_12.py
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
class StateAnalysis:
    spec: StateSpec
    capture4_direct: float
    capture4_from_full_spectrum: float
    capture_deficit: float
    hankel_tail_fraction: float
    tail_law_error: float
    reconstruction_error: float
    floor_gap_count: int
    no_floor_gap_count: int
    no_floor_gaps: tuple[float, ...]
    full_tone_active_count: int
    full_tone_total_count: int
    hankel_tail_energy: float
    hankel_total_energy: float


L = 3
NC = 3
DIM = L * NC
TAU = 0.35
T_STEPS = 256
CAPTURE_WINDOW = 64
COUPLING_FLOOR = 1.0e-8
FULL_TONE_ZERO_TOL = 1.0e-13

CAPTURE_TOL = 1.0e-10
RECONSTRUCTION_TOL = 1.0e-12
TAIL_LAW_TOL = 1.0e-12
ENERGY_TOL = 1.0e-8

STATES = (
    StateSpec("K=3", 3, 391),
    StateSpec("K=4", 4, 99),
    StateSpec("K=5(seed=99)", 5, 99),
    StateSpec("K=6", 6, 466),
)

FROZEN_CAPTURE4_W64 = (
    (3, 0.8981300885645052),
    (4, 0.7776195573427411),
    (5, 0.8991555454934871),
    (6, 0.9949365168913127),
)
FROZEN_CAPTURE_DEFICIT_W64 = (
    (3, 0.10186991143549484),
    (4, 0.22238044265725887),
    (5, 0.10084445450651291),
    (6, 0.005063483108687317),
)
FROZEN_HANKEL_TAIL_FRACTION_W64 = (
    (3, 0.10186991143549493),
    (4, 0.2223804426572589),
    (5, 0.10084445450651301),
    (6, 0.005063483108687255),
)
FROZEN_FLOOR_GAP_COUNTS = (
    (3, 3),
    (4, 3),
    (5, 3),
    (6, 3),
)
FROZEN_NO_FLOOR_GAP_COUNTS = (
    (3, 3),
    (4, 3),
    (5, 3),
    (6, 3),
)
FROZEN_FULL_ACTIVE_TONE_COUNTS = (
    (3, 255),
    (4, 255),
    (5, 255),
    (6, 255),
)
FROZEN_FULL_TOTAL_TONE_COUNTS = (
    (3, 256),
    (4, 256),
    (5, 256),
    (6, 256),
)
FROZEN_TAIL_ORDER_ASCENDING = (6, 5, 3, 4)
FROZEN_CAPTURE_ORDER_DESCENDING = (6, 5, 3, 4)
FROZEN_MIN_ACTIVE_TONES = 4
FROZEN_MIN_TAIL_ENERGY = 1.0


def lattice_hamiltonian(n_sites: int) -> np.ndarray:
    """Color-diagonal nearest-neighbor hopping on a periodic n-site ring."""
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


def phase_increment_sequence(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    q = state_modes(DIM, spec.k_occ, spec.seed)
    rho0 = q @ q.conj().T
    phases = []
    for t in range(T_STEPS + 1):
        u = evecs @ np.diag(np.exp(-1j * TAU * evals * t)) @ evecs.conj().T
        rho_t = u @ rho0 @ u.conj().T
        block_01 = rho_t[0:NC, NC : 2 * NC]
        phases.append(float(np.angle(np.linalg.det(polar_u(block_01)))))
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
    """Mirror the landed eigenbasis-pair gap inventory.

    The no-floor call uses floor=0.0 and still rounds the physical gap as the
    landed runner does.  The full determinant-phase spectrum below is a separate
    sampled Fourier object for the actual centered increment trajectory.
    """
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
    """Return all sampled Fourier coefficients; no amplitude floor is applied."""
    return np.fft.fft(x) / len(x)


def tone_sum(coeffs: np.ndarray) -> np.ndarray:
    return np.fft.ifft(coeffs * len(coeffs))


def hankel_from_full_spectrum(coeffs: np.ndarray, window: int) -> np.ndarray:
    n = len(coeffs)
    rows = np.arange(window, dtype=float)[:, None]
    cols = np.arange(n - window + 1, dtype=float)[None, :]
    times = rows + cols
    k = np.arange(n, dtype=float)
    phases = np.exp((2.0j * math.pi / n) * times[:, :, None] * k[None, None, :])
    return np.tensordot(phases, coeffs, axes=([2], [0])).real


def active_tone_count(coeffs: np.ndarray) -> int:
    return int(np.sum(np.abs(coeffs) > FULL_TONE_ZERO_TOL))


def tail_fraction_from_svals(svals: np.ndarray, order: int) -> tuple[float, float, float]:
    weights = svals * svals
    total = float(np.sum(weights))
    tail = float(np.sum(weights[order:]))
    return tail / total, tail, total


def analyze_state(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> StateAnalysis:
    rho0, increments = phase_increment_sequence(spec, evals, evecs)
    direct_svals = hankel_svals(increments, CAPTURE_WINDOW)
    direct_capture = sv_capture(direct_svals, 4)

    floor_gap_count = len(coupled_tone_weights(rho0, evals, evecs, COUPLING_FLOOR))
    no_floor_tones = coupled_tone_weights(rho0, evals, evecs, 0.0)
    no_floor_gap_count = len(no_floor_tones)
    no_floor_gaps = tuple(float(tone.gap) for tone in no_floor_tones)

    coeffs = full_sampled_tone_spectrum(increments)
    reconstructed = tone_sum(coeffs).real
    reconstruction_error = float(np.max(np.abs(increments - reconstructed)))

    spectrum_hankel = hankel_from_full_spectrum(coeffs, CAPTURE_WINDOW)
    spectrum_svals = np.linalg.svd(spectrum_hankel, compute_uv=False)
    capture_from_spectrum = sv_capture(spectrum_svals, 4)
    tail_fraction, tail_energy, total_energy = tail_fraction_from_svals(spectrum_svals, 4)
    deficit = 1.0 - direct_capture

    return StateAnalysis(
        spec=spec,
        capture4_direct=direct_capture,
        capture4_from_full_spectrum=capture_from_spectrum,
        capture_deficit=deficit,
        hankel_tail_fraction=tail_fraction,
        tail_law_error=abs(deficit - tail_fraction),
        reconstruction_error=reconstruction_error,
        floor_gap_count=floor_gap_count,
        no_floor_gap_count=no_floor_gap_count,
        no_floor_gaps=no_floor_gaps,
        full_tone_active_count=active_tone_count(coeffs),
        full_tone_total_count=len(coeffs),
        hankel_tail_energy=tail_energy,
        hankel_total_energy=total_energy,
    )


def close_tuple(
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


def order_by(
    records: tuple[StateAnalysis, ...],
    attr_name: str,
    reverse: bool,
) -> tuple[int, ...]:
    return tuple(
        record.spec.k_occ
        for record in sorted(records, key=lambda item: getattr(item, attr_name), reverse=reverse)
    )


def frozen_detail(rows: tuple[tuple[int, float], ...]) -> str:
    return ", ".join(f"K{k}:{value:.12g}" for k, value in rows)


def count_detail(rows: tuple[tuple[int, int], ...]) -> str:
    return ", ".join(f"K{k}:{value:d}" for k, value in rows)


def main() -> int:
    print("=" * 78)
    print("Capture-deficit exact tail accounting: L=3 det-phase trajectory")
    print("=" * 78)
    print(f"constants: L={L}, NC={NC}, tau={TAU}, T={T_STEPS}")
    print(
        f"Hankel capture window={CAPTURE_WINDOW}, Fourier bins={T_STEPS}, "
        f"full-tone zero tolerance={FULL_TONE_ZERO_TOL:.1e}"
    )
    print()

    h = lattice_hamiltonian(L)
    evals, evecs = np.linalg.eigh(h)
    records = tuple(analyze_state(spec, evals, evecs) for spec in STATES)

    print("S0 anchors")
    print("-" * 78)
    observed_capture = tuple((record.spec.k_occ, record.capture4_direct) for record in records)
    check(
        "ANCHOR: landed capture@order4/window64 frozen table is reproduced",
        close_tuple(observed_capture, FROZEN_CAPTURE4_W64, CAPTURE_TOL),
        frozen_detail(observed_capture),
    )

    observed_floor_gap_counts = tuple((record.spec.k_occ, record.floor_gap_count) for record in records)
    check(
        "ANCHOR: landed coupled-gap count above 1e-8 remains exactly three per state",
        observed_floor_gap_counts == FROZEN_FLOOR_GAP_COUNTS,
        count_detail(observed_floor_gap_counts),
    )

    observed_no_floor_gap_counts = tuple((record.spec.k_occ, record.no_floor_gap_count) for record in records)
    check(
        "ANCHOR: landed eigenpair gap inventory with no floor is still the frozen three-gap table",
        observed_no_floor_gap_counts == FROZEN_NO_FLOOR_GAP_COUNTS,
        count_detail(observed_no_floor_gap_counts),
    )

    observed_gap_sets = tuple(
        (record.spec.k_occ, tuple(round(g, 9) for g in sorted(record.no_floor_gaps)))
        for record in records
    )
    check(
        "ANCHOR: the no-floor coupled-gap SET is exactly (-3, 0, +3) for every state",
        all(gaps == (-3.0, 0.0, 3.0) for _, gaps in observed_gap_sets),
        ", ".join(f"K{k}:{gaps}" for k, gaps in observed_gap_sets),
    )

    observed_full_active_counts = tuple((record.spec.k_occ, record.full_tone_active_count) for record in records)
    check(
        "anti-fabrication: the full determinant-phase spectrum has more than three active tones",
        max(record.full_tone_active_count for record in records) >= FROZEN_MIN_ACTIVE_TONES,
        count_detail(observed_full_active_counts),
    )

    check(
        "anti-fabrication: full active tone counts reproduce the frozen no-floor spectrum",
        observed_full_active_counts == FROZEN_FULL_ACTIVE_TONE_COUNTS,
        count_detail(observed_full_active_counts),
    )

    observed_full_total_counts = tuple((record.spec.k_occ, record.full_tone_total_count) for record in records)
    check(
        "ANCHOR: all 256 sampled Fourier bins are retained before tail projection",
        observed_full_total_counts == FROZEN_FULL_TOTAL_TONE_COUNTS,
        count_detail(observed_full_total_counts),
    )

    print()
    print("S1 full-spectrum reconstruction")
    print("-" * 78)
    for record in records:
        print(
            f"  {record.spec.label:12s} active_tones={record.full_tone_active_count:d}/"
            f"{record.full_tone_total_count:d} recon_err={record.reconstruction_error:.3e}"
        )

    check(
        "S1: full tone sum reconstructs every centered phase-increment trajectory",
        max(record.reconstruction_error for record in records) <= RECONSTRUCTION_TOL,
        ", ".join(f"K{record.spec.k_occ}:{record.reconstruction_error:.3e}" for record in records),
    )

    print()
    print("S2 capture from full spectrum")
    print("-" * 78)
    observed_spectrum_capture = tuple(
        (record.spec.k_occ, record.capture4_from_full_spectrum) for record in records
    )
    for record in records:
        print(
            f"  K={record.spec.k_occ}: capture_direct={record.capture4_direct:.16g} "
            f"capture_from_spectrum={record.capture4_from_full_spectrum:.16g} "
            f"deficit={record.capture_deficit:.16g}"
        )

    check(
        "S2: full-spectrum Hankel projection reproduces landed capture values",
        close_tuple(observed_spectrum_capture, FROZEN_CAPTURE4_W64, CAPTURE_TOL),
        frozen_detail(observed_spectrum_capture),
    )

    observed_deficit = tuple((record.spec.k_occ, record.capture_deficit) for record in records)
    check(
        "S2: capture deficits reproduce the frozen landed-complement table",
        close_tuple(observed_deficit, FROZEN_CAPTURE_DEFICIT_W64, CAPTURE_TOL),
        frozen_detail(observed_deficit),
    )

    print()
    print("S3 exact tail law")
    print("-" * 78)
    observed_tail = tuple((record.spec.k_occ, record.hankel_tail_fraction) for record in records)
    for record in records:
        print(
            f"  K={record.spec.k_occ}: tail_fraction={record.hankel_tail_fraction:.16g} "
            f"tail_energy={record.hankel_tail_energy:.16g} "
            f"total_hankel_energy={record.hankel_total_energy:.16g} "
            f"tail_law_error={record.tail_law_error:.3e}"
        )

    check(
        "S3: Hankel-Frobenius tail fractions reproduce the frozen table",
        close_tuple(observed_tail, FROZEN_HANKEL_TAIL_FRACTION_W64, TAIL_LAW_TOL),
        frozen_detail(observed_tail),
    )

    check(
        "S3: deficit equals the order-4 Hankel-Frobenius tail fraction",
        max(record.tail_law_error for record in records) <= TAIL_LAW_TOL,
        ", ".join(f"K{record.spec.k_occ}:{record.tail_law_error:.3e}" for record in records),
    )

    check(
        "S3: retained tail energies are nonzero, so the deficit is not fabricated by zero mass",
        min(record.hankel_tail_energy for record in records) >= FROZEN_MIN_TAIL_ENERGY,
        ", ".join(f"K{record.spec.k_occ}:{record.hankel_tail_energy:.6g}" for record in records),
    )

    print()
    print("S4 depth ordering as tail arithmetic")
    print("-" * 78)
    capture_order = order_by(records, "capture4_direct", reverse=True)
    tail_order = order_by(records, "hankel_tail_fraction", reverse=False)
    print(f"  capture descending: {capture_order}")
    print(f"  tail ascending:     {tail_order}")
    check(
        "S4: capture ordering reproduces the frozen landed depth order",
        capture_order == FROZEN_CAPTURE_ORDER_DESCENDING,
        f"capture_order={capture_order}",
    )
    check(
        "S4: tail-mass ordering is the same arithmetic order K6,K5,K3,K4",
        tail_order == FROZEN_TAIL_ORDER_ASCENDING,
        f"tail_order={tail_order}",
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: exact finite one-body L=3 gauge-link system, realized seeds only.")
    print("CLAIM TESTED: capture deficit is exactly the order-4 Hankel-Frobenius")
    print("  tail fraction of the full sampled determinant-phase tone sum; the")
    print("  depth ordering is the ascending tail-mass arithmetic on these states.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
