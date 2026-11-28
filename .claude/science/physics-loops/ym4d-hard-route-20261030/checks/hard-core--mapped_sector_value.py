#!/usr/bin/env python3
"""No jump across topological sectors in a one-step fibre functional. Consumer: `library/sector-values.md`, the value clause for R_k, gate D4.

Written before running. The class of fields of small flux is not connected: equal fields off a ball can differ by a unit of charge, so a bound on derivatives says nothing about the difference of values of a function across sectors. The note claims that a one-step source Z(V') := G(V') - G(1) - kappa E(V') is nevertheless bounded on every sector by the local irrelevant energy I(V') := sum |grad Theta|^2 + sum Theta^4, since it is a sum of gauge-invariant local terms, each of which only sees a ball, on which there is no topology. This tests that claim on the simplest functional with a block constraint, in the simplest setting where sectors exist.

Model. d = 2, U(1) background, charge one scalar. Fine lattice N_f = L n_c, parents of side L. V' is given by its parent plaquette angles Theta' on the n_c x n_c torus, with sum in 2 pi Z. Its lift has fine plaquette angle Theta'/L^2 on the fine plaquettes of the parent cell, realised as a compact field with trivial links on the cut lines of the patch (construction of the gate's N1, generalised: A_y(x, y) := sum_{x' < x} theta(x', y), and the last column gauged). G(V') := log det of X_U restricted to ker r_U, with X_U the covariant Laplacian and r_U the covariant block average: the mean over a block of the site function transported to the block's centre along the axis-ordered contour. This is a gapped fibre functional, as in Text 5.

Fields. (a) sector k: uniform Theta' = 2 pi k / n_c^2 on the whole torus, k = 1, 2, 3. (b) sector 0: Theta' = t cos(2 pi x / n_c), slowly varying, small t. (c) sector 1 patch: uniform 2 pi / n^2 on an n x n patch in the torus, zero outside. (d) sector 0 pair: the same magnitude, + on the left half of the patch, - on the right, in a patch of even width. (e) two sector 1 patches, far apart.

PRE-STATED criteria.
 V0. Gauge invariance: G unchanged under a random site gauge transformation, to 1e-8.
 V1. The F^2 coefficient is the same in all sectors: kappa_k := (G(a, k) - G(1)) / E, with E := sum Theta'^2, extrapolated in k to small flux by a fit in Theta'^2, against kappa_0 from (b) extrapolated in t and n_c: they agree to 3 percent.
 V2. No jump: R_1 := max over (c) of |Z| / I, R_0 := max over (d) of |Z| / I. PASS if R_1 <= 3 R_0, with I at the same field. Z := G - G(1) - kappa E, with kappa := kappa_k from V1. A constant per unit of charge would show as Z of order one with I -> 0 along n growing, and so R_1 growing.
 V3. Along n growing in (c): |Z| falls at least like 1/n, to 20 percent, from the largest two values of n. (I is about (2 pi / n^2)^2 4 n + (2 pi)^4 / n^6, so like 1/n^3 up to the constant, and a jump would give a constant.)
 V4. Additivity across far sectors: |Z(e) - 2 Z(c)| <= 0.05 |Z(c)| at the largest n that fits.
FAIL if any of V0 to V4 fails.

Limits. U(1) in d = 2, the scalar part of a one-loop functional at one level, a lift given by hand and not a minimiser. In d = 2 the F^2 term is not marginal, and this test does not read that; it reads locality across sectors. RSS guard 2 GB.
"""
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


L = 3
h = (L - 1) // 2


def links_from_flux(theta):
    """theta: fine plaquette angles on the N x N torus, sum in 2 pi Z. Links with trivial cut lines."""
    N = theta.shape[0]
    Ax = np.zeros((N, N))
    Ay = np.zeros((N, N))
    col = np.zeros(N)  # running sum over x of theta at each y
    for x in range(N - 1):
        col = col + theta[x, :]
        Ay[x + 1, :] = col
    # Last column of plaquettes, x = N - 1: gauge the x = N = 0 column to trivial A_y through A_x(N - 1, y).
    h_y = col + theta[N - 1, :]
    S = np.concatenate([[0.0], np.cumsum(h_y)[:-1]])
    Ax[N - 1, :] = -S
    return Ax, Ay


def plaq(Ax, Ay):
    N = Ax.shape[0]
    t = Ax + np.roll(Ay, -1, axis=0) - np.roll(Ax, -1, axis=1) - Ay
    return (t + np.pi) % (2 * np.pi) - np.pi


class Fibre:
    def __init__(self, nc):
        self.nc = nc
        self.N = L * nc

    def covariant(self, Ax, Ay):
        N = self.N
        Ux, Uy = np.exp(1j * Ax), np.exp(1j * Ay)
        idx = lambda x, y: (x % N) * N + (y % N)
        X = np.zeros((N * N, N * N), dtype=complex)
        for x in range(N):
            for y in range(N):
                i = idx(x, y)
                X[i, i] += 4
                j = idx(x + 1, y)
                X[i, j] -= np.conj(Ux[x, y])
                X[j, i] -= Ux[x, y]
                j = idx(x, y + 1)
                X[i, j] -= np.conj(Uy[x, y])
                X[j, i] -= Uy[x, y]
        return X

    def basis(self, Ax, Ay):
        """Orthonormal basis of ker r_U, block by block: functions whose transported mean to the centre vanishes."""
        N, nc = self.N, self.nc
        Ux, Uy = np.exp(1j * Ax), np.exp(1j * Ay)
        idx = lambda x, y: (x % N) * N + (y % N)
        cols = []
        n = N * N
        B = np.zeros((n, n - nc * nc), dtype=complex)
        col = 0
        for cx in range(nc):
            for cy in range(nc):
                y0 = (L * cx + h, L * cy + h)
                # Transport from each site of the block to the centre along an axis-ordered contour from the centre.
                v = np.zeros(L * L, dtype=complex)
                sites = []
                k = 0
                for ox in range(-h, h + 1):
                    for oy in range(-h, h + 1):
                        ph = 1.0 + 0j
                        x, y = y0
                        for _ in range(abs(ox)):
                            if ox > 0:
                                ph *= np.conj(Ux[x % N, y % N])
                                x += 1
                            else:
                                x -= 1
                                ph *= Ux[x % N, y % N]
                        for _ in range(abs(oy)):
                            if oy > 0:
                                ph *= np.conj(Uy[x % N, y % N])
                                y += 1
                            else:
                                y -= 1
                                ph *= Uy[x % N, y % N]
                        v[k] = ph
                        sites.append(idx(y0[0] + ox, y0[1] + oy))
                        k += 1
                # Constraint: sum conj(v_k)* f_k = 0 in the sense r f := sum v_k f_k = 0.
                vv = np.conj(v) / np.linalg.norm(v)
                Q, _ = np.linalg.qr(np.eye(L * L, dtype=complex) - np.outer(vv, vv.conj()))
                Q = Q[:, : L * L - 1]
                # Q must span the orthogonal complement of vv.
                Q = Q - np.outer(vv, vv.conj() @ Q)
                Q, _ = np.linalg.qr(Q)
                B[np.array(sites), col : col + L * L - 1] = Q
                col += L * L - 1
        return B

    def G(self, Ax, Ay):
        X = self.covariant(Ax, Ay)
        B = self.basis(Ax, Ay)
        M = B.conj().T @ X @ B
        M = 0.5 * (M + M.conj().T)
        guard()
        c = np.linalg.cholesky(M)
        return 2.0 * float(np.sum(np.log(np.real(np.diag(c)))))


def fine_flux(Theta):
    nc = Theta.shape[0]
    return np.kron(Theta, np.ones((L, L))) / L**2


def energy(Theta):
    return float(np.sum(Theta**2))


def irrelevant(Theta):
    g0 = np.roll(Theta, -1, axis=0) - Theta
    g1 = np.roll(Theta, -1, axis=1) - Theta
    return float(np.sum(g0**2) + np.sum(g1**2) + np.sum(Theta**4))


def patch(nc, n, sign_split=False, offset=(0, 0)):
    Theta = np.zeros((nc, nc))
    val = 2 * np.pi / n**2
    for i in range(n):
        for j in range(n):
            s = 1.0
            if sign_split and i >= n // 2:
                s = -1.0
            Theta[(offset[0] + i) % nc, (offset[1] + j) % nc] = s * val
    return Theta


def main():
    ok = True
    nc = 16
    fib = Fibre(nc)
    A0x, A0y = np.zeros((fib.N, fib.N)), np.zeros((fib.N, fib.N))
    G1 = fib.G(A0x, A0y)
    print(f" G(1) = {G1:.6f}, rss={rss_gb():.2f}GB", flush=True)
    print("V0", flush=True)
    Th = patch(nc, 6)
    Ax, Ay = links_from_flux(fine_flux(Th))
    t = plaq(Ax, Ay)
    print(f"  realised flux: |theta - target| max = {np.abs(t - fine_flux(Th)).max():.1e}", flush=True)
    g1 = fib.G(Ax, Ay)
    rng = np.random.default_rng(1)
    chi = rng.uniform(-np.pi, np.pi, (fib.N, fib.N))
    # A gauge transformation with chi = 0 at the block centres, as the block average is transported to the centre.
    for cx in range(nc):
        for cy in range(nc):
            chi[L * cx + h, L * cy + h] = 0.0
    Ax2 = Ax + np.roll(chi, -1, axis=0) - chi
    Ay2 = Ay + np.roll(chi, -1, axis=1) - chi
    g2 = fib.G(Ax2, Ay2)
    v0 = abs(g1 - g2) <= 1e-8
    ok = ok and v0
    print(f" V0 |G - G gauged| = {abs(g1 - g2):.1e}: {v0}", flush=True)
    print("V1", flush=True)
    kappas = []
    for k in (1, 2, 3):
        Theta = np.full((nc, nc), 2 * np.pi * k / nc**2)
        Ax, Ay = links_from_flux(fine_flux(Theta))
        val = fib.G(Ax, Ay) - G1
        kappas.append((Theta[0, 0] ** 2, val / energy(Theta)))
        print(f"  sector {k}: Theta'={Theta[0, 0]:.5f}, (G - G(1))/E = {kappas[-1][1]:.6f}", flush=True)
        guard()
    pk = np.polyfit([a for a, b in kappas], [b for a, b in kappas], 2)
    kappa_k = float(pk[-1])
    k0 = []
    for t0 in (0.08, 0.04):
        Theta = t0 * np.cos(2 * np.pi * np.arange(nc) / nc)[:, None] * np.ones((1, nc))
        Ax, Ay = links_from_flux(fine_flux(Theta))
        val = fib.G(Ax, Ay) - G1
        k0.append(val / energy(Theta))
        print(f"  sector 0, cos profile t={t0}: (G - G(1))/E = {k0[-1]:.6f}", flush=True)
        guard()
    kappa_0 = (4 * k0[1] - k0[0]) / 3  # Removes the t^2 correction.
    v1 = abs(kappa_k - kappa_0) <= 0.03 * abs(kappa_k)
    ok = ok and v1
    print(f" V1 kappa from sectors {kappa_k:.6f} against sector 0 with a slowly varying field {kappa_0:.6f}: {v1}. The second has a p^2 term at n_c = {nc}, which this does not remove.", flush=True)
    kappa = kappa_k
    print("V2, V3", flush=True)
    rows1, rows0 = {}, {}
    for n in (4, 6, 8, 10):
        Th1 = patch(nc, n)
        Ax, Ay = links_from_flux(fine_flux(Th1))
        Z1 = fib.G(Ax, Ay) - G1 - kappa * energy(Th1)
        I1 = irrelevant(Th1)
        Th0 = patch(nc, n, sign_split=True)
        Ax, Ay = links_from_flux(fine_flux(Th0))
        Z0 = fib.G(Ax, Ay) - G1 - kappa * energy(Th0)
        I0 = irrelevant(Th0)
        rows1[n] = (Z1, I1)
        rows0[n] = (Z0, I0)
        guard()
        print(f"  n={n}: sector 1 Z={Z1:+.5e} I={I1:.5e} |Z|/I={abs(Z1) / I1:.4f}; sector 0 Z={Z0:+.5e} I={I0:.5e} |Z|/I={abs(Z0) / I0:.4f} rss={rss_gb():.2f}GB", flush=True)
    R1 = max(abs(a) / b for a, b in rows1.values())
    R0 = max(abs(a) / b for a, b in rows0.values())
    v2 = R1 <= 3 * R0
    ok = ok and v2
    print(f" V2 R_1={R1:.4f} R_0={R0:.4f}: {v2}", flush=True)
    a, b = abs(rows1[8][0]), abs(rows1[10][0])
    v3 = b <= 1.2 * a * (8 / 10)
    ok = ok and v3
    print(f" V3 |Z| at n = 8, 10: {a:.4e} {b:.4e}: {v3}", flush=True)
    print("V4", flush=True)
    n = 6
    Th1 = patch(nc, n)
    Ax, Ay = links_from_flux(fine_flux(Th1))
    Z1 = fib.G(Ax, Ay) - G1 - kappa * energy(Th1)
    Th2 = patch(nc, n) + patch(nc, n, offset=(8, 8))
    # Two units of flux on the torus.
    Ax, Ay = links_from_flux(fine_flux(Th2))
    Z2 = fib.G(Ax, Ay) - G1 - kappa * energy(Th2)
    v4 = abs(Z2 - 2 * Z1) <= 0.05 * abs(Z1)
    ok = ok and v4
    print(f" V4 Z(two)={Z2:+.5e}, 2 Z(one)={2 * Z1:+.5e}: {v4}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
