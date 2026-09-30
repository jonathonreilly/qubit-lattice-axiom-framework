#!/usr/bin/env python3
"""Kill-round checks for T59 (Claude Sonnet 5.5, same family as attacker).
K1: B2 exponent scan re-anchored at freeze-out (H(x_F) fixed) instead of x=1.
K2: B1 kernel with the integration range extended (tail ~ 1/x) -> percentile windows.
K3: A without the Riccati shortcut for a few hard starts (direct Y-space integration).
K4: Y_inf depends on H(x_F) only? scan H normalisation at freeze-out (factor 2 => yield).
"""
import math, sys
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import kve
from scipy.optimize import brentq

G_DOF, GST = 2.0, 427.0/4.0
COEF = math.log(45.0/(4*math.pi**4) * G_DOF/GST)
def lnYeq(x): return COEF + 2*np.log(x) + np.log(kve(2, x)) - x
def Yeq(x): return math.exp(lnYeq(x))

def rhs_factory(lam, q, fun=None):
    def rhs(x, D):
        c = lam * x**(q-4.0)
        if fun is not None: c *= fun(x)
        r = kve(1, x)/kve(2, x)
        return [r - 2.0*c*Yeq(x)*math.sinh(D[0])]
    return rhs

from scipy.integrate import quad
def run(lam, q, xi, ratio, xmax=400.0, fun=None, dense=False):
    xsw = min(xmax, 300.0)
    sol = solve_ivp(rhs_factory(lam, q, fun), (xi, xsw), [math.log(ratio)], method="Radau",
                    rtol=1e-10, atol=1e-12, dense_output=dense)
    if not sol.success: raise RuntimeError(sol.message)
    lnY = lnYeq(xsw) + sol.y[0, -1]
    if xmax > xsw:   # Yeq^2 ~ e^-600 negligible: d(1/Y)/dx = c(x)
        cf = lambda x: lam * x**(q-4.0) * (fun(x) if fun else 1.0)
        pts = np.exp(np.linspace(math.log(xsw), math.log(xmax), 40))
        integ = sum(quad(cf, a, b, epsabs=0, epsrel=1e-12)[0] for a, b in zip(pts[:-1], pts[1:]))
        lnY = -math.log(math.exp(-lnY) + integ)
    return (lnY, sol) if dense else lnY

# --- reproduce attack's lam by tuning on q=2, start x=1, ratio 1 (same convention)
MPL = 1.220890e19; M = 3940.0; S0, RHOC_H2 = 2891.2, 1.05368e-5
def oh2(lnY): return M*math.exp(lnY)*S0/RHOC_H2
LAM = math.exp(brentq(lambda l: oh2(run(math.exp(l), 2.0, 1.0, 1.0)) - 0.12, math.log(1e11), math.log(1e17), xtol=1e-10))
lnY0, sol0 = run(LAM, 2.0, 1.0, 1.0, dense=True)
xs = np.linspace(1, 400, 200000)
XF = float(xs[np.argmax(sol0.sol(xs)[0] >= math.log(2.5))])
print(f"LAM={LAM:.4e} XF={XF:.2f} Y={math.exp(lnY0):.4e}")

# ---------------- K1: anchor at freeze-out
print("\nK1. exponent scan with H(x_F) pinned (lam_q = LAM * XF^(2-q)); attack pinned H(x=1)")
res = {}
for q in [1.0, 1.5, 2.0, 2.5, 3.0]:
    lamq = LAM * XF**(2.0-q)
    y = run(lamq, q, 1.0, 1.0)
    res[q] = math.exp(y - lnY0)
    print(f"  q={q}: Y(q)/Y(q=2) = {res[q]:.3f}")
print("  (attack, anchored at x=1: q=1 -> 37.09)")
print("  ratio Y(q=1)/Y(q=2) anchored at x_F:", round(res[1.0],3), " prereg threshold >=10 ->", res[1.0] >= 10)

# ---------------- K4: factor-2 in H at freeze-out (Newtonian vs rho+3p type factor)
print("\nK4. yield vs coefficient of H (all x): H -> f H, i.e. lam -> lam/f")
for f in [0.5, 1.0, 2.0]:
    y = run(LAM/f, 2.0, 1.0, 1.0)
    print(f"  H x {f}: Y/Y0 = {math.exp(y-lnY0):.4f}")

# ---------------- K2: kernel with extended range
print("\nK2. kernel window with integration range to xmax=XM (attack used 400 with centres to 500)")
sig, eps = 0.2, 0.02
def bump(xc):
    return lambda x: math.exp(-(math.log(x)-math.log(xc))**2/(2*sig*sig))/(sig*math.sqrt(2*math.pi))
def window(XM, lo=0.2, n=60):
    cen = np.exp(np.linspace(math.log(lo), math.log(XM*0.6), n))
    du = float(np.diff(np.log(cen)).mean())
    K = []
    for xc in cen:
        w = bump(xc)
        up = run(LAM, 2.0, 5.0, Yeq(5.0)/Yeq(5.0), xmax=XM, fun=lambda x, w=w: 1.0/(1.0+eps*w(x)))
        dn = run(LAM, 2.0, 5.0, 1.0, xmax=XM, fun=lambda x, w=w: 1.0/(1.0-eps*w(x)))
        K.append((up-dn)/(2*eps))
    K = np.array(K); a = np.abs(K); cum = np.cumsum(a)/a.sum(); u = np.log(cen)
    pc = lambda p: float(np.exp(np.interp(p, cum, u)))
    gup = run(LAM, 2.0, 5.0, 1.0, xmax=XM, fun=lambda x: 1/(1+eps)); gdn = run(LAM, 2.0, 5.0, 1.0, xmax=XM, fun=lambda x: 1/(1-eps))
    return pc(0.05), pc(0.5), pc(0.95), pc(0.99), (gup-gdn)/(2*eps), K.sum()*du
for XM in [400.0, 4000.0, 40000.0]:
    p05, p50, p95, p99, G, Ki = window(XM)
    print(f"  xmax={XM:8.0f}: 5/50/95/99% at x = {p05:.1f}/{p50:.1f}/{p95:.1f}/{p99:.1f}; "
          f"decades(5-95) x = {math.log10(p95/p05):.2f}, time = {2*math.log10(p95/p05):.2f}; "
          f"decades(1-99..5-99) x = {math.log10(p99/p05):.2f}, time = {2*math.log10(p99/p05):.2f}; global resp {G:.3f}")

# ---------------- K3: A without shortcut
print("\nK3. direct Y-space integration (no Riccati shortcut), start x_i, ratio r")
def run_direct(xi, r, xmax=400.0):
    c = lambda x: LAM * x**(-2.0)
    def rhs(x, Y): return [-c(x)*(Y[0]**2 - Yeq(x)**2)]
    Y0 = r*Yeq(xi)
    sol = solve_ivp(rhs, (xi, xmax), [Y0], method="Radau", rtol=1e-11, atol=1e-30)
    return sol.y[0, -1] if sol.success else float('nan')
Yb = math.exp(lnY0)
for xi, r in [(2.0, 1e-3), (4.0, 1e-6), (8.0, 1e-6), (8.0, 1e3), (12.0, 1e3), (16.0, 1e-3), (20.0, 1e-3), (20.0, 1e3), (24.0, 1e-3), (24.0, 1e3)]:
    yv = run_direct(xi, r)
    print(f"  x_i={xi:5.1f} r={r:8.0e}: Y_inf/Y_base - 1 = {yv/Yb-1:+.3e}")
