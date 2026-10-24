#!/usr/bin/env python3
r"""Supplied real Fourier/plane identities and calibrated finite fixtures.
No physical phase selection, Berry holonomy or authority promotion is inferred.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25.md',)

PASSES: list[tuple[str, bool, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    PASSES.append((label, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def main() -> int:
    PASSES.clear()
    for name in AUDIT_INPUT_PATHS:
        if not (ROOT / name).is_file():
            print(f"FAIL: missing declared input {name}")
            return 1
    # ------------------------------------------------------------------------
    # Section 1: Symbolic Plancherel identity inside the Brannen parameterization
    # ------------------------------------------------------------------------
    section("§1. Symbolic identity inside the Brannen parameterization: arg(b) = δ")

    V0, c = sp.symbols("V_0 c", positive=True, real=True)
    delta = sp.symbols("delta", real=True)
    omega = sp.exp(sp.I * 2 * sp.pi / sp.Integer(3))

    sqrt_m = [V0 * (1 + c * sp.cos(delta + 2 * sp.pi * (k - 1) / sp.Integer(3))) for k in (1, 2, 3)]

    a0 = (sqrt_m[0] + sqrt_m[1] + sqrt_m[2]) / sp.sqrt(3)
    b = (sqrt_m[0] + sp.conjugate(omega) * sqrt_m[1] + omega * sqrt_m[2]) / sp.sqrt(3)

    a0_simplified = sp.simplify(sp.trigsimp(a0))
    b_simplified = sp.simplify(sp.trigsimp(b))

    a0_target = sp.sqrt(3) * V0
    b_target = (sp.sqrt(3) / 2) * V0 * c * sp.exp(sp.I * delta)

    check(
        "1.1 Symbolic: a_0 = √3 · V_0 (singlet Plancherel component)",
        sp.simplify(a0_simplified - a0_target) == 0,
        f"a_0   = {a0_simplified}\n"
        f"target = {a0_target}",
    )

    diff = sp.simplify(b_simplified - b_target)
    diff_re = sp.simplify(sp.re(diff))
    diff_im = sp.simplify(sp.im(diff))
    check(
        "1.2 Symbolic: b = (√3/2) · V_0 · c · exp(iδ), so arg(b) = δ (mod 2π)",
        diff_re == 0 and diff_im == 0,
        f"b      = {b_simplified}\n"
        f"target = {b_target}\n"
        f"|Re(diff)| = {diff_re}, |Im(diff)| = {diff_im}",
    )

    delta_num = sp.Rational(2, 9)
    arg_b = sp.atan2(sp.im(b_simplified), sp.re(b_simplified))
    arg_b_at = sp.simplify(arg_b.subs({V0: 1, c: sp.sqrt(2), delta: delta_num}))
    check(
        "1.3 Symbolic eval at V_0=1, c=√2, δ=2/9: arg(b) = 2/9 exactly",
        sp.simplify(arg_b_at - delta_num) == 0,
        f"arg(b) = {arg_b_at}\n"
        f"target  = {delta_num}",
    )

    # ------------------------------------------------------------------------
    # Section 2: PDG numerical signature inside the Brannen parameterization
    # ------------------------------------------------------------------------
    section("§2. PDG numerical signature: arg(b_PDG) ≈ 2/9 rad in first Z_3 sector")

    PDG_masses = [0.51099895e-3, 105.6583745e-3, 1776.86e-3]  # GeV
    PDG_sqrt = sorted([math.sqrt(m) for m in PDG_masses])

    v_PDG = np.array(PDG_sqrt, dtype=float)
    omega_n = np.exp(2j * math.pi / 3)
    a0_PDG = (v_PDG[0] + v_PDG[1] + v_PDG[2]) / math.sqrt(3)
    b_PDG = (v_PDG[0] + np.conj(omega_n) * v_PDG[1] + omega_n * v_PDG[2]) / math.sqrt(3)

    V0_PDG = a0_PDG / math.sqrt(3)
    c_PDG = 2 * abs(b_PDG) / (math.sqrt(3) * V0_PDG)
    delta_PDG = math.atan2(b_PDG.imag, b_PDG.real)
    delta_PDG_mod = abs(((delta_PDG + math.pi) % (2 * math.pi / 3)) - math.pi / 3)

    check(
        "2.1 Calibrated mass-triple c is within the stated tolerance of √2",
        abs(c_PDG - math.sqrt(2)) < 1e-2,
        f"c_PDG = {c_PDG:.6f}, √2 = {math.sqrt(2):.6f}",
    )

    check(
        "2.2 Folded phase of the supplied mass triple is near 2/9 under this convention",
        abs(delta_PDG_mod - 2 / 9) < 5e-3,
        f"|arg(b)|        = {delta_PDG_mod:.6f} rad\n"
        f"2/9             = {2/9:.6f} rad   (matches data)\n"
        f"4π/9 (χ-lift)   = {4*math.pi/9:.6f} rad   (does not match)",
    )

    delta_use = 2 / 9
    brannen_recon = sorted([
        V0_PDG * (1 + c_PDG * math.cos(delta_use + 2 * math.pi * j / 3))
        for j in range(3)
    ])
    rel_err = max(abs(brannen_recon[i] - PDG_sqrt[i]) / PDG_sqrt[i] for i in range(3))
    check(
        "2.3 Calibrated V0,c reconstruction with supplied δ=2/9 meets 0.1% fixture tolerance",
        rel_err < 1e-3,
        f"max rel err = {rel_err * 100:.5f}%\n"
        f"recon: {brannen_recon}\n"
        f"PDG:   {PDG_sqrt}",
    )

    delta_canonical = 4 * math.pi / 9
    brannen_canon = [
        V0_PDG * (1 + c_PDG * math.cos(delta_canonical + 2 * math.pi * j / 3))
        for j in range(3)
    ]
    canon_negative = any(b < 0 for b in brannen_canon)
    check(
        "2.4 Supplied δ=4π/9 fixture has a negative amplitude with these calibrated parameters",
        canon_negative,
        f"χ-lift recon: {brannen_canon}  [negative: not a positive square-root-amplitude instance]",
    )

    # ------------------------------------------------------------------------
    # Section 3: Numerical witness on the supplied selected line (cross-check)
    # ------------------------------------------------------------------------
    section("§3. Self-contained supplied chart fixture: α(m_*) − α(m_0) = −2/9 at 1e-12")

    GAMMA = 0.5
    E1 = math.sqrt(8.0 / 3.0)
    E2 = math.sqrt(8.0) / 3.0
    SELECTOR = math.sqrt(6.0) / 3.0

    T_M = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    T_DELTA = np.array([[0, -1, 1], [-1, 1, 0], [1, 0, -1]], dtype=complex)
    T_Q = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=complex)
    H_BASE = np.array(
        [[0, E1, -E1 - 1j * GAMMA], [E1, 0, -E2], [-E1 + 1j * GAMMA, -E2, 0]],
        dtype=complex,
    )

    def H_sel(m: float) -> np.ndarray:
        return H_BASE + m * T_M + SELECTOR * (T_DELTA + T_Q)

    singlet = np.ones(3) / math.sqrt(3)
    e1_perp = np.array([1, -1, 0]) / math.sqrt(2)
    e2_perp = np.array([1, 1, -2]) / math.sqrt(6)

    def perp_rotation_angle(m: float) -> float:
        x = expm(H_sel(m))
        v_22 = float(np.real(x[2, 2]))
        v_11 = float(np.real(x[1, 1]))
        rad = math.sqrt(3 * (v_22 * v_22 + 4 * v_22 * v_11 + v_11 * v_11))
        u_val = 2 * (v_22 + v_11) - rad
        s = np.array([u_val, v_22, v_11], dtype=float)
        s /= np.linalg.norm(s)
        s_perp = s - np.dot(s, singlet) * singlet
        p1 = float(np.dot(s_perp, e1_perp))
        p2 = float(np.dot(s_perp, e2_perp))
        return math.atan2(p2, p1)

    m_0 = -0.265815998702
    m_star = -1.160443440065

    ang_m0 = perp_rotation_angle(m_0)
    ang_mstar = perp_rotation_angle(m_star)

    check(
        "3.1 Supplied hard-coded coordinate witness: α(m_*) − α(m_0) = −2/9 (1e-12)",
        abs((ang_mstar - ang_m0) + 2 / 9) < 1e-12,
        f"α(m_*) − α(m_0) = {ang_mstar - ang_m0:.15f}\n"
        f"target          = {-2/9:.15f}\n"
        f"|diff|          = {abs((ang_mstar - ang_m0) + 2/9):.3e}\n"
        f"NOTE: hard-coded m_*; this is a numerical witness on supplied fixture data,\n"
        f"      not an analytic derivation of the value 2/9 from H_sel dynamics.",
    )

    # ------------------------------------------------------------------------
    # Section 4: Plancherel arg(b) ↔ perp rotation α basis-change consistency
    # ------------------------------------------------------------------------
    section("§4. Plancherel arg(b) ↔ perp rotation α basis-change consistency")

    def arg_b_on_selected_line(m: float) -> float:
        x = expm(H_sel(m))
        v_22 = float(np.real(x[2, 2]))
        v_11 = float(np.real(x[1, 1]))
        rad = math.sqrt(3 * (v_22 * v_22 + 4 * v_22 * v_11 + v_11 * v_11))
        u_val = 2 * (v_22 + v_11) - rad
        sqrt_m_vec = np.array([u_val, v_22, v_11], dtype=float)
        sqrt_m_vec /= np.linalg.norm(sqrt_m_vec)
        b_val = (
            sqrt_m_vec[0]
            + np.conj(omega_n) * sqrt_m_vec[1]
            + omega_n * sqrt_m_vec[2]
        ) / math.sqrt(3)
        return math.atan2(b_val.imag, b_val.real)

    arg_b_m0 = arg_b_on_selected_line(m_0)
    arg_b_mstar = arg_b_on_selected_line(m_star)

    diff_perp = ang_mstar - ang_m0
    diff_arg_b = arg_b_mstar - arg_b_m0

    def wrap(x: float) -> float:
        return math.atan2(math.sin(x), math.cos(x))

    diff_perp_w = wrap(diff_perp)
    diff_arg_b_w = wrap(diff_arg_b)

    matches_pos = abs(diff_perp_w - diff_arg_b_w) < 1e-10
    matches_neg = abs(diff_perp_w + diff_arg_b_w) < 1e-10

    check(
        "4.1 arg(b)-difference equals perp-rotation-difference up to sign",
        matches_pos or matches_neg,
        f"perp Δα   = {diff_perp_w:.15f}\n"
        f"arg(b) Δα = {diff_arg_b_w:.15f}\n"
        f"sum  = {diff_perp_w + diff_arg_b_w:.3e}, diff = {diff_perp_w - diff_arg_b_w:.3e}",
    )

    check(
        "4.2 |arg(b)(m_*) − arg(b)(m_0)| = 2/9 rad (Plancherel-side numerical witness)",
        abs(abs(diff_arg_b_w) - 2 / 9) < 1e-12,
        f"|arg(b)-difference| = {abs(diff_arg_b_w):.15f}\n"
        f"target               = {2/9:.15f} rad",
    )

    # Exact convention-specific plane identity, independently expanded.
    x0, x1, x2 = sp.symbols("x0 x1 x2", real=True)
    p1 = (x0-x1)/sp.sqrt(2)
    p2 = (x0+x1-2*x2)/sp.sqrt(6)
    b_plane = ((x0-(x1+x2)/2)+sp.I*sp.sqrt(3)*(x2-x1)/2)/sp.sqrt(3)
    phase_factor = sp.sqrt(3)/2 + sp.I/2
    check("5.1 Exact plane convention b=exp(i*pi/6)(p1-i*p2)/sqrt(2)",
          sp.simplify(b_plane-phase_factor*(p1-sp.I*p2)/sp.sqrt(2)) == 0)
    check("5.2 Specified orientation gives opposite wrapped angle differences", matches_neg)
    section("Scope")
    print("Fourier phase is a coordinate modulo2pi; component positivity is a separate premise.")
    print("Mass values, chart and m witnesses are supplied/calibrated, not predictions.")
    print("Coordinate angle differences are not invariant Berry holonomy.")
    print("The old Berry-promotion instruction is withdrawn; physical observable and dynamics remain open.")

    # ------------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------------
    section("Summary")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    n_fail = n_total - n_pass
    print(f"PASSED: {n_pass}/{n_total}")
    for label, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")

    print()
    print("Scope: conditional Fourier/plane identities and finite supplied fixtures only.")

    if n_fail == 0:
        print()
        print("VERDICT: support-grade algebraic identity + numerical witness verified.")
        print("  arg(b) = δ inside the Brannen parameterization (sympy-exact).")
        print("  Calibrated fixture comparison does not select a physical phase.")
        print("  Numerical 2/9 on supplied selected line (geometry-runner cross-check).")
        print("  No physical or audit closure follows from these checks.")
        return 0
    else:
        print()
        print(f"VERDICT: support claims not all verified — {n_fail} FAIL.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
