"""R11-6 pre-registered model comparison (PREREG_c.txt): AICc on ln T; (S) a - c r^beta, beta in {0.10..2.00 step 0.05};
(W) a - p ln r.  dAICc = AICc(W) - AICc(S): > +2 super-poly preferred, < -2 power preferred, else undecided."""
import numpy as np, sys, re
def aicc(sse, n, k): return n*np.log(sse/n) + 2*k + 2*k*(k+1)/(n-k-1)
def compare(r, T):
    r = np.asarray(r, float); y = np.log(np.asarray(T, float)); n = len(r)
    X = np.c_[np.ones(n), np.log(r)]; cW, *_ = np.linalg.lstsq(X, y, rcond=None); sW = np.sum((y - X@cW)**2)
    best = None
    for b in np.arange(0.10, 2.0001, 0.05):
        Xs = np.c_[np.ones(n), r**b]; cS, *_ = np.linalg.lstsq(Xs, y, rcond=None); sS = np.sum((y - Xs@cS)**2)
        if best is None or sS < best[0]: best = (sS, b, cS)
    sS, b, cS = best
    d = aicc(sW, n, 2) - aicc(sS, n, 3)
    verdict = 'super-poly' if d > 2 else ('power' if d < -2 else 'undecided')
    return d, verdict, -cW[1], -cS[1], b
def parse(fn, key=None):
    r, T = [], []
    for line in open(fn):
        m = re.search(r'r =\s*([\d.]+).*?= ([\d.eE+-]+)\s+\[odd', line)
        if m: r.append(float(m.group(1))); T.append(float(m.group(2)))
    return r, T
if __name__ == '__main__':
    for fn in sys.argv[1:]:
        r, T = parse(fn)
        if len(r) < 5: print(fn, 'too few points'); continue
        d, v, p, c, b = compare(r, T)
        ls = np.diff(np.log(T))/np.diff(np.log(r))
        print('%-40s n=%2d r=%.0f..%.0f  dAICc(W-S)=%+7.2f -> %-10s | power p=%.2f | super c=%.3g beta=%.2f | local slopes %s'
              % (fn.split('/')[-1], len(r), r[0], r[-1], d, v, p, c, b, ' '.join('%.1f' % -x for x in ls)))
