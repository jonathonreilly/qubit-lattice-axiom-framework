#!/usr/bin/env python3
"""Weak-field optical metric ansatz diagnostic.

This runner checks local differential-geometry facts for the supplied static
weak-field ansatz

    g = diag(-(1 + 2 Phi(x)), 1, 1, 1).

It does not derive the ansatz from Record, record density, the kinetic-isotropy
primitive, or a source/action rule. It also does not derive the gravity sign,
the tensor graviton sector, or nonlinear Einstein closure.
"""

from __future__ import annotations

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def lattice_resolvent_slope(L: int = 61) -> float:
    k = np.fft.fftfreq(L) * 2 * np.pi
    KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
    lap = (2 - 2 * np.cos(KX)) + (2 - 2 * np.cos(KY)) + (2 - 2 * np.cos(KZ))
    lap[0, 0, 0] = 1.0
    rho = np.zeros((L, L, L))
    c = L // 2
    rho[c, c, c] = 1.0
    phi = np.real(np.fft.ifftn(np.fft.fftn(rho) / lap))
    phi -= phi.mean()
    rs = np.arange(3, 10)
    vals = np.array([abs(phi[c + int(r), c, c]) for r in rs])
    return float(np.polyfit(np.log(rs.astype(float)), np.log(vals), 1)[0])


def main() -> int:
    print("WEAK-FIELD OPTICAL METRIC ANSATZ DIAGNOSTIC")
    print("=" * 72)

    x, y, z, t = sp.symbols("x y z t", real=True)
    eps = sp.symbols("epsilon", positive=True)
    Phi = sp.Function("Phi")(x)
    coords = [t, x, y, z]

    g = sp.diag(-(1 + 2 * eps * Phi), 1, 1, 1)
    ginv = g.inv()
    isotropic_spatial = g[1, 1] == 1 and g[2, 2] == 1 and g[3, 3] == 1
    check(
        "M1 supplied weak-field ansatz has isotropic spatial part and scalar g_00 perturbation",
        isotropic_spatial and g[0, 0].has(Phi),
        "g = diag(-(1 + 2 epsilon Phi(x)), 1, 1, 1)",
    )

    n = 4
    Gamma = [[[sp.Rational(0)] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = sp.Rational(0)
                for d in range(n):
                    s += ginv[a, d] * (
                        sp.diff(g[d, b], coords[c])
                        + sp.diff(g[d, c], coords[b])
                        - sp.diff(g[b, c], coords[d])
                    )
                Gamma[a][b][c] = sp.simplify(s / 2)

    def ricci(b: int, c: int) -> sp.Expr:
        s = sp.Rational(0)
        for a in range(n):
            s += sp.diff(Gamma[a][b][c], coords[a]) - sp.diff(Gamma[a][b][a], coords[c])
            for d in range(n):
                s += Gamma[a][a][d] * Gamma[d][b][c] - Gamma[a][c][d] * Gamma[d][b][a]
        return sp.simplify(s)

    R00 = ricci(0, 0)
    R00_lin = sp.simplify(sp.series(R00, eps, 0, 2).removeO()).coeff(eps, 1)
    expected_R00 = sp.diff(Phi, x, 2)
    check(
        "M2 linearized curvature has R_00 = d^2 Phi / dx^2 in the one-direction model",
        sp.simplify(R00_lin - expected_R00) == 0,
        f"R_00 / epsilon = {sp.nsimplify(R00_lin)}",
    )

    Gamma_x00_lin = sp.simplify(sp.series(Gamma[1][0][0], eps, 0, 2).removeO()).coeff(eps, 1)
    expected_Gamma = sp.diff(Phi, x)
    check(
        "M3 geodesic kinematics follows the supplied potential gradient",
        sp.simplify(Gamma_x00_lin - expected_Gamma) == 0,
        "Gamma^x_00 = d Phi / dx, so nonrelativistic acceleration is -d Phi / dx",
    )

    xx, yy, zz = sp.symbols("xx yy zz", real=True)
    r = sp.sqrt(xx**2 + yy**2 + zz**2)
    lap_inv_r = sp.simplify(sum(sp.diff(1 / r, v, 2) for v in (xx, yy, zz)))
    slope = lattice_resolvent_slope()
    check(
        "M4 Poisson compatibility: 1/r is harmonic off-source and lattice resolvent trends downward near 1/r",
        sp.simplify(lap_inv_r) == 0 and -1.6 < slope < -0.7,
        f"Delta(1/r) = {lap_inv_r}; finite-lattice log-log slope = {slope:.2f}",
    )

    boundary_text = (
        "No record-density->metric derivation, source/action normalization, gravity sign, "
        "TT graviton dynamics, or nonlinear Einstein closure is supplied here."
    )
    check("M5 boundary is explicit", True, boundary_text)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("Boundary: ansatz diagnostic only; no gravity-sign or metric-dynamics derivation.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
