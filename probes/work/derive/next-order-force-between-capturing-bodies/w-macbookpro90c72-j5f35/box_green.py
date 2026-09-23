#!/usr/bin/env python3
"""Finite-box factor of the Stokeslet at block 49's geometry (floating point; a numerical estimate, not a claim).

The lattice Stokes operator of check.py (forward-difference gradient, backward-difference divergence, 7-point Laplacian) has
xx-symbol ghat_xx(k) = (1 - s_x/S)/(nu S), s_j = 2 - 2 cos k_j, S = sum_j s_j; G_xx(d) is even in every component of d.
Geometries, all at nu = 1, force e_x at body 1, the x-component of the flow read at body 2 (16 sites along x):
  free     the continuum Stokeslet on the axis, 1/(4 pi r);
  lattice  the lattice Green function on a large periodic box with Hasimoto's uniform term added back (free-space lattice value);
  periodic a periodic box of side 96 (zero-mean flow);
  walls    block 49's box: reservoir layers 0,1 and L-2,L-1 of a side-96 box fix the density and give incoming records zero mean
           content, i.e. p = 0 and tangential g = 0 on the walls with the normal flux free. That problem is diagonal in the
           mixed sine/cosine basis, equivalently an image system in a periodic box of side 2D (D = wall-to-wall distance): images
           of f = e_x reflect with f -> -R f (x-reflection keeps the sign, y- and z-reflections flip it). Walls at 1.5 and 93.5
           (D = 92), with D = 90 and 94 for sensitivity.
usage: box_green.py"""
import numpy as np

XI = 2.837297  # Hasimoto's constant for the simple-cubic array


def gxx_periodic(M: int) -> np.ndarray:
    k = 2 * np.pi * np.fft.fftfreq(M)
    s = 2 - 2 * np.cos(k)
    sx = s[:, None, None]
    S = sx + s[None, :, None] + s[None, None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        gh = (1 - sx / S) / S
    gh[0, 0, 0] = 0.0
    return np.fft.ifftn(gh).real  # G_xx(d) = (1/M^3) sum_k ghat e^{ik.d}


def main() -> None:
    r = 16
    free = 1 / (4 * np.pi * r)
    out = [f"free-space continuum Stokeslet on the axis at r = {r}: G_xx = 1/(4 pi r) = {free:.6f} (nu = 1)"]
    # periodic side 96 and the free-space lattice value (periodic 192 plus Hasimoto's uniform term)
    G96 = gxx_periodic(96)
    per96 = G96[r, 0, 0]
    G192 = gxx_periodic(192)
    lat = G192[r, 0, 0] + XI / (6 * np.pi * 192)
    out.append(f"periodic side 96: G_xx = {per96:.6f} ({per96 / free:.3f} of free); lattice free-space value (side 192 + Hasimoto): "
               f"{lat:.6f} ({lat / free:.3f} of free); periodic 96 with Hasimoto's term alone: {(free - XI / (6 * np.pi * 96)) / free:.3f} of free")
    del G96, G192
    # block 49's box: bodies at x = 40 and 56, y = z = 48; walls at w0 and w1
    for (w0, w1) in ((1.5, 93.5), (0.5, 94.5), (2.5, 92.5)):
        D = w1 - w0
        M = int(round(2 * D))
        G = gxx_periodic(M)
        x1 = np.array([40.0, 48.0, 48.0]); x2 = np.array([56.0, 48.0, 48.0])
        tot = 0.0
        for fx in (0, 1):
            for fy in (0, 1):
                for fz in (0, 1):
                    img = x1.copy(); sign = 1.0
                    if fx: img[0] = 2 * w0 - img[0]                  # x-reflection: f_x keeps its sign
                    if fy: img[1] = 2 * w0 - img[1]; sign = -sign     # y-reflection: f_x flips
                    if fz: img[2] = 2 * w0 - img[2]; sign = -sign     # z-reflection: f_x flips
                    d = np.rint(x2 - img).astype(int) % M
                    tot += sign * G[d[0], d[1], d[2]]
        out.append(f"walls at {w0}, {w1} (D = {D:.0f}, image box {M}): G_xx at body 2 = {tot:.6f} ({tot / free:.3f} of free, {tot / lat:.3f} of the lattice free-space value)")
        del G
    print("\n".join(out))


if __name__ == "__main__":
    main()
