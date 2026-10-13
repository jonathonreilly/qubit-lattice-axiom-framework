#!/usr/bin/env python3
"""R19-8 [S]: E2's least-decoherence split and the a = 2 noise source, all four channels.
Inputs:
 * r198_modes.out [M6-M8]: E2 per-mode coefficients = c_hh |G_gam|^2 + c_hJ Re G_gam, E1 limit = R19-2 table at a = 2.
 * R15-2/R19-2 trade-off K = P^{-1}/4 + G P G^dagger (units 16 pi G = hbar = k = 1); E1 channel kernels
   S block [[(1-x^2)/2, 1/2],[1/2, 0]], V: -2 (per component), TT: 2/(1-x^2) (per polarization).
 * E2 (harmonic gauge, friction on every component of hbar): every component carries the same propagator
   G_gam = 1/(k^2 - w^2 - i gam w), so every channel kernel is R * (E1 kernel), R = (1-x^2)/(1-x^2-i g x), g = gam/(c k).
Claims checked here: (1) Re R = |R|^2, so per-mode coefficients scale as |R|^2 * E1; (2) P_E2 = P_E1/|R|, K_E2 = |R| K_E1
(numeric optimisation over PSD P with complex G); (3) tau_E2 = |R| tau_E1 per mode, every channel and every split defined
on the E1 structure; Theorem I0 (spacelike zero at the complete split) carries over exactly; (4) near-cone integrals.
Subtraction: none.  Run: OMP_NUM_THREADS=2 python3 r198_split.py
"""
import numpy as np, sympy as sp
from scipy import optimize, integrate
x, g = sp.symbols('x g', positive=True)
R = (1 - x**2)/(1 - x**2 - sp.I*g*x)
print("[S1] Re R - |R|^2 =", sp.simplify(sp.re(sp.expand_complex(R)) - sp.Abs(R)**2 if False else
      sp.simplify(sp.expand_complex(sp.re(R)) - sp.expand_complex(R*sp.conjugate(R)))))
print("     |R|^2 =", sp.factor(sp.simplify(sp.expand_complex(R*sp.conjugate(R)))))
# E2 coefficient with p = Re G, q = -Im G: c_hh (p^2+q^2) + c_hJ p.  E1: p1 = 1/(1-x^2).  Ratio for any (c_hh, c_hJ):
G = 1/(1 - x**2 - sp.I*g*x); p = sp.re(sp.expand_complex(G)); q = -sp.im(sp.expand_complex(G))
p1 = 1/(1 - x**2)
chh, chJ = sp.symbols('c_hh c_hJ')
ratio = sp.simplify((chh*(p**2 + q**2) + chJ*p)/(chh*p1**2 + chJ*p1))
print("[S2] E2/E1 per-mode coefficient ratio for arbitrary (c_hh, c_hJ):", sp.factor(ratio))

print("\n[S3] numeric least-decoherence optimisation with complex kernel G = R*G1 (K = P^-1/4 + G P G^dagger):")
def unpack(v):
    L = np.array([[np.exp(v[0]), 0], [v[1], np.exp(v[2])]]); return L @ L.T
def Kmat(P, Gc): return 0.25*np.linalg.inv(P) + np.real(Gc @ P @ Gc.conj().T)
for xv, gv in [(0.3, 0.2), (0.9, 0.05), (0.99, 0.01), (1.02, 0.03), (1.5, 0.5)]:
    Rv = (1 - xv**2)/(1 - xv**2 - 1j*gv*xv)
    G1 = np.array([[(1 - xv**2)/2, 0.5], [0.5, 0.0]]); Gc = Rv*G1
    best = None
    for s in range(30):
        res = optimize.minimize(lambda v: Kmat(unpack(v), Gc)[0, 0], np.random.default_rng(s).normal(size=3), method='Nelder-Mead',
                                options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 20000})
        if best is None or res.fun < best.fun: best = res
    floor = best.fun
    cons = {'type': 'ineq', 'fun': lambda v: floor*(1 + 1e-9) - Kmat(unpack(v), Gc)[0, 0]}
    best2 = None
    for s in range(30):
        res = optimize.minimize(lambda v: Kmat(unpack(v), Gc)[1, 1], np.random.default_rng(100 + s).normal(size=3), method='SLSQP',
                                constraints=[cons], options={'ftol': 1e-14, 'maxiter': 2000})
        if res.success and (best2 is None or res.fun < best2.fun): best2 = res
    P = unpack(best2.x); aR = abs(Rv)
    sgn = 1 if xv < 1 else -1
    g11 = (1 - xv**2)/2; p2s = abs(g11)/(2*0.25); gam_ = 0.5/g11
    P1 = np.array([[p2s*gam_**2 + 1/(2*abs(g11)), -p2s*gam_], [-p2s*gam_, p2s]])   # E1 complete split
    print("    x=%.2f g=%.2f |R|=%.5f: K_rr floor %.6f vs |R||g11| %.6f ; min K_pp %.6f vs |R| K1_pp %.6f ; max|P*|R| - P1| = %.1e"
          % (xv, gv, aR, floor, aR*abs(g11), best2.fun, aR*Kmat(P1, G1)[1, 1], np.abs(P*aR - P1).max()))
    # 1x1 channels
    for lab, G1s in (("V", -2.0), ("TT", 2/(1 - xv**2))):
        r_ = optimize.minimize_scalar(lambda lp: 0.25*np.exp(-lp) + abs(Rv*G1s)**2*np.exp(lp), bounds=(-30, 30), method='bounded')
        print("        %-2s: P_E2*|R| = %.6f vs P_E1 = 1/(2|G1|) = %.6f" % (lab, np.exp(r_.x)*aR, 1/(2*abs(G1s))))

# per-mode totals at a = 2, complete split, units u0 (R19-2 [B2] closed forms times |R|)
print("\n[S4] a = 2, complete split, E2 = |R| x E1 per channel (R19-2 B:13-16, B:26 times |R|):")
xs = sp.Symbol('x', positive=True); gs = sp.Symbol('g', positive=True)
aR = sp.Abs(1 - xs**2)/sp.sqrt((1 - xs**2)**2 + gs**2*xs**2)
ch_sp = {'rho': (-2*(3 - xs**2)/(1 - xs**2), -2*(1 + xs**2)/(1 - xs**2)), 'T_perp': (2, -2), 'V(2)': (2, -2),
         'TT(2)': (2*(1 + xs**2)/(1 - xs**2), 2*(3 - xs**2)/(1 - xs**2))}
t00 = sum(v[0] for v in ch_sp.values()); tkk = sum(v[1] for v in ch_sp.values())
print("    spacelike: sum over channels (E1) tau_00 = %s, tau_kk = %s ; E2 = |R| x that = 0 for every g" % (sp.simplify(t00), sp.simplify(tkk)))
print("    timelike (E1, B:26): (4, -4) u0 per mode ; E2: |R| (4, -4) u0, |R| <= 1")
# near-cone band: TT channel alone and the total, E2 regulator
for gv in (1e-2, 1e-4, 1e-8, 1e-12):
    f_tt = lambda xv: float(aR.subs({xs: xv, gs: gv})) * float(ch_sp['TT(2)'][1].subs(xs, xv)) if xv != 1 else 0.0
    aRf = lambda xv: abs(1 - xv**2)/np.sqrt((1 - xv**2)**2 + gv**2*xv**2)
    ftt = lambda xv: aRf(xv)*2*(3 - xv**2)/(1 - xv**2)
    I_tt = integrate.quad(ftt, 0.5, 1.0, points=[1 - 10*gv], limit=400)[0]
    # timelike deficit of |R| near the cone: int_1^2 (1 - |R|) dx
    I_def = integrate.quad(lambda xv: 1 - aRf(xv), 1.0, 2.0, points=[1 + 10*gv], limit=400)[0]
    print("    g=%.0e: TT-only spacelike band int_0.5^1 tau_kk^TT dx = %.4f (~ 2 ln(1/g) + c: %.4f) ; channel total = 0 ; "
          "timelike deficit int_1^2 (1-|R|) dx = %.3e (g/2 = %.3e)" % (gv, I_tt, 2*np.log(1/gv), I_def, gv/2))
print("    => friction regulates the near-cone TT log (E1: age ln(ck t)); at the complete split the channels cancel inside the band too")
# physical size of g for record-noise modes
c = 2.998e8; H0 = 67.7e3/3.0857e22
for gH in (0.016, 0.047, 7.0):
    for ctau in (1.49e-3, 5e-6, 4e-10):
        print("    gamma = %.3g H0, c tau = %.2e m: g = gamma/(c k) at k = 1/(c tau): %.2e" % (gH, ctau, gH*H0/(c/ctau)))

# ---------------- [S5] E2 has no gauge freedom: is a = 2 still selected? harmonic-gauge totals at the complete split, general a ----------------
print("\n[S5] E2's readout gauge is harmonic by law (friction breaks gauge invariance), so Theorem G's selection is not available.")
print("     Harmonic-law per-mode coefficients (r198_modes.out [M8]: harmonic = Poisson + Delta, Delta prop. to (a-2)) at the complete split:")
a = sp.Symbol('a')
c00P = {'rr': 2*a*xs**2 + 2*a - 3*xs**2 - 7, 'rT': -a, 'TT_': 0, 'jj': 4, 'tt': 4*(xs**2 + 1)/(xs**2 - 1)**2}
ckkP = {'rr': (xs**2 + 1)*(2*a*xs**2 - 4*xs**2 - 1), 'rT': a*xs**2 + 2*a - 2*xs**2 - 2, 'TT_': -(a - 2), 'jj': -4,
        'tt': -4*(xs**2 - 3)/(xs**2 - 1)**2}
d00 = {'rr': -2*xs**2*(a - 2), 'rT': (a - 2)*(xs**2 + 1)/((xs - 1)*(xs + 1)), 'TT_': 0, 'jj': 0, 'tt': 0}
dkk = {'rr': -2*xs**4*(a - 2), 'rT': -xs**2*(a - 2)*(xs**2 - 3)/((xs - 1)*(xs + 1)), 'TT_': (a - 2)*(xs**2 + 1)/((xs - 1)*(xs + 1)), 'jj': 0, 'tt': 0}
for region, sgn in (("spacelike", 1), ("timelike", -1)):
    g11 = (1 - xs**2)/2; gm_ = sp.Rational(1, 2)/g11; Dl = 1/(2*sgn*g11); p2s = sp.simplify(sgn*g11/(2*sp.Rational(1, 4)))
    p1 = sp.simplify(p2s*gm_**2 + Dl); qq = sp.simplify(-p2s*gm_); Pj = sp.Rational(1, 4); Pt = sgn*(1 - xs**2)/4
    def tot(cd, dd):
        c = {kk: cd[kk] + dd[kk] for kk in cd}
        return sp.factor(sp.simplify(c['rr']*p1 + c['rT']*qq + c['TT_']*p2s + 2*c['jj']*Pj + 2*c['tt']*Pt))
    T00, Tkk = tot(c00P, d00), tot(ckkP, dkk)
    print("     %s: tau_00/u0 = %s ; tau_kk/u0 = %s ; zero at a = %s / %s" % (region, T00, Tkk, sp.solve(T00, a), sp.solve(Tkk, a)))
print("     IR check, rho^2 coefficient of tau_kk, harmonic law:", sp.factor(sp.expand(ckkP['rr'] + dkk['rr'])), "(no x^4 term for any a)")

# ---------------- [S6] the complete split inside the friction band: record-variance growth and the effect of a cap ----------------
print("\n[S6] E2 complete split: S-block powers P_E2 = P_E1/|R|.  rho power p1_E2 = 2 sqrt(D')/(1-x^2)^2, D' = (1-x^2)^2 + g^2 x^2:")
y = sp.Symbol('y', positive=True)
p1E2 = sp.simplify((2/sp.Abs(1 - xs**2)) / aR)
print("     p1_E2 =", sp.simplify(p1E2), "; near the cone (1-x^2 = y -> 0): ~", sp.limit(p1E2.subs(xs, sp.sqrt(1 - y))*y**2, y, 0), "/ y^2")
print("     => int dx p1_E2 near the cone with an age cutoff |1-x| > 1/(c k t): ~ g c k t / 4 = gamma t / 4 (power law), on top of E1's ln(c k t):")
for gt in (0.016, 0.047, 1.0, 100.0):
    print("        gamma t = %-6g: excess S-channel record variance (units of the per-shell floor) ~ %.3g" % (gt, gt/4))
print("     so under P-r14b (t >> 1/gamma) the complete split is not record-finite at the cone; a cap in the band is a new datum.")
# effect of a cap: inside |1-x^2| < g replace the S block by its band-edge value; uncancelled residual vs the TT near-cone total
def chan_kk(xv, gv, cap):
    one = 1 - xv**2; Dp = one**2 + gv**2*xv**2; aRv = abs(one)/np.sqrt(Dp)
    sgn = 1 if xv < 1 else -1
    # E1 complete-split rows (tau_kk) per channel, E2 = |R| x E1 when uncapped
    rho = (-2*(1 + xv**2)/one) if sgn == 1 else (-2*(xv**2 + 1)/(xv**2 - 1))
    Tp = -2 if sgn == 1 else 2
    V = -2
    TT = (2*(3 - xv**2)/one) if sgn == 1 else (-2*(xv**2 - 3)/(xv**2 - 1))
    S = rho + Tp
    if cap and abs(one) < gv:
        # S block held at its band-edge power: P_S(x_e)/|R(x_e)|, coefficient |R(x)|^2 c1(x); S row of E1 is c1*P1 -> scale
        xe = np.sqrt(1 - sgn*gv); onee = 1 - xe**2; aRe = abs(onee)/np.sqrt(onee**2 + gv**2*xe**2)
        # E1 rows are c1(x) P1(x); P1 ~ 1/|1-x^2| for rho, ~1 for the cross term: use P1(x_e)/P1(x) factor on rho, 1 on T_perp
        S = rho*(abs(one)/abs(onee))*(aRv**2/aRe)/aRv + Tp*(aRv**2/aRe)/aRv
    return aRv*(S + V + TT), aRv*TT
for gv in (1e-3, 1e-5, 1e-7):
    xs_ = np.concatenate([np.linspace(0.5, 1 - 50*gv, 4000), 1 - np.logspace(np.log10(50*gv), np.log10(gv*1e-4), 4000),
                          1 + np.logspace(np.log10(gv*1e-4), np.log10(50*gv), 4000), np.linspace(1 + 50*gv, 1.5, 4000)])
    xs_ = np.unique(xs_); xs_ = xs_[np.abs(xs_ - 1) > 1e-15]
    tot_u = np.array([chan_kk(v, gv, False)[0] for v in xs_]); tot_c = np.array([chan_kk(v, gv, True)[0] for v in xs_])
    tt = np.array([chan_kk(v, gv, False)[1] for v in xs_])
    I_u, I_c, I_tt = np.trapezoid(tot_u, xs_), np.trapezoid(tot_c, xs_), np.trapezoid(tt, xs_)
    print("     g=%.0e: int_0.5^1.5 tau_kk dx: uncapped %.4f (timelike -4|R| only: %.4f) ; capped %.4f ; residual %.4f ; TT-only (trapezoid, coarse) %.1f ; leading-log TT 4 ln(2/g) = %.1f ; residual/(4 ln(2/g)) = %.3f"
          % (gv, I_u, -4*0.5, I_c, I_c - I_u, I_tt, 4*np.log(2/gv), (I_c - I_u)/(4*np.log(2/gv))))
for gv in (1.7e-31, 5e-31, 2e-35):
    print("     extrapolated to record-noise g = %.1e: residual/(4 ln(2/g)) = %.4f" % (gv, 2.3115/(4*np.log(2/gv))))
