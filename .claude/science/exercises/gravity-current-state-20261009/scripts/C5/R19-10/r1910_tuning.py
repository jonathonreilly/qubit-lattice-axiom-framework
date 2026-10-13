"""R19-10 (c)/(d): can the standing in-progress energy be zeroed?  Under the law-energy accounting (A_law),
delta(g) = E0(K(g)) - E0(K_B) need not be positive: the decoupled ("dark") site's on-site stiffness
d_A = m^2 + 6 + Delta is a free choice of the insertion law.  Find Delta* with mean_path delta = 0
(smoothstep path, adiabatic limit: A_law -> T * mean delta), per mass.  Distinct Delta*(m) = one tuned number
per species; d Delta*/d m^2 != 0 means loop shifts of m^2 move it (radiative instability of the zero).
"""
import numpy as np
from scipy.optimize import brentq
src = open('r1910_adiabatic.py').read().split('# static delta(g)')[0]
exec(src)

def build_D(N, m, s, Delta):
    KA, KB = build(N, m, s)
    KA[N, N] += Delta
    return KA, KB

taus, wt = np.polynomial.legendre.leggauss(12); taus = 0.5*(taus + 1); wt = 0.5*wt
def mean_delta(m, Delta, N=48):
    acc = 0.0
    for s, w in zip(S_nodes, S_w):
        KA, KB = build_D(N, m, s, Delta)
        E0B = 0.5*np.sqrt(np.linalg.eigvalsh(KB)).sum()
        d = 0.0
        for tau, wtau in zip(taus, wt):
            g = sstep(tau)
            d += wtau*(0.5*np.sqrt(np.linalg.eigvalsh((1-g)*KA + g*KB)).sum() - E0B)
        acc += w*d
    return acc

for m in (0.0, 0.3, 1.0):
    f = lambda D: mean_delta(m, D)
    vals = [(D, f(D)) for D in (-3.0, -2.0, -1.0, 0.0, 1.0)]
    pr('m=%.1f: mean in-progress excess per inserted site vs Delta: ' % m + ', '.join('%+.1f: %+.5f' % v for v in vals))
    Ds = brentq(f, -5.9, 0.0, xtol=1e-12)
    pr('   zero at Delta* = %+.6f (d_A = %.6f); check f(Delta*) = %.1e' % (Ds, m*m + 6 + Ds, f(Ds)))
    # sensitivity of the zero to the mass (radiative shift of m^2)
    dm2 = 1e-3
    Ds2 = brentq(lambda D: mean_delta(np.sqrt(m*m + dm2), D), -5.9, 0.0, xtol=1e-12)
    pr('   d Delta*/d m^2 = %+.4f ; slope d(mean delta)/d Delta at the zero = %+.5f'
       % ((Ds2 - Ds)/dm2, (f(Ds + 1e-4) - f(Ds - 1e-4))/2e-4))
