"""Reproduce R14-3's W08/W14 numbers with independent code; compute I(B); abstract soft-B2g vertex on W08/W14."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from laws import *
from math import gamma
T0 = time.time()
def xi_soft(g, f, m, eta, nu=2000, umin=-16.0):
    # vertex |V|^2 = 4 g_x g_y exp(-(g_x+g_y)/eta): nonnegative, k_z-independent, B2g (T2g) symmetric
    umax = np.log(80.0/min(m*m, 1.0)) + 2
    u = np.linspace(umin, umax, nu); t = np.exp(u); du = u[1]-u[0]
    mm = moments_from(g, f, t); mm2 = moments_from(g, f, t + 1.0/eta)
    J = 2*t*mm['F2'] - mm['E0']
    return float(np.sum(t*du*t**1.5*np.exp(-t*m*m)*J*4*mm2['G1']**2)/(32*gamma(2.5)))
if __name__ == '__main__':
    for law in [W08(), W14()]:
        g, f = law.samples(1 << 15); inf = law.info()
        print('== %s max|s\'|=%.6f sig(pi)=%.4f valleys(k,g)=%s' % (law.name, inf['maxabs'], inf['sig_pi'], inf['valleys']))
        for m in [1.0, 0.3, 0.1, 0.01]:
            X = xi_all(g, f, m)
            print('  m=%.2f vmax=%.5f ' % (m, law.vmax(m)) + ' '.join('%s %+.4e' % kv for kv in X.items()))
        Bs = [1e-4, 1e-2, 0.1, 0.5, 1, 2, 3, 5, 10]
        print('  I(B):', ' '.join('B=%g:%+.4g' % (B, I) for B, I in zip(Bs, Icurve(g, f, Bs))))
        for m in [0.3, 0.1]:
            print('  soft-B2g vertex 4g_xg_y e^{-(g_x+g_y)/eta}, m=%.1f: ' % m + ' '.join('eta=%g: %+.3e' % (eta, xi_soft(g, f, m, eta)) for eta in [10, 1, 0.3, 0.1, 0.03]))
    print('runtime %.1fs' % (time.time()-T0))
