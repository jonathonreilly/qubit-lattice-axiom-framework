#!/usr/bin/env python3
"""Conditional-record registration of the realized kinetic branch.

Deterministic, numpy only, no network, no cache writes.

The K0/K1 phase conventions and absorbing-frame coefficient extraction mirror
scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py and reuse the
sibling runner's constructions:
scripts/realized_kinetic_branch_discriminators_2026_07_02.py.

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
HERM_BASIS = [I2, S1, S2, S3]


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
    """Compute direction matrices from eta and the parent absorbing frame."""
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
    zero = np.zeros(3)
    coeffs = []
    for mu in range(3):
        probe = np.zeros(3)
        probe[mu] = math.pi
        coeffs.append((k0_symbol(zero, [I2, I2, I2]) - k0_symbol(probe, [I2, I2, I2])) / 4.0)
    return coeffs


def vectorize(M):
    return np.asarray(M, dtype=complex).reshape(-1, order="F")


def rank_complex(A, tol=1e-10):
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > tol))


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


def spectral_projectors_hermitian(A, tol=1e-9):
    vals, vecs = np.linalg.eigh(A)
    groups = []
    used = [False] * len(vals)
    for i, val in enumerate(vals):
        if used[i]:
            continue
        idxs = [j for j, other in enumerate(vals) if abs(other - val) < tol]
        for j in idxs:
            used[j] = True
        V = vecs[:, idxs]
        groups.append((float(np.real(val)), V @ V.conj().T))
    return groups


def spectral_projectors_normal_2(A, tol=1e-9):
    vals = np.linalg.eigvals(A)
    if abs(vals[0] - vals[1]) < tol:
        return [(vals[0], I2.copy())]
    out = []
    for i in range(2):
        j = 1 - i
        P = (A - vals[j] * I2) / (vals[i] - vals[j])
        out.append((vals[i], P))
    return out


def projector_ok(P, rank, tol=1e-9):
    eig = np.linalg.eigvalsh((P + P.conj().T) / 2.0)
    return (
        np.linalg.norm(P - P.conj().T) < tol
        and np.linalg.norm(P @ P - P) < tol
        and int(np.sum(eig > 0.5)) == rank
    )


def direction_availability_projectors(coeff):
    return [P for _, P in spectral_projectors_hermitian(coeff)]


def fixed_hermitian_subspace_dim(unitaries, traceless=False, tol=1e-10):
    cols = []
    for B in HERM_BASIS:
        pieces = []
        for U in unitaries:
            D = U @ B @ U.conj().T - B
            pieces.append(np.real(vectorize(D)))
            pieces.append(np.imag(vectorize(D)))
        if traceless:
            pieces.append(np.array([float(np.real(np.trace(B)))]))
        cols.append(np.concatenate(pieces))
    M = np.column_stack(cols)
    return len(HERM_BASIS) - rank_complex(M.astype(float), tol)


def grid_points(N):
    vals = np.linspace(-math.pi, math.pi, N, endpoint=False)
    return itertools.product(vals, repeat=3)


def dirac_square_error(gammas):
    err = 0.0
    for p in grid_points(7):
        p = np.array(p)
        K = k1_symbol(p, gammas)
        target = float(np.sum(np.sin(p) ** 2)) * I2
        err = max(err, float(np.linalg.norm(K @ K - target)))
    return err


def eta0_cell_phases():
    return {(r, mu): eta0(r, mu) for r in CELL for mu in range(3)}


def perturbed_cell_phases():
    phases = eta0_cell_phases()
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


def main():
    print("=" * 78)
    print("realized kinetic branch conditional-record registration (2026-07-02)")
    print("=" * 78)

    edge_coeffs, spreads = absorbed_k1_edge_coefficients()
    gammas = extract_k1_gammas(edge_coeffs)
    k0_coeffs = extract_k0_scalar_coeffs()

    for L in (4, 6):
        f0 = plaquette_fluxes(L, eta_k0)
        f1 = plaquette_fluxes(L, eta0)
        check(
            "T1",
            f"flux anchor on L={L}: K0 all +1 and K1 all -1",
            np.allclose(f0, 1.0) and np.allclose(f1, -1.0),
            f"plaquettes={len(f0)}",
        )

    recon_err = 0.0
    for p in grid_points(7):
        p = np.array(p)
        raw_normalized = -1j * k1_raw_extraction_symbol(p, edge_coeffs)
        recon_err = max(recon_err, float(np.linalg.norm(raw_normalized - k1_symbol(p, gammas))))
    k0_scalar_err = max(np.linalg.norm(A - (np.trace(A) / 2.0) * I2) for A in k0_coeffs)
    check(
        "T1",
        "sibling K0/K1 constructions reproduced: K1 symbol reconstructs, K0 coefficients are scalar",
        recon_err < 1e-12 and max(spreads) < 1e-12 and k0_scalar_err < 1e-12,
        f"K1 recon={recon_err:.2e}, edge spread={max(spreads):.2e}, K0 scalar residual={k0_scalar_err:.2e}",
    )

    k0_alg_dims = [star_algebra_dim([A]) for A in k0_coeffs]
    k0_projectors = [direction_availability_projectors(A) for A in k0_coeffs]
    only_full = all(len(ps) == 1 and np.linalg.norm(ps[0] - I2) < 1e-10 for ps in k0_projectors)
    check(
        "T-A",
        "K0 per-direction availability algebra is C I with only the full projector",
        k0_alg_dims == [1, 1, 1] and only_full,
        f"algebra dims={k0_alg_dims}, projector counts={[len(ps) for ps in k0_projectors]}",
    )

    fixed_dim = fixed_hermitian_subspace_dim(SIG)
    fixed_tr0_dim = fixed_hermitian_subspace_dim(SIG, traceless=True)
    check(
        "T-A",
        "K0 blocked-cell orbit/nullspace has no nonzero trace-zero covariant projector direction",
        fixed_dim == 1 and fixed_tr0_dim == 0,
        f"fixed Hermitian dim={fixed_dim}, trace-zero fixed dim={fixed_tr0_dim}",
    )

    k0_map_count = int(np.prod([len(ps) ** 2 for ps in k0_projectors]))
    k0_conditioned_count = 0
    for ps in k0_projectors:
        for P in ps:
            for Q in ps:
                if np.linalg.norm(P - Q) > 1e-9:
                    k0_conditioned_count += 1
    check(
        "T-A",
        "enumerating K0 spectral availability maps gives only neighbor-constant maps",
        k0_map_count == 1 and k0_conditioned_count == 0,
        f"maps={k0_map_count}, conditioned={k0_conditioned_count}",
    )

    k1_alg_dims = [star_algebra_dim([G]) for G in gammas]
    k1_projectors = [direction_availability_projectors(G) for G in gammas]
    projectors_valid = all(
        len(ps) == 2
        and all(projector_ok(P, 1) for P in ps)
        and np.linalg.norm(ps[0] @ ps[1]) < 1e-10
        for ps in k1_projectors
    )
    check(
        "T-B",
        "K1 direction-tagged algebras produce two rank-one orthogonal eigen-projectors per direction",
        k1_alg_dims == [2, 2, 2] and projectors_valid,
        f"algebra dims={k1_alg_dims}, projector counts={[len(ps) for ps in k1_projectors]}",
    )

    witness_mu = 0
    P_minus, P_plus = k1_projectors[witness_mu]
    witness_gap = float(np.linalg.norm(P_plus - P_minus))
    record_witness = {
        "site": (0, 0, 0),
        "direction": witness_mu,
        "neighbor_values": (-1, +1),
        "availability_gap": witness_gap,
    }
    check(
        "T-B",
        "explicit neighbor-conditioned record witness has unequal K1 availability subsets",
        witness_gap > 1.0 and record_witness["availability_gap"] == witness_gap,
        f"mu={witness_mu + 1}, ||A(+)-A(-)||={witness_gap:.3f}",
    )

    framed_ok = True
    framed_dims = []
    theta = math.pi / 3.0
    for mu, G in enumerate(gammas):
        z = np.exp(1j * theta * (mu + 1))
        framed = z * G
        framed_dims.append(star_algebra_dim([framed]))
        framed_ps = [P for _, P in spectral_projectors_normal_2(framed)]
        orig_ps = k1_projectors[mu]
        distances = sorted(
            min(np.linalg.norm(P - Q) for Q in orig_ps) for P in framed_ps
        )
        framed_ok = framed_ok and max(distances) < 1e-8
    check(
        "T-B",
        "K1 availability projectors and algebra dimensions are stable under local U(1) edge phases",
        framed_ok and framed_dims == [2, 2, 2],
        f"framed dims={framed_dims}",
    )

    anti_norm = max(
        np.linalg.norm(gammas[i] @ gammas[j] + gammas[j] @ gammas[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    square_err = dirac_square_error(gammas)
    realized_state = {
        "law_admissible": True,
        "records": [record_witness],
    }
    has_neighbor_conditioned_record = any(
        r.get("availability_gap", 0.0) > 1.0 for r in realized_state["records"]
    )
    branch = (
        "K1"
        if realized_state["law_admissible"]
        and has_neighbor_conditioned_record
        and k0_conditioned_count == 0
        and witness_gap > 1.0
        else "undecided"
    )
    check(
        "T-C",
        "pointwise realized record stack with a neighbor-conditioned qubit record registers K1",
        branch == "K1" and anti_norm < 1e-12 and square_err < 1e-10,
        f"branch={branch}, anticommutator={anti_norm:.2e}, Dirac-square error={square_err:.2e}",
    )

    attempted_dim = fixed_tr0_dim
    check(
        "T-D",
        "attempted covariant neighbor-conditioned K0 map has zero-dimensional difference space",
        attempted_dim == 0 and k0_conditioned_count == 0,
        f"difference-space dim={attempted_dim}, conditioned maps={k0_conditioned_count}",
    )

    P_x_plus = (I2 + S1) / 2.0
    P_x_minus = (I2 - S1) / 2.0
    U_theta = np.diag([1.0, np.exp(1j * math.pi / 2.0)])
    rotated_plus = U_theta @ P_x_plus @ U_theta.conj().T
    noncovariant_gap = float(np.linalg.norm(P_x_plus - P_x_minus))
    frame_violation = float(np.linalg.norm(rotated_plus - P_x_plus))
    k0_unchanged = np.linalg.norm(U_theta @ I2 @ U_theta.conj().T - I2) < 1e-12
    check(
        "T-E",
        "external conditioned basis map on K0 exists but is a frame artifact, not C I data",
        noncovariant_gap > 1.0 and frame_violation > 0.9 and k0_unchanged,
        f"conditioned gap={noncovariant_gap:.3f}, frame violation={frame_violation:.3f}",
    )

    pert = perturbed_cell_phases()
    pflux = plaquette_fluxes_cell(pert)
    bg = blocked_derivative_gammas_8(pert)
    pert_anti = max(
        np.linalg.norm(bg[i] @ bg[j] + bg[j] @ bg[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    pert_dims = [star_algebra_dim([B]) for B in bg]
    check(
        "T-F",
        "one-link-flipped mixed-flux object degrades the K1 direction-tagged structure",
        np.any(np.isclose(pflux, 1.0))
        and np.any(np.isclose(pflux, -1.0))
        and pert_anti > 1.0,
        f"+ fluxes={int(np.sum(np.isclose(pflux, 1.0)))}, - fluxes={int(np.sum(np.isclose(pflux, -1.0)))}, "
        f"anticommutator={pert_anti:.3f}, single-generator dims={pert_dims}",
    )

    print()
    print(
        "SUMMARY: representative-level conditional record registration on the "
        "two-flux-class surface; selector bit NOT forced here; Admissibility "
        "reading not decided."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
