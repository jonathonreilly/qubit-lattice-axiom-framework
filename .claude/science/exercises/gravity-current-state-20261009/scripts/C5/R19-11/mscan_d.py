"""R19-11 (a), Dirac: rows of one Dirac field on the root's D1(b_f, r), UD vertex, as functions of m.
Axis rows + mu_E + mu_T2: R18-5 smud_lib.dirac (archived, unmodified; dfam GL + xiud pointwise). Off-axis: R18-13 dface.xi_dirac (archived).
Root = vR18-9's retuned root."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18')); sys.path.insert(1, os.path.join(HERE, '..', 'arch18_13'))
from smud_lib import dirac
from content3 import D1q
import dface
z = np.load(os.environ.get('ROOT', os.path.join(HERE, '..', 'arch18_13', 'root_refR18-9.npy'))); bs, bf, r, a = z[:4]
ms = [float(v) for v in sys.argv[1].split(',')]; q = tuple(int(v) for v in sys.argv[2].split(','))
offax = len(sys.argv) < 4 or sys.argv[3] != 'nooff'
print('Dirac D1(%.10f, %.10f) UD; per field; GL%s' % (bf, r, q), flush=True)
for m in ms:
    t0 = time.time()
    F = dirac(bf, r, m=m, q=q)
    line = 'm=%-10g T2g %+.12e Eg %+.12e muE %+.12e muT2 %+.12e' % (m, *F)
    if offax:
        X = dface.xi_dirac(D1q(bf, r), m, rows=('T2g', 'Eg', 'face1', 'face2'), npan=q[0], ngl=q[1])
        line += ' | off: T2g %+.12e Eg %+.12e face1 %+.12e face2 %+.12e d1 %+.8e d2 %+.8e' % (X['T2g'], X['Eg'], X['face1'], X['face2'], X['face1'] - (3*X['Eg'] + X['T2g'])/4, X['face2'] - X['T2g'])
    print(line + ' [%.0fs]' % (time.time() - t0), flush=True)
