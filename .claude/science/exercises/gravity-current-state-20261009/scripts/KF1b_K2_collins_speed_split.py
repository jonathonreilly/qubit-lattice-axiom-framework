"""K2: one-loop speed split for Yukawa theory g phi psibar psi (Dirac psi, real phi,
equal bare speeds) with a SPATIAL-ONLY regulator f(|k|/Lambda) on every internal
propagator (Collins-Perez-Sudarsky-Urrutia-Vucetich form), continuous Euclidean
time.  Model of matter living on a liquid of sites, in the liquid's rest frame:
statistically isotropic in space, a rest frame, nothing mixing time and space.

Scalar:  Gamma_2 = 1/2 phi (p^2 + Pi) phi
         Pi(p) = 4 g^2 Int d^4k/(2pi)^4 [m^2 - k.(k+p)] / (D_k D_{k+p}) f(k) f(k+p)
         c_phi^2 = (1 + A_s)/(1 + A_0),  A_mu = coefficient of p_mu^2 in Pi.
Fermion: Sigma(p) = -g^2 Int S(k) Dphi(p-k) f(k) f(p-k), S = (-i kslash + m)/(k^2+m^2)
         inverse propagator i[(1+B0) p0 g0 + (1+Bs) p.g] -> c_psi = (1+B_s)/(1+B_0).
Both fields get the same IR mass m (IR regulator); the split is IR-safe as m -> 0.
Lambda = 1; the result is Lambda-independent (dimensionless, m/Lambda -> 0).
k0 integrals done in closed form: Int dk0 k0^(2a) (k0^2+E^2)^(-n)
   = E^(2a+1-2n) Gamma(a+1/2) Gamma(n-a-1/2) / Gamma(n).
"""
import sympy as sp
import numpy as np
from scipy.integrate import quad

k0, K, c, p0, pz, m, u = sp.symbols('k0 K c p0 pz m u', real=True)  # u = 1/(k0^2+E^2)
f0, f1, f2 = sp.symbols('f0 f1 f2')  # f(K), f'(K), f''(K)
E2 = K**2 + m**2


def f_shift(q):  # f(|k + q zhat|) to O(q^2), k = K n, n.zhat = c
    return f0 + f1 * (q * c + q**2 * (1 - c**2) / (2 * K)) + sp.Rational(1, 2) * f2 * q**2 * c**2


def inv_den(shift):  # 1/(k0^2 + E^2 + shift) to O(shift^2), in powers of u
    return u - shift * u**2 + shift**2 * u**3


def k0_integrate(expr):
    """expr polynomial in k0 and u; replace k0^(2a) u^n by the closed form."""
    expr = sp.expand(expr)
    poly = sp.Poly(expr, k0, u)
    out = 0
    for (a2, n), coeff in poly.terms():
        if a2 % 2:
            continue  # odd in k0 -> 0
        a = a2 // 2
        if n == 0:
            raise ValueError('divergent k0 integral')
        val = sp.sqrt(E2)**(2 * a + 1 - 2 * n) * sp.gamma(sp.Rational(2 * a + 1, 2)) * sp.gamma(n - a - sp.Rational(1, 2)) / sp.gamma(n)
        out += coeff * val
    return out


def ang(expr):
    return sp.integrate(sp.expand(expr), (c, -1, 1)) / 2


# ---------- scalar ----------
# time: p = (p0, 0):  D_{k+p} = k0^2 + E^2 + 2 k0 p0 + p0^2
I0 = (m**2 - (k0**2 + k0 * p0 + K**2)) * u * inv_den(2 * k0 * p0 + p0**2) * f0**2
A0 = sp.expand(I0).coeff(p0, 2)
# space: p = (0, pz zhat): D_{k+p} = k0^2 + E^2 + 2 K c pz + pz^2
Is = (m**2 - (k0**2 + K**2 + K * c * pz)) * u * inv_den(2 * K * c * pz + pz**2) * f0 * f_shift(pz)
As = sp.expand(Is).coeff(pz, 2)
meas = 4 * sp.pi * K**2 / (2 * sp.pi)**4
dA_rad = sp.simplify(4 * meas * ang(k0_integrate(As - A0)))  # times g^2
# ---------- fermion (Sigma = i g^2 Int kslash u Dphi(p-k) f f + mass part, odd part only) ----------
# time: Dphi(p-k) = 1/((k0-p0)^2 + E^2) ; coefficient of i g0 p0:
B0i = k0 * u * inv_den(-2 * k0 * p0 + p0**2) * f0**2
B0 = sp.expand(B0i).coeff(p0, 1) / 1  # gamma0 component k0 -> coefficient of p0
B0 = sp.expand(B0)
# space: |p-k| = |k + (-pz) zhat|
Bsi = K * c * u * inv_den(-2 * K * c * pz + pz**2) * f0 * f_shift(-pz)
Bs = sp.expand(Bsi).coeff(pz, 1)
dB_rad = sp.simplify(meas * ang(k0_integrate(Bs - B0)))  # times g^2
print('scalar  (A_s - A_0)/g^2 radial integrand:', dA_rad)
print('fermion (B_s - B_0)/g^2 radial integrand:', dB_rad)

# Lorentz-invariant control: f = 1 (f1 = f2 = 0) must give zero integrand
print('control f=1, scalar :', sp.simplify(dA_rad.subs({f0: 1, f1: 0, f2: 0})))
print('control f=1, fermion:', sp.simplify(dB_rad.subs({f0: 1, f1: 0, f2: 0})))

shapes = {
    'exp(-x^2)': (lambda x: np.exp(-x**2), lambda x: -2 * x * np.exp(-x**2), lambda x: (4 * x**2 - 2) * np.exp(-x**2)),
    'exp(-x^4)': (lambda x: np.exp(-x**4), lambda x: -4 * x**3 * np.exp(-x**4), lambda x: (16 * x**6 - 12 * x**2) * np.exp(-x**4)),
    '1/(1+x^4)': (lambda x: 1 / (1 + x**4), lambda x: -4 * x**3 / (1 + x**4)**2,
                  lambda x: (-12 * x**2 * (1 + x**4) + 32 * x**6) / (1 + x**4)**3),
    'exp(-(x/3)^2)': (lambda x: np.exp(-(x / 3)**2), lambda x: -2 * x / 9 * np.exp(-(x / 3)**2),
                      lambda x: (4 * x**2 / 81 - 2 / 9) * np.exp(-(x / 3)**2)),
}
fA = sp.lambdify((K, m, f0, f1, f2), dA_rad, 'numpy')
fB = sp.lambdify((K, m, f0, f1, f2), dB_rad, 'numpy')
unit = 1 / (16 * np.pi**2)
print('\nshape          m       dc_phi/(g^2/16pi^2)  dc_psi/(g^2/16pi^2)  Delta=(dc_psi-dc_phi)/(g^2/16pi^2)')
for name, (F, F1, F2) in shapes.items():
    for mv in [1e-2, 1e-3, 1e-4]:
        a = quad(lambda x: fA(x, mv, F(x), F1(x), F2(x)), 0, 50, limit=500, points=[mv, 10 * mv, 1.0])[0]
        b = quad(lambda x: fB(x, mv, F(x), F1(x), F2(x)), 0, 50, limit=500, points=[mv, 10 * mv, 1.0])[0]
        dphi = a / 2 / unit
        dpsi = b / unit
        print(f'{name:14s} {mv:7.0e}  {dphi:+.5f}             {dpsi:+.5f}             {dpsi - dphi:+.5f}')
print('\nfermion analytic, massless, shape-independent: +1/3 (derived by hand: -Int f f\' dx = 1/2)')
print('alpha = 1/137: g^2/16pi^2 = 4 pi alpha/16 pi^2 =', 4 * np.pi / 137 / (16 * np.pi**2))
