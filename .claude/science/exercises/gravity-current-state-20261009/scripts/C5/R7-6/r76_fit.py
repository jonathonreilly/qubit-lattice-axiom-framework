"""R7-6 script 2: fit E^2 = M0^2 + (1 - delta) P^2 to the trimer rows of script 1 (lam = -3, L = 300),
and compare with the BT 3-body law, whose mass operator is the P = 0 fibre of the naive law
(M_BT = H_naive(P=0), see report section 4.2), so E_BT(P) = sqrt(M0^2 + P^2) exactly."""
import re, numpy as np
rows = []
txt = open('r76_threebody_naive_fermi_lam-3.0_kap0.25.out').read().split('L = 300:')[1]
for P, E in re.findall(r'P = ([+-][0-9.]+) dim = +\d+ +E0 = ([0-9.]+)', txt):
    rows.append((float(P), float(E)))
rows = np.array(rows); P, E = rows[:, 0], rows[:, 1]; M0 = E[0]
out = []
for p, e in zip(P[1:], E[1:]):
    delta = 1 - (e*e - M0*M0)/(p*p)
    ebt = np.sqrt(M0*M0 + p*p)
    out.append('P = %.5f  E_naive = %.9f  E_BT = %.9f  E_BT - E_naive = %+.3e  delta = 1 - (E^2 - M0^2)/P^2 = %.4f' % (p, e, ebt, ebt - e, delta))
open('r76_fit.out', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
