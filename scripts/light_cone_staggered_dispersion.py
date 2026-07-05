#!/usr/bin/env python3
"""Validate the repaired light-cone framing note.

This runner is paired with docs/LIGHT_CONE_FRAMING_NOTE.md. It checks:

  [A] the corrected staggered Dirac dispersion maximum
      v_max(m) = sqrt(m^2 + 1) - m and the maximizer identity
      sin^2(k*) = m (sqrt(m^2 + 1) - m);
  [B] source-note guards for the 2026-06-12 repair wiring and absence of
      the retired J_action / fixed-step v_LR^CN formulas;
  [C] the quasilocal weighted-overlap shell condition used by the repaired
      note;
  [D] a small finite-block Crank-Nicolson cone-inheritance inequality using
      U_CN = (I - i a H/2)(I + i a H/2)^(-1).

Deterministic: no random input and no wall-clock data. Exit code 0 iff the
final line is TOTAL: PASS=n, FAIL=0.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0

MASSES = (0.0, 1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1.0, 2.0)
KGRID_N = 200_001
TOL_VMAX = 1e-6
TOL_KSTAR = 2e-5
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "LIGHT_CONE_FRAMING_NOTE.md"


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: [{tag}] {label}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: [{tag}] {label}" + (f" ({detail})" if detail else ""))


def op_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, 2))


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def v_g(k: np.ndarray, m: float) -> np.ndarray:
    """Absolute group velocity for E^2 = m^2 + sin^2(k)."""
    e = np.sqrt(m * m + np.sin(k) ** 2)
    safe_e = np.where(e > 0.0, e, 1.0)
    val = np.abs(np.sin(k) * np.cos(k)) / safe_e
    if m == 0.0:
        val = np.where(e > 0.0, val, 1.0)
    return val


def v_max_closed_form(m: float) -> float:
    return math.sqrt(m * m + 1.0) - m


def kstar_sin2_closed_form(m: float) -> float:
    return m * v_max_closed_form(m)


def shell_sum_linf(d: int, beta: float, tol: float = 1e-14) -> float:
    """Sum sum_z exp(-beta ||z||_inf) by shells."""
    total = 1.0
    r = 1
    while True:
        shell = (2 * r + 1) ** d - (2 * r - 1) ** d
        term = shell * math.exp(-beta * r)
        total += term
        if term < tol:
            return total
        r += 1
        if r > 100_000:
            raise RuntimeError("shell sum did not converge")


def kron_all(mats: tuple[np.ndarray, ...]) -> np.ndarray:
    out = mats[0]
    for mat in mats[1:]:
        out = np.kron(out, mat)
    return out


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)


def site_op(l_sites: int, site: int, op: np.ndarray) -> np.ndarray:
    return kron_all(tuple(op if i == site else I2 for i in range(l_sites)))


def two_site_op(
    l_sites: int, site_a: int, op_a: np.ndarray, site_b: int, op_b: np.ndarray
) -> np.ndarray:
    return kron_all(
        tuple(
            op_a
            if i == site_a
            else op_b
            if i == site_b
            else I2
            for i in range(l_sites)
        )
    )


def exp_hermitian(h: np.ndarray, t: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    return vecs @ np.diag(np.exp(-1j * t * vals)) @ vecs.conj().T


def cayley_forward(h: np.ndarray, a_step: float) -> np.ndarray:
    ident = np.eye(h.shape[0], dtype=complex)
    return (ident - 0.5j * a_step * h) @ np.linalg.inv(
        ident + 0.5j * a_step * h
    )


def alpha(unitary: np.ndarray, obs: np.ndarray) -> np.ndarray:
    return unitary.conj().T @ obs @ unitary


def run_dispersion_checks() -> None:
    print("LIGHT CONE FRAMING: repaired dispersion and cone checks")
    print("Dispersion: E^2 = m^2 + sin^2(k)")
    print("Closed-form maximum: v_max(m) = sqrt(m^2 + 1) - m")
    ks = np.linspace(0.0, math.pi, KGRID_N)

    for m in MASSES:
        vals = v_g(ks, m)
        arg = int(vals.argmax())
        vmax_num = float(vals[arg])
        k_argmax = float(ks[arg])
        vmax_pred = v_max_closed_form(m)
        diff = abs(vmax_num - vmax_pred)

        check(
            "A",
            f"v_max formula matches grid maximum at m={m:g}",
            diff < TOL_VMAX,
            f"diff={diff:.3e}, k={k_argmax:.6f}",
        )
        check(
            "A",
            f"subluminal dispersion at m={m:g}",
            vmax_num <= 1.0 + 1e-12 and (m == 0.0 or vmax_num < 1.0),
            f"vmax={vmax_num:.10f}",
        )
        if m == 0.0:
            v_pi_over_2 = float(v_g(np.array([math.pi / 2]), m)[0])
            check(
                "A",
                "massless maximum is not at k=pi/2",
                k_argmax < math.pi / 2 - 0.1 and v_pi_over_2 < 1e-12,
                f"k_argmax={k_argmax:.6f}, v(pi/2)={v_pi_over_2:.3e}",
            )
        else:
            sin2_num = math.sin(k_argmax) ** 2
            sin2_pred = kstar_sin2_closed_form(m)
            check(
                "A",
                f"maximizer identity sin^2(k*) at m={m:g}",
                abs(sin2_num - sin2_pred) < TOL_KSTAR,
                f"grid={sin2_num:.10f}, pred={sin2_pred:.10f}",
            )

    small_m = 1e-6
    vmax_small = v_max_closed_form(small_m)
    check(
        "A",
        "massless limit v_max -> 1",
        abs(vmax_small - 1.0) < 1e-5,
        f"v_max(1e-6)={vmax_small:.10f}",
    )
    large_m = 100.0
    vmax_large = v_max_closed_form(large_m)
    expected_large = 1.0 / (2.0 * large_m)
    check(
        "A",
        "heavy-mass limit v_max ~ 1/(2m)",
        abs(vmax_large - expected_large) / expected_large < 1e-3,
        f"v_max(100)={vmax_large:.6e}",
    )


def run_source_guards() -> None:
    text = NOTE.read_text()
    required = (
        "Status authority:** independent audit lane only.",
        "TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md",
        "FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md",
        "LIGHT_CONE_CRANK_NICOLSON_LIEB_ROBINSON_BRIDGE_NOTE_2026-05-09.md",
        "sin²(k*) = m·(√(m²+1) − m)",
        "zeta(A) := a_tau ||[H,A]|| y^2/(1 - y^2)",
        "W_mu := sup_x sum_y ||Phi_xy|| exp(mu d_1(x,y))",
    )
    for needle in required:
        check("B", f"source contains required repair text: {needle}", needle in text)

    forbidden = (
        ("J_" + "action <=", "source omits former action-budget inequality"),
        ("v_LR" + "^CN(a", "source omits former CN velocity equation"),
        ("1/(1 " + "- a_tau J/2)", "source omits former CN denominator"),
        ("Neumann-series " + "velocity", "source omits former velocity rationale"),
    )
    for needle, label in forbidden:
        check("B", label, needle not in text)


def run_quasilocal_shell_check() -> None:
    d = 3
    m = 0.3
    a_tau = 1.0
    eta_star = math.asinh(m)
    eta = 0.80 * eta_star
    mu = eta / (2.0 * d)
    beta = eta - d * mu
    c_d = math.sqrt(m * m + (d - 1) + math.cosh(eta) ** 2)
    bound = (c_d / a_tau) * shell_sum_linf(d, beta)

    check(
        "C",
        "weighted-overlap condition 0 < d*mu < eta < arcsinh(m)",
        0.0 < d * mu < eta < eta_star,
        f"d*mu={d * mu:.6f}, eta={eta:.6f}, eta*={eta_star:.6f}",
    )
    check(
        "C",
        "C_d(eta,m) prefactor is finite and positive",
        math.isfinite(c_d) and c_d > 0.0,
        f"C_d={c_d:.8f}",
    )
    check(
        "C",
        "shell-sum W_mu upper bound is finite",
        math.isfinite(bound) and bound > 0.0,
        f"bound={bound:.8f}, beta={beta:.6f}",
    )


def run_cn_inheritance_check() -> None:
    l_sites = 3
    h = (
        0.31 * two_site_op(l_sites, 0, X, 1, X)
        + 0.17 * two_site_op(l_sites, 1, Y, 2, Y)
        + 0.23 * site_op(l_sites, 1, Z)
        + 0.11 * site_op(l_sites, 2, X)
    )
    h = 0.5 * (h + h.conj().T)
    a_step = 0.2
    n_steps = 5
    obs_a = site_op(l_sites, 0, Z)
    obs_b = site_op(l_sites, 2, X)

    u_cn = cayley_forward(h, a_step)
    u_exact = exp_hermitian(h, a_step)
    vals, vecs = np.linalg.eigh(h)
    u_spec = vecs @ np.diag(np.exp(-2j * np.arctan(a_step * vals / 2.0))) @ vecs.conj().T
    backward_step = np.linalg.solve(
        np.eye(h.shape[0], dtype=complex) - 0.5j * a_step * h,
        np.eye(h.shape[0], dtype=complex) + 0.5j * a_step * h,
    )

    check(
        "D",
        "Cayley convention matches exp(-2i arctan(aH/2))",
        op_norm(u_cn - u_spec) < 1e-12,
        f"diff={op_norm(u_cn - u_spec):.3e}",
    )
    check(
        "D",
        "backward solve convention is not used",
        op_norm(u_cn - backward_step) > 1e-2,
        f"forward/backward diff={op_norm(u_cn - backward_step):.3e}",
    )

    h_norm = op_norm(h)
    y = a_step * h_norm / 2.0
    comm_ha = op_norm(comm(h, obs_a))
    zeta = a_step * comm_ha * y**2 / (1.0 - y**2)
    per_step = op_norm(alpha(u_cn, obs_a) - alpha(u_exact, obs_a))
    check(
        "D",
        "subcriticality y=a||H||/2 < 1",
        y < 1.0,
        f"y={y:.6f}",
    )
    check(
        "D",
        "CN per-step defect <= zeta",
        per_step <= zeta + 1e-14,
        f"defect={per_step:.3e}, zeta={zeta:.3e}",
    )

    u_cn_n = np.linalg.matrix_power(u_cn, n_steps)
    u_ex_n = exp_hermitian(h, n_steps * a_step)
    n_step = op_norm(alpha(u_cn_n, obs_a) - alpha(u_ex_n, obs_a))
    check(
        "D",
        "CN n-step defect <= n*zeta",
        n_step <= n_steps * zeta + 1e-14,
        f"defect={n_step:.3e}, n*zeta={n_steps * zeta:.3e}",
    )

    lhs = op_norm(comm(alpha(u_cn_n, obs_a), obs_b))
    rhs = op_norm(comm(alpha(u_ex_n, obs_a), obs_b)) + 2.0 * op_norm(obs_b) * n_steps * zeta
    check(
        "D",
        "CN cone-transfer inequality holds on the small block",
        lhs <= rhs + 1e-14,
        f"lhs={lhs:.3e}, rhs={rhs:.3e}",
    )


def main() -> int:
    run_dispersion_checks()
    run_source_guards()
    run_quasilocal_shell_check()
    run_cn_inheritance_check()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
