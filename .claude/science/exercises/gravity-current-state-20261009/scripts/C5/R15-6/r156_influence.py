"""R15-6 step 5: size of the instantaneous g-influence today, against stated bounds (b).
(i) Local (scales << c/H): the E-fluid pressure perturbation is dp_E = -g dN (p_E = g/N - lam, Lemma C), and in a
    quasi-static region the CMC lapse is dN = Phi_N/c^2 (R14-5 checked N - 1 = Phi_N in halos, referee-confirmed as
    conditional).  Newtonian limit of R_00: lap Phi_x = (1/2)(d lam + 3 dp_E) = -(3/2) g Phi_N/c^2  (d lam = 0).
    Point mass: Phi_x = (3/4) g (GM/c^2) r  ->  |a_x| = (3/4) |g| GM/c^2, set on the CMC slice (instantaneous),
    Yukawa-cut at r ~ Q^{-1/2} ~ 0.8 c/H0.  Ratio to Newton: (3/4)|g| r^2/c^2.
(ii) Hubble-scale modes: Lemma S jump factor 1 + (3g/2)/(k^2/a^2 + Qbar) (R15-1, checked there); today Qbar = 1.35 H0^2.
Bounds (RECALLED, not fetched): planetary-ephemeris limits on an anomalous constant radial acceleration toward the Sun
~1e-14 m/s^2 (Saturn, Cassini-era ranging); LLR limits on anomalous Earth-Moon accelerations ~1e-13..1e-14 m/s^2;
growth/ISW/lensing consistency with GR at the few-% level on k ~ (1-10) H0/c.
"""
import numpy as np
c = 2.998e8; H0 = 67.4e3/3.0857e22; H02 = H0**2
GMc2 = {'Sun': 1476.6, 'Earth': 4.435e-3, 'double pulsar (2.59 Msun)': 2.59*1476.6}
r = {'Sun': 9.5*1.496e11, 'Earth': 3.844e8, 'double pulsar (2.59 Msun)': 8.8e8}
bound = {'Sun': 1e-14, 'Earth': 1e-13, 'double pulsar (2.59 Msun)': None}
print(f"H0 = {H0:.3e} s^-1, H0^2 = {H02:.3e} s^-2")
for gh in [1e-5, 1.0, 6.0]:
    g = gh*H02
    for k in GMc2:
        a = 0.75*g*GMc2[k]; ratio = 0.75*g*r[k]**2/c**2
        b = bound[k]
        s = f", allowed g/H0^2 < {b/(0.75*H02*GMc2[k]):.1e}" if b else ""
        print(f"  g/H0^2 = {gh:g}: {k:28s} |a_x| = {a:.2e} m/s^2; |Phi_x/Phi_N| at r = {r[k]:.1e} m: {ratio:.1e}{s}")
print("Hubble-scale fraction of the instantaneous response today, (3/2)(g/H^2)/(k^2 + 1.35) (k in H0/c):")
for gh in [1e-5, 1e-3, 0.05, 1.0]:
    print(f"  g/H0^2 = {gh:g}: k = 0.3, 1, 3, 10 -> " + ", ".join(f"{1.5*gh/(kk**2 + 1.35):.1e}" for kk in (0.3, 1, 3, 10)))
