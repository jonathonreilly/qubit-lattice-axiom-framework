#!/usr/bin/env python3
"""Gauged-background invariance of the realized kinetic branch selection.

Deterministic, numpy only, no network, no cache writes.

The K0/K1 phase conventions and absorbing-frame coefficient extraction mirror
scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py and the
three realized-kinetic-branch sibling runners.  Legal gauge links act on the
lattice/color tensor factor only.  The qubit-factor coefficients are recovered
from gauged hop blocks by operator-Schmidt factor analysis before comparison.

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
SQRT2 = math.sqrt(2.0)


def eta0(x, mu):
    """Kawamoto-Smit signs, matching the parent kinetic-class runner."""
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** (x[0] % 2)
    return (-1.0) ** ((x[0] + x[1]) % 2)


def eta_k0(_x, _mu):
    return 1.0


def sites(L):
    return list(itertools.product(range(L), repeat=3))


def add_mod(x, mu, L):
    y = list(x)
    y[mu] = (y[mu] + 1) % L
    return tuple(y)


def Tmat(x):
    out = I2.copy()
    for mu, power in enumerate(x):
        if power % 2:
            out = out @ SIG[mu]
    return out


def absorbed_k1_edge_coefficients(tfun=eta0):
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


def grid_points(N):
    vals = np.linspace(-math.pi, math.pi, N, endpoint=False)
    return itertools.product(vals, repeat=3)


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


def projector_ok(P, rank, tol=1e-8):
    eig = np.linalg.eigvalsh((P + P.conj().T) / 2.0)
    return (
        np.linalg.norm(P - P.conj().T) < tol
        and np.linalg.norm(P @ P - P) < tol
        and int(np.sum(eig > 0.5)) == rank
    )


def availability_gap(coeff):
    projectors = [P for _, P in spectral_projectors_normal_2(coeff)]
    if len(projectors) < 2:
        return 0.0
    return max(
        float(np.linalg.norm(P - Q))
        for i, P in enumerate(projectors)
        for Q in projectors[i + 1 :]
    )


def phase_aligned_distance(A, B):
    z = np.trace(B.conj().T @ A)
    if abs(z) < 1e-12:
        return float(np.linalg.norm(A - B))
    return float(np.linalg.norm(A - (z / abs(z)) * B))


def normalize_factor(A, dim):
    scale = math.sqrt(max(float(np.real(np.trace(A.conj().T @ A))) / dim, 0.0))
    if scale < 1e-14:
        return A.copy()
    return A / scale


def random_su2(rng):
    q = rng.normal(size=4)
    q = q / np.linalg.norm(q)
    a, b, c, d = q
    return np.array(
        [[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]],
        dtype=complex,
    )


def make_links(L, color_dim, seed, kind):
    rng = np.random.default_rng(seed)
    links = {}
    for x in sites(L):
        for mu in range(3):
            if kind == "identity":
                U = np.eye(color_dim, dtype=complex)
            elif kind == "u1":
                theta = float(rng.uniform(0.0, 2.0 * math.pi))
                U = np.array([[np.exp(1j * theta)]], dtype=complex)
            elif kind == "su2":
                U = random_su2(rng)
            else:
                raise ValueError(kind)
            links[(x, mu)] = U
    return links


def block_slice(site, sidx, block_dim):
    start = sidx[site] * block_dim
    return slice(start, start + block_dim)


def build_gauged_hop_operator(L, links, coeffs, color_dim):
    ss = sites(L)
    sidx = {s: i for i, s in enumerate(ss)}
    block_dim = color_dim * 2
    H = np.zeros((len(ss) * block_dim, len(ss) * block_dim), dtype=complex)
    for x in ss:
        for mu in range(3):
            y = add_mod(x, mu, L)
            block = np.kron(links[(x, mu)], coeffs[mu])
            rs = block_slice(y, sidx, block_dim)
            cs = block_slice(x, sidx, block_dim)
            H[rs, cs] += block
            H[cs, rs] += block.conj().T
    return H, ss, sidx


def extract_link_block(H, x, mu, L, sidx, color_dim):
    y = add_mod(x, mu, L)
    block_dim = color_dim * 2
    return H[
        block_slice(y, sidx, block_dim),
        block_slice(x, sidx, block_dim),
    ]


def operator_schmidt_factor(block, color_dim):
    tensor = block.reshape(color_dim, 2, color_dim, 2)
    rearranged = tensor.transpose(0, 2, 1, 3).reshape(color_dim * color_dim, 4)
    U, s, Vh = np.linalg.svd(rearranged, full_matrices=False)
    A = (math.sqrt(float(s[0])) * U[:, 0]).reshape(color_dim, color_dim)
    B = (math.sqrt(float(s[0])) * Vh[0, :]).reshape(2, 2)
    rank1 = s[0] * np.outer(U[:, 0], Vh[0, :])
    residual = float(np.linalg.norm(rearranged - rank1) / max(np.linalg.norm(rearranged), 1e-14))
    tail = float(np.linalg.norm(s[1:]) / max(float(s[0]), 1e-14))
    return A, B, residual, tail


def analyze_case(L, links, coeffs, expected_coeffs, color_dim):
    H, ss, sidx = build_gauged_hop_operator(L, links, coeffs, color_dim)
    factors = {mu: [] for mu in range(3)}
    residuals = []
    tails = []
    color_unitarity = []
    expected_errors = []
    for x in ss:
        for mu in range(3):
            block = extract_link_block(H, x, mu, L, sidx, color_dim)
            A, B, residual, tail = operator_schmidt_factor(block, color_dim)
            A_unit = normalize_factor(A, color_dim)
            B_unit = normalize_factor(B, 2)
            factors[mu].append(B_unit)
            residuals.append(residual)
            tails.append(tail)
            color_unitarity.append(float(np.linalg.norm(A_unit.conj().T @ A_unit - np.eye(color_dim))))
            expected_errors.append(phase_aligned_distance(B_unit, expected_coeffs[mu]))
    return {
        "H": H,
        "factors": factors,
        "max_factor_residual": max(residuals),
        "max_tail_ratio": max(tails),
        "max_color_unitarity": max(color_unitarity),
        "max_expected_error": max(expected_errors),
    }


def link_family_spread(factors):
    spreads = []
    for mu in range(3):
        ref = factors[mu][0]
        spreads.append(max(phase_aligned_distance(C, ref) for C in factors[mu]))
    return spreads


def family_dims(factors):
    return [[star_algebra_dim([C]) for C in factors[mu]] for mu in range(3)]


def family_gaps(factors):
    return [[availability_gap(C) for C in factors[mu]] for mu in range(3)]


def dims_all(summary, target):
    dims = family_dims(summary["factors"])
    return all(all(d == target for d in per_mu) for per_mu in dims), dims


def gaps_all(summary, target, tol=1e-8):
    gaps = family_gaps(summary["factors"])
    return all(all(abs(g - target) < tol for g in per_mu) for per_mu in gaps), gaps


def representative_family(factors):
    return [factors[mu][0] for mu in range(3)]


def anticommutator_norm(reps):
    return max(
        float(np.linalg.norm(reps[i] @ reps[j] + reps[j] @ reps[i]))
        for i in range(3)
        for j in range(i + 1, 3)
    )


def dirac_square_error(gammas):
    err = 0.0
    for p in grid_points(7):
        p = np.array(p)
        K = k1_symbol(p, gammas)
        target = float(np.sum(np.sin(p) ** 2)) * I2
        err = max(err, float(np.linalg.norm(K @ K - target)))
    return err


def scalar_plaquette_phases(L, links, base_tfun):
    vals = []
    for x in sites(L):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = add_mod(x, mu, L)
                xn = add_mod(x, nu, L)
                U = (
                    links[(x, mu)][0, 0]
                    * links[(xm, nu)][0, 0]
                    * np.conj(links[(xn, mu)][0, 0])
                    * np.conj(links[(x, nu)][0, 0])
                )
                z2 = (
                    base_tfun(x, mu)
                    * base_tfun(xm, nu)
                    * np.conj(base_tfun(xn, mu))
                    * np.conj(base_tfun(x, nu))
                )
                vals.append(complex(U * z2))
    return np.array(vals, dtype=complex)


def su2_plaquette_traces(L, links):
    vals = []
    for x in sites(L):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = add_mod(x, mu, L)
                xn = add_mod(x, nu, L)
                W = (
                    links[(x, mu)]
                    @ links[(xm, nu)]
                    @ links[(xn, mu)].conj().T
                    @ links[(x, nu)].conj().T
                )
                vals.append(np.trace(W) / 2.0)
    return np.array(vals, dtype=complex)


def z2_fluxes(L, tfun):
    links = make_links(L, 1, 0, "identity")
    return scalar_plaquette_phases(L, links, tfun)


def survives_variation(summary):
    dims2, _ = dims_all(summary, 2)
    gaps2, _ = gaps_all(summary, SQRT2)
    return dims2 and gaps2


def illegal_frame(x):
    U = (I2 - 1j * S2) / math.sqrt(2.0)
    return U if x[0] == 1 else I2


def illegal_qubit_coeffs(coeffs):
    out = {mu: [] for mu in range(3)}
    for x in CELL:
        for mu in range(3):
            y = tuple(np.array(x) + E_UNIT[mu])
            out[mu].append(illegal_frame(x).conj().T @ coeffs[mu] @ illegal_frame(y))
    return out


def main():
    print("=" * 78)
    print("realized kinetic branch selection under fixed gauged backgrounds (2026-07-02)")
    print("=" * 78)

    edge_coeffs, edge_spreads = absorbed_k1_edge_coefficients()
    gammas = extract_k1_gammas(edge_coeffs)
    k0_coeffs = [I2, I2, I2]
    L = 3

    herm = all(np.linalg.norm(G - G.conj().T) < 1e-12 for G in gammas)
    unit = all(np.linalg.norm(G @ G - I2) < 1e-12 for G in gammas)
    anti = anticommutator_norm(gammas)
    check(
        "T0",
        "sibling absorbing-frame Gamma_mu family is reconstructed before gauging",
        max(edge_spreads) < 1e-12 and herm and unit and anti < 1e-12,
        f"edge spread={max(edge_spreads):.2e}, anticommutator={anti:.2e}",
    )

    legal_summaries = []
    u1_boundary_spreads = []
    for seed in (11, 17, 23):
        links = make_links(L, 1, seed, "u1")
        k0 = analyze_case(L, links, k0_coeffs, k0_coeffs, 1)
        k1 = analyze_case(L, links, gammas, gammas, 1)
        legal_summaries.append(("U1", seed, k0, k1))
        f0 = scalar_plaquette_phases(L, links, eta_k0)
        f1 = scalar_plaquette_phases(L, links, eta0)
        u1_boundary_spreads.append(float(np.max(np.abs(f0 - 1.0))))
        u1_boundary_spreads.append(float(np.max(np.abs(f1 + 1.0))))

    u1_factor_ok = all(
        max(k0["max_factor_residual"], k1["max_factor_residual"]) < 1e-12
        and max(k0["max_tail_ratio"], k1["max_tail_ratio"]) < 1e-12
        and max(k0["max_color_unitarity"], k1["max_color_unitarity"]) < 1e-12
        and max(k0["max_expected_error"], k1["max_expected_error"]) < 1e-10
        for kind, _seed, k0, k1 in legal_summaries
        if kind == "U1"
    )
    check(
        "T1",
        "random fixed U(1) backgrounds factor as recovered color link tensor qubit coefficient",
        u1_factor_ok,
        "seeds=11,17,23; extraction uses operator-Schmidt rank-one residuals",
    )

    u1_k0_ok = True
    u1_k1_ok = True
    max_u1_anti = 0.0
    max_u1_spread = 0.0
    for kind, _seed, k0, k1 in legal_summaries:
        if kind != "U1":
            continue
        d0, _ = dims_all(k0, 1)
        g0, _ = gaps_all(k0, 0.0)
        d1, _ = dims_all(k1, 2)
        g1, _ = gaps_all(k1, SQRT2)
        max_u1_anti = max(max_u1_anti, anticommutator_norm(representative_family(k1["factors"])))
        max_u1_spread = max(max_u1_spread, max(link_family_spread(k1["factors"])))
        u1_k0_ok = u1_k0_ok and d0 and g0
        u1_k1_ok = u1_k1_ok and d1 and g1
    check(
        "T1",
        "U(1) backgrounds preserve K0 vacuity and K1 direction-tagged variation",
        u1_k0_ok and u1_k1_ok and max_u1_anti < 1e-12 and max_u1_spread < 1e-10,
        f"K1 max anticommutator={max_u1_anti:.2e}, max link spread={max_u1_spread:.2e}",
    )

    check(
        "T2",
        "U(1) boundary exhibit: plaquette flux is background-dependent off the U=1 slice",
        min(u1_boundary_spreads) > 0.1,
        f"min max deviation from Z2 anchors={min(u1_boundary_spreads):.3f}",
    )

    su2_links = make_links(L, 2, 31, "su2")
    su2_k0 = analyze_case(L, su2_links, k0_coeffs, k0_coeffs, 2)
    su2_k1 = analyze_case(L, su2_links, gammas, gammas, 2)
    legal_summaries.append(("SU2", 31, su2_k0, su2_k1))
    su2_factor_ok = (
        max(su2_k0["max_factor_residual"], su2_k1["max_factor_residual"]) < 1e-12
        and max(su2_k0["max_tail_ratio"], su2_k1["max_tail_ratio"]) < 1e-12
        and max(su2_k0["max_color_unitarity"], su2_k1["max_color_unitarity"]) < 1e-12
        and max(su2_k0["max_expected_error"], su2_k1["max_expected_error"]) < 1e-10
    )
    check(
        "T1",
        "random fixed SU(2) color links factor as recovered color matrix tensor qubit coefficient",
        su2_factor_ok,
        f"max residual={max(su2_k0['max_factor_residual'], su2_k1['max_factor_residual']):.2e}",
    )

    su2_d0, su2_dims0 = dims_all(su2_k0, 1)
    su2_g0, _ = gaps_all(su2_k0, 0.0)
    su2_d1, su2_dims1 = dims_all(su2_k1, 2)
    su2_g1, _ = gaps_all(su2_k1, SQRT2)
    su2_anti = anticommutator_norm(representative_family(su2_k1["factors"]))
    su2_spread = max(link_family_spread(su2_k1["factors"]))
    check(
        "T1",
        "SU(2) color background preserves algebra dimensions, K1 anticommutation, and sqrt(2) gaps",
        su2_d0 and su2_g0 and su2_d1 and su2_g1 and su2_anti < 1e-12 and su2_spread < 1e-10,
        f"K0 dim sample={[row[0] for row in su2_dims0]}, K1 dim sample={[row[0] for row in su2_dims1]}",
    )

    su2_traces = su2_plaquette_traces(L, su2_links)
    check(
        "T2",
        "SU(2) boundary exhibit: Wilson plaquette traces vary with the fixed background",
        float(np.max(np.abs(su2_traces - su2_traces[0]))) > 0.1,
        f"trace spread={float(np.max(np.abs(su2_traces - su2_traces[0]))):.3f}",
    )

    selection_ok = True
    for _kind, _seed, k0, k1 in legal_summaries:
        d0, _ = dims_all(k0, 1)
        g0, _ = gaps_all(k0, 0.0)
        selection_ok = selection_ok and d0 and g0 and (not survives_variation(k0)) and survives_variation(k1)
    check(
        "T2",
        "clarified Admissibility variation still selects K1 for every fixed legal background tested",
        selection_ok,
        "legal cases: U(1) seeds 11/17/23 and SU(2) seed 31",
    )

    id_links = make_links(L, 1, 0, "identity")
    id_k0 = analyze_case(L, id_links, k0_coeffs, k0_coeffs, 1)
    id_k1 = analyze_case(L, id_links, gammas, gammas, 1)
    id_d0, _ = dims_all(id_k0, 1)
    id_g0, _ = gaps_all(id_k0, 0.0)
    id_d1, _ = dims_all(id_k1, 2)
    id_g1, _ = gaps_all(id_k1, SQRT2)
    check(
        "T4",
        "zero-background regression reproduces sibling K0/K1 algebra dimensions and variation gaps",
        id_d0 and id_g0 and id_d1 and id_g1,
        "K0 gaps=0; K1 gaps=sqrt(2) on each axis",
    )

    z2_k0 = z2_fluxes(4, eta_k0)
    z2_k1 = z2_fluxes(4, eta0)
    check(
        "T4",
        "zero-background regression reproduces the sibling Z2 flux anchors",
        np.allclose(z2_k0, 1.0) and np.allclose(z2_k1, -1.0),
        f"K0 plaquettes={len(z2_k0)}, K1 plaquettes={len(z2_k1)}",
    )

    id_anti = anticommutator_norm(representative_family(id_k1["factors"]))
    id_square = dirac_square_error(representative_family(id_k1["factors"]))
    check(
        "T4",
        "zero-background K1 carries the sibling nonzero first-order Dirac-square kinetic carrier",
        id_anti < 1e-12 and id_square < 1e-10,
        f"anticommutator={id_anti:.2e}, square error={id_square:.2e}",
    )

    illegal_k0 = illegal_qubit_coeffs(k0_coeffs)
    illegal_k1 = illegal_qubit_coeffs(gammas)
    illegal_k0_dims = [[star_algebra_dim([C]) for C in illegal_k0[mu]] for mu in range(3)]
    illegal_k0_gaps = [[availability_gap(C) for C in illegal_k0[mu]] for mu in range(3)]
    illegal_creates_k0_variation = any(
        d == 2 and abs(g - SQRT2) < 1e-8
        for mu in range(3)
        for d, g in zip(illegal_k0_dims[mu], illegal_k0_gaps[mu])
    )
    check(
        "T3",
        "illegal qubit-factor background can create apparent K0 variation outside the licensed gauge action",
        illegal_creates_k0_variation,
        f"K0 illegal dim rows={illegal_k0_dims}",
    )

    illegal_k1_spreads = []
    for mu in range(3):
        ref = illegal_k1[mu][0]
        illegal_k1_spreads.append(max(phase_aligned_distance(C, ref) for C in illegal_k1[mu]))
    check(
        "T3",
        "illegal sub-region SU(2) action on the direction-tag factor breaks uniform K1 coefficients",
        max(illegal_k1_spreads) > 0.5,
        f"direction spreads={[round(s, 3) for s in illegal_k1_spreads]}",
    )

    print()
    print(
        "SUMMARY: fixed-background gauged surface only; legal gauge links act on "
        "lattice/color factors and leave the qubit availability-variation selector "
        "unchanged. Link integration, interacting measures, and gauged log-transfer "
        "locality are not tested here."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
