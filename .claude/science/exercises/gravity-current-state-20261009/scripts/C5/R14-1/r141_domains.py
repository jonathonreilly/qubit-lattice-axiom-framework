"""R14-1: domain bookkeeping for the box-route runners at box half-width b (worst leg: q parallel to P).
Leg of a two-body state with total P and CM relative momentum q (equal masses m): k1 = (H0 q + P w)/M0,
w = sqrt(m^2+q^2), M0 = 2w, H0 = sqrt(M0^2 + P^2).  Pmax(b, kappa) = largest |P| with every leg in |k| < b."""
import numpy as np
from scipy.optimize import brentq
out = []
def pr(*a):
    l = ' '.join(str(x) for x in a); print(l, flush=True); out.append(l)
def leg(P, q, m):
    w = np.sqrt(m*m + q*q); M0 = 2*w; H0 = np.sqrt(M0**2 + P*P); return (H0*q + P*w)/M0
def Pmax(b, kap, m): return brentq(lambda P: leg(P, kap, m) - b, 0, 50)
m = 0.5
for lab, kap, Pi1, Pi2 in [('R8-1/R9-2 d=1 (kappa=0.4, Pi 0.6/1.2)', 0.4, 0.6, 1.2), ('R8-1 d=2 mass, R9-6, R11-4 (kappa=0.8, Pi 0.6/1.2)', 0.8, 0.6, 1.2),
                           ('R8-1 d=2 lattice algebra (kappa=1.0, Pi 1.0/1.4)', 1.0, 1.0, 1.4)]:
    pr('%s: max leg on supp W (|P|<=Pi2) = %.4f; on plateau (|P|<=Pi1) = %.4f; Pmax for legs<b: b=2.6 %.3f, b=2.0 %.3f, b=1.4 %.3f, b=1.2 %.3f'
       % (lab, leg(Pi2, kap, m), leg(Pi1, kap, m), *[Pmax(b, kap, m) for b in (2.6, 2.0, 1.4, 1.2)]))
pr('kappa_max at b=1.4 keeping Pi1 = 0.6 plateau with legs < b: %.4f (d=1/3 worst case)' % brentq(lambda k: leg(0.6, k, m) - 1.4, 0, 1.4))
pr('kappa_max at b=1.4 keeping Pi2 = 1.2 (R9-6/R11-4 shell) with legs < b: %.4f' % brentq(lambda k: leg(1.2, k, m) - 1.4, 0, 1.4))
for Mb in (0.95, 0.85, 0.70):
    pr('bound mass M_b=%.2f: plateau boost budget at rest asinh(Pi1/M_b) = %.4f (Pi1=0.6, b-independent while legs<b)' % (Mb, np.arcsinh(0.6/Mb)))
for mm in (0.3, 0.5):
    pr('one-body budget at rest, ball, m=%.1f: asinh(b/m): b=2.6 %.4f, b=2.0 %.4f, b=1.4 %.4f' % (mm, *[np.arcsinh(b/mm) for b in (2.6, 2.0, 1.4)]))
open('r141_domains.out', 'w').write('\n'.join(out) + '\n')
