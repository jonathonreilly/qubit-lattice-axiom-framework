#!/usr/bin/env python3
"""T15 tests: does the time doubler survive OS reconstruction, and can the hypercubic tick be a
real-time step?  Free staggered fermion only.  Pre-registered in PREREG.md.

Run:  python3 t15_test.py            (writes results.json next to this file)
"""
import itertools, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- lattice operators
def spatial_ops(N, d):
    """A (anti-Hermitian staggered hop, spatial), P (parity (-1)^{sum x}), sites list."""
    sites = list(itertools.product(range(N), repeat=d))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    A = np.zeros((n, n), dtype=complex)
    P = np.zeros((n, n))
    for s in sites:
        i = idx[s]
        P[i, i] = (-1) ** sum(s)
        for mu in range(d):
            eta = (-1) ** sum(s[:mu])
            sp = list(s); sp[mu] = (sp[mu] + 1) % N
            sm = list(s); sm[mu] = (sm[mu] - 1) % N
            A[i, idx[tuple(sp)]] += 0.5 * eta
            A[i, idx[tuple(sm)]] -= 0.5 * eta
    return A, P, sites


def euclid_D(N, d, L, m):
    """Full Euclidean staggered operator on N^d x L, time is the LAST direction (eta_t = (-1)^{sum x}),
    antiperiodic in time, periodic in space."""
    A, P, sites = spatial_ops(N, d)
    n = len(sites)
    D = np.zeros((n * L, n * L), dtype=complex)
    S = np.zeros((L, L))
    for t in range(L):
        S[t, (t + 1) % L] += 1.0 * (1 if t + 1 < L else -1)   # antiperiodic forward
        S[t, (t - 1) % L] -= 1.0 * (1 if t - 1 >= 0 else -1)  # antiperiodic backward
    # D = m + A (x) 1_t + (1/2) P (x) S
    D = m * np.eye(n * L, dtype=complex) + np.kron(A, np.eye(L)) + 0.5 * np.kron(P, S)
    return D, A, P


def ln_absdet(M):
    s, ld = np.linalg.slogdet(M)
    return ld


# ---------------------------------------------------------------- Test A
def ks_levels(A, P, m):
    """Single-particle levels of the spatial (Kogut-Susskind) problem: B = P (A + m), Hermitian,
    eigenvalues +-r with r^2 = m^2 + sum sin^2 k."""
    B = P @ (A + m * np.eye(A.shape[0]))
    assert np.allclose(B, B.conj().T)
    mu = np.linalg.eigvalsh(B)
    return mu


def lnZ_KS(levels, beta):
    """ln prod_j 2 cosh(beta e_j / 2)  (symmetric ordering, e_j single-particle levels)."""
    x = 0.5 * beta * levels
    return float(np.sum(np.abs(x) + np.log1p(np.exp(-2.0 * np.abs(x)))))


def testA(cases):
    rows = []
    for (d, N, m, Ls) in cases:
        for L in Ls:
            D, A, P = euclid_D(N, d, L, m)
            n = N ** d
            mu = ks_levels(A, P, m)
            e = np.sign(mu) * np.arcsinh(np.abs(mu))          # OS levels (+- asinh r)
            lhs = ln_absdet(D)
            sq = -n * L * math.log(2.0) + 2.0 * lnZ_KS(e, L)      # doubled (two KS copies)
            one = -0.5 * n * L * math.log(2.0) + 1.0 * lnZ_KS(e, L)  # single KS copy, same dispersion
            one_r = -0.5 * n * L * math.log(2.0) + 1.0 * lnZ_KS(mu, L)  # single KS copy, Hamiltonian dispersion r
            rows.append(dict(d=d, N=N, m=m, L=L, n=n, lnabsdet=lhs, squared=sq, single=one, single_r=one_r,
                             err_sq=abs(lhs - sq), err_one=abs(lhs - one), err_one_r=abs(lhs - one_r),
                             relerr_sq=abs(lhs - sq) / abs(lhs)))
    return rows


def recurrence_roots(N, d, m):
    A, P, _ = spatial_ops(N, d)
    n = A.shape[0]
    B = P @ (A + m * np.eye(n))
    M = np.block([[-2 * B, np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    z = np.linalg.eigvals(M)
    dec = z[np.abs(z) < 1 - 1e-12]
    gro = z[np.abs(z) > 1 + 1e-12]
    return dict(n=n, n_decaying=len(dec), n_growing=len(gro),
                n_decaying_pos=int(np.sum(dec.real > 0)), n_decaying_neg=int(np.sum(dec.real < 0)),
                n_growing_pos=int(np.sum(gro.real > 0)), n_growing_neg=int(np.sum(gro.real < 0)),
                decaying_moduli_match_exp_minus_asinh=bool(
                    np.allclose(np.sort(np.abs(dec)),
                                np.sort(np.exp(-np.arcsinh(np.abs(np.linalg.eigvalsh(B))))), atol=1e-9)))


# ---------------------------------------------------------------- Test B
def frac_r_gt_1(d, m, n_grid=None, n_mc=4_000_000, seed=1):
    rng = np.random.default_rng(seed)
    k = rng.uniform(-math.pi, math.pi, size=(n_mc, d))
    r2 = m * m + np.sum(np.sin(k) ** 2, axis=1)
    mc = float(np.mean(r2 > 1.0))
    out = dict(d=d, m=m, frac_MC=mc, r_max=math.sqrt(m * m + d), max_growth_per_step=None)
    if n_grid:
        g = (np.arange(n_grid) + 0.5) * 2 * math.pi / n_grid - math.pi
        s2 = np.sin(g) ** 2
        grids = np.meshgrid(*([s2] * d), indexing="ij")
        r2g = m * m + sum(grids)
        out["frac_grid"] = float(np.mean(r2g > 1.0))
    rmax = out["r_max"]
    out["max_growth_per_step"] = (rmax + math.sqrt(rmax ** 2 - 1)) if rmax > 1 else 1.0
    return out


def leapfrog_check(N, d, m, tau):
    """Direct eigenvalues of the real-time leapfrog 2-step matrix; report how many have |z| != 1."""
    A, P, _ = spatial_ops(N, d)
    n = A.shape[0]
    B = P @ (A + m * np.eye(n))                     # Hermitian, eigenvalues +-r
    Hn = B
    M = np.block([[-2j * tau * Hn, np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    z = np.linalg.eigvals(M)
    off = np.abs(np.abs(z) - 1) > 1e-8
    r = np.abs(np.linalg.eigvalsh(B))
    return dict(N=N, d=d, m=m, tau=tau, n_modes=len(z), n_off_unit_circle=int(np.sum(off)),
                n_H_levels_with_tau_r_gt_1=int(np.sum(tau * r > 1 + 1e-12)),
                max_abs_z=float(np.max(np.abs(z))))


# ---------------------------------------------------------------- Test C
def testC():
    out = {}
    for d in (1, 2, 3):
        rng = np.random.default_rng(3)
        k = rng.uniform(-math.pi, math.pi, size=(400000, d))
        s = np.sin(k)
        r = np.sqrt(np.sum(s ** 2, axis=1))
        E = np.arcsinh(r)
        # radial group velocity along random directions: grad_k E
        # dE/dk_i = cos k_i sin k_i / (r sqrt(1+r^2))
        grad = (np.cos(k) * s) / (r[:, None] * np.sqrt(1 + r[:, None] ** 2))
        speed = np.sqrt(np.sum(grad ** 2, axis=1))
        small = r < 0.05
        out[d] = dict(max_group_speed=float(np.max(speed)), min_over_small_r_E_over_r=float(np.min(E[small] / r[small])),
                      max_over_small_r_E_over_r=float(np.max(E[small] / r[small])),
                      speed_at_small_r_mean=float(np.mean(speed[small])))
    # series check asin - asinh
    r = np.array([0.05, 0.1, 0.2, 0.3])
    lhs = np.arcsin(r) - np.arcsinh(r)
    rhs = r ** 3 / 3 + 5 * r ** 7 / 56
    out["series_asin_minus_asinh_rel_resid"] = [float(x) for x in np.abs(lhs - rhs) / lhs]
    return out


# ---------------------------------------------------------------- Test D
def testD(N=4, d=3):
    A, P, _ = spatial_ops(N, d)
    n = A.shape[0]
    B = P @ (A + 0.0 * np.eye(n))
    w, V = np.linalg.eigh(B)                         # eigenvalues +-r, massless
    tau = 1.0
    res = {}
    def count(qe):
        qe = np.mod(qe + math.pi, 2 * math.pi) - math.pi
        return int(np.sum(np.abs(qe) < 1e-9)), int(np.sum(np.abs(np.abs(qe) - math.pi) < 1e-9)), len(qe)
    # exact flow, tau = 1
    res["flow_exp(-i tau H)"] = count(-tau * w)
    # Cayley
    U = (1 - 0.5j * tau * w) / (1 + 0.5j * tau * w)
    res["Cayley"] = count(-np.angle(U))
    # leapfrog: roots z of z^2 + 2 i tau w z - 1 = 0, |tau w| <=1 required
    om = []
    for wj in w:
        disc = 1 - (tau * wj) ** 2 + 0j
        for sgn in (+1, -1):
            z = -1j * tau * wj + sgn * np.sqrt(disc)
            om.append(-np.angle(z))
    res["leapfrog_tau=1 (roots, some |z|!=1 at r>1)"] = count(np.array(om))
    # leapfrog restricted to stable modes only
    om_s = []
    for wj in w:
        if abs(tau * wj) <= 1 + 1e-12:
            disc = 1 - (tau * wj) ** 2 + 0j
            for sgn in (+1, -1):
                z = -1j * tau * wj + sgn * np.sqrt(disc)
                om_s.append(-np.angle(z))
    res["leapfrog_stable_modes_only"] = count(np.array(om_s)) + (int(np.sum(np.abs(tau * w) > 1 + 1e-12)),)
    res["note"] = "entries are (# at quasi-energy 0, # at pi, # counted); last entry for stable-only = number of H levels excluded (r>1)"
    return res


def main():
    out = {}
    cases = [
        (1, 4, 0.5, [2, 4, 6, 8, 12]),
        (1, 6, 0.3, [2, 4, 8, 12]),
        (2, 4, 0.5, [2, 4, 6, 8]),
        (2, 6, 0.3, [2, 4, 6]),
        (3, 4, 0.5, [2, 4, 6, 8]),
        (3, 4, 0.2, [2, 4, 6]),
    ]
    rows = testA(cases)
    out["A_rows"] = rows
    out["A_max_relerr_squared"] = max(r["relerr_sq"] for r in rows)
    out["A_min_err_single_asinh"] = min(r["err_one"] for r in rows)
    out["A_min_err_single_r"] = min(r["err_one_r"] for r in rows)
    out["A_max_err_squared_abs"] = max(r["err_sq"] for r in rows)
    out["A_roots"] = {f"d{d}N{N}m{m}": recurrence_roots(N, d, m) for (d, N, m, _) in cases}
    out["B_fractions"] = [frac_r_gt_1(d, m, n_grid={1: None, 2: 1200, 3: 200}[d]) for d in (1, 2, 3) for m in (0.0, 0.5)]
    out["B_leapfrog_direct"] = [leapfrog_check(N, d, m, tau) for (N, d, m, tau) in
                                [(8, 1, 0.0, 1.0), (8, 2, 0.0, 1.0), (4, 3, 0.0, 1.0), (4, 3, 0.0, 0.5), (4, 3, 0.0, 1 / math.sqrt(3) - 1e-9)]]
    out["C"] = testC()
    out["D"] = testD()
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    # ------------------------------ readable summary
    print("== Test A: ln|det D| vs 2 x KS (doubled) and vs 1 x KS (single)")
    for r in rows:
        print(f"d={r['d']} N={r['N']} m={r['m']} L={r['L']:2d}  ln|det|={r['lnabsdet']:.10f}  "
              f"err_doubled={r['err_sq']:.2e}  err_single(asinh)={r['err_one']:.3f}  err_single(r)={r['err_one_r']:.3f}")
    print("max relerr doubled:", out["A_max_relerr_squared"], " min err single asinh:", out["A_min_err_single_asinh"],
          " min err single r:", out["A_min_err_single_r"])
    print("== recurrence roots")
    for k, v in out["A_roots"].items():
        print(k, v)
    print("== Test B fractions of BZ with r>1")
    for r in out["B_fractions"]:
        print(r)
    print("== leapfrog direct eigenvalues")
    for r in out["B_leapfrog_direct"]:
        print(r)
    print("== Test C", json.dumps(out["C"], indent=1))
    print("== Test D", json.dumps(out["D"], indent=1))


if __name__ == "__main__":
    main()
