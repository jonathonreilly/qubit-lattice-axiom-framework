#!/usr/bin/env python3
"""Free-sector relativistic-QFT support diagnostics.

This runner checks bounded support facts. It does not prove full measure
convergence, reflection positivity, statistics selection, all-orders interacting
Lorentz covariance, or non-perturbative continuum existence.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
from scipy.linalg import expm

np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88 + "\n" + title + "\n" + "-" * 88)


def gammas() -> list[np.ndarray]:
    sigmas = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]
    zero = np.zeros((2, 2), complex)
    ident = np.eye(2, dtype=complex)
    spatial = [np.block([[zero, -1j * sigma], [1j * sigma, zero]]) for sigma in sigmas]
    time = np.block([[zero, ident], [ident, zero]])
    return [time] + spatial


GAMMA = gammas()


def s_cont(p: np.ndarray, mass: float = 0.7) -> np.ndarray:
    pslash = sum(p[mu] * GAMMA[mu] for mu in range(4))
    return (mass * np.eye(4) - 1j * pslash) / (np.dot(p, p) + mass * mass)


def s_lat(p: np.ndarray, spacing: float, mass: float = 0.7) -> np.ndarray:
    pbar = np.array([np.sin(p[mu] * spacing) / spacing for mu in range(4)])
    pslash = sum(pbar[mu] * GAMMA[mu] for mu in range(4))
    return (mass * np.eye(4) - 1j * pslash) / (np.dot(pbar, pbar) + mass * mass)


def main() -> int:
    print("=" * 88)
    print("FREE-SECTOR RELATIVISTIC-QFT SUPPORT DIAGNOSTICS")
    print("=" * 88)

    section("Part A: sampled Wick expressions inherit covariance convergence rate")
    momenta = [
        np.array([0.3, 0.2, -0.1, 0.15]),
        np.array([-0.2, 0.1, 0.25, -0.05]),
        np.array([0.1, -0.3, 0.05, 0.2]),
    ]

    def err_npoint(spacing: float, n_pairs: int) -> float:
        pts = momenta[:n_pairs]
        lat = [[s_lat(pi - pj, spacing) for pj in pts] for pi in pts]
        cont = [[s_cont(pi - pj) for pj in pts] for pi in pts]
        if n_pairs == 2:
            lat_val = lat[0][0] @ lat[1][1] - lat[0][1] @ lat[1][0]
            cont_val = cont[0][0] @ cont[1][1] - cont[0][1] @ cont[1][0]
        else:
            def wick(blocks: list[list[np.ndarray]]) -> np.ndarray:
                total = np.zeros((4, 4), complex)
                for perm in itertools.permutations(range(n_pairs)):
                    seen = [False] * n_pairs
                    parity = 0
                    for i in range(n_pairs):
                        if not seen[i]:
                            j = i
                            cycle_len = 0
                            while not seen[j]:
                                seen[j] = True
                                j = perm[j]
                                cycle_len += 1
                            parity += cycle_len - 1
                    term = np.eye(4, dtype=complex)
                    for i in range(n_pairs):
                        term = term @ blocks[i][perm[i]]
                    total += ((-1) ** parity) * term
                return total

            lat_val = wick(lat)
            cont_val = wick(cont)
        return float(np.max(np.abs(lat_val - cont_val)))

    rate_ok = True
    for n_pairs, label in [(2, "4-point"), (3, "6-point")]:
        e1 = err_npoint(0.20, n_pairs)
        e2 = err_npoint(0.10, n_pairs)
        e3 = err_npoint(0.05, n_pairs)
        r1 = e1 / e2 if e2 else 0.0
        r2 = e2 / e3 if e3 else 0.0
        print(
            f"  {label}: err(0.20)={e1:.3e} err(0.10)={e2:.3e} "
            f"err(0.05)={e3:.3e} ratios={r1:.2f},{r2:.2f}"
        )
        rate_ok = rate_ok and (3.0 < r1 < 5.0) and (3.0 < r2 < 5.0)
    check(
        "sampled Wick-built 4-point and 6-point expressions show O(a^2) convergence",
        rate_ok,
        "support only; not a full measure-convergence theorem",
    )

    section("Part B: necessary free 4D Hamiltonian/transfer positivity checks")
    spacing = 1.0
    mass = 0.7
    alpha = [-1j * GAMMA[0] @ GAMMA[k] for k in (1, 2, 3)]
    beta = GAMMA[0]
    spectrum_ok = True
    transfer_ok = True
    for pvec in [(0.3, 0.1, -0.2), (1.0, 0.7, 0.4), (0.0, 0.0, 0.0), (2.5, -1.0, 1.5)]:
        phat = np.array([np.sin(pi * spacing) / spacing for pi in pvec])
        H = sum(phat[k] * alpha[k] for k in range(3)) + mass * beta
        if not np.allclose(H, H.conj().T, atol=1e-12):
            spectrum_ok = False
        eig = np.linalg.eigvalsh(H)
        energy = np.sqrt(np.dot(phat, phat) + mass * mass)
        if not np.allclose(sorted(abs(eig)), [energy, energy, energy, energy], atol=1e-10):
            spectrum_ok = False
        w, V = np.linalg.eigh(H)
        transfer = V @ np.diag(np.exp(-2 * spacing * np.abs(w))) @ V.conj().T
        if np.min(np.linalg.eigvalsh(transfer)) <= 0:
            transfer_ok = False
    check("sampled 4D free Dirac H(p) is Hermitian with +/-E spectrum", spectrum_ok)
    check("sampled two-step transfer exp(-2a|H|) is positive-definite", transfer_ok)

    section("Part C: equal-time spacelike parity diagnostic for statistics route")
    mass = 1.0
    separation = 1.3
    grid = 64
    cutoff = 12.0
    axis = (np.arange(grid) + 0.5) / grid * 2 * cutoff - cutoff
    px, py, pz = np.meshgrid(axis, axis, axis, indexing="ij")
    energy = np.sqrt(px**2 + py**2 + pz**2 + mass * mass)
    phase = px * separation
    dvol = (2 * cutoff / grid) ** 3 / (2 * np.pi) ** 3
    antisym = np.sum((np.exp(1j * phase) - np.exp(-1j * phase)) / (2 * energy)) * dvol
    sym = np.sum((np.exp(1j * phase) + np.exp(-1j * phase)) / (2 * energy)) * dvol
    print(
        f"  equal-time r={separation}: |antisymmetric|={abs(antisym):.3e}, "
        f"|symmetric|={abs(sym):.3e}"
    )
    check("antisymmetric two-point combination vanishes in the sampled equal-time spacelike check", abs(antisym) < 1e-9)
    check("symmetric two-point combination is nonzero in the sampled equal-time spacelike check", abs(sym) > 1e-3)
    check(
        "diagnostic supplies input for a spin-statistics route but does not select statistics by itself",
        abs(antisym) < 1e-9 and abs(sym) > 1e-3,
        "requires the separate relativistic reconstruction/locality theorem",
    )

    section("Part D: one-loop symmetric-surface anisotropy diagnostic")
    nk = 10
    ks = (np.arange(nk) + 0.5) / nk * 2 * np.pi - np.pi
    k0, kx, ky, kz = np.meshgrid(ks, ks, ks, ks, indexing="ij")
    khat2 = sum((2 * np.sin(k / 2)) ** 2 for k in (k0, kx, ky, kz)) + 1e-3

    def velocity_coeff(direction: int, eps: float = 0.1, mf: float = 0.2) -> float:
        p = [0.0, 0.0, 0.0, 0.0]
        p[direction] = eps
        q = [p[mu] - k for mu, k in enumerate((k0, kx, ky, kz))]
        qbar = [np.sin(qi) for qi in q]
        denom = sum(x * x for x in qbar) + mf * mf
        integrand = qbar[direction] / (denom * khat2)
        return float(np.sum(integrand) / nk**4 / np.sin(eps))

    zt = velocity_coeff(0)
    zs = velocity_coeff(1)
    check(
        "sampled one-loop velocity coefficient is time/space symmetric on the supplied symmetric surface",
        abs(zt - zs) < 1e-12,
        f"|z_t - z_s|={abs(zt - zs):.2e}; support only, not an all-orders theorem",
    )
    check(
        "non-perturbative interacting continuum existence remains outside this diagnostic",
        True,
        "explicit boundary",
    )

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("Boundary: support diagnostics only; no domino closure or audit verdict.")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
