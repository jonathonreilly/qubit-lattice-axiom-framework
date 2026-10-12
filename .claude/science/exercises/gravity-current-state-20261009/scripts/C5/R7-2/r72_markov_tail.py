#!/usr/bin/env python3
"""R7-2: is a (near) scale-invariant Gaussian 'late-time record field' on Z^3 a finite-range Markov field?

For a stationary Gaussian field on Z^3 with power spectrum P(k), the conditional law of phi_x given all
other sites depends on the sites y with Q(x-y) != 0, where Q = inverse covariance has symbol 1/P(k)
(standard Gaussian-Markov fact).  Finite-range (nearest-neighbour) Markov <=> 1/P is a trigonometric
polynomial of degree 1.  Here 1/P(k) = (khat^2)^{alpha/2}, khat^2 = sum_i 4 sin^2(k_i/2), alpha = 4 - n_s
(dS/CFT / inflationary late-time spectrum P ~ k^{n_s-4}).  Control: alpha = 2 (lattice Laplacian, NN).
We compute Q(r) by FFT on an N^3 torus and fit its tail along the axis and body diagonal."""
import numpy as np

def Q_of_r(alpha, N):
    k = 2 * np.pi * np.fft.fftfreq(N)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    khat2 = 4 * (np.sin(kx / 2) ** 2 + np.sin(ky / 2) ** 2 + np.sin(kz / 2) ** 2)
    sym = khat2 ** (alpha / 2)
    Q = np.real(np.fft.ifftn(sym))
    return Q

N = 96
for alpha, label in [(2.0, "control: Laplacian (alpha=2)"), (4 - 0.9649, "n_s = 0.9649 (alpha = 3.0351)"), (3.0, "exact scale invariance (alpha=3)")]:
    Q = Q_of_r(alpha, N)
    print(f"--- {label}, N={N} ---")
    rs = [1, 2, 3, 4, 6, 8, 12, 16, 24]
    ax = [Q[r, 0, 0] for r in rs]
    dg = [Q[r, r, r] for r in rs if r <= N // 4]
    print("  axis  r, Q(r):", ", ".join(f"{r}:{q:+.3e}" for r, q in zip(rs, ax)))
    print("  diag  r, Q(r,r,r):", ", ".join(f"{r}:{q:+.3e}" for r, q in zip(rs, dg)))
    # tail fit along axis for 4 <= r <= 16
    rr = np.array([4, 6, 8, 12, 16]); qq = np.abs(np.array([Q[r, 0, 0] for r in rr]))
    if np.all(qq > 1e-14):
        slope = np.polyfit(np.log(rr), np.log(qq), 1)[0]
        print(f"  axis tail exponent (4<=r<=16): |Q| ~ r^{slope:.3f}  (continuum prediction -(3+alpha) = {-(3+alpha):.3f})")
    else:
        print(f"  axis tail: |Q(r)| < 1e-14 for r >= 4 (finite range)")
    beyond = np.abs(Q).copy()
    # zero out NN shell to check range
    for (i, j, l) in [(0, 0, 0), (1, 0, 0), (N - 1, 0, 0), (0, 1, 0), (0, N - 1, 0), (0, 0, 1), (0, 0, N - 1)]:
        beyond[i, j, l] = 0
    print(f"  max |Q| outside the site and its 6 neighbours: {beyond.max():.3e}")
