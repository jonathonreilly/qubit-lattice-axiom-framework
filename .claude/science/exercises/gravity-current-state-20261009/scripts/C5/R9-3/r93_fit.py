"""R9-3 script 2: the pre-registered model comparison (TESTS.md R9-3 (c)): information criterion on log residuals,
super-polynomial  log y = a - c D^beta  (3 params)  against  power law  log y = a - p log D  (2 params).
AIC = n ln(SSE/n) + 2k ; AICc adds 2k(k+1)/(n-k-1).  Run on every '.out' given; reports (i) the full range,
(ii) the tail range D >= Dmin (given), excluding points at or below a stated numerical floor.
"""
import numpy as np, sys, re
from scipy.optimize import least_squares

def load(fn):
    D, y = [], []
    for line in open(fn):
        mm = re.search(r'D =\s+(\d+).*\|\| = ([0-9.eE+-]+)', line)
        if mm: D.append(float(mm.group(1))); y.append(float(mm.group(2)))
    return np.array(D), np.array(y)

def fits(D, y):
    L = np.log(y); n = len(D)
    A = np.vstack([np.ones(n), -np.log(D)]).T
    cp, res, *_ = np.linalg.lstsq(A, L, rcond=None); sse_p = np.sum((A@cp - L)**2)
    best = None
    for beta in np.linspace(0.1, 2.5, 481):          # profile likelihood over beta; (a, c) by linear least squares, c >= 0
        A2 = np.vstack([np.ones(n), -D**beta]).T
        cc, *_ = np.linalg.lstsq(A2, L, rcond=None)
        if cc[1] < 0: continue
        s = np.sum((A2@cc - L)**2)
        if best is None or s < best[0]: best = (s, np.array([cc[0], np.log(cc[1]), beta]))
    sse_s, th = best
    def aic(sse, k): return n*np.log(sse/n) + 2*k + (2*k*(k+1)/(n-k-1) if n-k-1 > 0 else np.inf)
    return dict(n=n, p=cp[1], sse_p=sse_p, aic_p=aic(sse_p, 2), c=np.exp(th[1]), beta=th[2], sse_s=sse_s, aic_s=aic(sse_s, 3))

floor = float(sys.argv[1]); Dmin = float(sys.argv[2])
for fn in sys.argv[3:]:
    D, y = load(fn)
    keep = y > 3*floor
    print('==', fn.split('/')[-1], ' points:', ' '.join('%d:%.2e' % (a, b) for a, b in zip(D, y)))
    for lab, sel in [('full range (above 3x floor)', keep), ('tail range D >= %d' % Dmin, keep & (D >= Dmin))]:
        if sel.sum() < 4: print('  %s: too few points (%d)' % (lab, sel.sum())); continue
        r = fits(D[sel], y[sel])
        loc = np.diff(np.log(y[sel]))/np.diff(np.log(D[sel]))
        print('  %s: n=%d D=%d..%d | power p=%.2f SSE=%.3f AICc=%.2f | super-poly c=%.3g beta=%.2f SSE=%.3f AICc=%.2f | dAICc(power - super) = %+.2f | local slopes %s'
              % (lab, r['n'], D[sel].min(), D[sel].max(), r['p'], r['sse_p'], r['aic_p'], r['c'], r['beta'], r['sse_s'], r['aic_s'],
                 r['aic_p'] - r['aic_s'], ' '.join('%.1f' % (-x) for x in loc)))
