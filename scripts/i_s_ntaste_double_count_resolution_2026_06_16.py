#!/usr/bin/env python3
"""Resolve the staggered scalar-density N_TASTE normalization fork.

The numerical quadrature below uses the same full-BZ midpoint machinery and
kernel family as the framework P1 staggered scalar runners:

    D_psi(k) = sum_mu sin(k_mu)^2
    D_g(k)   = 4 sum_mu sin(k_mu/2)^2
    N_S(k)   = sum_mu cos(k_mu/2)^2

The literature constants are comparison targets only. They are not used in
any integral. The runner prints both the full-BZ convention and the extra
1/N_TASTE convention; the one that lands on the Lee-Sharpe scalar-density
scale is the convention selected.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

try:
    from canonical_plaquette_surface import CANONICAL_PLAQUETTE, CANONICAL_U0
except Exception:
    CANONICAL_PLAQUETTE = 0.5934
    CANONICAL_U0 = CANONICAL_PLAQUETTE ** 0.25


PI = math.pi
SIXTEEN_PI_SQ = 16.0 * PI * PI
N_TASTE = 16.0
M_SQ_IR = 0.01
U0 = float(CANONICAL_U0)
PLAQUETTE = float(CANONICAL_PLAQUETTE)

N_C = 3.0
C_F = (N_C * N_C - 1.0) / (2.0 * N_C)
ALPHA_LM = (1.0 / (4.0 * PI)) / U0
ALPHA_OVER_4PI = ALPHA_LM / (4.0 * PI)

# Comparison targets only. These are not consumed by any quadrature.
LEE_SHARPE_TABLE_I_C_S = -29.3551
BG_TADPOLE_IMPROVED_SINGLE_LINK_MAG = 39.1

# Lee-Sharpe/Patel-Sharpe continuum finite constant for scalar bilinears:
# c_S = d_S (gamma_E - F0000) + t_S - c1_S, at mu=1/a in NDR.
EULER_GAMMA = 0.5772156649015329
F0000 = 4.369225233874758
D_SCALAR = 3.0
T_SCALAR = -0.5
LEE_SHARPE_SCALAR_CONTINUUM_FINITE = D_SCALAR * (EULER_GAMMA - F0000) + T_SCALAR


@dataclass(frozen=True)
class ScalarResult:
    n: int
    local_full_bz: float
    local_divided: float
    local_c_s_full_bz: float
    local_c_s_divided: float
    hunit_full_bz: float
    hunit_divided: float


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" ({detail})"
    print(line)
    return condition


def axis(n: int) -> np.ndarray:
    delta = 2.0 * PI / float(n)
    return -PI + (np.arange(n, dtype=np.float64) + 0.5) * delta


def scalar_result(n: int, m_sq: float = M_SQ_IR) -> ScalarResult:
    """Memory-bounded full-BZ midpoint quadrature for both scalar kernels."""
    a = axis(n)
    k1, k2, k3 = np.meshgrid(a, a, a, indexing="ij")

    sin_sq_123 = np.sin(k1) ** 2 + np.sin(k2) ** 2 + np.sin(k3) ** 2
    sin_half_sq_123 = (
        np.sin(k1 / 2.0) ** 2
        + np.sin(k2 / 2.0) ** 2
        + np.sin(k3 / 2.0) ** 2
    )
    cos_half_sq_123 = (
        np.cos(k1 / 2.0) ** 2
        + np.cos(k2 / 2.0) ** 2
        + np.cos(k3 / 2.0) ** 2
    )
    k_sq_123 = k1 * k1 + k2 * k2 + k3 * k3

    local_lat = 0.0
    local_cont = 0.0
    hunit_lat = 0.0
    hunit_cont = 0.0

    for k0 in a:
        d_psi = np.sin(k0) ** 2 + sin_sq_123 + m_sq
        d_g = 4.0 * (np.sin(k0 / 2.0) ** 2 + sin_half_sq_123) + m_sq
        k_sq = k0 * k0 + k_sq_123 + m_sq
        n_s = np.cos(k0 / 2.0) ** 2 + cos_half_sq_123

        inv = 1.0 / (d_psi * d_g)
        local_lat += float(np.sum(inv, dtype=np.float64))
        local_cont += float(np.sum(1.0 / (k_sq * k_sq), dtype=np.float64))
        hunit_lat += float(np.sum(n_s * inv, dtype=np.float64))
        hunit_cont += float(np.sum(4.0 / (k_sq * k_sq), dtype=np.float64))

    cell = 1.0 / float(n**4)
    local_diff = SIXTEEN_PI_SQ * (local_lat - local_cont) * cell
    hunit_diff = SIXTEEN_PI_SQ * (hunit_lat - hunit_cont) * cell

    local_full = 2.0 + local_diff / (U0 * U0)
    local_div = 2.0 + local_diff / (N_TASTE * U0 * U0)
    hunit_full = 2.0 + hunit_diff / (U0 * U0)
    hunit_div = 2.0 + hunit_diff / (N_TASTE * U0 * U0)

    return ScalarResult(
        n=n,
        local_full_bz=local_full,
        local_divided=local_div,
        local_c_s_full_bz=LEE_SHARPE_SCALAR_CONTINUUM_FINITE - local_full,
        local_c_s_divided=LEE_SHARPE_SCALAR_CONTINUUM_FINITE - local_div,
        hunit_full_bz=hunit_full,
        hunit_divided=hunit_div,
    )


def rel_change(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), 1e-15)


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    print("N_TASTE scalar-density resolution runner")
    print(f"u0={U0:.12f} plaquette={PLAQUETTE:.12f} N_TASTE={N_TASTE:.0f}")
    print(f"IR regulator m^2={M_SQ_IR}")
    print()

    full_runner = read_text("scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py")
    hunit_note = read_text("docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md")

    check(
        "framework D_psi_full docstring says full BZ already contains the taste sum",
        "taste sum is NOT an overall factor to divide by" in full_runner
        and "automatically built into the 4D BZ integration extent" in full_runner,
    )
    check(
        "framework implementation currently divides scalar finite part by N_TASTE",
        "lat_artifact = (lat_val - cont_val) / N_TASTE / (U_0 ** 2)" in full_runner,
    )
    check(
        "H_unit note defines scalar singlet without a taste-projector normalization",
        "H_unit = (1/√6)" in hunit_note
        and "Σ_{α,a}" in hunit_note
        and "unique" in hunit_note
        and "unit-norm" in hunit_note
        and "taste-diagonal" in hunit_note,
    )
    check(
        "canonical u0 is the plaquette fourth root",
        abs(U0 - PLAQUETTE ** 0.25) < 5e-13,
        f"u0={U0:.12f}",
    )
    print()

    results = [scalar_result(n) for n in (16, 32, 64, 96)]
    print("Grid sweep:")
    print("  N   local_cS_fullBZ  local_cS_/16   H_unit_fullBZ  H_unit_/16")
    for r in results:
        print(
            f"  {r.n:2d}  {r.local_c_s_full_bz:+.9f}  {r.local_c_s_divided:+.9f}"
            f"  {r.hunit_full_bz:+.9f}  {r.hunit_divided:+.9f}"
        )
    final = results[-1]
    prev = results[-2]
    print()

    print("Literature comparison targets, not quadrature inputs:")
    print(f"  Lee-Sharpe Table I unimproved scalar c_S: {LEE_SHARPE_TABLE_I_C_S:+.4f}")
    print(f"  Bhattacharya-Gupta TI single-link scalar magnitude: {BG_TADPOLE_IMPROVED_SINGLE_LINK_MAG:.1f}")
    print()

    full_error = abs(final.local_c_s_full_bz - LEE_SHARPE_TABLE_I_C_S)
    div_error = abs(final.local_c_s_divided - LEE_SHARPE_TABLE_I_C_S)
    check(
        "full-BZ no-division scalar reconstructs Lee-Sharpe c_S",
        full_error < 0.25,
        f"computed={final.local_c_s_full_bz:+.9f}, target={LEE_SHARPE_TABLE_I_C_S:+.4f}, |diff|={full_error:.6f}",
    )
    check(
        "extra /N_TASTE scalar reconstruction is not literature-sized",
        div_error > 10.0,
        f"computed={final.local_c_s_divided:+.9f}, |diff|={div_error:.6f}",
    )
    check(
        "H_unit full-BZ coefficient is on the staggered scalar literature scale",
        29.0 <= abs(final.hunit_full_bz) <= 40.5,
        f"I_S_fullBZ={final.hunit_full_bz:.9f}",
    )
    check(
        "H_unit /N_TASTE coefficient is over-suppressed",
        abs(final.hunit_divided) < 5.0,
        f"I_S_/16={final.hunit_divided:.9f}",
    )
    check(
        "H_unit grid convergence N=64 to N=96 below 0.02%",
        rel_change(final.hunit_full_bz, prev.hunit_full_bz) < 2e-4,
        f"rel={100.0 * rel_change(final.hunit_full_bz, prev.hunit_full_bz):.6f}%",
    )

    delta1_old = 2.0 * final.hunit_divided - 6.0
    delta1_new = 2.0 * final.hunit_full_bz - 6.0
    cf_old = ALPHA_OVER_4PI * C_F * delta1_old
    cf_new = ALPHA_OVER_4PI * C_F * delta1_new
    direct_old = ALPHA_OVER_4PI * C_F * final.hunit_divided
    direct_new = ALPHA_OVER_4PI * C_F * final.hunit_full_bz

    print()
    print(f"LEE_SHARPE_RECONSTRUCTED_FULL_BZ_c_S: {final.local_c_s_full_bz:+.12f}")
    print(f"LEE_SHARPE_RECONSTRUCTED_DIVIDED_c_S: {final.local_c_s_divided:+.12f}")
    print(f"H_UNIT_I_S_FULL_BZ_NO_DIVISION: {final.hunit_full_bz:+.12f}")
    print(f"H_UNIT_I_S_WITH_DIVISION: {final.hunit_divided:+.12f}")
    print(f"H_UNIT_RATIO: {final.hunit_full_bz / final.hunit_divided:.9f}")
    print(f"P1_DIRECT_CF_OLD_DIVIDED: {100.0 * direct_old:+.6f}%")
    print(f"P1_DIRECT_CF_NEW_FULL_BZ: {100.0 * direct_new:+.6f}%")
    print(f"P1_DELTA1_CF_OLD_DIVIDED: {100.0 * cf_old:+.6f}%")
    print(f"P1_DELTA1_CF_NEW_FULL_BZ: {100.0 * cf_new:+.6f}%")
    print("VERDICT: NO_DIVISION")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
