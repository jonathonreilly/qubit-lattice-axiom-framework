#!/usr/bin/env python3
"""A22 task 4 (supplied toy): is doubled content visible to records?
One excitation on A19's round (cells, A19 core1d.step convention).  Lambda = (-1)^j sigma_z per cell (site pattern + - - +).
 (a) exact identity  Lambda U Lambda^-1 = -U  on the one-excitation sector;
 (b) single-tick site-diagonal formation weights (n_x) respond identically to psi and Lambda psi;
 (c) A12-type T-tick energy window (seed at one site, carrier Omega, DPSS taper): response to ordinary content
     vs its doubled image (equal to the window shifted by pi);
 (d) A5's internal clock (two internal states, masses m +- delta/2): relative-phase rate for ordinary content,
     for its Lambda image, and for the other branch at K+pi ('backward clock').
 (e) A13-type weight P_singlet on a flipped bond is mapped by Lambda to P_triplet0 (not invariant).
"""
import numpy as np
from scipy.signal.windows import dpss
from core1d import step, plus_band, PI

M = 1024
m = 0.3
j = np.arange(M)


def lam(a, b):
    s = (-1.0) ** j
    return s * a, -s * b


def packet(K0, w, j0, band=+1, mm=m):
    K = 2 * PI * np.arange(M) / M
    dK = (K - K0 + PI) % (2 * PI) - PI
    ph = np.exp(-dK ** 2 * w ** 2) * np.exp(-1j * K * j0)
    uA, uB = plus_band(K, mm)
    if band < 0:
        uA, uB = -np.conj(uB), np.conj(uA)
    a = np.fft.ifft(ph * uA) * M; b = np.fft.ifft(ph * uB) * M
    n = np.sqrt(np.sum(np.abs(a) ** 2 + np.abs(b) ** 2))
    return a / n, b / n


# (a) identity
rng = np.random.default_rng(3)
a = rng.normal(size=M) + 1j * rng.normal(size=M); b = rng.normal(size=M) + 1j * rng.normal(size=M)
la, lb = lam(a, b); ua, ub = step(la, lb, m); va, vb = step(a, b, m); wa, wb = lam(va, vb)
print(f"(a) || Lambda U psi + U Lambda psi || = {np.sqrt(np.sum(np.abs(ua + wa)**2 + np.abs(ub + wb)**2)):.2e}  (Lambda U = -U Lambda)")

# (b) site densities over 50 ticks
a, b = packet(0.4, 12.0, 300)
la, lb = lam(a, b)
dmax = 0.0
for t in range(50):
    dmax = max(dmax, np.abs(np.abs(a) ** 2 - np.abs(la) ** 2).max(), np.abs(np.abs(b) ** 2 - np.abs(lb) ** 2).max())
    a, b = step(a, b, m); la, lb = step(la, lb, m)
print(f"(b) max |density(psi) - density(Lambda psi)| over 50 ticks, all sites: {dmax:.2e}")
# interference of ordinary + doubled content: tick-alternating, period-4 fringe
a, b = packet(0.4, 12.0, 300); la, lb = lam(a, b)
ca, cb = (a + 0.5 * la) / np.sqrt(1.25), (b + 0.5 * lb) / np.sqrt(1.25)
fr = []
for t in range(4):
    dens = np.abs(ca) ** 2 + np.abs(cb) ** 2
    plain = (np.abs(a) ** 2 + np.abs(b) ** 2)
    fr.append(np.sum(np.abs(ca[300]) ** 2 + np.abs(cb[300]) ** 2) / np.sum(np.abs(a[300]) ** 2 + np.abs(b[300]) ** 2))
    ca, cb = step(ca, cb, m); a, b = step(a, b, m)
print(f"    coherent mix psi + 0.5 Lambda psi: weight ratio at cell 300 vs pure psi, ticks 0..3: " + ", ".join(f"{x:.3f}" for x in fr)
      + "  (alternates: fringe (1 +- 2*0.5*cos)/1.25)")

# (c) energy window: seed = site a_{x0}; response |sum_t w(t) e^{i Omega t} <seed|U^t psi>|^2 / sum w^2
x0 = 512
K0 = 0.35
for T in (8, 16, 32, 64):
    tap = dpss(T, NW=3.0)
    a, b = packet(K0, 20.0, x0 - 0, band=+1)
    la, lb = lam(a, b)
    amps, lamps = [], []
    for t in range(T):
        amps.append(a[x0]); lamps.append(la[x0])
        a, b = step(a, b, m); la, lb = step(la, lb, m)
    amps, lamps = np.array(amps), np.array(lamps)
    # carrier: the ordinary packet's quasi-energy phase per tick (measured: best carrier over a fine grid)
    Om = np.linspace(-PI, PI, 4001)
    resp = np.abs(np.exp(1j * np.outer(Om, np.arange(T))) @ (tap * amps)) ** 2 / np.sum(tap ** 2)
    io = np.argmax(resp)
    r_ord = resp[io]
    r_dbl = np.abs(np.exp(1j * Om[io] * np.arange(T)) @ (tap * lamps)) ** 2 / np.sum(tap ** 2)
    r_shift = np.abs(np.exp(1j * (Om[io] + PI) * np.arange(T)) @ (tap * amps)) ** 2 / np.sum(tap ** 2)
    print(f"(c) T={T:3d} DPSS(NW=3) window tuned to ordinary content (Omega={Om[io]:+.3f}): ordinary {r_ord:.3e}, "
          f"doubled image {r_dbl:.3e}  (ratio {r_dbl/r_ord:.1e}; window shifted by pi on psi: {r_shift:.3e})")

# (d) clock: internal states with masses m +- delta/2, relative phase rate per tick
delta = 1e-3
def clock_rate(K0, band, apply_lambda):
    out = []
    for mm in (m + delta / 2, m - delta / 2):
        a, b = packet(K0, 40.0, 512, band=band, mm=m)
        if apply_lambda:
            a, b = lam(a, b)
        a0, b0 = a.copy(), b.copy()
        for t in range(200):
            a, b = step(a, b, mm)
        out.append((a, b))
    (a1, b1), (a2, b2) = out
    ov = np.sum(np.conj(a2) * a1 + np.conj(b2) * b1)       # <phi_-|phi_+>
    return -np.angle(ov) / 200 / delta                       # d(phase)/dt per unit delta (sign: e^{-iE} convention)
K0 = 0.35
cosW = np.cos(m) * np.cos(K0); W = np.arccos(cosW)
pred = np.sin(m) * np.cos(K0) / np.sin(W)                    # dW/dm at fixed K (band '+' quasi-energy = W + const)
print(f"(d) clock rate per unit delta: ordinary band+ at K0 {clock_rate(K0, +1, False):+.4f}; its Lambda image {clock_rate(K0, +1, True):+.4f}; "
      f"band+ at K0+pi {clock_rate(K0 + PI, +1, False):+.4f}; band- at K0+pi {clock_rate(K0 + PI, -1, False):+.4f}  (dW/dm = {pred:+.4f})")

# (e) P_singlet on a flipped bond under Lambda (2 qubits, signs (+,-)): Z_2 P_s Z_2 = P_t0
Ps = np.zeros((4, 4)); v = np.array([0, 1, -1, 0]) / np.sqrt(2); Ps = np.outer(v, v)
Z2 = np.diag([1, -1, 1, -1])            # sign on the second site (basis 00,01,10,11)
Pt0 = np.outer(np.array([0, 1, 1, 0]) / np.sqrt(2), np.array([0, 1, 1, 0]) / np.sqrt(2))
print(f"(e) || Z P_singlet Z - P_triplet0 || = {np.linalg.norm(Z2 @ Ps @ Z2 - Pt0):.1e}  (so a singlet-weight formation rule is not Lambda-invariant on flipped bonds)")
