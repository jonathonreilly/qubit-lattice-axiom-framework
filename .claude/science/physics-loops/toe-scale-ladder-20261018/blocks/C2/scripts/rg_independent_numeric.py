#!/usr/bin/env python3
"""Independent numerical check of the C2(ii) one-loop coefficients.

Different path from rg_one_loop_analytic.py:
  * explicit 4x4 Euclidean gamma matrices, numerical matrix inverse of the fermion kernel;
  * no hand angular averaging: full 4D hyperspherical quadrature (all four angles/radius);
  * a NON-spherical smooth regulator R(k) = g(k/L2) - g(k/L1), g = exp(-(k0^2 + 2|k|^2)),
    whose log coefficient is regulator-shape independent (Frullani) -> divide by ln(L2/L1);
  * the photon coefficients from an explicit fermion-loop Pi_{mu nu}(q) second derivative,
    not from the frame-rescaling argument;
  * a gauge-parameter term lambda k_mu k_nu/(k0^2+v^2 k^2)^2 added to check gauge independence.
Quantities compared (per unit l, e = 1):
  d ln c_psi/dl = [eta - 4/(1+eta)^2]/(6 pi^2),  d eps/dl = 1/(6 pi^2 c),  d(1/mu)/dl = c/(6 pi^2).
"""
import sys
import numpy as np

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from c2_common import Checks

ck = Checks()
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z = np.zeros((2, 2)); I2 = np.eye(2)
g0 = np.block([[Z, I2], [I2, Z]]).astype(complex)
gs = [np.block([[Z, -1j * s], [1j * s, Z]]) for s in (s1, s2, s3)]
gam = [g0] + gs
ok = all(np.allclose(gam[m] @ gam[n] + gam[n] @ gam[m], 2 * (m == n) * np.eye(4)) for m in range(4) for n in range(4))
ck.check('Euclidean gammas: {g_mu, g_nu} = 2 delta, Hermitian', ok and all(np.allclose(g, g.conj().T) for g in gam))

# quadrature grid
nr, nchi, nth, nph = 96, 20, 12, 12
x_r, w_r = np.polynomial.legendre.leggauss(nr); lr = -2.0 + 6.0 * x_r; wlr = 6.0 * w_r    # ln r in [-8, 4] (run 1 used [-4,4]: IR tail error 1.9e-4)
x_c, w_c = np.polynomial.legendre.leggauss(nchi); chi = np.pi / 2 * (x_c + 1); wchi = np.pi / 2 * w_c
x_t, w_t = np.polynomial.legendre.leggauss(nth)                                            # cos theta
ph = 2 * np.pi * (np.arange(nph) + 0.5) / nph; wph = np.full(nph, 2 * np.pi / nph)
R_, C_, T_, P_ = np.meshgrid(lr, chi, x_t, ph, indexing='ij')
W = (np.meshgrid(wlr, wchi, w_t, wph, indexing='ij'))
W = W[0] * W[1] * W[2] * W[3]
r = np.exp(R_); st = np.sqrt(1 - T_ ** 2)
k = np.stack([r * np.cos(C_), r * np.sin(C_) * st * np.cos(P_), r * np.sin(C_) * st * np.sin(P_), r * np.sin(C_) * T_], -1).reshape(-1, 4)
meas = (W * r ** 4 * np.sin(C_) ** 2).reshape(-1) / (2 * np.pi) ** 4                       # d^4k = r^3 dr dOmega = r^4 dln r ...
L1, L2 = 1.0, np.exp(1.5)
gfun = lambda q: np.exp(-(q[:, 0] ** 2 + 2 * np.sum(q[:, 1:] ** 2, 1)))
Rk = gfun(k / L2) - gfun(k / L1)
logL = np.log(L2 / L1)
# sanity of measure+regulator: int R(k)/k^4 d^4k = 2pi^2/(2pi)^4 * ln(L2/L1)
kk2 = np.sum(k ** 2, 1)
test = np.sum(meas * Rk / kk2 ** 2) / logL
ck.check('quadrature: int R(k)/k^4 = ln(L2/L1)/(8 pi^2) for the anisotropic regulator', abs(test * 8 * np.pi ** 2 - 1) < 1e-6, f"{test*8*np.pi**2:.8f}")

def Kmat(q, c):
    out = 1j * (q[:, 0, None, None] * g0 + c * sum(q[:, j + 1, None, None] * gs[j] for j in range(3)))
    return out

def fermion_speed_flow(c, v, lam=0.0):
    G = np.linalg.inv(Kmat(-k, c))                               # G(p-k) at p=0
    Kd = [1j * g0] + [1j * c * g for g in gs]                    # dK/dq_mu
    Gam = [1j * g0] + [1j * c * g for g in gs]                   # vertices
    den = k[:, 0] ** 2 + v ** 2 * np.sum(k[:, 1:] ** 2, 1)
    Dd = np.stack([v ** 3 / den] + [v / den] * 3, 1)             # diagonal Feynman part
    res = {}
    for mu_p in (0, 1):                                          # derivative w.r.t. p0 and p1
        dG = -G @ Kd[mu_p] @ G                                   # d G(p-k)/dp
        S = np.zeros((4, 4), complex)
        for m in range(4):
            S += np.einsum('n,nab->ab', meas * Rk * Dd[:, m], Gam[m] @ dG @ Gam[m])
        if lam:
            for m in range(4):
                for n in range(4):
                    wgt = meas * Rk * lam * k[:, m] * k[:, n] / den ** 2
                    S += np.einsum('n,nab->ab', wgt, Gam[m] @ dG @ Gam[n])
        res[mu_p] = S
    d0 = np.trace(g0 @ res[0]) / (4j)
    ds = np.trace(gs[0] @ res[1]) / (4j * c)
    # also check the structure: off-components vanish
    off = abs(np.trace(gs[0] @ res[0])) + abs(np.trace(g0 @ res[1]))
    return ((d0 - ds) / logL).real, off

def F(eta):
    return (eta - 4 / (1 + eta) ** 2) / (6 * np.pi ** 2)

for (c, v) in [(1.0, 1.0), (1.0, 1.5), (0.8, 1.6), (1.0, 0.6), (1.3, 1.0)]:
    val, off = fermion_speed_flow(c, v)
    ck.check(f'fermion speed flow, c_psi={c}, c_gamma={v}: numeric {val:.6e} vs closed form {F(v/c):.6e}',
             abs(val - F(v / c)) < 2e-4 * max(abs(F(v / c)), 1e-2) + 1e-7 and off < 1e-10)
val0, _ = fermion_speed_flow(1.0, 1.5)
val1, _ = fermion_speed_flow(1.0, 1.5, lam=0.7)
val2, _ = fermion_speed_flow(1.0, 1.5, lam=-1.3)
ck.check('gauge independence: adding lambda k_mu k_nu/(k0^2+v^2k^2)^2 (lambda=0.7,-1.3) leaves d ln c_psi/dl unchanged',
         abs(val1 - val0) < 1e-7 and abs(val2 - val0) < 1e-7, f"{val0:.8e},{val1:.8e},{val2:.8e}")

def vac_pol(c):
    """q^2 coefficients of Pi_00(q e_z) and Pi_xx(q e_z) per unit l, from the explicit fermion loop"""
    G = np.linalg.inv(Kmat(k, c))
    n = 3
    Kn = 1j * c * gs[2]
    Gp = -G @ Kn @ G
    Gpp = 2 * G @ Kn @ G @ Kn @ G
    out = {}
    for (m, Gm) in [(0, 1j * g0), (1, 1j * c * gs[0])]:
        f2 = 0.25 * np.trace(Gm @ Gpp @ Gm @ G, axis1=1, axis2=2) + 0.25 * np.trace(Gm @ G @ Gm @ Gpp, axis1=1, axis2=2) \
            - 0.5 * np.trace(Gm @ Gp @ Gm @ Gp, axis1=1, axis2=2)
        out[m] = (np.sum(meas * Rk * f2) / 2 / logL).real
    return out
for c in [1.0, 0.7, 1.4]:
    o = vac_pol(c)
    ck.check(f'vacuum polarisation c_psi={c}: d eps/dl = {o[0]:.6e} vs 1/(6pi^2 c) = {1/(6*np.pi**2*c):.6e}; d(1/mu)/dl = {o[1]:.6e} vs c/(6pi^2) = {c/(6*np.pi**2):.6e}',
             abs(o[0] * 6 * np.pi ** 2 * c - 1) < 2e-4 and abs(o[1] * 6 * np.pi ** 2 / c - 1) < 2e-4)
sys.exit(ck.total())
