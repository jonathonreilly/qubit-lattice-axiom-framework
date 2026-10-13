"""R19-16 (root, direct): R19-9's direct N = 224 face-row step (orig/r199_direct_solve.py), executed from its own source with
ONLY (i) the photon law replaced by the ANALYTIC law and (ii) the start point taken from resolve_sols_analytic.npy; the start
totals f0 are recomputed directly (as the R19-9 referee did), not hard-coded.  argv: r."""
import os, sys, numpy as np
import lib1916 as R
HERE = R.HERE; ORIG = os.path.join(HERE, 'orig')
r = sys.argv[1]
src = open(os.path.join(ORIG, 'r199_direct_solve.py')).read()
subs = [("HERE = os.path.dirname(os.path.abspath(__file__))", f"HERE = {ORIG!r}"),
        ("S = np.load('resolve_sols.npy')", f"S = np.load({os.path.join(HERE, 'resolve_sols_analytic.npy')!r})"),
        ("law = V.photonGw(bg, fw*(np.pi - bg))", "law = __import__('lib1916').AnalyticPhotonLaw()"),
        ("(r199_direct_r{r}.out)", "(recomputed directly, analytic law)")]
for a, b in subs:
    assert src.count(a) == 1, a
    src = src.replace(a, b)
sys.argv = ['r199_direct_solve.py', r, 'recompute']
exec(compile(src, 'r199_direct_solve.py[analytic]', 'exec'), {'__name__': '__main__', '__file__': os.path.join(ORIG, 'r199_direct_solve.py')})
