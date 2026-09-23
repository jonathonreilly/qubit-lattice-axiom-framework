#!/usr/bin/env python3
"""J:derive:inertial-gas-viscosity-and-damping:a2 - checks for ATTEMPT.md (same directory).

Block 44's clause (open PR #8550): (S) each record at rate 1 swaps the states of its site and the site its content points
to (enter if empty, exchange contents if occupied); (C) each bond at rate gamma re-draws two records uniformly on their
momentum class. Tags: EXACT (Fractions / sympy), CLOSURE (the one-point product closure, exact algebra inside it),
FLOAT (floating point; simulations are evidence, not proof).
"""
import sys
import time
from fractions import Fraction as Fr
from itertools import product

import numpy as np
import sympy as sp
from scipy.linalg import expm

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


D6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]  # index d, opposite d ^ 1


# ------------------------------------------------------------------ A: the collision operator of (C), six axes (EXACT)
def pair_T():
    T = [[Fr(0)] * 36 for _ in range(36)]
    for a, b in product(range(6), repeat=2):
        i = 6 * a + b
        if b == a ^ 1:
            for e in range(6):
                T[i][6 * e + (e ^ 1)] += Fr(1, 6)
        elif a != b:
            T[i][i] += Fr(1, 2)
            T[i][6 * b + a] += Fr(1, 2)
        else:
            T[i][i] = Fr(1)
    return T


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)) if A[i][k]) for j in range(len(B[0]))] for i in range(len(A))]


def rank(M):
    M = [r[:] for r in M]
    rk, cols = 0, len(M[0])
    for c in range(cols):
        p = next((r for r in range(rk, len(M)) if M[r][c] != 0), None)
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][c] != 0:
                f = M[r][c] / M[rk][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[rk])]
        rk += 1
    return rk


T = pair_T()
mom = {}
for a, b in product(range(6), repeat=2):
    P = tuple(x + y for x, y in zip(D6[a], D6[b]))
    mom.setdefault(P, []).append(6 * a + b)
proj = matmul(T, T) == T
symm = all(T[i][j] == T[j][i] for i in range(36) for j in range(36))
stoch = all(sum(r) == 1 for r in T)
rT = rank(T)
cons = all(sum(T[i][j] for j in cl) == (1 if i in cl else 0) for cl in mom.values() for i in range(36))
csizes = sorted(len(c) for c in mom.values())
ok("A1", proj and symm and stoch and rT == 19 and len(mom) == 19 and cons,
   f"36x36 pair re-draw matrix T: symmetric, stochastic, T^2 = T; rank 19 = number of momentum classes {len(mom)} (sizes "
   f"{csizes.count(1)}x1, {csizes.count(2)}x2, {csizes.count(6)}x6); generator gamma(T - I) has eigenvalues 0 (x19: the "
   "class indicators, among them number and pair momentum) and -gamma (x17); an isolated pair evolved for time t is "
   "I + (1 - e^{-gamma t})(T - I) exactly")

U = [[Fr(0)] * 6 for _ in range(6)]
V = [[Fr(0)] * 6 for _ in range(6)]
for a, b, c, d in product(range(6), repeat=4):
    U[c][a] += T[6 * a + b][6 * c + d]  # site's pre-content a -> site's post-content c, partner summed
    V[c][b] += T[6 * a + b][6 * c + d]  # partner's pre-content b -> site's post-content c
rho, gam, k = sp.symbols("rho gamma k", positive=True)
Us, Vs = sp.Matrix(6, 6, lambda i, j: sp.Rational(U[i][j].numerator, U[i][j].denominator)), \
    sp.Matrix(6, 6, lambda i, j: sp.Rational(V[i][j].numerator, V[i][j].denominator))
J6, I6 = sp.ones(6, 6), sp.eye(6)
C0 = gam * rho * (Us + Vs - 6 * I6 - J6)  # one-site linearized collision operator at k = 0 (partner deviation equal)
ev = C0.eigenvals()
Yq = sp.Matrix([2, 2, -1, -1, -1, -1])
modes_ok = (C0 * sp.ones(6, 1) == sp.zeros(6, 1) and all(C0 * sp.Matrix([D6[d][j] for d in range(6)]) == sp.zeros(6, 1)
                                                          for j in range(3))
            and sp.simplify(C0 * Yq + 2 * gam * rho * Yq) == sp.zeros(6, 1))
a1 = (Us * sp.Matrix([D6[d][0] for d in range(6)]))[0] / 6
a2 = (Us * Yq)[0] / Yq[0] / 6
ok("A2", ev == {0: 4, -2 * gam * rho: 2} and modes_ok and Us == Vs and a1 == sp.Rational(1, 2) and a2 == sp.Rational(1, 3),
   "one-site 6x6 linearized collision operator gamma rho (U + V - 6I - J): eigenvalues 0 (x4: density, three momenta) and "
   "-2 gamma rho (x2: the axis quadrupole, the diagonal momentum flux); retention of a site's own content by one "
   "collision with a uniform partner: 1/2 (momentum), 1/3 (quadrupole); the partner's is the same")


# ------------------------------------------------------------------ B: the closure, six axes, k along an axis (CLOSURE)
def taylor_exp(z, n=5):
    return sum(z ** m / sp.factorial(m) for m in range(n + 1))


def M6(kk, g_, series=True):
    """one-point closure linearized at the uniform product state, Fourier mode k along x."""
    ex = (lambda s: taylor_exp(-sp.I * kk * s)) if series else (lambda s: sp.exp(-sp.I * kk * s))
    cosk = (1 - kk ** 2 / 2 + kk ** 4 / 24) if series else sp.cos(kk)
    ph = [ex(D6[d][0]) for d in range(6)]
    S = sp.zeros(6, 6)
    for c in range(6):
        for c2 in range(6):
            S[c, c2] = (rho / 6) * (1 - ph[c2])
        S[c, c] += (ph[c] - 1) + (rho / 6) * (2 * cosk - 2)
    two_sig = 2 * cosk + 4
    C = g_ * (rho / 6) * (6 * Us + two_sig * Vs - 36 * I6 - two_sig * J6)
    return S, C


S, C = M6(k, gam)
M = S + C
vecs = [sp.Matrix([1, 0, 0, 0, 0, 0]), sp.Matrix([0, 1, 0, 0, 0, 0]), sp.Matrix([0, 0, 1, 1, 1, 1])]
R = sp.zeros(3, 3)
for j, v in enumerate(vecs):
    w = M * v
    R[0, j], R[1, j], R[2, j] = w[0], w[1], w[2]
    assert all(sp.expand(w[i] - w[2]) == 0 for i in (3, 4, 5))
cs = sp.sqrt((1 - rho) / 3)
L2, L3 = sp.symbols("L2 L3")
lam_s = sp.I * cs * k + L2 * k ** 2 + L3 * k ** 3
det = sp.expand((R - lam_s * sp.eye(3)).det())
ser = det  # a polynomial in k: the entries are Taylor polynomials exact through k^5
c3 = sp.simplify(ser.coeff(k, 3))
L2sol = sp.solve(c3, L2)
Gam6 = sp.Rational(2, 3) + rho / 6 + gam * rho / 2 + 1 / (3 * gam * rho)
b1 = sp.simplify(ser.coeff(k, 2)) == 0 and len(L2sol) == 1 and sp.simplify(L2sol[0] + Gam6 / 2) == 0
Sx, Cx = M6(k, gam, series=False)
ty = sp.Matrix([0, 0, 1, -1, 0, 0])
shear = sp.simplify((Sx + Cx) * ty + (1 - sp.cos(k)) * rho * (sp.Rational(1, 3) + gam) * ty) == sp.zeros(6, 1)
ok("B1", b1 and shear,
   "closure, six axes, k along an axis: sound roots +-i sqrt((1-rho)/3) k - (Gamma/2) k^2 with Gamma = 2/3 + rho/6 + "
   "gamma rho/2 + 1/(3 gamma rho) (exact series of the longitudinal 3x3 block); shear eigenvalue exactly "
   "-(1 - cos k) rho (1/3 + gamma): nu_T = rho/6 + gamma rho/2, no collision-limited part")

# ------------------------------------------------------------------ C: sphere menu moments and retention (EXACT)
cth, th, u = sp.symbols("c theta u", real=True)
avg = lambda f: sp.integrate(f, (u, -1, 1)) / 2  # uniform sphere: s_x = u uniform on [-1, 1]
m2, m4, mabs, mabs3 = avg(u ** 2), avg(u ** 4), avg(sp.Abs(u)), avg(sp.Abs(u) ** 3)
# <|s_x| s_y^2> = (1/2)<|s_x|(1 - s_x^2)> by the y <-> z symmetry
mabsy2 = avg(sp.Abs(u) * (1 - u ** 2)) / 2
x_new = (1 + cth) / 2 + (1 - cth) / 2 * sp.cos(th)
al = [sp.simplify(sp.integrate(sp.integrate(sp.legendre(l, x_new), (th, 0, 2 * sp.pi)) / (2 * sp.pi), (cth, -1, 1)) / 2)
      for l in range(5)]
Gs = (sp.Rational(5, 8) + rho / 4) / sp.sqrt(3) + gam * rho / 2 + sp.Rational(4, 135) / (gam * rho)
nuTs = sp.sqrt(3) / 16 + rho / (4 * sp.sqrt(3)) + gam * rho / 2 + sp.Rational(1, 45) / (gam * rho)
ok("C1", (m2, m4, mabs, mabs3, mabsy2) == (sp.Rational(1, 3), sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(1, 4),
                                          sp.Rational(1, 8)) and al[:3] == [1, sp.Rational(1, 2), sp.Rational(1, 4)],
   f"sphere: <s_x^2> = 1/3, <s_x^4> = 1/5, <|s_x|> = 1/2, <|s_x|^3> = 1/4, <|s_x| s_y^2> = 1/8; re-draw retention "
   f"a_l = E P_l(s_new.s) = {', '.join(map(str, al))} (l = 0..4): quadrupole relaxation 3 gamma rho; closure Gamma_s = "
   "(5/8 + rho/4)/sqrt3 + gamma rho/2 + 4/(135 gamma rho), nu_T = sqrt3/16 + rho/(4 sqrt3) + gamma rho/2 + 1/(45 gamma rho)")

# ------------------------------------------------------------------ C2: sphere closure by Galerkin (FLOAT, truncation)
def octant_rule(n):
    x, w = np.polynomial.legendre.leggauss(n)
    th_ = (x + 1) * np.pi / 4
    wt = w * np.pi / 4
    pts, wts = [], []
    for sx_, sy_, sz_ in product((1, -1), repeat=3):
        for i in range(n):
            for j in range(n):
                t_, p_ = th_[i], th_[j]
                pts.append((sx_ * np.sin(t_) * np.cos(p_), sy_ * np.sin(t_) * np.sin(p_), sz_ * np.cos(t_)))
                wts.append(np.sin(t_) * wt[i] * wt[j] / (4 * np.pi))
    return np.array(pts), np.array(wts)


def sphere_basis(Dg, pts, wts):
    """orthonormal basis of polynomials of degree <= Dg on the sphere, grouped by degree (block l spans the degree-l
    harmonics)."""
    basis, deg = [], []
    for dgr in range(Dg + 1):
        for a in range(dgr + 1):
            for b in range(dgr + 1 - a):
                c_ = dgr - a - b
                f = pts[:, 0] ** a * pts[:, 1] ** b * pts[:, 2] ** c_
                for _ in range(2):
                    for g_ in basis:
                        f = f - (wts @ (f * g_)) * g_
                nrm = np.sqrt(wts @ (f * f))
                if nrm > 1e-8:
                    basis.append(f / nrm)
                    deg.append(dgr)
    return np.array(basis), np.array(deg)


pts, wts = octant_rule(24)
Bs, degs = sphere_basis(10, pts, wts)
al_num = []
xg, wg = np.polynomial.legendre.leggauss(40)
for l in range(11):
    tot = 0.0
    for xi, wi in zip(xg, wg):
        for tj, wj in zip(np.pi * (xg + 1), np.pi * wg):
            xn = (1 + xi) / 2 + (1 - xi) / 2 * np.cos(tj)
            tot += wi * wj * np.polynomial.legendre.legval(xn, [0] * l + [1]) / (2 * 2 * np.pi)
    al_num.append(tot)


def sphere_ops(kk, rho_, gam_):
    px, mx = np.maximum(0, pts[:, 0]) / np.sqrt(3), np.maximum(0, -pts[:, 0]) / np.sqrt(3)
    pbar = 1 / (4 * np.sqrt(3))
    fS = px * (np.exp(-1j * kk) - 1) + mx * (np.exp(1j * kk) - 1)
    Smat = (Bs * wts) @ (fS[:, None] * Bs.T) + rho_ * pbar * (2 * np.cos(kk) - 2) * np.eye(len(Bs))
    avg_b = Bs @ wts
    Smat += rho_ * np.outer(avg_b, ((1 - np.exp(-1j * kk)) * (Bs * wts) @ px + (1 - np.exp(1j * kk)) * (Bs * wts) @ mx))
    two_sig = 2 * np.cos(kk) + 4
    cdiag = np.array([0.0 if d == 0 else gam_ * rho_ * (al_num[d] * (6 + two_sig) - 6) for d in degs])
    return Smat, np.diag(cdiag)


def sound_eig(Mm):
    lam_ = np.linalg.eigvals(Mm)
    cand = [z for z in lam_ if abs(z.imag) > 1e-7]
    return max(cand, key=lambda z: z.real)


Gs_f = float(Gs.subs({rho: sp.Rational(3, 10), gam: 1}))
nT_f = float(nuTs.subs({rho: sp.Rational(3, 10), gam: 1}))
kk0 = 0.01
Ss, Cs = sphere_ops(kk0, 0.3, 1.0)
eg = np.linalg.eigvals(Ss + Cs)
zs = max((z for z in eg if abs(z.imag) > 1e-7), key=lambda z: z.real)
zt = max((z for z in eg if abs(z.imag) <= 1e-7), key=lambda z: z.real)
ok("C2", abs(-2 * zs.real / kk0 ** 2 - Gs_f) < 2e-3 * Gs_f and abs(abs(zs.imag) / kk0 - np.sqrt(0.7) / 3) < 1e-3
   and abs(-zt.real / kk0 ** 2 - nT_f) < 2e-3 * nT_f,
   f"FLOAT: sphere closure as a Galerkin operator (harmonics l <= 10, octant Gauss rule) at rho = 0.3, gamma = 1, "
   f"k = 0.01: Gamma {-2 * zs.real / kk0 ** 2:.5f} vs {Gs_f:.5f}, speed {abs(zs.imag) / kk0:.5f} vs sqrt(1 - rho)/3, "
   f"shear {-zt.real / kk0 ** 2:.5f} vs nu_T {nT_f:.5f}")


# ------------------------------------------------------------------ D: the simulator's tick (CLOSURE + exact pair map)
def six_ops(kk, rho_, gam_):
    Sm, Cm = M6(sp.Float(kk), gam_, series=False)
    f = sp.lambdify([rho], (Sm, Cm), "numpy")
    Sn, Cn = f(rho_)
    return np.array(Sn, complex), np.array(Cn, complex)


def tick_rates(kk, rho_, gam_, menu):
    if menu == "six":
        Sn, Cn = six_ops(kk, rho_, gam_)
    else:
        Sn, Cn = sphere_ops(kk, rho_, gam_)
    geff = 1 - np.exp(-gam_)
    cont = sound_eig(Sn + Cn)
    tick = np.log(sound_eig_T((np.eye(len(Sn)) + Cn * geff / gam_) @ expm(Sn)))
    return -cont.real, -tick.real, cont, tick


def sound_eig_T(Tm):
    mu = np.linalg.eigvals(Tm)
    cand = [z for z in mu if abs(np.log(z).imag) > 1e-7]
    return max(cand, key=lambda z: abs(z))


ge = 1 - np.exp(-1.0)
G6t = 2 / 3 + 0.3 / 6 + ge * 0.3 / 2 + 1 / (3 * ge * 0.3) - 1 / 3
Gst = float((sp.Rational(5, 8) + sp.Rational(3, 40)) / sp.sqrt(3)) + ge * 0.3 / 2 + (4 / 45) * (1 / (3 * ge * 0.3) - 0.5)
small = 0.004
d6c, d6t, _, _ = tick_rates(small, 0.3, 1.0, "six")
dsc, dst, _, _ = tick_rates(small, 0.3, 1.0, "sphere")
G6 = float(Gam6.subs({rho: sp.Rational(3, 10), gam: 1}))
ok("D1", abs(2 * d6t / small ** 2 - G6t) < 1e-3 * G6t and abs(2 * dst / small ** 2 - Gst) < 2e-3 * Gst
   and abs(2 * d6c / small ** 2 - G6) < 1e-3 * G6,
   f"tick of block 44's simulator (all streaming, then a collision phase on a frozen configuration, each bond Poisson(gamma)"
   f" times): per isolated pair the phase is I + (1 - e^-gamma)(T - I) (A1), so a quadrupole keeps 1 - 2 geff rho per tick "
   f"(six) with geff = 1 - e^-gamma; the tick's Gamma replaces gamma by geff and 1/lambda by 1/lambda_tick - 1/2: six "
   f"{2 * d6t / small ** 2:.4f} = {G6t:.4f}, sphere {2 * dst / small ** 2:.4f} = {Gst:.4f} (FLOAT eigenvalues at k = 0.004)")

# ------------------------------------------------------------------ E: predictions for block 44's four numbers
meas = {("six", 1): (0.0130, 0.0140), ("six", 2): (0.0500, 0.0480), ("sphere", 1): (0.0030, 0.0030),
        ("sphere", 2): (0.0130, 0.0130)}
lines = []
pred = {}
for menu in ("six", "sphere"):
    for mode in (1, 2):
        kk = 2 * np.pi * mode / 64
        dc, dt_, _, _ = tick_rates(kk, 0.3, 1.0, menu)
        pred[(menu, mode)] = (dc, dt_)
        lines.append(f"{menu} lambda {64 // mode}: closure {dc:.4f}, tick {dt_:.4f}, measured {meas[(menu, mode)][0]:.4f}/"
                     f"{meas[(menu, mode)][1]:.4f}")
sph_ok = all(abs(pred[("sphere", m)][0] - meas[("sphere", m)][0]) < 0.12 * meas[("sphere", m)][0] for m in (1, 2))
six_low = all(pred[("six", m)][0] < 0.85 * min(meas[("six", m)]) for m in (1, 2))
ok("E1", sph_ok and six_low, "rho = 0.3, gamma = 1 (damping per tick = -Re of the sound eigenvalue, FLOAT): "
   + "; ".join(lines) + ". The closure meets the sphere's numbers and falls 25-30 per cent short of the six-axis ones")

# ------------------------------------------------------------------ F: simulations (FLOAT evidence)
sys.path.insert(0, __file__.rsplit("/probes/", 1)[0] + "/probes/lib")
from numba import njit  # noqa: E402
from inertial import fit_damped, seed_compiled, sound, tick6  # noqa: E402

EK = np.array(D6, np.int64)


@njit(cache=False)
def seed_ct(s):
    np.random.seed(s)


@njit(cache=False)
def tick_ct(dirn, L, gamma):
    """the clause in continuous time: streaming attempts and bond draws interleaved at random."""
    n_att = L * L * L
    n_col = gamma * 3.0 * n_att
    p_str = n_att / (n_att + n_col)
    for _ in range(int(n_att + n_col)):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L)
        if np.random.random() < p_str:
            d = dirn[x, y, z]
            if d < 0:
                continue
            tx = (x + EK[d, 0]) % L; ty = (y + EK[d, 1]) % L; tz = (z + EK[d, 2]) % L
            d2 = dirn[tx, ty, tz]; dirn[tx, ty, tz] = d; dirn[x, y, z] = d2
        else:
            kd = 2 * np.random.randint(0, 3)
            tx = (x + EK[kd, 0]) % L; ty = (y + EK[kd, 1]) % L; tz = (z + EK[kd, 2]) % L
            d = dirn[x, y, z]; d2 = dirn[tx, ty, tz]
            if d < 0 or d2 < 0:
                continue
            if d2 == (d ^ 1):
                e = np.random.randint(0, 6); dirn[x, y, z] = e; dirn[tx, ty, tz] = e ^ 1
            elif np.random.random() < 0.5:
                dirn[x, y, z] = d2; dirn[tx, ty, tz] = d


def sound_ct(L, rho0, gamma, modes, T_, runs, seed, eps=0.2):
    rng = np.random.default_rng(seed); seed_ct(seed); xs = np.arange(L); out = {}
    for mode in modes:
        kk = 2 * np.pi * mode / L; amps = np.zeros(T_ + 1)
        for _ in range(runs):
            prof = rho0 * (1 + eps * np.cos(kk * xs))[:, None, None] * np.ones((L, L, L))
            dirn = np.full((L, L, L), -1, np.int8); o = rng.random((L, L, L)) < prof
            dirn[o] = rng.integers(0, 6, o.sum())
            for t_ in range(T_ + 1):
                amps[t_] += 2 * np.mean((dirn >= 0).sum(axis=(1, 2)) / L ** 2 * np.cos(kk * xs)) / (rho0 * eps) / runs
                tick_ct(dirn, L, gamma)
        out[mode] = amps
    return out


def q_rate(L, rho0, gamma, stepper, seed, T_=6, runs=4):
    rng = np.random.default_rng(seed); acc = np.zeros(T_ + 1)
    for _ in range(runs):
        dirn = np.full((L, L, L), -1, np.int8); o = rng.random((L, L, L)) < rho0
        dirn[o] = rng.choice(6, size=o.sum(), p=np.array([0.25, 0.25, 0.125, 0.125, 0.125, 0.125])).astype(np.int8)
        for t_ in range(T_ + 1):
            cnt = np.bincount(dirn[dirn >= 0], minlength=6)
            acc[t_] += ((cnt[0] + cnt[1]) - 0.5 * cnt[2:].sum()) / runs
            stepper(dirn, L, gamma)
    r = -np.log(acc[1:] / acc[:-1])
    return float(np.mean(r[1:4]))


t0 = time.time()
seed_compiled(44)
blk = sound("six", 64, 0.3, 1.0, (1, 2), 300, 4, seed=44)
g_blk = [fit_damped(blk[m], 2 * np.pi * m / 64)[2] for m in (1, 2)]
seed_compiled(45)
sph = sound("sphere", 64, 0.3, 1.0, (1, 2), 300, 4, seed=45)
g_sph = [fit_damped(sph[m], 2 * np.pi * m / 64)[2] for m in (1, 2)]
ok("F1", abs(g_blk[0] - 0.0135) <= 0.0025 and abs(g_blk[1] - 0.049) <= 0.006 and abs(g_sph[0] - 0.003) <= 0.001
   and abs(g_sph[1] - 0.013) <= 0.002,
   f"FLOAT: block 44's simulator (side 64, 4 runs, 300 ticks, its own fit) reproduces the measured damping: six "
   f"{g_blk[0]:.4f}, {g_blk[1]:.4f}; sphere {g_sph[0]:.4f}, {g_sph[1]:.4f} ({time.time() - t0:.0f} s)")

t0 = time.time()
rows = []
good_rows = True
for rho_, gam_ in ((0.3, 1.0), (0.5, 1.0), (0.15, 1.0)):
    qr = q_rate(32, rho_, gam_, tick_ct, seed=7)
    res = sound_ct(64, rho_, gam_, (1,), 300, 4, seed=8)
    g_ct = fit_damped(res[1], 2 * np.pi / 64)[2]
    kk = 2 * np.pi / 64
    Gcl = 2 / 3 + rho_ / 6 + gam_ * rho_ / 2 + 1 / (3 * gam_ * rho_)
    Gq = 2 / 3 + rho_ / 6 + gam_ * rho_ / 2 + (2 / 3) / qr
    rows.append(f"rho {rho_}: Q rate {qr:.3f} (closure {2 * gam_ * rho_:.2f}), damping {g_ct:.4f}; closure "
                f"{Gcl * kk ** 2 / 2:.4f}, closure with the measured Q rate {Gq * kk ** 2 / 2:.4f}")
    good_rows &= qr < 0.9 * 2 * gam_ * rho_ and g_ct > Gcl * kk ** 2 / 2 and abs(Gq * kk ** 2 / 2 - g_ct) < 0.2 * g_ct
ok("F2", good_rows, "FLOAT: the clause in continuous time (streaming and bond draws interleaved at random; side 64, mode "
   "1, gamma = 1): " + "; ".join(rows) + f" ({time.time() - t0:.0f} s)")

status = "PARTIAL" if not FAILS else "PARTIAL (failed checks: " + ", ".join(FAILS) + ")"
ps = [pred[(m_, i)][0] for m_ in ("sphere", "six") for i in (1, 2)]
print(f"SUMMARY: {status} exact one-point closure of block 44's clause: the pair re-draw is the projection on 19 momentum "
      "classes, the one-site operator has 0 x4 and -2 gamma rho x2; Gamma = 2/3 + rho/6 + gamma rho/2 + 1/(3 gamma rho) "
      "(six axes), (5/8 + rho/4)/sqrt3 + gamma rho/2 + 4/(135 gamma rho) (sphere); it meets the sphere's damping and "
      "falls 25-30 per cent short on the six axes, where the clause relaxes the quadrupole slower than 2 gamma rho")
if not FAILS:
    print("HIT: in the one-point product closure of block 44's clause the sound attenuation is Gamma = D + nu_L, D = "
          "(1 - rho)/6 + rho/6 = 1/6, nu_L = 1/2 + rho/6 + gamma rho/2 + 1/(3 gamma rho) on the six-axis menu (shear "
          "exactly rho/6 + gamma rho/2), and Gamma = (5/8 + rho/4)/sqrt3 + gamma rho/2 + 4/(135 gamma rho) on the "
          f"sphere menu; at rho = 0.3, gamma = 1 it gives {ps[0]:.4f} and {ps[1]:.4f} against the sphere's measured "
          f"0.0030 and 0.0130, and {ps[2]:.4f} and {ps[3]:.3f} against the six axes' 0.013-0.014 and 0.048-0.050, the "
          "gap sitting in the quadrupole's relaxation, measured near 0.47 per tick against the closure's 0.6")
