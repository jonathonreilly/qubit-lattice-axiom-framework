#!/usr/bin/env python3
"""Frame-class transport of realized-kinetic-branch selection.

Deterministic, numpy only, no network, no cache writes.

The K0/K1 phase conventions mirror
scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py:
K0 is t == 1 and K1 is the Kawamoto-Smit eta0 sign system.  The local
U(1) frame action and spanning-tree recovery below mirror the parent
runner's PhaseSystem.gauge and solve_gauge machinery.

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
TOL = 1e-9


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


def framed_tfun(base_tfun, frame, L):
    def out(x, mu):
        y = add_mod(x, mu, L)
        return np.conj(frame[x]) * complex(base_tfun(x, mu)) * frame[y]

    return out


def apply_gauge(tfun, gauge, L):
    def out(x, mu):
        y = add_mod(x, mu, L)
        return np.conj(gauge[x]) * complex(tfun(x, mu)) * gauge[y]

    return out


def random_u1_frame(L, seed):
    rng = np.random.default_rng(seed)
    frame = {}
    for x in sites(L):
        angle = 2.0 * math.pi * float(rng.random())
        frame[x] = np.exp(1j * angle)
    return frame


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


def build_hopping(L, tfun):
    ss = sites(L)
    idx = {s: i for i, s in enumerate(ss)}
    H = np.zeros((L**3, L**3), dtype=complex)
    for x in ss:
        for mu in range(3):
            y = add_mod(x, mu, L)
            t = complex(tfun(x, mu))
            H[idx[y], idx[x]] += t
            H[idx[x], idx[y]] += np.conj(t)
    return H


def finite_abs_spectrum(L, tfun):
    return np.sort(np.abs(np.linalg.eigvalsh(build_hopping(L, tfun))))


def solve_gauge(L, sys_a, sys_b):
    """Find g with sys_b = gauge(sys_a, g), mirroring the parent runner."""
    ratio = {}
    for x in sites(L):
        for mu in range(3):
            a = complex(sys_a(x, mu))
            b = complex(sys_b(x, mu))
            ratio[(x, mu)] = b / a

    origin = (0, 0, 0)
    g = {origin: 1.0 + 0j}
    frontier = [origin]
    while frontier:
        nxt = []
        for v in frontier:
            for mu in range(3):
                w = add_mod(v, mu, L)
                e = (v, mu)
                if w not in g:
                    g[w] = ratio[e] * g[v]
                    nxt.append(w)

                u = list(v)
                u[mu] = (u[mu] - 1) % L
                u = tuple(u)
                e_back = (u, mu)
                if u not in g:
                    g[u] = g[v] / ratio[e_back]
                    nxt.append(u)
        frontier = nxt

    if len(g) != L**3:
        return None
    for x in sites(L):
        for mu in range(3):
            y = add_mod(x, mu, L)
            lhs = np.conj(g[x]) * complex(sys_a(x, mu)) * g[y]
            if abs(lhs - complex(sys_b(x, mu))) > TOL:
                return None
    if any(abs(abs(v) - 1.0) > TOL for v in g.values()):
        return None
    return g


def Tmat(x):
    out = I2.copy()
    for mu, power in enumerate(x):
        if power % 2:
            out = out @ SIG[mu]
    return out


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
    vals, vecs = np.linalg.eigh((A + A.conj().T) / 2.0)
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


def availability_gap_from_coeff(A):
    projectors = [P for _, P in spectral_projectors_hermitian(A)]
    if len(projectors) < 2:
        return 0.0
    return max(
        float(np.linalg.norm(P - Q))
        for i, P in enumerate(projectors)
        for Q in projectors[i + 1 :]
    )


def anti_norm(coeffs):
    return max(
        float(np.linalg.norm(coeffs[i] @ coeffs[j] + coeffs[j] @ coeffs[i]))
        for i in range(3)
        for j in range(i + 1, 3)
    )


def k_symbol(kind, p, coeffs):
    M = np.zeros((2, 2), dtype=complex)
    if kind == "K0":
        for mu in range(3):
            M += 2.0 * math.cos(float(p[mu])) * coeffs[mu]
    else:
        for mu in range(3):
            M += math.sin(float(p[mu])) * coeffs[mu]
    return M


def symbol_abs_profile(kind, coeffs, N=5):
    vals = np.linspace(-math.pi, math.pi, N, endpoint=False)
    out = []
    for p in itertools.product(vals, repeat=3):
        ev = np.linalg.eigvalsh(k_symbol(kind, np.array(p), coeffs))
        out.extend(np.abs(ev))
    return np.sort(np.array(out))


def k0_coefficients_from_recovered_frame(L, tfun):
    g = solve_gauge(L, tfun, eta_k0)
    if g is None:
        return None, float("inf")
    canonical = apply_gauge(tfun, g, L)
    err = max(
        abs(complex(canonical(x, mu)) - 1.0)
        for x in sites(L)
        for mu in range(3)
    )
    return [I2.copy(), I2.copy(), I2.copy()], err


def absorbing_frame_for_k1(L, tfun):
    # Mirrors the parent runner's absorbing-frame construction:
    # T(x)=sigma_1^x1 sigma_2^x2 sigma_3^x3, with the recovered local U(1)
    # gauge supplying the framed member's site-local scalar factor.
    g = solve_gauge(L, tfun, eta0)
    if g is None:
        return None, None, float("inf"), float("inf")
    frame = {x: np.conj(g[x]) * Tmat(x) for x in sites(L)}
    canonical = apply_gauge(tfun, g, L)
    eta_err = max(
        abs(complex(canonical(x, mu)) - complex(eta0(x, mu)))
        for x in sites(L)
        for mu in range(3)
    )
    scalarization_err = 0.0
    for x in sites(L):
        for mu in range(3):
            y = add_mod(x, mu, L)
            lhs = frame[x].conj().T @ SIG[mu] @ frame[y]
            scalarization_err = max(
                scalarization_err,
                float(np.linalg.norm(lhs - complex(tfun(x, mu)) * I2)),
            )
    return g, frame, eta_err, scalarization_err


def k1_coefficients_from_absorbing_frame(L, tfun):
    _g, frame, eta_err, scalarization_err = absorbing_frame_for_k1(L, tfun)
    if frame is None:
        return None, float("inf"), float("inf"), float("inf")
    coeffs = []
    spread = 0.0
    for mu in range(3):
        mats = []
        for x in sites(L):
            y = add_mod(x, mu, L)
            mats.append(complex(tfun(x, mu)) * frame[x] @ frame[y].conj().T)
        avg = sum(mats) / len(mats)
        coeffs.append(avg)
        spread = max(spread, max(float(np.linalg.norm(M - avg)) for M in mats))
    return coeffs, eta_err, scalarization_err, spread


def branch_discriminators(L, kind, tfun):
    if kind == "K0":
        coeffs, recover_err = k0_coefficients_from_recovered_frame(L, tfun)
        if coeffs is None:
            return None
        absorb_err = 0.0
        spread = 0.0
    else:
        coeffs, recover_err, absorb_err, spread = k1_coefficients_from_absorbing_frame(L, tfun)
        if coeffs is None:
            return None
    flux_target = 1.0 if kind == "K0" else -1.0
    fluxes = plaquette_fluxes(L, tfun)
    return {
        "flux_ok": np.allclose(fluxes, flux_target, atol=1e-9),
        "dims": [star_algebra_dim([A]) for A in coeffs],
        "gaps": [availability_gap_from_coeff(A) for A in coeffs],
        "anti": anti_norm(coeffs),
        "symbol": symbol_abs_profile(kind, coeffs),
        "finite_abs": finite_abs_spectrum(L, tfun),
        "recover_err": recover_err,
        "absorb_err": absorb_err,
        "spread": spread,
    }


def rep_data(L, kind):
    tfun = eta_k0 if kind == "K0" else eta0
    return branch_discriminators(L, kind, tfun)


def data_equal(actual, expected):
    return (
        actual["flux_ok"]
        and actual["dims"] == expected["dims"]
        and np.allclose(actual["gaps"], expected["gaps"], atol=1e-8)
        and abs(actual["anti"] - expected["anti"]) < 1e-8
        and np.allclose(actual["symbol"], expected["symbol"], atol=1e-8)
        and np.allclose(actual["finite_abs"], expected["finite_abs"], atol=1e-8)
        and actual["recover_err"] < 1e-8
        and actual["absorb_err"] < 1e-8
        and actual["spread"] < 1e-8
    )


def dirac_square_error(coeffs, N=5):
    err = 0.0
    vals = np.linspace(-math.pi, math.pi, N, endpoint=False)
    for p in itertools.product(vals, repeat=3):
        p = np.array(p)
        K = k_symbol("K1", p, coeffs)
        target = float(np.sum(np.sin(p) ** 2)) * I2
        err = max(err, float(np.linalg.norm(K @ K - target)))
    return err


def survives_variation(data):
    determined = data["dims"] in ([1, 1, 1], [2, 2, 2])
    varies = all(gap > 1.0 for gap in data["gaps"])
    return determined and varies


def raw_phase_vector(L, tfun):
    return np.array([complex(tfun(x, mu)) for x in sites(L) for mu in range(3)])


def illegal_su2_spread(L):
    def illegal_frame(x):
        U = (I2 - 1j * S2) / math.sqrt(2.0)
        return U if x[0] >= L // 2 else I2

    spread = 0.0
    for mu in range(3):
        mats = []
        for x in sites(L):
            y = add_mod(x, mu, L)
            mats.append(illegal_frame(x).conj().T @ SIG[mu] @ illegal_frame(y))
        avg = sum(mats) / len(mats)
        spread = max(spread, max(float(np.linalg.norm(M - avg)) for M in mats))
    return spread


def main():
    print("=" * 78)
    print("realized kinetic branch selection frame-class transport (2026-07-02)")
    print("=" * 78)

    reps = {(L, kind): rep_data(L, kind) for L in (4, 6) for kind in ("K0", "K1")}
    rep_ok = all(data is not None and data["flux_ok"] for data in reps.values())
    check(
        "T0",
        "representative anchors recomputed for K0 and K1 on L=4,6",
        rep_ok,
        "K0 flux +1, K1 flux -1",
    )

    seeds = (11, 23, 37)
    for L in (4, 6):
        for kind, base in (("K0", eta_k0), ("K1", eta0)):
            for seed in seeds:
                frame = random_u1_frame(L, seed + (0 if kind == "K0" else 1000))
                tfun = framed_tfun(base, frame, L)
                data = branch_discriminators(L, kind, tfun)
                ok = data is not None and data_equal(data, reps[(L, kind)])
                check(
                    "T1",
                    f"{kind} discriminator tuple invariant under random local U(1) frame, L={L}, seed={seed}",
                    ok,
                    f"dims={None if data is None else data['dims']}",
                )

    for L, seed in ((4, 101), (6, 202)):
        frame = random_u1_frame(L, seed)
        tfun = framed_tfun(eta0, frame, L)
        coeffs, eta_err, scalarization_err, spread = k1_coefficients_from_absorbing_frame(L, tfun)
        ok = (
            coeffs is not None
            and eta_err < 1e-8
            and scalarization_err < 1e-8
            and spread < 1e-8
            and all(np.linalg.norm(coeffs[mu] - SIG[mu]) < 1e-8 for mu in range(3))
        )
        check(
            "T2",
            f"random framed flux(-1) member absorbs back to eta0 and constant Gamma_mu, L={L}",
            ok,
            f"eta error={eta_err:.2e}, scalarization={scalarization_err:.2e}, spread={spread:.2e}",
        )

    class_selection_ok = True
    dirac_transport_ok = True
    for L in (4, 6):
        frame0 = random_u1_frame(L, 503 + L)
        frame1 = random_u1_frame(L, 907 + L)
        d0 = branch_discriminators(L, "K0", framed_tfun(eta_k0, frame0, L))
        d1 = branch_discriminators(L, "K1", framed_tfun(eta0, frame1, L))
        selected = []
        if survives_variation(d0):
            selected.append("+1")
        if survives_variation(d1):
            selected.append("-1")
        class_selection_ok = class_selection_ok and selected == ["-1"]
        coeffs, _eta_err, _scalarization_err, _spread = k1_coefficients_from_absorbing_frame(
            L, framed_tfun(eta0, frame1, L)
        )
        dirac_transport_ok = dirac_transport_ok and coeffs is not None and dirac_square_error(coeffs) < 1e-10
    check(
        "T3",
        "variation premise selects the flux(-1) class after local U(1) transport",
        class_selection_ok,
        "K0 remains neighbor-constant; K1 remains direction-tagged varying",
    )
    check(
        "T3",
        "Dirac-square carrier transports through the recovered absorbing frame",
        dirac_transport_ok,
        "max checked square error below 1e-10",
    )

    L = 4
    frame = random_u1_frame(L, 313)
    framed_k1 = framed_tfun(eta0, frame, L)
    raw_changed = np.max(np.abs(raw_phase_vector(L, framed_k1) - raw_phase_vector(L, eta0))) > 0.1
    invariant_data = branch_discriminators(L, "K1", framed_k1)
    check(
        "T4",
        "raw per-link phases change under an allowed frame while discriminators remain fixed",
        raw_changed and invariant_data is not None and data_equal(invariant_data, reps[(L, "K1")]),
        f"max raw change={np.max(np.abs(raw_phase_vector(L, framed_k1) - raw_phase_vector(L, eta0))):.3f}",
    )

    spread = illegal_su2_spread(4)
    check(
        "T4",
        "illegal sub-region SU2 frame makes the K1 edge coefficient family nonuniform",
        spread > 0.5,
        f"coefficient spread={spread:.3f}",
    )

    flux_separated = True
    for L in (4, 6):
        for seed in (41, 43, 47):
            tfun = framed_tfun(eta_k0, random_u1_frame(L, seed), L)
            fluxes = plaquette_fluxes(L, tfun)
            flux_separated = flux_separated and np.allclose(fluxes, 1.0, atol=1e-9)
            flux_separated = flux_separated and not np.any(np.isclose(fluxes, -1.0, atol=1e-9))
    check(
        "T4",
        "local U(1) frames applied to flux(+1) members never produce flux(-1)",
        flux_separated,
        "plaquette flux stays +1 on all sampled K0 frames",
    )

    print()
    print(
        "SUMMARY: class-function transport on the local U(1) frame orbits of "
        "the licensed two-flux-class surface; gauge-link backgrounds remain separate."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
