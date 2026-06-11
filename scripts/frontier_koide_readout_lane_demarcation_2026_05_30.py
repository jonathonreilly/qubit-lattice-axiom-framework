#!/usr/bin/env python3
"""Koide readout-lane demarcation.

The native signed/Hermitian (det_R) mass-readout supplies the formula
Q=(1+2r)/3, theta-independence, and the signed readout class, but the tested
non-degenerate native readout freedoms do not supply the (1,1) center weight
r=1/2. Reproduces:

  1. Q_unit = (1+2r)/3, theta-independent; dQ/dr = 2/3 (r=1/2 not an extremum).
  2. Residue no-go: arbitrary spectral residues (Z0, Z1=Z2=w) give an
     r-independent Q only at the single-pole collapse (Z0=0 or w=0 -> Q=1),
     which destroys the 3 distinct masses.
  3. A "center-mimicking" residue Z=(1, 1/2, 1/2) gives a theta- and r-dependent
     Q, not 2/3.
  4. The tracial pre-record reference rho=I/3 gives uniform Born weights
     p_k=1/3 -> block-resolved (1/3, 2/3) = the dimension (1,2) weight -> Q=1.
  5. F1 = log E+ + log E_perp extremizes at r=1/2; F3 = log E+ + 2 log E_perp
     at r=1. The (1,1)-vs-(1,2) choice (a dynamics/weight question) selects
     between them; the readout selects neither.
"""

from __future__ import annotations

import numpy as np
from sympy import (Rational, cos, diff, eye, nsimplify, pi, simplify, solve,
                   sqrt, symbols)

AUDIT_TIMEOUT_SEC = 120

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def lams(a: float, bmag: float, theta: float) -> np.ndarray:
    return np.array([a + 2 * bmag * np.cos(theta + 2 * np.pi * k / 3) for k in range(3)])


def main() -> int:
    section("Check 1 - unit-residue readout: Q=(1+2r)/3, theta-independent, dQ/dr=2/3")
    a, bm, th, r = symbols("a b_mag theta r", positive=True)
    lam = [a + 2 * bm * cos(th + 2 * pi * k / 3) for k in range(3)]
    Q = simplify(sum(l**2 for l in lam) / (sum(lam))**2)
    Q_in_r = simplify(Q.subs(bm, sqrt(r) * a))  # r = b^2/a^2 => bmag = sqrt(r)*a
    check("Q = (1+2r)/3 (unit residues)", simplify(Q_in_r - (1 + 2 * r) / 3) == 0, f"Q={Q_in_r}")
    check("Q is theta-independent", diff(Q, th) == 0)
    check("dQ/dr = 2/3 (r=1/2 is NOT an extremum)", simplify(diff(Q_in_r, r) - Rational(2, 3)) == 0)

    section("Check 2 - residue no-go: r-independent Q only at single-pole collapse")
    # theta=0 slice: lam0=a+2b, lam1=lam2=a-b; residues (Z0, w=Z1+Z2); x=b/a.
    Z0, w, x = symbols("Z0 w x", positive=True)
    l0, l12 = 1 + 2 * x, 1 - x
    Qx = (Z0 * l0**2 + w * l12**2) / (Z0 * l0 + w * l12)**2
    dQx = simplify(diff(Qx, x))
    # solve dQ/dx = 0 for all x  <=>  numerator of dQx vanishes identically in x.
    num = simplify(dQx.as_numer_denom()[0])
    Q_unit_x = simplify(Qx.subs({Z0: 1, w: 2}))  # unit residues: Z0=1, Z1=Z2=1 -> w=2
    check("non-degenerate unit residues: Q depends on x (NOT r-independent)",
          simplify(diff(Q_unit_x, x)) != 0, f"dQ/dx={simplify(diff(Q_unit_x, x))}")
    # no non-degenerate (Z0,w) makes the dQ/dx-numerator vanish identically in x
    # (so no residue pattern makes the 3-mass Q r-independent / pinnable at 2/3);
    # the only x-independent readings are the residue-collapse / mass-loss ones.
    sol = solve(num.as_poly(x).all_coeffs(), [Z0, w], dict=True) if num.free_symbols else []
    check("no non-degenerate (Z0,w) makes Q x-independent (residue DOF exhausted)",
          all((s.get(Z0, 1) == 0 or s.get(w, 1) == 0) for s in sol), f"sols={sol}")

    section("Check 2b - Z=(1,t,t) theta-independence endpoints")

    def q_weighted(a0: float, b0: float, theta0: float, t0: float) -> float:
        L = lams(a0, b0, theta0)
        Z = np.array([1.0, t0, t0])
        return float(np.sum(Z * L**2) / (np.sum(Z * L))**2)

    theta_grid = [0.0, 0.31, 0.73, 1.27]
    b_grid = [0.25, 0.5, 0.7071]
    unit_vals = [q_weighted(1.0, b0, theta0, 1.0) for b0 in b_grid for theta0 in theta_grid]
    collapse_vals = [q_weighted(1.0, b0, theta0, 0.0) for b0 in b_grid for theta0 in theta_grid]
    half_vals_by_b = [
        [q_weighted(1.0, b0, theta0, 0.5) for theta0 in theta_grid]
        for b0 in b_grid
    ]
    check(
        "Z=(1,1,1) unit residues are theta-independent but keep r free",
        max(abs(q_weighted(1.0, b0, theta0, 1.0) - ((1 + 2 * b0**2) / 3.0))
            for b0 in b_grid for theta0 in theta_grid) < 1e-10
        and max(unit_vals) - min(unit_vals) > 1e-3,
        "theta cancels at fixed r, while Q changes with r",
    )
    check(
        "Z=(1,0,0) theta-independent endpoint is single-pole collapse Q=1",
        max(abs(v - 1.0) for v in collapse_vals) < 1e-10,
        "theta independence here is mass-loss collapse, not a 3-mass selector",
    )
    check(
        "Z=(1,1/2,1/2) is not theta-independent",
        any(max(vals) - min(vals) > 1e-3 for vals in half_vals_by_b),
        "nonunit noncollapse residue choice retains theta dependence",
    )

    section("Check 3 - center-mimicking residue Z=(1,1/2,1/2): not 2/3, theta/r-dependent")
    vals = []
    for theta in (0.0, 0.6, 1.2):
        for bb in (0.4, 0.7071, 1.0):
            L = lams(1.0, bb, theta)
            Zc = np.array([1.0, 0.5, 0.5])
            Qc = np.sum(Zc * L**2) / (np.sum(Zc * L))**2
            vals.append(Qc)
    spread = max(vals) - min(vals)
    check("center-mimicking Q varies with theta,r and is not pinned at 2/3",
          spread > 1e-3 and not all(abs(v - 2 / 3) < 1e-6 for v in vals), f"range=[{min(vals):.3f},{max(vals):.3f}]")

    section("Check 4 - tracial reference rho=I/3 -> uniform Born -> (1,2) dimension weight")
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    M = 1.0 * np.eye(3) + (0.5 + 0.3j) * C + (0.5 - 0.3j) * (C @ C)
    _, vecs = np.linalg.eigh(M)
    rho = np.eye(3) / 3.0
    p = np.array([np.real(vecs[:, k].conj() @ rho @ vecs[:, k]) for k in range(3)])
    check("Born weights p_k uniform = 1/3 under tracial rho=I/3", np.allclose(p, 1 / 3))
    # singlet projector vs doublet: block-resolved weight = (1/3, 2/3) = dimension
    Ps = (np.eye(3) + C + C @ C) / 3.0
    w_singlet = float(np.real(np.trace(rho @ Ps)))
    check("block-resolved tracial weight = (1/3, 2/3) = dimension (1,2) -> Q=1",
          abs(w_singlet - 1 / 3) < 1e-9, f"(singlet,doublet)=({w_singlet:.3f},{1-w_singlet:.3f})")

    section("Check 5 - F1 extremizes at r=1/2, F3 at r=1 (the dynamics/weight choice)")
    # E+ = 3 a^2, E_perp = 6 b^2; fix E+ + E_perp = S; extremize F = mu*log E+ + nu*log E_perp.
    aa, bb2, lam_mult = symbols("aa bb lam", positive=True)
    Ep, Eperp = 3 * aa, 6 * bb2  # use aa=a^2, bb=b^2 as the energies' variables
    for (mu, nu, r_expect, name) in [(1, 1, Rational(1, 2), "F1 (1,1)"), (1, 2, 1, "F3 (1,2)")]:
        # Lagrange: d/d aa [mu log(3 aa) + nu log(6 bb) - lam(3aa+6bb)] etc.
        F = mu * __import__("sympy").log(3 * aa) + nu * __import__("sympy").log(6 * bb2)
        st = solve([diff(F, aa) - lam_mult * 3, diff(F, bb2) - lam_mult * 6], [aa, bb2], dict=True)
        s = st[0]
        r_at = simplify((s[bb2]) / (s[aa]))  # r = b^2/a^2 = bb/aa
        check(f"{name} extremum at r={r_expect}", simplify(r_at - r_expect) == 0, f"r={r_at}")

    section("Summary")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("Readout supplies the formula Q=(1+2r)/3 + theta-independence + signed class;")
    print("tested readout freedoms do NOT supply r=1/2.")
    print("The F1-vs-F3 (1,1)-vs-(1,2) choice is the dynamics lane.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
