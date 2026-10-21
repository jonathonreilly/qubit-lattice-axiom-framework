#!/usr/bin/env python3
"""C2(ii): one-loop flow of c_gamma, c_psi, e^2 in U(1) + one Dirac fermion with independent speeds.

Euclidean action (hbar = 1), l = ln(Lambda/mu) increasing toward the IR:
  S_psi = int psibar [gamma0 (d0 + i A0) + c gamma_j (d_j + i A_j)] psi          (c = c_psi)
  S_A   = (1/2e^2) int [ (1/v) F_{0j}^2 + v (1/2) F_{jk}^2 ]                     (v = c_gamma)
          == (1/2) int [eps E^2 + (1/mu) B^2],  eps = 1/(e^2 v),  1/mu = v/e^2.
Photon propagator, Feynman gauge in the v-rescaled frame (derived in NOTE):
  D_00 = e^2 v^3/(k0^2+v^2 k^2),  D_jl = e^2 v delta_jl/(k0^2+v^2 k^2).
Fermion speed: Sigma_lin = i(delta_0 gamma0 p0 + delta_s c gamma.p);  d ln c/dl = delta_0 - delta_s.
Photon:  one fermion loop = standard QED loop in the c-rescaled frame ->
  d eps/dl = 1/(6 pi^2 c),  d(1/mu)/dl = c/(6 pi^2).
Everything symbolic here; the independent check is rg_independent_numeric.py.
"""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from c2_common import Checks

ck = Checks()
u, c, v, eta, e2, d = sp.symbols('u c v eta e2 delta', positive=True)

# ---- fermion self-energy (Feynman gauge in photon frame), angular reduction done by hand:
#  linear part of X(q)=qslash_c/w(q) at q=-k, spatial average k_j k_l -> delta k^2/3:
#    a0 = 1/w - 2 k0^2/w^2 ,  as = 1/w - (2/3) c^2 k^2/w^2
#  gamma sandwiches: g0 X g0 -> (a0 g0p0 - as c g.p) ; sum_j gj X gj -> (-3 a0 g0p0 - as c g.p)
#  => delta_0 - delta_s = int [a0 (D00 - 3 c^2 Ds) + as (D00 + c^2 Ds)]
# 4D shell: k0 = K cos th, |k| = K sin th, dOmega_3 = 4 pi sin^2 th dth; u = tan th.
C2_, S2_ = 1 / (1 + u ** 2), u ** 2 / (1 + u ** 2)
w = C2_ + c ** 2 * S2_
den = C2_ + v ** 2 * S2_
D00, Ds = v ** 3 / den, v / den               # times e^2
a0 = 1 / w - 2 * C2_ / w ** 2
as_ = 1 / w - sp.Rational(2, 3) * c ** 2 * S2_ / w ** 2
integrand = (a0 * (D00 - 3 * c ** 2 * Ds) + as_ * (D00 + c ** 2 * Ds)) * 4 * sp.pi * S2_ / (2 * sp.pi) ** 4 / (1 + u ** 2) * 2
I = sp.factor(sp.together(integrand.subs(c, 1).subs(v, eta)))
Fpsi = sp.simplify(sp.integrate(sp.apart(I, u), (u, 0, sp.oo)))
Fclosed = (eta - 4 / (eta + 1) ** 2) / (6 * sp.pi ** 2)
ck.check('d ln c_psi/dl = e^2 [eta - 4/(1+eta)^2]/(6 pi^2), eta = c_gamma/c_psi (exact integral)',
         sp.simplify(Fpsi - Fclosed) == 0, f"sympy result: {Fpsi}")
# depends only on v/c: check homogeneity numerically at (c,v)=(2,3) vs (1,1.5)
fnum = sp.lambdify((u, c, v), integrand)
from scipy.integrate import quad
q1 = quad(lambda x: fnum(x, 2.0, 3.0), 0, np.inf)[0]
q2 = quad(lambda x: fnum(x, 1.0, 1.5), 0, np.inf)[0]
ck.check('fermion flow depends on c_gamma/c_psi only (time-rescaling invariance)', abs(q1 - q2) < 1e-10 and abs(q2 - float(Fclosed.subs(eta, 1.5))) < 1e-10)
ck.check('Lorentz point eta=1 is fixed: F_psi(1)=0', Fclosed.subs(eta, 1) == 0)
alphaC = sp.symbols('alpha_C', positive=True)
lim = sp.limit(Fclosed * 4 * sp.pi * alphaC / eta, eta, sp.oo)  # e^2 = 4 pi alpha_C / eta  (alpha_C = e^2 v/(4 pi c))
ck.check('instantaneous-Coulomb limit eta->inf: d ln c_psi/dl -> 2 alpha_C/(3 pi), alpha_C = e^2 c_gamma/(4 pi c_psi)',
         sp.simplify(lim - 2 * alphaC / (3 * sp.pi)) == 0)

# ---- photon: frame-rescaling of the standard loop
# x' = x/c, A'_j = c A_j: E' = c E, B' = c^2 B, d^3x' = d^3x/c^3; standard loop adds (l/(6pi^2))(1/2)(E'^2 - B'^2) (Minkowski)
E_, B_ = sp.symbols('E B')
dL = sp.expand(((c * E_) ** 2 - (c ** 2 * B_) ** 2) / c ** 3)
ck.check('fermion loop adds (l/6pi^2)(1/2)(E^2/c_psi - c_psi B^2): d eps = 1/(6pi^2 c), d(1/mu) = c/(6pi^2)',
         sp.simplify(dL - (E_ ** 2 / c - c * B_ ** 2)) == 0)
epsv, imu = 1 / (e2 * v), v / e2
dlneps = (1 / (6 * sp.pi ** 2 * c)) / epsv
dlnimu = (c / (6 * sp.pi ** 2)) / imu
dlnv = sp.simplify((dlnimu - dlneps) / 2)
ck.check('d ln c_gamma/dl = (e^2/12 pi^2)(1/eta - eta)', sp.simplify(dlnv - e2 / (12 * sp.pi ** 2) * (c / v - v / c)) == 0)
dinv_e2 = sp.simplify((1 / e2) * (dlneps + dlnimu) / 2)
ck.check('d(1/e^2)/dl = (eta + 1/eta)/(12 pi^2) -> 1/(6 pi^2) at eta=1 (standard QED, d(1/alpha)/dl = 2/(3 pi))',
         sp.simplify(dinv_e2 - (v / c + c / v) / (12 * sp.pi ** 2)) == 0)

# ---- combined flow of eta
beta_eta = sp.simplify(e2 / (12 * sp.pi ** 2) * (1 / eta - eta) - e2 * Fclosed)
target = e2 / (12 * sp.pi ** 2) * (1 / eta - 3 * eta + 8 / (1 + eta) ** 2)
ck.check('d ln eta/dl = (e^2/12pi^2)[1/eta - 3 eta + 8/(1+eta)^2]', sp.simplify(beta_eta - target) == 0)
slope = sp.simplify(sp.diff(target, eta).subs(eta, 1))
ck.check('linearised: d delta/dl = -(e^2/2pi^2) delta = -(2 alpha/pi) delta, delta = ln eta', sp.simplify(slope + e2 / (2 * sp.pi ** 2)) == 0)
# sign of beta: attractive for all eta>0 ?
xs = np.linspace(0.05, 20, 4000)
bf = sp.lambdify(eta, target.subs(e2, 1))
vals = bf(xs)
ck.check('attractive globally on (0.05,20): sign d ln eta/dl = -sign(ln eta)', np.all(np.sign(vals[np.abs(xs - 1) > 1e-6]) == -np.sign(np.log(xs[np.abs(xs - 1) > 1e-6]))))
# c_gamma^2 c_psi stationary to second order (structure reported for Isobe-Nagaosa 2012)
comb = sp.simplify(2 * e2 / (12 * sp.pi ** 2) * (1 / eta - eta) + e2 * Fclosed)
ck.check('d ln(c_gamma^2 c_psi)/dl = (e^2/6pi^2)[1/eta - 4/(1+eta)^2] = O((eta-1)^2)',
         sp.simplify(comb - e2 / (6 * sp.pi ** 2) * (1 / eta - 4 / (1 + eta) ** 2)) == 0
         and comb.subs(eta, 1) == 0 and sp.diff(comb, eta).subs(eta, 1) == 0)

# ---- N_f species with a common speed (photon drag scales with N_f; fermion drag does not)
Nf, al = sp.symbols('N_f alpha', positive=True)
lin = -(e2 / (6 * sp.pi ** 2)) * Nf - (e2 / (6 * sp.pi ** 2)) * 2   # photon part Nf*(-2)/(12pi^2), fermion part -2/(6pi^2)
ck.check('N_f: d delta/dl = -(2 alpha/3pi)(N_f + 2) delta; equals -(2alpha/pi) at N_f=1',
         sp.simplify(lin.subs(e2, 4 * sp.pi * al).subs(Nf, 1) + 2 * al / sp.pi) == 0)
# with d alpha/dl = -(2 N_f/3pi) alpha^2 : delta_IR/delta_UV = (alpha_IR/alpha_UV)^((N_f+2)/N_f)
print("  closed form: delta(l)/delta(0) = (alpha(l)/alpha(0))^((N_f+2)/N_f)  [linearised, one loop]")

# ---- numbers: declared inputs
alpha_IR = 1 / 137.035999   # Thomson-limit fine-structure constant (CODATA, ~1/137.036)
def run(eta0, ell, Nf=1):
    """integrate nonlinear one-loop system from UV (l=0) to IR (l=ell); returns eta(ell), alpha(ell)"""
    # choose alpha_UV so that the Lorentz-limit running gives alpha_IR at ell (declared matching)
    inv_aUV = 1 / alpha_IR - 2 * Nf / (3 * np.pi) * ell
    def rhs(l, y):
        x, inv_e2 = y          # x = ln eta
        et = np.exp(x); E2 = 1 / inv_e2
        dlnv = E2 / (12 * np.pi ** 2) * Nf * (1 / et - et)
        dlnc = E2 * (et - 4 / (et + 1) ** 2) / (6 * np.pi ** 2)
        return [dlnv - dlnc, Nf * (et + 1 / et) / (12 * np.pi ** 2)]
    y0 = [np.log(eta0), inv_aUV / (4 * np.pi)]
    sol = solve_ivp(rhs, [0, ell], y0, rtol=1e-11, atol=1e-14)
    return np.exp(sol.y[0, -1]), 1 / (4 * np.pi * sol.y[1, -1]), 1 / inv_aUV

print("\n  declared: alpha(m_e) = 1/137.036, l = ln(M/m_e); one Dirac species unless stated")
for ell in [51.0, np.log(1.22091e19 / 0.51099895e-3), np.log(2.435e18 / 0.51099895e-3)]:
    print(f"  l = {ell:.3f}")
    for eta0 in [1 + 1e-3, 1.025 / 0.9144, 1.2, 2.0]:
        etaIR, aIR, aUV = run(eta0, ell)
        r = np.log(etaIR) / np.log(eta0)
        print(f"    eta_UV={eta0:.6f}  ->  eta_IR={etaIR:.6f}   ln eta_IR/ln eta_UV = {r:.4f}   (alpha_UV=1/{1/aUV:.3f})")
etaIR, aIR, aUV = run(1 + 1e-6, 51.0)
pred = (aIR / aUV) ** 3
ck.check('l=51, N_f=1, small mismatch: numerical residual ratio = (alpha_IR/alpha_UV)^3 (closed form)',
         abs(np.log(etaIR) / np.log(1 + 1e-6) - pred) < 1e-4, f"num={np.log(etaIR)/np.log(1+1e-6):.5f}, closed={pred:.5f}")
ck.check('the IR mismatch retains >70% of its UV value over l=51 (N_f=1)', pred > 0.7)
for Nf_ in [1, 3, 8]:
    inv_aUV = 1 / alpha_IR - 2 * Nf_ / (3 * np.pi) * 51.0
    print(f"  N_f={Nf_} (unit charges, common speed; illustrative): alpha_UV=1/{inv_aUV:.2f}, residual factor (alpha_IR/alpha_UV)^((N+2)/N) = {(inv_aUV*alpha_IR)**((Nf_+2)/Nf_):.4f}")
# required UV tuning for a declared IR bound
for bound in [1e-15, 1e-20]:
    print(f"  |delta_IR| < {bound:.0e}  requires |delta_UV| < {bound/pred:.2e} (N_f=1, l=51)")
sys.exit(ck.total())
