#!/usr/bin/env python3
"""Lane T check C: time dilation of a moving packet's internal clock under the 1D Dirac step.

Supplied model: the walker carries an internal two-state clock {a, b}; the mixing angle depends on the clock state,
m_a = m - delta/2, m_b = m + delta/2 (internal energy entering as mass). Each clock component is a positive-band packet
(Gaussian in k around k0, width sigma_k) of its own step. Exact evolution in k-space (the step is diagonal in k).
Measured:
  * clock coherence C(t) = <psi_b(t)|psi_a(t)>, its phase slope / delta  -> clock rate R (rest value 1)
  * packet centroid velocity v from real-space positions at t=0 and t=T (inverse FFT)
Compared with the lattice law R = sign(cos k0) sqrt(1 - v^2/cos^2 m) and the continuum law sqrt(1 - v^2).
Also a decoupled internal rotation (fixed phase per tick, not entering the mixing) -> rate 1 at every speed.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np

N = 2 ** 14
x = np.arange(N)
k = 2 * np.pi * np.fft.fftfreq(N)


def bands(m):
    c, s = np.cos(m), np.sin(m)
    U = np.zeros((N, 2, 2), complex)
    U[:, 0, 0] = c * np.exp(-1j * k)
    U[:, 0, 1] = -1j * s * np.exp(1j * k)
    U[:, 1, 0] = -1j * s * np.exp(-1j * k)
    U[:, 1, 1] = c * np.exp(1j * k)
    lam, V = np.linalg.eig(U)
    w = -np.angle(lam)
    # positive band: quasi-energy in (0, pi)
    idx = np.argmax(w, axis=1)
    wp = w[np.arange(N), idx]
    up = V[np.arange(N), :, idx]
    up = up / np.linalg.norm(up, axis=1)[:, None]
    return wp, up


def packet(m, k0, sk):
    wp, up = bands(m)
    dk = np.angle(np.exp(1j * (k - k0)))
    g = np.exp(-dk ** 2 / (4 * sk ** 2))
    # fix the gauge of up smoothly near k0: make the R component real-positive (it is nonzero near k0 unless degenerate)
    ph = up[:, 0] / np.maximum(np.abs(up[:, 0]), 1e-300)
    upg = up * np.conj(ph)[:, None]
    # center the packet at x = N/4 in real space
    amp = g * np.exp(-1j * k * (N // 4))
    psi = amp[:, None] * upg
    psi /= np.linalg.norm(psi)
    return psi, wp


def centroid(psik):
    # psi(x) = ifft over k for each component
    px = np.fft.ifft(psik, axis=0)
    p = np.sum(np.abs(px) ** 2, axis=1)
    p /= p.sum()
    # unwrap around the expected center using circular mean
    ang = np.angle(np.sum(p * np.exp(2j * np.pi * x / N)))
    return ang * N / (2 * np.pi)


m, delta, sk, T = 0.3, 1e-3, 0.004, 400
print("m=%.2f delta=%.0e sigma_k=%.3f T=%d ticks; cos m = %.6f" % (m, delta, sk, T, np.cos(m)))
print("   k0      v_meas     R_meas      R_lattice=sgn(cos k0)sqrt(1-v^2/cos^2m)   R_cont=sqrt(1-v^2)   rel.err(lattice)")
for k0 in (0.0, 0.05, 0.1, 0.3, 0.6, 1.0, 1.4, np.pi / 2, 1.8, 2.4, 3.0):
    psa, wa = packet(m - delta / 2, k0, sk)
    psb, wb = packet(m + delta / 2, k0, sk)
    ts = np.arange(0, T + 1, 20)
    ph = []
    for t in ts:
        a = psa * np.exp(-1j * wa * t)[:, None]
        b = psb * np.exp(-1j * wb * t)[:, None]
        ph.append(np.angle(np.vdot(b, a)))
    ph = np.unwrap(np.array(ph))
    slope = np.polyfit(ts, ph, 1)[0]
    R_meas = slope / delta
    # centroid velocity of the mean-mass packet
    ps0, w0 = packet(m, k0, sk)
    x0 = centroid(ps0)
    x1 = centroid(ps0 * np.exp(-1j * w0 * T)[:, None])
    dx = (x1 - x0 + N / 2) % N - N / 2
    v = dx / T
    Rl = np.sign(np.cos(k0)) * np.sqrt(max(0.0, 1 - v ** 2 / np.cos(m) ** 2))
    Rc = np.sqrt(max(0.0, 1 - v ** 2))
    err = abs(R_meas - Rl) / max(abs(Rl), 1e-3)
    print("  %5.3f  %9.6f  %+10.6f   %+10.6f                              %9.6f          %.1e" % (k0, v, R_meas, Rl, Rc, err))

print("\n-- decoupled internal rotation (phase eps per tick, independent of the mixing): rate/eps at several speeds")
eps = 1e-3
for k0 in (0.0, 0.6, 1.4):
    ps0, w0 = packet(m, k0, sk)
    ts = np.arange(0, T + 1, 20)
    ph = []
    for t in ts:
        a = ps0 * np.exp(-1j * (w0 - eps / 2) * t)[:, None]
        b = ps0 * np.exp(-1j * (w0 + eps / 2) * t)[:, None]
        ph.append(np.angle(np.vdot(b, a)))
    slope = np.polyfit(ts, np.unwrap(np.array(ph)), 1)[0]
    print("   k0=%.2f  rate/eps = %.6f  (no dilation)" % (k0, slope / eps))
