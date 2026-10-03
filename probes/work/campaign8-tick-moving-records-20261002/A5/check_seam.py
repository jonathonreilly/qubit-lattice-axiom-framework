#!/usr/bin/env python3
"""Lane T check F: a seam between neighbourhoods ticking at different rates (supplied toy rule).

Region A (x < 0) takes one Dirac step per reference tick, region B (0 <= x <= xmax) takes two.
Per reference tick: W = U_full . U_B, where U_B is a Dirac step restricted to B with a turn-around at B's ends
(L at x=0 -> R at x=0; R at xmax -> L at xmax), so W is unitary and local.
Measured for packets sent into the seam from A and from B: transmitted / reflected weight and the wavenumber content.
Slot counting predicts: from the fast side at most r_slow/r_fast = 1/2 of the conveyor slots can pass.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np

N = 8000
xs = np.arange(N) - N // 2          # x from -N/2 .. N/2-1 ; A: x<0, B: 0<=x<xmax_idx
B = (xs >= 0) & (xs < N // 2 - 1)
iB = np.where(B)[0]
i0, imax = iB[0], iB[-1]


def coin(R, L, m, mask=None):
    c, s = np.cos(m), np.sin(m)
    if mask is None:
        return c * R - 1j * s * L, -1j * s * R + c * L
    R2, L2 = R.copy(), L.copy()
    R2[mask] = c * R[mask] - 1j * s * L[mask]
    L2[mask] = -1j * s * R[mask] + c * L[mask]
    return R2, L2


def step_full(R, L, m):
    return coin(np.roll(R, 1), np.roll(L, -1), m)


def step_B(R, L, m):
    R2, L2 = R.copy(), L.copy()
    # R: x -> x+1 inside B, R at xmax -> L at xmax
    R2[i0 + 1:imax + 1] = R[i0:imax]
    L2[imax] = R[imax]
    # L: x -> x-1 inside B, L at 0 -> R at 0
    L2[i0:imax] = L[i0 + 1:imax + 1]
    R2[i0] = L[i0]
    return coin(R2, L2, m, B)


def run(m, side, k, T=1300, w=120.0):
    R = np.zeros(N, complex)
    L = np.zeros(N, complex)
    if side == 'A':   # right-moving packet in A, centred at x=-600
        env = np.exp(-(xs + 600) ** 2 / (4 * w ** 2)) * np.exp(1j * k * xs)
        R[:] = env
    else:             # left-moving packet in B, centred at x=+1200
        env = np.exp(-(xs - 1200) ** 2 / (4 * w ** 2)) * np.exp(1j * k * xs)
        L[:] = env
    nrm = np.sqrt(np.sum(np.abs(R) ** 2 + np.abs(L) ** 2))
    R /= nrm
    L /= nrm
    for _ in range(T):
        R, L = step_B(R, L, m)
        R, L = step_full(R, L, m)
    P = np.abs(R) ** 2 + np.abs(L) ** 2
    inA = xs < 0
    return P[inA].sum(), P[~inA].sum(), R, L, P.sum()


for m in (0.0, 0.1):
    for side, k in (('A', 0.3), ('B', 0.15)):
        pA, pB, R, L, tot = run(m, side, k)
        if side == 'A':
            trans, refl = pB, pA
            reg = xs >= 0
        else:
            trans, refl = pA, pB
            reg = xs < 0
        # wavenumber content of the transmitted part (dominant component)
        comp = R if (side == 'A') else L
        f = np.abs(np.fft.fft(np.where(reg, comp, 0))) ** 2
        kk = 2 * np.pi * np.fft.fftfreq(N)
        order = np.argsort(f)[::-1]
        peaks = []
        for idx in order:
            if all(abs(np.angle(np.exp(1j * (kk[idx] - p)))) > 0.05 for p in peaks):
                peaks.append(kk[idx])
            if len(peaks) == 2:
                break
        wts = []
        for p in peaks:
            sel = np.abs(np.angle(np.exp(1j * (kk - p)))) < 0.05
            wts.append(f[sel].sum() / f.sum())
        print("m=%.1f from %s (k=%.2f): transmitted %.4f reflected %.4f (norm %.12f); transmitted wavenumbers %s with weights %s" % (
            m, side, k, trans, refl, tot, ", ".join("%+.3f" % p for p in peaks), ", ".join("%.3f" % x for x in wts)))
