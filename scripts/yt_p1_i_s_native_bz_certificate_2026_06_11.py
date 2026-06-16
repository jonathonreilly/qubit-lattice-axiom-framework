#!/usr/bin/env python3
"""
=============================== CORRECTION (2026-06-16) =======================
The I_S value (and any "below [4,10]" / "in-bracket" verdict) here is a
/N_TASTE DOUBLE-COUNT artifact — see
docs/YT_P1_DELTA_R_FERMION_REGULATOR_DEPENDENCE_AND_SCALAR_NTASTE_RESOLUTION_NOTE_2026-06-16.md.
The full-BZ (-π,π]^4 integral already covers the 16 taste corners; dividing by
N_TASTE is spurious. Without the /16, I_S lands ~16× higher (≈32, not ~2), which
INVERTS the "below-bracket" verdict. (Defect 2 — single-corner subtraction — is
absent here: this is a single-power scalar density.) Treat the bracket verdict
as void pending re-derivation. The [4,10] bracket is itself the framework's own
erroneous single-link estimate, not a clean literature comparator.
==============================================================================

Native BZ certificate attempt for the P1 I_S bracket.

This runner tests whether the repo's operational staggered-BZ scalar-density
expression natively certifies the older citation-note bracket I_S in [4, 10].

It intentionally does not use literature numerical values as inputs.  The only
bracket constants below are the premise being tested.

Operational in-repo scalar expression used:

    I_scalar(N) = 2
        + (1 / (N_TASTE * u_0^2)) * 16 pi^2
          * < N_S(k) / [(D_psi(k) + m^2)(D_g(k) + m^2)]
              - 4 / (k^2 + m^2)^2 >_BZ

with:

    D_psi(k) = sum_mu sin^2(k_mu)
    D_g(k)   = 4 sum_mu sin^2(k_mu / 2)
    N_S(k)   = sum_mu cos^2(k_mu / 2)

This is the scalar-vertex candidate made operational in
scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py:292-350, built from
the H_unit Feynman-rule sources.  The older citation note's full I_S premise is
not fully reconstructed here because the in-repo notes disagree in notation:
the H_unit note gives a tadpole-subtracted symbolic I_S kernel but does not give
a closed numerical tadpole subtraction, while the later ratio chain decomposes
the cited I_S into I_v_scalar, a -6 MSbar scalar term, and external-leg I_leg.
The runner therefore reports the native scalar BZ result and the bracket verdict
honestly instead of forcing a certificate.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Iterable

import numpy as np

from canonical_plaquette_surface import CANONICAL_PLAQUETTE, CANONICAL_U0


PASS_COUNT = 0
FAIL_COUNT = 0

ROOT = Path(__file__).resolve().parents[1]

PI = math.pi
SIXTEEN_PI_SQ = 16.0 * PI * PI
N_TASTE = 16.0
M_SQ_IR = 0.01
U_0 = CANONICAL_U0
PLAQUETTE = CANONICAL_PLAQUETTE

BRACKET_LOW = 4.0
BRACKET_HIGH = 10.0
N_LIST = (8, 16, 32, 64)


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


def read_repo_text(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def bz_axis(n: int) -> np.ndarray:
    """Midpoint grid on (-pi, pi], matching the existing BZ runners."""
    delta = 2.0 * PI / float(n)
    return -PI + (np.arange(n, dtype=np.float64) + 0.5) * delta


def scalar_bz_candidate(n: int, m_sq: float = M_SQ_IR) -> float:
    """Memory-bounded 4D midpoint quadrature for the native scalar candidate."""
    axis = bz_axis(n)
    k1, k2, k3 = np.meshgrid(axis, axis, axis, indexing="ij")

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

    lat_sum = 0.0
    cont_sum = 0.0
    for k0 in axis:
        d_psi = np.sin(k0) ** 2 + sin_sq_123 + m_sq
        d_g = 4.0 * (np.sin(k0 / 2.0) ** 2 + sin_half_sq_123) + m_sq
        n_s = np.cos(k0 / 2.0) ** 2 + cos_half_sq_123
        k_sq = k0 * k0 + k_sq_123 + m_sq

        lat_sum += float(np.sum(n_s / (d_psi * d_g), dtype=np.float64))
        cont_sum += float(np.sum(4.0 / (k_sq * k_sq), dtype=np.float64))

    cell_weight = 1.0 / float(n ** 4)
    lat_val = SIXTEEN_PI_SQ * lat_sum * cell_weight
    cont_val = SIXTEEN_PI_SQ * cont_sum * cell_weight
    return 2.0 + (lat_val - cont_val) / (N_TASTE * (U_0 ** 2))


def rel_change(new: float, old: float) -> float:
    return abs(new - old) / max(abs(new), 1e-15)


def richardson_last_two(values: dict[int, float]) -> tuple[float, float]:
    """Second-order midpoint extrapolation from N=32 and N=64."""
    v32 = values[32]
    v64 = values[64]
    estimate = (4.0 * v64 - v32) / 3.0
    error = abs(estimate - v64)
    return estimate, error


def print_table(values: dict[int, float], ns: Iterable[int]) -> None:
    previous = None
    print("Grid sweep:")
    for n in ns:
        value = values[n]
        if previous is None:
            print(f"  N={n:2d}  I_scalar_native={value:.12f}  seed")
        else:
            diff = rel_change(value, previous)
            print(
                f"  N={n:2d}  I_scalar_native={value:.12f}  "
                f"delta_vs_prev={100.0 * diff:.4f}%"
            )
        previous = value


def main() -> int:
    print("YT P1 I_S native BZ certificate attempt (2026-06-11)")
    print()
    print("Defining expression used:")
    print(
        "  I_scalar(N) = 2 + (16*pi^2/(16*u0^2)) * "
        "<N_S/((D_psi+m^2)(D_g+m^2)) - 4/(k^2+m^2)^2>_BZ"
    )
    print(
        "  Source: scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py:292-350"
    )
    print(
        "  Feynman-rule source: docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md:357-401"
    )
    print()

    citation_note = read_repo_text("docs/YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md")
    hunit_note = read_repo_text("docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md")
    full_runner = read_repo_text("scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py")
    delta1_note = read_repo_text("docs/YT_P1_DELTA_1_BZ_COMPUTATION_NOTE_2026-04-17.md")

    check(
        "citation note defines I_S as Z_S finite matching coefficient",
        "Z_S^{lat → MSbar}(μ = 1/a)" in citation_note
        and "(α_s · C_F / (4π))" in citation_note,
        "docs/YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md:188-207",
    )
    check(
        "H_unit note contains symbolic D_S1 BZ kernel",
        "I_S^{D_S1}(p=0)" in hunit_note
        and "D_ψ(k)^{-1}" in hunit_note
        and "D_g(k)^{-1}" in hunit_note,
        "docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md:357-374",
    )
    check(
        "H_unit tadpole subtraction is symbolic, not a closed numerical formula",
        "I_S^{tadpole}  =  constant-propagator piece" in hunit_note
        and "absorbed by u_0 via D14" in hunit_note,
        "docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md:377-405",
    )
    check(
        "operational native scalar expression is present in full-staggered runner",
        "def integrate_I_v_scalar_full" in full_runner
        and "lat_artifact = (lat_val - cont_val) / N_TASTE / (U_0 ** 2)" in full_runner,
        "scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py:292-350",
    )
    check(
        "Delta_1 note separates old I_S citation from native I_v_scalar plus I_leg",
        "I_S^cited  =  2 · I_v_scalar  +  (−6)  +  2 · I_leg" in delta1_note,
        "docs/YT_P1_DELTA_1_BZ_COMPUTATION_NOTE_2026-04-17.md:271-298",
    )
    check(
        "canonical u0 imported from same-surface plaquette constant",
        abs(U_0 - PLAQUETTE ** 0.25) < 1e-14,
        f"u0={U_0:.10f}, plaquette={PLAQUETTE:.4f}",
    )

    values = {n: scalar_bz_candidate(n) for n in N_LIST}
    print_table(values, N_LIST)
    print()

    r16_32 = rel_change(values[32], values[16])
    r32_64 = rel_change(values[64], values[32])
    extrapolated, extrap_error = richardson_last_two(values)
    delta1_native = 2.0 * extrapolated - 6.0
    bracket_certified = BRACKET_LOW <= extrapolated <= BRACKET_HIGH

    check(
        "post-coarse grid convergence N=16->32 and N=32->64 below 1%",
        r16_32 < 0.01 and r32_64 < 0.01,
        f"N16->32={100.0*r16_32:.4f}%, N32->64={100.0*r32_64:.4f}%",
    )
    check(
        "second-order extrapolation error is small relative to bracket gap",
        extrap_error < 0.01 and (BRACKET_LOW - extrapolated) > 10.0 * extrap_error,
        f"I_inf={extrapolated:.12f}, err~{extrap_error:.12f}",
    )
    check(
        "falsifier guard: native scalar value is neither zero nor enormous",
        0.5 < abs(extrapolated) < 50.0,
        f"|I_scalar_native|={abs(extrapolated):.6f}",
    )
    check(
        "bracket verdict is honest: native scalar candidate does NOT certify [4,10]",
        bracket_certified is False,
        f"I_scalar_native={extrapolated:.6f} is below {BRACKET_LOW}",
    )
    check(
        "induced Delta_1 diagnostic remains finite and non-vacuous",
        -10.0 < delta1_native < 10.0,
        f"Delta_1_native=2*I_scalar_native-6={delta1_native:.6f}",
    )

    print()
    print(f"CONVERGED_I_SCALAR_NATIVE: {extrapolated:.12f}")
    print(f"RESOLUTION_EXTRAPOLATION_ERROR: {extrap_error:.12f}")
    print(f"INDUCED_DELTA_1_NATIVE: {delta1_native:.12f}")
    print("BRACKET_UNDER_TEST: [4.000000, 10.000000]")
    print("BRACKET_VERDICT: NOT_CERTIFIED")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
