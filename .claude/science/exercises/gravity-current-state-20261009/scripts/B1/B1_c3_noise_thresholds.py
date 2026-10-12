"""B1 check c3: how fast must per-realization substrate noise fade with wavelength to pass
coherence data?  Toy model (SUGGESTED, not a theorem; a random-phase screen):

  fractional change of the wave operator, coarse-grained over one wavelength cell, delta_lambda = A (l/lambda)^p
  each cell adds an independent phase ~ 2 pi delta_lambda; a ray crosses N = D/lambda cells
  phi_rms = 2 pi A (l/lambda)^p sqrt(D/lambda)        coherence needs phi_rms < 1

Power counting of p for white noise of one realization (EXACT dimensional analysis):
  noise in a mass-type term (delta m^2), frozen in 3D space      : p = -1/2 (relevant; F1a)
  noise in a mass-type term, white in 4D spacetime              : p =  0   (marginal; E1 power count)
  noise in a dimensionless kinetic coefficient, frozen in 3D    : p = 3/2
  noise in a dimensionless kinetic coefficient, white in 4D     : p = 2
(The E1 BD operator adds a gain that grows with the size of the past: A^2 ~ eps (T/l_k)^2.)
Source distances/wavelengths are representative, not fitted.
"""
import math
Gpc = 3.0857e25; Mpc = Gpc / 1e3; km = 1e3
probes = [
    ("LIGO GW, 100 Hz, 1 Gpc",                3.0e6,   1 * Gpc),
    ("LISA GW, 1 mHz, 10 Gpc",                3.0e11, 10 * Gpc),
    ("optical quasar imaging, 3 Gpc",         5.0e-7,  3 * Gpc),
    ("GRB 090510 31 GeV photon, ~3 Gpc",      4.0e-17, 3 * Gpc),
    ("TeV blazar photon, 0.5 Gpc",            1.2e-18, 0.5 * Gpc),
    ("LHAASO GRB221009A 10 TeV, ~0.75 Gpc",   1.2e-19, 0.75 * Gpc),
    ("electron Compton phase over 1 km",      2.43e-12, 1 * km),
    ("proton Compton phase over 1 km",        1.32e-15, 1 * km),
]
def pmin(lam, D, l, A=1.0):
    # need 2 pi A (l/lam)^p sqrt(D/lam) < 1
    return (math.log(2 * math.pi * A) + 0.5 * math.log(D / lam)) / math.log(lam / l)
classes = [("mass-type, frozen 3D", -0.5), ("mass-type, 4D white", 0.0),
           ("kinetic, frozen 3D", 1.5), ("kinetic, 4D white", 2.0)]
for l, lname in [(1.616e-35, "l = l_P"), (1e-19, "l = 1e-19 m")]:
    print(f"\n=== {lname} ===")
    print(f"{'probe':40s} {'p_min(A=1)':>10s} {'p_min(A=1e3)':>12s} | " + " ".join(f"{c[0]:>22s}" for c in classes))
    for name, lam, D in probes:
        if lam <= l:
            print(f"{name:40s}  wavelength below l: probe resolves the grain"); continue
        p1 = pmin(lam, D, l); p3 = pmin(lam, D, l, 1e3)
        verdicts = []
        for cname, p in classes:
            phi = 2 * math.pi * (l / lam) ** p * math.sqrt(D / lam)
            verdicts.append(f"{'PASS' if phi < 1 else 'FAIL'} (log10 phi={math.log10(phi):6.1f})")
        print(f"{name:40s} {p1:10.3f} {p3:12.3f} | " + " ".join(f"{v:>22s}" for v in verdicts))

# E1-type growing gain: A = sqrt(kappa eps) * (T/l_k), T = Hubble time, eps = (l_P/l_k)^4, kappa ~ 1.674*4 (slab)
print("\nE1-type gain (volume-only kernel, infinite valency): A^2 = 6.7 eps (T/l_k)^2, T = c/H0")
T = 1.37e26
for lk in [1e-19, 1e-17, 1e-15]:
    eps = (1.616e-35 / lk) ** 4
    A = math.sqrt(6.7 * eps) * T / lk
    print(f"  l_k = {lk:.0e} m: eps = {eps:.1e}, A = {A:.2e}  (A >> 1 means the one-step noise exceeds the signal)")
