#!/usr/bin/env python3
"""Decisive question at Gaussian level: variance of a smooth bump against its separated covariance."""
import os, sys, resource, itertools
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

ORIENT = list(itertools.combinations(range(4), 2))


def correlator(T):
    k1 = 2 * np.pi * np.fft.fftfreq(T)
    ks = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    d = [np.exp(1j * k) - 1 for k in ks]
    khat2 = sum(np.abs(x) ** 2 for x in d)
    khat2[0, 0, 0, 0] = np.inf
    r = np.zeros((T, T, T, T))
    for i, (m, n) in enumerate(ORIENT):
        for j, (rr, s) in enumerate(ORIENT):
            if j < i:
                continue
            sym = np.zeros((T, T, T, T), dtype=np.complex128)
            if n == s:
                sym += d[m] * np.conj(d[rr])
            if n == rr:
                sym -= d[m] * np.conj(d[s])
            if m == s:
                sym -= d[n] * np.conj(d[rr])
            if m == rr:
                sym += d[n] * np.conj(d[s])
            sym /= khat2
            p = np.fft.ifftn(sym)
            if i == j:
                r += 1.5 * np.abs(p) ** 2
            else:
                # P_{ij}(x) and P_{ji}(x) have the same modulus at x and -x; add both for a symmetric kernel
                a = 1.5 * np.abs(p) ** 2
                r += a + a[tuple(np.ix_(*[(-np.arange(T)) % T] * 4))]
            del p, sym
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > 2.0:
                sys.exit("RSS above 2 GB")
    return r


def phi1(u):
    # compact bump in u, u = x/T, width 1/8 on each side
    w = 1.0 / 8
    z = np.abs(u) / w
    out = np.zeros_like(u)
    inside = z < 1
    out[inside] = np.exp(1 - 1 / (1 - z[inside] ** 2))
    return out


def main():
    # continuum norm by fine sum
    g = np.linspace(-0.2, 0.2, 400001)
    n2 = (np.sum(phi1(g) ** 2) * (g[1] - g[0])) ** 4
    print(f"||phi||_2^2 = {n2:.8e}")
    for T in (16, 24, 32, 48):
        r = correlator(T)
        M0 = r.sum()
        M2 = sum(((((np.arange(T) + T // 2) % T - T // 2) ** 2).reshape([T if k == mu else 1 for k in range(4)]) * r).sum() for mu in range(4))
        x = (np.arange(T) - T // 2) / T
        f1 = phi1(x)
        f = np.einsum("i,j,k,l->ijkl", f1, f1, f1, f1, optimize=True)
        F = np.fft.fftn(f)
        Fr = np.fft.fftn(r)
        conv = np.real(np.fft.ifftn(F * Fr))
        var = float(np.sum(f * conv))
        shift = 3 * T // 8
        cov = float(np.sum(np.roll(f, shift, axis=0) * conv))
        sumf2 = float(np.sum(f**2))
        # B4: periodic array of the same bump with period T/4 (images touch at the faces, vanishing to all orders).
        arr = np.zeros_like(f)
        for k in itertools.product(range(4), repeat=4):
            arr += np.roll(f, tuple(int(c) * T // 4 for c in k), axis=(0, 1, 2, 3))
        conv_arr = np.real(np.fft.ifftn(np.fft.fftn(arr) * Fr))
        var_arr = float(np.sum(arr * conv_arr))
        X = var_arr / 4**4 - var
        del arr, conv_arr
        grad = (var - 4.5 * sumf2) / T**2
        print(f"T={T} M0={M0:.6f} M2={M2:.5f} V={var:.6e} V/T^4={var/T**4:.6e} target {4.5*n2:.6e} "
              f"(V-4.5 sum f^2)/T^2={grad:.6e} C={cov:.6e} X={X:.6e}", flush=True)
        del r, F, Fr, conv, f


if __name__ == "__main__":
    main()
