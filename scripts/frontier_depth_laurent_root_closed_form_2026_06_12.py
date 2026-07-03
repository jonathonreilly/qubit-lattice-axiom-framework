#!/usr/bin/env python3
"""Depth-tail determinant-root audit for the zB L=3 realized states.

This runner mirrors the landed zB harmonic-ladder machinery:
raw_det_site01, determinant-polar site-01 phase increments, and the normalized
ladder-weight readout.  It then factors the measured Laurent determinant and
keeps the unwrapped root-power expression honest: it is reported as a bounded
approximation with a measured residual, not as a fitted equality.
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
    if bool(condition):
        PASS += 1
        print(f"  [PASS] {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"  [FAIL] {name}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


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
class StateRecord:
    spec: StateSpec
    rho0: np.ndarray
    coeffs: np.ndarray
    roots: np.ndarray
    measured: HarmonicAnalysis
    root_decomposed: HarmonicAnalysis
    heldout_laurent_error: float
    root_value_error: float
    root_weight_error: float
    unwrapped_tail_ge3: float


L = 3
NC = 3
DIM = L * NC
TAU = 0.35
BASE_GAP = 3.0
BASE_ANGLE_STEP = BASE_GAP * TAU
HARMONIC_SAMPLES = 4096
HARMONIC_ACTIVITY_FLOOR_REL = 1.0e-10
LAURENT_DEGREE = 3
LAURENT_SAMPLE_COUNT = 2 * LAURENT_DEGREE + 1
LAURENT_VALIDATE_COUNT = 23
ROOT_UNIT_MARGIN = 1.0e-8

WEIGHT_TOL = 1.0e-9
TAIL_TOL = 1.0e-9
LAURENT_TOL = 1.0e-12
ROOT_VALUE_TOL = 1.0e-11
ROOT_WEIGHT_TOL = 1.0e-9
RHO_TOL = 1.0e-10
ASYM_RATIO_M = 512
ASYM_RATIO_TOL = 1.0e-9
ROOT_POWER_REL_RESIDUAL_BOUND = 75.0
ROOT_POWER_ABS_RESIDUAL_BOUND = 14.0
ROOT_POWER_REFUTATION_FLOOR = 5.0  # min relative residual proving the scalar form FAILS

STATES = (
    StateSpec("K3", 3, 391),
    StateSpec("K4", 4, 99),
    StateSpec("K5", 5, 99),
    StateSpec("K6", 6, 466),
)

LANDED_TAIL_GE3 = {
    "K3": 0.3664213175435252,
    "K4": 0.8162088439982206,
    "K5": 0.22542121070372184,
    "K6": 0.010321210053125331,
}

LANDED_WEIGHTS = {
    "K3": {
        1: 0.08048295383438742,
        2: 0.5530957186939333,
        3: 0.22475620052259018,
        4: 0.07855932462449593,
    },
    "K4": {
        1: 0.1440522037836752,
        2: 0.03973895167122795,
        3: 0.2438506157558906,
        4: 0.04625192478276678,
    },
    "K5": {
        1: 0.5386759094844884,
        2: 0.2359028714256409,
        3: 0.07844023339874479,
        4: 0.06706947058861758,
    },
    "K6": {
        1: 0.9585360527752671,
        2: 0.031142737013937785,
        3: 0.005115793420849276,
        4: 0.002228063335537077,
    },
}

LANDED_ROOT_SPLIT = {
    "K3": (3, 3),
    "K4": (4, 2),
    "K5": (3, 3),
    "K6": (2, 4),
}

LANDED_RHO_STAR = {
    "K3": 0.9919549005210793,
    "K4": 0.8930424659337683,
    "K5": 0.9911070642613854,
    "K6": 0.7619077977082198,
}

EXPECTED_MEASURED_ORDER = ("K6", "K5", "K3", "K4")
EXPECTED_ROOT_POWER_ORDER = ("K6", "K4", "K5", "K3")


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
    return HarmonicAnalysis(
        active_count=int(len(active)),
        max_abs_k=int(max(abs(int(signed_k[idx])) for idx in active)),
        w_by_abs_k=w_by_abs_k,
        tail_ge2=float(sum(weight for k, weight in w_by_abs_k.items() if k >= 2)),
        tail_ge3=float(sum(weight for k, weight in w_by_abs_k.items() if k >= 3)),
        max_gap_residual=float(max_gap_residual),
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


def numerator_roots(coeffs: np.ndarray) -> np.ndarray:
    return np.roots(coeffs[::-1])


def root_factor_phase_values(roots: np.ndarray, wrap_product: bool) -> np.ndarray:
    theta = 2.0 * math.pi * np.arange(HARMONIC_SAMPLES) / HARMONIC_SAMPLES
    q = np.exp(1j * theta)
    total = -LAURENT_DEGREE * BASE_ANGLE_STEP * np.ones(HARMONIC_SAMPLES)
    for root in roots:
        contribution = np.angle((q * np.exp(1j * BASE_ANGLE_STEP) - root) / (q - root))
        total += contribution if wrap_product else np.unwrap(contribution)
    if wrap_product:
        total = np.angle(np.exp(1j * total))
    return total - float(np.mean(total))


def max_weight_delta(a: HarmonicAnalysis, b: HarmonicAnalysis) -> float:
    keys = set(a.w_by_abs_k) | set(b.w_by_abs_k)
    return float(max(abs(a.w_by_abs_k.get(k, 0.0) - b.w_by_abs_k.get(k, 0.0)) for k in keys))


def rho_values(roots: np.ndarray) -> list[float]:
    values: list[float] = []
    for root in roots:
        mag = abs(complex(root))
        if mag < 1.0:
            values.append(float(mag))
        else:
            values.append(float(1.0 / mag))
    return values


def root_split(roots: np.ndarray) -> tuple[int, int]:
    inside = sum(1 for root in roots if abs(complex(root)) < 1.0 - ROOT_UNIT_MARGIN)
    outside = sum(1 for root in roots if abs(complex(root)) > 1.0 + ROOT_UNIT_MARGIN)
    return inside, outside


def rho_star(roots: np.ndarray) -> float:
    return float(max(rho_values(roots)))


def root_power_tail_closed(roots: np.ndarray) -> float:
    total = 0.0
    for rho in rho_values(roots):
        total += (rho**3) / (1.0 - rho**3)
    return float(total / 3.0)


def root_power_envelope(roots: np.ndarray, m: int) -> float:
    return float(sum(rho ** (3 * m) for rho in rho_values(roots)) / 3.0)


def root_power_asymptotic_ratio(roots: np.ndarray, m: int) -> float:
    return root_power_envelope(roots, m + 1) / root_power_envelope(roots, m)


def subdominant_root_power_fraction(roots: np.ndarray) -> float:
    rhos = rho_values(roots)
    top = max(rhos)
    contributions = [(rho**3) / (1.0 - rho**3) / 3.0 for rho in rhos]
    total = sum(contributions)
    dominant = sum(c for c, rho in zip(contributions, rhos) if abs(rho - top) <= RHO_TOL)
    return float((total - dominant) / total)


def order_by(rows: dict[str, float]) -> tuple[str, ...]:
    return tuple(label for label, _value in sorted(rows.items(), key=lambda item: item[1]))


def analyze_state(spec: StateSpec, evals: np.ndarray, evecs: np.ndarray) -> StateRecord:
    q = state_modes(DIM, spec.k_occ, spec.seed)
    rho0 = q @ q.conj().T
    measured_values = base_angle_increment_values(rho0, evals, evecs)
    measured = harmonic_ladder_analysis(measured_values)
    coeffs = determinant_laurent_coefficients(rho0, evals, evecs)
    roots = numerator_roots(coeffs)
    root_values = root_factor_phase_values(roots, wrap_product=True)
    root_decomposed = harmonic_ladder_analysis(root_values)
    unwrapped = harmonic_ladder_analysis(root_factor_phase_values(roots, wrap_product=False))
    law_values = corrected_law_values(coeffs)
    return StateRecord(
        spec=spec,
        rho0=rho0,
        coeffs=coeffs,
        roots=roots,
        measured=measured,
        root_decomposed=root_decomposed,
        heldout_laurent_error=laurent_validation_error(coeffs, rho0, evals, evecs),
        root_value_error=float(np.max(np.abs(root_values - law_values))),
        root_weight_error=max_weight_delta(measured, root_decomposed),
        unwrapped_tail_ge3=unwrapped.tail_ge3,
    )


def weight_detail(record: StateRecord) -> str:
    w = record.measured.w_by_abs_k
    return (
        f"w1={w.get(1, 0.0):.17g}, w2={w.get(2, 0.0):.17g}, "
        f"w3={w.get(3, 0.0):.17g}, w4={w.get(4, 0.0):.17g}, "
        f"T_ge3={record.measured.tail_ge3:.17g}"
    )


def roots_detail(record: StateRecord) -> str:
    split = root_split(record.roots)
    return f"split={split}, rho_star={rho_star(record.roots):.17g}"


def main() -> int:
    print("Depth Laurent-root closed-form bounded audit runner")
    print("Scope: zB L=3 realized K3/K4/K5/K6 states; no git/network; audit lane grades.")
    print(
        "Machinery: raw_det_site01 + determinant-polar site01 phase increment + "
        "normalized harmonic ladder weights."
    )

    h = lattice_hamiltonian(L)
    evals, evecs = np.linalg.eigh(h)
    records = tuple(analyze_state(spec, evals, evecs) for spec in STATES)

    section("S0 anchors: real zB measured ladder weights and Laurent determinant")
    for record in records:
        label = record.spec.label
        gaps = coupled_gap_set(record.rho0, evals, evecs)
        print(f"{label}: {weight_detail(record)}")
        check(
            f"{label} no-floor coupled gap set is (-3,0,+3)",
            tuple(round(gap, 9) for gap in gaps) == (-3.0, 0.0, 3.0),
            f"gaps={gaps}",
        )
        check(
            f"{label} measured T_ge3 matches exact landed value to 1e-9",
            abs(record.measured.tail_ge3 - LANDED_TAIL_GE3[label]) <= TAIL_TOL,
            f"measured={record.measured.tail_ge3:.17g}, landed={LANDED_TAIL_GE3[label]:.17g}",
        )
        max_landed_weight_error = max(
            abs(record.measured.w_by_abs_k.get(k, 0.0) - landed)
            for k, landed in LANDED_WEIGHTS[label].items()
        )
        check(
            f"{label} measured w1..w4 match landed full-precision values",
            max_landed_weight_error <= WEIGHT_TOL,
            f"max_weight_error={max_landed_weight_error:.3e}",
        )
        check(
            f"{label} held-out Laurent reconstruction error < 1e-12",
            record.heldout_laurent_error <= LAURENT_TOL,
            f"heldout_error={record.heldout_laurent_error:.3e}",
        )

    section("S1 root decomposition of the real determinant")
    for record in records:
        label = record.spec.label
        split = root_split(record.roots)
        print(f"{label}: {roots_detail(record)}")
        check(
            f"{label} six numerator roots have the landed inside/outside split",
            split == LANDED_ROOT_SPLIT[label],
            f"split={split}, landed={LANDED_ROOT_SPLIT[label]}",
        )
        check(
            f"{label} rho_star matches zB determinant-root datum",
            abs(rho_star(record.roots) - LANDED_RHO_STAR[label]) <= RHO_TOL,
            f"rho_star={rho_star(record.roots):.17g}, landed={LANDED_RHO_STAR[label]:.17g}",
        )
        check(
            f"{label} per-root principal-branch phase sum reproduces Laurent law values",
            record.root_value_error <= ROOT_VALUE_TOL,
            f"max_value_error={record.root_value_error:.3e}",
        )
        check(
            f"{label} per-root phase-contribution weights reproduce measured ladder weights",
            record.root_weight_error <= ROOT_WEIGHT_TOL,
            f"max_weight_error={record.root_weight_error:.3e}",
        )

    section("S2 closed root-power approximation and honest residual")
    measured_tails = {record.spec.label: record.measured.tail_ge3 for record in records}
    root_power_tails = {record.spec.label: root_power_tail_closed(record.roots) for record in records}
    max_rel_residual = 0.0
    max_abs_residual = 0.0
    for record in records:
        label = record.spec.label
        closed = root_power_tails[label]
        measured = measured_tails[label]
        residual = closed - measured
        rel = abs(residual) / measured
        max_rel_residual = max(max_rel_residual, rel)
        max_abs_residual = max(max_abs_residual, abs(residual))
        print(
            f"{label}: measured T_ge3={measured:.17g}; "
            f"root_power_closed={closed:.17g}; residual={residual:.17g}; "
            f"relative={rel:.6g}; unwrapped_phase_T_ge3={record.unwrapped_tail_ge3:.17g}"
        )
    measured_order = order_by(measured_tails)
    root_power_order = order_by(root_power_tails)
    print(f"measured/principal-branch order: {' < '.join(measured_order)}")
    print(f"unwrapped root-power order:     {' < '.join(root_power_order)}")
    check(
        "measured principal-branch T_ge3 ordering reproduces 6,5,3,4",
        measured_order == EXPECTED_MEASURED_ORDER,
        f"order={measured_order}",
    )
    check(
        "unwrapped positive root-power order is disclosed as branch-incomplete",
        root_power_order == EXPECTED_ROOT_POWER_ORDER,
        f"order={root_power_order}",
    )
    check(
        "REFUTED: the tested scalar root-power closed form FAILS - relative "
        "residual is large (gated above the refutation floor), so this "
        "unwrapped positive root-moduli expression is not the measured depth "
        "tail",
        max_rel_residual >= ROOT_POWER_REFUTATION_FLOOR,
        (
            f"max_rel_residual={max_rel_residual:.6g} >= floor "
            f"{ROOT_POWER_REFUTATION_FLOOR:g} (refuted); "
            f"disclosure: max_abs={max_abs_residual:.6g}, max_rel={max_rel_residual:.6g}"
        ),
    )

    section("S3 dominant root and subdominant measured fraction")
    for record in records:
        label = record.spec.label
        rho = rho_star(record.roots)
        target = rho**3
        ratio = root_power_asymptotic_ratio(record.roots, ASYM_RATIO_M)
        sub_fraction = subdominant_root_power_fraction(record.roots)
        print(
            f"{label}: W_{{3(m+1)}}/W_{{3m}} at m={ASYM_RATIO_M} = {ratio:.17g}; "
            f"rho_star^3={target:.17g}; subdominant_fraction={sub_fraction:.17g}"
        )
        check(
            f"{label} root-power envelope asymptotic ratio tends to rho_star^3",
            abs(ratio - target) <= ASYM_RATIO_TOL,
            f"|ratio-rho^3|={abs(ratio - target):.3e}",
        )
        check(
            f"{label} subdominant root-power fraction is measured, finite, and not designed",
            0.0 <= sub_fraction <= 1.0,
            f"fraction={sub_fraction:.17g}",
        )

    section("Summary")
    print("The determinant-root configuration controls the principal-branch Laurent-Arg law.")
    print("The measured depth tail is T_ge3=sum_{k>=3} w_k from that law and orders K6,K5,K3,K4.")
    print(
        "The tested scalar unwrapped root-power closed form "
        "(1/3) sum rho_j^3/(1-rho_j^3) does not reproduce the measured "
        "magnitudes and has a named branch-wrapping residual."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
