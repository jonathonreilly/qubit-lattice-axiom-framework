#!/usr/bin/env python3
"""Uniform ice: the static photon stiffens in a background flux, and saturation leaves square ice.

Open PRs 8871 and 8881 found that one Gaussian stiffness sets the flux cost
and the correlations of uniform ice at small flux. A Gaussian field is
linear: its cost is quadratic in the flux, and its excitations do not feel a
background flux. This runner measures how uniform ice departs from that, up
to full polarization, with the layer transfer T of the landed layer-unit note
(PR 8740) applied by the row transfer of the landed note of PR 8859.

Checks:

A. Saturation. At full polarization |S| = A every vertex has exactly one of
   its two vertical links occupied, so each layer must carry two of four
   horizontal links at every vertex: square ice. On 2 x 2, 2 x 4, 2 x 6, 2 x 8
   and 4 x 4 the top level of the |S| = A sector equals the number of
   square-ice configurations of that torus (2970 on 4 x 4).
B. The equation of state on 4 x 4. The flux cost c(S) = (A/S^2) ln(lam_0 / lam_S)
   rises monotonically from 0.3270 at |S| = 2 to 0.4373 at |S| = 16.
C. The photon in a background flux on 4 x 4. The branch rate
   D_s = ln(lam_s / |lam_top(k)|) at physical wavenumber (pi/2, 0) rises
   with |S| = s from 1.2963 at s = 0 to 1.6846 at s = 10. At small flux the
   shift is quadratic: D_4 - D_0 is 4 times D_2 - D_0 within 5%.
D. A local quartic cost c(rho) = c_2 + d rho^2, fitted at |S| = 2 and 4,
   stiffens the field along the background (c_2 + 6 d rho^2) more than
   across it (c_2 + 2 d rho^2), so it predicts D_s / D_0 - 1 = 2 d rho^2 / c_2.
   At (pi/2, 0) that accounts for between 55% and 80% of the measured shift
   at s = 2 and 4.
E. The shift does not scale with the wavenumber. At physical (0, pi), where
   D_0 is a third larger, the shifts at s = 2 and 4 equal those at (pi/2, 0)
   within 2%. A background flux raises the rate by a near-constant amount,
   which the smooth quartic rescaling does not describe; its fraction
   depends on the wavenumber.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

PASS = FAIL = 0
T0 = time.time()


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


def row_tensor(a):
    n = 1 << a
    R = np.zeros((n, n, n, n))
    bits = lambda z: [(z >> i) & 1 for i in range(a)]
    for h in range(n):
        hb = bits(h)
        hdeg = [hb[(x - 1) % a] + hb[x] for x in range(a)]
        for w in range(n):
            wb = bits(w)
            for i in range(n):
                ib = bits(i)
                for o in range(n):
                    ob = bits(o)
                    need = [3 - hdeg[x] - ib[x] - ob[x] - wb[x] for x in range(a)]
                    if all(t in (0, 1) for t in need):
                        R[sum(t << x for x, t in enumerate(need)), o, w, i] += 1
    return R


class Prism:
    def __init__(self, a, b):
        self.a, self.b, self.n, self.A, self.N = a, b, 1 << a, a * b, 1 << (a * b)
        self.R = row_tensor(a)
        idx = np.arange(self.N)
        S = np.zeros(self.N, dtype=np.int64)
        for y in range(b):
            for x in range(a):
                S += (-1) ** (x + y) * (2 * ((idx >> ((b - 1 - y) * a + x)) & 1) - 1)
        self.S = S
        self.rot = np.array([((v << 1) | (v >> (a - 1))) & (self.n - 1) for v in range(self.n)])

    def T(self, phi):
        n, b = self.n, self.b
        A = phi.reshape((n,) * b)
        A = np.einsum("...,ij->...ij", A, np.eye(n))
        for r in range(b):
            A = np.tensordot(A, self.R, axes=([r, b], [2, 3]))
            A = np.moveaxis(A, [b, b + 1], [r, b])
        return np.einsum("...ii->...", A).reshape(-1)

    def ty(self, u):
        return np.transpose(u.reshape((self.n,) * self.b), axes=list(range(1, self.b)) + [0]).reshape(-1)

    def tx(self, u):
        A = u.reshape((self.n,) * self.b)
        for ax in range(self.b):
            A = np.take(A, self.rot, axis=ax)
        return A.reshape(-1)

    def proj(self, u, kx, ky):
        out = np.zeros(self.N, dtype=complex)
        cy = u.astype(complex)
        for jy in range(self.b):
            cx = cy
            for jx in range(self.a):
                out += np.exp(-1j * (kx * jx + ky * jy)) * cx
                cx = self.tx(cx)
            cy = self.ty(cy)
        return out / (self.a * self.b)

    def top(self, s, k=None):
        # T maps the flux S of one layer to -S, so a flux sector is |S| = s
        m = (np.abs(self.S) == s).astype(float)
        sel = np.where(m > 0)[0]
        if k is None and len(sel) <= 400:
            cols = []
            for i in sel:
                e = np.zeros(self.N)
                e[i] = 1.0
                cols.append(self.T(e)[sel])
            M = np.column_stack(cols)
            return float(np.max(np.abs(np.linalg.eigvals(M))))
        if k is None:
            op = LinearOperator((self.N, self.N), matvec=lambda u: m * self.T(m * u), dtype=float)
            return float(abs(eigsh(op, k=1, which="LM", tol=1e-11, maxiter=50000)[0][0]))

        def f(u):
            v = self.proj(u * m, *k) * m
            w = self.T(v.real) + 1j * self.T(v.imag)
            return self.proj(w * m, *k) * m
        op = LinearOperator((self.N, self.N), matvec=f, dtype=complex)
        return float(abs(eigsh(op, k=1, which="LM", tol=1e-10, maxiter=50000)[0][0]))


def square_ice(a, b):
    # 2D torus a x b: two of four links occupied at every vertex, by row transfer
    n = 1 << a
    Tm = np.zeros((n, n))
    for vin in range(n):
        for vout in range(n):
            for h in range(n):
                if all(((h >> ((x - 1) % a)) & 1) + ((h >> x) & 1) + ((vin >> x) & 1) + ((vout >> x) & 1) == 2 for x in range(a)):
                    Tm[vout, vin] += 1
    return int(round(np.trace(np.linalg.matrix_power(Tm, b))))


print("== A. Saturation leaves square ice ==")
sat = {}
for (a, b) in ((2, 2), (2, 4), (2, 6), (2, 8), (4, 4)):
    P = Prism(a, b)
    sat[(a, b)] = (P.top(a * b), square_ice(a, b))
    del P
check("at |S| = A the top level equals the square-ice count of the torus on 2x2, 2x4, 2x6, 2x8 and 4x4",
      all(abs(t - z) < 1e-6 * z for t, z in sat.values()),
      ", ".join(f"{a}x{b}: {t:.1f} vs {z}" for (a, b), (t, z) in sat.items()))
print()

P = Prism(4, 4)
A = 16
lam = {s: P.top(s) for s in range(0, 17, 2)}
c = {s: (A / s ** 2) * np.log(lam[0] / lam[s]) for s in range(2, 17, 2)}
print("== B. The equation of state on 4 x 4 ==")
seq = [c[s] for s in range(2, 17, 2)]
check("c(S) rises monotonically from 0.3270 at |S| = 2 to 0.4373 at |S| = 16",
      all(x < y for x, y in zip(seq, seq[1:])) and abs(c[2] - 0.3270) < 5e-5 and abs(c[16] - 0.4373) < 5e-5,
      ", ".join(f"{s}: {c[s]:.4f}" for s in range(2, 17, 2)))
print()

kq = (2 * np.pi * 3 / 4, 2 * np.pi * 2 / 4)       # physical (pi/2, 0) at occupation wavenumber + (pi, pi)
D = {s: np.log(lam[s] / P.top(s, kq)) for s in (0, 2, 4, 6, 8, 10)}
print("== C. The photon in a background flux ==")
d2, d4 = D[2] - D[0], D[4] - D[0]
check("D_s at (pi/2, 0) rises with s from 1.2963 to 1.6846, and the small-flux shift is quadratic: D_4 - D_0 = 4 (D_2 - D_0) within 5%",
      all(D[x] < D[y] for x, y in zip((0, 2, 4, 6, 8), (2, 4, 6, 8, 10))) and abs(D[0] - 1.29627) < 1e-4 and abs(D[10] - 1.68456) < 1e-4
      and abs(d4 / d2 / 4 - 1) < 0.05,
      ", ".join(f"{s}: {D[s]:.5f}" for s in D) + f"; shift ratio {d4 / d2:.3f}")
print()

print("== D. A local quartic cost ==")
r2, r4 = (2 / A) ** 2, (4 / A) ** 2
dq = (c[4] - c[2]) / (r4 - r2)
c2 = c[2] - dq * r2
frac = [(2 * dq * r / c2) * D[0] / (D[s] - D[0]) for s, r in ((2, r2), (4, r4))]
check("the quartic fit stiffens along the background more than across, and accounts for 55% to 80% of the shift at s = 2 and 4",
      dq > 0 and all(0.55 < f < 0.80 for f in frac),
      f"c_2 = {c2:.4f}, d = {dq:.4f}; fraction explained {frac[0]:.3f}, {frac[1]:.3f}")
print()
print("== E. The shift does not scale with the wavenumber ==")
kpi = (2 * np.pi * 2 / 4, 0.0)                     # physical (0, pi) at occupation (pi, 0)
Dpi = {s: np.log(lam[s] / P.top(s, kpi)) for s in (0, 2, 4)}
same = [abs((Dpi[s] - Dpi[0]) / (D[s] - D[0]) - 1) for s in (2, 4)]
frac_pi = [(2 * dq * r / c2) * Dpi[0] / (Dpi[s] - Dpi[0]) for s, r in ((2, r2), (4, r4))]
check("at (0, pi) the shifts at s = 2 and 4 equal those at (pi/2, 0) within 2%, although D_0 differs by a third: a near-constant rise, not a rescaling",
      max(same) < 0.02 and Dpi[0] / D[0] > 1.3,
      f"D_0 {D[0]:.5f} vs {Dpi[0]:.5f}; shifts {D[2] - D[0]:.5f}, {D[4] - D[0]:.5f} vs {Dpi[2] - Dpi[0]:.5f}, {Dpi[4] - Dpi[0]:.5f}; "
      f"quartic fraction at (0, pi) {frac_pi[0]:.3f}, {frac_pi[1]:.3f}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
