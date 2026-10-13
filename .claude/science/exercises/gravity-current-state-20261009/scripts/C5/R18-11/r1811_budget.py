#!/usr/bin/env python3
"""R18-11 [5]-[7]: spectral averages of the per-mode coefficients of r1811_modes.out, and the budget against rho_Lambda.
Per-mode coefficients (units: per-mode u1 = pi rho^2/k^2 of the rho channel; x = w/(c k)), Poisson law (r1811_modes.out [3]-[4]):
  rho channel:   tau_00 = 2a(1+x^2) - 7 - 3x^2 ;  tau_kk = (1+x^2)(2(a-2)x^2 - 1)
  T_perp:        tau_00 += -a q ;  tau_kk += ((a-2)(x^2+2) + 2) q - (a-2) r ,  q = <rho T>/<rho^2>, r = <T^2>/<rho^2>
  V:             tau_00 += +uV ;  tau_kk += -uV  (uV = V-channel field energy in the same units)
Readings: (U) stationary S/V noise with its homogeneous energy present from the start: rho_act = tau_00 + tau_kk.
          (P) noise switched on from zero at t0 with exact flat conservation (Pi): <tau_00> pinned to 0, rho_act = tau_kk.
Weights over modes (u = k l, v = w tau, s = c tau / l, x = v/(u s)):
  W1 = u^2 exp(-u^2) |F_t(v)|^2   (R15-2's u1 normalization, quasi-static response)
  W2 = W1 / |1 - x^2|             (exact least-decoherence rho-rho floor 4 pi G |k^2 - w^2|/k^4; log-integrable at the cone)
Subtraction: none.  OMP_NUM_THREADS=2.
"""
import numpy as np
from scipy import integrate
Ft2 = lambda v: (1 + 16*v**2)/(1 + v**2)**4

def moments(s, weight, umin=1e-6, delta=1e-2):
    """<x^n> for n = 0, 2, 4 under the weight, normalised to the W1 total (R15-2's u1). Nested quad, breakpoints at the cone."""
    Fv = [integrate.quad(lambda v: v**n*Ft2(v), 0, np.inf, epsabs=0, epsrel=1e-12, limit=400)[0] for n in (0, 2, 4)]
    norm1 = 2*Fv[0]*integrate.quad(lambda u: u**2*np.exp(-u**2), 0, np.inf)[0]
    out = []
    for n in (0, 2, 4):
        if weight == 1:
            val = 2*Fv[n//2]/s**n*integrate.quad(lambda u: u**(2-n)*np.exp(-u**2), umin, np.inf, limit=400)[0]
        else:
            def inner(u):
                vc = u*s
                f = lambda v: Ft2(v)*(v/vc)**n/max(abs(1 - (v/vc)**2), delta)
                a1 = integrate.quad(f, 0, vc, limit=400, epsabs=0, epsrel=1e-8)[0]
                a2 = integrate.quad(f, vc, 2*vc + 5, limit=400, epsabs=0, epsrel=1e-8)[0]
                a3 = integrate.quad(f, 2*vc + 5, np.inf, limit=400, epsabs=0, epsrel=1e-8)[0]
                return 2*(a1 + a2 + a3)
            lu = np.linspace(np.log(umin), np.log(8.0), 500)
            uu = np.exp(lu)
            vals = np.array([inner(u)*u**2*np.exp(-u**2)*u for u in uu])     # d u = u d ln u
            val = np.trapezoid(vals, lu)
        out.append(val/norm1)
    return tuple(out)

print("[5] mode averages of x = w/(ck) (subtraction: none; normalised to the W1 total, i.e. to R15-2's u1)")
res = {}
for lab, s in (("strict, c tau = l", 1.0), ("tau_c, c tau/l = 10", 10.0), ("tau_c, c tau/l = 300 (l = 5e-6, ceiling)", 1.49e-3/5e-6)):
    for wgt, umin, dl in ((1, 1e-3, 0), (1, 1e-4, 0), (2, 1e-4, 1e-2), (2, 1e-4, 1e-4)):
        m0, m2, m4 = moments(s, wgt, umin, dl)
        res[(lab, wgt, umin, dl)] = (m0, m2, m4)
        print("    %-42s W%d  u_min=%.0e delta=%.0e: <1> = %.4f  <x^2> = %.4e  <x^4> = %.4e" % (lab, wgt, umin, dl, m0, m2, m4))
print("    (W1: <x^4> grows as 1/u_min -- the far-off-cone IR region. W2 = W1/max(|1-x^2|, delta): the exact rho-rho floor is log-divergent at the cone,\n     so W2 needs the cone regulator delta (R15-2:126 'bounded choice near the cone'); its <1> grows as ln(1/delta).)")

print("\n[6] active density at the gauge-independent insertion a = 2 (units u1; T_perp ratios q = -r <= 0 anticorrelated, R15-2:125)")
for (lab, wgt, umin, dl), (m0, m2, m4) in res.items():
    if umin != 1e-4:
        continue
    U = -4*m0                                   # (U): exactly -4 per mode, independent of x, T_perp and V
    for r in (0.0, 0.5, 1.0):
        P = -(m0 + m2) + 2*(-r)*m0              # (P): tau_kk = -(1+x^2) + 2 q, q = -r ; V adds -uV
        print("    %-42s W%d d=%.0e r=%.1f: (U) rho_act = %+.4f u1 ; (P) rho_act = %+.4f u1 - uV" % (lab, wgt, dl, r, U, P))

print("\n    zeros away from a = 2 (rho channel; u_min = 1e-4; the a != 2 x^4 terms are IR-sensitive under W1):")
for (lab, wgt, umin, dl), (m0, m2, m4) in res.items():
    if umin != 1e-4:
        continue
    # (U): <2a(1+x^2)^2 - 4(2+2x^2+x^4)> = 0
    aU = 2*(2*m0 + 2*m2 + m4)/(m0 + 2*m2 + m4)
    # (P): <(1+x^2)(2(a-2)x^2 - 1)> = 0  ->  a = 2 + <1+x^2>/(2<x^2+x^4>)
    aP = 2 + (m0 + m2)/(2*(m2 + m4))
    resid4 = 8*m2 + 4*m4      # (U) residual at a = 4
    print("    %-42s W%d d=%.0e: (U) a* = %.4f (static 4) ; residual at a = 4: %+.3e u1 ; (P) a* = %.4g" % (lab, wgt, dl, aU, resid4, aP))
print("    static T_perp shift (U): a* = (4 - 2r)/(1 - r): r = 0 -> 4, 0.25 -> %.3f, 0.5 -> %.3f (dust value 6)" % ((4-0.5)/0.75, (4-1)/0.5))
print("    static (P) with T_perp and V: rho_act/u1 = -1 - r(3a - 4) - uV/u1; zero only for a < 4/3 with r = (1 + uV/u1)/(4 - 3a)")

print("\n[7] budget: |u1| = hbar I_F/(32 pi^1.5 l^3 tau), I_F = 21/32 (vR15-2:17); window l in [4e-10, 5e-6] m (vR6-4 (i)); tau strict l/c or tau_c <= 1.49e-3 m / c")
hbar = 1.054571817e-34; G = 6.674e-11; c = 2.99792458e8
H0 = 67.7e3/3.0857e22; rho_L = 0.69*3*H0**2/(8*np.pi*G)
def u1(l, ctau):
    return hbar*(21/32)/(32*np.pi**1.5*l**3*(ctau/c))/c**2
print("    rho_L = %.4e kg/m^3" % rho_L)
for l in (4e-10, 1e-8, 5e-8, 1e-6, 3.65e-6, 5e-6):
    a_s = u1(l, l)/rho_L; a_c = u1(l, 1.49e-3)/rho_L
    print("    l = %.2e m: u1/rho_L strict = %.3e ; at tau_c ceiling = %.3e ; a=2 (U) |rho_act|/rho_L >= %.3e ; a=2 (P) >= %.3e"
          % (l, a_s, a_c, 4*a_c, a_c))
print("    minimum over the window (l = 5e-6 m, c tau_c = 1.49e-3 m): u1/rho_L = %.4f" % (u1(5e-6, 1.49e-3)/rho_L))
# FRW attractor reading (suggested): rho_tot -> -p_s = -tau_kk/3, w = -1
l_eq = 5e-6*(u1(5e-6, 1.49e-3)/rho_L/3)**(1/3)
print("    (P)+FRW attractor (suggested): rho_noise -> -tau_kk/3 = (1 + <x^2> + 2r + uV/u1) u1/3 with w = -1;")
print("      rho-only, tau_c ceiling: equals rho_L at l = %.3e m ; strict variant would need l = %.2e m (outside the window)"
      % (l_eq, 5e-6*(u1(5e-6, 5e-6)/rho_L/3)**0.25))
print("      gamma-trade (P-r15c) needed for |rho_act| < rho_L at a = 2 (U): gamma <= rho_L/(4 u1) = %.1e (l = 4e-10, ceiling) ... %.2f (l = 5e-6, ceiling)"
      % (rho_L/(4*u1(4e-10, 1.49e-3)), rho_L/(4*u1(5e-6, 1.49e-3))))

print("\n[7b] local test: Mercury |rho_act| < 9.286e-15 kg/m^3 (vR16-14:11) at a = 2; (U) |rho_act| = 4 u1, (P) >= (1 + <x^2>) u1 (W1: <x^2> = 1.62 strict, ~0 at the tau_c ceiling)")
merc = 9.286e-15
from scipy.optimize import brentq
for lab, fac_s, fac_c in (("(U)", 4.0, 4.0), ("(P)", 2.62, 1.0)):
    ls = brentq(lambda l: fac_s*u1(l, l) - merc, 1e-11, 1e-5)
    lc = brentq(lambda l: fac_c*u1(l, 1.49e-3) - merc, 1e-12, 1e-5)
    print("    %s: Mercury fails for l < %.2e m (strict) and l < %.2e m (tau_c ceiling)" % (lab, ls, lc))
