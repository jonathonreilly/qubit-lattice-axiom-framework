"""R19-16 (root): R19-9's 6-knob re-solve model (orig/r199_resolve.py), executed from its own source text with ONLY the photon
row inputs replaced, so that the model, Jacobian, corner term and iteration are byte-identical to R19-9's.
  mode 'analytic' : photon axial coefficients (T2g, Eg quadratic in a; mu_E) and face rows (values at (w_d, w_o) = 0 and exact
                    w-derivatives) from the archived evaluators run with the ANALYTIC law (r1916_photrows.py, N = 224);
  mode 'tabfull'  : archived tabulated law, face inputs at full precision (control; R19-9 used 10/7-digit printed values).
argv: mode, r-list (default 0.05,0.1).  Saves resolve_sols_<mode>.npy."""
import os, sys, numpy as np
import lib1916 as R
HERE = R.HERE; ORIG = os.path.join(HERE, 'orig')
mode = sys.argv[1]; rlist = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else '0.05,0.1'
src = open(os.path.join(ORIG, 'r199_resolve.py')).read()
face = np.load(os.path.join(HERE, f'photface_{"analytic" if mode == "analytic" else "tab"}_N224.npy'))
subs = [("HERE = os.path.dirname(os.path.abspath(__file__))", f"HERE = {ORIG!r}"),
        ("F1_0, F2_0 = 2.182473207e-01, 1.092917123e-01", f"F1_0, F2_0 = {face[0]!r}, {face[1]!r}"),
        ("DF1_WD, DF1_WO, DF2_WO = 1.397040e-01, 2.892797e-01, 5.785714e-01", f"DF1_WD, DF1_WO, DF2_WO = {face[2]!r}, {face[3]!r}, {face[5]!r}"),
        ("np.save('resolve_sols.npy',", f"np.save({os.path.join(HERE, 'resolve_sols_' + mode + ('_tight' if '--tight' in sys.argv else '') + '.npy')!r},")]
if mode == 'analytic':
    subs.append(("PQ = os.path.join(HERE, 'photquad_N224.npy')", f"PQ = {os.path.join(HERE, 'photquad_analytic_N224.npy')!r}"))
if '--tight' in sys.argv:          # one tighter stopping rule (R19-9 stops below 1e-10); everything else identical
    subs.append(("if np.abs(R).max() < 1e-10: break", "if np.abs(R).max() < 1e-12: break"))
for a, b in subs:
    assert src.count(a) == 1, a
    src = src.replace(a, b)
print(f'[r1916_resolve] mode {mode}; face inputs {face.tolist()} (face2 d/dwd = {face[4]:.1e}, = 0 by Lemma O)', flush=True)
sys.argv = ['r199_resolve.py', rlist]
exec(compile(src, 'r199_resolve.py[' + mode + ']', 'exec'), {'__name__': '__main__', '__file__': os.path.join(ORIG, 'r199_resolve.py')})
