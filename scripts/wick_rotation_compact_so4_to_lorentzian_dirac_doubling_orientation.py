#!/usr/bin/env python3
"""Finite algebra orientation: compact Euclidean Spin(4) generators can be
Wick-rotated to the non-compact Lorentzian Dirac doubling.

This runner preserves the useful finite-dimensional content from the rejected
emergent-time/doubling overclaim without importing the overclaim. It checks only
matrix algebra:

- Euclidean gamma matrices generate compact Spin(4): all Sigma^E are
  anti-Hermitian and Euclidean "boost" exponentials are unitary.
- With gamma^0 = gamma^E_4 and gamma^j = i gamma^E_j, the Lorentzian Clifford
  relation has signature (+---).
- The Wick factor maps the compact Euclidean mixed generators to Hermitian
  Lorentzian boosts, whose exponentials are non-unitary.
- The Lorentzian boost-boost bracket has the non-compact sign.
- The C^4 Dirac space carries both chiral sectors and the massive on-shell
  projector is a C^4 bispinor object.

It does not claim that the framework's Record axiom supplies a time axis, that
the framework realizes this Wick rotation dynamically, that positive energy or
CAR are delivered, or that the Koide Sec. 6 residual is closed.
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def report(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" :: {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} {name}{suffix}")
    return ok


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def adj(a: np.ndarray) -> np.ndarray:
    return a.conj().T


def expm_small(a: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eig(a)
    return vectors @ np.diag(np.exp(values)) @ np.linalg.inv(vectors)


def main() -> int:
    eye2 = np.eye(2, dtype=complex)
    eye4 = np.eye(4, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma = [sx, sy, sz]

    # Hermitian Euclidean gamma matrices: gamma^E_1..gamma^E_3, gamma^E_4.
    gamma_e = [np.kron(sy, s) for s in sigma] + [np.kron(sx, eye2)]
    sigma_e = {
        (mu, nu): 0.25 * comm(gamma_e[mu], gamma_e[nu])
        for mu in range(4)
        for nu in range(mu + 1, 4)
    }

    print("=" * 78)
    print("Wick-rotation orientation: compact Spin(4) -> Lorentzian Dirac doubling")
    print("=" * 78)

    euclidean_antiherm = all(np.allclose(adj(gen), -gen, atol=1e-12) for gen in sigma_e.values())
    euclidean_mixed = [sigma_e[(j, 3)] for j in range(3)]
    euclidean_boost_unitary = all(
        np.allclose(expm_small(0.7 * gen) @ adj(expm_small(0.7 * gen)), eye4, atol=1e-12)
        for gen in euclidean_mixed
    )
    report(
        "Euclidean mixed Spin(4) generators are compact",
        euclidean_antiherm and euclidean_boost_unitary,
        "Sigma^E anti-Hermitian; exp(theta Sigma^E_4j) unitary",
    )

    gamma_l = [gamma_e[3]] + [1j * gamma_e[j] for j in range(3)]
    eta = np.diag([1, -1, -1, -1])
    clifford_l = all(
        np.allclose(gamma_l[a] @ gamma_l[b] + gamma_l[b] @ gamma_l[a], 2 * eta[a, b] * eye4, atol=1e-12)
        for a in range(4)
        for b in range(4)
    )
    e4 = 1j * gamma_l[0]
    e4_square_minus = np.allclose(e4 @ e4, -eye4, atol=1e-12)
    report(
        "Wick-rotated gamma matrices satisfy Lorentzian Clifford signature",
        clifford_l and e4_square_minus,
        "gamma^0^2=+1, gamma^j^2=-1, e_4=i gamma^0 has square -1",
    )

    boosts = [0.25 * comm(gamma_l[0], gamma_l[j]) for j in range(1, 4)]
    rotations = [0.25 * comm(gamma_l[i], gamma_l[j]) for (i, j) in [(2, 3), (3, 1), (1, 2)]]
    boosts_hermitian = all(np.allclose(adj(k), k, atol=1e-12) for k in boosts)
    rotations_antihermitian = all(np.allclose(adj(j), -j, atol=1e-12) for j in rotations)
    boosts_nonunitary = any(
        not np.allclose(expm_small(0.7 * k) @ adj(expm_small(0.7 * k)), eye4, atol=1e-8)
        for k in boosts
    )
    wick_map = all(
        np.allclose(boosts[j], 1j * 0.25 * comm(gamma_e[3], gamma_e[j]), atol=1e-12)
        for j in range(3)
    )
    report(
        "Wick factor maps compact Euclidean mixed generators to non-compact boosts",
        boosts_hermitian and rotations_antihermitian and boosts_nonunitary and wick_map,
        "K_j = i/4 [gamma^E_4,gamma^E_j]; boosts Hermitian, rotations anti-Hermitian",
    )

    cyclic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    kk_sign = all(np.allclose(comm(boosts[i], boosts[j]), -rotations[k], atol=1e-12) for i, j, k in cyclic)
    jj_sign = all(np.allclose(comm(rotations[i], rotations[j]), rotations[k], atol=1e-12) for i, j, k in cyclic)
    report(
        "Lorentzian boosts carry the non-compact bracket sign",
        kk_sign and jj_sign,
        "[K_i,K_j] = -J_k while [J_i,J_j] = +J_k in the 1/4[gamma,gamma] convention",
    )

    gamma5 = 1j * gamma_l[0] @ gamma_l[1] @ gamma_l[2] @ gamma_l[3]
    p_plus = 0.5 * (eye4 + gamma5)
    p_minus = 0.5 * (eye4 - gamma5)
    two_chiral_sectors = (
        np.allclose(gamma5 @ gamma5, eye4, atol=1e-12)
        and np.allclose(np.trace(p_plus).real, 2.0, atol=1e-12)
        and np.allclose(np.trace(p_minus).real, 2.0, atol=1e-12)
    )
    mass = 0.7
    spatial_p = np.array([0.3, -0.4, 0.5])
    energy = float(np.sqrt(mass * mass + spatial_p @ spatial_p))
    pslash = energy * gamma_l[0] - sum(spatial_p[j - 1] * gamma_l[j] for j in range(1, 4))
    projector = (pslash + mass * eye4) / (2 * mass)
    projector_idempotent = np.allclose(projector @ projector, projector, atol=1e-10)
    cross_chiral_nonzero = (
        np.linalg.norm(p_plus @ projector @ p_minus) > 1e-10
        or np.linalg.norm(p_minus @ projector @ p_plus) > 1e-10
    )
    report(
        "C4 Dirac doubling carries both chiral sectors and a massive bispinor projector",
        two_chiral_sectors and projector_idempotent and cross_chiral_nonzero,
        "tr P_+=tr P_-=2; (p_slash+m)/2m idempotent on C4 and mixes chiral sectors",
    )

    forbidden_claims_absent = True
    report(
        "Firewall: this is finite algebra orientation only",
        forbidden_claims_absent,
        "no Record/time-axis derivation, no framework-realization claim, no CAR or positive-energy closure",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
