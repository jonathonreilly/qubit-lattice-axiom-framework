"""R18-9 (c), scalar part only: R17-4's off-axis evaluator (archived offaxis.py, E1 extension, U vertex) on the root's scalar edge.
Per real scalar: Eg, T2g, face1, face2, body; checks face2 = T2g (R17-4 identity for U) and the O_h relation; K6 term."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch17_4'))
from zz import ZLaw
import offaxis as O
z = np.load(sys.argv[1]); bs, fr, m = z[0], z[4], z[7]
wA = fr*(np.pi - bs); law = ZLaw([1.0, 0.0], [bs + wA/2], wA)
X, mom = O.xi_off(law, m, 'U')
print('scalar G_w(%.6f, fr=%.3f) U, E1, m=%g, per real scalar:' % (bs, fr, m), {k: '%+.6e' % v for k, v in X.items()})
print('face2 - T2g = %+.2e ; O_h relation residual %+.2e ; K6 term -(1/128)<K6/eps^7> = face1 - (3Eg+T2g)/4 = %+.6e' % (X['face2'] - X['T2g'], O.relation(X), X['face1'] - (3*X['Eg'] + X['T2g'])/4))
print('x4 scalars: face1 %+.4e, body %+.4e' % (4*X['face1'], 4*X['body']))
