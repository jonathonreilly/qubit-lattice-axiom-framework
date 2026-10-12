"""(b) witness: |sigma'| <= 1 law (subluminal for every m) with gapped edge valleys and Xi_{M,Eg} > 0.
sigma' nodes on [b, pi] (equal spacing, sstep blends): 1 | c_1..c_8 | 0.  Checks: Laplace evaluator (two resolutions)
and the direct 3D zone grid in both forms (A-form <|V|^2 A_zz/eps^5>/32 and IBP form)."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
def make(b, c, name):
    K = len(c); a = np.linspace(b, np.pi, K+2)[:-1]; w = a[1]-a[0]
    vals = [1.0] + list(c) + [0.0]; starts = list(a); widths = [w]*(K+1); widths[-1] = np.pi - a[-1]
    return Law(vals, starts, widths, name)
W14 = make(1.4, [-1, 1, -1, -1, -1, 1, 1, -1], 'W14 (b=1.4; c=-1,1,-1,-1,-1,1,1,-1)')
W08 = make(0.8, [-1, 1, 1, -1, -1, 1, 1, -1], 'W08 (b=0.8; c=-1,1,1,-1,-1,1,1,-1)')
for law in [W14, W08]:
    kk = np.linspace(0, np.pi, 200001); sp = law.dsig(kk); s = law._s(kk); g = s*s
    # local minima of g on (b, pi]
    gi = np.where((g[1:-1] < g[:-2]) & (g[1:-1] <= g[2:]))[0] + 1
    print('== %s: |sigma\'| max = %.6f; sigma(pi) = %.4f; A in [%.2f, %.2f]; edge g local minima at k = %s, g = %s; edge min eps^2 - m^2 = %.4f'
          % (law.name, np.abs(sp).max(), law.sig_pi, *law.Amax()[::-1], np.round(kk[gi], 3), np.round(g[gi], 4), g[kk >= law.b].min()), flush=True)
    for m in [1.0, 0.3, 0.1, 0.01]:
        mu, X = evaluate(law, m); mu2, X2 = evaluate(law, m, n=1 << 17, nu=5000, umin=-22)
        print('   m=%.2f v_max(d=3)=%.5f mu_E=%+.5e | Xi ' % (m, law.vmax(m), mu) + ' '.join('%s %+.5e' % (v, x) for v, x in X.items())
              + ' | refined M,Eg %+.6e' % X2['M,Eg'], flush=True)
    for m in [0.3]:
        for N in [160, 240, 320]:
            Xg = Xi(law, m, N)
            print('   3D grid m=%.1f N=%d: ' % (m, N) + ' '.join('%s A %+.5e / IBP %+.5e' % (v, x[0], x[1]) for v, x in Xg.items()), flush=True)
print('runtime %.1fs' % (time.time()-T0))
