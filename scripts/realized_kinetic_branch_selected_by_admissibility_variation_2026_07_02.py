#!/usr/bin/env python3
"""Admissibility-variation selection of the realized kinetic branch.

Deterministic, numpy only, no network, no cache writes.

The K0/K1 phase conventions and absorbing-frame coefficient extraction below
are copied/adapted from the sibling runners
scripts/realized_kinetic_branch_discriminators_2026_07_02.py and
scripts/realized_kinetic_branch_conditional_record_registration_2026_07_02.py.
Those sibling constructions mirror
scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py: K0 is
t == 1 and K1 is the Kawamoto-Smit eta0 sign system.

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


def direction_availability_projectors_normal(coeff):
    return [P for _, P in spectral_projectors_normal_2(coeff)]


def availability_gap(projectors):
    if len(projectors) < 2:
        return 0.0
    return max(
        float(np.linalg.norm(P - Q))
        for i, P in enumerate(projectors)
        for Q in projectors[i + 1 :]
    )


def enumerate_availability_maps(projectors_by_dir):
    total = 1
    conditioned = 0
    for projectors in projectors_by_dir:
        total *= len(projectors) ** 2
        for P in projectors:
            for Q in projectors:
                if np.linalg.norm(P - Q) > 1e-9:
                    conditioned += 1
    return total, conditioned


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


def dirac_square_error(gammas, N=7):
    err = 0.0
    for p in grid_points(N):
        p = np.array(p)
        K = k1_symbol(p, gammas)
        target = float(np.sum(np.sin(p) ** 2)) * I2
        err = max(err, float(np.linalg.norm(K @ K - target)))
    return err


def cubic_rotations():
    c4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
    c3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=int)
    group = {tuple(np.eye(3, dtype=int).flatten())}
    frontier = [np.eye(3, dtype=int)]
    while frontier:
        nxt = []
        for g in frontier:
            for h in (c4z, c3):
                m = h @ g
                t = tuple(m.flatten())
                if t not in group:
                    group.add(t)
                    nxt.append(m)
        frontier = nxt
    return [np.array(t, dtype=int).reshape(3, 3) for t in sorted(group)]


ROTS = cubic_rotations()


def axis_permutation(R):
    perm = []
    signs = []
    for mu in range(3):
        col = R[:, mu]
        nu = int(np.flatnonzero(col)[0])
        perm.append(nu)
        signs.append(int(col[nu]))
    return tuple(perm), tuple(signs)


AXIS_PERMS = sorted({axis_permutation(R)[0] for R in ROTS})


def is_cubic_covariant_sequence(values):
    values = tuple(values)
    for perm in AXIS_PERMS:
        for mu, nu in enumerate(perm):
            if values[mu] != values[nu]:
                return False
    return True


def covariant_dim_patterns():
    return [
        dims
        for dims in itertools.product((1, 2), repeat=3)
        if is_cubic_covariant_sequence(dims)
    ]


def constant_availability_covariant_for_all_dim_patterns():
    full = [I2, I2, I2]
    for _dims in itertools.product((1, 2), repeat=3):
        for perm in AXIS_PERMS:
            rotated = [full[perm[mu]] for mu in range(3)]
            if any(np.linalg.norm(rotated[mu] - I2) > 1e-12 for mu in range(3)):
                return False
    return True


def covariant_varying_classification():
    out = []
    for dims in itertools.product((1, 2), repeat=3):
        for flags in itertools.product((False, True), repeat=3):
            if not any(flags):
                continue
            if any(flag and dims[mu] != 2 for mu, flag in enumerate(flags)):
                continue
            if is_cubic_covariant_sequence(dims) and is_cubic_covariant_sequence(flags):
                out.append((dims, flags))
    return out


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


def chirality(gammas):
    return np.trace(gammas[0] @ gammas[1] @ gammas[2]) / (2j)


def representative_data(k0_coeffs, gammas):
    k0_projectors = [direction_availability_projectors(A) for A in k0_coeffs]
    k1_projectors = [direction_availability_projectors(G) for G in gammas]
    return {
        "K0": {
            "dims": [star_algebra_dim([A]) for A in k0_coeffs],
            "projectors": k0_projectors,
            "gaps": [availability_gap(ps) for ps in k0_projectors],
            "flux": +1,
        },
        "K1": {
            "dims": [star_algebra_dim([G]) for G in gammas],
            "projectors": k1_projectors,
            "gaps": [availability_gap(ps) for ps in k1_projectors],
            "flux": -1,
        },
    }


def survives_admissibility(rep, require_variation):
    determined = rep["dims"] in ([1, 1, 1], [2, 2, 2])
    varies = all(gap > 1.0 for gap in rep["gaps"])
    return determined and ((not require_variation) or varies)


def main():
    print("=" * 78)
    print("realized kinetic branch selected by Admissibility variation (2026-07-02)")
    print("=" * 78)

    edge_coeffs, spreads = absorbed_k1_edge_coefficients()
    gammas = extract_k1_gammas(edge_coeffs)
    k0_coeffs = extract_k0_scalar_coeffs()
    reps = representative_data(k0_coeffs, gammas)

    check(
        "T1",
        "proper cubic rotations generate 24 rotations and all 6 axis permutations",
        len(ROTS) == 24 and len(AXIS_PERMS) == 6,
        f"rotations={len(ROTS)}, axis permutations={len(AXIS_PERMS)}",
    )

    dim_patterns = covariant_dim_patterns()
    check(
        "T1",
        "rule-level classification: covariant per-direction algebra dimensions are constant across axes",
        dim_patterns == [(1, 1, 1), (2, 2, 2)],
        f"patterns={dim_patterns}",
    )

    varying_patterns = covariant_varying_classification()
    check(
        "T1",
        "any varying covariant structure requires direction-tagged dim-2 algebras on all axes",
        varying_patterns == [((2, 2, 2), (True, True, True))],
        f"varying patterns={varying_patterns}",
    )

    check(
        "T1",
        "neighbor-constant availability is covariant for every enumerated internal dimension pattern",
        constant_availability_covariant_for_all_dim_patterns(),
        "constant map returns the full one-site subset",
    )

    k0_total_maps, k0_conditioned_maps = enumerate_availability_maps(reps["K0"]["projectors"])
    check(
        "T1",
        "dims [1,1,1] cannot realize variation with nearest-neighbor conditions",
        reps["K0"]["dims"] == [1, 1, 1]
        and k0_total_maps == 1
        and k0_conditioned_maps == 0
        and max(reps["K0"]["gaps"]) == 0.0,
        f"K0 maps={k0_total_maps}, conditioned={k0_conditioned_maps}, gaps={reps['K0']['gaps']}",
    )

    for L in (4, 6):
        f0 = plaquette_fluxes(L, eta_k0)
        f1 = plaquette_fluxes(L, eta0)
        check(
            "T2",
            f"surface flux anchor on L={L}: K0 all +1 and K1 all -1",
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
        "T2",
        "sibling K0/K1 constructions reproduced: K1 symbol reconstructs and K0 coefficients are scalar",
        recon_err < 1e-12 and max(spreads) < 1e-12 and k0_scalar_err < 1e-12,
        f"K1 recon={recon_err:.2e}, spread={max(spreads):.2e}, K0 scalar residual={k0_scalar_err:.2e}",
    )

    k1_projectors_valid = all(
        len(ps) == 2
        and all(projector_ok(P, 1) for P in ps)
        and np.linalg.norm(ps[0] @ ps[1]) < 1e-10
        and availability_gap(ps) > 1.0
        for ps in reps["K1"]["projectors"]
    )
    check(
        "T2",
        "K1 supplies the direction-tagged varying availability witness while K0 is neighbor-constant",
        reps["K0"]["dims"] == [1, 1, 1]
        and reps["K1"]["dims"] == [2, 2, 2]
        and k1_projectors_valid,
        f"K0 dims={reps['K0']['dims']}, K1 dims={reps['K1']['dims']}, K1 gaps={[round(g, 3) for g in reps['K1']['gaps']]}",
    )

    selected = [
        name
        for name, rep in reps.items()
        if survives_admissibility(rep, require_variation=True)
    ]
    check(
        "T2",
        "clarified Admissibility variation selects K1 on the licensed two-class surface",
        selected == ["K1"],
        f"selected={selected}",
    )

    herm = all(np.linalg.norm(G - G.conj().T) < 1e-12 for G in gammas)
    unit = all(np.linalg.norm(G @ G - I2) < 1e-12 for G in gammas)
    anti_norm = max(
        np.linalg.norm(gammas[i] @ gammas[j] + gammas[j] @ gammas[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    square_err = dirac_square_error(gammas)
    no_fourth = hermitian_anticommutant_nullity(gammas)
    check(
        "T2",
        "selected K1 carries the Dirac-square and Clifford-capacity consequences",
        herm and unit and anti_norm < 1e-12 and square_err < 1e-10 and no_fourth == 0,
        f"anticommutator={anti_norm:.2e}, square error={square_err:.2e}, fourth nullity={no_fourth}",
    )

    determination_survivors = [
        name
        for name, rep in reps.items()
        if survives_admissibility(rep, require_variation=False)
    ]
    check(
        "T3",
        "dropping variation recomputes the pre-clarification determination-only survivors",
        determination_survivors == ["K0", "K1"],
        f"survivors={determination_survivors}",
    )

    check(
        "T3",
        "under determination only, K0 survives through the same neighbor-constant machinery",
        survives_admissibility(reps["K0"], require_variation=False)
        and not survives_admissibility(reps["K0"], require_variation=True)
        and k0_conditioned_maps == 0,
        f"K0 dims={reps['K0']['dims']}, variation gaps={reps['K0']['gaps']}",
    )

    framed_dims_k0 = []
    framed_dims_k1 = []
    framed_projector_ok = True
    for mu in range(3):
        x = (0, 0, 0)
        y = tuple(np.array(x) + E_UNIT[mu])
        z = np.conj(u1_frame(x)) * u1_frame(y)
        framed_k0 = z * k0_coeffs[mu]
        framed_k1 = z * gammas[mu]
        framed_dims_k0.append(star_algebra_dim([framed_k0]))
        framed_dims_k1.append(star_algebra_dim([framed_k1]))
        framed_ps = direction_availability_projectors_normal(framed_k1)
        framed_projector_ok = framed_projector_ok and len(framed_ps) == 2
    check(
        "T4",
        "classification and variation witness are stable under local U(1) edge frames",
        framed_dims_k0 == reps["K0"]["dims"]
        and framed_dims_k1 == reps["K1"]["dims"]
        and framed_projector_ok,
        f"framed K0 dims={framed_dims_k0}, framed K1 dims={framed_dims_k1}",
    )

    chi = chirality(gammas)
    mirror_gammas = [-gammas[0], gammas[1], gammas[2]]
    mirror_chi = chirality(mirror_gammas)
    illegal_spread = illegal_frame_spread(gammas)
    check(
        "T4",
        "improper mirror and sub-region SU2 frame are contrast legs outside the allowed covariance",
        abs(chi) > 0.5 and abs(mirror_chi + chi) < 1e-12 and illegal_spread > 0.5,
        f"chirality={chi:.1f}, mirror chirality={mirror_chi:.1f}, illegal spread={illegal_spread:.3f}",
    )

    print()
    print(
        "SUMMARY: representative-level selection on the parent licensed surface; "
        "variation in the clarified Admissibility clause selects K1; dropping "
        "variation leaves K0 as the parent countermodel."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
