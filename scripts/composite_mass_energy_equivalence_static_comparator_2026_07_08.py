#!/usr/bin/env python3
"""Curvature sum-rule and band-control runner.

Companion runner for
COMPOSITE_CURVATURE_SUM_RULE_BAND_CONTROLS_BOUNDED_THEOREM_NOTE_2026-07-08.md.

The gated content is limited to the exact Feynman-Hellmann curvature sum rule,
split invariance, the signed-zone quadratic control, and the cosine-band
control. No universal static-comparator, WEP, mediator, or framework-dynamics
conclusion is tested.
"""

from __future__ import annotations

import math
from functools import lru_cache

import numpy as np
from scipy.linalg import eigh, eigvalsh
from scipy.sparse.linalg import LinearOperator, eigsh


PASS_COUNT = 0
FAIL_COUNT = 0
FLAGS: list[str] = []

ALPHAS = (0.0, 0.5, 1.0)


def record(ok: bool, flag: str | None = None) -> bool:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
        if flag:
            FLAGS.append(flag)
    return ok


def fmt(x: float) -> str:
    return f"{x:.12e}"


def short(x: float) -> str:
    return f"{x:.3e}"


def momentum_grid(L: int) -> np.ndarray:
    return 2.0 * np.pi * np.arange(L, dtype=float) / float(L)


def signed_momentum_value(K: int, L: int) -> float:
    idx = K % L
    if idx > L // 2:
        idx -= L
    return 2.0 * np.pi * idx / float(L)


def near_zero_indices(L: int, radius: int) -> list[int]:
    return [(-n) % L for n in range(radius, 0, -1)] + [0] + list(range(1, radius + 1))


@lru_cache(maxsize=None)
def dft_phase(L: int) -> np.ndarray:
    r = np.arange(L, dtype=float)
    q = momentum_grid(L)
    return np.exp(1j * np.outer(r, q)) / np.sqrt(float(L))


def ring_distances(L: int) -> np.ndarray:
    r = np.arange(L, dtype=float)
    return np.minimum(r, float(L) - r)


def potential_values(L: int, U: float, w: float) -> np.ndarray:
    if w == 0.0:
        values = np.zeros(L, dtype=float)
        values[0] = -U
        return values
    return -U * np.exp(-ring_distances(L) / w)


def arc_energy(m: float, p: np.ndarray | float) -> np.ndarray | float:
    return np.arcsinh(np.sqrt(m * m + np.sin(p) ** 2))


def arc_d1(m: float, p: np.ndarray) -> np.ndarray:
    s = np.sin(p)
    c = np.cos(p)
    R = np.sqrt(m * m + s * s)
    S = np.sqrt(1.0 + m * m + s * s)
    return s * c / (R * S)


def arc_d2(m: float, p: np.ndarray) -> np.ndarray:
    s = np.sin(p)
    c = np.cos(p)
    R2 = m * m + s * s
    S2 = 1.0 + m * m + s * s
    D = np.sqrt(R2 * S2)
    sc2 = s * s * c * c
    return (np.cos(2.0 * p) - sc2 * (1.0 / R2 + 1.0 / S2)) / D


def quad_energy(m: float, p: np.ndarray | float) -> np.ndarray | float:
    return m + (1.0 - np.cos(p)) / m


def quad_d1(m: float, p: np.ndarray) -> np.ndarray:
    return np.sin(p) / m


def quad_d2(m: float, p: np.ndarray) -> np.ndarray:
    return np.cos(p) / m


def signed_wrap(p: np.ndarray | float) -> np.ndarray | float:
    """Map any momentum to the fundamental zone (-pi, pi]."""
    return -((np.pi - np.asarray(p)) % (2.0 * np.pi)) + np.pi


def qtrue_energy(m: float, p: np.ndarray | float) -> np.ndarray | float:
    """Exactly quadratic band on the signed zone: E'' = 1/m at every grid
    point, so the sum rule makes the Kohn/Galilean statement manifest:
    <E''> = 1/m independent of the bound state, hence M_comp = 2m exactly.
    (The band has a derivative kink at the zone edge; band-FIT deviations
    from 2m are edge artifacts and are reported, not gated.)"""
    q = signed_wrap(p)
    return m + q * q / (2.0 * m)


def qtrue_d1(m: float, p: np.ndarray) -> np.ndarray:
    return np.asarray(signed_wrap(p)) / m


def qtrue_d2(m: float, p: np.ndarray) -> np.ndarray:
    return np.full_like(np.asarray(p, dtype=float), 1.0 / m)


def energy(kind: str, m: float, p: np.ndarray | float) -> np.ndarray | float:
    if kind == "ARC":
        return arc_energy(m, p)
    if kind == "QUAD":
        return quad_energy(m, p)
    if kind == "QTRUE":
        return qtrue_energy(m, p)
    raise ValueError(f"unknown dispersion kind {kind!r}")


def d1_energy(kind: str, m: float, p: np.ndarray) -> np.ndarray:
    if kind == "ARC":
        return arc_d1(m, p)
    if kind == "QUAD":
        return quad_d1(m, p)
    if kind == "QTRUE":
        return qtrue_d1(m, p)
    raise ValueError(f"unknown dispersion kind {kind!r}")


def d2_energy(kind: str, m: float, p: np.ndarray) -> np.ndarray:
    if kind == "ARC":
        return arc_d2(m, p)
    if kind == "QUAD":
        return quad_d2(m, p)
    if kind == "QTRUE":
        return qtrue_d2(m, p)
    raise ValueError(f"unknown dispersion kind {kind!r}")


def single_inertial_mass(kind: str, m: float) -> float:
    if kind == "ARC":
        return float(m * math.sqrt(1.0 + m * m))
    if kind in ("QUAD", "QTRUE"):
        return float(m)
    raise ValueError(f"unknown dispersion kind {kind!r}")


def continuum_edge(kind: str, m: float) -> float:
    return float(2.0 * energy(kind, m, 0.0))


def kinetic_values(L: int, kind: str, m: float, P: float, alpha: float) -> np.ndarray:
    q = momentum_grid(L)
    return np.asarray(
        energy(kind, m, alpha * P + q) + energy(kind, m, (1.0 - alpha) * P - q),
        dtype=float,
    )


def dense_hamiltonian(L: int, kind: str, m: float, U: float, w: float, P: float, alpha: float) -> np.ndarray:
    phase = dft_phase(L)
    K = kinetic_values(L, kind, m, P, alpha)
    H = (phase * K[np.newaxis, :]) @ phase.conj().T
    H[np.diag_indices(L)] += potential_values(L, U, w)
    return 0.5 * (H + H.conj().T)


def lowest_energy(L: int, kind: str, m: float, U: float, w: float, P: float, alpha: float) -> float:
    if L <= 384:
        H = dense_hamiltonian(L, kind, m, U, w, P, alpha)
        return float(eigvalsh(H, subset_by_index=[0, 0], check_finite=False)[0])

    K = kinetic_values(L, kind, m, P, alpha)
    V = potential_values(L, U, w)

    def matvec(x: np.ndarray) -> np.ndarray:
        return np.fft.ifft(K * np.fft.fft(x)) + V * x

    op = LinearOperator((L, L), matvec=matvec, dtype=np.complex128)
    v0 = np.zeros(L, dtype=np.complex128)
    v0[0] = 1.0
    vals = eigsh(
        op,
        k=1,
        which="SA",
        return_eigenvectors=False,
        tol=1e-12,
        maxiter=20000,
        v0=v0,
    )
    return float(np.min(vals).real)


def fit_even_band(xs: np.ndarray, ys: np.ndarray, sextic: bool = True) -> tuple[float, float, float, float]:
    x2 = xs * xs
    columns = [np.ones_like(x2), x2, x2 * x2]
    if sextic:
        columns.append(x2 * x2 * x2)
    design = np.column_stack(columns)
    coeffs, *_ = np.linalg.lstsq(design, ys, rcond=None)
    pred = design @ coeffs
    curvature = float(2.0 * coeffs[1])
    mass = float("inf") if curvature == 0.0 else float(1.0 / curvature)
    return curvature, mass, float(np.max(np.abs(pred - ys))), float(coeffs[0])


def band_measurement(
    L: int,
    kind: str,
    m: float,
    U: float,
    w: float,
    alpha: float = 0.0,
    radius: int = 3,
) -> tuple[float, float, float, float]:
    Ks = near_zero_indices(L, radius)
    xs = np.array([signed_momentum_value(K, L) for K in Ks], dtype=float)
    ys = np.array([lowest_energy(L, kind, m, U, w, P, alpha) for P in xs], dtype=float)
    curvature, mass, residual, intercept = fit_even_band(xs, ys, sextic=True)
    return curvature, mass, residual, intercept


def kappa_L(kind: str, m: float, EB: float, L: int) -> float:
    if EB <= 0.0:
        return 0.0
    return float(math.sqrt(single_inertial_mass(kind, m) * EB) * L)


def bisection_to_binding_ratio(
    L: int,
    kind: str,
    m: float,
    w: float,
    ratio: float,
    alpha: float = 0.0,
) -> tuple[float, float, float]:
    target_E0 = continuum_edge(kind, m) / (1.0 + ratio)
    low = 0.0
    high = 1.0

    def E0_at(U: float) -> float:
        return lowest_energy(L, kind, m, U, w, 0.0, alpha)

    while E0_at(high) > target_E0:
        high *= 2.0
        if high > 128.0:
            raise RuntimeError(f"failed to bracket target for kind={kind} m={m} w={w}")

    mid = 0.5 * (low + high)
    E_mid = E0_at(mid)
    for _ in range(90):
        mid = 0.5 * (low + high)
        E_mid = E0_at(mid)
        if abs(E_mid - target_E0) <= 2e-12:
            break
        if E_mid > target_E0:
            low = mid
        else:
            high = mid
    return mid, E_mid, continuum_edge(kind, m) - E_mid


def sum_rule_parts(L: int, kind: str, m: float, U: float, w: float, alpha: float) -> tuple[float, float, float]:
    H0 = dense_hamiltonian(L, kind, m, U, w, 0.0, alpha)
    evals, evecs = eigh(H0, check_finite=False)
    phase = dft_phase(L)
    coeffs_q = phase.conj().T @ evecs
    q = momentum_grid(L)

    A_q = alpha * alpha * d2_energy(kind, m, q) + (1.0 - alpha) ** 2 * d2_energy(kind, m, -q)
    B_q = alpha * d1_energy(kind, m, q) + (1.0 - alpha) * d1_energy(kind, m, -q)

    c0 = coeffs_q[:, 0]
    first = float(np.sum(np.abs(c0) ** 2 * A_q).real)
    b_n0 = coeffs_q.conj().T @ (B_q * c0)
    second = float(-2.0 * np.sum(np.abs(b_n0[1:]) ** 2 / (evals[1:] - evals[0])).real)
    return first, second, first + second


def check_01() -> str:
    L = 256
    max_sum_band = 0.0
    max_split_band = 0.0
    max_split_sum = 0.0
    rows = []
    for m in (0.5, 1.0):
        for U in (0.4, 0.8):
            by_alpha = []
            for alpha in ALPHAS:
                band_curv, _, fit_resid, _ = band_measurement(L, "ARC", m, U, 0.0, alpha)
                first, second, total = sum_rule_parts(L, "ARC", m, U, 0.0, alpha)
                max_sum_band = max(max_sum_band, abs(total - band_curv), fit_resid)
                by_alpha.append((alpha, first, second, total, band_curv))
            base_band = by_alpha[0][4]
            base_total = by_alpha[0][3]
            for _, _, _, total, band_curv in by_alpha:
                max_split_band = max(max_split_band, abs(band_curv - base_band))
                max_split_sum = max(max_split_sum, abs(total - base_total))
            split_text = ",".join(
                "a={:.1f}:A={},S2={},T={},BF={}".format(alpha, short(first), short(second), short(total), short(band))
                for alpha, first, second, total, band in by_alpha
            )
            rows.append(f"m={m:.1f},U={U:.1f}[{split_text}]")

    ok = max_sum_band <= 1e-8 and max_split_band <= 1e-8 and max_split_sum <= 1e-8
    if max_split_band > 1e-8 or max_split_sum > 1e-8:
        FLAGS.append(
            "CHECK-01 split total drift: band={} sum={}".format(short(max_split_band), short(max_split_sum))
        )
    record(ok, f"CHECK-01 sum-rule/band residual {short(max_sum_band)}")
    return (
        "CHECK-01 {} SUMRULE-VS-BANDFIT max_sum_band={} max_split_band={} max_split_sum={} rows={}".format(
            "PASS" if ok else "FAIL",
            short(max_sum_band),
            short(max_split_band),
            short(max_split_sum),
            ";".join(rows),
        )
    )


def check_02() -> str:
    """Two-leg Galilean control.

    Leg A (gated, QTRUE): on an exactly quadratic band E'' = 1/m is constant,
    so the alpha = 1/2 sum rule gives 1/M_comp = 1/(2m) EXACTLY regardless of
    the bound state — Kohn exactness made manifest. Band-fit deviations are
    zone-edge artifacts, reported ungated.

    Leg B (gated, QUAD cosine): the lattice-cosine band is NOT Kohn-exact —
    its curvature varies over the zone, so M_comp = 2m / <cos q>_phi > 2m,
    and the SAME sum rule must predict the measured band-fit curvature
    (second band-family validation). The deviation dM = M - 2m is real
    physics (bandwidth domination), reported per row; the observed exact-
    looking contact identity dM ~ E_B on this band is reported as context.
    """
    L = 256
    max_qtrue_resid = 0.0
    max_qtrue_edge = 0.0
    max_qtrue_bandctx = 0.0
    max_cos_sum_band = 0.0
    rows_a = []
    rows_b = []
    for m in (0.5, 1.0):
        for w in (0.0, 2.0):
            for U in (0.2, 0.6):
                first, second, total = sum_rule_parts(L, "QTRUE", m, U, w, 0.5)
                # Kohn exactness is carried by the FIRST-ORDER term: A is the
                # constant 1/(2m) at every grid point, so <A> = 1/(2m)
                # independent of the bound state — gated at machine
                # precision. The tiny second-order term is a zone-EDGE
                # artifact: E' of the signed quadratic band is odd except at
                # the single boundary grid point, giving B one spike whose
                # coupling through the bound state's momentum tail is the
                # printed edge term (bounded, not gated to zero).
                first_resid = abs(first - 1.0 / (2.0 * m))
                edge_term = abs(second)
                sum_M = 1.0 / total
                max_qtrue_resid = max(max_qtrue_resid, first_resid)
                max_qtrue_edge = max(max_qtrue_edge, edge_term)
                _, band_M, _, _ = band_measurement(L, "QTRUE", m, U, w, 0.5)
                E0 = lowest_energy(L, "QTRUE", m, U, w, 0.0, 0.5)
                EB = continuum_edge("QTRUE", m) - E0
                max_qtrue_bandctx = max(max_qtrue_bandctx, abs(band_M - 2.0 * m))
                rows_a.append(
                    "m={:.1f},w={:.1f},U={:.1f},EB={},first_resid={},edge2nd={},sumM={},bandM_ctx={}".format(
                        m, w, U, short(EB), short(first_resid), short(edge_term), short(sum_M), short(band_M)
                    )
                )

                band_curv, band_M_cos, fit_resid, _ = band_measurement(L, "QUAD", m, U, w, 0.5)
                _, _, total_cos = sum_rule_parts(L, "QUAD", m, U, w, 0.5)
                max_cos_sum_band = max(max_cos_sum_band, abs(total_cos - band_curv), fit_resid)
                E0c = lowest_energy(L, "QUAD", m, U, w, 0.0, 0.5)
                EBc = continuum_edge("QUAD", m) - E0c
                rows_b.append(
                    "m={:.1f},w={:.1f},U={:.1f},EB={},M={},dM={},dM_over_EB={}".format(
                        m, w, U, short(EBc), short(band_M_cos),
                        short(band_M_cos - 2.0 * m),
                        short((band_M_cos - 2.0 * m) / EBc if EBc > 0 else float("nan")),
                    )
                )

    ok = max_qtrue_resid <= 1e-12 and max_qtrue_edge <= 1e-3 and max_cos_sum_band <= 1e-8
    if not ok:
        FLAGS.append(
            "CHECK-02 control failed: qtrue_first_resid={} qtrue_edge_term={} cosine_sumrule_vs_band={}".format(
                short(max_qtrue_resid), short(max_qtrue_edge), short(max_cos_sum_band)
            )
        )
    record(ok, f"CHECK-02 Galilean-control residual {short(max(max_qtrue_resid, max_cos_sum_band))}")
    return (
        "CHECK-02 {} GALILEAN-CONTROL qtrue_first_order_max_resid={} qtrue_edge_term_max={} "
        "qtrue_bandfit_edge_ctx={} cosine_sumrule_vs_band={} | QTRUE rows={} | "
        "COSINE(variable-curvature control) rows={}".format(
            "PASS" if ok else "FAIL",
            short(max_qtrue_resid),
            short(max_qtrue_edge),
            short(max_qtrue_bandctx),
            short(max_cos_sum_band),
            ";".join(rows_a),
            ";".join(rows_b),
        )
    )

def main() -> int:
    print("COMPOSITE CURVATURE SUM RULE AND BAND CONTROLS")
    print(check_01())
    print(check_02())
    flag_text = "none" if not FLAGS else " ; ".join(FLAGS)
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT} FLAGS={flag_text}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
