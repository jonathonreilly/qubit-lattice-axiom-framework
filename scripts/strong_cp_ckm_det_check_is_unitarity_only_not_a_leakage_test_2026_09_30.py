#!/usr/bin/env python3
"""
Strong CP runner check `|det V_CKM| = 1` is a unitarity sanity check, not a leakage test
========================================================================================

STATUS: correction evidence (corrigendum 2026-09-30) for
`docs/STRONG_CP_THETA_ZERO_NOTE.md` and `scripts/frontier_strong_cp_theta_zero.py`.
It confers no audit verdict and proves no strong-CP statement.

WHAT THIS SCRIPT SHOWS (finite numerical controls plus one exact identity):

  1. |det V| = 1 for every unitary V, since |det V|^2 = det(V^dag V) = 1.
     Checked on 2000 unitaries from two independent constructions.
  2. On the runner's own CKM parametrization (same lambda, A, rho, eta as the
     runner), |det V| = 1 and V^dag V = 1 for every value of the CP phase delta
     tried, including delta = 0 where the Jarlskog invariant J = 0.  The check
     is therefore blind to the CKM phase: it cannot detect any dependence of
     anything on delta.
  3. |det V| = 1 does not even imply unitarity (diag(2, 1/2, 1) passes), which
     is why the relabelled runner check also tests V^dag V = 1.
  4. At tree level a CP-violating CKM matrix and arg det(M_u M_d) = 0 coexist
     (positive-definite Hermitian mass matrices with generic diagonalizers).
     This is coexistence at the mass-matrix level only, not a stability result.

WHAT IT DOES NOT SHOW:

  Whether the CKM phase feeds into theta-bar through radiative corrections
  (weak-sector loops) is NOT tested here or in the strong-CP runner.  That
  question is open.
"""

from __future__ import annotations

# Explicit bounded execution cap; scientific content is unchanged by this metadata.
AUDIT_TIMEOUT_SEC = 120

import sys

import numpy as np

from canonical_plaquette_surface import CANONICAL_ALPHA_S_V

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    return condition


def haar_unitary_qr(rng, n):
    """Haar-distributed unitary from the QR decomposition of a Ginibre matrix."""
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def unitary_from_hermitian(rng, n):
    """Unitary exp(iH) for a random Hermitian H, via the eigendecomposition of H."""
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    h = (a + a.conj().T) / 2.0
    w, u = np.linalg.eigh(h)
    return (u * np.exp(1j * w)) @ u.conj().T


def ckm_matrix(s12, s23, s13, delta):
    """Standard CKM parametrization, written exactly as in the strong-CP runner."""
    c12, c23, c13 = (np.sqrt(1.0 - x**2) for x in (s12, s23, s13))
    e = np.exp(1j * delta)
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * np.conj(e)],
            [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13],
        ]
    )


def jarlskog(v):
    """Jarlskog invariant J; values below 1e-15 are floating-point zero and printed as 0."""
    j = float(np.imag(v[0, 0] * v[1, 1] * np.conj(v[0, 1]) * np.conj(v[1, 0])))
    return 0.0 if abs(j) < 1e-15 else j


def unitarity_deviation(v):
    return float(np.max(np.abs(v.conj().T @ v - np.eye(v.shape[0]))))


def main():
    rng = np.random.default_rng(20260930)

    print("=" * 78)
    print("Strong-CP runner check |det V_CKM| = 1: unitarity sanity only")
    print("=" * 78)

    print("\n=== 1. |det V| = 1 for every unitary matrix ===\n")
    dets_qr = np.array([abs(np.linalg.det(haar_unitary_qr(rng, 3))) for _ in range(1000)])
    dets_h = np.array([abs(np.linalg.det(unitary_from_hermitian(rng, 3))) for _ in range(1000)])
    check(
        "1000 Haar (QR) unitary 3x3 matrices all have |det| = 1",
        float(np.max(np.abs(dets_qr - 1.0))) < 1e-12,
        f"min {dets_qr.min():.12f}, max {dets_qr.max():.12f}",
    )
    check(
        "1000 exp(iH) unitary 3x3 matrices all have |det| = 1",
        float(np.max(np.abs(dets_h - 1.0))) < 1e-12,
        f"min {dets_h.min():.12f}, max {dets_h.max():.12f}",
    )
    u = haar_unitary_qr(rng, 3)
    check(
        "identity |det V|^2 = det(V^dag V) = 1 on a sample unitary",
        abs(abs(np.linalg.det(u)) ** 2 - np.linalg.det(u.conj().T @ u).real) < 1e-12
        and abs(np.linalg.det(u.conj().T @ u).real - 1.0) < 1e-12,
        "so the check holds for any unitary whatever its phases",
    )

    print("\n=== 2. The runner's CKM matrix: check is blind to the CP phase delta ===\n")
    lam = np.sqrt(CANONICAL_ALPHA_S_V / 2.0)
    a_wolf = np.sqrt(2.0 / 3.0)
    rho = 1.0 / 6.0
    eta = np.sqrt(5.0) / 6.0
    delta_std = float(np.arctan2(eta, rho))
    s12 = lam
    s23 = a_wolf * lam**2
    s13 = a_wolf * lam**3 * float(np.hypot(rho, eta))

    deltas = [0.0, 0.5, delta_std, np.pi / 2.0, np.pi, 4.0]
    dets = []
    devs = []
    jvals = []
    for d in deltas:
        v = ckm_matrix(s12, s23, s13, d)
        dets.append(abs(np.linalg.det(v)))
        devs.append(unitarity_deviation(v))
        jvals.append(jarlskog(v))
        print(f"    delta = {d:.6f} rad: |det V| = {dets[-1]:.15f}, max|V^dag V - 1| = {devs[-1]:.2e}, J = {jvals[-1]:+.4e}")
    check(
        "|det V| = 1 and V^dag V = 1 at every delta tried",
        max(abs(x - 1.0) for x in dets) < 1e-12 and max(devs) < 1e-12,
        f"max ||det|-1| = {max(abs(x - 1.0) for x in dets):.2e}",
    )
    check(
        "the check passes at delta = 0, where J = 0 (CP-conserving CKM matrix)",
        abs(jvals[0]) < 1e-15 and abs(dets[0] - 1.0) < 1e-12,
        f"J(delta=0) = {jvals[0]:.1f}",
    )
    check(
        "at the runner's delta = arctan(sqrt 5), J matches the cited framework value 3.331e-5",
        abs(jvals[2] - 3.331e-5) < 5e-9,
        f"J = {jvals[2]:.4e}, delta = {np.degrees(delta_std):.3f} deg",
    )
    check(
        "J varies over more than 3e-5 across the sweep while |det V| does not move",
        (max(jvals) - min(jvals)) > 3e-5 and (max(dets) - min(dets)) < 1e-12,
        f"J range = {max(jvals) - min(jvals):.3e}, |det V| spread = {max(dets) - min(dets):.2e}",
    )

    print("\n=== 3. |det V| = 1 does not imply unitarity ===\n")
    n_bad = np.diag([2.0, 0.5, 1.0])
    check(
        "diag(2, 1/2, 1) has |det| = 1 but is not unitary",
        abs(abs(np.linalg.det(n_bad)) - 1.0) < 1e-12 and unitarity_deviation(n_bad) > 1.0,
        f"|det| = {abs(np.linalg.det(n_bad)):.12f}, max|N^dag N - 1| = {unitarity_deviation(n_bad):.3f}",
    )
    m = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    m = m / abs(np.linalg.det(m)) ** (1.0 / 3.0)
    check(
        "a generic complex matrix rescaled to |det| = 1 passes the determinant test but is not unitary",
        abs(abs(np.linalg.det(m)) - 1.0) < 1e-12 and unitarity_deviation(m) > 0.1,
        f"max|M^dag M - 1| = {unitarity_deviation(m):.3f}",
    )

    print("\n=== 4. Tree-level coexistence of a CKM phase with arg det(M_u M_d) = 0 ===\n")
    d_u = np.diag(np.sort(rng.uniform(0.1, 10.0, size=3)))
    d_d = np.diag(np.sort(rng.uniform(0.1, 10.0, size=3)))
    uu = haar_unitary_qr(rng, 3)
    ud = haar_unitary_qr(rng, 3)
    m_u = uu @ d_u @ uu.conj().T
    m_d = ud @ d_d @ ud.conj().T
    v_mix = uu.conj().T @ ud
    arg_det = float(np.angle(np.linalg.det(m_u @ m_d)))
    check(
        "positive-definite Hermitian M_u, M_d give arg det(M_u M_d) = 0 while V = U_u^dag U_d has J != 0",
        abs(arg_det) < 1e-12 and abs(jarlskog(v_mix)) > 1e-3,
        f"arg det = {arg_det:.2e}, J = {jarlskog(v_mix):+.3e}",
    )

    print("\n=== NOT TESTED ===\n")
    print("  [INFO] Radiative transmission of the CKM phase into theta-bar through weak-sector")
    print("         loops is not tested here or in scripts/frontier_strong_cp_theta_zero.py.")
    print("         The leakage question remains open.")

    print()
    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
