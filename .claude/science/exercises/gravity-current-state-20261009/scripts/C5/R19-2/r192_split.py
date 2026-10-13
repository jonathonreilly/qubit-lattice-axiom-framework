#!/usr/bin/env python3
"""R19-2 [B]: the a-insertion mean source of the least-decoherence record noise, all four R15-2 channels.
Inputs:
  * per-mode coefficients tau_00, tau_kk (units pi/k^2) from r192_modes.out (independently recomputed; equal to R18-11's table);
  * R15-2's least-decoherence trade-off per frame mode (R15-2 [8], units 16 pi G = hbar = 1, k = 1):
       K = P^{-1}/4 + G P G,  G = exchange kernel of Lemma A in the channel variables:
       S block (rho, T_perp): [[(1-x^2)/2, 1/2], [1/2, 0]];  V (per component j_a): -2;  TT (per polarization t): 2/(1-x^2).
    1x1 least decoherence: P = 1/(2|G|).  S block: K_rr at its floor |g11| (family p1 = p2 g^2 + Delta, q = -p2 g,
    g = g12/g11, Delta = 1/(2|g11|)); p2 free (R15-2 'finite K_pp'); p2* = argmin K_pp ('complete split').
Output: per-mode tau_00, tau_kk in units of u0 := pi * (1x1 static rho floor) -- i.e. units of R15-2's per-mode u1.
Readings: (U) rho_act = tau_00 + tau_kk;  (P) rho_act = tau_kk;  FRW lift A late-time rho_n = -tau_kk/3 (r192_frw.py).
Subtraction: none.
"""
import sympy as sp, numpy as np
from scipy import optimize
x = sp.Symbol('x', positive=True); a = sp.Symbol('a'); p2 = sp.Symbol('p2', positive=True); r = sp.Symbol('r', positive=True)
# coefficients (units pi/k^2), r192_modes.out [A2] (== R18-11 table, rR18-11:166-171)
c00 = {'rr': 2*a*x**2 + 2*a - 3*x**2 - 7, 'rT': -a, 'TT_': 0, 'jj': 4, 'tt': 4*(x**2 + 1)/(x**2 - 1)**2}
ckk = {'rr': (x**2 + 1)*(2*a*x**2 - 4*x**2 - 1), 'rT': a*x**2 + 2*a - 2*x**2 - 2, 'TT_': -(a - 2), 'jj': -4,
       'tt': -4*(x**2 - 3)/(x**2 - 1)**2}

def totals(p1, q, pT, Pj, Pt, with_TT=True, with_V=True):
    t00 = c00['rr']*p1 + c00['rT']*q + c00['TT_']*pT + (2*c00['jj']*Pj if with_V else 0) + (2*c00['tt']*Pt if with_TT else 0)
    tkk = ckk['rr']*p1 + ckk['rT']*q + ckk['TT_']*pT + (2*ckk['jj']*Pj if with_V else 0) + (2*ckk['tt']*Pt if with_TT else 0)
    return sp.simplify(t00), sp.simplify(tkk)

print("[B1] numeric check of the S-block least-decoherence structure (minimize K_rr over PSD P, then K_pp at the K_rr floor)")
def Kmat(P, G): return 0.25*np.linalg.inv(P) + G @ P @ G
for xv in [0.0, 0.3, 0.7, 1.4, 2.5]:
    G = np.array([[(1 - xv**2)/2, 0.5], [0.5, 0.0]]); g11, g12 = G[0, 0], G[0, 1]
    def unpack(v):
        L = np.array([[np.exp(v[0]), 0], [v[1], np.exp(v[2])]]); return L @ L.T
    best = None
    for s in range(40):
        v0 = np.random.default_rng(s).normal(size=3)
        res = optimize.minimize(lambda v: Kmat(unpack(v), G)[0, 0], v0, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 20000})
        if best is None or res.fun < best.fun: best = res
    floor = best.fun
    # minimize K_pp subject to K_rr <= floor (penalty)
    cons = {'type': 'ineq', 'fun': lambda v: floor*(1 + 1e-9) - Kmat(unpack(v), G)[0, 0]}
    best2 = None
    for s in range(40):
        v0 = np.random.default_rng(100 + s).normal(size=3)
        res = optimize.minimize(lambda v: Kmat(unpack(v), G)[1, 1], v0, method='SLSQP', constraints=[cons], options={'ftol': 1e-14, 'maxiter': 2000})
        if res.success and (best2 is None or res.fun < best2.fun): best2 = res
    P = unpack(best2.x); gam = g12/g11; Dl = 1/(2*abs(g11)); p2s = abs(g11)/(2*g12**2)
    print("    x=%.1f: min K_rr = %.6f (|g11| = %.6f); at the floor min K_pp = %.6f; P = [[%.5f, %.5f], [., %.5f]]; formula p2* = %.5f, p1 = %.5f, q = %.5f"
          % (xv, floor, abs(g11), best2.fun, P[0, 0], P[0, 1], P[1, 1], p2s, p2s*gam**2 + Dl, -p2s*gam))

for region, sgn in (("x < 1 (spacelike)", 1), ("x > 1 (timelike)", -1)):
    one_m = sgn*(1 - x**2)              # = |1 - x^2|
    g11 = (1 - x**2)/2; g12 = sp.Rational(1, 2); gam = g12/g11; Dl = 1/(2*sgn*g11)
    Pj = sp.Rational(1, 4); Pt = one_m/4
    p2s = sp.simplify(sgn*g11/(2*g12**2))
    print("\n[B2] %s, full least-decoherence floor in every channel" % region)
    # complete split
    p1 = sp.simplify(p2s*gam**2 + Dl); q = sp.simplify(-p2s*gam)
    t00, tkk = totals(p1, q, p2s, Pj, Pt)
    print("    complete split (K_rr floor, K_pp minimal): p1 = %s, q = %s, p2 = %s, r = p2/p1 = %s" % (p1, q, p2s, sp.factor(p2s/p1)))
    print("      general a: tau_00/u0 = %s ; tau_kk/u0 = %s" % (sp.factor(t00), sp.factor(tkk)))
    print("      a = 2:     tau_00/u0 = %s ; tau_kk/u0 = %s ; (U) rho_act = %s" % (sp.simplify(t00.subs(a, 2)), sp.simplify(tkk.subs(a, 2)), sp.simplify((t00 + tkk).subs(a, 2))))
    print("      zero of tau_00 in a: a = %s ; zero of tau_kk in a: a = %s" % (sp.solve(t00, a), sp.solve(tkk, a)))
    # channel breakdown at a = 2
    br = {}
    br['rho'] = (sp.simplify((c00['rr']*p1).subs(a, 2)), sp.simplify((ckk['rr']*p1).subs(a, 2)))
    br['T_perp'] = (sp.simplify((c00['rT']*q + c00['TT_']*p2s).subs(a, 2)), sp.simplify((ckk['rT']*q + ckk['TT_']*p2s).subs(a, 2)))
    br['V (2)'] = (sp.simplify(2*c00['jj']*Pj), sp.simplify(2*ckk['jj']*Pj))
    br['TT (2)'] = (sp.simplify(2*c00['tt']*Pt), sp.simplify(2*ckk['tt']*Pt))
    for kk, v in br.items():
        print("      channel %-7s: tau_00/u0 = %-28s tau_kk/u0 = %s" % (kk, sp.factor(v[0]), sp.factor(v[1])))
    # R15-2's printed choice p2 = Delta
    p2R = Dl; p1R = sp.simplify(p2R*gam**2 + Dl); qR = sp.simplify(-p2R*gam)
    t00R, tkkR = totals(p1R, qR, p2R, Pj, Pt)
    print("    R15-2 printed choice p2 = Delta (r152_checks.py:268): a = 2: tau_00/u0 = %s ; tau_kk/u0 = %s" % (sp.factor(t00R.subs(a, 2)), sp.factor(tkkR.subs(a, 2))))
    print("      small-x series of tau_kk/u0 (a = 2):", sp.series(tkkR.subs(a, 2), x, 0, 5) if sgn == 1 else "n/a")
    # r-family (static notation of R18-11: r = p2/p1, q = -r g p1)
    p1r = sp.simplify(Dl/(1 - r*gam**2)); qr = sp.simplify(-r*p1r*gam); p2r = r*p1r
    t00r, tkkr = totals(p1r, qr, p2r, Pj, Pt)
    if sgn == 1:
        print("    r-family at x -> 0, a = 2: tau_00/u0 = %s ; tau_kk/u0 = %s ; zero of tau_kk at r = %s"
              % (sp.factor(t00r.subs(a, 2).subs(x, 0)), sp.factor(tkkr.subs(a, 2).subs(x, 0)), sp.solve(tkkr.subs(a, 2).subs(x, 0), r)))
        t00n, tkkn = totals(p1r, qr, p2r, Pj, Pt, with_TT=False)
        print("    R18-11's channel set (rho, T_perp, V; TT omitted), x -> 0, a = 2: tau_kk/u0 = %s ; FRW-A rho_n/u0 = -tau_kk/3 = %s"
              % (sp.factor(tkkn.subs(a, 2).subs(x, 0)), sp.factor(-tkkn.subs(a, 2).subs(x, 0)/3)))
        print("      (= R18-11's (1 + 2r + u_V/u1) u1/3 with u1 = u0/(1-r) and u_V = 2 u0: the V channel at its floor carries 2 u0)")
    # matrix-|G| choice for the S block: P = |G|^{-1}/2
print("\n[B3] matrix-|G| S-block choice P_S = |G_S|^{-1}/2 (K = |G_S|), numeric, a = 2, other channels at their floors:")
for xv in [0.0, 0.3, 0.7, 1.4, 2.5]:
    G = np.array([[(1 - xv**2)/2, 0.5], [0.5, 0.0]]); ev, U = np.linalg.eigh(G)
    absG = U @ np.diag(np.abs(ev)) @ U.T; P = 0.5*np.linalg.inv(absG)
    sub = {x: xv, a: 2}
    t00 = float(c00['rr'].subs(sub))*P[0, 0] + float(c00['rT'].subs(sub))*P[0, 1] + 2*4*0.25 + 2*float(c00['tt'].subs(sub))*abs(1 - xv**2)/4
    tkk = float(ckk['rr'].subs(sub))*P[0, 0] + float(ckk['rT'].subs(sub))*P[0, 1] + float(ckk['TT_'].subs(sub))*P[1, 1] - 2*4*0.25 + 2*float(ckk['tt'].subs(sub))*abs(1 - xv**2)/4
    print("    x=%.1f: K_rr = %.4f (floor %.4f); tau_00/u0 = %+.4f ; tau_kk/u0 = %+.4f" % (xv, Kmat(P, G)[0, 0], abs(G[0, 0]), t00, tkk))
