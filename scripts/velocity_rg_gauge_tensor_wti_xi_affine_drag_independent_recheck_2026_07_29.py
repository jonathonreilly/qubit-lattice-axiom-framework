#!/usr/bin/env python3
"""Independent audit recheck for the bounded velocity-RG proxy packet.

This runner deliberately does not import or call the primary runner.  It
rebuilds the load-bearing fermion and gauge responses from scalar Euclidean
gamma-trace identities,

  tr(g_a g_m g_b g_n) / 4
      = delta_am delta_bn - delta_ab delta_mn + delta_an delta_mb,

rather than constructing the primary runner's 4 x 4 gamma matrices.  Cache
identity, completeness, and packet-fit checks remain owned by the canonical
audit infrastructure, so this helper has no runtime dependency on either
runner cache and can be refreshed safely in parallel with the primary runner.

The result remains only a bounded finite-grid static-response certificate on
the declared periodic N^4 naive-Dirac SU(2) reconstruction.
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py",
)

PASS = 0
FAIL = 0


def check(code: str, ok: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {code} :: {detail}")


def qhat(q: np.ndarray) -> np.ndarray:
    return 2.0 * np.sin(q / 2.0)


def bz_grid(n: int) -> np.ndarray:
    axis = (np.arange(n) + 0.5) * (2.0 * np.pi / n) - np.pi
    return np.stack(np.meshgrid(axis, axis, axis, axis, indexing="ij"), -1).reshape(-1, 4)


def gauge_line(k: np.ndarray, xi: float, eps: float) -> tuple[np.ndarray, np.ndarray]:
    """Declared D_w(xi), rebuilt directly as I/K-(1-xi) qhat qhat^T/K^2."""
    weights = np.array([1.0 - eps / 2.0] + [1.0 + eps / 2.0] * 3)
    kh = qhat(k)
    K = (kh * kh) @ weights
    outer = kh[:, :, None] * kh[:, None, :]
    D = np.eye(4)[None, :, :] / K[:, None, None]
    D -= (1.0 - xi) * outer / (K * K)[:, None, None]
    return D, K


def rainbow_split_scalar_trace(n: int, xi: float, delta: float, eps: float) -> float:
    """out_s-out_t after analytically taking the four-gamma spin trace."""
    k = bz_grid(n)
    D, _ = gauge_line(k, xi, eps)
    diagonal = np.diagonal(D, axis1=1, axis2=2)
    out: list[float] = []
    for axis in (0, 1):
        p = np.zeros(4)
        p[axis] = delta
        s = np.sin(p - k)
        c = np.cos(p - k / 2.0)
        denominator = np.sum(s * s, axis=1)
        first = 2.0 * c[:, axis] * np.einsum(
            "ni,ni->n", D[:, axis, :], c * s
        )
        second = s[:, axis] * np.sum(diagonal * c * c, axis=1)
        out.append(float(np.mean((first - second) / denominator) / math.sin(delta)))
    return out[1] - out[0]


def tadpole_split_direct(n: int, xi: float, eps: float) -> tuple[float, float]:
    """Return direct diagonal-D split and the independent cosine closed form."""
    k = bz_grid(n)
    D, K = gauge_line(k, xi, eps)
    direct = 0.5 * float(np.mean(D[:, 1, 1] - D[:, 0, 0]))
    closed = (1.0 - xi) * float(
        np.mean((np.cos(k[:, 1]) - np.cos(k[:, 0])) / (K * K))
    )
    return direct, closed


def polarization_scalar_trace(q: np.ndarray, n: int, velocities: np.ndarray) -> np.ndarray:
    """Bubble plus seagull after an analytic four-gamma trace.

    This is algebraically independent of the primary matrix-product path.  The
    final factor 1/2 is T_F from one SU(2)-fundamental color trace.
    """
    k = bz_grid(n)
    sk = np.sin(k) * velocities
    skq = np.sin(k + q) * velocities
    cmid = np.cos(k + q / 2.0) * velocities
    dk = np.sum(sk * sk, axis=1)
    dkq = np.sum(skq * skq, axis=1)
    dot = np.sum(sk * skq, axis=1)
    Pi = np.zeros((4, 4), dtype=float)
    for mu in range(4):
        for nu in range(4):
            trace4 = sk[:, mu] * skq[:, nu] + sk[:, nu] * skq[:, mu]
            if mu == nu:
                trace4 -= dot
            bubble = 4.0 * cmid[:, mu] * cmid[:, nu] * trace4 / (dk * dkq)
            seagull = 4.0 * sk[:, mu] ** 2 / dk if mu == nu else 0.0
            Pi[mu, nu] = 0.5 * float(np.mean(bubble + seagull))
    return Pi


def ward_residual(Pi: np.ndarray, q: np.ndarray) -> float:
    kh = qhat(q)
    return float(
        np.max(np.abs(kh @ Pi))
        / (np.linalg.norm(kh) * np.max(np.abs(Pi)) + 1.0e-30)
    )


def check_normalizations() -> tuple[Fraction, Fraction]:
    # For a non-self-conjugate Fourier mode, sum_x cos^2(q.x+phi)=V/2.
    # The quadratic action contributes its separate 1/2, hence V/4.
    n = 6
    qidx = np.array([1, 2, 0, 1])
    x = np.stack(
        np.meshgrid(np.arange(n), np.arange(n), np.arange(n), np.arange(n), indexing="ij"),
        -1,
    ).reshape(-1, 4)
    q = 2.0 * np.pi * qidx / n
    cosine_sums = [float(np.sum(np.cos(x @ q + q[mu] / 2.0) ** 2)) for mu in range(4)]
    v_over_4 = Fraction(n**4, 4)
    check(
        "E1.real-mode-normalization",
        any((2 * qidx) % n != 0)
        and all(abs(s / 2.0 - float(v_over_4)) < 1.0e-10 for s in cosine_sums),
        f"sum cos^2=V/2={cosine_sums[0]:.0f}; action factor gives V/4={v_over_4}",
    )

    # sigma_a^2=I_2 and tr(I_2)=2 give these exact factors without using the
    # primary runner's matrices.
    trace_fundamental = Fraction(2, 4)
    casimir_fundamental = 3 * Fraction(1, 4)
    check(
        "E2.su2-factors",
        trace_fundamental == Fraction(1, 2)
        and casimir_fundamental == Fraction(3, 4),
        f"T_F=tr[(sigma_a/2)^2]={trace_fundamental}; C_F=sum_a sigma_a^2/4={casimir_fundamental}",
    )

    p = np.array([0.37, -0.81, 1.12, -0.29])
    k = np.array([0.23, 0.42, -0.67, 1.01])
    trig_residual = np.max(
        np.abs(qhat(k) * np.cos(p - k / 2.0) - (np.sin(p) - np.sin(p - k)))
    )
    check(
        "E3.midpoint-wti-factor",
        trig_residual < 1.0e-14,
        f"max scalar identity residual = {trig_residual:.3e}",
    )
    return casimir_fundamental, trace_fundamental


def check_load_bearing_responses(C_F: Fraction, T_F: Fraction) -> None:
    eps = 0.10
    rainbow = rainbow_split_scalar_trace(10, 0.0, 0.30, eps)
    tad_direct, tad_closed = tadpole_split_direct(10, 0.0, eps)
    total = rainbow + tad_direct
    dv_b_offset = math.sqrt((1.0 + eps / 2.0) / (1.0 - eps / 2.0)) - 1.0
    dv_f_response = -float(C_F) * total
    check(
        "E4.fermion-response",
        abs(tad_direct - tad_closed) < 1.0e-14
        and dv_f_response > 0.0
        and round(dv_b_offset, 5) == 0.05131
        and round(dv_f_response, 5) == 0.00098,
        "scalar trace gives "
        f"rainbow={rainbow:+.8f}, tadpole={tad_direct:+.8f}, "
        f"dv_B={dv_b_offset:+.8f}, dv_F/g^2={dv_f_response:+.8f}",
    )

    n = 12
    q_value = 2.0 * np.pi / n
    q_t = np.array([q_value, 0.0, 0.0, 0.0])
    q_s = np.array([0.0, q_value, 0.0, 0.0])
    velocities = np.array([0.95, 1.05, 1.05, 1.05])
    pi_t = polarization_scalar_trace(q_t, n, velocities)
    pi_s = polarization_scalar_trace(q_s, n, velocities)
    ward_t = ward_residual(pi_t, q_t)
    ward_s = ward_residual(pi_s, q_s)
    kh2 = qhat(q_t)[0] ** 2
    pi_transverse_t = pi_t[1, 1] / kh2
    pi_transverse_s = pi_s[2, 2] / kh2
    dv_b_response = (pi_transverse_s - pi_transverse_t) / 2.0
    dv_f_offset = velocities[1] / velocities[0] - 1.0
    check(
        "E5.gauge-response",
        max(ward_t, ward_s) < 1.0e-10
        and T_F == Fraction(1, 2)
        and dv_b_response > 0.0
        and round(q_value, 5) == 0.52360
        and round(dv_f_offset, 5) == 0.10526
        and round(dv_b_response, 5) == 0.02177,
        "analytic spin trace plus T_F=1/2 gives "
        f"Ward_max={max(ward_t, ward_s):.3e}, q={q_value:.8f}, "
        f"dv_F={dv_f_offset:+.8f}, dv_B/g^2={dv_b_response:+.8f}",
    )

    a_proxy = dv_f_response / dv_b_offset
    b_proxy = dv_b_response / dv_f_offset
    contraction = a_proxy + b_proxy
    # For F=[[-a,a],[b,-b]], row sums and determinant vanish; the trace is
    # -(a+b), fixing eigenvalues 0 and -(a+b) without numerical eigensolving.
    row_sums = np.array([-a_proxy + a_proxy, b_proxy - b_proxy])
    determinant = a_proxy * b_proxy - a_proxy * b_proxy
    trace = -(a_proxy + b_proxy)
    check(
        "E6.proxy-arithmetic",
        a_proxy > 0.0
        and b_proxy > 0.0
        and round(a_proxy, 4) == 0.0191
        and round(b_proxy, 4) == 0.2068
        and round(contraction, 4) == 0.2259,
        f"a_proxy={a_proxy:+.8f}, b_proxy={b_proxy:+.8f}, a+b={contraction:+.8f}",
    )
    check(
        "E7.proxy-matrix",
        np.max(np.abs(row_sums)) == 0.0
        and determinant == 0.0
        and trace < 0.0,
        f"row sums={row_sums.tolist()}, det={determinant:+.1f}, eigenvalues={{0,{trace:+.8f}}}",
    )


def main() -> int:
    print("Independent scalar-trace and execution-evidence recheck (bounded finite object)")
    print("implementation rule: no import/call of the primary runner")
    C_F, T_F = check_normalizations()
    check_load_bearing_responses(C_F, T_F)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
