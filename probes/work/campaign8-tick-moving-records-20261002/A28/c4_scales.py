"""A28 c4: order-of-magnitude arithmetic (ARGUED inputs; comparator data, not adopted).

Light recorded at record edges.  Per tick a photon is recorded with chance kappa * (its weight
on gate-open sites).  Averaged over a medium whose gate-open (record-adjacent) sites fill volume
fraction f_adj = n * A * l_P (one-site shell of area A per recorded object, n objects per m^3):
    optical depth  tau = kappa * n * A * L / v_L      (v_L = light speed in sites per tick)
    recording cross-section per object  sigma = kappa * A / v_L.
Record-geometry hypotheses per nucleon: H-pt (one isolated recorded site: A = 6 l_P^2),
H-ball (nucleon-sized recorded ball, r = 0.84 fm), H-atom (Bohr-radius ball per atom).
Second part: heating bound on edge false records (sea vacuum next to records), using A19's
'sharp registration < 1e-90 per nucleon per Planck tick' and c2's O(J) energy per sharp lock.
"""
import numpy as np
from scipy.integrate import quad

lP = 1.616e-35; tP = 5.391e-44; c = 2.998e8; mN = 1.6605e-27
A = {'H-pt (1 recorded site/nucleon)': 6 * lP ** 2,
     'H-ball (r = 0.84 fm/nucleon)': 4 * np.pi * (0.84e-15) ** 2,
     'H-atom (r = 0.53 A per atom; per nucleon of H)': 4 * np.pi * (0.529e-10) ** 2}

# cosmology (flat LCDM; Planck-2018-like comparator values)
H0 = 67.7e3 / 3.0857e22; Om, Ob, Orad = 0.31, 0.049, 9.1e-5; OL = 1 - Om - Orad
rho_c = 3 * H0 ** 2 / (8 * np.pi * 6.674e-11)
nb0 = Ob * rho_c / mN
E = lambda z: np.sqrt(Om * (1 + z) ** 3 + OL + Orad * (1 + z) ** 4)
col = lambda z1: nb0 * (c / H0) * quad(lambda z: (1 + z) ** 2 / E(z), 0, z1, limit=200)[0]

# (name, nucleon column [m^-2] over the path, allowed extra tau)
cases = [
    ('silica fibre, 1 km (0.2 dB/km at 1550 nm)', 2.2e3 / mN * 1e3, 0.2 / (10 * np.log10(np.e))),
    ('pure water, 1 m (abs ~5e-3/m at 420 nm)', 1.0e3 / mN * 1.0, 5e-3),
    ('Earth atmosphere, zenith (extra tau <~ 0.05)', 1.033e4 / mN, 0.05),
    ('Galactic ISM, 1 kpc at n_H = 1/cm^3 (extra tau <~ 0.1)', 1.4e6 * 3.0857e19, 0.1),
    ('IGM z<6 (quasar continua; extra tau <~ 0.1)', col(6.0), 0.1),
    ('since recombination z<1090 (CMB; extra tau <~ 0.1)', col(1090.0), 0.1),
]
print(f'n_b0 = {nb0:.3f} m^-3 ; IGM columns: z<6 {col(6.0):.3e}, z<1090 {col(1090.0):.3e} nucleons/m^2')
print('kappa_max (per contact tick, v_L = 1) = tau_allowed / (A * column):')
hdr = '  {:58s}'.format('medium') + ''.join(f'{k.split()[0]:>12s}' for k in A)
print(hdr)
for name, colm, tau in cases:
    row = '  {:58s}'.format(name)
    for k, a in A.items():
        row += f'{tau / (a * colm):12.2e}'
    print(row)
print('  (kappa_max > 1 means no constraint: recording on every contact tick is allowed)')

# Heating: edge false records in a full-rank sea
EP = 1.956e9  # Planck energy, J
bound = 1e-90  # A19: sharp registrations per nucleon per Planck tick (ARGUED there)
print(f'\nA19 bound 1e-90 /nucleon/tick at ~E_P each = {bound * EP / tP / mN:.2e} W/kg of matter')
for k, a in A.items():
    if 'atom' in k:
        continue
    nedge = a / lP ** 2
    for lam in (5e-6, 5.3e-4):
        cmax = bound / (nedge * lam)
        print(f'  {k:34s} edge sites/nucleon {nedge:8.2e}; floor lambda_min = {lam:.1e} -> '
              f'formation strength c <~ {cmax:.1e}/tick -> time to record a true excitation '
              f'~ {tP / cmax:.1e} s')
print(f'  (age of the universe ~ {13.8e9 * 3.156e7:.2e} s = {13.8e9 * 3.156e7 / tP:.2e} ticks)')

# Edge creep (Eden-like, no record moves): front advance over the age at rate eps_edge per tick
for cc in (5.4e-44, 1e-3):
    for lam in (5e-6, 5.3e-4):
        adv = cc * lam * 13.8e9 * 3.156e7 / tP
        print(f'  creep: c = {cc:.1e}/tick, floor {lam:.1e}: advance over the age ~ {adv:.2e} sites = {adv * lP:.2e} m')

# Ungated comparison: sharp false records in VOIDS at eps per site per tick, each injecting
# ~E_P (c2: 0.21-0.85 J in lattice units), must not build up more than the observed dark-energy
# density over the age of the universe (a generous ceiling).  Gating makes this rate exactly 0.
age = 13.8e9 * 3.156e7
rho_DE = 0.69 * rho_c * c ** 2  # J/m^3
pdens = EP / (lP ** 3 * tP)     # W/m^3 at one sharp record per site per tick
for eJ in (0.21, 0.85):
    print(f'void heating (ungated, sharp records, {eJ} E_P each): eps_void <~ {rho_DE / age / (eJ * pdens):.1e} per site per tick '
          f'(compare A12/A4 freezing 1.2e-61)')
