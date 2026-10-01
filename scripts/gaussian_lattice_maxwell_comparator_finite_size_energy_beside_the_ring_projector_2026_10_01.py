#!/usr/bin/env python3
"""Gaussian lattice-Maxwell comparator: finite-size zero-point energy per plaquette, beside the ring-model projector energies.

Supplied comparison model (landed note GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_
AND_MISSES_THE_PURE_RING_LEVEL_STEP, 2026-09-24): H = (U/2) E^2 + (K/2) A^T C^T C A on the 3N links of the L^3 torus with the Gauss law
D E = 0 and the holonomy zero modes removed. Its nonzero transverse oscillators are two per k != 0 with omega = sqrt(UK) |s(k)|,
|s|^2 = sum_a 4 sin^2(k_a/2). The landed reading U = 1/chi, K = 4 u0 gives v = sqrt(UK) = 1.025. The zero-point energy per plaquette is
e(L) = (v/3) Z(L), Z(L) = N^-1 sum_{k != 0} |s(k)|, so the comparator's u = -E/(3N) shifts by (v/3)(Z_inf - Z(L)).
Checks: (1) explicit spectrum on L = 4, 6, 8: Gauss law, kernel N + 2, 2(N - 1) oscillators, zero-point energy = v N Z(L); (2) Z_inf
by the heat-kernel integral (30 digits) with two independent cross-checks; (3) the shift table for L = 4..24 and its continuum Casimir
limit sum_{k != 0}|k| = -Z_E/(pi^2 L), Z_E = sum_{n != 0} |n|^-4; (4) beside the landed ring-model projector energies per plaquette on
8^3, 12^3, 16^3, 24^3 (reported). Floating-point and 30-digit numerics; not interval-certified. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import time

import mpmath as mp
import numpy as np

AUDIT_TIMEOUT_SEC = 300

RESULTS = []
T0 = time.time()
V = 1.025                                   # landed reading: U = 1/chi = 0.913, K = 4 u0 = 1.152


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def geometry(L):
    N = L ** 3
    xs = np.array(list(np.ndindex(L, L, L)))

    def site(x):
        x = np.mod(x, L)
        return x[..., 0] * L * L + x[..., 1] * L + x[..., 2]

    def link(x, a):
        return 3 * site(x) + a

    D = np.zeros((N, 3 * N))
    for a in range(3):
        ea = np.eye(3, dtype=int)[a]
        D[np.arange(N), link(xs, a)] += 1
        D[np.arange(N), link(xs - ea, a)] -= 1
    C = np.zeros((3 * N, 3 * N))
    for p, (a, b) in enumerate([(0, 1), (0, 2), (1, 2)]):
        ea, eb = np.eye(3, dtype=int)[a], np.eye(3, dtype=int)[b]
        rows = 3 * np.arange(N) + p
        C[rows, link(xs, a)] += 1
        C[rows, link(xs + ea, b)] += 1
        C[rows, link(xs + eb, a)] -= 1
        C[rows, link(xs, b)] -= 1
    return N, D, C


def Z_direct(L):
    q = 4.0 * np.sin(np.pi * np.arange(L) / L) ** 2
    s = np.sqrt(q[:, None, None] + q[None, :, None] + q[None, None, :]).ravel()
    s = np.sort(s[s > 0])
    return float(mp.fsum(s.tolist()) / L ** 3) if L <= 64 else float(s.sum() / L ** 3)


# ---------------------------------------------------------------- 1. explicit spectrum
rows, ok1 = [], True
Ut, Kt = 1.7, 1.2
for L in (4, 6, 8):
    N, D, C = geometry(L)
    dc = float(np.abs(D @ C.T).max())
    w = np.linalg.eigvalsh(C.T @ C)
    nz = w > 1e-9
    Eexp = 0.5 * np.sqrt(Ut * Kt * w[nz]).sum()
    Efor = np.sqrt(Ut * Kt) * N * Z_direct(L)
    ok1 &= dc == 0 and int((~nz).sum()) == N + 2 and int(nz.sum()) == 2 * (N - 1) and abs(Eexp - Efor) < 1e-9 * Efor
    rows.append(f"L = {L}: kernel {int((~nz).sum())} (N + 2 = {N + 2}), oscillators {int(nz.sum())}, |E_explicit - sqrt(UK) N Z(L)| {abs(Eexp - Efor):.1e}")
check("explicit comparator spectrum on L = 4, 6, 8 (test couplings U = 1.7, K = 1.2): the curl preserves the Gauss law, C^T C has kernel "
      "N + 2 and 2(N - 1) nonzero eigenvalues, and the oscillator zero-point energy equals sqrt(UK) N Z(L)", ok1, "; ".join(rows))

# ---------------------------------------------------------------- 2. Z_inf
mp.mp.dps = 30
th = lambda t: mp.exp(-2 * t) * mp.besseli(0, 2 * t)
Tc = mp.mpf(400)
head = mp.quad(lambda t: t ** mp.mpf(-1.5) * (1 - th(t) ** 3), [0, mp.mpf("0.05"), 1, 5, 25, 100, Tc])
tail = 2 / mp.sqrt(Tc) - mp.quad(lambda t: t ** mp.mpf(-1.5) * th(t) ** 3, [Tc, 4 * Tc, 40 * Tc, mp.inf])
Zinf = (head + tail) / (2 * mp.sqrt(mp.pi))
q = 4.0 * np.sin(np.pi * (np.arange(96) + 0.5) / 96) ** 2
mid96 = float(np.sqrt(q[:, None, None] + q[None, :, None] + q[None, None, :]).mean())
mp.mp.dps = 20


def theta_L(t, L):
    s = mp.besseli(0, 2 * t); n = 1
    while True:
        term = mp.besseli(n * L, 2 * t); s += 2 * term
        if term < s * mp.mpf(10) ** (-22) and n * L > 2 * t:
            break
        n += 1
    return mp.exp(-2 * t) * s


img = {}
for L in (4, 8):
    N = L ** 3; TL = mp.mpf(80)
    hd = mp.quad(lambda t: t ** mp.mpf(-1.5) * (1 - theta_L(t, L) ** 3), [0, mp.mpf("0.05"), 1, 5, 25, TL])
    img[L] = float((hd + 2 / mp.sqrt(TL) * (1 - mp.mpf(1) / N)) / (2 * mp.sqrt(mp.pi)))
ZL = {L: Z_direct(L) for L in (4, 6, 8, 12, 16, 20, 24, 32, 64, 128)}
ok2 = abs(mid96 - float(Zinf)) < 1e-8 and all(abs(img[L] - ZL[L]) < 1e-9 for L in img)
check("Z_inf = BZ average of |s(k)| by the heat-kernel integral; independent checks: shifted midpoint sum on 96^3, and the image heat "
      "kernel of Z(4), Z(8) against the direct sums", ok2,
      f"Z_inf {mp.nstr(Zinf, 16)}; midpoint 96^3 {mid96:.10f}; image Z(4) {img[4]:.12f} vs {ZL[4]:.12f}, Z(8) {img[8]:.12f} vs {ZL[8]:.12f}")

# ---------------------------------------------------------------- 3. shift table and continuum Casimir limit
mp.mp.dps = 30


def theta1(t):
    t = mp.mpf(t)
    return 1 + 2 * mp.nsum(lambda n: mp.exp(-mp.pi * n * n * t), [1, mp.inf]) if t >= 1 else theta1(1 / t) / mp.sqrt(t)


ZE = mp.pi ** 2 * mp.quad(lambda t: t * (theta1(t) ** 3 - 1), [0, mp.mpf("0.25"), 1, 4, 20])
cc = float(ZE / mp.pi ** 2)
zf = float(Zinf)
shift = {L: V / 3 * (zf - ZL[L]) for L in ZL}
ok3 = all(shift[L] > 0 for L in ZL) and all(shift[a] > shift[b] for a, b in zip(sorted(ZL)[:-1], sorted(ZL)[1:])) \
    and abs(128 ** 4 * (ZL[128] - zf) + cc) < 1e-3
check("the comparator's u(L) - u_inf = (v/3)(Z_inf - Z(L)) is positive and decreasing for L = 4 to 128, and L^4 (Z(L) - Z_inf) tends to "
      "-Z_E/pi^2 with Z_E = sum_(n != 0) |n|^-4 (continuum Casimir constant)", ok3,
      "; ".join(f"L = {L}: {shift[L]:.3e}" for L in (4, 6, 8, 12, 16, 20, 24)) + f"; Z_E/pi^2 {cc:.8f}, L^4 (Z - Z_inf) at L = 128 {128 ** 4 * (ZL[128] - zf):.6f}")

# ---------------------------------------------------------------- 4. beside the landed ring-model projector energies
PROJ = {8: 0.28844, 12: 0.28807, 16: 0.28676, 24: 0.28509}  # landed: 8^3 (two schemes 0.28837, 0.28851), 12^3 (3840 walkers), 16^3, 24^3
d_comp = {L: shift[L] - shift[8] for L in (12, 16, 24)}
d_proj = {L: PROJ[L] - PROJ[8] for L in (12, 16, 24)}
ok4 = all(abs(d_proj[L]) > 5 * abs(d_comp[L]) for L in (16, 24))
check("beside the landed ring-model projector energies per plaquette (8^3 0.2884, 12^3 0.2881, 16^3 0.2868, 24^3 0.2851): from 8^3 the "
      "comparator's finite-size shift is at least five times smaller than the projector's decrease on 16^3 and 24^3 (reported)", ok4,
      "; ".join(f"L = {L}: comparator {d_comp[L]:+.2e}, projector {d_proj[L]:+.2e}, ratio {d_proj[L] / d_comp[L]:.0f}" for L in (12, 16, 24))
      + f"; whole comparator shift at 8^3 {shift[8]:.2e}; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
