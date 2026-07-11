#!/usr/bin/env python3
"""
YT P1 - H_unit 1-loop: framework-native infrared-obstruction certificate.

What this runner is
-------------------
The composite-scalar ``H_unit`` 1-loop ``C_F``-channel reduces to a single
gluon-sandwich stand-in whose zero-external-momentum scalar kernel is
infrared-divergent at the Brillouin-zone origin. This runner probes the
displayed, normalization-stripped kernel

    K(k) = N_S(k) / ( D_psi(k)**2 * D_g(k) )

directly and certifies the origin obstruction through *structural constants
of the kernel itself* (a power, a ratio, a projector value). It compares to
**no** external numerical target: there is no coupling, no plaquette
average, no mean-link, no color factor, and no framework module imported
here. Each gate ships with an explicit wrong-kernel negative control and
passes only because the true kernel gives the structural constant while the
control gives a different value.

The paired note
    docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md
withdraws the earlier finite "envelope" claim; this runner makes no
finite-value claim about the divergent integral. An honest computed value
that lands on a structural constant (-6, 64, 4, growth exponent 2, 4*pi**2,
projector 4 vs 2) is the result.

Kernel (lattice units, a = 1; mu, rho run over 1..4)
----------------------------------------------------
    D_psi(k) = sum_mu sin(k_mu)**2          # staggered fermion  -> |k|**2
    D_g(k)   = 4 * sum_rho sin(k_rho/2)**2  # Wilson gluon       -> |k|**2
    N_S(k)   = sum_mu cos(k_mu/2)**2        # scalar numerator   -> 4
    K(k)     = N_S(k) / (D_psi(k)**2 * D_g(k))   # -> 4 / |k|**6 as k -> 0

Self-contained: standard library (math, pathlib, sys) + numpy.
"""

from __future__ import annotations

import itertools
import math
from pathlib import Path

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, observed: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        verdict = "PASS"
    else:
        FAIL_COUNT += 1
        verdict = "FAIL"
    line = f"  {verdict} {name}"
    if observed:
        line += f"  |  {observed}"
    print(line)
    return condition


# ----------------------------------------------------------------------
# Kernel and its wrong-kernel controls
# ----------------------------------------------------------------------
def d_psi(k: np.ndarray) -> float:
    return float(np.sum(np.sin(k) ** 2))


def d_g(k: np.ndarray) -> float:
    return 4.0 * float(np.sum(np.sin(k / 2.0) ** 2))


def n_s(k: np.ndarray) -> float:
    return float(np.sum(np.cos(k / 2.0) ** 2))


def kernel(k: np.ndarray) -> float:
    """True displayed kernel: N_S / (D_psi**2 * D_g) -> 4 / |k|**6."""
    return n_s(k) / (d_psi(k) ** 2 * d_g(k))


def kernel_soft(k: np.ndarray) -> float:
    """Control: one fewer propagator power, N_S / (D_psi * D_g) -> 4 / |k|**4."""
    return n_s(k) / (d_psi(k) * d_g(k))


def kernel_unit_numerator(k: np.ndarray) -> float:
    """Control: N_S replaced by the constant 1 -> 1 / |k|**6."""
    return 1.0 / (d_psi(k) ** 2 * d_g(k))


def kernel_mass_reg(k: np.ndarray, m2: float = 1e-2) -> float:
    """Control: massive regulator gives a finite origin value (no divergence)."""
    return n_s(k) / ((d_psi(k) + m2) ** 2 * (d_g(k) + m2))


# ----------------------------------------------------------------------
# Ray and S^3 angular set
# ----------------------------------------------------------------------
QHAT = np.array([1.0, 2.0, 3.0, 4.0])
QHAT /= np.linalg.norm(QHAT)  # unit ray, generic (off every symmetry axis)


def sphere_nodes() -> np.ndarray:
    """48 unit vectors on S^3, hyperoctahedrally symmetric, equal weight.

    8  : sign/position perms of (+-1, 0, 0, 0)
    16 : (+-1, +-1, +-1, +-1) / 2
    24 : 2-of-4 position choices of (+-1, +-1, 0, 0) / sqrt(2)
    The leading kernel term is isotropic, so the equal-weight average over
    this symmetric set is exact at leading order and its symmetry cancels the
    low-order anisotropy.
    """
    nodes = []
    for axis in range(4):
        for sign in (1.0, -1.0):
            v = np.zeros(4)
            v[axis] = sign
            nodes.append(v)
    for signs in itertools.product((1.0, -1.0), repeat=4):
        nodes.append(np.array(signs) / 2.0)
    for i, j in itertools.combinations(range(4), 2):
        for si in (1.0, -1.0):
            for sj in (1.0, -1.0):
                v = np.zeros(4)
                v[i] = si
                v[j] = sj
                nodes.append(v / math.sqrt(2.0))
    return np.array(nodes)


NODES = sphere_nodes()
SOLID_ANGLE_S3 = 2.0 * math.pi ** 2  # |S^3|


def sphere_avg(f, r: float) -> float:
    return float(np.mean([f(r * node) for node in NODES]))


# ----------------------------------------------------------------------
# Gate 1 - ray log-log slope -> -6
# ----------------------------------------------------------------------
def gate_ray_slope() -> None:
    rs = [1e-2 * 2.0 ** (-j) for j in range(11)]

    def slope(f):
        a, b = rs[-2], rs[-1]
        return (math.log(f(b * QHAT)) - math.log(f(a * QHAT))) / (
            math.log(b) - math.log(a)
        )

    s_true = slope(kernel)
    s_soft = slope(kernel_soft)
    ok = abs(s_true - (-6.0)) < 5e-3 and abs(s_soft - (-4.0)) < 5e-3
    check(
        "IR_RAY_LOG_SLOPE_MINUS_SIX",
        ok,
        f"slope_true={s_true:+.6f} (target -6)  slope_soft={s_soft:+.6f} (control -4)",
    )


# ----------------------------------------------------------------------
# Gate 2 - halving factor K(r/2)/K(r) -> 64
# ----------------------------------------------------------------------
def gate_halving_factor() -> None:
    r = 1e-2 * 2.0 ** (-9)

    def ratio(f):
        return f((r / 2.0) * QHAT) / f(r * QHAT)

    ratio_true = ratio(kernel)
    ratio_soft = ratio(kernel_soft)
    ok = abs(ratio_true - 64.0) < 1e-2 and abs(ratio_soft - 16.0) < 1e-2
    check(
        "IR_RAY_HALVING_FACTOR_64",
        ok,
        f"ratio_true={ratio_true:.6f} (target 64)  ratio_soft={ratio_soft:.6f} (control 16)",
    )


# ----------------------------------------------------------------------
# Gate 3 - leading coefficient r^6 K -> 4, O(r^2) contraction
# ----------------------------------------------------------------------
def gate_leading_coefficient() -> None:
    rs = [1e-2 * 2.0 ** (-j) for j in range(11)]
    c = [rs[j] ** 6 * kernel(rs[j] * QHAT) for j in range(len(rs))]
    c_unit = rs[-1] ** 6 * kernel_unit_numerator(rs[-1] * QHAT)
    dev = [abs(cj - 4.0) for cj in c]
    contraction = dev[-1] / dev[-2]  # -> (1/2)^2 = 0.25
    ok = (
        abs(c[-1] - 4.0) < 1e-4
        and 0.20 <= contraction <= 0.30
        and abs(c_unit - 1.0) < 1e-4
        and abs(c_unit - 4.0) > 1.0
    )
    check(
        "IR_LEADING_COEFFICIENT_FOUR",
        ok,
        f"c_last={c[-1]:.8f} (target 4)  contraction={contraction:.4f} (target 0.25)  "
        f"unit_num_c={c_unit:.8f} (control 1)",
    )


# ----------------------------------------------------------------------
# Gate 4 - origin-ball integral grows quadratically; eps^2 J -> 4 pi^2
# ----------------------------------------------------------------------
def _origin_ball_integral(f, eps: float, cap: float, n_gl: int = 96) -> float:
    """J(eps;R) = |S^3| * int_eps^R r^3 sphere_avg(f,r) dr, Gauss-Legendre in log r."""
    x, w = np.polynomial.legendre.leggauss(n_gl)
    a, b = math.log(eps), math.log(cap)
    t = 0.5 * (b - a) * x + 0.5 * (a + b)
    wt = 0.5 * (b - a) * w
    vals = np.array([math.exp(4.0 * ti) * sphere_avg(f, math.exp(ti)) for ti in t])
    return SOLID_ANGLE_S3 * float(np.sum(wt * vals))


def gate_quadratic_growth() -> None:
    cap = 0.25  # R = 1/4
    eps = cap * 2.0 ** (-8)

    def exponent(f):
        return math.log(
            _origin_ball_integral(f, eps / 2.0, cap) / _origin_ball_integral(f, eps, cap)
        ) / math.log(2.0)

    exp_true = exponent(kernel)
    exp_soft = exponent(kernel_soft)
    eps2_j = eps ** 2 * _origin_ball_integral(kernel, eps, cap)
    four_pi2 = 4.0 * math.pi ** 2
    ok = (
        abs(exp_true - 2.0) < 5e-2
        and abs(eps2_j - four_pi2) < 0.2
        and exp_soft < 0.6  # log-divergent control: sub-quadratic, not -> 2
    )
    check(
        "FOUR_D_PARTIAL_INTEGRAL_QUADRATIC_GROWTH",
        ok,
        f"exp_true={exp_true:.4f} (target 2)  eps^2*J={eps2_j:.4f} (target 4pi^2={four_pi2:.4f})  "
        f"exp_soft={exp_soft:.4f} (control ->0)",
    )


# ----------------------------------------------------------------------
# Gate 5 - shell max diverges: no finite max x volume envelope
# ----------------------------------------------------------------------
def gate_no_finite_envelope() -> None:
    rms = [1e-2 * 2.0 ** (-m) for m in range(1, 9)]

    def shell_max(f):
        return [max(f(r * node) for node in NODES) for r in rms]

    s_true = shell_max(kernel)
    s_reg = shell_max(kernel_mass_reg)
    halving_true = s_true[-1] / s_true[-2]  # -> 64 (diverges)
    halving_reg = s_reg[-1] / s_reg[-2]  # -> 1  (bounded plateau)
    r6s_true = rms[-1] ** 6 * s_true[-1]  # -> 4
    r6s_reg = rms[-1] ** 6 * s_reg[-1]  # -> 0
    ok = (
        abs(halving_true - 64.0) < 1e-2
        and abs(r6s_true - 4.0) < 1e-2
        and abs(halving_reg - 1.0) < 0.5
        and r6s_reg < 1e-6
    )
    check(
        "NO_FINITE_MAX_TIMES_VOLUME_ENVELOPE",
        ok,
        f"halving_true={halving_true:.4f} (->64, diverges)  r^6*S_true={r6s_true:.6f} (->4)  |  "
        f"reg halving={halving_reg:.6f} (->1, bounded)  r^6*S_reg={r6s_reg:.3g} (->0)",
    )


# ----------------------------------------------------------------------
# Gate 6 - external-leg Z_q required and omitted (structural note contract)
# ----------------------------------------------------------------------
def gate_external_leg_zq() -> None:
    note_path = (
        Path(__file__).resolve().parent.parent
        / "docs"
        / "YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md"
    )
    text = note_path.read_text(encoding="utf-8")

    # The displayed D_S1 kernel block must exclude the external leg.
    fenced = [seg for seg in text.split("```") if "I_S^{D_S1}(p=0)" in seg]
    displayed_kernel_has_no_zq = len(fenced) == 1 and "Z_q" not in fenced[0]

    conditions = {
        "external-leg Z_q named": "external-leg Z_q" in text,
        "omission stated": "currently omitted" in text,
        "displayed kernel excludes Z_q": displayed_kernel_has_no_zq,
        "Z_q discussed in assembly": text.count("Z_q") >= 1,
    }
    ok = all(conditions.values())
    check(
        "EXTERNAL_LEG_ZQ_REQUIRED_AND_OMITTED",
        ok,
        "  ".join(f"{k}={v}" for k, v in conditions.items())
        + f"  (Z_q count={text.count('Z_q')})",
    )


# ----------------------------------------------------------------------
# Gate 7 - tadpole constant-piece projector is scheme-dependent
# ----------------------------------------------------------------------
def _bz_axis_average(f_axis, n: int = 512) -> float:
    grid = np.linspace(-math.pi, math.pi, n, endpoint=False)
    return float(np.mean(f_axis(grid)))


def gate_tadpole_scheme_dependence() -> None:
    # True numerator N_S(k) = sum_mu cos^2(k_mu/2), separable over axes.
    p_soft = n_s(np.zeros(4))  # point/soft projector at k = 0 -> 4
    p_bz = 4.0 * _bz_axis_average(lambda g: np.cos(g / 2.0) ** 2)  # <N_S>_BZ -> 2

    # Control: genuinely constant numerator (== 1) is scheme-independent.
    p_soft_ctrl = 1.0
    p_bz_ctrl = 4.0 * _bz_axis_average(lambda g: np.full_like(g, 0.25))  # 4 * 1/4 = 1

    ok = (
        abs(p_soft - 4.0) < 1e-6
        and abs(p_bz - 2.0) < 1e-6
        and abs(p_soft - p_bz) > 1.0
        and abs(p_soft_ctrl - p_bz_ctrl) < 1e-6
    )
    check(
        "TADPOLE_COEFFICIENT_IS_SCHEME_DEPENDENT",
        ok,
        f"P_soft={p_soft:.4f} (target 4)  P_BZ={p_bz:.4f} (target 2)  |P_soft-P_BZ|={abs(p_soft - p_bz):.4f}  |  "
        f"const-numerator control: P_soft={p_soft_ctrl:.4f}=P_BZ={p_bz_ctrl:.4f}",
    )


# ----------------------------------------------------------------------
def main() -> int:
    print("=" * 72)
    print("YT P1 H_unit 1-loop: framework-native infrared-obstruction certificate")
    print("  kernel K(k) = N_S(k) / (D_psi(k)^2 * D_g(k)) ; probed vs NO external target")
    print("=" * 72)
    print()
    gate_ray_slope()
    gate_halving_factor()
    gate_leading_coefficient()
    gate_quadratic_growth()
    gate_no_finite_envelope()
    gate_external_leg_zq()
    gate_tadpole_scheme_dependence()
    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
