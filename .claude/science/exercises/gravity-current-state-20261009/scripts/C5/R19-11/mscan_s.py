"""R19-11 (a), scalars: rows of one real scalar on the root's Higgs edge G_w(b_s, fr=1), U vertex, as functions of m.
Axis rows + mu_E: R16-13/R18-5 content4.scalw (archived, unmodified). Off-axis rows: R17-4's offaxis.xi_off (archived, E1, U).
Root = vR18-9's retuned root (arch18_13/root_refR18-9.npy)."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18')); sys.path.insert(1, os.path.join(HERE, '..', 'arch17_4'))
from content4 import scalw
import importlib.util
spec = importlib.util.spec_from_file_location('offaxis', os.path.join(HERE, '..', 'arch17_4', 'offaxis.py')); O = importlib.util.module_from_spec(spec); spec.loader.exec_module(O)
spec2 = importlib.util.spec_from_file_location('zz174', os.path.join(HERE, '..', 'arch17_4', 'zz.py')); Z4 = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(Z4)
z = np.load(os.environ.get('ROOT', os.path.join(HERE, '..', 'arch18_13', 'root_refR18-9.npy'))); bs, bf, r, a = z[:4]; fr = 1.0
ms = [float(v) for v in sys.argv[1].split(',')]
offax = len(sys.argv) < 3 or sys.argv[2] != 'nooff'
print('scalar G_w(%.10f, fr=1) U; per real scalar' % bs, flush=True)
for m in ms:
    t0 = time.time()
    S, L = scalw(bs, fr, m, vert='U')
    line = 'm=%-10g T2g %+.12e Eg %+.12e muE %+.12e' % (m, S[0], S[1], S[2])
    if offax:
        wA = fr*(np.pi - bs); law4 = Z4.ZLaw([1.0, 0.0], [bs + wA/2], wA)
        X, _ = O.xi_off(law4, m, 'U')
        line += ' | off: Eg %+.12e T2g %+.12e face1 %+.12e face2 %+.12e d1 %+.6e d2 %+.2e' % (X['Eg'], X['T2g'], X['face1'], X['face2'], X['face1'] - (3*X['Eg'] + X['T2g'])/4, X['face2'] - X['T2g'])
    print(line + ' [%.0fs]' % (time.time() - t0), flush=True)
