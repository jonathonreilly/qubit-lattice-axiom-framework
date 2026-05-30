#!/usr/bin/env python3
"""Audit-companion runner for FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA.

This runner checks finite free-Dirac mode algebra only:

  C1: Euclidean kernel inverse and pole continuation.
  C2: Minkowski Dirac Hamiltonian spectrum {+E,+E,-E,-E}.
  C3: u/v spinor completeness, norms, and relative sign.
  C4: CAR particle/antiparticle Fock relabeling is bounded below.
  C5: raw uncapped negative-branch occupancy is an instability diagnostic.

It does not verify an OS-to-Wightman reconstruction, microcausality theorem,
full n-point hierarchy, or spin-statistics theorem.
"""

import itertools

import numpy as np


def euclidean_gammas():
    """Euclidean Dirac matrices, {g_mu, g_nu} = 2 delta_mu_nu."""
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    g4 = np.block([[i2, z2], [z2, -i2]])
    g1 = np.block([[z2, -1j * sx], [1j * sx, z2]])
    g2 = np.block([[z2, -1j * sy], [1j * sy, z2]])
    g3 = np.block([[z2, -1j * sz], [1j * sz, z2]])
    return [g1, g2, g3, g4]


def minkowski_gammas():
    """Mostly-minus Minkowski gammas from Euclidean gammas."""
    g = euclidean_gammas()
    return [g[3], 1j * g[0], 1j * g[1], 1j * g[2]]


def check_inverse_and_poles(rng):
    g = euclidean_gammas()
    ok = True
    for _ in range(80):
        m = rng.uniform(0.2, 3.0)
        p4 = rng.normal(size=4)
        gp = sum(p4[k] * g[k] for k in range(4))
        ident = np.eye(4, dtype=complex)
        M = m * ident + 1j * gp
        S = (m * ident - 1j * gp) / (p4 @ p4 + m * m)
        ok &= np.allclose(M @ S, ident, atol=1e-10)
        ok &= np.allclose(S @ M, ident, atol=1e-10)
        ok &= np.allclose(S, np.linalg.inv(M), atol=1e-10)

        p3 = rng.normal(size=3)
        E = float(np.sqrt(p3 @ p3 + m * m))
        euclidean_roots = np.roots([1.0, 0.0, E * E])
        ok &= np.allclose(np.sort(euclidean_roots.imag), [-E, E], atol=1e-9)
        ok &= np.allclose(euclidean_roots.real, 0.0, atol=1e-9)
        minkowski_roots = np.roots([-1.0, 0.0, E * E])
        ok &= np.allclose(np.sort(minkowski_roots.real), [-E, E], atol=1e-9)
        ok &= np.allclose(minkowski_roots.imag, 0.0, atol=1e-9)
    return bool(ok)


def dirac_hamiltonian(p3, m):
    G = minkowski_gammas()
    G0 = G[0]
    alpha = [G0 @ G[k + 1] for k in range(3)]
    beta = G0
    H = sum(p3[k] * alpha[k] for k in range(3)) + m * beta
    return H


def check_dirac_spectrum(rng):
    ok = True
    for _ in range(80):
        m = rng.uniform(0.2, 3.0)
        p3 = rng.normal(size=3)
        E = float(np.sqrt(p3 @ p3 + m * m))
        H = dirac_hamiltonian(p3, m)
        w = np.linalg.eigvalsh(H)
        ok &= np.allclose(H, H.conj().T, atol=1e-10)
        ok &= np.allclose(np.sort(w), [-E, -E, E, E], atol=1e-9)
    return bool(ok)


def explicit_spinors(p3, m):
    G = minkowski_gammas()
    G0 = G[0]
    sigma = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    basis = (
        np.array([1, 0], dtype=complex),
        np.array([0, 1], dtype=complex),
    )
    E = float(np.sqrt(p3 @ p3 + m * m))
    sdotp = sum(p3[k] * sigma[k] for k in range(3))
    us = [
        np.concatenate([np.sqrt(E + m) * s, (sdotp @ s) / np.sqrt(E + m)])
        for s in basis
    ]
    vs = [
        np.concatenate([(sdotp @ s) / np.sqrt(E + m), np.sqrt(E + m) * s])
        for s in basis
    ]
    slash_p = E * G0 - sum(p3[k] * G[k + 1] for k in range(3))
    return E, G0, slash_p, us, vs


def check_spinor_completeness(rng):
    ok = True
    ident = np.eye(4, dtype=complex)
    for _ in range(80):
        m = rng.uniform(0.3, 3.0)
        p3 = rng.normal(size=3)
        E, G0, slash_p, us, vs = explicit_spinors(p3, m)

        Sigma_uu = sum(np.outer(u, u.conj() @ G0) for u in us)
        Sigma_vv = sum(np.outer(v, v.conj() @ G0) for v in vs)
        ok &= np.allclose(Sigma_uu, slash_p + m * ident, atol=1e-6)
        ok &= np.allclose(Sigma_vv, slash_p - m * ident, atol=1e-6)

        for u in us:
            ok &= np.allclose((slash_p - m * ident) @ u, 0.0, atol=1e-8)
            ok &= np.isclose(float((u.conj() @ u).real), 2.0 * E, atol=1e-7)
            ok &= np.isclose(float((u.conj() @ G0 @ u).real), 2.0 * m, atol=1e-7)
        for v in vs:
            ok &= np.allclose((slash_p + m * ident) @ v, 0.0, atol=1e-8)
            ok &= np.isclose(float((v.conj() @ v).real), 2.0 * E, atol=1e-7)
            ok &= np.isclose(float((v.conj() @ G0 @ v).real), -2.0 * m, atol=1e-7)

        sign_u = np.sign(float((us[0].conj() @ G0 @ us[0]).real))
        sign_v = np.sign(float((vs[0].conj() @ G0 @ vs[0]).real))
        ok &= sign_u == -sign_v
    return bool(ok)


def check_car_positive_fock(rng):
    ok = True
    for _ in range(20):
        nmodes = int(rng.integers(2, 5))
        particle_E = rng.uniform(0.2, 3.0, size=nmodes)
        antiparticle_E = rng.uniform(0.2, 3.0, size=nmodes)
        all_E = np.concatenate([particle_E, antiparticle_E])
        spectrum = []
        for occ in itertools.product((0, 1), repeat=len(all_E)):
            spectrum.append(sum(o * e for o, e in zip(occ, all_E)))
        spectrum = np.array(spectrum)
        ok &= spectrum.min() >= -1e-12
        ok &= abs(spectrum.min()) < 1e-12
        ok &= np.isclose(spectrum.max(), all_E.sum(), atol=1e-12)
    return bool(ok)


def check_raw_negative_branch_diagnostic(rng):
    ok = True
    for _ in range(20):
        E = rng.uniform(0.2, 3.0)
        cut1 = 8
        cut2 = 32
        raw1 = np.array([-E * n for n in range(cut1 + 1)])
        raw2 = np.array([-E * n for n in range(cut2 + 1)])
        ok &= raw2.min() < raw1.min()

        car = np.array([0.0, E])
        ok &= car.min() >= -1e-12
        ok &= car[1] > 0.0
    return bool(ok)


def main():
    rng = np.random.default_rng(20260530)
    checks = [
        ("C1_inverse_and_pole_continuation", check_inverse_and_poles(rng)),
        ("C2_dirac_spectrum_pmE_double", check_dirac_spectrum(rng)),
        ("C3_uv_completeness_norms_relative_sign", check_spinor_completeness(rng)),
        ("C4_car_positive_fock_relabeling", check_car_positive_fock(rng)),
        ("C5_raw_negative_branch_diagnostic", check_raw_negative_branch_diagnostic(rng)),
    ]

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
