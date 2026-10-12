"""R11-1 (b): assemble c_matter - c_T at one loop (prescription dD-M) from r111_matter_speed{,_light}.out (J, N = 96,
lambda -> 0 by Richardson in lambda^2 from lambda = 0.2, 0.1) and R9-9's refereed Xi (scripts/C5/R9-9/r99_tt_selfenergy.out,
N = 128, member M; lines 28-29, 40-41, 52-53, 64-65).  Conventions: c_m^2 - 1 = 4 kappa_lat J (kappa^2 = 32 pi G = 4 kappa_lat),
c_T^2 - 1 = 2 kappa_lat Xi (R9-9), so c_m - c_T = kappa_lat (2J - Xi) at first order; kappa_lat = 8 pi (l_P/a)^2."""
import re, numpy as np
U = 16 * np.pi ** 2
def readJ(fn):
    d = {}
    for line in open(fn):
        mm = re.match(r'(\w+) m=([\d.]+) N=\s*(\d+) lam=([\d.]+) \| J_on=([-+\de.]+)', line)
        if mm: d[(mm[1], float(mm[2]), int(mm[3]), float(mm[4]))] = float(mm[5])
    return d
J = readJ('r111_matter_speed.out'); J.update(readJ('r111_matter_speed_light.out'))
Xi = {('G', 1.0): (-9.602325e-04, -5.291787e-04), ('G', 0.3): (-1.112054e-03, -6.278535e-04),
      ('L', 1.0): (+2.408543e-03, +2.319010e-03), ('L', 0.3): (+5.275332e-03, +5.518134e-03)}
kl = 8 * np.pi
print('J (lambda->0, N=96) and J/m^2:')
for name in ['G', 'L']:
    for m in [1.0, 0.3, 0.1, 0.05]:
        j2, j1 = J[(name, m, 96, 0.2)], J[(name, m, 96, 0.1)]
        j0 = (4 * j1 - j2) / 3
        jn = J.get((name, m, 64, 0.1))
        print('  %s m=%.2f  J0 = %+.5e  (lam=0.1: N=64 %+.5e, N=96 %+.5e)  J0/m^2 = %+.4e' % (name, m, j0, jn, j1, j0 / m ** 2))
print('\nc_m - c_T = kappa_lat (2J - Xi); in units kappa_lat/(16 pi^2): 16pi^2 (2J - Xi); size at a = l_P (kappa_lat = 8 pi):')
for name in ['G', 'L']:
    for m in [1.0, 0.3]:
        j0 = (4 * J[(name, m, 96, 0.1)] - J[(name, m, 96, 0.2)]) / 3
        for pol, xi in zip(['T2g', 'Eg'], Xi[(name, m)]):
            sp = 2 * j0 - xi
            print('  %s m=%.1f %-3s: 2J = %+.4e  Xi = %+.4e  2J - Xi = %+.4e  | x16pi^2 = %+.4f | at a=l_P: c_m - c_T = %+.3e  (dc_m = %+.3e, dc_T = %+.3e)'
                  % (name, m, pol, 2 * j0, xi, sp, U * sp, kl * sp, 2 * kl * j0, kl * xi))
print('\nLight external matter (m_ext a -> 0; J = m^2 J2 -> 0), loop species at m = 0.3 (R9-9): c_m - c_T -> -kappa_lat Xi:')
for name in ['G', 'L']:
    for pol, xi in zip(['T2g', 'Eg'], Xi[(name, 0.3)]):
        print('  %s %-3s: -Xi x16pi^2 = %+.4f ; at a=l_P: %+.3e ; vs GW170817 band ~1e-15: ratio ~ %.0e' % (name, pol, -U * xi, -kl * xi, abs(kl * xi) / 1e-15))
print('\nMatter-side shift for a proton at a = l_P (m a = 0.938 GeV / 1.22e19 GeV = 7.7e-20): dc_m = 2 kappa_lat m^2 J2 ~ %.1e (G), %.1e (L)'
      % (2 * kl * (7.7e-20) ** 2 * (-5.7e-3), 2 * kl * (7.7e-20) ** 2 * (-7.3e-3)))
