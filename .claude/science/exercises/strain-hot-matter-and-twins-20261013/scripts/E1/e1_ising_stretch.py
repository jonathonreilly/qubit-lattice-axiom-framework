#!/usr/bin/env python3
"""E1 (A) and (D) for the 2D Ising model, exact (Onsager), using the free-fermion law
verified on strips in e1_ising_tm.out.

Exact inputs (disordered phase, Kx < Ky*):
  xi_y = 1 / (2 (Ky* - Kx)),  xi_x = 1 / (2 (Kx* - Ky)),  tanh K* = exp(-2K)
  (xi_y = 1/eps(0) of the y-transfer matrix; xi_x by the x<->y symmetry.)
Mass shell: D(q) = cosh2Kx cosh2Ky - sinh2Kx cos qx - sinh2Ky cos qy (Onsager's kernel).
Decay rate of the D-propagator along unit n: support function of the region
  R = {kappa : sinh2Kx cosh kx + sinh2Ky cosh ky < cosh2Kx cosh2Ky}.
Memory: 1D arrays only (<= 2e6 doubles).
"""
import numpy as np
from scipy.optimize import brentq

Kc = 0.5 * np.arcsinh(1.0)
def dual(K): return np.arctanh(np.exp(-2.0 * K))
def xis(Kx, Ky):
    return 1.0 / (2 * (dual(Kx) - Ky)), 1.0 / (2 * (dual(Ky) - Kx))
def crit(Kx, Ky): return np.sinh(2 * Kx) * np.sinh(2 * Ky)

def eps(q, Kx, Ky):
    Ks = dual(Ky)
    return np.arccosh(np.cosh(2 * Ks) * np.cosh(2 * Kx) - np.sinh(2 * Ks) * np.sinh(2 * Kx) * np.cos(q))
def lnZ(Kx, Ky, N=1000000):
    q = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    return 0.5 * np.log(2 * np.sinh(2 * Ky)) + 0.5 * eps(q, Kx, Ky).mean()

def support_aniso(Kx, Ky, nth=2001):
    """Support function of R in coordinates rescaled by the exact axis xi's; returns
    h(45deg)/h(0) - 1 and (max-min)/mean over directions (rescaled frame)."""
    sx, sy, C = np.sinh(2 * Kx), np.sinh(2 * Ky), np.cosh(2 * Kx) * np.cosh(2 * Ky)
    kxmax = np.arccosh((C - sy) / sx)
    # boundary parametrised by kx in [-kxmax, kxmax]; ky = arccosh((C - sx cosh kx)/sy)
    u = np.linspace(-1, 1, 400001)
    kx = kxmax * np.sin(0.5 * np.pi * u)                 # cluster points near the ends
    arg = np.maximum((C - sx * np.cosh(kx)) / sy, 1.0)
    ky = np.arccosh(arg)
    xix, xiy = xis(Kx, Ky)
    X, Y = kx * xix, ky * xiy                            # rescaled: axis rates become 1
    th = np.linspace(0, 0.5 * np.pi, nth)
    h = np.array([np.max(X * np.cos(a) + Y * np.sin(a)) for a in th])
    return h[nth // 2] / h[0] - 1.0, (h.max() - h.min()) / h.mean(), h[0], h[-1]

if __name__ == "__main__":
    print(f"Kc = {Kc:.15f};  2*sqrt2*Kc^2 = {2*np.sqrt(2)*Kc**2:.12f}")
    # ---------------- (a) covariance: xi ratio vs the metric ratio --------------------
    print("\n(a1) exact xi_x/xi_y vs metric ratio sqrt(sinh2Kx/sinh2Ky), off-critical, stretch Kx=K(1+t),Ky=K(1-t)")
    print("  t      xi_bar(t=0)   xi_x      xi_y     ratio_exact  ratio_metric  rel.dev   dev*xi^2")
    for t in (0.02, 0.05, 0.1):
        for xi0 in (5.0, 20.0, 80.0, 320.0):
            K = brentq(lambda K: xis(K, K)[0] - xi0, 0.05, Kc - 1e-14)
            Kx, Ky = K * (1 + t), K * (1 - t)
            if crit(Kx, Ky) >= 1: continue
            xx, xy = xis(Kx, Ky)
            rm = np.sqrt(np.sinh(2 * Kx) / np.sinh(2 * Ky))
            d = (xx / xy) / rm - 1
            print(f"  {t:.2f}  {xi0:9.1f}  {xx:9.3f} {xy:9.3f}  {xx/xy:.8f}  {rm:.8f}  {d:+.3e}  {d*np.sqrt(xx*xy)**2:+.4f}")
    print("\n(a2) mass-shell isotropy in the frame rescaled by the exact xi_j (D-propagator decay rates)")
    print("  Kx       Ky       xi_x     xi_y     h45/h0-1     (max-min)/mean   x xi_bar^2")
    for (Kx0, t) in ((None, 0.1), (None, 0.3)):
        for xi0 in (3.0, 10.0, 30.0, 100.0):
            # choose the anisotropic pair at fixed stretch ratio Kx/Ky=(1+t)/(1-t) with xi_bar = xi0
            r = (1 + t) / (1 - t)
            f = lambda K: np.sqrt(np.prod(xis(K * r, K))) - xi0
            Ky = brentq(f, 0.02, 0.999999 * brentq(lambda K: crit(K * r, K) - 1, 0.05, 1.0))
            Kx = Ky * r
            a45, amm, h0, h90 = support_aniso(Kx, Ky)
            xx, xy = xis(Kx, Ky)
            print(f"  {Kx:.5f}  {Ky:.5f}  {xx:8.3f} {xy:8.3f}  {a45:+.4e}  {amm:.4e}   {amm*xx*xy:.4f}   (h0={h0:.6f}, h90={h90:.6f})")
    # ---------------- (b) tuned gap under stretch ----------------------------------------
    print("\n(b1) at criticality K=Kc: stretch opens a gap; m = 1/sqrt(xi_x xi_y) (lattice units)")
    print("  param      t        sinh2Kx*sinh2Ky   m_x=1/xi_x     m_y=1/xi_y    m/t^2")
    for name, fx, fy in (("linear", lambda t: Kc * (1 + t), lambda t: Kc * (1 - t)),
                         ("expon ", lambda t: Kc * np.exp(t), lambda t: Kc * np.exp(-t))):
        for t in (0.1, 0.03, 0.01, 0.003, 0.001):
            Kx, Ky = fx(t), fy(t)
            c = crit(Kx, Ky)
            if c < 1:
                mx, my = 1 / xis(Kx, Ky)[0], 1 / xis(Kx, Ky)[1]
                print(f"  {name}  {t:.3f}  {c:.12f}   {mx:.6e}   {my:.6e}   {np.sqrt(mx*my)/t**2:.6f}  (disordered)")
            else:
                # ordered side: distance to criticality via the signed eps(0); xi = 1/(2 eps0)
                e0y = 2 * (Kx - dual(Ky)); e0x = 2 * (Ky - dual(Kx))
                print(f"  {name}  {t:.3f}  {c:.12f}   2e0x={2*e0x:.6e} 2e0y={2*e0y:.6e}   {np.sqrt(4*e0x*e0y)/t**2:.6f}  (ordered; m=2|eps0|)")
    print("  analytic (linear): Ky* - Kx = sqrt2*Kc^2 t^2 + O(t^3) => m = 2 sqrt2 Kc^2 t^2 =", f"{2*np.sqrt(2)*Kc**2:.10f} t^2")
    print("  analytic (expon ): Ky* - Kx = Kc t^2 (sqrt2 Kc - 1)  => ordered side, |eps0| coefficient", f"{2*Kc*abs(np.sqrt(2)*Kc-1):.10f}")
    print("\n(b2) off-critical start (xi0 = 1/m0), linear stretch: is delta m set by the lattice or by xi0?")
    print("  xi0       delta m / t^2 (t=1e-3)   delta m/(m0 t^2) = relative shift per t^2")
    for xi0 in (10.0, 100.0, 1000.0, 10000.0):
        K = brentq(lambda K: xis(K, K)[0] - xi0, 0.05, Kc - 1e-15)
        m0 = 1 / xi0
        t = 1e-3
        xx, xy = xis(K * (1 + t), K * (1 - t))
        dm = 1 / np.sqrt(xx * xy) - m0
        print(f"  {xi0:8.0f}   {dm/t**2:.8f}               {dm/(m0*t**2):.4e}")
    print("\n(b3) the tuned flow along Onsager's curve: sinh2Kx = s e^u, sinh2Ky = s e^-u (keeps crit = s^2)")
    for s in (1.0, 0.999, 0.99):
        for u in (0.0, 0.1, 0.3):
            Kx, Ky = 0.5 * np.arcsinh(s * np.exp(u)), 0.5 * np.arcsinh(s * np.exp(-u))
            if s < 1:
                xx, xy = xis(Kx, Ky); m = 1 / np.sqrt(xx * xy)
                print(f"  s={s} u={u}: crit={crit(Kx,Ky):.12f}  m = {m:.8e}  (Kx,Ky)=({Kx:.6f},{Ky:.6f})")
            else:
                print(f"  s={s} u={u}: crit={crit(Kx,Ky):.15f}  gapless (Kx,Ky)=({Kx:.6f},{Ky:.6f})")
    # the response the neighbour rule would need: K_j(t) on the curve, expanded
    print("  needed response to stay critical with Kx = Kc(1+t): Ky = Kx* ; Ky/Kc - 1 + t =")
    for t in (0.1, 0.01, 0.001):
        Ky = dual(Kc * (1 + t))
        print(f"    t={t}: (Ky/Kc - (1-t))/t^2 = {(Ky/Kc - (1 - t))/t**2:.8f}  (sqrt2*Kc = {np.sqrt(2)*Kc:.8f})")
    # ---------------- (D) fabric stretch stiffness at criticality ----------------------
    print("\n(D) d^2 lnZ/dt^2 per site at t=0 (central differences, N=1e6 midpoint), at K=Kc")
    for name, fx, fy in (("linear  Kx=Kc(1+t)   ", lambda t: Kc * (1 + t), lambda t: Kc * (1 - t)),
                         ("expon   Kx=Kc e^t     ", lambda t: Kc * np.exp(t), lambda t: Kc * np.exp(-t)),
                         ("onsager sinh2Kx=e^t   ", lambda t: 0.5 * np.arcsinh(np.exp(t)), lambda t: 0.5 * np.arcsinh(np.exp(-t)))):
        out = []
        for h in (0.04, 0.02, 0.01):
            d2 = (lnZ(fx(h), fy(h)) + lnZ(fx(-h), fy(-h)) - 2 * lnZ(fx(0), fy(0))) / h**2
            out.append(d2)
        print(f"  {name}: h=0.04 {out[0]:+.8f}  h=0.02 {out[1]:+.8f}  h=0.01 {out[2]:+.8f}")
    print("  same at K = 0.8 Kc (disordered) and 1.2 Kc (ordered), linear param:")
    for K in (0.8 * Kc, 1.2 * Kc):
        h = 0.01
        d2 = (lnZ(K * (1 + h), K * (1 - h)) + lnZ(K * (1 - h), K * (1 + h)) - 2 * lnZ(K, K)) / h**2
        print(f"    K={K:.5f}: d2 lnZ/dt2 = {d2:+.8f}")
