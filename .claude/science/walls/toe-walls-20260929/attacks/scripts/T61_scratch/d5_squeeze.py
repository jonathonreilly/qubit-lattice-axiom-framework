#!/usr/bin/env python3
"""T61 D5: arithmetic squeeze. P6 T8 bridge (hop = hbar c/a, GR normalisation alpha/wbar = 1/(64 pi G)):
   m_g^2 = 32 pi G |c| / a^4  ->  m_g = sqrt(32 pi |c|) * l_P / a^2   (natural units)
Reference inputs (not derived here): LVK GWTC-3 dispersion bound m_g < 1.27e-23 eV; H0 ~ 1.5e-33 eV;
matter-sector quadratic Lorentz-violation bound E_QG2 >~ 1e11 GeV (Fermi-LAT GRB, Vasileiou et al. 2013) -> a <~ 2e-27 m (reading).
"""
import numpy as np
lP = 1.616255e-35       # m
hbarc = 1.973270e-7     # eV m
mLVK = 1.27e-23; H0 = 1.5e-33
c = 0.109
pref = np.sqrt(32 * np.pi * c) * lP * hbarc      # eV m^2
def mg(a): return pref / a**2
print("m_g(a) = %.3e eV m^2 / a^2" % pref)
for a in (lP, 1e-30, 1e-27, 1e-19, 1e-15, 1e-10, 1e-9):
    m = mg(a)
    print("a=%.2e m  m_g=%.3e eV   need |c| suppressed by %.1e (mass bound, c>0)   by %.1e (Hubble yardstick, c<0)" % (a, m, (mLVK / m)**2, (H0 / m)**2))
amin = np.sqrt(pref / mLVK)
print("untuned pass of the LVK bound needs a >= %.2e m" % amin)
aLIV = 1.973270e-16 / 1e11   # hbarc[GeV m]/E_QG2
print("matter-sector quadratic LIV reference: a <~ %.1e m ; gap to a_min = %.1f orders of magnitude" % (aLIV, np.log10(amin / aLIV)))
print("at a = a_LIV: needed suppression of c = %.1e" % ((aLIV / amin) ** 4))
