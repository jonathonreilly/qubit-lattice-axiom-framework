"""R17-4 (b): terraced zigzags TZ(b, V, A, lv, lp, wt): box to b; down (slope -1) to V; then repeat [flat lv at V; up +1 to V+A;
flat lp at V+A; down -1 to V] until pi - 0.08; flat end. Flats at the valley add f = 0 states at the lowest edge level (kurtosis),
which is what K6 < 0 needs (section 3.5). U vertex, E1, m = 0.1 and 0.01."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw
from fastU import rowsU
T0 = time.time(); NF = 1 << 15; res = []
def TZ(b, V, A, lv, lp, wt):
    vals = [1.0, -1.0]; bks = [b]; k = b + (b - V)
    seq = [(0.0, lv), (1.0, A), (0.0, lp), (-1.0, A)]; i = 0
    while True:
        v, L = seq[i % 4]
        if L <= 0: i += 1; continue
        if k + L > np.pi - 0.08: break
        bks.append(k); vals.append(v); k += L; i += 1
    bks.append(k); vals.append(0.0)
    if min(np.diff(bks)) < 1.05*wt: return None
    return ZLaw(vals, bks, wt, 'TZ(b=%.1f,V=%.2f,A=%.2f,lv=%.2f,lp=%.2f)' % (b, V, A, lv, lp), nf=NF)
for b in [0.6, 1.0]:
    for V in [0.2, 0.3, 0.4, 0.5, 0.6]:
        for A in [0.04, 0.08, 0.15, 0.3]:
            for lv in [0.0, 0.03, 0.06, 0.12, 0.25]:
                for lp in [0.0, 0.06]:
                    L = TZ(b, V, A, lv, lp, 0.02)
                    if L is None: continue
                    g, f = L.samples(1 << 12)
                    for m in [0.1, 0.01]:
                        R = rowsU(g, f, m, nu=500, shear=False); res.append((m, L.name, R))
print('laws x masses evaluated: %d' % len(res))
for m in [0.1, 0.01]:
    rr = [r for r in res if r[0] == m]
    feas = [r for r in rr if r[2]['Eg'] >= 0 and r[2]['T2g'] >= 0]
    print('m=%.2f: %d with Eg,T2g >= 0; max face1 among them: %s' % (m, len(feas), ('%+.3e (%s)' % max((r[2]['face1'], r[1]) for r in feas)) if feas else 'none'))
    print('   max face1 overall %+.3e (%s); max min(Eg,T2g,face1) %+.3e (%s)' % (*max((r[2]['face1'], r[1]) for r in rr), *max((min(r[2]['Eg'], r[2]['T2g'], r[2]['face1']), r[1]) for r in rr)))
    for r in sorted(feas, key=lambda r: -r[2]['face1'])[:5]:
        print('   %s Eg %+.2e T2g %+.2e face1 %+.3e K6row %+.3e' % (r[1], r[2]['Eg'], r[2]['T2g'], r[2]['face1'], r[2]['K6row']))
print('runtime %.0fs' % (time.time()-T0))
