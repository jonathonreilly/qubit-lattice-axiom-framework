#!/usr/bin/env python3
"""Gaussian approximation of the contact and surface terms (criteria G1-G5).

Plaquette fields of orientation (mu,nu) based at x have the covariance
(4/beta) P with P the orthogonal projector on exact two-forms, so
Cov(s_p,s_q) = (3/(2 beta^2)) P_pq^2. All outputs are in units of 1/beta^2.
"""
import os, resource, sys, itertools
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np


def check_rss(limit_gb=2.0):
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9  # bytes on darwin
    if rss > limit_gb:
        sys.exit(f"RSS {rss:.2f} GB above limit")


ORIENT = list(itertools.combinations(range(4), 2))


def kernels(T):
    """Return P[(o1,o2)](x) real arrays via FFT. P(k) = D(k) D*(k)/khat^2 for k != 0."""
    k1 = 2 * np.pi * np.fft.fftfreq(T)
    ks = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    # forward difference symbol d_mu(k) = exp(i k_mu) - 1
    d = [np.exp(1j * k) - 1 for k in ks]
    khat2 = sum(np.abs(x) ** 2 for x in d)
    khat2[0, 0, 0, 0] = np.inf
    out = {}
    # F_{mu nu}(k) = d_mu A_nu - d_nu A_mu; on transverse A, A*A^dagger covariance 1/khat2
    # P_{(mu nu),(rho sig)}(k) = (d_mu conj(d_rho) delta_{nu sig} - d_mu conj(d_sig) delta_{nu rho}
    #                            - d_nu conj(d_rho) delta_{mu sig} + d_nu conj(d_sig) delta_{mu rho})/khat2
    for i, (m, n) in enumerate(ORIENT):
        for j, (r, s) in enumerate(ORIENT):
            if j < i:
                continue
            sym = np.zeros((T, T, T, T), dtype=np.complex128)
            if n == s:
                sym += d[m] * np.conj(d[r])
            if n == r:
                sym -= d[m] * np.conj(d[s])
            if m == s:
                sym -= d[n] * np.conj(d[r])
            if m == r:
                sym += d[n] * np.conj(d[s])
            sym /= khat2
            out[(i, j)] = np.fft.ifftn(sym)
            check_rss()
    return out


def main():
    results = {}
    for T in (16, 24, 32):
        P = kernels(T)
        # G1: 3/2 sum_{o,o'} sum_x |P(x)|^2 = 3/2 Tr P per site = 9/2 (1 - 1/T^4) in the
        # sense that k = 0 is removed (rank 3 for each k != 0).
        total = 0.0
        for (i, j), arr in P.items():
            w = 1 if i == j else 2
            total += w * np.sum(np.abs(arr) ** 2)
        g1 = 1.5 * total
        g1_exact = 4.5 * (1 - 1 / T**4)
        print(f"T={T} G1 sum rule {g1:.8f} exact {g1_exact:.8f}")
        # plaquette correlator r(o,o',x) = 3/2 |P_{o o'}(x)|^2, forward energy
        r = np.zeros((T, T, T, T))
        for (i, j), arr in P.items():
            r += (1 if i == j else 2) * 1.5 * np.abs(arr) ** 2
        # forward-energy correlator has symmetrization caveat for i<j: use real symmetric part
        # G3
        axis = [r[x, 0, 0, 0] for x in range(1, T // 2 + 1)]
        if T >= 32:
            s = (np.log(axis[7]) - np.log(axis[3])) / (np.log(8) - np.log(4))
            print(f"T={T} G3 on-axis slope 4..8: {s:.3f}")
        # G2 and blocks need weights on plaquettes, so build exact interface sums per orientation.
        # Time direction index 0. Closed half 0<=t<=T/2: plaquette (o,x) spans 0 and n.
        # Membership weights for + side, per plaquette (o, t):
        #   oriented with 0 in o: spans t..t+1, in + if 0<=t<T/2, weight 1 else 0.
        #   oriented without 0: at time t: weight 1/2 at t=0 or T/2, 1 if 0<t<T/2, else 0.
        wplus = {}
        for i, (m, n) in enumerate(ORIENT):
            w = np.zeros(T)
            if m == 0 or n == 0:
                w[:T // 2] = 1.0
            else:
                w[1:T // 2] = 1.0
                w[0] = 0.5
                w[T // 2] = 0.5
            wplus[i] = w
        wminus = {i: 1 - wplus[i] for i in wplus}
        # time-time correlators summed over space: c[(i,j)](dt) = 3/2 sum_xbar |P|^2 per spatial site
        cov = 0.0
        for (i, j), arr in P.items():
            ct = 1.5 * np.sum(np.abs(arr) ** 2, axis=(1, 2, 3))
            # sum over t,t' of wplus_i(t) wminus_j(t') ct(t'-t) + symmetric part
            fp = np.fft.fft(wplus[i])
            fm = np.fft.fft(wminus[j])
            fc = np.fft.fft(ct)
            # Cov(s_{i,t}, s_{j,t'}) uses P_{ij}(t'-t) by the convention x = target - source
            val = np.real(np.sum(np.conj(fp) * fm * fc)) / T
            if i != j:
                fp2 = np.fft.fft(wplus[j])
                fm2 = np.fft.fft(wminus[i])
                val += np.real(np.sum(np.conj(fp2) * fm2 * np.conj(fc))) / T
            cov += val
        # cov is per spatial site, for the two planes
        print(f"T={T} G2 Cov(W+,W-) per plane site {cov/2:.5f} target 0.75")
        results[T] = (P, r)
        if T < 32:
            del P, r
            results[T] = None
        check_rss()
    # G4, G5 at T=32 with closed cubes of side ell = 2,4,8 lattice units, block weights 2^-c.
    T = 32
    P, r = results[T]
    h2 = 4.5 * (1 - 1 / T**4)
    prev = None
    for ell in (2, 4, 8):
        # block B: closed cube [0,ell]^4; plaquette (o,x) in B with weight 2^-c.
        B_w = {}
        for i, (m, n) in enumerate(ORIENT):
            w = np.zeros((T, T, T, T))
            ranges = []
            for mu in range(4):
                if mu == m or mu == n:
                    arr = np.zeros(T)
                    arr[:ell] = 1.0
                else:
                    arr = np.zeros(T)
                    arr[:ell + 1] = 1.0
                    arr[0] = 0.5
                    arr[ell] = 0.5
                ranges.append(arr)
            w = np.einsum("i,j,k,l->ijkl", *ranges, optimize=True)
            B_w[i] = np.fft.fftn(w)
            check_rss()
        var = 0.0
        for (i, j), arr in P.items():
            Fc = np.fft.fftn(1.5 * np.abs(arr) ** 2)
            v = np.real(np.sum(np.conj(B_w[i]) * B_w[j] * Fc)) / T**4
            var += v if i == j else 2 * v
        size = ell**4
        d = size * h2 - var
        print(f"ell={ell} Var(W_B)={var:.5f} |B|h''={size*h2:.5f} D_B={d:.5f} D_B/ell^3={d/ell**3:.5f}")
        if prev is not None:
            print(f"   ratio D_B/ell^3 to previous {d/ell**3/prev:.4f}")
        prev = d / ell**3
    print("peak RSS GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9)


if __name__ == "__main__":
    main()
