import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw, Mix
from floor_scan import Zz
from offaxis import xi_off
from fastU import rowsU
T0 = time.time(); NF = 1 << 16; m = 0.1
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03)
# cross-check fastU against the general symbolic code
for L in [A, C2]:
    g, f = L.samples(1 << 14); R = rowsU(g, f, m); X, _ = xi_off(L, m, 'U')
    print('check %s: fastU Eg %+.9e T2g %+.9e face1 %+.9e | general %+.9e %+.9e %+.9e' % (L.name, R['Eg'], R['T2g'], R['face1'], X['Eg'], X['T2g'], X['face1']))
laws = []
for b in [0.3, 0.5, 0.7, 1.0]:
    for k1 in [1.2, 1.6, 2.0, 2.4]:
        for L2 in [0.3, 0.6, 0.9]:
            k2 = k1 + L2
            if k2 > np.pi - 0.1: continue
            laws.append(ZLaw([1.0, 0.0, 1.0, 0.0], [b, k1, k2], 0.03, 'T(b=%.1f,k1=%.1f,k2=%.1f)' % (b, k1, k2), nf=NF))
for b in [0.5, 0.7, 1.0, 1.4]:
    for V in [0.3, 0.45, 0.6, 0.75]:
        for P in [V + 0.08, V + 0.15, V + 0.3]:
            L = Zz(b, V, P, 0.03)
            if L is not None: laws.append(L)
for b in [0.3, 0.6, 1.0, 1.5, 2.0]: laws.append(ZLaw([1.0, 0.0], [b + (np.pi-b)/2], np.pi-b, 'G(%.1f)' % b, nf=NF))
for b in [0.5, 1.0]:
    for wt in [0.05, 0.2]: laws.append(ZLaw([1.0, 0.0], [b + wt/2], wt, 'Gw(%.1f,%.2f)' % (b, wt), nf=NF))
# box -> down to a floor -> flat (a single gapped valley at the end), and box -> flat -> zigzag
for b in [0.6, 1.0]:
    for V in [0.2, 0.4, 0.6]:
        laws.append(ZLaw([1.0, -1.0, 0.0], [b, b + (b - V)], 0.03, 'DF(b=%.1f,V=%.1f)' % (b, V), nf=NF))
res = []
for L in laws:
    g, f = L.samples(1 << 13); R = rowsU(g, f, m, nu=800)
    res.append((L.name, R))
pos = [r for r in res if r[1]['face1'] > 0]
print('laws scanned %d; with U face1 > 0 at m=0.1: %d' % (len(res), len(pos)))
for nm, R in sorted(res, key=lambda r: -r[1]['face1'])[:25]:
    print('%-34s Eg %+.3e T2g %+.3e face1 %+.3e K6row %+.3e mu_E %+.3e' % (nm, R['Eg'], R['T2g'], R['face1'], R['K6row'], R['mu_E']))
print('... most negative face1:')
for nm, R in sorted(res, key=lambda r: r[1]['face1'])[:5]:
    print('%-34s Eg %+.3e T2g %+.3e face1 %+.3e K6row %+.3e mu_E %+.3e' % (nm, R['Eg'], R['T2g'], R['face1'], R['K6row'], R['mu_E']))
print('runtime %.1fs' % (time.time()-T0))
