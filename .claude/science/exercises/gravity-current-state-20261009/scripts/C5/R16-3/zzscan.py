"""Smooth zigzag laws: sigma' = 1 on [0,b], then -1 down to x0-d, then +-1 zigzag of half-amplitude d, final flat to pi.
Transition width wt (C^inf step).  Scan b, x0, d; report Xi for all four vertices at m = 0.3, 0.1."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *
T0 = time.time()
def zig(b, x0, d, wt, endflat=0.12):
    vals = [1.0]; bks = [b]
    k = b; lev = b
    # descend to x0-d
    L = lev - (x0 - d); vals.append(-1.0); k += L; lev = x0 - d
    s = +1
    while k + 2*d < np.pi - endflat:
        bks.append(k); vals.append(float(s)); k += 2*d; lev += 2*d*s; s = -s
    bks.append(k); vals.append(0.0)
    return ZLaw(vals, bks, wt, name='Z(b=%.2f,x0=%.2f,d=%.2f,wt=%.2f)' % (b, x0, d, wt))
if __name__ == '__main__':
    n = 1 << 14
    for b in [1.0, 1.4]:
        for x0 in [0.6, 0.8, 1.0]:
            for d in [0.1, 0.2, 0.3]:
                law = zig(b, x0, d, 0.06)
                g, f = law.samples(n); inf = law.info()
                r = []
                for m in [0.3, 0.1]:
                    X = xi_all(g, f, m, nu=800)
                    r.append('m=%.1f T2g M %+.2e U %+.2e | Eg M %+.2e U %+.2e' % (m, X['M,T2g'], X['U,T2g'], X['M,Eg'], X['U,Eg']))
                print('%s max|s\'|=%.4f sig(pi)=%.3f minvalley g=%.3f :: %s' % (law.name, inf['maxabs'], inf['sig_pi'],
                      min([v[1] for v in inf['valleys']] + [9]), ' || '.join(r)), flush=True)
    print('runtime %.1f' % (time.time()-T0))
