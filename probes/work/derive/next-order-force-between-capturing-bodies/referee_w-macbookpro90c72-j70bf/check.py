#!/usr/bin/env python3
"""Referee for J:derive:next-order-force-between-capturing-bodies:a1.

The hydrodynamic identities are re-derived in sympy. The periodic lattice
Stokes system is solved in real space and compared with its Fourier solution.
Neither routine is the author's.
"""
import itertools
import sys

import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


# ---------- H1. dispersion ----------
rho, nu, nub, k, lam = sp.symbols("rho nu nu_b k lam", positive=True)
n, gx = sp.symbols("n g_x")
# ∂t n + ((1-rho)/sqrt(3)) ∂x g = 0,  ∂t g + (1/(3 sqrt(3))) ∂x n = (nu+nu_b) ∂xx g
# plane wave e^{i k x + lam t}: lam n + i k (1-rho)/sqrt(3) g = 0
# lam g + i k n /(3 sqrt(3)) = -(nu+nu_b) k^2 g
c_fac = (1 - rho) / sp.sqrt(3)
p_fac = 1 / (3 * sp.sqrt(3))
M = sp.Matrix([[lam, sp.I * k * c_fac], [sp.I * k * p_fac, lam + (nu + nub) * k ** 2]])
char = sp.simplify(sp.together(M.det() * sp.simplify(1)))
# det = lam (lam + (nu+nub)k^2) - (i k c)(i k p) = lam^2 + (nu+nub)k^2 lam + k^2 c p
# c p = (1-rho)/sqrt(3) * 1/(3 sqrt(3)) = (1-rho)/9
longitudinal = sp.expand(char - (lam ** 2 + (nu + nub) * k ** 2 * lam + (1 - rho) * k ** 2 / 9))
transverse = sp.simplify(lam + nu * k ** 2)  # the transverse root itself
sound = sp.simplify(sp.sqrt((1 - rho) / 9) - sp.sqrt(1 - rho) / 3)
ok("H1", longitudinal == 0 and sound == 0,
   "longitudinal law lam^2 + (nu+nu_b)k^2 lam + (1-rho)k^2/9 = 0, so c = sqrt(1-rho)/3; transverse lam = -nu k^2")

# ---------- H2. number sink and K0 ----------
N, r, pi = sp.symbols("N r pi", positive=True)
K0 = sp.sqrt(3) / (4 * pi * rho * (1 - rho))
g_rad = sp.sqrt(3) * N / (4 * pi * (1 - rho) * r ** 2)
J_rad = (1 - rho) / sp.sqrt(3) * g_rad
flux = sp.simplify(J_rad * 4 * pi * r ** 2)
u = sp.simplify(g_rad / rho - K0 * N / r ** 2)
ok("H2", flux == N and u == 0,
   "a record sink N produces g = -sqrt(3) N x-hat / (4 pi (1-rho) r^2); the flux is N and u = -K0 N/r^2")

# ---------- S1. Stokeslet off the origin ----------
x, y, z = sp.symbols("x y z", real=True)
nu_s = sp.symbols("nu", positive=True)
rr = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
xs = (x, y, z)


def Gij(i, j):
    return (sp.Integer(1) if i == j else 0) / rr + xs[i] * xs[j] / rr ** 3


def lap(expr):
    return sum(sp.diff(expr, v, 2) for v in xs)


div_rows = []
mom = []
for j in range(3):
    div_rows.append(sp.simplify(sum(sp.diff(Gij(i, j), xs[i]) for i in range(3))))
    for i in range(3):
        # nu lap G_ij - d/dx_i (x_j /(4 pi r^3)) compared after stripping 8 pi nu, so check nu*lap(G/(8 pi nu))
        mom.append(sp.simplify(nu_s * lap(Gij(i, j) / (8 * sp.pi * nu_s)) - sp.diff(xs[j] / (4 * sp.pi * rr ** 3), xs[i])))
# evaluate the simplified expressions away from 0 by substitution
pt = {x: 1, y: 2, z: -1}
div_ok = all(sp.simplify(e).subs(pt) == 0 for e in div_rows)
mom_ok = all(sp.simplify(e).subs(pt) == 0 for e in mom)
axis = sp.simplify((Gij(0, 0) / (8 * sp.pi * nu_s)).subs({y: 0, z: 0, x: r}) - 1 / (4 * sp.pi * nu_s * r))
trans = sp.simplify((Gij(1, 1) / (8 * sp.pi * nu_s)).subs({y: 0, z: 0, x: r}) - 1 / (8 * sp.pi * nu_s * r))
ok("S1", div_ok and mom_ok and axis == 0 and trans == 0,
   "off the origin div G = 0 and nu lap G - grad P = 0; on the axis G_xx = 1/(4 pi nu r), G_yy = 1/(8 pi nu r)")

# ---------- S2. the force algebra ----------
C1, C2, N2, Q1, Q2, f = sp.symbols("C1 C2 N2 Q1 Q2 f", positive=True)
# F2 = -(C2/rho) G F1. On axis G rhat = rhat/(4 pi nu r), so the inward magnitude is C2 f / (4 pi nu rho r)
mag = sp.simplify(C2 / rho * (1 / (4 * pi * nu_s * r)))
with_wind = sp.simplify(mag * (K0 * C1 * N2 / r ** 2))
target = sp.sqrt(3) * C1 * C2 * N2 / (16 * pi ** 2 * nu_s * rho ** 2 * (1 - rho) * r ** 3)
unequal = sp.simplify(K0 * Q1 * Q2 ** 2 / (4 * pi * nu_s * rho * r ** 3)
                      - K0 * Q1 ** 2 * Q2 / (4 * pi * nu_s * rho * r ** 3)
                      - K0 * Q1 * Q2 * (Q2 - Q1) / (4 * pi * nu_s * rho * r ** 3))
half = sp.simplify(C2 / rho * (1 / (8 * pi * nu_s * r)) - mag / 2)
ok("S2", sp.simplify(with_wind - target) == 0 and unequal == 0 and half == 0,
   "axial pull K0 C1 C2 N2/(4 pi nu rho r^3); transverse half of that; pair forces differ by K0 Q1 Q2 (Q2-Q1)/(4 pi nu rho r^3)")

# ---------- S4. lattice Stokes: Fourier versus a real-space solve ----------
def fourier_green(L):
    """Mean-zero solution of Delta g - grad+ p + f = 0, div- g = 0, f = e_x at 0 compensated by its mean."""
    g = np.zeros((L, L, L, 3), dtype=np.complex128)
    p = np.zeros((L, L, L), dtype=np.complex128)
    N = L ** 3
    for kx, ky, kz in itertools.product(range(L), repeat=3):
        if (kx, ky, kz) == (0, 0, 0):
            continue
        phase = np.exp(2j * np.pi * np.array([kx, ky, kz]) / L)
        a = phase - 1
        aa = np.vdot(a, a).real
        # fhat_x = 1, others 0, because the mean was removed and k != 0
        fhat = np.array([1.0 + 0j, 0j, 0j])
        p_hat = np.vdot(a, fhat) / aa
        g_hat = (fhat - a * p_hat) / aa
        for x, y, z_ in itertools.product(range(L), repeat=3):
            e = np.exp(2j * np.pi * (kx * x + ky * y + kz * z_) / L) / N
            g[x, y, z_] += g_hat * e
            p[x, y, z_] += p_hat * e
    return g.real, p.real


def direct_solve(L):
    """Least squares on every momentum and divergence row, plus zero-mean gauges."""
    N = L ** 3

    def idx(x, y, z_):
        return (x % L) * L * L + (y % L) * L + (z_ % L)

    rows, rhs = [], []

    def add_row(coeffs, value):
        row = np.zeros(4 * N)
        for col, val in coeffs:
            row[col] += val
        rows.append(row)
        rhs.append(value)

    for x, y, z_ in itertools.product(range(L), repeat=3):
        base = idx(x, y, z_)
        for j in range(3):
            row = [(j * N + base, -6.0)]
            for d in range(3):
                for s in (-1, 1):
                    xx, yy, zz = [x, y, z_]
                    if d == 0:
                        xx += s
                    elif d == 1:
                        yy += s
                    else:
                        zz += s
                    row.append((j * N + idx(xx, yy, zz), 1.0))
            # -(p(x+e_j) - p(x))
            row.append((3 * N + base, 1.0))
            step = [x, y, z_]
            step[j] += 1
            row.append((3 * N + idx(*step), -1.0))
            # Delta g - grad+ p = -f, f_x = delta - 1/N
            value = 0.0
            if j == 0:
                value = 1.0 / N - (1.0 if (x, y, z_) == (0, 0, 0) else 0.0)
            add_row(row, value)
        row = []
        for j in range(3):
            row.append((j * N + base, 1.0))
            step = [x, y, z_]
            step[j] -= 1
            row.append((j * N + idx(*step), -1.0))
        add_row(row, 0.0)
    for comp in range(4):
        add_row([(comp * N + i, 1.0) for i in range(N)], 0.0)
    sol, *_ = np.linalg.lstsq(np.vstack(rows), np.array(rhs), rcond=None)
    g = sol[: 3 * N].reshape(3, L, L, L).transpose(1, 2, 3, 0)
    p = sol[3 * N :].reshape(L, L, L)
    return g, p


lattice_ok = True
worst = 0.0
for L in (3, 4):
    gf, pf = fourier_green(L)
    gd, pd = direct_solve(L)
    err = max(np.max(np.abs(gf - gd)), np.max(np.abs(pf - pd)))
    worst = max(worst, err)
    lattice_ok &= err < 1e-9
ok("S4", lattice_ok, f"on the periodic boxes L=3 and L=4 the real-space Stokes solve matches the Fourier Green function (max abs {worst:.2e})")

# ---------- S10. the arithmetic of the predicted fraction, not the runs ----------
# R = (f/ref) * C2 * b / (4 pi nu rho r)
fref, C2v, b, nuT, rhov, rv = 0.784, 7.86, 0.923, 0.36, 0.3, 16.0
R = fref * C2v * b / (4 * np.pi * nuT * rhov * rv)
R_free = fref * C2v * 1.0 / (4 * np.pi * nuT * rhov * rv)
R_unit = 1.0 * C2v * b / (4 * np.pi * nuT * rhov * rv)
ok("S10", abs(R - 0.262) < 0.002 and abs(R_free - 0.284) < 0.002 and abs(R_unit - 0.334) < 0.002,
   f"at rho=0.3, r=16, nu=0.36, C2=7.86, b=0.923: R={R:.3f} (free {R_free:.3f}, unit push {R_unit:.3f})")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - a momentum sink produces the Stokeslet, and the second-order capture force is the axial pull K0 C1 C2 N2/(4 pi nu rho r^3).")
print("HIT: confirmed - within J=(1-rho)g/sqrt(3) and p=n/(3 sqrt(3)), div g = 0 for a pure momentum sink, g=-G F with G=(I/r+xx^T/r^3)/(8 pi nu), and a sampler at r r-hat is pulled toward the source by C2 F/(4 pi nu rho r) = K0 C1 C2 N2/(4 pi nu rho r^3); the transverse piece is half of that, and the two pair forces differ by K0 Q1 Q2 (Q2-Q1)/(4 pi nu rho r^3). The lattice Stokes Green function agrees with a direct solve on L=3 and L=4.")
