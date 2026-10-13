"""R19-26 (root, direct): R19-9's direct N = 224 face-row step (orig/r199_direct_solve.py), executed from its own source with
ONLY (i) the analytic photon law (R0, as R19-16), (ii) the re-placed off-diagonal vertex (lib1926.vertex_geo_F_factory) in the
photon face evaluator, (iii) the start (b_s, b_f, r_D, a) from R19-16's resolve_sols_analytic.npy and (w_d, w_o) = R19-16's final
direct-step values.  The start totals are recomputed directly with the re-placed vertex.  Axial rows are unchanged exactly
(q || z: F(0)^2 = 1).  argv: r."""
import os, sys, numpy as np
import lib1926 as R
HERE = R.HERE; ORIG = os.path.join(HERE, 'orig')
r = sys.argv[1]
WSTART = {'0.1': (-1.1715533810, -0.1954183962), '0.05': (-1.1715532496, -0.1954183730)}[r]   # R19-16 r1916_direct_r*.out:3
src = open(os.path.join(ORIG, 'r199_direct_solve.py')).read()
subs = [("HERE = os.path.dirname(os.path.abspath(__file__))", f"HERE = {ORIG!r}"),
        ("S = np.load('resolve_sols.npy')", f"S = np.load({os.path.join(HERE, 'resolve_sols_analytic.npy')!r})"),
        ("bs, bf, rD, a, wd, wo = x", f"bs, bf, rD, a, wd, wo = x; wd, wo = {WSTART!r}"),
        ("import dface as DF, vwface as V", "import dface as DF, vwface as V; V.vertex_geo = __import__('lib1926').vertex_geo_F_factory(V.vertex_geo)"),
        ("law = V.photonGw(bg, fw*(np.pi - bg))", "law = __import__('lib1916').AnalyticPhotonLaw()"),
        ("(r199_direct_r{r}.out)", "(recomputed directly: analytic law + re-placed off-diagonal vertex)")]
for a_, b_ in subs:
    assert src.count(a_) == 1, a_
    src = src.replace(a_, b_)
sys.argv = ['r199_direct_solve.py', r, 'recompute']
exec(compile(src, 'r199_direct_solve.py[R19-26]', 'exec'), {'__name__': '__main__', '__file__': os.path.join(ORIG, 'r199_direct_solve.py')})
