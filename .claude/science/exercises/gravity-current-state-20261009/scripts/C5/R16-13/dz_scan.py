"""R16-13: does a zigzag stretch in the Dirac edge raise the fermion's Eg/T2g ratio (birefringence) ? m = 0.01, per Dirac."""
import numpy as np, time
import dfam
from dz import DZ
t0 = time.time(); m = 0.01
for (b, l, nz, wt, r) in [(1.0, 0.0001, 2, 0.03, 0.5), (1.0, 0.1, 2, 0.03, 0.5), (1.0, 0.15, 4, 0.03, 0.5), (1.0, 0.2, 2, 0.04, 0.5), (0.8, 0.15, 4, 0.03, 0.5), (1.2, 0.08, 2, 0.03, 0.5)]:
    try:
        L = DZ(b, l, nz, wt, r)
    except AssertionError:
        print('skip', b, l, nz); continue
    for q in ((1, 8), (2, 8)):
        o = dfam.evaluate(L, m, *q)
        print('DZ(b=%.2f,l=%.3f,nz=%d,wt=%.2f,r=%.2f) q=%s s(pi)=%.1e: T2g %+.5e Eg %+.5e  E/T %.4f  a %+.3e  muE %+.5e muT2 %+.3e' % (
            b, l, nz, wt, r, q, L.Spi, o['T2g'], o['Eg'], o['Eg']/o['T2g'], o['a'], o['muE'], o['muT2']), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
