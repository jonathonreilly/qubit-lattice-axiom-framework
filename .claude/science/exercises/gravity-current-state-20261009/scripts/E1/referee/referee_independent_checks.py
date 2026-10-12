"""Independent analytic/numeric checks for the E1 referee report.

This file does not import the worker scripts.  It rederives the small-epsilon
row-norm coefficient from factorial-moment identities, quantifies the SMAX
tail, and compares the short evolution/window sequences with simple fits.
"""

from math import comb, factorial, gamma, log, pi, sqrt

import mpmath as mp
import numpy as np


mp.mp.dps = 50


def g4(s):
    return mp.exp(-s) * (1 - 9 * s + 8 * s**2 - mp.mpf(4) * s**3 / 3)


def gain_coefficient_exact(eps):
    """Return lim_{T->inf} A^2/(eps*T^2) at fixed eps.

    If N~Poisson(m), E[z^N N_(r)] = (m z)^r exp(m(z-1)).
    The product identity
      N_(i) N_(j) = sum_k C(i,k) C(j,k) k! N_(i+j-k)
    makes the m integral elementary.  Here rho_k=1 and rho=1/eps.
    """

    e = mp.mpf(eps)
    q = 1 - e
    aa = [mp.mpf(1), mp.mpf(-9), mp.mpf(8), -mp.mpf(4) / 3]
    decay = 1 - q**2
    integral = mp.mpf(0)
    for i, ai in enumerate(aa):
        for j, aj in enumerate(aa):
            pref = e**2 * ai * aj * e ** (i + j) / q ** (i + j)
            for k in range(min(i, j) + 1):
                r = i + j - k
                coeff = comb(i, k) * comb(j, k) * factorial(k)
                # E[(eps f(N))^2] contains exp(-decay*m)*(m*q^2)^r.
                integral += (
                    pref
                    * coeff
                    * q ** (2 * r)
                    * mp.gamma(mp.mpf(r) + mp.mpf("0.5"))
                    / decay ** (mp.mpf(r) + mp.mpf("0.5"))
                )
    # d^4y asymptotically gives (pi/2) T^2 tau d tau; changing
    # m=rho*pi*tau^4/24 contributes the indispensable Jacobian 1/4.
    a = mp.pi / 24
    a2_over_t2 = (mp.pi / 8) * mp.sqrt((1 / e) / a) * integral
    return a2_over_t2 / e


I_inf = mp.quad(lambda u: g4(u) ** 2 / mp.sqrt(u), [0, 1, 5, 20, mp.inf])
C_inf = (mp.pi / 8) * mp.sqrt(24 / mp.pi) * I_inf
print("small-epsilon integral =", mp.nstr(I_inf, 18))
print("correct C_inf=A^2/(eps*T^2) =", mp.nstr(C_inf, 18))
for e in [0.2, 0.1, 0.05, 0.01, 0.001]:
    c = gain_coefficient_exact(e)
    print(
        f"eps={e:7g} exact coefficient={float(c):.9f} "
        f"ratio_to_limit={float(c/C_inf):.6f}"
    )


SMAX = mp.mpf(24)
prefactor = (mp.pi / 8) * mp.sqrt(24 / mp.pi)
mean_tail = prefactor * mp.quad(lambda s: g4(s) / mp.sqrt(s), [SMAX, mp.inf])
gain_tail = prefactor * mp.quad(lambda s: g4(s) ** 2 / mp.sqrt(s), [SMAX, mp.inf])
print("SMAX=24 asymptotic omitted mean row-sum coefficient times T^2 =", mp.nstr(mean_tail, 12))
print("SMAX=24 omitted continuum gain coefficient times eps*T^2 =", mp.nstr(gain_tail, 12))
print("SMAX=24 omitted gain fraction =", mp.nstr(gain_tail / C_inf, 12))


def fits(name, x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ly = np.log(y)
    exp_coef = np.polyfit(x, ly, 1)
    pow_coef = np.polyfit(np.log(x), ly, 1)
    exp_rss = float(np.sum((ly - np.polyval(exp_coef, x)) ** 2))
    pow_rss = float(np.sum((ly - np.polyval(pow_coef, np.log(x))) ** 2))
    print(
        f"{name}: exp_rate={exp_coef[0]:.5f}, exp_logRSS={exp_rss:.6g}; "
        f"power={pow_coef[0]:.5f}, power_logRSS={pow_rss:.6g}"
    )


fits("evolution eps=.2 E1_6", [4.5, 5.5, 6.5, 7.5, 8.5], [0.4975, 0.9653, 2.2169, 4.7519, 8.8540])
fits("evolution eps=.2 E1_5", [4.5, 5.5, 6.5, 7.0], [0.5565, 1.1813, 2.5594, 3.6108])
fits("evolution eps=.1 E1_5", [4.5, 5.5, 6.5], [0.2418, 0.3703, 0.5999])
fits("evolution eps=.05 E1_5", [4.5, 5.5, 6.5], [0.1735, 0.2701, 0.3912])

fits("window eps=.2 E1_3B", [0.4, 0.6, 0.8, 1.0, 1.3], [1.3291, 0.6767, 0.5505, 0.4054, 0.1837])
fits("window eps=.1 E1_3B", [0.4, 0.6, 0.8, 1.0], [0.6314, 0.3145, 0.2396, 0.1881])
fits("window eps=.2 E1_6", [1.0, 1.4, 1.8, 2.2], [0.3595, 0.1757, 0.1253, 0.0505])


strain_s = np.array([1e-5, 1e-4, 1e-3, 1e-2, 1e-1])
strain_sd = np.array([0.0224, 0.1167, 0.2492, 0.7880, 2.9637])
strain_fit = np.polyfit(np.log(strain_s), np.log(strain_sd), 1)
print(f"strain sd exponent over all five points = {strain_fit[0]:.5f}")


tau = np.array([6.75, 9.25, 12.25, 14.75])
var = np.array([17.478, 36.850, 65.383, 96.374])
var_fit = np.polyfit(np.log(tau), np.log(var), 1)
print(f"element-variance exponent over worker's last four bins = {var_fit[0]:.5f}")


l_planck = 1.616e-35
D = 3.086e25
L_H = 1.31e26
kappa = 3.0
coef = 0.5 * sqrt(2 * 1.673867577 * kappa)
lk_D = (coef * l_planck**2 * D) ** (1 / 3)
lk_H = (coef * l_planck**2 * L_H) ** (1 / 3)
du = 3e7
lk_wave = (1.673867577 * kappa * l_planck**4 * du * D) ** (1 / 6)
print(f"renewal coefficient in lk^3 criterion = {coef:.9f}")
print(f"renewal lk bound: D={lk_D:.9e} m, Hubble={lk_H:.9e} m")
print(f"isolated-wave arithmetic lk bound = {lk_wave:.9e} m")
