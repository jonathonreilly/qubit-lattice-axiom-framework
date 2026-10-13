"""Map: best Xi_T2g (M and U) over zigzag laws Zz(b, V, P, wt) as a function of the valley floor V (edge minimum of sigma).
Zz: sigma' = 1 on [0,b]; -1 down to V; then +1 to P, -1 to V, ... ; final flat (sigma'=0) on last >= 0.1; C^inf steps width wt."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *
T0 = time.time()
def Zz(b, V, P, wt, endmin=0.1):
    vals = [1.0, -1.0]; bks = [b]; k = b + (b - V); lev = V; s = +1
    if k > np.pi - endmin: return None
    while True:
        L = (P - V)
        if k + L > np.pi - endmin: break
        bks.append(k); vals.append(float(s)); k += L; s = -s
    bks.append(k); vals.append(0.0)
    if min(np.diff(bks)) < wt*1.05 if len(bks) > 1 else False: return None
    return ZLaw(vals, bks, wt, 'Zz(b=%.2f,V=%.2f,P=%.2f,wt=%.2f)' % (b, V, P, wt), nf=1 << 16)
if __name__ == '__main__':
    n = 1 << 13
    for wt in [0.06, 0.12]:
        print('=== wt = %.2f' % wt)
        for Vf in [0.3, 0.45, 0.6, 0.75, 0.9, 1.05, 1.2]:
            best = {}
            for b in np.arange(0.6, 2.61, 0.2):
                for V in np.arange(Vf, b - 0.05, 0.1):
                    for P in np.arange(V + 0.1, b + 0.001, 0.1):
                        law = Zz(b, V, P, wt)
                        if law is None: continue
                        g, f = law.samples(n)
                        if np.sqrt(g[np.abs(2*np.pi*(np.arange(n)+0.5)/n - np.pi) >= b].min()) < Vf - 1e-6: continue
                        for m in [0.3, 0.1]:
                            X = xi_all(g, f, m, nu=600)
                            for v in ['M,T2g', 'U,T2g']:
                                key = (m, v)
                                if key not in best or X[v] > best[key][0]:
                                    best[key] = (X[v], law.name, X)
            print('V_floor=%.2f: ' % Vf + ' | '.join('m=%.1f %s best %+.3e [%s; Eg M %+.2e U %+.2e]' % (k[0], k[1], val[0], val[1], val[2]['M,Eg'], val[2]['U,Eg']) for k, val in sorted(best.items())), flush=True)
    print('runtime %.1fs' % (time.time()-T0))
