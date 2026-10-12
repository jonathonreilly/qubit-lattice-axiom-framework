"""R8-4 script D2: is toy N's two-loop LV a dimension-4 (unsuppressed) effect?  Scale all masses by s at fixed
form-factor scales (Lam1, Lam2) and measure the speed coefficient xi_mix = [m2_mix(p) - m2_mix(0)]/p^2 at p = 0.3 m_X
(non-relativistic-to-mildly-relativistic), together with the one-loop xi_1 (should be 0)."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import r84_toyN_cont as D
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
base = dict(D.mass)
for stat in ('F', 'B'):
    D.STAT[0] = stat
    for sc, G in [(1.0, 121), (1.0, 161), (0.5, 201), (0.25, 321)]:
        D.mass.update({k: v*sc for k, v in base.items()})
        mX = D.mass['X']
        # reuse run() but with custom p list: monkeypatch via closure
        grid = None
        def run_p(plist, G=G, K=2.6):
            import types
            src = D.run.__code__
            return None
        # simple re-implementation of the p loop using D.run internals is long; instead call D.run and pick rows
        rows, yrows = D.run(G)
        # D.run evaluates p in [0, .1, .2, .3, .4, .6]; use p = 0.1 and 0.2
        r0 = rows[0]
        out = []
        for r in rows[1:3]:
            p = r[0]; out.append(f'p={p:.2f}(p/m={p/mX:.2f}): xi_1={(r[1]-r0[1])/p**2:+.2e} xi_mix={(r[4]-r0[4])/p**2:+.4e} (m2_mix(0)={r0[4]:+.4e}, xi_mix/|m2_mix(0)|={(r[4]-r0[4])/p**2/abs(r0[4]):+.3f})')
        pr(f'{stat} mass scale {sc} (m_X={mX:.4f}) G={G}: ' + ' | '.join(out))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(OUT) + '\n')
