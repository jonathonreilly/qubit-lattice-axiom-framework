#!/usr/bin/env python3
"""T71 test 1: does stability fix the sign of Newton's coupling in the linearised
foliation-preserving class?  (Pre-registered in PREREG.md.)

Static energy functional (lapse phi, conformal psi, G_H, xi, eta as in PREREG):
    E = -a [ xi*(2|grad psi|^2 + 4 grad phi.grad psi) + eta*|grad phi|^2 ] + m phi(x0),  a = 1/(16 pi G_H)
"""
import sys
import numpy as np
import sympy as sp
import scipy.sparse as sps
import scipy.sparse.linalg as spla

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


# ---------------------------------------------------------------- 1a symbolic
x, y, z, eps = sp.symbols('x y z epsilon')
X = (x, y, z)


def ricci_scalar(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gam = [[[sum(ginv[a, d] * (sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]

    def Ric(b, c):
        s = 0
        for a in range(n):
            s += sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
            for d in range(n):
                s += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
        return s
    return sum(ginv[b, c] * Ric(b, c) for b in range(n) for c in range(n))


psi = sp.Function('psi')(x, y, z)
phi = sp.Function('phi')(x, y, z)
g = sp.exp(2 * eps * psi) * sp.eye(3)
R = sp.simplify(ricci_scalar(g, X))
sqrtg = sp.exp(3 * eps * psi)
L_conf = (1 + eps * phi) * sqrtg * R
L2 = sp.series(L_conf, eps, 0, 3).removeO().coeff(eps, 2)
target = 2 * sum(sp.diff(psi, c) ** 2 for c in X) + 4 * sum(sp.diff(phi, c) * sp.diff(psi, c) for c in X)
from sympy.calculus.euler import euler_equations
eq1 = euler_equations(sp.expand(L2), [phi, psi], list(X))
eq2 = euler_equations(sp.expand(target), [phi, psi], list(X))
diffs = [sp.simplify(e1.lhs - e2.lhs) for e1, e2 in zip(eq1, eq2)]
check("1a-i conformal channel: (N sqrt(g) R3)^(2) = 2|grad psi|^2 + 4 grad phi.grad psi (mod total derivative)",
      all(d == 0 for d in diffs), f"Euler-Lagrange differences {diffs}")

f = sp.Function('f')(z)
gTT = sp.diag(sp.exp(eps * f), sp.exp(-eps * f), 1)
RTT = sp.simplify(ricci_scalar(gTT, X))
L_TT = sp.series(RTT, eps, 0, 3).removeO().coeff(eps, 2)   # sqrt(g) = 1
tgt_TT = -sp.Rational(1, 2) * sp.diff(f, z) ** 2   # -(1/4)(d h_ij)^2 with h_xx = f, h_yy = -f
e1 = euler_equations(sp.expand(L_TT), [f], [z])[0].lhs
e2 = euler_equations(tgt_TT, [f], [z])[0].lhs
check("1a-ii TT channel: (sqrt(g) R3)^(2) = -(1/4)(d h_ij)^2 (mod total derivative), opposite in sign to the conformal channel",
      sp.simplify(e1 - e2) == 0, f"Euler-Lagrange difference {sp.simplify(e1 - e2)}")

# scalar sector: kinetic and potential
lam, xi, eta, k, zd, B, n, zeta = sp.symbols('lambda xi eta k zetadot B n zeta', real=True)
# K_ij = zetadot delta_ij + k_i k_j B (Fourier, N_i = d_i B, h_ij = 2 zeta delta_ij)
kv = sp.Matrix([k, 0, 0])
Kij = zd * sp.eye(3) + kv * kv.T * B
Ktr = Kij.trace()
Lkin = sp.expand((Kij * Kij).trace() - lam * Ktr ** 2)
Bsol = sp.solve(sp.diff(Lkin, B), B)[0]
Lkin_red = sp.simplify(Lkin.subs(B, Bsol))
A_coef = sp.simplify(Lkin_red / zd ** 2)
check("1a-iii scalar kinetic coefficient 2(3 lambda-1)/(lambda-1) after the momentum constraint",
      sp.simplify(A_coef - 2 * (3 * lam - 1) / (lam - 1)) == 0, f"A = {sp.factor(A_coef)}")
Vpot = xi * (2 * k ** 2 * zeta ** 2 + 4 * k ** 2 * n * zeta) + eta * k ** 2 * n ** 2
nsol = sp.solve(sp.diff(Vpot, n), n)[0]
Vred = sp.simplify(Vpot.subs(n, nsol))
Bc = sp.simplify(-Vred / (k ** 2 * zeta ** 2))    # L = A zd^2 - Bc k^2 zeta^2
cs2 = sp.simplify(Bc / A_coef)
cs2_target = xi * (2 * xi - eta) * (lam - 1) / (eta * (3 * lam - 1))
check("1a-iv scalar speed c_s^2 = xi (2 xi - eta)(lambda-1)/(eta (3 lambda-1)) (BPS eq. 19 at xi = 1)",
      sp.simplify(cs2 - cs2_target) == 0, f"c_s^2 = {sp.factor(cs2)}")

# static Newtonian coupling
GH, m, kk = sp.symbols('G_H m kk', positive=True)
a = 1 / (16 * sp.pi * GH)
ph, ps = sp.symbols('ph ps')
Efun = -a * kk ** 2 * (xi * (2 * ps ** 2 + 4 * ph * ps) + eta * ph ** 2) + m * ph
sol = sp.solve([sp.diff(Efun, ph), sp.diff(Efun, ps)], [ph, ps], dict=True)[0]
GN = sp.simplify(-sol[ph] * kk ** 2 / (4 * sp.pi * m))   # phi_k = -4 pi G_N m / k^2
check("1a-v Newtonian coupling G_N = 2 G_H/(2 xi - eta)  (BPS eq. 22: G_N = G_H/(1 - alpha/2) at xi = 1, alpha = eta)",
      sp.simplify(GN - 2 * GH / (2 * xi - eta)) == 0, f"G_N = {sp.factor(GN)}")

# ---------------------------------------------------------------- 1b scan
rng = np.random.default_rng(20260929)
Ndraw = 2_000_000
sG = rng.choice([-1.0, 1.0], Ndraw)
lam_ = rng.uniform(-5, 5, Ndraw)
xi_ = rng.uniform(-3, 3, Ndraw)
eta_ = rng.uniform(-4, 4, Ndraw)
GH_ = sG * rng.uniform(0.1, 3, Ndraw)
A_ = 2 * (3 * lam_ - 1) / (lam_ - 1)
cs2_ = xi_ * (2 * xi_ - eta_) * (lam_ - 1) / (eta_ * (3 * lam_ - 1))
GN_ = 2 * GH_ / (2 * xi_ - eta_)
tensor_ok = (GH_ > 0) & (xi_ > 0)                # no ghost, c_t^2 = xi > 0
scalar_ok = (A_ / GH_ > 0) & (cs2_ > 0)          # no ghost, c_s^2 > 0
stable = tensor_ok & scalar_ok
n_stable = int(stable.sum())
bad = int((stable & (GN_ <= 0)).sum())
check("1b all four stability conditions (tensor and scalar, ghost and gradient) force G_N > 0",
      bad == 0 and n_stable > 1000, f"{n_stable} stable draws of {Ndraw}; stable draws with G_N <= 0: {bad}")
unst_pos = int(((~stable) & (GN_ > 0)).sum())
unst_neg = int(((~stable) & (GN_ < 0)).sum())
print(f"       info: unstable draws with G_N>0: {unst_pos}, with G_N<0: {unst_neg} (attraction is not sufficient for stability)")
# tensor-only (eta = 0 branch, no scalar mode)
xi2 = rng.uniform(-3, 3, 200000); GH2 = rng.choice([-1, 1], 200000) * rng.uniform(0.1, 3, 200000)
st2 = (GH2 > 0) & (xi2 > 0)
check("1b' eta = 0 (Einstein branch, scalar frozen): tensor no-ghost + tensor gradient stability alone force G_N = G_H/xi > 0",
      bool(np.all((GH2 / xi2)[st2] > 0)) and st2.sum() > 1000, f"{int(st2.sum())} stable draws, all G_N > 0")
# half-stable sign combos (which single condition is needed)
for label, mask in [("ghost tensor (G_H<0), xi>0", (GH_ < 0) & (xi_ > 0)),
                    ("tensor gradient-unstable (G_H>0, xi<0)", (GH_ > 0) & (xi_ < 0))]:
    sel = mask & (np.abs(eta_) < 0.05)
    print(f"       info: eta~0, {label}: fraction with G_N<0 = {np.mean(GN_[sel] < 0):.3f}")
# pole
etas = np.array([1.9, 1.99, 2.01, 2.1])
print("       info: G_N (G_H = xi = 1) across the pole at eta = 2:", dict(zip(etas.tolist(), (2 / (2 - etas)).round(2).tolist())))
print("       info: c_s^2 (lambda=2, xi=1) at the same eta:", (((2 - etas) * 1 * (2 - 1)) / (etas * (6 - 1))).round(4).tolist())

# ---------------------------------------------------------------- 1c lattice solve
Lside = 24


def lap3(L):
    e = np.ones(L)
    D = sps.diags([2 * e, -e[:-1], -e[:-1]], [0, 1, -1]).tolil()
    D[0, L - 1] = -1
    D[L - 1, 0] = -1
    D = D.tocsr()
    I = sps.identity(L, format='csr')
    return sps.kron(sps.kron(D, I), I) + sps.kron(sps.kron(I, D), I) + sps.kron(sps.kron(I, I), D)


Lap = lap3(Lside).tocsr()
Nsite = Lside ** 3
idx = lambda i, j, kx: (i * Lside + j) * Lside + kx
# Green function of the lattice Laplacian (mean removed) by FFT for comparison
kg = 2 * np.pi * np.arange(Lside) / Lside
KX, KY, KZ = np.meshgrid(kg, kg, kg, indexing='ij')
lamk = (2 - 2 * np.cos(KX)) + (2 - 2 * np.cos(KY)) + (2 - 2 * np.cos(KZ))
lamk[0, 0, 0] = np.inf
Glat = np.real(np.fft.ifftn(1.0 / lamk))    # L^{-1} delta, mean zero


def pair_energy(c, b, eta_v, r, m=1.0, GH_v=1.0):
    """Stationary point of E(phi,psi) with two point masses at separation r along x;
    returns the interaction energy E(two) - E(one) - E(one), by a sparse linear solve."""
    a_v = 1.0 / (16 * np.pi * GH_v)
    K = sps.bmat([[-2 * a_v * eta_v * Lap, -2 * a_v * b * Lap], [-2 * a_v * b * Lap, -2 * a_v * c * Lap]], format='csc')
    reg = sps.identity(2 * Nsite, format='csc') * 1e-10   # remove the constant zero modes
    K = K + reg

    lu = spla.splu(K)

    def energy(sites):
        rhs = np.zeros(2 * Nsite)
        for s in sites:
            rhs[s] = -m
        rhs[:Nsite] -= rhs[:Nsite].mean()      # neutral background
        sol = lu.solve(rhs)
        # E = (1/2) x.K.x + lin.x  at stationarity = (1/2) lin.x ; lin = m at the source sites (phi block)
        return 0.5 * sum(m * sol[s] for s in sites)
    s1, s2 = idx(0, 0, 0), idx(0, 0, r)
    return energy([s1, s2]) - energy([s1]) - energy([s2])


cases = [
    ("GR-like: conformal channel wrong-sign, no lapse gradient (xi=1: c=2, b=2, eta=0)", 2.0, 2.0, 0.0, +1),
    ("Horava window (xi=1, eta=1)", 2.0, 2.0, 1.0, +1),
    ("Horava outside the window (xi=1, eta=3): scalar tachyon", 2.0, 2.0, 3.0, -1),
    ("ground-state conformal channel (c=-2, b=2, eta=0): all static channels positive", -2.0, 2.0, 0.0, -1),
    ("Nordstrom-like: lapse with a healthy own stiffness, no mixing (b=0, eta=-1)", 2.0, 0.0, -1.0, +1),
    ("healthy lapse stiffness but healthy conformal channel (c=-2, b=2, eta=-3)", -2.0, 2.0, -3.0, +1),
]
allok = True
rows = []
for name, c, bb, et, expect in cases:
    Q = (1 / (16 * np.pi)) * (bb ** 2 / c - et)
    pred_sign = np.sign(Q)
    r = 5
    E = pair_energy(c, bb, et, r)
    # analytic prediction: E(phi) = Q phi.L.phi + m s.phi  =>  E_int = -(m^2/(2Q)) Glat(r)
    E_pred = -1.0 / (2 * Q) * Glat[0, 0, r]
    got = -1 if E > 0 else +1     # attraction = negative interaction energy = +1
    ok = (got == expect) and (pred_sign == expect) and abs(E / E_pred - 1) < 1e-6
    allok &= ok
    rows.append((name, round(E, 6), round(E_pred, 6), ok))
    print(f"       {name}: E_int(r=5) = {E:+.6f} (closed form {E_pred:+.6f}); {'attracts' if got > 0 else 'repels'}; Q_eff sign {int(pred_sign):+d}")
check("1c independent lattice solve: pair-energy sign = sign of Q_eff = a(b^2/c - eta) in all six cases; GR-like and Horava-window attract; ground-state conformal channel with eta = 0 repels; outside the window repels",
      allok, "see lines above")
# G_N magnitude from the diffeo-structured cases
E_gr = pair_energy(2.0, 2.0, 0.0, 5)
E_h1 = pair_energy(2.0, 2.0, 1.0, 5)
print(f"       info: E_int(eta=1)/E_int(eta=0) = {E_h1 / E_gr:.4f}  (G_N ratio 2/(2-1) = {2 / (2 - 1):.4f})")
check("1c' G_N ratio between eta=1 and eta=0 equals 2/(2-eta)", abs(E_h1 / E_gr - 2.0) < 1e-6, f"{E_h1 / E_gr:.6f}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
