#!/usr/bin/env python3
"""The Wilson term of parts/hard-core--independent.md, Text 8.7, equation (8.3), on the lattice.

Second order in an abelian background U = exp(i theta sigma_3), theta_mu(x) = 2 eps_mu cos(q.(x + mu / 2)),
of Phi_A = -(1/2) log det H_F + log det Gh, Feynman gauge, for A = sum_p (1 - (1/2) tr U_p), on a periodic
torus N^4. In the left-exponential chart U = exp(i b.sigma) V, the charged field phi = b^1 + i b^2 has on
one plaquette the Hermitian form with entries

    h_ij = s_i s_j exp(2 i (a_i - a_j)) exp(i Theta sgn(j - i)) for i != j,    h_ii = cos Theta,

s = (+, +, -, -), a = (0, th_1, th_1 + th_2 - th_3, Theta), Theta = th_1 + th_2 - th_3 - th_4, derived in this
file's companion text from E = prod exp(i s_i b_i), [b.sigma, b'.sigma] = 2 i (b x b').sigma, and
exp(i a sigma_3) phi exp(-i a sigma_3) = exp(-2 i a) phi. The gauge term is |D^+ phi|^2 per site, with
(D chi)_mu(x) = exp(-2 i th_mu(x)) chi(x + mu) - chi(x), and the ghost is D^+ D. The charged sector
contributes -log det_C H + 2 log det_C Gh. The neutral component sees theta only through cos Theta, which gives
a constant times A at this order, so it is left out, and it cancels in the difference below.

Claims under test. R(q) := Phi^(2) / A^(2), with A^(2) = sum_p Theta_p^2 / 2.
    (8.3): R(q) - R(3 q) = b log 3 + o(1), b = 11 / (3 pi^2) = 0.37152.

Pre-registered criteria, written before the first run.
    PASS-WARD: for eps proportional to qhat, a pure gauge, |Phi^(2)| / (N^4 eps^2) <= 1e-2 / N^2 at every q run.
    If this fails, the code or the form above is wrong, and nothing else is read.
    PASS-B: at N = 48 and q = 2 pi n / N along axis 0, eps along axis 1, for n = 2,
    | (R(q) - R(3 q)) / log 3 - b | <= 0.1 b. FAIL-B otherwise. Sign and size of b are what is tested.
    The zero mode p = 0 is left out of all propagators; for finite N this is an error of order 1 / (q N)^2 in R.

Result of the first run. FAIL-WARD as registered, against a threshold I set without computing the
zero-mode term. In fact ward * N^4 * qhat^2 = 16.0 at every q and N run, to three digits: the deficit is exactly
the term left out with the zero mode, of order 1 / V, so the Ward identity holds. PASS-B at N = 48, n = 2: ratio
0.9255. At n = 1 the ratio is 0.64 at both N = 24 and N = 48, so it is a function of q N: a finite-size effect.

Follow-up criterion, written before that run: N = 72, n = 3 (the same q as N = 48, n = 2 and N = 24, n = 1).
    PASS-B2: | ratio - 1 | <= 0.05, and closer to 1 than the ratio 0.9255 at n = 2.

Run under the numeric lock, BLAS threads 1, nice, RSS checked against 2 GB.
"""
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

RSS_LIMIT_BYTES = 2 * 1024**3
DIM = 4


def check_rss():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT_BYTES:
        print("ABORT rss")
        sys.exit(3)


def plaquette_tables():
    """L_ij as coefficient vectors over (th_1, th_2, th_3, th_4), i, j in 0..3."""
    theta = np.array([1.0, 1.0, -1.0, -1.0])  # Theta
    a = np.array(
        [
            [0.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, -1.0, 0.0],
            [1.0, 1.0, -1.0, -1.0],
        ]
    )
    table = np.zeros((4, 4, 4))
    for i in range(4):
        for j in range(4):
            if i != j:
                table[i, j] = 2 * (a[i] - a[j]) + (1.0 if j > i else -1.0) * theta
    return table


S = np.array([1.0, 1.0, -1.0, -1.0])
LTAB = plaquette_tables()


def run(N, q, eps):
    q = np.asarray(q, dtype=float)
    eps = np.asarray(eps, dtype=float)
    k = 2 * np.pi * np.arange(N) / N
    hat2 = 4 * np.sin(k / 2) ** 2
    V = float(N**DIM)

    # lattice propagators at separation 0 and e_mu
    # p-sum by coordinates: 1 / phat^2 has no product form, so use a full grid, in slices
    grid = np.meshgrid(k, k, k, indexing="ij")
    p123 = [g.ravel() for g in grid]
    h123 = 4 * np.sin(p123[0] / 2) ** 2 + 4 * np.sin(p123[1] / 2) ** 2 + 4 * np.sin(p123[2] / 2) ** 2

    planes = list(itertools.combinations(range(DIM), 2))

    def t_plane(mu, nu):
        qm, qn = q[mu], q[nu]
        return np.array(
            [
                eps[mu] * np.exp(1j * qm / 2),
                eps[nu] * np.exp(1j * qm) * np.exp(1j * qn / 2),
                eps[mu] * np.exp(1j * qn) * np.exp(1j * qm / 2),
                eps[nu] * np.exp(1j * qn / 2),
            ]
        )

    # precompute per-plane coefficient c_ij = i s_i s_j L_ij . t
    plane_c = {}
    for mu, nu in planes:
        t = t_plane(mu, nu)
        c = np.zeros((4, 4), dtype=complex)
        for i in range(4):
            for j in range(4):
                if i != j:
                    c[i, j] = 1j * S[i] * S[j] * (LTAB[i, j] @ t)
        plane_c[(mu, nu)] = c

    g0 = 0.0
    ge = np.zeros(DIM)
    sum_h = 0.0  # sum ||W||^2 / (phat^2 (p+q)hat^2)
    sum_g = 0.0  # sum |w|^2 / (phat^2 (p+q)hat^2)

    for p0 in k:
        p = [np.full_like(p123[0], p0), p123[0], p123[1], p123[2]]
        ph2 = 4 * np.sin(p0 / 2) ** 2 + h123
        with np.errstate(divide="ignore"):
            g = np.where(ph2 > 1e-12, 1.0 / np.where(ph2 > 1e-12, ph2, 1.0), 0.0)
        g0 += g.sum()
        for mu in range(DIM):
            ge[mu] += (g * np.cos(p[mu])).sum()
        pq = [p[m] + q[m] for m in range(DIM)]
        pq2 = sum(4 * np.sin(pq[m] / 2) ** 2 for m in range(DIM))
        with np.errstate(divide="ignore"):
            gq = np.where(pq2 > 1e-12, 1.0 / np.where(pq2 > 1e-12, pq2, 1.0), 0.0)

        W = np.zeros((DIM, DIM, p[0].size), dtype=complex)
        phase_in = [np.exp(1j * p[m]) for m in range(DIM)]
        phase_out = [np.exp(-1j * pq[m]) for m in range(DIM)]
        for mu, nu in planes:
            c = plane_c[(mu, nu)]
            dirs = (mu, nu, mu, nu)
            # r_a: (0, mu, nu, 0)
            out = (1.0, phase_out[mu], phase_out[nu], 1.0)
            inn = (1.0, phase_in[mu], phase_in[nu], 1.0)
            for i in range(4):
                for j in range(4):
                    if i != j and c[i, j] != 0:
                        W[dirs[i], dirs[j]] += out[i] * inn[j] * c[i, j]
        # gauge term: for each direction, a minus field at r = -mu with beta_hat, a plus field at r = 0
        beta = [eps[m] * np.exp(-1j * q[m] / 2) for m in range(DIM)]
        for a in range(DIM):
            for b in range(DIM):
                # (a-, b-): tau tau = +1, 2 i (beta_b - beta_a)
                coef = 1j * 2 * (beta[b] - beta[a])
                out_a = np.exp(1j * pq[a])  # exp(-i (p+q).(-mu))
                in_b = np.exp(-1j * p[b])  # exp(i p.(-nu))
                W[a, b] += out_a * in_b * coef
                # (a-, b+): tau tau = -1, 2 i (0 - beta_a), times -1
                W[a, b] += out_a * (-1.0) * 1j * 2 * (0 - beta[a])
                # (a+, b-): tau tau = -1, 2 i (beta_b - 0), times -1
                W[a, b] += in_b * (-1.0) * 1j * 2 * (beta[b])
                # (a+, b+): zero
        w = np.zeros(p[0].shape, dtype=complex)
        for m in range(DIM):
            w += eps[m] * np.exp(1j * q[m] / 2) * (2j * phase_in[m] - 2j * phase_out[m])
        weight = g * gq
        sum_h += (weight * (np.abs(W) ** 2).sum(axis=(0, 1))).sum()
        sum_g += (weight * np.abs(w) ** 2).sum()
        check_rss()

    g0 /= V
    ge /= V

    # Tr(G H_2) per volume
    tr2 = 0.0
    for mu, nu in planes:
        t = t_plane(mu, nu)
        T = t[0] + t[1] - t[2] - t[3]
        # diagonal: -|T|^2 per field, four fields, G(0)
        tr2 += 4 * (-(abs(T) ** 2)) * g0
        # pairs (1, 3) and (3, 1): direction mu, separation nu
        L13 = LTAB[0, 2] @ t
        tr2 += 2 * (-S[0] * S[2] * abs(L13) ** 2) * ge[nu]
        L24 = LTAB[1, 3] @ t
        tr2 += 2 * (-S[1] * S[3] * abs(L24) ** 2) * ge[mu]
    # gauge term
    for m in range(DIM):
        tr2 += 8 * eps[m] ** 2 * ge[m]
    # ghost Tr(G Gh_2) per volume
    trg2 = 0.0
    for m in range(DIM):
        trg2 += 2 * eps[m] ** 2 * 4 * ge[m]

    phi2 = -(V * tr2 - sum_h) + 2 * (V * trg2 - sum_g)
    # A^(2)
    A2 = 0.0
    for mu, nu in planes:
        t = t_plane(mu, nu)
        T = t[0] + t[1] - t[2] - t[3]
        A2 += V * abs(T) ** 2
    return phi2, A2


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    ns = [int(a) for a in sys.argv[2:]] or [1, 2, 3, 6]
    b = 11 / (3 * np.pi**2)
    V = float(N**DIM)
    ok = True
    R = {}
    for n in ns:
        q = np.array([2 * np.pi * n / N, 0.0, 0.0, 0.0])
        qhat = 2 * np.sin(q / 2)
        pg, _ = run(N, q, qhat / np.linalg.norm(qhat))
        ward = abs(pg) / V
        phi2, A2 = run(N, q, np.array([0.0, 1.0, 0.0, 0.0]))
        R[n] = phi2 / A2
        print(f"N={N} n={n} q={q[0]:.4f} ward={ward:.3e} R={R[n]:.5f}", flush=True)
        if ward > 1e-2 / N**2:
            ok = False
    print("PASS-WARD" if ok else "FAIL-WARD")
    for n in ns:
        if 3 * n in R:
            d = (R[n] - R[3 * n]) / np.log(3)
            print(f"n={n}: (R(q) - R(3 q)) / log 3 = {d:.5f}, b = {b:.5f}, ratio {d / b:.4f}", flush=True)
    if N == 48 and 2 in R and 6 in R:
        d = (R[2] - R[6]) / np.log(3)
        print("PASS-B" if abs(d - b) <= 0.1 * b else "FAIL-B")


if __name__ == "__main__":
    main()
