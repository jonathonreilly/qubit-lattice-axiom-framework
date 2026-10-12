"""C5 R9-9: physical sizes (readings). GR normalisation, reduced Planck mass; kappa_lat = 1/(M a)^2 = 8 pi (l_P/a)^2.
c_T^2 - 1 = 2 kappa_lat Xi ;  Dm_T^2 (E_g - T_2g) = 2 kappa_lat Dmu / a^2.
GW170817 band -3e-15 <= dc <= 7e-16 (as cited in C5_R7-4_report.md:46). Graviton-mass bound 1.27e-23 eV: RECALLED (LVK GWTC-3), not verified."""
import numpy as np
lP = 1.616255e-35; hbarc = 1.97327e-7   # m, eV m
cases = {'G, M-vertex, T2g, m=1': -9.6023e-4, 'G, M-vertex, Eg, m=1': -5.2918e-4,
         'L, M-vertex, T2g, m=1': +2.4087e-3, 'L, U-vertex, Eg, m=1': +9.0551e-2, 'NN, M-vertex, T2g, m=1': -1.9030e-3}
for name, Xi in cases.items():
    dc = 0.5*16*np.pi*Xi     # at a = l_P
    bound = 3e-15 if dc < 0 else 7e-16
    amin = np.sqrt(abs(dc)/bound)   # a/l_P needed, per species
    print('%-26s Xi=%+.3e  dc_T(a=l_P)=%+.3e  ratio to GW170817 band %.1e  needs a >= %.1e l_P = %.1e m (one species)' % (name, Xi, dc, abs(dc)/bound, amin, amin*lP))
for name, Dmu in {'G, metric seagull, m=1': 4.8736e-2, 'L, metric seagull, m=1': 2.3114e-2}.items():
    for a in (lP, 1e-19):
        mT2 = 2*8*np.pi*(lP/a)**2*Dmu/a**2   # m^-2
        print('%-26s Dmu=%.3e  a=%.1e m: |Dm_T^2|^(1/2) = %.2e eV  (ratio to 1.27e-23 eV: %.1e)' % (name, Dmu, a, np.sqrt(mT2)*hbarc, np.sqrt(mT2)*hbarc/1.27e-23))
