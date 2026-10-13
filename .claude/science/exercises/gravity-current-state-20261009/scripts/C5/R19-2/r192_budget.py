#!/usr/bin/env python3
"""R19-2 [D]: late-time FRW (lift A) noise density rho_n = -p_tot for the channel splits of r192_split.out, vs rho_Lambda,
over R15-2's window; matches; Mercury; precision.  Per-mode phase-space weight (R15-2 4.5(b), vR15-2:17):
   w(k, omega) = (hbar/4) e^{-k^2 l^2} |F_t(omega tau)|^2 / (2 pi)^4,  int d^3k d omega w = u0 = hbar I_F/(32 pi^{3/2} l^3 tau).
Constants as the R18-11 referee (r1811_referee_checks.py): H = 67.7 km/s/Mpc, rho_L = 0.69 rho_crit; Mercury 9.286e-15 kg/m^3.
Thresholds are recomputed here (bisection on exact integrals / closed forms); RECALLED inputs are labelled.
"""
import math, numpy as np
from scipy import integrate
hbar = 1.054571817e-34; G = 6.674e-11; c = 2.99792458e8
Hh = 67.7e3 / 3.0857e22; rho_crit = 3 * Hh**2 / (8 * math.pi * G); rho_L = 0.69 * rho_crit          # kg/m^3
eL = rho_L * c**2                                                                                     # J/m^3
IF = 21 / 32; tH = 4.35e17; c1 = math.log(8) + 0.5772156649 - 2
F2 = lambda y: (1 + 16 * y * y) / (1 + y * y)**4
u0 = lambda l, L: hbar * IF / (32 * math.pi**1.5 * l**3 * (L / c))                                 # J/m^3, L = c tau
print("[D0] rho_Lambda = %.6e kg/m^3 (%.6e J/m^3); u0/rho_L at the corner (5e-6, 1.49e-3) = %.9f [vR18-11 referee: 1.170953060]"
      % (rho_L, eL, u0(5e-6, 1.49e-3) / eL))
# check normalisation of w by direct integration at one point
l, L = 1e-6, 1e-5
tot = integrate.dblquad(lambda y, kk: 4 * math.pi * kk**2 * math.exp(-(kk * l)**2) * F2(y) * (hbar / 4) / (2 * math.pi)**4 * (c / L),
                        0, 8 / l, lambda kk: -60, lambda kk: 60, epsabs=0, epsrel=1e-7)[0]
print("     direct int w = %.6e vs u0 formula %.6e (F tail |y|>60 omitted: ~1e-8)" % (tot, u0(l, L)))

def U_IR(l, L):
    """int over |omega| > c k of w (timelike modes): (hbar/4)(4 pi/(2 pi)^4) int d omega |F|^2 int_0^{|omega|/c} k^2 e^{-k^2 l^2} dk."""
    def inner(y):          # y = omega tau; kmax = |y| / L
        kmax = abs(y) / L
        s = math.sqrt(math.pi) / (4 * l**3) * math.erf(kmax * l) - kmax * math.exp(-(kmax * l)**2) / (2 * l**2)
        return F2(y) * s
    v = 2 * integrate.quad(inner, 0, np.inf, limit=400, epsrel=1e-10)[0] * (c / L)
    return (hbar / 4) * 4 * math.pi / (2 * math.pi)**4 * v
cIR = 11 / (96 * math.pi**3)
print("\n[D1] complete split (all channels at the floor up to the cone): spacelike modes cancel exactly (r192_split [B2]);")
print("     timelike modes give (tau_00, tau_kk) = (4, -4) u per mode -> lift A: rho_n = (4/3) U_IR > 0, w = -1.")
print("     closed form l << c tau: U_IR = 11 hbar c/(96 pi^3 (c tau)^4); check exact/closed at l = 1e-9, c tau = 1e-4: %.8f"
      % (U_IR(1e-9, 1e-4) / (cIR * hbar * c / 1e-4**4)))
Lmatch = ((4 / 3) * cIR * hbar * c / eL)**0.25
print("     match (4/3) U_IR = rho_L (l -> 0): c tau = %.6e m" % Lmatch)
for l in [4e-10, 1e-8, 1e-6, 5e-6]:
    lo, hi = 1e-7, 1e-1
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if (4 / 3) * U_IR(l, mid) > eL: lo = mid
        else: hi = mid
    print("     l = %.0e m: (4/3)U_IR/rho_L at ceiling 1.49e-3 = %.3e ; strict (c tau = l) = %.3e ; match at c tau = %.6e m (c tau/l = %.3g)"
          % (l, (4 / 3) * U_IR(l, 1.49e-3) / eL, (4 / 3) * U_IR(l, l) / eL, hi, hi / l))
lowerR152 = {4e-10: 1.53e-3, 1e-9: 1.13e-3, 2e-9: 8.9e-4, 1e-8: 5.2e-4, 1e-6: 1.40e-4, 5e-6: 1.21e-4}
print("     R15-2's tau_c window lower end (TT budget under its bounded near-cone reading, rR15-2:220): min over l = %.2e m > %.2e m"
      % (min(lowerR152.values()), Lmatch))

print("\n[D2] near-cone TT radiation if the S block is NOT at its floor near the cone (R15-2's bounded interpolation, a reading):")
print("     the cancellation fails in the cone band; the TT on-shell content (rho_GW, R15-2 4.3, exact weight, ln(c k t_H) + c1)")
print("     contributes p = rho_GW/3, i.e. lift A rho_n -> -rho_GW/3 (bounded S-block band terms not included: reading).")
def rho_GW(l, L):
    f = lambda lk: (lambda kk: kk**4 * math.exp(-(kk * l)**2) * F2(kk * L) * (math.log(c * kk * tH) + c1))(math.exp(lk))
    return hbar * c / (2 * math.pi**3) * integrate.quad(f, math.log(1e-6 / L), math.log(30 / l), limit=400)[0]
for (l, L) in [(5e-6, 1.49e-3), (5e-6, 1.21e-4), (1e-8, 5.2e-4), (1e-9, 1.13e-3), (1e-9, Lmatch), (5e-6, Lmatch)]:
    g = rho_GW(l, L)
    print("     l = %.0e, c tau = %.3e: rho_GW/rho_L = %.3e ; -rho_GW/3 vs +(4/3)U_IR: %.3e vs %.3e rho_L"
          % (l, L, g / eL, -g / 3 / eL, (4 / 3) * U_IR(l, L) / eL))

print("\n[D3] R15-2's printed S-block choice p2 = Delta (rho, T_perp, V, TT at floors), quasi-static bulk:")
print("     tau_kk/u0 = -6 x^2 - 13 x^4 + ... (r192_split [B2]) -> lift A rho_n = 2<x^2> u0 + O(x^4); <x^2> = 2 (l/c tau)^2 <y^2>, <y^2> = 17/21 (exact)")
y2 = integrate.quad(lambda y: y * y * F2(y), -np.inf, np.inf)[0] / integrate.quad(F2, -np.inf, np.inf)[0]
print("     <y^2> numeric = %.8f (17/21 = %.8f)" % (y2, 17 / 21))
bulk = lambda l, L: 2 * 2 * (l / L)**2 * (17 / 21) * u0(l, L)
for l in [4e-10, 1e-9, 1e-8, 1e-6, 5e-6]:
    # match on the bulk term alone: rho_n = rho_L
    Lm = (2 * 2 * (17 / 21) * hbar * IF * c / (32 * math.pi**1.5) / (l * eL))**(1 / 3)
    print("     l = %.0e: bulk rho_n/rho_L at ceiling = %.3e ; bulk match at c tau = %.3e m ; R15-2 lower end %s"
          % (l, bulk(l, 1.49e-3) / eL, Lm, ("%.2e m" % lowerR152[l]) if l in lowerR152 else "n/a"))
lstar = 2 * 2 * (17 / 21) * hbar * IF * c / (32 * math.pi**1.5) / (eL * 1.49e-3**3)
print("     at the ceiling the bulk match is at l = %.3e m (window starts at 4e-10 m)" % lstar)

print("\n[D4] R18-11's channel set (TT omitted), floors, x -> 0: lift A rho_n = u0/(1 - r) >= u0 (r192_split [B2])")
print("     corner (5e-6, 1.49e-3): rho_n/rho_L >= %.6f ; |rho_act| = 2 rho_n >= %.6f rho_L  [reproduces R18-11's suggested formula with u_V = 2 u0]"
      % (u0(5e-6, 1.49e-3) / eL, 2 * u0(5e-6, 1.49e-3) / eL))
print("     with TT at its floor and r free: rho_n = (2r - 1)/(1 - r) u0; rho_n = rho_L needs r - 1/2 = y/(2(2 + y)), y = rho_L/u0:")
for (l, L) in [(5e-6, 1.49e-3), (1e-6, 1.49e-3), (1e-8, 1.49e-3), (4e-10, 1.49e-3), (5e-6, 5e-6)]:
    yv = eL / u0(l, L)
    print("       l = %.0e, c tau = %.2e: required r = %.12g (relative precision of r - 1/2 ~ %.1e)" % (l, L, 0.5 + yv / (2 * (2 + yv)), yv))

print("\n[D5] gamma-trade (P-r15c, price only): channel noise scaled by gamma_S, gamma_V, gamma_TT at x -> 0, complete split:")
print("     lift A rho_n = (4 gamma_S + 2 gamma_V - 6 gamma_TT) u0 / 3  (zero at gamma_S = gamma_V = gamma_TT); a match needs the")
print("     channel imbalance tuned to rho_L/u0 (1e-19 .. 0.85 across the window), e.g. at the corner gamma_TT = 1 - rho_L/(2 u0) = %.4f"
      % (1 - eL / (2 * u0(5e-6, 1.49e-3))))

print("\n[D6] Mercury (|rho_act| < 9.286e-15 kg/m^3, vR16-14:11): FRW lift A |rho_act| = 2 rho_n; at any rho_n = rho_L match: %.2e kg/m^3 (margin %.1e)"
      % (2 * rho_L, 9.286e-15 / (2 * rho_L)))
print("     complete split, flat (P): rho_act = tau_kk = -4 U_IR; at the ceiling |rho_act| <= %.2e kg/m^3 for every l in the window"
      % (4 * max(U_IR(l, 1.49e-3) for l in [4e-10, 5e-6]) / c**2))
print("     strict variant (c tau = l), complete split: |rho_act| = 4 U_IR(l, l)/c^2; Mercury crossing:")
lo, hi = 1e-10, 1e-5
for _ in range(80):
    mid = math.sqrt(lo * hi)
    if 4 * U_IR(mid, mid) / c**2 > 9.286e-15: lo = mid
    else: hi = mid
print("       |rho_act| > Mercury bound for l < %.4e m (strict)" % hi)
print("\n[D7] precision: lift A complete split fixes c tau alone: d(c tau)/(c tau) = (1/4) d rho_L/rho_L; l is not fixed.")
