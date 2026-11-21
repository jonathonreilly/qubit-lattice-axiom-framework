#!/usr/bin/env python3
"""Non-concentration of the constrained minimiser, abelian, at the trivial background: (R3) of Text 5.3.

Written before running. Abelian linear model on a periodic torus, fine lattice spacing 1, N = ell n_c, ell = L^k odd.
Coarse data Y on level-ell bonds. H minimises ||dH||^2 subject to curl(Q H) = curl Y, Q the composite path average:
(Q H)_mu(y) = ell^-d sum_{x in B(y)} sum_{t<ell} H_mu(x + t e_mu). flux' := max |coarse plaquette angle|.
Intermediate level ell' = ell/L: theta' := plaquette angles of Q^(ell') H, flux_1 := max |theta'|.
E(Q) := sum of fine plaquette angles squared in a cube of side l in level-ell' cells.

Data: 'bump' (one coarse bond set to 1), 'random' (Gaussian on coarse bonds, seed fixed).

PRE-STATED criteria.
 C0. Constraint: sup |curl(Q H) - curl Y| < 1e-8 flux'.
 C1. (Registered in Text 5.3.) d = 3, L = 3, non-uniform data: R1 := flux_1 / (flux'/L) is below 10 at k = 1, 2 and not growing
     from k = 1 to k = 2, with 10 percent numerical tolerance. Also reported at k = 3, under the same rule.
 C2. R1 < 10 for every case run.
 C3. Non-concentration with C free of L: E3 := max_Q E(Q) / (|Q|^{1/2} L^-2 flux'^2), |Q| = l^d in level-ell' cells for l = 1, 2.
     For each d, the value at the largest L is at most 1.5 times the value at the smallest L, at k = 1, for each data type and l.
 Read-outs, not criteria: R2 := flux_1/(flux'/L^2), to see whether L^-2 holds; E4 := max_Q E(Q) / (|Q| L^-4 flux'^2).
 FAIL if any criterion fails. Limitation: abelian, trivial background; it says nothing about the non-abelian case.
 Self-limits RSS to 2 GB; one job under the numeric lock, BLAS threads 1, nice.
"""
import itertools
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2.0:
        raise SystemExit("RSS above 2 GB")


def d_box(q, ell):
    s = np.sin(q / 2)
    out = np.full_like(q, float(ell), dtype=float)
    nz = np.abs(s) > 1e-12
    out[nz] = np.sin(ell * q[nz] / 2) / s[nz]
    return out


def rho_hat(qs, mu, ell, d):
    """Fourier transform of the weight of (Q H)_mu at y = 0, as a product of 1-d factors, broadcast shape."""
    out = 1.0 + 0j
    for nu in range(d):
        q = qs[nu]
        f = d_box(q, ell) / ell
        if nu == mu:
            f = f * d_box(q, ell) * np.exp(-1j * q * (ell - 1) / 2)
        shape = [1] * d
        shape[nu] = -1
        out = out * f.reshape(shape)
    return out


def curl_on_grid(Y, step, d):
    """Y[mu] is a real array sampled on a lattice; returns the max |plaquette angle| and the arrays. step: 1 in sample units."""
    best = 0.0
    arrs = {}
    for mu in range(d):
        for nu in range(mu + 1, d):
            th = np.roll(Y[nu], -step, axis=mu) - Y[nu] - np.roll(Y[mu], -step, axis=nu) + Y[mu]
            arrs[(mu, nu)] = th
            best = max(best, float(np.abs(th).max()))
    return best, arrs


def solve(d, L, k, nc, data, seed=20261030):
    ell = L**k
    N = ell * nc
    grid1d = 2 * np.pi * np.arange(N) / N
    qs = [grid1d] * d
    # coarse data
    rng = np.random.default_rng(seed)
    Yc = [np.zeros([nc] * d) for _ in range(d)]
    if data == "bump":
        Yc[0][tuple([0] * d)] = 1.0
    else:
        for mu in range(d):
            Yc[mu] = rng.standard_normal([nc] * d)
    fluxp, _ = curl_on_grid(Yc, 1, d)
    Yc = [y / fluxp for y in Yc]
    fluxp = 1.0
    Ychat = [np.fft.fftn(y) for y in Yc]
    # lattice symbols
    dq = [np.exp(1j * q) - 1 for q in qs]
    shape1 = lambda nu: tuple(-1 if a == nu else 1 for a in range(d))
    dfine = [dq[nu].reshape(shape1(nu)) for nu in range(d)]
    lap = 0.0
    for nu in range(d):
        lap = lap + np.abs(dfine[nu]) ** 2
    G = np.zeros_like(lap)
    nz = lap > 1e-14
    G[nz] = 1.0 / lap[nz]
    rho = [rho_hat(qs, mu, ell, d) for mu in range(d)]
    # alias sum: M_{mu nu}(p) = ell^-d sum_{q = p mod} conj(rho_mu) G P^{mu nu} rho_nu
    idx = np.indices([N] * d)
    pidx = np.ravel_multi_index(tuple(i % nc for i in idx), [nc] * d)
    del idx
    M = np.zeros((nc**d, d, d), dtype=complex)
    for mu in range(d):
        for nu in range(d):
            term = np.conj(rho[mu]) * rho[nu] * G * ((1.0 if mu == nu else 0.0) - dfine[mu] * np.conj(dfine[nu]) * G)
            M[:, mu, nu] = (
                np.bincount(pidx.ravel(), weights=term.real.ravel(), minlength=nc**d)
                + 1j * np.bincount(pidx.ravel(), weights=term.imag.ravel(), minlength=nc**d)
            ) / ell**d
    guard()
    # coarse transverse projection and solve
    pgrid = np.indices([nc] * d).reshape(d, -1).T
    Lam = np.zeros((nc**d, d), dtype=complex)
    for ip, m in enumerate(pgrid):
        if np.all(m == 0):
            continue
        dc = np.exp(2j * np.pi * m / nc) - 1
        Pc = np.eye(d, dtype=complex) - np.outer(dc, np.conj(dc)) / np.sum(np.abs(dc) ** 2)
        y = np.array([Ychat[mu][tuple(m)] for mu in range(d)])
        Lam[ip] = np.linalg.pinv(Pc @ M[ip] @ Pc, rcond=1e-11) @ (Pc @ y)
    # H in Fourier
    Hhat = []
    LamF = [Lam[:, nu][pidx] for nu in range(d)]
    for mu in range(d):
        v = 0.0
        for nu in range(d):
            v = v + ((1.0 if mu == nu else 0.0) - dfine[mu] * np.conj(dfine[nu]) * G) * rho[nu] * LamF[nu]
        Hhat.append(G * v)
    del LamF, pidx
    guard()
    H = [np.fft.ifftn(h).real for h in Hhat]
    # C0
    Yrec = []
    sl = tuple(slice(0, N, ell) for _ in range(d))
    for mu in range(d):
        Yrec.append(np.fft.ifftn(Hhat[mu] * np.conj(rho[mu])).real[sl])
    _, a = curl_on_grid(Yrec, 1, d)
    _, b = curl_on_grid(Yc, 1, d)
    c0 = max(float(np.abs(a[key] - b[key]).max()) for key in a)
    # intermediate level
    ell1 = ell // L
    sl1 = tuple(slice(0, N, ell1) for _ in range(d))
    Y1 = []
    for mu in range(d):
        r1 = rho_hat(qs, mu, ell1, d)
        Y1.append(np.fft.ifftn(Hhat[mu] * np.conj(r1)).real[sl1])
    flux1, _ = curl_on_grid(Y1, 1, d)
    # energy density on fine plaquettes, summed into level-ell1 cells
    dens = 0.0
    for mu in range(d):
        for nu in range(mu + 1, d):
            th = np.roll(H[nu], -1, axis=mu) - H[nu] - np.roll(H[mu], -1, axis=nu) + H[mu]
            dens = dens + th**2
    guard()
    out = dict(N=N, c0=c0, flux1=flux1, fluxp=fluxp, ell1=ell1)
    n1 = N // ell1
    cell = dens
    for ax in range(d):
        cell = np.add.reduceat(cell, np.arange(0, N, ell1), axis=ax)
    Eq = {}
    for l in (1, 2):
        c = cell
        for ax in range(d):
            c = sum(np.roll(c, -s, axis=ax) for s in range(l))
        Eq[l] = float(c.max())
    out["Eq"] = Eq
    guard()
    return out


def main():
    cases = {
        3: [(3, 1, 6), (3, 2, 6), (3, 3, 4), (5, 1, 6), (7, 1, 6), (9, 1, 6), (11, 1, 6)],
        4: [(3, 1, 4), (5, 1, 4), (7, 1, 4), (9, 1, 4), (3, 2, 4)],
    }
    ok = True
    table = {}
    for d, lst in cases.items():
        for L, k, nc in lst:
            for data in ("bump", "random"):
                r = solve(d, L, k, nc, data)
                R1 = r["flux1"] * L
                R2 = r["flux1"] * L**2
                E3 = {l: r["Eq"][l] / (l ** (d / 2) * L**-2) for l in (1, 2)}
                E4 = {l: r["Eq"][l] / (l**d * L**-4) for l in (1, 2)}
                table[(d, L, k, data)] = (R1, E3, E4)
                good = r["c0"] < 1e-8 and R1 < 10
                ok = ok and good
                print(
                    f"d={d} L={L:2d} k={k} nc={nc} N={r['N']:3d} {data:6s} c0={r['c0']:.1e} R1={R1:7.3f} R2={R2:7.3f} "
                    f"E3(1)={E3[1]:8.3f} E3(2)={E3[2]:8.3f} E4(1)={E4[1]:8.3f} E4(2)={E4[2]:8.3f} rss={rss_gb():.2f}GB {'ok' if good else 'VIOLATION'}",
                    flush=True,
                )
    # C1
    for data in ("bump", "random"):
        for k in (1, 2):
            a, b = table[(3, 3, k, data)][0], table[(3, 3, k + 1, data)][0]
            grow = b <= 1.1 * a
            print(f"C1 {data}: R1(k={k})={a:.3f} R1(k={k+1})={b:.3f} {'ok' if grow else 'GROWS'}")
            ok = ok and grow
    # C3
    for d, lst in cases.items():
        Ls = sorted({L for L, k, nc in lst if k == 1})
        for data in ("bump", "random"):
            for l in (1, 2):
                a = table[(d, Ls[0], 1, data)][1][l]
                b = table[(d, Ls[-1], 1, data)][1][l]
                good = b <= 1.5 * a
                print(f"C3 d={d} {data} l={l}: E3(L={Ls[0]})={a:.3f} E3(L={Ls[-1]})={b:.3f} {'ok' if good else 'GROWS'}")
                ok = ok and good
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
