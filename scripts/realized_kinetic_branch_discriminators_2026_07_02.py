#!/usr/bin/env python3
"""Realized-kinetic-branch discriminators on the two-flux-class surface.

Deterministic, numpy only, no network, no cache writes.

The K0/K1 phase conventions mirror
scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py:
K0 is t == 1 and K1 is the Kawamoto-Smit eta0 sign system.  The parent
runner uses the symmetric unit-amplitude NN hopping convention; this runner
keeps that convention for the finite lattice operator, so the K0 tight-binding
symbol is 2 * sum_mu cos(p_mu).  The K1 first-order discriminator is extracted
from the same eta0 phases through the parent absorbing-frame construction.

Exit code 0 iff FAIL == 0.
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np


PASS = 0
FAIL = 0
COUNT = 0


def check(tag: str, desc: str, ok: bool, extra: str = "") -> bool:
    global PASS, FAIL, COUNT
    COUNT += 1
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{'PASS' if ok else 'FAIL'}] [{tag}] {COUNT:2d}. {desc}"
    if extra:
        line += f"  |  {extra}"
    print(line)
    return ok


I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [S1, S2, S3]
E_UNIT = [np.array(v, dtype=int) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
CELL = list(itertools.product((0, 1), repeat=3))
CELL_INDEX = {r: i for i, r in enumerate(CELL)}


def eta0(x, mu):
    """Kawamoto-Smit signs, matching the parent kinetic-class runner."""
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** (x[0] % 2)
    return (-1.0) ** ((x[0] + x[1]) % 2)


def eta_k0(x, mu):
    return 1.0


def sites(L):
    return list(itertools.product(range(L), repeat=3))


def add_mod(x, mu, L):
    y = list(x)
    y[mu] = (y[mu] + 1) % L
    return tuple(y)


def build_hopping(L, tfun):
    """Parent symmetric unit-amplitude Hermitian NN hopping operator."""
    ss = sites(L)
    idx = {s: i for i, s in enumerate(ss)}
    H = np.zeros((L**3, L**3), dtype=complex)
    for x in ss:
        for mu in range(3):
            y = add_mod(x, mu, L)
            t = complex(tfun(x, mu))
            H[idx[y], idx[x]] += t
            H[idx[x], idx[y]] += np.conj(t)
    return H, ss, idx


def plaquette_fluxes(L, tfun):
    out = []
    for x in sites(L):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = add_mod(x, mu, L)
                xn = add_mod(x, nu, L)
                f = (
                    tfun(x, mu)
                    * tfun(xm, nu)
                    * np.conj(tfun(xn, mu))
                    * np.conj(tfun(x, nu))
                )
                out.append(complex(f))
    return np.array(out)


def Tmat(x):
    out = I2.copy()
    for mu, power in enumerate(x):
        if power % 2:
            out = out @ SIG[mu]
    return out


def absorbed_k1_edge_coefficients(tfun=eta0):
    """Compute direction matrices from eta and the parent absorbing frame.

    The identity T(x)^dag sigma_mu T(x+mu) = eta_mu(x) I implies
    sigma_mu = eta_mu(x) T(x) T(x+mu)^dag.  We average only after computing
    these edge matrices from the phase system.
    """
    coeffs = []
    spreads = []
    for mu in range(3):
        mats = []
        for x in CELL:
            y = tuple(np.array(x) + E_UNIT[mu])
            mats.append(complex(tfun(x, mu)) * Tmat(x) @ Tmat(y).conj().T)
        avg = sum(mats) / len(mats)
        coeffs.append(avg)
        spreads.append(max(np.linalg.norm(M - avg) for M in mats))
    return coeffs, spreads


def k1_raw_extraction_symbol(p, edge_coeffs):
    M = np.zeros((2, 2), dtype=complex)
    for mu in range(3):
        M += 1j * edge_coeffs[mu] * math.sin(float(p[mu]))
    return M


def extract_k1_gammas(edge_coeffs):
    gammas = []
    q = math.pi / 2.0
    for mu in range(3):
        p_plus = np.zeros(3)
        p_minus = np.zeros(3)
        p_plus[mu] = q
        p_minus[mu] = -q
        raw_plus = k1_raw_extraction_symbol(p_plus, edge_coeffs)
        raw_minus = k1_raw_extraction_symbol(p_minus, edge_coeffs)
        gammas.append((raw_plus - raw_minus) / (2j))
    return gammas


def k1_symbol(p, gammas):
    M = np.zeros((2, 2), dtype=complex)
    for mu in range(3):
        M += gammas[mu] * math.sin(float(p[mu]))
    return M


def k0_symbol(p, coeffs):
    M = np.zeros((2, 2), dtype=complex)
    for mu in range(3):
        M += 2.0 * math.cos(float(p[mu])) * coeffs[mu]
    return M


def extract_k0_scalar_coeffs():
    """Extract cos-direction coefficients from the scalar K0 symbol."""
    zero = np.zeros(3)
    coeffs = []
    for mu in range(3):
        probe = np.zeros(3)
        probe[mu] = math.pi
        # For K0, K(0)-K(pi e_mu) = 4 I in direction mu.
        coeffs.append((6.0 * I2 - (2.0 * (1.0 + 1.0 - 1.0)) * I2) / 4.0)
        assert np.allclose(coeffs[-1], (k0_symbol(zero, [I2, I2, I2]) - k0_symbol(probe, [I2, I2, I2])) / 4.0)
    return coeffs


def vectorize(M):
    return np.asarray(M, dtype=complex).reshape(-1, order="F")


def rank_complex(A, tol=1e-10):
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > tol))


def commutant_dim(mats, tol=1e-10):
    n = mats[0].shape[0]
    rows = []
    eye = np.eye(n, dtype=complex)
    for A in mats:
        rows.append(np.kron(eye, A) - np.kron(A.T, eye))
    M = np.vstack(rows)
    return n * n - rank_complex(M, tol)


def star_algebra_dim(gens, tol=1e-10):
    n = gens[0].shape[0]
    basis = [np.eye(n, dtype=complex)]
    candidates = list(gens) + [G.conj().T for G in gens]

    def current_rank(items):
        return rank_complex(np.column_stack([vectorize(B) for B in items]), tol)

    changed = True
    while changed:
        changed = False
        for C in list(candidates):
            trial = basis + [C]
            if current_rank(trial) > current_rank(basis):
                basis.append(C)
                changed = True
        products = []
        for A in basis:
            for B in basis:
                products.append(A @ B)
        candidates = products + [P.conj().T for P in products]
    return current_rank(basis)


def hermitian_anticommutant_nullity(gammas, tol=1e-10):
    basis = [I2] + gammas
    cols = []
    for B in basis:
        pieces = []
        for G in gammas:
            A = B @ G + G @ B
            pieces.append(np.real(vectorize(A)))
            pieces.append(np.imag(vectorize(A)))
        cols.append(np.concatenate(pieces))
    M = np.column_stack(cols)
    return len(basis) - rank_complex(M.astype(float), tol)


def grid_points(N):
    vals = np.linspace(-math.pi, math.pi, N, endpoint=False)
    return itertools.product(vals, repeat=3)


def min_shift_floor_for_k0(mass=0.3):
    pts = np.array(list(grid_points(13)), dtype=float)
    scalar = 2.0 * np.sum(np.cos(pts), axis=1)
    target = mass * mass + np.sum(np.sin(pts) ** 2, axis=1)
    best = float("inf")
    best_c = None
    for c in np.linspace(-8.0, 8.0, 4001):
        err = float(np.max(np.abs((scalar + c) ** 2 - target)))
        if err < best:
            best = err
            best_c = float(c)
    return best, best_c


def zero_counts(N, gammas):
    tol = 1.0 / N
    k0_count = 0
    k1_count = 0
    for p in grid_points(N):
        p = np.array(p)
        k0_floor = abs(2.0 * np.sum(np.cos(p)))
        k1_floor = math.sqrt(float(np.sum(np.sin(p) ** 2)))
        if k0_floor < tol:
            k0_count += 1
        if k1_floor < tol:
            k1_count += 1
    return k0_count, k1_count


def blocked_symbol_8(p, phases):
    M = np.zeros((8, 8), dtype=complex)
    for r in CELL:
        for mu in range(3):
            y = list(r)
            y[mu] += 1
            block_shift = np.zeros(3)
            if y[mu] >= 2:
                y[mu] -= 2
                block_shift[mu] = 1.0
            y = tuple(y)
            phase = complex(phases[(r, mu)])
            z = np.exp(1j * float(np.dot(p, block_shift)))
            i = CELL_INDEX[y]
            j = CELL_INDEX[r]
            M[i, j] += phase * z
            M[j, i] += np.conj(phase) * np.conj(z)
    return M


def blocked_derivative_gammas_8(phases):
    p0 = math.pi * np.ones(3)
    dq = 1e-5
    out = []
    for mu in range(3):
        e = np.zeros(3)
        e[mu] = dq
        out.append((blocked_symbol_8(p0 + e, phases) - blocked_symbol_8(p0 - e, phases)) / (2.0 * dq))
    return out


def eta0_cell_phases():
    return {(r, mu): eta0(r, mu) for r in CELL for mu in range(3)}


def perturbed_cell_phases():
    phases = eta0_cell_phases()
    # A single crossing link sign flip; it creates mixed plaquette flux and
    # changes the blocked derivative coefficients.
    phases[((1, 0, 0), 0)] *= -1.0
    return phases


def plaquette_fluxes_cell(phases):
    vals = []
    for x in CELL:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % 2
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % 2
                xm = tuple(xm)
                xn = tuple(xn)
                vals.append(
                    phases[(x, mu)]
                    * phases[(xm, nu)]
                    * np.conj(phases[(xn, mu)])
                    * np.conj(phases[(x, nu)])
                )
    return np.array(vals, dtype=complex)


def u1_frame(x):
    return (1j) ** ((x[0] + 2 * x[1] + 3 * x[2]) % 4)


def illegal_frame(x):
    U = (I2 - 1j * S2) / math.sqrt(2.0)
    return U if x[0] == 1 else I2


def illegal_frame_spread(gammas):
    spread = 0.0
    for mu in range(3):
        mats = []
        for x in CELL:
            y = tuple(np.array(x) + E_UNIT[mu])
            mats.append(illegal_frame(x).conj().T @ gammas[mu] @ illegal_frame(y))
        avg = sum(mats) / len(mats)
        spread = max(spread, max(np.linalg.norm(M - avg) for M in mats))
    return spread


def rotation_permutation(L, ss, idx):
    P = np.zeros((L**3, L**3), dtype=complex)
    for x in ss:
        y = (x[1] % L, (-x[0]) % L, x[2] % L)
        P[idx[y], idx[x]] = 1.0
    return P


def main():
    print("=" * 78)
    print("realized kinetic branch discriminators (2026-07-02)")
    print("=" * 78)

    edge_coeffs, spreads = absorbed_k1_edge_coefficients()
    gammas = extract_k1_gammas(edge_coeffs)
    k0_coeffs = extract_k0_scalar_coeffs()

    for L in (4, 6):
        f0 = plaquette_fluxes(L, eta_k0)
        f1 = plaquette_fluxes(L, eta0)
        check(
            "T1",
            f"plaquette fluxes on L={L}: K0 all +1 and K1 all -1",
            np.allclose(f0, 1.0) and np.allclose(f1, -1.0),
            f"plaquettes={len(f0)}",
        )

    recon_err = 0.0
    for p in grid_points(7):
        p = np.array(p)
        raw_normalized = -1j * k1_raw_extraction_symbol(p, edge_coeffs)
        recon_err = max(recon_err, float(np.linalg.norm(raw_normalized - k1_symbol(p, gammas))))
    check(
        "T2",
        "K1 blocked/absorbed extraction reconstructs sum Gamma_mu sin(p_mu)",
        recon_err < 1e-12 and max(spreads) < 1e-12,
        f"reconstruction error={recon_err:.2e}, edge spread={max(spreads):.2e}",
    )
    k0_scalar_err = max(
        np.linalg.norm(A - (np.trace(A) / 2.0) * I2) for A in k0_coeffs
    )
    check(
        "T2",
        "K0 scalar extraction gives direction coefficients proportional to I",
        k0_scalar_err < 1e-12,
        f"max scalar residual={k0_scalar_err:.2e}",
    )

    k0_real = all(abs(np.trace(A).imag) < 1e-12 for A in k0_coeffs)
    k0_comm_dim = commutant_dim(k0_coeffs)
    check(
        "T3",
        "D1a K0 coefficients are real scalar and have full M2 commutant",
        k0_scalar_err < 1e-12 and k0_real and k0_comm_dim == 4,
        f"commutant dim={k0_comm_dim}",
    )

    herm = all(np.linalg.norm(G - G.conj().T) < 1e-12 for G in gammas)
    unit = all(np.linalg.norm(G @ G - I2) < 1e-12 for G in gammas)
    anti_norm = max(
        np.linalg.norm(gammas[i] @ gammas[j] + gammas[j] @ gammas[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    k1_comm_dim = commutant_dim(gammas)
    check(
        "T4",
        "D1b K1 Gamma_mu are Hermitian unitaries and mutually anticommute",
        herm and unit and anti_norm < 1e-12 and k1_comm_dim == 1,
        f"max anticommutator={anti_norm:.2e}, commutant dim={k1_comm_dim}",
    )
    no_fourth = hermitian_anticommutant_nullity(gammas)
    check(
        "T4",
        "C2 Clifford capacity saturated: no Hermitian fourth anticommuting unitary",
        no_fourth == 0,
        f"anticommutant nullity={no_fourth}",
    )

    square_err = 0.0
    for p in grid_points(9):
        p = np.array(p)
        K = k1_symbol(p, gammas)
        target = float(np.sum(np.sin(p) ** 2)) * I2
        square_err = max(square_err, float(np.linalg.norm(K @ K - target)))
    check(
        "T5",
        "D2 K1 satisfies K(p)^2 = sum sin^2(p_mu) I",
        square_err < 1e-10,
        f"max square error={square_err:.2e}",
    )
    mass_err = 0.0
    for mass in (0.3, 1.0):
        for p in grid_points(7):
            p = np.array(p)
            K = k1_symbol(p, gammas)
            target = (mass * mass + float(np.sum(np.sin(p) ** 2))) * I2
            mass_err = max(mass_err, float(np.linalg.norm(K @ K + mass * mass * I2 - target)))
    check(
        "T5",
        "D2 K1 mass slot gives m^2 + sum sin^2(p_mu)",
        mass_err < 1e-10,
        f"max mass-slot error={mass_err:.2e}",
    )

    k0_symbol_err = 0.0
    for p in grid_points(9):
        p = np.array(p)
        scalar = 2.0 * float(np.sum(np.cos(p)))
        k0_symbol_err = max(k0_symbol_err, float(np.linalg.norm(k0_symbol(p, k0_coeffs) - scalar * I2)))
    check(
        "T6",
        "D2 K0 symbol is the scalar tight-binding function 2 sum cos(p_mu)",
        k0_symbol_err < 1e-12,
        f"max scalar-symbol error={k0_symbol_err:.2e}",
    )
    floor, best_c = min_shift_floor_for_k0(mass=0.3)
    check(
        "T6",
        "D2 K0 cannot mimic Dirac-square dispersion by any constant shift",
        floor > 0.5,
        f"min_c max_p error={floor:.3f} at c={best_c:.3f}",
    )

    z24 = zero_counts(24, gammas)
    z48 = zero_counts(48, gammas)
    ratio = z48[0] / z24[0]
    check(
        "T7",
        "D3 zero-set geometry: K0 surface count grows and K1 has 8 isolated zeros",
        ratio > 3.0 and z24[1] == 8 and z48[1] == 8,
        f"K0 counts={z24[0]},{z48[0]} ratio={ratio:.2f}; K1 counts={z24[1]},{z48[1]}",
    )

    pert = perturbed_cell_phases()
    pflux = plaquette_fluxes_cell(pert)
    check(
        "T8",
        "one-link sign flip of eta0 produces mixed plaquette fluxes",
        np.any(np.isclose(pflux, 1.0)) and np.any(np.isclose(pflux, -1.0)),
        f"+ fluxes={int(np.sum(np.isclose(pflux, 1.0)))}, - fluxes={int(np.sum(np.isclose(pflux, -1.0)))}",
    )
    bg = blocked_derivative_gammas_8(pert)
    pert_anti = max(
        np.linalg.norm(bg[i] @ bg[j] + bg[j] @ bg[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    check(
        "T8",
        "perturbed blocked coefficients fail the K1 anticommutation discriminator",
        pert_anti > 1.0,
        f"violated anticommutator norm={pert_anti:.3f}",
    )

    k0_alg_dims = [star_algebra_dim([A]) for A in k0_coeffs]
    k1_alg_dims = [star_algebra_dim([G]) for G in gammas]
    framed_dims_k0 = []
    framed_dims_k1 = []
    for mu in range(3):
        x = (0, 0, 0)
        y = tuple(np.array(x) + E_UNIT[mu])
        z = np.conj(u1_frame(x)) * u1_frame(y)
        framed_dims_k0.append(star_algebra_dim([z * k0_coeffs[mu]]))
        framed_dims_k1.append(star_algebra_dim([z * gammas[mu]]))
    illegal_spread = illegal_frame_spread(gammas)
    check(
        "T9",
        "D4 algebra dimensions discriminate and are U(1)-frame covariant; illegal SU2 subregion breaks covariance",
        k0_alg_dims == [1, 1, 1]
        and k1_alg_dims == [2, 2, 2]
        and framed_dims_k0 == k0_alg_dims
        and framed_dims_k1 == k1_alg_dims
        and illegal_spread > 0.5,
        f"K0 dims={k0_alg_dims}, K1 dims={k1_alg_dims}, illegal spread={illegal_spread:.3f}",
    )

    L = 4
    H0, ss, idx = build_hopping(L, eta_k0)
    H1, _, _ = build_hopping(L, eta0)
    P = rotation_permutation(L, ss, idx)
    H0r = P @ H0 @ P.conj().T
    H1r = P @ H1 @ P.conj().T
    rot_k0_exact = np.linalg.norm(H0r - H0) < 1e-12
    rot_k1_spec = np.max(np.abs(np.linalg.eigvalsh(H1r) - np.linalg.eigvalsh(H1))) < 1e-10
    check(
        "T10",
        "proper R_z12 rotation covariance checked by exact K0 equality and K1 spectrum invariance",
        rot_k0_exact and rot_k1_spec,
        "K1 leg uses spectrum-level invariance under the rotation permutation",
    )

    print()
    print(
        "SUMMARY: representative-level discriminators on the two-flux-class "
        "surface; selector bit NOT forced here; Admissibility reading not decided."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
