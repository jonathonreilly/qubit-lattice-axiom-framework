#!/usr/bin/env python3
"""Criterion G3b: on-axis forward energy correlator via partial Fourier sums, large T."""
import os, sys, resource, itertools
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

ORIENT = list(itertools.combinations(range(4), 2))


def main(T):
    kp = 2 * np.pi * np.fft.fftfreq(T)
    d_perp = [np.exp(1j * k) - 1 for k in np.meshgrid(kp, kp, kp, indexing="ij")]  # directions 1,2,3
    perp2 = sum(np.abs(x) ** 2 for x in d_perp)
    k0s = 2 * np.pi * np.arange(T) / T
    Q = {}
    for i, j in itertools.product(range(6), range(6)):
        if j < i:
            continue
        Q[(i, j)] = np.zeros(T, dtype=np.complex128)
    for t, k0 in enumerate(k0s):
        d0 = np.exp(1j * k0) - 1
        den = perp2 + abs(d0) ** 2
        if t == 0:
            den = den.copy()
            den[0, 0, 0] = np.inf
        d = [np.full_like(d_perp[0], d0)] + d_perp
        for i, (m, n) in enumerate(ORIENT):
            for j, (r, s) in enumerate(ORIENT):
                if j < i:
                    continue
                sym = 0
                if n == s:
                    sym = sym + d[m] * np.conj(d[r])
                if n == r:
                    sym = sym - d[m] * np.conj(d[s])
                if m == s:
                    sym = sym - d[n] * np.conj(d[r])
                if m == r:
                    sym = sym + d[n] * np.conj(d[s])
                if np.isscalar(sym) and sym == 0:
                    continue
                Q[(i, j)][t] = np.sum(sym / den) / T**3
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > 2.0:
            sys.exit("RSS above 2 GB")
    r = np.zeros(T)
    for (i, j), q in Q.items():
        p = np.fft.ifft(q)  # x along direction 0
        r += (1 if i == j else 2) * 1.5 * np.abs(p) ** 2
    print(f"T={T}  target x^8 r(x) -> 9/pi^4 = {9/np.pi**4:.5f}")
    for x in (2, 3, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48):
        if x < T // 2:
            print(f"x={x:3d} r={r[x]:.6e} x^8 r={x**8*r[x]:.5f}")


if __name__ == "__main__":
    main(int(sys.argv[1]))
