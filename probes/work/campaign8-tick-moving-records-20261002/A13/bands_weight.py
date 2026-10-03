#!/usr/bin/env python3
"""A13 check 5: where the quiet formation weight looks, on the 1D cycle (brickwork of partial swaps) over the
aligned emptiness (supplied toy).

One-excitation Bloch matrix (2-site cell, relative to the emptiness):
  even step  W_e   = e^{i th} [[cos, -i sin], [-i sin, cos]]
  odd step   W_o(K)= e^{i th} [[cos, -i sin e^{-iK}], [-i sin e^{iK}, cos]]
  U(K) = W_o(K) W_e  (one round = two ticks).
Registration chance per tick for a delocalized Bloch eigenstate (a, b) under F = c P_singlet on the tick's pairs:
  even tick: c |a - b|^2 / 2 ;  odd tick: c |b - a e^{iK}|^2 / 2   (per excitation; EXACT for plane waves).
Claims checked: (i) a branch with quasi-energy exactly 0 at K = 0 (the rotated emptiness: never registered),
quadratic nearby; (ii) the linear (Dirac-like) crossing at K = pi sits at quasi-energy 2 th relative to the
emptiness, where the registration chance is the largest, c/2 per tick.
"""
import numpy as np


def U(K, th):
    c, s = np.cos(th), np.sin(th)
    We = np.exp(1j * th) * np.array([[c, -1j * s], [-1j * s, c]])
    Wo = np.exp(1j * th) * np.array([[c, -1j * s * np.exp(-1j * K)], [-1j * s * np.exp(1j * K), c]])
    return Wo, We


def main():
    th = 0.6
    print(f"theta = {th}")
    for K in [0.0, 0.05, 0.1, 0.2, np.pi - 0.1, np.pi - 0.05, np.pi]:
        Wo, We = U(K, th)
        ev, vec = np.linalg.eig(Wo @ We)
        out = []
        for k in range(2):
            ph = np.angle(ev[k])
            v = vec[:, k] / np.linalg.norm(vec[:, k])
            a, b = v
            w_even = abs(a - b) ** 2 / 2
            v2 = We @ v                                  # state entering the odd tick
            a2, b2 = v2 / np.linalg.norm(v2)
            w_odd = abs(b2 - a2 * np.exp(1j * K)) ** 2 / 2
            out.append(f"phase {ph:+.6f} (|phase|/K^2 = {abs(ph)/K**2 if K>0 else float('nan'):.4f}) "
                       f"weight/c even {w_even:.4f} odd {w_odd:.4f}")
        print(f"  K={K:.3f}: " + " | ".join(out))
    print(f"  predicted: soft-branch coefficient tan(th)/4 per round = {np.tan(th)/4:.4f} (from cos w = cos^2 th - "
          f"sin^2 th cos K);  crossing phase 2 th = {2*th:.4f}")


if __name__ == '__main__':
    main()
