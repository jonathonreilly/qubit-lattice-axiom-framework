#!/usr/bin/env python3
"""Bertrand stable-orbit upper-bound support repair.

This runner verifies the continuum radial Green-potential law for integer
d >= 3 and the exact circular-orbit stability algebra. It does not claim a
framework-native dimensional-gravity law or retire the full Bertrand theorem.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


REPO = Path(__file__).resolve().parent.parent
NOTE = REPO / "docs" / "BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f" | {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def main() -> int:
    print("Bertrand stable-orbit upper-bound support repair")
    print("Scope: continuum radial Green-potential law + circular stability algebra.")
    print()

    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(REPO)))
    for phrase in [
        "Continuum `d`-Law Derivation",
        "not an extrapolation from",
        "central-potential Hamiltonian surface",
        "does not establish a framework-native universal dimensional-gravity law",
    ]:
        check(f"scope phrase present: {phrase}", phrase in text)

    r, d, k, L, m = sp.symbols("r d k L m", positive=True)

    # Radial Green-potential derivation: Delta r^(2-d)=0 for r>0, d>=3.
    f = r ** (2 - d)
    radial_laplacian = sp.simplify(sp.diff(f, r, 2) + ((d - 1) / r) * sp.diff(f, r))
    check("radial Laplacian of r^(2-d) vanishes", radial_laplacian == 0, str(radial_laplacian))

    V = -k / r ** (d - 2)
    force = sp.simplify(-sp.diff(V, r))
    expected_force = -k * (d - 2) / r ** (d - 1)
    check(
        "force scales as attractive inverse r^(d-1)",
        sp.simplify(force - expected_force) == 0,
        f"force={force}",
    )

    V_eff = V + L**2 / (2 * m * r**2)
    dV = sp.diff(V_eff, r)
    circular_L2 = sp.solve(sp.Eq(dV, 0), L**2)[0]
    expected_L2 = k * m * (d - 2) * r ** (4 - d)
    check(
        "circular-orbit condition gives L^2",
        sp.simplify(circular_L2 - expected_L2) == 0,
        f"L2={circular_L2}",
    )

    d2V = sp.diff(V_eff, r, 2)
    stability_curvature = sp.simplify(d2V.subs(L**2, circular_L2))
    expected_curvature = k * (d - 2) * (4 - d) / r**d
    check(
        "curvature after eliminating L^2 is k(d-2)(4-d)/r^d",
        sp.simplify(stability_curvature - expected_curvature) == 0,
        f"curvature={stability_curvature}",
    )

    stable = []
    marginal = []
    unstable = []
    for dim in range(3, 13):
        sign = sp.sign((dim - 2) * (4 - dim))
        if sign > 0:
            stable.append(dim)
        elif sign == 0:
            marginal.append(dim)
        else:
            unstable.append(dim)
    check("integer d=3 is the only stable case in 3..12", stable == [3], f"stable={stable}")
    check("integer d=4 is marginal", marginal == [4], f"marginal={marginal}")
    check("integer d>=5 are unstable in scan", unstable == list(range(5, 13)), f"unstable={unstable}")

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
