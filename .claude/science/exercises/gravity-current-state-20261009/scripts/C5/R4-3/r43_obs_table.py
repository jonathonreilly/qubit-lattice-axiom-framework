"""R4-3 check C: physical-unit arithmetic for LRL at a = l_P and a = 1e-19 m.
(1) Law-independent kinematics: the invariant Bragg gap |G^2| >= (2 pi)^2/(7 a^2) (refereed, R2-2) against the
    pair invariants of observed processes ('in band' = every pair invariant below the gap).
(2) Rest-frame location of the Bragg resonance shell for a massive particle, |G|_E ~ |G^2|/(2m) (R3-1 kinematics).
(3) Conditional (law-dependent) LV: required size of the per-realization automorphic coefficient for each bound,
    for three scaling hypotheses of the realised dispersion  delta v / c = eps * (E a)^n * A(direction):
      n = +1 (naive transfer of R3-1's single-shell tube 'relative LV ~ kappa*tau'),
      n = +2, and n = -3 (moment-conditioned finite-shell kernels: abs LV ~ 1/kappa vs LI ~ kappa^2; check B).
Bounds (refereed in the packet unless marked):
  LHAASO GRB 221009A ToF: E_QG,1 > 10 E_Pl, E_QG,2 > 6e-8 E_Pl  (C5_O1_report.md:43; C4_B1_referee.md item 7)
  LHAASO 1.4 PeV photon survival: c_gamma - c_e < 2.66449e-19     (C5_O1_report.md:41; O1 referee 5)
  LHAASO spectra (superluminal photon decay): E_LV,1 > ~1e5 E_Pl    (C5_O1_report.md:42)
  Auger/HESS vacuum Cherenkov (iron-based, indicative): 6e-20       (C5_O1_report.md:44; O1 referee)
  GRB 140206A polarisation, dim-5 birefringence: xi < 1e-16         (web: Gotz et al. 2014, arXiv:1408.4121; COMPARATOR)
  Ne-Rb-K comagnetometer neutron c_jk ~ 1e-29                         (C5_O1_report.md:48)
  Yb+ clock electron c_jk ~ 1e-21                                     (web: Sanner et al. Nature 567, 204 (2019); COMPARATOR)
  GW170817: (c_T - c)/c in [-3e-15, 7e-16]                            (C5_O1_report.md:47)
"""
import numpy as np
hbarc = 1.97327e-16          # GeV m
lP = 1.616255e-35            # m
EPl = hbarc / lP             # 1.2209e19 GeV
GeV = 1.0
cases = {"a = l_P": lP, "a = 1e-19 m": 1e-19}
gap_lat = (2 * np.pi) ** 2 / 7
print(f"E_Pl = hbar c / l_P = {EPl:.4e} GeV;  lattice gap |G^2|min = (2pi)^2/7 = {gap_lat:.4f} a^-2  (sqrt = {np.sqrt(gap_lat):.4f}/a)")
procs = [  # (label, invariant |s| in GeV^2)
    ("1.4 PeV gamma x CMB photon (1e-3 eV), 4 E e", 4 * 1.4e6 * 1e-12),
    ("13 TeV GRB gamma x EBL photon (1 eV), 4 E e", 4 * 1.3e4 * 1e-9),
    ("1e20 eV proton x CMB (GZK), s", 0.938**2 + 4 * 1e11 * 1e-12),
    ("3e20 eV primary x air nucleon, s = 2 E m", 2 * 3e11 * 0.938),
    ("1.4 PeV gamma x detector nucleon, 2 E m", 2 * 1.4e6 * 0.938),
    ("LHC pp, s = (13.6 TeV)^2", 13.6e3 ** 2),
    ("nucleon rest-frame internal (Fermi 0.25 GeV), (2 m)^2-ish", (2 * 0.938) ** 2),
]
for lab, a in cases.items():
    Ea = hbarc / a
    gap = gap_lat * Ea ** 2
    print(f"\n[{lab}]  1/a = {Ea:.4e} GeV;  gap |G^2|min = {gap:.4e} GeV^2 (sqrt {np.sqrt(gap):.4e} GeV)")
    for name, s in procs:
        status = "IN band" if s < gap else "OUT of band (umklapp channels kinematically open)"
        print(f"   {name:58s} s = {s:.3e} GeV^2   log10(gap/s) = {np.log10(gap/s):7.2f}   {status}")
    for name, m in [("electron", 0.511e-3), ("nucleon", 0.938)]:
        print(f"   Bragg resonance shell for a {name} at rest: |G|_E ~ |G^2|/(2m) = {gap/(2*m):.3e} GeV = {gap/(2*m)/EPl:.3e} E_Pl")

print("\n(3) Conditional LV requirements.  delta v/c = eps * (E a)^n * A, |A| ~ 1")
bounds = [  # (label, E in GeV, allowed |delta v/c|)
    ("GRB 221009A ToF, linear (13 TeV): dv < E/E_QG1, E_QG1 = 10 E_Pl", 1.3e4, 1.3e4 / (10 * EPl)),
    ("GRB 221009A ToF, quadratic (13 TeV): dv < (E/E_QG2)^2, E_QG2 = 6e-8 E_Pl", 1.3e4, (1.3e4 / (6e-8 * EPl)) ** 2),
    ("1.4 PeV photon survival (photon-fast vs e): dv < 2.66e-19", 1.4e6, 2.66449e-19),
    ("LHAASO superluminal decay, linear: dv < E/(1e5 E_Pl) at 1 PeV", 1e6, 1e6 / (1e5 * EPl)),
    ("GRB polarisation birefringence (helicity-odd, ~300 keV): |dv_+ - dv_-| < 2 xi E/E_Pl, xi=1e-16", 3e-4, 2 * 1e-16 * 3e-4 / EPl),
    ("Hughes-Drever neutron c_jk ~ 1e-29 (internal p ~ 0.25 GeV)", 0.25, 1e-29),
    ("Yb+ clock electron c_jk ~ 1e-21 (bound electron p ~ few keV)", 5e-6, 1e-21),
    ("Optical cavity isotropy of c ~ 1e-18 (1 eV photons; comparator, from memory)", 1e-9, 1e-18),
]
for lab, a in cases.items():
    Ea = hbarc / a
    print(f"\n[{lab}]")
    print(f"   {'bound':92s} {'E a':>10s}  eps_max(n=+1)  eps_max(n=+2)  eps_max(n=-3)")
    for name, E, dv in bounds:
        Ea_ = E / Ea
        r = [dv / Ea_ ** n for n in (1, 2, -3)]
        print(f"   {name:92s} {Ea_:10.3e}  {r[0]:12.3e}  {r[1]:12.3e}  {r[2]:12.3e}")

# naive n=+1 transfer of R3-1's single-shell numbers: rel LV ~ C (kappa tau)^1, C ~ 3.4e-3..5.6e-3 (r31_lv_scaling.out:16,33)
print("\nNaive n = +1 transfer (single-shell tube numbers, eps = C*tau, C*tau ~ 5.6e-3*sqrt3 .. 3.4e-3*sqrt7 ~ 1e-2):")
eps1 = 1e-2
for lab, a in cases.items():
    Ea = hbarc / a
    print(f"[{lab}]")
    for name, E, dv in bounds:
        pred = eps1 * (E / Ea)
        print(f"   {name:92s} predicted dv ~ {pred:.2e}  allowed {dv:.2e}  -> {'violates by ' + format(pred/dv, '.1e') if pred > dv else 'passes by ' + format(dv/pred, '.1e')}")
# GRB 221009A time delay for the naive transfer
D_lt = 1.9e9 * 3.156e7      # light-travel time ~ 1.9 Gyr at z = 0.151 (approximate; comparator)
print(f"\nGRB 221009A (z=0.151, light-travel ~1.9 Gyr): naive n=+1 delay at 13 TeV, a=l_P: {D_lt*eps1*1.3e4/EPl:.2f} s")
# IR-growing case: the scale below which the LV term dominates the LI d'Alembertian for coefficient eps_B
print("\nn = -3 (abs LV ~ eps_B/kappa against LI ~ (pi/4) kappa^2): LV dominates for kappa a < (4 eps_B/pi)^(1/3)")
for epsB in [1e-2, 1e-6, 1e-20, 1e-60, 1e-120]:
    ka = (4 * epsB / np.pi) ** (1 / 3)
    print(f"   eps_B = {epsB:.0e}: crossover kappa a = {ka:.2e} -> E = {ka*EPl:.2e} GeV at a = l_P, {ka*hbarc/1e-19:.2e} GeV at 1e-19 m")
H0 = 1.44e-42  # GeV (hbar H0)
for lab, a in cases.items():
    Ea = hbarc / a
    print(f"[{lab}] to keep rel LV < 1e-18 down to kappa = 1/(1 m): eps_B < {1e-18*(np.pi/4)*(hbarc/1.0/Ea)**3:.1e};"
          f"  down to the Hubble scale: eps_B < {1e-18*(np.pi/4)*(H0/Ea)**3:.1e}")
# stability: forward-tube zero at kappa* ~ (4 eps_B/pi)^(1/3)/a must be slower than the Hubble rate
for lab, a in cases.items():
    Ea = hbarc / a
    print(f"[{lab}] stability over a Hubble time (kappa*/a < H0): eps_B < (pi/4)(H0 a)^3 = {(np.pi/4)*(H0/Ea)**3:.2e};"
          f"  if eps_B ~ exp(-c l_k/a): l_k/a > {-np.log((np.pi/4)*(H0/Ea)**3):.0f}/c")
