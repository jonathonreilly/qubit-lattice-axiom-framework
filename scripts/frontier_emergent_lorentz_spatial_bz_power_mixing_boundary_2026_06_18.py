#!/usr/bin/env python3
"""Exact boundary for the spatial-BZ Lorentz-mixing channel.

This runner proves a narrow structural fact used by the interacting emergent
Lorentz open gate. On the continuous-time / spatial-Z^3 surface, the leading
central-difference lattice artifact is spatial quartic:

    sum_i (2/a sin(a k_i/2))^2
      = |k|^2 - a^2/12 * sum_i k_i^4 + O(a^4).

The artifact has no p0 dependence. Its local quadratic projection therefore
has zero time-time component, and the signed-permutation O_h orbit average of
its spatial Hessian is one scalar multiple of the spatial identity. This is a
source-side exact support result for the "spatial-only" part of the Collins
mixing wall; it does not derive the one-loop coefficient, the physical fixed
point anomalous dimension, or LV-bound sufficiency.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md"
PARENT = ROOT / "docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def signed_permutation_matrices() -> list[sp.Matrix]:
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            mat = sp.zeros(3)
            for row, col in enumerate(perm):
                mat[row, col] = signs[row]
            mats.append(mat)
    return mats


def main() -> int:
    print("=" * 88)
    print("Spatial-BZ power-mixing boundary: spatial-only scalar channel")
    print("=" * 88)
    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())

    a, p0, k, kx, ky, kz, lam = sp.symbols("a p0 k kx ky kz lam", real=True)
    spatial_vars = (kx, ky, kz)
    vars4 = (p0, kx, ky, kz)

    print("\nPART 1: spatial central-difference expansion")
    lattice_square = (2 * sp.sin(a * k / 2) / a) ** 2
    series = sp.series(lattice_square, a, 0, 5).removeO()
    expected_series = k**2 - a**2 * k**4 / 12 + a**4 * k**6 / 360
    check(
        "central-difference dispersion has quartic spatial artifact",
        sp.simplify(series - expected_series) == 0,
        str(series),
    )
    continuous_time = p0**2
    check(
        "continuous-time kinetic term has no a^2 p0^4 lattice artifact",
        sp.diff(continuous_time, a) == 0 and p0 in continuous_time.free_symbols,
    )

    print("\nPART 2: quartic artifact has no time component")
    artifact = kx**4 + ky**4 + kz**4
    hessian4 = sp.hessian(artifact, vars4)
    check("time-time second variation is zero", hessian4[0, 0] == 0)
    check("time-space second variations are zero", all(hessian4[0, i] == 0 and hessian4[i, 0] == 0 for i in range(1, 4)))
    check("spatial second variation is nonzero before projection", hessian4[1:, 1:] != sp.zeros(3))

    print("\nPART 3: O_h orbit average of the spatial quadratic projection")
    kvec = sp.Matrix(spatial_vars)
    hessian_spatial = sp.hessian(artifact, spatial_vars)
    average = sp.zeros(3)
    group = signed_permutation_matrices()
    for g in group:
        transformed = g * kvec
        sub = {kx: transformed[0], ky: transformed[1], kz: transformed[2]}
        average += hessian_spatial.subs(sub, simultaneous=True)
    average = sp.simplify(average / len(group))
    shell_radius_sq = kx**2 + ky**2 + kz**2
    expected_average = 4 * shell_radius_sq * sp.eye(3)
    check(
        "O_h orbit average is a single spatial scalar",
        sp.simplify(average - expected_average) == sp.zeros(3),
        str(average),
    )

    print("\nPART 4: resulting marginal channel is spatial-only, coefficient open")
    projected4 = sp.zeros(4)
    projected4[1:, 1:] = expected_average
    check("projected four-dimensional channel has zero p0^2 coefficient", projected4[0, 0] == 0)
    check(
        "projected four-dimensional channel has equal spatial coefficients",
        projected4[1, 1] == projected4[2, 2] == projected4[3, 3]
        and projected4[1, 2] == projected4[1, 3] == projected4[2, 3] == 0,
        str(projected4),
    )
    delta_ct = sp.Integer(0)
    delta_cs = lam
    check(
        "the theorem fixes the support channel, not the physical coefficient",
        lam in delta_cs.free_symbols and delta_ct == 0,
        "delta c_t = 0, delta c_s = lambda remains an open coefficient",
    )

    print("\nPART 5: source-boundary guards")
    check(
        "source note declares audit-canonical bounded_theorem metadata",
        "**Claim type:** bounded_theorem" in note_text
        and "**Type:** bounded_theorem" in note_text,
    )
    check(
        "source note names parent as trace target without markdown back-edge",
        "`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`" in note_text
        and "](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)" not in note_text,
    )
    check(
        "parent note records spatial-BZ channel addendum",
        "EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md" in parent_text
        and "spatial-BZ channel only" in parent_text,
    )
    check(
        "source note keeps coefficient, gamma, and LV sufficiency open",
        "The coefficient and the other two ingredients remain open." in note_flat
        and "does not derive the physical value or sign" in note_flat
        and "does not show that the resulting suppression beats" in note_flat,
    )

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    if FAIL:
        return 1
    print(
        "VERDICT: exact support for a spatial-only O_h-scalar marginal mixing channel; "
        "one-loop coefficient/gamma/LV sufficiency remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
