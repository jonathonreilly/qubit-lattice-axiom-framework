"""R16-13: convergence of the GL evaluator (dfam.evaluate) against a uniform midpoint grid and the shift method, DG laws."""
import numpy as np, time
import dfam
from dirac import dirac_xi
t0 = time.time()
def uniform_eval(law, m, N):
    orig = dfam.gl_nodes
    def uni(breaks, npan, ngl):
        k = (np.arange(N)+0.5)*2*np.pi/N - np.pi
        return k, np.full(N, 1.0/N)
    dfam.gl_nodes = uni
    try: return dfam.evaluate(law, m)
    finally: dfam.gl_nodes = orig
class Wrap:   # adapter for dirac_xi (needs S, W callables)
    def __init__(s, law): s.law = law
    def S(s, k): return s.law.tables(np.asarray(k, float))[0]
    def W(s, k): return s.law.tables(np.asarray(k, float))[3]
for (b, w, r) in [(1.0, 0.25, 0.3), (0.8, 0.5, 0.5)]:
    law = dfam.DG(b, w, r)
    print(law.name, 'W_pi %.4f  s(pi) %.2e' % (law.Wpi, law.Spi), flush=True)
    for (npan, ngl) in [(2, 8), (3, 8), (4, 10)]:
        o = dfam.evaluate(law, 0.3, npan, ngl)
        print('  GL npan=%d ngl=%2d (n1d=%d): T2g %+.7e Eg %+.7e a %+.4e muE %+.7e muT2 %+.4e' % (npan, ngl, 2*npan*ngl*(len(law.breaks())-1), o['T2g'], o['Eg'], o['a'], o['muE'], o['muT2']), flush=True)
    for N in (160, 240):
        o = uniform_eval(law, 0.3, N)
        print('  uniform N=%d: T2g %+.7e Eg %+.7e a %+.4e muE %+.7e muT2 %+.4e' % (N, o['T2g'], o['Eg'], o['a'], o['muE'], o['muT2']), flush=True)
    rr = dirac_xi(Wrap(law), 0.3, 160, pol='T2g', Nc=4, kind='D1'); re = dirac_xi(Wrap(law), 0.3, 160, pol='Eg', Nc=4, kind='D1')
    print('  shift-method N=160: T2g %+.7e Eg %+.7e' % (rr['Xi'], re['Xi']), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
