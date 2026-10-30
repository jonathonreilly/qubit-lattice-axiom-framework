#!/usr/bin/env python3
"""Criterion B3': separated bump covariance with the continuum kernel, periodic images."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np


def phi1(u):
    w = 1.0 / 8
    z = np.abs(u) / w
    out = np.zeros_like(u)
    inside = z < 1
    out[inside] = np.exp(1 - 1 / (1 - z[inside] ** 2))
    return out


def main():
    for T in (32, 48, 64, 96):
        c = (np.arange(T) + T // 2) % T - T // 2
        r = np.zeros((T, T, T, T))
        grids = np.meshgrid(c, c, c, c, indexing="ij", sparse=True)
        x2 = sum(g.astype(float) ** 2 for g in grids)
        x2[0, 0, 0, 0] = 1e30
        r = 9.0 / np.pi**4 * x2**-4  # nearest image only; further images are O(T^-8) each
        del x2
        x = (np.arange(T) - T // 2) / T
        f1 = phi1(x)
        f = np.einsum("i,j,k,l->ijkl", f1, f1, f1, f1, optimize=True)
        shift = 3 * T // 8
        g = np.roll(f, shift, axis=0)
        conv = np.fft.irfftn(np.fft.rfftn(f) * np.fft.rfftn(r), s=f.shape)
        print(f"T={T} C_cont={float(np.sum(g*conv)):.6e}", flush=True)
        del r, f, g, conv


if __name__ == "__main__":
    main()
